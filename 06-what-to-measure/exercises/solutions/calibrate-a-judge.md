---
type: example
status: reviewed
audience: [qa, data-ai, compliance]
---

# Solution — Calibrate a judge

Read this only after attempting [the exercise](../calibrate-a-judge.md).

## 1. The numbers

### a. Overall agreement

`(20 + 7) / 30 = 27/30 = **90%**`. The team's figure is correct, and it is the least informative number available.

### b. The two directions, overall

| | Calculation | Result |
|---|---|:--:|
| Of what the **human rejected**, the judge also rejected | 7 / (3 + 7) | **70%** |
| Of what the **judge rejected**, the human also rejected | 7 / (0 + 7) | **100%** |

Read together: **when the judge fires, it is right. When it stays silent, that means nothing** — it missed 3 of the 10 outputs the adviser considered unacceptable.

### c. Within the fabrication subgroup

The adviser rejected all six. The judge rejected three.

| | Calculation | Result |
|---|---|:--:|
| Of what the **human rejected**, the judge also rejected | 3 / 6 | **50%** |
| Of what the **judge rejected**, the human also rejected | 3 / 3 | **100%** |

**A coin.** On the exact failure mode the veto exists to catch, the judge is right half the time — and all three of its overall errors sit here. A 90% headline and a coin flip on what matters are the same 30 cases.

### d. The empty cell

`Judge: reject / Human: accept = 0`. The judge never rejects something the adviser would have accepted.

Had that cell been populated, it would mean **false alarms**: the judge flagging good briefings. Annoying, expensive in review time, corrosive to trust — and *visible*, because somebody investigates every flagged case and discovers it was fine.

Its emptiness is not the good news it looks like. It says the judge's error is **entirely one-directional**: it errs by accepting. That is the worst possible asymmetry for a control whose purpose is to catch the unacceptable, and it is invisible by construction, because nobody investigates a passing case.

## 2. The reading, for a product owner

> The judge agrees with our senior adviser on 90% of cases, but agreement is not the useful number here — almost all these briefings are fine, so a judge that accepted everything would score around 67% without doing anything at all.
>
> What matters is what it catches. Of the briefings the adviser rejected, it caught 70%; of the fabricated client statements specifically — the thing we said can never ship — it caught **half**.
>
> Every mistake it makes is in the same direction: it lets things through. It has never once flagged a briefing that turned out to be fine.

The first paragraph is the one to keep. **A high agreement rate on an imbalanced population is close to free**, and quoting it without the base rate is how a broken control gets approved.

## 3. The decision, taken separately

### For the groundedness metric — possible, with the bias stated

Defensible, if two things travel with it. First, the score is **biased upward** by a known amount: the judge accepts things the adviser would reject, so the groundedness figure is an optimistic estimate, not a neutral one. Second, that bias is written into the design as the metric's blind spot, per [does the metric measure it](../../does-the-metric-measure-it.md).

Whether a metric with that bias is good enough for the decision it feeds is **the product owner's call**, not yours and not the judge author's. Your job is to make sure they are choosing with the 70% and the 50% in front of them, not the 90%.

### For the fabrication veto — no

Not "with caveats", not "provisionally". No.

The reason is one sentence: **a veto is a claim about absence, and this judge's silence carries no information.** A veto reports *nothing unacceptable happened*. To carry that claim, an evaluator must be reliable when it does not fire. This one, on the veto class, is right half the time when it stays quiet.

Wire it to the veto and the report will state *no fabrication veto triggered* over a run in which roughly half the fabrications went unseen. That sentence would be false, and it would be false in a document a decision owner uses to release.

**What makes the two different:** a metric is an estimate, and a known bias can be carried into a decision as long as it is declared. A veto is an assertion of absence, and an assertion you are 50% confident in is not an assertion. Same judge, same numbers, opposite answers — because the two instruments make different kinds of claim.

For the veto, prefer the deterministic route: a forbidden-content check on statements attributed to the client that appear in no source record for the case. That is the option [module 06](../../evaluators-and-metrics.md) puts first — do not use a judge where code can give a more exact, explainable and reproducible answer.

## 4. What is missing from the calibration

| # | Gap | Owner |
|:--:|---|---|
| 1 | **No sufficiency criterion agreed in advance.** Nobody said what agreement rate would be enough, so 90% is being judged after the fact against nothing | Product owner; **Compliance** for anything feeding the veto |
| 2 | **One annotator.** No second expert, so no inter-annotator agreement. If two advisers disagree about what "grounded" means, the judge cannot be better than the disagreement — and that disagreement is a defect in the requirement | Product owner, with a second business expert |
| 3 | **Six cases in the subgroup.** Half of six is not a measurement. Three clean cases would have been consistent with a 63% failure rate — see [how many cases is enough](../../../07-designing-evidence/how-many-cases-is-enough.md) | Product owner + data/AI |
| 4 | **Nothing pinned.** No judge model version, no prompt version, no parameters, and no rule that a change to any of them invalidates the calibration | Data/AI + engineering |
| 5 | **Provenance of the 30 cases.** Representative or convenient? Drawn from the evaluation set itself, which would make the judge calibrated on cases it will later score? | Data/AI + QA |
| 6 | **Data handling.** The judge is an external recipient of client briefings and client records | Data protection, with the product owner |

Three would have been enough. Items 1 and 4 are the ones that recur everywhere: a control with no agreed sufficiency criterion, and a control that silently changes underneath its own approval.

## 5. What you send

> Your calibration is the reason we can have this conversation at all — most judges reach production without one, and yours is what makes the problem visible.
>
> The 90% is carrying a base rate: most of these briefings are fine, so accepting everything would score about 67% by itself. The numbers that decide it are the ones on what we reject — 70% overall, and 3 of 6 on the fabricated statements.
>
> That is enough to discuss it as a groundedness metric, with the upward bias stated in the design. It is not enough for the fabrication veto, and the reason is structural rather than a matter of tuning: a veto asserts that nothing unacceptable happened, so it needs a judge that is trustworthy **when it stays silent**. Yours is trustworthy when it fires.
>
> Two things would move this: a second adviser labelling the same set, so we know whether "grounded" is even consistently defined, and more fabrication cases — six is too few to conclude from in either direction. And we should ask the product owner and Compliance what agreement rate they need before we measure again, rather than after.

What it does: credits real work, replaces the wrong number with the right ones, separates the two uses, and gives a concrete next step. What it avoids: arguing about whether the judge is "good", which is not a question anyone can settle.

## Locate yourself

The four figures were checked by `check_answer.py`. These are the four judgements it cannot check. Find the line closest to **what you actually wrote**.

### 1. What you said about the 90%

| | You wrote | |
|:--:|---|---|
| **A** | It is inflated by the base rate — accepting everything scores about 67% here | ✅ |
| **B** | "90% is not high enough for a control like this" | ⚠️ Arguing the level accepts the measure. The problem is that agreement on an imbalanced population barely moves however good or bad the judge is |
| **C** | "90% is decent, the subgroup is the worry" | ⚠️ Right conclusion, and it leaves the headline standing. Someone will quote it in the release note |

### 2. Metric versus veto

| | | |
|:--:|---|---|
| **A** | Metric possible with the upward bias declared; veto **no**, because a veto asserts absence | ✅ |
| **B** | No to both | ⚠️ Defensible and over-strict. A biased estimate whose bias is stated is usable evidence; refusing both means the team ships with no measurement at all |
| **C** | Yes to both, with monitoring or a post-launch review | ❌ "We will watch it" is not a control. The veto would report *no fabrication triggered* over runs where half went unseen |
| **D** | Yes to both once the agreement rate improves to some level | ❌ You set a sufficiency threshold. That belongs to the product owner, with Compliance for the veto class |

### 3. The empty cell

| | | |
|:--:|---|---|
| **A** | The judge's error is entirely one-directional — it only ever over-accepts | ✅ |
| **B** | Read as good news: no false alarms, so no wasted review time | ❌ It is the worst possible asymmetry for a control meant to catch the unacceptable, and invisible by construction: nobody investigates a passing case |
| **C** | Not mentioned | ⚠️ An empty cell is data. It is the one figure in the table that tells you *which way* the judge is wrong |

### 4. What you sent the engineer

| | | |
|:--:|---|---|
| **A** | Credited the calibration, replaced the headline with the two figures that decide it, separated the two uses, gave a concrete next step | ✅ |
| **B** | Explained why the judge is not good enough | ⚠️ Accurate and unusable. "Not good enough" invites tuning, and the veto problem is structural — tuning will not reach it |
| **C** | Asked them to redo the calibration properly | ❌ They did calibrate, which is the only reason any of this is visible. Most judges reach production with neither a calibration nor this conversation |

**Two or more ❌:** reread [AI-as-a-judge: useful, but not an oracle](../../ai-judge-calibration.md) and [does the metric measure it](../../does-the-metric-measure-it.md).
