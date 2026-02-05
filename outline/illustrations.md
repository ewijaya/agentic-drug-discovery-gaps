This document outlines the visual elements needed to effectively communicate the gaps and opportunities in drug discovery AI agents. Each figure is designed to be publication-ready, accessible, and compelling.

---

## Figure 1: Overview/Hero Figure

Section: Introduction — The Promise vs Reality of Agentic AI in Drug Discovery

Title: The Agent Reality Gap in Drug Discovery

Description: A split-panel conceptual diagram. Left side shows what current AI agents excel at: clean computational workflows (SMILES strings, databases, literature mining, virtual screening). Right side shows what real drug discovery requires: messy biological data (animal behavior, clinical scores, imaging, longitudinal measurements), wet lab iteration, multi-objective trade-offs.

- Layout: Vertical split with connecting arrows/gaps in the middle labeled 'The Reality Gap'
- Color scheme: Cool blues/purples for computational side, warm oranges/greens for biological side, gray gap in middle
- Why compelling: Immediately visualizes the central thesis; accessible to non-experts while being technically accurate
- Creation method: BioRender or Figma (needs custom icons and scientific illustrations)
---

## Figure 2: Small Molecule vs Peptide Workflows

Section: Gap 1: The Small Molecule Bias

Title: Workflow Complexity: Small Molecules vs Peptides

Description: Side-by-side flowchart comparison. Top panel: Small molecule workflow (linear, simple) - SMILES → RDKit → Property prediction → Generation → Docking. Bottom panel: Peptide workflow (branching, complex) - Sequence → PLM embedding → Multiple parallel paths (structural prediction, aggregation propensity, stability, immunogenicity, membrane permeability, protease resistance) → Multi-endpoint integration → Design iteration.

- Layout: Horizontal alignment, small molecule on top (4-5 nodes), peptide below (15-20 nodes with branches)
- Color scheme: Single color (blue gradient) for small molecules, multi-color nodes for peptides (each property type gets a distinct hue)
- Why compelling: Visual contrast immediately shows complexity gap; validates the 'bias' claim
- Creation method: Matplotlib/NetworkX (programmatic flowchart) or Figma for polish
---

## Figure 3: The In Vivo–In Silico Gap

Section: Gap 2: The In Vivo–In Silico Bridge

Title: What Agents Can and Cannot Process

Description: Matrix-style visualization with data types on Y-axis and agent capabilities on X-axis. Green checkmarks for data types agents handle well (text, SMILES, PDB files, CSV data, literature). Red X's for data types agents struggle with (behavioral videos, clinical score trajectories, tissue imaging, multi-modal transcriptomics, longitudinal measurements with dropout).

- Layout: Grid/matrix with icons representing each data type, color-coded by accessibility
- Color scheme: Green (accessible), yellow (partial), red (inaccessible), using colorblind-friendly palette
- Why compelling: Clear, scannable visualization of concrete limitations; useful reference figure
- Creation method: Matplotlib/seaborn heatmap or Figma for custom icons
---

## Figure 4: Multi-Paradigm Architecture

Section: Gap 3: Multi-Paradigm, Not Multi-Agent

Title: From LLM-Centric to Multi-Paradigm Orchestration

Description: Two-tier comparison diagram. Top: Current LLM-centric architecture - a central LLM node with spokes to various tools (calculator, web search, Python REPL, RAG database). All arrows go through the LLM. Bottom: Proposed multi-paradigm architecture - an orchestrator coordinates different AI paradigms in parallel: ML training pipeline, RL optimization loop, PLM fine-tuning, CV analysis, physics simulation. Each runs independently with results fed back to orchestrator.

- Layout: Stacked architecture diagrams, same scale for easy comparison
- Color scheme: Monochrome (gray/black) for current, multi-color for proposed (each paradigm gets distinct color)
- Why compelling: Challenges current agent design patterns; suggests concrete alternative
- Creation method: Figma or Illustrator (needs clean architecture diagram aesthetics)
---

## Figure 5: The Resource Reality

Section: Gap 4: The Small Biotech Reality

Title: Big Pharma vs Small Biotech: The Resource Gap

Description: Infographic with two columns comparing resources. Left: Big Pharma - 10,000+ compounds, 50-person ML team, multi-GPU clusters, dedicated data engineers, months of compute budget. Right: Small Biotech - 50-200 compounds, 1-person AI team, single GPU or cloud spot instances, scientist who also codes, hours-to-days compute budget. Use icons, scale representations, and numbers.

- Layout: Side-by-side comparison with size-scaled icons (bigger team → bigger icon, etc.)
- Color scheme: Saturated colors for big pharma, muted/pale versions for small biotech
- Why compelling: Quantifies the reality most researchers face; validates resource constraints
- Creation method: Matplotlib for bar charts + Figma for icon overlay, or full Figma design
---

## Figure 6: Multi-Objective Trade-off Visualization

Section: Gap 5: Multi-Objective Navigation

Title: The Pareto Frontier Agents Ignore

Description: 3D scatter plot showing candidate compounds plotted across three axes: Efficacy (IC50), Safety (LD50 ratio), Stability (half-life). Show Pareto frontier surface with several optimal candidates highlighted. Include annotations showing real decision points: 'Lower efficacy but much safer', 'Highly effective but stability concerns', etc. Contrast with typical single-objective optimization (arrow pointing to max efficacy only).

- Layout: 3D plot with clear axis labels, Pareto surface rendered semi-transparent, candidate points as colored spheres
- Color scheme: Gradient from red (dominated) to green (Pareto-optimal), using perceptually uniform colormap
- Why compelling: Shows complexity of real decisions; visualizes what 'multi-objective' actually means
- Creation method: Matplotlib with mpl_toolkits.mplot3d (fully programmatic with real or synthetic data)
---

## Additional Visual Elements

### Inset Boxes / Callouts

> **📦** Inset 1: 'The Tuesday Morning Reality Check'

Placement: Section 2 (Introduction)

Content: Brief anecdote (anonymized) illustrating the gap between agent demos and real workflow. Example: 'An agent correctly predicted binding affinity for 50 peptides. On Tuesday morning, the wet lab reported that 40% aggregated in solution before they could even be tested. The agent had no way to know this would happen.'

Style: Light background color, italicized story text, small box (1/3 column width)

> **📦** Inset 2: 'The 3am Animal Facility Call'

Placement: Section 4 (In Vivo-In Silico Gap)

Content: Day-in-the-life scenario showing the messy reality of in vivo work. Example: 'Animal showed unexpected behavior at night. Video review required. Scoring protocol needed adjustment. Re-analysis of all prior data. Agent's tidy CSV input assumptions: shattered.'

Style: Same style as Inset 1

> **📦** Inset 3: 'The Grant Proposal Trade-off'

Placement: Section 7 (Multi-Objective Navigation)

Content: Real decision dilemma showing multi-objective trade-offs. Example: 'Compound A: 10x more potent, but LD50 margin too narrow for FDA. Compound B: Half the efficacy, but safety profile that gets past Phase I. Which does the agent recommend? (Spoiler: it optimized for potency only.)'

Style: Same style as Inset 1 & 2

---

### Additional Tables

Table 1: Agent Capability Matrix

- Rows: Task types (literature review, SMILES generation, docking, aggregation prediction, in vivo analysis, multi-objective optimization, etc.)
- Columns: Capability level (✓ Excellent, ◐ Partial, ✗ Poor/None), Requires human review (Yes/No), Typical runtime
- Purpose: Quick reference showing where agents excel and where they struggle
Table 2: Data Type Accessibility

- Columns: Data type, Format, Agent-readable (Yes/Partial/No), Processing method, Example use case
- Purpose: Detailed version of Figure 3, with specific examples and current workarounds
Table 3: Wishlist Priority Matrix

- Columns: Feature, Impact (High/Med/Low), Difficulty (High/Med/Low), Who needs it (All/Biotech/Academia), Priority score
- Rows: Features from Section 8 (Practitioner's Wishlist)
- Purpose: Actionable roadmap for agent developers
---

### Graphical Abstract

Purpose: Simplified visual summary for journal submission (typically 1-panel, high-impact)

Concept: Condensed version of Figure 1 (the hero figure). Central concept: 'The Reality Gap'. Left side: stylized icon representing current AI agents (clean, computational, text-based). Right side: stylized icon representing real drug discovery (messy, biological, multi-modal). Large gap in the middle with the 5 paper themes as bridge labels: Peptides, In Vivo, Multi-Paradigm, Resources, Multi-Objective.

Dimensions: Square format (1000x1000px at 300 DPI), works in color or grayscale

Style: Minimal, iconic, high contrast, works well as thumbnail. BioRender or Illustrator.

---

## Style & Production Guidelines

### Overall Visual Identity

- Journal aesthetic: Nature/Science style - clean, modern, uncluttered. Prioritize clarity over decoration.
- Typography: Sans-serif fonts (Arial, Helvetica, or Open Sans). Consistent sizing across all figures. Minimum 8pt for body text, 10pt for labels, 12pt for titles.
- Color palette: Colorblind-friendly throughout. Suggest: Okabe-Ito palette or Paul Tol's vibrant scheme. Test all figures with a colorblind simulator before finalizing.
- Resolution: 300 DPI minimum for all raster elements. Vector formats (SVG, PDF) preferred where possible. TIFF or high-quality PNG for final submission.
- Consistency: Use the same icon style across figures (e.g., if Figure 1 uses flat icons, all figures should use flat icons). Consistent line weights, arrow styles, and annotation conventions.
### Accessibility Checklist

- ✓ Colorblind-safe palette (avoid red-green only distinctions)
- ✓ High contrast text (black or dark gray on white/light backgrounds)
- ✓ Patterns/textures in addition to color for distinguishing categories
- ✓ Clear labels (avoid relying solely on legends when possible)
- ✓ Legible when printed in grayscale
### Production Workflow Recommendations

1. Sketches first: Rough hand sketches or wireframes before committing to design software. Get feedback early.
1. Data-driven where possible: For Figures 2, 3, and 6, generate with real or realistic synthetic data using Python (matplotlib, seaborn, NetworkX). Export as high-res PNG or SVG for touch-ups in Figma/Illustrator.
1. Design software for conceptual figures: For Figures 1, 4, and 5, use BioRender (for scientific icons), Figma (for clean layouts), or Illustrator (for precise control).
1. Iterate with co-authors: Share draft figures early and often. Non-expert feedback is valuable for clarity.
1. Final polish: Ensure all text is editable (not rasterized), all elements are aligned and properly labeled, and file formats match journal requirements.
---

### Tools & Resources

- Python libraries: matplotlib, seaborn, plotly, NetworkX, mpl_toolkits.mplot3d
- Design tools: BioRender (scientific illustrations), Figma (collaborative design), Adobe Illustrator (vector graphics)
- Color palettes: Okabe-Ito (https://jfly.uni-koeln.de/color/), Paul Tol's schemes (https://personal.sron.nl/~pault/), ColorBrewer (colorbrewer2.org)
- Accessibility testing: Coblis colorblind simulator (https://www.color-blindness.com/coblis-color-blindness-simulator/)
---

> **💡** Final Note: These figures should tell the story even if the reader skips the text. Each one must be self-contained, clearly labeled, and visually compelling. Aim for figures that get shared on Twitter/X and cited in other papers.


