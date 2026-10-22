# Data Handling Rules

Use approved data classifications, processing environments, access controls, retention, and redaction.

## Rules currently established by this repository

These four are stated by the methodology and enforced or enforceable today.

**1. Every dataset declares its anonymisation status.** Evaluation cases are anonymised, pseudonymised or synthetic as appropriate, and the manifest records which. A dataset whose status is undeclared is not eligible for a run.

**2. Protected data never reaches an unapproved evaluator.** An AI judge, a hosted metric service and an external annotation tool are all destinations. Each must be approved for the classification of the data it will receive, before the run, and named in the manifest.

**3. Secrets never enter evidence.** Case outputs, traces and reports are redacted before they are written. The key stays visible so a reader can see a credential was present and suppressed; the value does not. This is implemented, not merely stated — see the redaction applied on the report-writing path in `run-product-evaluation`.

**4. Retention is declared before it is needed.** Where evidence is stored, who may read it and how long it is kept are declared in the manifest evidence section, not decided after a failure makes the question urgent.

## The decisions behind these rules

The four rules above are the operational consequences of nine decisions that must be taken and owned before a dataset exists: classification, lawful basis, transformation, minimisation, approved destinations, processing environment, evidence retention, subject rights, and the owner of the residual risk.

Those decisions, their questions and their typical owners are set out in [protecting evaluation data](../../07-designing-evidence/data-protection.md), together with the regulatory anchors they derive from — GDPR Art. 5, 6, 9, 28 and 15-17, and EU AI Act Art. 10 on data governance for testing datasets.

**If any of the nine is missing, the evaluation is Not Ready.** This policy applies them; it does not decide them.

## What remains open

- **The classification scheme itself.** Which classes exist, and which processing environment each permits, is an organisational decision. Until it is named, "approved data classification" has no referent and this policy is a checklist rather than a standard.
- **Jurisdictional scope.** The anchors assume EU applicability. An organisation operating elsewhere must substitute its own.

Where a question is not answered, escalate to the security, compliance and data protection stakeholder named in the manifest ownership section rather than inferring an answer.

Identity and authentication are **not** in scope here. Access control is a deterministic behaviour and a veto candidate, covered by the DoD gate.

## What this policy does not decide

- The data classification scheme itself, or which environment each class may be processed in.
- Whether a given evaluator is approved for a given classification. That is an approval, recorded before the run.
- Anything about identity or authentication testing, which the methodology does not yet cover.

## Related

- [Building a Golden Dataset](../../07-designing-evidence/golden-datasets.md) — anonymisation among the dataset design principles
- [Roles and human gates](../../09-governance/roles-and-human-gates.md) — who approves data constraints
- [Decisions required](../../annexes/decisions-required.md) — storage, access control and retention listed as open group decisions
