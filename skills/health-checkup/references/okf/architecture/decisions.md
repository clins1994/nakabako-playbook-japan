---
{
  "type": "Architecture Decision",
  "title": "Knowledge, behavior and private state boundaries",
  "description": "One portable skill with its canonical OKF bundle, no runtime service or patient store.",
  "generated": {
    "by": "nakabako-bootstrap/0.1.0",
    "at": "2026-09-25T08:42:46.062752+00:00"
  },
  "status": "stable",
  "sources": [
    {
      "id": "okf-spec",
      "resource": "https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/SPEC.md",
      "title": "OKF v0.2 specification"
    },
    {
      "id": "skills-spec",
      "resource": "https://agentskills.io/specification",
      "title": "Agent Skills specification"
    }
  ],
  "x_nakabako": {
    "license": "CC-BY-4.0",
    "decision_status": "accepted-user-scope",
    "statement_ids": [
      "nakabako.architecture.boundaries"
    ]
  }
}
---

# Decisions

<a id="nakabako.architecture.boundaries"></a>
**nakabako.architecture.boundaries** — OKF is durable knowledge; SKILL.md is agent behavior; user state is session-only by default with explicit opt-in minimal external private file. No automatic harness memory, patient store, remote resources or credential collection.

The single canonical bundle lives inside the skill so copy-only installers preserve dependencies. `knowledge/README.md` points here; there is no second editable copy. Future multiple skills can introduce a build-time shared bundle only when needed.

Use OKF v0.2 native type/sources/generated/status/stale_after and optional verified. Stable concept IDs are bundle-relative paths without .md; stable claim identifiers are explicit anchors and x_nakabako.statement_ids. Metadata extensions capture retrieved time, jurisdiction, effective dates, volatility and rediscovery evidence without pretending they are native OKF fields. Frontmatter uses indented JSON, a valid YAML subset, so standard-library tooling can parse our producer profile; general OKF permits broader YAML.[^okf-spec]

Agent Skills metadata uses string values and relative resources; no harness-only hooks or implicit tool permissions. Manual operation remains useful without Python or browser automation.[^skills-spec]

Content is CC-BY-4.0; scripts/schemas are MIT; no copied upstream implementation. Avoid organizational infrastructure: only README repository URLs need changing for a future nakabako/playbook-japan migration. English-first prose preserves Japanese labels; the workflow and identifiers can support future other-language renderings without English-only intent assumptions.

[^okf-spec]: Inspected current upstream SPEC.md at pinned commit.
[^skills-spec]: Inspected Agent Skills specification.
