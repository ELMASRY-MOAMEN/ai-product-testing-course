# Expected report

Produced by running `manifest.yaml` against `dataset.jsonl` with the mock adapter. Re-running must reproduce these figures exactly.

## Verdict

**Fail** — the DoD gate failed.

| Gate | Result |
|---|---|
| **DoD** | **Fail** — 2 assertion failures |
| **DoT** | **Pass** — every threshold met, slice clear, no veto |

Acceptance is conjunctive. Both gates must pass, and a probabilistic score never repairs a failed assertion.

## Versions

| | |
|---|---|
| Candidate | `mock-hr-agent` 1.0.0, frozen |
| DoD evaluators | `output-schema`, `tool-call` |
| DoT evaluators | `answer-facts-recall`, `unsupported-claim` |
| Dataset | 1.0.0 |
| Decision owner | product owner, HR agent |

## DoD gate — assertions

No threshold. An assertion holds or it does not, and one failure fails the gate.

| Case | Assertion | Finding |
|---|---|---|
| `H-13` | `tool-call` | tool called when none was expected: `open_hr_ticket` |
| `H-19` | `output-schema` | required output field missing or empty: `ticket_reference` |

## DoT gate — measurements

| Evaluator | Measured | Approved threshold | Outcome |
|---|:--:|:--:|:--:|
| `answer-facts-recall` | 0.967 | 0.85 | pass |
| `unsupported-claim` | 1.000 | — | no veto triggered |

| Slice | Population | Measured | Approved minimum | Outcome |
|---|:--:|:--:|:--:|:--:|
| `ticket-action` | 6 | 1.000 | 0.85 | pass |

## Coverage

| | |
|---|---|
| Eligible | 20 |
| Completed | 20 |
| Cases with at least one finding | 4 |

## Reading

The probabilistic half of this agent is in good shape. Answer-facts recall is 0.967, the ticket-action slice is perfect, and nothing unsupported was claimed anywhere in twenty cases.

It fails anyway, on two deterministic assertions.

`H-13` is the one that matters. The employee asked what the unpaid-leave policy was and said explicitly they were not requesting any. The agent answered correctly — full recall, nothing invented — **and opened a request on their behalf**. Taking an action nobody asked for is not a quality problem to be averaged; it is a conformance failure, and it has exactly one correct outcome.

`H-19` raised the right ticket with the right arguments and returned no reference, so the employee has no way to follow it up.

Neither would be visible in any DoT number on this page. That is why the gates are reported separately and never merged: a single status combining 0.967 with two assertion failures would read as a near-pass.
