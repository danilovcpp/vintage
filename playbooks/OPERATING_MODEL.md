# Engagement operating model

## Phases and hard decision boundaries

0 **Intake** — elicit idea, owner, context, goal and non-goals; build `workspace/PROJECT_BRIEF.md`.
1 **Discovery** — progressive interview and observed workflow mapping; do not prematurely commit to a specific architecture.
2 **Viability** — customer/problem evidence, market scan (if external product), competitor matrix, build/buy, technical feasibility, legal/security exposure, economic model and staged validation. Present `GO / PIVOT / NO-GO / MORE-EVIDENCE` with why, evidence grade, confidence and what would change the conclusion.
3 **Product definition** — define JTBD, personas, use cases, business rules, journey, MVP vs later, metrics, out of scope and measurable acceptance. Request scope sign-off.
4 **SRS** — complete functional & non-functional requirements; API and domain semantics, edge cases, RBAC, data, failure states, acceptance. Request requirements sign-off.
5 **Architecture** — compare solution options and their costs, context/container/component diagrams, ADRs, security and threat model, data lifecycle, integration contracts, reliability and deployment. Request architecture sign-off.
6 **UX/UI** — navigation, journey, user flows, low-fidelity then detailed UI system; accessibility; acceptance. User approves the primary flows before implementation.
7 **Delivery** — small vertical slices, dependencies, risks, QA, DoD, infrastructure, estimates with uncertainty. Request phased-plan sign-off.
8 **Readiness** — cross-functional red-team review: check traceability, conflicts, missing critical decisions, tests, NFR, evidence, realistic cost. Gate is PASS / CONDITIONAL / FAIL; CONDITIONAL needs explicit approved waivers and no severe safety blockers.
9 **Build** — only under explicit user approval, implement one named approved phase at a time, tests + review + demo evidence.

## Status vocabulary

`NOT_STARTED`, `IN_DISCOVERY`, `DRAFT`, `IN_REVIEW`, `APPROVED`, `BLOCKED`, `SUPERSEDED`. Status applies independently to artifacts. Owner approval is a human decision, not an AI quality score.

## Stage-gate checkpoint format

- Phase and document versions examined; approver identity (user/owner) and explicit approval wording.
- What was learned, quality of evidence, open P0/P1/P2 issues, risks.
- Recommendations and alternatives; trade-offs and reversible decisions.
- Suggested next phase and its expected input/output.
- Never block low-risk ideation for lack of perfect certainty; never claim implementation readiness with P0 unknowns.

## Delegation policy

Main agent owns the interview and writes to `workspace/` and `deliverables/`. Spawn specialized read-only investigations (market vs technical feasibility vs risk) in parallel, with expected output format, source requirements and stop condition. Subagents should not concurrently modify canonical files; the coordinator merges the results. Use 1–3 agents for most questions, not 16 by default. Work sequentially when tasks depend on earlier user answers.

## Efficient communication

1. At most 3–5 highest-value questions per turn (one question if the idea itself is unknown).
2. Each question: purpose + options or example answer, when helpful; do not force a user into preset alternatives.
3. After user answers: concise recap, decisions vs assumptions, contradictions, current confidence, next questions.
4. After enough information: prepare coherent proposals but show unsupported assumptions and ask for explicit approval of irreversible choices.
5. The phrase «пропускаем» closes only the optional questions and creates a transparent assumption record; it never means implicit sign-off on major costs/security choices.
