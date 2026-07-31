---
type: reference
status: reviewed
audience: [qa, engineering]
---

# Minimum execution manifest

The manifest is the contract between the approved evaluation design and the execution runner.

```yaml
scenario_suite: <name and version>
user_story: <ID and version>
output_nature: deterministic | probabilistic | hybrid
validation_framework: DoD | DoT | Hybrid

candidate:
  code_version: <version>
  model_version: <version or N/A>
  prompt_version: <version or N/A>
  tool_configuration_version: <version or N/A>

evaluation_data:
  dataset: <name and version>
  anonymisation_status: <status>
  eligible_cases: <count and rule>

evaluator:
  name: <name>
  version: <version>
  rubric_or_formula: <reference>

execution:
  environment: <controlled environment>
  repetitions: <count>
  parameters: <temperature, seed or N/A>

acceptance:
  thresholds: <approved references>
  critical_slices: <list>
  vetoes: <list>

evidence:
  outputs: <location>
  report: <location>
  logs: <location>

decision:
  verdict: pass | fail | not_ready
  owner: <authorized owner>
  residual_risks: <list>
```

No credential, tenant identifier, client identifier, secret name or subscription key belongs in the manifest.

> **Takeaway:** If the manifest is incomplete, the agent must stop with **Not Ready** instead of guessing.

---

Previous: [End-to-end methodology](end-to-end-methodology.md) · [Course map](../00-orientation/progression.md) · Next: [What the automated evaluation runner should produce](reporting-and-evidence.md)
