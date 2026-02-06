# Devil's Advocate Review: Counter-Evidence Assessment

**Paper:** "The Blind Spots of Agentic Drug Discovery"
**Reviewer Role:** Challenge whether the 5 claimed gaps are real, using recent 2025-2026 evidence
**Date:** 2026-02-06

---

## Executive Summary

The paper identifies five blind spots in agentic drug discovery systems. After extensive searching for counter-evidence from 2025-2026, I find the paper's core thesis remains sound, but the claims need calibration. **Gaps 2 and 4 are the strongest and most defensible.** Gaps 1, 3, and 5 face moderate-to-significant counter-evidence from very recent work that the paper does not acknowledge. The paper risks being blindsided by reviewers who cite PepTune, TxGemma/Agentic-Tx, Agentomics, Medea, PepMLM, PMMG, or CheapVS. Specific recommendations for each gap follow.

---

## Gap 1: The Small Molecule Bias

### Paper's Claim
Current agents are architected around small molecules (SMILES, docking, fingerprints). No agent supports protein language model fine-tuning, peptide conformational sampling, or aggregation prediction. Peptide discovery is a fundamentally different paradigm that agents ignore.

### Counter-Evidence Found

| Paper | Date | Relevance | URL |
|---|---|---|---|
| **PepTune** (Tang et al.) | Dec 2024 / ICML 2025 | Multi-objective peptide design using masked diffusion language model + MCTS; optimizes binding affinity, solubility, permeability, hemolysis, non-fouling simultaneously | [arXiv:2412.17780](https://arxiv.org/abs/2412.17780) |
| **PepMLM** (Chatterjee et al.) | Oct 2023 / Nature Biotechnology Aug 2025 | ESM-2-based masked language model for de novo peptide binder design, experimentally validated | [Nature Biotech](https://www.nature.com/articles/s41587-025-02761-2) |
| **TxGemma / Agentic-Tx** (Google DeepMind) | Apr 2025 | Handles amino acid sequences (proteins/peptides), MHC molecules, T-cell receptors; Agentic-Tx system with 18 tools including PLM integration | [arXiv:2504.06196](https://arxiv.org/abs/2504.06196) |
| **Chai-2** (Chai Discovery) | Jun 2025 | Zero-shot antibody/nanobody/minibinder design; 16% hit rate de novo; works from sequence alone | [bioRxiv](https://www.biorxiv.org/content/10.1101/2025.07.05.663018v1) |
| **NVIDIA BioNeMo Protein Design Blueprint** | Jan 2025-2026 | AlphaFold2 + RFdiffusion + ProteinMPNN workflow for protein therapeutics including peptides | [NVIDIA Developer](https://developer.nvidia.com/blog/accelerate-protein-engineering-with-the-nvidia-bionemo-blueprint-for-generative-protein-binder-design/) |
| **Generate Biomedicines' Generative Biologics** | 2025 | Generative AI for peptides, nanobodies, antibodies with epitope specification | Industry platform |
| **LLAMP** (species-aware PLM) | 2025 | ESM-2-based model for antimicrobial peptide MIC prediction across bacterial species | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12271573/) |

### Strength of Challenge: **Moderate-to-Strong**

PepTune is the most direct counter-evidence: it is a multi-objective peptide design system that uses a protein language model (masked diffusion on sequences), performs multi-objective optimization via MCTS, and handles peptide-specific properties (permeability, hemolysis, solubility). PepMLM, published in Nature Biotechnology (Aug 2025), fine-tunes ESM-2 for peptide binder design. TxGemma/Agentic-Tx explicitly handles amino acid sequences and has an agentic wrapper.

**However**, these are standalone tools/models, not integrated agent systems. PepTune does not orchestrate full discovery workflows (data curation, training, validation, active learning). Agentic-Tx uses TxGemma for prediction but does not support fine-tuning PLMs on proprietary data. None of these address the paper's deeper claim about first-class PLM fine-tuning pipelines within an agent. The distinction between "a model that handles peptides" and "an agent that orchestrates peptide discovery workflows" is crucial but currently underarticulated in the paper.

### Does the Paper Acknowledge This?
The paper mentions TxGemma in the introduction as providing "therapeutics-focused language understanding" but does not discuss Agentic-Tx's peptide capabilities, PepTune, PepMLM, Chai-2, or BioNeMo's protein design workflows. This is a significant omission given that PepMLM was published in Nature Biotechnology and PepTune was at ICML 2025.

### Recommendation: **Soften and sharpen the claim**
The paper should:
1. Acknowledge PepTune, PepMLM, and Agentic-Tx as recent peptide-capable systems
2. Sharpen the distinction: these are peptide-aware *models* but not peptide-aware *agents* that support full workflow orchestration (fine-tuning on proprietary data, active learning, iterative design-test cycles)
3. Move from "no agent supports peptides" to "emerging peptide-capable tools exist but lack agent-level workflow integration"

---

## Gap 2: The In Vivo to In Silico Bridge

### Paper's Claim
No agent handles longitudinal in vivo data (behavioral scores, histology, RNA-seq, clinical notes over weeks-to-months). Critical validation happens in vivo, but agents are confined to in vitro automation.

### Counter-Evidence Found

| Paper | Date | Relevance | URL |
|---|---|---|---|
| **DiscoVerse** (Roche) | Nov 2025 | Multi-agent pharmaceutical co-scientist for reverse translation; traces clinical outcomes back to preclinical/animal findings across 40+ years of Roche data (15,762 PDFs) | [arXiv:2511.18259](https://arxiv.org/abs/2511.18259) |
| **Medea** (Harvard/Zitnik Lab) | Jan 2026 | Omics AI agent for therapeutic discovery; handles transcriptomics, protein networks, pathway analysis; 5,679 analyses across target identification, synthetic lethality, immunotherapy prediction | [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.01.16.696667v1) |
| **Lab-in-the-Loop** (NVIDIA/industry) | 2025-2026 | Concept of closed-loop experimental feedback, but focused on in vitro assays and lab automation, not in vivo animal studies | [NVIDIA](https://www.nvidia.com/en-us/use-cases/lab-in-the-loop-ai-for-life-science/) |
| **scAInce** review (Hartung, 2025) | 2025 | Comprehensive review of agentic lab automation; acknowledges agents orchestrate instruments and robotic systems | [Frontiers](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1649155/full) |

### Strength of Challenge: **Weak**

DiscoVerse is the closest counter-evidence: it integrates preclinical and clinical data from Roche's archives for reverse translation. However, DiscoVerse performs *literature/document mining* over existing PDFs of completed studies, not *computational modeling* of longitudinal in vivo data streams. It retrieves and cross-references toxicity findings across phases but does not train temporal models, process behavioral videos, perform differential expression analysis, or construct dose-response curves. It is a RAG system over pharmaceutical documents, not an in vivo data analysis agent.

Medea handles transcriptomics and multi-omics analysis, which partially addresses the RNA-seq gap. However, it processes static datasets, not longitudinal in vivo time-series. It does not handle behavioral phenotyping, imaging quantification, or composite efficacy metrics across timepoints.

The NVIDIA Lab-in-the-Loop paradigm is promising but focused on in vitro closed loops (flow cytometry, robotic synthesis), not in vivo animal studies which cannot be automated.

### Does the Paper Acknowledge This?
The paper cites DiscoVerse in the introduction but does not discuss its reverse-translation capabilities that partially touch in vivo data. Medea (Jan 2026) is too recent to have been cited but is directly relevant.

### Recommendation: **Well-calibrated; minor softening needed**
This is the paper's strongest gap claim. Recommendations:
1. Acknowledge DiscoVerse's reverse-translation as a step toward in vivo data integration, while noting it operates on documents rather than raw data
2. Acknowledge Medea as addressing multi-omics analysis, while noting it handles static omics rather than longitudinal in vivo data
3. The core claim (no agent processes behavioral video, longitudinal clinical scores, histology imaging, or temporal efficacy modeling) remains unchallenged

---

## Gap 3: Multi-Paradigm, Not Multi-Agent

### Paper's Claim
Current agents are LLM-centric tool callers. They cannot orchestrate ML training, RL, simulation, and optimization as first-class primitives. "Multi-agent" means multiple LLMs chatting, not multi-paradigm workflows.

### Counter-Evidence Found

| Paper | Date | Relevance | URL |
|---|---|---|---|
| **Agentomics** (BioGeMT) | Jan 2026 | Autonomous ML experimentation agent; generates state-of-the-art models for 11/20 biomedical benchmarks; handles data preprocessing, model selection, training, hyperparameter tuning, evaluation | [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.01.27.702049v1.full) |
| **Agentomics-ML** | Jun 2025 | Earlier version; autonomous ML for genomic/transcriptomic data; outperforms existing agent-based methods | [arXiv:2506.05542](https://arxiv.org/abs/2506.05542) |
| **ML-Agent** | May 2025 | RL-trained LLM agent for autonomous ML engineering; 7B model outperforms 671B DeepSeek-R1 on ML tasks; trained with step-wise RL | [arXiv:2505.23723](https://arxiv.org/abs/2505.23723) |
| **GenoMAS** | Jul 2025 | Multi-agent framework for gene expression analysis; six specialized agents for preprocessing, statistical analysis, gene identification | [arXiv:2507.21035](https://arxiv.org/abs/2507.21035) |
| **DrugGen** | 2025 | LLM + RL (proximal policy optimization) for drug-target interactions; combines language model generation with RL reward optimization | [Nature Scientific Reports](https://www.nature.com/articles/s41598-025-98629-1) |
| **Agentic RL for Chemical Language Models** | Jan 2026 | RL-based training paradigm for chemistry agents; shows tool orchestration is a learnable policy | [arXiv:2601.17687](https://arxiv.org/html/2601.17687v2) |
| **BioAgent Bench** | Jan 2026 | AI agent evaluation suite for bioinformatics; benchmarks agent capabilities across bioinformatics tasks | [arXiv:2601.21800](https://arxiv.org/html/2601.21800v1) |

### Strength of Challenge: **Moderate-to-Strong**

Agentomics is the most significant counter-evidence. It is an LLM-powered system that autonomously performs end-to-end ML experimentation: data preprocessing, feature engineering, model architecture selection, training, hyperparameter optimization, and evaluation. It achieved state-of-the-art on 11/20 biomedical benchmarks, with a 100% success rate on producing working solutions. This directly contradicts the claim that "agents cannot train models."

ML-Agent goes further by using RL to train an LLM to become an autonomous ML engineer. GenoMAS orchestrates six specialized agents for gene expression analysis workflows.

**However**, these systems orchestrate *supervised ML* workflows. None of them coordinate the full multi-paradigm stack the paper describes: concurrent RL-based peptide generation + supervised bioactivity prediction + Bayesian optimization for batch selection + structural simulation, all in a closed loop. They each handle one paradigm (ML training) rather than multi-paradigm orchestration. The paper's claim is about integrating *fundamentally different computational paradigms* within a single workflow, which remains unaddressed.

### Does the Paper Acknowledge This?
The paper does not mention Agentomics, ML-Agent, GenoMAS, BioAgent Bench, or DrugGen. Given that Agentomics (Jan 2026) and ML-Agent (May 2025) directly address autonomous ML training, this is a notable omission.

### Recommendation: **Significant reframing needed**
1. The blanket claim "agents cannot train models" is no longer accurate. Agentomics, ML-Agent, and GenoMAS demonstrate autonomous ML training capabilities
2. Reframe to: agents can now handle single-paradigm ML workflows, but multi-paradigm orchestration (coordinating ML training + RL + simulation + optimization in integrated pipelines) remains unsupported
3. Specifically acknowledge Agentomics as a significant advance while noting it handles one paradigm per run, not multi-paradigm coordination
4. Emphasize that the gap is in *integration across paradigms*, not in any single paradigm's automation

---

## Gap 4: The Small Biotech Reality

### Paper's Claim
Current agents assume large pharma contexts (millions of compounds, GPU clusters, specialized teams). Small biotechs with 50-500 sequences, single GPUs, and one-person teams are left behind. Transfer learning, few-shot adaptation, and active learning are essential but unsupported.

### Counter-Evidence Found

| Paper | Date | Relevance | URL |
|---|---|---|---|
| **BioAutoMATED** (MIT) | Jun 2023 | AutoML platform for biological sequences; specifically designed for small, sparse datasets; supports DNA, RNA, peptides | [Cell Systems](https://www.cell.com/cell-systems/fulltext/S2405-4712(23)00151-5) |
| **Boltz-2** (MIT/Recursion) | 2025 | Open-source biomolecular foundation model; 1,000x faster than traditional simulations; practical for early-stage teams | Industry announcement |
| **TuneLab** (Lilly/NVIDIA) | 2025-2026 | AI platform allowing selective access for biotech companies to train and deploy models without building full infrastructure | [NVIDIA](https://www.bio-itworld.com/news/2026/01/12/nvidia-bets-big-on-ai-driven-drug-discovery--physical-ai--and-a--1-billion-eli-lilly-partnership) |
| **Agentomics** (BioGeMT) | Jan 2026 | Costs $9.40 per 8-hour run; requires no ML expertise or programming experience; open-source | [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.01.27.702049v1.full) |
| **2026 Biotech AI Report** (Benchling) | 2026 | Reports data quality as #1 bottleneck; many AI pilots fail due to data readiness, not model capability | [Benchling](https://www.benchling.com/biotech-ai-report-2026) |

### Strength of Challenge: **Weak-to-Moderate**

BioAutoMATED is the most relevant but is from 2023 and is not an agent; it is an AutoML tool. Boltz-2 and TuneLab are platforms, not agents. Agentomics is low-cost and open-source, which partially addresses the resource constraint, but it still requires computational infrastructure and does not specifically target few-shot/transfer learning for small proprietary datasets.

Critically, **none of these systems are agentic drug discovery agents designed for small biotech constraints.** BioAutoMATED is a static tool. TuneLab requires a Lilly partnership. Boltz-2 is a foundation model. The Benchling report actually *supports* the paper's thesis by documenting that data readiness is the #1 bottleneck, confirming that small teams struggle with fragmented, incomplete data.

The paper's claims about active learning loops, few-shot adaptation, resource-aware recommendations, and batch-mode workflows for one-person teams remain largely unaddressed by any agentic system.

### Does the Paper Acknowledge This?
The paper does not mention BioAutoMATED, Boltz-2, TuneLab, or Agentomics. However, since none of these are agentic systems targeting small biotech, the omission is less critical.

### Recommendation: **Well-calibrated; minor updates**
1. This is the paper's second-strongest gap claim
2. Consider mentioning Agentomics' low cost ($9.40/run) as a step toward accessibility, while noting it does not address the core needs (few-shot, active learning, transfer learning, resource-aware recommendations)
3. The Benchling 2026 report's finding that data quality is the #1 bottleneck could be cited to strengthen the claim
4. Consider acknowledging BioAutoMATED as an AutoML tool that helps democratize ML for biology but is not an agentic system

---

## Gap 5: Multi-Objective Navigation

### Paper's Claim
Current agents optimize single metrics or weighted sums. They ignore Pareto frontiers, uncertainty quantification, sensitivity analysis, and context-dependent trade-off navigation.

### Counter-Evidence Found

| Paper | Date | Relevance | URL |
|---|---|---|---|
| **PepTune** (Tang et al.) | Dec 2024 / ICML 2025 | Multi-objective peptide design via MCTS with Pareto optimization; simultaneous optimization of 5+ properties | [arXiv:2412.17780](https://arxiv.org/abs/2412.17780) |
| **PMMG** (Liu et al.) | 2025 | Pareto MCTS molecular generation; 51.65% success on 7 simultaneous objectives; 2.5x SOTA | [Advanced Science](https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/advs.202410640) |
| **Mothra** | 2024 | Multi-objective de novo molecular generation via MCTS with Pareto frontiers | [JCIM](https://pubs.acs.org/doi/10.1021/acs.jcim.4c00759) |
| **CheapVS** (Dang et al.) | Mar 2025 | Human-centered preferential multi-objective Bayesian optimization; chemists guide trade-offs via pairwise comparison | [arXiv:2503.16841](https://arxiv.org/abs/2503.16841) |
| **DrugEx v2/v3** | 2021-2023 | Pareto-based multi-objective RL for de novo drug design; PRCD and PRTD distance metrics for Pareto frontier diversity | [J Cheminform](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-021-00561-9) |
| **MOSWO** | 2025 | Multi-objective spider-wasp optimizer for drug design trade-offs | [MDPI](https://www.mdpi.com/2313-7673/10/4/219) |

### Strength of Challenge: **Moderate**

PMMG and PepTune provide strong evidence that multi-objective optimization with Pareto frontiers is being actively developed for molecular/peptide design. PMMG achieves 51.65% success on 7 simultaneous objectives. CheapVS specifically addresses the human-in-the-loop trade-off navigation the paper calls for.

**However**, these are standalone optimization algorithms, not integrated into agentic workflows. An agent would need to (1) identify that multi-objective optimization is appropriate, (2) select and configure the optimizer, (3) present Pareto frontiers interactively, (4) incorporate uncertainty quantification, (5) support sensitivity analysis, and (6) adapt to development stage. None of the counter-evidence achieves this full integration.

Moreover, CheapVS is the closest to the paper's vision of interactive trade-off navigation but is limited to virtual screening with fixed objectives. It does not handle the dynamic, context-dependent multi-objective reasoning the paper describes (e.g., "choose A if dosing can be tightly controlled, choose B for robustness").

### Does the Paper Acknowledge This?
The paper does not mention PepTune, PMMG, Mothra, CheapVS, or MOSWO. DrugEx is not cited. This is a notable omission, especially for PMMG and CheapVS which were published in 2025.

### Recommendation: **Sharpen the distinction**
1. Acknowledge that multi-objective optimization methods exist (PMMG, DrugEx, Mothra) and are increasingly sophisticated
2. Acknowledge CheapVS as the closest system to human-in-the-loop trade-off navigation
3. Reframe the gap: the issue is not that multi-objective optimization does not exist, but that it is not integrated into agent workflows with uncertainty quantification, sensitivity analysis, stage-adaptive recommendations, and interactive decision support
4. The paper currently implies no multi-objective tools exist; this is inaccurate and should be corrected

---

## Overall Assessment

### Ranked by Defensibility (strongest to weakest):

1. **Gap 2 (In Vivo-In Silico Bridge)** - Strongest claim. No counter-evidence addresses longitudinal in vivo data modeling, behavioral phenotyping, or temporal efficacy prediction within agents. DiscoVerse and Medea are tangential.

2. **Gap 4 (Small Biotech Reality)** - Strong claim. No agentic system specifically targets small biotech constraints. The broader industry confirms data readiness as the top bottleneck.

3. **Gap 3 (Multi-Paradigm)** - Needs significant reframing. Autonomous ML training agents now exist (Agentomics, ML-Agent). The gap should be repositioned as multi-paradigm *integration* rather than single-paradigm automation.

4. **Gap 5 (Multi-Objective)** - Needs sharpening. Multi-objective Pareto optimization tools are mature. The real gap is their integration into agent workflows with uncertainty and interactive decision support.

5. **Gap 1 (Small Molecule Bias)** - Needs most revision. PepTune, PepMLM, TxGemma, Chai-2, and BioNeMo show substantial investment in peptide/protein-aware AI. The gap should focus on workflow orchestration for peptide discovery rather than the absence of peptide-aware tools.

### Cross-Cutting Recommendations

1. **Add a "Recent Advances" acknowledgment** to each gap section, noting emerging work that partially addresses the gap before explaining what remains missing. This strengthens credibility and preempts reviewer objections.

2. **Sharpen the tool-vs-agent distinction throughout.** The paper conflates "no tool exists" with "no agent integrates this." Many relevant tools exist; the gap is in agentic workflow integration. Making this distinction explicit would make the paper more precise and harder to challenge.

3. **Update the references.** The paper cites nothing from mid-2025 onward. Key omissions:
   - PepTune (ICML 2025)
   - PepMLM (Nature Biotechnology, Aug 2025)
   - Agentomics (bioRxiv, Jan 2026)
   - Medea (bioRxiv, Jan 2026)
   - GenoMAS (arXiv, Jul 2025)
   - ML-Agent (arXiv, May 2025)
   - CheapVS (ICLR 2025 Workshop)
   - PMMG (Advanced Science, 2025)
   - Agentic-Tx details from TxGemma paper

4. **Reposition the thesis slightly.** Instead of "agents have blind spots" (which implies no one is working on them), consider "agents have blind spots that emerging tools are beginning to address, but integrated workflow-level solutions remain absent." This is more defensible and more nuanced.

5. **The paper's strongest differentiator is the practitioner perspective.** No counter-evidence comes from someone who has actually tried to use these tools in a small biotech peptide discovery context. This experiential authority should be emphasized more.
