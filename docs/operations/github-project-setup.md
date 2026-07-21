---
id: CONEXUS-GHPROJECT-001
title: Configuração do GitHub Project
type: operating-guide
status: active
owner: founder
created_at: 2026-07-21
last_reviewed_at: 2026-07-21
---

# Configuração do GitHub Project

## Nome

`Conexus Company OS`

## Campos

| Campo | Opções iniciais |
|---|---|
| Status | Inbox, Discovery, Ready, In Progress, Review, Done, Parked |
| Type | Objective, Initiative, Task, Opportunity, Experiment, Research, Decision, Risk |
| Area/Product | Company, MetalDocs, Marketplace, Data Intelligence, Metal Shopping, Conexus Sales, Developer Harness |
| Horizon | Now, Next, Later |
| Priority | P0, P1, P2, P3 |
| Evidence | Idea, Anecdotal, Observed, Measured, Paid |
| Effort | XS, S, M, L, XL |
| Iteration | Ciclo atual e ciclos futuros |
| Start Date | Data |
| Target Date | Data |
| Blocked | Yes, No |

## Visões

1. **00 — Founder Cockpit**: iniciativa ativa, milestone, atrasos, riscos e decisões pendentes.
2. **01 — Now**: Kanban de `Discovery → Ready → In Progress → Review → Done`, filtrado por `Horizon = Now`.
3. **02 — Portfolio**: tabela agrupada por produto.
4. **03 — Discovery**: oportunidades, pesquisas e experimentos.
5. **04 — Roadmap**: timeline somente de compromissos aprovados.
6. **05 — This Cycle**: tarefas da iteração atual.
7. **99 — Parked**: iniciativas deliberadamente fora de execução.

## Hierarquia

```text
Objective
└── Initiative
    └── Task
```

## Limites

- Uma Initiative em `In Progress`.
- Até três Tasks em `In Progress`.
- Roadmap contém compromissos; Inbox contém possibilidades.
