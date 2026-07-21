---
id: CONEXUS-SPEC-001
title: Conexus Company OS v0.1 — Design
status: approved
owner: founder
created_at: 2026-07-21
last_reviewed_at: 2026-07-21
---

# Conexus Company OS v0.1 — Design

## 1. Problema

O fundador possui capacidade técnica, acesso a uma empresa real e múltiplas ideias, mas distribui trabalho entre vários projetos sem completar com frequência o ciclo de entrega, uso, medição e decisão. Conversas e conhecimento também podem se dispersar entre ferramentas.

## 2. Objetivo

Criar um sistema operacional empresarial mínimo, visual e acessível por agentes que torne explícitos o conhecimento oficial, o estado atual, as decisões, o portfólio, os compromissos e os limites de trabalho em andamento.

## 3. Princípios

- Ferramentas prontas antes de software próprio.
- GitHub como memória institucional versionada.
- GitHub Projects como estado visual da execução.
- ChatGPT Project como sala de conselho.
- Codex como executor de alterações e desenvolvimento.
- Work como executor de pesquisas e auditorias longas.
- Uma fonte canônica para cada tipo de informação.
- Progressive disclosure em vez de carregar toda a wiki.
- Uma iniciativa estratégica ativa por vez.

## 4. Componentes

### Founder Boardroom

Um ChatGPT Project com memória limitada ao projeto, usado para discussão estratégica, análise adversarial, reviews e decisões propostas.

### Conexus HQ

Repositório privado de Markdown contendo visão, estratégia, mercado, portfólio, decisões, operação, templates e o estado atual.

### GitHub Project

Cockpit visual com Kanban, tabela, roadmap, discovery, riscos e trabalho estacionado. O Project representa execução; os documentos representam contexto e racional.

### Codex e Claude Code

Codex é o executor primário. `AGENTS.md` contém o contrato canônico; `CLAUDE.md` importa esse contrato e adiciona apenas instruções específicas.

### Calendar

Contém reviews, blocos reais de trabalho, reuniões e compromissos com data. Não duplica todo o backlog.

## 5. Arquitetura da informação

- `docs/INDEX.md` é o roteador global.
- Cada área possui `README.md` local.
- `docs/NOW.md` é o estado atual e deve permanecer curto.
- Documentos institucionais usam frontmatter mínimo.
- Decisões materiais usam ADRs imutáveis em significado; mudanças supersedem registros anteriores.
- Títulos e nomes de arquivo devem ser descritivos para melhorar recuperação por busca.

## 6. Protocolo de acesso dos agentes

1. Ler `AGENTS.md`.
2. Ler `docs/INDEX.md`.
3. Ler `docs/NOW.md`.
4. Ler o decision log.
5. Ler a latest weekly review, quando existir.
6. Seguir o índice local até o menor conjunto suficiente de documentos.
7. Distinguir fato, evidência, hipótese, suposição, proposta, decisão e compromisso.

## 7. Fluxo de decisão

```text
Conversa no Boardroom
→ proposta estruturada
→ aprovação do fundador
→ Codex registra diff e ADR quando necessário
→ GitHub preserva
→ GitHub Project reflete execução
→ weekly review audita coerência
```

## 8. Fluxo de produto

```text
Opportunity
→ Discovery
→ Evidence
→ Decision
→ Ready
→ In Progress
→ Review
→ Done, Parked ou Cancelled
```

## 9. Governança

Mudanças de estratégia, prioridade, escopo material, deadline ou política exigem aprovação do fundador. Agentes podem preparar, analisar e recomendar. Conversas não são registros oficiais.

## 10. Segurança

O repositório não armazenará segredos, credenciais, dados pessoais, dumps de ERP, dados brutos de funcionários ou informação comercial sensível desnecessária da Metalnobra.

## 11. Fora de escopo da v0.1

- Aplicativo próprio de Founder OS.
- Banco vetorial ou RAG próprio.
- Grafo de conhecimento.
- Orquestração multiagente customizada.
- Dashboard próprio.
- Sincronização bidirecional entre todas as ferramentas.
- Desenvolvimento de produto antes da review de portfólio.

## 12. Critérios de sucesso

A v0.1 estará operacional quando:

1. O repositório estiver versionado no GitHub.
2. `INDEX.md`, `NOW.md`, contexto do fundador, portfólio e decision log estiverem ativos.
3. O Project possuir campos e visões acordados.
4. A primeira weekly review estiver registrada.
5. A capacidade semanal estiver medida.
6. Todos os projetos estiverem classificados.
7. Uma única iniciativa de produto estiver escolhida.

## 13. Decisões intencionalmente posteriores

- Capacidade semanal e calendário.
- Primeiro wedge.
- Projeto prioritário.
- Migração para uma organização GitHub.

Essas decisões dependem de evidência e não impedem o bootstrap técnico do repositório.
