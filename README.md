# AI Product Testing — the course

[![validate](https://github.com/ELMASRY-MOAMEN/ai-product-testing-course/actions/workflows/validate.yml/badge.svg)](https://github.com/ELMASRY-MOAMEN/ai-product-testing-course/actions/workflows/validate.yml)

**Learn to test products that embed AI.** From the basics of testing to a complete evaluation package you could hand to a decision owner.

Nine modules in two parts, thirteen exercises with worked solutions, one capstone. Python 3.10, a terminal, and two pip packages — no model, no API key, no network.

## Start here

```bash
git clone https://github.com/ELMASRY-MOAMEN/ai-product-testing-course.git
cd ai-product-testing-course
pip install -r requirements.txt
python lab/run-product-evaluation/scripts/run_evaluation.py worked-examples/02-llm-summary/manifest.yaml
```

That run reports **Fail** while every average passes its threshold. Fifteen minutes on [why that is the point](03-first-evaluation/run-your-first-evaluation.md) will tell you whether this course is for you.

**Part 1**, modules 01 and 02, covers what any product needs: tests whose expected results someone specified, at the right level, and a campaign reported without claiming more than was tested. If you already know it, start with the run above and [module 03](03-first-evaluation/run-your-first-evaluation.md). **Part 2**, modules 03 to 09, covers what generative AI adds.

Then follow the **`Next`** link at the foot of each page. It runs from [the first page](00-orientation/how-to-use-this-course.md) to the capstone through every module and every exercise — there is nothing else to keep track of.

*In a hurry, or coming back for something specific? [The course map](00-orientation/progression.md).*

## What you will be able to do

| | |
|---|---|
| **A** | Classify an observable behaviour and pick the validation path it requires |
| **B** | Build the evidence: a governed dataset, metrics, thresholds, slices and vetoes |
| **C** | Report **Not Ready** and name the role that owns a missing decision, instead of inventing a value |
| **D** | Run an approved evaluation and read its verdict as evidence, not as a score |
| **E** | Design the tests of a behaviour that has one right answer, at the right level, from an expected result someone specified |
| **F** | Run a test campaign and report its state without claiming more than was tested |

Criterion **C** is the one this course is built around, and the one most people fail first.

## The idea it exists for

When several outputs are acceptable, exact comparison stops being a valid oracle. Testing does not disappear — it changes shape. It becomes an experiment over a population of cases, with an approved threshold, risk-sensitive slices analysed independently, and vetoes that block acceptance regardless of the average.

That gate has a name here: the **Definition of Trustworthy (DoT)**. It sits beside the Definition of Done, which keeps doing its job on everything deterministic.

## Three rules that hold everywhere in this course

1. **Never invent a threshold, a slice minimum, a veto condition, a reference answer or an approval.** Keep the placeholder, report `Not Ready`, and name the role that owns the decision.
2. **Deterministic conformance and probabilistic quality are separate gates.** They combine; they never merge.
3. **A good average never cancels a critical failure.**

## What is in here

You only ever need the first two rows. The rest is there when the course sends you to it.

| Folder | What it holds |
|---|---|
| `00-orientation/` | Where you start: how to work through it |
| `01-testing-basics/`, `02-running-a-campaign/` | Part 1: testing a product, for any product, with or without AI |
| `03-first-evaluation/` → `09-governance/` | Part 2: evaluating generative AI, from a real run before any theory to governance |
| `capstone/` | Evaluate a capability of your own choosing, and be assessed on it |
| `toolkit/` | Checklists, templates, policies and schemas you keep using after the course |
| `worked-examples/` | Four complete evaluations to read — [never to copy](worked-examples/READ-ME-BEFORE-COPYING.md) |
| `lab/` | The evaluation runner the exercises execute, and the test-report summary of module 02 |
| `tools/` | The checks that keep this repository honest — links, reading path, documented figures |
| `annexes/` | Deliberately out of scope: skill authoring, and adopting the method in an organisation |

## Scope

This course teaches the **testing of products that embed AI**: designing and running tests for what has one right answer, and evaluating what does not. It does not teach how to build models, it does not benchmark them, and it does not cover performance, security or accessibility testing, which each need their own methods.

## Status

The methodology is proposed, for discussion and pilot application. It comes from the companion repository `ai-product-testing-skills`, which packages the same practices as skills for coding agents; this repository is the human path through them, and stands alone.

Every documented figure in these pages is asserted by [a check that runs on each push](.github/workflows/validate.yml) — if a note says a run reports 0.960 and one veto, it still does.

## Licence

Two parts, because they are two different things:

| | |
|---|---|
| **The written content** — every note, exercise, solution, template and checklist | [CC BY-SA 4.0](LICENSE-CONTENT.md). Credit the source, and keep your version open under the same terms |
| **The code** — `tools/` and `lab/` | [MIT](LICENSE) |

The canonical repository is <https://github.com/ELMASRY-MOAMEN/ai-product-testing-course>; a copy elsewhere may be stale. To cite it, see [CITATION.cff](CITATION.cff).
