# HQ-0 — Repository & Authority Foundation

> **Scope owner:** Conexus HQ institutional repository foundation.  
> **Current status:** owned only by [../roadmap.md](../roadmap.md).

## Problem

The company needs durable institutional knowledge before its future Brain exists, but the repository must not become a second Product authority, a speculative Brain implementation, or a collection of chat-derived notes with unclear status.

An older Draft PR #1 attempted a broad `Company OS v0.1` bootstrap. It contains useful intent but predates the current DevelopmentConexus Repository Standard and mixes status surfaces, company strategy, experiments, templates, portfolio pages, reviewer/spec material, and operational process in one 40-file candidate.

## Target invariant

> A fresh human or agent can identify current institutional status, the exact owning authority, the relationship to Product repositories, and the smallest relevant context without reconstructing conversation history or mistaking research/proposals for decisions.

## Accepted design

HQ-0 uses the same organizational operating envelope as the Product repositories, specialized for company knowledge:

```text
README.md          landing only
AGENTS.md          bootstrap only
docs/index.md      task/intention router only
docs/roadmap.md    sole mutable status/next-action authority
```

Durable current owners added by HQ-0 are deliberately small:

```text
docs/decisions/index.md
docs/portfolio/map.md
docs/development/repository-rules.md
docs/phases/hq-0-repository-foundation.md
```

No company-thesis, market, brand, naming, research, template, weekly-review, or Brain-runtime taxonomy is pre-created before its owning gate/consumer exists.

## Authority boundary

```text
HQ                  company / portfolio / brand authority
conexus-methodology engineering method + repository standard
conexus-os          platform Product authority
MetalDocs           controlled-document Product authority
marketplace-central marketplace Product authority
```

Portfolio direction may require later Product work; it does not rewrite Product semantics inside HQ.

## Working-name law

`Conexus` and `Conexus OS` remain engineering/working names. HQ-0 records that uncertainty rather than triggering repository/domain renames before brand architecture and naming clearance are deliberately executed.

## Future Brain seam

HQ is the authored company source of truth from which future Brain knowledge may be compiled or published. HQ-0 prepares that seam by keeping knowledge explicit, routed, provenance-friendly, and non-duplicated. It does not select or implement RAG, vector storage, ontologies, embeddings, ingestion infrastructure, or agent memory.

## Legacy-candidate adjudication

From Draft PR #1, HQ-0 preserves concepts that still survive current reasoning:

- institutional source-of-truth intent;
- explicit epistemic separation;
- progressive disclosure for agents/humans;
- decision provenance;
- security/minimization guardrails.

The old structure itself is not preserved. `docs/INDEX.md`, `docs/NOW.md`, `docs/operations/roadmap.md`, `docs/superpowers/**`, generic templates, Mitra experiment state, premature product one-pagers, and broad operating taxonomy are removed from the HQ-0 candidate. Git history remains the evidence/archive.

## Verification / falsification

HQ-0 is not closed merely because Markdown exists. The candidate must prove:

- required bootstrap exists;
- bootstrap total is at most 20 KiB;
- exactly one current-status marker exists and belongs to `docs/roadmap.md`;
- no forbidden legacy status surfaces or `docs/superpowers/**` / `docs/work/**` survive the merge candidate;
- relative Markdown links resolve;
- GitHub aggregate `required` passes;
- `main` is protected for PR-based change and requires the aggregate check;
- independent fresh review finds no unresolved material authority/coherence defect.

## Out of scope

HQ-0 does not ratify:

```text
company thesis
category / ICP
permanent product wedge
portfolio prioritization
brand architecture
company/product naming
logo / palette / typography
pricing / business model
technical Enterprise Brain architecture
migration of MetalDocs or Marketplace Central into Conexus OS
```

## Reopen triggers

Reopen HQ-0 only if real use proves the repository model creates duplicate/missing authority, cannot route institutional knowledge within the five-file default context, conflicts materially with the organizational Method/Repository Standard, or blocks a named future Brain consumer without a safe additive seam.
