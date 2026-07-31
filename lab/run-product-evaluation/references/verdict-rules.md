# Verdict Rules

Governs how a completed run is turned into `Pass`, `Fail` or `Not Ready`, and what may never change that outcome.

## Rule

Evaluate in this order and stop at the first failing step. A later step never overturns an earlier one.

1. **Readiness** — every mandatory input, approval, owner and executable resource is present.
2. **Vetoes** — no critical failure occurred on any case.
3. **Critical slices** — every risk-sensitive slice met its own approved threshold.
4. **Aggregate thresholds** — the overall result met its approved threshold.

Failing step 1 yields `Not Ready`. Failing step 2, 3 or 4 yields `Fail`. Passing all four yields `Pass`.

`Pass` is a recommendation supported by evidence. It is not an acceptance, and must never be reported as one.

## How to apply

| Step | Check | If it fails |
|:--:|---|---|
| 1 | Manifest complete, thresholds approved, versions frozen, resources readable | `Not Ready` — report blockers and the decision owner. Measure nothing. |
| 2 | Any case with a triggered veto | `Fail` — report the triggering cases, whatever the aggregate says |
| 3 | Each critical slice against its own minimum | `Fail` — name the slice and its measured value |
| 4 | Aggregate against its approved threshold | `Fail` — report the gap |

Three rules bind the application:

- **Compute every step, even after one fails.** Stopping the *verdict* is not stopping the *measurement*: later results stay in the report because they inform remediation. Only the outcome is decided early.
- **Never derive a threshold from the results.** A threshold absent from the approved manifest makes the run `Not Ready`. It is not inferred, rounded, or borrowed from a previous run.
- **Report slice and veto outcomes separately from the aggregate.** Collapsing them into one number destroys the evidence that justifies the verdict.

## Worked example

A run measures 0.91 against an approved aggregate threshold of 0.85. Every critical slice clears its minimum. One case out of 240 triggered the factual-invention veto.

The verdict is **Fail**.

Step 2 decides it. The 0.91 is still reported, the slice results are still reported, and the single triggering case is reported with its output and trace — but no aggregate result can buy off a veto. Reporting this run as `Pass` with a note about one bad case would invert the rule the veto exists to enforce.

Counter-example: the same run with no veto triggered and one critical slice at 0.79 against a minimum of 0.80 is also **Fail**, at step 3, despite the 0.91 aggregate.

## What this does not cover

- **The value of any threshold, slice minimum or veto condition.** These are approved before the run. This file applies them; it does not set them.
- **Whether a `Fail` blocks a release.** That is a business decision taken by the authorized owner, who may accept, accept with conditions, or refuse.
- **Whether a veto was correctly defined.** A veto that fires on the wrong condition is a design defect, raised as a finding, not corrected mid-run.
- **What the report must contain.** Structure and required evidence fields are governed by the evidence policy reference.
