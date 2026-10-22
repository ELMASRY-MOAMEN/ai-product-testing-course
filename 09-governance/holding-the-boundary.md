---
type: procedure
status: reviewed
audience: [qa, product-owner, compliance]
---

# Holding the boundary

You now know which decisions are not yours. The remaining skill is saying so, to someone who outranks you, on the evening of a release, without becoming the person the team routes around.

Refusing is the easy half and it is worth almost nothing on its own. **A refusal that leaves the release blocked and offers nothing is indistinguishable, from the other side of the table, from an obstruction** — and the next time the decision comes up, it will be taken without you.

## What is actually at stake

Not your integrity. The artefact.

When you type a value nobody approved, the manifest asserts that somebody did, the report inherits the assertion, and the release ticket inherits it from the report. Nothing downstream distinguishes a threshold the product owner set from one you typed at 19:40 to unblock a pipeline. The record becomes false, quietly, and stays false.

That is the sentence to have ready, because it is concrete and it is not about you:

> *The moment I type 0.90 there, the report says the product owner approved a gate for high-value claims, and they did not. That is the one line in the file that would not be true.*

Note what it does not say: *I am not comfortable*, *that would not be rigorous*, *the methodology says*. Those invite a debate about your judgement. Naming the specific false statement does not.

## The three moves

### 1. Name the falsehood, not the principle

Point at the field and say what it would claim. One sentence. Principles invite argument; a false record does not.

### 2. Offer the legitimate paths, both of them

There are almost always two, and they are both fast:

- **Get the decision.** Usually five minutes of the owner's time — a one-line confirmation by email, which you then transcribe. Offer to draft it for them.
- **Ship the honest artefact.** Run it, report `Not Ready` on the one unresolved item, and let everything else be measured. That is a complete, correct deliverable, and it blocks nothing except a conclusion nobody is entitled to draw.

A person who wants the release, not the number, will take one of these. Most of the pressure you feel is someone assuming the only options are *fill it in* or *nothing ships*.

### 3. Attribute the decision to whoever makes it

If someone with the authority wants the value in, it can go in — under **their** name:

> *You can set it yourself and I will record it as your decision, with your name in `approved_by`.*

This is not a threat and it should not be delivered as one. A decision made by someone entitled to make it, recorded under their name, is **legitimate**. What is illegitimate is a decision made by you and recorded as theirs. Offering to attribute it correctly resolves the conflict without anyone inventing anything.

In practice this is the sentence that most often ends the discussion — because an unattributed shortcut and an attributed one are very different propositions for the person asking.

## Accepting risk is allowed

The most common misreading of this material is that a veto makes release impossible. It does not.

A veto blocks **automated** acceptance and forces the decision to a human who is accountable for it. That human may accept the risk. That is what the gate is for.

What must not happen is the acceptance being disguised as a pass:

| | |
|---|---|
| **Correct** | The run stands at `Fail`. A documented override sits beside it: who accepted, what they accepted, on what date, with what mitigation |
| **Wrong** | The veto is narrowed, or removed, or the run is repeated until it is green |

An accepted failure and a passing run are not the same artefact, and only one of them is true. Your job at that moment is clerical and it matters enormously: record it accurately.

## When you are overruled

It happens. Say it once more, in writing, without escalating your tone, and then do the part that is yours:

- **Do not author the value.** Not under pressure, not "provisionally".
- **Run what can be run.** `Not Ready` on the open item, everything else measured, so the evening is not wasted.
- **Put the gap where the decision owner will see it** — the release ticket, not a private message.

If it goes in anyway without an owner, you have done your part: you refused to author it, you offered the legitimate paths, and you left a written trace for the person who is accountable. What you have not done is make yourself the last line of defence for a decision that was never yours — which is not a role anyone can hold, and not one this methodology asks you to.

## The failure this prevents

Three things that look completely different and are the same defect: narrowing a veto after seeing what it caught, filling a threshold nobody approved, and correcting a dataset reference yourself.

In all three, **someone substitutes their own judgement for a decision that belongs to a named owner, and the artefact ends up looking finished.** That is what makes them worse than a visible failure. A `Fail` is read as a `Fail`. An invented approval is read as an approval.

> **Takeaway:** Naming the specific falsehood beats invoking a principle, offering the two legitimate paths beats refusing, and attributing a decision to whoever makes it beats making it yourself.

---

Previous: [Roles and human gates](roles-and-human-gates.md) · [Course map](../00-orientation/progression.md) · Next: [The methodology in five rules](five-rules-recap.md)
