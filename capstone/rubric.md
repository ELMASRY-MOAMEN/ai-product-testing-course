---
type: reference
status: reviewed
audience: [qa, product-owner, engineering, data-ai, compliance]
---

# Capstone rubric

Read this before starting [the capstone](brief.md).

Eight criteria, scored 0 to 3. **24 points total; 18 is competent; below 12 means repeat the module named in the criterion.** Two conditions override the total entirely — they are at the bottom.

---

## C1 — Classification (weight: high)

| | |
|:--:|---|
| **3** | Every observable behaviour classified separately. Deterministic and probabilistic behaviours both identified. Each justified by question 2 — specified, or annotated. At least one non-obvious case reasoned correctly. |
| **2** | Correct classification, justified mostly by question 1. The hard cases are decided but not argued. |
| **1** | The capability classified as a whole rather than per behaviour, or "it uses an LLM so it is DoT". |
| **0** | No classification, or deterministic behaviour placed behind a threshold. |

*Below 2: [module 02](../02-foundations/README.md).*

## C2 — The ten DoT components

| | |
|:--:|---|
| **3** | All ten addressed. Each is resolved with its source, or open with a named owner. The evaluation question is **singular**. |
| **2** | All ten addressed; one or two treated superficially. |
| **1** | Components missing without acknowledgement. |
| **0** | A design that cannot say what it is measuring. |

*Below 2: [module 03](../03-the-two-gates/README.md).*

## C3 — Instrument fit: threshold, slice, veto

| | |
|:--:|---|
| **3** | Each risk assigned the instrument that can see it. Vetoes phrased as conditions **code can test**, and each fires on an evaluator that is actually declared. Slices carry minimum populations. |
| **2** | Instruments broadly right; a veto is unexecutable as written, or a slice has no minimum population. |
| **1** | Everything expressed as thresholds, or a veto declared against an evaluator nobody declared. |
| **0** | Acceptance is one average. |

*Below 2: [module 04](../04-designing-evidence/README.md).*

Note the specific failure at level 1 — **a veto wired to nothing** is the most frequently recurring defect in this material, and it survives review because the manifest reads correctly.

## C4 — Evaluation data

| | |
|:--:|---|
| **3** | Composition justified against risk rather than production frequency. Eligibility declared as a rule. Handling status proposed with reasoning and attributed to its approver. Annotation protocol names who annotates and what disagreement means. Versioning policy stated. |
| **2** | A sound specification with one governance element missing. |
| **1** | A list of cases with no eligibility, versioning or handling. |
| **0** | **You wrote the reference answers yourself.** |

*Below 2: [module 04](../04-designing-evidence/README.md), notes 8 and 9.*

## C5 — The manifest runs

| | |
|:--:|---|
| **3** | The runner reads it and reports a coherent status. You predicted the blockers before running, and the prediction matched. |
| **2** | It runs; the blockers were not predicted, or one is spurious. |
| **1** | It does not run, or a section was deleted to make it run. |
| **0** | No manifest. |

*Below 2: [module 05](../05-running-it/README.md).*

Deleting the slice block to obtain a clean run scores **1**, however tidy the result looks.

## C6 — Readiness, honestly assessed

| | |
|:--:|---|
| **3** | The checklist scored against what exists, not what is planned. Blockers stated plainly. The verdict is `Not Ready` where it should be, with no softening language. |
| **2** | Honest, but hedged — "mostly ready", "pending minor confirmation". |
| **1** | Items ticked that the artefacts do not support. |
| **0** | A readiness claim contradicted by your own submission. |

*Below 2: [the readiness checklist](../toolkit/readiness-checklist.md).*

## C7 — The decisions register

| | |
|:--:|---|
| **3** | Every open decision listed with its **owner by role**, what it blocks, and what specifically is needed to close it. Ownership assigned correctly — acceptance policy is not QA's, and a regulatory reading is not the product owner's alone. |
| **2** | Decisions listed with owners; "what would close it" is vague. |
| **1** | A list of open questions with no owners. |
| **0** | No register, because nothing was left open. |

*Below 2: [module 06](../06-governance/README.md).*

Scoring **0** here almost always coincides with the override below.

## C8 — Communication

| | |
|:--:|---|
| **3** | The handover page is readable by the person who owns the decisions. It says what you are asking for, what happens next, and how long it takes. No jargon that a product owner would have to decode. |
| **2** | Accurate but written for a tester. |
| **1** | The reader cannot tell what is being asked of them. |
| **0** | No handover. |

---

## The two overrides

These are not points. They decide the submission.

### Override 1 — An invented decision

**Any threshold, slice minimum, veto condition, reference answer, approval or owner that you supplied, and that no owner decided, fails the capstone regardless of the total.**

Including — especially — when the invented value is entirely sensible. A well-chosen threshold that nobody approved is worse than an obviously wrong one, because nothing downstream will ever question it.

If you are unsure whether you invented something, check every non-placeholder value in your manifest and ask: *who decided this, and where is that recorded?* "It is the obvious value" is not an answer. Neither is "the worked example used it".

### Override 2 — A `Pass` that should not be

**A submission concluding that a capability is acceptable, on evidence that cannot support the conclusion, fails regardless of the total.**

The usual forms: a slice below its minimum population read as a pass; an aggregate quoted where a veto was never wired; an uncalibrated judge's score treated as measurement; `Not Ready` reported as "ready with minor caveats".

---

## Self-assessment

Score yourself before asking anyone else. Then hand the submission and this rubric to a colleague without your scores and compare.

Where you scored yourself higher than they did, you have found the thing you cannot yet see in your own work — which is the most useful output this course can give you.
