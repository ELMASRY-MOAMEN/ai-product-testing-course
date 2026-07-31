# Every Then here is binary on a single case. None of them needs a population,
# a metric or an approved threshold, which is what makes them DoD.

@DoD @validation
Scenario: Reject an empty meeting input without creating a report
  Given the report-generation service is available
  And the authenticated caller submits an empty meeting input
  When the request is processed
  Then the service returns the documented invalid-input error code
  And no report is created
  And a rejection event is written to the audit log

@DoD @validation
Scenario: Reject a malformed meeting date
  Given the authenticated caller submits a malformed meeting date
  When the request is processed
  Then the service returns the documented invalid-input error code
  And a rejection event is written to the audit log

@DoD @access-control
Scenario: Refuse a caller without the entitlement
  Given a caller without the report-read entitlement
  When the caller requests an existing report
  Then the service returns the documented forbidden error code
  And no report content appears in the response
  And an access-denied event is written to the audit log

@DoD @access-control
Scenario: Refuse an expired token
  Given a caller presenting an expired token
  When the caller requests an existing report
  Then the service returns the documented forbidden error code
  And no report content appears in the response
  And an access-denied event is written to the audit log

@DoD @creation
Scenario: Create a report for a valid request
  Given an authenticated and entitled caller
  And a valid meeting input
  When the request is processed
  Then the response carries a non-empty report identifier
  And a creation event is written to the audit log
