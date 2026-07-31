---
type: example
status: reviewed
audience: [qa, engineering]
---

# Exercise — Run a DoD gate

**Time:** 35 minutes. **Do it before opening [the solution](solutions/run-a-dod-gate.md).**

The other exercises in this course evaluate probabilistic behaviour, because that is the part that is new. This one is the half you already half-know — and it is where the two gates stop looking alike.

## The capability

*ClaimTriage* again, the three **deterministic** behaviours you classified in [module 02](../../02-foundations/exercises/classify-five-behaviours.md):

| | Behaviour | The specification it comes from |
|:--:|---|---|
| **B1** | Reject the request if the staff member's role is not entitled to the claim's product line | The entitlement matrix, maintained by Compliance |
| **B3** | Return the triage card as JSON with `claim_id`, `urgency`, `summary`, `recommended_queue`, all required | The documented response contract |
| **B5** | Route the claim: `critical` → `queue-A`; otherwise the queue for the product line | The routing table in the ops runbook |

The dataset is at `03-the-two-gates/exercises/data/claimtriage-dod-dataset.jsonl` — eight cases, `annotation_status: derived`.

## What to produce

**1. The DoD scenarios.** Write them in Gherkin, following [the scenario-writing rules](../../toolkit/gherkin-and-test-contracts.md). One scenario per behaviour is enough; make the entitlement one cover both directions.

**2. The manifest.** Start from [the template](../../toolkit/templates/evaluation-manifest.yaml), copied into `my-work/`. Two evaluator types from `lab/run-product-evaluation/scripts/evaluators.py` cover all three behaviours.

**3. Before running — predict.** Write down the status you expect, and how many cases you expect to fail.

```bash
python lab/run-product-evaluation/scripts/run_evaluation.py my-work/claimtriage-dod-manifest.yaml
```

**4. Read the output and answer:**

- **a.** What did you put in `acceptance.thresholds`, and why is that the right answer rather than an unfinished one?
- **b.** The report contains `aggregate_results` with a number in it. Find it. **Is that number the verdict?** What decided the verdict instead?
- **c.** One case produces **two** findings from two different evaluators. Which case, and why is that worth more to a reader than a single "failed" flag?
- **d.** Someone proposes: *"three failures out of eight is 62.5% passing; set the DoD bar at 60% and we ship."* Answer them.
- **e.** The dataset says `annotation_status: derived`, not `approved`. Every DoT dataset in this course says `approved`. What is the difference, and which question from module 02 explains it?

**5. The boundary.** One of the five behaviours from module 02 is deliberately absent from this exercise. Which one, why can it not be here, and what would go wrong if you tried to assert it with `exact_values`?

## Constraint

You do not own the response contract, the entitlement matrix or the routing table. If your assertions disagree with the dataset's expected values, the interesting question is which of the two is wrong — and that is a question for the specification's owner, not something to settle by editing the dataset until the run is green.

---

Previous: [DoD: testing deterministic behaviour](../definition-of-done.md) · [Course map](../../00-orientation/progression.md) · Next: [DoT: evaluating probabilistic quality](../definition-of-trustworthy.md)
