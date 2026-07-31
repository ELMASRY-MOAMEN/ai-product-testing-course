"""An impartial assessor for the exercises whose answers are discrete.

Most exercises in this course are judged by a worked solution and by you. That
works for reasoning and fails for scoring: reading a solution makes it feel
obvious, and you tick the box. Two exercises have answers that are either right
or not, so they can be checked by something that does not care how convinced
you are.

It tells you WHICH answers are wrong and WHICH question to re-ask. It does not
tell you the right answer — the solution file does that, and reaching for it
before you have re-thought the item wastes the exercise.

    python tools/check_answer.py classify B1=DoD B2=DoT B3=DoD B4=DoT B5=DoD

    python tools/check_answer.py calibrate agreement=90 reject_recall=70 \
        reject_precision=100 fabrication_recall=50
"""
import sys

CLASSIFY = {
    "B1": ("DoD", "The entitlement matrix is a documented table. Ask question 2: is the "
                  "expected decision derivable from a specification, without running the system?"),
    "B2": ("DoT", "The urgency mapping was learned from past claims and is written down nowhere. "
                  "Ask question 2: could two people derive the correct urgency from a document, "
                  "or would a qualified human have to judge each case?"),
    "B3": ("DoD", "Required fields, types and the allowed enum are fixed by the response contract. "
                  "Ask question 2 — and note that a fixed set of allowed values is not what makes "
                  "something deterministic."),
    "B4": ("DoT", "Several phrasings of a summary are acceptable. Ask question 1 first: can the "
                  "correct output be stated in advance and compared exactly?"),
    "B5": ("DoD", "The routing table is in the ops runbook. Ask question 2, and be careful not to "
                  "classify by data flow: B5 consumes B2's output, which changes nothing about "
                  "whether B5's own expected output is derivable."),
}

CALIBRATE = {
    "agreement": (90.0, "(20 + 7) / 30 — the cases where judge and human said the same thing."),
    "reject_recall": (70.0, "Of the 10 the human rejected, how many did the judge also reject?"),
    "reject_precision": (100.0, "Of the cases the judge rejected, how many did the human also reject?"),
    "fabrication_recall": (50.0, "Within the 6 fabrication cases only: the human rejected all six."),
}


def parse(arguments):
    pairs = {}
    for argument in arguments:
        if "=" not in argument:
            raise SystemExit(f"expected key=value, got {argument!r}")
        key, _, value = argument.partition("=")
        pairs[key.strip()] = value.strip()
    return pairs


def classify(answers):
    if not answers:
        raise SystemExit("give five answers, e.g. B1=DoD B2=DoT B3=DoD B4=DoT B5=DoD")
    wrong = []
    for key, (expected, hint) in CLASSIFY.items():
        given = answers.get(key)
        if given is None:
            print(f"{key}: not answered")
            wrong.append(key)
            continue
        normalised = given.strip().lower()
        if normalised in ("dod", "deterministic"):
            normalised = "DoD"
        elif normalised in ("dot", "probabilistic"):
            normalised = "DoT"
        if normalised != expected:
            print(f"{key}: not right.\n    {hint}\n")
            wrong.append(key)
    return wrong


def calibrate(answers):
    if not answers:
        raise SystemExit("give four figures, e.g. agreement=90 reject_recall=70 "
                         "reject_precision=100 fabrication_recall=50")
    wrong = []
    for key, (expected, hint) in CALIBRATE.items():
        given = answers.get(key)
        if given is None:
            print(f"{key}: not answered\n    {hint}\n")
            wrong.append(key)
            continue
        try:
            value = float(given.rstrip("%"))
        except ValueError:
            print(f"{key}: {given!r} is not a number\n")
            wrong.append(key)
            continue
        if abs(value - expected) > 1.0:
            print(f"{key}: {value:g}% is not right.\n    {hint}\n")
            wrong.append(key)
    return wrong


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("classify", "calibrate"):
        raise SystemExit(__doc__)

    exercise = sys.argv[1]
    answers = parse(sys.argv[2:])
    checker, total = (classify, len(CLASSIFY)) if exercise == "classify" else (calibrate, len(CALIBRATE))
    wrong = checker(answers)

    if not wrong:
        print(f"All {total} correct.")
        print("Now open the solution. The reasoning is the part worth reading, "
              "and getting the answer right for the wrong reason is common here.")
        return 0

    print(f"{total - len(wrong)} of {total} correct. Wrong: {', '.join(wrong)}")
    print("\nRe-think those before opening the solution. The hint above each one is "
          "the question to re-ask, not the answer.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
