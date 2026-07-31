---
type: moc
status: reviewed
audience: [qa, engineering, data-ai]
---

# Module 05 — Running it

**Objective:** turn an approved design into a manifest a runner will execute, and read the evidence it produces.

This is the first module where you produce a file the machine reads. It is also where `Not Ready` stops being a concept and becomes an exit code.

## Notes, in order

| # | Note | Answers |
|:--:|---|---|
| 12 | [End-to-end methodology](end-to-end-methodology.md) | The seven steps, in execution order |
| 13 | [Minimum execution manifest](evaluation-manifest.md) | What an approved run declares before it starts |
| 14 | [What the automated evaluation runner should produce](reporting-and-evidence.md) | Which evidence must survive the run |

## Exercise

[Fill a manifest from a brief](exercises/fill-a-manifest-from-a-brief.md) — you will run what you write. Then compare with [the solution](exercises/solutions/fill-a-manifest-from-a-brief.md).

## Read alongside

[Worked example 04 — Hybrid agent](../worked-examples/04-hybrid-agent/README.md), for a manifest that carries a DoD gate and a DoT gate at once — and fails while everything probabilistic is excellent.

Two toolkit references become useful here and stay useful afterwards: [`policies/verdict-rules.md`](../toolkit/policies/verdict-rules.md), the order acceptance is decided in and why averages come last, and [`policies/readiness-rules.md`](../toolkit/policies/readiness-rules.md), which is what the runner is actually applying when it refuses to run. The [schemas](../toolkit/schemas/) let you validate an artefact before anyone reviews it.

## Mastery criterion

From a brief containing both approved and unapproved decisions, you produce a manifest that **runs and reports `Not Ready` for exactly the right reasons** — and you can say, before running it, which blockers it will list.

Predicting the blockers matters more than producing them. It means you can read a design and know what it cannot yet conclude.

---

Previous: [Exercise — Build a golden set](../04-designing-evidence/exercises/build-a-golden-set.md) · [Course map](../00-orientation/progression.md) · Next: [End-to-end methodology](end-to-end-methodology.md)
