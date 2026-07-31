# Expected report

Produced by running `manifest.yaml` against `dataset.jsonl` with the mock adapter. Re-running must reproduce this exactly.

## Verdict

**Fail** — the DoD gate failed.

| Gate | Result |
|---|---|
| **DoD** | **Fail** — 2 assertion failures |
| **DoT** | **Not evaluated** — no DoT evaluator is declared |

## Versions

| | |
|---|---|
| Candidate | `mock-report-api` 1.0.0, frozen |
| Evaluators | `response-schema`, `audit-event`, both `gate: DoD` 1.0.0 |
| Dataset | 1.0.0, synthetic |
| Decision owner | engineering lead, report API |

## Assertions

No threshold. An assertion holds or it does not.

| Case | Assertion | Finding |
|---|---|---|
| `API-09` | `response-schema` | required output field missing or empty: `error_code` |
| `API-09` | `audit-event` | expected tool call was not made: `write_audit_event` |

Each entry carries the findings of that assertion alone. Two controls failed on one case, and each names what it found.

## Coverage

| | |
|---|---|
| Eligible | 10 |
| Completed | 10 |
| Cases with at least one finding | 1 |

## Reading

`API-09` presented an expired token and received the report contents. The API returned no error code and wrote no audit event: the refusal did not happen, and nothing recorded that it did not happen.

Nine of ten cases conform. No aggregate makes the tenth acceptable, and none is computed — an access-control leak is not a quality level.

The absence of a `thresholds` entry is deliberate and readiness accepts it, because an evaluation made entirely of assertions has nothing to approve a threshold for.
