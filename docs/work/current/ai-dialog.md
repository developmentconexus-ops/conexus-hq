# HQ-0 Independent Fable Review

## Review target

Repository: `developmentconexus-ops/conexus-hq`

Candidate branch: `agent/bootstrap-conexus-company-os`

Exact candidate HEAD:

```text
3a33df62ba4928ded8346ce1a98a056136a07832
```

Review branch: `review/hq-0-fable`

The review branch must differ from the candidate **only** by this file.

## Review authority

Apply, in order:

1. current Conexus HQ candidate authority;
2. `developmentconexus-ops/conexus-methodology/METHOD.md` v1.0.0;
3. `developmentconexus-ops/conexus-methodology/REPOSITORY-STANDARD.md` v1.0.0.

Reviewer output is Evidence, not Product/company authority. Do not silently create company strategy, Product semantics, naming decisions, or engineering rules.

## Default review pack

Read only:

```text
AGENTS.md
docs/index.md
docs/roadmap.md
docs/phases/hq-0-repository-foundation.md
docs/portfolio/map.md
```

Add `docs/decisions/index.md` or `docs/development/repository-rules.md` only when a concrete finding requires them. Do not read the old 40-file candidate or Git history by default; history is Evidence, not current authority.

## Context

HQ-0 intentionally collapses an older broad `Company OS v0.1` Draft PR into the smallest institutional repository foundation consistent with the current organizational standards.

The candidate deliberately establishes:

- `conexus-hq` as company-level institutional source of truth;
- one fresh-actor route;
- `docs/roadmap.md` as sole mutable status/next-action authority;
- explicit authority separation among HQ, `conexus-methodology`, `conexus-os`, MetalDocs, and Marketplace Central;
- `Conexus` / `Conexus OS` as working names, not ratified brand decisions;
- strategic future convergence of MetalDocs and Marketplace Central into the future platform while preserving their own Product authorities;
- HQ as authored knowledge / future Brain input seam, not a Brain runtime;
- a bounded aggregate repository verification job named `required`.

Exact candidate CI evidence at review start:

```text
workflow required / run 32653369086 = SUCCESS
job 97228274744 = SUCCESS
repository verification PASSED
```

Known unresolved infrastructure condition:

```text
main protected = false
required status checks enforcement = off
```

The candidate roadmap treats protected `main` + required aggregate check as a mandatory HQ-0 closure condition. Do not reinterpret that known gap as already closed.

## Adversarial questions

Challenge the candidate, especially for:

1. **Duplicate or missing authority** — Does HQ own anything that should remain in a Product repository or methodology? Is any company-level meaning ownerless?
2. **Status fragmentation** — Is `docs/roadmap.md` genuinely the only mutable current-status/next-action authority?
3. **Portfolio convergence boundary** — Does the MetalDocs / Marketplace Central → future platform direction preserve Product/domain authority, or does it smuggle in semantic/code fusion?
4. **Brain seam** — Is HQ correctly positioned as authored source knowledge without prematurely selecting/implementing Brain/RAG/ontology/runtime machinery?
5. **Working-name treatment** — Does recording `Conexus` and `Conexus OS` as working names avoid both premature renaming and accidental brand ratification?
6. **Repository minimality** — Is the 10-file net candidate the smallest sustainable structure, or is any file/abstraction unnecessary or missing?
7. **Fresh-actor correctness** — Can a new human/agent reach current status and exact owners within the five-file default pack without conversation archaeology?
8. **Verification quality** — Does `scripts/verify_repository.py` falsify material repository invariants rather than merely check file presence? Identify any important false-positive or false-negative class.
9. **Security/minimization** — Does the repository model avoid encouraging founder/customer/ERP/commercial data to become an unnecessary institutional-data dump?
10. **Closure integrity** — Given `main` is not protected, is the roadmap correct to keep HQ-0 OPEN? Identify any other unmet closure condition.
11. **Future evolution** — Does the design prepare additive seams for company thesis, market/ICP, portfolio, brand, naming, identity, and future Brain integration without building those future capabilities now?
12. **Global Maximum** — Is this a sustainable structure for the real company problem, or merely a cleaner local maximum inherited from the prior PR?

## Required output format

Write the independent review below this line. For every finding include:

```text
ID
Materiality: MATERIAL | NON-MATERIAL
Claim / defect
Affected authority or invariant
Evidence
Why it matters
Smallest correct correction, if any
Reopen required: YES | NO
```

Then give a final verdict:

```text
CONVERGED | NOT CONVERGED
MATERIAL FINDINGS = N
NON-MATERIAL FINDINGS = N
HQ-0 RATIFICATION RECOMMENDATION = READY | NOT READY
```

A recommendation of `READY` still does **not** override the known branch-protection closure condition or authorize merge.

---

## Fable output

_Write the independent review here._
