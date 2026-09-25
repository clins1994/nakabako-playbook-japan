---
{
  "type": "Reference",
  "title": "Employment examinations and changing requirements",
  "description": "An item-level orientation with explicit future-amendment warning; verify the examination date.",
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
      "id": "revision",
      "resource": "https://jsite.mhlw.go.jp/yamanashi-roudoukyoku/hourei_seido_tetsuzuki/anzen_eisei/hourei_seido/kenkoushindankaisei.html",
      "title": "Notice of changes applying April 2027",
      "publisher": "MHLW / Yamanashi Labour Bureau",
      "source_type": "official-government",
      "jurisdiction": "Japan",
      "language": "ja",
      "retrieved_at": "2026-09-25T08:33:26.360447+00:00",
      "resolved_url": "https://jsite.mhlw.go.jp/yamanashi-roudoukyoku/hourei_seido_tetsuzuki/anzen_eisei/hourei_seido/kenkoushindankaisei.html",
      "retrieval_sha256": "b2193fe0ce3c7962ca535526d97237e1d119eaa6eefae1c7b86eac84c00e9952",
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
      "jp.healthcheck.employment.baseline",
      "jp.healthcheck.employment.future-change",
      "jp.healthcheck.employment.aftercare"
    ],
    "research_evidence": "/sources/research.md",
    "verification_note": "Source text inspected during bootstrap; not certified current. Runtime revalidation plus rediscovery required."
  }
}
---

# Employment requirement matrix

<a id="jp.healthcheck.employment.baseline"></a>
**jp.healthcheck.employment.baseline** — The inspected Labour Bureau page lists a periodic check once within each year and distinguishes hiring examinations. Its baseline groups are below; this is not a universally applicable prescription or a current-law certificate.[^periodic]

| Japanese baseline label | Working English for matching an issuer's form |
|---|---|
| 既往歴及び業務歴 / 自覚症状及び他覚症状 | Medical/work history and symptoms/signs review |
| 身長、体重、腹囲、視力及び聴力 | Height, weight, waist, vision and hearing |
| 胸部エックス線検査 | Chest X-ray |
| 血圧 | Blood pressure |
| 貧血検査 | Anemia blood tests |
| 肝機能検査 | Liver function tests |
| 血中脂質検査 | Blood lipids |
| 血糖検査 | Blood glucose |
| 尿検査（糖・蛋白） | Urine glucose and protein |
| 心電図 | ECG |

The old periodic list also includes 喀痰検査 (sputum), and discusses specified omissions at a physician's discretion. Hiring and periodic omission rules differ. Do **not** remove tests on your own based on age or copy a package's title as evidence of coverage. Get doctor/issuer confirmation and verify the effective rules.[^periodic]

<a id="jp.healthcheck.employment.future-change"></a>
**jp.healthcheck.employment.future-change** — A separately discovered official notice is explicitly titled “令和9年4月から適用” (applies from April 2027). It describes removal of sputum examination, liver-enzyme naming changes and addition of serum creatinine examination. It is a **future change at bootstrap retrieval**, not evidence that these changes already apply in September 2026. The linked national leaflet returned HTTP 404 during bootstrap; exact conditions and original legal text were not verified. Reopen national legislation/guidance and confirm with employer/provider for the actual examination date.[^revision]

The old page remains accessible. Its existence and hash do not settle whether its item list is applicable now or after the future effective date. Record both sources, scope and dates. Do not automatically replace today's requirements with a newer publication.

<a id="jp.healthcheck.employment.aftercare"></a>
**jp.healthcheck.employment.aftercare** — Tokyo Labour Bureau guidance describes post-examination physician input and employer measures where abnormal findings require it, as well as careful handling of sensitive worker health information. This is distinct from the individual's clinical follow-up. Help the user get the correct certificate to the authorized recipient, not distribute the entire medical report to everyone at work. Employer regulatory reporting is not automatically the employee's filing task.[^followup]

[^periodic]: Baseline article 43/44 overview; potential aging content.
[^revision]: April 2027 change notice; original linked PDF unavailable at retrieval.
[^followup]: Tokyo Labour Bureau aftercare and information-handling guidance.
