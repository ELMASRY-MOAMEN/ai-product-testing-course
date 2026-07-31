# Deterministic API — a run with no threshold at all

Synthetic, runnable end to end. Every evaluator here **asserts**; none measures. There is no threshold to approve, no aggregate to compute, and no slice to inspect — and that is correct, not an omission.

It is the counterpart to the other three examples. Where they show the ways a probabilistic run gets refused, this one shows what evaluation looks like when nothing is probabilistic.

## What it evaluates

A report-creation API. Valid requests create a report and write an audit event; invalid ones return an error code and write a rejection event; unauthorised callers are refused.

| | |
|---|---|
| Framework | DoD |
| Cases | 10 across three slices: 4 valid-request, 3 invalid-input, 3 access-control |
| Evaluators | `schema_conformance`, `tool_call_conformance` — both `gate: DoD` |
| Thresholds | **none** |

## Run it

```bash
python .github/skills/run-product-evaluation/scripts/run_evaluation.py examples/01-deterministic-api/manifest.yaml
```

## What it produces

```
gates: {"DoD": "Fail", "DoT": "Not evaluated"}
reasons: ["DoD gate: 2 assertion failure(s) on audit-event, response-schema"]
```

**Verdict: Fail**, on one case.

| Case | Assertion | Finding |
|---|---|---|
| `API-09` | `response-schema` | required output field missing or empty: `error_code` |
| `API-09` | `audit-event` | expected tool call was not made: `write_audit_event` |

## The failure

`API-09` submits an **expired token** and asks for report 4473. The API returned the report contents.

No error code. No audit event. The access-control refusal did not happen, and nothing recorded that it did not happen.

Nine cases out of ten conform. There is no average that makes this acceptable, and no threshold anyone could have approved that would let it through — which is exactly why it is asserted rather than scored.

## Why there is no threshold

`acceptance.thresholds` is empty in the manifest. Readiness accepts that, because it only requires an approved threshold when a DoT evaluator is declared.

An assertion has nothing to average. "Nine out of ten schemas conformed" is not a quality level, it is one broken contract and nine intact ones. Reporting it as 0.9 against an approved 0.85 would convert a conformance failure into a passing measurement — the manoeuvre [the hybrid example](../04-hybrid-agent/README.md) demonstrates in one YAML edit.

## Try it

Set `mock_tool_call` on `API-09` to the expected audit event, and give it an `mock_error_code`. The run reports **Pass** with `DoD: "Pass"`, and the access-control behaviour is genuinely conformant rather than averaged into acceptability.

## The set

| Example | Fails at | Shows |
|---|---|---|
| **01 — this one** | DoD gate | Assertion, no threshold anywhere |
| [02 — LLM summary](../02-llm-summary/README.md) | Veto | One occurrence overrides a 0.96 aggregate |
| [03 — RAG assistant](../03-rag-assistant/README.md) | Critical slice | 0.833 on a slice refuses a 0.958 aggregate |
| [04 — hybrid agent](../04-hybrid-agent/README.md) | DoD, while DoT passes | Acceptance is conjunctive |

## Related

- [DoD: testing deterministic behaviour](../../03-the-two-gates/definition-of-done.md) — including why access control is usually a veto candidate
- [One product can contain three types of behaviour](../../02-foundations/output-classification.md)
