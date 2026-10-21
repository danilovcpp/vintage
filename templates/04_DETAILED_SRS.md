> TEMPLATE ONLY · NOT A PROJECT DOCUMENT
>
> При создании в `deliverables/` удалите это предупреждение и заполните метаданные.
> Не подменяйте `UNKNOWN` догадкой. `APPROVED` возможен только после явного согласия владельца.

- **Project:** TBD
- **Version:** 0.1
- **Status:** DRAFT
- **Author:** Codex (prepared for owner review)
- **Reviewed/approved by:** NOT APPROVED
- **Date:** YYYY-MM-DD
- **Sources:** `workspace/SOURCES.md`, `workspace/DECISIONS.md`

# Software Requirements Specification / Подробное ТЗ

## 1. Scope and normative language
MUST = обязательное; SHOULD = желательное; MAY = опциональное. Ссылка на APPROVED PRD/version, glossary and decisions.

## 2. Actors / permissions
| ROLE-ID | Auth context | Allowed actions | Denied actions | Resource ownership boundary | Audit needed |
|---|---|---|---|---|---|

## 3. Functional requirements
Каждому FR выделяйте полноценную карточку:

### FR-001 — [описание]
- Source: GOAL / JRN / DEC / owner statement
- Priority: MUST / SHOULD / MAY
- Actor and preconditions:
- Inputs + validation rules:
- Main flow numbered steps:
- Alternatives / invalid states / failures:
- Outputs, state transitions, business invariants:
- Permission matrix / security:
- Audit + telemetry + data retention if relevant:
- Acceptance (Gherkin examples, success AND negative):
- Test references: TEST-ID
- Unresolved assumptions: ASM-ID / none

## 4. Data requirements
Entities/attributes, types, constraints, ownership, taxonomy, PII, lifecycle, migration, export/delete, consistency, search/filters/pagination if needed.

## 5. Integration requirements
| INT-ID | System | Direction | Protocol (proposed/approved) | Schema/version | Auth | Rate/retry/idempotency/timeouts | Failure/degradation | Source |
|---|---|---|---|---|---|---|---|---|

## 6. NFR (measurable, conditional on evidence)
| NFR-ID | Domain | Required behavior | Measurement | Target + load/conditions | Evidence or assumption | Test |
|---|---|---|---|---|---|---|
Categories: performance, availability, RPO/RTO, resilience, security/privacy, scale, observability, supportability, accessibility, localization, portability, maintainability, backup/restore.

## 7. Operational + deployment acceptance
Environments, secrets, rollout/rollback, license checks, support ownership, runbooks, acceptance test data.

## 8. Requirements traceability and open questions
Links to `workspace/TRACEABILITY.md`, P0 blockers and risks. Request explicit owner approval.
