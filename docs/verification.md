# Bootstrap verification

SPDX-License-Identifier: CC-BY-4.0

Executed on 2026-09-25 in the local checkout. This is evidence of a bootstrap, not clinical certification.

## Offline checks

```sh
python3 -m unittest discover -s tests -v
python3 skills/health-checkup/scripts/validate.py
```

Observed **21 tests passed** after implementing the missing validator (baseline: 18 passed, 3 failed). The validator returned `PASS: portable dependencies and OKF producer-profile checks`.

A separate clean-tree run exposed a test-fixture bug: the first artifact test assumed the ignored `.work` directory already existed. The fixture now creates it in class setup, independent of test ordering. Verification includes a clean copied tree with no pre-existing `.work` directory.

Coverage includes ambiguous intent, extracted Japanese employer requirements/package coverage, municipal uncertainty, insufficient English evidence, Japanese booking help, bot handoff, no-browser fallback, sensitive transmission priority, stale/superseding sources, provider-specific preparation, non-diagnostic follow-up, exact consent snapshots and freshness/proposal gates. Artifact mutation tests delete an OKF dependency and add a source-less footnote; both are rejected. Closed private-case tests reject identifiers, raw documents, medical results, dates, notes, free-text next actions and wrong boolean types.

These tests operate on synthetic **already-extracted facts**. They do not run a live agent, OCR, medical/legal review, real booking site, payment, authentication, reminder service or private-state writer. The consent helper compares a snapshot; the caller must enforce one-time use and actual execution boundaries.

## Actual Skills CLI copy installation

Node v22.22.3, npm 10.9.8, npm package `skills@1.7.0`. From the checkout root, the equivalent commands are:

```sh
ROOT="$PWD"
mkdir -p .work/install-check/{home,cache,project,tmp}
export HOME="$ROOT/.work/install-check/home"
export XDG_CACHE_HOME="$ROOT/.work/install-check/cache"
export XDG_CONFIG_HOME="$HOME/config"
export npm_config_cache="$ROOT/.work/install-check/cache/npm"
export TMPDIR="$ROOT/.work/install-check/tmp"
export DISABLE_TELEMETRY=1 DO_NOT_TRACK=1
cd "$ROOT/.work/install-check/project"
npm exec --yes --package=skills@1.7.0 -- skills add "$ROOT" --skill health-checkup --agent codex --copy --yes
python3 "$ROOT/skills/health-checkup/scripts/validate.py" --skill .agents/skills/health-checkup
```

Use an isolated shell for those exports. `.work` is ignored. The CLI reported **Found 1 skill**, **Installed 1 skill**, copied into `.agents/skills/health-checkup`. The installed directory was **not a symlink**. All **22 source files** (excluding Python bytecode) were compared byte-for-byte against the installed copy: **zero mismatches**. The copied bundle also passed the validator.

Exact retained local test installation:
`/opt/data/Development/nakabako-playbook-japan/.work/install-check/project/.agents/skills/health-checkup`.

No actual harness profile or global skill directory was targeted. Telemetry opt-out variables were set; no packet-level network audit was performed. npm package download is network access. No remote repository changes or push occurred.

## Review and remaining gates

Source and tests were read; metadata/link/privacy and license boundaries reviewed. Independent review by the coordinating agent remains a separate gate. No independent reviewer tool was available to this worker. Production use still requires domain review and live harness evaluations. Git author identity was absent in the checkout/environment; do not invent a personal author to bypass that blocker.