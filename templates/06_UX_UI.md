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

# UX/UI Blueprint & Design System Specification

## UX principles / user context
Users, environment, essential tasks, density, device form factors, brand constraints, research evidence.

## Information architecture
Navigation tree, entity hierarchy, naming, permissions-dependent routes, global search if applicable.

## User flow & journey map
Mermaid flow chart for each central JRN-ID incl. decision/validation/failure paths.

## Screen/state catalog
| SCR-ID | Persona/role | JRN/FR refs | Purpose | Primary CTA | Data/actions | Loading/empty/error/no-access/offline | Responsive behavior |
|---|---|---|---|---|---|---|---|

## Wireframe and high-fidelity handoff
For each SCR-ID: layout hierarchy; component tree; content/copy; example real-world data; interactions, navigation and keyboard interactions; visual alternatives and rationale. Link actual prototype/design file **only if it exists**.

## Design tokens
Color semantic roles (not just hex), typography, spacing scale, elevation, radii, breakpoints, dark theme where requested. Component states: default, hover, focus, active, disabled, loading, error.

## Component inventory
| CMP-ID | Component | Variants and props | Behavior/state | A11y semantics | Code ownership | Test |
|---|---|---|---|---|---|---|

## Accessibility / i18n
Contrast/keyboard/screen reader, reduced motion, localization, RTL when relevant, truncation and error strings.

## Usability validation
Top tasks, proposed usability script, completion/time/error criteria; issues and owner sign-off. Do not claim actual user tests if not performed.
