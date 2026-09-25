---
{
  "type": "Reference",
  "title": "Preparation, results and administrative closure",
  "description": "Provider-specific instructions and result handling continue beyond booking.",
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
    },
    {
      "id": "followup",
      "resource": "https://jsite.mhlw.go.jp/tokyo-roudoukyoku/hourei_seido_tetsuzuki/roudoukijun_kenshin_0001.html",
      "title": "Post-examination measures and worker health information",
      "publisher": "MHLW / Tokyo Labour Bureau",
      "source_type": "official-government",
      "jurisdiction": "Japan",
      "language": "ja",
      "retrieved_at": "2026-09-25T08:33:26.567615+00:00",
      "resolved_url": "https://jsite.mhlw.go.jp/tokyo-roudoukyoku/hourei_seido_tetsuzuki/roudoukijun_kenshin_0001.html",
      "retrieval_sha256": "f2f9001954cecf9576b2c1c0b515d52f40097991dce60bf8391bee9af4b310a4",
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
      "jp.healthcheck.lifecycle.preparation",
      "jp.healthcheck.lifecycle.certificates",
      "jp.healthcheck.lifecycle.results"
    ],
    "research_evidence": "/sources/research.md",
    "verification_note": "Source text inspected during bootstrap; not certified current. Runtime revalidation plus rediscovery required."
  }
}
---

# Booking is not completion

<a id="jp.healthcheck.lifecycle.preparation"></a>
**jp.healthcheck.lifecycle.preparation** — Providers may send instructions and sample kits after booking. Shonan Fujisawa Tokushukai's official page describes a detailed instruction sheet and specimen kit when needed, fasting/preparation instructions, documentation to bring, and restrictions associated with sedated upper endoscopy. Tokyo Midtown directs patients to advance examination precautions and describes online questionnaires and results. These are provider-specific examples, not a common medical protocol.[^prep][^provider]

Extract, do not invent: appointment timezone and arrival time; correct branch; when kits arrive and whom to contact if missing; sample collection windows/storage **as instructed**; dietary/water restrictions and exceptions; medication questions for the provider; questionnaires and required documents; payment; cancellation/no-show terms; transport/escort requirements and accessibility. Do not merge a municipal general instruction with a different provider's endoscopy instruction. If instructions conflict or relate to diabetes medicines, pregnancy or other clinical factors, have the user contact the provider; never adjust treatment.

<a id="jp.healthcheck.lifecycle.certificates"></a>
**jp.healthcheck.lifecycle.certificates** — Tokyo Midtown says designated employer-form transcription must be requested in advance; it reviews the form and possible fee and may not accommodate a request first made at the visit. Ask about exact issuer format, signature/stamp, English translation/certificate, paper versus digital, turnaround and delivery **before** choosing a package. Obtain transmission consent before sending a form, even for a quote.[^provider]

Payment and reimbursement checklist: confirm who pays, whether prior authorization is needed, what is outside subsidy, acceptable payment method, receipt name and required originals, submission deadline and where to retain a private receipt. No blanket insurance-coverage promise.

<a id="jp.healthcheck.lifecycle.results"></a>
**jp.healthcheck.lifecycle.results** — Shinjuku describes a later results explanation; Tokyo Midtown describes online results and secondary-exam support. Result delivery can therefore be a separate appointment, portal or other provider-specific step. Check missing-result escalation, portal access, language and expected arrival against the submission deadline. Work-related aftercare can involve an occupational physician/employer process separate from clinical retesting.[^municipal][^provider][^followup]

Explain the provider's administrative wording and requested next contact. Do not interpret numerical results, tell the user they are healthy/unfit, or map every provider's letter grades to one diagnosis. For 要再検査 / 要精密検査, help arrange clarification/follow-up and preserve the provider's stated timing. For urgent instructions or acute symptoms, direct to immediate professional help rather than delay for paperwork.

Closure: results received → certificate matches request → user approves minimal submission → receipt/acknowledgment confirmed → reimbursement tracked → follow-up arranged or explicitly pending. A reminder is only scheduled if a tool actually created it with consent; otherwise provide a user-owned checklist.

[^prep]: Shonan Fujisawa Tokushukai preparation page.
[^provider]: Tokyo Midtown workflow and FAQ.
[^municipal]: Shinjuku result-notification flow.
[^followup]: Tokyo Labour Bureau post-examination measures.
