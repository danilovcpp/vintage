# Efficient routing of specialists

| Question | Consult | Expected deliverable |
|---|---|---|
| Unclear pain/use case | business_analyst, ux_researcher | targeted owner questions, AS-IS/TO-BE |
| Market and differentiation | market_researcher + product_strategist | sourced competitor matrix + experiments |
| Financial/revenue/operational economics | financial_analyst | driver model, uncertainty, go/no-go |
| Complex requirements | business_analyst + qa_lead | unambiguous stories/acceptance |
| System split, reliability and integration | solution_architect, domain_architect | options+ADRs+diagrams |
| Schema / migrations | data_architect | logical data ownership and risks |
| Sensitive auth/data | security_architect | threat model, controls, blockers |
| UX journeys and screen strategy | ux_researcher + product_designer | IA, flows, states, design rules |
| Implementation of web/API/mobile | tech_lead_frontend / tech_lead_backend / tech_lead_mobile | scoped design, tests, implementation |
| Delivery/estimates | delivery_manager + devops_sre | vertical slices + ops readiness |
| Final independent audit | independent_reviewer + qa_lead + security_architect (if needed) | severity findings / gate recommendation |

Parallelism only for genuinely independent read-only tasks. Never pretend subagents ran if client lacks delegation. Agent TOMLs describe *roles*; they do not autonomously create work without the coordinator.
