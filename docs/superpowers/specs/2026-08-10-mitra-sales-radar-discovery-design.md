---
id: SPEC-MITRA-SALES-RADAR-001
title: Conexus Sales Radar — Mitra Discovery Design
status: approved
type: product-discovery-design
owner: founder
approved_at: 2026-08-10
---

# Conexus Sales Radar — Mitra Discovery Design

## 1. Purpose

Use the Mitra immersion as a bounded product-discovery environment to test one vertical slice of the future Conexus commercial-intelligence vision without starting a permanent parallel product.

The experiment asks:

> Can real commercial data be converted into an auditable daily prioritization of quotations that deserve attention, with a useful next-best action for the seller?

The experiment is not intended to prove the complete Conexus vision, replace MNOS, build a CRM, or establish Mitra as the production architecture.

## 2. Why this experiment

Several candidate projects were considered:

1. **MetalDocs** — already advanced; the immersion would duplicate an existing implementation and yield limited new product learning.
2. **Marketplace Central** — already under construction and strongly dependent on marketplace-specific API work.
3. **Data Intelligence / MNOS** — strategically relevant but already an active technical stream; rebuilding it in Mitra would duplicate infrastructure work.
4. **Price tracking** — valuable, but the hardest problem is external price acquisition rather than the application layer the immersion is best suited to exercise.
5. **Purchasing forecast** — potentially high value, but requires more mature historical data treatment, lead-time modeling, rupture handling and validation than is appropriate for a bounded immersion.
6. **Generic CRM** — easy to demonstrate but weakly differentiated and prone to scope expansion.
7. **Sales Radar** — selected because it can exercise data integration, business rules, ranking, AI explanation, user action and measurable commercial outcomes in one narrow end-to-end flow.

## 3. Users

### Primary user

A seller responsible for following quotations and deciding where to spend attention.

### Secondary user

A commercial manager who needs to see where potential revenue is at risk and which opportunities deserve intervention.

## 4. User problem

Commercial operations accumulate many quotations and fragmented signals. Sellers and managers may not know:

- which quotations deserve attention today;
- which signals make an opportunity important;
- what relevant context is missing;
- what action should be taken next.

Manual review does not scale and can favor the most recent, memorable or loudest opportunities rather than the economically relevant ones.

## 5. Product hypothesis

If the system combines reliable commercial signals — such as quotation age, quotation value, customer history, item composition, availability and other trustworthy indicators — it can produce a more useful prioritization than undifferentiated manual review and can help a seller take a contextual next action.

This is a hypothesis, not an accepted fact.

## 6. Vertical slice

The minimum end-to-end experience is:

```text
real commercial data
        ↓
deterministic signals
        ↓
opportunity ranking
        ↓
ranked quotation list
        ↓
auditable explanation
        ↓
AI-assisted next-best action
        ↓
seller action
        ↓
observed outcome
```

### Minimum user flow

1. User opens the Sales Radar.
2. System shows a small ranked list of quotations that deserve attention.
3. User opens one opportunity.
4. System shows the objective signals that caused the ranking.
5. System offers a suggested next action and optional wording/support.
6. User records whether an action was taken.
7. When feasible, a later outcome is associated with the opportunity.

## 7. Data scope

Use only fields needed by the experiment.

Candidate inputs:

- quotation identifier;
- quotation creation/last-activity dates;
- quotation value;
- quotation items and quantities;
- seller identifier;
- customer identifier or anonymized stable key;
- product identifier/category;
- stock or availability when reliable;
- historical purchases or prior quotations when available;
- price and margin only when their semantics are understood and trustworthy.

### Data evidence rule

For claims that the experiment works, use either:

- a safe read-only connection to real data; or
- a sanitized extract of real historical data.

Synthetic data may support UI construction only. It must not be used as evidence that the ranking or business hypothesis is valid.

## 8. Intelligence boundary

The design deliberately separates deterministic facts from generative behavior.

### Deterministic layer

Responsible for:

- dates;
- monetary values;
- item counts;
- stock/availability;
- customer history calculations;
- business-rule flags;
- ranking inputs;
- links back to source records.

### AI layer

May:

- summarize why an opportunity matters;
- turn multiple signals into a concise explanation;
- suggest questions for the seller;
- draft a contact approach;
- explain relevant product/context information when grounded in available evidence.

The AI must not manufacture values, stock, historical behavior or ranking evidence.

## 9. Ranking strategy

The immersion does not require a predictive ML model.

Start with an interpretable rule/score or ordering based on trustworthy signals. Examples of candidate signals include:

- high quotation value;
- elapsed time without activity;
- prior customer purchases;
- product availability;
- commercial stage when reliable;
- known product/category context.

Weights or thresholds are hypotheses and must remain inspectable. A more sophisticated model is allowed only if the bounded experiment produces evidence that simple interpretable signals are insufficient.

## 10. Explanation design

Every priority shown to a user must answer:

1. **Why is this here?**
2. **Which facts support that conclusion?**
3. **What should I consider doing next?**

Example structure:

```text
Quotation: R$ 48,210
Last activity: 6 days ago
Customer history: 4 prior purchases
Availability: items available according to source data

Why prioritized:
High-value quotation with no recent activity and an established customer relationship.

Suggested next action:
Confirm whether the project timeline changed and whether the customer needs assistance finalizing item quantities or complementary items.
```

The explanation must make it possible for the seller to challenge the recommendation.

## 11. Product-complement opportunity

Complementary-item suggestions are strategically attractive but are not required for the first flow.

If time remains after the quotation-priority flow works, one limited complementary-item rule may be added as an optional extension. This must not expand into a complete recommender system during the immersion.

## 12. Historical evaluation

When historical data permits, perform a basic backtest:

1. Select a historical cutoff date `T0`.
2. Restrict the experiment to information that would have been available at `T0`.
3. Generate the ranking.
4. Inspect what happened afterward.
5. Record where the ranking was useful, misleading or impossible to evaluate.

This does not establish causality, but it provides better evidence than subjective enthusiasm alone.

## 13. Live pilot

If operationally safe and feasible, expose the ranked list to one or more representative users and record:

- whether they considered the opportunity relevant;
- whether they opened it;
- whether they took the suggested or another action;
- whether a quotation was reactivated, changed, won or lost;
- qualitative reasons for ignoring a recommendation.

No automated external communication is required for the immersion.

## 14. Metrics

### Long-term economic metric candidate

**Revenue or contribution margin recovered/incrementally generated from opportunities surfaced by the system.**

### Immersion evidence metrics

- number of ranked opportunities inspected;
- percentage judged relevant by representative users;
- actions taken after recommendation;
- quotations reactivated when measurable;
- ranking explanations with traceable supporting data;
- false or misleading recommendations and their causes;
- data gaps discovered.

No arbitrary target is invented before observing baseline data.

## 15. Failure and uncertainty handling

The application should prefer explicit uncertainty over fabricated confidence.

Examples:

- If stock is stale or unavailable, label availability as unknown.
- If margin semantics are not trustworthy, exclude margin rather than estimate it silently.
- If customer history is incomplete, disclose the limitation.
- If the ranking cannot explain why an item is prioritized, do not present the ranking as authoritative.
- If the AI response cannot be grounded in available facts, fall back to the deterministic context rather than inventing an answer.

## 16. Security and privacy

For the immersion:

- use the minimum necessary data;
- prefer stable anonymized customer keys when identity is not required;
- do not expose credentials or database secrets in prompts or project documentation;
- avoid unnecessary personal data;
- use read-only access when direct database access is used;
- do not copy production dumps into the Conexus HQ repository.

## 17. Out of scope

The following are explicitly out of scope:

- full CRM;
- complete sales pipeline replacement;
- purchasing forecast;
- competitor-price crawling;
- full substitute/complement recommendation engine;
- autonomous WhatsApp outreach;
- general-purpose Enterprise Brain;
- production-grade MNOS replacement;
- definitive Conexus data architecture;
- multi-agent orchestration platform;
- migration away from existing ERP/CRM systems.

## 18. Relation to Conexus strategy

The experiment is valuable because it exercises a representative Conexus pattern:

```text
enterprise systems
      ↓
trusted business context
      ↓
intelligence
      ↓
recommendation
      ↓
human action
      ↓
measured outcome
```

It can also reveal which knowledge relationships a future Enterprise Brain actually needs, rather than designing the entire knowledge layer in advance.

## 19. Completion criteria for the immersion

The bounded experiment is complete when the team can show:

1. one working end-to-end quotation-priority flow;
2. real or sanitized-real evidence behind the ranking;
3. auditable explanation of at least the principal ranking signals;
4. AI-generated recommendation grounded in those signals;
5. at least one retrospective evaluation or real-user evaluation when data/access permit;
6. a written list of learned constraints, missing data and false assumptions;
7. a post-immersion recommendation: `continue`, `reshape`, `park` or `stop`.

A polished general-purpose application is not required.

## 20. Governance

This design is governed by `ADR-0004`. Approval of this design authorizes the bounded discovery experiment only. It does not authorize a permanent product initiative, production rollout or broader Conexus implementation.
