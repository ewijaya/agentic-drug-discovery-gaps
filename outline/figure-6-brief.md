# Figure 6: The Pareto Frontier Agents Ignore

**Illustrator Brief — Comprehensive & Self-Sufficient**

---

## Important Note: 2D vs 3D Design Decision

**The manuscript figure caption currently says** "Three-dimensional scatter plot" — however, **this brief specifies a 2D design** with the third dimension (stability) encoded via **point size**. This is intentional:
- 3D plots are difficult to read, don't print well, and require specific viewing angles
- Encoding the third dimension as point size is standard practice for publication-quality multi-objective visualizations
- **The manuscript caption will be updated** to match this design

If you're an illustrator reading this: **follow this brief (2D design), not the current manuscript caption.**

---

## Paper Context

This figure appears in **Section 6 (Blind Spot 5: Multi-Objective Navigation)** of a position paper titled *"The Blind Spots of Agentic Drug Discovery."*

**Core argument of this section:** Drug discovery is multi-objective optimization. Candidates must simultaneously satisfy bioactivity, selectivity, safety, stability, manufacturability, and cost. These objectives **conflict**: potency improvements reduce selectivity, stability enhancements increase immunogenicity, high-purity synthesis is expensive. Navigating this requires understanding **Pareto frontiers** — candidates where improving one objective requires degrading another — and making decisions based on risk tolerance, development stage, and context.

**Current agent limitation:** Current agents optimize single objectives. ChemCrow optimizes binding affinity or synthetic accessibility. Coscientist targets synthesis yield. When handling multiple objectives, they collapse them to weighted sums: "Maximize 0.6×bioactivity + 0.4×drug-likeness." This **discards critical information**: which candidates are Pareto-optimal, how sensitive rankings are to weight changes, what trade-offs exist. Agents present single "optimal" solutions, obscuring the decision space.

**The "single-metric trap" (from manuscript):** Single-metric optimization mirrors ML training objectives (minimize loss, maximize accuracy). This works for unidimensional goals, but drug discovery is multidimensional and context-dependent. Optimality depends on indication, development stage, competitive landscape, and risk tolerance. No scalar objective captures this.

**Real practitioner example (from manuscript):** In in vivo peptide development, safety-efficacy trade-offs dominated candidate selection:
- **Peptide A:** Tenfold higher proliferation bioactivity but triggered hepatotoxicity at effective doses
- **Peptide B:** Half the bioactivity but higher tolerated dosing, yielding comparable efficacy with better safety  
- **Peptide C:** Intermediate bioactivity and safety but superior stability enabling less frequent dosing

**"Optimal" depends on patient population, dosing regimen, and regulatory risk tolerance.** Agents cannot represent these trade-offs. They predict "A > B" but cannot articulate: "A is twice as potent but has a threefold narrower safety margin; choose A if dosing can be tightly controlled, choose B for robustness."

**Audience:** AI researchers building drug discovery agents, medicinal chemists, computational biologists, biotech decision-makers. The figure must communicate both the mathematical concept (Pareto optimality) and the practical implications (why single-objective optimization fails).

**Placement:** Mid-to-late in the paper. This is a key technical figure demonstrating a concrete failure mode of current agent architectures.

---

## Figure Specifications

### Dimensions & Format

- **Size:** 180 mm × 135 mm (full-width, portrait orientation)
- **Resolution:** 300 DPI minimum; vector (SVG/PDF) preferred
- **Bleed:** None
- **Delivery formats:** SVG (primary), high-res PNG (review), layered source file (Figma/Illustrator/Python script)
- **File name:** `fig6_pareto_frontier`

---

## Typography

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Figure title | Open Sans or Helvetica Neue | 12 pt | Bold | #333333 |
| Axis titles | Open Sans or Helvetica Neue | 10 pt | SemiBold | #333333 |
| Axis tick labels | Open Sans or Helvetica Neue | 8 pt | Regular | #555555 |
| Candidate callout labels | Open Sans or Helvetica Neue | 7.5 pt | Regular | #333333 |
| Callout text | Open Sans or Helvetica Neue | 7 pt | Regular | #555555 |
| Legend title | Open Sans or Helvetica Neue | 9 pt | SemiBold | #333333 |
| Legend items | Open Sans or Helvetica Neue | 8 pt | Regular | #555555 |
| Inset panel labels | Open Sans or Helvetica Neue | 7.5 pt | Regular | #333333 |
| Arrow annotations | Open Sans or Helvetica Neue | 8 pt | Bold Italic | #CC3311 (red, for emphasis) |

**All text must remain editable** (not rasterized).

---

## Color Palette (Okabe-Ito — Full Colorblind-Safe Palette)

| Role | Name | Hex | Usage in This Figure |
|------|------|-----|---------------------|
| Primary 1 | Orange | #E69F00 | Non-Pareto optimal points (dominated) |
| Primary 2 | Sky Blue | #56B4E9 | Pareto-optimal points |
| Primary 3 | Bluish Green | #009E73 | Pareto frontier curve |
| Primary 4 | Yellow | #F0E442 | Point size legend (stability high) |
| Primary 5 | Blue | #0072B2 | Inset panel color (1D view) |
| Primary 6 | Vermillion | #D55E00 | Highlighted candidate callouts |
| Primary 7 | Reddish Purple | #CC79A7 | Alternative candidate group (if needed) |
| Alert | Red | #CC3311 | "Typical agent behavior" arrow |
| Neutral 1 | Charcoal | #333333 | Text, axes, borders |
| Neutral 2 | Medium Gray | #888888 | Grid lines |
| Neutral 3 | Light Gray | #DDDDDD | Inset panel background |
| Background | Off-White | #FAFAFA | Main plot background |

**Rule:** Do not rely on color alone to convey information. Pareto-optimal vs non-optimal points must also be distinguishable by position (above/on vs below the curve). Point size encodes stability.

---

## Layout

The figure consists of:
1. **Main scatter plot** (occupies 75% of figure area)
2. **Inset panel** (top-right corner, 20% of figure width)
3. **Legend** (bottom-right corner, below inset)

```
┌─────────────────────────────────────────────────┐
│  Figure Title                                   │
│                                                 │
│                        ┌──────────────┐         │
│                        │ INSET PANEL  │         │
│                        │ (1D View)    │         │
│                        └──────────────┘         │
│                                                 │
│                                                 │
│      MAIN SCATTER PLOT                          │
│      (2D: Efficacy vs Safety)                   │
│                                                 │
│                                                 │
│                                                 │
│                        ┌──────────────┐         │
│                        │   LEGEND     │         │
│                        └──────────────┘         │
└─────────────────────────────────────────────────┘
```

---

## Main Scatter Plot — 2D with Point Size Encoding

### Overall Design
A clean, publication-quality scatter plot showing **candidate compounds** as circular points. This is a **2D plot** (NOT 3D) with:
- **X-axis:** Efficacy
- **Y-axis:** Safety
- **Point size:** Stability (third dimension encoded via circle diameter)

### Axes

#### X-Axis: Efficacy (IC50)
- **Label:** "Efficacy (Lower IC50 = More Potent)" 
  - Position: Centered below axis
  - Font: 10 pt SemiBold, #333333
- **Scale:** Log scale (logarithmic), ranging from 10^-9 to 10^-5 M (molar)
  - Tick marks: 10^-9, 10^-8, 10^-7, 10^-6, 10^-5
  - Tick labels: Use scientific notation (1 nM, 10 nM, 100 nM, 1 μM, 10 μM) — 8 pt Regular
  - **Direction:** Lower IC50 (more efficacious) is to the LEFT — axis increases right-to-left for efficacy
- **Rationale:** IC50 (half-maximal inhibitory concentration) — lower values mean higher potency. Realistic range for peptide therapeutics.
- **Grid lines:** Vertical dotted lines at each major tick, #DDDDDD, 0.5 pt

#### Y-Axis: Safety (Therapeutic Index)
- **Label:** "Safety (Therapeutic Index = LD50/IC50)"
  - Position: Centered, rotated 90° left of axis
  - Font: 10 pt SemiBold, #333333
- **Scale:** Linear, ranging from 10 to 1000
  - Tick marks: 10, 100, 500, 1000
  - Tick labels: 8 pt Regular, #555555
  - **Direction:** Higher is safer (larger safety margin)
- **Rationale:** Therapeutic Index (TI) = LD50 (lethal dose) / IC50 (effective dose). TI > 100 is generally acceptable; TI < 50 is concerning. Realistic range for drug candidates.
- **Grid lines:** Horizontal dotted lines at each major tick, #DDDDDD, 0.5 pt

### Plot Background
- Fill: Off-white (#FAFAFA)
- Border: 1.5 pt solid line, Charcoal (#333333)

---

## Data Points — Synthetic Candidate Compounds

Generate **100 synthetic data points** with realistic distributions:

### Point Distribution (Three Zones)

#### Zone 1: Non-Pareto Dominated Points (60 points)
- **Location:** Below and to the right of the Pareto frontier
- **Color:** Orange (#E69F00)
- **Interpretation:** These candidates are strictly worse than Pareto-optimal ones — there exists at least one other candidate that is better in both efficacy AND safety
- **Distribution:** 
  - Efficacy (IC50): 10^-8 to 10^-5 M (spread across range)
  - Safety (TI): 10 to 300 (lower safety margins)
  - Stability: Random point sizes (see below)

#### Zone 2: Pareto-Optimal Points (30 points)
- **Location:** On or very near the Pareto frontier curve
- **Color:** Sky Blue (#56B4E9)
- **Interpretation:** These candidates represent the best achievable trade-offs — improving efficacy requires sacrificing safety, and vice versa
- **Distribution:**
  - Efficacy (IC50): 10^-9 to 10^-6 M (better efficacy than dominated points)
  - Safety (TI): 100 to 1000 (better safety)
  - Positioned to form the frontier: highest safety at low efficacy, highest efficacy at moderate safety

#### Zone 3: "Agent's Favorite" (10 points)
- **Location:** Top-left corner (highest efficacy, moderate safety)
- **Color:** Mix of Orange and Sky Blue depending on Pareto status
- **Interpretation:** Where single-objective agents focus (maximize efficacy only)
- **Distribution:**
  - Efficacy (IC50): 10^-9 to 5×10^-9 M (highest potency)
  - Safety (TI): 50 to 200 (acceptable but not great)

### Point Size Encoding (Stability — Third Dimension)

Each point's diameter encodes a **stability metric** (e.g., peptide half-life in hours):
- **Small points:** 3 mm diameter = Low stability (half-life < 1 hour)
- **Medium points:** 5 mm diameter = Moderate stability (half-life 1-6 hours)
- **Large points:** 8 mm diameter = High stability (half-life > 6 hours)

**Distribution of stability:**
- Random assignment across all points
- Ensure mix of all three sizes in both Pareto and non-Pareto zones
- **Critical visual point:** Some highly efficacious points (top-left) should have SMALL point sizes (low stability) to illustrate the trade-off agents miss

### Point Style
- **Shape:** Perfect circles
- **Fill:** Solid color (Orange or Sky Blue)
- **Stroke:** 0.75 pt, darker shade of fill color (e.g., Sky Blue points get #3A9BD9 stroke)
- **Opacity:** 85% (allow slight overlap visibility)

---

## Pareto Frontier Curve

### Visual Design
A smooth curve connecting the Pareto-optimal points, representing the boundary of achievable trade-offs.

**From manuscript:** "A candidate is Pareto-optimal if no other improves one objective without degrading another. The Pareto frontier is a curve (two objectives) or surface (three+)." Methods like **NSGA-II** and **multi-objective Bayesian optimization** construct this frontier — but current agents don't support these approaches.

- **Path:** Smooth Bézier curve through the Sky Blue (#56B4E9) points
- **Color:** Bluish Green (#009E73) 
- **Style:** 2.5 pt solid line
- **Start point:** Left side (highest efficacy, moderate safety)
- **End point:** Top-right (moderate efficacy, highest safety)
- **Shape:** Convex curve (bowed outward/upward) — this is the mathematical property of Pareto frontiers. The curve should be "smooth and continuous," not jagged.

### Frontier Annotation
Small text label near the curve (middle section):
- Text: "Pareto Frontier" 
- Font: 8 pt SemiBold, #009E73 (matching curve color)
- Position: Above the curve, centered horizontally
- Optional: Small arrow pointing to the curve

**Contrast with weighted sums (manuscript critique):** Agents that use "0.6×bioactivity + 0.4×drug-likeness" would collapse this 2D frontier into a single diagonal line. The Pareto curve reveals the true non-linear trade-off structure.

**Manuscript insight on frontier shape:** "Steep regions require large sacrifices for modest gains; flat regions allow improvements with minimal cost." The curve should show this curvature variation:
- **Steep section (left side):** Near high efficacy, improving safety much requires large efficacy sacrifice → steep downward slope as you move right
- **Flat section (right side):** In the moderate efficacy zone, safety can be improved with less efficacy cost → gentler slope
- This non-uniformity is why human judgment is essential — different contexts favor different regions

---

## Candidate Callouts — 4 Annotated Examples

Four specific candidates are highlighted with **leader lines** and **text callouts** to illustrate different trade-off scenarios. Each represents a real decision dilemma.

### Callout Style
- **Leader line:** 1 pt solid line, Vermillion (#D55E00)
- **Endpoint:** Small circle (2 mm diameter) around the target point, Vermillion stroke
- **Text box:** 
  - Background: White (#FFFFFF) with 0.75 pt border, #D55E00
  - Padding: 2 mm internal padding
  - Rounded corners: 2 px radius

### Callout Positions & Text

**Note:** These callouts echo the real practitioner examples from the manuscript (peptides A, B, C with different bioactivity-safety-stability profiles).

#### Callout 1: "High Potency, Narrow Margin"
- **Target point location:** Left side of Pareto frontier (highest efficacy, moderate safety)
  - IC50: ~2 nM (very potent)
  - TI: ~150 (acceptable but not wide margin)
  - Stability: LARGE point (high stability)
- **Callout position:** Upper-left area, leader line pointing to the point
- **Text:**
  ```
  Candidate A
  High Potency, Narrow Margin
  
  10× more potent (2 nM IC50)
  Moderate safety (TI = 150)
  Stable — but narrow dosing window
  Requires tight control
  ```

#### Callout 2: "Lower Efficacy, Robust Safety"
- **Target point location:** Right side of Pareto frontier (moderate efficacy, highest safety)
  - IC50: ~20 nM (half the potency of A)
  - TI: ~800 (excellent safety margin)
  - Stability: MEDIUM point (moderate stability)
- **Callout position:** Upper-right area
- **Text:**
  ```
  Candidate B
  Lower Efficacy, Robust Safety
  
  Half A's potency (20 nM IC50)
  but 5× wider safety margin (TI = 800)
  Comparable efficacy via higher dosing
  Preferred for broad patient populations
  ```

#### Callout 3: "The Stability Winner"
- **Target point location:** Middle-upper of Pareto frontier
  - IC50: ~8 nM
  - TI: ~400
  - Stability: LARGE point (highest stability — this is the key differentiator)
- **Callout position:** Right side, upper-middle height
- **Text:**
  ```
  Candidate C
  The Stability Winner
  
  Intermediate bioactivity (8 nM IC50)
  Good safety (TI = 400)
  Superior stability (t½ > 12 hr)
  Enables less frequent dosing
  ```

#### Callout 4: "Dominated — No Justification"
- **Target point location:** Lower-middle, clearly below Pareto frontier (dominated)
  - IC50: ~50 nM
  - TI: ~100
  - Stability: SMALL point (low stability)
- **Callout position:** Lower-left area
- **Text:**
  ```
  Candidate D
  Dominated — No Justification
  
  Worse than C in efficacy AND safety
  No compensating advantage
  Strictly inferior choice
  ```

---

## "Typical Agent Behavior" Arrow

A large, prominent arrow showing the failure mode of single-objective optimization.

### Visual Design
- **Start point:** Center-right of plot (moderate efficacy region, mid-height)
- **End point:** Center-left of plot (highest efficacy region, SAME height — the arrow is roughly HORIZONTAL)
- **Direction:** The arrow points LEFT (toward lower IC50 = higher potency), NOT upward. This is critical: the agent maximizes efficacy while IGNORING the Y-axis (safety) entirely. A diagonal arrow toward top-left would point toward the ideal region, which is wrong — the point is that agents move along one axis only.
- **Arrow style:**
  - 4 pt wide line, Red (#CC3311)
  - Large arrowhead (8 mm length)
  - Straight horizontal or very slightly curved
- **Transparency:** 60% opacity (so it doesn't obscure points)

### Arrow Label
- **Text:** "← Typical Agent Behavior: Maximize Efficacy Only"
- **Position:** Below the arrow shaft, centered
- **Font:** 8 pt Bold Italic, Red (#CC3311)
- **Background:** White semi-transparent box (80% opacity) so text is legible over points

### Why Horizontal?
The manuscript says agents "optimize single metrics" and "predict A > B but cannot articulate: 'A is twice as potent but has a threefold narrower safety margin.'" The horizontal arrow shows the agent moving along one dimension (efficacy) while completely ignoring the other (safety). If the arrow pointed diagonally toward top-left, it would suggest the agent seeks both high efficacy AND high safety — which would be good, not a failure mode.

---

## Inset Panel — "What the Agent Sees" (1D View)

### Purpose
Show that when agents optimize a single objective (efficacy), they collapse the 2D trade-off space into a 1D ranking. This visually demonstrates why they miss Pareto frontiers.

### Position
- **Location:** Top-right corner of main plot, inset
- **Size:** 50 mm × 30 mm
- **Background:** Light Gray (#DDDDDD)
- **Border:** 1.5 pt solid, Charcoal (#333333)

### Content
A **1D horizontal axis** showing only efficacy:

- **Axis:** Horizontal line across center of inset
- **Label (below axis):** "Efficacy Only (What Agent Optimizes)" — 7.5 pt SemiBold, #333333
- **Scale:** Same as main plot X-axis (10^-9 to 10^-5 M), but compressed
- **Tick marks:** 10^-9, 10^-7, 10^-5 (simplified)
- **Tick labels:** 1 nM, 100 nM, 10 μM — 7 pt Regular

### Points on 1D Axis
- **All 100 points from main plot** projected onto this 1D axis (using their efficacy values only)
- **Style:** Small circles (2 mm diameter)
- **Color:** All Blue (#0072B2) — no distinction between Pareto and non-Pareto anymore
- **Position:** Stacked vertically at their X-coordinate (efficacy value) if they overlap
- **Key visual:** Densest clustering at left (high efficacy) — this is where the agent focuses

### Annotation Inside Inset
- **Arrow:** Pointing left (toward high efficacy)
- **Text:** "Agent focuses here" — 7 pt Italic, Blue (#0072B2)
- **Position:** Top-left corner of inset

---

## Legend

### Position
- **Location:** Bottom-right corner, below the inset panel
- **Size:** 50 mm × 40 mm
- **Background:** White (#FFFFFF)
- **Border:** 1 pt solid, Medium Gray (#888888)
- **Padding:** 3 mm internal

### Legend Items

#### 1. Point Color
- **Title:** "Pareto Status" — 9 pt SemiBold
- **Items (vertically stacked):**
  - ● (Sky Blue circle, 4 mm) — "Pareto-optimal" (8 pt Regular)
  - ● (Orange circle, 4 mm) — "Dominated" (8 pt Regular)

#### 2. Point Size
- **Title:** "Stability (Half-Life)" — 9 pt SemiBold
- **Items (horizontally arranged):**
  - ● (3 mm circle) — "< 1 hr" (7 pt Regular)
  - ● (5 mm circle) — "1-6 hr" (7 pt Regular)
  - ● (8 mm circle) — "> 6 hr" (7 pt Regular)

#### 3. Frontier Line
- **Item:** 
  - — (Bluish Green line, 2.5 pt, 10 mm long) — "Pareto Frontier" (8 pt Regular)

#### 4. Callouts
- **Item:**
  - — (Vermillion line with circle endpoint, 1 pt) — "Highlighted Candidates" (8 pt Regular)

---

## Realistic Synthetic Data Generation Notes (For Illustrator or Python Script)

If generating data programmatically:

### Efficacy (IC50) Values
- Log-uniform distribution: `IC50 = 10^uniform(-9, -5)` M
- Pareto points biased toward lower IC50 (higher efficacy): `10^uniform(-9, -6.5)` M

### Safety (TI) Values
- For Pareto points: Inverse relationship with efficacy (trade-off)
  - High efficacy (IC50 ~ 1 nM) → moderate TI (100-300)
  - Lower efficacy (IC50 ~ 100 nM) → high TI (500-1000)
  - Functional form: `TI = 50 + 800 * (log10(IC50) + 9) / 4` (rough heuristic)
- For dominated points: Lower TI than Pareto points at same efficacy
  - Randomly reduce TI by 30-70%

### Stability (Point Size)
- Uniform random assignment: 1/3 small, 1/3 medium, 1/3 large
- **No correlation** with efficacy or safety (this is realistic — stability is often independent)

### Pareto Frontier Calculation
After generating all points:
1. Sort by efficacy (ascending IC50)
2. Identify Pareto-optimal set: points where no other point has both better efficacy AND better safety
3. Fit a smooth convex curve through Pareto points (spline interpolation)

---

## What NOT to Do

- ❌ **Do not use 3D plots** — this is explicitly a 2D scatter plot with point size encoding the third dimension. 3D plots are hard to read and don't print well.
- ❌ **Do not use pie charts, bar charts, or box plots** — this is a scatter plot showing individual candidates.
- ❌ **Do not use red-green as the only distinction** between Pareto and non-Pareto points (colorblind safety). Blue-orange is colorblind-safe.
- ❌ **Do not make the Pareto frontier a straight line** — it must be a convex curve (bowed outward), which is the mathematical property of Pareto frontiers.
- ❌ **Do not use arbitrary or toy data** — values should be realistic for peptide drug candidates (IC50 in nM range, TI > 10, half-life in hours).
- ❌ **Do not omit the inset panel** — it's critical for showing what the agent sees (1D) vs reality (2D).
- ❌ **Do not make all high-efficacy points large (stable)** — some must be small to show the trade-off agents miss.
- ❌ **Do not rasterize text or vector elements** — everything should remain editable.
- ❌ **Do not use decorative elements** (backgrounds, shadows, glows) — keep it clean and scientific.

---

## Key Visual Messages (What the Reader Should Understand)

These messages directly support the manuscript's critiques of current agentic AI systems:

1. **Trade-offs are real and non-linear** (Manuscript: "Objectives conflict: potency improvements reduce selectivity, stability enhancements increase immunogenicity"): The Pareto frontier shows that improving efficacy costs safety (and vice versa). The curve's non-uniform shape shows these trade-offs are complex, not simple linear exchanges.

2. **Single-objective optimization misses the decision space** (Manuscript: "ChemCrow optimizes binding affinity... Coscientist targets synthesis yield"): The red horizontal arrow shows agents chase maximum efficacy, completely ignoring the safety dimension. They land in a narrow region when the full Pareto frontier offers diverse strategic choices.

3. **Pareto-optimal ≠ "the answer"** (Manuscript: "Optimality depends on indication, development stage, competitive landscape, and risk tolerance"): Even Pareto-optimal candidates (Sky Blue) represent different trade-offs. Choosing among A (high potency, narrow margin), B (robust safety), or C (stability advantage) requires human judgment about context — which agents cannot provide.

4. **Dominated candidates are objectively inferior:** Orange points below the frontier are strictly worse — there exists a Pareto point that beats them on ALL objectives. These can be safely eliminated without human deliberation.

5. **Hidden dimensions matter** (Manuscript: "Stability modifications can reduce affinity, increase aggregation, or complicate synthesis"): Point size (stability) shows that some high-efficacy candidates are unstable. An agent optimizing efficacy as a scalar would rank these highest, missing a deal-breaking constraint.

6. **Weighted sums discard information** (Manuscript: "Multiple objectives collapse to weighted sums... This discards information"): The inset shows how agents flatten 2D+ decision spaces into 1D rankings. All context about trade-off structure, sensitivity to weights, and alternative strategies disappears.

7. **The real problem: agents can't represent this** (Manuscript: "Agents do not visualize Pareto frontiers or sensitivity to weight changes"): This figure shows what practitioners need — and what current agent architectures cannot deliver.

---

## Accessibility Checklist

- [ ] Colorblind-safe palette (Okabe-Ito, tested with Coblis)
- [ ] Pareto vs dominated points distinguishable in grayscale (position + color)
- [ ] High-contrast text (dark on light backgrounds throughout)
- [ ] Point sizes large enough to distinguish (3 mm, 5 mm, 8 mm)
- [ ] Grid lines subtle enough not to clutter (dotted, light gray)
- [ ] All callout text legible at print size (minimum 7 pt)
- [ ] Legend items clearly labeled with both visual + text descriptions

---

## Delivery Checklist

- [ ] SVG (editable vector) with all text as text objects (not paths)
- [ ] High-res PNG (300 DPI, 180 mm × 135 mm at print size)
- [ ] Layered source file (Figma / Illustrator / Python Matplotlib script with data)
- [ ] Grayscale version (verify Pareto frontier legible)
- [ ] Colorblind simulation screenshots (deuteranopia, protanopia, tritanopia)
- [ ] Data file (CSV with 100 points: IC50, TI, Stability, Pareto_status)

---

## Optional Enhancements (If Space/Time Permits)

### Enhancement 1: Uncertainty Bands (Aligned with Manuscript § "Incorporating Uncertainty and Risk")
The manuscript emphasizes prediction uncertainty: **"IC50 equals 10 nM might have a 95% interval of 5-20 nM or 1-100 nM. Ignoring uncertainty leads to poor decisions."**

If showing predicted vs experimental candidates:
- Add error bars or confidence ellipses around selected points (e.g., the 4 callout candidates)
- Use lighter shade of point color for uncertainty region (e.g., faint orange halos around dominated points showing uncertainty overlap with frontier)
- Label: "Prediction uncertainty (95% CI)" in legend
- This would visually demonstrate that some "dominated" candidates might actually be on the frontier when uncertainty is accounted for

### Enhancement 2: Decision Region Shading
- Shade regions of the plot by desirability:
  - Green tint: High safety + high efficacy (top-left, above frontier — theoretically ideal but often infeasible)
  - Yellow tint: Acceptable trade-offs (near frontier)
  - Red tint: Unacceptable (low safety + low efficacy, bottom-right)
- Use subtle transparency (20% opacity) so points remain visible

**From manuscript on constraints:** "Constraints add complexity: synthesizability, solubility, permeability, absence of toxicophores. Constrained optimization identifies the Pareto frontier within feasible regions, which may be disjoint or conflicting." 

Optionally, add a small shaded "infeasible region" (e.g., diagonal hatching in upper-left) labeled "High predicted performance but synthesis infeasible" to show that not everything above the frontier is actually achievable.

### Enhancement 3: Interactive Version (Web/Supplementary)
If creating an interactive version for supplementary materials:
- Hovering over points shows full candidate details
- Toggle to show/hide dominated points
- Slider to filter by minimum stability threshold
- Clickable callouts to expand detailed annotations

---

## Reference Style

**Target aesthetic:** Nature Methods / Nature Machine Intelligence scatter plots — clean, modern, data-dense but not cluttered. Prioritize clarity of the Pareto frontier and the contrast between agent behavior (1D, single-objective) and reality (2D+, multi-objective).

**Visual references:**
- Multi-objective optimization figures in drug discovery papers
- Pareto frontier diagrams in optimization literature
- Scatter plots with categorical encoding (color + size)

---

## Technical Notes for Python/Matplotlib Implementation

If generating this figure programmatically (recommended for reproducibility):

### Context from Manuscript

The manuscript discusses two multi-objective optimization methods that **construct Pareto frontiers** but are **not supported by current agents**:

1. **NSGA-II (Non-dominated Sorting Genetic Algorithm II)**: "Maintains candidate populations and selects non-dominated solutions"
2. **Multi-objective Bayesian optimization**: "Models objectives, selects candidates via acquisition functions balancing exploration and Pareto improvement"

This figure illustrates what these methods produce — and what agents that use single-objective optimization or weighted sums cannot represent.

### Python Implementation

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import UnivariateSpline

# Figure setup
fig, ax = plt.subplots(figsize=(7.09, 5.31))  # 180mm × 135mm at 100 DPI
ax.set_facecolor('#FAFAFA')

# Generate synthetic data
np.random.seed(42)  # Reproducibility
n_dominated = 60
n_pareto = 30
n_agent_favorite = 10

# Efficacy (IC50) - log scale
ic50_dominated = 10**np.random.uniform(-8, -5, n_dominated)
ic50_pareto = 10**np.random.uniform(-9, -6.5, n_pareto)
ic50_agent = 10**np.random.uniform(-9, -8.3, n_agent_favorite)

# Safety (TI) - correlated with efficacy for Pareto, reduced for dominated
def ti_pareto_func(ic50):
    return 50 + 800 * (np.log10(ic50) + 9) / 4 + np.random.normal(0, 50)

ti_pareto = np.array([ti_pareto_func(ic50) for ic50 in ic50_pareto])
ti_pareto = np.clip(ti_pareto, 100, 1000)

ti_dominated = ti_pareto_func(ic50_dominated) * np.random.uniform(0.3, 0.7, n_dominated)
ti_dominated = np.clip(ti_dominated, 10, 300)

ti_agent = ti_pareto_func(ic50_agent)
ti_agent = np.clip(ti_agent, 50, 200)

# Stability (point sizes) - random
sizes_dominated = np.random.choice([30, 60, 120], n_dominated)
sizes_pareto = np.random.choice([30, 60, 120], n_pareto)
sizes_agent = np.random.choice([30, 60, 120], n_agent_favorite)

# Plot dominated points
ax.scatter(ic50_dominated, ti_dominated, s=sizes_dominated, 
           c='#E69F00', alpha=0.85, edgecolors='#CC7A00', linewidths=0.75)

# Plot Pareto points
ax.scatter(ic50_pareto, ti_pareto, s=sizes_pareto,
           c='#56B4E9', alpha=0.85, edgecolors='#3A9BD9', linewidths=0.75)

# Pareto frontier curve
sorted_indices = np.argsort(ic50_pareto)
ic50_sorted = ic50_pareto[sorted_indices]
ti_sorted = ti_pareto[sorted_indices]
spline = UnivariateSpline(np.log10(ic50_sorted), ti_sorted, s=5000, k=3)
ic50_curve = np.logspace(-9, -6.5, 100)
ti_curve = spline(np.log10(ic50_curve))
ax.plot(ic50_curve, ti_curve, color='#009E73', linewidth=2.5, label='Pareto Frontier')

# Axes setup
ax.set_xscale('log')
ax.set_xlabel('Efficacy (Lower IC50 = More Potent)', fontsize=10, weight='semibold')
ax.set_ylabel('Safety (Therapeutic Index = LD50/IC50)', fontsize=10, weight='semibold')
ax.set_xlim(1e-9, 1e-5)
ax.set_ylim(10, 1000)
ax.grid(True, linestyle=':', color='#DDDDDD', linewidth=0.5)

# Inset panel
inset_ax = fig.add_axes([0.65, 0.72, 0.25, 0.15])  # [left, bottom, width, height]
inset_ax.set_facecolor('#DDDDDD')
# ... (implement 1D projection)

plt.tight_layout()
plt.savefig('fig6_pareto_frontier.svg', format='svg', dpi=300)
plt.savefig('fig6_pareto_frontier.png', format='png', dpi=300)
```

---

*Brief version: 1.0 — 2026-02-05*
