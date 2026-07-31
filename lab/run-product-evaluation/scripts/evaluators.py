"""Evaluators available to the runner.

Each evaluator answers one question about one case and returns a score with
the findings that explain it. An evaluator that returns a number without
naming what failed produces a result nobody can act on.
"""


def text_of(output):
    """The candidate's answer, whatever shape the adapter normalised it into."""
    if isinstance(output, dict):
        return str(output.get("answer", output)).lower()
    return str(output).lower()


def required_facts_recall(case, output):
    """Fraction of the case's required facts present in the output."""
    required = (case.get("reference") or {}).get("required_facts") or []
    if not required:
        return {"score": None, "findings": [], "note": "no required facts declared"}

    text = text_of(output)
    missing = [fact for fact in required if str(fact).lower() not in text]
    score = (len(required) - len(missing)) / len(required)
    findings = [f"missing required fact: {fact}" for fact in missing]
    return {"score": score, "findings": findings}


def forbidden_claims(case, output):
    """Detect claims the case declares must never appear.

    Returns a triggered flag rather than a score: this evaluator exists to
    feed a veto, and a veto is not an average.
    """
    forbidden = (case.get("reference") or {}).get("forbidden_claims") or []
    text = text_of(output)
    present = [claim for claim in forbidden if str(claim).lower() in text]
    return {
        "score": 0.0 if present else 1.0,
        "triggered": bool(present),
        "findings": [f"forbidden claim present: {claim}" for claim in present],
    }


def retrieval_recall(case, output):
    """Fraction of the sources the case requires that were actually retrieved.

    A retrieval-backed answer can be fluent, complete and wrong for the right
    reason: if the passage that carries the answer was never fetched, whatever
    the candidate produced came from somewhere else.
    """
    required = (case.get("reference") or {}).get("required_sources") or []
    if not required:
        return {"score": None, "findings": [], "note": "no required source declared"}

    retrieved = set(output.get("retrieved") or []) if isinstance(output, dict) else set()
    missing = [source for source in required if source not in retrieved]
    score = (len(required) - len(missing)) / len(required)
    return {"score": score, "findings": [f"required source not retrieved: {source}" for source in missing]}


def citation_support(case, output):
    """Every cited source must be one the candidate actually retrieved.

    Citing a source that was never fetched is a fabricated citation. It reads
    as evidence, survives a reader's spot-check of the source list, and is not
    a matter of degree — which is why it belongs behind a veto.
    """
    if not isinstance(output, dict):
        return {"score": None, "triggered": False, "findings": []}

    retrieved = set(output.get("retrieved") or [])
    cited = output.get("cited") or []
    unsupported = [source for source in cited if source not in retrieved]
    return {
        "score": 0.0 if unsupported else 1.0,
        "triggered": bool(unsupported),
        "findings": [f"cited a source that was not retrieved: {source}" for source in unsupported],
    }


def schema_conformance(case, output):
    """Assertion: the output carries every field the contract requires.

    Deterministic. A field is present or it is not, so this returns a pass and
    never a score to be averaged.
    """
    required = (case.get("reference") or {}).get("required_fields") or []
    present = output if isinstance(output, dict) else {}
    missing = [field for field in required if not present.get(field)]
    return {
        "passed": not missing,
        "score": 0.0 if missing else 1.0,
        "findings": [f"required output field missing or empty: {field}" for field in missing],
    }


def tool_call_conformance(case, output):
    """Assertion: the expected tool was called, and only when it should be.

    Both directions matter. Failing to act is one defect; acting when the case
    declares no tool call is another, and usually the more serious — an agent
    that opens a ticket nobody asked for has taken an action on someone's
    behalf.
    """
    expected = (case.get("reference") or {}).get("expected_tool_call")
    actual = output.get("tool_call") if isinstance(output, dict) else None

    if not expected:
        if actual:
            return {
                "passed": False, "score": 0.0,
                "findings": [f"tool called when none was expected: {actual.get('name')}"],
            }
        return {"passed": True, "score": 1.0, "findings": []}

    if not actual:
        return {
            "passed": False, "score": 0.0,
            "findings": [f"expected tool call was not made: {expected.get('name')}"],
        }

    problems = []
    if actual.get("name") != expected.get("name"):
        problems.append(f"wrong tool called: {actual.get('name')} instead of {expected.get('name')}")
    for key, value in (expected.get("arguments") or {}).items():
        found = (actual.get("arguments") or {}).get(key)
        if found != value:
            problems.append(f"tool argument {key!r} was {found!r}, expected {value!r}")
    return {"passed": not problems, "score": 0.0 if problems else 1.0, "findings": problems}


def exact_values(case, output):
    """Assertion: declared output fields equal their expected values exactly.

    For calculations, totals, codes and any field whose correct value is
    derivable from a specification rather than annotated by a human. Rounding
    is part of the expected value: declare the rounded figure, and a candidate
    that rounds differently fails.
    """
    expected = (case.get("reference") or {}).get("expected_values") or {}
    if not expected:
        return {"passed": True, "score": None, "findings": [], "note": "no expected value declared"}

    present = output if isinstance(output, dict) else {}
    problems = []
    for field, value in expected.items():
        found = present.get(field)
        if found != value:
            problems.append(f"{field} was {found!r}, expected {value!r}")
    return {"passed": not problems, "score": 0.0 if problems else 1.0, "findings": problems}


REGISTRY = {
    "required_facts_recall": required_facts_recall,
    "forbidden_claims": forbidden_claims,
    "retrieval_recall": retrieval_recall,
    "citation_support": citation_support,
    "schema_conformance": schema_conformance,
    "tool_call_conformance": tool_call_conformance,
    "exact_values": exact_values,
}


def resolve(evaluator_type):
    if evaluator_type not in REGISTRY:
        raise KeyError(f"unknown evaluator type {evaluator_type!r}")
    return REGISTRY[evaluator_type]
