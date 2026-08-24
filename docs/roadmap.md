<!-- current-status-authority -->
# Conexus HQ Roadmap

This is the sole mutable current-stage/status/allowed-work/next-action authority for Conexus HQ.

## Current state

```text
COMPANY NAME                    CONEXUS / WORKING NAME / NOT RATIFIED
PRODUCT NAME                    CONEXUS OS / WORKING NAME / NOT RATIFIED
HQ-0 REPOSITORY FOUNDATION      CANDIDATE CONVERGED / AWAITING OPERATOR RATIFICATION
HQ-0 INDEPENDENT REVIEW         CONVERGED / NO UNRESOLVED MATERIAL FINDINGS
HQ-0 F2 VERIFIER DEFECT         RESOLVED / REGRESSION PROVEN
HQ-0 F1 MAIN PROTECTION         RESOLVED / ACTIVE RULESET / PR + required / NO BYPASS
HQ-1 COMPANY THESIS             NOT OPEN
HQ-2 CATEGORY / MARKET / ICP    NOT OPEN
HQ-3 PORTFOLIO ARCHITECTURE     NOT OPEN
HQ-4 BRAND ARCHITECTURE         NOT OPEN
HQ-5 NAMING & CLEARANCE         NOT OPEN
HQ-6 BRAND IDENTITY             NOT OPEN
HQ-7 PRODUCT DESIGN FOUNDATION  NOT OPEN
```

## Current gate — HQ-0 Repository & Authority Foundation

HQ-0 establishes the institutional repository before company thesis, naming, or visual-identity work becomes durable authority.

HQ-0 must close all of the following:

- one institutional source-of-truth role for `conexus-hq`;
- fresh-actor route aligned with Repository Standard v1.0.0;
- one mutable status authority: this roadmap;
- explicit company/product/methodology authority boundaries;
- working-name treatment for Conexus / Conexus OS;
- portfolio relationship of Conexus OS, MetalDocs, Marketplace Central, and `conexus-methodology` without semantic flattening;
- future Brain ingestion seam without implementing Brain machinery in HQ;
- research/Evidence/reviewer-output separation from authority;
- aggregate repository verification named `required`;
- protected `main` configured to require PR-based integration and the aggregate verification check;
- fresh independent review for the cross-repository authority boundary;
- explicit operator ratification and separate merge authorization.

All technical, structural, protection, and independent-review conditions are satisfied on the candidate. Operator ratification and separate merge authorization remain intentionally distinct human gates.

## Review and adjudication

The first independent Fable review found two material issues and eight non-material observations. Lead adjudication accepted both material findings:

- **F2 — case-insensitive forbidden-path false positive:** corrected with a regression test and exact-component casing checks. The defect class was reproduced and the correction was independently revalidated on the affected platform class.
- **F1 — protected-main merge gate:** the repository now has one active ruleset for the default branch requiring pull-request integration and the GitHub Actions check `required`; deletion and non-fast-forward changes are blocked; no ordinary bypass actor is configured.
- **F3–F10:** remain non-material under current evidence.

Final bounded Fable revalidation against substantive candidate `8b833c343ed31554ee4110dae8391c2ca520228e` returned:

```text
F1                              RESOLVED
F2                              RESOLVED
NEW MATERIAL FINDINGS           0
RATIFICATION RECOMMENDATION     READY
VERDICT                         CONVERGED
```

This roadmap update is Lead adjudication/status alignment only; it does not change HQ-0 architecture or authority semantics.

## Exact next action

```text
operator ratification of HQ-0
→ if ratified, record OPERATOR-RATIFIED / NOT YET INTEGRATED
→ run final aggregate `required` verification on the ratified candidate
→ separate explicit merge authorization
→ squash merge PR #1 only after that authorization
→ verify main and then open HQ-1
```

Do not open HQ-1 or ratify a company/product name while HQ-0 remains unintegrated.

## Program sequence

| Gate | Owns | Opens after |
| --- | --- | --- |
| HQ-0 — Repository & Authority Foundation | repository purpose, authority boundaries, knowledge governance, review/CI envelope | current |
| HQ-1 — Company Thesis | structural problem, vision, company thesis, non-goals | HQ-0 integrated |
| HQ-2 — Category / Market / ICP | category, market framing, initial customer, wedge hypotheses | HQ-1 |
| HQ-3 — Portfolio Architecture | platform/application relationships and portfolio rules | HQ-2 |
| HQ-4 — Brand Architecture | company/product/sub-brand relationship | HQ-3 |
| HQ-5 — Naming & Clearance | naming exploration, domain/trademark clearance, final naming decision | HQ-4 |
| HQ-6 — Brand Identity | verbal + visual identity system | HQ-5 |
| HQ-7 — Product Design Foundation | translation of brand/product principles into product design foundations | HQ-6 |

## Reopen law

Completed institutional decisions reopen only on material evidence: changed company objective, a real new consumer, proven authority conflict, legal/brand constraint, product-portfolio change, or evidence that the repository model creates duplicate/missing authority. Preference or historical sunk cost is not enough.
