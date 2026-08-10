---
id: SPEC-MITRA-SALES-RADAR-001
title: Conexus Sales Radar — Design de Discovery na Mitra
status: proposed
type: product-discovery-design
owner: founder
proposed_at: 2026-08-10
---

# Conexus Sales Radar — Design de Discovery na Mitra

## 1. Propósito

Usar a imersão Mitra como um ambiente bounded de product discovery para testar uma vertical slice da futura visão de inteligência comercial da Conexus sem iniciar, por inércia, outro produto permanente em paralelo.

O experimento responde à pergunta:

> Dados comerciais reais podem ser transformados em uma priorização diária e auditável de orçamentos que merecem atenção, acompanhada de uma próxima melhor ação útil para o vendedor?

O experimento não pretende provar toda a visão da Conexus, substituir o MNOS, construir um CRM nem definir a Mitra como arquitetura de produção.

## 2. Por que este experimento

Foram considerados vários projetos candidatos:

1. **MetalDocs** — já está avançado; a imersão duplicaria uma implementação existente e geraria pouco aprendizado novo de produto.
2. **Marketplace Central** — já está em construção e depende fortemente de integrações específicas com APIs de marketplaces.
3. **Data Intelligence / MNOS** — é estrategicamente relevante, mas já constitui uma frente técnica existente; reconstruí-lo na Mitra duplicaria trabalho de infraestrutura.
4. **Rastreamento de preços** — possui valor, porém o problema mais difícil está na aquisição externa dos preços, e não na camada de aplicação em que a imersão gera maior aprendizado.
5. **Previsão de compras** — pode ter alto valor, mas exige tratamento mais maduro de histórico, lead time, ruptura, sazonalidade e validação do que cabe em uma imersão bounded.
6. **CRM genérico** — é simples de demonstrar, porém pouco diferenciado e propenso a expansão de escopo.
7. **Sales Radar** — escolhido por conseguir exercitar integração de dados, regras de negócio, ranking, explicação por IA, ação do usuário e resultado comercial mensurável em um único fluxo estreito ponta a ponta.

## 3. Usuários

### Usuário primário

Vendedor responsável por acompanhar seus orçamentos e decidir onde investir atenção.

### Usuário secundário

Gestor comercial que precisa enxergar onde há receita potencial em risco e quais oportunidades merecem intervenção.

## 4. Problema do usuário

Operações comerciais acumulam muitos orçamentos e sinais fragmentados. Vendedores e gestores podem não saber:

- quais orçamentos merecem atenção hoje;
- quais sinais tornam uma oportunidade importante;
- qual contexto relevante está faltando;
- qual ação deveria ser tomada em seguida.

A revisão manual não escala e pode favorecer as oportunidades mais recentes, memoráveis ou urgentes em aparência, em vez das economicamente relevantes.

## 5. Hipótese de produto

Se o sistema combinar sinais comerciais confiáveis — como idade do orçamento, valor, histórico do cliente, composição dos itens, disponibilidade e outros indicadores compreendidos — poderá produzir uma priorização mais útil do que uma revisão manual indiferenciada e ajudar o vendedor a tomar uma próxima ação contextual.

Isso permanece uma hipótese, não um fato aceito.

## 6. Vertical slice

A experiência mínima ponta a ponta é:

```text
dados comerciais reais
        ↓
sinais determinísticos
        ↓
ranking de oportunidades
        ↓
lista priorizada de orçamentos
        ↓
explicação auditável
        ↓
next-best action assistida por IA
        ↓
ação do vendedor
        ↓
resultado observado
```

### Fluxo mínimo do usuário

1. O usuário abre o Sales Radar.
2. O sistema exibe uma lista pequena e ranqueada de orçamentos que merecem atenção.
3. O usuário abre uma oportunidade.
4. O sistema mostra os sinais objetivos responsáveis pela priorização.
5. O sistema oferece uma próxima ação sugerida e, opcionalmente, apoio de comunicação.
6. O usuário registra se realizou uma ação.
7. Quando viável, um resultado posterior é associado à oportunidade.

## 7. Escopo de dados

Usar apenas os campos necessários ao experimento.

Entradas candidatas:

- identificador do orçamento;
- datas de criação e/ou última atividade;
- valor do orçamento;
- itens e quantidades;
- identificador do vendedor;
- identificador do cliente ou chave estável anonimizada;
- identificador e categoria do produto;
- estoque ou disponibilidade quando confiáveis;
- compras ou orçamentos históricos quando disponíveis;
- preço e margem somente quando suas semânticas estiverem compreendidas e forem confiáveis.

### Regra de evidência dos dados

Para afirmar que o experimento funciona, usar uma destas alternativas:

- conexão segura e somente leitura com dados reais; ou
- extrato sanitizado de dados históricos reais.

Dados sintéticos podem ser usados para construir e testar interface, mas não podem servir como evidência de que o ranking ou a hipótese de negócio funcionam.

## 8. Fronteira da inteligência

O design separa deliberadamente fatos determinísticos de comportamento generativo.

### Camada determinística

Responsável por:

- datas;
- valores monetários;
- quantidades;
- estoque e disponibilidade;
- cálculos sobre histórico do cliente;
- flags de regras de negócio;
- sinais usados no ranking;
- referência aos registros de origem.

### Camada de IA

Pode:

- resumir por que uma oportunidade merece atenção;
- transformar múltiplos sinais em uma explicação concisa;
- sugerir perguntas para o vendedor;
- sugerir abordagem de contato;
- explicar contexto comercial ou de produto quando fundamentado nas evidências disponíveis.

A IA não deve fabricar valores, estoque, comportamento histórico ou evidência de ranking.

## 9. Estratégia de ranking

A imersão não exige um modelo preditivo de machine learning.

Começar com regras, score ou ordenação interpretável baseados em sinais confiáveis. Sinais candidatos incluem:

- alto valor do orçamento;
- tempo decorrido sem atividade;
- compras anteriores do cliente;
- disponibilidade de produto;
- estágio comercial quando confiável;
- contexto conhecido de produto ou categoria.

Pesos e thresholds são hipóteses e precisam permanecer inspecionáveis. Um modelo mais sofisticado só deve ser considerado se o experimento bounded produzir evidência de que sinais simples e interpretáveis são insuficientes.

## 10. Design da explicação

Toda prioridade exibida ao usuário precisa responder:

1. **Por que isto está aqui?**
2. **Quais fatos sustentam essa conclusão?**
3. **O que devo considerar fazer em seguida?**

Exemplo:

```text
Orçamento: R$ 48.210
Última atividade: há 6 dias
Histórico do cliente: 4 compras anteriores
Disponibilidade: itens disponíveis segundo a fonte consultada

Por que foi priorizado:
Orçamento de alto valor, sem atividade recente, de cliente com relacionamento anterior.

Próxima ação sugerida:
Confirmar se o cronograma da obra mudou e se o cliente precisa de apoio para fechar quantidades ou itens complementares.
```

A explicação deve permitir que o vendedor conteste a recomendação.

## 11. Oportunidade de produtos complementares

Sugestões de itens complementares são estrategicamente atraentes, mas não são requisito do primeiro fluxo.

Se houver tempo após o fluxo de priorização de orçamentos funcionar, uma única regra limitada de complementaridade pode ser adicionada como extensão opcional. Isso não deve evoluir para um recomendador completo durante a imersão.

## 12. Avaliação histórica

Quando os dados históricos permitirem, executar um backtest simples:

1. Selecionar uma data histórica de corte `T0`.
2. Restringir o experimento às informações que estariam disponíveis em `T0`.
3. Gerar o ranking.
4. Inspecionar o que aconteceu depois.
5. Registrar onde o ranking foi útil, enganoso ou impossível de avaliar.

Isso não estabelece causalidade, mas produz evidência melhor do que entusiasmo subjetivo isolado.

## 13. Piloto real

Se for operacionalmente seguro e viável, mostrar a lista priorizada a um ou mais usuários representativos e registrar:

- se consideraram a oportunidade relevante;
- se abriram a oportunidade;
- se executaram a ação sugerida ou outra ação;
- se o orçamento foi reativado, alterado, ganho ou perdido;
- razões qualitativas para ignorar uma recomendação.

Nenhuma comunicação externa automatizada é necessária para a imersão.

## 14. Métricas

### Métrica econômica candidata de longo prazo

**Receita ou margem de contribuição recuperada/incremental associada às oportunidades encontradas pelo sistema.**

### Métricas de evidência para a imersão

- quantidade de oportunidades ranqueadas e inspecionadas;
- percentual considerado relevante por usuários representativos;
- ações executadas após recomendação;
- orçamentos reativados quando mensurável;
- explicações de ranking com dados de suporte rastreáveis;
- recomendações falsas ou enganosas e suas causas;
- lacunas de dados descobertas.

Nenhuma meta numérica arbitrária deve ser inventada antes de observar o baseline real.

## 15. Tratamento de falhas e incerteza

A aplicação deve preferir incerteza explícita a confiança fabricada.

Exemplos:

- se o estoque estiver desatualizado ou indisponível, marcar disponibilidade como desconhecida;
- se a semântica de margem não for confiável, excluir margem em vez de estimá-la silenciosamente;
- se o histórico do cliente estiver incompleto, expor a limitação;
- se o ranking não conseguir explicar por que um item foi priorizado, não apresentá-lo como autoridade;
- se a resposta de IA não puder ser fundamentada nos fatos disponíveis, retornar o contexto determinístico em vez de inventar uma resposta.

## 16. Segurança e privacidade

Durante a imersão:

- usar o mínimo necessário de dados;
- preferir chaves estáveis anonimizadas de cliente quando identidade não for necessária;
- não expor credenciais ou segredos de banco em prompts ou documentação;
- evitar dados pessoais desnecessários;
- usar acesso somente leitura quando houver conexão direta ao banco;
- não copiar dumps de produção para o repositório `conexus-hq`.

## 17. Fora de escopo

Estão explicitamente fora de escopo:

- CRM completo;
- substituição completa do pipeline comercial;
- previsão de compras;
- crawling de preços de concorrentes;
- recomendador completo de substitutos e complementares;
- outreach autônomo por WhatsApp;
- Enterprise Brain de propósito geral;
- substituição do MNOS em produção;
- arquitetura definitiva de dados da Conexus;
- plataforma própria de orquestração multiagente;
- migração para fora dos sistemas ERP/CRM existentes.

## 18. Relação com a estratégia da Conexus

O experimento é valioso porque exercita um padrão representativo da Conexus:

```text
sistemas empresariais
      ↓
contexto de negócio confiável
      ↓
inteligência
      ↓
recomendação
      ↓
ação humana
      ↓
resultado medido
```

Ele também pode revelar quais relações de conhecimento um futuro Enterprise Brain realmente precisa, em vez de desenhar toda a camada de conhecimento antecipadamente.

## 19. Critérios de conclusão da imersão

O experimento bounded estará completo quando for possível demonstrar:

1. um fluxo ponta a ponta funcional de priorização de orçamentos;
2. evidência real ou sanitizada-real por trás do ranking;
3. explicação auditável dos principais sinais usados;
4. recomendação gerada por IA fundamentada nesses sinais;
5. ao menos uma avaliação retrospectiva ou avaliação com usuário real quando dados e acesso permitirem;
6. lista escrita de restrições aprendidas, dados faltantes e hipóteses incorretas;
7. recomendação pós-imersão: `continue`, `reshape`, `park` ou `stop`.

Uma aplicação genérica e polida não é necessária.

## 20. Governança

Este design é governado pelo `ADR-0004`. A escolha do experimento foi aprovada; este documento permanece `proposed` até revisão explícita do design escrito. Após essa revisão, poderá ser promovido a `approved` e somente então seguirá para plano de implementação.
