# Formal Peer Review: "The Blind Spots of Agentic Drug Discovery"

**Reviewer:** Simulated Venue Reviewer (arXiv cs.AI / Nature Machine Intelligence)
**Date:** 2026-02-06
**Manuscript type:** Perspective / Position Paper

---

## 1. Summary

This manuscript identifies five "blind spots" in current agentic AI systems for drug discovery: (1) a small-molecule bias that excludes peptide therapeutics and protein language models; (2) the absence of in vivo to in silico bridges for longitudinal, multi-modal animal data; (3) LLM-centric orchestration that cannot handle ML training, reinforcement learning, or simulation as first-class primitives; (4) resource assumptions mismatched to small biotech realities; and (5) single-metric optimization that ignores multi-objective trade-offs under uncertainty. The author draws on practitioner experience at a small biotech specializing in therapeutic peptides to ground each gap in concrete workflow failures.

The paper positions itself as a complementary counterpoint to three recent works: He et al. (2026), describing AstraZeneca's ChatInvent deployment; Seal et al. (2025), a comprehensive survey of AI agents in drug discovery; and Lakhan (2025), an editorial advocating agentic AI adoption. The author argues these works collectively describe what exists without identifying what is structurally missing. The paper concludes with five design principles and three concrete use cases for next-generation agents.

The contribution is timely and the practitioner perspective is distinctive. The core argument, that current agent architectures embed assumptions about data modality, organizational scale, and optimization objectives that limit their generalizability, is well-articulated and largely convincing. The paper fills a gap in the literature between surveys cataloging existing tools and editorials cheerleading adoption, offering instead a structured critique from operational experience.

---

## 2. Strengths

- **Distinctive practitioner voice.** The paper's authority derives from the author's unusual position as both drug designer and AI practitioner. This dual expertise enables critiques grounded in actual workflow failures rather than theoretical limitations. The paper cites experience across 14+ project types spanning ML, RL, protein language models, computer vision, and bioinformatics, giving each gap concrete backing.

- **Well-structured gap taxonomy.** The five blind spots are clearly delineated, logically ordered (from molecular representation through in vivo data, orchestration, resources, to optimization), and individually well-argued. Each section follows a consistent pattern: identify the gap, provide evidence, explain why current architectures fail, and propose what would be needed. This makes the paper easy to navigate.

- **The multi-paradigm vs. multi-agent distinction (Section 4) is a genuinely novel contribution.** The observation that "multi-agent" means multiple LLM instances but practitioners need "multi-paradigm" coordination of fundamentally different computational approaches (gradient-based training, RL, simulation, optimization) is incisive and underappreciated. This reframing could influence how the community thinks about agent architecture design.

- **Effective positioning against prior work.** The paper clearly articulates what He et al., Seal et al., and Lakhan each contribute and what they miss. The framing is respectful rather than adversarial: "you showed us what you built; here's what you're not seeing."

- **Concrete design principles and use cases.** Section 7 moves beyond critique to constructive proposals. The three use cases (peptide lead optimization, in vivo efficacy prediction, multi-endpoint assay analysis) are specific enough to be actionable and clearly illustrate what next-generation agents should support. The priority matrix (Table 3) is a useful artifact for developers.

- **Good figures and tables.** The data accessibility table (Table 1), agent capability matrix (Table 2), and priority matrix (Table 3) effectively summarize information. The figures (from descriptions) appear to visualize the core arguments well.

- **Appropriate scope.** The paper does not attempt to solve each gap but rather to articulate them clearly and propose principles. This is appropriate for a perspective piece.

---

## 3. Weaknesses

- **Generalizability from a single-author perspective.** The paper's greatest strength is also its most vulnerable point. The critique is grounded almost entirely in one practitioner's experience at one small biotech working on one therapeutic modality (peptides). A skeptical reviewer would ask: How representative is this experience? Are the described gaps also felt by practitioners working on antibodies, ADCs, cell therapies, or gene therapies? The paper could strengthen its case by briefly surveying whether similar gaps have been noted (even informally) by other practitioners or in other modalities. Without this, the paper risks being read as a niche complaint rather than a field-wide critique.

- **The peptide focus may limit perceived relevance.** Sections 2 (small molecule bias) and parts of Sections 3 and 5 are heavily oriented toward peptide therapeutics. While the author correctly notes that peptides are an important and growing therapeutic class, the paper would benefit from acknowledging that many of these gaps (PLM integration, conformational flexibility, aggregation) apply more broadly to biologics, including antibodies, nanobodies, and fusion proteins. Without this broadening, readers outside the peptide community may dismiss the paper as too specialized.

- **Insufficient engagement with the pace of development.** The agentic AI field is moving extremely rapidly. Some gaps the paper identifies (e.g., integration with structural biology tools, support for non-SMILES molecular representations) may be partially addressed by the time of publication or shortly thereafter. The paper would benefit from acknowledging this and framing the gaps as structural/architectural rather than merely reflecting current feature sets. This is partially done but could be more explicit.

- **Limited evidence for the "small biotech reality" gap (Section 5).** While the resource constraints are real, the argument that agents are specifically designed for large pharma and cannot serve small biotechs is somewhat under-supported. Many of the described challenges (limited data, limited compute, generalist practitioners) are not unique to agentic AI; they affect all computational tools. The paper should distinguish between gaps that are specific to agent architecture (e.g., no support for few-shot learning, no resource-aware recommendations) and those that are general challenges in computational drug discovery.

- **The in vivo gap (Section 3) conflates multiple distinct problems.** This section bundles together: (a) multi-modal data integration, (b) longitudinal temporal modeling, (c) bioinformatics pipeline orchestration (RNA-seq), (d) behavioral phenotyping from video, and (e) dose-response toxicology. While these are all important, they are architecturally quite different problems. Grouping them as a single "gap" obscures the distinct engineering challenges each represents. A more precise decomposition would strengthen the argument.

- **Missing quantitative evidence.** The paper relies on qualitative assertions ("no agent supports X," "current agents cannot Y"). While plausible, some quantitative grounding would strengthen the case. For example: How many of the agents surveyed by Seal et al. support any peptide-related tool? How many handle time-series data? A systematic assessment of even a few agents against the identified gaps would make the critique more rigorous.

- **The wishlist section (Section 7) could be more prioritized.** While the priority matrix is helpful, the section reads as a comprehensive list rather than a focused prescription. Given that the paper targets developers and researchers, a more opinionated prioritization of what should be built first (and why) would increase impact. The "critical" and "high" categories contain 8 of 10 items, which dilutes the signal.

- **Some claims about existing agent capabilities may be outdated or imprecise.** For instance, the claim that "ChemCrow includes RDKit, which does not handle peptide conformational sampling" is true but somewhat misleading; RDKit was never designed for conformational sampling of peptides, so its inclusion in ChemCrow does not constitute a "bias" so much as a scope limitation. Similarly, stating that "ChatInvent mines small-molecule synthesis routes, irrelevant to peptide synthesis" should be verified against the actual ChatInvent paper, as its scope may be broader than described here.

---

## 4. Questions for Authors

1. **Representativeness:** Have you sought feedback from practitioners at other small biotechs or working with other therapeutic modalities (antibodies, oligonucleotides, cell therapies) to validate that these gaps are broadly felt? If so, even brief mention would strengthen the paper.

2. **Scope vs. depth trade-off:** Would the paper be stronger if it focused on 2-3 gaps in greater depth rather than 5 at moderate depth? The multi-paradigm orchestration gap and the multi-objective optimization gap seem the most novel; the small-molecule bias and resource constraints are more widely recognized.

3. **Benchmarking proposal:** Have you considered proposing a benchmark or evaluation framework for agent systems along the dimensions you identify? This could significantly increase the paper's impact and citability. Even a conceptual framework (e.g., a scorecard with the 5 gaps as axes) would be valuable.

4. **Implementation feasibility:** Some of the proposed capabilities (e.g., agents that autonomously fine-tune protein language models, run RL optimization, and manage molecular dynamics simulations) represent substantial engineering challenges. What is the realistic timeline for these capabilities? Are there partial solutions or prototypes the paper should reference?

5. **The "partnership" framing:** The conclusion frames agents as "partners" rather than "assistants." How does this framing relate to the broader debate about AI autonomy in high-stakes domains? Should agents in drug discovery have more or less autonomy than in other domains, given regulatory requirements?

6. **Active learning claims:** Section 5 states that "active learning reduced assays by one-third." Can you provide more context for this claim? Is this from your own experience, and if so, how was it measured? This is a strong quantitative claim that warrants supporting detail.

7. **Competitive landscape:** Are there any emerging systems (academic or commercial) that partially address the gaps you identify? If so, acknowledging them would demonstrate awareness of the rapidly evolving landscape.

---

## 5. Minor Issues

- **Abstract:** The abstract is dense but effective. Consider slightly expanding it (by 1-2 sentences) to mention the practitioner experience basis, as this is the paper's key differentiator from Seal et al.

- **Section 1, paragraph 2:** "The architectural pattern is consistent" could be softened; some agents (e.g., DiscoVerse, PharmAgents) have non-trivial architectural differences from pure LLM-orchestration.

- **Section 2:** "Structure-activity relationships do not transfer; conservative substitutions can abolish activity while drastic changes improve potency." This is stated without citation. While likely true from the author's experience, a reference to peptide SAR literature would strengthen it.

- **Section 3, Table 1:** "RNA-seq data" listed as "FASTQ/BAM" format with "No" for agent-readability. This is accurate for raw data but some agents can process gene expression matrices (CSV format). The table should distinguish between raw sequencing data and processed expression data.

- **Section 4, Table 2:** The "Typical Runtime" column conflates computational runtime with experimental turnaround. "In vivo analysis: Days to weeks" refers to experiment duration, not computation time. Clarify.

- **Section 5:** "ESM-2 pre-trained on millions of protein sequences enables fine-tuning lightweight classifiers on 50-200 examples." Consider citing the specific studies demonstrating this, beyond the original ESM-2 paper.

- **Section 6:** The use of math-mode for the > symbol ("A $>$ B") is correct but the surrounding sentence could be clearer. Consider rephrasing.

- **References:** The bibliography is generally well-curated. A few observations:
  - The note "Replaces hallucinated zhou2023rl entry" in the tan2022rl entry should be removed before submission; this is an internal processing artifact.
  - Several entries use "and others" rather than full author lists. While acceptable for arXiv, Nature Machine Intelligence typically requires complete author lists or "et al." with first author.
  - The He et al. (2026) entry has "author={He, Jiazhen and others}" but a journal paper should list at least the first 3-5 authors.

- **Consistency:** The paper uses both "in vivo to in silico" and "in vivo-in silico" formulations. Standardize.

- **Word count:** The paper appears to be within the 6,000-8,000 word target, though a precise count is difficult from the LaTeX source. Verify before submission.

---

## 6. Recommendation

**Recommendation: Minor Revision (Accept with Revisions)**

**Justification:**

This is a well-conceived, clearly written perspective paper that identifies genuine gaps in the agentic AI for drug discovery literature. The practitioner grounding is the paper's most distinctive feature and its core contribution is timely. The five-gap taxonomy is logical, the positioning against prior work is effective, and the constructive proposals in the wishlist section add practical value.

The paper's primary weaknesses are addressable: (1) broadening the argument beyond peptides to biologics generally, (2) adding brief quantitative evidence for the identified gaps (e.g., a simple table showing which surveyed agents support which modalities/capabilities), (3) sharpening the prioritization in the wishlist section, and (4) cleaning up minor reference and consistency issues.

For **arXiv cs.AI**, the paper is suitable for posting as-is after minor corrections, as the venue has no formal review process but benefits from well-argued perspective pieces.

For **Nature Machine Intelligence** (perspective piece), the paper would benefit from the revisions described above, particularly: broadening beyond peptides, adding quantitative evidence, and tightening the in vivo section. With these changes, the paper would be competitive for this venue. The practitioner voice is exactly what the perspective format is designed for, and the topic is timely given the rapid proliferation of agentic AI papers in this space.

For **Drug Discovery Today**, the paper is well-suited to the venue's audience. Minor revisions to ensure accessibility to non-AI-specialist readers (e.g., briefly defining reinforcement learning, protein language models, and Pareto optimization on first use) would be appropriate.

**Overall assessment:** This paper makes a contribution the field needs: a structured, experience-grounded critique of agentic AI's blind spots from someone who has tried to use these approaches in practice. With minor revisions to broaden the scope and add quantitative grounding, it should be published.

---

## Scores (1-10)

| Criterion | Score | Notes |
|---|---|---|
| Novelty | 7 | Multi-paradigm vs. multi-agent distinction is genuinely novel; other gaps are recognized but not previously articulated together |
| Significance | 8 | Addresses a real and growing disconnect between agent demos and practitioner reality |
| Clarity | 8 | Well-organized, consistent structure, accessible writing |
| Balance | 7 | Generally fair; could better acknowledge partial solutions and the pace of development |
| Technical soundness | 7 | Qualitatively sound; would benefit from quantitative evidence |
| Positioning | 8 | Clear and respectful differentiation from prior work |
| Actionability | 7 | Design principles are useful; prioritization could be sharper |
| **Overall** | **7.5** | Strong perspective piece that would benefit from modest revisions |
