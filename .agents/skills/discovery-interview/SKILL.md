---
name: discovery-interview
description: Run an iterative owner interview for an unformed product idea or incomplete project scope.
---

# Discovery interview

When owner says «Начни discovery», launches a blank repository, or brings a changed idea, use this skill. Do **not** infer requirements the user did not state.

Read `workspace/STATUS.md` and `playbooks/DISCOVERY_METHOD.md`. If the idea is absent, ask for it with **one** open question. Otherwise paraphrase it, label inferred points `ASSUMPTION`, and ask 3–5 top-priority questions. Prefer high-information questions about problem, users, intended outcome, constraints and go/no-go criteria. For each nontrivial question give why, candidate answers and a recommendation for controllable choices.

After every answer: write relevant text to `PROJECT_BRIEF.md`, `QUESTIONS.md`, `DECISIONS.md` only if an explicit owner decision occurred, `ASSUMPTIONS.md`, `RISKS.md`, and update `STATUS.md`. Do not manufacture owner decisions. De-duplicate answered questions. Detect contradictions and request resolution. In every 2–3 rounds summarize what has changed.

Stop when critical blockers are answered, or when only bounded assumptions remain that the owner accepts. Present a **discovery synthesis** for confirmation, not a surprise completed technical specification. Ask explicit permission before marking a stage APPROVED. When an answer is «не знаю», propose a low-cost experiment, safe default, or defer as P1/P2; do not get stuck.

Related methodology: `playbooks/OPERATING_MODEL.md`. Use templates for downstream artifacts only when the phase is reached.
