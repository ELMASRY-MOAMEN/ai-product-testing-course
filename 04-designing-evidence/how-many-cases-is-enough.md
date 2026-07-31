---
type: concept
status: reviewed
audience: [qa, product-owner, data-ai]
---

# How many cases is enough

You now know that a critical slice must pass on its own. The question that follows is the one you will be asked in the first meeting, and it is the question that most clearly separates evaluating an AI product from testing a deterministic one:

> **How many cases does a slice need before its result means anything?**

A deterministic suite never asks this. One case proves one thing, and a rule either holds or it does not. The moment acceptance becomes a proportion, the size of what you measured decides how much you are allowed to conclude from it.

## The trap: all of them passed

A slice of four cases reports `1.00`. Every case passed. It is tempting — and wrong — to read that as *this subgroup is safe*.

What zero observed failures actually licenses you to say has a standard form. If you saw no failures in `n` independent cases, the highest failure rate still consistent with that observation, at 95% confidence, is:

```text
p_max = 1 − 0.05 ^ (1 / n)
```

| Cases, all passing | The failure rate could still be as high as |
|:--:|:--:|
| 3 | **63%** |
| 5 | 45% |
| 10 | 26% |
| 20 | 14% |
| 30 | 9.5% |
| 50 | 5.8% |
| 100 | 3.0% |
| 300 | 1.0% |

For larger `n` this is close to the familiar shortcut **3/n** — thirty clean cases put the ceiling near 10%, three hundred near 1%. Below about ten cases the shortcut breaks down and the exact form is the one to use.

Read the first row again. **Three cases, all passing, is consistent with a capability that fails nearly two times in three.** A report showing `1.00` next to a population of three has not measured that subgroup; it has failed to look at it.

## What this gives you, and what it does not

**It gives you a floor.** Ask the decision owner the only question that matters here: *what failure rate would be unacceptable for this subgroup?* Then read the table backwards. If a 10% failure rate for vulnerable clients would be unacceptable, a clean slice of fewer than thirty cases cannot tell you that you are under 10%, so thirty is your floor — before any other consideration.

**It does not give you a sample size.** Three things it says nothing about, all of which you will meet:

| Question | Why this does not answer it |
|---|---|
| Is candidate B *better* than candidate A? | Comparing two proportions is a different calculation, and the difference you can detect depends on how big it is |
| How many repetitions for a candidate that is not deterministic? | The same input can produce different outputs; that variance has to be measured before it can be planned for |
| My slices are over-represented relative to production — what does the aggregate mean? | Deliberate stratification is correct for finding risk, and it makes the aggregate a weighted quantity rather than an estimate of live performance |

Those need someone who does statistics for a living. **Knowing which three questions to bring them is the deliverable**; inventing an answer to them is the same failure as inventing a threshold, with more arithmetic on top.

## The rule this produces

Every slice declares a **minimum population**. Below it, the slice result is reported as **`not concluded`** — never as passed, and never as a score.

`not concluded` is to a slice what `Not Ready` is to a run: a statement that nothing was measured, so nothing may be concluded. Both exist to stop an absence of evidence from being read as evidence.

Who decides what:

| Decision | Owner |
|---|---|
| What failure rate is unacceptable for this subgroup | Product owner, with Compliance where a regulator is involved |
| The method that turns that into a population | Data/AI specialist |
| The minimum population, once both are known | Product owner approves it, like any acceptance criterion |
| Reporting `not concluded` below it | You — this one is reporting accuracy, and it is yours |

You may compute the arithmetic and propose the floor. You may not decide what rate is acceptable, because that is a risk decision.

## A worked example, from this course

[The module 05 exercise](../05-running-it/exercises/fill-a-manifest-from-a-brief.md) gates a `high-value` slice at a minimum of 0.90. The slice contains **three cases**. It scored 0.917 and passed.

Apply what you just read. Three cases, and had all three passed cleanly, the failure rate could still have been 63%. The gate was satisfied and it demonstrated close to nothing about high-value claims — which are, by the brief's own words, the ones that matter more than the rest.

The exercise is not wrong to contain that slice; a real dataset often starts that way. What would be wrong is a report presenting `0.917 ≥ 0.90 — pass` with no note that the population cannot support the conclusion.

**And the manifest schema in this course has no field for a minimum population.** You cannot express this rule in the artefact. That is a limitation of the tooling, not permission to drop the rule: record the minimum in the dataset specification, state the gap in your decisions register, and report `not concluded` yourself. Lowering an acceptance rule to whatever the instrument happens to measure is how a control quietly stops existing.

> **Takeaway:** A passing slice too small to conclude from is not evidence of safety. State a minimum population, report `not concluded` below it, and bring the three questions you cannot answer to someone who can.

---

Previous: [Exercise — Write a veto an average hides](exercises/write-a-veto-an-average-hides.md) · [Course map](../00-orientation/progression.md) · Next: [AI-as-a-judge: useful, but not an oracle](ai-judge-calibration.md)
