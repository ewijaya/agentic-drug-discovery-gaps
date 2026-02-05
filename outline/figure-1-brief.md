# Figure 1: The Agent Reality Gap in Drug Discovery

**Illustrator Brief — Comprehensive & Self-Sufficient**

---

## Paper Context

This figure is the **hero/overview figure** for a position paper titled *"What Drug Discovery AI Agents Still Can't Do."*

**Core argument:** Current AI "agents" in drug discovery are built for a narrow use case — small-molecule drug design at big pharmaceutical companies. They fail when applied to peptide drugs, animal study data, real ML training workflows, small biotech constraints, and multi-objective decisions.

**Central metaphor:** "The Reality Gap" — the divide between what AI agent demos show (clean, computational, text-based) and what drug discovery actually requires (messy, biological, multi-modal).

**Audience:** AI researchers, drug discovery scientists, biotech practitioners. The figure must be understandable to both computational and experimental scientists.

**Placement:** Introduction section. This is the first figure the reader sees. It must communicate the paper's thesis in a single glance.

---

## Figure Specifications

### Dimensions & Format

- **Size:** 180 mm × 120 mm (full-width, landscape — Nature/Science standard)
- **Resolution:** 300 DPI minimum; vector (SVG/PDF) preferred
- **Bleed:** None
- **Delivery formats:** SVG (primary), high-res PNG (review), layered source file (Figma/Illustrator/Affinity)
- **File name:** `fig1_reality_gap`

---

## Typography

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Figure title | Open Sans or Helvetica Neue | 12 pt | Bold | #333333 |
| Panel headers | Open Sans or Helvetica Neue | 10 pt | SemiBold | Panel color (see below) |
| Element labels | Open Sans or Helvetica Neue | 8–9 pt | Regular | #555555 |
| Sub-labels / descriptions | Open Sans or Helvetica Neue | 7 pt | Regular | #888888 |
| Gap zone label | Open Sans or Helvetica Neue | 11 pt | Bold | #333333 |
| Bridge tags | Open Sans or Helvetica Neue | 7–8 pt | SemiBold | #666666 |
| Bottom strip text | Open Sans or Helvetica Neue | 8 pt | Italic | Panel color |

**All text must remain editable** (not rasterized).

---

## Color Palette (Colorblind-Safe — Okabe-Ito derived)

| Role | Hex | Usage in This Figure |
|------|-----|---------------------|
| Steel Blue | #4477AA | Left panel (computational/AI side) |
| Warm Orange | #EE6677 | Right panel (biological/real side) |
| Medium Gray | #AAAAAA | Gap zone divider |
| Charcoal | #333333 | Text, borders |
| Off-White | #F7F7F7 | General neutral background |
| Left panel background | #E8F0FE | Light blue tint |
| Right panel background | #FFF3E8 | Light warm tint |

**Rule:** Never rely on color alone to convey information. Always pair with shape, pattern, or label.

---

## Icon Style (Applies to All Elements)

- **Flat, outlined icons** — 2 pt stroke, no gradients, no 3D, no drop shadows
- Rounded corners on boxes (4 px radius)
- No clip art or stock icons — all icons drawn in the same consistent style
- Scientific accuracy matters more than decorative appeal

---

## Layout

Horizontal split-panel diagram with three zones:

```
┌─────────────────────┬──────────┬─────────────────────┐
│                     │          │                     │
│   LEFT PANEL        │   GAP    │   RIGHT PANEL       │
│   "What Agents      │  ZONE    │   "What Drug        │
│    Excel At"        │          │    Discovery         │
│                     │          │    Requires"         │
│   (Computational)   │          │   (Biological)      │
│                     │          │                     │
└─────────────────────┴──────────┴─────────────────────┘
         40%              20%             40%
```

---

## Left Panel — "What AI Agents Excel At"

### Overall Feel
Clean, orderly, almost sterile. Conveys "tidy computational world."

### Background
Light blue tint (#E8F0FE)

### Header
"What AI Agents Excel At" — 10 pt, SemiBold, Steel Blue (#4477AA). Top of panel, left-aligned.

### Elements
Six items arranged in a neat **2-column × 3-row grid** (or a tidy vertical list). Even spacing, consistent sizing. Each element is a rounded rectangle (approx 35 × 18 mm) containing:
- **Left:** A small icon (12 × 12 mm)
- **Right:** Label text + subtext

| # | Label | Subtext | Icon Description |
|---|-------|---------|-----------------|
| 1 | SMILES & Molecular Representations | Text-based chemical notation | Simplified molecular text string (e.g., "CC(=O)Oc..." in monospace) inside a code-style box |
| 2 | Chemical Databases | ChEMBL, PubChem, ZINC | Database cylinder with a small molecule symbol on it |
| 3 | Literature Mining & Synthesis | PubMed, patents, reviews | Stack of papers/documents with a magnifying glass overlay |
| 4 | Virtual Screening & Docking | Rigid-body, score-based ranking | A funnel shape — many small circles entering the top, few exiting the bottom |
| 5 | Property Prediction | LogP, solubility, toxicity flags | A simple line chart showing a prediction curve or bar chart |
| 6 | Synthesis Planning | Retrosynthesis, route scoring | A retrosynthesis arrow tree — one molecule at top branching down to 2–3 building blocks |

### Connections
Light connecting lines (0.75 pt, #CCCCCC) between elements suggesting a smooth linear workflow (top-left → top-right → middle-left → etc., or top-to-bottom). The flow should feel orderly and sequential.

### Key Visual Properties
- All boxes: same size, same alignment
- Spacing: uniform
- Lines: straight, no crossing
- Overall impression: organized, predictable, under control

---

## Gap Zone — "The Reality Gap"

### Overall Feel
A fracture, a divide, an absence. Not a wall (walls block); this is a gap (gaps are missing bridges).

### Background
Subtle gradient from light blue (#E8F0FE, left edge) to light warm (#FFF3E8, right edge).

### Central Visual
A **jagged diagonal crack/fracture** running top to bottom through the center — like a geological fault line. Should be:
- Subtle but unmistakable
- Not cartoonish — more like cracked glass or a tectonic rift
- The crack line in medium gray (#AAAAAA), approximately 2–3 pt, with slight irregularity

### Central Label
"THE REALITY GAP" — 11 pt, Bold, Charcoal (#333333). Centered vertically and horizontally within the gap zone.

### Bridge Labels
Five labels arranged vertically along the crack, as if they are missing bridge segments. Each label represents one of the paper's five gaps:

| # | Label | Position |
|---|-------|----------|
| 1 | Peptides | Top |
| 2 | In Vivo | Upper-middle |
| 3 | Multi-Paradigm | Center |
| 4 | Resources | Lower-middle |
| 5 | Multi-Objective | Bottom |

**Style for each label:**
- Inside a small rounded pill/tag shape (approx 20 × 8 mm)
- Dashed border (1 pt, #AAAAAA)
- Fill: white or very light gray (#FAFAFA)
- Text: 7–8 pt, SemiBold, #666666
- These tags should feel like placeholders — labels for bridges that don't exist yet

---

## Right Panel — "What Drug Discovery Actually Requires"

### Overall Feel
Complex, organic, interconnected, slightly "messy." Conveys "rich real-world complexity." This is NOT disorganized or ugly — it is dense and demanding.

### Background
Light warm tint (#FFF3E8)

### Header
"What Drug Discovery Actually Requires" — 10 pt, SemiBold, Warm Orange (#EE6677). Top of panel, left-aligned.

### Elements
Six items arranged **more organically** than the left panel — slightly offset from each other, varied sizes, some minor overlapping of edges. This visual contrast with the left panel's neat grid is intentional and critical.

| # | Label | Subtext | Icon Description |
|---|-------|---------|-----------------|
| 1 | In Vivo Animal Studies | Longitudinal scores, behavioral data | Simplified mouse silhouette with a data trace line (like a recovery curve) overlaid on it |
| 2 | Clinical Scoring & Phenotyping | Ordinal, subjective, time-series | Clipboard with a rating scale — 5 dots or checkboxes, some filled |
| 3 | Tissue Imaging & Histology | Spatial, high-dimensional | Microscope slide shape with simplified stained tissue (purple/pink circles suggesting cells) |
| 4 | Multi-Modal Omics | RNA-seq, proteomics, metabolomics | Three overlapping circles (Venn diagram style) labeled "RNA," "Protein," "Metabolite" |
| 5 | Wet Lab Iteration Cycles | Synthesis → test → redesign | Circular arrow (cycle) connecting three tiny icons: a flask, a chart, and a notepad |
| 6 | Safety–Efficacy Trade-offs | Pareto frontiers, human judgment | A balance scale — "Efficacy" on one side, "Safety" on the other, slightly tilted (not balanced) |

### Connections
**Curved lines** (not straight) between elements, 0.75 pt, #CCCCCC to #DDCCBB. Some lines cross each other. The connections suggest a web, not a pipeline.

### Key Visual Properties
- Boxes: varied sizes (some slightly larger, some smaller)
- Alignment: deliberately imperfect — slight offsets
- Lines: curved, branching, some crossing
- Some elements slightly overlap edges
- Overall impression: rich, interconnected, complex, real

---

## Bottom Strip (Optional Enhancement)

A thin horizontal bar (10 mm height) spanning the full figure width beneath the three panels.

| Position | Text | Style |
|----------|------|-------|
| Left-aligned | "Clean · Computational · Text-Based" | 8 pt, italic, Steel Blue (#4477AA) |
| Center | ← gap → (small arrows and space) | 8 pt, #AAAAAA |
| Right-aligned | "Messy · Biological · Multi-Modal" | 8 pt, italic, Warm Orange (#EE6677) |

---

## Critical Visual Contrasts (The Whole Point of This Figure)

The figure's message is communicated through deliberate contrast between left and right panels. Every design choice should reinforce this contrast:

| Aspect | Left Panel (AI Agents) | Right Panel (Reality) |
|--------|----------------------|----------------------|
| Layout | Grid-aligned, uniform spacing | Organic, varied, slight overlaps |
| Connections | Straight lines, linear flow | Curved lines, branching, crossing |
| Background | Cool, clean (#E8F0FE) | Warm, organic (#FFF3E8) |
| Icon density | Spacious, breathing room | Dense, packed |
| Element sizing | Identical sizes | Varied sizes |
| Overall impression | Orderly, sterile, under control | Complex, rich, lived-in |

---

## What NOT to Do

- ❌ **Do not make the right panel look "bad" or "chaotic"** — it should look complex and rich, not disorganized. Biology is hard, not ugly.
- ❌ **Do not use clip art or stock icons** — all icons should be drawn in the same flat outlined style.
- ❌ **Do not make the gap zone look like a wall or barrier** — it's a gap (absence), not a block (presence). Something is missing, not blocking.
- ❌ **Do not include any proprietary data, company names, or drug names** anywhere in the figure.
- ❌ **Do not use red-green as the only distinction** between any elements (colorblind safety).
- ❌ **Do not use gradients, 3D effects, or drop shadows** on any element.
- ❌ **Do not rasterize any text** — all labels must remain editable in the source file.

---

## Accessibility Checklist

- [ ] Colorblind-safe (test with [Coblis simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/))
- [ ] Legible when printed in grayscale (verify left/right are distinguishable without color)
- [ ] High-contrast text (dark text on light backgrounds throughout)
- [ ] All elements have text labels (no information conveyed by color/shape alone)
- [ ] Minimum 7 pt font size for smallest text

---

## Delivery Checklist

- [ ] SVG (editable vector)
- [ ] High-res PNG (300 DPI)
- [ ] Layered source file (Figma / Illustrator / Affinity Designer)
- [ ] Grayscale version (verify legibility)
- [ ] Colorblind simulation screenshot

---

## Reference Style

**Target aesthetic:** Nature Reviews / Science perspective figures — clean, modern, uncluttered. Prioritize clarity over decoration. The figure should be understandable in 10 seconds and worth studying for 60.

---

*Brief version: 1.0 — 2026-02-05*
