# Provider discovery and comparison

SPDX-License-Identifier: CC-BY-4.0

Start from requirements, not “best Tokyo clinic.” Example public queries (replace placeholders, never include IDs):

- `<station> 雇入時 健康診断 心電図 診断書 英語`
- `<municipality> 令和<year> 特定健康診査 実施医療機関`
- `<provider branch> 健康診断 検査項目 結果 日数 英語 対応`

Use issuer/insurer designated lists first where mandated. Confirm fiscal-year eligibility, booking route, prior authorization and whether the selected provider accepts the voucher. Do not assume a private 人間ドック meets a required form or that general medical insurance pays for screening. Distinguish covered/subsidized screening, self-pay add-ons and later clinical care. Ask the payer about reimbursement and required receipt naming before payment.

Build a session-only table (usually up to three candidates). For **each attribute**, keep value, certainty, source URL, retrieval time, and relevant passage or direct confirmation:

- provider and exact branch; station/location; travel estimate and assumptions (not exact home address);
- package name and included tests **individually**, exclusions, unclear substitutions;
- price including tax, interpreter/certificate/add-on fees, payment methods, subsidy acceptance;
- actual English support separately for booking, on-site clinician/staff and results; interpreter availability/cost;
- available dates, opening hours, booking method, cancellation/no-show policy;
- accessibility and clinician preferences if raised, result turnaround and format, employer-form transcription and English certificate capability;
- unresolved caveats, official source freshness, last checked for this user.

Reject or leave unresolved a package with missing mandatory items. `compare_package` in `scripts/policy.py` can compare already-extracted normalized test names; it cannot extract Japanese, assess clinical equivalence or waive tests. If a doctor's judgment permits omission, obtain that judgment and issuer acceptance; never omit tests just because a user is young.

Prefer official national authority for legal rules; municipality/insurer for the user's program; requesting institution for its form and deadline; provider for package, preparation and capacity. This is a scope hierarchy, not a rule that a general national page overrules specific booking instructions. Secondary/community sources can suggest candidates but cannot confirm availability or compliance.

A provider's official statement is **verified as a statement at retrieval**, not a guarantee of today's staffed appointment. Say “official page says…” and confirm appointment-specific support. **Strongly inferred/likely** requires a stated reason and cannot satisfy a hard requirement; **unknown** stays unknown. No universal score: explain tradeoffs (deadline vs travel, cost vs confirmed language), then ask the user to choose.

Research examples, not a live shortlist: Tokyo Midtown's page warns its English is machine-translated and describes employer-form review in advance; Shonan Fujisawa Tokushukai's English page says its current questionnaire flow requires Japanese or a separately charged interpreter. See OKF source evidence. These are cautionary examples, not endorsements or live recommendations.
