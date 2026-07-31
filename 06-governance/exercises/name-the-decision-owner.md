---
type: example
status: reviewed
audience: [qa, product-owner, compliance]
---

# Exercise — Name the decision owner

**Time:** 30 minutes. **Do it before opening [the solution](solutions/name-the-decision-owner.md).**

Six situations, from a single release week. For each one:

| Question | |
|---|---|
| **Who owns this decision?** | A named role, not "the team" |
| **What do you do?** | Concretely, today |
| **What do you say?** | One or two sentences you would actually send |

Then answer the two questions at the end, which are the real ones.

---

**S1.** The run reports `Fail` on a triggered veto — one case in 240. The product owner reads the report and replies: *"Understood. It's one case out of 240, we accept the risk, ship it."*

**S2.** Same run, same veto. The **engineering lead** replies instead: *"That veto is too broad, it fires on phrasing. I've narrowed the pattern and now it doesn't trigger. Rerunning."*

**S3.** Thursday's slice-minimum decision did not happen; the meeting was cancelled. Release is tonight. Your manager says: *"Put 0.90 in, same as the aggregate. It's the obvious value and nobody will argue with it. We'll confirm Monday."*

**S4.** The AI judge scoring generation quality has never been calibrated against human-labelled examples. It is producing scores that look plausible. Nobody has asked about it.

**S5.** The report shows the `vulnerable-client` slice at `1.00`, population 4. A stakeholder quotes it in the release note as evidence that the capability is safe for vulnerable clients.

**S6.** A dataset case has been marked `approved` for three months. You notice its reference contradicts the requirement it traces to — one of them is wrong. Six evaluations have already run against it.

---

## The two questions

**A.** Three of these six are the *same* failure wearing different clothes. Which three, and what is the shared shape?

**B.** In S3, your manager is more senior than you and the reasoning is sound — 0.90 *is* the obvious value. Write what you send. Then say what you do if the answer comes back: *"Noted. Do it anyway."*

## Constraint

"Escalate it" is not an answer on its own. Say to whom, with what, and what you do while waiting — the release is still tonight.
