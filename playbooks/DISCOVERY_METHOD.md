# Discovery methodology — consultative interview

Use **funnel questions**: what problem exists, who experiences it, current workflow, frequency/consequence, desired outcome, motivation to change, constraints, priority, evidence. Ask the user to describe a real recent incident rather than only opinions. Separate buyer, user, operator, regulator. Ask about no-product alternative and current workaround.

## Adaptive coverage

- **Problem**: pain point, recurrence, current workaround, consequences of inaction, why now.
- **People**: primary/secondary segments, buyers, roles, accessibility, power users, admin.
- **Value**: outcomes, measurable success/guardrails, business model (if applicable), distribution.
- **Workflow**: happy path, exceptions, offline/failures, approvals, human intervention, lifecycle.
- **Scope**: must-have MVP, nice-to-have, excluded; core differentiator, potential abuse.
- **Data**: origin, types, sensitivity, PII, volumes, retention, legal basis, deletion.
- **Integration**: external systems, APIs, migration, formats, change ownership, SLAs.
- **Operations**: hosting, environments, observability, backups, on-call, maintenance owner.
- **Quality**: reliability, performance, recovery, expected load, threat model, auditability.
- **Constraints**: deadline, team skill, money, tech preferences vs hard constraints.
- **Design**: devices, contexts, brand, competitors, workflows, locale, accessibility.
- **Validation**: what evidence would invalidate the idea, pilot tests, pricing tests if relevant.

## Question strategy

Mark each question P0 (blocks product direction/safety), P1 (needed for detailed spec) or P2 (may be deferred). Pose 3–5 per round ranked by information gain and irreversibility; mention that «пока не знаю» is valid. Offer a recommended default for implementation choices, but NOT for facts only the owner knows. Track Q IDs, exact answer, status and related assumptions. Every 2–3 cycles summarize scope and ask whether you understood correctly.

If requirements are self-contradictory, stop drafting and show the trade-off. Avoid interviewing endlessly: when no P0 questions remain and P1s can be bounded by explicit assumptions, offer a structured summary and ask owner to confirm stage transition. Never infer user approval from silence.
