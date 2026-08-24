# Conexus HQ Repository Rules

This document specializes the DevelopmentConexus Engineering Method v1.0.0 and Repository Standard v1.0.0 for an institutional/company repository.

## 1. Repository purpose

`conexus-hq` preserves durable company-level knowledge and decisions so humans and agents can operate from explicit authority rather than conversation archaeology.

It is not a Product codebase, ERP mirror, personal notes archive, generic wiki, or Enterprise Brain runtime.

## 2. Authority classes

Durable HQ content must make its epistemic role clear:

```text
Authority  → accepted company meaning/decision within HQ scope
Research   → external/comparative investigation; never authority by existence
Evidence   → support/provenance for a claim; never authority by existence
Proposal   → candidate meaning awaiting decision
```

For reasoning, apply the organizational Method's `Known / Inferred / Unknown / Deferred` distinctions. Unknown never becomes a convenient fact.

A document is not made authoritative by location, length, model confidence, reviewer language, or commit age.

## 3. Ownership boundaries

HQ may decide company-level:

- thesis and strategic direction;
- market/category/ICP choices;
- portfolio relationships and priorities;
- brand architecture, naming, verbal/visual identity;
- institutional governance and operating principles.

HQ may not silently redefine Product or engineering authority. When a company decision implies Product change, HQ records the direction and the owning Product repository performs its own decision/reopen process.

## 4. Knowledge / future Brain seam

Author HQ knowledge so provenance, ownership, status, and meaning are understandable to humans and machines. Add minimal frontmatter only when it materially improves routing or future machine use.

Do **not** create a parallel ontology, vector database, RAG pipeline, ingestion framework, agent memory, or synchronization system before the future Brain has a named integration consumer and exact contract.

Future Brain ingestion should compile from current durable authority rather than turning HQ into runtime authority.

## 5. Documents and routing

Required bootstrap:

```text
README.md
AGENTS.md
docs/index.md
docs/roadmap.md
```

`docs/roadmap.md` alone carries mutable current-stage/status/next-action state. Other documents may describe stable meaning or frozen gate outcomes but must route mutable status back to the roadmap.

Create new directories/files only for a real consumer. Do not pre-create complete company, market, brand, research, or template taxonomies.

## 6. Git / review

- No direct commits to `main`.
- One coherent gate/stage per Draft PR by default.
- Normal integration is squash merge.
- No force-push/shared-history rewrite.
- Temporary work/review material is branch-only under `docs/work/**` and absent from the merge candidate.
- Cross-repository authority decisions require independent fresh challenge before ratification.
- Fable review branch must derive from the exact candidate; only `docs/work/current/ai-dialog.md` may differ.
- Reviewer output is Evidence. Lead/operator adjudication decides what changes.
- Merge requires explicit operator authorization after ratification; ratification alone is not merge authorization.

## 7. Verification

Run:

```bash
python scripts/verify_repository.py
```

The check falsifies required bootstrap presence, the 20 KiB bootstrap budget, duplicate mutable-status markers, forbidden legacy/temporary surfaces, top-level sprawl, and broken relative Markdown links.

The GitHub Actions aggregate job is named `required`. Branch protection must require PR-based changes and this aggregate check before HQ-0 can close.

## 8. Security and minimization

Do not commit secrets, credentials, tokens, personal customer data, raw ERP exports, confidential employee data, or unnecessary commercially sensitive data from an operating company. Prefer evidence summaries and sanitized fixtures when business evidence is needed.
