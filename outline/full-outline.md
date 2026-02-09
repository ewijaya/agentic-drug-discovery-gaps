# Research Article Outline

Title: "A Systematic Gap Analysis of Agentic AI Frameworks for Drug Discovery Beyond Small Molecules"

Target: arXiv cs.AI (primary), Drug Discovery Today, Nature Machine Intelligence

Word Count Target: 6,000-8,000 words

---

# 1. Abstract (200-250 words)

## Structure

- Opening: The promise of agentic AI in drug discovery (ChatInvent, Coscientist, etc.)
- Gap statement: No systematic evaluation of these frameworks against real-world drug discovery requirements beyond small-molecule, target-based workflows
- Method: We evaluate 6 agentic AI frameworks against 15 task classes spanning peptide discovery, in vivo modeling, and resource-constrained settings
- Findings: Five critical capability gaps identified: (1) small-molecule bias in molecular representations, (2) absence of in vivo-in silico integration, (3) limited computational paradigm support, (4) misalignment with small-biotech constraints, (5) single-objective optimization assumptions
- Contribution: Capability matrix, derived design requirements, and concrete use cases for next-generation frameworks

## Key Arguments

- Current agentic AI systems (ChatInvent, PharmAgents, MADD) showcase impressive capabilities but have not been systematically evaluated against diverse drug discovery contexts
- Our analysis maps 6 frameworks against 15 real-world task classes, revealing coverage gaps in peptide discovery, in vivo modeling, and resource-constrained settings
- We derive design requirements for multi-paradigm orchestration frameworks from the identified gaps

## References

- He et al. 2026 (ChatInvent)
- Seal et al. 2025 (AI Agents survey)
- Boiko et al. 2023 (Coscientist)
- Lakhan 2025 (Agentic Era editorial)

---

# 2. Introduction: Agentic AI in Drug Discovery (800-1,000 words)

## 2.1 The Current Landscape

### Key Arguments

- Recent demonstrations (ChatInvent at AstraZeneca, Coscientist in organic chemistry) have established proof-of-concept for agentic AI in drug discovery
- Industry excitement centers on autonomous hypothesis generation, literature mining, and experimental design
- Dominant paradigm: LLM-based orchestration of domain-specific tools (ChemCrow, PharmAgents, DiscoVerse)

### Examples

- ChatInvent: 13-month deployment at AstraZeneca, literature synthesis + hypothesis generation
- Coscientist: Autonomous chemical synthesis planning and execution
- ChemCrow: GPT-4 orchestrating 18 chemistry tools for synthesis planning and safety assessment

### References

- He et al. 2026 (ChatInvent/AstraZeneca)
- Boiko et al. 2023 (Coscientist)
- Bran et al. 2023 (ChemCrow)
- Seal et al. 2025 (comprehensive survey)
- Swanson et al. 2024 (PharmAgents)
- TxGemma (Google, 2024)

## 2.2 Scope and Motivation

### Key Arguments

- Existing surveys (Seal et al. 2025) catalog agent architectures but do not evaluate them against diverse real-world task requirements
- Drug discovery extends well beyond small-molecule, target-based workflows: peptides, biologics, in vivo studies, and resource-constrained environments present distinct challenges
- A systematic evaluation of framework capabilities against practitioner task requirements is needed to guide future development

### Contribution Statement

- We present a systematic gap analysis evaluating 6 agentic AI frameworks against 15 drug discovery task classes
- We introduce a capability matrix mapping framework features to task requirements across 5 evaluation dimensions
- We derive design requirements for next-generation frameworks from the identified gaps

Suggested Figure 1: Timeline of agentic AI systems in drug discovery (2023-2026): ChemCrow, Coscientist, ChatInvent, PharmAgents, MADD, DiscoVerse. Annotation showing modal focus on small molecules + synthesis planning.

---

# 3. Methods: Evaluation Framework (600-800 words)

## 3.1 Agent Framework Selection

### Frameworks Evaluated

| Framework | Year | Organization | Primary Focus |
|-----------|------|-------------|---------------|
| ChemCrow | 2023 | EPFL/Rochester | Chemistry tool orchestration |
| Coscientist | 2023 | CMU | Autonomous synthesis |
| PharmAgents | 2024 | Stanford | Target-compound interaction |
| ChatInvent | 2026 | AstraZeneca | Literature-driven hypothesis |
| MADD | 2025 | Multi-institutional | Multi-agent drug design |
| DiscoVerse | 2025 | Industry | Discovery workflow automation |

### Selection Criteria

- Published or preprint with sufficient architectural detail
- Demonstrated application to drug discovery tasks
- Representative of distinct design paradigms (single-agent, multi-agent, tool-augmented)

## 3.2 Task Class Definition

Fifteen task classes derived from real-world drug discovery workflows spanning peptide therapeutics, in vivo pharmacology, and computational biology (full descriptions in Appendix A):

1. ML bioactivity prediction (multi-endpoint)
2. Generative peptide design (PLM fine-tuning)
3. Peptide-receptor binding site analysis and clustering
4. In vivo TBI recovery modeling
5. Peptide-enzyme interaction modeling for stability optimization
6. Protein language model-based receptor type prediction
7. Monte Carlo Metropolis-Hastings optimization for peptide discovery
8. RNA sequencing and single-cell transcriptomics analysis
9. Digital image processing for bone formation quantification
10. Immune response profiling (pathway analysis)
11. Functional annotation and pathway enrichment
12. Computer vision for behavioral phenotyping
13. Predictive modeling bridging in vivo/in vitro (PEM development)
14. RL for de novo peptide generation (GRPO variants)
15. Safety/toxicology modeling (GLMM, dose-response, multi-objective trade-offs)

## 3.3 Evaluation Dimensions

Each framework evaluated across five dimensions:

1. **Molecular representation coverage**: Support for peptides, proteins, and biologics beyond SMILES/fingerprints
2. **Computational paradigm support**: ML training, RL, simulation, optimization (beyond LLM inference + API calls)
3. **Data modality integration**: In vivo longitudinal data, imaging, transcriptomics, behavioral data
4. **Resource assumptions**: Data volume, compute budget, team size requirements
5. **Optimization framework**: Single vs multi-objective, uncertainty quantification, constraint handling

## 3.4 Analysis Approach

- Binary capability assessment (supported / not supported) for each framework-task pair
- Coverage score: fraction of 15 task classes addressable per framework
- Gap identification: task classes with zero or minimal framework coverage
- Design requirement derivation: capabilities needed to close identified gaps

Suggested Table 1 (Core Result): Capability Matrix. Rows: 15 task classes. Columns: 6 frameworks. Cells: ✓ (supported), ◐ (partial), ✗ (not supported). Summary row: coverage score per framework.

---

# 4. Results: Five Capability Gaps (4,200-5,200 words total)

## 4.1 Gap 1: Small-Molecule Representation Bias (1,200-1,500 words)

### 4.1.1 Findings

- All 6 frameworks assume small-molecule representations (SMILES strings, molecular fingerprints, docking scores)
- Task classes 2, 3, 5, 6, 7 (peptide-specific) receive zero coverage across all frameworks
- No framework supports protein language models (ProtBERT, ESM-2, ProGen) as first-class components

### 4.1.2 Analysis: The Peptide-Specific Challenge Space

- Peptides occupy a distinct chemical space: 2-50 amino acids, conformationally flexible, immunogenic, protease-labile
- Discovery workflow differs fundamentally: structure-activity relationships non-transferable from small molecules, stability/bioavailability dominant constraints
- Existing agent architectures assume SMILES strings, docking scores, and synthetic accessibility; none map cleanly to peptides

### Examples from Uncovered Task Classes

- Generative peptide design (ProtBERT/ProtGPT2 fine-tuning): Requires protein language models, not molecular fingerprints
- Peptide-enzyme interaction modeling for stability: Protease cleavage site prediction ≠ cytochrome P450 metabolism
- Peptide-receptor binding site analysis: Flexible docking with conformational sampling, not rigid-body screening

### 4.1.3 Derived Requirements

- Explicit support for protein language model fine-tuning pipelines (dataset curation → training → validation)
- Multi-objective optimization over non-decomposable constraints (bioactivity + stability + immunogenicity + synthesis feasibility)
- Integration with structural biology tools (AlphaFold, docking, MD simulations) as first-class components

### References

- Ferruz et al. 2022 (ProtGPT2)
- Lin et al. 2023 (ESM-2)
- AlQuraishi 2019 (protein structure prediction paradigms)
- Jumper et al. 2021 (AlphaFold2)
- Rives et al. 2021 (ESM-2)
- Elnaggar et al. 2021 (ProtBERT)
- Madani et al. 2023 (ProGen2)

Suggested Table 2: Small Molecule vs Peptide Discovery Workflows. Columns: Representation, Generative Models, Key Constraints, Optimization Paradigm, Validation Methods. Rows: Small Molecules vs Peptides.

## 4.2 Gap 2: Absence of In Vivo-In Silico Integration (1,200-1,500 words)

### 4.2.1 Findings

- Task classes 4, 9, 12, 13 (in vivo and imaging tasks) receive zero coverage
- All frameworks terminate at in vitro automation or literature-based hypothesis generation
- No framework supports longitudinal data modeling, multi-modal fusion, or causal inference

### 4.2.2 Analysis: The Lab Automation Ceiling

- Current agents excel at in vitro automation (Emerald Cloud Lab, Strateos) but have no pathway to in vivo modeling
- Animal studies generate longitudinal, multi-modal data (clinical scores, imaging, transcriptomics) that don't fit high-throughput screening paradigms
- The in vivo-in silico bridge requires temporal modeling, causality inference, and safety-efficacy trade-off navigation

### Examples from Uncovered Task Classes

- TBI recovery modeling: Longitudinal neurological scores over 28 days, identifying temporal efficacy signatures
- Behavioral phenotyping: Computer vision (DeepLabCut) to quantify social bonding, gait, anxiety-like behaviors
- Bone formation quantification: Digital image processing to extract morphometric features from histology

### 4.2.3 Multi-Modal, Longitudinal Data Integration

- In vivo studies yield heterogeneous data: clinical scores (ordinal), imaging (spatial), transcriptomics (high-dimensional), behavioral (video)
- Current systems treat data sources independently; no support for causal inference or temporal dynamics
- Predictive efficacy modeling (PEM): Combining in vitro bioactivity + early in vivo markers to forecast 28-day outcomes

### 4.2.4 Derived Requirements

- Temporal state-space models for longitudinal in vivo trajectories
- Causal inference tools (do-calculus, counterfactual reasoning) to separate correlation from mechanism
- Multi-objective Bayesian optimization with safety constraints and interpretable Pareto frontiers

### References

- Boiko et al. 2023 (Coscientist: stops at in vitro synthesis)
- He et al. 2026 (ChatInvent: literature synthesis, no in vivo integration)
- Swanson et al. 2024 (PharmAgents: targets + compounds, not organisms)
- Subramanian et al. 2005 (GSEA)
- Mathis et al. 2018 (DeepLabCut)
- Kanehisa et al. 2023 (KEGG pathways)

Suggested Figure 2: The In Vivo-In Silico Gap. Left: Current agent coverage (literature → targets → compounds → in vitro assays). Right: Practitioner reality (in vivo studies → multi-modal data → safety/efficacy integration → clinical decisions). Gap highlighted in center.

## 4.3 Gap 3: Limited Computational Paradigm Support (1,000-1,200 words)

### 4.3.1 Findings

- All 6 frameworks use LLM-as-orchestrator architecture: LLM reasoning + tool API calls
- Task classes requiring model training (1, 2, 6, 14), RL (7, 14), or simulation receive no support
- No framework supports gradient-based optimization, hyperparameter search, or curriculum learning

### 4.3.2 Analysis: The LLM-as-Orchestrator Limitation

- LLM-centric designs work for literature mining and synthesis planning (text-in, text-out) but break for gradient-based optimization, RL, and simulation
- Real drug discovery requires ML model training, not just inference
- Drug discovery practitioners use 5+ computational paradigms: supervised learning, generative modeling, RL, simulation, optimization

### Missing Paradigms Across Frameworks

- Supervised learning pipelines: Dataset versioning, train/val/test splits, cross-validation, model selection
- Generative model fine-tuning: VAE/GAN/diffusion training on domain-specific data
- Reinforcement learning: Environment definition, reward shaping, policy optimization
- Simulation integration: Molecular dynamics, pharmacokinetic modeling, dose-response simulation
- Optimization: Bayesian optimization, genetic algorithms, constrained optimization with safety margins

### 4.3.3 Derived Requirements

- Support for workflow DAGs with typed nodes: Data → Preprocessing → Training → Evaluation → Selection
- Parallel execution, checkpointing, and resource allocation
- Human-in-the-loop decision points at key junctures (model selection, safety thresholds, experimental validation)
- Declarative goal specification rather than imperative step-by-step instructions

### References

- Seal et al. 2025 (notes LLM-centric design pattern)
- Bran et al. 2023 (ChemCrow: GPT-4 + 18 tools)
- Swanson et al. 2024 (PharmAgents: LLM + knowledge graph queries)
- Stokes et al. 2020 (ML for antibiotic discovery: multi-paradigm approach)
- Schneider et al. 2020 (generative models for drug discovery)
- Zhou et al. 2023 (RL for molecular design)

Suggested Figure 3: LLM-Centric vs Multi-Paradigm Architecture. Top: Current design (LLM → Tool API calls). Bottom: Proposed design (Orchestrator → Workflow DAG with ML training, RL, simulation, optimization nodes).

## 4.4 Gap 4: Misalignment with Small-Biotech Constraints (800-1,000 words)

### 4.4.1 Findings

- All evaluated frameworks assume large-pharma resource levels: abundant proprietary data, cluster-scale compute, specialized teams
- No framework supports few-shot adaptation, active learning, or transfer learning for data-scarce settings
- Interactive chat interfaces assume dedicated operator time, impractical for small teams

### 4.4.2 Analysis: Resource Assumptions vs Reality

- ChatInvent assumes AstraZeneca-scale literature access, computational infrastructure, and expert teams
- Small biotechs operate with 10-100x less: limited proprietary data (50-500 assayed compounds vs 50,000+), modest compute budgets (single GPU vs clusters), small multidisciplinary teams
- Cold-start problems, data efficiency, and generalization under scarcity are unaddressed

### 4.4.3 Derived Requirements

- Few-shot learning modules for rapid adaptation to new assays
- Active learning loops with acquisition functions (epistemic uncertainty, expected improvement)
- Transfer learning pipelines that compose public pre-training + private fine-tuning
- Batch-mode orchestration: "Analyze all 14 RNA-seq samples, return differential expression + pathway enrichment"

### References

- He et al. 2026 (ChatInvent deployed at AstraZeneca: resource-rich context)
- Lakhan 2025 (editorial assumes large pharma budgets)
- DiMasi et al. 2016 (drug development costs: small biotech vs pharma economics)

Suggested Table 3: Resource Assumptions. Rows: Data availability, Compute budget, Team structure, Workflow mode. Columns: Framework assumptions vs Small biotech reality.

## 4.5 Gap 5: Single-Objective Optimization Assumptions (800-1,000 words)

### 4.5.1 Findings

- All frameworks optimize single objectives or use fixed weighted sums
- No framework supports Pareto optimization, constraint satisfaction, or uncertainty-aware candidate selection
- Task class 15 (safety/toxicology modeling with multi-objective trade-offs) has zero coverage

### 4.5.2 Analysis: The Single-Metric Trap

- Most agent demonstrations optimize single objectives: binding affinity, synthetic accessibility, literature relevance
- Real drug discovery requires simultaneous optimization of conflicting goals: bioactivity + safety + stability + synthesizability + cost
- Drug candidates lie on Pareto frontiers: improving one property degrades another

### Examples

- Peptide stability vs bioactivity: Stabilizing modifications (D-amino acids, cyclization) may reduce target affinity
- Efficacy vs toxicity: High-potency peptides may trigger immune responses or off-target effects
- Multi-endpoint assays: Optimize proliferation + migration + secretion simultaneously; no single "best" candidate

### 4.5.3 Derived Requirements

- Multi-objective Bayesian optimization with constraint handling
- Pareto frontier visualization with interactive filtering
- Uncertainty quantification: epistemic uncertainty in bioactivity prediction, dose-response confidence bands
- Risk-aware candidate selection appropriate to development stage

### References

- Reker 2020 (multi-objective optimization in drug discovery)
- Grisoni et al. 2021 (balancing activity, selectivity, and drug-likeness)
- Bickerton et al. 2012 (quantitative estimate of drug-likeness)

Suggested Figure 4: Multi-Objective Trade-off Example. Scatter plot: Bioactivity vs Toxicity for peptide candidates. Pareto frontier highlighted. Annotation showing candidate selection based on risk tolerance.

---

# 5. Design Requirements for Next-Generation Frameworks (1,000-1,200 words)

## 5.1 Requirements Derived from Gap Analysis

### Requirement 1: Multi-Paradigm Orchestration

- Support ML training, RL, simulation, and optimization as architectural primitives
- Declarative workflow specification: "Train ensemble of bioactivity models, return Pareto-optimal architectures"
- Batch-mode execution with checkpointing and resource management

### Requirement 2: Modality-Aware Representations

- First-class support for peptides, proteins, and biologics (not just small molecules)
- PLM fine-tuning pipelines, structural biology integration, protease stability prediction
- Extensible to antibodies, nucleic acids, and other therapeutic modalities

### Requirement 3: In Vivo-In Silico Data Fusion

- Temporal modeling for longitudinal efficacy/safety data
- Multi-modal data fusion (clinical scores + imaging + transcriptomics)
- Causal inference and mechanistic hypothesis generation

### Requirement 4: Data-Efficient Learning

- Few-shot adaptation to new assays with <100 examples
- Active learning loops to minimize experimental cost
- Knowledge transfer across related tasks (peptide-receptor → peptide-enzyme)

### Requirement 5: Multi-Objective, Risk-Aware Optimization

- Pareto optimization with constraint satisfaction
- Uncertainty quantification and sensitivity analysis
- Interactive trade-off visualization for human decision-making

## 5.2 Illustrative Use Cases

### Use Case 1: Peptide Lead Optimization

- Input: 50 peptides with bioactivity data, target receptor structure
- Workflow: Fine-tune PLM → generate 1,000 candidates → filter by stability + immunogenicity → dock top 100 → present Pareto frontier (activity vs safety)
- Output: 10 candidates for synthesis + rationale + uncertainty estimates

### Use Case 2: In Vivo Efficacy Prediction

- Input: In vitro bioactivity + early (day 3) in vivo markers for 20 peptides
- Workflow: Train PEM → forecast day 28 outcomes → identify temporal signatures → suggest next candidates
- Output: Predicted efficacy + confidence intervals + mechanistic insights

### Use Case 3: Multi-Endpoint Assay Analysis

- Input: Proliferation + migration + secretion + toxicity data for 100 peptides
- Workflow: Multi-task learning → cluster by activity profile → pathway enrichment → hypothesis generation
- Output: Candidate selection + mechanism-of-action hypotheses + suggested validations

## 5.3 Infrastructure Considerations

### Technical

- API standards for PLMs, docking tools, MD simulators (not just LLM inference)
- Version-controlled datasets and model registries
- Provenance tracking for reproducibility (workflow → data → models → results)

### Organizational

- Alignment with small biotech budgets and team sizes
- Integration with existing tools (GraphPad, FlowJo, ImageJ, R/Bioconductor)

Suggested Table 4: Gap-to-Requirement Mapping. Columns: Identified Gap, Derived Requirement, Example Capability, Illustrative Use Case. One row per gap.

---

# 6. Discussion (500-600 words)

## 6.1 Scope and Limitations

- Task classes derived from peptide therapeutics context; applicability to antibodies, gene therapies, and other modalities requires further evaluation
- Binary capability assessment may oversimplify nuanced partial support
- Rapidly evolving field; new frameworks may address some identified gaps

## 6.2 Relation to Existing Work

- Seal et al. 2025 provides comprehensive architectural survey but does not evaluate against task requirements
- He et al. 2026 demonstrates deep single-organization deployment but does not assess generalizability
- This work complements both by providing a requirements-driven evaluation framework

## 6.3 Future Directions

- Empirical benchmarks reflecting diverse drug discovery contexts (beyond molecular generation)
- Open-source multi-paradigm orchestration frameworks
- Community-driven task class definitions spanning therapeutic modalities

---

# 7. Conclusion (300-400 words)

- Summary: Systematic evaluation of 6 agentic AI frameworks against 15 drug discovery task classes reveals 5 critical capability gaps
- The gaps are structural, not incremental: addressing them requires architectural changes, not feature additions
- Next-generation frameworks should support multi-paradigm orchestration, modality-aware representations, in vivo data integration, data-efficient learning, and multi-objective optimization
- The capability matrix and derived requirements provide a roadmap for framework developers and a benchmarking tool for practitioners

---

# Appendix A: Task Class Descriptions

Full descriptions of the 15 task classes with representative inputs, outputs, computational requirements, and evaluation criteria.

1. ML bioactivity prediction (multi-endpoint)
2. Generative peptide design (PLM fine-tuning)
3. Peptide-receptor binding site analysis and clustering
4. In vivo TBI recovery modeling
5. Peptide-enzyme interaction modeling for stability optimization
6. Protein language model-based receptor type prediction
7. Monte Carlo Metropolis-Hastings optimization for peptide discovery
8. RNA sequencing and single-cell transcriptomics analysis
9. Digital image processing for bone formation quantification
10. Immune response profiling (pathway analysis)
11. Functional annotation and pathway enrichment
12. Computer vision for behavioral phenotyping
13. Predictive modeling bridging in vivo/in vitro (PEM development)
14. RL for de novo peptide generation (GRPO variants)
15. Safety/toxicology modeling (GLMM, dose-response, multi-objective trade-offs)

# Appendix B: Detailed Capability Matrix

Extended version of Table 1 with per-dimension scores, evidence citations, and notes on partial support.

Compare ChatInvent, ChemCrow, Coscientist, PharmAgents, MADD, DiscoVerse across: modality coverage, workflow support, computational paradigms, resource requirements, decision support.

# Key References (Representative)

- He et al. 2026 (ChatInvent, Drug Discovery Today)
- Seal et al. 2025 (AI Agents survey, arXiv)
- Lakhan 2025 (Agentic Era, Cureus)
- Boiko et al. 2023 (Coscientist, Nature)
- Bran et al. 2023 (ChemCrow, Nat. Mach. Intell.)
- Swanson et al. 2024 (PharmAgents, arXiv)
- TxGemma (Google, 2024)
