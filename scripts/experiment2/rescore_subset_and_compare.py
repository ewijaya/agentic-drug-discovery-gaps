"""Rescore fixed audit subset with a judge model and compare vs Sonnet baseline."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from config import (
    CLAUDE_CLI,
    CLAUDE_DELAY_SECONDS,
    MODELS,
    QUESTIONS_PATH,
    RESPONSES_DIR,
    SCORES_DIR,
    ensure_directories,
)
from score_responses import PROMPT_TEMPLATE, parse_score

SUBSET_MANIFEST_PATH = SCORES_DIR / "audit_subset_manifest.csv"
OPUS_SUBSET_PATH = SCORES_DIR / "audit_subset_opus_scores.csv"
COMPARISON_ROWS_PATH = SCORES_DIR / "audit_subset_opus_vs_sonnet.csv"
COMPARISON_SUMMARY_PATH = SCORES_DIR / "audit_subset_opus_vs_sonnet.json"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def parse_int_score(value: Any) -> int | None:
    if value is None:
        return None
    text = str(value).strip()
    if text == "":
        return None
    try:
        num = int(float(text))
    except ValueError:
        return None
    if num not in {0, 1, 2, 3}:
        return None
    return num


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return [dict(row) for row in csv.DictReader(f)]


def write_csv_rows(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})


def ensure_csv_header(path: Path, fieldnames: list[str]) -> None:
    if path.exists() and path.stat().st_size > 0:
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()


def load_subset_manifest() -> list[dict[str, Any]]:
    if not SUBSET_MANIFEST_PATH.exists():
        raise FileNotFoundError(f"Missing subset manifest: {SUBSET_MANIFEST_PATH}")
    rows = read_csv_rows(SUBSET_MANIFEST_PATH)
    if len(rows) != 40:
        print(f"WARNING: expected 40 manifest rows, found {len(rows)}")
    parsed: list[dict[str, Any]] = []
    for row in rows:
        sonnet_score = parse_int_score(row.get("sonnet_score"))
        if sonnet_score is None:
            raise RuntimeError(f"Manifest row missing/invalid sonnet_score: {row}")
        parsed.append(
            {
                "response_id": str(row.get("response_id", "")),
                "question_id": str(row.get("question_id", "")),
                "pair_id": str(row.get("pair_id", "")),
                "category": str(row.get("category", "")),
                "domain": str(row.get("domain", "")),
                "model": str(row.get("model", "")),
                "sonnet_score": sonnet_score,
            }
        )
    return parsed


def load_questions() -> dict[str, dict[str, Any]]:
    with QUESTIONS_PATH.open("r", encoding="utf-8") as f:
        rows = json.load(f)
    return {q["id"]: q for q in rows}


def load_successful_responses_by_id() -> dict[str, dict[str, Any]]:
    rows_by_id: dict[str, dict[str, Any]] = {}
    for model_cfg in MODELS:
        path = RESPONSES_DIR / model_cfg["response_file"]
        if not path.exists():
            continue
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    continue
                response_id = row.get("response_id")
                if not response_id:
                    continue
                if row.get("success") is not True:
                    continue
                if not str(row.get("response_text", "")).strip():
                    continue
                rows_by_id[str(response_id)] = row
    return rows_by_id


def load_existing_judge_scores(path: Path, judge_model: str) -> set[str]:
    if not path.exists():
        return set()
    seen: set[str] = set()
    for row in read_csv_rows(path):
        if str(row.get("judge_model", "")) != judge_model:
            continue
        rid = str(row.get("response_id", ""))
        if rid:
            seen.add(rid)
    return seen


def call_judge(
    prompt: str,
    judge_model: str,
    timeout_seconds: float,
) -> tuple[int | None, str, str, int]:
    try:
        result = subprocess.run(
            [CLAUDE_CLI, "-p", "--model", judge_model],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
        )
    except subprocess.TimeoutExpired as exc:
        return None, exc.stdout or "", f"TimeoutExpired: {exc}", 124
    score = parse_score(result.stdout)
    return score, result.stdout, result.stderr, result.returncode


def score_single(
    response_text: str,
    question_row: dict[str, Any],
    judge_model: str,
    timeout_seconds: float,
) -> tuple[int | None, bool]:
    prompt = PROMPT_TEMPLATE.format(
        question=question_row["question"],
        reference_answer=question_row["reference_answer"],
        key_concepts=", ".join(question_row["key_concepts"]),
        model_response=response_text,
    )

    score, _, _, returncode = call_judge(
        prompt,
        judge_model=judge_model,
        timeout_seconds=timeout_seconds,
    )
    if score is not None and returncode == 0:
        return score, True

    time.sleep(CLAUDE_DELAY_SECONDS)
    score2, stdout2, stderr2, returncode2 = call_judge(
        prompt,
        judge_model=judge_model,
        timeout_seconds=timeout_seconds,
    )
    if score2 is not None and returncode2 == 0:
        return score2, True

    print(
        "WARNING: unable to parse score after retry "
        f"(judge={judge_model}; returncodes={returncode},{returncode2}; "
        f"stdout={stdout2!r}; stderr={stderr2!r})"
    )
    return None, False


def quadratic_weighted_kappa(y_true: list[int], y_pred: list[int], n_classes: int = 4) -> float:
    if len(y_true) != len(y_pred) or not y_true:
        raise ValueError("Lists must be same non-zero length")

    observed = [[0.0 for _ in range(n_classes)] for _ in range(n_classes)]
    for a, b in zip(y_true, y_pred, strict=True):
        observed[a][b] += 1.0

    total = float(len(y_true))
    observed = [[v / total for v in row] for row in observed]

    hist_a = [0.0] * n_classes
    hist_b = [0.0] * n_classes
    for v in y_true:
        hist_a[v] += 1.0
    for v in y_pred:
        hist_b[v] += 1.0
    hist_a = [v / total for v in hist_a]
    hist_b = [v / total for v in hist_b]

    expected = [[hist_a[i] * hist_b[j] for j in range(n_classes)] for i in range(n_classes)]
    weights = [
        [((i - j) ** 2) / ((n_classes - 1) ** 2) for j in range(n_classes)]
        for i in range(n_classes)
    ]
    num = sum(weights[i][j] * observed[i][j] for i in range(n_classes) for j in range(n_classes))
    den = sum(weights[i][j] * expected[i][j] for i in range(n_classes) for j in range(n_classes))
    if den == 0:
        return 1.0
    return 1.0 - (num / den)


def compare_and_write_outputs(
    manifest_rows: list[dict[str, Any]],
    judge_model: str,
) -> None:
    if not OPUS_SUBSET_PATH.exists():
        raise FileNotFoundError(f"Missing scored subset file: {OPUS_SUBSET_PATH}")

    opus_rows = [r for r in read_csv_rows(OPUS_SUBSET_PATH) if r.get("judge_model") == judge_model]
    opus_by_id = {
        str(r["response_id"]): r for r in opus_rows if str(r.get("response_id", "")).strip()
    }

    comparison_rows: list[dict[str, Any]] = []
    y_true: list[int] = []
    y_pred: list[int] = []
    shifts: list[int] = []
    shift_counts = {-3: 0, -2: 0, -1: 0, 0: 0, 1: 0, 2: 0, 3: 0}

    for row in sorted(manifest_rows, key=lambda r: r["response_id"]):
        rid = row["response_id"]
        sonnet = row["sonnet_score"]
        opus_row = opus_by_id.get(rid)
        opus = parse_int_score(opus_row.get("judge_score")) if opus_row else None
        parse_success = (
            str(opus_row.get("parse_success", "")).strip().lower() == "true" if opus_row else False
        )

        shift: int | None
        exact = False
        within_one = False
        if opus is not None and parse_success:
            shift = opus - sonnet
            exact = shift == 0
            within_one = abs(shift) <= 1
            y_true.append(sonnet)
            y_pred.append(opus)
            shifts.append(shift)
            if shift in shift_counts:
                shift_counts[shift] += 1
        else:
            shift = None

        comparison_rows.append(
            {
                "response_id": rid,
                "question_id": row["question_id"],
                "pair_id": row["pair_id"],
                "category": row["category"],
                "domain": row["domain"],
                "model": row["model"],
                "sonnet_score": sonnet,
                "opus_score": "" if opus is None else opus,
                "opus_parse_success": parse_success,
                "shift_opus_minus_sonnet": "" if shift is None else shift,
                "exact_match": exact,
                "within_one": within_one,
            }
        )

    write_csv_rows(
        COMPARISON_ROWS_PATH,
        comparison_rows,
        [
            "response_id",
            "question_id",
            "pair_id",
            "category",
            "domain",
            "model",
            "sonnet_score",
            "opus_score",
            "opus_parse_success",
            "shift_opus_minus_sonnet",
            "exact_match",
            "within_one",
        ],
    )

    n_compared = len(shifts)
    exact_rate = (sum(1 for s in shifts if s == 0) / n_compared) if n_compared else None
    within_one_rate = (sum(1 for s in shifts if abs(s) <= 1) / n_compared) if n_compared else None
    mean_signed_shift = (sum(shifts) / n_compared) if n_compared else None
    mean_abs_shift = (sum(abs(s) for s in shifts) / n_compared) if n_compared else None
    kappa = quadratic_weighted_kappa(y_true, y_pred) if n_compared else None

    summary = {
        "created_at": utc_now_iso(),
        "judge_model": judge_model,
        "manifest_rows": len(manifest_rows),
        "compared_rows": n_compared,
        "exact_agreement_rate": exact_rate,
        "within_one_rate": within_one_rate,
        "mean_signed_shift_opus_minus_sonnet": mean_signed_shift,
        "mean_absolute_shift": mean_abs_shift,
        "quadratic_weighted_kappa": kappa,
        "shift_counts": shift_counts,
        "comparison_rows_path": str(COMPARISON_ROWS_PATH),
        "opus_subset_scores_path": str(OPUS_SUBSET_PATH),
    }

    with COMPARISON_SUMMARY_PATH.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print("Comparison complete.")
    print(f"- rows compared: {n_compared}/{len(manifest_rows)}")
    print(f"- exact agreement: {exact_rate}")
    print(f"- within-one agreement: {within_one_rate}")
    print(f"- mean signed shift (opus-sonnet): {mean_signed_shift}")
    print(f"- mean absolute shift: {mean_abs_shift}")
    print(f"- quadratic weighted kappa: {kappa}")
    print(f"- comparison rows: {COMPARISON_ROWS_PATH}")
    print(f"- summary json: {COMPARISON_SUMMARY_PATH}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--judge-model",
        default="opus",
        help="Claude CLI model name for audit scoring (default: opus)",
    )
    parser.add_argument(
        "--delay-seconds",
        type=float,
        default=CLAUDE_DELAY_SECONDS,
        help="Delay between judge calls (default from config)",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=float,
        default=180.0,
        help="Claude CLI timeout per call in seconds (default: 180)",
    )
    args = parser.parse_args()

    ensure_directories()
    manifest_rows = load_subset_manifest()
    questions = load_questions()
    responses_by_id = load_successful_responses_by_id()

    fieldnames = [
        "response_id",
        "question_id",
        "pair_id",
        "category",
        "domain",
        "model",
        "judge_model",
        "judge_score",
        "parse_success",
        "timestamp",
    ]
    ensure_csv_header(OPUS_SUBSET_PATH, fieldnames)
    seen = load_existing_judge_scores(OPUS_SUBSET_PATH, judge_model=args.judge_model)

    scored_new = 0
    parse_failures = 0
    with OPUS_SUBSET_PATH.open("a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        for row in sorted(manifest_rows, key=lambda r: r["response_id"]):
            rid = row["response_id"]
            if rid in seen:
                continue

            response_row = responses_by_id.get(rid)
            if response_row is None:
                print(f"WARNING: missing successful response row for response_id={rid}")
                continue
            qid = str(response_row.get("question_id", row["question_id"]))
            q = questions.get(qid)
            if q is None:
                print(f"WARNING: missing question metadata for question_id={qid}")
                continue

            score, ok = score_single(
                response_text=str(response_row.get("response_text", "")),
                question_row=q,
                judge_model=args.judge_model,
                timeout_seconds=args.timeout_seconds,
            )
            if not ok:
                parse_failures += 1

            writer.writerow(
                {
                    "response_id": rid,
                    "question_id": qid,
                    "pair_id": row["pair_id"],
                    "category": row["category"],
                    "domain": row["domain"],
                    "model": row["model"],
                    "judge_model": args.judge_model,
                    "judge_score": "" if score is None else score,
                    "parse_success": ok,
                    "timestamp": utc_now_iso(),
                }
            )
            f.flush()
            scored_new += 1
            seen.add(rid)
            time.sleep(args.delay_seconds)

    print("Subset rescoring complete.")
    print(f"- judge model: {args.judge_model}")
    print(f"- newly scored: {scored_new}")
    print(f"- parse failures (new): {parse_failures}")
    print(f"- output: {OPUS_SUBSET_PATH}")

    compare_and_write_outputs(manifest_rows, judge_model=args.judge_model)
    return 0 if parse_failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
