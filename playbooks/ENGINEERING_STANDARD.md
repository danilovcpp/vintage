# Engineering delivery standard

Applies **after** owner approves implementation phase. Use architecture/SRS/UX as contracts, but challenge contradictions rather than coding around them. Favor simplest adequate solution. Choose conventions suited to ecosystem; evaluate maintenance cost, licencing and vendor lock-in.

For changes affecting runtime: define implementation plan + touched files, behavior and dependencies. Deliver small vertical slices (UI/API/data/observability/testing) instead of layers that cannot be demonstrated. Add unit, integration and contract tests where meaningful; E2E for critical flows; performance/security tests for material risks. Run available relevant tests, label unrun checks.

Security baseline: secret management, input validation, authn/authz per boundary, safe error output, encryption where needed, dependency vulnerability review, least privilege, audit events, rate limits when exposed, data minimization. Check supply chain and licenses for introduced dependencies.

Operational baseline: structured logs without PII, metrics/traces and alerts where required, readiness/liveness, graceful shutdown, migration/rollback, backups and restore tests, SLOs as justified. Never claim 'production-ready' solely because a service builds.

Review: code should be readable, cohesive, testable, observable, backwards compatible where contracts demand. Identify error cases, race conditions, idempotency, timezone/localization, concurrency, pagination, accessibility. Provide measurable evidence at phase acceptance.

Keep specializations stack-agnostic until stack decisions are approved. Senior/principal backend/frontend/mobile roles can propose technology-specific conventions once approved.
