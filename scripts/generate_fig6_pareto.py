"""Generate Figure 6: The Pareto Frontier Agents Ignore.

This script implements the full PRD in scripts/PRD-fig6-pareto.md:
- 100 random points + 4 explicit callout candidates
- computed non-dominated sorting (no pre-assigned Pareto labels)
- monotone Pareto frontier envelope that stays above all points
- publication-quality figure with inset, legends, and callouts
"""

from __future__ import annotations

import time
from pathlib import Path

import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import PchipInterpolator

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------
SEED = 42
N_RANDOM = 100
N_FRONTIERISH = 35
N_DOMINATED = 55
N_AGENT_FAVORITES = 10

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "latex" / "figures"
OUTPUT_JPEG = OUTPUT_DIR / "fig6-pareto-frontier.jpeg"
OUTPUT_SVG = OUTPUT_DIR / "fig6-pareto-frontier.svg"

# Okabe-Ito palette
ORANGE = "#E69F00"
SKY_BLUE = "#56B4E9"
BLUISH_GREEN = "#009E73"
BLUE = "#0072B2"
VERMILLION = "#D55E00"
RED = "#CC3311"
CHARCOAL = "#333333"
MED_GRAY = "#888888"
LIGHT_GRAY = "#DDDDDD"
OFF_WHITE = "#FAFAFA"

# Scatter sizes (points^2)
SIZE_SMALL = 25
SIZE_MED = 70
SIZE_LARGE = 160
STABILITY_CHOICES = np.array([SIZE_SMALL, SIZE_MED, SIZE_LARGE])

# Candidate specifications (fixed points, not sampled)
CALL_OUTS = {
    "A": {
        "ic50": 2e-9,
        "ti": 150,
        "size": SIZE_LARGE,
        "subtitle": "High Potency, Narrow Margin",
        "lines": [
            "10x more potent (2 nM IC50)",
            "Moderate safety (TI = 150)",
            "Stable, but narrow dosing window",
        ],
        "expect_pareto": True,
    },
    "B": {
        "ic50": 2e-8,
        "ti": 800,
        "size": SIZE_MED,
        "subtitle": "Lower Efficacy, Robust Safety",
        "lines": [
            "Half of A's potency (20 nM IC50)",
            "5x wider safety margin (TI = 800)",
            "Preferred for broad populations",
        ],
        "expect_pareto": True,
    },
    "C": {
        "ic50": 8e-9,
        "ti": 400,
        "size": SIZE_LARGE,
        "subtitle": "The Stability Winner",
        "lines": [
            "Intermediate potency (8 nM IC50)",
            "Good safety (TI = 400)",
            "Superior stability (t1/2 > 12 hr)",
        ],
        "expect_pareto": True,
    },
    "D": {
        "ic50": 5e-8,
        "ti": 100,
        "size": SIZE_SMALL,
        "subtitle": "Dominated",
        "lines": [
            "Worse than C in efficacy AND safety",
            "No compensating advantage",
            "Strictly inferior choice",
        ],
        "expect_pareto": False,
    },
}
CALL_OUT_ORDER = ["A", "B", "C", "D"]


def trend_ti(log_ic50: np.ndarray) -> np.ndarray:
    """Baseline efficacy-safety trade-off trend in log(IC50) space."""
    return 95 + 860 * (log_ic50 + 9) / 4


def non_dominated_mask(ic50: np.ndarray, ti: np.ndarray) -> np.ndarray:
    """Return mask of non-dominated points.

    Dominance definition from PRD:
    point j dominates point i iff ic50_j < ic50_i AND ti_j > ti_i.
    """
    n = ic50.size
    mask = np.ones(n, dtype=bool)
    for i in range(n):
        dominated = (ic50 < ic50[i]) & (ti > ti[i])
        if np.any(dominated):
            mask[i] = False
    return mask


def clear_callout_neighborhoods(
    rng: np.random.Generator,
    log_ic50: np.ndarray,
    ti: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Move random points away from callout neighborhoods for clear annotation."""
    callout_logs = np.array([np.log10(CALL_OUTS[k]["ic50"]) for k in CALL_OUT_ORDER])
    callout_tis = np.array([CALL_OUTS[k]["ti"] for k in CALL_OUT_ORDER])

    for i in range(log_ic50.size):
        attempts = 0
        while attempts < 50:
            near_any_callout = np.any(
                (np.abs(log_ic50[i] - callout_logs) < 0.08)
                & (np.abs(ti[i] - callout_tis) < 65)
            )
            if not near_any_callout:
                break

            # Resample to a dominated location away from dense callout area.
            log_ic50[i] = rng.uniform(-8.1, -5.0)
            ti[i] = np.clip(
                trend_ti(np.array([log_ic50[i]]))[0]
                - rng.uniform(140, 380)
                + rng.normal(0, 20),
                20,
                860,
            )
            attempts += 1

    return log_ic50, ti


def generate_random_points(rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Generate 100 random points with requested distribution biases."""
    if N_FRONTIERISH + N_DOMINATED + N_AGENT_FAVORITES != N_RANDOM:
        raise ValueError("Random point counts must sum to 100.")

    # Near-frontier candidates with explicitly monotone trade-off shape.
    # This yields a realistic Pareto-rich band (30-40 points) by construction.
    log_front = np.sort(rng.uniform(-9.0, -5.25, N_FRONTIERISH))
    ti_front_raw = trend_ti(log_front) + rng.normal(0, 14, N_FRONTIERISH)
    ti_front = np.clip(np.maximum.accumulate(ti_front_raw), 95, 1000)

    # Dominated bulk
    log_dom = rng.uniform(-8.25, -5.0, N_DOMINATED)
    ti_dom = np.clip(
        trend_ti(log_dom) - rng.uniform(170, 440, N_DOMINATED) + rng.normal(0, 30, N_DOMINATED),
        20,
        860,
    )

    # Agent-favorite high-efficacy region (single-objective behavior)
    log_agent = rng.uniform(-9.0, -8.3, N_AGENT_FAVORITES)
    ti_agent = np.clip(140 + rng.normal(0, 22, N_AGENT_FAVORITES), 75, 240)

    log_ic50 = np.concatenate([log_front, log_dom, log_agent])
    ti = np.concatenate([ti_front, ti_dom, ti_agent])

    # Keep callout A/C non-dominated by random points.
    a_dom = (10 ** log_ic50 < CALL_OUTS["A"]["ic50"]) & (ti > CALL_OUTS["A"]["ti"] - 5)
    ti[a_dom] = rng.uniform(90, 145, a_dom.sum())

    c_dom = (10 ** log_ic50 < CALL_OUTS["C"]["ic50"]) & (ti > CALL_OUTS["C"]["ti"] - 5)
    ti[c_dom] = rng.uniform(170, 360, c_dom.sum())

    log_ic50, ti = clear_callout_neighborhoods(rng, log_ic50, ti)

    sizes = rng.choice(STABILITY_CHOICES, size=N_RANDOM)

    # Force high-efficacy points to skew smaller stability to expose hidden trade-off.
    high_eff = log_ic50 < -8.3
    forced = rng.random(high_eff.sum()) < 0.65
    high_eff_indices = np.where(high_eff)[0]
    sizes[high_eff_indices[forced]] = SIZE_SMALL

    # Track the 10-point high-efficacy cluster for inset emphasis.
    agent_mask = np.zeros(N_RANDOM, dtype=bool)
    agent_mask[-N_AGENT_FAVORITES:] = True

    return 10 ** log_ic50, ti, sizes, agent_mask


def build_monotone_frontier(
    ic50: np.ndarray,
    ti: np.ndarray,
    pareto_mask: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Build a monotone, smooth frontier that stays above all points."""
    log_ic50 = np.log10(ic50)

    pf_log = log_ic50[pareto_mask]
    pf_ti = ti[pareto_mask]
    order = np.argsort(pf_log)
    pf_log = pf_log[order]
    pf_ti = pf_ti[order]

    unique_pf_log = np.unique(pf_log)
    unique_pf_ti = np.array([pf_ti[pf_log == x].max() for x in unique_pf_log])

    if unique_pf_log.size < 2:
        raise RuntimeError("Need at least 2 Pareto points to build frontier.")

    pchip = PchipInterpolator(unique_pf_log, unique_pf_ti)
    curve_log = np.linspace(log_ic50.min(), log_ic50.max(), 700)

    # Start from a linear baseline across full range; replace interior by PCHIP.
    smooth_curve = np.interp(curve_log, unique_pf_log, unique_pf_ti)
    interior = (curve_log >= unique_pf_log.min()) & (curve_log <= unique_pf_log.max())
    smooth_curve[interior] = pchip(curve_log[interior])

    # Envelope from all points to guarantee no point sits above the curve.
    all_order = np.argsort(log_ic50)
    env_log = log_ic50[all_order]
    env_ti = np.maximum.accumulate(ti[all_order])
    unique_env_log = np.unique(env_log)
    unique_env_ti = np.array([env_ti[env_log == x].max() for x in unique_env_log])

    env_interp = np.interp(curve_log, unique_env_log, unique_env_ti)
    curve_ti = np.maximum(smooth_curve, env_interp)
    curve_ti = np.maximum.accumulate(curve_ti) + 2.0

    return curve_log, curve_ti, unique_pf_log, unique_pf_ti


def assert_no_orange_dominates_blue(
    ic50: np.ndarray,
    ti: np.ndarray,
    pareto_mask: np.ndarray,
) -> None:
    """Assert no dominated (orange) point dominates any Pareto (blue) point."""
    blue_idx = np.where(pareto_mask)[0]
    orange_idx = np.where(~pareto_mask)[0]
    for i in orange_idx:
        if np.any((ic50[i] < ic50[blue_idx]) & (ti[i] > ti[blue_idx])):
            raise AssertionError("Found dominated point that dominates a Pareto point.")


def validate_dataset(
    ic50_all: np.ndarray,
    ti_all: np.ndarray,
    pareto_all: np.ndarray,
    curve_log: np.ndarray,
    curve_ti: np.ndarray,
    random_count: int,
) -> dict[str, int]:
    """Run PRD validation checks and return summary counts."""
    if ic50_all.size != 104:
        raise AssertionError(f"Expected 104 total points, found {ic50_all.size}.")
    if random_count != 100:
        raise AssertionError(f"Expected 100 random points, found {random_count}.")

    # Random-point composition checks (SC-1 / FR 4.1).
    # This requirement applies to the 100 synthetic random compounds.
    random_pareto = non_dominated_mask(ic50_all[:random_count], ti_all[:random_count])
    n_random_pareto = int(random_pareto.sum())
    n_random_dominated = int((~random_pareto).sum())
    if n_random_pareto < 25:
        raise AssertionError(f"Need >=25 Pareto random points, got {n_random_pareto}.")
    if n_random_dominated < 50:
        raise AssertionError(f"Need >=50 dominated random points, got {n_random_dominated}.")

    # Candidate checks (SC-1)
    candidate_idx = {
        name: random_count + i for i, name in enumerate(CALL_OUT_ORDER)
    }
    for name in ["A", "B", "C"]:
        if not pareto_all[candidate_idx[name]]:
            raise AssertionError(f"Candidate {name} must be Pareto-optimal.")
    if pareto_all[candidate_idx["D"]]:
        raise AssertionError("Candidate D must be dominated.")

    # Explicit dominance C -> D
    idx_c = candidate_idx["C"]
    idx_d = candidate_idx["D"]
    if not ((ic50_all[idx_c] < ic50_all[idx_d]) and (ti_all[idx_c] > ti_all[idx_d])):
        raise AssertionError("Candidate C must dominate Candidate D.")

    # Orange cannot dominate blue
    assert_no_orange_dominates_blue(ic50_all, ti_all, pareto_all)

    # Frontier monotonicity and envelope checks (SC-2)
    if np.any(np.diff(curve_ti) < -1e-9):
        raise AssertionError("Frontier must be monotone non-decreasing in data coordinates.")

    point_logs = np.log10(ic50_all)
    frontier_at_points = np.interp(point_logs, curve_log, curve_ti)
    if np.any(frontier_at_points + 1e-8 < ti_all):
        raise AssertionError("Found plotted point above frontier curve.")

    return {
        "random_pareto": n_random_pareto,
        "random_dominated": n_random_dominated,
        "total_pareto": int(pareto_all.sum()),
        "total_dominated": int((~pareto_all).sum()),
    }


def draw_figure(
    ic50_random: np.ndarray,
    ti_random: np.ndarray,
    sizes_random: np.ndarray,
    agent_mask: np.ndarray,
    ic50_all: np.ndarray,
    ti_all: np.ndarray,
    sizes_all: np.ndarray,
    pareto_all: np.ndarray,
    curve_log: np.ndarray,
    curve_ti: np.ndarray,
) -> None:
    """Render and save final figure."""
    fig, ax = plt.subplots(figsize=(180 / 25.4, 140 / 25.4))
    fig.patch.set_facecolor("white")
    ax.set_facecolor(OFF_WHITE)

    # Plot random points with computed classification.
    random_pareto = pareto_all[:N_RANDOM]
    dom_mask = ~random_pareto
    ax.scatter(
        ic50_random[dom_mask],
        ti_random[dom_mask],
        s=sizes_random[dom_mask],
        c=ORANGE,
        alpha=0.82,
        edgecolors="#CC7A00",
        linewidths=0.7,
        zorder=2,
    )
    ax.scatter(
        ic50_random[random_pareto],
        ti_random[random_pareto],
        s=sizes_random[random_pareto],
        c=SKY_BLUE,
        alpha=0.86,
        edgecolors="#3A9BD9",
        linewidths=0.7,
        zorder=3,
    )

    # Pareto frontier curve.
    curve_ic50 = 10 ** curve_log
    ax.plot(curve_ic50, curve_ti, color=BLUISH_GREEN, linewidth=2.5, zorder=4)

    mid = int(0.56 * len(curve_log))
    ax.annotate(
        "Pareto Frontier",
        xy=(curve_ic50[mid], curve_ti[mid]),
        xytext=(curve_ic50[mid] * 5.8, curve_ti[mid] + 70),
        fontsize=8,
        fontweight="semibold",
        color=BLUISH_GREEN,
        arrowprops=dict(arrowstyle="-", color=BLUISH_GREEN, lw=0.9),
        zorder=5,
    )

    # Explicit candidate points with high-contrast vermillion ring.
    candidate_positions = {
        "A": (1.2e-8, 260),
        "B": (6.0e-7, 920),
        "C": (3.0e-7, 500),
        "D": (4.0e-7, 210),
    }

    for i, name in enumerate(CALL_OUT_ORDER):
        idx = N_RANDOM + i
        x = ic50_all[idx]
        y = ti_all[idx]
        is_pareto = pareto_all[idx]
        color = SKY_BLUE if is_pareto else ORANGE

        ax.scatter(
            [x],
            [y],
            s=sizes_all[idx] + 170,
            facecolors="none",
            edgecolors=VERMILLION,
            linewidths=2.3,
            zorder=8,
        )
        ax.scatter(
            [x],
            [y],
            s=sizes_all[idx],
            c=color,
            edgecolors=VERMILLION,
            linewidths=1.2,
            alpha=0.98,
            zorder=9,
        )

        text_x, text_y = candidate_positions[name]
        text = (
            f"Candidate {name}: {CALL_OUTS[name]['subtitle']}\n"
            + "\n".join(CALL_OUTS[name]["lines"])
        )
        ax.annotate(
            text,
            xy=(x, y),
            xytext=(text_x, text_y),
            fontsize=6.7,
            color=CHARCOAL,
            va="center",
            bbox=dict(
                boxstyle="round,pad=0.36",
                facecolor="white",
                edgecolor=VERMILLION,
                linewidth=0.8,
            ),
            arrowprops=dict(arrowstyle="-", color=VERMILLION, lw=1.1),
            zorder=10,
        )

    # Typical agent behavior arrow and matching rightward text symbol.
    arrow_y = 38
    ax.annotate(
        "",
        xy=(1.6e-9, arrow_y),
        xytext=(4.5e-7, arrow_y),
        arrowprops=dict(
            arrowstyle="-|>",
            color=RED,
            lw=3.4,
            alpha=0.60,
            mutation_scale=20,
        ),
        zorder=5,
    )
    ax.text(
        4.0e-8,
        arrow_y + 28,
        "Typical Agent Behavior: Maximize Efficacy Only \u2192",
        fontsize=7.6,
        fontstyle="italic",
        fontweight="bold",
        color=RED,
        ha="center",
        va="bottom",
        bbox=dict(facecolor="white", edgecolor="none", alpha=0.85, pad=1.2),
        zorder=6,
    )

    # Axes formatting.
    ax.set_xscale("log")
    ax.set_xlim(1e-9, 1e-5)
    ax.invert_xaxis()
    ax.set_ylim(0, 1050)
    ax.set_xlabel(
        "Efficacy (Lower IC$_{50}$ = More Potent)",
        fontsize=10,
        fontweight="semibold",
        color=CHARCOAL,
    )
    ax.set_ylabel(
        "Safety (Therapeutic Index = LD$_{50}$ / IC$_{50}$)",
        fontsize=10,
        fontweight="semibold",
        color=CHARCOAL,
    )
    ax.set_xticks([1e-9, 1e-8, 1e-7, 1e-6, 1e-5])
    ax.set_xticklabels(["1 nM", "10 nM", "100 nM", "1 $\\mu$M", "10 $\\mu$M"])
    ax.tick_params(colors="#555555", labelsize=8)
    ax.grid(True, linestyle=":", color=LIGHT_GRAY, linewidth=0.5)
    for spine in ax.spines.values():
        spine.set_color(CHARCOAL)
        spine.set_linewidth(1.2)

    # Inset: 1D efficacy view with density strip to highlight high-efficacy cluster.
    inset = fig.add_axes([0.60, 0.64, 0.30, 0.20])
    inset.set_facecolor(LIGHT_GRAY)
    for spine in inset.spines.values():
        spine.set_color(CHARCOAL)
        spine.set_linewidth(1.0)

    random_logs = np.log10(ic50_random)
    hist_counts, hist_edges = np.histogram(random_logs, bins=np.linspace(-9, -5, 18))
    hist_counts = hist_counts / max(hist_counts.max(), 1) * 0.52
    centers = 10 ** ((hist_edges[:-1] + hist_edges[1:]) / 2)
    widths = 10 ** hist_edges[1:] - 10 ** hist_edges[:-1]
    inset.bar(centers, hist_counts, width=widths, color=BLUE, alpha=0.20, edgecolor="none", zorder=0)

    jitter = np.random.default_rng(SEED + 1).uniform(-0.28, 0.14, N_RANDOM)
    inset.scatter(ic50_random, jitter, s=8, c=BLUE, alpha=0.70, edgecolors="none", zorder=1)

    # Subtle highlight around high-efficacy region where agent-favorite points cluster.
    inset.axvspan(1e-9, 3e-9, color=BLUE, alpha=0.08, zorder=0)
    cluster_x = np.median(ic50_random[agent_mask])
    inset.annotate(
        "Agent focuses\nhere",
        xy=(cluster_x, 0.25),
        xytext=(7e-9, 0.55),
        fontsize=6.7,
        fontstyle="italic",
        color=BLUE,
        ha="center",
        arrowprops=dict(arrowstyle="->", color=BLUE, lw=0.9),
        zorder=2,
    )

    inset.set_xscale("log")
    inset.set_xlim(1e-9, 1e-5)
    inset.invert_xaxis()
    inset.set_ylim(-0.32, 0.62)
    inset.set_xticks([1e-9, 1e-7, 1e-5])
    inset.set_xticklabels(["1 nM", "100 nM", "10 $\\mu$M"], fontsize=6.5, color="#555555")
    inset.set_yticks([])
    inset.set_xlabel(
        "Efficacy Only (What Agent Optimizes)",
        fontsize=7,
        fontweight="semibold",
        color=CHARCOAL,
        labelpad=1,
    )
    inset.set_title("What the Agent Sees (1D)", fontsize=7.6, fontweight="semibold", color=CHARCOAL, pad=2)

    # Legends.
    pareto_handle = mlines.Line2D(
        [], [], marker="o", color="w", markerfacecolor=SKY_BLUE,
        markeredgecolor="#3A9BD9", markersize=8, label="Pareto-optimal"
    )
    dominated_handle = mlines.Line2D(
        [], [], marker="o", color="w", markerfacecolor=ORANGE,
        markeredgecolor="#CC7A00", markersize=8, label="Dominated"
    )
    frontier_handle = mlines.Line2D([], [], color=BLUISH_GREEN, linewidth=2.5, label="Pareto Frontier")

    leg1 = ax.legend(
        handles=[pareto_handle, dominated_handle, frontier_handle],
        title="Pareto Status",
        title_fontproperties={"weight": "semibold", "size": 8},
        loc="upper left",
        fontsize=7,
        frameon=True,
        fancybox=True,
        edgecolor=MED_GRAY,
        facecolor="white",
    )
    ax.add_artist(leg1)

    # markersize is in points, scatter s is points^2
    stab_small = mlines.Line2D(
        [], [], marker="o", color="w", markerfacecolor=MED_GRAY,
        markeredgecolor=MED_GRAY, markersize=np.sqrt(SIZE_SMALL), label="< 1 hr"
    )
    stab_med = mlines.Line2D(
        [], [], marker="o", color="w", markerfacecolor=MED_GRAY,
        markeredgecolor=MED_GRAY, markersize=np.sqrt(SIZE_MED), label="1-6 hr"
    )
    stab_large = mlines.Line2D(
        [], [], marker="o", color="w", markerfacecolor=MED_GRAY,
        markeredgecolor=MED_GRAY, markersize=np.sqrt(SIZE_LARGE), label="> 6 hr"
    )

    ax.legend(
        handles=[stab_small, stab_med, stab_large],
        title="Stability (Half-Life)",
        title_fontproperties={"weight": "semibold", "size": 8},
        loc="lower left",
        fontsize=7,
        frameon=True,
        fancybox=True,
        edgecolor=MED_GRAY,
        facecolor="white",
    )

    fig.suptitle("The Pareto Frontier Agents Ignore", fontsize=12, fontweight="bold", color=CHARCOAL, y=0.98)

    plt.tight_layout(rect=[0, 0, 1, 0.95])

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_JPEG, format="jpeg", dpi=300, bbox_inches="tight", pil_kwargs={"quality": 95})
    fig.savefig(OUTPUT_SVG, format="svg", bbox_inches="tight")
    plt.close(fig)


def validate_outputs() -> None:
    """Basic output-file validity checks required by PRD."""
    if not OUTPUT_JPEG.exists():
        raise AssertionError(f"Missing JPEG output: {OUTPUT_JPEG}")
    if not OUTPUT_SVG.exists():
        raise AssertionError(f"Missing SVG output: {OUTPUT_SVG}")

    jpeg_sig = OUTPUT_JPEG.read_bytes()[:2]
    if jpeg_sig != b"\xff\xd8":
        raise AssertionError("JPEG signature check failed.")

    svg_head = OUTPUT_SVG.read_text(encoding="utf-8", errors="ignore")[:500].lower()
    if "<svg" not in svg_head:
        raise AssertionError("SVG signature check failed.")


def main() -> None:
    start = time.perf_counter()
    rng = np.random.default_rng(SEED)

    # Retry generation until all hard constraints are simultaneously satisfied.
    summary: dict[str, int] | None = None
    for _ in range(500):
        ic50_random, ti_random, sizes_random, agent_mask = generate_random_points(rng)

        callout_ic50 = np.array([CALL_OUTS[k]["ic50"] for k in CALL_OUT_ORDER])
        callout_ti = np.array([CALL_OUTS[k]["ti"] for k in CALL_OUT_ORDER])
        callout_sizes = np.array([CALL_OUTS[k]["size"] for k in CALL_OUT_ORDER])

        ic50_all = np.concatenate([ic50_random, callout_ic50])
        ti_all = np.concatenate([ti_random, callout_ti])
        sizes_all = np.concatenate([sizes_random, callout_sizes])

        pareto_all = non_dominated_mask(ic50_all, ti_all)
        curve_log, curve_ti, _, _ = build_monotone_frontier(ic50_all, ti_all, pareto_all)

        try:
            summary = validate_dataset(
                ic50_all=ic50_all,
                ti_all=ti_all,
                pareto_all=pareto_all,
                curve_log=curve_log,
                curve_ti=curve_ti,
                random_count=N_RANDOM,
            )
        except AssertionError:
            continue

        draw_figure(
            ic50_random=ic50_random,
            ti_random=ti_random,
            sizes_random=sizes_random,
            agent_mask=agent_mask,
            ic50_all=ic50_all,
            ti_all=ti_all,
            sizes_all=sizes_all,
            pareto_all=pareto_all,
            curve_log=curve_log,
            curve_ti=curve_ti,
        )
        validate_outputs()
        break
    else:
        raise RuntimeError("Unable to generate dataset satisfying PRD constraints after 500 attempts.")

    elapsed = time.perf_counter() - start
    if elapsed >= 10:
        raise AssertionError(f"Runtime exceeded 10 seconds ({elapsed:.2f}s).")

    print("Figure 6 generated successfully.")
    print(f"Saved JPEG: {OUTPUT_JPEG}")
    print(f"Saved SVG:  {OUTPUT_SVG}")
    print(
        "Random points: "
        f"Pareto={summary['random_pareto']}, "
        f"Dominated={summary['random_dominated']}"
    )
    print(
        "All points: "
        f"Pareto={summary['total_pareto']}, "
        f"Dominated={summary['total_dominated']}"
    )
    print(f"Runtime: {elapsed:.2f}s")


if __name__ == "__main__":
    main()
