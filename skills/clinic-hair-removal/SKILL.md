---
name: clinic-hair-removal
description: Compare clinic-based hair removal in Japan on total cost, quality and suitability; prepare clinician consultation, a small shortlist and a consent-gated future booking handoff.
license: CC-BY-4.0; bundled scripts MIT (see LICENSES.md)
metadata:
  author: nakabako contributors
  version: "0.1.0"
  compatibility: Prose works without tools; current public-source access required. Offline checks support Python 3.11+.
---

# Clinic-based hair removal in Japan

Start with the desired area and outcome: **less maintenance, substantial reduction, or a particular appearance?** Help an adult compare clinic-based options on total affordability, quality and suitability. This is administrative decision support, not diagnosis, laser selection, prescribing or a guarantee of permanent removal. Minors need a clinician and the clinic's guardian rules rather than this adult workflow.

Read [clinical orientation](references/okf/procedure.md), [refresh and shortlist](references/refresh.md) and [handoff/privacy](references/handoff.md). Missing resources require a complete skill copy. Use [synthetic dry run](references/dry-run.md) when testing; no live records or clinic submissions.

## Five decisions

1. **Clarify the goal.** Ask area/outcome first, then station/travel limit, total budget, schedule and language/access needs as they become relevant. Include no treatment and consultation-only choices. Do not presume gender, body area or accept a “whole body” package without its exact exclusions. User-raised skin reactions, recent tanning, medicines, prior procedures or pregnancy questions go to clinician assessment; collect no detailed health dossier.
2. **Refresh the facts.** Reopen official safety/consumer sources and search for revisions on every run. Fetch branch-specific scope, device information, price/fees, consent, preparation, aftercare and contract terms. Stored research dates are history. Classify each finding as verified for this question now, provider claim, clinician-dependent or unknown.
3. **Build a small explained shortlist.** Use the reference table. Compare like-for-like areas and an explicit session scenario, including extra-session uncertainty. Balance known total and upfront burden against medical assessment, aftercare access, staffing, ability to complete the course and suitability review. Separate hard language requirements from preferences; exclude unsupported clinics from the eligible shortlist. Compare total course/review travel, confirmed treatment intervals and interpreter costs using the refresh reference; require clinic-approved usable communication before booking. No universal best machine, “five sessions finishes everyone,” ranking by ads, or promised safety. Describe laser/clinic alternatives as consultation topics; the clinician chooses appropriate method/settings with the person.
4. **Let the person choose.** Show the tradeoff of pay-as-you-go versus prepaid courses, likely repeat visits, pain/skin risks and no-treatment alternatives. Require a clinician's suitability/expectations discussion before treatment. Separate consultation choice, treatment choice and clinic choice. Prepare the exact future handoff for review; contact or booking belongs only in a future separately authorized execution.
5. **Support the whole visit.** In a future authorized booking run, follow action-specific transmission/booking approvals in the handoff. Produce directions, bring-list, provider-specific preparation, aftercare, cancellation and follow-up details. Leave pending medical questions explicit; neither a paid course nor attendance proves outcome.

At each turn lead with the next bounded action, briefly show known/unknown state and end with one concrete decision. Favor a short usable plan over a long questionnaire.

## Offline checks

Run `python3 scripts/validate.py` from this skill directory, and repository tests with `python3 -m unittest discover -s tests -v` from the checkout root. [decision.py](scripts/decision.py) checks synthetic extracted flags, cost unknowns and exact consent snapshots; it never executes actions, decides treatment or enforces agent behavior. Read the dry-run protocol for clinical/advertising cases that require an actual agent evaluation.
