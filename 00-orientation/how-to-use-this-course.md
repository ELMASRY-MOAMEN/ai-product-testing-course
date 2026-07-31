---
type: procedure
status: reviewed
audience: [qa, product-owner, engineering, data-ai, compliance]
---

# How to use this course

## Who it is for

Anyone who will be asked to test a product that embeds AI: QA and test engineers first, but product owners, developers, data specialists and compliance stakeholders follow the same path. No machine-learning background is assumed, and none is taught.

If you have tested software before, the first module will feel familiar and then stop being familiar. That moment is the subject of the course.

## The loop

Each module works the same way:

1. **Read the notes**, in the order given. Each carries one message, and links to the next.
2. **Do the exercise** before opening its solution. This matters more than it sounds — see below.
3. **Compare** with the worked solution, which explains the reasoning, not just the answer.
4. **Check yourself** against the module's mastery criterion. If you cannot meet it, the notes to reread are named there.

## Do the exercises before reading the solutions

Reading a solution produces recognition, not competence. You will read the reasoning, find it obvious, and be unable to reproduce it three weeks later on your own product.

Every defect this methodology was built from was found by **constructing something**, never by reviewing it. The same holds for learning it.

## Use a real capability as early as you can

From module 02 onwards, apply each step to a capability from your own work in parallel with the exercises. By the capstone you will already have the material, and the exercises will have stopped being abstract.

If you cannot use a real one, the [capstone brief](../capstone/brief.md) provides a scenario deliberately unlike the four worked examples.

## The failure mode to watch for in yourself

You will reach a point where an artefact is nearly complete and one value is missing: a threshold nobody approved, a reference answer nobody annotated, an owner nobody named.

The pull to fill it with something plausible so the work looks finished is strong, and it is the single most common failure — for humans and for coding agents alike. Filling it converts a missing decision into evidence that nobody approved.

**Keep the placeholder. Report `Not Ready`. Name the role that owns the decision.** That is a complete, correct deliverable, and the course assesses it as one.

## Reading it in Obsidian

This repository is also an [Obsidian](https://obsidian.md) vault: the vault root is the repository root, so opening the cloned folder as a vault gives you graph view, backlinks and outgoing links with no setup.

Links are relative Markdown, never `[[wikilinks]]`, so everything also renders on GitHub. If you contribute a note, keep that convention — `tools/validate_links.py` only checks standard Markdown links.

## What this course does not cover

- **Building or fine-tuning models.** The scope is evaluating products that embed AI.
- **Benchmarking models against each other.** A benchmark is not an evaluation of your product.
- **Authoring the coding-agent skills** that automate this. Those notes are kept in [`annexes/`](../annexes/README.md), out of the reading order.

---

[Course map](progression.md) · Next: [Prerequisites](prerequisites.md)
