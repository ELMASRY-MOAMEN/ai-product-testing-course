---
type: concept
status: reviewed
audience: [qa, product-owner, engineering, data-ai, compliance]
---

# What just happened

Three things, and each one is a module of this course in miniature.

## 1. The average was not the answer

The run measured 0.960 against a required 0.85, and failed. Not because the threshold was wrong — because **a threshold answers one question only**: is the typical output good enough?

It cannot answer the other one: did anything unacceptable happen at all?

A fabricated approval is not a small amount of wrong. It is a different kind of wrong, and averaging it with 24 correct summaries destroys the very information you needed. That is why acceptance is decided by three instruments, not one:

| Instrument | Question it answers | What it cannot see |
|---|---|---|
| **Threshold** | Is the typical output good enough? | A rare, catastrophic case |
| **Critical slice** | Is a risk-sensitive subgroup good enough on its own? | A failure spread evenly across slices |
| **Veto** | Did anything unacceptable happen at all? | Gradual quality decline |

Module 04 builds all three. If you remember one sentence from this course, make it the one you just saw demonstrated: **a good average never cancels a critical failure.**

## 2. `Not Ready` is not `Fail`

When you replaced the threshold with a placeholder, the runner refused to produce a verdict. It did not fail the candidate, and it did not guess.

| Verdict | Means | About the candidate |
|---|---|---|
| **Pass** | Measured, and cleared every gate | Evidence supports acceptance |
| **Fail** | Measured, and fell short of a gate | Evidence supports rejection |
| **Not Ready** | **Nothing was measured** | **Nothing may be concluded** |

The distinction protects you. `Fail` is a statement about the product. `Not Ready` is a statement about the evaluation: a decision that belongs to a human has not been made, so no measurement is meaningful yet.

Inventing a threshold to make the run proceed would turn a missing decision into evidence nobody approved — and it would look identical, in the report, to evidence somebody did approve. That is the failure this course cares most about preventing.

## 3. The evaluation was an experiment, not an assertion

You did not compare one output to one expected sentence. You ran a **frozen candidate** over a **versioned population of cases**, scored by **declared evaluators**, against acceptance rules approved **before** anyone saw the results.

That shape has a name — the Definition of Trustworthy — and ten mandatory components. Module 03 lists them. Miss one, and the correct verdict is `Not Ready`.

## What you have not seen yet

- Why the deterministic parts of the same product still need a completely different gate (module 03)
- How those 25 cases came to exist, and who is allowed to annotate them (module 04)
- Where the human decision sits, and why the runner never makes it (module 06)

## Check yourself

You should be able to answer these before moving on. If you cannot, rerun the steps in the previous note rather than reading ahead.

1. The run scored 0.96 and failed. In one sentence, why?
2. What would have been lost if the veto had been expressed as a stricter threshold — say, 0.99 — instead?
3. A colleague says: "the threshold field is empty, put 0.8 in it so the pipeline is green, we will confirm with the owner later." What do you answer?

---

Previous: [Run your first evaluation](run-your-first-evaluation.md) · [Course map](../00-orientation/progression.md) · Next: [Why AI products need a different testing approach](../02-foundations/testing-foundations.md)
