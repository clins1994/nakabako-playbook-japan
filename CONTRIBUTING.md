# Contributing

SPDX-License-Identifier: CC-BY-4.0

Start small: one public claim, missing branch, translation correction or deterministic scenario. Do not post private documents, patient data, credentials, identifiers or case screenshots. Use invented fixtures; distinguish them from actual retrieval evidence.

1. Read [architecture](skills/health-checkup/references/okf/architecture/decisions.md), [licensing](LICENSES.md) and [refresh procedure](skills/health-checkup/references/refresh.md).
2. Edit the canonical OKF bundle inside the skill, not `knowledge/`. Keep stable statement IDs; preserve old-source history and identify replacements. Use JSON frontmatter for this producer profile. Preserve Japanese terms and explain procedural meaning.
3. For factual updates, record publisher, URL, jurisdiction, relevant passage, retrieval time, effective bounds and uncertainty. Revalidate the old source **and** search for newer/more specific authority. Document queries, current hubs, candidate assessments and failed fetches. A new hash alone cannot earn a verification event. Never claim research you did not perform.
4. Draft an update proposal using the synthetic asset as a shape, not evidence. Contributor-owned compute is optional; no credentials are shared. The structural `proposal_ready` helper checks completeness only. Maintainers review source authority, applicability, both research tracks, attribution, privacy and licensing before accepting knowledge changes. Record honest native verification actor/time only after substantive verification; update stale_after and bundle log accordingly.
5. For software changes, add a failing scenario before implementation. Use `python3 -m unittest discover -s tests -v` and `python3 skills/health-checkup/scripts/validate.py`. Exercise a whole-directory copy installation when changing resource paths. State exactly what tests did and did not validate.
6. Review the diff for sensitive data and unintended files. Open a normal PR only when you deliberately choose to publish. This playbook never automatically pushes, opens issues or sends evidence.

Submissions are under the applicable [artifact license map](skills/health-checkup/LICENSES.md): content CC BY 4.0, software/tests/schemas MIT. Retain attribution and identify modifications to reused content. Keep substantial executable code separate from knowledge; the documented mixed-file convention is mandatory. Do not import third-party documents wholesale without permission. New helper scripts should include `SPDX-License-Identifier: MIT`; new prose should identify CC-BY-4.0.

Review checklist: requirements vs package marketing; current vs future-effective law; local vs national eligibility; evidence vs inference; English website vs actual support; action-specific consent; human takeover without bot bypass; provider-specific preparation; results and administrative closure; no diagnosis or unnecessary storage.