---
type: example
status: reviewed
audience: [qa, product-owner, engineering, data-ai]
---

# Exercise — Score a DoT against its ten components

**Time:** 30 minutes. **Do it before opening [the solution](solutions/score-a-dot-against-its-ten-components.md).**

## What you are handed

A team sends you the design below and asks you to sign it off so the run can start tomorrow morning.

> ## Evaluation design — Support reply assistant, v2
>
> **What we are testing.** Our assistant drafts replies to customer support tickets. We want to know whether the drafts are good enough to be offered to agents as a starting point. We are also checking that the tone stays on-brand and that response latency stays acceptable.
>
> **Data.** We exported 300 real tickets from the production database last Thursday, with the replies our senior agents actually sent. Those sent replies are our references. The export is in `tickets_march.jsonl` on the shared drive.
>
> **How we score.** An LLM judge compares the draft to the reference reply and returns a score from 1 to 5. We use `gpt-latest` with the prompt in `judge_prompt.txt`. We take the mean across all cases.
>
> **Bar to clear.** Mean score of 4.0 or above. We picked 4.0 because the last vendor demo scored 4.2, so it is achievable.
>
> **What we watch out for.** Replies that promise a refund we cannot honour are a serious problem — Legal has been clear about that.
>
> **Reporting.** We will report the mean score, and a pass/fail, in the release ticket.
>
> **Sign-off.** QA lead to approve the results.

## What to produce

**1. The scorecard.** For each of the ten mandatory DoT components: present, partially present, or missing — with one line of evidence from the text above.

| Component | Status | Evidence or gap |
|---|---|---|

**2. The verdict.** What is the correct status of this evaluation, and what exactly do you write in the blocker list?

**3. The three most dangerous problems**, ranked, with the consequence of each if the run proceeds as designed. At least one of them is not a missing component — it is a stated choice that is wrong.

**4. One sentence to the team.** They need the run to start tomorrow. Write what you actually send them.

## Constraint

Do not repair the design. You are not the owner of any of the missing decisions, and proposing a threshold here — even a sensible one — is the exact failure the course assesses.
