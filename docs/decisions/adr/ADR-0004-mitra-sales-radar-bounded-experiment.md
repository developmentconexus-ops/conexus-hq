---
id: ADR-0004
title: Autorizar Sales Radar como experimento bounded da imersão Mitra
status: accepted
decided_at: 2026-08-10
owner: founder
---

# ADR-0004 — Autorizar Sales Radar como experimento bounded da imersão Mitra

## Contexto

A Conexus possui várias frentes possíveis — MetalDocs, Marketplace Central, Data Intelligence/MNOS, inteligência de preços, previsão de compras, CRM e inteligência comercial. A imersão Mitra cria uma oportunidade limitada no tempo para construir e testar uma aplicação empresarial sem autorizar outro produto permanente por inércia.

## Decisão

Durante a imersão Mitra, o projeto escolhido será **Conexus Sales Radar — Orçamentos em Risco & Next Best Action**.

O experimento deverá testar se dados comerciais reais conseguem ser transformados em uma lista priorizada de orçamentos que merecem atenção, com explicação dos sinais e uma próxima ação útil para o vendedor.

Esta decisão:

- autoriza um **experimento de discovery bounded**;
- não escolhe formalmente o primeiro wedge comercial da Conexus;
- não autoriza continuidade de desenvolvimento após a imersão sem nova review;
- não transforma a Mitra na arquitetura ou plataforma definitiva do Conexus;
- não autoriza expandir o escopo para CRM completo, previsão de compras, rastreamento de concorrentes ou Enterprise Brain.

## Escopo mínimo

1. Ingerir ou conectar um subconjunto seguro de dados comerciais reais.
2. Identificar e ranquear orçamentos que merecem atenção.
3. Mostrar os sinais objetivos usados no ranking.
4. Gerar uma recomendação de próxima ação sem inventar valores ou fatos.
5. Registrar a ação do usuário e, quando possível, o resultado posterior.

## Princípio de inteligência

Fatos, valores, estoque, datas e histórico devem vir de dados determinísticos. IA pode interpretar, explicar, resumir e sugerir abordagem, mas não deve fabricar os números que fundamentam a recomendação.

## Evidência de sucesso

O experimento será considerado informativo se produzir pelo menos:

- um fluxo ponta a ponta funcional com dados reais ou extrato sanitizado de dados reais;
- uma priorização cuja justificativa possa ser auditada;
- uma avaliação retrospectiva ou piloto que permita comparar recomendações com resultados observados;
- aprendizados documentados sobre utilidade, dados necessários e limitações da abordagem.

Não é necessário provar product-market fit durante a imersão.

## Relação com ADR-0003

Esta é uma **exceção bounded e explicitamente registrada** à política de uma única iniciativa estratégica ativa, motivada por uma oportunidade externa com duração limitada. A exceção expira ao fim da imersão. O Bootstrap do Company OS continua sendo a iniciativa institucional ativa, e nenhum outro novo projeto recebe autorização por implicação.

## Próxima decisão obrigatória

Ao terminar a imersão, realizar uma review `continue / reshape / park / stop`. Somente uma nova decisão poderá promover o Sales Radar a iniciativa oficial do portfólio.
