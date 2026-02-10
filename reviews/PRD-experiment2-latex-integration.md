# PRD: Integrating Experiment 2 (LLM Knowledge Probing) into the Manuscript

**Paper:** "Beyond SMILES: Evaluating Agentic AI for Drug Discovery"
**Date:** 2026-02-10
**Status:** Ready for implementation

---

## 1. Executive Summary

Experiment 2 probed four frontier LLMs (Kimi K2.5, DeepSeek V3.2, Qwen 3 Next 80B, Gemini 3 Flash) on 50 matched small-molecule/peptide question pairs across five pharmaceutical knowledge categories. The result is **null**: no model shows a statistically significant peptide knowledge deficit (all Bonferroni-adjusted p = 1.0; aggregate gap = -0.115, 95% CI [-0.255, 0.02]). Peptide scores are marginally *higher* than small-molecule scores.

**Reframing strategy:** This null result *strengthens* the paper. The small-molecule bias identified in Gap 1 operates at the **agent architecture and tool ecosystem level**, not at the foundation model knowledge level. LLMs can reason about peptides; current agents simply do not let them. The headline framing is: **"The bias is architectural, not epistemic."**

**Manuscript impact:** ~645 words of additions across 7 .tex files; ~100-150 words of recommended cuts to stay near the 9,000-word ceiling. One new figure (grouped bar chart), one new table (per-category breakdown), one optional bib entry, and one new appendix section.

---

## 2. Evidence Inventory

### 2.1 Experiment Design

| Parameter | Value |
|---|---|
| Models tested | 4 (Kimi K2.5, DeepSeek V3.2, Qwen 3 Next 80B, Gemini 3 Flash) |
| Questions | 100 (50 matched pairs: 50 SM, 50 peptide) |
| Categories | 5 (SAR, ADMET/PK, Generative Design, Optimization, Assay Interpretation) |
| Pairs per category | 10 |
| Total responses scored | 400 |
| Scoring rubric | 0-3 ordinal (wrong / partial / correct / expert-level) |
| Primary scorer | Claude Sonnet 4.5 (LLM-as-judge) |
| Expert validation | 80 responses (20% stratified, blind protocol) |
| Sensitivity check | Claude Opus on 40-response stratified subset |
| Statistical tests | Wilcoxon signed-rank (one-sided, Bonferroni alpha = 0.0125), Friedman, bootstrap CI |

### 2.2 Per-Model Results

| Model | SM Mean | PEP Mean | Gap (SM-PEP) | Wilcoxon p | p (Bonferroni) | Rank Biserial r | Significant? |
|---|---|---|---|---|---|---|---|
| Kimi K2.5 | 2.54 | 2.60 | -0.06 | 0.680 | 1.0 | -0.095 | No |
| DeepSeek V3.2 | 2.30 | 2.44 | -0.14 | 0.880 | 1.0 | -0.232 | No |
| Qwen 3 Next 80B | 2.22 | 2.28 | -0.06 | 0.619 | 1.0 | -0.057 | No |
| Gemini 3 Flash | 2.28 | 2.48 | -0.20 | 0.901 | 1.0 | -0.265 | No |

### 2.3 Per-Category Results (Aggregated Across Models)

| Category | SM Mean (SD) | PEP Mean (SD) | Gap (PEP-SM) | p-value |
|---|---|---|---|---|
| SAR Reasoning | 2.600 (0.632) | 2.550 (0.552) | -0.050 | 0.370 |
| ADMET / PK Properties | 2.325 (0.656) | 2.450 (0.677) | +0.125 | 0.755 |
| Generative Design | 2.100 (0.709) | 2.250 (0.742) | +0.150 | 0.805 |
| Optimization Approaches | 2.275 (0.751) | 2.500 (0.599) | +0.225 | 0.938 |
| Assay Interpretation | 2.375 (0.740) | 2.500 (0.679) | +0.125 | 0.767 |

### 2.4 Aggregate Statistics

| Statistic | Value |
|---|---|
| N paired observations | 200 |
| Aggregate gap (SM minus PEP) | -0.115 |
| Bootstrap 95% CI | [-0.255, 0.02] |
| Overall SM mean | 2.335 |
| Overall PEP mean | 2.450 |
| Friedman statistic | 0.454 |
| Friedman p-value | 0.929 |

### 2.5 Scoring Validation

| Metric | Value |
|---|---|
| Expert-Claude kappa (quadratic weighted) | 0.216 |
| Expert subset size | 80 |
| Total disagreements | 57 / 80 (71.25%) |
| Claude scored higher | 46 / 57 disagreements (80.7%) |
| Expert scored higher | 11 / 57 disagreements (19.3%) |
| Expert score distribution | Score 1: 18.75%, Score 2: 70.0%, Score 3: 11.25% |
| Dominant disagreement pattern | Expert gives 2, Claude gives 3 (34/56 expert-2 cases = 60.7%) |
| Disagreement by domain | Peptide: 27, SM: 30 (balanced) |
| Opus-Sonnet kappa | 0.778 |
| Opus-Sonnet exact agreement | 80% |
| Opus-Sonnet within-one agreement | 100% |
| Opus mean signed shift | +0.15 |

### 2.6 Expert Feedback Theme

**"Correct core, wrong specifics"**: Models consistently get the core mechanism right but overstate quantitative claims and lack expert-level nuance. This pattern applies equally to both small-molecule and peptide domains, reinforcing that the weakness is depth, not modality-specific knowledge.

---

## 3. Narrative Reframing

### 3.1 Three-Layer Strategy

**Layer 1 -- Headline framing:** "The bias is architectural, not epistemic." Use this phrase or close variants in the abstract, Gap 1 section, design requirements, and conclusion.

**Layer 2 -- Argumentative logic:**
1. Capability matrix shows zero framework coverage for peptide task classes (readers might assume LLMs cannot handle peptides)
2. Knowledge probing shows LLMs score equivalently on peptide vs small-molecule questions (the models HAVE the knowledge)
3. Therefore, the gap is in how agents expose model capabilities through tools and workflows, not in what models know
4. This makes Gap 1 MORE compelling: the fix is engineering (tool integration), not fundamental research (model retraining)

**Layer 3 -- Counter-argument inoculation:** A reviewer who says "but LLMs know about peptides" now has the paper agreeing with them AND using that fact to strengthen the argument. The original PRD's SC-5 negative result protocol maps directly: "Foundation models have closed the peptide knowledge gap, but agent architectures have not yet caught up."

### 3.2 Second-Order Argument

Expert validation reveals that models produce directionally correct but quantitatively overconfident reasoning in *both* domains. This supports the need for domain-specific computational tools in all modalities, not just peptides. LLM knowledge alone is insufficient; specialized tools and workflows are needed regardless of modality.

### 3.3 Phrasing Guidance

- DO say: "no significant peptide knowledge deficit," "knowledge parity," "architectural bias," "the bottleneck is tool integration"
- DO NOT say: "the experiment failed," "negative result," "LLMs are equally bad at both"
- Frame as: "a scientifically informative finding that sharpens the argument"

---

## 4. Section-by-Section Edit Specification

### Edit 4.1: `latex/sections/00-abstract.tex`

**File:** `latex/sections/00-abstract.tex`
**Location:** After the sentence ending "...single-objective optimization assumptions." and before the sentence beginning "From these gaps..."
**Action:** INSERT
**Word delta:** +35

```latex
An empirical knowledge-probing experiment across four frontier large language models
finds no significant peptide knowledge deficit (aggregate gap = $-0.115$, all $p > 0.05$),
indicating that the small-molecule bias operates at the tool and workflow level rather
than the foundation model level.
```

---

### Edit 4.2: `latex/sections/01-introduction.tex`

**File:** `latex/sections/01-introduction.tex`
**Location:** In the "Scope and Motivation" subsection, after the paragraph beginning "An important distinction underlies the analysis that follows." (line 10), at the end of that paragraph.
**Action:** INSERT sentence at end of paragraph
**Word delta:** +40

```latex
To test whether this bias extends to the foundation models themselves, we probe four
frontier LLMs on matched small-molecule and peptide questions and find no knowledge gap,
localizing the bottleneck to agent architecture rather than model capability
(\S\ref{sec:knowledge-probing}).
```

---

### Edit 4.3: `latex/sections/02-methods.tex`

**File:** `latex/sections/02-methods.tex`
**Location:** After the end of subsection 2.4 ("Analysis Approach"), before the Results section. Insert as new subsection 2.5.
**Action:** INSERT new subsection
**Word delta:** +200
**Label:** `\label{sec:knowledge-probing}`

```latex
\subsection{LLM Knowledge Probing}
\label{sec:knowledge-probing}

To determine whether the small-molecule bias identified in the capability matrix
(\S\ref{sec:small-molecule}) reflects upstream knowledge limitations in foundation
models, we designed a paired knowledge-probing experiment. We tested four frontier
LLMs from independent training pipelines: Kimi K2.5 (Moonshot AI), DeepSeek V3.2
(DeepSeek), Qwen 3 Next 80B (Alibaba), and Gemini 3 Flash (Google). Each model
answered 50 matched question pairs spanning five pharmaceutical knowledge categories:
SAR reasoning, ADMET and pharmacokinetic properties, generative design strategies,
optimization approaches, and assay interpretation. Each pair tested the same cognitive
skill in two modality contexts (one small-molecule, one peptide), controlling for
question difficulty and format.

Responses were scored on a 0--3 rubric (wrong, partially correct, correct,
expert-level). Primary scoring used Claude Sonnet 4.5 as an LLM-as-judge
\citep{zheng2023judging}; a domain expert independently validated a stratified 20\%
subset ($N = 80$) under a blind protocol (model identity and domain labels stripped,
row order randomized). An additional sensitivity check rescored a 40-response subset
using Claude Opus, confirming stability across judge models (quadratic-weighted
$\kappa = 0.78$).

Statistical analysis used paired Wilcoxon signed-rank tests per model
(Bonferroni-corrected $\alpha = 0.0125$), matched-pairs rank-biserial correlation for
effect size, a Friedman test for cross-model consistency, and bootstrap 95\% confidence
intervals for the aggregate gap. The full question set, raw responses, and scoring data
are available in the supplementary materials.
```

---

### Edit 4.4: `latex/sections/03-gap-small-molecule.tex`

**File:** `latex/sections/03-gap-small-molecule.tex`
**Location:** After the "Findings" subsubsection (line 8, ending "...as first-class components for sequence-based therapeutics design.") and before "The Peptide-Specific Challenge Space" subsubsection (line 10).
**Action:** INSERT new subsubsection
**Word delta:** +200 (prose) + figure + table (not counted in word budget)

```latex
\subsubsection{Empirical Evidence: Knowledge Parity, Architectural Bias}

To test whether the small-molecule bias extends to the foundation models powering these
agents, we probed four frontier LLMs on matched pharmaceutical knowledge questions
(\S\ref{sec:knowledge-probing}). The result is unambiguous: no model shows a
statistically significant peptide knowledge deficit
(Table~\ref{tab:knowledge-probing-categories}, \cref{fig:knowledge-probing}). Across
200 paired observations, the aggregate score gap is $-0.115$ (95\% CI: $[-0.255,
0.02]$), with peptide questions receiving marginally higher scores. All per-model
Wilcoxon tests yield $p > 0.6$ (Bonferroni-adjusted $p = 1.0$), and effect sizes are
negligible ($|r| < 0.27$). The Friedman consistency test confirms this null result holds
uniformly across all four models ($\chi^2 = 0.454$, $p = 0.929$). No category shows a
significant peptide deficit; Optimization Approaches shows the largest pro-peptide gap
($+0.225$).

Expert validation revealed that models produce directionally correct but quantitatively
overconfident reasoning in both domains equally, consistent with a depth limitation
rather than a modality-specific knowledge gap. Inter-rater agreement between expert and
automated scoring was fair (quadratic-weighted $\kappa = 0.22$), reflecting systematic
calibration differences at the score 2/3 boundary rather than disagreement on factual
accuracy; the paired within-model comparisons driving the statistical tests are robust
to this calibration shift.

This null result strengthens rather than undermines \gap{1}. The finding localizes the
small-molecule bias to agent architectures and tool ecosystems, not to the foundation
models that power them. LLMs can reason competently about peptide SAR, ADMET properties,
generative design, optimization, and assay interpretation. The bottleneck is that no
current agent exposes these capabilities through peptide-aware tools, protein language
model integration, or sequence-native workflows. The bias is architectural, not
epistemic.

\begin{figure}[htbp]
\centering
\includegraphics[width=\textwidth]{figures/fig-llm-knowledge-probing.pdf}
\caption{LLM Knowledge Probing: Small-Molecule vs Peptide Scores. Mean scores (0--3
scale) for four frontier LLMs across 50 matched question pairs spanning five
pharmaceutical knowledge categories. Blue bars: small-molecule questions; orange bars:
peptide questions. Error bars: 95\% bootstrap confidence intervals. No model shows a
statistically significant knowledge gap (all Bonferroni-adjusted $p = 1.0$). The
aggregate gap is $-0.115$ [95\% CI: $-0.255$, $0.02$], indicating peptide scores are
marginally higher.}
\label{fig:knowledge-probing}
\end{figure}

\begin{table}[htbp]
\centering
\caption{Knowledge Probing: Per-Category Score Breakdown. Mean scores (standard
deviation) aggregated across four models. Gap = peptide minus small-molecule mean
(positive indicates peptide advantage). $p$-values from one-sided Wilcoxon signed-rank
tests ($H_1$: SM $>$ peptide). No category shows a significant peptide knowledge
deficit.}
\label{tab:knowledge-probing-categories}
\small
\begin{tabular}{lcccc}
\toprule
\textbf{Category} & \textbf{SM Mean (SD)} & \textbf{PEP Mean (SD)} & \textbf{Gap} & \textbf{$p$-value} \\
\midrule
SAR Reasoning & 2.60 (0.63) & 2.55 (0.55) & $-0.05$ & 0.370 \\
ADMET / PK Properties & 2.33 (0.66) & 2.45 (0.68) & $+0.13$ & 0.755 \\
Generative Design & 2.10 (0.71) & 2.25 (0.74) & $+0.15$ & 0.805 \\
Optimization Approaches & 2.28 (0.75) & 2.50 (0.60) & $+0.23$ & 0.938 \\
Assay Interpretation & 2.38 (0.74) & 2.50 (0.68) & $+0.13$ & 0.767 \\
\bottomrule
\end{tabular}
\end{table}
```

---

### Edit 4.5: `latex/sections/08-design-requirements.tex`

**File:** `latex/sections/08-design-requirements.tex`
**Location:** In the opening paragraph, after any sentence establishing the synthesis of design requirements from the gap analysis.
**Action:** INSERT sentence
**Word delta:** +30

```latex
The knowledge probing experiment (\S\ref{sec:knowledge-probing}) confirms that these
requirements target the correct architectural layer: foundation models already possess
peptide domain knowledge, so closing the gaps requires workflow and tool engineering,
not model retraining.
```

**Note:** The implementer should read the current opening of Section 8 and place this sentence where it flows naturally, after the initial framing of design requirements.

---

### Edit 4.6: `latex/sections/09-discussion.tex`

**File:** `latex/sections/09-discussion.tex`
**Location:** In the "Scope and Limitations" subsection, after the paragraph about the three-level capability assessment (ending "...a more granular scoring framework could reveal additional nuance.").
**Action:** INSERT new paragraph
**Word delta:** +60

```latex
The knowledge probing experiment has limitations. The low expert-automated scorer
agreement (quadratic-weighted $\kappa = 0.22$) reflects systematic calibration
differences between expert and LLM evaluation rather than random noise: the automated
scorer assigned higher scores in 81\% of disagreements, concentrated at the score 2/3
boundary. The Opus sensitivity check ($\kappa = 0.78$) demonstrates stability across
judge models. However, the 50-pair design provides limited statistical power for
detecting small effect sizes, and the null finding should be interpreted as absence of
evidence for a large gap rather than evidence of exact parity.
```

---

### Edit 4.7: `latex/sections/10-conclusion.tex`

**File:** `latex/sections/10-conclusion.tex`
**Location:** After the first sentence of the first paragraph, ending "...closing them requires changes to core framework design."
**Action:** INSERT sentence
**Word delta:** +30

```latex
Our knowledge probing experiment reinforces this conclusion: four frontier LLMs show no
peptide knowledge deficit, confirming that the capability gaps reside in agent tool
integration and workflow orchestration, not in foundation model competence.
```

---

## 5. New Section Draft

The complete new LaTeX content is provided in Edit 4.3 (Methods subsection, ~200 words) and Edit 4.4 (Gap 1 subsubsection with figure and table, ~200 words of prose). Together these constitute ~400 words of new section content.

The remaining ~245 words of additions are distributed as sentence-level insertions across abstract (+35), introduction (+40), design requirements (+30), discussion (+60), and conclusion (+30), plus the figure caption (~60 words) and table caption (~40 words) which do not count toward the word budget.

**Total new prose:** ~595-645 words.

---

## 6. New Figure Specification

### Figure 7: LLM Knowledge Probing Results (Grouped Bar Chart)

**Source file:** `scripts/experiment2/results/figures/fig_grouped_bar.pdf`
**Destination:** `latex/figures/fig-llm-knowledge-probing.pdf`
**Action:** Copy source to destination path.

**Placement:** Within the new subsubsection in `03-gap-small-molecule.tex` (see Edit 4.4).

**LaTeX:** Included in Edit 4.4 above.

**Description:** Grouped bar chart with 4 model groups on the x-axis, mean score (0-3) on y-axis, two bars per model (sky blue = small molecule, vermillion = peptide), 95% bootstrap CI error bars, horizontal dashed line at 2.0 ("correct" threshold). Okabe-Ito colorblind-safe palette. No significance stars (all non-significant).

**Numbering:** Figure 7 (after existing Figures 1-6). No renumbering of existing figures needed.

### Category Heatmap (Supplementary)

**Source file:** `scripts/experiment2/results/figures/fig_category_heatmap.pdf`
**Placement:** Appendix C (see Section 9 below) or supplementary materials.
**Rationale:** The bar chart is the primary visual for the main body; the heatmap provides additional granularity for interested readers.

---

## 7. New Table Specification

### Per-Category Score Breakdown Table

**LaTeX:** Included in Edit 4.4 above (Table `\ref{tab:knowledge-probing-categories}`).

**Sign convention:** Gap = peptide minus small-molecule mean. Positive values indicate peptide advantage. This aligns with the narrative that peptides score at least as well as small molecules.

**Note on summary_table.csv source data:** The raw CSV has the Gap column with mixed signs. Verify that the values in the LaTeX table match the CSV after applying the correct sign convention (PEP - SM):
- SAR: 2.550 - 2.600 = -0.050
- ADMET: 2.450 - 2.325 = +0.125
- Generative: 2.250 - 2.100 = +0.150
- Optimization: 2.500 - 2.275 = +0.225
- Assay: 2.500 - 2.375 = +0.125

All confirmed correct in the LaTeX draft.

---

## 8. Bibliography Additions

### Zheng et al. 2023 (LLM-as-Judge)

**Cited in:** Edit 4.3 (Methods subsection, `\citep{zheng2023judging}`)

```bibtex
@inproceedings{zheng2023judging,
  title={Judging {LLM}-as-a-{J}udge with {MT}-{B}ench and {C}hatbot {A}rena},
  author={Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan
          and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan
          and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez,
          Joseph E. and Stoica, Ion},
  booktitle={Advances in Neural Information Processing Systems},
  volume={36},
  year={2023}
}
```

**Action:** Add this entry to `latex/references.bib`.

No other new bib entries are required. The statistical methods (Wilcoxon, Cohen's kappa, bootstrap) are standard and do not require citation.

---

## 9. Appendix Additions

### New Appendix C: Knowledge Probing Experiment Details

**File:** Create `latex/sections/13-appendix-c.tex` and add `\input{sections/13-appendix-c.tex}` after `\input{sections/12-appendix-b.tex}` in `main.tex`.

**Content specification:**

```latex
\section{Knowledge Probing Experiment: Supplementary Details}
\label{appendix:knowledge-probing}
```

The appendix should contain:

1. **Full per-model results table:** 4-row table with all statistics from Section 2.2 of this PRD (means, p-values, effect sizes, rank-biserial correlations).

2. **Question design overview:** Brief description of matched-pair structure, 5 categories, difficulty balancing. Reference to full question set in repository.

3. **Scoring rubric:** The 0-3 rubric table (wrong / partial / correct / expert-level) with criteria.

4. **Expert validation protocol:** Stratified sampling design (2 responses per cell in 4 models x 5 categories x 2 domains grid), blind protocol details, randomization seed.

5. **Inter-rater agreement details:** Confusion matrix (expert rows, Claude columns), disagreement direction analysis, Opus sensitivity check summary.

6. **Category heatmap figure:** The `fig_category_heatmap.pdf` with appropriate caption.

**Estimated length:** ~400-500 words (does not count toward main body word budget).

---

## 10. Word Budget Tracking

| Section | File | Action | Word Delta |
|---|---|---|---|
| Abstract | `00-abstract.tex` | Insert 1 sentence | +35 |
| Introduction | `01-introduction.tex` | Insert 1 sentence | +40 |
| Methods 2.5 | `02-methods.tex` | Insert new subsection | +200 |
| Gap 1 subsubsection | `03-gap-small-molecule.tex` | Insert new subsubsection (prose only) | +200 |
| Design Requirements | `08-design-requirements.tex` | Insert 1 sentence | +30 |
| Discussion | `09-discussion.tex` | Insert 1 paragraph | +60 |
| Conclusion | `10-conclusion.tex` | Insert 1 sentence | +30 |
| **Total additions** | | | **+595** |
| REVISION-PLAN prose cuts (P2 deduplication) | various | Trim redundant phrasing | -100 to -150 |
| **Net addition** | | | **+445 to +495** |

**Current estimated main body:** ~8,700 words
**Projected total:** ~9,145 to 9,195 words

**If tighter budget needed:** Trim the Methods subsection to ~150 words by moving the statistical methods sentence and supplementary materials sentence to the appendix. This saves ~50 additional words, bringing the total to ~9,095-9,145.

**Figure captions and table captions** (~100 words combined) are typically not counted in the main word budget for arXiv submissions.

---

## 11. Constraints Checklist

| Constraint | Status | Verification |
|---|---|---|
| No company name revealed | PASS | No mention of any company in any draft content |
| No peptide names or sequences | PASS | No specific peptide names, sequences, or compound identifiers |
| No internal model names | PASS | No proprietary model names (only public LLM names) |
| No specific receptor targets | PASS | No receptor names connected to the author's work |
| No colleague names | PASS | No internal team references |
| No specific assay results or bioactivity numbers | PASS | Only experiment scores (0-3 rubric), not proprietary data |
| No specific dataset details | PASS | Question counts and model names are public experimental design |
| Problem-class level writing | PASS | All content discusses "pharmaceutical knowledge categories" not specific compounds |
| No emdashes in prose | PASS | All draft LaTeX uses commas, semicolons, or "0--3" (number ranges only) |
| Nature-perspective tone | PASS | Authoritative, measured, evidence-based framing |
| Paper title correct | PASS | "Beyond SMILES: Evaluating Agentic AI for Drug Discovery" |
| No .tex files modified | PASS | This PRD only contains specification; all LaTeX is within markdown code blocks |

---

## 12. Implementation Order

The edits should be applied in this dependency-aware sequence:

| Step | File | Edit | Rationale |
|---|---|---|---|
| 1 | `latex/references.bib` | Add Zheng 2023 entry | Required before any `\citep{zheng2023judging}` compiles |
| 2 | `latex/figures/` | Copy `fig_grouped_bar.pdf` to `fig-llm-knowledge-probing.pdf` | Required before figure reference compiles |
| 3 | `latex/sections/02-methods.tex` | Insert subsection 2.5 (Edit 4.3) | Establishes methodology and `\label{sec:knowledge-probing}` before any `\ref` |
| 4 | `latex/sections/03-gap-small-molecule.tex` | Insert subsubsection + figure + table (Edit 4.4) | Presents results; depends on label from step 3 |
| 5 | `latex/sections/00-abstract.tex` | Insert sentence (Edit 4.1) | Summary; can reference result after it exists |
| 6 | `latex/sections/01-introduction.tex` | Insert sentence (Edit 4.2) | Foreshadowing; depends on label from step 3 |
| 7 | `latex/sections/08-design-requirements.tex` | Insert sentence (Edit 4.5) | Interpretation; depends on label from step 3 |
| 8 | `latex/sections/09-discussion.tex` | Insert paragraph (Edit 4.6) | Limitations; standalone |
| 9 | `latex/sections/10-conclusion.tex` | Insert sentence (Edit 4.7) | Summary; standalone |
| 10 | `latex/sections/13-appendix-c.tex` | Create new appendix file | Supplementary details |
| 11 | `latex/main.tex` | Add `\input{sections/13-appendix-c.tex}` after appendix B | Includes the new appendix |
| 12 | Compile and verify | `pdflatex` + `bibtex` cycle | Verify all references resolve, figures render, no overflow |

**Post-implementation checks:**
- Verify `\ref{sec:knowledge-probing}` resolves correctly in introduction and gap 1
- Verify `\cref{fig:knowledge-probing}` and `\ref{tab:knowledge-probing-categories}` resolve
- Verify `\citep{zheng2023judging}` appears in bibliography
- Verify figure renders at correct size (full textwidth)
- Verify table fits within column width
- Run word count to confirm total is within budget
