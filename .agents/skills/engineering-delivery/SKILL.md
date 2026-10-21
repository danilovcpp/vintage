---
name: engineering-delivery
description: Implement one explicitly approved development phase using senior engineering and verifiable tests.
---

# Senior engineering delivery

Only if owner explicitly authorizes development and a named phase. Read `playbooks/ENGINEERING_STANDARD.md`, selected tasks/REQs/ADRs, UX contract. Preflight dependencies and codebase, propose small plan with affected paths and tests, then implement in sequential or non-overlapping isolated workstreams. Route backend/frontend/mobile to matching principal leads; QA should challenge edge cases.

Keep implementation minimal, idiomatic and dependency-conscious. Produce tests and observability relevant to scope, run them and report results honestly. Record architecture deviations as proposed ADR updates, not silent changes. Close with what changed, mapped requirement IDs, evidence, known limitations and the next approved task. No unrelated refactors, commits/deployments or paid services without permission.
