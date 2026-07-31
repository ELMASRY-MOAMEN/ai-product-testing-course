---
type: reference
status: reviewed
audience: [qa, engineering]
---

# What the automated evaluation runner should produce

## Suggested execution command

```bash
python .github/skills/run-product-evaluation/scripts/run_evaluation.py \
  --manifest evaluation/evaluation.yaml
```

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

Previous: [Minimum execution manifest](evaluation-manifest.md) · [Course map](../00-orientation/progression.md) · Next: [Roles and human gates](../06-governance/roles-and-human-gates.md)
