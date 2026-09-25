# Upstream audit

SPDX-License-Identifier: CC-BY-4.0

Bootstrap inspection date: 2026-09-25. Pinning records what was inspected, not a promise that upstream will never change.

| Upstream | Inspected reference | Adoption |
|---|---|---|
| Open Knowledge Format | [SPEC.md v0.2](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/SPEC.md), commit `ad30107c31c06aec8a7d5636e0d1058118604e6f` | Directory bundle, concept path IDs, YAML frontmatter, native provenance/trust/lifecycle, source-keyed footnotes and bundle-root links |
| Agent Skills | [Specification](https://agentskills.io/specification), unversioned page retrieved on inspection date | SKILL.md name/description, optional license/compatibility/string metadata, progressive references/scripts/assets and portable relative dependencies |
| Vercel Labs Skills | [README](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/README.md) and installer inspected in preceding research at `7407f3893ad4dceab546ac002c3ef806e4000c73` | Local source discovery, named skill selection, explicit agent, project scope and whole-directory `--copy` |
| Published Skills CLI | npm `skills@1.7.0` | Actual isolated project-local install executed; package version is not asserted to equal the inspected Git commit |

The continuation re-fetched the pinned OKF specification, Skills README and current Agent Skills page. SHA-256 of retrieved bytes:

```text
OKF SPEC.md:         26aa5da029278939f914e578107242d9607d4f2dc5fe153272b82f9ed1030101
Agent Skills HTML:  0c8fa2e34481b7ce8aa8b04ebef56b25e55155586eb858eb08c29bf24d8ea6c2
Skills README.md:   f1835e9d5cc091a82b3ea75ec93bdd96e3c8f86187358ca046a3ac3acdb3983b
```

## Deliberate profile decisions

- OKF only requires `type` for a concept; our producer profile is stricter, requiring useful titles, generated/status/source metadata. This does not redefine general OKF compliance.
- JSON frontmatter is a YAML subset. `validate.py` validates this repository's producer profile and simple local links, **not arbitrary YAML, Markdown or all OKF constraints**. It does not check source truth, external URLs, every timestamp or clinical applicability.
- `x_nakabako` and source extensions carry retrieval, jurisdiction, effective bounds, volatility and statement IDs. They are explicitly not native OKF fields. Source state is separate from native concept status.
- No native `verified` event is emitted merely because a source was fetched. Health concepts remain drafts. Architecture is a stable local decision, not a verified healthcare claim.
- Root-relative OKF links resolve against the bundle root, not the filesystem or GitHub repository root. A generic Markdown renderer may need that context; the checker resolves it explicitly.
- Agent Skills name matches its directory; no experimental allowed-tools permission grant or vendor-specific hooks are required. The installer is not an execution sandbox.
- Copy installation must preserve all references, schemas, helper scripts and license files. A SKILL.md-only distribution is unsupported.

No upstream implementation is vendored or relicensed. The CLI was downloaded/executed only for the documented installation check, with isolated home/cache and telemetry opt-out. External medical-source retrieval and unresolved authority are recorded separately in [research evidence](../skills/health-checkup/references/okf/sources/research.md).