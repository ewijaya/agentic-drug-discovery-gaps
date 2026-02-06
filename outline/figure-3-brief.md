# Figure 3: What Agents Can and Cannot Process

**Illustrator Brief — Comprehensive & Self-Sufficient**

---

## Paper Context

This figure supports **Gap 2: The In Vivo–In Silico Bridge** in a position paper titled *"The Blind Spots of Agentic Drug Discovery."*

**The argument from the manuscript:** Current AI agents excel at in vitro automation (synthesis, screening, literature mining) but hit a hard ceiling at in vivo studies. Animal experiments generate fundamentally different data: longitudinal (days to months), multi-modal (behavioral scores, imaging, molecular profiling), noisy, low-throughput, and expensive. These characteristics make in vivo data the bottleneck, yet agents provide no pathway to incorporate it.

**Specific quote from manuscript:** "In vivo studies yield heterogeneous streams. Neurological injury evaluation includes behavioral assessments (motor coordination via beam walking, generating ordinal scores), tissue histology (cell proliferation requiring computer vision), RNA sequencing (high-dimensional gene expression needing differential expression and pathway enrichment), and clinical notes (semi-structured weight and adverse events). Current agents cannot integrate these modalities."

**What this figure must communicate in 5 seconds:** There's a stark accessibility divide: agents handle text-based and structured formats well (green checkmarks), but the messy biological data that dominates real drug discovery remains inaccessible (red X's) or only partially accessible with heavy preprocessing (yellow half-circles).

**Audience:** AI researchers, drug discovery scientists, biotech practitioners. This is a practical reference figure — a reader should be able to glance at it and immediately understand what's feasible vs. what requires custom pipelines vs. what's currently impossible.

**Placement:** Section 3 (labeled "Blind Spot 2: The In Vivo to In Silico Bridge"). This figure accompanies Table 1 in the manuscript, which lists the same data types in tabular form.

---

## Figure Specifications

### Dimensions & Format

- **Size:** 180 mm × 110 mm (full-width, landscape — wider to show visual gradient clearly)
- **Resolution:** 300 DPI minimum; vector (SVG/PDF) preferred
- **Bleed:** None
- **Delivery formats:** SVG (primary), high-res PNG (review), layered source file
- **File name:** `fig3-invivo-insilico-gap` (matches manuscript reference)

---

## Typography

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Figure title | Open Sans or Helvetica Neue | 12 pt | Bold | #333333 |
| Section headers | Open Sans or Helvetica Neue | 9 pt | SemiBold | #555555 |
| Data type labels | Open Sans or Helvetica Neue | 8 pt | Regular | #333333 |
| Format sublabels | Open Sans or Helvetica Neue | 6.5 pt | Regular | #777777 |
| Use case examples | Open Sans or Helvetica Neue | 6.5 pt | Italic | #888888 |
| Icons (✓/◐/✗) | 18 pt symbol font or vector | — | Bold | See color palette |
| Legend text | Open Sans or Helvetica Neue | 7 pt | Regular | #555555 |
| Annotation text | Open Sans or Helvetica Neve | 7 pt | Italic | #999999 |

**All text must remain editable** (not rasterized).

---

## Color Palette (Colorblind-Safe — Okabe-Ito derived)

| Role | Hex | Symbol | Usage |
|------|-----|--------|-------|
| Accessible | #228833 | ✓ | Agent can process natively with high reliability |
| Partial | #CCBB44 | ◐ | Requires significant preprocessing or human curation |
| Inaccessible | #EE6677 | ✗ | Agent cannot meaningfully process this data type |
| Accessible fill (light) | #E8F5E9 | — | Background tint for accessible items |
| Partial fill (light) | #FFFBEA | — | Background tint for partial items |
| Inaccessible fill (light) | #FDECEA | — | Background tint for inaccessible items |
| Neutral Background | #F7F7F7 | — | General background |
| Divider | #DDDDDD | — | Section separators |
| Charcoal | #333333 | — | Primary text |
| Medium Gray | #777777 | — | Secondary text |

**Design Rule:** Each data type has BOTH a color-coded background AND an icon symbol. Never rely on color alone.

---

## Icon Style

- **Symbols:** 
  - ✓ (bold checkmark) for Accessible
  - ◐ (half-filled circle, left half filled) for Partial
  - ✗ (bold X mark) for Inaccessible
- **Size:** 16–18 pt or vector equivalent (approx 5.5 mm tall)
- **Weight:** Bold/heavy stroke weight for visibility at print scale
- **Color:** Symbols use the saturated color (not tint):
  - Accessible: #228833
  - Partial: #998822 (darker than fill)
  - Inaccessible: #CC4455
- **Alignment:** Left-aligned within each data type row, before the label

---

## Layout Overview

**Visual structure:** Horizontal layout showing data types as cards/rows, arranged from most accessible (left) to least accessible (right), creating a visual gradient from green → yellow → red.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Figure 3: What Agents Can and Cannot Process                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐            │
│  │ AGENTS EXCEL    │  │ PARTIAL/LIMITED │  │ AGENTS FAIL     │            │
│  │ (Native support)│  │ (Heavy lifting) │  │ (Not supported) │            │
│  ├─────────────────┤  ├─────────────────┤  ├─────────────────┤            │
│  │ ✓ Data Type 1   │  │ ◐ Data Type 5   │  │ ✗ Data Type 7   │            │
│  │ ✓ Data Type 2   │  │ ◐ Data Type 6   │  │ ✗ Data Type 8   │            │
│  │ ✓ Data Type 3   │  │                 │  │ ✗ Data Type 9   │            │
│  │ ✓ Data Type 4   │  │                 │  │                 │            │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘            │
│                                                                             │
│  [Legend: ✓ Accessible, ◐ Partial, ✗ Inaccessible]                         │
│  [Annotation: "The lab automation ceiling: agents stop where biology begins"]│
└─────────────────────────────────────────────────────────────────────────────┘
```

**Key design principle:** The horizontal grouping into three columns creates an immediate visual understanding of the accessibility divide. The size of each column (more red than green) reinforces the message that most real drug discovery data is inaccessible.

---

## Data Types — Exact List from Manuscript

The manuscript's **Table 1** (Data Type Accessibility for Current Agent Systems) lists these 9 data types. The figure must match this list exactly:

| # | Data Type | Format | Agent-Readable | Example Use Case (from manuscript) |
|---|-----------|--------|---------------|-----------------------------------|
| 1 | SMILES strings | Text | Yes (✓) | Small molecule property prediction |
| 2 | Literature abstracts | Text | Yes (✓) | Knowledge synthesis |
| 3 | PDB structures | Structured | Yes (✓) | Protein structure analysis |
| 4 | CSV assay data | Tabular | Yes (✓) | High-throughput screening |
| 5 | Tissue imaging | Image | Partial (◐) | Histological quantification |
| 6 | Clinical trajectories | Time-series | Partial (◐) | Longitudinal efficacy modeling |
| 7 | Clinical notes | Semi-structured text | Partial (◐) | Adverse event detection |
| 8 | Behavioral videos | Video | No (✗) | Phenotyping analysis |
| 9 | RNA-seq data | FASTQ/BAM | No (✗) | Transcriptomic profiling |

**Additional context from manuscript text (not in table but mentioned):**
- "Multi-modal transcriptomics" (mentioned in figure caption)
- "Longitudinal measurements with dropout" (mentioned in figure caption)

These are implicitly covered by items 6, 8, and 9 above.

---

## Three-Column Layout — Detailed Specifications

### Left Column — "Agents Excel" (4 items)
**Header:** "Agents Excel" — 9 pt, SemiBold, #228833
**Subheader:** "Native support, high reliability" — 6.5 pt, Regular, #777777

**Column background:** Very light green tint (#E8F5E9), subtle (5% opacity)
**Column width:** ~50 mm
**Column border:** 1.5 pt left border in #228833

**Data type cards (4 items stacked vertically):**

Each card contains:
- Icon (✓) — 18 pt, #228833, left-aligned
- Primary label (e.g., "SMILES strings") — 8 pt, Regular, #333333
- Format sublabel (e.g., "Text") — 6.5 pt, Regular, #777777
- Example use case (e.g., "Property prediction") — 6.5 pt, Italic, #888888

**Card appearance:**
- Dimensions: ~45 × 16 mm each
- Internal padding: 2 mm
- Background: white or very light green (#F1F8F1)
- Border: 0.75 pt, #CCCCCC
- Border radius: 3 px
- Spacing between cards: 2 mm

**Order (top to bottom):**
1. SMILES strings — Text — Small molecule property prediction
2. Literature abstracts — Text — Knowledge synthesis
3. PDB structures — Structured — Protein structure analysis
4. CSV assay data — Tabular — High-throughput screening

---

### Middle Column — "Partial/Limited" (3 items)
**Header:** "Partial/Limited" — 9 pt, SemiBold, #998822 (darker yellow)
**Subheader:** "Requires heavy preprocessing" — 6.5 pt, Regular, #777777

**Column background:** Very light yellow tint (#FFFBEA), subtle
**Column width:** ~50 mm
**Column border:** 1.5 pt left border in #CCBB44

**Data type cards (3 items stacked vertically):**

Same card structure as left column, but:
- Icon: ◐ (half-filled circle) — 18 pt, #998822
- Card background: white or very light yellow (#FFFEF5)

**Order (top to bottom):**
1. Tissue imaging — Image — Histological quantification
2. Clinical trajectories — Time-series — Longitudinal efficacy modeling
3. Clinical notes — Semi-structured text — Adverse event detection

---

### Right Column — "Agents Fail" (2 items)
**Header:** "Agents Fail" — 9 pt, SemiBold, #CC4455
**Subheader:** "Not supported by current architectures" — 6.5 pt, Regular, #777777

**Column background:** Very light red/pink tint (#FDECEA), subtle
**Column width:** ~50 mm
**Column border:** 1.5 pt left border in #EE6677

**Data type cards (2 items stacked vertically):**

Same card structure, but:
- Icon: ✗ — 18 pt, #CC4455
- Card background: white or very light pink (#FEF5F5)

**Order (top to bottom):**
1. Behavioral videos — Video — Phenotyping analysis
2. RNA-seq data — FASTQ/BAM — Transcriptomic profiling

**Important note:** The manuscript figure caption mentions "behavioral videos, clinical score trajectories, tissue imaging, multi-modal transcriptomics, longitudinal measurements with dropout" — these are all covered by the 9 items above. No need to add more.

---

## Visual Hierarchy — The Gradient Effect

**Critical design goal:** The three columns should create an immediate visual gradient from left (green, many items) to right (red, fewer items but representing more of real work).

**Reinforcement strategies:**
1. **Column heights:** Left column is tallest (4 items), middle is medium (3 items), right is shorter (2 items) — BUT the message is that the 2 items on the right represent the majority of in vivo work
2. **Color intensity:** Background tints get slightly more saturated from left to right (green is subtle, yellow is medium, red is noticeable)
3. **Border weight:** Left border of each column gets slightly heavier from left to right (1.5 pt → 2 pt → 2.5 pt)
4. **White space:** More padding inside cards in the right column to emphasize emptiness/absence

---

## Additional Visual Elements

### Connecting annotation (optional)
A subtle arrow or gradient bar beneath the three columns showing the spectrum from "Accessible" → "Partial" → "Inaccessible", with the label:

"The lab automation ceiling: agents stop where in vivo biology begins" — 7 pt, italic, #999999

Position: Centered below the three columns, 5 mm spacing from bottom of cards.

### Alternative annotation (from manuscript quote):
"No agent executes workflows spanning video processing, supervised learning, time-series engineering, and hypothesis testing" — 7 pt, italic, #999999

Choose whichever feels more impactful given the visual layout.

---

## Legend

Small legend box positioned **bottom-right** of the figure (approx 40 × 18 mm):

**Title:** "Agent Capability" — 7 pt, SemiBold, #555555

| Symbol | Color Swatch | Label |
|--------|-------------|-------|
| ✓ | Green circle (#228833) | Accessible |
| ◐ | Yellow half-circle (#998822) | Partial |
| ✗ | Red X (#CC4455) | Inaccessible |

Each swatch is a 5 mm icon followed by the label in 7 pt Regular, #555555.

---

## Alternative Layout Option — If Horizontal Doesn't Work

If the three-column horizontal layout feels too cramped, use a **vertical gradient layout** instead:

```
┌────────────────────────────────────────────┐
│  Data Type          Format      Capability │
├────────────────────────────────────────────┤
│  ✓ SMILES strings   Text        [green]   │
│  ✓ Literature       Text        [green]   │
│  ✓ PDB structures   Structured  [green]   │
│  ✓ CSV assay data   Tabular     [green]   │
│  ─────────────────────────────────────────  │
│  ◐ Tissue imaging   Image       [yellow]  │
│  ◐ Clinical traj.   Time-series [yellow]  │
│  ◐ Clinical notes   Semi-struct [yellow]  │
│  ─────────────────────────────────────────  │
│  ✗ Behavioral vid.  Video       [red]     │
│  ✗ RNA-seq data     FASTQ/BAM   [red]     │
└────────────────────────────────────────────┘
```

This creates a top-to-bottom gradient (green → yellow → red) that may be easier to scan than left-to-right columns.

**Use this option if:**
- The three-column layout feels too wide for the labels
- Vertical scanning feels more natural for a "list of data types"
- You want to emphasize the ordering (accessible at top, inaccessible at bottom)

**Formatting for vertical layout:**
- Each row: 10 mm height
- Icon column: 10 mm width
- Data type column: 50 mm width
- Format column: 35 mm width
- Capability indicator (colored bar or background): 15 mm width
- Horizontal divider lines (1 pt, #DDDDDD) between the three groups

---

## What the Manuscript Says (Direct Quotes for Context)

**Figure caption in LaTeX:**
> "Matrix showing data types on the vertical axis and agent accessibility on the horizontal axis. Green checkmarks indicate data types current agents handle well (text, SMILES, PDB files, CSV data, literature). Red X marks denote data types agents struggle with (behavioral videos, clinical score trajectories, tissue imaging, multi-modal transcriptomics, longitudinal measurements with dropout). This visualization reveals the systematic exclusion of in vivo data modalities from current agent architectures."

**Key manuscript passages:**
> "In vivo studies yield heterogeneous streams. Neurological injury evaluation includes behavioral assessments (motor coordination via beam walking, generating ordinal scores), tissue histology (cell proliferation requiring computer vision), RNA sequencing (high-dimensional gene expression needing differential expression and pathway enrichment), and clinical notes (semi-structured weight and adverse events). Current agents cannot integrate these modalities."

> "Behavioral phenotyping via DeepLabCut tracks animal poses in videos, generating time-series keypoint coordinates. Computing behavioral metrics (inter-animal distance, contact time, grooming) requires training pose estimation, validating tracking, computing features, and statistical testing. No agent executes this workflow spanning video processing, supervised learning, time-series engineering, and hypothesis testing."

> "RNA-seq requires quality control, alignment, and quantification into expression matrices. Differential expression identifies treatment effects. Pathway enrichment maps genes to biological processes via KEGG or Gene Ontology. Upstream regulator analysis infers transcription factors driving changes. The FASTQ-to-hypothesis pipeline needs bioinformatics tools (STAR, HISAT2, DESeq2, edgeR, GSEA) that agents do not integrate."

---

## What NOT to Do

- ❌ **Do not add data types not in the manuscript** — stick to the 9 items in Table 1
- ❌ **Do not use a complex multi-axis matrix** — the manuscript describes a simple accessibility categorization, not a detailed capability breakdown
- ❌ **Do not make the figure taller than 110 mm** — it needs to fit on the page with the table
- ❌ **Do not use only color to distinguish categories** — symbols (✓/◐/✗) are mandatory
- ❌ **Do not make symbols too small** — they must be visible when printed at 180 mm width
- ❌ **Do not add proprietary examples** — use only the generic use cases from the table
- ❌ **Do not forget the gradient effect** — the visual should make it obvious that most real work falls in the yellow/red zones
- ❌ **Do not use ambiguous half-fill for ◐** — the left half or top half should be clearly filled, with a crisp boundary
- ❌ **Do not crowd the layout** — white space is important for scannability

---

## Key Message Reinforcement

**The figure must make these points visually obvious:**

1. **Agents handle 4 data types well** — all text-based or highly structured (SMILES, literature, PDB, CSV)
2. **3 data types are partially accessible** — but require heavy preprocessing (imaging, time-series, semi-structured text)
3. **2 data types are completely inaccessible** — and these represent the core of in vivo validation (videos, raw sequencing)
4. **The ratio is damning** — 4 accessible vs. 5 inaccessible/partial, and the 5 represent where most drug discovery cost and risk lives

**Visual strategy:** Make the green zone look clean and organized (agents excel here). Make the yellow zone look workable but demanding. Make the red zone feel sparse and unserved (this is the gap).

---

## Accessibility Checklist

- [ ] Colorblind-safe (test with [Coblis simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/))
- [ ] Legible when printed in grayscale (symbols must be distinguishable without color)
- [ ] High-contrast text (dark text on light backgrounds throughout)
- [ ] All data types have both color AND symbol (redundant encoding)
- [ ] Symbols are bold/heavy weight for visibility
- [ ] Minimum 6.5 pt font size for smallest text
- [ ] No information conveyed by color alone

---

## Testing the Figure

After creating the figure, verify:

1. **3-second test:** Can a reader immediately see three distinct accessibility zones?
2. **5-second test:** Can they identify which zone "behavioral videos" and "RNA-seq" fall into?
3. **Scannability:** Can they quickly locate a specific data type (e.g., "PDB structures") and see its accessibility status?
4. **Message clarity:** Is it obvious that agents struggle with in vivo biological data?
5. **Grayscale test:** Print or convert to grayscale — are ✓/◐/✗ still distinguishable?
6. **Colorblind test:** Run through deuteranopia and protanopia simulators — do the three zones remain distinct?

---

## Delivery Checklist

- [ ] SVG (editable vector, all text as text objects not paths)
- [ ] High-res PNG (300 DPI, for review and manuscript submission)
- [ ] Layered source file (Figma / Illustrator / Affinity Designer with named layers)
- [ ] Grayscale version (verify all symbols are distinguishable)
- [ ] Colorblind simulation screenshots (deuteranopia, protanopia, tritanopia)
- [ ] Confirmation that data types match Table 1 exactly (9 items, no additions)

---

## Reference Style

**Target aesthetic:** Nature Reviews Drug Discovery data visualization — clean, scannable, information-dense but not cluttered. The figure should feel like a practical reference chart, not a decorative infographic.

**Comparable figures to reference:**
- Data accessibility matrices in bioinformatics papers
- Tool capability comparison charts in software papers
- Clinical trial outcome summary figures

**The core goal:** A practitioner should be able to print this figure, put it on their desk, and consult it when planning a project: "Can agents help me with this data type? Ah, no — it's in the red zone. I'll need a custom pipeline."

---

## Usage Context

This figure appears in the manuscript alongside Table 1, which provides the detailed data. The figure's role is to provide an **immediate visual understanding** of the accessibility divide. The table gives specifics; the figure gives the "at a glance" takeaway.

**Relationship to other figures:**
- **Figure 1** (Agent Reality Gap) — shows the conceptual divide between what agents do vs. what discovery needs
- **Figure 2** (Small Molecule vs. Peptide Workflows) — shows complexity contrast in computational workflows
- **Figure 3** (this figure) — shows the data type accessibility gap
- Together, they build the case that current agents have fundamental blind spots

---

*Brief version: 2.0 — 2026-02-06 — Revised to match manuscript exactly*
