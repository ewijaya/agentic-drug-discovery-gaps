"""Analyze Experiment 2 scores and generate statistical outputs + figures."""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import friedmanchisquare, rankdata, wilcoxon

from config import (
    CHARCOAL,
    EXPECTED_CATEGORIES,
    EXPECTED_DOMAINS,
    MODELS,
    OFF_WHITE,
    RANDOM_SEED,
    RESULTS_DIR,
    RESULTS_FIGURES_DIR,
    SCORES_DIR,
    OKABE_ITO_SKY_BLUE,
    OKABE_ITO_VERMILLION,
    ensure_directories,
)

FINAL_SCORES_PATH = SCORES_DIR / "final_scores.csv"
SUMMARY_TABLE_PATH = RESULTS_DIR / "summary_table.csv"
STATS_PATH = RESULTS_DIR / "statistical_tests.json"
GROUPED_BAR_PATH = RESULTS_FIGURES_DIR / "fig_grouped_bar.pdf"
HEATMAP_PATH = RESULTS_FIGURES_DIR / "fig_category_heatmap.pdf"

BONFERRONI_ALPHA = 0.05 / 4
BOOTSTRAP_SAMPLES = 1000


def parse_score(value: Any) -> float | None:
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def read_final_scores(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows: list[dict[str, Any]] = []
        for row in reader:
            score = parse_score(row.get("final_score"))
            if score is None:
                continue
            if row.get("domain") not in EXPECTED_DOMAINS:
                continue
            rows.append(
                {
                    "response_id": row.get("response_id", ""),
                    "question_id": row.get("question_id", ""),
                    "pair_id": row.get("pair_id", ""),
                    "category": row.get("category", ""),
                    "domain": row.get("domain", ""),
                    "model": row.get("model", ""),
                    "final_score": float(score),
                }
            )
        return rows


def bootstrap_ci(values: np.ndarray, rng: np.random.Generator) -> tuple[float, float]:
    if values.size == 0:
        return float("nan"), float("nan")
    if values.size == 1:
        return float(values[0]), float(values[0])
    samples = rng.choice(values, size=(BOOTSTRAP_SAMPLES, values.size), replace=True)
    means = samples.mean(axis=1)
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def rank_biserial_from_paired(sm: np.ndarray, pep: np.ndarray) -> float:
    diff = sm - pep
    nonzero = diff != 0
    diff = diff[nonzero]
    if diff.size == 0:
        return 0.0

    ranks = rankdata(np.abs(diff), method="average")
    w_plus = float(ranks[diff > 0].sum())
    w_minus = float(ranks[diff < 0].sum())
    denom = w_plus + w_minus
    if denom == 0:
        return 0.0
    return (w_plus - w_minus) / denom


def p_to_stars(p_adj: float) -> str:
    if p_adj < 0.001:
        return "***"
    if p_adj < 0.01:
        return "**"
    if p_adj < 0.05:
        return "*"
    return ""


def write_summary_table(rows: list[dict[str, Any]]) -> None:
    fieldnames = ["category", "sm_mean_sd", "pep_mean_sd", "gap", "p_value"]
    with SUMMARY_TABLE_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main() -> int:
    ensure_directories()
    if not FINAL_SCORES_PATH.exists():
        raise FileNotFoundError(f"Missing final scores: {FINAL_SCORES_PATH}")

    rows = read_final_scores(FINAL_SCORES_PATH)
    if not rows:
        raise RuntimeError("No valid final_score rows found.")

    rng = np.random.default_rng(RANDOM_SEED)
    model_names = [m["name"] for m in MODELS]

    by_model_pair_domain: dict[tuple[str, str, str], float] = {}
    for row in rows:
        key = (row["model"], row["pair_id"], row["domain"])
        by_model_pair_domain[key] = row["final_score"]

    # Primary model-wise paired tests.
    model_stats: list[dict[str, Any]] = []
    grouped_bar_payload: list[dict[str, Any]] = []
    pair_diffs_by_model: dict[str, dict[str, float]] = defaultdict(dict)

    for model in model_names:
        sm_values = np.array(
            [r["final_score"] for r in rows if r["model"] == model and r["domain"] == "small_molecule"],
            dtype=float,
        )
        pep_values = np.array(
            [r["final_score"] for r in rows if r["model"] == model and r["domain"] == "peptide"],
            dtype=float,
        )

        sm_ci = bootstrap_ci(sm_values, rng)
        pep_ci = bootstrap_ci(pep_values, rng)

        pair_ids = sorted({r["pair_id"] for r in rows if r["model"] == model})
        sm_paired: list[float] = []
        pep_paired: list[float] = []
        for pid in pair_ids:
            sm = by_model_pair_domain.get((model, pid, "small_molecule"))
            pep = by_model_pair_domain.get((model, pid, "peptide"))
            if sm is None or pep is None:
                continue
            sm_paired.append(sm)
            pep_paired.append(pep)
            pair_diffs_by_model[model][pid] = sm - pep

        sm_arr = np.array(sm_paired, dtype=float)
        pep_arr = np.array(pep_paired, dtype=float)
        if sm_arr.size == 0:
            p_value = float("nan")
            stat = float("nan")
            effect_r = float("nan")
        else:
            try:
                w = wilcoxon(sm_arr, pep_arr, alternative="greater", zero_method="wilcox")
                p_value = float(w.pvalue)
                stat = float(w.statistic)
            except ValueError:
                p_value = 1.0
                stat = 0.0
            effect_r = float(rank_biserial_from_paired(sm_arr, pep_arr))

        p_adj = min(p_value * 4, 1.0) if np.isfinite(p_value) else float("nan")
        model_stats.append(
            {
                "model": model,
                "n_pairs": int(sm_arr.size),
                "wilcoxon_statistic": stat,
                "p_value": p_value,
                "p_value_bonferroni": p_adj,
                "significant_bonferroni": bool(p_value < BONFERRONI_ALPHA)
                if np.isfinite(p_value)
                else False,
                "rank_biserial_correlation": effect_r,
                "mean_small_molecule": float(sm_values.mean()) if sm_values.size else float("nan"),
                "mean_peptide": float(pep_values.mean()) if pep_values.size else float("nan"),
            }
        )
        grouped_bar_payload.append(
            {
                "model": model,
                "sm_mean": float(sm_values.mean()) if sm_values.size else float("nan"),
                "pep_mean": float(pep_values.mean()) if pep_values.size else float("nan"),
                "sm_ci_low": sm_ci[0],
                "sm_ci_high": sm_ci[1],
                "pep_ci_low": pep_ci[0],
                "pep_ci_high": pep_ci[1],
                "p_adj": p_adj,
                "stars": p_to_stars(p_adj) if np.isfinite(p_adj) else "",
            }
        )

    # Secondary analysis: category table aggregated across models.
    summary_table_rows: list[dict[str, Any]] = []
    for category in EXPECTED_CATEGORIES:
        cat_rows = [r for r in rows if r["category"] == category]
        sm_vals = np.array([r["final_score"] for r in cat_rows if r["domain"] == "small_molecule"], dtype=float)
        pep_vals = np.array([r["final_score"] for r in cat_rows if r["domain"] == "peptide"], dtype=float)

        cat_pairs: dict[tuple[str, str], dict[str, float]] = defaultdict(dict)
        for r in cat_rows:
            cat_pairs[(r["model"], r["pair_id"])][r["domain"]] = r["final_score"]

        sm_paired = []
        pep_paired = []
        for d in cat_pairs.values():
            if "small_molecule" in d and "peptide" in d:
                sm_paired.append(d["small_molecule"])
                pep_paired.append(d["peptide"])

        if sm_paired:
            try:
                w = wilcoxon(
                    np.array(sm_paired, dtype=float),
                    np.array(pep_paired, dtype=float),
                    alternative="greater",
                    zero_method="wilcox",
                )
                p_value = float(w.pvalue)
            except ValueError:
                p_value = 1.0
        else:
            p_value = float("nan")

        sm_mean = float(sm_vals.mean()) if sm_vals.size else float("nan")
        pep_mean = float(pep_vals.mean()) if pep_vals.size else float("nan")
        sm_sd = float(sm_vals.std(ddof=1)) if sm_vals.size > 1 else 0.0
        pep_sd = float(pep_vals.std(ddof=1)) if pep_vals.size > 1 else 0.0
        gap = pep_mean - sm_mean if np.isfinite(sm_mean) and np.isfinite(pep_mean) else float("nan")

        summary_table_rows.append(
            {
                "category": category,
                "sm_mean_sd": f"{sm_mean:.3f} ({sm_sd:.3f})" if np.isfinite(sm_mean) else "",
                "pep_mean_sd": f"{pep_mean:.3f} ({pep_sd:.3f})" if np.isfinite(pep_mean) else "",
                "gap": f"{gap:.3f}" if np.isfinite(gap) else "",
                "p_value": f"{p_value:.6f}" if np.isfinite(p_value) else "",
            }
        )

    write_summary_table(summary_table_rows)

    # Secondary analysis: Friedman consistency test across models over pair gaps.
    common_pairs = sorted(set.intersection(*[set(d.keys()) for d in pair_diffs_by_model.values()]))
    if common_pairs:
        model_gap_arrays = [
            np.array([pair_diffs_by_model[m][pid] for pid in common_pairs], dtype=float) for m in model_names
        ]
        try:
            friedman = friedmanchisquare(*model_gap_arrays)
            friedman_stat = float(friedman.statistic)
            friedman_p = float(friedman.pvalue)
        except ValueError:
            friedman_stat = float("nan")
            friedman_p = float("nan")
    else:
        friedman_stat = float("nan")
        friedman_p = float("nan")

    # Aggregate pooled gap and bootstrap CI.
    pooled_diffs = np.array(
        [diff for model_diffs in pair_diffs_by_model.values() for diff in model_diffs.values()], dtype=float
    )
    pooled_mean_gap = float(pooled_diffs.mean()) if pooled_diffs.size else float("nan")
    pooled_ci = bootstrap_ci(pooled_diffs, rng) if pooled_diffs.size else (float("nan"), float("nan"))

    stats_payload = {
        "alpha": 0.05,
        "bonferroni_alpha": BONFERRONI_ALPHA,
        "model_wise_tests": model_stats,
        "friedman_consistency_test": {
            "n_pairs": len(common_pairs),
            "statistic": friedman_stat,
            "p_value": friedman_p,
        },
        "aggregate_gap": {
            "n_paired_observations": int(pooled_diffs.size),
            "mean_small_minus_peptide": pooled_mean_gap,
            "bootstrap_95ci": {"low": pooled_ci[0], "high": pooled_ci[1]},
        },
    }

    with STATS_PATH.open("w", encoding="utf-8") as f:
        json.dump(stats_payload, f, indent=2)

    # Figure 1: grouped bars.
    plt.style.use("default")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    fig.patch.set_facecolor(OFF_WHITE)
    ax.set_facecolor(OFF_WHITE)

    x = np.arange(len(grouped_bar_payload))
    width = 0.35

    sm_means = np.array([d["sm_mean"] for d in grouped_bar_payload], dtype=float)
    pep_means = np.array([d["pep_mean"] for d in grouped_bar_payload], dtype=float)
    sm_err = np.array(
        [[d["sm_mean"] - d["sm_ci_low"] for d in grouped_bar_payload], [d["sm_ci_high"] - d["sm_mean"] for d in grouped_bar_payload]],
        dtype=float,
    )
    pep_err = np.array(
        [[d["pep_mean"] - d["pep_ci_low"] for d in grouped_bar_payload], [d["pep_ci_high"] - d["pep_mean"] for d in grouped_bar_payload]],
        dtype=float,
    )

    ax.bar(
        x - width / 2,
        sm_means,
        width,
        yerr=sm_err,
        label="Small molecule",
        color=OKABE_ITO_SKY_BLUE,
        edgecolor=CHARCOAL,
        linewidth=0.8,
        capsize=4,
    )
    ax.bar(
        x + width / 2,
        pep_means,
        width,
        yerr=pep_err,
        label="Peptide",
        color=OKABE_ITO_VERMILLION,
        edgecolor=CHARCOAL,
        linewidth=0.8,
        capsize=4,
    )

    ax.axhline(2.0, linestyle="--", color=CHARCOAL, linewidth=1, alpha=0.6)

    for i, d in enumerate(grouped_bar_payload):
        stars = d["stars"]
        if not stars:
            continue
        y = max(d["sm_ci_high"], d["pep_ci_high"]) + 0.08
        ax.text(i, y, stars, ha="center", va="bottom", color=CHARCOAL, fontsize=12)

    ax.set_xticks(x)
    ax.set_xticklabels([d["model"] for d in grouped_bar_payload], rotation=0)
    ax.set_ylabel("Mean score (0-3)")
    ax.set_xlabel("Model")
    ax.set_title("LLM Knowledge Probing: Small Molecule vs Peptide")
    ax.set_ylim(0, 3.2)
    ax.legend(frameon=False)
    ax.grid(axis="y", alpha=0.2)
    for spine in ax.spines.values():
        spine.set_color(CHARCOAL)
    ax.tick_params(colors=CHARCOAL)
    ax.yaxis.label.set_color(CHARCOAL)
    ax.xaxis.label.set_color(CHARCOAL)
    ax.title.set_color(CHARCOAL)

    fig.tight_layout()
    fig.savefig(GROUPED_BAR_PATH, dpi=300)
    plt.close(fig)

    # Figure 2: category gap heatmap (sm - pep).
    heatmap = np.full((len(EXPECTED_CATEGORIES), len(model_names)), np.nan)
    for i, category in enumerate(EXPECTED_CATEGORIES):
        for j, model in enumerate(model_names):
            cat_model = [r for r in rows if r["category"] == category and r["model"] == model]
            sm = [r["final_score"] for r in cat_model if r["domain"] == "small_molecule"]
            pep = [r["final_score"] for r in cat_model if r["domain"] == "peptide"]
            if sm and pep:
                heatmap[i, j] = float(np.mean(sm) - np.mean(pep))

    fig2, ax2 = plt.subplots(figsize=(10, 5), dpi=300)
    fig2.patch.set_facecolor(OFF_WHITE)
    ax2.set_facecolor(OFF_WHITE)
    im = ax2.imshow(heatmap, cmap="RdBu", vmin=-1.5, vmax=1.5, aspect="auto")

    ax2.set_xticks(np.arange(len(model_names)))
    ax2.set_xticklabels(model_names)
    ax2.set_yticks(np.arange(len(EXPECTED_CATEGORIES)))
    ax2.set_yticklabels(EXPECTED_CATEGORIES)
    ax2.set_title("Category Gap Heatmap (Small molecule - Peptide)")

    for i in range(len(EXPECTED_CATEGORIES)):
        for j in range(len(model_names)):
            val = heatmap[i, j]
            if np.isfinite(val):
                ax2.text(j, i, f"{val:.2f}", ha="center", va="center", color=CHARCOAL, fontsize=8)

    cbar = fig2.colorbar(im, ax=ax2, fraction=0.046, pad=0.04)
    cbar.set_label("Mean score difference")

    fig2.tight_layout()
    fig2.savefig(HEATMAP_PATH, dpi=300)
    plt.close(fig2)

    print("Analysis complete.")
    print(f"- summary table: {SUMMARY_TABLE_PATH}")
    print(f"- statistical tests: {STATS_PATH}")
    print(f"- grouped bar: {GROUPED_BAR_PATH}")
    print(f"- category heatmap: {HEATMAP_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
