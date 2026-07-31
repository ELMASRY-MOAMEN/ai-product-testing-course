---
type: example
status: reviewed
audience: [qa, product-owner, compliance]
---

# Solution — Name the decision owner

Read this only after attempting [the exercise](../name-the-decision-owner.md).

## S1 — The product owner accepts the risk

**Owner: the authorized decision owner — which, for release, is the product owner here.** This one is theirs, and the answer is that they may.

Accepting residual risk is precisely what the human gate exists for. The methodology never says a veto makes release impossible; it says a veto blocks *automated* acceptance and forces the decision to a human who is accountable for it.

**What you do:** record it. The verdict stays `Fail` — you do not rerun to obtain a green report, and you do not amend the manifest. What changes is that a documented override sits beside the failing evidence: who accepted, what they accepted, on what date, and with which mitigation.

**What you say:**

> Recorded. To be clear about what is in the file: the run stands at `Fail`, and your acceptance of the CT-xxx veto is attached to it as an override with today's date. Can you confirm in writing, and tell me whether Legal needs to see it — the condition was theirs.

The distinction that matters: **an accepted failure and a passing run are not the same artefact**, and only one of them is true.

## S2 — Engineering narrows the veto until it stops firing

**Owner: not engineering.** A veto condition is approved by the product owner on Compliance's advice. Engineering implements it; they do not get to redefine what is unacceptable, and least of all after seeing which cases it caught.

This is the most dangerous of the six, because it is done in good faith and it leaves no trace. The rerun produces a clean `Pass`, and the report looks exactly like a report from a product that never had the problem.

**What you do:** stop the rerun from being the record. The original run stays; the narrowed veto is a proposed change to an approved acceptance rule, which goes back to the owner with the case it now misses attached.

**What you say:**

> Hold the rerun as evidence for now. Narrowing a veto after seeing what it caught changes an approved acceptance rule, so it needs the product owner and Legal, not just us — and they will want to see CT-xxx, which the new pattern no longer fires on. If it genuinely is a phrasing false positive, that is a strong argument to make to them, and it takes an hour.

Note the last sentence. Engineering may well be **right**. The objection is to who decides, not to the substance.

## S3 — "Put 0.90 in, we'll confirm Monday"

**Owner: the product owner.** Slice minimums are acceptance policy.

**What you do:** you do not fill it. See question B for the full handling — this is the situation the course is built around.

## S4 — The uncalibrated AI judge

**Owner: the data/AI specialist implements and calibrates; the product owner approves the evaluator as fit for the decision it feeds.** Your part is that nobody has asked — and you noticed.

An uncalibrated judge produces numbers with no established relationship to human judgement. Plausible-looking scores are the problem, not the reassurance: an obviously broken judge gets fixed, a plausible one gets quoted.

**What you do:** raise it now, before the results are used, not after. Propose the smallest thing that resolves it — a calibration set of human-labelled examples, and agreement in advance on what agreement rate is sufficient. Until then the affected metric is `Not Ready`, even though the run technically produced a number.

**What you say:**

> Before we quote the quality scores: the judge has never been checked against human labels, so we do not know what its 4.1 corresponds to. I would rather we agree a small calibration set this week than defend the number later. Everything else in the run is unaffected.

**Nobody asked** is the operative detail. A control nobody has questioned for months is the normal state of a control that was never wired up.

## S5 — `1.00` on a four-case slice

**Owner: shared — but the correction is yours, because you produced the report.** The reporting rule is the product owner's to set; the accuracy of what your report implies is yours.

Four passing cases out of four is not evidence that a subgroup is safe. It is evidence that nobody has looked hard. The number `1.00` is arithmetically correct and, at that population, tells you almost nothing.

**What you do:** correct the release note, and fix the report so it cannot happen again — a slice below its declared minimum population must render as **not concluded**, never as a score. If your report shows `1.00` next to a population of 4 with no marker, the report is the defect.

**What you say:**

> That 1.00 is four cases out of four, which is not enough to conclude anything about vulnerable clients — I would take it out of the release note. If we need that claim, we need more cases in the slice, and I can tell you how many by tomorrow.

## S6 — The approved case that contradicts its requirement

**Owner: the business expert who annotated it, and the product owner for the requirement.** Not you — you found it, you do not resolve it.

**What you do:**

1. **Quarantine the case** so it stops entering runs, and record why.
2. **Do not silently fix the reference.** The dataset is versioned precisely so that this creates a new version rather than a quiet edit.
3. **Take it to the owners** as a *requirement* question — reference and requirement disagree, and which one is wrong is a business decision.
4. **Handle the six past runs honestly.** They are not deleted and not recomputed. They stated a result against a dataset version now known to contain a defective case. Whether anything approved on that basis must be re-examined is the product owner's call; your job is to make sure they know, with the six runs identified.

**What you say:**

> Case AB-xxx's reference and the requirement it traces to contradict each other — one of them is wrong and it is not mine to decide which. I have quarantined the case. Six runs used this dataset version; here they are. Nothing needs undoing today, but you should know before the next release cites them.

The instinct to fix a broken reference yourself is strong and it is the same failure as inventing a threshold, one step upstream: you would be deciding what "correct" means for that case.

## A. The three that share a shape

**S2, S3 and S6.**

The shape: **someone substitutes their own judgement for a decision that belongs to a named owner, in a way that leaves the artefact looking complete.**

- S2 redefines what is unacceptable, and the report reads as a clean pass.
- S3 supplies a threshold, and the report reads as an approved gate.
- S6 corrects a reference, and the dataset reads as approved.

In all three the work looks *finished*, and nothing in the output shows that a decision was made by the wrong person. That is what makes them worse than a visible failure: a `Fail` is read as a `Fail`, but an invented approval is read as an approval.

S1 is its legitimate counterpart — the same decision, taken by the person who owns it, recorded as an override rather than disguised as a pass. S4 and S5 are a different family: controls that were never validated, and numbers that imply more than they contain.

## B. What you send your manager, and what you do next

> I can have everything else ready tonight. The one thing I cannot do is fill in the slice minimum — the moment I type 0.90 there, the report says the product owner approved a gate for high-value claims, and they did not. That is the one line in the file that would not be true.
>
> Two ways through: a one-line confirmation from [owner] on the 0.90, by email, and I run it the moment it lands — that is five minutes of their time. Or we ship with the run reporting `Not Ready` on that slice and everything else measured, which is an honest artefact and blocks nothing else.
>
> Which do you want me to chase?

What makes this hold: it does not argue about who is right, it names the concrete falsehood, and it puts two workable options on the table. The manager wants the release, not the number — give them the fastest legitimate route and the objection usually stops being one.

### "Do it anyway"

You still do not type the value, and you say why once more, in writing, without escalating your tone:

> I would rather not put my name on a value the owner hasn't approved. I will run it `Not Ready` on that slice tonight so everything else is measured, and I will flag the gap in the release ticket. If you want the gate in, I need one line from [owner] — or you can set it yourself and I will record it as your decision, with your name in `approved_by`.

The last clause is the important one, and it is not a threat. **A decision made by someone with the authority to make it, recorded under their name, is legitimate.** What is not legitimate is a decision made by you and recorded as theirs. Offering to attribute it correctly resolves the conflict without you inventing anything — and in practice, it is the sentence that most often ends the discussion, because an unattributed shortcut and an attributed one are very different propositions for the person asking.

If it still goes in without an owner, you have done your part: you refused to author it, you offered the legitimate paths, and you put the gap in writing where the decision owner will see it.

## Locate yourself

For each item, find the line closest to **what you actually wrote**, then read the verdict.

### 1. S1 — the product owner accepts the risk

| | You wrote | |
|:--:|---|---|
| **A** | They may. Record it as an override sitting beside a run that stays `Fail` | ✅ |
| **B** | They may, and you rerun so the record shows the accepted state | ❌ An accepted failure and a passing run are not the same artefact, and only one of them is true |
| **C** | They may not — a veto blocks release | ❌ The commonest misreading of this material. A veto blocks *automated* acceptance and pushes the decision to the human accountable for it. That is what the gate is for |

### 2. S2 — engineering narrows the veto until it stops firing

| | | |
|:--:|---|---|
| **A** | Not theirs to decide; the change goes to the owner with the case it now misses attached — and they may well be right on the merits | ✅ |
| **B** | You argued the pattern was not a false positive | ⚠️ You took the technical fight and left the ownership question standing. If they win the argument, the veto changes anyway, still without an owner |
| **C** | Accepted it — the rerun is cleaner and they know the system | ❌ The most dangerous item in the exercise, because it is done in good faith and leaves no trace. The clean `Pass` is indistinguishable from a product that never had the problem |

### 3. Question A — the three that share a shape

| | | |
|:--:|---|---|
| **A** | S2, S3, S6 | ✅ Someone substitutes their judgement for a named owner's, and the artefact still looks finished |
| **B** | You included S1 | ❌ S1 is the legitimate counterpart — the same decision, taken by the person who owns it, recorded honestly |
| **C** | You included S4 or S5 | ⚠️ Close, and a different family: a control nobody validated, and a number implying more than it contains. Both are real defects; neither is a decision taken by the wrong person |

### 4. Question B — what you sent your manager

| | | |
|:--:|---|---|
| **A** | Named the specific false statement, offered both legitimate paths, and offered to attribute the decision to whoever makes it | ✅ |
| **B** | Explained the principle and refused | ⚠️ Half the skill. A refusal that leaves the release blocked and offers nothing reads as obstruction, and the next decision gets taken without you |
| **C** | Escalated over their head | ⚠️ Sometimes necessary, rarely first. It also skips the move that usually ends the discussion — an attributed shortcut is a very different proposition from an unattributed one |
| **D** | Filled it in and flagged it afterwards | ❌ The flag does not travel with the value. The manifest, the report and the ticket all carry the approval; your message does not |

**Two or more ❌:** reread [Roles and human gates](../../roles-and-human-gates.md) and [Holding the boundary](../../holding-the-boundary.md) before the capstone.
