---
{
  "type": "Reference",
  "title": "Choose the administrative route",
  "description": "Distinguish work, institution, insurer, municipality and personal screening before provider search.",
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
      "id": "periodic",
      "resource": "https://jsite.mhlw.go.jp/yamanashi-roudoukyoku/hourei_seido_tetsuzuki/anzen_eisei/hourei_seido/5-9.html",
      "title": "Employment examination baseline",
      "publisher": "MHLW / Yamanashi Labour Bureau",
      "source_type": "official-government",
      "jurisdiction": "Japan",
      "language": "ja",
      "retrieved_at": "2026-09-25T08:33:26.161688+00:00",
      "resolved_url": "https://jsite.mhlw.go.jp/yamanashi-roudoukyoku/hourei_seido_tetsuzuki/anzen_eisei/hourei_seido/5-9.html",
      "retrieval_sha256": "3cec48fc920ace1c51b0e1f47e7acd8bbd372eef0e8e06f8f1551b0f86ecebe2",
      "source_state": "active",
      "last_verified_at": null
    },
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
    },
    {
      "id": "prep",
      "resource": "https://fujisawatokushukai.jp/en/dock/",
      "title": "Medical check-up and preparation",
      "publisher": "Shonan Fujisawa Tokushukai Hospital",
      "source_type": "official-provider",
      "jurisdiction": "Shonan Fujisawa Tokushukai Hospital, Kanagawa",
      "language": "en",
      "retrieved_at": "2026-09-25T08:34:24.205941+00:00",
      "resolved_url": "https://fujisawatokushukai.jp/en/dock/",
      "retrieval_sha256": "6da740339efaafc2db82732f198c3c29ea521c4cd732f40e8cde35491f2d4c3e",
      "source_state": "active",
      "last_verified_at": null
    }
  ],
  "x_nakabako": {
    "license": "CC-BY-4.0",
    "jurisdiction": "Japan",
    "volatility": "mutable",
    "review_interval_days": 30,
    "last_verified_at": null,
    "effective_from": null,
    "effective_until": null,
    "superseded_by": null,
    "statement_ids": [
      "jp.healthcheck.route.work",
      "jp.healthcheck.route.program",
      "jp.healthcheck.route.personal"
    ],
    "research_evidence": "/sources/research.md",
    "verification_note": "Source text inspected during bootstrap; not certified current. Runtime revalidation plus rediscovery required."
  }
}
---

# Route by purpose, not by package name

<a id="jp.healthcheck.route.work"></a>
**jp.healthcheck.route.work** — Employment examinations include 雇入時 (at hiring) and 定期健康診断 (periodic); they are distinct. Official Labour Bureau guidance points to Articles 43 and 44. Obtain the employer's form, deadline and designated payment/provider arrangements rather than selecting a generic “full checkup.” School or other institution requirements are document-specific, not automatically the employment baseline.[^periodic]

<a id="jp.healthcheck.route.program"></a>
**jp.healthcheck.route.program** — 特定健診 focuses on metabolic-syndrome-related risk in the 40–74 target population; insurer and local program conditions still determine a person's route. 特定保健指導 is a subsequent professional support pathway, not equivalent to a diagnostic retest. Municipal programs can serve other groups: the [Shinjuku example](/health/programs.md) includes younger residents without workplace/school access.[^tokutei][^municipal]

<a id="jp.healthcheck.route.personal"></a>
**jp.healthcheck.route.personal** — 人間ドック is a comprehensive preventive checkup offering, not a synonym for every statutory or subsidized examination. Provider package scope and payment differ. The Shonan provider page separately describes general packages and private Ningen Dock and says its Ningen Dock fees are not covered by National Health Insurance. Do not generalize that statement into a denial of all insurer/employer subsidies.[^prep]

がん検診 (cancer screening), diagnostic care for symptoms, occupational exposure examinations and pregnancy-specific care should not be silently substituted for routine health-check administration. Route complex or clinical questions to issuer/provider. This is a workflow boundary, not advice about which medical tests someone should have.

[^periodic]: Labour Bureau employment guidance.
[^tokutei]: MHLW specific-checkup overview.
[^municipal]: Shinjuku City FY2026 guidance.
[^prep]: Shonan Fujisawa Tokushukai official checkup page.
