# Execution Policy

Governs how an approved run is executed, so that its result stays attributable to a known configuration.

## Rule

A run may start only when candidate, evaluators and dataset are **frozen** at declared versions. Nothing that affects an output may change while the run is in progress.

Execute only cases marked eligible. Submit the controlled input exactly as the case declares it. Record the output and the execution trace for every case, including the ones that error.

Never modify the manifest during a run. A manifest that needs changing ends the run and starts a new one under a new version.

Never retry silently. A retry that is not declared and counted turns a flaky result into an apparently stable one.

## How to apply

Before the first case:

1. Resolve every declared version and record it. An unresolvable version ends the run as `Not Ready`.
2. Confirm the adapter, evaluator implementations and dataset are readable.
3. Record the variability controls in force: model, prompt, tools, parameters and repetition count.

During the run:

| Situation | Action |
|---|---|
| Case marked ineligible | Skip before invocation. Never score then discard. |
| Candidate errors or times out | Record the error, mark the case incomplete, continue |
| Declared repetitions above one | Run every repetition; report dispersion, not only the mean |
| Evaluator unavailable mid-run | Stop. A partially evaluated population is not a population. |

After the last case:

4. Report coverage: cases eligible, executed, completed, incomplete.
5. Report the frozen versions alongside the results, in the same artefact.

## Worked example

A run of 240 cases declares three repetitions per case. At case 118 the prompt template is corrected to fix a typo.

The run is **void**. Cases 1 to 117 answered a different prompt from cases 118 to 240, so the aggregate describes no single candidate. The correct action is to abandon the run, version the corrected prompt, and start again. Reporting the aggregate with a footnote about the change would present two candidates as one.

Contrast: the candidate times out on case 43. That case is marked incomplete, the run continues, and coverage is reported as 239 completed of 240 eligible. The result stands, with its coverage stated.

## What this does not cover

- **Which cases are eligible.** Eligibility is a property of the dataset, decided before execution.
- **How many repetitions are enough.** That is a variability control approved in the manifest.
- **How the outcome is decided.** Verdict computation is governed by the verdict rules reference.
- **How errors are classified.** See the error classification reference.
