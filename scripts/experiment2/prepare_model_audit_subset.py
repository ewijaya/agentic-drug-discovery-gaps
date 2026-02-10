"""Prepare a fixed 40-row stratified subset for Sonnet-vs-Opus audit.

This script:
1) Freezes the current Sonnet score file as a baseline reference.
2) Creates a reproducible 40-row subset manifest (4 models x 2 domains x 5 categories).
3) Writes Sonnet baseline rows for that subset to a separate CSV.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from config import (
    EXPECTED_CATEGORIES,
    EXPECTED_DOMAINS,
    MODELS,
    RANDOM_SEED,
    SCORES_DIR,
    ensure_directories,
)

CLAUDE_SCORES_PATH = SCORES_DIR / "claude_scores.csv"
SONNET_BASELINE_PATH = SCORES_DIR / "claude_scores_sonnet_baseline.csv"
SUBSET_MANIFEST_PATH = SCORES_DIR / "audit_subset_manifest.csv"
SUBSET_SONNET_PATH = SCORES_DIR / "audit_subset_sonnet.csv"
SUBSET_METADATA_PATH = SCORES_DIR / "audit_subset_metadata.json"


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


def freeze_sonnet_baseline(force: bool) -> None:
    if not CLAUDE_SCORES_PATH.exists():
        raise FileNotFoundError(f"Missing Sonnet scores file: {CLAUDE_SCORES_PATH}")
    if SONNET_BASELINE_PATH.exists() and not force:
        print(f"Baseline already exists, keeping existing file: {SONNET_BASELINE_PATH}")
        return
    shutil.copy2(CLAUDE_SCORES_PATH, SONNET_BASELINE_PATH)
    print(f"Baseline frozen: {SONNET_BASELINE_PATH}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=RANDOM_SEED)
    parser.add_argument(
        "--force-baseline",
        action="store_true",
        help="Overwrite existing claude_scores_sonnet_baseline.csv",
    )
    args = parser.parse_args()

    ensure_directories()
    freeze_sonnet_baseline(force=args.force_baseline)

    rows = read_csv_rows(SONNET_BASELINE_PATH)
    if not rows:
        raise RuntimeError(f"No rows found in {SONNET_BASELINE_PATH}")

    valid_rows: list[dict[str, str]] = []
    for row in rows:
        score = parse_int_score(row.get("claude_score"))
        parse_success = str(row.get("parse_success", "")).strip().lower() == "true"
        if score is None or not parse_success:
            continue
        valid_rows.append(row)

    if len(valid_rows) < 400:
        print(f"WARNING: only {len(valid_rows)} valid Sonnet rows found (expected 400).")

    by_cell: dict[tuple[str, str, str], list[dict[str, str]]] = {}
    for row in valid_rows:
        key = (str(row.get("model", "")), str(row.get("category", "")), str(row.get("domain", "")))
        by_cell.setdefault(key, []).append(row)

    selected: list[dict[str, str]] = []
    rng = random.Random(args.seed)
    for model in [m["name"] for m in MODELS]:
        for category in EXPECTED_CATEGORIES:
            for domain in EXPECTED_DOMAINS:
                key = (model, category, domain)
                candidates = sorted(
                    by_cell.get(key, []),
                    key=lambda r: str(r.get("response_id", "")),
                )
                if not candidates:
                    raise RuntimeError(f"No baseline rows found for cell={key}")
                selected.append(rng.choice(candidates))

    selected_ids = [str(r["response_id"]) for r in selected if r.get("response_id")]
    if len(selected_ids) != 40:
        raise RuntimeError(f"Expected 40 selected rows, got {len(selected_ids)}")
    if len(set(selected_ids)) != 40:
        raise RuntimeError("Selected subset contains duplicate response_id values")

    selected = sorted(selected, key=lambda r: str(r.get("response_id", "")))

    manifest_rows: list[dict[str, Any]] = []
    for row in selected:
        manifest_rows.append(
            {
                "response_id": row.get("response_id", ""),
                "question_id": row.get("question_id", ""),
                "pair_id": row.get("pair_id", ""),
                "category": row.get("category", ""),
                "domain": row.get("domain", ""),
                "model": row.get("model", ""),
                "sonnet_score": parse_int_score(row.get("claude_score")),
            }
        )

    write_csv_rows(
        SUBSET_MANIFEST_PATH,
        manifest_rows,
        ["response_id", "question_id", "pair_id", "category", "domain", "model", "sonnet_score"],
    )

    write_csv_rows(
        SUBSET_SONNET_PATH,
        selected,
        [
            "response_id",
            "question_id",
            "pair_id",
            "category",
            "domain",
            "model",
            "claude_score",
            "parse_success",
            "timestamp",
        ],
    )

    metadata = {
        "created_at": utc_now_iso(),
        "seed": args.seed,
        "source_baseline_path": str(SONNET_BASELINE_PATH),
        "manifest_path": str(SUBSET_MANIFEST_PATH),
        "subset_sonnet_path": str(SUBSET_SONNET_PATH),
        "n_selected": len(manifest_rows),
        "design": "stratified_1_per_model_domain_category_cell",
        "models": [m["name"] for m in MODELS],
        "domains": EXPECTED_DOMAINS,
        "categories": EXPECTED_CATEGORIES,
    }
    with SUBSET_METADATA_PATH.open("w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print("Prepared audit subset.")
    print(f"- baseline: {SONNET_BASELINE_PATH}")
    print(f"- subset manifest: {SUBSET_MANIFEST_PATH}")
    print(f"- subset sonnet rows: {SUBSET_SONNET_PATH}")
    print(f"- metadata: {SUBSET_METADATA_PATH}")
    print(f"- selected rows: {len(manifest_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
