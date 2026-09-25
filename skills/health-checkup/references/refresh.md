# Source verification and voluntary refresh proposals

SPDX-License-Identifier: CC-BY-4.0

## Runtime authority and certainty

For every important mutable requirement, inspect the current official source and search for newer, stronger, more specific or superseding sources. Use national ministry/legislation for legal baseline; prefecture/municipality for local programs; insurer for benefits; issuer for submission requirements; provider for package and appointment instructions. Context matters more than a mechanical rank. Secondary specialists are fallback leads; community reports are supplementary only.

Separate **verified for this decision** (matched source, date/scope and rediscovery checked), **strongly inferred** (reason stated, remaining gap disclosed), and **unknown**. An accessible page, new retrieval time, model confidence, or a hash match cannot elevate a claim to verified. If sources disagree, retain both and compare legal authority, applicability, effective date, amendment status and specificity; do not simply choose newest publication. Ask issuer/provider when unresolved, and avoid the consequential action.

## OKF producer profile

The canonical bundle is `references/okf/`, targeting upstream OKF **v0.2**. Frontmatter is indented JSON (a valid YAML subset), deliberately allowing zero-dependency parsing. This project's checker is not a general YAML/OKF validator.

- Native `type`, `sources[].resource/id`, keyed footnotes, `generated`, `status`, `stale_after`; native `verified` only for an actual claim-confirmation event. A mapping or list of verification events is accepted as upstream specifies.
- Concept IDs are file paths within bundle minus `.md`. Never reuse a claim's `x_nakabako.statement_ids` anchor for a different meaning. If meaning changes, deprecate and link replacement.
- Extensions (`x_nakabako` and extra source keys) record jurisdiction, language, publisher/type, retrieval hash/time, volatility, effective bounds, source state, review interval and research evidence. `last_verified_at: null` honestly means no complete freshness verification. Unknown effective dates stay null, not inferred from page update dates.
- `active/superseded/deprecated/unavailable/disputed` are **source** states, not native OKF `status`; native status remains `draft/stable/deprecated`.
- The initial health concepts are drafts with **no** native `verified` event. Source text was inspected; whole-claim current applicability and all supersession questions were not fully verified. Architecture is an accepted local decision, not a government fact.

## Two required tracks

**Revalidate:** record old URL, final URL/redirect, retrieval time, status, content fingerprint when available, relevant section and short quotation/summary. Check changed text, amendment/effective dates, obsolescence and scope. Inaccessible is not false and unchanged is not current.

**Rediscover:** record exact public queries, search time, official hubs/catalogs checked, candidate URLs, and why each is adopted/rejected/pending. Seek latest law, ministry notification, fiscal-year program and issuer/provider detail. If no replacement found, record the searched current hub as a candidate with a bounded assessment; do not pretend the search was exhaustive. A search snippet is not evidence of the candidate's substantive claim.

Resolve the claim against both tracks before proposing a new verification event. For supersession retain old source history and mark its state; set replacement link and effective date only when supported. A future-effective amendment can coexist with current rules. The bootstrap discovered exactly this pattern in employment examinations.

## Volatility

- Stable terminology/lifecycle orientation: target review ~180 days, sooner on a reported issue.
- Mutable requirements/eligibility/ministry guidance: target ~30 days **and verify at use**. Review before known effective-date boundaries.
- Highly volatile prices, availability, hours and staffing: fetch live for each decision; do not promote a quoted session result into durable OKF truth. Check again immediately before commitment.

A review interval is a queueing aid, not an accuracy guarantee. A draft or missing verification cannot become fresh just because `stale_after` has not arrived. `policy.freshness` conservatively returns a signal, never permission to skip runtime checks.

## Contributor-owned compute, no automatic shared writes

After useful help, the user may opt in to refresh a **public claim** using their own agent/model quota. No keys/tokens are collected. Declining does not affect assistance. Start from public sources anew; do not copy the user's case transcript, documents, screenshots, employer-private form or medical details.

1. Pick a stable statement ID and a narrow scope.
2. Run both tracks above. Save a local proposal modeled on `assets/refresh-proposal.example.json` (synthetic example, not evidence), outside private-case storage. Include old/new evidence, proposed text, scope, effective dates, supersession and unresolved questions.
3. Use `policy.proposal_ready` for a structural completeness check. It cannot validate authority, correctness or whether the claimed research happened.
4. Show the user the proposal and privacy scan. **Do not edit the canonical bundle, run git push, open a PR or publish automatically.** In this bootstrap only a proposal/checking interface is implemented; no contribution service exists.
5. A future contributor may deliberately create a local branch, update the claim and evidence, run tests, and submit a normal PR themselves. Maintainers inspect attribution/licensing, both research tracks, scope, effective dates and absence of private data. Only after substantive review add an honest `verified` actor/time, update `stale_after`, and record the log. Human review uses `human:<id>`; machine confirmation uses the actual producer/version or process actor, never fabricated human approval.

Do not add “verified” merely because the proposal checker or CI passes. There is no automatic source crawler, medical evaluator, PR bot or continuous refresh claim in this version.
