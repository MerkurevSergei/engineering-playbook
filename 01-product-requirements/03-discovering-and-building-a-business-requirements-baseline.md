# Discovering and Building a Business Requirements Baseline

> Status: Draft
> Area: product-requirements

## Problem

A Business Requirements Specification is organized for review and approval, not for the order in which knowledge is discovered.

If analysts fill the template from top to bottom, several problems appear:

- stakeholder statements are copied directly into the baseline before they are confirmed or analyzed;
- stakeholder needs are mistaken for business rules;
- scope is fixed before the current state and affected parties are understood;
- a proposed screen, service, or data field becomes the assumed solution;
- detailed stakeholder, solution, and transition requirements are mixed into the BRS;
- rules, scenarios, terms, and constraints are discovered in isolation even though they refine one another;
- the document is declared complete before its value can be measured.

Teams need a repeatable discovery workflow that turns source evidence into a controlled BRS while preserving requirements levels, business ownership, traceability, and iteration.

## Core Idea

Run discovery and specification as two connected loops:

```text
Discovery:
sources -> questions -> elicitation
        -> raw results -> confirmation -> analysis

Specification:
problem and need -> outcome and value -> scope
                 -> capabilities -> scenarios -> downstream requirements
                         |              |
                         +-- governed by rules and constraints
                         +-- uses business information
                         +-- triggered by business events
                         +-- measured by success evidence
                 -> verification -> validation -> approval
```

The loops are not phases in a waterfall. A capability workshop can reveal a missing stakeholder, a scenario can expose a new rule, and a downstream requirement can reveal a gap in the business baseline.

Do not treat an interview statement as an approved requirement. Move information through explicit states:

```text
Raw -> Confirmed -> Analyzed -> Accepted -> Baselined
          |             |
          |             +-> Rejected
          |             +-> Deferred
          |             +-> Open question
          |
          +-> Disputed
```

The BRS is the approved business-level result of this work. Interview notes, observations, research findings, detailed stakeholder requirements, solution requirements, transition plans, and design decisions remain distinct linked information.

## Tailor Discovery and the Baseline Together

Tailoring is part of the discovery workflow, not a separate requirements process. Treat the BRS as one logical baseline and use progressive disclosure: begin with the smallest reviewable form that preserves the applicable business information, then add structure only when complexity, ownership, reuse, tooling, assurance, or review size creates a concrete need.

| Tailoring decision | Start with | Expand when |
|---|---|---|
| Baseline lifecycle | One BRS when no governed baseline covers the affected business boundary | Use a BRS Delta when an existing baseline may change; reference the baseline without changing it when work only realizes or restores approved behavior |
| Capability packaging | One inline business capability when it provides enough context | Add a Capability Map and linked modules when several coherent outcomes, owners, rule sets, or review boundaries emerge |
| Models | Clear narrative and compact tables | Add decision, state, process, information, event, or scenario models when prose hides material combinations, transitions, handoffs, or meaning |
| Physical package | One controlled baseline page and one working page | Split by ownership, reuse, independent approval, specialized tooling, assurance, access control, or review size |
| Traceability | Stable source and downstream links | Add a formal traceability register when regulation, contract, safety, audit, or cross-artifact impact analysis requires it |

Tailoring can change the physical form, level of detail, and supporting models. It must not remove information material to the business decision or blur business requirements with stakeholder, solution, transition, or design information.

## Sources and Standards

| Source | Contribution | Use Here |
|---|---|---|
| [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) and the [IEEE record](https://standards.ieee.org/ieee/29148/6937/) | Business or mission analysis, stakeholder needs and requirements definition, system requirements definition, and BRS, StRS, SyRS, and SRS content | Normative requirements-engineering process and information-item context |
| [BABOK Guide v3](https://www.iiba.org/knowledgehub/business-analysis-body-of-knowledge-babok-guide/) | Planning and Monitoring, Elicitation and Collaboration, Requirements Life Cycle Management, Strategy Analysis, Requirements Analysis and Design Definition, and Solution Evaluation | Business-analysis workflow around the BRS |
| [The TOGAF Standard](https://publications.opengroup.org/standards/togaf) | Business capabilities as a business-architecture view distinct from processes and solution components | Capability-centered decomposition and traceability |
| [IIBA Business Analysis Standard](https://www.iiba.org/knowledgehub/the-business-analysis-standard/) | Accessible task cards for the 30 BABOK tasks and current IIBA requirements classification | Practical task and terminology reference |
| [IIBA Global Business Analysis Core Standard](https://www.iiba.org/globalassets/standards-and-resources/core-standard/iiba-core-standard.pdf) | BACCM, requirements categories, and the six BABOK knowledge areas | Completeness lens for interviews and analysis |
| [IREB Requirements Elicitation](https://cpre.ireb.org/en/concept/requirements-elicitation) | Structured source management, technique selection, conflict resolution, and validation | Elicitation planning and source control |
| [Business Rules Manifesto](https://www.businessrulesgroup.org/brmanifesto.htm) and [OMG SBVR](https://www.omg.org/spec/SBVR) | Rule independence, declarative rules, business vocabulary, and rule validation | Separation of terms, facts, rules, processes, and implementation |
| [GOV.UK user research planning](https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service) and [research analysis](https://www.gov.uk/service-manual/user-research/analyse-a-research-session) | Research questions, iterative rounds, participant selection, and separation of observations from findings | Practical research discipline |
| [NASA Stakeholder Expectations Definition](https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/) | Lifecycle stakeholders, scenarios, ConOps, constraints, and measures of effectiveness | Operational and lifecycle coverage |

ISO supplies the requirements-engineering process and BRS content model. BABOK supplies the analysis workflow and requirements lifecycle. The other sources strengthen elicitation, research, rule, and operational practices. The status model, registers, gates, and physical packaging below are local playbook conventions.

## Reconcile BABOK and ISO Terminology

### Requirements Categories

BABOK classifies requirements by purpose:

| BABOK category | Meaning | Normal destination |
|---|---|---|
| Business requirement | A goal, objective, or outcome that explains why a change is initiated | BRS problem, outcome, success, scope, and capability outcomes |
| Stakeholder requirement | A need of a stakeholder or stakeholder class that must be met to achieve the business requirements | Summarized in the BRS; specified in detail in the StRS |
| Solution requirement | A capability or quality of a solution that meets stakeholder requirements | SyRS or SRS |
| Transition requirement | A temporary capability or condition needed to move from the current state to the future state | Transition plan or a linked transition specification |

The terms do not align one-to-one:

- BABOK uses **business requirement** narrowly for goals, objectives, and outcomes.
- ISO uses **Business Requirements Specification** for a broader information item that includes purpose, scope, stakeholders, environment, processes, policies, rules, constraints, operational concepts, and scenarios.
- An ISO-shaped BRS is therefore not merely a list of BABOK business requirements.

Use the BRS to hold the controlled business context and behavior. Route detailed stakeholder, solution, transition, and design information to their owning artifacts.

### Stated Requirement

The BABOK glossary defines a stated requirement as a requirement articulated by a stakeholder that has not yet been analyzed, verified, or validated. Treat it as a raw source statement:

```text
Stated requirement
        |
        v
Confirmed elicitation result
        |
        v
Classified and analyzed information
        |
        v
Verified and validated requirement or model
        |
        v
Approved baseline element
```

The original statement remains in the Elicitation Log even when the analyzed result is rewritten, split, rejected, or routed outside the BRS.

### BACCM as an Interview Completeness Lens

Use the six Business Analysis Core Concept Model concepts to test whether discovery is balanced:

| BACCM concept | Discovery question |
|---|---|
| Change | What controlled transformation needs to occur? |
| Need | What problem, opportunity, or constraint has potential value? |
| Stakeholder | Who is affected, provides knowledge, receives value, owns rules, or decides? |
| Value | What value is expected, for whom, and how will it be measured? |
| Context | Which internal and external conditions influence the change? |
| Solution | Which possible ways could satisfy the need without prematurely selecting a design? |

BACCM is a reasoning checklist, not a replacement for BRS headings.

## Working Registers

The registers can be tables in one working page, a requirements tool, or separate controlled artifacts. Keep them together for a small initiative and split them only when ownership, reuse, tooling, assurance, or review size justifies it.

### Source Register

| Field | Meaning |
|---|---|
| Source ID | Stable local identifier |
| Source | Stakeholder, document, system, observation, or dataset |
| Authority and version | Owner, role, date, version, or effective period |
| Knowledge or jurisdiction | What this source can authoritatively explain or decide |
| Related questions and capabilities | Discovery scope covered by the source |
| Status | Available, pending, superseded, or inaccessible |

People are not the only requirements sources. Policies, regulations, contracts, analytics, operational records, current systems, and observed work can confirm or contradict interview statements.

### Research Question Backlog

| Field | Meaning |
|---|---|
| Question ID | Stable local identifier |
| Question | A specific uncertainty to resolve |
| Decision affected | Why the answer matters |
| Candidate sources | Who or what can provide evidence |
| Method | Interview, observation, workshop, document analysis, data analysis, or another technique |
| Capability | Local or initiative-wide scope |
| Priority | Blocking, high, normal, or low |
| Status and answer | Open, planned, answered, disputed, or deferred |

Turn an unsupported opinion into a research question instead of copying it into the BRS.

### Elicitation Log

| Field | Meaning |
|---|---|
| Entry ID | Stable local identifier |
| Source and context | Participant or evidence source, date, situation, and technique |
| Raw statement or observation | What was actually said, seen, or measured |
| Evidence | Recording, note, document, metric, case, or link |
| Initial type | Statement, observation, assumption, issue, rule candidate, scenario, or question |
| Confirmation | Raw, confirmed, disputed, or rejected |

Keep observation and interpretation distinct:

```text
Observation    what was seen or measured
Statement      what a participant said
Finding        what the evidence supports
Interpretation the analyst's explanation
```

### Analysis Register

Classify confirmed results as one of:

- problem or evidence;
- goal, objective, outcome, or measure;
- stakeholder need;
- term or business fact;
- scenario;
- business rule;
- constraint;
- assumption;
- dependency;
- risk;
- decision;
- open question;
- stakeholder, solution, or transition requirement candidate;
- design candidate.

Record the source, rationale, capability scope, status, and destination for every accepted item.

### Decision and Conflict Log

| Field | Meaning |
|---|---|
| Decision or conflict ID | Stable local identifier |
| Positions or alternatives | The competing interpretations or options |
| Affected outcomes and capabilities | Business impact |
| Authority | Decision owner and consulted parties |
| Criteria | Value, risk, cost, policy, evidence, or other basis |
| Resolution and rationale | Decision, date, and reason |
| Status | Open, decided, superseded, or deferred |

### Traceability Register

Maintain enough lineage to navigate change and validate value:

```text
Source
  -> stated requirement or observation
    -> confirmed finding
      -> business outcome
        -> capability
          -> BRS rule, scenario, constraint, or decision
            -> StRS / SyRS / SRS / transition requirement
              -> delivery and outcome evidence
```

Do not duplicate entire downstream repositories. Keep stable links, aggregate status, and the evidence needed for impact analysis.

## Capability-Centered Information Model

A business capability answers:

> What must the organization be able to do or ensure to produce a business outcome?

It is a stable business ability, not a summary of one process and not a set of rules with a label. The capability normally remains recognizable when a workflow, team structure, or supporting system changes. People, processes, information, and technology can all contribute to exercising it.

Use these distinctions consistently:

| Element | Question answered | Example |
|---|---|---|
| Business capability | What must the business be able to do? | Determine whether a customer may access an offering |
| Scenario or process | How is the capability exercised in a particular context? | A customer attempts to open a restricted offering |
| Business rule | Which governed condition, permission, prohibition, derivation, or obligation applies? | Only an eligible customer may access the offering |
| Business information | Which business facts does the capability use or produce? | Customer eligibility and offering restrictions |
| Business event | What starts the behavior or changes which behavior applies? | Customer requests access or a restriction becomes effective |
| System requirement | What must a solution do to support the business behavior? | The system shall obtain the customer's current eligibility status |

Treat the capability as the main node of business decomposition and traceability:

```text
Business capability
    = outcome and boundary
    + owner and participants
    + inputs and business information
    + triggering events
    + business scenarios
    + governing business rules
    + constraints and dependencies
    + success evidence
    + links to downstream requirements
```

This expression is a completeness checklist, not a claim that a capability is mechanically derived from its rules. Rules govern and constrain the capability; scenarios demonstrate how it is exercised; information and events supply its business context; system requirements implement the necessary solution behavior.

Use explicit relationships when maintaining formal traceability:

| From | Relationship | To |
|---|---|---|
| Business outcome | `requires` | Capability |
| Capability | `is governed by` | Business rule |
| Capability | `is exercised through` | Scenario or process |
| Capability | `uses` or `produces` | Business information |
| Capability | `is triggered by` | Business event |
| Capability | `is measured by` | Success evidence |
| Scenario | `applies` | Business rule |
| Scenario | `is implemented by` | System requirement |
| Business rule | `is enforced by` | System requirement |

Capabilities can be decomposed into smaller business abilities when each child has its own coherent outcome and boundary. Stop before the names become technical actions such as `Call API`, `Read flag`, `Write record`, or `Display screen`; those are solution responsibilities.

### Add Models Only When Triggered

| Model or artifact | Add it when | Do not use it for |
|---|---|---|
| Context or process model | Several participants, handoffs, approvals, or external parties shape the outcome | Component orchestration or deployment topology |
| Decision table or decision model | Conditions interact, exceptions overlap, or combinations are easy to miss | Repeating a simple rule in tabular form |
| State or lifecycle model | Permitted behavior depends on a business object's state or valid transition | Describing technical job or service states |
| Separate rule catalog | Rules are reused, independently owned, regulated, or have their own lifecycle | Splitting a short initiative into many pages |
| Conceptual information model | Meaning, ownership, validity, or relationships between business concepts drive decisions | Database tables, schemas, or serialization |
| Business event catalog | The occurrence and business consequence matter before a transport mechanism is selected | Defining message topics or payload contracts |
| Detailed scenarios | Important positive, negative, ownership, continuity, or transition paths clarify outcomes | Enumerating every condition combination |

State whether each model applies to one capability or the whole initiative. Keep the model with its owning scope and link it from the logical BRS.

## Recommended Working Directory

The BRS is a logical baseline, not a mandatory folder tree. ISO 29148 does not prescribe this layout. Start with one controlled page and one working page; expand the package only when the tailoring triggers above justify the split.

A small initiative can start with:

```text
<baseline-id>/
  README.md        package identity, owner, status, and navigation
  brs.md           reviewable Business Requirements Specification
  working.md       sources, questions, elicitation, analysis, and decisions
```

When a single page becomes difficult to own or review, evolve toward:

```text
<baseline-id>/
  README.md

  baseline/
    brs.md
    capabilities/
      CAP-01-<capability-name>/
        README.md
        rules.md                 optional split
        scenarios.md             optional split
        models/                  optional decision, state, process, or information models
      CAP-02-<capability-name>/
        README.md
    cross-cutting/
      README.md                  shared rules, scenarios, information, events, and decisions
    models/                      initiative-wide models only

  working/
    source-register.md
    research-questions.md
    elicitation-log.md
    analysis-register.md
    decisions-and-conflicts.md
    traceability.md

  downstream/
    README.md                    links and aggregate status for StRS, SyRS, SRS, and transition work

  evidence/
    README.md                    controlled links to delivery, verification, and outcome evidence
```

Use the directories as ownership boundaries, not as lifecycle stages through which files are copied:

| Location | Fill with | Do not put here |
|---|---|---|
| Root `README.md` | Baseline ID, version, owner, governing baseline, status, entry points, and access notes | Detailed requirements or duplicated registers |
| `baseline/brs.md` | Approved initiative context, outcomes, scope, capability map, cross-cutting concerns, readiness, and approval | Raw notes or detailed solution design |
| `baseline/capabilities/<CAP-ID>/README.md` | One capability's outcome, boundary, owner, participants, information, events, rules, scenarios, evidence, and downstream links | Initiative-wide duplicates or component responsibilities |
| Capability `rules.md`, `scenarios.md`, or `models/` | Material extracted from the capability page because size, reuse, ownership, or tooling requires it | One-file-per-item fragmentation by default |
| `baseline/cross-cutting/` | Behavior that genuinely governs or spans several capabilities | Copies of local or external rules |
| `working/` | Raw, confirmed, disputed, analyzed, rejected, deferred, and open discovery information with source lineage | Content presented as approved merely because it is recorded |
| `downstream/` | Stable links, relationship type, owner, version, and aggregate status of downstream specifications | Copies of downstream repositories |
| `evidence/` | Links to approval, delivery, verification, and outcome evidence with access and retention notes | Uncontrolled sensitive evidence or copied authoritative records |

Fill the package in this order:

1. Create the root identity and the working registers before elicitation.
2. Draft the problem, outcome, success measures, scope hypothesis, stakeholders, and shared vocabulary in `brs.md`.
3. Add the Capability Map, then fill one capability page at a time from confirmed and analyzed information.
4. Move genuinely shared behavior into `cross-cutting/`; do not copy it into every capability.
5. Add downstream and evidence links as those artifacts appear, preserving the capability relationship.
6. Baseline only the reviewable `baseline/` content and its controlled references. Retain working history according to the agreed information-management policy.

If an authoritative policy, rule catalog, evidence store, or downstream specification already exists elsewhere, link to its stable identifier and version. Do not create a second source of truth merely to make the directory look complete.

## How It Works

### 0. Start the Intake and Choose the Baseline Form

Do not choose the baseline form from a ticket title or proposed solution alone. First open an intake entry in the working material and preserve the original request as a source. The choice remains provisional until source review and the sponsor interview confirm it.

1. Capture the original request in its own wording, its source, date, requester, and links to supplied evidence.
2. Hold a short intake conversation with the requester or sponsor. Establish what decision is expected, why it is needed now, what problem or outcome is assumed, which business area is affected, and who may own it.
3. Request the known governing materials: current BRS and deltas, business case or product direction, policies and contracts, process or operating guidance, metrics and incident evidence, and prior relevant decisions. Record each source as available, pending, or unknown; do not wait for every item before continuing.
4. Check the requirements repository or artifact catalog for an existing governed baseline, its exact version, boundary, and owner. Treat screens, APIs, services, data fields, and delivery dates from the request as hypotheses until their business rationale is analyzed.

Choose the baseline approach:

| Finding | Action |
|---|---|
| No governed baseline covers the affected business boundary | Open a new BRS |
| A governed baseline exists and the request may change business intent, outcomes, capabilities, rules, scenarios, or constraints | Open a [BRS Delta](04-working-with-brs-deltas.md) against its exact version |
| A governed baseline already defines the required business behavior and the request only realizes or restores it | Reference the baseline; do not create competing BRS content |

If the evidence is insufficient to choose, record the approach as `Undetermined` and add the missing facts to the Research Question Backlog. Continue planning and source collection, but do not invent a boundary or open a BRS or Delta merely to keep work moving.

A capability module is a packaging decision, not an alternative change lifecycle. Create or modify one within the selected BRS or Delta only when the area has a coherent outcome, boundary, owner, and business behavior. A screen, API, service, database change, or delivery task is not by itself a business capability.

Output:

- preserved copy or versioned reference to the original request;
- expected decision and problem or outcome hypothesis;
- provisional business boundary and business owner;
- requested sources with availability status;
- selected baseline approach and rationale;
- draft baseline ID, or governing baseline and exact base version;
- unresolved intake questions added to the Research Question Backlog.

Exit condition:

> The original request is preserved, initial evidence is requested, and the analyst can justify a new BRS, a BRS Delta, or no baseline change while naming the owner and applicable baseline version; otherwise, the missing decision evidence is explicit.

### 1. Plan the Business Analysis

Apply BABOK Business Analysis Planning and Monitoring:

- plan the analysis approach;
- plan stakeholder engagement;
- define governance;
- define information management;
- define expected analysis outcomes and checkpoints.

Decide:

- who owns and approves the BRS;
- who owns capability and cross-cutting rules;
- who resolves scope, priority, and rule conflicts;
- how interview results are confirmed;
- how information is stored, accessed, retained, and versioned;
- how confidentiality, consent, recordings, and personal data are handled;
- how changes are assessed and approved.

Exit condition:

> Participants know what will be produced, how their information will be used, and who has decision authority.

### 2. Complete Initial Source Collection Before Detailed Elicitation

Review:

- the original request;
- organization strategy and objectives;
- business cases and product visions;
- current BRS baselines and deltas;
- policies, laws, contracts, and standards;
- current process and decision models;
- metrics, analytics, complaints, and incident records;
- existing systems and operational procedures;
- previous decisions, assumptions, and known constraints.

Complete the initial Source Register and expand the Research Question Backlog created during intake.

Do not ask participants to reproduce facts that can be obtained more reliably from authoritative documents or data. Use interview time to interpret, challenge, and complete the evidence.

### 3. Conduct the Sponsor and Business-Owner Interview

Use BACCM to establish the initiative frame:

1. **Need** — What problem, opportunity, or constraint requires attention?
2. **Value** — What result is expected, for whom, and how will it be measured?
3. **Change** — What must change in business behavior or capability?
4. **Context** — Why now, and what external or internal conditions matter?
5. **Stakeholders** — Who is affected, knowledgeable, accountable, or able to block the change?
6. **Solution** — Which solution classes are assumed, and which remain hypotheses?

Also ask:

- Which facts demonstrate the current problem?
- What is the baseline for each proposed success measure?
- What is provisionally in and out of scope?
- Which constraints, risks, and deadlines are already known?
- Which decision will this BRS enable?

Update:

- BRS References and Business Purpose;
- Mission, Goals, and Objectives;
- provisional Business Scope;
- Business Overview when an initiative summary is needed.

Gate:

> The problem is stated without prescribing a screen, API, database, component, or architecture.

### 4. Build the Stakeholder Map

Consider:

- sponsor and final approvers;
- process, policy, rule, and data owners;
- actual users and operators;
- operations, support, and service teams;
- legal, compliance, risk, security, privacy, and audit;
- partners and external parties;
- acquisition, deployment, training, maintenance, and retirement stakeholders;
- affected groups that do not hold decision authority.

For each stakeholder or class, record:

- relation to the need, change, and possible solution;
- expected value;
- knowledge or jurisdiction;
- concerns and constraints;
- influence and decision rights;
- capabilities and research questions they can confirm.

Update Major Stakeholders and Business Structure at initiative level. Keep capability-specific participants in their owning capability module and reflect material interactions in the High-Level Operational Concept.

### 5. Build and Prioritize the Research Question Backlog

Rewrite opinions as answerable questions:

| Weak statement | Research question |
|---|---|
| Customers do not understand the process | At which step do customers stop or seek help, and what evidence explains why? |
| The check is mandatory | Which authority establishes the check, for which cases, and with which exceptions? |
| We need a new service | Which required business behavior is not provided by current capabilities? |
| The process is too slow | What is the current duration distribution, where is time spent, and what outcome requires a different target? |

Prioritize a question as **blocking** when its answer can change:

- the initiative outcome;
- scope or non-goals;
- a mandatory rule or constraint;
- the capability boundary;
- approval of the baseline.

### 6. Plan Elicitation Rounds

Apply the BABOK Elicitation and Collaboration loop:

```text
Prepare -> Conduct -> Confirm
        -> Communicate -> Manage collaboration
```

For every round identify:

- research questions;
- participant classes and sources;
- selected techniques;
- supporting materials;
- expected outputs;
- confirmation approach;
- analysis time;
- decisions enabled by the results.

Choose techniques by the question:

| Need to learn | Preferred techniques |
|---|---|
| Goals, motivation, authority, and concerns | Interview |
| Actual work, workarounds, and environmental constraints | Observation or contextual inquiry |
| Handoffs and shared understanding | Workshop and process modelling |
| Policies, rules, and regulatory constraints | Document analysis plus rule-owner interview |
| Interacting conditions and exceptions | Decision-table workshop |
| Frequency, scale, and performance | Data analysis, case sampling, survey, or benchmarking |
| Future interactions and operational context | Scenarios, ConOps, use cases, or prototype |
| Conflicting interests | Separate interviews followed by a facilitated decision workshop |

Complete a round when its priority questions are answered with confirmed evidence or are recorded as open questions with owners and dates. Do not use an arbitrary interview count as the exit criterion.

### 7. Analyze the Current State

Apply BABOK Analyze Current State.

Determine:

- what triggers and ends the current process;
- who actually participates;
- which activities, decisions, and handoffs occur;
- which information is used and who owns it;
- which rules are documented and which are applied in practice;
- where errors, delays, queues, rework, and workarounds occur;
- which measures exist and what their baselines are;
- where documented and observed behavior differ;
- which organizational, market, regulatory, technology, and lifecycle conditions matter.

Use multiple sources for material findings where practical. A policy can establish authority, observation can show actual behavior, and data can show scale.

Update:

- Business Purpose, Business Overview, and Business Environment;
- Definitions and Information Environment;
- Business Processes;
- current-state context, process, decision, state, or information models when triggered.

Gate:

> The problem and material causes are supported by an authoritative source or corroborated evidence, not only one opinion.

### 8. Define the Future State and Change Strategy

Apply BABOK:

1. Define Future State.
2. Assess Risks.
3. Define Change Strategy.

Determine:

- the necessary future business conditions;
- target outcomes, value, measures, and thresholds;
- affected areas of the enterprise;
- future-state and transition risks;
- candidate solution classes;
- intermediate states;
- organization and operating-model changes;
- preliminary transition requirements.

If solution classes differ materially, perform a separate option or trade-off analysis. Reference the selected class and rationale from the BRS without embedding architecture or design.

Update Mission, Goals, and Objectives; Business Scope; High-Level Operational Concept; and applicable Other Lifecycle Concepts.

Treat scope as provisional until current-state evidence, future-state conditions, stakeholders, and the capability map are coherent.

### 9. Stabilize the Capability Map

For each capability define:

- business outcome;
- owned behavior and explicit boundary;
- business owner;
- affected stakeholders;
- inputs and business information used or produced;
- events that trigger the capability or change its applicable behavior;
- governing business rules and constraints;
- scenarios through which the capability is exercised;
- contribution to initiative value;
- success evidence;
- downstream requirements or specifications that support it, when they exist;
- dependencies on other capabilities.

Gate:

- the capability is named for a business ability, not a component;
- it has a coherent outcome and owner;
- it covers a meaningful part of scope;
- it does not duplicate a neighboring capability;
- the complete map covers in-scope target business behavior.

### 10. Run a Discovery Cycle for Each Capability

#### Prepare

- choose capability research questions;
- identify participants and authoritative sources;
- assemble known terms, facts, scenarios, and models;
- list assumptions to test;
- choose confirmation and validation reviewers.

#### Conduct

Gather:

- stakeholder needs, responsibilities, and concerns;
- current and target behavior;
- terms and business facts;
- normal, alternative, negative, and boundary scenarios;
- decisions, criteria, and exceptions;
- business rules and authoritative sources;
- business information and events;
- outcome measures;
- constraints, assumptions, dependencies, and risks;
- transition concerns;
- decisions and open questions.

All session results begin as `Raw`.

#### Confirm

- play back the result to the source;
- compare it with authoritative documents, data, and other participants;
- identify errors, omissions, ambiguity, and conflicts;
- mark each result `Confirmed`, `Disputed`, or `Rejected`.

Confirmation asks whether the elicitation record is accurate. It does not yet approve the analyzed requirement.

#### Specify and Model

Transform confirmed information into a capability module and the applicable BRS sections:

- Outcome and Boundary;
- Success Evidence;
- Capability Stakeholders and Decision Rights;
- Local Terms and Business Concepts;
- Inputs, Business Information, and Events;
- Capability Rules;
- Capability Scenarios;
- Applicable Models;
- Decisions and Open Questions;
- Local Constraints, Assumptions, Dependencies, and Risks;
- Downstream Requirements and Evidence Links, when they exist.

Route detailed stakeholder, solution, transition, and design information to their owning artifacts.

#### Validate

With business participants and owners, ask:

- Does the capability contribute to the business need and outcome?
- Does it represent the intended target behavior?
- Do rule owners confirm the policies and exceptions?
- Do scenarios cover the contexts that materially change the outcome?
- Is the expected value sufficient to justify the change?

Repeat the cycle while new evidence materially changes the outcome, boundary, main rules, material scenarios, or stakeholder agreement.

### 11. Formalize Business Rules as Independent Governed Knowledge

Discover rules together with processes and scenarios, but manage them as independent business knowledge:

```text
Terms -> Facts -> Decisions and constraints -> Rules
```

Independent does not mean peer to a capability in the decomposition hierarchy. A capability describes the business ability; a rule independently states the governed logic that applies whenever that ability or a related scenario is exercised.

For every rule record:

- a declarative natural-language statement;
- source and authority;
- business owner;
- motivating goal, policy, risk, or obligation;
- scope and applicable capabilities;
- related terms and facts;
- exceptions as separate rules;
- related scenarios and decisions;
- effective date or validity;
- status and version.

Do not classify as a business rule:

- a stakeholder preference;
- a sequence of process steps;
- a UI or API behavior;
- an implementation mechanism;
- an unverified assumption.

A stakeholder need can reveal that a rule must be investigated. It does not automatically establish the rule.

### 12. Perform Cross-Capability Synthesis

After capability cycles:

- move shared rules to Cross-Cutting Concerns;
- build end-to-end scenarios;
- inspect handoffs and ownership gaps;
- define shared business information and events;
- remove duplicated terms, rules, and constraints;
- resolve conflicts between capabilities;
- record initiative-wide constraints, assumptions, dependencies, risks, and decisions.

Update the applicable Information Environment, Business Processes, Operational Policies and Rules, Business Structure, High-Level Operational Concept, and High-Level Operational Scenarios sections.

### 13. Classify and Route Analyzed Results

Assign one primary classification to every accepted item:

| Result | Classification | Destination |
|---|---|---|
| Goal, objective, outcome, or reason for change | Business requirement | BRS |
| Need of a stakeholder or stakeholder class | Stakeholder requirement | StRS; summarized in BRS when needed |
| Permanent function or behavior of a solution | Functional solution requirement | SyRS or SRS |
| Permanent quality or condition of a solution | Non-functional solution requirement | SyRS or SRS |
| Temporary migration, training, continuity, or adoption condition | Transition requirement | Transition plan or specification |
| Governed norm of business behavior | Business rule | BRS or authoritative rule catalog |
| Chosen implementation approach | Design | Architecture or design decision |
| Unanalyzed participant statement | Stated requirement | Elicitation Log |

When one raw statement contains several types, split it into separately traceable analyzed items.

### 14. Verify the BRS

Verification asks:

> Is the business-analysis information represented well?

Check:

- clarity and unambiguity;
- consistency;
- completeness for the tailored scope;
- feasibility;
- verifiability;
- correct classification;
- consistent terminology;
- model correctness;
- backward and forward traceability;
- absence of hidden design;
- absence of avoidable duplication.

Verification is primarily an analytical quality review. It does not establish that the BRS describes the right change.

### 15. Validate the BRS

Validation asks:

> Does this baseline describe the right change and sufficient value?

Check:

- alignment to the business need;
- contribution of every capability to outcomes;
- adequacy of success measures;
- coverage of key stakeholder needs and contexts;
- suitability of scope and non-goals;
- consistency with authoritative rules and constraints;
- expected value relative to risk and change cost;
- absence of capabilities that do not contribute to the stated outcome.

Use business-owner playback, scenario review, model walkthroughs, evidence review, and option analysis as appropriate.

### 16. Prioritize Without Weakening Mandatory Content

Prioritize:

- outcomes;
- stakeholder needs;
- capabilities;
- scenarios;
- open questions;
- proposed changes.

Do not apply ordinary feature priority to every item:

- a law or contractual obligation is mandatory within its applicability;
- a business rule is classified by authority, criticality, and effective date;
- a constraint is mandatory while it applies;
- an assumption requires validation;
- a risk requires a response decision;
- a transition requirement has a limited period of applicability.

### 17. Resolve Conflicts

For each conflict record:

- competing positions or interpretations;
- sources and authority;
- affected outcomes and capabilities;
- alternatives and trade-offs;
- decision criteria;
- decision owner;
- resolution and rationale.

Resolve conflicts that block outcome, scope, mandatory rules, capability boundaries, or required behavior before baseline approval. Non-blocking conflicts may remain visible with owners and decision dates.

### 18. Approve and Establish the Baseline

Apply BABOK Approve Requirements through:

- capability playback;
- cross-capability review;
- rule-owner review;
- business-owner review;
- approve, reject, or revise decisions;
- revision history;
- baseline version and status.

Only accepted information enters the approved BRS. Raw, merely stated, disputed, or unvalidated requirements cannot silently become normative.

### 19. Maintain and Change the Baseline

Apply BABOK Requirements Life Cycle Management:

- trace requirements;
- maintain requirements;
- prioritize requirements;
- assess requirements changes;
- approve requirements.

After approval:

- propose local changes through a BRS Delta;
- assess shared-rule and scope changes across all affected capabilities;
- preserve source, rationale, identifiers, and history;
- trace downstream changes back to the governing baseline;
- do not delete superseded meaning without version history.

### 20. Close the Value Loop Through Solution Evaluation

After implementation:

- measure actual performance and value using BRS success measures;
- compare baseline, target, and observed results;
- assess solution limitations;
- assess enterprise and operating-model limitations;
- recommend corrective actions;
- create a BRS Delta when business intent, rules, scope, or outcomes need to change.

Solution Evaluation is outside initial BRS authoring, but it is the evidence that the approved business outcome was or was not achieved.

## Quality Gates

A BRS is ready for approval when:

- [ ] **Need** — The problem, opportunity, or constraint is supported by evidence.
- [ ] **Value** — Outcomes have owners, measures, baselines, and targets where meaningful.
- [ ] **Change** — The required business transformation is understandable.
- [ ] **Context** — Material internal, external, operational, and lifecycle conditions are represented.
- [ ] **Stakeholders** — Relevant classes, sources, rule owners, and decision rights are covered.
- [ ] **Capability** — The capability map covers scope using business outcomes rather than solution components, and each capability has enough information, events, rules, scenarios, and evidence to explain the ability.
- [ ] **Source** — Every material element has a source or explicit rationale.
- [ ] **Classification** — Business, stakeholder, solution, and transition requirements are not mixed.
- [ ] **Rule** — Rules are declarative, scoped, sourced, and confirmed by their owners.
- [ ] **Scenario** — Normal, alternative, negative, and material boundary contexts are covered.
- [ ] **Traceability** — Downstream requirements can trace to sources, outcomes, rules, constraints, or decisions.
- [ ] **Verification** — The representation is clear, consistent, feasible, and appropriately complete.
- [ ] **Validation** — The baseline addresses the business need and expected value.
- [ ] **Conflict** — Blocking conflicts are resolved and remaining questions have owners and dates.
- [ ] **Decision** — The business owner can approve, reject, or reshape the initiative.

## Why Source Order Can Be Misleading

- ISO 29148 defines process outcomes and information-item content. BRS section 9.3 is not an interview script or authoring sequence.
- The BRS template is organized for reading and approval. Its headings are not the order in which facts must be discovered.
- BABOK groups tasks by knowledge area, but analysis tasks are tailored, iterative, and often concurrent. Its chapter order is not a mandatory lifecycle.
- BABOK business requirements are narrower than the complete ISO BRS information item.
- Stakeholder planning occurs before most elicitation even though the template's stakeholder section follows problem, outcome, and scope.
- Scope begins as a hypothesis and stabilizes only after current-state, future-state, stakeholder, risk, and capability analysis.
- Rules and scenarios are discovered together, but rules remain independent from processes and technical enforcement.
- Transition requirements are temporary and should not be converted into permanent business rules.
- Solution Evaluation occurs after the initial BRS, but the BRS must define success evidence early enough to enable it.

## Common Mistakes

- Filling the BRS template from top to bottom as a questionnaire.
- Treating an interview statement as an approved requirement.
- Interviewing only the sponsor or only current users.
- Asking stakeholders for facts that authoritative documents or data can answer more reliably.
- Converting a stakeholder need into a business rule without a governing source or owner.
- Treating a capability as merely the sum of its rules or naming one after a technical function.
- Keeping a flat initiative-wide list of rules and scenarios after coherent capability boundaries have emerged.
- Using one generic `In Progress` status for elicitation, analysis, approval, delivery, and value realization.
- Treating provisional scope as final before current-state and capability analysis.
- Mixing transition requirements with durable target behavior.
- Writing system functions, interfaces, data structures, or components into the BRS.
- Confirming interview notes but skipping verification and business validation.
- Prioritizing a mandatory obligation as though it were an optional feature.
- Approving a document that has success metrics but no data source or baseline.
- Closing discovery without preserving source statements, conflicts, and decision rationale.
- Declaring success at release without evaluating the business outcome.

## Interview Angle

> I do not fill the BRS as a questionnaire. I use BABOK to plan the analysis, manage elicitation, analyze current and future states, classify and trace requirements, and verify and validate the result. I use ISO 29148 as the BRS coverage model and business capabilities as the main decomposition and traceability nodes. Interview statements stay raw until confirmed and analyzed; business rules govern capabilities and require business authority; stakeholder, solution, transition, and design information is routed to the appropriate downstream artifact. The approved BRS then provides the measures used to evaluate whether the delivered change created the intended value.

## Related Topics

- [Choosing the First Requirements Artifact](01-choosing-the-first-requirements-artifact.md)
- [Business Requirements Specification standard](02-business-requirements-specification-standard.md)
- [Working with BRS Deltas](04-working-with-brs-deltas.md)
- [Requirements discovery techniques](requirements-discovery-techniques.md)
- [System boundary checklist](system-boundary-checklist.md)
- [Product and Requirements index](README.md)
