---
type: procedure
status: reviewed
audience: [qa, product-owner, engineering, data-ai, compliance]
---

# Prerequisites

## What you need

- **Python 3.10 or later**, and a terminal.
- **A text editor.** [Obsidian](https://obsidian.md) is a bonus, not a requirement.
- No machine-learning background, no API key, no model access. Every exercise runs against a mock candidate offline.

## Setup

```bash
git clone https://github.com/ELMASRY-MOAMEN/ai-product-testing-course.git
cd ai-product-testing-course
```

Create the virtual environment **outside** the repository, so the link validator does not scan it:

```bash
python -m venv ../course-venv
```

Activate it — `../course-venv/Scripts/activate` on Windows, `source ../course-venv/bin/activate` on macOS and Linux. Nothing needs to be installed for the exercises; the runner uses the standard library.

## Check that it works

```bash
python lab/run-product-evaluation/scripts/run_evaluation.py worked-examples/02-llm-summary/manifest.yaml
```

It should print a verdict. If it prints **Fail**, that is the expected result — [module 01](../01-warm-up/run-your-first-evaluation.md) explains why, and that explanation is the beginning of the course.

## Where to put your own work

Anything you produce — exercise attempts, your capstone — goes in `my-work/`, which is gitignored. Your work stays yours and never collides with an update to this repository.

```bash
mkdir my-work
```

---

Previous: [How to use this course](how-to-use-this-course.md) · [Course map](progression.md) · Next: [Run your first evaluation](../01-warm-up/run-your-first-evaluation.md)
