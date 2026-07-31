"""Shared fixtures for the runner tests.

Manifests and datasets are built per test rather than kept as files, so each
test states the exact condition it exercises instead of leaving the reader to
diff two near-identical fixtures.
"""
import json
import sys
from pathlib import Path

import pytest
import yaml

SCRIPTS = Path(__file__).parents[1] / "scripts"
ADAPTERS = Path(__file__).parents[1] / "adapters"
for path in (SCRIPTS, ADAPTERS):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))


def case(case_id, required, answer, slices, forbidden=None):
    return {
        "case_id": case_id,
        "input": {"prompt": "summarise"},
        "context": {},
        "reference": {"required_facts": required, "forbidden_claims": forbidden or []},
        "slices": slices,
        "criticality": "normal",
        "eligibility": True,
        "annotation_status": "approved",
        "mock_answer": answer,
    }


def manifest(**overrides):
    """A complete, ready manifest. Tests override the one section they exercise."""
    base = {
        "evaluation": {"id": "fixture", "version": "1.0.0", "framework": "DoT"},
        "candidate": {"name": "mock", "version": "1.0.0", "frozen": True},
        "candidate_adapter": {"type": "mock"},
        "evaluation_data": {"path": "dataset.jsonl", "version": "1.0.0", "anonymisation": "synthetic"},
        "evaluators": [
            {"id": "recall", "type": "required_facts_recall", "gate": "DoT", "version": "1.0.0"},
            {"id": "unsupported", "type": "forbidden_claims", "gate": "DoT", "version": "1.0.0"},
        ],
        "execution": {"repetitions": 1},
        "acceptance": {
            "thresholds": {"recall": 0.85},
            "critical_slices": [],
            "vetoes": [{"evaluator": "unsupported", "condition": "any_triggered"}],
        },
        "evidence": {"output_dir": "evidence"},
        "ownership": {"decision_owner": "product owner"},
    }
    base.update(overrides)
    return base


@pytest.fixture
def evaluation(tmp_path):
    """Write a manifest and dataset to disk, and return the manifest path."""
    def build(cases, **overrides):
        (tmp_path / "dataset.jsonl").write_text(
            "\n".join(json.dumps(entry) for entry in cases) + "\n", encoding="utf-8"
        )
        path = tmp_path / "manifest.yaml"
        path.write_text(yaml.safe_dump(manifest(**overrides)), encoding="utf-8")
        return path
    return build
