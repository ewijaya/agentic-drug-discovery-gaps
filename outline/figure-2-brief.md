# Figure 2: Workflow Complexity — Small Molecules vs Peptides

**Illustrator Brief — Comprehensive & Self-Sufficient**

---

## Paper Context

This figure supports **Gap 1: The Small Molecule Bias** in a position paper titled *"What Drug Discovery AI Agents Still Can't Do."*

**The argument:** Current AI agents in drug discovery are designed around small-molecule workflows — linear pipelines using SMILES strings, molecular fingerprints, and docking scores. Peptide drug discovery is fundamentally different: it requires protein language models, multiple parallel property assessments, and iterative redesign cycles. The visual contrast between the two workflows validates the claim that current agents are biased toward one modality.

**What this figure must communicate in 5 seconds:** Small-molecule discovery is a short straight road. Peptide discovery is a branching highway with loops. Current AI agents only know how to drive the straight road.

**Audience:** AI researchers, drug discovery scientists, biotech practitioners.

**Placement:** Section 3 (Gap 1: The Small Molecule Bias). This is the first "evidence" figure after the hero figure.

---

## Figure Specifications

### Dimensions & Format

- **Size:** 180 mm × 120 mm (full-width, landscape)
- **Resolution:** 300 DPI minimum; vector (SVG/PDF) preferred
- **Bleed:** None
- **Delivery formats:** SVG (primary), high-res PNG (review), layered source file
- **File name:** `fig2_workflow_complexity`

---

## Typography

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Figure title | Open Sans or Helvetica Neue | 12 pt | Bold | #333333 |
| Panel headers | Open Sans or Helvetica Neue | 10 pt | SemiBold | Panel color |
| Node labels | Open Sans or Helvetica Neue | 8 pt | SemiBold | #333333 |
| Node sublabels | Open Sans or Helvetica Neue | 7 pt | Regular | #777777 |
| Annotation text | Open Sans or Helvetica Neue | 7 pt | Italic | #999999 |
| Legend text | Open Sans or Helvetica Neue | 7 pt | Regular | #555555 |

**All text must remain editable** (not rasterized).

---

## Color Palette (Colorblind-Safe — Okabe-Ito derived)

| Role | Hex | Usage |
|------|-----|-------|
| Steel Blue | #4477AA | Small molecule workflow (all nodes, single color family) |
| Light Blue fill | #D6E4F0 | Small molecule node fills |
| Warm Orange | #EE6677 | Peptide workflow header |
| Branch A — Structural | #4477AA | AlphaFold / structural prediction |
| Branch B — Aggregation | #EE6677 | Aggregation propensity |
| Branch C — Stability | #228833 | Protease stability |
| Branch D — Immunogenicity | #CCBB44 | Immunogenicity risk |
| Branch E — Permeability | #AA3377 | Membrane permeability |
| Branch F — Resistance | #66CCEE | Protease resistance |
| Integration node | #F0F0F0 | Multi-endpoint integration (neutral gray) |
| Iteration arrow | #EE6677 | Feedback loop (dashed) |
| Charcoal | #333333 | Text, borders |

**Rule:** Never rely on color alone. Each branch also has a distinct icon inside its node.

---

## Icon & Shape Style

- **Flat, outlined icons** — 2 pt stroke, no gradients, no 3D
- Rounded corners on all node rectangles (4 px radius)
- Consistent icon style across both panels
- Arrow style: 1.5 pt stroke, pointed arrowheads, #555555

---

## Layout

Two horizontal flowcharts stacked vertically. The visual size difference between them IS the message.

```
┌──────────────────────────────────────────────────────────────┐
│  TOP PANEL: Small Molecule Workflow                          │
│  ~30% of figure height                                       │
│                                                              │
│  [Node] → [Node] → [Node] → [Node] → [Node]                │
│  Simple. Linear. Done.                                       │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│  Thin divider with annotation                                │
├──────────────────────────────────────────────────────────────┤
│  BOTTOM PANEL: Peptide Workflow                              │
│  ~70% of figure height                                       │
│                                                              │
│                    ┌→ [Branch A]──┐                          │
│                    ├→ [Branch B]──┤                          │
│  [Input] → [PLM] ─┼→ [Branch C]──┼→ [Integration] → [Iter] │
│                    ├→ [Branch D]──┤         ↑                │
│                    ├→ [Branch E]──┤         │                │
│                    └→ [Branch F]──┘    ◄────┘ (feedback)     │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## Top Panel — Small Molecule Discovery Workflow

### Header
"Small Molecule Discovery" — 10 pt, SemiBold, Steel Blue (#4477AA)

### Flow Direction
Left to right, single linear path, 5 nodes.

### Nodes (in order)

| # | Node Label | Sublabel | Icon Inside Node |
|---|-----------|----------|-----------------|
| 1 | SMILES Input | Text-based notation | Monospace text snippet: "CC(=O)Oc..." inside a code-box shape |
| 2 | Molecular Descriptors | RDKit fingerprints | A small grid/matrix pattern (suggesting a fingerprint bit vector) |
| 3 | Property Prediction | LogP, solubility, tox | A simple line chart trending upward |
| 4 | Generative Design | de novo candidates | A molecule icon with a small sparkle/star (generation) |
| 5 | Docking & Ranking | Score-based selection | A lock-and-key icon (ligand fitting into receptor pocket) |

### Node Appearance
- **Shape:** Rounded rectangle, approx 28 × 20 mm each
- **Fill:** Light blue (#D6E4F0), slightly darker left-to-right gradient optional (lightest at node 1, slightly deeper at node 5)
- **Border:** 1.5 pt, Steel Blue (#4477AA)
- **All 5 nodes: same size, same shape, same color family**

### Connections
- Straight horizontal arrows between nodes (1.5 pt, #555555, pointed arrowheads)
- Equal spacing between all nodes
- No branching, no loops, no alternate paths

### Annotation Below the Flow
"Linear · 1 representation (SMILES) · 1 toolchain · No iteration" — 7 pt, italic, #999999

Positioned centered below the 5 nodes.

---

## Divider

A thin horizontal line (1 pt, #DDDDDD) separating the two panels, with a small centered label:

"Compare the complexity ▼" — 8 pt, SemiBold, #AAAAAA

Or simply a blank 5 mm gap with a subtle dashed line.

---

## Bottom Panel — Peptide Discovery Workflow

### Header
"Peptide Discovery" — 10 pt, SemiBold, Warm Orange (#EE6677)

### Flow Direction
Left to right, with a major fan-out (parallel branches) in the middle and a fan-in (convergence) before the final stage.

### Stage 1 — Input (Single Node)

| Node Label | Sublabel | Icon |
|-----------|----------|------|
| Amino Acid Sequence | MKTLLF... (example) | Monospace letter sequence in a code-box, similar style to SMILES node above but with amino acid letters |

- **Shape:** Rounded rectangle, 30 × 22 mm
- **Fill:** Light gray (#F5F5F5)
- **Border:** 1.5 pt, #888888

### Stage 2 — Embedding (Single Node)

| Node Label | Sublabel | Icon |
|-----------|----------|------|
| PLM Embedding | ESM-2 / ProtBERT | A neural network icon — 3 layers of connected dots (simplified) |

- **Shape:** Rounded rectangle, 32 × 22 mm
- **Fill:** Light gray (#F0F0F0)
- **Border:** 1.5 pt, #888888
- Connected from Stage 1 by a single horizontal arrow

### Stage 3 — Parallel Analysis Branches (6 Branches)

From the PLM Embedding node, **6 arrows fan out** — spreading vertically to connect to 6 parallel branch nodes. The fan should look like a tree branching or river delta.

Each branch is its own node with a distinct color and icon:

| Branch | Label | Sublabel | Color (fill / border) | Icon Inside |
|--------|-------|----------|-----------------------|-------------|
| A | Structural Prediction | AlphaFold, homology | #D6E4F0 / #4477AA | Simplified protein ribbon (helix + sheet) |
| B | Aggregation Propensity | Self-assembly risk | #F8D7DA / #EE6677 | 3–4 circles clustering together |
| C | Protease Stability | Enzymatic degradation | #D4EDDA / #228833 | Scissors icon cutting a chain |
| D | Immunogenicity Risk | Immune response | #FFF3CD / #CCBB44 | Shield with exclamation mark |
| E | Membrane Permeability | Cellular uptake | #E8D5E8 / #AA3377 | Simple cell membrane cross-section (lipid bilayer with arrow passing through) |
| F | Protease Resistance | Design for stability | #D4F0F0 / #66CCEE | Chain link with a small lock |

**Each branch node:**
- **Shape:** Rounded rectangle, approx 24 × 16 mm (smaller than Stage 1/2 nodes)
- **Fill:** Light tint of its designated color
- **Border:** 1.5 pt, saturated version of its color
- **Icon:** Small (10 × 10 mm), positioned left of the label text inside the node

**Vertical arrangement:**
- 6 branches stacked vertically with ~3 mm spacing between them
- Branch A at top, Branch F at bottom
- All left edges aligned vertically
- Fan-out arrows from PLM Embedding connect to the left edge of each branch

### Stage 4 — Integration (Single Node)

| Node Label | Sublabel | Icon |
|-----------|----------|------|
| Multi-Endpoint Integration | Combine all results | Overlapping squares or a merge/funnel icon — multiple inputs converging into one |

- **Shape:** Rounded rectangle, **larger** than other nodes — 36 × 22 mm
- **Fill:** Light gray (#F0F0F0)
- **Border:** 2 pt, #888888
- **6 arrows converge** from all branch nodes into this single node (fan-in)
- This is the visual bottleneck — 6 paths merging into 1

### Stage 5 — Iteration (Single Node + Feedback Loop)

| Node Label | Sublabel | Icon |
|-----------|----------|------|
| Design Iteration | Optimize & redesign | Circular arrow icon (cycle/refresh symbol) |

- **Shape:** Rounded rectangle, 30 × 22 mm
- **Fill:** Light warm (#FFF3E8)
- **Border:** 1.5 pt, Warm Orange (#EE6677)
- Connected from Integration node by a forward arrow

**Feedback loop arrow:**
- A **dashed curved arrow** (2 pt, #EE6677, dashed) from the Iteration node **looping back** to Stage 1 (Amino Acid Sequence)
- The arrow should arc below or above the entire workflow, clearly showing the cycle
- This feedback loop is critical — it shows that peptide discovery is iterative, not one-shot
- Label on the feedback arrow: "Redesign cycle" — 7 pt, italic, #EE6677

### Annotation Below the Flow
"Branching · 6+ property types · Multiple toolchains · Iterative redesign" — 7 pt, italic, #999999

Positioned centered below the bottom panel.

---

## Node Count Contrast (The Core Message)

This is the single most important visual takeaway:

| Metric | Small Molecule (Top) | Peptide (Bottom) |
|--------|---------------------|-------------------|
| Total nodes | 5 | 10+ (input + PLM + 6 branches + integration + iteration) |
| Parallel paths | 0 | 6 |
| Feedback loops | 0 | 1 (explicit redesign cycle) |
| Color variety | 1 color family (blue) | 6+ colors (one per branch) |
| Visual height | ~25 mm of flow | ~70 mm of flow |

The size ratio between the two panels should make a reader think: "Oh. That's why current agents can't handle peptides."

---

## Legend

Small color legend in the **bottom-right corner** of the figure (approx 35 × 30 mm):

**Title:** "Peptide Property Branches" — 7 pt, SemiBold

| Color Swatch | Label |
|-------------|-------|
| #4477AA dot | Structural |
| #EE6677 dot | Aggregation |
| #228833 dot | Stability |
| #CCBB44 dot | Immunogenicity |
| #AA3377 dot | Permeability |
| #66CCEE dot | Resistance |

Each swatch is a small filled circle (4 mm diameter) followed by the label in 7 pt Regular.

---

## Spatial Relationships — Detailed

Here is a more precise spatial map of the bottom panel flow:

```
                                          ┌──────────────────┐
                                          │  A: Structural   │──┐
                                          │  Prediction      │  │
                                          └──────────────────┘  │
                                          ┌──────────────────┐  │
                                          │  B: Aggregation  │──┤
                                          │  Propensity      │  │
┌──────────────┐    ┌──────────────┐      └──────────────────┘  │    ┌──────────────────┐    ┌──────────────┐
│ Amino Acid   │───→│    PLM       │──┬──→┌──────────────────┐  ├──→│  Multi-Endpoint   │───→│   Design     │
│ Sequence     │    │  Embedding   │  │   │  C: Protease     │──┤   │  Integration      │    │  Iteration   │
└──────────────┘    └──────────────┘  │   │  Stability       │  │   └──────────────────┘    └──────┬───────┘
       ▲                              │   └──────────────────┘  │                                  │
       │                              │   ┌──────────────────┐  │                                  │
       │                              ├──→│  D: Immunogenicity│──┤                                  │
       │                              │   │  Risk            │  │                                  │
       │                              │   └──────────────────┘  │                                  │
       │                              │   ┌──────────────────┐  │                                  │
       │                              ├──→│  E: Membrane     │──┤                                  │
       │                              │   │  Permeability    │  │                                  │
       │                              │   └──────────────────┘  │                                  │
       │                              │   ┌──────────────────┐  │                                  │
       │                              └──→│  F: Protease     │──┘                                  │
       │                                  │  Resistance      │                                     │
       │                                  └──────────────────┘                                     │
       │                                                                                           │
       └───────────────────── (dashed feedback loop) ──────────────────────────────────────────────┘
```

---

## What NOT to Do

- ❌ **Do not make the bottom panel look "worse" or "inferior"** — it should look richer and more demanding, not broken or ugly. Peptide discovery is harder, not worse.
- ❌ **Do not compress the bottom panel to match the top panel's simplicity** — the size difference IS the message. Let the bottom panel breathe and fill its 70% of the figure height.
- ❌ **Do not use generic node shapes for the branches** — each of the 6 branches must have a distinct small icon suggesting its specific domain (scissors for protease, shield for immunogenicity, etc.).
- ❌ **Do not forget the feedback loop arrow** — the dashed curve from Iteration back to Input. Iteration is a fundamental difference between small-molecule (one-shot) and peptide (cyclic) workflows.
- ❌ **Do not use only color to distinguish branches** — each branch has both a unique color AND a unique icon. The figure must work in grayscale.
- ❌ **Do not make arrows overlap or tangle** — even though the bottom panel is complex, the arrow paths should be traceable. Use clean fan-out and fan-in patterns.
- ❌ **Do not add more than 6 branches** — the current 6 are the key peptide-specific property types. More would be clutter.

---

## Accessibility Checklist

- [ ] Colorblind-safe (test with [Coblis simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/))
- [ ] Legible when printed in grayscale (each branch distinguishable by icon + label, not just color)
- [ ] High-contrast text (dark text on light backgrounds)
- [ ] All nodes have text labels (no unlabeled shapes)
- [ ] Minimum 7 pt font size for smallest text
- [ ] Arrow paths are traceable without ambiguity

---

## Delivery Checklist

- [ ] SVG (editable vector)
- [ ] High-res PNG (300 DPI)
- [ ] Layered source file (Figma / Illustrator / Affinity Designer)
- [ ] Grayscale version (verify each branch is distinguishable)
- [ ] Colorblind simulation screenshot

---

## Reference Style

**Target aesthetic:** Nature Reviews / Science perspective figures. Clean, modern, uncluttered. The top panel should feel almost boring in its simplicity. The bottom panel should feel substantial and demanding — but still organized and readable.

The contrast between "boring simple" and "organized complex" is the entire message.

---

*Brief version: 1.0 — 2026-02-05*
