# Experiment 2: LLM Knowledge Probing — TODO

## Status

- [x] Write questions.json (100 questions, 50 matched pairs)
- [x] Implement all pipeline scripts
- [x] Fix empty response bug in run_probing.py
- [ ] Run run_probing.py to completion (currently running)

---

## After `run_probing.py` finishes

### Step 1: Verify responses

```bash
python3 -c "
import json
for f in ['kimi-k2.5','deepseek-v3.2','qwen3-next-80b','gemini-3-flash']:
    lines = open(f'scripts/experiment2/responses/{f}.jsonl').readlines()
    empties = sum(1 for l in lines if json.loads(l)['response_text'] == '')
    print(f'{f}: {len(lines)} responses, {empties} empty')
"
```

**Pass criteria:** 400 total responses, < 20 empty (PRD SC-1: failure rate < 5%)

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

- **After Step 1:** If > 20 empty responses, investigate and re-run affected models
- **After Step 5:** If kappa < 0.4, fall back to full manual scoring of all 400 responses
- **After Step 6:** If fewer than 2 models show significant gap (p < 0.0125), adjust claim strength in paper
