# Error Classification

Governs how a failure observed during a run is attributed, so that only the candidate's failures count against the candidate.

## Rule

Every failure belongs to exactly one class. The class determines whether the case counts as a scored failure, is excluded from scoring, or ends the run.

| Class | Meaning | Effect on the verdict |
|---|---|---|
| **Candidate failure** | The candidate produced an output that did not meet the criterion | Scored. Counts as a failure. |
| **Harness failure** | The adapter, network or runner failed before or after the candidate | Not scored. Case marked incomplete. |
| **Data failure** | The case itself is malformed, unapproved or missing its reference | Not scored. Case excluded and reported as a dataset defect. |
| **Evaluator failure** | The evaluator errored, or returned a result outside its declared range | Ends the run. Nothing measured by that evaluator is trustworthy. |

Attributing a harness or data failure to the candidate manufactures a defect. Attributing a candidate failure to the harness hides one. Both corrupt the evidence.

## How to apply

Ask, in order:

1. **Did the candidate return an output at all?** No, and the cause is transport, timeout or adapter error → harness failure.
2. **Was the case usable?** Missing reference, unapproved annotation, malformed input → data failure.
3. **Did the evaluator return a valid score?** Error, or a score outside its range → evaluator failure. Stop the run.
4. **Otherwise** → candidate failure. Score it.

Report every class separately. A run that completed 200 of 240 cases must say why the 40 did not complete, broken down by class, because a reader cannot otherwise judge whether the aggregate means anything.

When harness or data failures exceed the coverage the manifest requires, the run is **not** a `Fail` — it is `Not Ready`, because the declared population was never evaluated.

## Worked example

A run reports 12 failures. Investigation shows: 7 cases where the candidate omitted a mandatory section, 4 cases where the adapter timed out, 1 case whose reference answer was never approved.

Only the 7 are scored failures. The 4 are harness failures and the case is incomplete. The 1 is a data failure and the case is excluded, plus reported as a dataset defect for correction.

Reporting 12 failures against the threshold would understate the candidate by 40 percent and hide a real defect in the dataset.

## What this does not cover

- **Retry policy.** Whether and how often a harness failure may be retried is declared before the run.
- **Coverage minimums.** The proportion of the population that must complete is an approved acceptance criterion.
- **Fixing the causes.** This file attributes failures; remediation is out of scope for a run.
