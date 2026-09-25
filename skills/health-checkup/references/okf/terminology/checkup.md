---
{
  "type": "Reference",
  "title": "Japanese administrative terms",
  "description": "Working procedural translations; issuer and page context determine exact meaning.",
  "tags": [
    "japan",
    "health-checkup"
  ],
  "generated": {
    "by": "nakabako-bootstrap/0.1.0",
    "at": "2026-09-25T08:42:46.062752+00:00"
  },
  "status": "draft",
  "stale_after": "2027-03-24T08:42:46.062752+00:00",
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
      "id": "provider",
      "resource": "https://www.tokyomidtown-mc.jp/en/health/",
      "title": "Medical checkup official service page",
      "publisher": "Tokyo Midtown Clinic",
      "source_type": "official-provider",
      "jurisdiction": "Tokyo Midtown Clinic, Tokyo",
      "language": "en",
      "retrieved_at": "2026-09-25T08:34:23.719317+00:00",
      "resolved_url": "https://www.tokyomidtown-mc.jp/en/health/",
      "retrieval_sha256": "2f9b4197370027bf562dbfb2a1a4fb4a82ff299640a99dc1a119aff36be14ca3",
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
    "volatility": "stable",
    "review_interval_days": 180,
    "last_verified_at": null,
    "effective_from": null,
    "effective_until": null,
    "superseded_by": null,
    "statement_ids": [
      "jp.healthcheck.terms.forms",
      "jp.healthcheck.terms.results"
    ],
    "research_evidence": "/sources/research.md",
    "verification_note": "Source text inspected during bootstrap; not certified current. Runtime revalidation plus rediscovery required."
  }
}
---

# Terms in context

<a id="jp.healthcheck.terms.forms"></a>
**jp.healthcheck.terms.forms** — 健康診断 / 健診: health examination/checkup; 特定健康診査 / 特定健診: a specific insurer-organized screening pathway, not any thorough examination; 受診券: voucher/eligibility ticket; 受診票 / 問診票: health-check form/questionnaire, whose completion/bring requirements depend on the issuer. Shinjuku explicitly distinguishes its voucher from the form supplied at the medical institution.[^tokutei][^municipal]

雇入時: at hiring; 定期: periodic; 検査項目: examination items; 健康診断書: medical-check certificate/report; 人間ドック: comprehensive preventive package. Do not assume the document called 診断書 matches an employer's prescribed form.[^periodic][^provider][^prep]

<a id="jp.healthcheck.terms.results"></a>
**jp.healthcheck.terms.results** — Working translation for navigation: 要再検査 = repeat examination requested; 要精密検査 = detailed further examination requested; 要受診 = medical consultation requested; 経過観察 = observation/follow-up according to the provider's instructions. These labels are not diagnoses and their urgency/letter-grade mapping is not standardized here. Read the provider's actual explanation; ask them if the timing is missing.

The result-label translations above are linguistic orientation by the bootstrap author, not a sourced clinical classification. They intentionally carry no verified event.

[^tokutei]: MHLW terminology for specific examination/guidance.
[^municipal]: City voucher/form distinction.
[^periodic]: Labour Bureau examination terminology.
[^provider]: Employer certificate arrangements.
[^prep]: General and private checkup terminology.
