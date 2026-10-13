---
name: armpit-odor
description: Navigate armpit odor care in Japan, distinguishing clinician diagnosis, potentially insured odor or sweating treatment and cosmetic self-pay options; prepare a shortlist and future booking handoff.
license: CC-BY-4.0; bundled scripts MIT (see LICENSES.md)
metadata:
  author: nakabako contributors
  version: "0.1.0"
  compatibility: Prose works without tools; current public-source access required. Offline checks support Python 3.11+.
  compatibility: Prose works without tools; current public-source access required. Offline checks support Python 3.11+.
---

# Armpit odor care in Japan

Start with **odor, excessive sweating, or both—and whether a clinician has already assessed it.** Help an adult choose a consultation and compare clinician-discussed routes. Never diagnose 腋臭症 (axillary odor) or 原発性腋窩多汗症 (primary axillary hyperhidrosis), dismiss distress, promise cure, or guarantee insurance coverage. Minors require clinician/guardian guidance outside this adult workflow.

Read [clinical and insurance orientation](references/okf/procedure.md), [refresh and shortlist](references/refresh.md) and [handoff/privacy](references/handoff.md). Missing resources require a complete copy. Test with [synthetic dry run](references/dry-run.md) only.

## Five decisions

1. **Choose assessment before a procedure.** Clarify the person's concern without diagnosing it from earwax, clothing, family history, a questionnaire or photographs. If not assessed, shortlist dermatology/appropriate plastic-surgery consultation rather than sell an odor procedure. Sudden change, skin pain/rash, generalized/night sweating or systemic symptoms belong with a clinician; urgent symptoms need timely medical care. Ask only relevant station/travel, budget, time away from work, language and accessibility constraints.
2. **Refresh and separate indications.** Recheck current official fee rules, relevant guideline and device/drug labeling, then exact clinic policies on every use. Distinguish odor treatment, sweating treatment, medical-device approval and insurance reimbursement. A diagnosis is the clinician's decision; procedure-specific billing/coverage is confirmed by the clinic and insurer when needed. Never turn a clinic's “保険適用” banner into eligibility.
3. **Compare routes without prescribing.** Present consultation/conservative management, potentially insured clinician-indicated surgery, sweating treatment only if assessed for that condition, and cosmetic/self-pay options in separate rows. Include no intervention or a second opinion. Explain scars, wound complications, recovery, repeat treatment and uncertain outcomes using current sources. The cheapest copay can still entail substantial recovery and follow-up burden.
4. **Build the shortlist and obtain the person's choice.** Compare two or three clinics on diagnostic assessment, applicable insured route versus self-pay, written itemized total/unknowns, specialist evidence, complications support, follow-up, travel and language. Do not choose irreversible treatment on their behalf. Ask the person to choose consultation/procedure and clinic after clinician discussion; then prepare the exact future booking/data-sharing review. Clinic contact and booking belong only in a future separately authorized execution.
5. **Complete the lifecycle in a future authorized run.** Follow the handoff's separate consent for field entry/transmission, booking, payment and cancellation. Produce verified directions, required documents, preparation, aftercare, dressing/drain or suture follow-up if prescribed, work/arm-movement/driving restrictions, return transport and cancellation terms. Unknown recovery or coverage details remain clinician/clinic checkpoints.

Lead each turn with one next action and a short known/unknown statement. Present Japanese labels beside English. Support the person without shame; clinician assessment may lead away from procedures and should not be represented as a failed booking workflow.

## Offline checks

Run `python3 scripts/validate.py` from this skill directory, and repository tests with `python3 -m unittest discover -s tests -v` from the checkout root. [decision.py](scripts/decision.py) checks synthetic extracted flags, cost unknowns and exact consent snapshots; it never executes actions, decides treatment or enforces agent behavior. Read the dry-run protocol for clinical/advertising cases that require an actual agent evaluation.
