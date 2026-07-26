# Requirements Structure and Routing Model

## Contents

- [Design principles](#design-principles)
- [Starter structure](#starter-structure)
- [Lifecycle states](#lifecycle-states)
- [Primary classifications and destinations](#primary-classifications-and-destinations)
- [Placement algorithm](#placement-algorithm)
- [Clarification gates](#clarification-gates)
- [Stable identifiers](#stable-identifiers)
- [Capability boundary rules](#capability-boundary-rules)
- [Tailoring triggers](#tailoring-triggers)
- [Examples](#examples)

## Design Principles

1. Treat the BRS as one logical baseline, not as a mandatory folder tree.
2. Separate source evidence and working analysis from accepted baseline content.
3. Give every information item one primary home and link to it elsewhere.
4. Use capabilities as the main business decomposition nodes.
5. Route stakeholder, solution, transition, and design information to their owning artifacts.
6. Preserve lineage from source through analysis, baseline, downstream work, and evidence.
7. Expand the physical package only when ownership, reuse, approval, tooling, assurance, access, or review size requires it.

## Starter Structure

```text
requirements/
  README.md
  00-governance.md
  01-purpose-scope-and-overview.md
  02-stakeholders-and-business-structure.md
  03-environment-and-business-model.md
  04-mission-goals-and-objectives.md
  05-information-and-processes.md
  06-cross-cutting-rules-constraints-and-quality.md
  07-operational-concept-and-scenarios.md
  08-lifecycle-and-project-constraints.md
  09-readiness-and-approval.md
  capability-map.md
  glossary.md
  references.md

  capabilities/
    README.md
    CAP-001-<business-ability>/
      README.md
      # rules.md, scenarios.md, models/ only when triggered

  working/
    README.md
    source-register.md
    research-questions.md
    elicitation-log.md
    analysis-register.md
    decisions-and-conflicts.md
    traceability.md
    sources/
      README.md

  downstream/
    README.md

  evidence/
    README.md

  changes/
    README.md
```

Root numbered files contain project-wide BRS information. `capabilities/` contains coherent local business abilities. `working/` contains raw-to-analyzed discovery history, including source material links. `downstream/` points to detailed StRS, SyRS, SRS, transition, and design artifacts. `evidence/` points to approval, delivery, verification, and business-outcome evidence. `changes/` records proposed baseline deltas without editing an approved baseline silently.

The source material folder is deliberately nested under `working/`: possession of a document, quote, or observation does not make its content accepted business intent.

## Lifecycle States

Use explicit transitions:

```text
Raw -> Confirmed -> Analyzed -> Accepted -> Baselined
          |             |
          |             +-> Rejected
          |             +-> Deferred
          |             +-> Open question
          |
          +-> Disputed
```

- `Raw`: captured but not confirmed.
- `Confirmed`: the source agrees the record is accurate, or evidence is authenticated.
- `Analyzed`: classified, normalized, scoped, and checked for implications.
- `Accepted`: authorized business owner or decision authority accepts the item.
- `Baselined`: included in an approved controlled baseline version.
- `Disputed`: sources or authorities disagree.
- `Rejected`: explicitly not adopted; retain rationale and lineage.
- `Deferred`: valid work postponed with owner or revisit condition.
- `Open question`: a material uncertainty prevents completion.

Confirmation is not acceptance. File location is not lifecycle state.

## Primary Classifications and Destinations

| Primary classification | Normal destination | Baseline eligibility |
|---|---|---|
| Raw statement or observation | `working/elicitation-log.md` | No |
| Source or authoritative record | `working/source-register.md`; link or controlled note under `working/sources/` | No by itself |
| Research question | `working/research-questions.md` | No |
| Analysis result | `working/analysis-register.md` | No by itself |
| Decision or conflict | `working/decisions-and-conflicts.md`; accepted effect also updates owning baseline item | Only the accepted business effect |
| Business purpose, problem, opportunity, scope, context | Corresponding project-wide root file | Yes after acceptance |
| Goal, objective, outcome, success measure | `04-mission-goals-and-objectives.md`, or capability page when local | Yes after acceptance |
| Stakeholder or organizational structure | `02-stakeholders-and-business-structure.md`, or capability page when local | Yes after acceptance |
| Business term or fact | `glossary.md`, `05-information-and-processes.md`, or capability page | Yes after acceptance |
| Business capability | `capability-map.md` and `capabilities/CAP-.../README.md` | Yes after acceptance |
| Business rule | Capability page if local; `06-cross-cutting-rules-constraints-and-quality.md` if shared | Yes after authority and applicability are known |
| Business scenario or event | Capability page if local; `07-operational-concept-and-scenarios.md` if end-to-end | Yes after acceptance |
| Operational or project constraint | Relevant root file if initiative-wide; capability page if local | Yes after source and applicability are known |
| Stakeholder requirement | Owning StRS; link in `downstream/README.md` | Summarize only when needed for BRS context |
| Functional solution requirement | Owning SyRS/SRS; link in `downstream/README.md` | No |
| Non-functional solution requirement | Owning SyRS/SRS; link in `downstream/README.md` | Business quality target may be represented separately |
| Transition requirement | Transition specification or plan; link in `downstream/README.md` | Only lifecycle concept summary when material |
| Design candidate or decision | Architecture/design artifact; link in `downstream/README.md` when traceability matters | No |
| Approval, delivery, verification, or outcome evidence | `evidence/README.md` as a controlled link | Referenced, not re-authored |
| Proposed baseline change | `changes/README.md` and a BRS Delta when governed | Only after change approval |

## Placement Algorithm

Apply these tests in order:

1. **Is it a source record or unanalyzed statement?** Keep it in `working/`.
2. **Is its record disputed, rejected, deferred, or still a question?** Keep it visible in `working/`; do not phrase it as baseline truth.
3. **What requirement level owns it?** Route detailed stakeholder, solution, transition, and design content outside the BRS.
4. **Is it business information accepted for the baseline?** Continue.
5. **Does it describe the project or initiative as a whole?** Put it in the mapped root file.
6. **Does it belong to one coherent business ability?** Put it in that capability page.
7. **Does it genuinely govern several capabilities?** Put it in the project-wide cross-cutting root section and link from affected capabilities.
8. **Does it merely repeat an external authority?** Link the stable authoritative identifier and version; do not create a second source of truth.
9. **Does the destination already express the same meaning?** Update or link the existing item instead of duplicating it.

For compound statements, split first and run the algorithm for every resulting item.

## Clarification Gates

Ask or research only the missing facts that can change classification, route, or normative meaning.

| Gate | Questions |
|---|---|
| Source | Who said, observed, measured, or governs this? When and in what context? |
| Authority | Who may approve the outcome, rule, exception, or constraint? |
| Intent | What business problem, outcome, or stakeholder need is behind the wording? |
| Scope | Project-wide, cross-capability, one capability, stakeholder-specific, or solution-specific? |
| Applicability | Which trigger, conditions, population, location, mode, dates, and exceptions apply? |
| Measure | What observation or evidence would show that the outcome or quality target is met? |
| Level | Durable business intent, stakeholder need, permanent solution behavior/quality, temporary transition, or design choice? |
| State | Raw, confirmed, analyzed, accepted, baselined, disputed, rejected, deferred, or open? |

When answers are unknown, capture them as research questions. Do not invent authority or acceptance.

## Stable Identifiers

Use the repository's established scheme when present. Otherwise use monotonic, zero-padded IDs and never recycle them:

| Prefix | Item |
|---|---|
| `SRC-###` | Source |
| `RQ-###` | Research question |
| `EL-###` | Elicitation entry |
| `AN-###` | Analysis item |
| `DEC-###` / `CON-###` | Decision / conflict |
| `OBJ-###` | Goal or objective |
| `CAP-###` | Capability |
| `BR-###` | Business rule |
| `SCN-###` | Scenario |
| `CST-###` | Constraint |
| `TR-###` | Traceability relationship when an explicit row ID is useful |

Inspect all existing IDs before allocating the next one. Never renumber published IDs to close gaps.

## Capability Boundary Rules

A capability answers: **What must the organization be able to do or ensure to produce a business outcome?**

Each capability needs:

- outcome and explicit boundary;
- business owner and participants;
- inputs, outputs, and business information;
- triggering business events;
- normal, alternative, negative, and material boundary scenarios;
- governing rules and constraints;
- dependencies and success evidence;
- links to downstream requirements.

Accept names such as `Determine customer eligibility` or `Manage partner settlement`. Reject technical names such as `Call eligibility API`, `Render settlement screen`, `Write customer row`, or `Run nightly job`.

Create a separate capability only when it has a coherent outcome and boundary and does not duplicate a neighbor. Stop decomposing before child names become technical operations.

## Tailoring Triggers

Split a capability `README.md` into `rules.md`, `scenarios.md`, or `models/` only when at least one trigger exists:

- distinct owner or independent approval;
- reuse across several contexts;
- specialized modeling or requirements tooling;
- assurance, regulation, contract, safety, or audit need;
- access-control or confidentiality boundary;
- page size or review scope materially harms comprehension.

Add a separate rule catalog, event catalog, information model, decision model, process model, state model, or scenario set only when its complexity warrants it. Link it from its owning project-wide or capability scope.

## Examples

### Proposed implementation phrased as a need

Input: `We need a new service that sends an email after approval.`

Split and route:

- verbatim statement -> `working/elicitation-log.md` as `Raw`;
- unresolved business need -> `working/research-questions.md`;
- `send an email` -> functional solution requirement candidate in the owning SRS, linked from `downstream/README.md`;
- any confirmed business outcome such as timely notification -> capability outcome or business quality target, after acceptance.

### Candidate rule with missing authority

Input: `Customer records must be retained for five years.`

Route first to the elicitation log and source register. Clarify governing policy/law, applicable records, start event, exceptions, owner, and effective period. After confirmation and acceptance, place a shared constraint or rule in `06-cross-cutting-rules-constraints-and-quality.md`; link the external authority rather than copying it.

### Capability-local behavior

Input: `An eligible customer may cancel an order until fulfillment starts.`

Potential split:

- business rule defining permission and applicability -> capability page;
- term/state definition for `fulfillment starts` -> capability-local concept or shared glossary;
- negative and boundary scenarios -> capability scenario section;
- UI control or API endpoint, if proposed, -> downstream solution/design artifact.

### Measurable initiative outcome

Input: `Reduce median partner onboarding time from ten days to two days by Q4; the Operations Director owns the target.`

If source and acceptance are established, place the objective and measure in `04-mission-goals-and-objectives.md`, relate it to required capabilities in `capability-map.md`, and add the measurement source to `evidence/README.md` or the objective row.
