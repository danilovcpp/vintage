---
name: quality-readiness
description: Audit project documentation for contradictions, traceability and critical gaps before implementation.
---

# Cross-functional readiness gate

Use `playbooks/QUALITY_STANDARD.md` and `templates/08_READINESS.md`. Review viability, PRD, SRS, architecture, UX, plan, decision/question/risk/source logs. Commission independent_reviewer and qa_lead as read-only reviewers; security_architect for relevant threats. For each finding specify Severity, location/ID, impact, fix/mitigation and owner.

Check P0 unknowns, missing acceptance, untested NFR, contradictions, unsourced material claims, unapproved irreversible choices, resource/operational gaps and linked traceability. Assign `PASS`, `CONDITIONAL` or `FAIL`; **AI PASS does not constitute owner approval**. Conditional waivers require explicit owner acknowledgement and must not override non-negotiable safety blockers. Record required changes; no implementation if FAIL.
