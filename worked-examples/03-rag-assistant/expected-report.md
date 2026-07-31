# Expected report

Produced by running `manifest.yaml` against `dataset.jsonl` with the mock adapter. Re-running must reproduce these figures exactly.

## Verdict

**Fail** — critical slice `policy-change` below its approved minimum.

No veto was triggered, and every aggregate threshold was met. The run fails at step 3 of the verdict order, not step 2.

## Versions

| | |
|---|---|
| Candidate | `mock-rag-assistant` 1.0.0, frozen |
| Evaluators | `retrieval-recall`, `answer-facts-recall`, `citation-support`, all 1.0.0 |
| Dataset | 1.0.0 |
| Decision owner | product owner, HR handbook assistant |

## Coverage

| | |
|---|---|
| Eligible | 24 |
| Completed | 24 |
| Cases with no finding | 20 |
| Cases with at least one finding | 4 |

## Aggregate results

| Evaluator | Measured | Approved threshold | Outcome |
|---|:--:|:--:|:--:|
| `retrieval-recall` | 0.958 | 0.85 | pass |
| `answer-facts-recall` | 0.889 | 0.85 | pass |
| `citation-support` | 1.000 | — | no veto triggered |

## Slice results

| Slice | Population | Measured | Approved minimum | Outcome |
|---|:--:|:--:|:--:|:--:|
| `policy-change` | 6 | **0.833** | 0.85 | **fail** |
| `multi-source` | 4 | 1.000 | 0.85 | pass |

## Failing cases

| Case | Slice | Finding |
|---|---|---|
| `P-01` | policy-change | required source not retrieved: `HB-REMOTE-06-V3`; missing required fact: three days per week |
| `P-02` | policy-change | required source not retrieved: `HB-LEAVE-12-V4`; missing required fact: sixteen weeks |
| `S-07` | standard | missing required fact: no payment |
| `M-03` | multi-source | missing required fact: logged in the portal |

## Reading

`P-01` and `P-02` retrieved the **superseded** version of a policy that had changed — `HB-REMOTE-06-V2` where the current version is `V3`, `HB-LEAVE-12-V3` where the current is `V4`. Both answers are fluent, cite a real document, and state the entitlement that applied last year.

Two cases out of twenty-four decide this run. The overall retrieval recall is 0.958; a reader looking only at that number would ship a system that tells employees the wrong parental-leave entitlement whenever the policy has recently changed.

That concentration is exactly what a critical slice exists to expose, and it is invisible in every aggregate on this page.

Note that `citation-support` reports 1.000 and triggers no veto. The candidate cited what it retrieved: the citations are honest, the retrieval was not. Groundedness and correctness are different questions, and a system can be perfectly grounded in the wrong document.
