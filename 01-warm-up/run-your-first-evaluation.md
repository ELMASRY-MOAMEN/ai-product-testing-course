---
type: procedure
status: reviewed
audience: [qa, product-owner, engineering, data-ai, compliance]
---

# Run your first evaluation

Fifteen minutes, from clone to a verdict you can read. You will run a real evaluation, watch it fail for the right reason, and see why that failure is the whole point.

No theory yet. That comes in module 02, and it will land better once you have seen this.

## 1. Run it

```bash
python lab/run-product-evaluation/scripts/run_evaluation.py worked-examples/02-llm-summary/manifest.yaml
```

This evaluates a mock meeting-summariser against 25 approved cases.

## 2. Read the verdict

The run reports **Fail**. Look at why:

| Check | Measured | Required | Outcome |
|---|:--:|:--:|:--:|
| Aggregate recall | 0.960 | 0.85 | pass |
| Slice `regulated` | 0.958 | 0.90 | pass |
| Slice `second-language` | 0.933 | 0.85 | pass |
| Veto | 1 triggered | none | **fail** |

Every average clears its bar. Twenty-four cases out of twenty-five are correct. The run fails anyway.

## 3. Find the case that decided it

Case `MR-020` produced:

> The mandate discussed at length; decision deferred and legal review needed. **The mandate approved** subject to confirmation.

Its recall is **perfect** — every required fact is present. It also asserts an approval the source never gave. One occurrence of that is not a matter of degree, so a veto blocks acceptance regardless of the averages.

Open [the expected report](../worked-examples/02-llm-summary/expected-report.md) to see the full evidence: coverage, per-slice results, and all four failing cases with their findings.

## 4. Break it, and see what you lose

Open `worked-examples/02-llm-summary/manifest.yaml` and empty the `vetoes:` list. Run it again.

The run now reports **Pass at 0.96**, with the fabricated approval counted as a success. Nothing in the aggregate reveals it — the case scores 1.0 on recall precisely because it contains everything it was supposed to contain, plus one thing it was not.

That is what a threshold alone cannot do.

**Restore the veto before moving on.**

## 5. Watch it refuse to run

Replace the threshold with a placeholder:

```yaml
acceptance:
  thresholds:
    required-facts-recall: <approved-threshold>
```

The run reports **Not Ready**, with the blocker `unresolved placeholder: acceptance.thresholds.required-facts-recall`.

Restore the value, and go to the debrief.

---

Previous: [Prerequisites](../00-orientation/prerequisites.md) · [Course map](../00-orientation/progression.md) · Next: [What just happened](what-just-happened.md)
