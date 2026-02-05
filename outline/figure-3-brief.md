# Figure 3: What Agents Can and Cannot Process

**Illustrator Brief — Comprehensive & Self-Sufficient**

---

## Paper Context

This figure supports **Gap 2: The In Vivo–In Silico Bridge** in a position paper titled *"What Drug Discovery AI Agents Still Can't Do."*

**The argument:** Current AI agents excel at processing clean, structured, text-based data (SMILES strings, CSV tables, literature PDFs). They struggle or fail entirely with messy biological data that dominates real drug discovery: behavioral videos, clinical score trajectories with dropout, tissue imaging, multi-modal omics, and longitudinal measurements. This gap prevents agents from bridging in vitro predictions to in vivo reality.

**What this figure must communicate in 5 seconds:** There's a stark divide between data types agents can process (green checkmarks) and data types that define real drug discovery but remain inaccessible to agents (red X's).

**Audience:** AI researchers, drug discovery scientists, biotech practitioners. This figure is a practical reference — readers should be able to glance at it and immediately understand what's feasible vs. what's not.

**Placement:** Section 4 (Gap 2: The In Vivo–In Silico Bridge). This is the second "evidence" figure, illustrating the concrete limitations of current agent architectures.

---

## Figure Specifications

### Dimensions & Format

- **Size:** 180 mm × 135 mm (full-width, portrait orientation — taller to accommodate the matrix)
- **Resolution:** 300 DPI minimum; vector (SVG/PDF) preferred
- **Bleed:** None
- **Delivery formats:** SVG (primary), high-res PNG (review), layered source file
- **File name:** `fig3_data_accessibility`

---

## Typography

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Figure title | Open Sans or Helvetica Neue | 12 pt | Bold | #333333 |
| Matrix title | Open Sans or Helvetica Neue | 10 pt | SemiBold | #555555 |
| Row labels (Y-axis) | Open Sans or Helvetica Neue | 8 pt | Regular | #333333 |
| Row sublabels | Open Sans or Helvetica Neue | 6.5 pt | Regular | #777777 |
| Column headers (X-axis) | Open Sans or Helvetica Neue | 8 pt | SemiBold | #333333 |
| Column subheaders | Open Sans or Helvetica Neue | 6.5 pt | Regular | #777777 |
| Icons (✓/◐/✗) | 16 pt symbol font or vector | — | — | See color palette |
| Legend text | Open Sans or Helvetica Neue | 7 pt | Regular | #555555 |
| Annotation text | Open Sans or Helvetica Neue | 7 pt | Italic | #999999 |

**All text must remain editable** (not rasterized).

---

## Color Palette (Colorblind-Safe — Okabe-Ito derived)

| Role | Hex | Symbol | Usage |
|------|-----|--------|-------|
| Accessible (High) | #228833 | ✓ | Agent can process this data type natively with high reliability |
| Partial (Medium) | #CCBB44 | ◐ | Agent can process with significant preprocessing or human curation |
| Inaccessible (Low/None) | #EE6677 | ✗ | Agent cannot meaningfully process this data type |
| Neutral Background | #F7F7F7 | — | General background |
| Grid Lines | #DDDDDD | — | Matrix cell borders |
| Charcoal | #333333 | — | Text, labels |
| Medium Gray | #888888 | — | Secondary text |

**Additional Design Rule:**
- Each cell has BOTH a color fill and an icon symbol
- Color-only or icon-only would fail accessibility — both are required
- Pattern fills (optional): Accessible = solid, Partial = diagonal stripes, Inaccessible = crosshatch (use if colorblind testing shows ambiguity)

---

## Icon Style

- **Symbols:** ✓ (checkmark), ◐ (half-filled circle), ✗ (X mark)
- **Size:** 14–16 pt or vector equivalent (approx 5 mm tall)
- **Weight:** Bold/heavy stroke weight for visibility
- **Color:** Symbols inherit the cell's color (darker than fill)
  - Accessible cell: #228833 fill → #1A6626 symbol
  - Partial cell: #CCBB44 fill → #998822 symbol
  - Inaccessible cell: #EE6677 fill → #CC4455 symbol
- **Alignment:** Centered in each matrix cell

---

## Layout

Matrix/grid visualization with:
- **Rows (Y-axis):** 12 data types commonly encountered in drug discovery
- **Columns (X-axis):** 4 agent capability dimensions
- **Cells:** 12 rows × 4 columns = 48 cells total

### Matrix Structure

```
┌─────────────────────────────────────────────────────────────────────┐
│  Figure Title: "What Agents Can and Cannot Process"                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│                    ┌──────┬──────┬──────┬──────┐                    │
│                    │ Col1 │ Col2 │ Col3 │ Col4 │  (Column headers)  │
│                    ├──────┼──────┼──────┼──────┤                    │
│  Row 1 (label)     │  ✓   │  ✓   │  ✗   │  ◐   │                    │
│  Row 2 (label)     │  ✓   │  ◐   │  ✗   │  ✗   │                    │
│  Row 3 (label)     │  ◐   │  ✗   │  ✗   │  ✗   │                    │
│     ...            │ ...  │ ...  │ ...  │ ...  │                    │
│  Row 12 (label)    │  ✗   │  ✗   │  ✗   │  ◐   │                    │
│                    └──────┴──────┴──────┴──────┘                    │
│                                                                     │
│  [Legend: ✓ Accessible, ◐ Partial, ✗ Inaccessible]                 │
│  [Annotation: Summary insight]                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Column Definitions (X-Axis)

Four capability dimensions representing what agents need to do with data:

| # | Column Header | Subheader | Description |
|---|--------------|-----------|-------------|
| 1 | Native Parsing | Direct ingestion | Can the agent read/parse this data format without custom preprocessing? |
| 2 | Semantic Understanding | Reasoning over content | Can the agent extract meaning, identify patterns, or make inferences? |
| 3 | Temporal Integration | Longitudinal analysis | Can the agent model change over time, handle dropout, or infer trajectories? |
| 4 | Multi-Modal Fusion | Cross-modality synthesis | Can the agent integrate this data type with other modalities? |

**Visual layout:**
- Column width: ~40 mm each
- Column headers: Bold 8 pt, left-aligned within each column
- Subheaders: Regular 6.5 pt, left-aligned, medium gray (#777777)
- 2 mm padding inside each column header cell

---

## Row Definitions (Y-Axis)

Twelve data types, arranged from "most accessible" (top) to "least accessible" (bottom). This ordering creates a visual gradient of accessibility.

| # | Row Label | Sublabel | Description (for context — not shown in figure) |
|---|-----------|----------|------------------------------------------------|
| 1 | Text Literature | PubMed, patents, reviews | Structured text documents — LLM native format |
| 2 | SMILES Strings | Chemical notation | Text-based molecular representation |
| 3 | CSV/Tabular Data | Assay results, databases | Structured numerical data |
| 4 | PDB Files | Protein structures | Standardized 3D structure format |
| 5 | FASTA Sequences | Amino acid, nucleic acid | Text-based sequence data |
| 6 | Microscopy Images | Cell cultures, histology | 2D spatial images — requires computer vision |
| 7 | Clinical Scores | Ordinal, subjective ratings | Longitudinal ordinal data with human judgment |
| 8 | RNA-Seq Count Matrices | High-dimensional transcriptomics | Thousands of features, sparsity, batch effects |
| 9 | Behavioral Videos | Animal phenotyping | Unstructured video requiring pose estimation |
| 10 | Tissue Imaging (Spatial) | Multi-channel microscopy | 3D/4D imaging with spatial transcriptomics |
| 11 | Longitudinal In Vivo Trajectories | Time-series with dropout | Recovery curves, missing data, variability |
| 12 | Multi-Modal Omics | RNA-seq + proteomics + metabolomics | Integration across measurement platforms |

**Visual layout:**
- Row height: ~9 mm each (enough for label + sublabel + some breathing room)
- Row labels: Regular 8 pt, left-aligned, 2 mm padding
- Sublabels: Regular 6.5 pt, left-aligned, medium gray (#777777), directly below main label

---

## Cell Content — The Matrix Values

Each of the 48 cells (12 rows × 4 columns) contains:
1. A **fill color** (green, yellow, or red tint)
2. A **symbol** (✓, ◐, or ✗)

### Row 1: Text Literature

| Column | Native Parsing | Semantic Understanding | Temporal Integration | Multi-Modal Fusion |
|--------|---------------|----------------------|---------------------|-------------------|
| Value | ✓ Accessible | ✓ Accessible | ◐ Partial | ◐ Partial |
| Rationale | PDF/HTML parsing is mature | LLMs excel at text reasoning | Timeline extraction is partial | Can reference but not deeply integrate with non-text |

### Row 2: SMILES Strings

| Column | Native Parsing | Semantic Understanding | Temporal Integration | Multi-Modal Fusion |
|--------|---------------|----------------------|---------------------|-------------------|
| Value | ✓ Accessible | ✓ Accessible | ✗ Inaccessible | ◐ Partial |
| Rationale | Standard text format | Cheminformatics tools integrated | No temporal dimension | Can combine with docking/assays but not biology |

### Row 3: CSV/Tabular Data

| Column | Native Parsing | Semantic Understanding | Temporal Integration | Multi-Modal Fusion |
|--------|---------------|----------------------|---------------------|-------------------|
| Value | ✓ Accessible | ◐ Partial | ◐ Partial | ◐ Partial |
| Rationale | Trivial to parse | Depends on column semantics; agents guess | Time columns exist but modeling limited | Can merge tables but struggles with heterogeneity |

### Row 4: PDB Files

| Column | Native Parsing | Semantic Understanding | Temporal Integration | Multi-Modal Fusion |
|--------|---------------|----------------------|---------------------|-------------------|
| Value | ✓ Accessible | ◐ Partial | ✗ Inaccessible | ◐ Partial |
| Rationale | Standard format, parsers exist | 3D geometry yes, biology insight limited | Structural dynamics ignored | Can combine with sequences/docking |

### Row 5: FASTA Sequences

| Column | Native Parsing | Semantic Understanding | Temporal Integration | Multi-Modal Fusion |
|--------|---------------|----------------------|---------------------|-------------------|
| Value | ✓ Accessible | ✓ Accessible | ✗ Inaccessible | ◐ Partial |
| Rationale | Simple text format | PLMs provide embeddings | No time dimension | Combines with structures/assays moderately |

### Row 6: Microscopy Images

| Column | Native Parsing | Semantic Understanding | Temporal Integration | Multi-Modal Fusion |
|--------|---------------|----------------------|---------------------|-------------------|
| Value | ◐ Partial | ◐ Partial | ✗ Inaccessible | ✗ Inaccessible |
| Rationale | Image formats parsable but need CV pipelines | Basic detection yes, biological interpretation limited | No temporal modeling out-of-box | Hard to integrate with omics/scores |

### Row 7: Clinical Scores

| Column | Native Parsing | Semantic Understanding | Temporal Integration | Multi-Modal Fusion |
|--------|---------------|----------------------|---------------------|-------------------|
| Value | ◐ Partial | ✗ Inaccessible | ✗ Inaccessible | ✗ Inaccessible |
| Rationale | Can read tables but ordinal semantics lost | Treats as numbers, misses clinical meaning | No longitudinal modeling | Requires domain knowledge to merge with biomarkers |

### Row 8: RNA-Seq Count Matrices

| Column | Native Parsing | Semantic Understanding | Temporal Integration | Multi-Modal Fusion |
|--------|---------------|----------------------|---------------------|-------------------|
| Value | ◐ Partial | ✗ Inaccessible | ✗ Inaccessible | ✗ Inaccessible |
| Rationale | CSV-like but huge/sparse; needs normalization | No pathway understanding without specialized tools | No time-series modeling | Integration with proteomics/metabolomics beyond agents |

### Row 9: Behavioral Videos

| Column | Native Parsing | Semantic Understanding | Temporal Integration | Multi-Modal Fusion |
|--------|---------------|----------------------|---------------------|-------------------|
| Value | ✗ Inaccessible | ✗ Inaccessible | ✗ Inaccessible | ✗ Inaccessible |
| Rationale | Requires DeepLabCut or equivalent; not agent territory | Pose → behavior inference needs domain models | Temporal dynamics exist but not agent-accessible | Isolated from other data modalities |

### Row 10: Tissue Imaging (Spatial)

| Column | Native Parsing | Semantic Understanding | Temporal Integration | Multi-Modal Fusion |
|--------|---------------|----------------------|---------------------|-------------------|
| Value | ✗ Inaccessible | ✗ Inaccessible | ✗ Inaccessible | ✗ Inaccessible |
| Rationale | Multi-channel 3D/4D imaging requires specialized pipelines | Morphology + spatial transcriptomics = expert domain | Time-lapse requires tracking | Cross-modal with clinical data nearly impossible |

### Row 11: Longitudinal In Vivo Trajectories

| Column | Native Parsing | Semantic Understanding | Temporal Integration | Multi-Modal Fusion |
|--------|---------------|----------------------|---------------------|-------------------|
| Value | ◐ Partial | ✗ Inaccessible | ✗ Inaccessible | ✗ Inaccessible |
| Rationale | Can read time-series CSVs but dropout/variability breaks assumptions | Causal inference not supported | No temporal state-space models | Cannot link recovery curves to molecular data |

### Row 12: Multi-Modal Omics

| Column | Native Parsing | Semantic Understanding | Temporal Integration | Multi-Modal Fusion |
|--------|---------------|----------------------|---------------------|-------------------|
| Value | ✗ Inaccessible | ✗ Inaccessible | ✗ Inaccessible | ✗ Inaccessible |
| Rationale | Each modality = separate preprocessing pipeline | No cross-modality reasoning frameworks | Temporal multi-omics = research frontier | Integration is the entire challenge |

---

## Summary — The Accessibility Pattern

Looking at the matrix as a whole:

| Data Type Category | Accessibility Level | Percentage of Cells |
|-------------------|---------------------|-------------------|
| Text/Structured (Rows 1-5) | Mostly ✓ Accessible or ◐ Partial | ~70% green or yellow |
| Biological/Complex (Rows 6-12) | Mostly ✗ Inaccessible | ~75% red |

**Visual gradient:** The matrix should show a clear color shift from top (green-dominant) to bottom (red-dominant).

---

## Legend

Small legend box positioned **bottom-left** of the figure (approx 50 × 20 mm):

**Title:** "Agent Capability" — 7 pt, SemiBold

| Symbol | Color Swatch | Label | Description |
|--------|-------------|-------|-------------|
| ✓ | Green dot (#228833) | Accessible | Native support, high reliability |
| ◐ | Yellow dot (#CCBB44) | Partial | Requires preprocessing, limited reliability |
| ✗ | Red dot (#EE6677) | Inaccessible | No meaningful processing capability |

Each swatch is a small filled square (5 × 5 mm) followed by the symbol and label in 7 pt Regular.

---

## Annotation (Below the Matrix)

A single-sentence summary positioned **centered below the matrix**, 7 pt italic, #999999:

"Current agents handle text and structured formats well but cannot process the messy biological data that dominates in vivo drug discovery."

Or alternative:

"The accessibility divide: 5 data types agents excel at vs 7 data types that define real biology."

---

## Visual Details — Cell Appearance

Each cell in the matrix:

| Element | Specification |
|---------|--------------|
| Cell width | ~40 mm (matches column width) |
| Cell height | ~9 mm (matches row height) |
| Border | 1 pt, #DDDDDD (light gray grid lines) |
| Fill | Color tint: #228833 (20% opacity), #CCBB44 (25% opacity), or #EE6677 (20% opacity) |
| Symbol | Centered, 14-16 pt, darker shade of the fill color |
| Padding | 1 mm internal padding |

**Color fill guidelines:**
- Use tints, not saturated colors — cells should feel readable, not overpowering
- Accessible: Very light green (#E8F5E9 or similar)
- Partial: Very light yellow (#FFFBEA or similar)
- Inaccessible: Very light red/pink (#FDECEA or similar)

**Symbol weights:**
- ✓: Bold/heavy checkmark, not thin
- ◐: Half-filled circle (left or top half filled), clear boundary
- ✗: Bold X with balanced stroke weight

---

## Axis Labels

### Y-Axis (Left side)
- **Main label:** "Data Types in Drug Discovery" — 8 pt, SemiBold, rotated 90° counterclockwise
- Position: Centered vertically along the left edge of the matrix

### X-Axis (Top)
- **Main label:** "Agent Capabilities" — 8 pt, SemiBold
- Position: Centered horizontally above the column headers

---

## Alternative Accessibility Enhancement (Optional)

If colorblind testing reveals ambiguity, add **pattern fills** to cells:

| Accessibility | Pattern |
|--------------|---------|
| ✓ Accessible | Solid fill (no pattern) |
| ◐ Partial | Diagonal stripe pattern (45° lines, 1 pt, spaced 2 mm) |
| ✗ Inaccessible | Crosshatch pattern (both 45° and -45° lines) |

Pattern color should match the symbol color (darker than fill).

---

## What NOT to Do

- ❌ **Do not make the matrix too small to read** — each cell needs enough space for the symbol and a light background. If 48 cells don't fit legibly in 180 × 135 mm, adjust row/column counts (prioritize readability).
- ❌ **Do not use red-green as the only distinction** — symbols (✓/◐/✗) are mandatory. Color + symbol together = accessible.
- ❌ **Do not use ambiguous symbols** — ✓ must clearly be a checkmark, ✗ must clearly be an X, ◐ must clearly be half-filled.
- ❌ **Do not vary symbol sizes within the matrix** — all checkmarks same size, all X's same size. Consistency is critical for scannability.
- ❌ **Do not make the grid lines too prominent** — they should structure the matrix, not dominate it. 1 pt light gray (#DDDDDD) is sufficient.
- ❌ **Do not fill cells with 100% saturated colors** — use light tints (20-25% opacity) so symbols remain visible and text is legible.
- ❌ **Do not add extra columns or rows beyond the specified 4 × 12** — the matrix is intentionally compact to be scannable. More dimensions = less clarity.
- ❌ **Do not forget row sublabels** — "Clinical Scores" alone is ambiguous; "Ordinal, subjective ratings" clarifies.

---

## Spatial Precision — Cell Alignment

All cells must be:
- **Perfectly aligned** — no offset rows or columns
- **Equal cell dimensions within rows/columns** — no irregular sizing
- **Grid lines continuous** — no gaps or overlaps in borders

Use alignment tools in vector software (Figma/Illustrator) to ensure pixel-perfect grid structure.

---

## Accessibility Checklist

- [ ] Colorblind-safe (test with [Coblis simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/))
- [ ] Legible when printed in grayscale (symbols distinguishable even without color)
- [ ] High-contrast text (dark text on light backgrounds)
- [ ] All symbols use bold/heavy strokes for visibility
- [ ] Legend clearly explains the three categories
- [ ] Minimum 6.5 pt font size for sublabels
- [ ] No information conveyed by color alone

---

## Testing the Figure — Key Questions

After creating the figure, verify:

1. **5-second test:** Can a reader immediately see the green-to-red gradient from top to bottom?
2. **Scannability:** Can a reader quickly locate a specific data type (e.g., "Behavioral Videos") and see its accessibility profile across all 4 columns?
3. **Message clarity:** Is it obvious that agents struggle with biological/in vivo data?
4. **Grayscale test:** Print or convert to grayscale — are the three categories (✓/◐/✗) still distinguishable?
5. **Colorblind test:** Run through deuteranopia and protanopia simulators — do green and red remain distinct?

---

## Delivery Checklist

- [ ] SVG (editable vector, all text as text objects not paths)
- [ ] High-res PNG (300 DPI, for review)
- [ ] Layered source file (Figma / Illustrator / Affinity Designer with named layers)
- [ ] Grayscale version (verify all symbols/patterns are distinguishable)
- [ ] Colorblind simulation screenshots (deuteranopia, protanopia, tritanopia)
- [ ] Confirmation that all cells are perfectly aligned (no gaps or misalignments)

---

## Reference Style

**Target aesthetic:** Nature Reviews data visualization — clean, scannable, information-dense but not cluttered. The matrix should feel like a practical reference chart, not a decorative infographic.

Inspiration: Gene expression heatmaps, clinical trial outcome tables, accessibility matrices in HCI papers.

**The core message:** This figure is a tool for practitioners. A scientist should be able to glance at it during a project and think: "Can agents help me with this data type? Ah, no — it's in the red zone. I'll need a custom pipeline."

---

## Usage Note for Practitioners

This figure is designed to be **cited and reused**. When the paper is published, this matrix should become a reference chart that researchers bookmark and share. Prioritize:
- Clarity over cleverness
- Scannability over aesthetics
- Practical utility over visual polish

If a scientist can print this figure, tape it to their lab wall, and consult it weekly — it's working.

---

*Brief version: 1.0 — 2026-02-05*
