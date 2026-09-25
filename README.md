# nakabako-playbook-japan

SPDX-License-Identifier: CC-BY-4.0

Community-maintained agent playbooks for navigating real-world processes:
requirements → rules → decisions → sources → forms → actions → follow-up.

The first workflow is **health-checkup management in Japan**, from choosing the correct administrative route through preparation, results paperwork, reimbursement and follow-up coordination—not just finding a clinic.

**Bootstrap, not production clinical software.** English-speaking adult residents are the initial audience. The skill assists administration, not diagnosis, treatment, emergency care or selection of medically appropriate screening. Factual knowledge is deliberately **draft**, not certified current. Verify mutable requirements against current authorities at use. No automated booking service, OCR engine, browser extension, scheduler or persistence writer is bundled.

## Install and use

Review the skill and licenses before letting an agent use it. With Node/npm available, from the project where you want the skill installed:

```sh
# From an existing local clone (replace the absolute path):
DISABLE_TELEMETRY=1 DO_NOT_TRACK=1 npx --yes skills@1.7.0 add /absolute/path/to/nakabako-playbook-japan --skill health-checkup --agent codex --copy --yes
```

This selects a project-local Codex-compatible installation, not a global install. Choose your supported agent using the CLI's help; do not use `--global` unless you deliberately want a global install. Other harnesses can copy the **whole** `skills/health-checkup/` directory into their documented skill directory. Copying only SKILL.md breaks its knowledge dependencies. Python 3.11+ is optional for offline checks; the prose workflow works without Python or browser automation.

Once this local bootstrap is published, the corresponding remote-source command will be:

```sh
DISABLE_TELEMETRY=1 DO_NOT_TRACK=1 npx --yes skills@1.7.0 add clins1994/nakabako-playbook-japan --skill health-checkup --agent codex --copy --yes
```

**The remote is not populated by this bootstrap; that remote command is not yet a working installation source.** No push was authorized. Package download uses npm's network service; telemetry flags are not a claim of zero network access. See [verification](docs/verification.md) for the isolated local-copy test.

Ask your agent: “I need a health checkup in Japan.” It should ask the next material question, or inspect a supplied requirement document, rather than start a long questionnaire. A host without browser tools can still guide manual completion with Japanese/English procedural help. See the [realistic synthetic end-to-end example](docs/end-to-end-example.md).

## Architecture and tree

```text
README.md / CONTRIBUTING.md / LICENSES.md
LICENSE-content / LICENSE-software
knowledge/README.md                   canonical-bundle pointer, not a duplicate
docs/                                audit, example, verification
skills/health-checkup/
  SKILL.md                           progressive agent behavior
  LICENSES.md / LICENSE-*             portable licensing
  references/
    privacy.md / browser-handoff.md / providers.md / refresh.md
    research-receipts.json            actual public retrieval receipts
    okf/
      index.md / log.md
      health/                        routes, employment, programs, lifecycle
      terminology/ / sources/ / architecture/
  scripts/                           deterministic policy and bundle checks
  schemas/private-case.schema.json   closed minimal opt-in checkpoint
  assets/refresh-proposal.example.json
tests/                               synthetic offline behavioral scenarios
```

**OKF = durable knowledge; Agent Skill = behavior; private state = this user's case.**
One meaningful intent gets one skill. Its canonical OKF v0.2 bundle is nested inside it so copy-only installers preserve references. There is no parallel editable knowledge copy. JSON frontmatter is a YAML subset and permits standard-library validation of our limited producer profile. See [architecture decisions](skills/health-checkup/references/okf/architecture/decisions.md) and the [upstream audit](docs/upstream-audit.md).

State is session-only by default; this cannot disable a host's chat/tool logging. Optional user-approved persistence is a minimal closed checkpoint outside every Git tree, with no identifiers, appointment details, medical results, documents or free text. No private data belongs in knowledge, issues or tests. Reading data is not permission to send it. Consequential actions and sensitive live-field entry require destination/payload review and explicit consent. Authentication, CAPTCHA, OTP and payment verification are human checkpoints, never bypass targets.

## Provenance and freshness

OKF concepts carry native sources, keyed footnotes, generated metadata, status and stale_after. Stable claim anchors and `x_nakabako` extensions record scope, retrieval timestamps/hashes, effective dates, review interval and source state. Null dates remain unknown. Retrieval is not verification; the initial health concepts have **no native verified event**.

A refresh must both **revalidate existing evidence** and **rediscover better/newer/superseding authority**. An old URL remaining live proves neither currentness nor applicability. Bootstrap research found a separate April 2027 employment-examination amendment and an updated MHLW handbook; unresolved amendment details are explicitly recorded. Prices, appointment availability and staffing must be fetched live, not promoted to durable truth.

After assistance succeeds, a user may volunteer their own model quota for a narrow public-source-only refresh. No API keys or private case transcript are requested. Produce a proposal with both research tracks, evidence, scope and unresolved questions; a contributor and maintainer review before any shared update. No automatic PR or publication pipeline exists. [Refresh guide](skills/health-checkup/references/refresh.md) · [Contributor guide](CONTRIBUTING.md).

## Develop and test

```sh
python3 -m unittest discover -s tests -v
python3 skills/health-checkup/scripts/validate.py
```

The tests exercise deterministic decisions over already-extracted facts, privacy-schema rejection, consent snapshots, freshness, source supersession and portable dependencies. They **do not** demonstrate live agent compliance, actual Japanese OCR, browser operation, booking success or clinical/legal accuracy.

## Licensing, assumptions and roadmap

**CC BY 4.0** covers knowledge, documentation and prose; **MIT** covers scripts, schemas and tests. See [licensing map](LICENSES.md), including mixed-file rules and external-source limits.

Initial assumptions: adult residents, English-first help with original Japanese labels, user-controlled accounts and final decisions, current sources reachable or uncertainty disclosed. Employer/insurer/municipality/provider requirements remain case-specific. Before broader release, prioritize independent Japanese-domain review, amendment verification, accessibility/user testing and real harness/OCR/browser evaluations with consented synthetic data.

The broader design is **language-agnostic**: future language renderings should share stable knowledge IDs rather than fork facts. Japan is a proving ground, not a universal framework. Future countries, cities and reusable capabilities should emerge from demonstrated needs. A future `nakabako/playbook-japan` organization migration should require repository-link updates, not hardcoded runtime changes. No organization infrastructure is created now.