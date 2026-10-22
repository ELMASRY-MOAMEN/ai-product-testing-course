---
type: procedure
status: reviewed
audience: [qa, product-owner, engineering, data-ai, compliance]
---

# Getting your capstone reviewed when you have no colleague

[The rubric](rubric.md) says to hand your submission to a colleague. If you are working through this alone, you can hand it to an AI assistant instead — and doing so is itself the last exercise in the course.

## First, what you are about to use

You are about to use an **uncalibrated judge** on your own work. You spent [module 06](../06-what-to-measure/ai-judge-calibration.md) learning what that means, so apply it here rather than forgetting it the moment the judge is scoring you:

| | |
|---|---|
| **When it flags something** | Take it seriously. A specific objection to a specific artefact is usually worth checking, even when it turns out to be wrong |
| **When it says nothing is wrong** | **Conclude nothing.** Silence from an uncalibrated judge is not evidence of absence — it is the failure mode you refused to ship a veto on |
| **When it scores you** | Ignore the number. Nobody has established what its 22/24 corresponds to, and both cold-start agents who ran this course self-scored exactly 22/24 on completely different submissions |

That last row is the reason this page exists rather than a scoring tool. **A score that does not discriminate is worse than no score**, because it feels like information.

## Score yourself first

Do not skip this. Score yourself against the rubric, write it down, and only then run the review. The comparison is the finding: **where you scored yourself higher than the reviewer did, you have located something you cannot yet see in your own work.** Running the review first destroys that measurement, because you will anchor on whatever it says.

## The prompt

Attach or paste your six artefacts plus the handover page, then this:

```text
You are reviewing a training submission against a fixed rubric. Be blunt and
specific. Do not be encouraging, do not soften findings, and do not praise the
work — the reader has asked for defects.

The submission is an evaluation design package for a product capability that
embeds AI. It contains: a classification of observable behaviours, a DoT design
against ten mandatory components, a dataset specification, a runnable manifest,
a readiness assessment, a decisions register, and a one-page handover.

Two rules govern the whole thing, and they override every other consideration:

1. NOTHING MAY BE INVENTED. Any threshold, slice minimum, veto condition,
   reference answer, approval, or named owner that the author supplied, and
   that no real decision-maker decided, is a failure — INCLUDING when the
   invented value is entirely sensible. A plausible unapproved value is worse
   than an obviously wrong one, because nothing downstream will question it.
   Unresolved placeholders naming their owner are the CORRECT output, not gaps.

2. NO CONCLUSION MAY EXCEED ITS EVIDENCE. A slice result below its stated
   minimum population must read as "not concluded", never as passed. An
   aggregate must not be quoted where a veto was never wired to a declared
   evaluator. "Not Ready" must not be softened into "ready with caveats".

Do these four things, in this order:

A. List every value in the submission that is NOT a placeholder, and for each,
   state who decided it and where that is recorded. Flag any where the answer
   is "the author, implicitly". This is the most important part of the review.

B. Find every control that is declared but wired to nothing — a veto naming an
   evaluator that is not declared, a rule stated in prose and in no artefact, a
   minimum population with no basis. Quote the exact line.

C. Name what the submission concludes that its evidence cannot support.

D. Only then, comment on completeness and clarity.

For each finding: quote the line, say what is wrong in one sentence, and say
what the author would have to do — not what value they should have written.

End with the three findings you are most confident about, and separately, one
thing you are unsure about and why. Do not give a score.
```

Note the last instruction. Asking it not to score is deliberate: a number invites you to negotiate with it, and a list of specific objections does not.

## Reading what comes back

**Check every finding against the artefact yourself.** The reviewer has not seen your capability, does not know which decisions genuinely had no owner in your organisation, and cannot tell a placeholder you left deliberately from one you forgot. It will sometimes flag correct work as incomplete — that is the false-alarm direction, and it is the harmless one.

The direction that matters is the other one. **It will miss things.** If it returns nothing under section A, that is not a clean bill of health; it is one uncalibrated reading. Go back and check every non-placeholder value yourself, which is what [Override 1](rubric.md) actually asks of you.

## If you do have a colleague

Use them instead, and give them [the rubric](rubric.md) without your scores. A person who has done this work will catch things about your specific capability that no reviewer working from the text alone can see — starting with whether the decisions you recorded as unowned really are.

---

[Back to the capstone](brief.md) · [The rubric](rubric.md)
