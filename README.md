# Beyond SMILES: Evaluating Agentic AI for Drug Discovery

**Edward Wijaya, StemRIM, Inc.**

## Abstract

Agentic AI systems have advanced drug discovery automation, with frameworks such as ChatInvent, Coscientist, and ChemCrow demonstrating autonomous synthesis planning, literature mining, and molecular design. However, no systematic evaluation of these frameworks against real-world drug discovery requirements beyond small-molecule, target-based workflows has been conducted. We evaluate six agentic AI frameworks against 15 task classes spanning peptide discovery, in vivo modeling, and resource-constrained settings across five evaluation dimensions: molecular representation coverage, computational paradigm support, data modality integration, resource assumptions, and optimization framework. Our analysis reveals five critical capability gaps:

1. **Small-molecule representation bias** excluding protein language models and peptide-specific prediction
2. **Absent in vivo-in silico bridges** for longitudinal, multi-modal animal data
3. **Limited computational paradigm support** excluding ML training, reinforcement learning, and multi-paradigm coordination
4. **Resource assumptions mismatched** to small biotech realities
5. **Single-objective optimization** ignoring multi-objective trade-offs in safety, efficacy, and stability

From these gaps, we derive design requirements for next-generation frameworks and provide a capability matrix with concrete use cases to guide development toward computational partners that augment practitioner judgment under realistic constraints.

## Paper Structure

| Section | File | Words |
|---|---|---|
| Abstract | `00-abstract.tex` | 171 |
| Introduction | `01-introduction.tex` | 732 |
| Evaluation Framework | `02-methods.tex` | 852 |
| Capability Matrix | `03a-capability-matrix.tex` | 546 |
| Gap 1: Small-Molecule Bias | `03-gap-small-molecule.tex` | 1,025 |
| Gap 2: In Vivo-In Silico | `04-gap-invivo-insilico.tex` | 1,036 |
| Gap 3: Multi-Paradigm | `05-gap-multi-paradigm.tex` | 1,018 |
| Gap 4: Small Biotech | `06-gap-small-biotech.tex` | 949 |
| Gap 5: Multi-Objective | `07-gap-multi-objective.tex` | 974 |
| Design Requirements | `08-design-requirements.tex` | 706 |
| Discussion | `09-discussion.tex` | 552 |
| Conclusion | `10-conclusion.tex` | 180 |
| Appendix A: Task Classes | `11-appendix-a.tex` | 1,256 |
| Appendix B: Capability Matrix | `12-appendix-b.tex` | 1,315 |

**Total: ~11,300 words** (main body ~8,700 + appendices ~2,600)

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
├── latex/
│   ├── main.tex              # Master LaTeX file
│   ├── preamble.tex          # Packages and formatting
│   ├── references.bib        # BibTeX bibliography
│   ├── sections/             # 14 independent .tex files per section
│   └── figures/              # 6 figures (JPEG + SVG)
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
2. **Practitioner perspective** grounded in 14+ real projects, not benchmarks
3. **Peptide-specific analysis** exposing the small-molecule bias in current agents
4. **In vivo gap identification** absent from all existing surveys
5. **Design requirements** for next-generation agent architectures
6. **Small biotech lens** representing the majority of pharma companies

## Target Venues

- **arXiv cs.AI** (primary)
- **Drug Discovery Today** (perspectives)
- **Nature Machine Intelligence** (perspective piece)

## Related Work

Positions against He et al. 2026 (AstraZeneca ChatInvent), Seal et al. 2025 (AI Agents survey), and Lakhan 2025 (Cureus editorial). Builds on ChemCrow, Coscientist, PharmAgents, MADD, and DiscoVerse.

---

**License**: CC BY 4.0
**Contact**: wijaya@stemrim.com
