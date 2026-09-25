---
{
  "type": "Reference",
  "title": "Insurer and municipal pathways",
  "description": "Verify fiscal year, insurer, age definition, voucher and designated provider; Shinjuku is only an example.",
  "tags": [
    "japan",
    "health-checkup"
  ],
  "generated": {
    "by": "nakabako-bootstrap/0.1.0",
    "at": "2026-09-25T08:42:46.062752+00:00"
  },
  "status": "draft",
  "stale_after": "2026-10-25T08:42:46.062752+00:00",
  "sources": [
    {
      "id": "tokutei",
      "resource": "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000161103.html",
      "title": "Specific health checks and specific health guidance",
      "publisher": "Ministry of Health, Labour and Welfare",
      "source_type": "official-government",
      "jurisdiction": "Japan",
      "language": "ja",
      "retrieved_at": "2026-09-25T08:32:40.966005+00:00",
      "resolved_url": "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000161103.html",
      "retrieval_sha256": "8110d140e39859ac42cb066ba715b1e95c2ec2aeb10cd451cf99b0d44aba44fd",
      "source_state": "active",
      "last_verified_at": null
    },
    {
      "id": "handbook",
      "resource": "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/handbook_31132.html",
      "title": "Fourth-period implementation handbook landing page",
      "publisher": "Ministry of Health, Labour and Welfare",
      "source_type": "official-government",
      "jurisdiction": "Japan",
      "language": "ja",
      "retrieved_at": "2026-09-25T08:33:59.851898+00:00",
      "resolved_url": "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/handbook_31132.html",
      "retrieval_sha256": "6e4c6e09c455fb1e19fe86c2f6edafb1cac5ad13a3adfb11ba15a650b3561de3",
      "source_state": "active",
      "last_verified_at": null
    },
    {
      "id": "municipal",
      "resource": "https://www.city.shinjuku.lg.jp/kenkou/kenko02_001008.html",
      "title": "FY2026 municipal health checks",
      "publisher": "Shinjuku City",
      "source_type": "official-government",
      "jurisdiction": "Shinjuku City, Tokyo",
      "language": "ja",
      "retrieved_at": "2026-09-25T08:33:26.882365+00:00",
      "resolved_url": "https://www.city.shinjuku.lg.jp/kenkou/kenko02_001008.html",
      "retrieval_sha256": "d4d50d3ecaa514613161d858297c01ec1549f63edc6539634f4827198f8160ad",
      "source_state": "active",
      "last_verified_at": null
    }
  ],
  "x_nakabako": {
    "license": "CC-BY-4.0",
    "jurisdiction": "Japan; Shinjuku example only",
    "volatility": "mutable",
    "review_interval_days": 30,
    "last_verified_at": null,
    "effective_from": null,
    "effective_until": null,
    "superseded_by": null,
    "statement_ids": [
      "jp.healthcheck.program.tokutei",
      "jp.healthcheck.program.shinjuku-2026"
    ],
    "research_evidence": "/sources/research.md",
    "verification_note": "Source text inspected during bootstrap; not certified current. Runtime revalidation plus rediscovery required."
  }
}
---

# Program eligibility is not a national free-checkup promise

<a id="jp.healthcheck.program.tokutei"></a>
**jp.healthcheck.program.tokutei** — MHLW describes 特定健診 for the 40–74 target population and subsequent 特定保健指導 for those selected for professional support. Its current landing page announces implementation handbook v4.3 on 2026-03-09 while also retaining a v4.2 announcement. Finding an older handbook is not enough: inspect the current hub and superseding material.[^tokutei][^handbook]

Ask municipality and insurer **category**, then the minimum age information relevant to that program's fiscal-year rule. Distinguish employee, dependent, municipal NHI and other insurance pathways. The bootstrap could not retrieve Kyokai Kenpo's program hub (HTTP 403), so it deliberately does not assert its current ages, prices or subsidy terms. Verify the actual insurer's current official guidance.

<a id="jp.healthcheck.program.shinjuku-2026"></a>
**jp.healthcheck.program.shinjuku-2026** — **Example only, Shinjuku City FY2026:** the inspected page (displayed update 2026-07-09) lists residents aged 16–39 without a school/workplace opportunity; 40–74 with Shinjuku NHI or specified public-assistance status; and 75+ with the Tokyo late-elderly system or specified public-assistance status. Age is defined at the birthday reached by 2027-03-31; exclusions may apply, including some institutional residents. Other-insurer members aged 40–74 should ask their insurer, not assume city eligibility. This skill serves adults; it is not a child-health workflow.[^municipal]

The page describes a voucher, designated medical institutions, direct provider booking, bringing the voucher plus applicable eligibility documentation, and receiving results afterward. It lists free examination under its program, with FY-specific periods ending 2027-03-31. Treat that as a scoped retrieved statement, never a live price or a guarantee for another city. Request and verify the current voucher before booking; do not save its number.[^municipal]

The city also describes use of qualifying employer/Ningen Dock results for its specific-guidance pathway. Ask the city about necessary items and submission before duplicating an examination; transmission of prior results still needs consent.[^municipal]

[^tokutei]: MHLW specific-checkup overview and latest announcements.
[^handbook]: Current fourth-period handbook landing page, retrieved but handbook PDF not exhaustively reviewed.
[^municipal]: Shinjuku current-year health-check page; recheck at use.
