"""An impartial assessor for the exercises whose answers are discrete.

Most exercises in this course are judged by a worked solution and by you. That
works for reasoning and fails for scoring: reading a solution makes it feel
obvious, and you tick the box. Some exercises have answers that are either
right or not, so they can be checked by something that does not care how
convinced you are.

It tells you WHICH answers are wrong and WHICH question to re-ask. It does not
tell you the right answer — the solution file does that, and reaching for it
before you have re-thought the item wastes the exercise.

    python tools/check_answer.py criteria AC1=testable AC2=not-testable ...
    python tools/check_answer.py boundaries lowest_accepted=20 below=19 ...
    python tools/check_answer.py levels L1=component L2=integration ...
    python tools/check_answer.py verdicts V1=passed V2=failed ...
    python tools/check_answer.py report J1=product J2=environment J3=gap
    python tools/check_answer.py failures K1=product K2=test K3=environment
    python tools/check_answer.py figures preparation=83 execution=67 ...

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


# Part 1: discrete answers. Each entry: the expected value, and the question to re-ask.
CHOICES = {
    "criteria": {
        "AC1": ("testable", "Could two people run it and agree on the result? Look for an observable "
                            "outcome, a number, and a place where it is measured."),
        "AC2": ("not-testable", "What would a tester observe to say it passed, and would a second "
                                "tester observe the same thing?"),
        "AC3": ("testable", "Look for the three parts: a starting situation, an action, an outcome "
                            "someone can see."),
        "AC4": ("not-testable", "Correct according to what? Is the source of the right answer named?"),
    },
    "levels": {
        "L1": ("component", "Can the unit's code alone decide it, with its inputs controlled?"),
        "L2": ("integration", "Where does it break if it breaks: inside one unit, or at the seam "
                              "between two?"),
        "L3": ("system", "Does this behaviour exist before the product is assembled and deployed "
                         "with its real sign-in?"),
        "L4": ("component", "Pure validation logic. What would a slower level prove that this one "
                            "does not?"),
        "L5": ("integration", "It is about how two parts handle each other's failure. Where is that "
                              "seam tested?"),
        "L6": ("ai", "Can the right output be stated in advance and compared exactly?"),
    },
    "verdicts": {
        "V1": ("passed", "Which verdict says the case proved what it was written to prove?"),
        "V2": ("failed", "The step ran and the result differs from the specification."),
        "V3": ("blocked", "Did the product do anything wrong, or could the test not run at all?"),
        "V4": ("not-applicable", "Does the case still make sense for this release?"),
        "V5": ("not-testable", "Nothing went wrong. Does the campaign have the means to test it?"),
        "V6": ("settled", "The failure happened, and someone with authority decided about it. "
                          "Which verdict keeps both facts?"),
    },
    "report": {
        "J1": ("product", "Where does the expected value come from, and does someone own it?"),
        "J2": ("environment", "Did any assertion about the product run before the test stopped?"),
        "J3": ("gap", "It neither passed nor failed. What does the report prove about it, and is "
                      "the reason given a reason?"),
    },
    "failures": {
        "K1": ("product", "The expected result comes from the routing table. Which of the two "
                          "disagrees with it?"),
        "K2": ("test", "Which one follows the current contract: the product or the test?"),
        "K3": ("environment", "Did the test get as far as looking at what the product did?"),
    },
}

# Part 1: figures. Each entry: the expected value, the tolerance, and the question to re-ask.
FIGURES = {
    "boundaries": {
        "lowest_accepted": (20, 0, "Is the lower bound included or excluded?"),
        "below": (19, 0, "A boundary is tested on the limit and on the first value either side."),
        "highest_accepted": (2000, 0, "Is the upper bound included or excluded?"),
        "above": (2001, 0, "The first value past the upper limit."),
        "classes": (3, 0, "How many different treatments does the rule give a length?"),
    },
    "figures": {
        "preparation": (83, 1, "Testable requirements with at least one designed case. Is EX-07 "
                               "testable? Does EX-06 have a case?"),
        "execution": (67, 1, "Requirements with at least one case run Passed, Failed or Settled. "
                             "Was any EX-02 case actually run?"),
        "progress": (70, 1, "Planned cases executed over planned cases. A blocked case is not "
                            "executed."),
        "quality": (57, 1, "Passed over Passed, Failed and Settled. A settled case is not a "
                           "success."),
    },
}


def choose(table, answers):
    if not answers:
        raise SystemExit("give one answer per item: " + " ".join(f"{key}=..." for key in table))
    wrong = []
    for key, (expected, hint) in table.items():
        given = answers.get(key)
        if given is None:
            print(f"{key}: not answered")
            wrong.append(key)
        elif given.strip().lower() != expected:
            print(f"{key}: not right.\n    {hint}\n")
            wrong.append(key)
    return wrong


def measure(table, answers):
    if not answers:
        raise SystemExit("give one figure per item: " + " ".join(f"{key}=..." for key in table))
    wrong = []
    for key, (expected, tolerance, hint) in table.items():
        given = answers.get(key)
        if given is None:
            print(f"{key}: not answered\n    {hint}\n")
            wrong.append(key)
            continue
        try:
            value = float(given.rstrip("%").replace(",", ""))
        except ValueError:
            print(f"{key}: {given!r} is not a number\n")
            wrong.append(key)
            continue
        if abs(value - expected) > tolerance:
            print(f"{key}: {value:g} is not right.\n    {hint}\n")
            wrong.append(key)
    return wrong


def main():
    exercises = ("classify", "calibrate", *CHOICES, *FIGURES)
    if len(sys.argv) < 2 or sys.argv[1] not in exercises:
        raise SystemExit(__doc__)

    exercise = sys.argv[1]
    answers = parse(sys.argv[2:])
    if exercise == "classify":
        checker, total = classify, len(CLASSIFY)
    elif exercise == "calibrate":
        checker, total = calibrate, len(CALIBRATE)
    elif exercise in CHOICES:
        checker, total = (lambda given: choose(CHOICES[exercise], given)), len(CHOICES[exercise])
    else:
        checker, total = (lambda given: measure(FIGURES[exercise], given)), len(FIGURES[exercise])
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
