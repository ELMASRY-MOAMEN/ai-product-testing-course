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

Answer these in your own words **before** reading the answers below them. Writing the sentence and then comparing is the whole exercise; reading the answer first produces recognition, which feels identical and is not the same thing.

### 1. The run scored 0.96 and failed. In one sentence, why?

<details>
<summary>Answer</summary>

Because one case did something that has no acceptable rate — it asserted an approval the source never gave — and a veto blocks acceptance on kind, not on degree, however good the average is.

If your sentence was *"because one case failed"*, it is not yet right: four cases failed, and three of them did not block anything. The blocking one is blocking because of **what** it did, not because it failed.
</details>

### 2. What would have been lost if the veto had been expressed as a stricter threshold — say 0.99 — instead?

<details>
<summary>Answer</summary>

Nothing would have been caught. The fabricating case scores **1.000** on recall — it contains every required fact — so it passes any threshold you can write, including 1.0. Raising the bar filters out cases that are *incomplete*; this one was complete and false.

That is the general point: a threshold ranks outputs on a scale the metric can measure. A veto catches something the metric was never measuring.
</details>

### 3. A colleague says: "the threshold field is empty, put 0.8 in it so the pipeline is green, we will confirm with the owner later." What do you answer?

<details>
<summary>Answer</summary>

That the moment 0.8 goes in, the report states that someone approved a gate, and nobody did — and the report, the release ticket and any audit inherit that statement as fact. There is no marker anywhere distinguishing an approved 0.8 from a typed one.

The useful reply also offers the way through: get one line from the owner, or run it and report `Not Ready` on that one item with everything else measured. Both take minutes. **Refusing without offering either is the half of the answer that gets you left out of the next decision** — module 07 is entirely about this.
</details>

---

Previous: [Run your first evaluation](run-your-first-evaluation.md) · [Course map](../00-orientation/progression.md) · Next: [Module 02 — Foundations](../02-foundations/README.md)
