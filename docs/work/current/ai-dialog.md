# HQ-0 Bounded Fable R2 Review

## Review target

Repository: `developmentconexus-ops/conexus-hq`

Candidate branch: `agent/bootstrap-conexus-company-os`

Exact candidate HEAD:

```text
8b833c343ed31554ee4110dae8391c2ca520228e
```

Review branch:

```text
review/hq-0-r2-fable
```

Before reviewing, prove that this review branch differs from the exact candidate only by this file:

```text
docs/work/current/ai-dialog.md
```

Reviewer output is Evidence only. Do not modify any other file, ratify HQ-0, or merge anything.

## Why this is a bounded R2 review

The first independent HQ-0 review returned:

```text
NOT CONVERGED
MATERIAL FINDINGS = 2
NON-MATERIAL FINDINGS = 8
```

The architecture/content findings were otherwise converged. This R2 must **not** repeat the whole architectural review and must **not** reopen F3–F10 without new material evidence.

Review only the disposition of the two prior material findings:

- `F1` — branch protection / mandatory `required` merge gate;
- `F2` — case-insensitive false positive in `scripts/verify_repository.py`.

## F2 correction to verify

The candidate now contains a regression test and a case-exact path check.

Observed Lead evidence before R2:

```text
red run:
required run 32667773723 = FAILURE
failure reason = regression test expected `exact_path_exists` but implementation did not yet provide it

green run after correction:
required run 32667803169 = SUCCESS
job 97263874543 = SUCCESS
both "Verify repository tests" and "Verify repository" = SUCCESS
```

The final candidate later moved only for HQ-0 roadmap/adjudication state and its current aggregate verification is:

```text
required run 32667858457 = SUCCESS
```

Revalidate the exact current candidate rather than trusting these observations.

### F2 question

Does the corrected implementation now avoid treating legitimate `docs/index.md` as forbidden `docs/INDEX.md` on a case-insensitive filesystem **while still detecting a genuinely distinct exact-case legacy path where the filesystem permits it**?

If yes, mark F2 `RESOLVED`.

If no, provide the smallest concrete counterexample.

## F1 state to verify

The first review found that `main` was not protected and the then-current GitHub capability returned 403 for protection/ruleset configuration.

The operator has since changed GitHub configuration.

Current Lead-observed branch response now includes:

```text
main.protected = true
```

Do **not** stop at that boolean.

### F1 proof required

Independently determine whether the effective GitHub protection/ruleset for `main` actually enforces the HQ-0 invariant:

```text
changes to main require PR-based integration
AND
aggregate status check `required` must pass before merge
```

Use the strongest GitHub evidence available in your environment, including classic branch-protection API and/or repository rulesets where applicable.

Explicitly distinguish:

```text
branch is marked protected
!=
required status check is enforced as a merge gate
```

Also report any bypass that makes the claimed invariant materially false for the repository owner/operator. Do not invent stronger governance than HQ-0 requires.

If the platform configuration genuinely enforces PR-based integration plus the `required` check, mark F1 `RESOLVED`.

If protection exists but the check is not actually mandatory, F1 remains open.

## Candidate verification

Re-run or otherwise independently inspect the candidate's aggregate verification on exact HEAD `8b833c343ed31554ee4110dae8391c2ca520228e`.

Do not treat a green workflow as proof of F1; it proves the workflow passes, not that GitHub requires it for merging.

## Output format

Write the review below this line.

For each prior material finding use exactly this structure:

```text
F1
Disposition: RESOLVED | OPEN
Evidence:
Reasoning:
Residual risk:

F2
Disposition: RESOLVED | OPEN
Evidence:
Reasoning:
Residual risk:
```

Then finish with:

```text
R2 VERDICT: CONVERGED | NOT CONVERGED
UNRESOLVED MATERIAL FINDINGS = N
HQ-0 RATIFICATION RECOMMENDATION = READY | NOT READY
```

`READY` means the independent-review material findings are resolved. It does not itself ratify HQ-0 or authorize merge.

---

## Fable R2 output

