class MockAdapter:
    """Replays a scripted answer, so a run exercises the pipeline, not a model.

    A retrieval-backed candidate returns more than an answer: which sources it
    retrieved, and which it cited. Those are separate observations — a citation
    to a source that was never retrieved is a different defect from failing to
    retrieve the right one — so they are carried separately.
    """

    def invoke(self, case):
        # `mock_output` carries whatever the domain needs — premium, rating
        # table, decision reference, anything. The named keys below are the
        # vocabulary the bundled examples happen to use; they are not the set
        # of fields a candidate may return, and a new domain should use
        # `mock_output` rather than bending one of them out of shape.
        output = {
            "answer": case.get("mock_answer", ""),
            "retrieved": case.get("mock_retrieved", []),
            "cited": case.get("mock_cited", []),
            "tool_call": case.get("mock_tool_call"),
            "ticket_reference": case.get("mock_ticket_reference"),
            "report_id": case.get("mock_report_id"),
            "error_code": case.get("mock_error_code"),
        }
        output.update(case.get("mock_output") or {})

        return {
            "case_id": case["case_id"],
            "status": "completed",
            "candidate_output": output,
            "latency_ms": 0,
            "tool_calls": [case["mock_tool_call"]] if case.get("mock_tool_call") else [],
            "source_references": case.get("mock_retrieved", []),
            "trace_reference": None,
            "error": None,
        }
