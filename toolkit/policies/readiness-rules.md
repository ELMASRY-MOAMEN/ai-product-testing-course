# Readiness Rules

Missing mandatory inputs, approvals, owners, or executable resources produce Not Ready.

## Not Ready is not Fail

The distinction matters and is often lost.

| Outcome | Meaning |
|---|---|
| **Fail** | The evaluation ran and the candidate did not meet its approved criteria |
| **Not Ready** | The evaluation could not run as declared. Nothing was measured, so nothing may be concluded about the candidate |

Reporting `Not Ready` as `Fail` slanders the candidate. Reporting it as `Pass` is worse: it claims evidence that does not exist.

## What makes a run Not Ready

Any one of these is sufficient:

- an evaluation question, dataset, reference or rubric, metric, threshold, critical slice, veto, variability control, evidence location or owner is missing;
- a declared threshold has no recorded approval;
- the candidate, evaluator or dataset version is not frozen, so the result would not be attributable;
- a declared resource — adapter, evaluator implementation, dataset file — cannot be executed or read;
- cases exist whose annotation status is not approved and whose eligibility was not resolved.

## The rule that follows

**Never invent the missing element to make the run proceed.** Inventing a threshold produces a number that looks like evidence and is not. Report the blocker, name the decision required, and name who owns it.

## Worked example

A manifest declares every section but leaves the acceptance threshold empty.

Correct outcome: `Not Ready`, with the blocker `missing approved threshold` naming the metric, and the decision owner identified. Incorrect outcome: any run at all, at any assumed threshold.

## What this policy does not decide

- Who approves a missing element. That belongs to the [human decision boundary](human-decision-boundary.md).
- How long a blocked evaluation may stay blocked.

## Related

- [DoT: evaluating probabilistic quality](../../05-the-two-gates/definition-of-trustworthy.md) — the ten mandatory components
- [Readiness checklist](../readiness-checklist.md) — the check to run before starting
