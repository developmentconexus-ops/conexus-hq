# HQ-0 Final Bounded Fable Revalidation — F1 Only

## Review target

Repository: `developmentconexus-ops/conexus-hq`

Candidate branch: `agent/bootstrap-conexus-company-os`

Exact candidate HEAD:

```text
8b833c343ed31554ee4110dae8391c2ca520228e
```

Review branch:

```text
review/hq-0-f1-final-fable
```

Before reviewing, prove this review branch differs from the exact candidate only by:

```text
docs/work/current/ai-dialog.md
```

Reviewer output is Evidence only. Do not modify any other file, ratify HQ-0, or merge anything.

## Scope

This is a final **F1-only** revalidation. Do not repeat the HQ-0 architecture review. Do not reopen F2–F10 unless the current GitHub configuration produces genuinely new material evidence.

Prior bounded R2 established:

```text
F1 = UNRESOLVED
F2 = RESOLVED
R2 NEW MATERIAL FINDINGS = 0
```

F1 remained open for exactly one reason: the active GitHub ruleset required status check context `validate`, while the candidate workflow produces aggregate check `required`.

The operator has now edited the GitHub ruleset and reports that the required status check was changed from:

```text
validate
```

to:

```text
required
```

The candidate code did not change. This review exists only because the decisive evidence is external GitHub repository configuration.

## F1 invariant

Prove whether the effective GitHub configuration for `main` now enforces:

```text
main is protected
AND
ordinary changes require pull-request integration
AND
aggregate status check `required` must pass before merge
AND
force-push is blocked
AND
branch deletion is blocked
AND
no material bypass contradicts the claimed normal protected path
```

Do not accept `protected=true` alone as proof.

## Required evidence

Use the strongest available GitHub source, preferably the effective branch rules endpoint and ruleset detail used in R2.

At minimum verify:

1. effective rules apply to `main` / default branch;
2. the ruleset is active;
3. a `pull_request` rule is present;
4. `required_status_checks` now names **`required`**, not `validate`;
5. deletion and non-fast-forward protections remain present;
6. bypass actors/current-user bypass do not materially defeat the stated invariant;
7. the exact candidate still has a successful check run named `required`;
8. no `validate` requirement remains applicable to `main`.

If the effective configuration still references `validate`, multiple conflicting rulesets apply, or `required` is not an enforced merge gate, F1 remains unresolved.

## Candidate identity

Do not silently review a moved candidate. Confirm PR #1 head is still:

```text
8b833c343ed31554ee4110dae8391c2ca520228e
```

If it moved, STOP and report the mismatch instead of extrapolating.

## Output

Write the result below this line using exactly:

```text
F1
Prior disposition: UNRESOLVED
Current disposition: RESOLVED | UNRESOLVED
Evidence:
Reasoning:
Residual risk:
Reopen required: YES | NO
```

Then:

```text
NEW MATERIAL FINDINGS = N
HQ-0 RATIFICATION RECOMMENDATION = READY | NOT READY
```

Finish with exactly one:

```text
VERDICT: CONVERGED
```

or

```text
VERDICT: NOT CONVERGED
```

`CONVERGED` requires F1 resolved and zero new material findings. It does not ratify HQ-0 and does not authorize merge.

---

## Fable output

Reviewer: independent Fable final F1 revalidation (Claude Fable 5), 2026-08-23.

### Review-branch integrity proof

Review branch `review/hq-0-f1-final-fable` HEAD is `4bb2110` ("docs(review): prepare final F1 ruleset revalidation"), parented directly on exact candidate HEAD `8b833c343ed31554ee4110dae8391c2ca520228e`.

```text
git diff 8b833c3..HEAD --name-status
A	docs/work/current/ai-dialog.md
```

The review branch differs from the exact candidate only by this file. Integrity condition satisfied.

### Candidate identity proof

PR #1 (`GET` via gh): state OPEN, draft, base `main`, `headRefOid = 8b833c343ed31554ee4110dae8391c2ca520228e`. The candidate has not moved. No STOP condition.

```text
F1
Prior disposition: UNRESOLVED
```

Evidence (all queried live against GitHub on 2026-08-23, after the operator's ruleset edit of 2026-08-23T22:42:53-03:00):

1. **Effective rules for `main`** (`GET /repos/developmentconexus-ops/conexus-hq/rules/branches/main` — the merged, authoritative per-branch view): exactly four rules apply, all from repository ruleset `21252266` — `deletion`, `non_fast_forward`, `pull_request`, and `required_status_checks`.
2. **Required status check is now `required`:** `required_status_checks: [{"context":"required","integration_id":15368}]`. Integration 15368 is the GitHub Actions app, so the requirement is pinned to the check produced by the candidate's own `.github/workflows/ci.yml` aggregate job and cannot be satisfied by a same-named context from another integration.
3. **`validate` no longer appears anywhere** in the effective rules for `main`. The repository has exactly one ruleset (`GET /rulesets` returns only `21252266`, "main protection"), so no second ruleset can reintroduce a conflicting requirement.
4. **Ruleset detail** (`GET /rulesets/21252266`): `enforcement: "active"`, `conditions.ref_name.include: ["~DEFAULT_BRANCH"]` (i.e. `main`) with no excludes, `updated_at: 2026-08-23T22:42:53-03:00` — the only change since R2 is the status-check context correction, exactly as the operator reported.
5. **PR-required integration:** the `pull_request` rule is present and active (0 required approvals; merge methods merge/squash/rebase), so ordinary changes to `main` must arrive via pull request.
6. **Force-push and deletion blocked:** `non_fast_forward` and `deletion` rules remain present and active.
7. **No material bypass:** `bypass_actors: []` and `current_user_can_bypass: "never"` — no actor, including the operator, holds an ordinary bypass of the enforced path. (As adjudicated in R2: a repository admin editing or deleting the ruleset itself is deliberate privileged reconfiguration under GitHub's model, not a silent bypass, and does not defeat the invariant.)
8. **The gate is live and satisfied by the real check:** the exact candidate `8b833c3` carries check run `required` with `conclusion: success` (workflow run 32667858457), and PR #1's `mergeStateStatus` is now `CLEAN` — it was `BLOCKED` in R2 under the phantom `validate` requirement. The state transition BLOCKED → CLEAN, caused solely by the context correction, behaviorally corroborates that `required` is the check the merge gate actually evaluates.

```text
Current disposition: RESOLVED
```

Reasoning: R2 left F1 open for exactly one defect — the enforced ruleset named a status check context (`validate`) that nothing produces, so the aggregate `required` check was not the merge gate. That defect is corrected in the live configuration: the single active ruleset covering `main` now requires context `required` from the GitHub Actions integration, alongside unchanged PR-required integration, force-push blocking, deletion blocking, and an empty bypass list. Every element of the HQ-0 F1 invariant is now present in the effective configuration, and the PR merge-state transition confirms the gate binds to the check that actually reports. The R2 falsifier for the fix ("effective rules must show `{"context":"required"}` and PR #1 must become gated on the actually-reporting check") is satisfied.

Residual risk: (a) as in R2, direct-push rejection is proven at the configuration level (active `pull_request` rule, no bypass actors), not by a live push probe, which would violate the repository's own no-direct-commit rule; the effective-rules endpoint remains the strongest non-destructive source. (b) `strict_required_status_checks_policy` is false, so a stale-but-green PR branch can merge without re-running against the latest `main` — not demanded by the HQ-0 invariant; non-material. (c) The ruleset remains editable by repository admins; continued enforcement is an operational property, as with any GitHub-hosted control. (d) The candidate's roadmap text still records the pre-fix F1 blocker state; realigning it is part of the operator's HQ-0 closure motion and is not a configuration defect.

```text
Reopen required: NO
```

### Scope control statement

F2–F10 were not re-reviewed. The only configuration change since R2 is the status-check context correction inside ruleset 21252266; it produces no new evidence touching any other finding.

```text
NEW MATERIAL FINDINGS = 0
HQ-0 RATIFICATION RECOMMENDATION = READY
```

```text
F1 = RESOLVED
NEW MATERIAL FINDINGS = 0
HQ-0 RATIFICATION RECOMMENDATION = READY
```

```text
VERDICT: CONVERGED
```

`READY` and `CONVERGED` state only that no unresolved material finding remains in the bounded scope. They do not ratify HQ-0 and do not authorize merge. Reviewer output is Evidence, never authority.
