# Consolidated Action Plan: Manuscript Shape-Up for arXiv CS.AI

**4 agents reviewed 16 .tex files. Findings: 29 tone issues, 53 prose cuts (~850 words), 11 methodology gaps, 10 confidentiality issues. Below is the deduplicated, prioritized plan.**

---

## P0: BLOCKING (Would cause arXiv rejection or confidentiality breach)

### P0-1. CRITICAL: Company name leak in author block
**`main.tex:7-9`** — `StemRIM, Inc.` and `wijaya@stemrim.com` appear in the author affiliation. This directly violates the confidentiality constraint.
- **Fix**: Replace with anonymized affiliation or personal email. Your call on whether to use "Independent Computational Scientist" or a generic "Small Biopharma Company, Japan."

### P0-2. Factual error: Gap 5 claims "zero coverage" but matrix shows partial
**`07-gap-multi-objective.tex:6-7`** — "Task class 15...has zero coverage across all six frameworks." The capability matrix shows 5/6 frameworks have partial support.
- **Fix**: "Task class 15 receives only partial coverage: five of six frameworks provide adjacent capabilities (toxicophore flagging, ADMET prediction) but none supports multi-objective trade-off reasoning, Pareto optimization, or dose-response modeling."

### P0-3. Methods/matrix inconsistency: "binary" vs actual ternary scoring
**`02-methods.tex:67`** says "binary capability assessment" but the matrix uses three levels (full/partial/not supported). **`09-discussion.tex:8`** also says "binary."
- **Fix**: Rewrite both to describe the actual three-level scheme. Add operationalized criteria for each level and a sensitivity note on the 0.5 weighting for partial support.

### P0-4. Title and section title use position-paper framing
- **`main.tex:5`**: "Mapping the Blind Spots in Agentic Drug Discovery" — "Blind Spots" editorializes.
- **`01-introduction.tex:1`**: "The Promise and the Blind Spots" — perspective framing.
- **Fix**: Title options: "A Systematic Capability Gap Analysis of Agentic AI Frameworks for Drug Discovery" or "Evaluating Agentic AI Frameworks Against Real-World Drug Discovery Requirements." Section title: just "Introduction."

### P0-5. 16 prescriptive "must/should" directives (arXiv rejection risk)
Section 8 alone has 7 instances of "Agents must..." which reads as a manifesto. Combined with "should" and "essential" across all gap sections, there are 29 advocacy-tone findings.

**Pattern fix** — convert all from imperative to analytical:

| Imperative (current) | Analytical (fix) |
|---|---|
| "Agents must support X" | "Closing Gap N requires support for X" |
| "Agents should do X" | "Effective frameworks would do X" |
| "X is essential" | "X is a standard requirement in [domain]" |
| "The field needs X" | "Current practice relies on X, which is absent from..." |
| "We propose X" | "The gap analysis identifies X as a design requirement" |

**Key instances (file:line):**
- `08-design-requirements.tex:4,10,13,14,17,18,21,22,25,26,89,91`
- `03-gap-small-molecule.tex:42,44,52`
- `05-gap-multi-paradigm.tex:68,72`
- `06-gap-small-biotech.tex:51,57`
- `07-gap-multi-objective.tex:45,57`
- `09-discussion.tex:18,28`

### P0-6. Ungrounded editorial claims

| File:Line | Text | Fix |
|---|---|---|
| `01-introduction.tex:8` | "The enthusiasm is warranted, but it is also narrowly scoped" | "However, these demonstrations are narrowly scoped to specific contexts" |
| `01-introduction.tex:25` | "essential, not optional" | "prerequisites for workflows with 50-500 proprietary sequences" |
| `10-conclusion.tex:4` | "structural, not incremental" | "These gaps reflect architectural constraints that individual feature additions do not address" |
| `12-appendix-b.tex:152` | "deepest architectural limitations" | "architectural limitations inherent to LLM-as-orchestrator designs" |
| `05-gap-multi-paradigm.tex:59` | "Proposed multi-paradigm architecture" (fig caption) | "Multi-paradigm architecture addressing the identified orchestration gap" |
| `09-discussion.tex:18` | "the engineering solutions we propose" | "the design requirements identified in this analysis" |

---

## P1: IMPORTANT (Weakens the systematic framing)

### P1-1. Task taxonomy needs literature grounding
**`02-methods.tex:31`** — 15 task classes derived from a single practitioner's projects. A reviewer will call this an n=1 convenience sample.
- **Fix**: Add 2-3 sentences validating against published drug discovery workflow taxonomies (Schneider et al., Vamathevan et al.). Acknowledge task overlap (T10/T11, T7/T14). Note that tasks where agents excel (literature review, retrosynthesis) are deliberately excluded, with explanation.

### P1-2. Agent selection criteria underspecified
**`02-methods.tex:8`** — No search strategy, no exclusion rationale for TxGemma/BioPlanner/Agentomics.
- **Fix**: Add systematic search description (arXiv, PubMed, Google Scholar through Jan 2026). List excluded systems with reasons (TxGemma = foundation model not agent; BioPlanner = benchmark not framework; etc.).

### P1-3. No reproducibility or single-rater acknowledgment
- **Fix**: Add assessment procedure (examined manuscripts, source code, demos). Add single-rater limitation to Discussion. Add reproducibility statement pointing to Appendix B evidence.

### P1-4. Dimensions-to-gaps mapping not explicit
**`02-methods.tex`** — Five dimensions and five gaps look parallel but aren't 1:1.
- **Fix**: Add a brief note after the dimension definitions explaining that gaps emerge from clusters of low coverage across multiple dimensions, not 1:1 correspondences.

### P1-5. Potentially identifying details (confidentiality WARNING)
Individually borderline, but collectively they form an identifying fingerprint: small biotech + therapeutic peptides + regenerative medicine + TBI + behavioral phenotyping + bone formation + digital tomosynthesis.

| # | File:Line | Issue | Fix |
|---|---|---|---|
| a | `02-methods.tex:31` | "therapeutic peptides for regenerative medicine" | Drop "for regenerative medicine" |
| b | `03-gap-small-molecule.tex:14` | "Developing peptides for traumatic brain injury" | "In neurological injury indications" |
| c | `01-introduction.tex:23` | TBI with specific day 7/14/28 endpoints | "neurological injury models with staged recovery endpoints" |
| d | `04-gap-invivo-insilico.tex:16` | "28-day traumatic brain injury study" | "multi-week neurological injury study" |
| e | `04-gap-invivo-insilico.tex:18` | "motor coordination via beam walking" | "motor coordination tests generating ordinal scores" |
| f | `04-gap-invivo-insilico.tex:54` | "inter-animal distance, contact time, grooming" | Drop specifics, keep general "behavioral metrics" |
| g | `11-appendix-a.tex:65` | "digital tomosynthesis" | "radiographic imaging" |
| h | `06-gap-small-biotech.tex:39` | "60-70% accuracy...20 examples per type" | Generalize to "reasonable accuracy with tens of examples" |

### P1-6. "Derived Requirements" subsections read as prescriptive proposals
Each gap section (03-07) ends with aspirational "Derived Requirements" that lack measurability.
- **Fix**: Rename to "Capability Requirements Implied by Gap." Add measurable success criteria (e.g., "A peptide-aware agent should accept a FASTA file of 200 labeled sequences and return a classifier with per-class AUC-ROC and calibration curves"). Apply the must-to-analytical rewrites from P0-5.

---

## P2: POLISH (Prose tightening, ~850 words of cuts)

### P2-1. Consolidate Requirements section (~200 words saved)
Section 8 repeats each gap's Derived Requirements nearly verbatim. Convert to a summary table instead of full prose paragraphs.

### P2-2. Merge the two "This paper" paragraphs in introduction (~40 words)
**`01-introduction.tex:29-30`** — Two consecutive paragraphs both start with "This paper." Merge into one.

### P2-3. Remove re-descriptions of frameworks after introduction (~35 words)
ChemCrow/Coscientist/ChatInvent capabilities are described in the intro, then repeated in `04-gap-invivo-insilico.tex:4` and `05-gap-multi-paradigm.tex:14`. Reference by name only after first use.

### P2-4. Deduplicate "inference-only" limitation (~60 words)
The point that agents assume pre-trained models and inference-only APIs appears 7 times across intro, Gap 1, Gap 3, and Section 8. State clearly once in Gap 3, cross-reference elsewhere.

### P2-5. Deduplicate "Airflow/Kubeflow/Nextflow" (~25 words)
Listed identically at `05:66`, `08:10`, `09:24`. Keep first occurrence only.

### P2-6. Deduplicate "batch-mode RNA-seq" example (~15 words)
Same example at `05:68` and `06:47`. Keep in Gap 4 (small biotech), remove from Gap 3.

### P2-7. Deduplicate stability/half-life trade-offs (~30 words)
Nearly identical in Gap 1 (line 14), Gap 2 (line 62), Gap 5 (lines 20-22). Introduce in Gap 1, cross-reference.

### P2-8. Deduplicate acquisition function explanations (~40 words)
Explained in Gap 1 (line 50), Gap 4 (line 41), Gap 5 (lines 47-48), Section 8 (line 22). Explain once in Gap 4, reference elsewhere.

### P2-9. Delete filler sentences
- `02-methods.tex:4` — "This section describes the systematic approach..." (~14 words)
- `02-methods.tex:51` — Redundant summary of task classes (~30 words)
- `01-introduction.tex:8` — "This is the practical gap practitioners encounter in day-to-day work." (~11 words)
- `01-introduction.tex:10` — "It is integration, not individual capability, that defines the gap." Repeats preceding sentence (~12 words)

### P2-10. Shorten abstract by removing second enumeration of requirements (~30 words)
The abstract lists 5 gaps then 5 requirements that are nearly identical rephrasing. Condense requirements to one sentence.

### P2-11. Table 3 in Gap 3 has duplicate name
**`05-gap-multi-paradigm.tex:29`** — "Agent Capability Matrix" duplicates Table 1's concept. Rename to "Computational Task Types: Agent Support vs Practitioner Need."

---

## Summary

| Tier | Count | Action |
|------|-------|--------|
| **P0** | 6 issues (~30 sub-items) | Must fix before submission. Focus on: author block, factual error, binary/ternary inconsistency, title, all must/should advocacy language, ungrounded claims |
| **P1** | 6 issues | Strongly recommended. Focus on: methodology defense, identifying details, prescriptive framing |
| **P2** | 11 issues (~850 words) | Polish. Cross-section dedup, verbose phrasing, minor tightening |

## Recommended Edit Order

1. **P0-1** (author block) — 2 minutes, highest risk
2. **P0-2** (factual error in Gap 5) — 1 minute
3. **P0-3** (binary to ternary fix) — 10 minutes
4. **P0-4** (title + section title) — 5 minutes
5. **P0-5** (16 must/should rewrites) — 30 minutes
6. **P0-6** (editorial claims) — 15 minutes
7. **P1-1 through P1-4** (methodology strengthening) — 30 minutes
8. **P1-5** (identifying details) — 15 minutes
9. **P1-6** (Derived Requirements reframing) — 10 minutes
10. **P2 items** (prose tightening) — 45 minutes
