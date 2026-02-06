# PRD: Figure 6 — The Pareto Frontier Agents Ignore

## 1. Purpose

Generate a publication-quality 2D scatter plot for Section 6 (Blind Spot 5: Multi-Objective Navigation) of the paper "The Blind Spots of Agentic Drug Discovery." The figure demonstrates why single-objective optimization by current AI agents fails in drug discovery, where candidates must balance competing objectives (efficacy, safety, stability).

The script replaces `scripts/generate_fig6_pareto.py` and outputs `latex/figures/fig6-pareto-frontier.jpeg`.

## 2. Context

**Source specification:** `outline/figure-6-brief.md`

**Key message:** Current AI agents optimize a single metric (e.g., efficacy) and collapse multi-dimensional trade-off spaces into 1D rankings. This discards critical information about Pareto frontiers, trade-off structure, and context-dependent optimality. The figure must make this failure mode visually obvious.

**Audience:** AI researchers, medicinal chemists, computational biologists. Must communicate both the mathematical concept (Pareto optimality) and the practical implication (agents miss the decision space).

## 3. Known Bugs in Current Script (v1)

These must all be fixed. Each is a visual inconsistency that undermines the figure's message.

### Bug 1: Arrow direction vs text symbol mismatch
- **Problem:** The red "Typical Agent Behavior" arrow points **rightward** on the inverted x-axis (toward high efficacy), but the text label contains a **leftward** Unicode arrow (`←`).
- **Root cause:** The x-axis is inverted (lower IC50 = right = more potent). The `annotate` arrow correctly goes from left to right in data coordinates, but the text symbol was written assuming a non-inverted axis.
- **Fix:** Change the text arrow symbol to `→`, matching the visual arrow direction. The full label should read: `"Typical Agent Behavior: Maximize Efficacy Only →"`

### Bug 2: Orange (dominated) points above the Pareto frontier curve
- **Problem:** On the left side of the plot (low efficacy, ~1-10 μM), several orange points sit at TI ~300, visually **above** the green Pareto frontier curve. This makes it look like the frontier is wrong.
- **Root cause:** Two issues: (a) dominated points are generated independently of the actual frontier, with TI clipped to 300, which can exceed the frontier in low-efficacy regions; (b) the spline fit is too smooth (high `s` parameter), causing the curve to sag below actual Pareto points.
- **Fix:** After generating all points, run a proper non-dominated sort across ALL 100 points (not just the pre-labeled "pareto" set). Color points blue/orange based on actual dominance status. Fit the frontier curve only through verified non-dominated points. Ensure the curve is an upper envelope: no point of any color should appear above it.

### Bug 3: Arrow label text truncated by Candidate D callout
- **Problem:** The Candidate D callout box overlaps and obscures the right portion of the "Typical Agent Behavior" label text.
- **Root cause:** The arrow label (`y=60`) and Candidate D callout (at TI=100 with downward offset) occupy the same visual region.
- **Fix:** Place the agent behavior arrow and label in a region with no callout conflicts. Options: (a) move the arrow to a lower y position with the label below, (b) move Candidate D's callout to a non-conflicting position, (c) place the arrow label above the arrow shaft instead of below.

### Bug 4: Candidate C callout targets ambiguous region
- **Problem:** The Candidate C callout arrow lands near a cluster where orange and blue points overlap, making it unclear which specific point is Candidate C.
- **Root cause:** Candidate C is placed at (8 nM, 400) which falls in a dense region. Randomly generated points land nearby.
- **Fix:** Ensure the four callout candidates are plotted as distinct, explicitly placed points (not part of the random scatter). Give them a visually distinct marker style: larger vermillion ring, slightly higher z-order, and clear separation from nearby random points. Alternatively, clear a small radius around each callout point so no random point obscures it.

### Bug 5: Inset panel density does not match annotation
- **Problem:** The "Agent focuses here →" annotation in the inset points to the right (high efficacy end), but the 1D point density does not show obvious clustering there. The dominated points (60% of total) are spread across the left/middle, diluting the visual signal.
- **Root cause:** All 100 points are plotted uniformly on the 1D axis. The 10 "agent favorite" points at the high-efficacy end are visually lost among 90 others.
- **Fix:** Either (a) highlight the agent-favorite cluster with a different color or heavier opacity in the inset, or (b) add a subtle density shading/histogram behind the 1D points to show the concentration, or (c) add a bracket/brace annotation around the high-efficacy cluster.

## 4. Functional Requirements

### 4.1 Data Generation

| Requirement | Specification |
|---|---|
| Total points | 100 synthetic candidate compounds |
| Random seed | Fixed (`SEED = 42`) for reproducibility |
| X-axis variable | IC50 (molar), log-uniform distribution |
| Y-axis variable | Therapeutic Index (TI = LD50/IC50), linear scale |
| Point size variable | Stability (half-life in hours), 3 discrete sizes |
| Pareto classification | Computed by non-dominated sorting over ALL 100 points, not pre-assigned |

**Data generation procedure:**

1. Generate 100 points with IC50 log-uniform in `[10^-9, 10^-5]` M, biased so ~30-40 end up near the frontier and ~60-70 are dominated.
2. For each point, compute TI with an inverse relationship to efficacy (high efficacy = moderate TI, low efficacy = high TI) plus noise.
3. Run non-dominated sorting: a point is Pareto-optimal if no other point has BOTH lower IC50 (better efficacy) AND higher TI (better safety).
4. Color assignment: blue for non-dominated, orange for dominated. This must be computed, not pre-assigned.
5. Stability assignment: random 1/3 each of small/medium/large, uncorrelated with efficacy and safety. Exception: force some high-efficacy points to have small stability (to illustrate the hidden trade-off).

**Validation:** After generation, assert that:
- No orange point has both better efficacy AND better safety than any blue point (i.e., no orange point dominates a blue point).
- The Pareto frontier curve lies at or above all plotted points at every x-coordinate.
- At least 25 points are Pareto-optimal and at least 50 are dominated.

### 4.2 Four Callout Candidates

These are fixed, explicitly placed points (not drawn from the random distribution). They illustrate specific decision trade-offs from the manuscript.

| Candidate | IC50 | TI | Stability | Color | Message |
|---|---|---|---|---|---|
| A | 2 nM | 150 | Large (> 6 hr) | Blue (Pareto) | High potency but narrow safety margin |
| B | 20 nM | 800 | Medium (1-6 hr) | Blue (Pareto) | Lower efficacy but robust safety |
| C | 8 nM | 400 | Large (> 6 hr) | Blue (Pareto) | Intermediate, but best stability |
| D | 50 nM | 100 | Small (< 1 hr) | Orange (Dominated) | Strictly inferior to C on all objectives |

**Validation:**
- Candidates A, B, C must be verifiably non-dominated among all 104 points (100 random + 4 callout).
- Candidate D must be verifiably dominated (at minimum, C dominates D: C has better efficacy [8 nM < 50 nM] AND better safety [400 > 100]).

### 4.3 Pareto Frontier Curve

- Smooth convex curve connecting verified non-dominated points.
- Fit method: monotone interpolation or convex hull upper envelope, NOT unconstrained spline (which can sag below points).
- The curve must be monotonically decreasing when moving from left (high efficacy) to right (low efficacy) on the inverted axis. In data terms: as IC50 increases (worse efficacy), TI must increase (better safety) along the frontier.
- The curve must lie at or above every plotted point at every x-value. No point (blue or orange) should visually appear above the curve.
- Color: Bluish Green (#009E73), 2.5 pt linewidth.
- Label: "Pareto Frontier" placed near the curve's midsection, with a small leader arrow. Must not overlap data points.

### 4.4 "Typical Agent Behavior" Arrow

- Horizontal arrow in the lower portion of the plot.
- Direction: points **rightward** on the inverted x-axis (toward lower IC50 = higher efficacy).
- Visual: 3-4 pt red (#CC3311) line, large arrowhead, 60% opacity.
- Label: `"Typical Agent Behavior: Maximize Efficacy Only →"` placed below or above the arrow shaft, fully visible (no truncation or overlap with callout boxes).
- The arrow must be in a clear region of the plot, not conflicting with any callout annotation.

### 4.5 Inset Panel — "What the Agent Sees (1D)"

- Position: upper-right area of the figure (using `fig.add_axes`), not overlapping main plot data.
- Content: All 100 points projected onto a 1D horizontal efficacy axis with vertical jitter.
- All points rendered in uniform blue (#0072B2), erasing the Pareto/dominated distinction. This is the point: agents lose trade-off information.
- The high-efficacy cluster (right end, where the ~10 agent-favorite points sit) must be visually distinguishable. Use one of: (a) density shading, (b) bracket annotation, (c) slight color/opacity differentiation, or (d) a small histogram strip above the axis.
- Label: "Agent focuses here" with arrow pointing toward the high-efficacy cluster.
- Axis labels: "Efficacy Only (What Agent Optimizes)".
- X-axis matches main plot orientation (inverted, high efficacy on right).

### 4.6 Legends

Two legend boxes:

**Legend 1 — Pareto Status:**
- Blue circle: "Pareto-optimal"
- Orange circle: "Dominated"
- Green line: "Pareto Frontier"

**Legend 2 — Stability (Half-Life):**
- Small circle: "< 1 hr"
- Medium circle: "1-6 hr"
- Large circle: "> 6 hr"

Placement: in regions of low data density (e.g., upper-left for Pareto Status where low-efficacy/high-safety region has few points; lower-left for Stability). Must not overlap data points, callout boxes, or inset panel.

### 4.7 Axes and Formatting

| Property | Value |
|---|---|
| X-axis | Log scale, inverted (lower IC50 = right = more potent) |
| X-axis range | 10^-9 to 10^-5 M |
| X-axis tick labels | 1 nM, 10 nM, 100 nM, 1 μM, 10 μM |
| Y-axis | Linear scale |
| Y-axis range | 0 to ~1050 |
| Y-axis label | Safety (Therapeutic Index = LD50 / IC50) |
| Grid | Dotted, light gray (#DDDDDD), 0.5 pt |
| Background | Off-white (#FAFAFA) |
| Spine color | Charcoal (#333333), 1.2 pt |
| Figure title | "The Pareto Frontier Agents Ignore", 12 pt bold |

### 4.8 Color Palette (Okabe-Ito, colorblind-safe)

| Role | Hex | Usage |
|---|---|---|
| Orange | #E69F00 | Dominated points |
| Sky Blue | #56B4E9 | Pareto-optimal points |
| Bluish Green | #009E73 | Pareto frontier curve |
| Blue | #0072B2 | Inset panel points |
| Vermillion | #D55E00 | Callout highlights |
| Red | #CC3311 | Agent behavior arrow |
| Charcoal | #333333 | Text, axes |
| Medium Gray | #888888 | Grid, legend borders |
| Light Gray | #DDDDDD | Inset background |
| Off-White | #FAFAFA | Plot background |

## 5. Non-Functional Requirements

| Requirement | Specification |
|---|---|
| Output format | JPEG (300 DPI, quality 95) primary; SVG secondary |
| Output path | `latex/figures/fig6-pareto-frontier.jpeg` and `.svg` |
| Figure size | ~180 mm x 140 mm at print resolution |
| Dependencies | matplotlib, numpy, scipy (standard scientific Python stack) |
| Runtime | < 10 seconds |
| Reproducibility | Fixed random seed; deterministic output |
| Script location | `scripts/generate_fig6_pareto.py` |

## 6. Success Criteria

The figure passes review when ALL of the following are true:

### SC-1: Data Integrity
- [ ] Exactly 100 random points + 4 explicit callout candidates = 104 total
- [ ] Non-dominated sorting is computed, not pre-assigned. Every blue point is verifiably non-dominated; every orange point is verifiably dominated.
- [ ] Candidate D is dominated by Candidate C (and possibly others)
- [ ] Candidates A, B, C are non-dominated among all 104 points

### SC-2: Pareto Frontier Correctness
- [ ] The green curve is monotonically decreasing in data coordinates (as IC50 increases, TI increases along the frontier)
- [ ] No point of any color is plotted visually above the green frontier curve
- [ ] The curve passes through or near (within noise) the non-dominated point set

### SC-3: Visual Consistency — No Contradictions
- [ ] The red arrow direction and the text arrow symbol both point the same way (rightward, toward high efficacy on the inverted axis)
- [ ] The "Typical Agent Behavior" label text is fully visible and not truncated or obscured by any other element
- [ ] Each callout leader arrow clearly connects its text box to the correct point, with no ambiguity about which point is being annotated
- [ ] The inset panel's "Agent focuses here" annotation matches the visible density pattern (the high-efficacy end should show noticeably more points or a visual highlight)

### SC-4: No Element Overlap
- [ ] Callout boxes do not overlap each other
- [ ] Callout boxes do not overlap legend boxes
- [ ] Callout boxes do not overlap the inset panel
- [ ] The "Pareto Frontier" label does not overlap callout boxes
- [ ] The agent behavior arrow label does not overlap callout boxes
- [ ] Legend boxes are in low-density regions and do not obscure data

### SC-5: Legibility at Print Size
- [ ] All text is readable at 300 DPI on a 180 mm wide print
- [ ] The three point sizes (small, medium, large) are visually distinguishable
- [ ] Blue and orange points are distinguishable (both in color and by position relative to frontier)
- [ ] Grid lines are subtle and do not compete with data

### SC-6: Message Clarity
- [ ] A reader unfamiliar with the paper can look at this figure and understand: (a) there is a trade-off between efficacy and safety, (b) the green curve shows optimal trade-offs, (c) the red arrow shows that agents chase one axis only, (d) point size adds a hidden third dimension agents ignore, (e) the inset shows what agents actually see (1D ranking)
- [ ] The four callout candidates tell a coherent story: A is potent but risky, B is safe but less potent, C balances with stability, D is strictly worse

### SC-7: Output Files
- [ ] `latex/figures/fig6-pareto-frontier.jpeg` exists, is valid JPEG, ≥ 300 DPI
- [ ] `latex/figures/fig6-pareto-frontier.svg` exists, is valid SVG
- [ ] Script runs cleanly with no errors (warnings about tight_layout are acceptable)
- [ ] Script completes in < 10 seconds
