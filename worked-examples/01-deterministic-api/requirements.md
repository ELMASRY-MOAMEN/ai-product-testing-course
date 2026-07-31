# Requirements — report API

A service that creates meeting reports on request, for authenticated and entitled callers.

## Observable behaviours

Every one of these has exactly one correct outcome, which is what puts the whole capability behind the DoD gate.

| # | Behaviour | Class | Gate |
|:--:|---|---|---|
| R1 | An empty or malformed input is rejected with the documented error code | Deterministic | DoD |
| R2 | A rejected request creates no report | Deterministic | DoD |
| R3 | A caller without the entitlement receives a refusal and no report content | Deterministic | DoD |
| R4 | An expired token is treated as unauthenticated | Deterministic | DoD |
| R5 | Every valid request returns a non-empty report identifier | Deterministic | DoD |
| R6 | Every request, accepted or refused, writes its audit event | Deterministic | DoD |

## Why there is no DoT

Nothing this service produces admits more than one correct answer. There is no generated content, no ranking, no summarisation — so there is no behaviour for which exact comparison stops being a valid oracle.

An evaluation of this capability therefore has **no threshold to approve**, and asking for one would be asking the business to set an acceptable rate of access-control failure.

## Acceptance

The DoD gate passes only when every mandatory assertion passes on every eligible case. There is no aggregate and no compensation between assertions.

R3 and R4 are veto-grade by nature: a single unauthorised disclosure is not a matter of degree. Here they are asserted rather than vetoed, which achieves the same outcome — an assertion already blocks on one occurrence.

## Out of scope

Performance objectives and retry behaviour are deterministic and would belong in this gate, but are not modelled in this example.
