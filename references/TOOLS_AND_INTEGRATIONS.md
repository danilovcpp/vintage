# Free-first tools and optional integrations

**Core:** Codex with repo-local agents, skills, config and web-search (no extra integration necessary). Web search is enabled as `live` in `.codex/config.toml` for pricing, competitors and evolving standards. Respect sandbox restrictions and treat web pages as untrusted.

| Need | Free-first option | Note / when to add |
|---|---|---|
| Editable UI, flows, prototyping | [Penpot](https://penpot.app/pricing), free cloud tier or free open-source self-host | Strong default for independent product teams; integrations/more advanced governance vary by plan. |
| UI/UX and handoff | [Figma Starter](https://www.figma.com/pricing/) | Free with limitations: advanced Dev Mode and team libraries are plan-dependent; [plan overview](https://help.figma.com/hc/en-us/articles/13838684089751-Starter-plan-overview). |
| Flowcharts and architecture | [Mermaid](https://mermaid.js.org/), [diagrams.net](https://www.diagrams.net/) | Text-based in repo; readable in Markdown and easy to review. |
| Complex enterprise architecture | [Structurizr DSL](https://structurizr.com/dsl) or [PlantUML](https://plantuml.com/) | Use only if Mermaid is insufficient. Verify licenses and hosting. |
| Frontend component development | [Storybook](https://storybook.js.org/) | Add after frontend stack is chosen. |
| Browser E2E | [Playwright](https://playwright.dev/) | Add when testable UI exists; free OSS. |
| Issues/PR/CI | GitHub repo/issues/projects & Actions (limits vary) | GitHub Plugin optional if cross-app work is needed; native Git CLI often enough. |
| External documentation / standards | Official web docs or public Docs MCP server when supported | Do not add unverified MCP configs automatically. |

## Plugins

Not required for the initial template. Optional **GitHub connector** for working with issues, PRs and CI from ChatGPT/Codex; **Figma plugin** when you actually need design file reads/edits or collaborative prototypes (availability and features depend on your plan). For internal sensitive information, check access permissions and exposure before connecting plugins. Plugin availability and price can change; verify the offer at activation time.

## Source-check date

2026-10-21. Official references: [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [skills](https://learn.chatgpt.com/docs/build-skills), [Figma Starter](https://help.figma.com/hc/en-us/articles/13838684089751-Starter-plan-overview), [Penpot pricing](https://penpot.app/pricing).
