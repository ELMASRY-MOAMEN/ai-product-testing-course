---
type: concept
status: reviewed
audience: [product-owner, qa, engineering]
---

# Why AI products need a different testing approach

## Traditional software testing

A deterministic system is normally tested with a controlled input and one expected observable result.

```text
Controlled input + fixed rule -> expected output -> Pass or Fail
```

Examples:

- an empty mandatory field is rejected;
- an unauthorized user cannot access a client record;
- an API response follows the approved JSON schema;
- a calculation returns the expected value;
- an audit event is written after a sensitive operation.

## What changes with an LLM

An LLM may produce several acceptable answers for the same input. The wording may change even when the meaning remains correct.

```text
Same input + probabilistic generation -> several possible outputs
```

A generated answer therefore cannot always be evaluated through exact string equality.

We must answer two separate questions:

1. **Did the system behave exactly as required?**
2. **Is the generated result sufficiently trustworthy for the intended use and risk level?**

## The two forms of evidence

| Evidence | Question | Typical verdict |
|---|---|---|
| **Conformance evidence** | Did the system, integration and control layer behave exactly as specified? | Binary Pass or Fail |
| **Trust evidence** | Did the AI output meet the agreed quality and risk thresholds? | Thresholds, slices and vetoes |

> **Takeaway:** AI evaluation does not replace software testing. It adds a second layer of evidence for probabilistic behaviour.

---

Previous: [What just happened](../01-warm-up/what-just-happened.md) · [Course map](../00-orientation/progression.md) · Next: [One product can contain three types of behaviour](output-classification.md)
