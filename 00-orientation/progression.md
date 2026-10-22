---
type: moc
status: reviewed
audience: [qa, product-owner, engineering, data-ai, compliance]
---

# The course map

Nine modules in two parts, in order. Each ends with an exercise and a mastery criterion you can check against yourself.

**Part 1, modules 01 and 02, holds for any product, with or without AI:** designing tests and running a campaign. If you already know the basics of testing, start at [module 03](../03-first-evaluation/run-your-first-evaluation.md). **Part 2, modules 03 to 09, is about what generative AI adds**: deciding whether answers are reliable enough to ship, and proving it.

**The `Next` link is the course.** It runs from [how to use this course](how-to-use-this-course.md) to the capstone and passes through every module opener and **every exercise** — 53 steps. Follow it and you cannot skip an exercise by accident. This page exists to jump around, not to make progress.

**Time:** roughly ten to fourteen hours of work, spread however you like, of which about two for part 1. The capstone is extra, and it is the part that proves anything.

## Before you start

- [How to use this course](how-to-use-this-course.md) — how to work through it, and what will make you fail
- [Prerequisites](prerequisites.md) — Python 3.10, a terminal, two pip packages
- [Glossary](../toolkit/glossary.md) — keep it open. *Oracle*, *slice*, *veto*, *groundedness* and *DoT* all appear before they are defined

# Part 1: testing a product

## Module 01: [Testing basics](../01-testing-basics/README.md)

**What a test proves, where its expected result comes from, and at which level to prove it.** It starts with a run, like the course does.

| # | Note | Answers |
|:--:|---|---|
| 1 | [A green suite on a bug](../01-testing-basics/a-green-suite-on-a-bug.md) | What a test proves, and where its expected result must come from |
| 2 | [A criterion someone can test](../01-testing-basics/testable-criteria.md) | What makes an acceptance criterion testable |
| 3 | [From criteria to test cases](../01-testing-basics/from-criteria-to-cases.md) | The techniques that turn one criterion into its cases |
| 4 | [The right level for each test](../01-testing-basics/test-levels.md) | Component, integration or system, and what no level proves |

**Exercises:** [Judge and rewrite criteria](../01-testing-basics/exercises/judge-and-rewrite-criteria.md) · [One criterion, end to end](../01-testing-basics/exercises/one-criterion-end-to-end.md)

## Module 02: [Running a campaign](../02-running-a-campaign/README.md)

**Frame it, run it, turn failures into defects, and say where it stands without claiming more than was tested.**

| # | Note | Answers |
|:--:|---|---|
| 5 | [The frame of a campaign](../02-running-a-campaign/the-frame-of-a-campaign.md) | Scope, testable requirements, entry and exit criteria |
| 6 | [Run, and read the results](../02-running-a-campaign/run-and-read-results.md) | The six verdicts, and how to read a test report by level |
| 7 | [From a failure to a defect](../02-running-a-campaign/from-failure-to-defect.md) | Qualifying a failure, writing a defect, closing it |
| 8 | [Where do we stand?](../02-running-a-campaign/where-do-we-stand.md) | The figures of a campaign, and what each one hides |

**Exercises:** [Read a pipeline report](../02-running-a-campaign/exercises/read-a-pipeline-report.md) · [Write a defect](../02-running-a-campaign/exercises/write-a-defect.md) · [The status, and the report](../02-running-a-campaign/exercises/status-and-report.md)

# Part 2: evaluating generative AI

## Module 03 — First evaluation

**You see it work before you understand it.** Run a real evaluation, watch it fail while every average passes.

| Note | Answers |
|---|---|
| [Run your first evaluation](../03-first-evaluation/run-your-first-evaluation.md) | What does this actually do? |
| [What just happened](../03-first-evaluation/what-just-happened.md) | Why did a run at 96% fail, and why is `Not Ready` not `Fail`? |

## Module 04 — [Foundations](../04-foundations/README.md)

**Why AI changes testing, and how to classify what you are looking at.**

| # | Note | Answers |
|:--:|---|---|
| 9 | [Why AI products need a different testing approach](../04-foundations/testing-foundations.md) | Why exact-match assertions stop working |
| 10 | [One product can contain three types of behaviour](../04-foundations/output-classification.md) | How to classify an observable behaviour — **two** questions, not one |
| 11 | [The Hybrid validation model](../04-foundations/dod-dot-hybrid.md) | How the gates combine, and what the acceptance rule is |

**Exercise:** [Classify five behaviours](../04-foundations/exercises/classify-five-behaviours.md)

## Module 05 — [The two gates](../05-the-two-gates/README.md)

**What each gate proves, and what it refuses to conclude.** One exercise per gate.

| # | Note | Answers |
|:--:|---|---|
| 12 | [DoD: testing deterministic behaviour](../05-the-two-gates/definition-of-done.md) | What belongs in a Definition of Done, and how its gate runs |
| 13 | [DoT: evaluating probabilistic quality](../05-the-two-gates/definition-of-trustworthy.md) | What a Definition of Trustworthy proves, and its ten mandatory components |

**Exercises:** [Run a DoD gate](../05-the-two-gates/exercises/run-a-dod-gate.md) · [Score a DoT against its ten components](../05-the-two-gates/exercises/score-a-dot-against-its-ten-components.md)

## Module 06 — [What to measure](../06-what-to-measure/README.md)

**Short. One question: is this number measuring the thing?**

| # | Note | Answers |
|:--:|---|---|
| 14 | [What exactly should we evaluate](../06-what-to-measure/evaluators-and-metrics.md) | Which evaluation families exist, and how to pick the simplest valid evaluator |
| 15 | [Does the metric measure the thing](../06-what-to-measure/does-the-metric-measure-it.md) | Whether your metric measures the property or something correlated with it |
| 16 | [AI-as-a-judge: useful, but not an oracle](../06-what-to-measure/ai-judge-calibration.md) | When an LLM may score outputs, and under which controls |

**Exercise:** [Calibrate a judge](../06-what-to-measure/exercises/calibrate-a-judge.md)

## Module 07 — [Designing the evidence](../07-designing-evidence/README.md)

**Where the craft is. Two sittings, and do not start the golden-set exercise tired.**

| # | Note | Answers |
|:--:|---|---|
| 17 | [From a business requirement to executable evidence](../07-designing-evidence/requirement-to-evidence.md) | A worked example, end to end |
| 18 | [Building a Golden Dataset](../07-designing-evidence/golden-datasets.md) | What a governed evaluation set contains, and how it lives |
| 19 | [Protecting evaluation data](../07-designing-evidence/data-protection.md) | Which decisions must be taken before the data exists, and who owns them |
| 20 | [Thresholds, slices and vetoes](../07-designing-evidence/thresholds-slices-vetoes.md) | How acceptance is decided, and what overrides an average |
| 21 | [How many cases is enough](../07-designing-evidence/how-many-cases-is-enough.md) | What a slice population lets you conclude, and what it does not |

**Exercises:** [Write a veto an average hides](../07-designing-evidence/exercises/write-a-veto-an-average-hides.md) · [Build a golden set](../07-designing-evidence/exercises/build-a-golden-set.md)

## Module 08 — [Running it](../08-running-it/README.md)

**From a design to an executed run with evidence that survives it.**

| # | Note | Answers |
|:--:|---|---|
| 22 | [End-to-end methodology](../08-running-it/end-to-end-methodology.md) | The seven steps, in execution order |
| 23 | [Minimum execution manifest](../08-running-it/evaluation-manifest.md) | What an approved run declares before it starts |
| 24 | [What the automated evaluation runner should produce](../08-running-it/reporting-and-evidence.md) | Which evidence must survive the run |

**Exercise:** [Fill a manifest from a brief](../08-running-it/exercises/fill-a-manifest-from-a-brief.md)

## Module 09 — [Governance](../09-governance/README.md)

**Where automation stops and a human decides — and how to say so on a release evening.**

| # | Note | Answers |
|:--:|---|---|
| 25 | [Roles and human gates](../09-governance/roles-and-human-gates.md) | Who decides what, and where automation stops |
| 26 | [Holding the boundary](../09-governance/holding-the-boundary.md) | How to refuse a decision that is not yours **and stay useful** |
| 27 | [The methodology in five rules](../09-governance/five-rules-recap.md) | The whole thing, compressed |

**Exercise:** [Name the decision owner](../09-governance/exercises/name-the-decision-owner.md)

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
| [01 Deterministic API](../worked-examples/01-deterministic-api/README.md) | Module 05, with the DoD exercise |
| [02 LLM summary](../worked-examples/02-llm-summary/README.md) | Module 03, then again at module 07 |
| [03 RAG assistant](../worked-examples/03-rag-assistant/README.md) | Module 06 |
| [04 Hybrid agent](../worked-examples/04-hybrid-agent/README.md) | Module 04, and again at module 08 |

## Not on the path

[The annexes](../annexes/README.md) hold what this course deliberately leaves out: authoring the coding-agent skills that automate this, and the artefacts for **adopting** the methodology in an organisation — decisions to agree, and a pilot proposal. Useful if that is your job; not a skill for running the tests.
