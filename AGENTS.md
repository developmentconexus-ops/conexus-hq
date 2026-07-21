# Conexus HQ — Agent Operating Contract

## Purpose

This repository is the institutional source of truth for Conexus. It is not a product source-code repository.

## Required context

Before giving strategic advice or changing company documents:

1. Read `docs/INDEX.md`.
2. Read `docs/NOW.md`.
3. Read `docs/decisions/decision-log.md`.
4. Read the latest weekly review, when one exists.
5. Read the local area index and documents relevant to the request.

Do not read the entire repository by default. Use progressive disclosure and follow indexes to the smallest sufficient context set.

## Information classification

Always distinguish:

- **Fact** — directly observed or reliably established.
- **Evidence** — a source supporting a claim.
- **Hypothesis** — testable statement not yet validated.
- **Assumption** — condition temporarily accepted for planning.
- **Proposal** — recommendation not yet approved.
- **Accepted decision** — formally recorded choice.
- **Commitment** — accepted outcome with owner and timing.

Never present a hypothesis, assumption, or proposal as an accepted decision.

## Source-of-truth rules

- Chat conversations are not official records.
- Accepted material decisions require a decision record.
- Do not silently rewrite accepted decisions; supersede them with a new record.
- Do not duplicate canonical information across documents.
- Mark superseded or archived documents explicitly.
- Update indexes when creating, moving, or archiving documents.
- Update `docs/NOW.md` whenever the active objective, initiative, milestone, blocker, or commitment changes.
- Preserve links to supporting evidence whenever available.

## Change protocol

For material changes:

1. Identify the affected canonical documents.
2. State the proposed change and rationale.
3. Obtain founder approval when strategy, portfolio priority, scope, deadline, or governance changes.
4. Apply the change through a reviewable diff.
5. Update related indexes and decision records.
6. Report assumptions, unresolved contradictions, and downstream consequences.

## Writing rules

- Prefer concise Markdown with descriptive headings.
- Keep one primary subject per document.
- Start institutional documents with YAML frontmatter.
- Use ISO dates (`YYYY-MM-DD`).
- Prefer relative repository links.
- Avoid vague words such as “soon”, “later”, or “almost” without a concrete meaning.

## Security

Never commit secrets, credentials, tokens, personal customer data, raw ERP exports, confidential employee data, or unnecessary Metalnobra commercial data.
