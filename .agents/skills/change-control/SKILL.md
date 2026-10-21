---
name: change-control
description: Evaluate change requests after scope or technical decisions were approved.
---

# Change control

When owner changes requirements, first classify change: clarification, additive requirement, removal, architecture reversal, urgent fix. Write `CHANGE-*` impact note: reason, alternatives, affected GOAL/JRN/FR/NFR/ADR/UI/TEST/MILESTONE, cost/time/risk range, migration and rollback, recommendation. Update only DRAFT versions until owner accepts changes; keep old decisions as `SUPERSEDED` with a link, never erase history. Re-run relevant review gates and readiness if scope materially shifts. Do not let developers silently expand the approved MVP.
