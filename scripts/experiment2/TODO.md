# Experiment 2: LLM Knowledge Probing — TODO

## Status

- [x] Write questions.json (100 questions, 50 matched pairs)
- [x] Implement all pipeline scripts
- [x] Fix empty response bug in run_probing.py
- [ ] Run run_probing.py to completion (currently running)
- [ ] Run score_responses.py (after probing completes)
- [ ] Run prepare_expert_subset.py (after scoring completes)
- [ ] STOP here (do not run merge_scores.py or analyze_results.py yet)

### Live snapshot (update as needed)

- Active probing PID: `39271`
- Current progress:
  - `kimi-k2.5.jsonl`: `success=9`, `failed=13`

---

## After `run_probing.py` finishes

### Step 1: Verify responses

```bash
python - <<'PY'
import json,glob,os
for p in sorted(glob.glob("scripts/experiment2/responses/*.jsonl")):
    s=f=0
    with open(p) as fh:
        for line in fh:
            r=json.loads(line)
            if r.get("success") is True:
                s+=1
            else:
                f+=1
    print(f"{os.path.basename(p)} success={s} failed={f}")
PY
```

**Pass criteria:** each model file has `success=100` (4 files total). Failed attempts may be non-zero and are expected with retry logging.

### Step 2: Run Claude CLI scoring

```bash
python scripts/experiment2/score_responses.py
```

- ~15-20 min runtime
- Produces `scores/claude_scores.csv`
- Can be delegated to agent

### Step 3: Generate blind expert subset

```bash
python scripts/experiment2/prepare_expert_subset.py
```

- Produces 80 randomized, blinded responses for expert scoring
- Can be delegated to agent (same session as Step 2)

### Step 4: Expert scores 80 responses (MANUAL)

- ~40 min, done by author
- Fill in expert scores in the output file from Step 3
- Blind protocol: model identity and domain labels are stripped

### Step 5: Merge scores + compute agreement

```bash
python scripts/experiment2/merge_scores.py
```

- Produces `scores/final_scores.csv` + `scores/agreement_analysis.json`
- Reports quadratic-weighted Cohen's kappa
- Can be delegated to agent

### Step 6: Run analysis + generate figures

```bash
python scripts/experiment2/analyze_results.py
```

- Produces grouped bar chart, category table, statistical tests
- Output in `results/` directory
- Can be delegated to agent (same session as Step 5)

### Step 7: Commit everything

```
/gp
```

---

## Decision Points

- **After Step 1:** If any model has `success < 100`, re-run `run_probing.py` until all four reach 100 successes
- **After Step 5:** If kappa < 0.4, fall back to full manual scoring of all 400 responses
- **After Step 6:** If fewer than 2 models show significant gap (p < 0.0125), adjust claim strength in paper

---

## Current run scope guard

For the current execution request, stop after:
1. `python scripts/experiment2/score_responses.py`
2. `python scripts/experiment2/prepare_expert_subset.py`

Do not run:
- `python scripts/experiment2/merge_scores.py`
- `python scripts/experiment2/analyze_results.py`
