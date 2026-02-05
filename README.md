# The Blind Spots of Agentic Drug Discovery

**A position paper identifying five critical blind spots in current agentic AI systems for drug discovery**

## Author
Edward Wijaya, StemRIM, Inc.

## Status
📝 Draft complete (Feb 2026)

## Abstract

Agentic AI systems like ChatInvent and Coscientist demonstrate impressive capabilities but reveal systematic blind spots when applied beyond small-molecule workflows at well-resourced pharmaceutical companies. Drawing on experience leading 14+ AI-driven drug discovery projects at a small biotech specializing in therapeutic peptides, this perspective identifies five critical blind spots:

1. **The Small Molecule Bias** — Peptide discovery requires protein language models and sequence-based design, not SMILES and retrosynthesis
2. **The In Vivo to In Silico Bridge** — No agent handles longitudinal animal data, behavioral phenotyping, or multi-modal biological imaging
3. **Multi-Paradigm, Not Multi-Agent** — Real workflows need RL, PLMs, computer vision, and classical ML orchestrated together, not multiple LLMs chatting
4. **The Small Biotech Reality** — Tiny datasets, limited compute, one-person AI teams
5. **Multi-Objective Navigation** — Safety vs efficacy vs stability trade-offs, not single-metric optimization

We propose five design principles for next-generation agents: multi-paradigm orchestration, modality-aware architectures, in vivo integration, data-efficient learning, and multi-objective optimization with uncertainty quantification.

## Target Venues
- **arXiv cs.AI** (primary)
- **Drug Discovery Today** (perspectives)
- **Nature Machine Intelligence** (perspective piece)

## Word Count
~6,300 words (target: 6,000-8,000)

## Repository Structure

```
├── CLAUDE.md              # Project context for AI-assisted writing
├── README.md              # This file
├── outline/
│   ├── full-outline.md    # Complete paper outline
│   └── illustrations.md   # Figure and visual asset specifications
├── references/
│   └── key-papers.md      # Bibliography
├── latex/
│   ├── main.tex           # Master LaTeX file
│   ├── preamble.tex       # Packages and formatting
│   ├── references.bib     # BibTeX bibliography
│   ├── sections/          # Independent .tex files per section
│   └── figures/           # Generated figures
├── drafts/                # Markdown drafts
└── figures/               # Source figures
```

## Key Contributions

1. **Practitioner perspective** grounded in 14+ real projects, not benchmarks
2. **Peptide-specific analysis** exposing the small-molecule bias in current agents
3. **In vivo gap identification** absent from all existing surveys
4. **Actionable design principles** for next-generation agent architectures
5. **Small biotech lens** representing the majority of pharma companies

## Timeline

- **Feb 2026**: Outline + draft complete ✓
- **Mar 2026**: Revision and figure generation
- **Apr 2026**: Internal review + submission to arXiv

## Related Work

Positions against He et al. 2026 (AstraZeneca ChatInvent), Seal et al. 2025 (AI Agents survey), and Lakhan 2025 (Cureus editorial). Builds on ChemCrow, Coscientist, PharmAgents, and MADD.

---

**License**: CC BY 4.0  
**Contact**: wijaya@stemrim.com
