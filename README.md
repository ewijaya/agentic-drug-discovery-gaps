# Beyond SMILES: Evaluating Agentic Systems for Drug Discovery

**Edward Wijaya, StemRIM, Inc.**

[![arXiv](https://img.shields.io/badge/arXiv-2602.10163-b31b1b.svg)](https://arxiv.org/abs/2602.10163)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## Abstract

Agentic systems for drug discovery have demonstrated autonomous synthesis planning, literature mining, and molecular design. We ask how well they generalize. Evaluating six frameworks against 15 task classes drawn from peptide therapeutics, in vivo pharmacology, and resource-constrained settings, we find five capability gaps: no support for protein language models or peptide-specific prediction, no bridges between in vivo and in silico data, reliance on LLM inference with no pathway to ML training or reinforcement learning, assumptions tied to large-pharma resources, and single-objective optimization that ignores safety-efficacy-stability trade-offs. A paired knowledge-probing experiment suggests the bottleneck is architectural rather than epistemic: four frontier LLMs reason about peptides at levels comparable to small molecules, yet no framework exposes this capability. We propose design requirements and a capability matrix for next-generation frameworks that function as computational partners under realistic constraints.

## Paper Structure

| Section | File | Words |
|---|---|---|
| Abstract | `00-abstract.tex` | 135 |
| Introduction | `01-introduction.tex` | 696 |
| Evaluation Framework | `02-methods.tex` | 980 |
| Capability Matrix | `03a-capability-matrix.tex` | 349 |
| Gap 1: Small-Molecule Bias | `03-gap-small-molecule.tex` | 1,369 |
| Gap 2: In Vivo-In Silico | `04-gap-invivo-insilico.tex` | 888 |
| Gap 3: Multi-Paradigm | `05-gap-multi-paradigm.tex` | 891 |
| Gap 4: Small Biotech | `06-gap-small-biotech.tex` | 848 |
| Gap 5: Multi-Objective | `07-gap-multi-objective.tex` | 877 |
| Design Requirements | `08-design-requirements.tex` | 632 |
| Discussion | `09-discussion.tex` | 624 |
| Conclusion | `10-conclusion.tex` | 211 |
| Appendix A: Task Classes | `11-appendix-a.tex` | 1,024 |
| Appendix B: Capability Matrix | `12-appendix-b.tex` | 1,073 |
| Appendix C: LLM Probing | `13-appendix-c.tex` | 526 |

**Total: ~11,100 words** (main body ~8,500 + appendices ~2,600) | 46 pages, 8 figures, 15 tables

## Frameworks Evaluated

| Framework | Organization | Primary Focus |
|---|---|---|
| ChemCrow | EPFL/Rochester | Chemistry tool orchestration |
| Coscientist | CMU | Autonomous synthesis |
| PharmAgents | Tsinghua | Target-compound interaction |
| ChatInvent | AstraZeneca | Literature-driven hypothesis |
| MADD | Multi-institutional | Multi-agent drug design |
| DiscoVerse | Roche | Discovery workflow automation |

## Repository Structure

```
├── CLAUDE.md                 # Project context for AI-assisted writing
├── README.md                 # This file
├── arxiv-submission.tar       # arXiv submission archive (monolithic main.tex + PDF figures)
├── latex/
│   ├── main.tex              # Master LaTeX file
│   ├── preamble.tex          # Packages and formatting
│   ├── references.bib        # BibTeX bibliography
│   ├── sections/             # 15 independent .tex files per section
│   └── figures/              # 8 figures (6 JPEG + 2 PDF)
├── outline/
│   ├── full-outline.md       # Complete paper outline
│   ├── illustrations.md      # Figure specifications
│   └── figure-{1..6}-brief.md
├── references/
│   └── key-papers.md         # Annotated bibliography
├── reviews/                  # Multi-perspective self-review
│   ├── 00-executive-summary.md
│   ├── 01..05-*.md           # Devil's advocate, structure, venue, technical, tone
│   ├── 06-experiment-candidates.md
│   └── REVISION-PLAN.md
├── scripts/
│   ├── generate_fig6_pareto.py
│   └── experiment2/          # LLM knowledge probing experiment
│       ├── questions.json    # 100 questions (50 matched pairs)
│       ├── run_probing.py    # Query multiple LLMs
│       ├── score_responses.py
│       ├── analyze_results.py
│       └── responses/        # Raw model outputs
└── drafts/                   # Early markdown drafts
```

## Key Contributions

1. **Capability matrix** evaluating 6 frameworks against 15 task classes across 5 dimensions
2. **LLM knowledge-probing experiment** showing the bottleneck is architectural, not epistemic
3. **Practitioner perspective** grounded in 14+ real projects, not benchmarks
4. **Peptide-specific analysis** exposing the small-molecule bias in current agents
5. **In vivo gap identification** absent from all existing surveys
6. **Design requirements** for next-generation agent architectures
7. **Small biotech lens** representing the majority of pharma companies

## Venue

Published on **arXiv** (q-bio.QM, cs.AI) on 2026-02-10. arXiv:2602.10163

## Related Work

Positions against He et al. 2026 (AstraZeneca ChatInvent), Seal et al. 2025 (AI Agents survey), and Lakhan 2025 (Cureus editorial). Builds on ChemCrow, Coscientist, PharmAgents, MADD, and DiscoVerse.

---

**License**: CC BY 4.0
**Contact**: wijaya@stemrim.com
