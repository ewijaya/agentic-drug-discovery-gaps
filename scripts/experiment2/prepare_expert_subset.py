"""Prepare blind stratified expert-scoring subset for Experiment 2."""

from __future__ import annotations

import csv
import json
import random
from collections import defaultdict
from pathlib import Path
from typing import Any

from config import (
    EXPECTED_CATEGORIES,
    EXPECTED_DOMAINS,
    EXPERT_SUBSET_FRACTION,
    MODELS,
    RANDOM_SEED,
    RESPONSES_DIR,
    SCORES_DIR,
    ensure_directories,
)

BLIND_SUBSET_PATH = SCORES_DIR / "expert_subset_blind.csv"
METADATA_PATH = SCORES_DIR / "expert_subset_metadata.csv"
SCORING_TEMPLATE_PATH = SCORES_DIR / "expert_scoring_template.csv"


def load_response_rows() -> list[dict[str, Any]]:
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
                rid = row.get("response_id")
                if not rid:
                    continue
                rows_by_id[rid] = row

    rows = list(rows_by_id.values())
    rows = [r for r in rows if r.get("success") is True and str(r.get("response_text", "")).strip()]
    return rows


def stratified_sample(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    target_models = [m["name"] for m in MODELS]

    by_cell: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        key = (str(row.get("model")), str(row.get("category")), str(row.get("domain")))
        by_cell[key].append(row)

    selected: list[dict[str, Any]] = []
    rng = random.Random(RANDOM_SEED)

    for model in target_models:
        for category in EXPECTED_CATEGORIES:
            for domain in EXPECTED_DOMAINS:
                key = (model, category, domain)
                candidates = sorted(by_cell.get(key, []), key=lambda r: str(r.get("response_id", "")))
                if len(candidates) < 2:
                    raise RuntimeError(
                        f"Not enough responses in cell {key}: need 2, found {len(candidates)}"
                    )
                selected.extend(rng.sample(candidates, 2))

    expected_total = int(round(len(rows) * EXPERT_SUBSET_FRACTION))
    if len(selected) != 80:
        raise RuntimeError(f"Expected 80 sampled rows, got {len(selected)}")
    if expected_total != 80:
        print(
            f"WARNING: 20% of available rows is {expected_total}, but PRD-stratified design requires 80."
        )

    randomizer = random.Random(RANDOM_SEED)
    randomizer.shuffle(selected)
    return selected


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})


def main() -> int:
    ensure_directories()
    rows = load_response_rows()
    if not rows:
        raise RuntimeError("No successful responses found. Run run_probing.py first.")

    selected = stratified_sample(rows)

    blind_rows = [
        {
            "response_id": row["response_id"],
            "category": row["category"],
            "question_text": row["question_text"],
            "response_text": row["response_text"],
        }
        for row in selected
    ]
    write_csv(
        BLIND_SUBSET_PATH,
        blind_rows,
        ["response_id", "category", "question_text", "response_text"],
    )

    metadata_rows = [
        {
            "response_id": row["response_id"],
            "question_id": row["question_id"],
            "pair_id": row["pair_id"],
            "category": row["category"],
            "domain": row["domain"],
            "model": row["model"],
        }
        for row in selected
    ]
    write_csv(
        METADATA_PATH,
        metadata_rows,
        ["response_id", "question_id", "pair_id", "category", "domain", "model"],
    )

    scoring_template_rows = [
        {
            "response_id": row["response_id"],
            "expert_score": "",
            "notes": "",
        }
        for row in selected
    ]
    write_csv(
        SCORING_TEMPLATE_PATH,
        scoring_template_rows,
        ["response_id", "expert_score", "notes"],
    )

    print("Expert subset prepared.")
    print(f"- total successful responses available: {len(rows)}")
    print(f"- selected for expert review: {len(selected)}")
    print(f"- blind subset: {BLIND_SUBSET_PATH}")
    print(f"- metadata key: {METADATA_PATH}")
    print(f"- scoring template: {SCORING_TEMPLATE_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
