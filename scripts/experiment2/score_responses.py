"""Score model responses with Claude CLI using the Experiment 2 rubric."""

from __future__ import annotations

import csv
import json
import re
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from config import (
    CLAUDE_CLI,
    CLAUDE_DELAY_SECONDS,
    CLAUDE_MODEL,
    MODELS,
    QUESTIONS_PATH,
    RESPONSES_DIR,
    SCORES_DIR,
    ensure_directories,
)

CLAUDE_SCORES_PATH = SCORES_DIR / "claude_scores.csv"

PROMPT_TEMPLATE = """You are an expert pharmaceutical scientist evaluating an AI model's answer
about drug discovery. Score the answer on a 0-3 scale:

0 = Wrong or hallucinated: factually incorrect, fabricated data, or nonsensical
1 = Partially correct: some correct elements but missing key nuance or significant errors
2 = Correct: accurate and reasonably complete
3 = Expert-level: correct with domain-expert nuance, specific quantitative details

Question: {question}
Reference answer: {reference_answer}
Key concepts that should be covered: {key_concepts}

Model's answer to evaluate:
{model_response}

Reply with ONLY a single integer (0, 1, 2, or 3). No explanation.
"""


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_questions() -> dict[str, dict[str, Any]]:
    with QUESTIONS_PATH.open("r", encoding="utf-8") as f:
        rows = json.load(f)
    return {q["id"]: q for q in rows}


def load_response_rows() -> list[dict[str, Any]]:
    rows_by_id: dict[str, dict[str, Any]] = {}
    for model_cfg in MODELS:
        path = RESPONSES_DIR / model_cfg["response_file"]
        if not path.exists():
            print(f"WARNING: response file missing: {path}")
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

                # Only score successful responses with non-empty text.
                if row.get("success") is not True:
                    continue
                if not str(row.get("response_text", "")).strip():
                    continue

                # Keep the latest successful row for each response_id.
                rows_by_id[str(response_id)] = row
    return list(rows_by_id.values())


def load_scored_response_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    seen: set[str] = set()
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rid = row.get("response_id")
            if rid:
                seen.add(rid)
    return seen


def ensure_csv_header(path: Path, fieldnames: list[str]) -> None:
    if path.exists() and path.stat().st_size > 0:
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()


def parse_score(text: str) -> int | None:
    stripped = text.strip()
    if stripped in {"0", "1", "2", "3"}:
        return int(stripped)

    matches = re.findall(r"\b([0-3])\b", stripped)
    if len(matches) == 1:
        return int(matches[0])
    if len(matches) > 1:
        return int(matches[0])
    return None


def call_claude(prompt: str) -> tuple[int | None, str, str, int]:
    """Return (score, stdout, stderr, returncode)."""
    result = subprocess.run(
        [CLAUDE_CLI, "-p", "--model", CLAUDE_MODEL],
        input=prompt,
        capture_output=True,
        text=True,
        timeout=60,
    )
    score = parse_score(result.stdout)
    return score, result.stdout, result.stderr, result.returncode


def score_single_response(
    response_row: dict[str, Any],
    question_row: dict[str, Any],
) -> tuple[int | None, bool]:
    prompt = PROMPT_TEMPLATE.format(
        question=question_row["question"],
        reference_answer=question_row["reference_answer"],
        key_concepts=", ".join(question_row["key_concepts"]),
        model_response=response_row.get("response_text", ""),
    )

    score, stdout, stderr, returncode = call_claude(prompt)
    if score is not None and returncode == 0:
        return score, True

    # One retry on parse/command failure.
    time.sleep(CLAUDE_DELAY_SECONDS)
    score2, stdout2, stderr2, returncode2 = call_claude(prompt)
    if score2 is not None and returncode2 == 0:
        return score2, True

    print(
        "WARNING: unable to parse Claude score after retry for "
        f"response_id={response_row.get('response_id')} "
        f"(returncodes={returncode},{returncode2}; stdout={stdout2!r}; stderr={stderr2!r})"
    )
    return None, False


def main() -> int:
    ensure_directories()

    questions = load_questions()
    response_rows = load_response_rows()
    scored_ids = load_scored_response_ids(CLAUDE_SCORES_PATH)

    fieldnames = [
        "response_id",
        "question_id",
        "pair_id",
        "category",
        "domain",
        "model",
        "claude_score",
        "parse_success",
        "timestamp",
    ]
    ensure_csv_header(CLAUDE_SCORES_PATH, fieldnames)

    response_rows = sorted(
        response_rows,
        key=lambda r: (str(r.get("model", "")), str(r.get("question_id", ""))),
    )

    total = 0
    scored = 0
    parse_failures = 0

    with CLAUDE_SCORES_PATH.open("a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        for row in response_rows:
            response_id = row.get("response_id")
            question_id = row.get("question_id")

            if not response_id or not question_id:
                continue

            total += 1
            if response_id in scored_ids:
                continue

            q = questions.get(question_id)
            if q is None:
                print(f"WARNING: missing question metadata for question_id={question_id}")
                continue

            score, ok = score_single_response(row, q)
            if not ok:
                parse_failures += 1

            writer.writerow(
                {
                    "response_id": response_id,
                    "question_id": question_id,
                    "pair_id": row.get("pair_id", q["pair_id"]),
                    "category": row.get("category", q["category"]),
                    "domain": row.get("domain", q["domain"]),
                    "model": row.get("model", ""),
                    "claude_score": "" if score is None else score,
                    "parse_success": ok,
                    "timestamp": utc_now_iso(),
                }
            )
            f.flush()
            scored += 1
            scored_ids.add(response_id)
            time.sleep(CLAUDE_DELAY_SECONDS)

    final_rows = load_scored_response_ids(CLAUDE_SCORES_PATH)
    print("Scoring complete.")
    print(f"- responses discovered: {total}")
    print(f"- newly scored: {scored}")
    print(f"- parse failures (new): {parse_failures}")
    print(f"- total rows in claude_scores.csv: {len(final_rows)}")

    return 0 if parse_failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
