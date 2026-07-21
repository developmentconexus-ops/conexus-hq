---
id: ADR-0001
title: GitHub como fonte institucional da verdade
status: accepted
decided_at: 2026-07-21
owner: founder
---

# ADR-0001 — GitHub como fonte institucional da verdade

## Contexto

Conversas com IA são úteis para raciocínio, mas não oferecem sozinhas um registro institucional explícito, versionado e portável.

## Decisão

O repositório privado `conexus-hq` será a fonte canônica para visão, estratégia, decisões, pesquisas, portfólio e estado operacional da Conexus. GitHub Projects será a fonte canônica do estado de execução.

## Consequências

- Conversas não serão tratadas como decisões oficiais.
- Mudanças materiais serão registradas em Markdown versionado.
- Agentes consultarão índices e documentos canônicos antes de aconselhar ou editar.
- Código de produto continuará em repositórios separados.
