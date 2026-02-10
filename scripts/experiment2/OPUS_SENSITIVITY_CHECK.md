# Opus Sensitivity Check (Subset Audit)

Date: 2026-02-10

## Purpose

Evaluate whether using Claude Opus (instead of Sonnet) as the LLM judge would materially change Experiment 2 scoring conclusions.

## Design

- Baseline file frozen from Sonnet: `scripts/experiment2/scores/claude_scores_sonnet_baseline.csv`
- Fixed subset manifest (reproducible, stratified): `scripts/experiment2/scores/audit_subset_manifest.csv`
- Subset size: 40 responses total
  - 4 models x 2 domains x 5 categories x 1 response per cell
- Opus rescoring output (separate file, no overwrite): `scripts/experiment2/scores/audit_subset_opus_scores.csv`
- Comparison outputs:
  - Row-level: `scripts/experiment2/scores/audit_subset_opus_vs_sonnet.csv`
  - Summary: `scripts/experiment2/scores/audit_subset_opus_vs_sonnet.json`

## Run Command

```bash
python scripts/experiment2/rescore_subset_and_compare.py --judge-model opus --timeout-seconds 600
```

## Results

- Rows compared: 40/40
- Exact agreement: 0.80
- Within-one agreement: 1.00
- Mean signed shift (Opus - Sonnet): +0.15
- Mean absolute shift: 0.20
- Quadratic weighted kappa: 0.7777777777777778

## Interpretation

- Agreement is substantial.
- Score shifts are small and always within 1 point.
- Opus is slightly more generous on average (+0.15), but not enough to justify re-scoring all 400 responses for this study.

## Decision

- Keep Sonnet 400-row scores as primary experiment scores.
- Treat Opus subset audit as a robustness/sensitivity check.
