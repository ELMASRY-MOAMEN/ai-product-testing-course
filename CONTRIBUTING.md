# Contributing

Corrections, better exercises and reports of things that did not teach well are all welcome. Open an issue or a pull request.

## What is most useful

**Tell me where the course failed you.** Which note you had to read twice, which exercise was ambiguous, which solution answered a question you were not asking. That is worth more than a typo fix, and it is the only way the course improves at the thing it claims to do.

**New exercises**, especially for concepts that currently have none. An exercise here has a shape: a realistic artefact with defects in it, a constraint that forbids inventing the missing decisions, and a worked solution that explains the reasoning rather than announcing the answer.

**Real-capability capstone reports.** If you ran the capstone on something from your own work, what the methodology missed is a finding.

## Conventions

**Links are relative Markdown, never `[[wikilinks]]`.** GitHub does not render wikilinks outside its own wiki, and the link validator only parses standard Markdown. This repository is also an Obsidian vault, configured with `useMarkdownLinks: true` and `newLinkFormat: relative`, so backlinks and graph view work normally.

**Every note in the course zones carries front-matter:**

```yaml
---
type: moc | concept | procedure | reference | example
status: draft | reviewed | approved
audience: [product-owner, qa, engineering, data-ai, compliance]
---
```

`type` follows the [Diátaxis](https://diataxis.fr) split — a note has exactly one. A note that explains *and* instructs must be split.

**The reading chain is real.** Every note in the course order ends with `Previous · Course map · Next`. Inserting a note means updating its neighbours.

**`lab/` is vendored, not authored here.** It is a copy of the `run-product-evaluation` skill from the companion `ai-product-testing-skills` repository. Fix it there, not here.

## Before opening a pull request

```bash
pip install -r requirements.txt && python tools/validate_links.py && python tools/validate_path.py
```

**`validate_links.py`** — every relative link resolves. Because wikilinks are not used, this covers every link in the corpus.

**`validate_path.py`** — the checks that link validity cannot make, because they are about *absence*: every chained page ends with exactly one footer, each `Next` is answered by the matching `Previous`, every exercise sits on the chain, and every page has at least one inbound link.

The second one exists because the first was green while the reading chain skipped all six exercises. A chain that omits a page contains no broken link. If you add a page, add it to the chain or link it from somewhere — `validate_path.py` will tell you which you forgot.

**If you change the chain**, edit both the footer of the page and the footers of its two neighbours. Running `validate_path.py` after a one-sided edit reports exactly which side you missed.

If you changed anything the exercises run against, rerun them:

```bash
python lab/run-product-evaluation/scripts/run_evaluation.py worked-examples/02-llm-summary/manifest.yaml
python lab/run-product-evaluation/scripts/run_evaluation.py 06-running-it/exercises/solutions/claimtriage-manifest.yaml
```

Both are expected to report **Fail** on a triggered veto. A solution that stops matching its exercise is worse than no solution.

## Rules that are not up for negotiation

The course teaches people to refuse to invent decisions. Any contribution that supplies a threshold, slice minimum, veto condition, reference answer or approval as a helpful default contradicts the thing being taught — including in an example, and including when the value is a good one.
