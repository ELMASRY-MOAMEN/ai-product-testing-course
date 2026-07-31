# AI Product Testing — the course

**Learn to evaluate products that embed AI.** From your first failing run to a complete evaluation package you could hand to a decision owner.

Seven modules, eight exercises with worked solutions, one capstone. Python 3.10, a terminal, and two pip packages.

> **Fifteen minutes to decide whether this is for you:** do the [setup](00-orientation/prerequisites.md), then run [module 01](01-warm-up/run-your-first-evaluation.md). You will execute a real evaluation, watch it fail while every average passes, and understand why that failure is the point.

From there, follow the `Next` link at the foot of each page. It runs to the capstone through every module and every exercise — there is nothing else to keep track of.

## What you will be able to do

| | |
|---|---|
| **A** | Classify an observable behaviour and pick the validation path it requires |
| **B** | Build the evidence: a governed dataset, metrics, thresholds, slices and vetoes |
| **C** | Report **Not Ready** and name the role that owns a missing decision, instead of inventing a value |
| **D** | Run an approved evaluation and read its verdict as evidence, not as a score |

Criterion **C** is the one this course is built around, and the one most people fail first.

## The idea it exists for

When several outputs are acceptable, exact comparison stops being a valid oracle. Testing does not disappear — it changes shape. It becomes an experiment over a population of cases, with an approved threshold, risk-sensitive slices analysed independently, and vetoes that block acceptance regardless of the average.

That gate has a name here: the **Definition of Trustworthy (DoT)**. It sits beside the Definition of Done, which keeps doing its job on everything deterministic.

## Start

| You are | Go to |
|---|---|
| **Starting the course** | [How to use this course](00-orientation/how-to-use-this-course.md) — then just follow `Next` |
| In a hurry, want to see it work first | [Setup](00-orientation/prerequisites.md), then [run your first evaluation](01-warm-up/run-your-first-evaluation.md) — 15 min |
| Looking for a specific module | [The course map](00-orientation/progression.md) |
| Already trained, here for the tools | [The toolkit](toolkit/README.md) |

## What is in here

| Folder | What it holds |
|---|---|
| `00-orientation/` | The map, the method, the prerequisites |
| `01-warm-up/` | A real run, before any theory |
| `02-foundations/` → `07-governance/` | The six teaching modules: notes, exercises, solutions |
| `toolkit/` | Checklists, templates, policies and schemas you keep using afterwards |
| `worked-examples/` | Four complete evaluations to read — [never to copy](worked-examples/READ-ME-BEFORE-COPYING.md) |
| `capstone/` | Evaluate a capability of your own choosing, and be assessed on it |
| `lab/` | The runner that executes the exercises |
| `annexes/` | Out of scope for the course: skill authoring, and adopting the method in an organisation |

## Three rules that hold everywhere in this course

1. **Never invent a threshold, a slice minimum, a veto condition, a reference answer or an approval.** Keep the placeholder, report `Not Ready`, and name the role that owns the decision.
2. **Deterministic conformance and probabilistic quality are separate gates.** They combine; they never merge.
3. **A good average never cancels a critical failure.**

## Scope

This course teaches the **evaluation of products that embed AI**. It does not teach how to build models, and it does not benchmark them.

## Status and licence

The methodology is proposed, for discussion and pilot application. It comes from the companion repository `ai-product-testing-skills`, which packages the same practices as skills for coding agents; this repository is the human path through them, and stands alone.

MIT — see [LICENSE](LICENSE).
