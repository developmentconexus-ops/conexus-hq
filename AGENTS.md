# Conexus HQ — Agent Bootstrap

## Start here

```text
AGENTS.md
→ docs/index.md
→ docs/roadmap.md
→ 1–2 task-specific owning documents
```

Default context is at most five files. Do not recursively read `docs/`, Git history, old PRs, research, or review material before a concrete task requires them.

## Organizational standards

Engineering reasoning follows `developmentconexus-ops/conexus-methodology/METHOD.md` v1.0.0. Repository organization/workflow follows `developmentconexus-ops/conexus-methodology/REPOSITORY-STANDARD.md` v1.0.0.

Current accepted authority beats historical Git content. Research, Evidence, reviewer output, conversations, and implementation are not institutional authority by existence.

## HQ authority boundary

Conexus HQ may own company-level strategy, portfolio direction, brand/naming, institutional operating decisions, and the relationship among company initiatives.

Conexus HQ must not redefine:

- Conexus OS Product semantics or architecture;
- MetalDocs Product semantics or architecture;
- Marketplace Central Product semantics or architecture;
- the DevelopmentConexus Engineering Method or Repository Standard.

A company decision may set portfolio direction without absorbing a product repository's semantic authority.

## Hard stops

- `docs/roadmap.md` is the sole mutable current-stage/status/next-action authority.
- `Conexus` and `Conexus OS` are working names, not ratified brand names.
- HQ is an authored institutional source of truth, not the future Enterprise Brain runtime. Do not add RAG, vector storage, agent memory, knowledge-runtime infrastructure, or speculative ingestion machinery merely because HQ knowledge may later feed the Brain.
- MetalDocs and Marketplace Central may converge strategically into the future platform only through explicit product/architecture work in their owning repositories; do not merge domains or code by implication.
- Unknown stays unknown. Proposals, hypotheses, research, and reviewer findings never become decisions silently.
- Never commit credentials, secrets, customer PII, raw ERP exports, confidential employee data, or unnecessary operating-company commercial data.

## Git, review, and verification

- No direct commits to `main`; normal integration is squash merge after explicit operator merge authorization.
- One coherent gate owns one Draft PR by default.
- Temporary work belongs under `docs/work/**` and must not enter the merge candidate or `main`.
- Independent Fable review uses a branch derived from the exact candidate and may differ only by `docs/work/current/ai-dialog.md`; reviewer output is Evidence, never authority.
- Run `python scripts/verify_repository.py` before claiming the candidate is repository-conformant.
- Never merge without explicit operator authorization.

Current stage and exact next action live only in [docs/roadmap.md](docs/roadmap.md).
