# Position Paper Outline

Working Title: "What Drug Discovery AI Agents Still Can't Do: Lessons from Peptide Design, In Vivo Modeling, and Multi-Paradigm AI at a Small Biotech"

Target: arXiv cs.AI (primary), Drug Discovery Today, Nature Machine Intelligence (perspective)

Word Count Target: 6,000-8,000 words

---

# 1. Abstract (200-250 words)

## Structure

- Opening: The promise of agentic AI in drug discovery (ChatInvent, Coscientist, etc.)
- Gap statement: Current systems optimized for small-molecule, target-based workflows at large pharma
- Three blind spots: (1) peptide-specific requirements, (2) in vivo–in silico bridge, (3) multi-paradigm orchestration needs
- Positioning: Practitioner perspective from 14+ AI-driven projects at small biotech
- Contribution: Identifies five critical gaps and proposes practitioner-informed design principles
- Call to action: Move from LLM-centric multi-agent chat to true computational partnership
## Key Arguments

- Current agentic AI systems (ChatInvent, PharmAgents, MADD) showcase impressive capabilities but reveal systematic blind spots when applied beyond their design context
- Peptide drug discovery, in vivo modeling, and resource-constrained settings expose fundamental architectural limitations
- The field needs multi-paradigm orchestration frameworks, not just better LLM prompting strategies
## References

- He et al. 2026 (ChatInvent)
- Seal et al. 2025 (AI Agents survey)
- Boiko et al. 2023 (Coscientist)
- Lakhan 2025 (Agentic Era editorial)
---

# 2. Introduction: The Promise vs Reality of Agentic AI in Drug Discovery (800-1,000 words)

## 2.1 The Current Narrative

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
## 2.2 The Gap: What Happens Outside the Lab Automation Paradigm

### Key Arguments

- Current systems excel at well-defined, literature-rich, high-throughput scenarios
- Peptide discovery, in vivo modeling, and small-biotech constraints create fundamentally different requirement profiles
- The "agentic" label often masks brittle orchestration of narrow tools rather than genuine adaptability
### Examples

- Multi-endpoint bioactivity prediction (proliferation + migration + secretion + toxicity) requires paradigm integration, not just tool selection
- Longitudinal in vivo efficacy modeling (TBI recovery trajectories) has no lab automation equivalent
- Small biotech teams need batch-mode orchestration, not interactive chat workflows
> **💡** Key Takeaway: Current State: Agentic AI in drug discovery is optimized for small-molecule synthesis at well-resourced organizations with high-throughput screening infrastructure. The Reality Check: Peptide discovery, in vivo modeling, and resource-constrained settings expose architectural assumptions that don't generalize.

Suggested Figure 1: Timeline of agentic AI systems in drug discovery (2023-2026): ChemCrow, Coscientist, ChatInvent, PharmAgents, MADD, DiscoVerse. Annotation showing modal focus on small molecules + synthesis planning.

---

# 3. Gap 1: The Small Molecule Bias (1,200-1,500 words)

## 3.1 The Peptide-Specific Challenge Space

### Key Arguments

- Peptides occupy a distinct chemical space: 2-50 amino acids, conformationally flexible, immunogenic, protease-labile
- Discovery workflow differs fundamentally: structure-activity relationships non-transferable from small molecules, stability/bioavailability dominant constraints
- Existing agent architectures assume SMILES strings, docking scores, and synthetic accessibility—none map cleanly to peptides
### Examples from Problem Classes

- Generative peptide design (ProtBERT/ProtGPT2 fine-tuning): Requires protein language models, not molecular fingerprints
- Peptide-enzyme interaction modeling for stability: Protease cleavage site prediction ≠ cytochrome P450 metabolism
- Peptide-receptor binding site analysis: Flexible docking with conformational sampling, not rigid-body screening
### References

- Ferruz et al. 2022 (ProtGPT2)
- Lin et al. 2023 (ESM-2)
- AlQuraishi 2019 (protein structure prediction paradigms)
- Jumper et al. 2021 (AlphaFold2)
## 3.2 Protein Language Models vs Molecular Fingerprints

### Key Arguments

- PLMs (ProtBERT, ESM-2, ProGen) encode evolutionary and structural priors fundamentally different from chemical descriptors
- Current agent frameworks treat models as black-box APIs—no architectural support for transfer learning or fine-tuning workflows
- Receptor type prediction, binding site clustering, and stability optimization require model customization, not prompt engineering
### Examples

- Receptor type prediction with ESM-2: Multi-class classification on embeddings
- Transfer learning from general protein corpora to peptide bioactivity: Requires gradient-based optimization loops
- Monte Carlo Metropolis-Hastings for sequence optimization: Sampling in discrete sequence space, not continuous latent space
### References

- Rives et al. 2021 (ESM-2)
- Elnaggar et al. 2021 (ProtBERT)
- Madani et al. 2023 (ProGen2)
## 3.3 What Peptide-Aware Agents Would Need

### Key Arguments

- Explicit support for protein language model fine-tuning pipelines (dataset curation → training → validation)
- Multi-objective optimization over non-decomposable constraints (bioactivity + stability + immunogenicity + synthesis feasibility)
- Integration with structural biology tools (AlphaFold, docking, MD simulations) as first-class components, not external APIs
### Proposed Capabilities

- Curriculum learning for peptide generators: Start with simple bioactivity, progressively add stability/immunogenicity constraints
- Diversity-aware reward functions: Avoid mode collapse in sequence space (RL-based generation)
- Active learning loops: Select next peptide to synthesize based on epistemic uncertainty + expected improvement
> **💡** Key Takeaway: The Bias: Existing agent architectures assume small-molecule workflows (SMILES, fingerprints, synthesis planning). The Reality: Peptide discovery requires protein language models, flexible docking, protease stability prediction, and immunogenicity assessment—none of which fit the current paradigm. The Need: Peptide-aware agents must support PLM fine-tuning, multi-objective sequence optimization, and structural biology integration as architectural primitives.

Suggested Table 1: Small Molecule vs Peptide Discovery Workflows. Columns: Representation, Generative Models, Key Constraints, Optimization Paradigm, Validation Methods. Rows: Small Molecules vs Peptides. Highlights incompatibility of current agent assumptions.

---

# 4. Gap 2: The In Vivo–In Silico Bridge (1,200-1,500 words)

## 4.1 The Lab Automation Ceiling

### Key Arguments

- Current agents excel at in vitro automation (Emerald Cloud Lab, Strateos) but have no pathway to in vivo modeling
- Animal studies generate longitudinal, multi-modal data (clinical scores, imaging, transcriptomics) that don't fit high-throughput screening paradigms
- The "in vivo–in silico bridge" requires temporal modeling, causality inference, and safety-efficacy trade-off navigation
### Examples

- TBI recovery modeling: Longitudinal neurological scores over 28 days, identifying temporal efficacy signatures
- Immune response profiling: RNA-seq + pathway analysis to link peptide treatment to immunomodulation
- Behavioral phenotyping: Computer vision (DeepLabCut) to quantify social bonding, gait, anxiety-like behaviors
### References

- Boiko et al. 2023 (Coscientist—stops at in vitro synthesis)
- He et al. 2026 (ChatInvent—literature synthesis, no in vivo integration)
- Swanson et al. 2024 (PharmAgents—targets + compounds, not organisms)
## 4.2 Multi-Modal, Longitudinal Data Integration

### Key Arguments

- In vivo studies yield heterogeneous data: clinical scores (ordinal), imaging (spatial), transcriptomics (high-dimensional), behavioral (video)
- Agents need to integrate these modalities to identify mechanism-of-action and predict translational success
- Current systems treat data sources independently; no support for causal inference or temporal dynamics
### Examples

- Predictive efficacy modeling (PEM): Combining in vitro bioactivity + early in vivo markers to forecast 28-day outcomes
- Bone formation quantification: Digital image processing to extract morphometric features from histology
- RNA-seq → pathway enrichment → hypothesis generation loop: Requires bioinformatics pipelines (GSEA, KEGG), not LLM chat
### References

- Subramanian et al. 2005 (GSEA)
- Mathis et al. 2018 (DeepLabCut)
- Kanehisa et al. 2023 (KEGG pathways)
## 4.3 Safety, Efficacy, and the Translation Valley of Death

### Key Arguments

- In vivo models surface safety-efficacy trade-offs that in silico screens miss (e.g., peptide stabilization may increase immunogenicity)
- Toxicology modeling requires dose-response curves, GLMM for repeated measures, and multi-species extrapolation
- Agents need multi-objective optimization frameworks that respect Pareto frontiers, not single-metric maximization
### Examples

- Toxicity vs efficacy trade-off: A peptide with 10x higher bioactivity but 2x higher hepatotoxicity requires human judgment + modeling
- Species translation: Mouse→rat→primate pharmacokinetics requires allometric scaling and uncertainty quantification
- Dose optimization: Identifying therapeutic window where efficacy plateaus and toxicity remains acceptable
### Proposed Capabilities

- Temporal state-space models for longitudinal in vivo trajectories
- Causal inference tools (do-calculus, counterfactual reasoning) to separate correlation from mechanism
- Multi-objective Bayesian optimization with safety constraints and interpretable Pareto frontiers
> **💡** Key Takeaway: Where Agents Stop: In vitro automation, synthesis planning, and static binding predictions. Where Practitioners Start: Longitudinal in vivo data (clinical scores, imaging, transcriptomics), safety-efficacy trade-offs, and mechanistic hypothesis generation. The Bridge: Temporal modeling, multi-modal data fusion, causal inference, and multi-objective optimization under uncertainty.

Suggested Figure 2: The In Vivo–In Silico Gap. Left: Current agent coverage (literature → targets → compounds → in vitro assays). Right: Practitioner reality (in vivo studies → multi-modal data → safety/efficacy integration → clinical decisions). Gap highlighted in center.

---

# 5. Gap 3: Multi-Paradigm, Not Multi-Agent (1,000-1,200 words)

## 5.1 The LLM-as-Orchestrator Assumption

### Key Arguments

- Current agent frameworks (ChatInvent, PharmAgents, ChemCrow) position LLMs as central orchestrators calling tool APIs
- This works for literature mining and synthesis planning (text-in, text-out) but breaks for gradient-based optimization, RL, and simulation
- Real drug discovery requires ML model training, not just inference—a paradigm LLM-centric designs don't support
### Examples

- RL-based peptide generation: Requires policy networks, reward models, and gradient updates—not LLM tool calls
- Monte Carlo optimization: Metropolis-Hastings sampling in sequence space needs custom energy functions
- Transfer learning for bioactivity prediction: Fine-tuning ProtBERT on proprietary assay data ≠ API call to pre-trained model
### References

- Seal et al. 2025 (notes LLM-centric design pattern)
- Bran et al. 2023 (ChemCrow: GPT-4 + 18 tools)
- Swanson et al. 2024 (PharmAgents: LLM + knowledge graph queries)
## 5.2 The Missing Paradigms

### Key Arguments

- Drug discovery practitioners use 5+ computational paradigms: supervised learning, generative modeling, RL, simulation, optimization
- Current agents support at most 2: LLM reasoning + supervised model inference
- No architectural support for training loops, hyperparameter search, or curriculum learning
### Missing Capabilities

- Supervised learning pipelines: Dataset versioning, train/val/test splits, cross-validation, model selection
- Generative model fine-tuning: VAE/GAN/diffusion training on domain-specific data
- Reinforcement learning: Environment definition, reward shaping, policy optimization
- Simulation integration: Molecular dynamics, pharmacokinetic modeling, dose-response simulation
- Optimization: Bayesian optimization, genetic algorithms, constrained optimization with safety margins
### Examples

- Multi-endpoint bioactivity prediction: Requires training multi-task neural networks on assay data
- Binding site clustering: Unsupervised learning (k-means, DBSCAN) on docking poses
- Single-cell transcriptomics: Dimensionality reduction (UMAP), clustering, differential expression—none are LLM tasks
### References

- Stokes et al. 2020 (ML for antibiotic discovery—multi-paradigm approach)
- Schneider et al. 2020 (generative models for drug discovery)
- Zhou et al. 2023 (RL for molecular design)
## 5.3 What Multi-Paradigm Orchestration Looks Like

### Key Arguments

- Agents should coordinate workflows, not just call APIs—think "computational notebook on autopilot"
- Practitioners need batch-mode orchestration: "Train 10 models with different architectures, evaluate on holdout, return Pareto frontier"
- The interface should be declarative (specify goals + constraints) rather than imperative (step-by-step instructions)
### Proposed Architecture

- Workflow DAGs with typed nodes: Data → Preprocessing → Training → Evaluation → Selection
- Support for parallel execution, checkpointing, and resource allocation
- Human-in-the-loop decision points at key junctures (model selection, safety thresholds, experimental validation)
> **💡** Key Takeaway: The Limitation: LLM-centric agents excel at reasoning over text but cannot manage ML training, RL optimization, or simulation workflows. What's Missing: Architectural support for supervised learning, generative modeling, RL, and optimization as first-class primitives. The Solution: Multi-paradigm orchestration frameworks that coordinate workflows (not just API calls) and support declarative goal specification.

Suggested Figure 3: LLM-Centric vs Multi-Paradigm Architecture. Top: Current design (LLM → Tool API calls). Bottom: Proposed design (Orchestrator → Workflow DAG with ML training, RL, simulation, optimization nodes).

---

# 6. Gap 4: The Small Biotech Reality (800-1,000 words)

## 6.1 Resource Constraints Current Agents Ignore

### Key Arguments

- ChatInvent assumes AstraZeneca-scale literature access, computational infrastructure, and expert teams
- Small biotechs operate with 10-100x less: limited proprietary data, modest compute budgets, small multidisciplinary teams
- Agents designed for large pharma fail to address cold-start problems, data efficiency, and generalization under scarcity
### Examples

- Proprietary assay data: 50-500 peptides tested, not 50,000+ compounds in pharma databases
- Computational budget: Single GPU workstation, not AWS clusters—RL and MD simulations must be sample-efficient
- Team structure: One scientist orchestrating 14 project types, not specialized teams per modality
### References

- He et al. 2026 (ChatInvent deployed at AstraZeneca—resource-rich context)
- Lakhan 2025 (editorial assumes large pharma budgets)
- DiMasi et al. 2016 (drug development costs—small biotech vs pharma economics)
## 6.2 Transfer Learning and Few-Shot Adaptation

### Key Arguments

- Small biotechs need agents that leverage public data + transfer learning, not just proprietary fine-tuning
- Few-shot learning and meta-learning are critical: "Given 20 examples of peptide X bioactivity, predict for 100 new sequences"
- Current systems assume abundant labeled data—no support for active learning or uncertainty-aware sampling
### Examples

- Transfer learning from UniProt/PDB to peptide bioactivity: Pre-trained PLMs + fine-tuning on small proprietary datasets
- Active learning for peptide selection: Identify high-uncertainty sequences to minimize experimental cost
- Meta-learning across project types: Knowledge transfer from peptide-receptor binding to peptide-enzyme interactions
### Proposed Capabilities

- Few-shot learning modules for rapid adaptation to new assays
- Active learning loops with acquisition functions (epistemic uncertainty, expected improvement)
- Transfer learning pipelines that compose public pre-training + private fine-tuning
## 6.3 Batch-Mode Efficiency for Small Teams

### Key Arguments

- Interactive chat interfaces (ChatInvent, Coscientist) assume dedicated operator time—impractical for small teams juggling 14 project types
- Small biotechs need batch-mode agents: "Analyze all 14 RNA-seq samples, return differential expression + pathway enrichment"
- Emphasis should be on automation of repetitive tasks, not conversational assistance
### Examples

- Batch peptide design: "Generate 1,000 candidates, filter by stability + immunogenicity, return top 50 for synthesis"
- Parallelized docking: "Dock 500 peptides against 10 receptor structures, cluster binding modes, identify hotspots"
- Automated pathway analysis: "Run GSEA on 8 treatment groups, export plots + tables for manuscript"
> **💡** Key Takeaway: The Assumption: Abundant data, compute, and specialized teams (the AstraZeneca context). The Reality: Small biotechs operate with 10-100x less—requiring transfer learning, active learning, and batch-mode automation. The Need: Agents optimized for data efficiency, few-shot adaptation, and hands-off orchestration of parallel workflows.

Suggested Table 2: Large Pharma vs Small Biotech Context. Rows: Data availability, Compute budget, Team structure, Workflow mode. Columns: Large Pharma (AstraZeneca) vs Small Biotech. Highlights misalignment of current agent design assumptions.

---

# 7. Gap 5: Multi-Objective Navigation (800-1,000 words)

## 7.1 The Single-Metric Trap

### Key Arguments

- Most agent demonstrations optimize single objectives: binding affinity, synthetic accessibility, literature relevance
- Real drug discovery requires simultaneous optimization of conflicting goals: bioactivity + safety + stability + synthesizability + cost
- Current systems lack frameworks for Pareto optimization, constraint satisfaction, and interpretable trade-off navigation
### Examples

- Peptide stability vs bioactivity: Stabilizing modifications (D-amino acids, cyclization) may reduce target affinity
- Efficacy vs toxicity: High-potency peptides may trigger immune responses or off-target effects
- Multi-endpoint assays: Optimize proliferation + migration + secretion simultaneously—no single "best" candidate
### References

- Reker 2020 (multi-objective optimization in drug discovery)
- Grisoni et al. 2021 (balancing activity, selectivity, and drug-likeness)
- Bickerton et al. 2012 (quantitative estimate of drug-likeness)
## 7.2 Pareto Frontiers and Constraint Satisfaction

### Key Arguments

- Drug candidates lie on Pareto frontiers: improving one property degrades another
- Human decision-makers need interpretable trade-off visualizations, not black-box "optimal" suggestions
- Agents should present Pareto sets + sensitivity analysis, enabling informed selection
### Examples

- Safety-efficacy Pareto frontier: 50 peptides with varying bioactivity-toxicity profiles
- Stability-activity trade-off: RL-generated sequences with diversity-aware rewards to populate the frontier
- Multi-objective Bayesian optimization: Next-candidate selection balancing expected improvement across 3+ objectives
### Proposed Capabilities

- Multi-objective Bayesian optimization with constraint handling
- Pareto frontier visualization with interactive filtering
- Sensitivity analysis: "How robust is this candidate to assay variability?"
## 7.3 Incorporating Uncertainty and Risk

### Key Arguments

- Predictions come with uncertainty—agents should propagate this into decision-making
- Risk profiles differ by development stage: early discovery tolerates variance, clinical candidates require high confidence
- No support for risk-aware selection, confidence intervals, or "safe" regions of design space
### Examples

- Epistemic uncertainty in bioactivity prediction: Wide confidence intervals for novel peptide scaffolds
- Dose-response uncertainty: GLMM confidence bands for toxicity thresholds
- Translation risk: Mouse→human PK predictions with quantified inter-species variability
> **💡** Key Takeaway: The Problem: Current agents optimize single metrics or treat multi-objective problems as weighted sums. The Reality: Drug discovery requires navigating Pareto frontiers across safety, efficacy, stability, and synthesizability—with uncertainty quantification. The Need: Multi-objective optimization frameworks, Pareto visualization, and risk-aware decision support.

Suggested Figure 4: Multi-Objective Trade-off Example. Scatter plot: Bioactivity vs Toxicity for 100 peptide candidates. Pareto frontier highlighted. Annotation showing candidate selection based on risk tolerance.

---

# 8. A Practitioner's Wishlist: What Would Actually Help (1,000-1,200 words)

## 8.1 Design Principles for Next-Generation Agents

### Principle 1: Multi-Paradigm Orchestration

- Support ML training, RL, simulation, and optimization as architectural primitives
- Declarative workflow specification: "Train ensemble of bioactivity models, return Pareto-optimal architectures"
- Batch-mode execution with checkpointing and resource management
### Principle 2: Modality-Aware Architectures

- First-class support for peptides, proteins, and biologics (not just small molecules)
- PLM fine-tuning pipelines, structural biology integration, protease stability prediction
- Extensible to antibodies, nucleic acids, and other therapeutic modalities
### Principle 3: In Vivo–In Silico Integration

- Temporal modeling for longitudinal efficacy/safety data
- Multi-modal data fusion (clinical scores + imaging + transcriptomics)
- Causal inference and mechanistic hypothesis generation
### Principle 4: Data Efficiency and Transfer Learning

- Few-shot adaptation to new assays with <100 examples
- Active learning loops to minimize experimental cost
- Knowledge transfer across related tasks (peptide-receptor → peptide-enzyme)
### Principle 5: Multi-Objective, Risk-Aware Optimization

- Pareto optimization with constraint satisfaction
- Uncertainty quantification and sensitivity analysis
- Interactive trade-off visualization for human decision-making
## 8.2 Concrete Use Cases

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
## 8.3 Infrastructure Needs

### Technical Requirements

- API standards for PLMs, docking tools, MD simulators (not just LLM inference)
- Version-controlled datasets and model registries
- Provenance tracking for reproducibility (workflow → data → models → results)
### Organizational Requirements

- Alignment with small biotech budgets and team sizes
- Training/documentation for non-ML-expert biologists
- Integration with existing tools (GraphPad, FlowJo, ImageJ, R/Bioconductor)
> **💡** Key Takeaway: What We Have: LLM-centric agents for literature mining and synthesis planning in well-resourced labs. What We Need: Multi-paradigm orchestration, modality-aware architectures, in vivo integration, data-efficient learning, and multi-objective optimization. The Goal: Computational partners that augment practitioner expertise, not chatbots that require hand-holding.

Suggested Table 3: Gap Analysis and Proposed Solutions. Columns: Current Limitation, Real-World Impact, Proposed Capability, Example Use Case. Rows: Small molecule bias, In vivo gap, LLM-centric design, Resource constraints, Single-metric optimization.

---

# 9. Conclusion: From Assistants to True Partners (500-600 words)

## 9.1 Summary of Gaps

- Gap 1 (Small molecule bias): Peptides need PLMs, flexible docking, and stability prediction
- Gap 2 (In vivo–in silico bridge): Longitudinal, multi-modal data integration is unsupported
- Gap 3 (LLM-centric design): Missing ML training, RL, simulation, and optimization paradigms
- Gap 4 (Resource constraints): No support for data efficiency, transfer learning, or batch-mode automation
- Gap 5 (Multi-objective navigation): Single-metric optimization ignores real-world trade-offs
## 9.2 The Path Forward

- Next-generation agents as computational partners: augmenting human expertise, not replacing it
- Move from interactive chat to declarative workflow orchestration
- Embed uncertainty quantification, multi-objective reasoning, and interpretability
## 9.3 A Call to Action

### For Researchers

- Build multi-paradigm orchestration frameworks beyond LLM tool-calling
- Develop peptide/protein-aware agent architectures
- Create benchmarks reflecting small biotech realities
### For Practitioners

- Share anonymized problem formulations to guide agent development
- Collaborate on open-source tools and datasets
- Demand systems that respect resource constraints and multi-objective trade-offs
### For Funders

- Support research at the intersection of AI agents and biological complexity
- Fund open-source infrastructure for small biotech contexts
- Prioritize translational impact over benchmark performance
> **💡** Key Takeaway: Current State: Agentic AI in drug discovery is a promising proof-of-concept, optimized for narrow contexts. The Opportunity: Expand to peptides, in vivo modeling, and resource-constrained settings—where the impact could be transformative. The Challenge: Requires rethinking architectures, embracing multi-paradigm orchestration, and centering practitioner needs.

---

# Appendix A: The 15 Project Classes (Anonymized)

- ML bioactivity prediction (multi-endpoint)
- Generative peptide design (PLM fine-tuning)
- Peptide-receptor binding site analysis and clustering
- In vivo TBI recovery modeling
- Peptide-enzyme interaction modeling for stability optimization
- Protein language model-based receptor type prediction
- Monte Carlo Metropolis-Hastings optimization for peptide discovery
- RNA sequencing and single-cell transcriptomics analysis
- Digital image processing for bone formation quantification
- Immune response profiling (ICEPOP, pathway analysis)
- Functional annotation and pathway enrichment
- Computer vision for behavioral phenotyping
- Predictive modeling bridging in vivo/in vitro (PEM development)
- RL for de novo peptide generation (GRPO variants)
- Safety/toxicology modeling (GLMM, dose-response, multi-objective trade-offs)
# Appendix B: Agent System Comparison (Suggested)

Compare ChatInvent, ChemCrow, Coscientist, PharmAgents, MADD, DiscoVerse across: modality coverage, workflow support, computational paradigms, resource requirements, decision support.

# Key References (Representative)

- He et al. 2026 (ChatInvent, Drug Discovery Today)
- Seal et al. 2025 (AI Agents survey, arXiv)
- Lakhan 2025 (Agentic Era, Cureus)
- Boiko et al. 2023 (Coscientist, Nature)
- Bran et al. 2023 (ChemCrow, Nat. Mach. Intell.)
- Swanson et al. 2024 (PharmAgents, arXiv)
- TxGemma (Google, 2024)

