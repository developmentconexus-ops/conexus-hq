---
id: ADR-0002
title: Modelo operacional do Founder Boardroom
status: accepted
decided_at: 2026-07-21
owner: founder
---

# ADR-0002 — Modelo operacional do Founder Boardroom

## Contexto

A Conexus precisa de um espaço persistente para debate estratégico, um executor para mudanças em repositórios e uma memória institucional independente do modelo.

## Decisão

- O **Founder Boardroom** funcionará em um ChatGPT Project.
- O Chat será o modo padrão para diálogo, questionamento e decisões propostas.
- Work será usado sob demanda para pesquisas longas, auditorias e entregáveis.
- Codex será o executor primário de alterações em repositórios e implementação.
- Claude Code poderá atuar como executor secundário, importando as regras canônicas de `AGENTS.md` por `CLAUDE.md`.

## Consequências

- Não será criado um aplicativo próprio de Founder OS neste estágio.
- Toda decisão material aprovada será registrada no `conexus-hq`.
- Cada ferramenta terá responsabilidade explícita, reduzindo duplicação e confusão.
