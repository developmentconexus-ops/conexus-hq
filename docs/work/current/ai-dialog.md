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

Reviewer: Claude Fable 5 (independent adversarial review).
Review branch verified: `review/hq-0-fable` at `b6553e54432ef158d77ebb7bf862d23012f15328` = candidate `3a33df62ba4928ded8346ce1a98a056136a07832` + exactly one commit touching only `docs/work/current/ai-dialog.md` (confirmed via `git diff --stat 3a33df6..HEAD`).

Method: default review pack read first, then `docs/decisions/index.md`, `docs/development/repository-rules.md`, `README.md`, `.github/workflows/ci.yml`, and `scripts/verify_repository.py` — each required by a concrete verification-quality or conformance finding. Git history was consulted only as evidence for the archive-durability check (commit listing; no file contents from the superseded candidate were read). Controls were executed, not merely read: `scripts/verify_repository.py` was run on this review branch, GitHub branch state was queried via API, and the status-marker and link-format invariants were checked with `git grep`.

### Findings

---

**F1**
Materiality: **MATERIAL**
Claim / defect: The HQ-0 closure condition "protected `main` configured to require PR-based integration and the aggregate verification check" is not merely unconfigured — it is currently **unsatisfiable** under the repository's hosting plan and visibility. Both classic branch protection and repository rulesets return HTTP 403.
Affected authority or invariant: `docs/roadmap.md` (HQ-0 closure list, item "protected `main` …"; "Exact next action" step 3); `docs/phases/hq-0-repository-foundation.md` (Verification / falsification list); `docs/development/repository-rules.md` §7.
Evidence:
- `gh api repos/developmentconexus-ops/conexus-hq/branches/main` → `{"protected": false}`.
- `gh api repos/developmentconexus-ops/conexus-hq/branches/main/protection` → `403 — "Upgrade to GitHub Pro or make this repository public to enable this feature."`
- `gh api repos/developmentconexus-ops/conexus-hq/rulesets` → same 403.
- `gh api repos/developmentconexus-ops/conexus-hq` → `{"private": true, "visibility": "private", "owner_type": "User"}` — a private repository under a Free-plan user account, where GitHub gates both protection mechanisms.
Why it matters: The roadmap treats this closure item as a pending settings toggle ("establish/verify protected-main + required-check repository settings"). In reality it requires an operator decision outside the candidate: upgrade the plan, make the repository public (likely inappropriate for institutional company data), transfer to an organization/plan where enforcement exists, or consciously amend the closure condition to a compensating control (process-level no-direct-commits plus the existing post-merge `required` run on `main` as detection rather than prevention). If left implicit, the largest risk is that the condition is silently waived at closure time — exactly the "convenient fact" failure mode the Method forbids. Note also that the roadmap's own next-action sequence places this step **before** independent review; this review was dispatched with the step unresolved, which is harmless (reviewer output is Evidence and the two steps are independent) but should be acknowledged rather than silently reordered.
Smallest correct correction: No candidate-content change. Operator decision recorded as a decision-register entry: either (a) obtain enforcement (plan upgrade / org transfer) and configure protection requiring the `required` check, or (b) amend the HQ-0 closure condition to a named compensating control with an explicit reopen trigger for when enforcement becomes available.
Reopen required: **YES** — the HQ-0 closure contract in `docs/roadmap.md` must either be satisfied as written (infrastructure change) or consciously amended (operator ratification); it cannot be closed as currently specified.
Falsifier / proof after correction: `gh api repos/developmentconexus-ops/conexus-hq/branches/main --jq .protected` returns `true` and the protection/ruleset configuration lists `required` as a required status check; **or** a ratified HQ-D00x entry redefines the control and the roadmap closure list matches it.

---

**F2**
Materiality: **MATERIAL** (low severity, trivially fixable)
Claim / defect: `scripts/verify_repository.py` produces a guaranteed false positive on case-insensitive filesystems (Windows, default macOS): the forbidden-surface check `(ROOT / "docs/INDEX.md").exists()` matches the legitimate `docs/index.md`, so the mandated local verification run always fails on the operator's own platform.
Affected authority or invariant: `AGENTS.md` ("Run `python scripts/verify_repository.py` before claiming the candidate is repository-conformant"); `docs/development/repository-rules.md` §7; `scripts/verify_repository.py` lines 48–56.
Evidence: Executed on this Windows checkout: `repository verification FAILED / - forbidden legacy surface present: docs/INDEX.md` — while the actual directory listing contains only `index.md` (`Path('docs/INDEX.md').exists()` → `True`; `[p.name for p in Path('docs').iterdir()]` contains `index.md`, not `INDEX.md`). The CI run on `ubuntu-latest` (case-sensitive ext4) behaves correctly, which is why run `32653369086` passed.
Why it matters: The authoritative gate (CI) is unaffected, but the repository's own rules make the local run a precondition for claiming conformance. A control that always fails on the primary development OS trains its consumers to ignore verification failures — alarm fatigue is how tripwire controls die. It also masks any *real* local regression signal behind a permanent phantom error.
Smallest correct correction: Make the forbidden-exact check case-exact, e.g. resolve each forbidden path's parent and test exact-name membership: `parent.is_dir() and name in {p.name for p in parent.iterdir()}` (or test membership against `git ls-files`). One function, no behavior change on CI.
Reopen required: NO.
Falsifier / proof after correction: `python scripts/verify_repository.py` passes on a Windows checkout of the corrected candidate; planting a real `docs/INDEX.md` on a case-sensitive checkout still fails CI.

---

**F3**
Materiality: NON-MATERIAL
Claim / defect: The sole-mutable-status control detects **marker duplication**, not semantic status duplication. A second mutable status carrier without the `<!-- current-status-authority -->` marker (e.g. a future `docs/status.md` with stage/next-action prose) passes verification.
Affected authority or invariant: `scripts/verify_repository.py` lines 32–46; roadmap monopoly claim.
Evidence: Script logic matches only the literal marker string; `git grep current-status-authority` confirms exactly one owner today.
Why it matters (bounded): The written claims are honestly scoped — `repository-rules.md` §7 says the check falsifies "duplicate mutable-status markers", and the phase doc says "exactly one current-status marker exists". No document overclaims that the script proves semantic uniqueness. Residual coverage is review discipline, which is the correct residual for a semantic property.
Smallest correct correction: None required. Optionally note in §7 that the marker is a tripwire, not semantic proof.
Reopen required: NO.

---

**F4**
Materiality: NON-MATERIAL
Claim / defect: The bootstrap budget sums three files (`AGENTS.md` + `docs/index.md` + `docs/roadmap.md` = 8,791 bytes) while `repository-rules.md` §5 defines the required bootstrap as four files including `README.md` (total 9,348 bytes). A bloated README would not trip the budget.
Evidence: `scripts/verify_repository.py` lines 26–30 vs `repository-rules.md` lines 48–55; measured sizes via `wc -c`.
Why it matters (bounded): Current margin is large (≈9 KiB of 20 KiB) and README is the human landing page outside the agent context route, so the omission is defensible — but the claim "bootstrap budget ≤ 20 KiB" is slightly wider than what is measured.
Smallest correct correction: Either add README to the summed set or scope the printed claim to the agent-route files. Optional.
Reopen required: NO.

---

**F5**
Materiality: NON-MATERIAL
Claim / defect: The working-name fact ("Conexus / Conexus OS are working names, not ratified") is restated in five surfaces: `README.md`, `AGENTS.md` (hard stop), `docs/roadmap.md` (Current state), `docs/decisions/index.md` (HQ-D001), `docs/portfolio/map.md` (Naming). At HQ-5 ratification all five must change coherently.
Why it matters (bounded): The repetition is a deliberate guard-rail (the misuse risk — accidental brand ratification — is highest in exactly those entry surfaces), and HQ-D001 is unambiguously the owner. Drift risk is real but the mitigation at ratification time is a one-line grep for "working name". The policy itself is strong: decision-register entry, consequence ("no structural rename effort"), and a proportionate reopen trigger prevent both accidental ratification and premature rename churn.
Smallest correct correction: None now; at HQ-5, update via search for the working-name phrase.
Reopen required: NO.

---

**F6**
Materiality: NON-MATERIAL
Claim / defect: `docs/portfolio/map.md` (Convergence law) enumerates Product-platform vocabulary that no HQ document defines: "Brain context, Connections, governed capabilities, Builder/Paved Road, Product Agents, release/runtime machinery". A fresh reader cannot resolve these terms inside HQ, and the list presupposes a specific Conexus OS feature taxonomy that HQ does not own.
Evidence: `docs/portfolio/map.md` line 40.
Why it matters (bounded): The sentence is permissive ("may include … **only where the owning Product and platform authorities explicitly admit it**") and is immediately followed by the explicit negative list (no semantic copying, no giant domain model, no premature migration, no default shared schema, no brand decision), so it does not capture Product authority and does not force a monolithic conclusion. It also leaves room for evidence to change the strategy via HQ-D003's two-sided reopen triggers (standalone permanence, or platform unable to host without boundary violation). The defect is purely that undefined foreign vocabulary slightly weakens fresh-actor readability of an otherwise correct boundary statement.
Smallest correct correction: Optionally label the list as illustrative Product-owned vocabulary (one clause), or trim to capability-neutral wording. Not required for HQ-0.
Reopen required: NO.

---

**F7**
Materiality: NON-MATERIAL
Claim / defect: The governance actors "operator" and "Lead" are load-bearing (`docs/roadmap.md` next-action steps "Lead adjudication", "operator ratification"; `repository-rules.md` §6) but defined nowhere.
Why it matters (bounded): In the current single-operator reality the referents are unambiguous, and pre-creating a roles/governance document without a second human would violate the candidate's own no-taxonomy-before-consumer rule. Becomes material only when a second decision-making human or standing agent role appears.
Smallest correct correction: None now; additive later (one decision-register row or a short governance note when a real second actor exists).
Reopen required: NO.

---

**F8**
Materiality: NON-MATERIAL
Claim / defect: Link-checker coverage gaps: (a) reference-style Markdown links (`[text][ref]`) are not parsed — `git grep` confirms zero exist today; (b) inline links inside fenced code blocks **are** scanned, a latent false-positive class if a literal example link ever appears in a fence; (c) local case-insensitive filesystems can under-report broken links that CI's case-sensitive filesystem correctly catches — CI remains the authoritative gate, which is the right authority direction.
Evidence: `scripts/verify_repository.py` lines 69–88; corpus checks via `git grep`.
Why it matters (bounded): Zero live instances of any gap class; the control correctly falsifies every link that currently exists.
Smallest correct correction: None now.
Reopen required: NO.

---

**F9**
Materiality: NON-MATERIAL
Claim / defect: The `required` check is self-modifiable: a PR can edit `.github/workflows/ci.yml` to no-op the job, and even fully-enabled branch protection does not prevent workflow modification within the PR.
Why it matters (bounded): Inherent GitHub limitation, not a candidate defect. Residual control is exactly what the rules already mandate: no direct commits, one gate per Draft PR, explicit operator merge authorization — a human sees the diff that guts the check. Recorded so the limitation is known, not to demand tooling.
Reopen required: NO.

---

**F10**
Materiality: NON-MATERIAL
Claim / defect: The phase doc's archive claim ("Git history remains the evidence/archive" for the removed 40-file candidate) depends on ref retention: after the planned squash merge, the pre-collapse tree (last full state at `72a2f0b`, ancestor of the candidate HEAD) survives only through the candidate branch and GitHub's `refs/pull/1/head` (verified present).
Evidence: `git log origin/main..origin/agent/bootstrap-conexus-company-os` shows the full v0.1/Mitra/Sales Radar history; `git ls-remote origin refs/pull/1/head` → `3a33df6`.
Why it matters (bounded): PR head refs are retained by GitHub, so the evidence is reasonably durable; the fragility is only if the branch is deleted *and* the PR ref is someday garbage-collected or the repo migrated without PR refs. HQ-D005's reopen trigger ("material current semantics exist only in a removed file") remains exercisable as long as the ref exists.
Smallest correct correction: Optional one-time lightweight tag on `72a2f0b` (or simply do not delete the candidate branch) at merge time.
Reopen required: NO.

---

### Adversarial propositions — disposition

1. **Authority boundary exactly right** — Not falsified. Five-repository map is complete for named repositories, ownership direction is one-way (HQ sets direction; Product repositories own semantics and perform their own decision/reopen), methodology is excluded from HQ authority in both `AGENTS.md` and the map. No duplicate authority found; the only ownerless items found are the bounded notes F6 (foreign vocabulary) and F7 (actor definitions), neither of which is a live authority conflict.
2. **`docs/roadmap.md` sole mutable status authority** — Not falsified. Marker is unique (verified by grep and by script). The decision register's mutable dispositions (`CURRENT` → superseded) are a *declared, non-overlapping* ownership ("current institutional decision dispositions"), not stage/status/next-action state, and the register routes stage back to the roadmap. Phase doc routes its own status field back to the roadmap.
3. **Minimal because reduced, not incomplete** — Not falsified. Every one of the 10 files has a live consumer; every HQ-0 closure item has an owner **except** the infrastructure item in F1, which is a closure gap, not a missing document.
4. **No lost semantic obligation from the removed 40 files** — Not fully verifiable within the routing budget, and deliberately not verified by re-reading the superseded tree (that would reinstate history as authority). The residual risk is explicitly held by HQ-D005's reopen trigger, and the evidence remains reachable (F10). Accepted as a governed residual, not an open defect.
5. **Brain seam preserved without duplicate authority** — Not falsified. Seam is stated as a compile/publish direction from authored authority (rules §4, phase doc), zero runtime machinery exists in the candidate, and HQ-D004 carries the correct reopen trigger (a *named* integration consumer with a concrete contract).
6. **Convergence statement does not wrongly constrain Product architecture** — Not falsified (see F6). The statement is directional, guarded by owning-authority consent, carries an explicit anti-monolith negative list, and HQ-D003's reopen triggers permit evidence to reverse the strategy in either direction.
7. **Verification suite meaningfully falsifies its claims** — Partially falsified: F2 is a real false-positive class on the operator's own platform (material); F3/F4/F8 are honestly-scoped residual gaps (non-material). Positive control confirmed by execution: on this review branch the script correctly **fails** on `docs/work` presence (`temporary/noncanonical surface present in candidate: docs/work`, exit 1), proving the temporary-surface tripwire works.
8. **HQ-1 safely blocked** — Not falsified. `docs/roadmap.md` line 52 blocks HQ-1 and name ratification explicitly; `docs/index.md` routes thesis/brand questions back to the roadmap "until the owning gate opens".
9. **Review dialogue cannot leak into the candidate** — Not falsified; positively tested. The review branch was reverified as candidate + `ai-dialog.md` only; the verification script (run on any PR by the `required` workflow) hard-fails on any `docs/work/**` presence, so a leak into the merge candidate cannot pass CI.
10. **Global Maximum, not cleaner local maximum** — Not falsified. The structure matches the organizational operating envelope rather than inheriting the prior PR's shape; the prior shape's concepts were adjudicated (kept/removed with a recorded decision, HQ-D005); nothing in the candidate pre-builds future gates. The two material findings are an infrastructure/plan constraint and a portability bug — neither indicates a structural local maximum.

Security/minimization (objective 7): rules §8 and the `AGENTS.md` hard stop are proportionate normative controls; the 10-file candidate contains no credentials, PII, or ERP data (inspected). No automated secret scanning exists, and GitHub's push-protection for private repos is gated behind the same plan constraint as F1 — worth noting in the F1 operator decision, not a separate requirement. Inventing a compliance program now would violate the candidate's own minimality rule.

Scope discipline (objective 8): no over-engineering found (≈560 added lines, no speculative taxonomy, no premature Brain/brand/thesis surfaces); no under-design found beyond the governed residuals noted above. HQ-0 ratifies none of the out-of-scope items — verified the candidate contains no thesis, ICP, pricing, wedge, brand-identity, Brain-architecture, or migration decisions.

### Verdict

```text
NOT CONVERGED
MATERIAL FINDINGS = 2
NON-MATERIAL FINDINGS = 8
HQ-0 RATIFICATION RECOMMENDATION = NOT READY
```

Basis: F1 (closure condition unsatisfiable as written — requires an operator infrastructure or amendment decision) and F2 (mandated local verification fails permanently on the operator's platform). Both are small and precisely bounded: F2 is a one-function script fix inside the candidate; F1 requires no candidate change but must be resolved by explicit operator decision before HQ-0 can close. The candidate's *content* — authority architecture, working-name policy, portfolio convergence law, Brain seam, epistemic separation, and scope discipline — survived adversarial challenge with only non-material notes. After F2 is fixed in the candidate and F1 is resolved (enforcement obtained **or** the closure condition consciously amended and ratified), no known material finding would remain and this review supports re-adjudication to CONVERGED without a new full review pass.

Reviewer output is Evidence, not authority. Nothing here ratifies HQ-0, amends the roadmap, or authorizes merge.

```text
VERDICT: NOT CONVERGED
```
