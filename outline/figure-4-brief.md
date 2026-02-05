# Figure 4: From LLM-Centric to Multi-Paradigm Orchestration

**Illustrator Brief — Comprehensive & Self-Sufficient**

---

## Paper Context

This figure appears in **Gap 3: Multi-Paradigm, Not Multi-Agent** of a position paper titled *"What Drug Discovery AI Agents Still Can't Do."*

**Core argument:** Current AI agents in drug discovery are built around a **single paradigm** — LLMs orchestrating tool APIs through text. This works for literature mining and synthesis planning but breaks down when drug discovery requires **machine learning training, reinforcement learning optimization, molecular dynamics simulations, and gradient-based optimization**. The field needs multi-paradigm orchestration frameworks, not just smarter chatbots.

**Key insight:** Real drug discovery practitioners use 5+ computational paradigms in a single project:
- Supervised learning (training bioactivity predictors on assay data)
- Generative modeling (fine-tuning protein language models for peptide design)
- Reinforcement learning (reward-guided sequence optimization)
- Physics simulation (molecular dynamics, docking, pharmacokinetic modeling)
- Classical optimization (Bayesian optimization, genetic algorithms, constrained search)

Current agent architectures only support **LLM reasoning + calling pre-trained model APIs**. They cannot manage training loops, hyperparameter search, or curriculum learning.

**This figure's job:** Show the architectural limitation of current LLM-centric designs and propose an alternative: a multi-paradigm orchestrator that coordinates computational workflows as first-class primitives.

**Audience:** AI researchers building agent systems, drug discovery ML practitioners, computational biologists. Readers should immediately grasp why LLM-as-hub is limiting and what the alternative looks like.

**Placement:** Section 5 (Gap 3). This is a systems architecture diagram — technical but must remain accessible to experimentalists.

---

## Figure Specifications

### Dimensions & Format

- **Size:** 180 mm × 140 mm (full-width, vertical-stacked landscape — Nature/Science standard)
- **Resolution:** 300 DPI minimum; vector (SVG/PDF) preferred
- **Bleed:** None
- **Delivery formats:** SVG (primary), high-res PNG (review), layered source file (Figma/Illustrator/Affinity)
- **File name:** `fig4_multiparadigm_orchestration`

---

## Typography

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Figure title | Open Sans or Helvetica Neue | 12 pt | Bold | #333333 |
| Panel headers | Open Sans or Helvetica Neue | 10 pt | Bold | #333333 |
| Paradigm/node labels | Open Sans or Helvetica Neue | 8 pt | SemiBold | Node color (see below) |
| Sub-labels / descriptions | Open Sans or Helvetica Neue | 7 pt | Regular | #666666 |
| Arrow labels | Open Sans or Helvetica Neue | 6.5 pt | Regular | #888888 |
| Annotations | Open Sans or Helvetica Neue | 7 pt | Italic | #AA0000 (for "Problem" callout) |

**All text must remain editable** (not rasterized).

---

## Color Palette (Colorblind-Safe — Okabe-Ito)

| Role | Hex | Usage in This Figure |
|------|-----|---------------------|
| Charcoal | #333333 | Text, borders, arrows in top panel |
| Medium Gray | #888888 | LLM node fill (top panel), secondary text |
| Light Gray | #CCCCCC | Tool nodes (top panel), low-priority elements |
| Steel Blue | #4477AA | ML Training paradigm node (bottom panel) |
| Warm Orange | #EE6677 | RL Optimization paradigm node (bottom panel) |
| Teal | #009988 | PLM Fine-tuning paradigm node (bottom panel) |
| Purple | #AA3377 | CV Analysis paradigm node (bottom panel) |
| Gold | #CCBB44 | Physics Simulation paradigm node (bottom panel) |
| Orchestrator | #56B4E9 | Central orchestrator node (bottom panel) — light blue |
| Off-White | #F7F7F7 | General background |
| Accent Red | #AA0000 | Problem annotations (top panel only) |

**Rule:** Never rely on color alone to convey information. Patterns and labels always accompany color coding.

---

## Icon & Node Style

- **Rounded rectangles** for all nodes (corner radius: 6 px)
- **Flat design** — no gradients, no 3D, no drop shadows
- **Outlined icons inside nodes** — 2 pt stroke, consistent style
- **Arrows:** 1.5 pt stroke, single solid arrowhead (8 × 6 px)
- **Dotted lines:** 1 pt stroke with 3 px dot spacing (used for constraints/feedback)

---

## Layout

Two-tier vertical stack, same horizontal width, separated by visual divider:

```
┌─────────────────────────────────────────────────┐
│  TOP PANEL: Current LLM-Centric Architecture    │
│  (Monochrome, hub-and-spoke, bottleneck)        │
│  Height: ~60 mm                                  │
└─────────────────────────────────────────────────┘
         ║
         ║  ~10 mm vertical spacer + divider
         ║
┌─────────────────────────────────────────────────┐
│  BOTTOM PANEL: Proposed Multi-Paradigm          │
│  Orchestration (Colorful, distributed, parallel)│
│  Height: ~60 mm                                  │
└─────────────────────────────────────────────────┘
```

**Divider:** A thin dashed line (1 pt, #AAAAAA) spanning 50% of figure width, centered. Label to the right: "vs." (8 pt, italic, #666666).

---

## Top Panel — Current LLM-Centric Architecture

### Header
"Current: LLM-Centric Agent" — 10 pt, Bold, #333333. Top-left corner.

### Overall Feel
Monochrome, centralized, bottleneck. The LLM is the hub, everything goes through it. Conveys: "single point of control and single point of failure."

### Central Node — LLM
- **Position:** Center of the panel
- **Size:** 35 × 35 mm (noticeably larger than surrounding nodes)
- **Shape:** Rounded rectangle
- **Fill:** Medium Gray (#888888)
- **Border:** 2 pt, Charcoal (#333333)
- **Label:** "LLM" (10 pt, Bold, white text)
- **Sub-label:** "Text-based reasoning" (6.5 pt, white text, centered below main label)

### Surrounding Nodes — Tools (6 total)
Arranged in a radial hub-and-spoke pattern around the LLM. All nodes same size and style.

**Node specs:**
- **Size:** 22 × 18 mm each
- **Shape:** Rounded rectangle
- **Fill:** Light Gray (#CCCCCC)
- **Border:** 1.5 pt, #666666
- **Label:** 8 pt, SemiBold, Charcoal (#333333)
- **Sub-label:** 6.5 pt, Regular, #666666

**Arrangement:** Evenly spaced around LLM — approximately 60° apart in a circle (radius ~35 mm from LLM center).

| # | Position | Label | Sub-label | Tiny Icon Inside |
|---|----------|-------|-----------|-----------------|
| 1 | Top-left | Calculator | Arithmetic | Simple "Σ" symbol |
| 2 | Top | Web Search | RAG/retrieval | Magnifying glass over documents |
| 3 | Top-right | Python REPL | Code execution | Terminal prompt ">>>" |
| 4 | Bottom-right | Pre-trained Model API | Inference only | Neural network nodes (3 circles) |
| 5 | Bottom | Docking Tool | Virtual screening | Protein shape + small molecule |
| 6 | Bottom-left | Database Query | ChEMBL/PubChem | Database cylinder |

### Connections — All Go Through LLM
**Every tool node has a bidirectional arrow to/from the LLM:**
- **Arrow style:** 1.5 pt, solid, Charcoal (#333333)
- **Arrow labels:** Alternating sides to avoid overlap
  - Outbound (LLM → Tool): "request" (6.5 pt, #888888)
  - Inbound (Tool → LLM): "response" (6.5 pt, #888888)

**Critical visual:** No tool talks to any other tool. All arrows point to or from the LLM. This creates a star/hub pattern.

### Problem Annotation
A small callout (dashed red box, 1 pt stroke, #AA0000) positioned to the right of the LLM node:

**Text inside callout:**
"⚠ Problem: LLM cannot manage training loops, RL optimization, or gradient-based learning" (7 pt, italic, #AA0000)

**Arrow:** A thin red dashed line (1 pt, #AA0000) pointing from the callout to the LLM node.

### Visual Properties
- **Monochrome:** Only grays and charcoal (no color)
- **Centralized:** LLM dominates visually (largest node, center position)
- **Bottleneck:** Every information flow passes through LLM
- **Static:** No loops, no parallel paths — everything is sequential

---

## Bottom Panel — Proposed Multi-Paradigm Orchestration

### Header
"Proposed: Multi-Paradigm Orchestrator" — 10 pt, Bold, #333333. Top-left corner.

### Overall Feel
Colorful, distributed, parallel. The orchestrator coordinates but does not bottleneck. Paradigms run independently, feed results back. Conveys: "horizontal coordination, not vertical control."

### Central Node — Orchestrator
- **Position:** Horizontally centered, vertically positioned in upper third of panel
- **Size:** 40 × 22 mm (wide but not tall — suggests coordination, not dominance)
- **Shape:** Rounded rectangle
- **Fill:** Orchestrator color (#56B4E9)
- **Border:** 2 pt, #333333
- **Label:** "Multi-Paradigm Orchestrator" (9 pt, Bold, white text)
- **Sub-label:** "Workflow DAG • Resource allocation • Checkpointing" (6.5 pt, white text, centered below)

### Paradigm Nodes (5 total)
Arranged in a **horizontal row** below the orchestrator, evenly spaced. Each represents a different computational paradigm.

**Node specs:**
- **Size:** 28 × 24 mm each (larger than tools in top panel — they are first-class citizens)
- **Shape:** Rounded rectangle
- **Border:** 2 pt, Charcoal (#333333)
- **Label:** 8 pt, SemiBold, white text
- **Sub-label:** 6.5 pt, Regular, white text, centered below main label

**Spacing:** ~6 mm between nodes horizontally.

| # | Position | Label | Sub-label | Fill Color | Tiny Icon Inside |
|---|----------|-------|-----------|-----------|-----------------|
| 1 | Far left | ML Training | Dataset → Train → Validate | Steel Blue (#4477AA) | Simple neural network (3 layers, nodes connected) |
| 2 | Center-left | RL Optimization | Policy → Reward → Update | Warm Orange (#EE6677) | Circular arrow with "R" (reward) |
| 3 | Center | PLM Fine-tuning | Transfer learning | Teal (#009988) | Protein helix icon (simplified α-helix) |
| 4 | Center-right | CV Analysis | Image → Features → Insights | Purple (#AA3377) | Simplified microscope image (grid of circles) |
| 5 | Far right | Physics Simulation | MD • PK modeling | Gold (#CCBB44) | Molecule with movement arrows (dynamics) |

### Connections — Orchestrator ↔ Paradigms

**From Orchestrator to each Paradigm:**
- **Arrow style:** 1.5 pt, solid, paradigm's color
- **Direction:** Downward from orchestrator to paradigm
- **Label (above arrow):** "goals & constraints" (6.5 pt, #666666)

**From each Paradigm back to Orchestrator:**
- **Arrow style:** 1.5 pt, **dotted**, paradigm's color
- **Direction:** Upward from paradigm to orchestrator
- **Label (above arrow):** "results & metrics" (6.5 pt, #666666)

**Critical visual:** Paradigms do NOT connect to each other directly. All coordination goes through orchestrator, but orchestrator sends different instructions to different paradigms (not a bottleneck — it dispatches work in parallel).

### Inter-Paradigm Implicit Coordination
Add subtle **horizontal dashed lines** (0.75 pt, #CCCCCC) connecting adjacent paradigms at their base (below the nodes). These suggest implicit coordination through shared results, not direct communication.

**Label below these lines (centered, small):**
"Paradigms execute independently, share results via orchestrator" (6.5 pt, italic, #666666)

### Data Flow Example (Optional Annotation)
A small **workflow snippet** in a light background box (40 × 15 mm) positioned below the paradigm nodes:

**Box styling:**
- Fill: #F9F9F9
- Border: 1 pt dashed, #BBBBBB

**Content (simple workflow DAG inside box):**
```
PLM Fine-tuning → Candidate Sequences
         ↓
  ML Training (Bioactivity Predictor)
         ↓
  RL Optimization (Reward-guided refinement)
```

Tiny arrows (0.75 pt) connecting the three stages. Use paradigm colors for each node label.

**Box label (top-left inside):** "Example: Peptide Discovery Pipeline" (7 pt, italic, #666666)

### Visual Properties
- **Multi-color:** Each paradigm has its own distinct color (colorblind-safe Okabe-Ito)
- **Distributed:** Paradigms arranged horizontally — no single dominance
- **Parallel:** Visual suggestion that paradigms can run simultaneously
- **Coordinated, not controlled:** Orchestrator dispatches work but doesn't process everything

---

## Critical Visual Contrasts (The Whole Point of This Figure)

The figure's message is communicated through deliberate contrast between top and bottom panels:

| Aspect | Top Panel (LLM-Centric) | Bottom Panel (Multi-Paradigm) |
|--------|------------------------|------------------------------|
| Color scheme | Monochrome (grays only) | Multi-color (5 distinct hues) |
| Central node | Large, dominant LLM | Smaller orchestrator, coordination role |
| Surrounding nodes | Lightweight tools (inference only) | Heavy paradigms (training, optimization, simulation) |
| Connection pattern | Star/hub (everything through LLM) | Parallel dispatch + feedback |
| Bottleneck | Obvious — all arrows through LLM | None — paradigms execute independently |
| Arrow style | All solid (synchronous, sequential) | Solid outbound + dotted inbound (async, parallel) |
| Overall impression | Centralized, brittle, single-threaded | Distributed, robust, multi-threaded |

---

## Annotations & Labels

### Top Panel Annotation (Already specified above)
"⚠ Problem: LLM cannot manage training loops, RL optimization, or gradient-based learning" — red dashed callout.

### Bottom Panel Annotation (Optional)
A small checkmark (✓) in green (#009988) positioned near the orchestrator with text:
"✓ Supports ML training, RL, simulation as first-class primitives" (7 pt, #009988)

### Divider Label
Between the two panels, centered on the divider line:
"vs." (8 pt, italic, #666666)

---

## What NOT to Do

- ❌ **Do not make the orchestrator look like just a "bigger LLM"** — it should visually suggest coordination/routing, not processing. The wide-but-short shape helps convey this.
- ❌ **Do not connect paradigms directly to each other** in the bottom panel — all coordination goes through the orchestrator. The dashed horizontal lines below nodes suggest implicit sharing, not direct communication.
- ❌ **Do not use red-green as the only distinction** between any elements (colorblind safety).
- ❌ **Do not make the bottom panel look cluttered** — it should feel rich but organized. Even spacing is critical.
- ❌ **Do not use 3D effects, gradients, or drop shadows** — flat design throughout.
- ❌ **Do not rasterize any text** — all labels must remain editable.
- ❌ **Do not make the top panel look "stupid" or "broken"** — it works well for its intended use case (text-based reasoning, tool API calls). The limitation is architectural, not a failure.

---

## Accessibility Checklist

- [ ] Colorblind-safe (test with [Coblis simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/))
- [ ] Legible when printed in grayscale (top panel = grays, bottom panel = distinct shapes + labels)
- [ ] High-contrast text (white text on dark/saturated fills, dark text on light backgrounds)
- [ ] All elements have text labels (no information conveyed by color alone)
- [ ] Minimum 6.5 pt font size for smallest text (arrow labels)
- [ ] Dotted/dashed line patterns distinguishable from solid (feedback vs. dispatch)

---

## Delivery Checklist

- [ ] SVG (editable vector)
- [ ] High-res PNG (300 DPI)
- [ ] Layered source file (Figma / Illustrator / Affinity Designer)
- [ ] Grayscale version (verify legibility)
- [ ] Colorblind simulation screenshot (Deuteranopia, Protanopia, Tritanopia)
- [ ] Panel-by-panel source files (top and bottom panels as separate layers)

---

## Reference Style

**Target aesthetic:** Computer science architecture diagrams in *Nature Machine Intelligence* or *ACM Computing Surveys* — clean, technical, but accessible. Think "system architecture diagram that a biologist can understand."

**Similar figures in literature:**
- Workflow DAGs in Nextflow/Snakemake documentation (shows parallel execution)
- Microservices architecture diagrams (shows distributed coordination)
- Agent architecture diagrams from Seal et al. 2025 AI Agents survey

**This figure is NOT:**
- A flowchart (not step-by-step execution)
- A UML diagram (not software engineering pedantry)
- A data flow diagram (focus is on paradigms, not data)

**This figure IS:**
- A paradigm comparison (then vs. now, limitation vs. solution)
- An architectural proposal (what the field should build)
- A visual argument (showing why LLM-centric is limiting)

---

## Context: Why This Figure Matters

**Problem being solved:**  
Current AI agent papers showcase LLMs calling tool APIs (ChemCrow, Coscientist, ChatInvent). This creates the impression that "agentic AI" = "LLM with plugins." But real drug discovery requires training ML models on proprietary data, running RL loops for peptide optimization, fine-tuning protein language models, running molecular dynamics simulations, and performing Bayesian optimization. LLMs cannot manage these workflows because they require gradient updates, multi-step training loops, and resource allocation — not just text-based reasoning.

**What practitioners actually need:**  
A system that can coordinate a workflow like:
1. Fine-tune ProtBERT on peptide bioactivity data
2. Use the fine-tuned model to generate 1,000 candidate sequences
3. Train a multi-task predictor for stability + immunogenicity
4. Run RL optimization with a reward function balancing bioactivity + safety
5. Dock the top 50 candidates, cluster binding modes, return Pareto frontier

This workflow requires 5 different computational paradigms (PLM fine-tuning, supervised learning, RL, physics simulation, multi-objective optimization) running in sequence and in parallel. Current LLM-centric agents cannot do this.

**What this figure shows:**  
- **Top panel:** The current paradigm fails because everything must pass through the LLM, which cannot manage training loops or gradient-based optimization.
- **Bottom panel:** The proposed solution — an orchestrator that dispatches work to specialized paradigms, each running independently, coordinating through results (not by funneling everything through text).

**Reader takeaway (10 seconds):**  
"Oh, current agents are LLM-centric hub-and-spoke. That doesn't work for ML training. The proposed design has parallel paradigms coordinated by an orchestrator."

**Reader takeaway (60 seconds):**  
"I see why LLM-as-hub is limiting — it assumes text-based reasoning is sufficient. Drug discovery needs ML training, RL, simulation, and optimization as first-class operations. The orchestrator model makes sense: dispatch goals to paradigms, collect results, coordinate the workflow. This is what 'multi-paradigm orchestration' means."

---

*Brief version: 1.0 — 2026-02-05*
