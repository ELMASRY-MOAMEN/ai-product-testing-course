# Evidence Policy

Governs what a run must retain so its result can be re-examined by someone who did not watch it happen.

## Rule

A verdict without evidence is an opinion. Every run retains, for the whole population:

- the **verdict** and the rule that produced it;
- the **frozen versions** of candidate, evaluators and dataset;
- **per-case** input reference, output, score, evaluator findings and trace reference;
- **slice results and veto states**, reported separately from the aggregate;
- **coverage**: cases eligible, executed, completed, incomplete, with the reason for each incompletion.

All of it is **redacted before it is written**. Keys stay visible so a reader can see that a credential was present and suppressed; values do not.

Evidence that exists but cannot be located is not evidence. Every artefact is addressable from the report.

## How to apply

| Requirement | Test it must pass |
|---|---|
| Reproducible | A reader can identify exactly which candidate produced which output |
| Complete | Every eligible case appears, including the ones that failed or errored |
| Attributable | Each score names the evaluator and its version |
| Separable | Aggregate, slice and veto results are distinguishable, never collapsed |
| Redacted | No credential appears in any retained artefact |

Write the evidence as the run proceeds, not afterwards from memory. A run that crashes at case 200 must leave 199 usable case records.

Report failures in full. The temptation is to summarise them; a failure without its output and trace cannot be diagnosed, so summarising them destroys the reason for keeping them.

## Worked example

A report states: `Fail — aggregate 0.79 against threshold 0.85`.

That is not evidence. It cannot be re-examined, contested or reproduced. It names no candidate version, no evaluator, no failing case, and no slice result.

The same run, reported correctly, names the frozen candidate and evaluator versions, lists all 240 case results with the 51 failures carrying their outputs and traces, gives each slice against its own minimum, states that no veto triggered, and reports coverage of 240 executed and 240 completed. A reader can then agree, disagree, or reproduce.

## What this does not cover

- **Where evidence is stored and for how long.** Location and retention are declared in the manifest before the run.
- **Who may read it.** Access control is an approval, not a runner decision.
- **The verdict itself.** How `Pass`, `Fail` and `Not Ready` are derived is governed by the verdict rules reference.
