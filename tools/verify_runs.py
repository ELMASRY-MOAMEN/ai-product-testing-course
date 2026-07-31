"""Check that the figures printed in the course are still the figures it produces.

Several notes quote exact numbers — 0.960 aggregate in module 01, 0.927 and
0.917 in module 06, four assertion failures in module 03. Those numbers are
teaching material: a reader who runs the command and sees something else stops
trusting the page, and rightly.

Nothing else protects them. The datasets behind two of these runs have already
been edited twice, and the runner exits 0 whatever it concludes, so a shell
loop cannot tell a Fail from a Pass. This asserts the outcome and the figures.
"""
from pathlib import Path
import json
import shutil
import subprocess
import sys

ROOT = Path(__file__).parents[1]
RUNNER = ROOT / "lab" / "run-product-evaluation" / "scripts" / "run_evaluation.py"

# manifest -> what the course tells the reader they will see
EXPECTED = {
    "worked-examples/01-deterministic-api/manifest.yaml": {
        "status": "Fail",
        "gates": {"DoD": "Fail"},
    },
    "worked-examples/02-llm-summary/manifest.yaml": {
        "status": "Fail",
        "gates": {"DoT": "Fail"},
        "aggregate": {"required-facts-recall": 0.960},
        "slices": {"regulated": 0.958, "second-language": 0.933},
        "veto_cases": ["MR-020"],
    },
    "worked-examples/03-rag-assistant/manifest.yaml": {
        "status": "Fail",
        "gates": {"DoT": "Fail"},
    },
    "worked-examples/04-hybrid-agent/manifest.yaml": {
        "status": "Fail",
        "gates": {"DoD": "Fail", "DoT": "Pass"},
    },
    "03-the-two-gates/exercises/solutions/claimtriage-dod-manifest.yaml": {
        "status": "Fail",
        "gates": {"DoD": "Fail"},
        "assertion_failures": 4,
    },
    "06-running-it/exercises/solutions/claimtriage-manifest.yaml": {
        "status": "Fail",
        "gates": {"DoT": "Fail"},
        "aggregate": {"required-facts-recall": 0.927},
        "slices": {"high-value": 0.917},
        "veto_cases": ["CT-007"],
    },
}

TOLERANCE = 0.001


def run(manifest):
    result = subprocess.run(
        [sys.executable, str(RUNNER), manifest],
        cwd=ROOT, capture_output=True, text=True,
    )
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        raise SystemExit(f"{manifest}: runner produced no report\n{result.stderr}")


def compare(manifest, expected, report):
    problems = []

    if report.get("status") != expected["status"]:
        problems.append(f"status {report.get('status')!r}, expected {expected['status']!r}")

    for gate, value in expected.get("gates", {}).items():
        if report.get("gates", {}).get(gate) != value:
            problems.append(f"gate {gate} {report.get('gates', {}).get(gate)!r}, expected {value!r}")

    for name, value in expected.get("aggregate", {}).items():
        found = report.get("aggregate_results", {}).get(name)
        if found is None or abs(found - value) > TOLERANCE:
            problems.append(f"aggregate {name} {found}, expected ~{value}")

    for name, value in expected.get("slices", {}).items():
        found = (report.get("slice_results", {}).get(name) or {}).get("score")
        if found is None or abs(found - value) > TOLERANCE:
            problems.append(f"slice {name} {found}, expected ~{value}")

    if "assertion_failures" in expected:
        found = len(report.get("assertion_failures", []))
        if found != expected["assertion_failures"]:
            problems.append(f"{found} assertion failures, expected {expected['assertion_failures']}")

    if "veto_cases" in expected:
        found = sorted(veto.get("case_id") for veto in report.get("vetoes", []))
        if found != sorted(expected["veto_cases"]):
            problems.append(f"veto cases {found}, expected {expected['veto_cases']}")

    return problems


def main():
    failures = 0
    for manifest, expected in EXPECTED.items():
        report = run(manifest)
        problems = compare(manifest, expected, report)
        if problems:
            failures += 1
            print(f"{manifest}")
            for problem in problems:
                print(f"    {problem}")
        else:
            print(f"ok  {manifest}  ->  {expected['status']}")

    # The runner writes evidence next to each manifest; it is a run artefact.
    for directory in ROOT.rglob("evidence"):
        if directory.is_dir():
            shutil.rmtree(directory)

    if failures:
        print(f"\n{failures} run(s) no longer match what the course says they produce.")
        return 1
    print(f"\nall {len(EXPECTED)} documented runs reproduce their figures")
    return 0


if __name__ == "__main__":
    sys.exit(main())
