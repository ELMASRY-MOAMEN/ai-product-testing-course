---
type: reference
status: reviewed
audience: [qa, data-ai]
---

# What exactly should we evaluate

A complete suite should select metrics from the requirements and risks, not from what a tool happens to offer.

## Evaluation families

### 1. Domain capability

Does the output contain the business information required to perform the task?

Examples:

- required-fact recall;
- correct section placement;
- correct classification;
- correct entity or fund matching;
- correct extraction of next steps.

### 2. Generation quality

Is the generated content supported, relevant and safe?

Examples:

- groundedness;
- factual consistency;
- unsupported-claim rate;
- relevance;
- clarity;
- harmful or prohibited content.

### 3. Instruction following

Did the agent follow the requested contract?

Separate:

- exact checks, such as JSON schema, required sections or forbidden fields;
- judged checks, such as whether the response answered the user’s intent.

### 4. Operational quality

Does the system remain usable and sustainable?

Examples:

- latency;
- cost;
- tool-call volume;
- dependency failures;
- retry behaviour.

## Choose the simplest valid evaluator

| Requirement | Preferred evaluator |
|---|---|
| Exact schema or fixed rule | Deterministic code |
| Structured extraction or business matching | Custom deterministic or business evaluator |
| Expert qualitative judgement | Human rubric |
| Scalable semantic judgement | AI judge calibrated against human-labelled examples |

> **Takeaway:** Do not use an LLM judge where code can provide a more exact, explainable and reproducible answer.

---

Previous: [Module 06 — What to measure](README.md) · [Course map](../00-orientation/progression.md) · Next: [Does the metric measure the thing](does-the-metric-measure-it.md)
