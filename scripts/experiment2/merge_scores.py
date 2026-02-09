"""Merge Claude and expert scores, then compute inter-rater agreement."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from config import SCORES_DIR, ensure_directories

CLAUDE_SCORES_PATH = SCORES_DIR / "claude_scores.csv"
EXPERT_SCORES_PATH = SCORES_DIR / "expert_scores.csv"
FINAL_SCORES_PATH = SCORES_DIR / "final_scores.csv"
AGREEMENT_ANALYSIS_PATH = SCORES_DIR / "agreement_analysis.json"


def parse_int(value: Any) -> int | None:
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
        reader = csv.DictReader(f)
        return [dict(row) for row in reader]


def write_csv_rows(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})


def quadratic_weighted_kappa(y_true: list[int], y_pred: list[int], n_classes: int = 4) -> float:
    if len(y_true) != len(y_pred) or not y_true:
        raise ValueError("Lists must be same non-zero length")

    # Observed matrix
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


def main() -> int:
    ensure_directories()

    if not CLAUDE_SCORES_PATH.exists():
        raise FileNotFoundError(f"Missing {CLAUDE_SCORES_PATH}")
    if not EXPERT_SCORES_PATH.exists():
        raise FileNotFoundError(f"Missing {EXPERT_SCORES_PATH}")

    claude_rows = read_csv_rows(CLAUDE_SCORES_PATH)
    expert_rows = read_csv_rows(EXPERT_SCORES_PATH)

    claude_by_id = {row["response_id"]: row for row in claude_rows if row.get("response_id")}
    expert_by_id = {row["response_id"]: row for row in expert_rows if row.get("response_id")}

    overlap_ids = sorted(set(claude_by_id.keys()) & set(expert_by_id.keys()))

    claude_overlap_scores: list[int] = []
    expert_overlap_scores: list[int] = []
    confusion_matrix = [[0 for _ in range(4)] for _ in range(4)]
    disagreement_cases: list[dict[str, Any]] = []

    for rid in overlap_ids:
        c_score = parse_int(claude_by_id[rid].get("claude_score"))
        e_score = parse_int(expert_by_id[rid].get("expert_score"))
        if c_score is None or e_score is None:
            continue

        claude_overlap_scores.append(c_score)
        expert_overlap_scores.append(e_score)
        confusion_matrix[e_score][c_score] += 1

        if c_score != e_score:
            disagreement_cases.append(
                {
                    "response_id": rid,
                    "question_id": claude_by_id[rid].get("question_id", ""),
                    "pair_id": claude_by_id[rid].get("pair_id", ""),
                    "category": claude_by_id[rid].get("category", ""),
                    "domain": claude_by_id[rid].get("domain", ""),
                    "model": claude_by_id[rid].get("model", ""),
                    "claude_score": c_score,
                    "expert_score": e_score,
                }
            )

    if claude_overlap_scores:
        kappa = quadratic_weighted_kappa(expert_overlap_scores, claude_overlap_scores)
    else:
        kappa = None

    agreement_payload = {
        "overlap_count": len(claude_overlap_scores),
        "quadratic_weighted_kappa": kappa,
        "confusion_matrix_expert_rows_claude_cols": confusion_matrix,
        "disagreement_count": len(disagreement_cases),
        "disagreement_cases": disagreement_cases,
    }

    with AGREEMENT_ANALYSIS_PATH.open("w", encoding="utf-8") as f:
        json.dump(agreement_payload, f, indent=2)

    final_rows: list[dict[str, Any]] = []
    for rid, c_row in claude_by_id.items():
        e_row = expert_by_id.get(rid)
        c_score = parse_int(c_row.get("claude_score"))
        e_score = parse_int(e_row.get("expert_score") if e_row else None)

        if e_score is not None:
            final_score = e_score
            score_source = "expert"
        else:
            final_score = c_score
            score_source = "claude"

        final_rows.append(
            {
                "response_id": rid,
                "question_id": c_row.get("question_id", e_row.get("question_id", "") if e_row else ""),
                "pair_id": c_row.get("pair_id", e_row.get("pair_id", "") if e_row else ""),
                "category": c_row.get("category", e_row.get("category", "") if e_row else ""),
                "domain": c_row.get("domain", e_row.get("domain", "") if e_row else ""),
                "model": c_row.get("model", e_row.get("model", "") if e_row else ""),
                "final_score": "" if final_score is None else final_score,
                "score_source": score_source,
            }
        )

    final_rows = sorted(final_rows, key=lambda r: str(r["response_id"]))
    write_csv_rows(
        FINAL_SCORES_PATH,
        final_rows,
        [
            "response_id",
            "question_id",
            "pair_id",
            "category",
            "domain",
            "model",
            "final_score",
            "score_source",
        ],
    )

    print("Merged scores complete.")
    print(f"- claude rows: {len(claude_rows)}")
    print(f"- expert rows: {len(expert_rows)}")
    print(f"- overlap with numeric scores: {len(claude_overlap_scores)}")
    print(f"- agreement saved: {AGREEMENT_ANALYSIS_PATH}")
    print(f"- final scores saved: {FINAL_SCORES_PATH}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
