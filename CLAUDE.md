# CLAUDE.md - Project Context for AI Assistants

## Project Overview

This repository contains a **position paper** titled:

**"Beyond SMILES: Evaluating Agentic Systems for Drug Discovery"**

Published on arXiv: [2602.10163](https://arxiv.org/abs/2602.10163) (q-bio.QM, cs.AI)

46 pages, 8 figures, 15 tables, ~11,100 words

## Author

**Edward Wijaya** - A computational scientist at a small Japanese biopharma company (~50 employees) specializing in regenerative medicine through therapeutic peptides. He has led 14+ AI-driven drug discovery projects spanning ML, generative AI, reinforcement learning, protein language models, computer vision, and bioinformatics. He is both the drug designer and the AI practitioner - a rare combination that gives this paper its unique authority.

## Core Thesis

Current agentic AI systems for drug discovery are built for **small-molecule, target-based workflows at large pharma**. They fail to address five critical blind spots:

1. **The Small Molecule Bias** - Peptide drug discovery has fundamentally different requirements (sequence-based, PLMs, different SAR logic)
2. **The In Vivo-In Silico Bridge** - No agent can handle longitudinal animal model data, behavioral phenotyping, or imaging
3. **Multi-Paradigm, Not Multi-Agent** - Real drug discovery needs RL, PLMs, computer vision, classical ML orchestrated together, not just multiple LLMs chatting
4. **The Small Biotech Reality** - Tiny datasets, limited compute, one-person AI teams
5. **Multi-Objective Trade-offs** - Safety vs efficacy vs stability, not single-metric optimization

## ⚠️ CRITICAL CONSTRAINTS - READ CAREFULLY

### What MUST NOT be revealed:
- **Company name** (never write "StemRIM" or any identifiable company info)
- **Specific peptide names or sequences** (no TRIM2, TRIM3, TRIM4, TRIM5, SRA-9, Redasemtide)
- **Internal dataset details** (no specific assay results, bioactivity numbers, compound counts)
- **Proprietary model names** (no Seq2Risk, PEM, LEMUR by name)
- **Specific receptor targets** (no LRP1 by name in connection to the author's work)
- **Colleague names** (no Tamai, no internal team references)

### How to write about internal experience:
Write at the **problem-class level**, not the solution level.

| ❌ Never write this | ✅ Write this instead |
|---|---|
| "At StemRIM, we developed a PEM score for TBI peptides" | "Practitioners developing composite efficacy metrics for longitudinal in vivo data find no agent support for temporal modeling" |
| "Our ESM-2 model maps peptides to LRP1 receptor subtypes" | "Peptide-receptor interaction prediction requires protein language models, which no current agent integrates" |
| "GRPO optimization of ProtGPT2 for our therapeutic targets" | "RL-based peptide generation demands reward functions grounded in multi-endpoint efficacy" |
| "The 8-fold safety gap between SR-A9 and TRIM4" | "Safety-efficacy trade-offs in therapeutic peptides require agents capable of multi-objective reasoning" |
| "We used DeepLabCut to quantify mouse togetherness" | "Behavioral phenotyping from video data remains entirely outside the scope of current AI agents" |

### Author positioning:
- "A practitioner who has led 14+ AI-driven drug discovery projects at a small biotech"
- "Working across ML, generative AI, RL, protein language models, computer vision, and bioinformatics"
- "Specializing in therapeutic peptide development for regenerative medicine"
- Never claim to represent the company's views

## The 14 Project Categories (Anonymized)

These are the real projects that inform each gap. Reference them by category, never by internal name:

1. **ML bioactivity prediction** - Multi-endpoint regression (proliferation, migration, secretion, toxicity) using XGBoost/SVM with 2000+ peptide features
2. **Generative peptide design** - ProtBERT/ProtGPT2 fine-tuning with transfer learning for conditional peptide generation
3. **Binding site analysis** - Peptide-receptor docking, clustering by binding region, bioactivity correlation
4. **In vivo TBI recovery modeling** - Longitudinal clinical scores (foot slip test), temporal efficacy signatures, response classification
5. **Peptide-enzyme stability** - Modeling protease interactions, designing degradation-resistant modifications
6. **PLM-based receptor prediction** - ESM-2 for multi-class receptor type classification from peptide sequences
7. **MCMH optimization** - Monte Carlo Metropolis-Hastings for peptide landscape exploration, balancing exploitation/exploration
8. **RNA-seq / scRNA-seq analysis** - Differential expression, pseudotime trajectory, immune cell profiling
9. **Bone formation quantification** - Digital tomosynthesis image processing, automated ROI detection, gap filling metrics
10. **Immune response profiling** - Pathway enrichment, upstream regulator analysis, inflammatory scoring
11. **Functional annotation** - GO/KEGG annotation, gene network construction
12. **Behavioral phenotyping** - DeepLabCut pose estimation for social bonding quantification in animal models
13. **In vivo-in vitro bridging** - Composite efficacy metrics correlating in vitro bioactivity with long-term in vivo outcomes
14. **RL for peptide generation** - GRPO variants with curriculum learning, diversity-aware rewards, KL regularization
15. **Safety/toxicology modeling** - GLMM dose-response, multi-objective safety-efficacy trade-off analysis

## Strategic Positioning

This paper is NOT a rejoinder ("you're wrong"). It is a **complementary counterpoint**: "you showed us what you built; here's what you're not seeing."

The tone is: **"The field is exciting and moving fast, but there are five blind spots that nobody is talking about, and I know because I've been trying to use these approaches in a setting very different from AstraZeneca's."**

Think of it as the **field correction** that practitioners read and say "finally, someone said it." That's what makes position papers get cited: they articulate what everyone feels but nobody has written down.

| Paper | Their message | Our response |
|---|---|---|
| He et al. (AZ) | "Here's our working agent at big pharma" | "Great, but it only works in your context" |
| Seal et al. | "Here's everything that exists in the field" | "You cataloged the tools but missed the gaps" |
| Lakhan | "Biopharma must embrace agentic AI" | "Agreed, but current agents aren't ready for most of us" |

## Key Competing Papers

Position this paper AGAINST these three:

### 1. He et al. (Drug Discovery Today, Jan 2026)
"Democratising real-world drug discovery through agentic AI"
- AstraZeneca authors describing their ChatInvent system
- A **case study** of what they built, not a gap analysis
- Our angle: They show what exists at big pharma. We show what's MISSING for everyone else.

### 2. Seal et al. (arXiv, Oct 2025)
"AI Agents in Drug Discovery"
- 20-author comprehensive technical survey (45 pages, 12 figures)
- Maps the **landscape** of AI agents
- Our angle: They catalog what exists. We identify what doesn't work yet.

### 3. Lakhan (Cureus, May 2025)
"The Agentic Era: Why Biopharma Must Embrace AI That Acts"
- Single-author editorial, relatively surface-level
- High-level cheerleading about agentic AI potential
- Our angle: We go deeper with concrete practitioner evidence.

### Other papers to reference:
- ChemCrow (2023) - First major chemistry LLM agent, 18 tools
- Coscientist (2023) - Autonomous chemical research agent
- PharmAgents (March 2025) - Virtual pharma multi-agent system
- ChemToolAgent (2024-2025) - Chemistry tool benchmark
- MADD (Nov 2025) - Multi-agent drug discovery
- DiscoVerse (Nov 2025) - Roche's pharmaceutical co-scientist
- TxGemma (2025) - Google's therapeutics LLM
- BioPlanner (2023) - Protocol planning benchmark

## Writing Style

- **Tone:** Authoritative but accessible. Not academic-dry, not blog-casual. Think Nature perspective piece.
- **Voice:** First-person plural ("we") or first-person singular ("I") for practitioner anecdotes
- **Formatting:** No emdashes. Use commas, semicolons, or separate sentences instead.
- **Avoid:** Jargon without explanation, unsupported claims, revealing proprietary details
- **Include:** Concrete examples (anonymized), clear problem statements, actionable recommendations
- **Each section should have:** A clear gap statement, evidence from the field, practitioner insight, and what needs to change

## Repository Structure

```
agentic-drug-discovery-gaps/
├── CLAUDE.md                    # This file - project context
├── README.md                    # Project overview + abstract
├── arxiv-submission.tar         # arXiv submission archive (monolithic main.tex + PDF figures)
├── latex/
│   ├── main.tex                 # Master LaTeX file
│   ├── preamble.tex             # Packages and formatting
│   ├── references.bib           # BibTeX bibliography
│   ├── sections/                # 15 independent .tex files per section
│   └── figures/                 # 8 figures (6 JPEG + 2 PDF)
├── outline/
│   ├── full-outline.md          # Complete section-by-section outline
│   └── illustrations.md         # Figure and visual asset specifications
├── references/
│   └── key-papers.md            # Bibliography of papers to cite
├── reviews/                     # Multi-perspective self-review
├── scripts/
│   ├── generate_fig6_pareto.py
│   └── experiment2/             # LLM knowledge probing experiment
├── drafts/                      # Early markdown drafts
└── figures/                     # Legacy figure drafts
```

## Editing the Paper

1. Edit sections in `latex/sections/*.tex`
2. Compile with `cd latex && pdflatex main && bibtex main && pdflatex main && pdflatex main`
3. For arXiv resubmission: create uncompressed `.tar` with all figures as PDF

## Notion Pages (for reference)

- Outline: https://www.notion.so/2feff8341a0381079afefc4c1c468d1a
- Illustrations: https://www.notion.so/2feff834-1a03-8156-886d-c3b3da8dad0d
- Paper Ideas: https://www.notion.so/2feff8341a03810dbf12dcc613c00160
