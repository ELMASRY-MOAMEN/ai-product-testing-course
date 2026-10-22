---
type: example
status: reviewed
audience: [qa, product-owner, engineering, data-ai]
---

# Solution — Score a DoT against its ten components

Read this only after attempting [the exercise](../score-a-dot-against-its-ten-components.md).

## 1. The scorecard

| Component | Status | Evidence or gap |
|---|---|---|
| **Evaluation question** | Partial | Three questions in one: draft quality, brand tone, and latency. A DoT assesses **one** quality capability; latency is not a quality question at all and belongs to a performance gate. |
| **Evaluation set** | Partial | 300 cases exist, but no version, no eligibility rules, and no declared handling status — they are raw production tickets. |
| **Reference or rubric** | Partial | "What a senior agent sent" is not a reviewed reference. Nobody annotated those replies as *correct for this purpose*; they are one acceptable output among several, captured by accident. |
| **Metric** | Partial | An LLM judge on a 1–5 scale, aggregated by mean. The calculation method is not documented and the judge is uncalibrated against human-labelled examples. |
| **Threshold** | **Present but invalid** | 4.0 exists — and was chosen *because a vendor demo scored 4.2*. See problem 1. |
| **Critical slices** | **Missing** | No subgroup is analysed independently. Not by ticket type, channel, language, or customer tier. |
| **Veto** | **Missing** | Legal's refund concern appears in prose and in no rule. Declared, and implemented nowhere. |
| **Variability control** | **Missing** | No candidate version, nothing frozen, `gpt-latest` is a moving target, no parameters, no repetitions. |
| **Evidence** | **Missing** | A mean and a pass/fail in a release ticket. No case outputs, scores, traces or versions retained. |
| **Owner** | Partial, and wrong | "QA lead to approve the results" — approving *results* is not approving the *protocol* beforehand, and business acceptance is not QA's to own. |

## 2. The verdict

**`Not Ready`.** Not `Fail` — nothing has been measured, so nothing may be concluded about the assistant.

Any one missing component would be enough. Four are missing outright.

The blocker list:

```text
Not Ready — 4 mandatory DoT components missing, 1 invalid, 5 partial

BLOCKERS
  missing: critical slices              owner: product owner + Legal
  missing: veto conditions              owner: Legal (condition), product owner (acceptance)
  missing: variability control          owner: engineering
  missing: evidence retention policy    owner: engineering + product owner
  invalid: threshold derived from an observed result
                                        owner: product owner (approval before execution)
  unresolved: dataset version, eligibility rules, data-handling approval
                                        owner: data protection + product owner
  unresolved: reference status — sent replies are not reviewed references
                                        owner: product owner (or a delegated annotator)
  unresolved: decision owner — QA lead is not the acceptance owner
```

## 3. The three most dangerous problems

### 1. The threshold was derived from the results — the stated choice that is wrong

> "We picked 4.0 because the last vendor demo scored 4.2, so it is achievable."

Thresholds must be approved **before** anyone sees candidate results. A bar set to be clearable by an observed score is not a bar; it is a description of what already happened, dressed as a gate. It will report `Pass`, and that `Pass` carries no information about whether the drafts are fit for customers.

This is the most dangerous item precisely because it is the least likely to be caught later: everything downstream looks correct, and the report looks like evidence.

**If the run proceeds:** the release ticket records an approval nobody made a decision about.

### 2. Legal's veto exists in prose and nowhere else

A reply promising a refund the company cannot honour is not a matter of degree. One occurrence is unacceptable, and no mean of 4.2 changes that.

As designed, such a reply scores somewhere between 1 and 5 on the judge's scale, gets averaged with 299 others, and disappears. You watched this exact failure in [module 03](../../../03-first-evaluation/what-just-happened.md): a case with a *perfect* score that must still block acceptance.

**If the run proceeds:** the assistant ships with a `Pass` and the failure mode Legal named is live in production.

A veto stated in a meeting and wired into no rule is the most common defect in evaluation designs — the entry *veto declared but not implemented* exists because of how often it recurs.

### 3. Raw production tickets, sent to an external judge, against an unfrozen model

Three failures stacked in one sentence:

- **300 real tickets** with customer data, with no declared anonymisation status and no approved handling. Sending protected data to an unapproved evaluator is prohibited outright — and an external LLM judge is an evaluator.
- **`gpt-latest`** is not a version. The judge can change between the run and any rerun, so the results are not reproducible and no baseline comparison is possible.
- **Nothing is frozen** — not the candidate, not the judge, not the prompt.

**If the run proceeds:** a possible data incident, and results nobody can reproduce, including you, next week.

### Runner-up, worth naming

The mean of a 1–5 ordinal judge score is the same instrument that failed in module 03. Even with everything else fixed, the aggregate cannot see the rare catastrophic case. That is what slices and vetoes are for — and both are missing.

## 4. What you send them

> The design is `Not Ready` — four of the ten mandatory components are missing, so the run cannot produce a verdict about the assistant tomorrow. Two decisions unblock most of it and neither is mine: the product owner approving a threshold **before** we look at any result, and Legal stating the refund condition as a veto rule we can execute. Send me those and I will have the manifest ready the same day; engineering needs to pin the judge model and freeze the candidate in parallel.

Note what the sentence does **not** do: it does not offer a threshold to keep things moving, it does not soften `Not Ready` into "nearly ready", and it does not accept ownership of decisions that belong to the product owner and to Legal. It also stays useful — it names the shortest path to a run.

## Locate yourself

For each item, find the line closest to **what you actually wrote**, then read the verdict.

### 1. Your verdict

| | You wrote | |
|:--:|---|---|
| **A** | `Not Ready`, with the blockers listed | ✅ |
| **B** | `Fail` — the design is not good enough | ❌ `Fail` is a statement about the assistant, and the assistant has not been measured. Handing back `Fail` here asserts something about a product nobody tested |
| **C** | "Not ready yet, but close" | ⚠️ *Close* is how `Not Ready` gets read as *ready*. Four mandatory components are missing; that is not close, and softening it is what the team will quote |

### 2. The threshold of 4.0

| | | |
|:--:|---|---|
| **A** | Invalid — it was derived from an observed result, so the gate cannot fail | ✅ The subtlest item in the exercise |
| **B** | "4.0 on a 1–5 scale is arbitrary / too low" | ⚠️ Arguing the number accepts the method. The defect is not the value, it is that a vendor demo chose it |
| **C** | Marked present | ❌ A threshold that exists is not a threshold that was approved before results were seen. Those are different components |

### 3. Legal's refund concern

| | | |
|:--:|---|---|
| **A** | A veto stated in prose and wired to nothing — the run can report `Pass` with the failure live | ✅ |
| **B** | "They should add a check for it" | ⚠️ Right direction, and it misses that the *veto* is missing, not just the check. An evaluator without a veto gets averaged away |
| **C** | Counted as covered, because the design mentions it | ❌ This is the defect's whole trick: mentioning a control reads, on a page, exactly like having one |

### 4. What you did with the missing components

| | | |
|:--:|---|---|
| **A** | Named each one and its owner; proposed no values | ✅ |
| **B** | Suggested reasonable values "as a starting point for discussion" | ❌ There is no such thing as a starting-point threshold. The first number in the room is the one that gets approved |
| **C** | Named them, but assigned the ownership loosely — "the team", "whoever owns it" | ⚠️ A blocker without a named role is a blocker nobody closes. Note the trap in the brief: the QA lead was offered as approver, and acceptance is not QA's |

### 5. `gpt-latest`

| | | |
|:--:|---|---|
| **A** | A variability-control failure — the judge can change between the run and any rerun | ✅ |
| **B** | Flagged as a style or hygiene issue | ⚠️ It makes the results irreproducible and the baseline comparison impossible. That is a mandatory component, not tidiness |
| **C** | Not noticed | ❌ Along with "nothing is frozen", this is the row that means no result from this run can ever be re-obtained |

**Two or more ❌:** reread [DoT: evaluating probabilistic quality](../../definition-of-trustworthy.md), then the [readiness checklist](../../../toolkit/readiness-checklist.md), before module 06.
