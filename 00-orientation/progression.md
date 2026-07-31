---
type: moc
status: reviewed
audience: [qa, product-owner, engineering, data-ai, compliance]
---

# The course map

Six modules, in order. Each one ends with an exercise and a mastery criterion you can check against yourself.

**The `Next` link is the course.** It runs from [how to use this course](how-to-use-this-course.md) to the capstone and passes through every module opener and **every exercise** — 34 steps. Follow it and you cannot skip an exercise by accident. This page exists to jump around, not to make progress.

**Time:** roughly eight to twelve hours of work, spread however you like. The capstone is extra, and it is the part that proves anything.

## Before you start

- [How to use this course](how-to-use-this-course.md) — how to work through it, and what will make you fail
- [Prerequisites](prerequisites.md) — Python 3.10, a terminal, two pip packages
- [Glossary](../toolkit/glossary.md) — keep it open. *Oracle*, *slice*, *veto*, *groundedness* and *DoT* all appear before they are defined

## Module 01 — Warm-up

**You see it work before you understand it.** Run a real evaluation, watch it fail while every average passes.

| Note | Answers |
|---|---|
| [Run your first evaluation](../01-warm-up/run-your-first-evaluation.md) | What does this actually do? |
| [What just happened](../01-warm-up/what-just-happened.md) | Why did a run at 96% fail, and why is `Not Ready` not `Fail`? |

## Module 02 — [Foundations](../02-foundations/README.md)

**Why AI changes testing, and how to classify what you are looking at.**

| # | Note | Answers |
|:--:|---|---|
| 1 | [Why AI products need a different testing approach](../02-foundations/testing-foundations.md) | Why exact-match assertions stop working |
| 2 | [One product can contain three types of behaviour](../02-foundations/output-classification.md) | How to classify an observable behaviour — **two** questions, not one |
| 3 | [The Hybrid validation model](../02-foundations/dod-dot-hybrid.md) | How the gates combine, and what the acceptance rule is |

**Exercise:** [Classify five behaviours](../02-foundations/exercises/classify-five-behaviours.md)

## Module 03 — [The two gates](../03-the-two-gates/README.md)

**What each gate proves, and what it refuses to conclude.**

| # | Note | Answers |
|:--:|---|---|
| 4 | [DoD: testing deterministic behaviour](../03-the-two-gates/definition-of-done.md) | What belongs in a Definition of Done, and how its gate runs |
| 5 | [DoT: evaluating probabilistic quality](../03-the-two-gates/definition-of-trustworthy.md) | What a Definition of Trustworthy proves, and its ten mandatory components |

**Exercise:** [Score a DoT against its ten components](../03-the-two-gates/exercises/score-a-dot-against-its-ten-components.md)

## Module 04 — [Designing the evidence](../04-designing-evidence/README.md)

**The longest module, and the one that carries the craft.**

| # | Note | Answers |
|:--:|---|---|
| 6 | [What exactly should we evaluate](../04-designing-evidence/evaluators-and-metrics.md) | Which evaluation families exist, and how to pick the simplest valid evaluator |
| 7 | [From a business requirement to executable evidence](../04-designing-evidence/requirement-to-evidence.md) | A worked example, end to end |
| 8 | [Building a Golden Dataset](../04-designing-evidence/golden-datasets.md) | What a governed evaluation set contains, and how it lives |
| 9 | [Protecting evaluation data](../04-designing-evidence/data-protection.md) | Which decisions must be taken before the data exists, and who owns them |
| 10 | [Thresholds, slices and vetoes](../04-designing-evidence/thresholds-slices-vetoes.md) | How acceptance is decided, and what overrides an average |
| 11 | [AI-as-a-judge: useful, but not an oracle](../04-designing-evidence/ai-judge-calibration.md) | When an LLM may score outputs, and under which controls |

**Exercises:** [Write a veto an average hides](../04-designing-evidence/exercises/write-a-veto-an-average-hides.md) · [Build a golden set](../04-designing-evidence/exercises/build-a-golden-set.md)

## Module 05 — [Running it](../05-running-it/README.md)

**From a design to an executed run with evidence that survives it.**

| # | Note | Answers |
|:--:|---|---|
| 12 | [End-to-end methodology](../05-running-it/end-to-end-methodology.md) | The seven steps, in execution order |
| 13 | [Minimum execution manifest](../05-running-it/evaluation-manifest.md) | What an approved run declares before it starts |
| 14 | [What the automated evaluation runner should produce](../05-running-it/reporting-and-evidence.md) | Which evidence must survive the run |

**Exercise:** [Fill a manifest from a brief](../05-running-it/exercises/fill-a-manifest-from-a-brief.md)

## Module 06 — [Governance](../06-governance/README.md)

**Where automation stops and a human decides.**

| # | Note | Answers |
|:--:|---|---|
| 15 | [Roles and human gates](../06-governance/roles-and-human-gates.md) | Who decides what, and where automation stops |
| 16 | [Decisions required from the group](../06-governance/decisions-required.md) | What must be agreed before adoption |
| 17 | [Pilot proposal](../06-governance/pilot-proposal.md) | How to try the methodology on one real capability |
| 18 | [The methodology in five rules](../06-governance/five-rules-recap.md) | The whole thing, compressed |

**Exercise:** [Name the decision owner](../06-governance/exercises/name-the-decision-owner.md)

## Capstone

[Evaluate a capability of your own choosing](../capstone/brief.md), assessed against [the rubric](../capstone/rubric.md). It is the only part of this course that proves you can do the work.

## The toolkit

Not part of the reading order. Open it while you work, and keep it after the course.

| Reference | Use |
|---|---|
| [Readiness checklist](../toolkit/readiness-checklist.md) | Deciding whether an evaluation may start |
| [Scenario-writing rules](../toolkit/gherkin-and-test-contracts.md) | Writing DoD and DoT scenarios |
| [Glossary](../toolkit/glossary.md) | Shared vocabulary |
| [Templates, policies and schemas](../toolkit/README.md) | The artefacts you will fill in |

## Worked examples

Four complete evaluations, to read alongside the modules. Read [this first](../worked-examples/READ-ME-BEFORE-COPYING.md) — copying one as a starting artefact is the most common way to fail this course.

| Example | Read it during |
|---|---|
| [01 Deterministic API](../worked-examples/01-deterministic-api/README.md) | Module 03 |
| [02 LLM summary](../worked-examples/02-llm-summary/README.md) | Module 01, then again at module 04 |
| [03 RAG assistant](../worked-examples/03-rag-assistant/README.md) | Module 04 |
| [04 Hybrid agent](../worked-examples/04-hybrid-agent/README.md) | Module 02, and again at module 05 |
