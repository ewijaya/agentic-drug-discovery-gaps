# PRD: Experiment 2 — LLM Knowledge Probing Across Drug Modalities

## 1. Purpose

Empirically demonstrate that the foundation models underlying drug discovery agents have systematically lower competence on peptide therapeutics than on small-molecule drug discovery. This experiment supports **Gap 1 (The Small Molecule Bias)** in the paper "Beyond SMILES: Evaluating Agentic AI for Drug Discovery" and transforms the paper from a position piece into an empirical contribution suitable for arXiv cs.AI.

**Core claim to validate:** If multiple independently trained frontier LLMs all exhibit the same peptide knowledge deficit, the bias is structural (rooted in training data distribution), not architectural (specific to any single model or agent framework).

## 2. Context

### 2.1 Paper Integration

This experiment produces:
- A new results subsection within Section 3 (Gap 1: The Small Molecule Bias) or a dedicated Section 2.5 (Empirical Evaluation)
- Figure: grouped bar chart (model x domain) with error bars
- Table: per-category score breakdown across models
- Statistical results: Wilcoxon signed-rank test p-values, effect sizes

### 2.2 Relation to Other Experiments

This is a standalone experiment. It does not depend on Experiment #1 (Tool Registry Audit) or Experiment #3 (Representation Format Coverage), but complements them:
- Experiment #1 shows bias in **agent tool registries** (architectural)
- Experiment #2 shows bias in **foundation model knowledge** (upstream)
- Together they prove the bias is end-to-end: from training data through model knowledge to agent design

### 2.3 Source Specification

`reviews/06-experiment-candidates.md`, Experiment 2 (lines 54-102)

---

## 3. Infrastructure

### 3.1 Verified Setup

All models are accessed via **Ollama Cloud** using a single API key and the `ollama` Python library. This was verified on 2026-02-09.

| Component | Value |
|---|---|
| API endpoint | `https://ollama.com` |
| Auth method | Bearer token via `Authorization` header |
| Python library | `ollama==0.6.1` |
| API key env var | `OLLAMA_API_KEY` |

### 3.2 Verified Models

All four models were tested and confirmed working on 2026-02-09:

| Model | Ollama Tag | Provider | Training Pipeline | Verified |
|---|---|---|---|---|
| Kimi K2.5 | `kimi-k2.5:cloud` | Moonshot AI | Independent (Chinese lab) | Yes |
| DeepSeek V3.2 | `deepseek-v3.2:cloud` | DeepSeek | Independent (Chinese lab) | Yes |
| Qwen 3 Next 80B | `qwen3-next:80b-cloud` | Alibaba | Independent (Chinese lab) | Yes |
| Gemini 3 Flash | `gemini-3-flash-preview:cloud` | Google | Independent (US lab) | Yes |

**Why these four models:**
- 4 independent training pipelines from 4 different organizations
- Mix of geographies (3 Chinese, 1 US) rules out region-specific corpus bias
- All are frontier-class models (not toy/small models)
- All are used or usable in open-source agent frameworks
- Unified API via Ollama Cloud makes the experiment trivially reproducible

### 3.3 API Code Pattern

```python
from ollama import Client

client = Client(
    host="https://ollama.com",
    headers={"Authorization": f"Bearer {os.environ['OLLAMA_API_KEY']}"}
)

response = client.chat(
    model="kimi-k2.5:cloud",  # swap model tag here
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question_text},
    ],
)
answer = response.message.content
```

### 3.4 Cost Estimate

| Item | Estimate |
|---|---|
| Questions per domain | 50 |
| Domains | 2 (small-molecule, peptide) |
| Models | 4 |
| Total API calls | 400 |
| Avg tokens per call | ~500 input + ~500 output |
| Total tokens | ~200K input + 200K output |
| Ollama Cloud tier | Free (light usage) |
| **Estimated cost** | **$0 (within free tier)** |

If rate-limited on the free tier, the Pro plan ($20/month) covers this with margin.

### 3.5 Claude CLI (LLM-as-Judge)

Scoring uses Claude via the local CLI in print mode. Verified on 2026-02-09.

| Component | Value |
|---|---|
| Binary | `/home/ubuntu/.local/bin/claude` |
| Mode | `-p` (print: non-interactive, stdout only) |
| Model | `--model sonnet` (Claude Sonnet 4.5) |
| Auth | Existing Claude subscription (no additional cost) |
| Invocation | `echo "<prompt>" \| claude -p --model sonnet` |

**Why Claude as judge (not one of the 4 test models):**
- Completely independent from all 4 evaluated models (Anthropic vs Moonshot/DeepSeek/Alibaba/Google)
- Best-in-class rubric-following and nuanced evaluation
- No additional cost (existing subscription)
- No API key management (CLI handles auth)
- Fast (~2s per call)

**Code pattern:**

```python
import subprocess

def claude_judge(question, response, reference, key_concepts, score_rubric):
    prompt = f"""{score_rubric}

Question: {question}
Reference answer: {reference}
Key concepts expected: {', '.join(key_concepts)}
Model's answer: {response}

Reply with ONLY the integer score (0, 1, 2, or 3)."""

    result = subprocess.run(
        ["/home/ubuntu/.local/bin/claude", "-p", "--model", "sonnet"],
        input=prompt, capture_output=True, text=True, timeout=30
    )
    return int(result.stdout.strip())
```

### 3.6 Rate Limiting Strategy

Ollama Cloud free tier has unspecified "light usage" limits. To stay within bounds:
- Insert a 3-second delay between API calls (`time.sleep(3)`)
- Implement exponential backoff on 429/503 errors (max 3 retries, base 10s)
- Log all responses to disk incrementally so the experiment can resume from the last successful call if interrupted
- Run the experiment in two sessions if needed (small-molecule day 1, peptide day 2)

---

## 4. Question Design

### 4.1 Structure: Matched Pairs

Every question exists as a **matched pair**: one small-molecule version and one peptide version. The pairs test the same cognitive skill (SAR reasoning, ADMET knowledge, etc.) in two modality contexts, controlling for question difficulty and format.

**Example matched pair:**

| Domain | Question |
|---|---|
| Small molecule | "What is the typical logP range for orally bioavailable drugs, and why does it matter?" |
| Peptide | "What is the typical plasma half-life range for therapeutically viable peptides, and what structural features influence it?" |

Both questions require:
- Knowledge of a quantitative property range
- Understanding of why the range matters pharmacologically
- Awareness of structural/chemical factors that influence the property

### 4.2 Categories

5 categories, 10 matched pairs each = **50 matched pairs = 100 total questions**.

#### Category 1: SAR Reasoning (Structure-Activity Relationships)
Questions testing understanding of how structural modifications affect biological activity.
- Small molecule: functional group substitutions, scaffold hopping, bioisosteric replacements
- Peptide: amino acid substitutions, cyclization effects, stapled peptides, D-amino acid incorporation

#### Category 2: ADMET / Pharmacokinetic Properties
Questions about absorption, distribution, metabolism, excretion, and toxicity.
- Small molecule: Lipinski's rules, CYP metabolism, hERG liability, plasma protein binding
- Peptide: protease susceptibility, renal clearance, cell permeability, immunogenicity

#### Category 3: Generative Design Strategies
Questions about computational approaches to generating new candidates.
- Small molecule: SMILES-based generation, molecular graph generation, reaction-aware design
- Peptide: sequence-based generation, protein language models (ProtGPT2, ESM-2), structure-conditioned design

#### Category 4: Optimization Approaches
Questions about iterative improvement of candidates.
- Small molecule: Bayesian optimization on molecular descriptors, matched molecular pairs, multi-parameter optimization
- Peptide: directed evolution strategies, phage display-informed design, Pareto optimization across endpoints

#### Category 5: Assay Interpretation
Questions about interpreting experimental results and deciding next steps.
- Small molecule: dose-response curves, IC50 interpretation, selectivity panels, ADMET flag triage
- Peptide: MIC interpretation (antimicrobial), hemolysis assays, longitudinal in vivo scoring, multi-endpoint bioactivity profiling

### 4.3 Question Format

Each question is a JSON object:

```json
{
  "id": "SAR-SM-01",
  "category": "SAR Reasoning",
  "domain": "small_molecule",
  "pair_id": "SAR-01",
  "question": "Explain how replacing a phenyl ring with a pyridine ring affects the potency and selectivity of a kinase inhibitor. What factors would you consider?",
  "reference_answer": "Pyridine introduces a hydrogen bond acceptor...",
  "key_concepts": ["bioisosteric replacement", "hydrogen bonding", "pKa shift", "selectivity"],
  "difficulty": "intermediate"
}
```

Fields:
- `id`: unique identifier (`{CATEGORY}-{DOMAIN}-{NUMBER}`)
- `category`: one of the 5 categories
- `domain`: `small_molecule` or `peptide`
- `pair_id`: links matched pairs (e.g., `SAR-01` links `SAR-SM-01` and `SAR-PEP-01`)
- `question`: the prompt sent to the model
- `reference_answer`: gold-standard answer written by the author (domain expert) for scoring calibration
- `key_concepts`: list of concepts a correct answer should include (used as scoring rubric)
- `difficulty`: `basic`, `intermediate`, or `advanced` (balanced across domains)

### 4.4 Question Quality Criteria

Each question must:
1. Have a **definite correct answer** (not purely opinion-based)
2. Require **domain-specific knowledge** (not answerable from general reasoning alone)
3. Be **difficulty-matched** across the pair (a hard peptide question must be paired with a hard small-molecule question)
4. Avoid **leading or biased phrasing** (don't hint at the expected answer)
5. Be **self-contained** (no reference to external data, figures, or prior context)

### 4.5 Question Storage

All questions are stored in a single JSON file:

```
scripts/experiment2/questions.json
```

The file contains an array of 100 question objects. The author writes this file manually (this is the primary effort bottleneck). A validation script checks that all pairs are complete, categories are balanced, and required fields are present.

---

## 5. Execution Pipeline

### 5.1 Directory Structure

```
scripts/experiment2/
├── questions.json              # 100 questions (50 matched pairs)
├── run_probing.py              # Main execution script
├── score_responses.py          # Claude CLI automated scoring (all 400)
├── prepare_expert_subset.py    # Stratified sampling + blind export for expert validation
├── merge_scores.py             # Merge Claude + expert scores, compute agreement
├── analyze_results.py          # Statistical analysis + figure generation
├── validate_questions.py       # Question file validation
├── config.py                   # Model tags, API config, constants
├── responses/                  # Raw model outputs
│   ├── kimi-k2.5.jsonl
│   ├── deepseek-v3.2.jsonl
│   ├── qwen3-next-80b.jsonl
│   └── gemini-3-flash.jsonl
├── scores/                     # Scored responses
│   ├── claude_scores.csv
│   ├── expert_scores.csv
│   ├── agreement_analysis.json
│   └── final_scores.csv
├── results/                    # Analysis outputs
│   ├── summary_table.csv
│   ├── statistical_tests.json
│   └── figures/
│       ├── fig_grouped_bar.pdf
│       └── fig_category_heatmap.pdf
└── README.md                   # Reproduction instructions
```

### 5.2 `config.py`

```python
MODELS = [
    {"name": "Kimi K2.5",       "tag": "kimi-k2.5:cloud"},
    {"name": "DeepSeek V3.2",   "tag": "deepseek-v3.2:cloud"},
    {"name": "Qwen 3 Next 80B", "tag": "qwen3-next:80b-cloud"},
    {"name": "Gemini 3 Flash",  "tag": "gemini-3-flash-preview:cloud"},
]

SYSTEM_PROMPT = (
    "You are a pharmaceutical scientist with expertise in drug discovery. "
    "Answer the following question accurately and concisely. "
    "Include specific numbers, ranges, or examples where relevant. "
    "If you are uncertain, say so rather than guessing."
)

API_DELAY_SECONDS = 3
MAX_RETRIES = 3
RETRY_BASE_SECONDS = 10
TEMPERATURE = 0.3          # Low temperature for consistency
MAX_TOKENS = 1024          # Cap response length
RANDOM_SEED = 42           # For question ordering randomization

# Claude CLI judge config
CLAUDE_CLI = "/home/ubuntu/.local/bin/claude"
CLAUDE_MODEL = "sonnet"    # Claude Sonnet 4.5
CLAUDE_DELAY_SECONDS = 1   # Delay between CLI calls
EXPERT_SUBSET_FRACTION = 0.2  # 20% stratified sample for expert validation
```

### 5.3 `run_probing.py` — Execution Logic

```
1. Load questions from questions.json
2. For each model in MODELS:
   a. Check if a partial response file exists (for resumption)
   b. Shuffle questions with fixed seed (different order per model to avoid position bias)
   c. For each question:
      - Skip if already answered (resumption support)
      - Call Ollama Cloud API with system prompt + question
      - Record: question_id, model, raw_response, latency_ms, timestamp
      - Append to responses/{model}.jsonl (incremental save)
      - Sleep API_DELAY_SECONDS
      - On error: exponential backoff, max MAX_RETRIES, then log failure and continue
3. Print summary: total calls, successes, failures, total time
```

Key design decisions:
- **JSONL format** (one JSON object per line) for incremental writes and crash recovery
- **Per-model files** so models can be run independently or in parallel
- **Fixed random seed per model** for reproducible question ordering
- **Temperature 0.3** for reproducibility (low enough for consistency, high enough to avoid degenerate outputs)

### 5.4 `validate_questions.py` — Pre-flight Checks

Before running the experiment, validate:
- [ ] Exactly 100 questions
- [ ] Exactly 50 unique pair_ids
- [ ] Each pair_id has exactly 2 questions (one small_molecule, one peptide)
- [ ] Each category has exactly 10 small_molecule and 10 peptide questions
- [ ] All required fields are present and non-empty
- [ ] No duplicate question IDs
- [ ] All questions end with a question mark or explicit prompt

---

## 6. Scoring Methodology

### 6.1 Hybrid Approach (Option C)

Scoring uses a two-layer approach: Claude CLI scores all 400 responses automatically, the domain expert validates a stratified 20% subset, and inter-rater agreement validates the automated scores.

| Layer | Who | Responses Scored | Purpose |
|---|---|---|---|
| **Primary** | Claude Sonnet 4.5 via CLI | All 400 | Full coverage, reproducible |
| **Validation** | Expert (author) | 80 (20% stratified) | Ground truth calibration |
| **Agreement** | Cohen's kappa computation | 80 overlapping | Credibility metric |

**Why hybrid, not fully manual:**
- Scoring 400 responses manually takes 3-4 hours and is prone to fatigue drift
- LLM-as-judge is increasingly accepted in evaluation literature (Zheng et al., 2023)
- Expert validation on a stratified subset provides ground truth without full manual effort
- If agreement is high (kappa > 0.7), the Claude scores are credible as primary data
- If agreement is low (kappa < 0.5), fall back to full manual scoring and report the discrepancy

### 6.2 Scoring Rubric (Shared by Both Scorers)

| Score | Label | Criteria |
|---|---|---|
| 0 | Wrong / Hallucinated | Factually incorrect, fabricated data, or nonsensical |
| 1 | Partially Correct | Contains some correct elements but missing key nuance or includes significant errors |
| 2 | Correct | Accurate and reasonably complete; a competent scientist would accept this answer |
| 3 | Expert-Level | Correct with domain-expert nuance, specific quantitative details, or insight beyond textbook knowledge |

### 6.3 Claude CLI Scoring (All 400 Responses)

`score_responses.py` iterates over all 400 responses and calls Claude via CLI:

```
For each response in responses/*.jsonl:
  1. Load the matching question (reference_answer, key_concepts) from questions.json
  2. Construct scoring prompt with rubric + question + reference + model response
  3. Call: echo "<prompt>" | claude -p --model sonnet
  4. Parse integer score (0-3) from stdout
  5. On parse failure: retry once, then flag for manual review
  6. Append to scores/claude_scores.csv
  7. Sleep 1 second between calls (avoid overloading CLI)
```

**Scoring prompt template:**

```
You are an expert pharmaceutical scientist evaluating an AI model's answer
about drug discovery. Score the answer on a 0-3 scale:

0 = Wrong or hallucinated: factually incorrect, fabricated data, or nonsensical
1 = Partially correct: some correct elements but missing key nuance or significant errors
2 = Correct: accurate and reasonably complete
3 = Expert-level: correct with domain-expert nuance, specific quantitative details

Question: {question}
Reference answer: {reference_answer}
Key concepts that should be covered: {key_concepts}

Model's answer to evaluate:
{model_response}

Reply with ONLY a single integer (0, 1, 2, or 3). No explanation.
```

### 6.4 Expert Validation (80-Response Stratified Subset)

The author scores 80 responses (20% of 400) selected by stratified sampling:

**Stratification:** 2 responses per cell in a (4 models x 5 categories x 2 domains) grid = 80 responses. This ensures every combination of model, category, and domain is represented in the validation set.

**Blind protocol for the 80-response subset:**
1. Export the 80 selected responses with columns: `response_id`, `category`, `question_text`, `response_text`
2. **Strip model identity and domain labels**
3. **Randomize row order** with fixed seed
4. Expert scores without knowing which model or domain produced the response
5. After scoring, re-merge with metadata for agreement analysis

**Effort:** ~80 responses at ~30 seconds each = ~40 minutes.

### 6.5 Inter-Rater Agreement

Compute on the 80 overlapping responses:

```python
from sklearn.metrics import cohen_kappa_score

kappa = cohen_kappa_score(expert_scores, claude_scores, weights="quadratic")
```

**Quadratic-weighted kappa** is appropriate because the 0-3 scale is ordinal (a 0-vs-3 disagreement is worse than a 1-vs-2 disagreement).

| Kappa Range | Interpretation | Action |
|---|---|---|
| > 0.8 | Almost perfect agreement | Use Claude scores as primary data with high confidence |
| 0.6 - 0.8 | Substantial agreement | Use Claude scores as primary data, note agreement level |
| 0.4 - 0.6 | Moderate agreement | Report both scores; use expert scores for main analysis |
| < 0.4 | Poor agreement | Discard Claude scores; fall back to full manual scoring |

**Report in the paper:** "Inter-rater agreement between expert and automated scoring (quadratic-weighted Cohen's kappa = X.XX) on a stratified 20% subset (N=80)."

### 6.6 Scoring Storage

```
scripts/experiment2/scores/
├── claude_scores.csv          # All 400 Claude-scored responses
├── expert_scores.csv          # 80 expert-scored responses (validation subset)
├── agreement_analysis.json    # Kappa, confusion matrix, disagreement cases
└── final_scores.csv           # Merged: Claude scores + expert overrides where disagreed
```

**`claude_scores.csv` columns:**
`response_id, question_id, pair_id, category, domain, model, claude_score, parse_success, timestamp`

**`expert_scores.csv` columns:**
`response_id, question_id, pair_id, category, domain, model, expert_score, notes`

**`final_scores.csv` columns:**
`response_id, question_id, pair_id, category, domain, model, final_score, score_source`

Where `score_source` is `claude` (for the 320 non-validated responses) or `expert` (for the 80 validated responses, using expert score as ground truth regardless of agreement).

---

## 7. Statistical Analysis

### 7.1 Primary Test: Paired Wilcoxon Signed-Rank Test

For each model, test:
- H0: no difference in score distribution between small-molecule and peptide questions
- H1: small-molecule scores are systematically higher than peptide scores

**Why Wilcoxon (not t-test):** Scores are ordinal (0-3), not interval. The Wilcoxon signed-rank test is appropriate for paired ordinal data. Each matched pair provides one difference observation.

```python
from scipy.stats import wilcoxon

for model in models:
    sm_scores = [...]   # 50 small-molecule scores
    pep_scores = [...]  # 50 matched peptide scores
    stat, p_value = wilcoxon(sm_scores, pep_scores, alternative="greater")
```

### 7.2 Effect Size: Matched-Pairs Rank-Biserial Correlation

Report effect size `r = Z / sqrt(N)` where Z is the Wilcoxon Z-statistic and N is the number of pairs. Interpretation:
- r < 0.3: small effect
- 0.3 <= r < 0.5: medium effect
- r >= 0.5: large effect

### 7.3 Secondary Analyses

1. **Per-category breakdown:** Mean score (small-molecule vs peptide) for each of the 5 categories, across all models. Identifies which knowledge domains have the largest gaps.
2. **Cross-model consistency:** Friedman test across all 4 models to verify the gap is consistent (not driven by one outlier model).
3. **Aggregate gap:** Pool all models and report overall mean score difference with 95% CI via bootstrap.

### 7.4 Multiple Comparisons

4 models = 4 primary tests. Apply Bonferroni correction: significance threshold = 0.05 / 4 = 0.0125.

---

## 8. Output Deliverables

### 8.1 Figure: Grouped Bar Chart

**File:** `latex/figures/fig-llm-knowledge-probing.pdf`

**Layout:**
- X-axis: 4 model names
- Y-axis: Mean score (0-3 scale)
- Two bars per model: blue (small-molecule), orange (peptide)
- Error bars: 95% CI (bootstrap, 1000 resamples)
- Horizontal dashed line at score 2.0 ("correct" threshold)
- Significance stars above paired bars (* p < 0.05, ** p < 0.01, *** p < 0.001 after Bonferroni)

**Color palette:** Okabe-Ito (consistent with other paper figures):
- Small molecule: Sky Blue (#56B4E9)
- Peptide: Vermillion (#D55E00)

**Style:** Match existing paper figures (see `scripts/generate_fig6_pareto.py` for style reference). Off-white background (#FAFAFA), charcoal axes (#333333), 300 DPI.

### 8.2 Table: Per-Category Score Breakdown

**For the paper body or appendix:**

| Category | SM Mean (SD) | Pep Mean (SD) | Gap | p-value |
|---|---|---|---|---|
| SAR Reasoning | 2.4 (0.5) | 1.6 (0.7) | -0.8 | 0.003 |
| ADMET/PK | ... | ... | ... | ... |
| Generative Design | ... | ... | ... | ... |
| Optimization | ... | ... | ... | ... |
| Assay Interpretation | ... | ... | ... | ... |

(Aggregated across all 4 models; per-model tables go in appendix)

### 8.3 Raw Data Package

For reproducibility (included in arXiv supplementary or GitHub repo):
- `questions.json` (all 100 questions with reference answers)
- `responses/*.jsonl` (raw model outputs)
- `scores/claude_scores.csv` (automated scores for all 400)
- `scores/expert_scores.csv` (expert validation scores for 80)
- `scores/agreement_analysis.json` (inter-rater agreement metrics)
- `scores/final_scores.csv` (merged final scores used in analysis)
- `results/statistical_tests.json` (all test statistics)
- `README.md` (reproduction instructions)

---

## 9. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Ollama Cloud rate-limits free tier mid-experiment | Medium | Medium | Incremental save + resumption. Split across 2 days. Upgrade to Pro ($20) if needed. |
| One model refuses to answer drug questions (safety filter) | Low | Low | Log refusals as data (score 0). A refusal is itself evidence of the bias. |
| The gap is smaller than expected (< 10%) | Medium | High | Report the actual result honestly. Even a small systematic gap across 4 models is publishable. Shift framing to "models are improving but gaps persist in specific categories." |
| Claude CLI judge disagrees with expert (kappa < 0.4) | Low-Medium | High | Fall back to full manual scoring (3-4 hours). Report the discrepancy as a finding about LLM evaluation limitations. |
| Claude CLI rate-limited or unavailable | Low | Medium | Batch scoring across multiple sessions. CLI uses existing subscription, no separate quota. |
| A model produces very long responses that are hard to score | Low | Low | Cap at MAX_TOKENS=1024. Instruct models to be concise in system prompt. |
| Ollama Cloud deprecates a model tag before paper review | Low | Medium | Pin exact model tags in paper. Archive all raw responses. Results are reproducible from archived data even if models become unavailable. |

---

## 10. Timeline

| Day | Activity | Output |
|---|---|---|
| Day 1 | Write 50 matched question pairs with reference answers | `questions.json` |
| Day 1 | Implement `config.py`, `validate_questions.py`, `run_probing.py` | Scripts ready |
| Day 2 | Run experiment: all 4 models x 100 questions | `responses/*.jsonl` |
| Day 2 | Implement `score_responses.py` (Claude CLI judge) | Scoring script ready |
| Day 2 | Run Claude CLI scoring on all 400 responses (~15 min) | `scores/claude_scores.csv` |
| Day 2 | Run `prepare_expert_subset.py`, expert scores 80 responses (~40 min) | `scores/expert_scores.csv` |
| Day 3 | Run `merge_scores.py`, compute agreement (kappa) | `scores/final_scores.csv` |
| Day 3 | Implement `analyze_results.py`, generate figures and tables | Final outputs |
| Day 3 | Write results subsection for paper (~500-700 words) | LaTeX section |

**Total: 3 days, ~$0-20 cost.**

---

## 11. Success Criteria

### SC-1: Experiment Execution Completeness

- [ ] All 100 questions are well-formed and pass `validate_questions.py`
- [ ] All 50 matched pairs have balanced difficulty across domains
- [ ] All 4 models produce responses for all 100 questions (400 total responses)
- [ ] Response failure rate < 5% (fewer than 20 failures out of 400 calls)
- [ ] All responses are saved incrementally and the experiment is resumable

### SC-2: Statistical Rigor

- [ ] Wilcoxon signed-rank test is computed for each model (4 tests)
- [ ] Bonferroni correction is applied (threshold p < 0.0125)
- [ ] Effect sizes are reported with matched-pairs rank-biserial correlation
- [ ] At least 2 of 4 models show statistically significant gap (p < 0.0125) for the central claim to hold
- [ ] If fewer than 2 models show significance, the paper honestly reports this and adjusts the claim

### SC-3: Scoring Integrity

- [ ] All 400 responses are scored by Claude CLI (`scores/claude_scores.csv` has 400 rows)
- [ ] Claude score parse success rate > 95% (fewer than 20 parse failures out of 400)
- [ ] 80 stratified responses are scored by the domain expert (`scores/expert_scores.csv` has 80 rows)
- [ ] Expert scoring is blind (model identity and domain stripped during scoring)
- [ ] Expert scoring order is randomized with a fixed seed
- [ ] Quadratic-weighted Cohen's kappa is computed on the 80 overlapping responses
- [ ] If kappa >= 0.6: Claude scores used as primary data (report kappa in paper)
- [ ] If kappa < 0.4: fall back to full manual scoring of all 400 responses
- [ ] Agreement analysis is saved to `scores/agreement_analysis.json`

### SC-4: The Central Finding Holds

The experiment succeeds in supporting the paper's thesis if:
- [ ] Mean peptide score is lower than mean small-molecule score for **all 4 models** (direction consistency)
- [ ] The gap is statistically significant for **at least 2 of 4 models** after Bonferroni correction
- [ ] The effect is **not driven by a single category** (at least 3 of 5 categories show the same directional gap)
- [ ] The effect size is at least "medium" (r >= 0.3) for the aggregate analysis

If the gap is present but not statistically significant (e.g., p = 0.05-0.10 after correction), the finding is still reportable as a "consistent trend" with reduced claim strength.

### SC-5: Negative Result Protocol

If the central finding does **not** hold (peptide scores are comparable to or higher than small-molecule scores):
- [ ] Report the result honestly; do not cherry-pick or re-run with different questions
- [ ] Reframe the contribution: "Foundation models have closed the peptide knowledge gap, but agent architectures have not yet caught up" (this still supports the paper's thesis, just at a different layer)
- [ ] The experiment is still a valid contribution as a benchmark of LLM pharmaceutical knowledge

### SC-6: Figure Quality

- [ ] Grouped bar chart is generated as PDF at 300 DPI
- [ ] Chart uses Okabe-Ito colorblind-safe palette consistent with other paper figures
- [ ] Error bars show 95% CI (bootstrap)
- [ ] Significance stars are correctly placed
- [ ] Figure is self-explanatory with axis labels, legend, and title
- [ ] Figure renders correctly when included in LaTeX document

### SC-7: Reproducibility

- [ ] All code, questions, and raw data are committed to the repository
- [ ] `README.md` in `scripts/experiment2/` contains step-by-step reproduction instructions
- [ ] A reviewer can reproduce the probing phase by: (1) creating an Ollama account, (2) setting `OLLAMA_API_KEY`, (3) running `python run_probing.py`
- [ ] A reviewer can reproduce the scoring phase by: (1) having a Claude subscription, (2) running `python score_responses.py`, or (3) using the archived `scores/claude_scores.csv` directly
- [ ] A reviewer without Claude access can still reproduce analysis from archived scores: `python analyze_results.py`
- [ ] Random seed is fixed for question ordering, stratified sampling, and statistical bootstrapping

### SC-8: Paper Integration

- [ ] Results are written as a ~500-700 word subsection in the LaTeX paper
- [ ] The subsection includes: motivation, methodology summary, key finding, figure reference, and limitations
- [ ] The BibTeX file includes any new references cited in the methodology (e.g., Wilcoxon test, effect size measures)
- [ ] The figure is referenced in the paper with `\ref{}` and has a proper caption

---

## 12. Out of Scope

The following are explicitly **not** part of this experiment:
- Testing proprietary models (GPT-4, Claude, etc.) as subjects — addressed by the "4 independent training pipelines" argument. Note: Claude is used as a *judge*, not as a test subject, so there is no conflict.
- Fine-tuning or retraining any model
- Testing models on actual drug design tasks (that is Experiment #8)
- Building a benchmark dataset for community use (future work)
- Comparing against human expert baselines (out of scope for this paper)
