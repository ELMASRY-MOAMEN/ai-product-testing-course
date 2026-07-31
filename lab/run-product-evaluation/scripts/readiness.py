"""Decide whether an evaluation may run at all.

Structural validity is not readiness. A manifest can declare every section
and still leave the threshold as a placeholder, and running it would produce
a number that looks like evidence without any approved criterion behind it.
"""
import re

import evaluators

PLACEHOLDER = re.compile(r"^<.*>$")


def is_placeholder(value):
    return isinstance(value, str) and bool(PLACEHOLDER.match(value.strip()))


def unresolved(value, path=""):
    """Yield the dotted path of every placeholder or empty required value."""
    if is_placeholder(value):
        yield path
    elif isinstance(value, dict):
        for key, item in value.items():
            yield from unresolved(item, f"{path}.{key}" if path else key)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from unresolved(item, f"{path}[{index}]")


def blockers(manifest):
    """Return the reasons this manifest may not run, in reporting order."""
    found = []

    for dotted in unresolved(manifest):
        found.append(f"unresolved placeholder: {dotted}")

    declared_evaluators = manifest.get("evaluators") or []
    if not declared_evaluators:
        found.append("no evaluator declared")

    # An unimplemented evaluator type must block before the run, not raise
    # part-way through it. A manifest naming a type the registry does not have
    # promises a measurement nothing can make.
    for spec in declared_evaluators:
        kind = spec.get("type")
        if kind not in evaluators.REGISTRY:
            available = ", ".join(sorted(evaluators.REGISTRY))
            found.append(
                f"evaluator {spec.get('id', '?')!r} declares unknown type {kind!r}; available: {available}"
            )

    acceptance = manifest.get("acceptance") or {}

    # Only a measurement needs a threshold. An evaluation made entirely of DoD
    # assertions has nothing to average, so demanding an approved threshold
    # there would block a correctly specified deterministic run.
    measuring = [spec for spec in declared_evaluators if spec.get("gate", "DoT") == "DoT"]
    if measuring and not acceptance.get("thresholds"):
        found.append("no approved threshold declared")

    for slice_spec in acceptance.get("critical_slices") or []:
        if slice_spec.get("minimum") is None:
            found.append(f"critical slice {slice_spec.get('name', '?')} has no approved minimum")

    declared = {evaluator.get("id") for evaluator in manifest.get("evaluators") or []}
    for evaluator_id in (acceptance.get("thresholds") or {}):
        if evaluator_id not in declared:
            found.append(f"threshold names undeclared evaluator {evaluator_id!r}")

    # A veto naming an evaluator nobody declared is the canonical "control
    # declared but not applied": the manifest promises a blocking condition
    # that no case can ever be scored against, and the report reads as though
    # the control had held.
    for veto in acceptance.get("vetoes") or []:
        evaluator_id = veto.get("evaluator")
        if evaluator_id not in declared:
            found.append(f"veto names undeclared evaluator {evaluator_id!r}")

    for slice_spec in acceptance.get("critical_slices") or []:
        evaluator_id = slice_spec.get("evaluator")
        if evaluator_id is not None and evaluator_id not in declared:
            found.append(
                f"critical slice {slice_spec.get('name', '?')!r} names undeclared evaluator {evaluator_id!r}"
            )

    data = manifest.get("evaluation_data") or {}
    if not data.get("anonymisation"):
        found.append("evaluation data declares no anonymisation status")

    ownership = manifest.get("ownership") or {}
    if not ownership.get("decision_owner"):
        found.append("no decision owner named")

    candidate = manifest.get("candidate") or {}
    if not candidate.get("frozen", False):
        found.append("candidate is not frozen for the run")

    return found
