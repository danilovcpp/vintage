---
name: technical-specification
description: Turn approved product scope into testable detailed SRS, data and integration requirements.
---

# Detailed SRS / ТЗ

Read approved PRD and decisions; use `templates/04_DETAILED_SRS.md`. Create structured chapters for roles, user stories/use cases, domain/data, integrations, external contracts, system states, acceptance rules, and non-functional requirements. Every REQ/FR/NFR has source ID, priority, inputs, outputs, normal/error flows and verifiable acceptance. Include authorization, privacy, accessibility, data lifecycle, failure modes, migration, localization, telemetry, scale assumptions, release/operations requirements as relevant.

Review inconsistencies with business_analyst, data_architect, security_architect and qa_lead. Link requirements to `workspace/TRACEABILITY.md`; every MUST scenario needs a test approach. Do not fill unknown SLOs with invented milliseconds or 99.99% targets. Report blockers and request requirements approval.
