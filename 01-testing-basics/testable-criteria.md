---
type: concept
status: reviewed
audience: [qa, product-owner, engineering]
---

# A criterion someone can test

## Where the expected result comes from

In a product team, the expected result of a test comes from the **acceptance criteria** of a user story. If the criterion is vague, the tester has to invent the expected result, and you saw in [the previous note](a-green-suite-on-a-bug.md) what an invented expected result is worth.

So the first test happens before any test is written: **can this criterion be tested as written?**

## Three things a testable criterion has

1. **A starting situation**: who, with what data, in what state.
2. **An action**: what happens.
3. **An outcome someone can observe**: a value, a message, a code, a record, a time measured somewhere, and nothing that depends on taste.

Two people reading it must reach the same verdict on the same run. "Fast", "intuitive", "correct", "user-friendly" fail that test: two testers will disagree, and the developer will agree with whichever one passes.

The **Given / When / Then** form forces the three parts:

```gherkin
Scenario: Refuse a motor claim to an agent without the motor entitlement
  Given a front-office agent whose role is not entitled to the motor product line
  When they open motor claim 5003 in ClaimTriage
  Then ClaimTriage returns the error ENTITLEMENT_DENIED
  And no triage card is produced
```

You do not have to write every criterion in this form. You have to be able to. [The scenario-writing rules](../toolkit/gherkin-and-test-contracts.md) go further.

## What you cannot make testable on your own

Often a criterion is vague because **nobody has decided** the number or the rule yet. "The description must not be too long": too long is how many characters? That is not a tester's decision, and inventing a plausible number is the trap from the previous note in another form: a number nobody approved reads downstream exactly like an approved one.

The honest version keeps the decision open and names who takes it:

> Given an agent pastes a description longer than **‹maximum length, to confirm with the product owner›** characters, when they submit it, then ClaimTriage rejects it with the error `DESC_LENGTH` and nothing is sent to the model.

That criterion is not finished, and it says so. It is still far more useful than "not too long": everyone can see what is missing and who must supply it.

## Check yourself

### What three parts does a testable criterion have, and what do you do with a number nobody has decided?

<details>
<summary>Answer</summary>

A starting situation, an action, and an outcome someone can observe. A number nobody has decided stays "to confirm", with the name of who decides it: inventing a plausible one would make it read like an approved one.
</details>

---

Previous: [A green suite on a bug](a-green-suite-on-a-bug.md) · [Course map](../00-orientation/progression.md) · Next: [Exercise: judge and rewrite criteria](exercises/judge-and-rewrite-criteria.md)
