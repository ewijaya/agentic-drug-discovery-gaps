# What Drug Discovery AI Agents Still Can't Do

**Position paper on the architectural gaps in current agentic AI systems for drug discovery**

## Author
Edward Wijaya

## Status
📝 Outline phase (Feb 2026)

## Abstract (Working Draft)

Current agentic AI systems in drug discovery (ChatInvent, Coscientist, PharmAgents) showcase impressive capabilities but reveal systematic blind spots when applied beyond their design context. While these systems excel at small-molecule synthesis planning and target-based workflows at well-resourced organizations, they struggle with peptide-specific requirements, in vivo–in silico modeling bridges, and multi-paradigm orchestration needs.

This position paper, informed by 14+ AI-driven projects at a small biotech, identifies five critical gaps:

1. **Small molecule bias** - Lack of protein language model integration for peptide discovery
2. **In vivo modeling gap** - No frameworks for longitudinal efficacy prediction
3. **Multi-paradigm orchestration** - Brittleness when combining mechanistic + ML + symbolic reasoning
4. **Resource constraints** - Assumption of high-throughput infrastructure
5. **Evaluation metrics** - Focus on synthesis feasibility over biological relevance

The paper argues for moving from LLM-centric multi-agent chat systems to true computational partnership frameworks that support:
- Model fine-tuning workflows (not just API calls)
- Uncertainty-aware multi-objective optimization
- Batch-mode orchestration for resource-constrained settings
- Practitioner-in-the-loop design patterns

## Target Venues
- **arXiv cs.AI** (primary: rapid dissemination, preprint citation)
- **Drug Discovery Today** (perspectives section)
- **Nature Machine Intelligence** (opinion/perspective)

## Word Count Target
6,000-8,000 words

## Repository Structure

```
├── README.md              # This file
├── outline/
│   ├── full-outline.md    # Complete paper outline from Notion
│   └── illustrations.md   # Visual assets and figure specifications
├── references/
│   └── key-papers.md      # Bibliography of cited works
├── drafts/                # Section drafts (work in progress)
└── figures/               # Generated figures and diagrams
```

## Key Contributions

1. **Practitioner perspective** - Grounded in real-world deployments, not benchmarks
2. **Architectural analysis** - Identifies design assumptions that don't generalize
3. **Actionable recommendations** - Proposes specific framework improvements
4. **Domain specificity** - Focus on peptide/in vivo gaps underrepresented in current literature

## Timeline

- **Feb 2026**: Outline complete ✓
- **Mar 2026**: Section drafts
- **Apr 2026**: Full draft + figure generation
- **May 2026**: Internal review + revision
- **Jun 2026**: Submission to arXiv + target journal

## Related Work

This paper builds on recent surveys (Seal et al. 2025, Aoun & Garg 2025) and system demonstrations (He et al. 2026 ChatInvent, Boiko et al. 2023 Coscientist) to identify systematic gaps from a small-biotech practitioner lens.

---

**License**: TBD (likely CC BY 4.0 for arXiv)  
**Contact**: Edward Wijaya
