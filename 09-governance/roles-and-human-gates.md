---
type: concept
status: reviewed
audience: [product-owner, compliance]
---

# Roles and human gates

| Role | Responsibility |
|---|---|
| Product Owner | Clarify intended behaviour, use and product risk |
| Business Owner or expert | Approve business references, rubrics and acceptable quality |
| Engineering | Implement the candidate, instrumentation and technical controls |
| QA/Test | Design coverage, execute tests and preserve evidence |
| Data/AI specialist | Implement and calibrate evaluators where required |
| Security, Compliance and Data Protection | Approve relevant constraints and critical controls |
| Authorized decision owner | Accept or reject residual risk and candidate release |

## Authority boundary

The automated runner can:

- execute the approved protocol;
- calculate results;
- identify failures;
- recommend a verdict from configured rules.

It must not:

- invent acceptance policy;
- approve its own evaluator;
- waive a critical failure;
- accept residual risk;
- make the final production release decision without the authorized human gate.

> **Takeaway:** Automation produces evidence. Accountability remains human.

---

Previous: [Module 09 — Governance](README.md) · [Course map](../00-orientation/progression.md) · Next: [Holding the boundary](holding-the-boundary.md)
