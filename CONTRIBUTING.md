# Contributing

Corrections, better exercises and reports of things that did not teach well are all welcome. Open an issue or a pull request.

The course is free to read and not open for reuse (see [LICENSE](LICENSE)). By sending a contribution, you agree that it is published here under the same terms, and that I may use it in the course and its later versions.

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
pip install -r requirements-dev.txt
python tools/validate_links.py && python tools/validate_path.py && python tools/verify_runs.py && pytest lab/run-product-evaluation/tests -q
```

All four run on every push and pull request — see [the workflow](.github/workflows/validate.yml).

**`validate_links.py`** — every relative link resolves. Because wikilinks are not used, this covers every link in the corpus.

**`validate_path.py`** — the checks link validity cannot make, because they are about *absence*: every chained page ends with exactly one footer, each `Next` is answered by the matching `Previous`, every exercise sits on the chain, every page has an inbound link, and every path in a documented command exists.

It exists because the first was green while the reading chain skipped all six exercises. A chain that omits a page contains no broken link. If you add a page, add it to the chain or link it from somewhere — `validate_path.py` will tell you which you forgot.

**`verify_runs.py`** — the figures the notes quote are the figures the runner produces. Module 03 promises 0.960 and one veto on `MR-020`; module 08 promises 0.927, 0.917 and `CT-007`. A reader who runs the command and sees something else stops trusting the page. Note that the runner exits `0` whatever it concludes, so a shell loop cannot catch this — the assertion has to read the report.

**`pytest lab/…/tests`** — 29 tests that came with the vendored runner. Not part of the course; they are why `Not Ready` really blocks and why a veto naming an undeclared evaluator is caught before a run rather than during one.

**If you change the chain**, edit both the footer of the page and the footers of its two neighbours. Running `validate_path.py` after a one-sided edit reports exactly which side you missed.

**If you change an exercise whose answers `tools/check_answer.py` grades** — the module 04 classification and the module 06 calibration arithmetic — change the answer key in the same commit. Nothing enforces that link, and a checker that disagrees with its own solution is worse than no checker.

## On feedback, if you are writing an exercise

A self-taught reader cannot ask anyone whether they were right. Three instruments carry that weight here, in descending order of how hard they are to fool:

1. **Predict, then run.** The reader writes a prediction, the runner rules on it. Unfoolable, and the reason the two executable exercises are the strongest in the course. Reach for this first.
2. **A discrete answer key**, via `check_answer.py`. It names what is wrong and which question to re-ask, never the answer.
3. **Forced choice** — the *Locate yourself* block ending every solution. Three plausible things the reader might have written, one right, and a verdict on each near-miss.

Do not add a tick-box checklist. They were removed for a reason: after reading a solution, everything looks like what you meant, and the reader ticks the box.

If you changed anything the exercises run against, rerun them:

```bash
python lab/run-product-evaluation/scripts/run_evaluation.py worked-examples/02-llm-summary/manifest.yaml
python lab/run-product-evaluation/scripts/run_evaluation.py 08-running-it/exercises/solutions/claimtriage-manifest.yaml
```

Both are expected to report **Fail** on a triggered veto. A solution that stops matching its exercise is worse than no solution.

## Rules that are not up for negotiation

The course teaches people to refuse to invent decisions. Any contribution that supplies a threshold, slice minimum, veto condition, reference answer or approval as a helpful default contradicts the thing being taught — including in an example, and including when the value is a good one.
