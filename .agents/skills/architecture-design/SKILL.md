---
name: architecture-design
description: Compare solution options and create architecture diagrams, ADRs, data flows and quality tradeoffs.
---

# Architecture design

Read `playbooks/ENGINEERING_STANDARD.md`, approved SRS, known NFRs. Identify architectural drivers and constraints. Show minimum 2 genuine alternatives where consequential: for example modular monolith vs services, sync vs async, build vs managed, storage choice; choose based on complexity and reversibility.

Produce C4 context/container/component where useful in Mermaid, domain boundaries, APIs/events, data ownership, security trust boundaries, deployment, error handling, operations, scaling, costs, rollback/migrations. Use `templates/05_ARCHITECTURE.md` and an ADR from `templates/ADR.md` per significant decision. Have security, data, backend and SRE specialists independently critique focused portions. Track unresolved choices; request explicit approval of key ADRs. No invented performance guarantees.
