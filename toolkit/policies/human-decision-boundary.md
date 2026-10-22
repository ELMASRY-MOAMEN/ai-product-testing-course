# Human Decision Boundary

Automation produces evidence and a rules-based recommendation. Authorized humans own acceptance and residual risk.

## Where the line falls

| Automation may | Automation may not |
|---|---|
| Execute an approved protocol | Approve the protocol it executes |
| Compute metrics, slices and veto states | Set or adjust a threshold |
| Apply verdict rules and state `Pass`, `Fail` or `Not Ready` | Accept a result, or waive a failure |
| Report blockers and the decisions they require | Make those decisions, or assume they were made |
| Retain and organise evidence | Decide that evidence is sufficient |

A `Pass` is a **recommendation supported by evidence**. It is not an acceptance, and no report may word it as one.

## Why the boundary holds even when the evidence is good

The evidence answers *did the candidate meet the declared criteria*. It cannot answer *are these the right criteria for this risk*, nor *do we accept what remains*. Those two questions carry consequences an automated run cannot bear, so they stay with a person who can.

This is why a run that passes every threshold still ends with a named owner making a recorded decision.

## What the recommendation must carry

For a human decision to be possible rather than nominal, the recommendation must be accompanied by:

- the verdict and the rule that produced it;
- the frozen candidate, evaluator and dataset versions;
- case-level results, including every failure;
- slice results and veto states, reported separately from the aggregate;
- residual risk that remains after the controls.

A verdict handed over without these makes the human a rubber stamp, which defeats the boundary while appearing to respect it.

## Worked example

A run yields `Pass`. Two cases in the legal-exposure slice failed, but the slice still met its approved minimum.

The runner reports `Pass`, the slice result, and the two failing cases. The authorized owner may accept, accept with conditions, or refuse. **The runner does not narrow that choice**, and does not present acceptance as the default.

## What this policy does not decide

- Who the authorized person is for a given product. That is named in the manifest ownership section.
- What happens when the owner disagrees with the recommendation. The disagreement is recorded; the owner still decides.

## Related

- [Roles and human gates](../../09-governance/roles-and-human-gates.md) — who holds which authority
- [Verdict rules](verdict-rules.md) — how the recommendation is computed
