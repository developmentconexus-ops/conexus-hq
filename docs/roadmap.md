<!-- current-status-authority -->
# Conexus HQ Roadmap

This is the sole mutable current-stage/status/allowed-work/next-action authority for Conexus HQ.

## Current state

```text
COMPANY NAME                    CONEXUS / WORKING NAME / NOT RATIFIED
PRODUCT NAME                    CONEXUS OS / WORKING NAME / NOT RATIFIED
HQ-0 REPOSITORY FOUNDATION      OPEN / ACTIVE / EXTERNAL PROTECTION BLOCKER
HQ-0 FABLE REVIEW               NOT CONVERGED / MATERIAL=2 / NON-MATERIAL=8
HQ-0 F2 VERIFIER DEFECT         CORRECTED / REGRESSION TEST GREEN
HQ-0 F1 MAIN PROTECTION         BLOCKED BY CURRENT PRIVATE-REPO PLAN CAPABILITY
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

## Current review adjudication

Independent Fable review against candidate `3a33df62ba4928ded8346ce1a98a056136a07832` returned:

```text
VERDICT                       NOT CONVERGED
MATERIAL FINDINGS             2
NON-MATERIAL FINDINGS         8
RATIFICATION RECOMMENDATION   NOT READY
```

Lead disposition:

- **F2 — case-insensitive forbidden-path false positive:** accepted as a bounded implementation defect. A regression test first reproduced the missing exact-path behavior; the verifier now performs exact-component casing checks and the aggregate `required` job passes both the regression test and full repository verification on candidate `64afb20c191262b6b647c9778a0749288b1d2001`.
- **F1 — protected-main closure condition unavailable under current hosting capability:** accepted as a material external blocker. The HQ-0 safety requirement is preserved; it is not silently weakened into a process-only substitute merely to close the gate.
- **F3–F10:** non-material; no HQ-0 correction required unless later evidence changes materiality.

## Exact next action

```text
operator selects a GitHub hosting/plan path that supports branch protection for this private repository
→ configure main to require PR-based integration and the aggregate `required` check
→ revalidate protection through GitHub repository state
→ perform bounded Fable/Lead re-adjudication of F1/F2 against the final exact candidate
→ operator ratification of HQ-0
→ separate explicit merge authorization
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
