# Hybrid agent — a run where everything probabilistic is excellent and it fails anyway

Synthetic, runnable end to end. This is the example the methodology has always argued for and never showed: **acceptance is conjunctive**. The DoD gate and the DoT gate must both pass, and a strong quality score never repairs a failed assertion.

## What it evaluates

An HR agent that answers policy questions and can open a ticket on the employee's behalf.

| | |
|---|---|
| Framework | Hybrid |
| Cases | 20 — 14 answer-only, 6 ticket-action |
| DoD evaluators | `schema_conformance`, `tool_call_conformance` |
| DoT evaluators | `required_facts_recall`, `forbidden_claims` |
| Approved threshold | answer-facts recall ≥ 0.85 |
| Critical slice | ticket-action ≥ 0.85 |
| Veto | any unsupported claim |

## Run it

```bash
python lab/run-product-evaluation/scripts/run_evaluation.py worked-examples/04-hybrid-agent/manifest.yaml
```

## What it produces

| Gate | Result |
|---|---|
| **DoT** | **Pass** — recall 0.967, slice 1.000, no veto |
| **DoD** | **Fail** — 2 assertion failures |
| **Overall** | **Fail** |

The probabilistic half is in good shape. Twenty cases, nothing invented, a perfect ticket-action slice. It fails on two assertions.

## The two failures

**`H-13` is the one that matters.** The employee asked what the unpaid-leave policy was, and said explicitly that they were not requesting any. The agent answered correctly — full recall, nothing invented — **and opened a request on their behalf**.

An action taken on someone's behalf that nobody asked for is not a quality problem. It has exactly one correct outcome, so it is asserted, not scored. No amount of answer quality makes it acceptable.

**`H-19`** raised the right ticket with the right routing and returned no reference, so the employee has no way to follow it up.

Neither failure appears in any DoT number on this page.

## Why the gates are not merged

A single status combining 0.967 with two assertion failures would read as a near-pass. It is not: one of those failures is an unrequested action on an employee's record.

DoD assertions carry **no threshold**, because there is nothing to average — a schema conforms or it does not, a tool call was correct or it was not. That is why the report shows `gates: {DoD: Fail, DoT: Pass}` rather than one blended number.

## Try it

Change **both** `gate: DoD` lines to `gate: DoT`. The two assertions become ordinary measurements, each averaging to 0.95, and no threshold is declared against either.

The run reports **Pass**, with `gates: {DoD: "Not evaluated", DoT: "Pass"}`.

The unrequested ticket and the missing reference are still reported case by case — the findings do not disappear. They simply stop failing anything. Two conformance defects have been converted into a 0.95 that nothing checks.

Change only the one on `tool-call` and the run still fails, on the remaining schema assertion. `H-13` becomes invisible to the verdict while the report stays red for another reason, which is the more insidious version: the gate still looks like it is working.

That is the argument for keeping the gates separate, in one edit.

You cannot demonstrate this by *deleting* the `gate` line: the schema requires it, so a missing gate is a validation error rather than a silent default. That is deliberate — a gate is a decision, and a decision should not have a default.

## What else is here

| File | Shows |
|---|---|
| `requirements.md` | Six behaviours classified, and why this is Hybrid |
| `risks.yaml` | Risks pushed to a party and a cost, including one recorded **open** because nobody could size it |
| `scenarios.feature` | DoD and DoT scenarios side by side — a binary `Then` next to a population `Then` |

## Related

- [The Hybrid validation model](../../02-foundations/dod-dot-hybrid.md)
- [DoD: testing deterministic behaviour](../../03-the-two-gates/definition-of-done.md)
- [The LLM summary example](../02-llm-summary/README.md) — failure by veto
- [The RAG example](../03-rag-assistant/README.md) — failure by critical slice
