# Original founding brief

SPDX-License-Identifier: CC-BY-4.0

> Historical design context, not active execution instructions or a claim of completed features. This is the original Markdown brief supplied by Caio Lins, preserved verbatim below. The title, license notice and context block were added for archival use.
>
> See the [maintained vision](../vision.md), [current README](../../README.md), and [adopted architecture decisions](../../skills/health-checkup/references/okf/architecture/decisions.md). Later decisions include session-only state by default, opt-in minimal private checkpoints, an English-first adult-resident audience with a language-agnostic direction, and packaging canonical OKF inside the installable skill.
>
> The proposed tree and requested deliverables below record original intent, not necessarily the implemented layout or release status. Examples are illustrative, not current medical or administrative guidance.

---

You are helping me architect and bootstrap an open-source repository named:

`nakabako-playbook-japan`

Always write **nakabako** in lowercase.

This repository is the first implementation of a broader idea, but there is no GitHub organization yet.

In the future, if a `nakabako` organization is created, this repository may become:

`nakabako/playbook-japan`

Design things so that migration would be straightforward, but do not build unnecessary organization-level infrastructure now.

# What nakabako is

nakabako is an open ecosystem of community-maintained, installable agent playbooks for navigating real-world processes.

Many important parts of everyday life behave like black boxes:

- healthcare administration
- government procedures
- immigration
- driver's licenses
- taxes
- insurance
- moving
- utilities
- schools
- employment bureaucracy
- local administrative systems

nakabako exposes the inside of those boxes:

requirements → rules → decisions → sources → forms → actions → follow-up

The goal is not merely to explain processes.

The goal is to help agents guide users through them end to end.

Japan is the first playbook and proving ground.

Future playbooks may cover other countries, cities, communities, or institutions.

Do not prematurely build a universal framework, but avoid architecture that unnecessarily assumes Japan is the only possible playbook.

# Core architecture

Use two complementary concepts from the beginning:

## Open Knowledge Format, OKF

Use OKF for durable, inspectable knowledge.

Examples:

- how a Japanese procedure generally works
- terminology
- legal/administrative concepts
- relationships between requirements
- architecture decisions
- authoritative sources
- applicability
- provenance
- freshness information

Use the current OKF specification. Inspect the current upstream specification before implementing rather than relying on assumptions from this prompt.

OKF should remain:

- human-readable
- agent-readable
- git-versioned
- portable
- vendor-neutral
- inspectable without proprietary tooling

## Agent Skills

Use Agent Skills for executable behavior.

Examples:

- interview the user
- determine what process applies
- research current rules
- inspect documents
- search providers
- navigate websites
- compare options
- assist with forms
- handle browser handoff
- interpret confirmations
- coordinate follow-up

Use current Agent Skills conventions and Vercel Labs `skills` / skills.sh compatibility where appropriate.

Inspect the current tooling and conventions before implementation.

Prefer:

- concise `SKILL.md`
- references
- schemas
- scripts for deterministic tasks
- scenario tests
- OKF-backed knowledge

over giant monolithic prompts.

Mental model:

**OKF = what is known**

**Skill = how the agent acts**

**User state = what is happening to this particular user right now**

Do not mix private user state into the shared OKF knowledge base.

# Licensing

This repository will contain both knowledge/content and possibly software/scripts/tooling.

Use a dual-license approach:

- **CC BY 4.0** for knowledge, documentation, OKF content, prose, procedural guides, annotations, and other primarily textual/knowledge artifacts
- **MIT** for software, scripts, tooling, schemas/code generators, automation helpers, and executable code

Set this up clearly from the beginning.

Include files such as:

- `LICENSE-content`
- `LICENSE-software`

or another equally clear structure.

Document the split prominently in the README and contributor guidance.

The intent is:

- knowledge should be freely reusable, modifiable, and redistributable with attribution
- software/tooling should be permissively reusable under MIT

If some files contain both significant executable code and substantive knowledge content, establish a clear convention for which license applies and document it.

Do not leave licensing ambiguous.

# Repository philosophy

Do not create hundreds of tiny skills simply because the bureaucracy has hundreds of branches.

A skill should generally correspond to:

- a meaningful user intent, or
- a genuinely reusable agent capability

not every form, field, rule, or sub-step.

For example:

`health-checkup`

is a reasonable skill.

Separate skills for every possible health-check package or individual form field probably are not.

Shared factual knowledge should live in OKF rather than being duplicated across skills.

# Ask me important questions first

Before implementation, inspect this prompt and identify architectural choices that genuinely matter.

Ask me about those choices before building.

Grill me where necessary.

However:

- do not ask trivial questions
- do not ask about easily reversible implementation details
- do not ask questions with an obvious sensible default
- do not make me design things you can reasonably decide yourself

Group questions where possible and briefly explain why they matter.

After I answer, continue into implementation.

# First production workflow

The first complete skill is:

# Health Checkup Management in Japan

A user should be able to say:

> I need to do a health checkup in Japan.

The skill should help manage the entire process.

Do not reduce this to:

> Find a clinic.

Research the real lifecycle and identify important stages I have missed.

At minimum consider:

1. understand why the user needs the checkup
2. determine which type of checkup actually applies
3. inspect employer, school, municipality, insurer, or other requirements
4. identify legally or administratively required examination items
5. verify current rules
6. determine eligibility for subsidies or public programs
7. progressively gather user preferences
8. search suitable providers
9. compare providers
10. choose the correct examination/package
11. assist with booking
12. handle authentication and bot protection
13. support human takeover
14. help the user understand Japanese-only booking interfaces
15. understand booking confirmation
16. extract pre-appointment instructions
17. manage fasting or sample instructions where applicable
18. identify documents/items to bring
19. appointment-day guidance
20. payment/reimbursement considerations
21. understand result delivery
22. understand administrative implications of results
23. handle required certificates
24. employer/school submission where applicable
25. required follow-up examinations
26. reminders and deadlines

Do not assume this list is complete.

Research the actual workflow before finalizing the model.

# Progressive interaction

Do not begin with a giant questionnaire.

Ask only for information that materially affects the next decision.

Potential inputs include:

- purpose of checkup
- employer/school documentation
- municipality
- age when relevant
- sex when medically or administratively relevant
- insurance situation
- required tests
- deadline
- budget
- preferred dates
- nearest station or area
- acceptable travel time
- English support
- accessibility requirements
- clinician gender preference if the user cares
- result turnaround requirements
- English-language result/certificate requirements

When the user supplies a Japanese document, PDF, screenshot, email, or form, inspect that rather than asking them to manually re-enter information that can be extracted.

# Current knowledge and authoritative sources

Static repository knowledge must never automatically be treated as current truth.

For information that may change, verify it at runtime.

Preferred source hierarchy should generally be:

1. Japanese national government or ministry
2. prefecture or municipality
3. official public agency / health insurer
4. requesting employer, school, or institution
5. clinic/hospital official source
6. reputable specialist secondary source
7. community reports only as supplementary evidence

Distinguish clearly between:

- verified
- strongly inferred
- unknown

Do not present inference as fact.

# Provenance and freshness

This is a core nakabako requirement.

Important factual OKF knowledge derived from external authorities should preserve sufficient provenance to determine:

- where it came from
- who published it
- when it was retrieved
- which jurisdiction it applies to
- when it became effective, if known
- whether it has been superseded
- how volatile it is
- when it was last verified
- how often it should reasonably be reviewed

Use stable identifiers for important knowledge statements where practical.

Conceptually, metadata may include information such as:

```yaml
id: jp.healthcheck.periodic.required-items

source:
  url: ...
  publisher: ...
  source_type: official
  jurisdiction: Japan
  language: ja

freshness:
  retrieved_at: ...
  last_verified_at: ...
  effective_from: ...
  effective_until: ...
  review_interval: ...
  volatility: mutable

status:
  state: active
  superseded_by: null
```

Do not blindly use this exact schema if OKF provides a better native representation.

Use the current OKF specification and design the cleanest compatible approach.

# Knowledge refresh architecture

nakabako knowledge should be maintainable over time.

Eventually, users who receive value from a nakabako skill should be able to voluntarily contribute compute/model usage to help keep the shared knowledge fresh.

They should NOT share API keys, authentication tokens, or credentials.

The intended model is:

1. user runs a nakabako skill
2. workflow succeeds
3. nakabako can optionally suggest helping refresh relevant knowledge
4. update work runs using the contributor's own agent/model quota
5. the result is a proposed knowledge update
6. evidence and provenance are included
7. changes can become a normal open-source contribution / PR
8. maintainers or CI review before shared knowledge changes

Build the architecture so this is possible later.

Do not necessarily implement the complete contribution pipeline in the first version unless it falls out naturally.

## Important: refresh must not merely revisit old URLs

This is critical.

A knowledge refresh has TWO responsibilities:

### Source revalidation

Check existing sources:

- do they still exist?
- have they changed?
- have effective dates changed?
- have they been marked obsolete?
- do they redirect?
- have they been superseded?

### Source rediscovery

Search again for the best current authority.

Look for:

- newer official pages
- replacement ministry guidance
- revised legislation/regulations
- newer PDFs
- more specific municipal guidance
- newly authoritative sources
- sources that supersede previously stored evidence

Never treat:

> old source is unchanged

as equivalent to:

> knowledge is still current.

A knowledge item should only be considered freshly verified when the updater has also looked for newer, stronger, more specific, or superseding authoritative evidence.

Allow source states such as:

- active
- superseded
- deprecated
- unavailable
- disputed

where useful.

# Knowledge volatility

Different information should have different freshness strategies.

For example:

## Relatively stable

- terminology
- broad lifecycle structure
- conceptual relationships

May be reviewed infrequently.

## Mutable

- legal requirements
- municipal eligibility rules
- ministry guidance
- required examination items

Should be periodically reverified.

## Highly volatile

- clinic pricing
- appointment availability
- opening hours
- package availability

These generally should NOT be treated as durable OKF truth.

Fetch them live when the skill runs.

Design accordingly.

# Privacy and PII

nakabako should minimize unnecessary exposure of personal information.

Use progressive disclosure.

For location, for example:

country
→ prefecture
→ city
→ neighborhood/station
→ postal code
→ exact address

Do not request exact home addresses when station or municipality is enough.

Distinguish between:

> the agent knowing a value

and

> transmitting that value to another party.

Before sensitive information is transmitted, the user should understand what is being sent, where, and why.

Potentially sensitive data includes:

- exact address
- date of birth
- phone number
- medical details
- insurance identifiers
- My Number
- passport information
- residence-card information
- payment information

Do not store user-specific sensitive data in shared OKF.

# Browser execution

Different harnesses have different capabilities.

Do not assume that browser automation always exists or always works.

Model execution as a capability ladder.

Preferred order where appropriate:

1. structured API / plugin / site-native tool
2. browser automation
3. browser automation + human takeover
4. local browser handoff
5. guided manual completion

Optimize for:

**maximal assistance, not maximal autonomy**

A workflow is still successful if the agent does 90% of the difficult work and the user completes the final authentication or protected step.

# Authentication and bot protection

Expect:

- CAPTCHA
- Cloudflare / anti-bot systems
- SMS OTP
- email OTP
- passkeys
- Face ID / Touch ID
- payment verification
- government authentication

Treat these as normal human checkpoints rather than exceptional failure states.

For example:

1. agent finds the correct booking flow
2. agent fills safe fields
3. anti-bot challenge appears
4. user takes over
5. user authenticates
6. agent resumes afterward if possible

# Human takeover and semantic translation

This is a major requirement.

Users may need to take over a Japanese website when:

- bot protection blocks the agent
- authentication is required
- payment is required
- the user must confirm something personally
- browser automation is unavailable

They should not suddenly be stranded inside a Japanese-only interface.

Generic browser/page translation may sometimes break interactive websites.

Therefore nakabako should model a capability for:

# semantic translation during takeover

The underlying page should remain functional.

Possible implementations include:

- browser-native translation when safe
- browser extension
- content-script overlay
- side panel
- element-level annotations
- agent-guided field-by-field help

Do not couple the core health-checkup skill to one specific implementation.

The translation capability should be able to explain:

- labels
- fields
- buttons
- dropdown options
- validation errors
- warnings
- confirmation screens
- instructions

And it should provide PROCEDURAL meaning, not merely literal translation.

Example:

`受診票`

A generic translator may say:

> examination ticket

nakabako should understand the process and provide something more useful, such as:

> Health-check form. You may need to complete this before the appointment and bring it with you.

Another example:

`保険証番号`

nakabako should be able to explain what identifier is expected and warn the user not to substitute a different sensitive identifier such as My Number unless the site explicitly requests it.

This procedural translation is part of the core product idea.

# Consequential actions

Require appropriate confirmation before actions such as:

- submitting a booking
- cancelling
- paying
- sending sensitive information
- submitting employer forms
- submitting government forms

Do not repeatedly interrupt the user for harmless, reversible operations.

# Provider discovery

When searching clinics, derive queries from the user's actual needs rather than doing generic searches.

Collect structured information where useful:

- provider
- branch
- location
- travel time
- checkup/package
- included tests
- exclusions
- price
- English support
- booking method
- opening hours
- result turnaround
- certificate capability
- payment methods
- caveats
- source URL
- source freshness

Do not infer "English friendly" merely from the existence of an English landing page when stronger evidence can be found.

Separate:

- verified
- likely
- unknown

Present a useful shortlist rather than dumping dozens of results.

Avoid universal opaque scoring.

Explain tradeoffs based on the user's actual priorities.

# User workflow state

Model workflow state separately from OKF.

Examples:

- user's goal
- determined checkup type
- required tests
- unresolved questions
- provider shortlist
- selected provider
- appointment date
- preparation requirements
- pending forms
- result status
- follow-up required

Decide carefully whether state belongs in:

- session
- a local/private file
- harness memory
- another private state mechanism

If this decision materially affects the initial architecture, ask me.

# Testing

Use scenario-based tests.

At minimum cover:

### Ambiguous request

User only says:

> I need a health check.

### Employer requirements

User provides a Japanese employer document listing required examination items.

### Municipal program

User may qualify for a city/ward screening program.

### English requirement

User wants a provider with reliable English support.

### Japanese-only booking

User needs help navigating a Japanese-only form.

### Bot protection

Browser automation is blocked and the workflow falls back to human takeover.

### Sensitive PII

A form requests personal identifiers.

### Stale knowledge

Existing OKF knowledge conflicts with a newer official source.

### Superseded source

The old official page still exists, but newer authoritative guidance has replaced it.

### No browser automation

The user's harness cannot interact with the website.

### Post-booking

The user receives Japanese preparation instructions.

### Follow-up

Results require additional examination or administrative action.

Tests should validate behavior, not merely static prompt contents.

# Possible repository shape

Do not blindly implement this tree if your research suggests a cleaner structure.

Conceptually, I expect something in this direction:

```text
nakabako-playbook-japan/
├── README.md
├── LICENSE-content
├── LICENSE-software
├── skills/
│   └── health-checkup/
│       ├── SKILL.md
│       ├── references/
│       ├── schemas/
│       └── scripts/
│
├── knowledge/
│   └── okf/
│       ├── health/
│       ├── terminology/
│       ├── sources/
│       └── architecture/
│
├── tests/
└── docs/
```

Shared capabilities may eventually emerge, such as:

- source verification
- knowledge refresh
- PII handling
- browser handoff
- semantic translation

Do not prematurely split every capability into its own top-level skill unless reuse justifies it.

# Scope

The first goal is to make the Japan health-checkup workflow genuinely useful.

Do not spend most of the implementation designing hypothetical infrastructure for future countries.

When reusable abstractions naturally emerge, capture them cleanly.

The repository should remain understandable without relying on one specific model vendor.

# Deliverables

After asking me the necessary architecture questions and receiving my answers:

1. initialize `nakabako-playbook-japan`
2. inspect and adopt the current OKF specification
3. inspect and adopt current Agent Skills / Vercel Labs skills conventions where useful
4. set up the CC BY 4.0 / MIT licensing split clearly
5. document key architecture decisions
6. create the first OKF-backed Japan health-check knowledge
7. preserve provenance and freshness metadata
8. create the health-checkup Agent Skill
9. create privacy/PII conventions
10. create source verification and rediscovery conventions
11. design the knowledge-refresh mechanism
12. design browser capability and human-handoff behavior
13. design semantic translation during takeover
14. add representative scenario tests
15. add README and contributor documentation
16. make installation through modern Agent Skills tooling practical where possible

At the end, show me:

- repository tree
- major architecture decisions
- assumptions made
- open questions
- licensing structure
- how to install the health-checkup skill
- one realistic end-to-end example
- how knowledge provenance/freshness works
- how a future contributor could help refresh stale knowledge using their own compute
