---
id: PRODUCT-CONEXUS_SALES_INTELLIGENCE
title: Conexus Sales Intelligence
type: product-one-pager
status: discovery
owner: founder
created_at: 2026-07-21
last_reviewed_at: 2026-08-10
governance_status: bounded-experiment
---

# Conexus Sales Intelligence

## Resumo

Família de hipóteses de inteligência comercial para ajudar vendedores e gestores a transformar dados empresariais em melhores decisões e ações: complementares, substitutos, conhecimento técnico, orçamento, margem, priorização comercial e desempenho.

## Estado de governança

**Discovery.** Nenhum produto permanente foi autorizado.

Durante a imersão Mitra existe um experimento bounded aprovado: **Conexus Sales Radar — Orçamentos em Risco & Next Best Action**. Ver [`ADR-0004`](../../decisions/adr/ADR-0004-mitra-sales-radar-bounded-experiment.md).

## Problema do experimento

Uma operação comercial possui muitos orçamentos e sinais dispersos. O vendedor ou gestor pode não saber quais oportunidades merecem atenção primeiro, por que merecem atenção ou qual ação executar a seguir.

## Usuários iniciais

- vendedor que acompanha seus próprios orçamentos;
- gestor comercial que precisa priorizar oportunidades e identificar perdas evitáveis.

## Hipótese

Se o sistema combinar sinais reais como valor, idade do orçamento, histórico do cliente, disponibilidade e composição dos itens, então poderá produzir uma priorização útil de orçamentos e sugerir uma próxima ação contextual sem exigir que o usuário analise manualmente todos os dados.

## Vertical slice aprovada

Entrada mínima:

- orçamentos e itens;
- clientes;
- vendedores;
- produtos;
- estoque/disponibilidade quando disponível;
- histórico de vendas;
- preço e margem quando confiáveis e necessários.

Processamento conceitual:

`dados reais → sinais determinísticos → ranking → explicação/recomendação por IA → ação do vendedor → resultado observado`

## Princípio de evidência

- Números e fatos devem vir dos dados.
- IA pode explicar e sugerir, não inventar valores.
- Dados reais são preferidos; um extrato sanitizado de dados reais é aceitável para a imersão.
- Mock ou dado fabricado pode ser usado apenas para testar interface, nunca como evidência de que a hipótese funciona.

## Fora de escopo da imersão

- CRM completo;
- previsão de compras;
- monitoramento de concorrentes;
- automação completa de WhatsApp;
- Enterprise Brain genérico;
- recomendador completo de substitutos e complementares;
- escolha da arquitetura definitiva da Conexus.

## Evidências esperadas

1. Fluxo ponta a ponta funcional.
2. Justificativas de ranking auditáveis.
3. Backtest histórico ou piloto real.
4. Feedback de utilidade de pelo menos usuários representativos quando viável.
5. Registro de dados necessários, limitações e sinais que realmente ajudaram.

## Métrica econômica candidata

A métrica de longo prazo é **receita ou margem recuperada/incremental associada a oportunidades sugeridas pelo sistema**. Durante a imersão, indicadores intermediários são aceitáveis: relevância das prioridades, ações executadas, orçamentos reativados e capacidade de explicar corretamente os sinais.

## Relação com o Enterprise Brain

O Sales Radar pode revelar quais partes de um futuro Enterprise Brain são realmente necessárias — por exemplo, relações entre cliente, produto, orçamento, estoque e regras comerciais — sem autorizar a construção antecipada dessa infraestrutura.

## Próxima decisão

Ao final da imersão: `continue / reshape / park / stop`. A continuidade como iniciativa oficial exige decisão separada.
