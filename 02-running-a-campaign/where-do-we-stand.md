---
type: concept
status: reviewed
audience: [qa, product-owner, engineering]
---

# Where do we stand?

## Four figures

"Where are we?" is the question every campaign gets, several times a day near the end. The Testing Agent's method answers it with four figures. Other methods use other names, and the definitions vary from team to team; these are the ones used here, and the point is that each one is defined, so nobody reads into it more than it says.

| Figure | Definition | It answers |
|---|---|---|
| **Preparation coverage** | Testable requirements with at least one designed case, over testable requirements | Have we planned to test everything we can? |
| **Execution coverage** | Testable requirements with at least one case run Passed, Failed or Settled, over testable requirements | How much of what we can test has actually been tested? |
| **Progress** | Planned cases executed (Passed, Failed, Not applicable, Settled), over planned cases | How far through the campaign are we? |
| **Quality** | Passed, over Passed, Failed and Settled | Of what ran, how much worked? |

Two details carry most of the weight:

- **A blocked case is not executed.** It counts in neither progress nor quality: it is still to do.
- **A settled case is not a success.** It ran, it failed, and someone accepted the deviation. It counts against quality, because the product did not do what was required.

## What each figure hides

Each figure, quoted alone, misleads in a predictable way. Preparation coverage at 100% says every requirement has a case, not that any of them ran. Progress at 90% says nothing about whether those cases passed. Quality at 100% on three executed cases out of forty is three cases.

That is why the answer to "where are we?" never starts with a percentage. It starts with **what is not done**:

1. what remains to run, by importance, and which of it needs a person;
2. the requirements with no case, and those not testable;
3. the open defects, worst first;
4. the actions waiting on someone, and how late they are;
5. then the figures, side by side, never one alone.

## Check yourself

### After two days, a campaign reports quality at 100%. What do you need to know before you repeat that figure to anyone?

<details>
<summary>Answer</summary>

**How many cases it is computed on**, and therefore what progress and execution coverage are. Quality is a ratio over executed cases only: 100% can mean three passed cases out of forty planned, with the requirements that matter most not run yet. And whether anything was **blocked**, since blocked cases are in neither side of the ratio.

| | | |
|:--:|---|---|
| A | How many cases it covers, progress and execution coverage next to it, and what is blocked | ✅ |
| B | "Whether the tests are good" | ⚠️ A fair worry, and it does not tell you what the figure leaves out |
| C | Nothing, 100% is 100% | ❌ It is 100% of whatever ran, which may be almost nothing |
</details>

---

Previous: [Exercise: write a defect](exercises/write-a-defect.md) · [Course map](../00-orientation/progression.md) · Next: [Exercise: the status, and the report](exercises/status-and-report.md)
