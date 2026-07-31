# Expected report

Produced by running `manifest.yaml` against `dataset.jsonl` with the mock adapter. Re-running must reproduce these figures exactly; the candidate, evaluators and dataset are all frozen.

## Verdict

**Fail** — 1 veto triggered.

## Versions

| | |
|---|---|
| Candidate | `mock-summariser` 1.0.0, frozen |
| Evaluators | `required-facts-recall` 1.0.0, `unsupported-claim` 1.0.0 |
| Dataset | 1.0.0 |
| Decision owner | product owner, meeting-report capability |

## Coverage

| | |
|---|---|
| Eligible | 25 |
| Completed | 25 |
| Cases with no finding | 21 |
| Cases with at least one finding | 4 |

## Aggregate results

| Evaluator | Measured | Approved threshold | Outcome |
|---|:--:|:--:|:--:|
| `required-facts-recall` | 0.960 | 0.85 | pass |

## Slice results

Reported independently of the aggregate, as required.

| Slice | Population | Measured | Approved minimum | Outcome |
|---|:--:|:--:|:--:|:--:|
| `regulated` | 8 | 0.958 | 0.90 | pass |
| `second-language` | 5 | 0.933 | 0.85 | pass |

## Vetoes

| Case | Finding |
|---|---|
| `MR-020` | forbidden claim present: mandate approved |

## Failing cases

Retained in full, because a failure without its output cannot be diagnosed.

| Case | Slice | Recall | Finding |
|---|---|:--:|---|
| `MR-007` | standard | 0.667 | missing required fact: budget owner absent |
| `MR-018` | regulated | 0.667 | missing required fact: no change requested |
| `MR-022` | second-language | 0.667 | missing required fact: signature en attente |
| `MR-020` | regulated | 1.000 | forbidden claim present: mandate approved |

`MR-020` is the case that decides the run. Its recall is perfect: every required fact is present. It fails because it also asserts an approval the source never gave, and one occurrence of that is not a matter of degree.

## Reading

The aggregate cleared its threshold, both critical slices cleared their minimums, and the verdict is still `Fail`. The order of application is what produces this: vetoes are evaluated before slices, and slices before aggregates, so no average can absorb a critical failure.
