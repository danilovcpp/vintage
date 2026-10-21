# Quality bar and cross-discipline review

Every requirement: unique REQ/FR/NFR ID, rationale, source, priority, detailed conditions, positive/negative scenarios, measurable verification and traceability. A requirement like «fast» is invalid without measurement context; a UI state like «error» needs user-visible behavior and recovery. Differentiate acceptance criteria (product) and verification method (test).

## Gate checklist

- Problem and user backed by at least stated evidence, unsupported hypotheses explicit.
- Viability decision explains alternatives, economic sensitivity and what would change the decision.
- MVP and out-of-scope clear; contradictions resolved or documented as blocking.
- Functional behavior: state transitions, invariants, idempotency/retries, failure/compensation, user roles.
- NFR: sizing hypothesis, latency SLO/SLA if needed, availability/recovery, retention/deletion, compliance, cost envelope, security and accessibility.
- Architecture supports expected workflows; ADRs record options, cost, migration and rollback.
- UX covers keyboard, narrow widths, errors, loading, empty, offline if relevant, disabled/permission states, multi-language if needed.
- Every MUST feature has at least one positive and one edge/negative acceptance scenario; tests trace back to requirements.
- Plan accounts for testing, migrations, rollout, observability and maintenance; dependencies and critical path clear.

## Gate verdict

`PASS` only for evidence-backed coherent, actionable, testable scope with no open P0. `CONDITIONAL` if bounded P1s have mitigation/owner waiver and date; `FAIL` if contradictory, unsafe or unactionable. Critic must report findings by Severity (`BLOCKER`, `HIGH`, `MEDIUM`, `LOW`) with files/IDs and remediations. Quality score is not approval.

## Style

No filler, no invented claims, no mandatory microservices or shiny frameworks. Explicitly call out estimated vs measured, MVP vs future, reference architecture vs approved system, assumptions vs facts. Preserve links and dated decisions through revisions.
