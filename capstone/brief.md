---
type: procedure
status: reviewed
audience: [qa, product-owner, engineering, data-ai, compliance]
---

# Capstone: evaluate a capability of your own

Everything before this was practice on material chosen to teach. The capstone is the only part of this course that shows whether you can do the work when nobody has arranged the problem for you.

**Time:** a focused day, or a week of evenings.

## Choose your capability

**Option A — one from your own work.** Strongly preferred. A capability you can ask real questions about, with real people who own the decisions. The point of this course is a deliverable you could actually send.

**Option B — the supplied scenario**, below. Deliberately unlike all four worked examples, so nothing can be adapted from them.

> ### Alt-text assistant
>
> A publishing platform is adding a feature that generates **alt text** for images its editors upload. The generated text appears in a field the editor can accept or edit before publishing.
>
> What the team has told you:
>
> - Editors upload photographs, charts, diagrams, screenshots and decorative images.
> - There is a hard limit of 125 characters, and the platform rejects anything longer.
> - Alt text must not begin with "image of" or "picture of" — an accessibility guideline the team documented last year.
> - Purely decorative images should produce an empty alt attribute, not a description.
> - Accessibility compliance is being audited externally next quarter.
> - The accessibility lead has said, informally, that "describing someone's apparent ethnicity, age, or disability is a serious problem for us." Nothing is written down.
> - Roughly 8% of uploads are charts and diagrams, where a wrong description misleads rather than merely disappoints.
> - The team wants to know "whether it's good enough to turn on for everyone."

## What to produce

Six artefacts, in [`capstone/submission-template/`](submission-template/README.md). Copy that folder into `my-work/` and fill it in.

| # | Artefact | What it must contain |
|:--:|---|---|
| 1 | **Classification** | Every observable behaviour, its nature, its gate, and the question-2 justification |
| 2 | **DoT design** | The ten mandatory components — each one either resolved, or named as a pending decision with its owner |
| 3 | **Dataset specification** | Composition and reasoning, eligibility, slices with minimum populations, handling status, annotation protocol, and five case skeletons |
| 4 | **Manifest** | Runnable. It will almost certainly report `Not Ready`, and that is a correct submission |
| 5 | **Readiness assessment** | The [checklist](../toolkit/readiness-checklist.md), honestly scored, with the blockers |
| 6 | **Decisions register** | Every decision you did not make: what it is, who owns it, what it blocks, what you need in order to close it |

Plus **a one-page handover** at the top of the submission README: what you are asking the owner to decide, and what happens once they do.

## How it is assessed

Against [the rubric](rubric.md). Read it **before** you start — it is not a surprise, and knowing the criteria is part of doing the work.

One thing worth stating up front, because it decides more submissions than anything else:

> **A submission where every field is filled scores lower than one where the undecidable fields are named, attributed and left open.** The first looks finished. The second is finished.

## Working notes

**Do not copy a worked example as a starting artefact.** Start from [the templates](../toolkit/templates). Copying a runnable example inherits decisions approved for a different capability, and those decisions then hide inside your submission looking like your own work. Every reader of this material feels this pull; [the note in `worked-examples/`](../worked-examples/READ-ME-BEFORE-COPYING.md) explains why the templates exist to defeat it.

**Ask real questions if you took option A.** Half the value is discovering which of your capability's decisions have no owner. That discovery is a genuine result — record it in artefact 6.

**Run your manifest.** If the runner will not read it, the design is not finished. If it reports `Not Ready` with blockers you predicted, you are done.

**You have no dataset, and you are not going to build one.** Option B supplies no cases, and artefact 3 forbids you from writing a single reference — annotating five cases yourself to make the run proceed would fail the capstone under Override 1. So: point `evaluation_data.path` at a small `dataset.jsonl` of your case skeletons with their `reference` fields left as placeholders naming their owner, exactly as artefact 3 specifies. The run reaches `Not Ready` on the unresolved placeholders before it ever reads a case, which is the correct outcome and the one you should predict.

If you took option A and your capability *does* have annotated cases, use them.

## If you want it reviewed

Open a discussion on this repository with your submission attached, or hand it to a colleague with [the rubric](rubric.md). Assessing someone else's submission against the rubric is the fastest way to see the failure modes in your own.

---

Previous: [Exercise — Name the decision owner](../07-governance/exercises/name-the-decision-owner.md) · [Course map](../00-orientation/progression.md)
