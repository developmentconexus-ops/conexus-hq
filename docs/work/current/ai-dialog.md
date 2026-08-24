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

Reviewer: independent Fable R2 (Claude Fable 5), 2026-08-23.

### Review-branch integrity proof

Review branch `review/hq-0-r2-fable` HEAD is `c2a6cc80fdad68782f20be6fc091f6b060ffa41a`, parented directly on exact candidate HEAD `8b833c343ed31554ee4110dae8391c2ca520228e`.

```text
git diff 8b833c3..HEAD --name-status
A	docs/work/current/ai-dialog.md
```

The review branch differs from the exact candidate only by this file. Integrity condition satisfied. All F2 executions below were performed in a clean scratch worktree checked out at exact candidate HEAD `8b833c3` (not on the review branch, whose added `docs/work/**` surface is intentionally flagged by the verifier).

PR context confirmed: PR #1 is OPEN, draft, base `main`, head `agent/bootstrap-conexus-company-os`.

### F1

```text
Finding ID: F1 — branch protection / required merge gate
R1 disposition: MATERIAL OPEN — main.protected = false, no enforcement, hosting capability blocked configuration
```

R2 evidence:

1. Legacy branch API (`GET /repos/developmentconexus-ops/conexus-hq/branches/main`) returns `protected: true` but `protection.enabled: false` with `enforcement_level: off`. As anticipated by the R2 dispatch, this legacy surface does not render ruleset state and was not treated as proof in either direction.
2. Strongest available source — effective rules for the branch (`GET /repos/developmentconexus-ops/conexus-hq/rules/branches/main`) — shows an active repository ruleset applying to `main` with rules: `deletion`, `non_fast_forward`, `pull_request` (0 required approvals; allowed merge methods merge/squash/rebase), and `required_status_checks`.
3. Ruleset detail (`GET /repos/developmentconexus-ops/conexus-hq/rulesets/21252266`, name "main protection", created 2026-08-23T18:28:17-03:00): `enforcement: "active"`, `conditions.ref_name.include: ["~DEFAULT_BRANCH"]`, `bypass_actors: []`, `current_user_can_bypass: "never"`.
4. **The configured required status check context is `validate`, not `required`:** `required_status_checks: [{"context":"validate"}]`.
5. No workflow in the candidate produces a check named `validate`. The only workflow is `.github/workflows/ci.yml`; its aggregate job and check name is `required`. `grep -ri validate .github/` on the exact candidate tree returns nothing. Check runs on candidate HEAD `8b833c3` are exactly: `required` (SUCCESS) and a `CodeRabbit` commit status. No `validate` check exists or has ever reported on this candidate.
6. PR #1 `mergeStateStatus = BLOCKED`, consistent with a required check that nothing reports (and with draft state).

```text
Current disposition: UNRESOLVED
```

Reason: HQ-0 requires that the aggregate check named `required` be an enforced merge gate. The active ruleset enforces PR-based integration, blocks force pushes and deletion, and admits no bypass actors — criteria 1, 2, and 4 of the R2 pass conditions are met. Criterion 3 fails: the ruleset's required status check references `validate`, a check that does not exist in this repository. The aggregate `required` check is therefore **not** configured as the merge gate. This is a material configuration contradiction (criterion 5 fails as well). Practical effect is fail-closed but broken: no PR can ever satisfy the `validate` requirement, so the sanctioned integration path is permanently blocked regardless of whether `required` passes — and equally, the outcome of `required` has no bearing on mergeability. The intended invariant ("main accepts ordinary integration only via PR with the aggregate `required` check succeeding") is not implemented; what is implemented is "main accepts no ordinary integration at all."

Proof / falsifier: the ruleset JSON itself is the proof (`"required_status_checks":[{"context":"validate"}]` vs. check-run inventory on `8b833c3` containing only `required`). Falsifier for the fix: after the operator edits ruleset 21252266 to require context `required` instead of `validate`, `GET /repos/developmentconexus-ops/conexus-hq/rules/branches/main` must show `{"context":"required"}` and PR #1's merge state must become gated on the actually-reporting `required` check.

Bypass assessment (required by the R2 pass conditions): `bypass_actors` is empty and `current_user_can_bypass` is `never`, so no actor — including the operator — has an ordinary bypass of the active ruleset. A repository admin can still edit or delete the ruleset itself; under GitHub's model that is deliberate privileged reconfiguration, not a silent bypass of the enforced path, and it does not count against F1. No impossible absolute protection was demanded.

Residual risk / honesty note: direct-push rejection was proven at the configuration level (active `pull_request` rule on `~DEFAULT_BRANCH` with no bypass), not by a live push probe; a probe push to `main` was deliberately not attempted because it would violate the repository's own no-direct-commit rule and, on the failure branch of the experiment, would irreversibly pollute `main`. Configuration-level evidence via the effective-rules endpoint is the strongest non-destructive source available and is accepted here.

```text
Reopen required: YES — F1 remains open until the required check context is corrected to `required` and revalidated.
```

Non-material observations recorded in passing (not new material findings): (a) allowed merge methods include merge and rebase while repository rules name squash as normal integration — process default, not a technical requirement in the HQ-0 invariant; (b) `strict_required_status_checks_policy` is false (branch up-to-date not required) — not demanded by HQ-0; (c) the candidate's roadmap still states `HQ-0 F1 MAIN PROTECTION — BLOCKED BY CURRENT PRIVATE-REPO PLAN CAPABILITY`, which is now stale relative to observed GitHub state; the roadmap's own "exact next action" sequence anticipates this and the status line must be realigned in the closure motion that finishes F1 anyway.

### F2

```text
Finding ID: F2 — case-insensitive verifier false positive (docs/INDEX.md vs docs/index.md)
R1 disposition: MATERIAL OPEN — .exists()-based forbidden-path check false-positived on case-insensitive filesystems; mandated local verification permanently failed on operator platform
```

R2 evidence (all executions on Windows NTFS — the exact defect platform class — in a clean worktree at exact candidate HEAD `8b833c3`):

1. Production correction inspected: `scripts/verify_repository.py` defines `exact_path_exists(root, relative)` which walks each path component and requires an exact-casing name match against `iterdir()` entries. The forbidden-path loop calls this helper instead of `.exists()`. The mechanism is platform-independent (string comparison of directory entries, not filesystem case semantics).
2. Regression test inspected: `scripts/test_verify_repository.py` loads the production module and asserts, in a temp directory containing only `docs/index.md`, that `exact_path_exists(root, "docs/index.md") is True` and `exact_path_exists(root, "docs/INDEX.md") is False`. On a case-insensitive filesystem the second assertion is exactly the R1 defect. Side effect noted: loading via `exec_module` also executes the full verifier against the repository root, so the test run additionally re-proves the whole verification on the candidate tree.
3. Regression test executed on candidate: PASSED, exit 0.
4. Full verifier executed on candidate: `repository verification PASSED`, exit 0 — legitimate `docs/index.md` no longer triggers the forbidden `docs/INDEX.md` finding on the operator platform (R2 checklist item 5).
5. Defect-class demonstration on this platform: with only `docs/index.md` present, naive `(root / "docs" / "INDEX.md").exists()` returns `True` (the original false positive), while `exact_path_exists` returns `False`.
6. Exact-case detection preserved (R2 checklist item 6): with a real `docs/INDEX.md` present, `exact_path_exists(root, "docs/INDEX.md")` returns `True` — a genuine legacy surface would still be rejected.
7. Mutation falsifier — does the test prove the defect class rather than implementation detail? The reviewer reverted `exact_path_exists` to a naive `.exists()` implementation in a scratch copy and re-ran the regression test. Result: the run failed (exit 1) and reproduced the original R1 symptom verbatim — `repository verification FAILED / - forbidden legacy surface present: docs/INDEX.md` — against a tree containing only legitimate `docs/index.md`. The test therefore detects recurrence of the actual defect class on the platform where it manifests.
8. CI aggregate evidence independently confirmed: workflow run `32667858457` (`required`, event pull_request) has `head_sha = 8b833c343ed31554ee4110dae8391c2ca520228e` and `conclusion: success`, executing both `python scripts/test_verify_repository.py` and `python scripts/verify_repository.py`.

```text
Current disposition: RESOLVED
```

Reason: the correction replaces filesystem-semantics existence checks with case-exact component matching; the mandated local verification now passes on the operator's case-insensitive platform; a real exact-case forbidden path is still detected; and the regression test demonstrably fails when the defective implementation is reintroduced.

Proof / falsifier: items 3–7 above. Standing falsifier for the future: any change that makes `python scripts/test_verify_repository.py` pass on Windows while `docs/INDEX.md`-style false positives recur would refute this disposition; the mutation experiment shows the current test does not permit that.

Residual risk (non-material): CI runs on `ubuntu-latest`, whose case-sensitive filesystem cannot manifest the false positive; the mutation experiment implies a reintroduced `.exists()`-based check could pass CI and would only be caught by the mandated local verification on a case-insensitive platform, where it fails loudly at first run. Detection is preserved (the control that R1 found broken is exactly the one that catches it); the gap is that CI alone does not prove this property. Recorded as a hardening opportunity, not a material finding.

```text
Reopen required: NO
```

### Scope control statement

F3–F10 were not re-reviewed. No R2 evidence encountered during the bounded verification falsifies their R1 non-material dispositions. The F1 ruleset misconfiguration is adjudicated inside F1, not as a separate finding; the roadmap staleness and CI-platform notes above are non-material observations.

```text
R2 NEW MATERIAL FINDINGS = 0
```

### R2 verdict

```text
R2 VERDICT: NOT CONVERGED
UNRESOLVED MATERIAL FINDINGS = 1
HQ-0 RATIFICATION RECOMMENDATION = NOT READY
```

```text
F1 = UNRESOLVED
F2 = RESOLVED
R2 NEW MATERIAL FINDINGS = 0
HQ-0 RATIFICATION RECOMMENDATION = NOT READY
```

```text
VERDICT: NOT CONVERGED
```

Reviewer output is Evidence, never authority. This review does not ratify HQ-0 and does not authorize merge.

