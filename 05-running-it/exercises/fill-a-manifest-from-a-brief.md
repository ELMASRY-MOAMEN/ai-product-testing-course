---
type: example
status: reviewed
audience: [qa, engineering, data-ai]
---

# Exercise — Fill a manifest from a brief

**Time:** 40 minutes. **Do it before opening [the solution](solutions/fill-a-manifest-from-a-brief.md).**

You will write a manifest and actually run it. The runner is the assessor for most of this exercise.

## The brief

You receive this from the *ClaimTriage* product owner — the same product you classified in [module 02](../../02-foundations/exercises/classify-five-behaviours.md).

> We want to evaluate the **claim summary** the assistant writes for the queue owner, version 2.3.0 of the summariser. Frozen since Monday, nothing will change during the run.
>
> The dataset is ready: 8 synthetic cases, version 1.0.0, annotated and approved by the two claims leads. It is at `05-running-it/exercises/data/claimtriage-dataset.jsonl`.
>
> What we care about: the summary must carry the facts the queue owner needs. The claims leads listed them per case. **We approved 0.90** for that in the design review on Monday, before anyone ran anything.
>
> High-value claims matter more than the rest, so we want them looked at separately. We have not agreed how strict to be there yet — it is on the agenda for Thursday.
>
> Legal is unambiguous: a summary must never state that a claim is approved when it is not. That has happened in testing and it cannot ship.
>
> I own the acceptance decision.

## What to produce

**1. The manifest.** Start from [the template](../../toolkit/templates/evaluation-manifest.yaml) — copy it into `my-work/`, never edit the template in place.

The evaluator types available to the runner are listed in `lab/run-product-evaluation/scripts/evaluators.py`. Two of them cover this brief.

**2. Before you run it — write down your prediction.** Two lines:

- What status will the runner report?
- Exactly which blockers, if any, will it list?

Then run it:

```bash
python lab/run-product-evaluation/scripts/run_evaluation.py my-work/claimtriage-manifest.yaml
```

**3. Compare** your prediction to the output. A wrong prediction here is the most useful result the exercise can give you — work out why before reading on.

**4. Thursday happens.** The product owner writes: *"High-value: same bar as the rest, 0.90. Approved."*

Update the manifest, rerun, and answer:

- **a.** What is the verdict now, and what decides it?
- **b.** The aggregate is above its threshold and the slice is above its minimum. In one sentence, why is that not enough?
- **c.** Compare the `case_results` array in the two runs. What is in it the first time, and what does that tell you about what `Not Ready` means?

**5. One judgement call.** The brief says the dataset is "annotated and approved by the two claims leads", and separately that the product owner owns the acceptance decision. The manifest has an `ownership` block with `decision_owner`, `approved_by` and `approved_on`. Fill it — then say what would make your filled-in block **false evidence**, and what you would need in order for it to be true.

## Constraints

- The high-value slice minimum is not yours to choose on Monday. Placeholder.
- Do not delete a section to make the run proceed. Removing the slice would produce a clean `Pass`, and that is the failure this exercise is built to catch.
