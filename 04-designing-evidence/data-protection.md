---
type: concept
status: draft
audience: [qa, data-ai, compliance]
---

# Protecting evaluation data

Evaluating a product means building a dataset from something real, submitting it to a candidate, and retaining the results as evidence. Each of those three steps can create an exposure that the product itself never had.

This note structures the decisions that must be taken. It does **not** take them: which classes exist, which environment each permits, and how long evidence is kept are organisational decisions with named owners, exactly as thresholds are.

> **Status: draft.** The mandatory decisions below are established. The classification scheme they refer to is not — see *Open points* at the end.

## The three exposures

| Step | What can go wrong |
|---|---|
| **Building the dataset** | Real personal or client data is copied into cases that live longer, and travel further, than the source ever did |
| **Running the evaluation** | Every evaluator is a destination. An AI judge, a hosted metric service and an external annotation tool each receive what you send them |
| **Retaining evidence** | Case outputs and traces persist by design, because the point of evidence is that it survives the run |

The third is the one teams miss. Evidence is deliberately durable, so a mistake in it is deliberately durable too.

## Mandatory decisions

Modelled on the DoT components: each row is a decision with an owner, not a value this note supplies. **If any is missing, the evaluation is Not Ready.**

| Decision | The question it answers | Typical owner |
|---|---|---|
| **Classification** | Which class does the source data carry, under our scheme? | Data protection stakeholder |
| **Lawful basis** | On what basis may this data be processed for evaluation, as distinct from the basis for the product itself? | Data protection stakeholder |
| **Transformation** | Anonymised, pseudonymised, synthetic, or raw under recorded approval? | Domain owner with data protection |
| **Minimisation** | Which fields does the evaluation actually read? Everything else is removed. | Test designer |
| **Approved destinations** | Which evaluators and services may receive this class? | Data protection stakeholder |
| **Processing environment** | Where may this class be processed, and where may it not? | Security |
| **Evidence retention** | Where is evidence stored, who may read it, when is it destroyed? | Product owner with data protection |
| **Subject rights** | How is a case removed if the person it derives from exercises a right? | Data protection stakeholder |
| **Owner** | Who accepts the residual risk of this dataset existing? | Accountable owner |

## Anonymisation is a claim, not a step

Replacing names is not anonymisation. Data is anonymised when the individual can no longer be identified **by any party, using any means reasonably likely to be used** — including by combining the remaining fields.

A dataset of 240 meeting summaries with names removed, each carrying a date, a region and a job title, is not anonymised. It is pseudonymised at best, and the surviving combination often identifies one person.

Test the claim before making it: take a case, take the fields the evaluation reads, and ask whether someone with access to one internal system could name the subject. If yes, the dataset is pseudonymised, stays in scope, and needs a lawful basis.

**Pseudonymisation is still valuable** — it reduces exposure and is a recognised safeguard. It is simply not an exit from the regime.

There is a genuine tension here. Anonymising an evaluation set can destroy the behaviour under test: if you are testing whether the product attributes a decision to the right person, removing the people removes the test. Where that happens, do not quietly keep the data raw — escalate that specific case, name the conflict, and let the decision be recorded.

## Every evaluator is a disclosure

An AI judge is a third-party processor that receives your evaluation data, and often the reference answers too. So is a hosted metric endpoint, so is an external annotation platform.

Before a run:

- name each destination in the manifest;
- record the approval that permits that class of data to reach it;
- confirm what the destination retains, and for how long;
- confirm whether it trains on what it receives.

An evaluator with no recorded approval is a blocker, not a detail. This is where an evaluation most often leaks: the dataset was handled carefully and then sent somewhere nobody assessed.

## Regulatory anchors

Named so the decisions above can be traced to something, not to substitute for advice.

| Source | What it bears on |
|---|---|
| **GDPR Art. 5** | Minimisation, purpose limitation and storage limitation — the three principles that most constrain an evaluation set |
| **GDPR Art. 6, 9** | Lawful basis, and the stricter regime for special-category data |
| **GDPR Art. 28** | Every evaluator receiving personal data is a processor, with what that entails |
| **GDPR Art. 15-17** | Subject rights, which reach into retained evidence |
| **EU AI Act Art. 10** | Data governance for training, validation and **testing** datasets: relevance, representativeness, and examination for bias. It speaks directly to evaluation sets. |
| **ISO/IEC 27701** | Privacy information management, if the organisation needs a framework rather than a checklist |

The AI Act reference matters here beyond compliance: Art. 10's requirement that testing datasets be relevant and representative is the same requirement this methodology makes for a different reason — a dataset that is not representative produces an aggregate that describes the collection method rather than the product.

## Open points

Two things this note deliberately does not settle, because settling them here would be inventing them:

- **The classification scheme itself.** Which classes exist, and which processing environment each permits, is organisational. Until it is named, `data-handling-rules` is a checklist rather than a standard.
- **Jurisdictional scope.** The anchors above assume EU applicability. An organisation operating elsewhere must substitute its own and re-derive the mandatory decisions.

Identity and authentication are **not** covered here. Access control is a deterministic behaviour, tested by the DoD gate — see [DoD: testing deterministic behaviour](../03-the-two-gates/definition-of-done.md).

---

Previous: [Building a Golden Dataset](golden-datasets.md) · [Course map](../00-orientation/progression.md) · Next: [Thresholds, slices and vetoes](thresholds-slices-vetoes.md)
