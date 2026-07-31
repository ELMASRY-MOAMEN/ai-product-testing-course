---
type: concept
status: reviewed
audience: [product-owner, qa, data-ai]
---

# Thresholds, slices and vetoes

## Threshold

A threshold defines the level required for a metric to pass.

```yaml
required_fact_recall:
  minimum: <approved value>
```

Thresholds must be approved **before** viewing the candidate results.

## Critical slice

A slice is a meaningful subset of the dataset that must be analysed independently.

Examples:

- missing-data cases;
- authorization cases;
- a business segment;
- a language;
- a meeting type;
- cases using multiple sources;
- high-risk user intents.

A strong global average can hide a weak or unsafe subgroup.

## Veto

A veto is a critical failure that blocks acceptance regardless of averages.

Examples of possible veto categories, subject to product and risk approval:

- unauthorized data disclosure;
- fabricated critical business information;
- uncontrolled write operation;
- exposure of a secret or credential;
- prohibited recommendation presented as approved advice.

## Decision example

```text
Global groundedness: Pass
Required-fact recall: Pass
Authorization slice: Fail
Unauthorized disclosure veto: Triggered

Final DoT result: Fail
```

> **Takeaway:** A good average never cancels a critical failure.

---

Previous: [Protecting evaluation data](data-protection.md) · [Course map](../00-orientation/progression.md) · Next: [Exercise — Write a veto an average hides](exercises/write-a-veto-an-average-hides.md)
