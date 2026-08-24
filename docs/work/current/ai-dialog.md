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
