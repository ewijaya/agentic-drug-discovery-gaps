# New Bibliography Entries for Revision

**Created:** 2026-02-06
**Purpose:** Verified BibTeX entries for 7 papers needed by REVISION-PLAN.md (MF-02, MF-03, MF-04, SF-07)

---

## bib-researcher-2 Results

### 1. ML-Agent (mlagent2025)

```bibtex
@article{mlagent2025,
  title     = {{ML-Agent}: Reinforcing {LLM} Agents for Autonomous Machine Learning Engineering},
  author    = {Liu, Zexi and Chai, Jingyi and Zhu, Xinyu and Tang, Shuo and Ye, Rui and Zhang, Bo and Bai, Lei and Chen, Siheng},
  year      = {2025},
  journal   = {arXiv preprint arXiv:2505.23723},
  doi       = {10.48550/arXiv.2505.23723},
  note      = {Introduces a framework where LLM agents learn autonomous ML engineering through online RL with exploration-enriched fine-tuning, step-wise RL, and ML-specific reward modules. A 7B model trained on 9 tasks outperforms 671B DeepSeek-R1 agent.}
}
```

**Claim verification:** The expected topic "Uses RL to train autonomous ML engineers" is **accurate**. The paper proposes using online reinforcement learning to train LLM agents for autonomous machine learning engineering, featuring exploration-enriched fine-tuning, step-wise RL training, and an agentic ML-specific reward module.

---

### 2. PMMG (pmmg2025)

```bibtex
@article{pmmg2025,
  title     = {A Multi-Objective Molecular Generation Method Based on {Pareto} Algorithm and {Monte Carlo} Tree Search},
  author    = {Liu, Yifei and Zhu, Yiheng and Wang, Jike and Hu, Renling and Shen, Chao and Qu, Wanglin and Wang, Gaoang and Su, Qun and Zhu, Yuchen and Kang, Yu and Pan, Peichen and Hsieh, Chang-Yu and Hou, Tingjun},
  year      = {2025},
  journal   = {Advanced Science},
  volume    = {12},
  number    = {20},
  pages     = {2410640},
  doi       = {10.1002/advs.202410640},
  note      = {Proposes PMMG, which uses MCTS guided by Pareto optimality to generate molecules satisfying multiple simultaneous drug objectives. Achieves 51.65\% success rate on 7 simultaneous objectives (EGFR inhibition, solubility, permeability, metabolic stability, toxicity, QED, SAScore), outperforming baselines by 2.5x.}
}
```

**Claim verification:** The claim "PMMG achieves 51.65% success on 7 simultaneous objectives via Pareto MCTS" is **CONFIRMED**. The paper explicitly reports a 51.65% success rate when optimizing seven objectives simultaneously (EGFR inhibition, solubility, permeability, metabolic stability, toxicity, QED, and SAScore), far exceeding other baselines by 2.5 times. Published in Advanced Science, volume 12, issue 20, 2025.

---

### 3. CheapVS (cheapvs2025)

```bibtex
@article{cheapvs2025,
  title     = {Preferential Multi-Objective {Bayesian} Optimization for Drug Discovery},
  author    = {Dang, Tai and Pham, Long-Hung and Truong, Sang T. and Glenn, Ari and Nguyen, Wendy and Pham, Edward A. and Glenn, Jeffrey S. and Koyejo, Sanmi and Luong, Thang},
  year      = {2025},
  journal   = {arXiv preprint arXiv:2503.16841},
  doi       = {10.48550/arXiv.2503.16841},
  note      = {Introduces CheapVS, a human-guided framework combining preference learning with multi-objective Bayesian optimization for virtual screening. Allows chemists to express trade-off preferences via pairwise comparisons. Recovers up to 16/37 EGFR and 37/58 DRD2 known drugs while screening only 6\% of the library.}
}
```

**Claim verification:** The expected topic "Human-guided multi-objective Bayesian optimization" is **accurate**. CheapVS combines preferential multi-objective Bayesian optimization with docking models, allowing chemists to guide ligand selection through pairwise comparison preferences. The paper was submitted to ICML and is available on arXiv (2503.16841, March 2025).

---

## bib-researcher-3 Results

### 1. Medea (medea2026)

```bibtex
@article{medea2026,
  title     = {Medea: An Omics {AI} Agent for Therapeutic Discovery},
  author    = {Sui, Pengwei and Li, Michelle M. and Gao, Shanghua and Shen, Wanxiang and Giunchiglia, Valentina and Shen, Andrew and Huang, Yepeng and Kong, Zhenglun and Zitnik, Marinka},
  year      = {2026},
  journal   = {bioRxiv},
  doi       = {10.64898/2026.01.16.696667},
  note      = {Introduces Medea, an omics AI agent with four modules (planning, execution, literature reasoning, consensus) and 20 tools spanning single-cell/bulk transcriptomics, protein interaction networks, pathway knowledge bases, and cancer vulnerability maps. Evaluated across 5,679 analyses in target identification, synthetic lethality, and immunotherapy response prediction, improving over baselines by up to 46\%.}
}
```

**Claim verification:**

1. **"Medea handles transcriptomics, protein networks, and pathway analysis"** -- **CONFIRMED.** Medea uses 20 tools that span single-cell and bulk transcriptomic datasets, protein-protein interaction analysis (via HumanBase PPI tools), and pathway knowledge bases (WikiPathways, Reactome, MSigDB Hallmark, Gene Ontology). It also integrates single-cell foundation models (PINNACLE, TranscriptFormer) and gene enrichment analysis (Enrichr). The claim is accurate.

2. **"It processes static datasets rather than longitudinal in vivo time-series"** -- **CONFIRMED.** Medea works with static omics datasets (single-cell RNA-seq, bulk transcriptomics, DepMap genetic dependency data, clinical mutation profiles). There is no mention of longitudinal data, temporal dynamics, or time-series analysis anywhere in the paper or codebase. It analyzes snapshots of omics data, not temporal progressions.

3. **"It does not integrate behavioral phenotyping, imaging, or temporal efficacy modeling"** -- **CONFIRMED.** Medea is exclusively focused on molecular-level omics data. Its 20 tools cover transcriptomics, protein interactions, pathway enrichment, gene ontology, and literature search. There is no support for behavioral data (e.g., animal model phenotyping), imaging modalities, or temporal efficacy tracking. These modalities are entirely outside its scope.

**Summary of what Medea actually does:**

Medea (from Marinka Zitnik's lab at Harvard Medical School) is an omics AI agent that takes a biological research objective and executes transparent, multi-step analyses using a suite of 20 specialized tools. It comprises four modules: (1) research planning that specifies biological context and verifies plan integrity, (2) code execution with pre-run validation and post-run checks, (3) literature reasoning that retrieves and screens papers for contextual relevance, and (4) a consensus module that reconciles evidence from tool outputs, literature, and the underlying language model (or abstains when evidence is insufficient). It was evaluated on 5,679 analyses across three therapeutic discovery domains: target identification for five diseases (2,400 analyses), synthetic lethality reasoning in seven cancer cell lines (2,385 analyses), and immunotherapy response prediction in bladder cancer (894 patient analyses). It improved over existing approaches by up to 46%, 22%, and 24% respectively. Notably, Medea focuses on molecular omics (transcriptomics, protein networks, pathways) and does not handle in vivo longitudinal data, behavioral phenotyping, imaging, or temporal efficacy modeling, making it a good example of how even state-of-the-art agents address only a subset of the drug discovery pipeline.

---

## bib-researcher-1 Results

### 1. PepTune (peptune2024)

```bibtex
@inproceedings{peptune2024,
  title     = {{PepTune}: De Novo Generation of Therapeutic Peptides with Multi-Objective-Guided Discrete Diffusion},
  author    = {Tang, Sophia and Zhang, Yinuo and Chatterjee, Pranam},
  year      = {2025},
  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
  series    = {Proceedings of Machine Learning Research},
  volume    = {267},
  publisher = {PMLR},
  url       = {https://arxiv.org/abs/2412.17780},
  note      = {Introduces a masked discrete language model (MDLM) trained on 11M peptide SMILES with Monte Carlo Tree Search (MCTS)-guided multi-objective sampling for therapeutic peptide generation. Optimizes across target binding affinity, membrane permeability, solubility, hemolysis, and non-fouling properties simultaneously. Originally posted as arXiv:2412.17780 (Dec 2024), accepted at ICML 2025.}
}
```

**Claim verification:** The claim "PepTune uses masked diffusion PLM + MCTS for multi-objective peptide design" is **partially accurate, needs correction**:
- **MCTS for multi-objective guidance**: CONFIRMED. The paper explicitly uses Monte Carlo Tree Search (MCTS) for multi-objective guided sampling during inference.
- **Masked diffusion**: CONFIRMED. PepTune uses a Masked Discrete Language Model (MDLM) framework with a discrete diffusion process.
- **PLM (protein language model)**: INCORRECT. PepTune does NOT use a protein language model. It uses a RoFormer-based masked discrete language model trained on peptide SMILES strings, not protein sequences. The correct description is "masked discrete diffusion model + MCTS" rather than "masked diffusion PLM + MCTS."

---

### 2. PepMLM (pepmlm2025)

```bibtex
@article{pepmlm2025,
  title     = {Target sequence-conditioned design of peptide binders using masked language modeling},
  author    = {Chen, Leo Tianlai and Quinn, Zachary and Dumas, Madeleine and Peng, Christina and Hong, Lauren and Lopez-Gonzalez, Moises and Mestre, Alexander and Watson, Rio and Vincoff, Sophia and Zhao, Lin and Wu, Jianli and Stavrand, Audrey and Schaepers-Cheu, Mayumi and Wang, Tian Zi and Srijay, Divya and Monticello, Connor and Vure, Pranay and Pulugurta, Rishab and Pertsemlidis, Sarah and Kholina, Kseniia and Goel, Shrey and DeLisa, Matthew P. and Chi, Jen-Tsan Ashley and Truant, Ray and Aguilar, Hector C. and Chatterjee, Pranam},
  year      = {2025},
  journal   = {Nature Biotechnology},
  doi       = {10.1038/s41587-025-02761-2},
  note      = {Finetunes ESM-2 protein language model with a masking strategy to design de novo linear peptide binders conditioned on target protein sequences alone (no structure required). Experimentally validated with nanomolar binding affinity on disease-relevant targets including NCAM1 (acute myeloid leukemia) and AMHR2 (polycystic ovarian syndrome), hitting targets that RFdiffusion could not.}
}
```

**Claim verification:** PepMLM as an ESM-2-based peptide binder design tool is **CONFIRMED**. The paper finetunes ESM-2 (a protein language model) with masked language modeling to generate peptide binders conditioned on target protein sequences. Published in Nature Biotechnology on August 13, 2025. Note: the paper was published online ahead of print, so volume/pages are not yet assigned.

---

### 3. Agentomics (agentomics2026)

```bibtex
@article{agentomics2026,
  title     = {Agentomics: An Agentic System that Autonomously Develops Novel State-of-the-art Solutions for Biomedical Machine Learning Tasks},
  author    = {Martinek, Vlastimil and Gariboldi, Andrea and Tzimotoudis, Dimosthenis and Galea, Mark and Zacharopoulou, Elissavet and Alberdi Escudero, Aitor and Blake, Edward and {\v{C}}ech{\'a}k, David and Cassar, Luke and Balestrucci, Alessandro and Alexiou, Panagiotis},
  year      = {2026},
  journal   = {bioRxiv},
  doi       = {10.64898/2026.01.27.702049},
  note      = {Introduces Agentomics, an autonomous LLM-powered agentic system from BioGeMT that takes a biomedical dataset and iteratively develops complete ML solutions. Evaluated on 20 benchmark datasets across Protein Engineering, Drug Discovery, and Regulatory Genomics. Surpassed human-engineered SOTA on 11/20 datasets (6/6 Protein Engineering, 4/5 Regulatory Genomics), with 100\% success rate across 60 runs.}
}
```

**Claim verification:** The claim "Agentomics achieves SOTA on 11/20 biomedical benchmarks" is **CONFIRMED**. The paper explicitly reports that Agentomics surpassed the best reported human-engineered state-of-the-art on 11 out of 20 established benchmark datasets. The gains were most pronounced in Protein Engineering (6/6 tasks) and Regulatory Genomics (4/5 tasks). The system achieved a 100% success rate in generating working, reusable solutions across all 60 experimental runs. Posted on bioRxiv January 30, 2026 by the BioGeMT group.

---

