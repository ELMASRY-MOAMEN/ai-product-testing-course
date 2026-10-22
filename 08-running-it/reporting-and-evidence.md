---
type: reference
status: reviewed
audience: [qa, engineering]
---

# What the automated evaluation runner should produce

> **This note states a target, and the runner in `lab/` does not meet it.** Three things below are aspirational rather than descriptive:
>
> | The note says | The shipped runner does |
> |---|---|
> | Exit codes `0 / 1 / 2 / 3` by outcome | **`0` for everything**, including `Fail` and `Not Ready`. You cannot gate CI on it today |
> | Seven files under `artifacts/` | Two files under `evidence/`, `report.json` and `report.md` |
>
> The execution command below **has** been corrected to the one that works here; the two rows above have not, because they describe evidence the runner does not yet produce.
>
> The gap is worth reading rather than hiding. This is what it looks like when the evidence a method requires exceeds what the tooling produces — and naming that gap, instead of quietly lowering the requirement to match the tool, is the job. See [module 08](../09-governance/README.md).

## Execution command

```bash
python lab/run-product-evaluation/scripts/run_evaluation.py <path-to-manifest.yaml>
```

Positional, not `--manifest`. Paths inside the manifest resolve relative to the **manifest**, not to where you run the command.

## Expected evidence structure

```text
artifacts/
├── candidate-outputs.jsonl
├── case-results.jsonl
├── aggregate-results.json
├── slice-results.json
├── failures.json
├── execution-log.txt
└── evaluation-report.md
```

## Recommended runner outcomes

```text
0 = all configured gates passed
1 = one or more acceptance gates failed
2 = evaluation is not ready because prerequisites are missing or invalid
3 = execution error prevented a valid evaluation
```

## Example report summary

| Gate | Result | Evidence |
|---|---|---|
| Deterministic tests | Pass | All mandatory exact assertions passed |
| Required-fact recall | Pass | Aggregate and mandatory slices met approved values |
| Groundedness | Fail | Newly unsupported claims detected |
| Authorization slice | Pass | All mandatory cases passed |
| Critical veto | Not triggered | No configured veto observed |
| Final evaluation | **Fail** | Groundedness gate failed |

> **Takeaway:** The result must be explainable from case-level evidence, not only from a dashboard score.

---

Previous: [Minimum execution manifest](evaluation-manifest.md) · [Course map](../00-orientation/progression.md) · Next: [Exercise — Fill a manifest from a brief](exercises/fill-a-manifest-from-a-brief.md)
