# Figure 5: Big Pharma vs Small Biotech — The Resource Gap

**Illustrator Brief — Comprehensive & Self-Sufficient**

---

## Paper Context

This figure appears in a position paper titled *"The Blind Spots of Agentic Drug Discovery."*

**Core argument:** Current AI agent systems for drug discovery are designed with Big Pharma resources in mind. They assume massive datasets, large ML teams, extensive compute infrastructure, and months of runtime. Most drug discovery happens in small biotechs with 10-100x fewer resources. This figure quantifies that gap.

**Section context (Gap 4):** The paper's fourth gap addresses "The Small Biotech Reality" — the mismatch between agent system requirements and the resource constraints most practitioners face. While systems like ChatInvent are deployed at AstraZeneca with institutional databases, HPC clusters, and specialized teams built over decades, small biotechs operate with **10-100× leaner resource profiles**: 50-100 employees, single wet labs, limited computational infrastructure, and modest funding. One person designs experiments, analyzes results, and manages 14+ project types simultaneously.

**Key message:** Current agent architectures ignore cold-start problems, data efficiency, and generalization under scarcity. The manuscript emphasizes that **one person manages 14+ project types simultaneously** in small biotech contexts—a reality incompatible with interactive chat interfaces. This figure makes the resource disparity visible and quantifiable.

**Audience:** AI researchers building agent systems, drug discovery practitioners, biotech founders, and funding bodies. The figure must communicate the scale of resource inequality without making small biotechs look "inadequate" — they're constrained, not incompetent.

**Placement:** Section 6 (Gap 4: The Small Biotech Reality). This is the fourth major figure, following discussions of peptide bias, in vivo data, and multi-paradigm architectures.

---

## Figure Specifications

### Dimensions & Format

- **Size:** 180 mm × 100 mm (full-width, landscape — Nature/Science standard)
- **Resolution:** 300 DPI minimum; vector (SVG/PDF) preferred
- **Bleed:** None
- **Delivery formats:** SVG (primary), high-res PNG (review), layered source file (Figma/Illustrator/Affinity)
- **File name:** `fig5_resource_gap`

---

## Typography

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Figure title | Open Sans or Helvetica Neue | 12 pt | Bold | #333333 |
| Column headers | Open Sans or Helvetica Neue | 11 pt | Bold | Column color (see below) |
| Row category labels | Open Sans or Helvetica Neue | 9 pt | SemiBold | #555555 |
| Numerical values | Open Sans or Helvetica Neue | 10 pt | Bold | Column color |
| Ratio annotations | Open Sans or Helvetica Neue | 8 pt | SemiBold Italic | #D55E00 (orange) |
| Icon sublabels | Open Sans or Helvetica Neue | 7 pt | Regular | #888888 |
| Callout box text | Open Sans or Helvetica Neue | 8 pt | Regular | #333333 |
| Callout box title | Open Sans or Helvetica Neue | 9 pt | Bold | #D55E00 (orange) |

**All text must remain editable** (not rasterized).

---

## Color Palette (Colorblind-Safe — Okabe-Ito)

| Role | Hex | Name | Usage in This Figure |
|------|-----|------|---------------------|
| Deep Blue | #0072B2 | Sky Blue | Big Pharma column (saturated) |
| Pale Blue | #B3D9F2 | Light Sky Blue | Small Biotech column (muted version) |
| Warm Orange | #D55E00 | Vermillion | Ratio annotations, callout accents |
| Charcoal | #333333 | Near Black | Primary text, borders |
| Medium Gray | #888888 | Gray | Secondary text, sublabels |
| Light Gray | #F0F0F0 | Off-White | Background fill |
| Yellow | #F0E442 | Yellow | Callout box background |

**Design principle:** Big Pharma uses saturated, bold Deep Blue (#0072B2). Small Biotech uses the exact same hue but desaturated/lightened to Pale Blue (#B3D9F2). This creates visual hierarchy while maintaining conceptual continuity — they're the same "type" of organization, just different scales.

**Rule:** Never rely on color alone. Always pair with size, quantity, or label.

---

## Icon Style (Applies to All Elements)

- **Flat, outlined icons** — 2 pt stroke, no gradients, no 3D, no drop shadows
- Rounded corners on boxes (4 px radius)
- Proportional sizing is critical — icons must visually convey scale differences
- Scientific accuracy matters; avoid corporate clip art aesthetics

---

## Layout

Two-column comparison with five resource categories arranged vertically. A callout box at the bottom spans both columns.

```
┌─────────────────────────────────────────────────────────────┐
│  Figure 5: Big Pharma vs Small Biotech — The Resource Gap  │
├─────────────────────────┬───────────────────────────────────┤
│   BIG PHARMA            │   SMALL BIOTECH                   │
│   (Deep Blue #0072B2)   │   (Pale Blue #B3D9F2)             │
├─────────────────────────┼───────────────────────────────────┤
│                         │                                   │
│  Row 1: Data            │  Row 1: Data                      │
│  Row 2: Team            │  Row 2: Team                      │
│  Row 3: Compute         │  Row 3: Compute                   │
│  Row 4: Personnel       │  Row 4: Personnel                 │
│  Row 5: Budget          │  Row 5: Budget                    │
│                         │                                   │
├─────────────────────────┴───────────────────────────────────┤
│                    CALLOUT BOX                              │
│  "What This Means for AI Agents"                            │
└─────────────────────────────────────────────────────────────┘
```

**Column widths:** Equal (90 mm each).

**Row height:** Variable — leave sufficient space for icons to scale proportionally.

**Vertical spacing:** 8 mm between rows (measured from icon bottom to next icon top).

---

## Column Headers

### Big Pharma Column (Left)

**Header text:** "BIG PHARMA" — 11 pt, Bold, Deep Blue (#0072B2)

**Subheader:** "Resource-rich context (e.g., AstraZeneca, Pfizer)" — 7 pt, Regular, #888888

**Background:** Very light blue tint (#F7FBFF), subtle, doesn't interfere with white icons

---

### Small Biotech Column (Right)

**Header text:** "SMALL BIOTECH" — 11 pt, Bold, Pale Blue (#B3D9F2)

**Subheader:** "Resource-constrained reality (50-100 employees, single wet lab)" — 7 pt, Regular, #888888

**Background:** Very light gray tint (#FAFAFA)

---

## Row 1: Proprietary Data (Compounds/Peptides)

### Left Column (Big Pharma)

**Category label:** "Proprietary Data" — 9 pt, SemiBold, #555555 (positioned above icons)

**Icon:** Database cylinder (classic 3D cylinder representation as 2D flat outline)

- **Size:** 40 mm wide × 35 mm tall
- **Color:** Deep Blue (#0072B2), 2 pt stroke, no fill (outlined style)
- **Internal detail:** 5-6 horizontal lines inside suggesting stacked data layers

**Label below icon:** "Millions of tested molecules" — 10 pt, Bold, Deep Blue (#0072B2)

**Sublabel:** "Institutional databases built over decades" — 7 pt, Regular, #888888

---

### Right Column (Small Biotech)

**Category label:** "Proprietary Data" — 9 pt, SemiBold, #555555

**Icon:** Database cylinder (same style as left)

- **Size:** 8 mm wide × 7 mm tall (exactly 1/5 the area of Big Pharma icon)
- **Color:** Pale Blue (#B3D9F2), 2 pt stroke, no fill
- **Internal detail:** 2-3 horizontal lines

**Label below icon:** "50–500 proprietary sequences" — 10 pt, Bold, Pale Blue (#B3D9F2)

**Sublabel:** "Every assay is precious" — 7 pt, Regular, #888888

**Ratio annotation (between columns, centered):**
Arrow pointing from Small → Big with text "10,000× less data" — 8 pt, SemiBold Italic, Warm Orange (#D55E00)

---

## Row 2: ML/AI Team Size

### Left Column (Big Pharma)

**Category label:** "ML/AI Team" — 9 pt, SemiBold, #555555

**Icon:** Grid of person silhouettes (simple head + shoulders outline)

- **Arrangement:** 5 rows × 10 columns = 50 people
- **Individual silhouette size:** 3 mm × 4 mm each
- **Spacing:** 1 mm between silhouettes
- **Color:** Deep Blue (#0072B2), 2 pt stroke, no fill
- **Total grid size:** ~35 mm × 24 mm

**Label below icon:** "Specialized teams" — 10 pt, Bold, Deep Blue (#0072B2)

**Sublabel:** "ML engineers, chemists, biologists, data engineers" — 7 pt, Regular, #888888

---

### Right Column (Small Biotech)

**Category label:** "ML/AI Team" — 9 pt, SemiBold, #555555

**Icon:** Single person silhouette (same style)

- **Size:** 3 mm × 4 mm (one person)
- **Color:** Pale Blue (#B3D9F2), 2 pt stroke, no fill
- **Positioned to align with the center-left of the Big Pharma grid for visual comparison**

**Label below icon:** "1 person doing everything" — 10 pt, Bold, Pale Blue (#B3D9F2)

**Sublabel:** "Design, modeling, analysis, infrastructure" — 7 pt, Regular, #888888

**Ratio annotation (between columns, centered):**
Arrow with text "50× smaller team" — 8 pt, SemiBold Italic, Warm Orange (#D55E00)

---

## Row 3: Compute Infrastructure

### Left Column (Big Pharma)

**Category label:** "Compute Infrastructure" — 9 pt, SemiBold, #555555

**Icon:** Server rack (stylized rack-mount servers)

- **Representation:** 4 horizontal server units stacked vertically, each with small dots representing LED indicators
- **Size:** 30 mm wide × 28 mm tall
- **Color:** Deep Blue (#0072B2), 2 pt stroke, no fill
- **Internal detail:** Each server unit has 3-4 small circles (ports/LEDs)

**Label below icon:** "HPC clusters" — 10 pt, Bold, Deep Blue (#0072B2)

**Sublabel:** "Multi-GPU, dedicated infrastructure" — 7 pt, Regular, #888888

---

### Right Column (Small Biotech)

**Category label:** "Compute Infrastructure" — 9 pt, SemiBold, #555555

**Icon:** Single laptop (simple outline, open laptop shape)

- **Size:** 12 mm wide × 8 mm tall
- **Color:** Pale Blue (#B3D9F2), 2 pt stroke, no fill
- **Detail:** Screen and keyboard hinge visible

**Alternative icon (if preferred):** Single GPU card (smaller rectangle with PCIe connector detail)

**Label below icon:** "1–2 GPUs" — 10 pt, Bold, Pale Blue (#B3D9F2)

**Sublabel:** "Sparse cloud credits, no HPC" — 7 pt, Regular, #888888

**Ratio annotation (between columns, centered):**
Arrow with text "100× less compute power" — 8 pt, SemiBold Italic, Warm Orange (#D55E00)

---

## Row 4: Data Engineering Support

### Left Column (Big Pharma)

**Category label:** "Data Engineering" — 9 pt, SemiBold, #555555

**Icon:** Pipeline diagram (data flowing through processing stages)

- **Representation:** Three connected nodes (circles) with arrows flowing left-to-right: "Raw Data" → "ETL" → "Clean DB"
- **Size:** 35 mm wide × 12 mm tall
- **Color:** Deep Blue (#0072B2), 2 pt stroke
- **Detail:** Each node is a 10 mm diameter circle with label inside (6 pt)

**Label below icon:** "Dedicated data engineering team" — 10 pt, Bold, Deep Blue (#0072B2)

**Sublabel:** "Automated pipelines, version control, infrastructure support" — 7 pt, Regular, #888888

---

### Right Column (Small Biotech)

**Category label:** "Data Engineering" — 9 pt, SemiBold, #555555

**Icon:** Single file folder with wrench icon overlay

- **Representation:** Simple folder outline with small wrench/screwdriver crossed in corner
- **Size:** 10 mm × 10 mm
- **Color:** Pale Blue (#B3D9F2), 2 pt stroke, no fill

**Label below icon:** "Manual data wrangling" — 10 pt, Bold, Pale Blue (#B3D9F2)

**Sublabel:** "Scientist cleans CSVs in Jupyter notebooks" — 7 pt, Regular, #888888

**Ratio annotation (between columns, centered):**
Arrow with text "Ad-hoc vs systematic" — 8 pt, SemiBold Italic, Warm Orange (#D55E00)

---

## Row 5: Compute Budget (Time)

### Left Column (Big Pharma)

**Category label:** "Compute Budget (Time)" — 9 pt, SemiBold, #555555

**Icon:** Calendar grid showing multiple months

- **Representation:** 3-month calendar grid (simplified)
- **Size:** 30 mm wide × 20 mm tall
- **Color:** Deep Blue (#0072B2), 2 pt stroke
- **Detail:** Grid of small boxes representing days, with "Month 1, 2, 3" labels

**Label below icon:** "Weeks to months" — 10 pt, Bold, Deep Blue (#0072B2)

**Sublabel:** "Run large RL training, MD simulations, hyperparameter sweeps" — 7 pt, Regular, #888888

---

### Right Column (Small Biotech)

**Category label:** "Compute Budget (Time)" — 9 pt, SemiBold, #555555

**Icon:** Clock face showing ~8 hours

- **Representation:** Simple clock with hour and minute hands
- **Size:** 10 mm diameter
- **Color:** Pale Blue (#B3D9F2), 2 pt stroke, no fill
- **Detail:** Hands positioned at 8 o'clock to suggest "hours"

**Label below icon:** "Hours to days" — 10 pt, Bold, Pale Blue (#B3D9F2)

**Sublabel:** "Must be sample-efficient, fast iteration cycles" — 7 pt, Regular, #888888

**Ratio annotation (between columns, centered):**
Arrow with text "100× less runtime" — 8 pt, SemiBold Italic, Warm Orange (#D55E00)

---

## Callout Box (Bottom, Spanning Both Columns)

**Purpose:** Deliver the "so what" — connect these resource differences to the paper's thesis about agent design.

**Dimensions:** 180 mm wide × 25 mm tall

**Background:** Light yellow (#F0E442) with 1 pt border in Warm Orange (#D55E00)

**Corner radius:** 4 px (rounded)

**Content:**

**Title (left-aligned, 9 pt, Bold, Warm Orange #D55E00):**
"What This Means for AI Agents"

**Body text (8 pt, Regular, Charcoal #333333, left-aligned, 10 mm padding on all sides):**

"Current agent systems assume Big Pharma resources: millions of molecules, specialized teams, and HPC infrastructure. Small biotechs operate with **10-100× leaner profiles** but are where most early innovation happens. They need agents optimized for: **transfer learning** (ESM-2 pre-trained on millions enables fine-tuning on 50-200 examples), **active learning** (reducing experimental assays by 30-40%), and **batch-mode automation** (one person managing 14+ project types). Agents optimized for AstraZeneca leave the biotech ecosystem behind."

**Key phrases bolded:** "10-100× leaner profiles", "transfer learning", "active learning", "batch-mode automation"

---

## Visual Hierarchy and Proportions (Critical!)

The entire point of this figure is to make resource disparities **immediately visible through size/quantity**, not just numbers.

### Icon Sizing Rules

| Row | Big Pharma Icon | Small Biotech Icon | Ratio Preserved |
|-----|----------------|-------------------|----------------|
| 1: Data | 40 × 35 mm (area: 1400 mm²) | 8 × 7 mm (area: 56 mm²) | ~10,000:1 (millions vs hundreds) |
| 2: Team | 50 silhouettes (grid) | 1 silhouette | 50:1 count ratio (specialized teams vs 1 person) |
| 3: Compute | 30 × 28 mm server rack | 12 × 8 mm laptop | ~50:1 (HPC clusters vs 1-2 GPUs) |
| 4: Data Eng | 35 mm wide pipeline | 10 × 10 mm folder | Infrastructure vs manual (categorical difference) |
| 5: Budget | 30 × 20 mm calendar | 10 mm clock | Months vs hours-days (~100:1 time) |

**Critical design principle:** A reader should be able to glance at this figure and immediately think "Big Pharma has WAY more of everything." The size differences must be visceral, not subtle.

---

## Alignment and Spacing

- All icons in the same row should be **vertically centered** (aligned on their midpoint)
- Category labels should be **top-aligned** for each row
- Numerical labels should be **directly below** their corresponding icons (3 mm gap)
- Sublabels should be **directly below** numerical labels (2 mm gap)
- Ratio annotations should be **horizontally centered** between the two columns, vertically aligned with the icon midpoint

---

## What NOT to Do

- ❌ **Do not make Small Biotech icons look "sad" or "inadequate"** — they're smaller because of resource constraints, not incompetence. Avoid visual metaphors that suggest failure.
- ❌ **Do not use different icon styles** for the two columns — they must be the same visual language, just different scales.
- ❌ **Do not make the icons too small** — the Small Biotech icons must be clearly visible and legible even though they're much smaller than Big Pharma.
- ❌ **Do not exaggerate proportions** beyond the real-world ratios — stick to the 10–100× differences stated in the text.
- ❌ **Do not use corporate branding** (no AstraZeneca, Pfizer, or specific company logos) — keep it generic.
- ❌ **Do not use clip art or stock icons** — all icons must be drawn in the same consistent flat outlined style.
- ❌ **Do not rely on color alone** — size/quantity differences must be visible in grayscale.
- ❌ **Do not rasterize any text** — all labels must remain editable in the source file.
- ❌ **Do not use red-green as the primary distinction** (colorblind safety).

---

## Accessibility Checklist

- [ ] Colorblind-safe (test with [Coblis simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/))
- [ ] Legible when printed in grayscale (verify Big Pharma vs Small Biotech distinguishable by size/quantity, not just color)
- [ ] High-contrast text (dark text on light backgrounds throughout)
- [ ] All ratios communicated through size AND text annotation (no information conveyed by color/shape alone)
- [ ] Minimum 7 pt font size for smallest text
- [ ] Callout box text passes WCAG AA contrast standards (4.5:1 minimum)

---

## Tone and Messaging

**What this figure should communicate:**

- Small biotechs face massive resource constraints (objective fact)
- These constraints are systemic, not a reflection of competence
- Current AI agent systems are designed for the wrong context (Big Pharma)
- There's an opportunity to build agents that work for resource-constrained settings

**What this figure should NOT communicate:**

- Small biotechs are "worse" or "behind" (avoid deficit framing)
- Big Pharma is wasteful or excessive (no value judgments)
- One context is "better" than the other (they're just different)

**Visual tone:** Neutral, factual, slightly understated. Let the proportions speak for themselves.

---

## Delivery Checklist

- [ ] SVG (editable vector with all text as editable objects)
- [ ] High-res PNG (300 DPI, RGB color space)
- [ ] Layered source file (Figma / Illustrator / Affinity Designer with layers labeled)
- [ ] Grayscale version (verify legibility without color)
- [ ] Colorblind simulation screenshots (protanopia, deuteranopia, tritanopia)
- [ ] PDF export (embedded fonts, outlined text backup layer)

---

## Reference Style

**Target aesthetic:** Nature Reviews / Science perspective figures — clean, modern, data-driven. Similar to infographic styles in:

- *Nature Biotechnology* resource comparison figures
- McKinsey-style industry comparisons (but more scientific, less corporate)
- Data visualization in *The Economist* (clear, proportional, uncluttered)

**Key principle:** A reader should understand the resource gap in 5 seconds and appreciate the nuance in 30 seconds. The figure should be screenshot-friendly (clear even as a Twitter/X image) but reward closer inspection.

---

## Additional Context: Why This Figure Matters

From the paper's Section 5 (Gap 4: The Small Biotech Reality):

> "ChatInvent's deployment at AstraZeneca accessed institutional databases, HPC clusters, and proprietary libraries built over decades, with specialized teams (medicinal chemists, computational chemists, biologists, data scientists). This large pharma context defines current agent design assumptions but is not representative. Small biotechs face different constraints: 50-100 employees, single wet labs, limited computational infrastructure, modest funding. Proprietary datasets have hundreds of compounds, not millions. One person designs experiments, analyzes results, and manages projects. Resource profiles are 10-100 times leaner, yet agents assume large pharma contexts."

This figure makes that disparity concrete and visual. It validates the experience of small biotech practitioners who are underserved by current AI agent systems. It challenges AI researchers to design for **data efficiency** (transfer learning on 50-200 examples), **computational constraints** (1-2 GPUs, not clusters), and **batch-mode automation** (one person managing 14+ projects simultaneously)—contexts where most early drug discovery innovation actually happens.

---

*Brief version: 1.0 — 2026-02-05*
