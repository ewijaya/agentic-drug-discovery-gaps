# Figure 6: The Pareto Frontier Agents Ignore

**Illustrator Brief — Comprehensive & Self-Sufficient**

---

## Paper Context

This figure appears in **Section 7 (Gap 5: Multi-Objective Navigation)** of a position paper titled *"What Drug Discovery AI Agents Still Can't Do."*

**Core argument of this section:** Current AI agents optimize single objectives (e.g., maximize binding affinity) when real drug discovery requires balancing multiple conflicting goals simultaneously: efficacy, safety, stability, synthesizability, and cost. Real candidates lie on **Pareto frontiers** — where improving one property necessarily degrades another. Human decision-makers need interpretable trade-off visualizations to navigate these frontiers, not black-box "optimal" suggestions that ignore critical constraints.

**Specific problem:** Most agent demonstrations report success when they find a compound with the highest predicted binding affinity. In reality, that compound might be toxic, unstable in solution, or impossible to synthesize at scale. Drug discovery practitioners must identify candidates that represent **acceptable compromises** across multiple competing objectives.

**The "single-metric trap":** AI agents are typically rewarded for maximizing a single score (e.g., "find the peptide with the lowest IC50"). This leads them to ignore safety-efficacy trade-offs, stability constraints, and practical synthesizability — all of which are deal-breakers in real drug development.

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

- **Path:** Smooth Bézier curve through the Sky Blue (#56B4E9) points
- **Color:** Bluish Green (#009E73) 
- **Style:** 2.5 pt solid line
- **Start point:** Top-left (highest efficacy, moderate safety)
- **End point:** Top-right (lower efficacy, highest safety)
- **Shape:** Convex curve (bowed outward) — this is the mathematical property of Pareto frontiers

### Frontier Annotation
Small text label near the curve (middle section):
- Text: "Pareto Frontier" 
- Font: 8 pt SemiBold, #009E73 (matching curve color)
- Position: Above the curve, centered horizontally
- Optional: Small arrow pointing to the curve

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

#### Callout 1: "The Agent's Pick"
- **Target point location:** Top-left zone (highest efficacy)
  - IC50: ~1 nM
  - TI: ~100
  - Stability: SMALL point (low stability)
- **Callout position:** Upper-left area, leader line pointing to the point
- **Text:**
  ```
  Candidate A
  "The Agent's Pick"
  
  Highest efficacy (1 nM IC50)
  but unstable (t½ < 1 hr)
  Agent optimized for potency only
  ```

#### Callout 2: "The Safe Bet"
- **Target point location:** Right side of Pareto frontier (lower efficacy, highest safety)
  - IC50: ~100 nM
  - TI: ~900
  - Stability: LARGE point (high stability)
- **Callout position:** Upper-right area
- **Text:**
  ```
  Candidate B
  "The Safe Bet"
  
  Moderate efficacy (100 nM IC50)
  Excellent safety (TI = 900)
  Stable (t½ > 6 hr)
  ```

#### Callout 3: "The Balanced Compromise"
- **Target point location:** Middle of Pareto frontier
  - IC50: ~10 nM
  - TI: ~400
  - Stability: MEDIUM point
- **Callout position:** Right side, middle height
- **Text:**
  ```
  Candidate C
  "The Balanced Compromise"
  
  Good efficacy (10 nM IC50)
  Good safety (TI = 400)
  Moderate stability (t½ = 3 hr)
  ```

#### Callout 4: "The Dominated Candidate"
- **Target point location:** Lower-left, clearly below Pareto frontier (dominated)
  - IC50: ~50 nM
  - TI: ~80
  - Stability: MEDIUM point
- **Callout position:** Lower-left area
- **Text:**
  ```
  Candidate D
  "Dominated — Avoid"
  
  Worse than C in BOTH
  efficacy and safety
  No reason to choose this
  ```

---

## "Typical Agent Behavior" Arrow

A large, prominent arrow showing the failure mode of single-objective optimization.

### Visual Design
- **Start point:** Bottom-center of plot
- **End point:** Top-left corner (Zone 3 — highest efficacy)
- **Arrow style:**
  - 4 pt wide line, Red (#CC3311)
  - Large arrowhead (8 mm length)
  - Slightly curved (not perfectly straight) for visual interest
- **Transparency:** 60% opacity (so it doesn't obscure points)

### Arrow Label
- **Text:** "Typical Agent Behavior: Maximize Efficacy Only →"
- **Position:** Along the arrow shaft, bottom third
- **Font:** 8 pt Bold Italic, Red (#CC3311)
- **Background:** White semi-transparent box (80% opacity) so text is legible over points

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

1. **Trade-offs are real:** The Pareto frontier shows that improving efficacy costs safety (and vice versa). There is no "free lunch."

2. **Single-objective agents fail:** The red arrow shows agents chase maximum efficacy, landing in a region with poor safety and/or stability.

3. **Pareto-optimal ≠ perfect:** Even Pareto-optimal candidates (Sky Blue) have trade-offs. Choosing among them requires human judgment about acceptable compromises.

4. **Dominated candidates are easy to eliminate:** Orange points below the frontier are strictly worse — no reason to choose them.

5. **Stability matters too:** Point size shows that some high-efficacy candidates (small circles) are unstable — agents that optimize efficacy only will miss this.

6. **Dimensionality collapse:** The inset shows how agents flatten 2D (or higher) decision spaces into 1D rankings, losing critical information.

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

### Enhancement 1: Uncertainty Bands
If showing predicted vs experimental candidates:
- Add error bars or confidence ellipses around points
- Use lighter shade of point color for uncertainty region

### Enhancement 2: Decision Region Shading
- Shade regions of the plot by desirability:
  - Green tint: High safety + high efficacy (top-left, above frontier)
  - Yellow tint: Acceptable trade-offs (near frontier)
  - Red tint: Unacceptable (low safety + low efficacy, bottom-right)
- Use subtle transparency (20% opacity) so points remain visible

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
