# The nakabako vision

SPDX-License-Identifier: CC-BY-4.0

nakabako is an open ecosystem of community-maintained, installable agent playbooks for navigating real-world processes. It makes the requirements, decisions and next steps inside unfamiliar systems understandable and actionable.

**requirements → rules → decisions → sources → forms → actions → follow-up**

This is the maintained vision, not a feature-completion checklist. The [original founding brief](design/original-brief.md) preserves the source vision; the [README](../README.md) describes current capabilities and limitations, and the [architecture decisions](../skills/health-checkup/references/okf/architecture/decisions.md) record the adopted design.

## Help people finish, not just understand

A user should be able to bring an intent—“I need a health checkup in Japan”—and receive help through requirements, provider selection, booking, preparation, results paperwork and follow-up. Finding a clinic is a step, not the outcome.

Japan health-checkup administration is the first proving ground. Healthcare administration, immigration, taxes, moving, schools and other local systems are possible future domains, not current coverage promises. Build reusable capabilities when real workflows justify them, rather than designing a universal framework first.

## Three distinct layers

- **OKF: what is known.** Durable, inspectable, versioned knowledge with sources, applicability and freshness information.
- **Agent Skills: how the agent acts.** Concise workflows, references and deterministic helpers organized around meaningful user intents.
- **Private user state: what is happening now.** A person's documents, choices and progress never belong in the shared knowledge base.

These layers should remain portable and vendor-neutral. The current canonical OKF bundle travels inside the skill so installation preserves its dependencies; that packaging does not erase the conceptual separation.

## Assistance without surrendering control

Ask only what affects the next decision. Inspect supplied documents instead of asking users to transcribe them. Gather the least precise personal information necessary, and distinguish permission to read from permission to transmit.

Optimize for **maximal assistance, not maximal autonomy**. Authentication, CAPTCHA and payment verification are normal human checkpoints. When automation is unavailable, provide a useful manual handoff. Confirm consequential actions and sensitive transmissions without interrupting harmless work unnecessarily.

During Japanese-language takeover, explain procedural meaning as well as words: what a field expects, what a button will do, and what a confirmation commits the user to. Do not strand users at the hardest step or couple this capability to a single browser extension.

## Knowledge that earns trust

Static knowledge is not automatically current truth. Distinguish verified facts, inference and unknowns; preserve source attribution, jurisdiction, effective dates and uncertainty. Fetch highly volatile details such as availability and prices live.

Freshness requires two kinds of work:

1. **Revalidation:** check existing evidence for changes, disappearance and supersession.
2. **Rediscovery:** look for newer, stronger or more applicable authoritative evidence.

An unchanged old page is not proof that its guidance remains current.

After receiving help, users may voluntarily contribute their own model usage to research public-source updates. The output should be a reviewable proposal with evidence—not shared credentials, private case data or automatic publication.

## Open, accessible and deliberately scoped

Knowledge and documentation use CC BY 4.0; software and tooling use MIT, following the [licensing map](../LICENSES.md).

The initial audience is English-speaking adult residents of Japan. The longer-term direction is language-agnostic assistance: non-English speakers should benefit from the same underlying knowledge rather than disconnected factual forks. Other countries and institutions can follow demonstrated needs.

There is no organization-level infrastructure requirement. A future move to `nakabako/playbook-japan` should primarily require repository-link changes.

## What the bootstrap does not prove

The repository is an early test-drive implementation, not production clinical software. Deterministic scenario tests do not prove live model compliance, Japanese OCR accuracy, successful booking or legal/medical correctness. Domain review and real harness evaluations remain necessary. The playbook supports administration and provider instructions; it does not diagnose or prescribe treatment.
