# Privacy and user state

SPDX-License-Identifier: CC-BY-4.0

## Default and limits

Use session context only. Do not invoke harness memory, create case files, log medical text in test output, put documents in the repository, or send them to an external parser. A host may retain chat logs, screenshots, tool logs or backups independently; this playbook cannot prevent that. Explain the host's retention policy if known, otherwise say unknown. Encourage redaction and local viewing. No patient data belongs in an issue, PR, refresh proposal or public bug report.

Location ladder: country → prefecture → municipality → neighborhood/station → postal code → exact address. Stop at what the next task needs. Age band normally suffices for program discovery; exact birthday may be necessary only in an official booking/eligibility step. Never ask for sex/gender/medical history routinely; explain a specific requirement, allow user/provider completion, and avoid inferring it.

## Knowing is not transmitting

A value already visible in the session is not permission to submit it. Before external OCR, translation, live form entry (including autosave), email, insurer/employer upload or calendar creation:

1. Identify the exact service/domain, fields or pages, purpose and consequences.
2. Show only necessary values in a private review; never print credentials or full identifiers in tool logs.
3. Ask for explicit approval of this action. Material destination, amount, package or payload changes invalidate approval.
4. User enters passwords, OTPs, My Number, card data and authentication secrets themselves. Do not collect these in chat. An insurance identifier is not My Number.
5. After any consequential action, read a receipt or say the outcome is unconfirmed. Avoid duplicate submissions after timeouts; check history/receipt first.

Do harmless public browsing or local draft translation without repeated confirmation. “Find a clinic” does not authorize contact, booking, payments or sharing.

## Optional minimal private case file

Only when expressly requested: show the exact proposed closed-schema data and location first. Use `schemas/private-case.schema.json`. It permits workflow stage, coarse purpose and checklist flags, not free text, provider identity, appointment date, results, test items, attachments, IDs, addresses, tokens or URLs. This deliberately sacrifices rich resume state for privacy. Clinical follow-up detail stays with the user/provider, not in this file. Reopen and ask the next material question next session.

The user chooses a local directory **outside this repository and outside any Git working tree**, not a synced/public folder. Create a dedicated private directory (POSIX 0700), use exclusive creation for a new file (0600), and verify permissions; on Windows use user-only ACLs. Refuse symlinks and existing files unless a separately reviewed update is explicitly authorized. Do not promise encryption; use encrypted disk storage if the user requires it. No persistence writer is bundled in this bootstrap: the file is a documented opt-in handoff, never an automatic side effect.

Let the user review, delete or decline it. Ask a retention choice; default recommendation is delete after the administrative task closes. Deleting does not guarantee removal from snapshots/backups. `.gitignore` is defense in depth, not permission to save inside the repo.
