"""Render a run report a reader can act on.

An external test ran this script against real runner output and got `unknown`
for every case: it read a `result` key that case results have never carried.
Nothing called it either, and nothing was ever written to the evidence
directory the manifest is required to declare — while the evidence policy says
a result that cannot be located is not evidence.
"""
from pathlib import Path

from redact import redact


def _rows(title, lines):
    return [f"## {title}", ""] + lines + [""] if lines else []


def render(report):
    """The report as Markdown. Redaction is idempotent, so it is safe here too."""
    report = redact(report)
    out = ["# Evaluation report", ""]

    out += [f"**Verdict: {report['status']}**", ""]
    for reason in report.get("reasons") or []:
        out.append(f"- {reason}")
    if report.get("reasons"):
        out.append("")
    for blocker in report.get("blockers") or []:
        out.append(f"- blocker: {blocker}")
    if report.get("blockers"):
        out.append("")

    gates = report.get("gates") or {}
    if gates:
        out += ["| Gate | Result |", "|---|---|"]
        out += [f"| {name} | {result} |" for name, result in gates.items()]
        out.append("")

    candidate = report.get("candidate") or {}
    if candidate:
        out += _rows("Versions", [
            f"- candidate: {candidate.get('name')} {candidate.get('version')}"
            f"{', frozen' if candidate.get('frozen') else ', NOT FROZEN'}",
            f"- dataset: {report.get('dataset_version')}",
        ] + [
            f"- evaluator: {spec.get('id')} {spec.get('version')} ({spec.get('gate', 'DoT')})"
            for spec in report.get("evaluators") or []
        ])

    coverage = report.get("coverage") or {}
    if coverage:
        out += _rows("Coverage", [f"- {key}: {value}" for key, value in coverage.items()])

    aggregates = {k: v for k, v in (report.get("aggregate_results") or {}).items() if v is not None}
    if aggregates:
        out += _rows("Aggregate results", [
            f"- {name}: {value:.4f}" for name, value in aggregates.items()
        ])

    slices = report.get("slice_results") or {}
    if slices:
        out += ["## Slice results", "", "| Slice | Population | Measured | Minimum |", "|---|--:|--:|--:|"]
        for name, result in slices.items():
            score = result.get("score")
            out.append(
                f"| {name} | {result.get('population')} "
                f"| {'—' if score is None else f'{score:.4f}'} | {result.get('minimum')} |"
            )
        out.append("")

    out += _rows("Assertion failures", [
        f"- `{entry['case_id']}` / {entry['assertion']}: {'; '.join(entry['findings'])}"
        for entry in report.get("assertion_failures") or []
    ])

    out += _rows("Vetoes triggered", [
        f"- `{entry['case_id']}`: {'; '.join(entry['findings'])}"
        for entry in report.get("vetoes") or []
    ])

    failing = [
        entry for entry in report.get("case_results") or []
        if entry.get("findings") or entry.get("status") == "error"
    ]
    out += _rows("Cases with findings", [
        f"- `{entry['case_id']}` ({entry.get('status')}): "
        f"{'; '.join(entry.get('findings') or []) or entry.get('error')}"
        for entry in failing
    ])
    if not failing and report.get("case_results"):
        out += ["## Cases with findings", "", "None. Every case passed every evaluator.", ""]

    return "\n".join(out).rstrip() + "\n"


def create(report, path):
    Path(path).write_text(render(report), encoding="utf-8")
