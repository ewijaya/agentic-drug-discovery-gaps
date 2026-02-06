# Revision Plan: "The Blind Spots of Agentic Drug Discovery"

**Created:** 2026-02-06
**Based on:** 5-reviewer stress-test (reviews 01-05)
**Current word count:** ~7,200 (estimated from LaTeX source)
**Target word count:** 6,000-8,000
**Word budget remaining:** ~800 words net addition

---

## Success Criteria

The revision is complete when:

1. No reviewer-identified factual error remains uncorrected
2. All five gap claims withstand devil's-advocate counter-evidence from 2025-2026
3. The tool-vs-agent distinction is explicitly stated and used consistently
4. Confidentiality audit remains PASS (no new identifying details introduced)
5. Zero emdashes; tone stays "authoritative but accessible" throughout
6. References include at least 5 papers from mid-2025 onward
7. Paper remains within 6,000-8,000 word target

---

## Tier 1: Must-Fix (blocks submission)

### MF-01. Add tool-vs-agent framing to Introduction

| Field | Detail |
|---|---|
| **Files** | `latex/sections/01-introduction.tex` |
| **What to change** | After the current paragraph ending "narrowly scoped" (line 8), add a new paragraph defining the paper's core analytical distinction: individual tools addressing aspects of each gap are emerging, but the blind spots are the absence of agentic *workflow integration*, not the absence of individual capabilities. This is the thesis that makes every gap claim defensible. |
| **Specific location** | After "This is the practical gap practitioners encounter in day-to-day work." (end of line 8) |
| **Word count impact** | +60-80 words |
| **Why must-fix** | Without this framing, Gaps 1, 3, and 5 are vulnerable to "but PepTune/Agentomics/PMMG exist" rebuttals. This single paragraph inoculates the entire paper. |
| **Reviewer source** | Devil's Advocate (primary), Structure & Logic |
| **Success criterion** | A reader encountering PepTune or Agentomics can reconcile those tools with the paper's claims without contradiction. |

---

### MF-02. Acknowledge recent counter-evidence in Gap 1 (Section 2)

| Field | Detail |
|---|---|
| **Files** | `latex/sections/02-gap-small-molecule.tex`, `latex/references.bib` |
| **What to change** | In the "Protein Language Models vs Molecular Fingerprints" subsection (after line 25, the PLM descriptions), add a paragraph acknowledging: (a) PepTune (ICML 2025) as a multi-objective peptide design system using a masked diffusion PLM + MCTS; (b) PepMLM (Nature Biotechnology, Aug 2025) as ESM-2-based peptide binder design; (c) TxGemma/Agentic-Tx's peptide sequence handling. Then sharpen: these are peptide-aware *models* but not peptide-aware *agents* supporting end-to-end workflow orchestration (proprietary fine-tuning, active learning, iterative design-test cycles). |
| **Specific location** | New paragraph after line 25 ("ProtBERT fine-tuning enables transfer learning with fewer than 100 examples.") |
| **Word count impact** | +80-100 words |
| **New bib entries** | `peptune2024`, `pepmlm2025` (add to `references.bib`) |
| **Why must-fix** | PepTune was at ICML 2025 and PepMLM in Nature Biotechnology. A reviewer who cites these and finds no acknowledgment will question the paper's currency. |
| **Reviewer source** | Devil's Advocate |
| **Success criterion** | Gap 1 claim shifts from "no peptide tools exist" to "peptide-aware models are emerging but lack agentic workflow integration." |

---

### MF-03. Acknowledge recent counter-evidence in Gap 3 (Section 4)

| Field | Detail |
|---|---|
| **Files** | `latex/sections/04-gap-multi-paradigm.tex`, `latex/references.bib` |
| **What to change** | After line 44 ("They assume pre-trained models and inference-only tasks, which is the opposite of how discovery actually proceeds."), add a paragraph acknowledging: (a) Agentomics (bioRxiv Jan 2026) achieves autonomous ML experimentation with SOTA on 11/20 biomedical benchmarks; (b) ML-Agent (arXiv May 2025) uses RL to train autonomous ML engineers. Then sharpen: these handle single-paradigm ML workflows but do not orchestrate multi-paradigm pipelines (concurrent RL generation + supervised prediction + Bayesian batch selection + structural simulation in closed loops). The gap is cross-paradigm *integration*, not single-paradigm automation. |
| **Specific location** | New paragraph after line 44, before "What Multi-Paradigm Orchestration Looks Like" subsection |
| **Word count impact** | +80-100 words |
| **New bib entries** | `agentomics2026`, `mlagent2025` |
| **Why must-fix** | The blanket claim "agents cannot train models" (line 44) is factually no longer accurate as of Jan 2026. |
| **Reviewer source** | Devil's Advocate |
| **Success criterion** | The claim reads "agents can now automate single-paradigm ML workflows, but multi-paradigm orchestration remains unsupported." |

---

### MF-04. Acknowledge recent counter-evidence in Gap 5 (Section 6)

| Field | Detail |
|---|---|
| **Files** | `latex/sections/06-gap-multi-objective.tex`, `latex/references.bib` |
| **What to change** | In the "Pareto Frontiers and Constraint Satisfaction" subsection, after line 31 ("These require tight integration between generative models, predictive models, and optimizers, which agents do not support."), add a paragraph acknowledging: (a) PMMG (Advanced Science 2025) achieving 51.65% success on 7 simultaneous objectives via Pareto MCTS; (b) CheapVS (arXiv Mar 2025) enabling human-guided multi-objective Bayesian optimization. Then sharpen: these are standalone optimization algorithms, not integrated into agentic workflows with uncertainty quantification, sensitivity analysis, stage-adaptive recommendations, and interactive decision support. |
| **Specific location** | New paragraph after line 31 |
| **Word count impact** | +60-80 words |
| **New bib entries** | `pmmg2025`, `cheapvs2025` |
| **Why must-fix** | The paper currently implies no multi-objective Pareto tools exist. PMMG was published in Advanced Science. |
| **Reviewer source** | Devil's Advocate |
| **Success criterion** | Gap 5 framing shifts from "no one does multi-objective" to "multi-objective tools exist but are not agent-integrated." |

---

### MF-05. Fix ChatInvent mischaracterization

| Field | Detail |
|---|---|
| **Files** | `latex/sections/01-introduction.tex`, `latex/sections/04-gap-multi-paradigm.tex` |
| **What to change** | (a) Line 6 of 01-introduction.tex: change "ChatInvent completed a 13-month deployment at AstraZeneca for literature synthesis" to "ChatInvent completed a deployment at AstraZeneca for molecular design and synthesis planning". Drop "13-month" unless verified from the original paper. (b) Line 8 of 01-introduction.tex: change "ChatInvent mines literature for research gaps" to "ChatInvent generates molecular designs informed by literature". (c) Line 9 of 04-gap-multi-paradigm.tex: change "ChatInvent retrieves and synthesizes literature" to "ChatInvent supports molecular design and synthesis planning". (d) Line 12 of 02-gap-small-molecule.tex: "ChatInvent mines small-molecule synthesis routes" can remain but add "and molecular design" for accuracy. |
| **Word count impact** | Net 0 (replacement text) |
| **Why must-fix** | Mischaracterizing a key competing paper (He et al. 2026) undermines credibility with any reviewer familiar with the AZ work. This is the #1 factual error identified. |
| **Reviewer source** | Technical Accuracy |
| **Success criterion** | All ChatInvent references accurately reflect the scope described in He et al. 2026. |

---

### MF-06. Fix uncited/misattributed quantitative claims

| Field | Detail |
|---|---|
| **Files** | `latex/sections/05-gap-small-biotech.tex`, `latex/sections/02-gap-small-molecule.tex` |
| **What to change** | Three fixes: |
| | (a) **Section 5, line 35:** "Prototypical networks achieved 60-70% accuracy on peptide-receptor binding with only 20 examples per type, sufficient for initial prioritization." Prefix with "In our experience," to frame as practitioner anecdote. Change to: "In our experience, prototypical networks achieved 60-70\% accuracy on peptide-receptor binding classification with only 20 examples per type, sufficient for initial screening prioritization though dependent on the number of receptor classes and baseline rates." |
| | (b) **Section 5, line 21:** "Active learning reduced assays 30-40% by prioritizing uncertain predictions \citep{reker2017activelearning}." The 30-40% figure could not be verified in Reker 2017. Change to: "Active learning can substantially reduce experimental burden by prioritizing uncertain predictions \citep{reker2017activelearning}; in our peptide projects, this reduced required assays by approximately one-third." This separates the literature citation from the practitioner-specific number. |
| | (c) **Section 2, line 25:** "ProtBERT fine-tuning enables transfer learning with fewer than 100 examples." Soften to: "ProtBERT fine-tuning enables transfer learning from limited labeled data, often requiring only hundreds of examples for task-specific classifiers." |
| **Word count impact** | +20-30 words net |
| **Why must-fix** | Reviewers will flag uncited quantitative claims. Citation misattribution is a credibility risk. |
| **Reviewer source** | Technical Accuracy, Structure & Logic, Venue Reviewer |
| **Success criterion** | Every quantitative claim is either cited or explicitly framed as practitioner experience. |

---

### MF-07. Soften overstated technical claims

| Field | Detail |
|---|---|
| **Files** | `latex/sections/02-gap-small-molecule.tex` |
| **What to change** | Two fixes: |
| | (a) **Line 14:** "Peptides cannot encode as SMILES without losing stereochemistry." Change to: "SMILES encoding of peptides is error-prone, risking loss of stereochemical and conformational information, particularly for non-natural amino acids." |
| | (b) **Line 14:** "Molecular fingerprints (Morgan, MACCS) have no peptide analog." Change to: "Standard molecular fingerprints (Morgan, MACCS) perform poorly on peptides, which lack equivalent standard representations." |
| **Word count impact** | +5-10 words net |
| **Why must-fix** | Technically overstated claims invite nitpick rebuttals that distract from the paper's core argument. |
| **Reviewer source** | Technical Accuracy |
| **Success criterion** | A cheminformatics expert reads these sentences without objecting. |

---

### MF-08. Remove bib artifact

| Field | Detail |
|---|---|
| **Files** | `latex/references.bib` |
| **What to change** | Line 210: remove "Replaces hallucinated zhou2023rl entry" from the `note` field of `tan2022rl`. Change to: `note={PMID: 35510835}` |
| **Word count impact** | 0 |
| **Why must-fix** | Internal processing artifact visible to readers. Embarrassing if published. |
| **Reviewer source** | Venue Reviewer |
| **Success criterion** | No internal notes remain in any bib entry. |

---

## Tier 2: Should-Fix (significantly strengthens the paper)

### SF-01. Reduce Section 3/Section 6 overlap

| Field | Detail |
|---|---|
| **Files** | `latex/sections/03-gap-invivo-insilico.tex`, `latex/sections/06-gap-multi-objective.tex` |
| **What to change** | Section 3 lines 57-64 ("Safety, Efficacy, and Translation" subsection) extensively discusses safety-efficacy trade-offs, dose-response, Pareto-like reasoning, Bayesian optimization, and value-of-information analysis. This is Gap 5's thesis. Trim this subsection to ~50% of current length, keeping only the in-vivo-specific points (toxicology dose-response, species translation). Move the Pareto/Bayesian/value-of-information material to Section 6 as motivating examples, or add a forward reference: "We return to multi-objective trade-offs in \S\ref{sec:multiobjective}." |
| **Specific trimming targets** | Lines 58-60 (safety-efficacy general discussion) can be condensed. Line 64 (Bayesian optimization and value-of-information) should move to Section 6 or be replaced with a forward reference. |
| **Word count impact** | -100 to -150 words from Section 3 (net savings; reallocate to new counter-evidence paragraphs) |
| **Why should-fix** | Two reviewers independently flagged this as the biggest structural weakness. Section 3 pre-empts Section 6, making Section 6 feel like a retread. |
| **Reviewer source** | Structure & Logic, Venue Reviewer |
| **Success criterion** | Section 3 stays focused on data modality and temporal modeling. Section 6 owns multi-objective reasoning. |

---

### SF-02. Add gap-interaction paragraph to Introduction

| Field | Detail |
|---|---|
| **Files** | `latex/sections/01-introduction.tex` |
| **What to change** | After the roadmap paragraph (line 27, "We conclude with design principles..."), add one sentence acknowledging gap interactions: "These gaps are analytically distinct but practically intertwined: multi-paradigm orchestration (Gap 3) is a prerequisite for peptide-aware workflows (Gap 1), and multi-objective reasoning (Gap 5) is needed for both in vivo translation (Gap 2) and resource-constrained decision-making (Gap 4). We present them separately to clarify the architectural requirements, while recognizing that solutions must address them jointly." |
| **Word count impact** | +40-50 words |
| **Why should-fix** | Preempts the "your gaps overlap" criticism that two reviewers raised. |
| **Reviewer source** | Structure & Logic |
| **Success criterion** | A reader who notices overlap between gaps finds the paper has already acknowledged it. |

---

### SF-03. Fix adversarial tone in Section 5 closing

| Field | Detail |
|---|---|
| **Files** | `latex/sections/05-gap-small-biotech.tex` |
| **What to change** | Line 51: "Agents are optimized for AstraZeneca. The biotech sector where significant innovation happens is left behind." Change to: "Current agents are designed for large pharma contexts. The biotech sector, which accounts for a growing share of therapeutic innovation, remains underserved." |
| **Word count impact** | +3 words |
| **Why should-fix** | The current phrasing is adversarial toward AstraZeneca specifically and makes an unsupported claim about "significant innovation." Alienates the paper's natural readership. |
| **Reviewer source** | Tone & Positioning |
| **Success criterion** | An AstraZeneca researcher reads Section 5's closing without feeling attacked. |

---

### SF-04. Replace "not LLMs chatting" (2 occurrences)

| Field | Detail |
|---|---|
| **Files** | `latex/sections/04-gap-multi-paradigm.tex` |
| **What to change** | Line 64: "not LLMs chatting" -> "not LLM-to-LLM delegation." Also check Section 1 introduction roadmap for a second occurrence (the Structure & Logic reviewer noted this phrase appears twice). If found, apply the same replacement. |
| **Word count impact** | 0 |
| **Why should-fix** | Dismissive of the multi-agent paradigm. Too casual for Nature MI / Drug Discovery Today. |
| **Reviewer source** | Tone & Positioning |
| **Success criterion** | Zero occurrences of "chatting" in the manuscript. |

---

### SF-05. Strengthen practitioner positioning in Introduction

| Field | Detail |
|---|---|
| **Files** | `latex/sections/01-introduction.tex` |
| **What to change** | Line 26 currently says: "This paper draws on years of computational projects spanning peptide design, reinforcement learning optimization, in vivo efficacy modeling, behavioral phenotyping via computer vision, RNA-seq analysis, and multi-objective navigation." Strengthen by adding project count and explicit first-person positioning: "This paper draws on over a dozen computational projects spanning peptide design, reinforcement learning optimization, in vivo efficacy modeling, behavioral phenotyping via computer vision, RNA-seq analysis, and multi-objective navigation, led by the author at a small biotech serving as both drug designer and AI practitioner." |
| **Word count impact** | +15 words |
| **Why should-fix** | The practitioner voice is the paper's moat. Making it explicit increases authority. The "14+ projects" number from CLAUDE.md is a credibility anchor that was removed. |
| **Reviewer source** | Tone & Positioning, Venue Reviewer |
| **Success criterion** | The reader knows within the first two pages exactly who is writing and from what vantage point. |

---

### SF-06. Fix Table 3 priority matrix inconsistency

| Field | Detail |
|---|---|
| **Files** | `latex/sections/07-wishlist.tex` |
| **What to change** | Line 80: "In vivo data integration" is rated "Medium" impact. The paper's own Section 3 argues in vivo is where "most development cost and risk actually sit" (citing DiMasi 2016). Change impact to "High" for consistency. Also line 78: "Pareto frontier visualization" rated "Low" difficulty. Building a Pareto frontier requires multi-objective optimization backends, rated "High" difficulty in the same table. Change visualization difficulty to "Medium" (visualization is easy only if the optimization backend is solved). |
| **Word count impact** | 0 |
| **Why should-fix** | Internal inconsistency in a summary table undermines the paper's rigor. |
| **Reviewer source** | Structure & Logic |
| **Success criterion** | Table 3 ratings are internally consistent with the paper's own arguments. |

---

### SF-07. Acknowledge Medea in Gap 2 (Section 3)

| Field | Detail |
|---|---|
| **Files** | `latex/sections/03-gap-invivo-insilico.tex`, `latex/references.bib` |
| **What to change** | In the "Multi-Modal, Longitudinal Data Integration" subsection, after line 52 (RNA-seq pipeline paragraph), add one sentence: "Recent systems like Medea \citep{medea2026} have begun addressing multi-omics analysis agenically, handling transcriptomics, protein networks, and pathway analysis. However, these process static datasets rather than longitudinal in vivo time-series, and do not integrate behavioral phenotyping, imaging, or temporal efficacy modeling." |
| **Word count impact** | +30-40 words |
| **New bib entry** | `medea2026` |
| **Why should-fix** | Gap 2 is the paper's strongest claim. Acknowledging Medea strengthens it by showing even the closest counter-evidence falls short. |
| **Reviewer source** | Devil's Advocate |
| **Success criterion** | Gap 2 explicitly addresses the most relevant recent work and explains why it doesn't close the gap. |

---

### SF-08. Sharpen conclusion with explicit positioning against Lakhan and Seal et al.

| Field | Detail |
|---|---|
| **Files** | `latex/sections/08-conclusion.tex` |
| **What to change** | In the "Call to Action" subsection, after line 18 (funder paragraph), add a positioning paragraph: "Comprehensive surveys map the landscape of existing tools \citep{seal2025aiagents} and calls for adoption are necessary \citep{lakhan2025agentic}, but neither addresses the architectural gaps that prevent these systems from working in most real-world settings. This paper complements both: the gaps we identify are precisely the ones the surveys catalog but do not critique, and the adoption Lakhan advocates requires the engineering solutions we propose." |
| **Word count impact** | +50-60 words |
| **Why should-fix** | The CLAUDE.md explicitly positions this paper against these three works. The conclusion is where that positioning should land most clearly. |
| **Reviewer source** | Tone & Positioning |
| **Success criterion** | A reader who has also read Seal et al. and Lakhan understands exactly how this paper relates to both. |

---

### SF-09. Fix "the past three years" vagueness in conclusion

| Field | Detail |
|---|---|
| **Files** | `latex/sections/08-conclusion.tex` |
| **What to change** | Line 20: "The past three years showed what is possible." Change to: "Progress since 2023 showed what is possible." |
| **Word count impact** | 0 |
| **Why should-fix** | Vague timeframe when the cited systems span a known range. |
| **Reviewer source** | Structure & Logic |
| **Success criterion** | Temporal reference is precise. |

---

## Tier 3: Nice-to-Have (polish; do if word budget allows)

### NH-01. Broaden peptide examples to biologics generally

| Field | Detail |
|---|---|
| **Files** | `latex/sections/02-gap-small-molecule.tex`, `latex/sections/01-introduction.tex` |
| **What to change** | Add 1-2 sentences noting that the small-molecule bias also affects antibodies, nanobodies, and fusion proteins, not just peptides. In Section 2, after line 8 (peptide-specific challenges): "These challenges extend beyond peptides to biologics broadly: antibodies require CDR loop modeling, nanobodies need single-domain folding, and fusion proteins demand multi-domain interaction prediction. The small-molecule bias is a biologics-wide limitation." |
| **Word count impact** | +30-40 words |
| **Why nice-to-have** | Broadens perceived relevance beyond the peptide community. The venue reviewer flagged this as important for Nature MI. |
| **Reviewer source** | Venue Reviewer |
| **Success criterion** | An antibody researcher reads the paper and recognizes their challenges too. |

---

### NH-02. Add bridging sentences between Gaps 2-3 and 4-5

| Field | Detail |
|---|---|
| **Files** | `latex/sections/04-gap-multi-paradigm.tex`, `latex/sections/06-gap-multi-objective.tex` |
| **What to change** | (a) Start of Section 4 (line 1): after the opening paragraph, add a bridge: "The in vivo data integration challenge from the previous section illustrates a deeper architectural limitation: agents are not merely missing specific tools, they lack the capacity to orchestrate diverse computational paradigms." (b) Start of Section 6 (line 1): add bridge: "Resource constraints amplify the cost of poor decisions. When every experiment is precious, navigating multi-objective trade-offs becomes critical." |
| **Word count impact** | +30-40 words |
| **Why nice-to-have** | Smooths the two weakest transitions identified by Structure & Logic. |
| **Reviewer source** | Structure & Logic |

---

### NH-03. Strengthen Section 6 opening with drug-discovery-specific framing

| Field | Detail |
|---|---|
| **Files** | `latex/sections/06-gap-multi-objective.tex` |
| **What to change** | The opening paragraph (lines 1-6) currently reads as general optimization theory. Reorder to lead with the peptide three-candidate example (currently at line 14) and move the general Pareto definition later. The three-candidate example is "the paper's most effective concrete illustration" (Structure & Logic) and should open the section. |
| **Word count impact** | 0 (reordering, not adding) |
| **Why nice-to-have** | Section 6 is the "least persuasive section" (Tone & Positioning). Leading with a vivid practitioner example rather than textbook definitions would strengthen it. |
| **Reviewer source** | Tone & Positioning, Structure & Logic |

---

### NH-04. Vary "agents cannot" phrasing

| Field | Detail |
|---|---|
| **Files** | All section files (02-06) |
| **What to change** | Replace some instances of "agents cannot" / "no agent" with varied phrasing: "this remains outside agent scope," "no current system supports," "practitioners must handle this manually," "this exceeds current agent architectures." Target: reduce "agents cannot" / "no agent" occurrences by ~30%. |
| **Word count impact** | 0 |
| **Why nice-to-have** | The repetition risks monotony. Varying phrasing maintains the point with less drumbeat quality. |
| **Reviewer source** | Tone & Positioning |

---

### NH-05. Soften PharmAgents rigid-body docking claim

| Field | Detail |
|---|---|
| **Files** | `latex/sections/02-gap-small-molecule.tex` |
| **What to change** | Line 12: "PharmAgents assumes rigid-body docking, inappropriate for flexible peptides." Change to: "PharmAgents focuses on small-molecule structure-based design workflows not designed for flexible peptide interactions." |
| **Word count impact** | +3 words |
| **Why nice-to-have** | "Rigid-body docking" could not be verified in the PharmAgents paper. Softening avoids a factual dispute. |
| **Reviewer source** | Technical Accuracy |

---

### NH-06. Add Table 2 runtime clarification

| Field | Detail |
|---|---|
| **Files** | `latex/sections/04-gap-multi-paradigm.tex` |
| **What to change** | Table 2 (Agent Capability Matrix), "In vivo analysis: Days to weeks" in the Typical Runtime column refers to experiment duration, not computation time. Add a table footnote: "Runtime includes experimental turnaround, not just computation." |
| **Word count impact** | +8 words |
| **Why nice-to-have** | Minor precision issue flagged by Venue Reviewer. |
| **Reviewer source** | Venue Reviewer |

---

### NH-07. Standardize "in vivo to in silico" vs "in vivo-in silico"

| Field | Detail |
|---|---|
| **Files** | All section files |
| **What to change** | Grep for both formulations. Pick one (recommend "in vivo to in silico" as it appears in the section title) and standardize throughout. |
| **Word count impact** | 0 |
| **Why nice-to-have** | Consistency issue flagged by Venue Reviewer. |
| **Reviewer source** | Venue Reviewer |

---

## Word Budget Summary

| Tier | Items | Net word impact |
|---|---|---|
| Tier 1 (Must-Fix) | 8 items | +305-400 words |
| Tier 2 (Should-Fix) | 9 items | +40-70 words (after SF-01 savings) |
| Tier 3 (Nice-to-Have) | 7 items | +70-90 words |
| **Total** | **24 items** | **+415-560 words** |
| **Projected final count** | | **~7,600-7,760 words** |

This stays within the 8,000-word ceiling. If tight, SF-01 (trimming Section 3 overlap) recovers 100-150 words.

---

## New Bibliography Entries Required

| Key | Paper | Venue | Year |
|---|---|---|---|
| `peptune2024` | Tang et al., "PepTune" | ICML 2025 / arXiv:2412.17780 | 2024 |
| `pepmlm2025` | Chatterjee et al., "PepMLM" | Nature Biotechnology | 2025 |
| `agentomics2026` | BioGeMT, "Agentomics" | bioRxiv | 2026 |
| `mlagent2025` | "ML-Agent" | arXiv:2505.23723 | 2025 |
| `pmmg2025` | Liu et al., "PMMG" | Advanced Science | 2025 |
| `cheapvs2025` | Dang et al., "CheapVS" | arXiv:2503.16841 | 2025 |
| `medea2026` | Zitnik Lab, "Medea" | bioRxiv | 2026 |

---

## Execution Order

The revisions have dependencies. Recommended execution order:

1. **MF-08** (bib artifact) — trivial, zero risk
2. **MF-05** (ChatInvent fix) — factual correction, no structural impact
3. **MF-07** (soften SMILES/fingerprint claims) — local text changes
4. **MF-06** (fix quantitative claims) — local text changes
5. **SF-03, SF-04** (tone fixes) — local text changes
6. **MF-01** (tool-vs-agent framing in intro) — sets up everything that follows
7. **SF-02** (gap-interaction paragraph) — pairs with MF-01
8. **SF-05** (practitioner positioning) — pairs with MF-01
9. **SF-01** (reduce Section 3/6 overlap) — frees word budget
10. **MF-02, MF-03, MF-04** (counter-evidence paragraphs) — uses freed word budget; requires new bib entries
11. **SF-07** (Medea acknowledgment) — requires new bib entry
12. **SF-06** (Table 3 fixes) — standalone
13. **SF-08, SF-09** (conclusion fixes) — standalone
14. **NH-01 through NH-07** — polish pass, order doesn't matter

---

## Risk Assessment

| Risk | Mitigation |
|---|---|
| Word count exceeds 8,000 | SF-01 recovers 100-150 words; NH items are optional |
| New citations introduce claims that need verification | Verify each new paper's DOI and key claims via web search before adding |
| Tone shifts when acknowledging counter-evidence | Use consistent pattern: "Recent work has begun addressing X [cite]. However, Y remains unsupported." |
| New paragraphs disrupt flow | Read each section end-to-end after editing to check coherence |
| Confidentiality leak from new specifics | Run the same restricted-term check after revisions |
