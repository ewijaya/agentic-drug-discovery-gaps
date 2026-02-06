# Executive Summary: Manuscript Review Synthesis

**Paper:** "The Blind Spots of Agentic Drug Discovery"
**Date:** 2026-02-06
**Reviewers:** Devil's Advocate, Structure & Logic, Venue Reviewer, Technical Accuracy, Tone & Positioning

---

## Overall Verdict

**The paper is publishable with targeted revisions.** The venue reviewer recommends **Minor Revision (Accept with Revisions)** with an overall score of 7.5/10. Technical accuracy is rated at 90-95%. The practitioner voice and multi-paradigm vs. multi-agent distinction are genuine contributions the field needs. However, three of five gap claims need recalibration against recent 2025-2026 work, and several uncited quantitative claims create vulnerability under peer review.

---

## Top 5 Critical Issues (Ranked by Impact)

### 1. Missing Recent Papers That Challenge Gap Claims
**Source:** Devil's Advocate (primary), Technical Accuracy (supporting)
**Impact:** HIGH — a reviewer who cites these will undermine the paper's authority

The paper cites nothing from mid-2025 onward. Key omissions that directly challenge gap claims:

| Paper | Date | Challenges |
|---|---|---|
| **PepTune** (ICML 2025) | Dec 2024 | Gap 1 — multi-objective peptide design via PLM + MCTS |
| **PepMLM** (Nature Biotechnology) | Aug 2025 | Gap 1 — ESM-2-based peptide binder design, experimentally validated |
| **Agentomics** (bioRxiv) | Jan 2026 | Gap 3 — autonomous ML experimentation, SOTA on 11/20 benchmarks |
| **ML-Agent** (arXiv) | May 2025 | Gap 3 — RL-trained LLM for autonomous ML engineering |
| **Medea** (bioRxiv) | Jan 2026 | Gap 2 — omics AI agent for multi-omics analysis |
| **PMMG** (Advanced Science) | 2025 | Gap 5 — Pareto MCTS, 51.65% success on 7 simultaneous objectives |
| **CheapVS** (arXiv) | Mar 2025 | Gap 5 — human-in-the-loop multi-objective Bayesian optimization |

**Fix:** Add a "Recent Advances" subsection to each gap section acknowledging partial progress, then sharpen the claim to what remains unaddressed. This is the single most important revision.

### 2. Tool-vs-Agent Distinction Is Underarticulated
**Source:** Devil's Advocate (primary), Structure & Logic (supporting)
**Impact:** HIGH — this is the paper's core analytical framework but is not made explicit enough

Many tools addressing the gaps exist (PepTune for peptides, PMMG for multi-objective, Agentomics for ML training). The real gap is their **integration into agentic workflows** — no system orchestrates peptide PLM fine-tuning, active learning, multi-objective selection, and in vivo validation in a coordinated pipeline. The paper conflates "no tool exists" with "no agent integrates this." Making this distinction the paper's central framing would make it far more defensible.

**Fix:** Add an explicit paragraph in the Introduction defining the distinction: "Individual tools addressing aspects of each gap are emerging rapidly. The blind spots we identify are not the absence of capability but the absence of agentic integration — the orchestration of these capabilities into coherent, end-to-end workflows."

### 3. Gap Overlap Creates Redundancy
**Source:** Structure & Logic (primary), Venue Reviewer (supporting)
**Impact:** MEDIUM-HIGH — weakens structural clarity and invites reviewer criticism

Key overlaps identified:
- **Gaps 1 & 3:** Both argue agents can't do ML training. PLM fine-tuning (Gap 1) is a specific instance of multi-paradigm orchestration (Gap 3).
- **Gaps 2 & 5:** Section 3 (In Vivo) extensively discusses safety-efficacy trade-offs, dose-response, and Pareto-like reasoning — this is Gap 5's thesis. By the time the reader reaches Section 6, it feels like a retread.
- **Gaps 1 & 5:** Section 2's "What Peptide-Aware Agents Would Need" discusses multi-objective optimization and curriculum learning, pre-empting Section 6.

**Fix:** (a) Add an Introduction paragraph acknowledging that gaps interact ("analytically distinct but practically intertwined"). (b) Move safety-efficacy trade-off material from Section 3 to Section 6. (c) Tighten Section 2's wishlist subsection to avoid pre-empting later sections.

### 4. ChatInvent Mischaracterization
**Source:** Technical Accuracy
**Impact:** MEDIUM — mischaracterizing a competing paper's scope undermines credibility with reviewers familiar with the work

The paper describes ChatInvent as focused on "literature synthesis." The original He et al. paper describes it as "molecular design and synthesis planning." The "13-month deployment" figure could not be verified. Since ChatInvent is referenced multiple times (Sections 1, 4, 5, conclusion), getting this wrong is damaging.

**Fix:** Verify against the original paper. Revise to "molecular design and synthesis planning" or "literature-informed molecular design." Confirm the 13-month timeframe.

### 5. Uncited Quantitative Claims
**Source:** Structure & Logic (primary), Technical Accuracy (supporting), Venue Reviewer (supporting)
**Impact:** MEDIUM — creates vulnerability under peer review

Three specific claims lack adequate support:
- "Prototypical networks achieved 60-70% accuracy on peptide-receptor binding with only 20 examples per type" (Section 5) — unverifiable practitioner claim, not framed as such
- "Active learning reduced assays by 30-40%" (Section 5) — attributed to Reker 2017, but this specific figure could not be verified from that paper
- "ProtBERT fine-tuning enables transfer learning with fewer than 100 examples" (Section 2) — plausible but uncited

**Fix:** Frame the prototypical networks claim explicitly as practitioner experience ("in our experience"). Verify or remove the Reker 2017 attribution. Add a citation for the ProtBERT claim or soften to "on the order of hundreds of examples."

---

## Top 5 Strengths to Preserve

### 1. The Practitioner Voice
All five reviewers independently identified this as the paper's strongest asset. The dual role (drug designer + AI practitioner) enables critiques grounded in actual workflow failures. Details like "5-fold cross-validation leaves only 20 examples for evaluation" and the active learning round-by-round description are authentically practitioner and very hard to fake. **This is the paper's moat.**

### 2. The Multi-Paradigm vs. Multi-Agent Distinction (Section 4)
Identified by the venue reviewer as "genuinely novel" and by the tone reviewer as one of the most persuasive sections. The observation that "multi-agent" means multiple LLMs while practitioners need coordinated ML training + RL + simulation + optimization is the paper's most original conceptual contribution.

### 3. The In Vivo Gap (Section 3 / Gap 2)
The devil's advocate found this the most defensible gap — no counter-evidence addresses longitudinal in vivo data modeling, behavioral phenotyping, or temporal efficacy prediction. The tone reviewer rated it the most persuasive section rhetorically. The concrete data types (behavioral videos, RNA-seq, clinical trajectories) make the gap visceral.

### 4. Effective Positioning Against Prior Work
The "complementary counterpoint" framing works. The paper acknowledges what exists before identifying what's missing. Each gap section names specific systems and their capabilities before explaining insufficiency. This consistent pattern builds cumulative credibility.

### 5. The Wishlist's Structure and Concrete Use Cases
The 1:1 mapping of wishlist principles to gaps is structurally clean. The three use cases (peptide lead optimization, in vivo efficacy prediction, multi-endpoint assay) with Input/Workflow/Output/Human-decisions format are practical and actionable.

---

## Revision Recommendations (Prioritized by Effort vs. Impact)

### Quick Wins (Low Effort, High Impact)

| # | Recommendation | Source | Effort |
|---|---|---|---|
| 1 | Fix ChatInvent characterization ("molecular design and synthesis planning" not "literature synthesis") | Technical Accuracy | 30 min |
| 2 | Soften "Agents are optimized for AstraZeneca. The biotech sector... is left behind" in Section 5 | Tone & Positioning | 15 min |
| 3 | Replace "not LLMs chatting" (2 occurrences) with less dismissive phrasing | Tone & Positioning | 15 min |
| 4 | Frame prototypical networks claim as practitioner experience, not literature | Structure & Logic, Tech Accuracy | 15 min |
| 5 | Verify/fix active learning 30-40% attribution to Reker 2017 | Technical Accuracy | 30 min |
| 6 | Soften SMILES stereochemistry claim ("cannot encode" → "encoding is error-prone and incomplete") | Technical Accuracy | 15 min |
| 7 | Soften "no peptide analog" for fingerprints → "perform poorly on peptides" | Technical Accuracy | 15 min |
| 8 | Fix "the past three years" in conclusion to "since 2023" for precision | Structure & Logic | 5 min |
| 9 | Remove "Replaces hallucinated zhou2023rl entry" note from references.bib | Venue Reviewer | 5 min |

### Medium Effort, High Impact

| # | Recommendation | Source | Effort |
|---|---|---|---|
| 10 | Add "Recent Advances" acknowledgment to each gap section (cite PepTune, Agentomics, Medea, PMMG, CheapVS, etc.) | Devil's Advocate | 2-3 hrs |
| 11 | Add explicit tool-vs-agent distinction paragraph in Introduction | Devil's Advocate | 1 hr |
| 12 | Add Introduction paragraph acknowledging gap interactions | Structure & Logic | 30 min |
| 13 | Move safety-efficacy trade-off material from Section 3 to Section 6 | Structure & Logic | 1-2 hrs |
| 14 | Add first-person practitioner positioning in Introduction + restore "over a dozen projects" | Tone & Positioning | 30 min |
| 15 | Engage Seal et al. and Lakhan more explicitly in conclusion | Tone & Positioning | 30 min |

### Higher Effort, Medium Impact

| # | Recommendation | Source | Effort |
|---|---|---|---|
| 16 | Broaden beyond peptides to biologics (antibodies, nanobodies, ADCs) for generalizability | Venue Reviewer | 2-3 hrs |
| 17 | Add quantitative evidence table (which surveyed agents support which modalities) | Venue Reviewer | 2-3 hrs |
| 18 | Strengthen Section 6 (Multi-Objective) with vivid drug-discovery-specific opening | Tone & Positioning | 1 hr |
| 19 | Add concrete near-term research agenda to conclusion | Structure & Logic | 1 hr |
| 20 | Reconcile Table 3 priority matrix (in vivo should be High impact, not Medium) | Structure & Logic | 30 min |

---

## Contradictions Between Reviewers

### 1. Severity of Gap 1 Challenge
- **Devil's Advocate:** Gap 1 needs "most revision" — PepTune, PepMLM, TxGemma substantially challenge the small-molecule bias claim
- **Venue Reviewer:** Rates the paper's novelty at 7/10 overall, suggesting the contribution is still valid
- **Resolution:** Both are right. The gap claim as currently stated ("no agent supports peptides") is too strong, but the underlying point (no agentic workflow orchestration for peptides) is valid. Reframing resolves this.

### 2. Should Gaps Be Merged?
- **Structure & Logic:** "No gaps should be merged" — they serve different rhetorical functions despite overlap
- **Venue Reviewer:** Asks "Would the paper be stronger with 2-3 gaps in greater depth?"
- **Resolution:** Keep 5 gaps but acknowledge overlap in the Introduction and tighten scoping within each section to minimize redundancy.

### 3. Section 3 Quality
- **Tone & Positioning:** Rates Section 3 as "the paper's strongest section rhetorically"
- **Structure & Logic:** Criticizes Section 3 for "overextension into Gap 5 territory" with safety-efficacy material
- **Venue Reviewer:** Says Section 3 "conflates multiple distinct problems"
- **Resolution:** Section 3's strength is its concrete examples. Its weakness is scope creep. Trim the safety-efficacy material (move to Section 6) while preserving the temporal modeling and behavioral phenotyping arguments.

### 4. Technical Accuracy vs. Devil's Advocate
- **Technical Accuracy:** "90-95% of claims verified as accurate"
- **Devil's Advocate:** Several claims are "no longer accurate" (e.g., "agents cannot train models")
- **Resolution:** The claims were accurate when written but the field has moved fast. The issue is currency, not accuracy. Adding "as of late 2025" qualifiers and "Recent Advances" subsections resolves both.

---

## Bottom Line

The paper has a strong foundation: an authentic practitioner voice, a novel conceptual contribution (multi-paradigm vs. multi-agent), and two very defensible gap claims (in vivo bridge, small biotech reality). The main risk is being caught flat-footed by recent 2025-2026 work that partially addresses Gaps 1, 3, and 5. The fix is not to abandon these gaps but to sharpen them: acknowledge emerging tools, then explain why agentic workflow integration remains absent. This reframing would make the paper more nuanced, more defensible, and ultimately more impactful.

**Estimated revision time for all high-priority items: 1-2 days.**
