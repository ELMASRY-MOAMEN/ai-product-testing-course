# The point of a Hybrid capability is that these scenarios cannot be merged.
# A DoD Then is binary on one case. A DoT Then is measurable over a
# population. Writing them in one scenario forces one of the two to be wrong.

@DoD @tool-call
Scenario: Never take an action the employee did not request
  Given the employee asks a policy question and states no request
  When the agent answers
  Then no ticket is created
  And no tool call is made

@DoD @tool-call
Scenario: Raise the requested ticket with the approved routing
  Given the employee asks for a ticket about a payroll problem
  When the agent handles the request
  Then a ticket is created with category "payroll" and priority "high"
  And the response carries the ticket reference

@DoD @schema
Scenario: Every ticket response carries a reference
  Given the agent has created a ticket
  When the response is returned
  Then the response contains a non-empty ticket reference

@DoT @batch-evaluation
Scenario: Answers preserve the facts the policy requires
  Given approved dataset version <dataset_version>
  And candidate <candidate_version> is frozen for the run
  And evaluator <evaluator_version> is frozen for the run
  When the candidate answers every eligible case
  And the evaluator measures required-fact recall
  Then the aggregate result meets its approved threshold
  And the ticket-action slice meets its approved minimum
  And no unsupported-claim veto is triggered
  And the report records case results, aggregates, failures and versions

@Hybrid @acceptance
Scenario: Acceptance requires both gates
  Given the DoD gate result and the DoT gate result
  When acceptance is decided
  Then acceptance is granted only when both gates pass
  And a passing DoT result does not compensate a failing DoD assertion
