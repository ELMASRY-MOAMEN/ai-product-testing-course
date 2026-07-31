---
type: reference
status: reviewed
audience: [qa, product-owner, engineering, data-ai]
---

# Read this before copying anything here

These four evaluations are complete and they run. That makes them the most useful thing in this repository to **read**, and the most dangerous thing to **copy**.

## Do not start your own artefact from one of these

Start from [the templates](../toolkit/templates/) instead. Always.

A worked example is a set of decisions that somebody approved **for a different capability**: a threshold of 0.85 because that capability's owner accepted that error rate, a slice on `regulated` because that capability had regulated cases, a veto on fabricated approvals because that capability could fabricate them.

Copy the file and you inherit all of it. The values then sit in your manifest looking like your own analysis — and by the time anyone reviews it, nothing distinguishes a decision your owner made from one this example's fictional owner made.

**A template gives you placeholders that force the question. An example gives you answers to questions you never asked.**

Everyone feels this pull, and it is strongest exactly when you are short of time. It is why the capstone [fails a submission](../capstone/rubric.md) for any value that no owner decided, however sensible that value is.

## What these are for

Read them **alongside** the module that covers what they demonstrate:

| Example | Read during | What it shows | The evidence |
|---|---|---|---|
| [01 Deterministic API](01-deterministic-api/README.md) | Module 03 | A DoD gate: assertions, no threshold, no dataset population to average | [report](01-deterministic-api/expected-report.md) · [requirements](01-deterministic-api/requirements.md) |
| [02 LLM summary](02-llm-summary/README.md) | Modules 01 and 04 | A DoT gate failing on a veto while every average passes | [report](02-llm-summary/expected-report.md) |
| [03 RAG assistant](03-rag-assistant/README.md) | Module 04 | Retrieval quality, groundedness and disclosure risk in one design | [report](03-rag-assistant/expected-report.md) |
| [04 Hybrid agent](04-hybrid-agent/README.md) | Modules 02 and 05 | The conjunctive rule: everything probabilistic excellent, and the run fails anyway | [report](04-hybrid-agent/expected-report.md) · [requirements](04-hybrid-agent/requirements.md) |

**Read the reports, not just the READMEs.** The report is the artefact a decision owner actually receives, and reading four of them teaches more about what evidence must survive a run than any description of it. The two `requirements.md` files show where the scenarios came from — the traceability the [readiness checklist](../toolkit/readiness-checklist.md) asks you to demonstrate.

## The values in these files are synthetic

Every threshold, minimum, veto and ownership entry here is fictional and approved for the example only. The ownership block in example 02 carries a comment explaining why it says so *inside the file* rather than in a header: a reader once filled those fields with a plausible role name and shipped a runnable manifest, citing the example as precedent.

A name typed into an ownership field is not a sign-off — not there, and not in your work.
