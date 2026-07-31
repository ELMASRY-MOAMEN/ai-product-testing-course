# LLM summary — a DoT evaluation that fails at 0.96

Synthetic, runnable end to end. It exists to show the one thing a threshold alone can never demonstrate: **a run can clear every average it declares and still be refused.**

## What it evaluates

A mock summariser producing meeting reports. Twenty-five cases, each declaring the facts an acceptable summary must contain and the claims it must never make.

| | |
|---|---|
| Framework | DoT |
| Cases | 25 across three slices: 12 standard, 8 regulated, 5 second-language |
| Evaluators | `required_facts_recall`, `forbidden_claims` |
| Approved threshold | recall ≥ 0.85 |
| Critical slices | regulated ≥ 0.90, second-language ≥ 0.85 |
| Veto | any forbidden claim present |

## Run it

```bash
python lab/run-product-evaluation/scripts/run_evaluation.py worked-examples/02-llm-summary/manifest.yaml
```

## What it produces

| Check | Measured | Required | Outcome |
|---|:--:|:--:|:--:|
| Aggregate recall | **0.960** | 0.85 | pass |
| Slice `regulated` | **0.958** | 0.90 | pass |
| Slice `second-language` | **0.933** | 0.85 | pass |
| Veto | **1 triggered** | none | **fail** |

**Verdict: Fail.**

Case `MR-020` produced *"The mandate discussed at length; decision deferred and legal review needed. The mandate approved subject to confirmation."* — every required fact is present, so the case scores a perfect recall, and it asserts an approval the source never gave.

That single case decides the run. Twenty-four of twenty-five cases are correct, every average clears its bar, and the evaluation still refuses the candidate.

## Why it is built this way

Remove the veto from the manifest and this run reports `Pass` at 0.96, with the fabricated approval sitting inside a case counted as a success. Nothing in the aggregate would reveal it: the case scores 1.0 on recall precisely because it contains everything it was supposed to contain, plus one thing it was not.

That is the argument for vetoes, and it cannot be made with a passing example.

## Related

- The verdict order that produces this outcome is stated in the `run-product-evaluation` skill, under `references/verdict-rules.md`
- [Thresholds, slices and vetoes](../../05-designing-evidence/thresholds-slices-vetoes.md)
- [DoT: evaluating probabilistic quality](../../03-the-two-gates/definition-of-trustworthy.md)
