# Experiment Candidates for arXiv Qualification

> **Problem:** arXiv cs.AI discourages pure position/perspective papers. Adding at least one empirical experiment transforms the submission from opinion into a research contribution.

---

## Ranking Summary

| Rank | Experiment | Effort | Cost | Impact | Best For |
|------|-----------|--------|------|--------|----------|
| 1 | Tool Registry Audit | 0.5-1 day | $0 | Very High | Quantitative bias proof |
| 2 | LLM Knowledge Probing (local models) | 2-3 days | $0 | Very High | Foundation model bias |
| 3 | Representation Format Coverage | 0.5-1 day | $0 | High | Low-hanging quantitative proof |
| 4 | Workflow DAG Expressiveness | 1-2 days | $0 | High | Formal/theoretical contribution |
| 5 | Citation/Reference Bias Analysis | 1 day | $0 | Medium-High | Bibliometric evidence |
| 6 | Multi-Objective vs Single-Objective | 2-3 days | $0 | High | Gap 5 evidence |
| 7 | Few-Shot Degradation Curve | 2-3 days | $0 | Medium-High | Gap 4 evidence |
| 8 | General-Purpose Agent Stress Test | 2-3 days | $0 | Medium | Failure mode taxonomy |
| 9 | Simulated Peptide Orchestrator | 3-5 days | $0 | High | Constructive prototype |
| 10 | Practitioner Survey | 1-2 weeks | $0 | Medium-High | Community validation |

> **Design principle:** All experiments use zero-cost resources (open-source repos, public data, local models via Ollama). No proprietary API calls required.

---

## Experiment 1: Tool Registry Audit

**Goal:** Programmatically analyze the tool registries of all 6 frameworks and quantify the small-molecule bias.

**What to do:**
- Clone ChemCrow, Coscientist, PharmAgents, MADD repos (or read papers for closed-source systems like ChatInvent, DiscoVerse)
- For each framework, enumerate every tool/API it integrates
- Classify each tool along three axes:
  - **Modality:** small molecule / peptide / protein / nucleic acid / in vivo / imaging / general
  - **Paradigm:** LLM inference / API call / model training / RL / simulation / optimization
  - **Data type:** SMILES / InChI / FASTA / PDB / tabular / image / time-series / text
- Compute coverage percentages per framework

**Expected output:**

| Framework | Total Tools | Small Mol | Peptide/Protein | In Vivo | Imaging |
|-----------|------------|-----------|-----------------|---------|---------|
| ChemCrow | 18 | 17 (94%) | 1 (6%) | 0 | 0 |
| Coscientist | ~8 | ~7 (88%) | ~1 (12%) | 0 | 0 |
| ... | ... | ... | ... | ... | ... |

**Why it works for arXiv:** Quantitative, reproducible, and immediately visual. A single bar chart showing "94% of agent tools target small molecules" is more persuasive than any argument. No reviewer can dispute a tool count.

**Effort:** 0.5-1 day
**Cost:** $0

---

## Experiment 2: LLM Knowledge Probing (Local Open-Source Models via Ollama)

**Goal:** Demonstrate that the foundation models underlying drug discovery agents have systematically lower competence on peptide tasks than small-molecule tasks.

**Setup:** Run all models locally via Ollama. No API costs.

**Models to test:**
- Kimi K2 (Moonshot AI) - frontier-class reasoning model
- Llama 3.3 70B (Meta) - widely used in open-source agent frameworks
- Qwen 2.5 72B (Alibaba) - strong multilingual/scientific reasoning
- DeepSeek-R1 (DeepSeek) - strong reasoning, popular in research

**Why multiple open models instead of proprietary APIs:**
- Testing 4 models shows the bias is **systematic across training corpora**, not a single-vendor artifact
- Stronger scientific claim: if the gap persists across models trained on different data mixtures, it reflects structural underrepresentation of peptide knowledge in the literature itself
- Many open-source agent frameworks (AutoGen, CrewAI, LangGraph) actually run on these models, making results directly relevant to the agent ecosystem
- Fully reproducible: any reviewer can install Ollama and replicate

**What to do:**
- Design 50-100 matched question pairs:
  - Small-molecule version: "What is the typical logP range for orally bioavailable drugs?"
  - Peptide version: "What is the typical protease half-life range for therapeutically viable peptides?"
- Categories (10 questions per category):
  - SAR reasoning
  - ADMET / pharmacokinetic properties
  - Generative design strategies
  - Optimization approaches
  - Assay interpretation
- Run each question through all 4 models via Ollama API
- Score answers on a 0-3 scale:
  - 0 = wrong or hallucinated
  - 1 = partially correct but missing key nuance
  - 2 = correct
  - 3 = correct with domain-expert-level nuance
- Blind scoring: randomize question order, score without knowing which model produced the answer

**Statistical analysis:**
- Paired Wilcoxon signed-rank test on small-molecule vs peptide scores per model
- Report mean score gap, effect size, and per-category breakdowns
- Visualize as grouped bar chart (model x domain) with error bars

**Hypothesis:** LLMs score 20-40% lower on peptide-specific questions because pre-training corpora skew heavily toward small-molecule literature. The gap should be consistent across all 4 models.

**Preempting the "you didn't test GPT-4" objection:** If 4 independently trained frontier models all exhibit the same peptide knowledge deficit, the finding is about training data distribution, not model capability. The bias is upstream of any specific model.

**Why it works for arXiv:** Novel evaluation of LLM domain competence with reproducible methodology. Shows the bias is structural (in the training data), not just architectural (in the agent design). Connects to the growing body of LLM-evaluation literature. Zero cost to run, zero cost to replicate.

**Effort:** 2-3 days (question design + Ollama runs + scoring)
**Cost:** $0 (local GPU only)

---

## Experiment 3: Representation Format Coverage Matrix

**Goal:** Empirically audit which molecular input formats each framework can parse.

**What to do:**
- Clone open-source repos (ChemCrow, Coscientist, MADD)
- Grep for input parsers, file readers, and format handlers
- For closed-source systems (ChatInvent, DiscoVerse), analyze from published papers and documentation
- Test formats: SMILES, InChI, FASTA, PDB, SDF/MOL, CSV (tabular bioactivity), NIfTI (imaging), FASTQ (sequencing)
- For open-source systems, actually try feeding a FASTA peptide sequence and record the error

**Output:** A format support matrix:

| Format | ChemCrow | Coscientist | PharmAgents | ChatInvent | MADD | DiscoVerse |
|--------|----------|-------------|-------------|------------|------|------------|
| SMILES | Y | Y | Y | Y | Y | Y |
| FASTA | N | N | N | N | N | ? |
| PDB | N | N | N | N | N | ? |
| Longitudinal CSV | N | N | N | N | N | N |
| Image (histology) | N | N | N | N | N | N |

**Why it works for arXiv:** Simple empirical audit. The table is immediately convincing: if no framework can even parse a peptide sequence, the small-molecule bias is self-evident.

**Effort:** 0.5-1 day
**Cost:** $0

---

## Experiment 4: Workflow DAG Expressiveness Analysis

**Goal:** Formally characterize the computational workflows required by each task class and show that LLM-as-orchestrator architectures can only express a subset.

**What to do:**
- For each of the 15 task classes, define the workflow as a directed acyclic graph (DAG) with typed nodes:
  - Node types: data-load, preprocess, train, evaluate, optimize, human-checkpoint, simulate, generate
  - Edge types: data-flow, control-flow, feedback-loop
- Characterize each DAG by structural properties: depth, branching factor, presence of cycles (RL), fan-out (ensembles), human-in-the-loop nodes
- Define the "expressiveness" of LLM-as-orchestrator: can execute linear chains and simple branches (tool calls), cannot execute cycles, parallel training, or checkpointed workflows
- Compute: what fraction of task class DAGs fall within the expressible subset?

**Expected result:** Only 2-3 of 15 task classes (literature search, functional annotation, pathway enrichment) have DAGs expressible by current agent architectures.

**Why it works for arXiv:** Formal, theoretical contribution. Provides a framework for reasoning about agent expressiveness. Novel framing that the community can build on.

**Effort:** 1-2 days (mostly diagramming + formal description)
**Cost:** $0

---

## Experiment 5: Citation/Reference Bias Analysis

**Goal:** Bibliometric evidence that the field's framing is structurally biased toward small molecules.

**What to do:**
- For each of the 6 framework papers, extract all references
- Classify each reference into categories: small-molecule drug discovery, peptide/protein therapeutics, in vivo/preclinical, imaging/computer vision, ML methods (general), LLM/NLP, other
- Compute the distribution per paper and aggregate
- Optionally: extend to the broader field by analyzing references in Seal et al.'s 45-page survey

**Expected result:** 70-90% of references focus on small-molecule workflows. Peptide/protein therapeutics represent <5% of citations.

**Why it works for arXiv:** Bibliometric analyses are accepted methodology. Provides structural evidence that the blind spots are baked into how the field cites and frames its work.

**Effort:** 1 day
**Cost:** $0

---

## Experiment 6: Multi-Objective vs Single-Objective on Public Peptide Data

**Goal:** Quantify the cost of single-objective optimization (what current agents do) versus multi-objective Pareto optimization for peptide candidate selection.

**What to do:**
- Use a public multi-endpoint peptide dataset:
  - DBAASP (antimicrobial peptides with MIC values against multiple organisms + hemolysis)
  - APD3 (antimicrobial peptide database)
  - Or SATPdb (therapeutic peptides)
- Define 2-3 objectives: antimicrobial activity, low hemolytic toxicity, predicted stability
- Compare three selection strategies:
  1. Single-objective ranking by activity alone (what agents do)
  2. Weighted sum (naive multi-objective)
  3. Pareto optimization (NSGA-II or similar)
- Measure: how many Pareto-optimal candidates does each strategy miss? What is the "cost" in objective space?

**Expected result:** Single-objective ranking misses 40-60% of Pareto-optimal candidates, selecting some dominated solutions instead.

**Why it works for arXiv:** Concrete, quantitative demonstration that single-objective optimization leads to suboptimal drug candidates. Directly supports Gap 5. Uses public data, fully reproducible.

**Effort:** 2-3 days (data download, preprocessing, MOBO experiment, visualization)
**Cost:** $0

---

## Experiment 7: Few-Shot Degradation Curve

**Goal:** Show that model performance degrades catastrophically at small-biotech data scales, and that transfer learning / active learning can partially recover it.

**What to do:**
- Take a public bioactivity dataset: ChEMBL peptide assays, or DBAASP antimicrobial peptides
- Train a standard model (random forest or XGBoost) at varying data sizes: N = 5000, 2000, 500, 200, 50
- Plot the learning curve (performance vs N)
- Then show recovery strategies:
  - Transfer learning: pre-train on large public dataset, fine-tune on small private set
  - PLM features: use ESM-2 embeddings instead of hand-crafted features
  - Active learning: simulate iterative selection of most informative examples

**Expected result:** Performance cliff below N~200. Transfer learning / PLM features recover 50-70% of the gap at N=50.

**Why it works for arXiv:** Standard ML experiment with clear narrative. Demonstrates that frameworks assuming big data are inappropriate for most drug discovery settings. The "recovery via PLM" result is itself a contribution.

**Effort:** 2-3 days
**Cost:** $0

---

## Experiment 8: General-Purpose Agent Stress Test

**Goal:** Test whether general-purpose LLM agent frameworks (not chemistry-specific ones) can orchestrate peptide drug discovery workflows.

**Why NOT test ChemCrow on peptide tasks:**
ChemCrow is explicitly designed for small-molecule chemistry. Testing it on peptide tasks is a straw man: the result is predetermined and reviewers would dismiss it as confirming the obvious. It is like testing a calculator on essay writing.

**What to test instead:**
- **General-purpose agent frameworks** that claim task generality: AutoGen, CrewAI, LangGraph agents backed by local open-source LLMs (via Ollama)
- **Agents claiming broad "drug discovery" scope:** PharmAgents and MADD position themselves as drug discovery agents without qualifying "small molecule only." Testing whether their architectures can accommodate peptide tasks is a fair and revealing experiment.

**What to do:**
- Set up AutoGen or CrewAI with a local model (Llama 3.3 or Qwen 2.5 via Ollama)
- Design 15 task prompts, one per task class (using public peptides like GLP-1 analogs, antimicrobial peptides)
- For each prompt, record:
  - (a) does the agent attempt the task or refuse?
  - (b) does it hallucinate tools that don't exist?
  - (c) does it fall back to small-molecule logic (e.g., generating SMILES when asked for peptide sequences)?
  - (d) does it produce a meaningful result?
- Classify failure modes: tool-not-found, wrong-representation, paradigm-mismatch, data-format-error, graceful-refusal

**Example prompts:**
- "Design 10 novel peptide analogs of GLP-1 optimized for protease stability and receptor binding"
- "Analyze longitudinal neurological recovery scores from a 28-day rodent TBI study and identify temporal efficacy signatures"
- "Train a bioactivity prediction model on this dataset of 50 peptides with proliferation and migration endpoints"
- "Run multi-objective optimization balancing antimicrobial activity against hemolytic toxicity for this peptide library"

**Output:** A failure mode taxonomy table. Rows = 15 task classes. Columns = agent framework, failure type, error message/behavior, whether it attempted a workaround.

**Why it works for arXiv:** Tests frameworks that should be able to handle diverse tasks. The finding isn't "a small-molecule tool fails on peptides" (obvious) but "even general-purpose agent architectures cannot orchestrate peptide discovery because the tool ecosystem doesn't exist" (non-trivial).

**Effort:** 2-3 days
**Cost:** $0 (local models via Ollama)

---

## Experiment 9: Simulated Peptide Orchestrator Prototype

**Goal:** Build a minimal proof-of-concept pipeline that addresses Gap 1, showing that a peptide-aware agent is feasible.

**What to do:**
- Build a simple orchestrator (Python script or LangChain/AutoGen pipeline) that chains:
  1. ESM-2 embedding extraction for input peptides
  2. ProtGPT2 generation of candidate peptides
  3. Multi-objective filtering (predicted activity + predicted stability + diversity)
  4. Ranked output with Pareto frontier visualization
- Compare: give a general-purpose agent the same task. Document what the agent does vs what the prototype does.

**Why it works for arXiv:** Constructive contribution, not just critique. Shows that closing the gaps is architecturally feasible. Reviewers value "here's what we built" alongside "here's what's missing."

**Effort:** 3-5 days
**Cost:** $0

---

## Experiment 10: Practitioner Survey / Needs Assessment

**Goal:** Validate that the 15 task classes and 5 gaps reflect community needs, not just one lab's experience.

**What to do:**
- Design a structured questionnaire (15-20 questions):
  - "Which of these task types do you perform?" (checklist of 15)
  - "Which does your current AI tooling support?" (same checklist)
  - "What is your team size / data scale / compute budget?"
  - "What is your primary therapeutic modality?" (small molecule / peptide / antibody / other)
- Distribute via: BioML Slack/Discord, computational chemistry Twitter/X, LinkedIn drug discovery groups, local JSAI or CBI networks
- Target: 15-30 respondents (sufficient for descriptive statistics)

**Expected result:** Significant gap between "tasks I perform" and "tasks my AI tools support," especially for peptide, in vivo, and multi-objective tasks.

**Why it works for arXiv:** Grounds the gap analysis in community evidence rather than a single practitioner's experience. Even small-N surveys are accepted in cs.AI when the population is specialized.

**Effort:** 1-2 weeks (design + distribution + collection + analysis)
**Cost:** $0

---

## Recommended Combinations

### Weekend Sprint (1-2 days, $0)
**Experiments #1 + #3:** Tool Registry Audit + Representation Format Coverage. Pure codebase analysis, no data dependencies, immediately quantitative. Produces two tables and a bar chart that anchor the entire paper.

### One-Week Sprint (5-7 days, $0)
**Experiments #1 + #2 + #3:** Tool Registry Audit + LLM Knowledge Probing (Ollama) + Format Coverage. The knowledge probing adds a novel evaluation dimension (foundation model bias) on top of the architectural audits. Three complementary angles, all zero cost.

### Maximum Impact (2 weeks, $0)
**Experiments #1 + #2 + #6 + #7:** Tool Audit + Knowledge Probing + Multi-Objective Experiment + Few-Shot Curve. Four complementary experiments, each supporting a different gap. This would make the paper a strong empirical contribution, not just a gap analysis.

### Fastest Single Experiment (0.5-1 day, $0)
**Experiment #1 alone** (Tool Registry Audit). Minimum viable experiment: a systematic, quantitative audit that no one has published. This alone may be sufficient to reframe the paper from "perspective" to "empirical analysis."
