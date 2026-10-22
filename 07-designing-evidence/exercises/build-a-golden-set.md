---
type: example
status: reviewed
audience: [qa, data-ai, compliance]
---

# Exercise — Build a golden set

**Time:** 45 minutes. **Do it before opening [the solution](solutions/build-a-golden-set.md).**

## The brief

You are asked to build the evaluation set for *AdvisorBrief*, the pre-meeting briefing generator from the [previous exercise](write-a-veto-an-average-hides.md).

What you are given:

- The capability's requirements, including the list of fact types the business considers mandatory.
- Read access to production: 40,000 real client records and their interaction histories.
- Two business experts, available for a total of three days.
- The risks named in the previous exercise: unauthorised disclosure, fabricated client statements, missing suitability warnings for vulnerable clients, out-of-scope product recommendations.

You are asked for **200 cases**.

## What to produce

**1. A dataset specification** — not the data. Cover:

- name, version, and what a material change would be;
- eligibility rules for inclusion in a run;
- the composition: how many cases of which category, and the reasoning;
- slice labels, and the minimum population you would want per slice;
- the handling status you propose, and why;
- the annotation protocol: who annotates, what a disagreement means, when a case becomes `approved`.

**2. Three case skeletons**, in the case shape below, for three deliberately different categories. Fill every field you legitimately can.

```yaml
case_id: <stable identifier>
input: <user request or source input>
context: <controlled evidence available to the candidate>
reference: <required facts, acceptable result or reviewed rubric>
slices: <business and risk segments>
criticality: <normal or critical>
eligibility: <rule for inclusion in the run>
annotation_status: <draft, reviewed or approved>
```

**3. Answer these:**

- **a.** The 40,000 records are real client data. What must be decided before a single case exists, and who decides it?
- **b.** Three days of expert time for 200 cases is roughly seven minutes per case. What do you do — and what do you refuse to do?
- **c.** Six months in, the business changes what counts as a mandatory fact. What happens to the dataset, and what happens to the historical results?
- **d.** A colleague proposes sampling 200 records at random, on the grounds that random sampling is unbiased and therefore representative. Answer them.

## Constraint, and it is the whole point

**You may not write a single `reference` value.** Deciding what the correct answer is for a case is the business expert's decision, not yours. Your job is to specify the set, label it, and make the annotation possible.

The moment your skeletons contain plausible reference answers you wrote yourself, the exercise is failed — however good those answers are.

---

Previous: [How many cases is enough](../how-many-cases-is-enough.md) · [Course map](../../00-orientation/progression.md) · Next: [Module 08 — Running it](../../08-running-it/README.md)
