# Business Requirements Specification Template

> Status: Draft
> Area: product-requirements

Use this template to create a controlled business-level requirements baseline that is complete enough for the initiative without becoming a system specification.

The coverage model follows [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html), especially the general information-item content in section 9.2 and the BRS content in section 9.3. The standard defines required information and content; it does not require every initiative to use the same physical file or heading structure. The prompts below are an original working interpretation, not a reproduction of the standard. Consult the licensed standard when formal conformance is required.

Practical additions come from Karl Wiegers and Joy Beatty's Vision and Scope approach described in [Software Requirements, Third Edition](https://www.microsoftpressstore.com/store/software-requirements-9780735679610) and the working materials available from [Software Requirements Essentials](https://softwarereqs.com/).

Read [Choosing the First Requirements Artifact](01-choosing-the-first-requirements-artifact.md) for the artifact decision and [Tailoring the Business Requirements Baseline](02-tailoring-the-business-requirements-baseline.md) for guidance on conditional models and physical organization.

## How to Use This Template

1. Preserve the original business request and authoritative evidence as linked sources.
2. Complete the core sections below for a typical initiative. For a small governed change, record a [BRS Delta](04-working-with-brs-deltas.md) and link to the governing baseline.
3. For a small initiative, use one inline capability and omit the separate Capability Map when it adds no navigation value.
4. For a larger initiative, assign every local rule and scenario to a business capability. Store only shared behavior in Cross-Cutting Concerns and link external rules without copying them.
5. Add a conditional model only when its trigger applies and state whether its scope is one capability or the whole initiative.
6. Keep the baseline on one page by default. Split information only when it is reused, independently owned or approved, tool-managed, or too large to review effectively.
7. Keep business outcomes and observable behavior separate from system responsibilities, interfaces, data structures, and architecture.
8. For regulatory, contractual, safety-relevant, or audit-sensitive work, complete the ISO coverage register and record evidence or a justified `Not applicable` decision for every concern.

Do not call a tailored profile `BRS-lite` as though that were an external standard. Document the local tailoring decision instead.

## Identifier Conventions

Stable identifiers are useful when an element is referenced from another artifact, backlog item, test, rule catalog, or decision record. They are optional when the baseline is small and self-contained.

| Example | Meaning | Origin |
|---|---|---|
| `BRS-initiative-key` | Logical baseline identifier | Local convention |
| `BO-1`, `SM-1`, `RI-1`, `FE-1` | Objective, metric, risk, and major feature | Wiegers-style convention |
| `CAP-01` | Business capability within the initiative | Local convention |
| `BR-CAP01-01`, `SC-CAP01-01` | Capability rule and local scenario | Local convention |
| `BR-CROSS-01`, `SC-E2E-01` | Cross-cutting rule and end-to-end scenario | Local convention |

Declare every organization-specific prefix before using it.

Copy from the heading below, replace each italic prompt, and remove conditional modules that do not apply.

---

# Business Requirements Specification: _[Initiative name]_

## 1. Baseline Identification and Sources

| Field | Value |
|---|---|
| Baseline ID | _[Stable ID when external traceability is needed]_ |
| Version and status | _[Draft, In Review, Baselined, or Superseded]_ |
| Business owner | _[Name or accountable role]_ |
| Analyst or author | _[Name or role]_ |
| Created / updated | _[Dates]_ |
| Target decision date | _[Date]_ |

### Executive Summary

_[In three to five sentences, state the problem or opportunity, desired outcome, business boundary, and decision this baseline enables.]_

### Authoritative Sources

| Source | Authority and version | Relationship |
|---|---|---|
| _[Original request or evidence]_ | _[Owner, date, or version]_ | Source input |
| _[Policy, regulation, business case, or model]_ | _[Authority and version]_ | Governing or supporting |

Preserve the original request. Record analyzed statements separately instead of silently rewriting the source.

## 2. Problem and Current Context

### Problem or Opportunity

_[Describe the undesirable current state or opportunity without prescribing a service, screen, field, API, or database change.]_

### Current Behavior and Evidence

_[Describe how the business works today, where the problem appears, who is affected, and which facts or observations support the need for change.]_

### Reason to Act Now

_[State the event, obligation, risk, or value opportunity that makes the initiative timely.]_

## 3. Desired Outcome and Success

### Desired Business Outcome

_[Describe the required change in business capability, customer outcome, risk, compliance, cost, or performance.]_

### Objectives and Success Measures

| Objective or outcome | Measure and target | Evidence source | Owner and date |
|---|---|---|---|
| _[Measurable result]_ | _[Baseline, target, or acceptance threshold]_ | _[Authoritative data source]_ | _[Owner and target date]_ |

Use identifiers such as `BO-1` and `SM-1` only when the elements need to be referenced elsewhere.

## 4. Scope and Non-Goals

### In Scope

- _[Business capability, behavior, process, policy, population, or channel changed by this initiative]_

### Out of Scope

- _[Explicit non-goal or behavior this initiative does not change]_

### Existing Baseline or Deferred Scope

_[Link to governing requirements and identify later-release scope when relevant.]_

Describe scope through business behavior before naming components. Component impact is determined during system analysis and architecture.

## 5. Initiative Stakeholders and Decision Rights

| Stakeholder or class | Need or expected value | Concerns or constraints | Decision rights |
|---|---|---|---|
| _[Role, group, or external party]_ | _[Need or value]_ | _[Concern, conflict, or limitation]_ | _[Approve, decide, consult, or inform]_ |

Include sponsors, final approvers, and parties whose concerns apply to the initiative as a whole. Put capability-specific participants and rule owners inside the relevant Capability Specification.

Record stakeholder requirements separately when they need detailed treatment. Do not turn every stakeholder need into a system requirement inside the BRS.

## 6. Shared Terms and Business Concepts

| Term or concept | Business meaning | Owner or authoritative source |
|---|---|---|
| _[Domain term]_ | _[Unambiguous definition]_ | _[Owner or link]_ |

Include only terms used across the initiative. Put capability-specific concepts inside the relevant Capability Specification. Add acronyms when they are not obvious to the intended readers.

## 7. Target Business Behavior and Capability Map

### Target State

_[Describe the intended observable behavior and business responsibilities without assigning them to services or components.]_

### Capability Map

| ID | Capability | Business outcome | Owner | Specification |
|---|---|---|---|---|
| `CAP-01` | _[Stable business capability]_ | _[Outcome or risk controlled]_ | _[Business owner]_ | _[Inline section or link]_ |

A capability is a stable business slice with a coherent outcome, boundary, and rule set. It is not a screen, API, service, database change, or delivery task.

For a single-capability initiative, omit this index when the Capability Specification immediately below provides sufficient navigation. Identifiers such as `CAP-01` and `FE-1` are optional local and Wiegers-style aids, not ISO identifiers.

## 8. Capability Specifications

Repeat this block for each capability in the Capability Map. Do not repeat initiative-level context inherited from earlier sections.

### Capability: `CAP-01` — _[Capability name]_

#### Outcome and Boundary

_[State the concrete business outcome produced by this capability, the behavior it owns, and the behavior explicitly outside its boundary.]_

#### Success Evidence

| Measure or acceptance signal | Target | Evidence source | Owner |
|---|---|---|---|
| _[Capability-level success evidence]_ | _[Target or threshold]_ | _[Authoritative source]_ | _[Owner]_ |

#### Capability Stakeholders and Decision Rights

| Participant or owner | Need or responsibility | Concern | Decision rights |
|---|---|---|---|
| _[Capability-specific role]_ | _[Need, value, or rule ownership]_ | _[Concern or conflict]_ | _[Decide, approve, consult, or inform]_ |

#### Local Terms and Business Concepts

| Term or concept | Business meaning | Owner or authoritative source |
|---|---|---|
| _[Capability-specific term]_ | _[Unambiguous meaning]_ | _[Owner or link]_ |

Omit this subsection when all required language is already defined in Shared Terms and Business Concepts.

#### Capability Rules

| ID | Rule | Source and owner | Exceptions or notes |
|---|---|---|---|
| `BR-CAP01-01` | _[Declarative permission, prohibition, calculation, derivation, or obligation]_ | _[Authority and owner]_ | _[Exception or unresolved case]_ |

A capability rule applies only within this capability. Put a rule that governs several capabilities in Cross-Cutting Rules. Keep an external policy or catalog rule under its authoritative identifier and link to it instead of copying or renaming it.

#### Capability Scenarios

| ID or name | Trigger and context | Business outcome | Rules or questions |
|---|---|---|---|
| `SC-CAP01-01` | _[Participant, trigger, and preconditions]_ | _[Observable result]_ | _[Rule or question references]_ |

Use local scenarios for important situations within one capability. Put a scenario spanning several capabilities in End-to-End Scenarios. Use a decision table when interacting conditions make scenario enumeration ambiguous.

#### Applicable Models

| Model | Trigger | Scope | Link or section |
|---|---|---|---|
| _[Decision, state, process, information, or event model]_ | _[Why the model is needed]_ | `CAP-01` | _[Embedded model or controlled link]_ |

#### Capability Decisions and Open Questions

| Type and ID | Item | Impact or rationale | Owner | Status or resolution |
|---|---|---|---|---|
| _[Decision or question]_ | _[Statement]_ | _[Affected rule, scenario, or boundary]_ | _[Owner]_ | _[Status, date, or link]_ |

#### Local Constraints, Assumptions, Dependencies, and Risks

| Type | Item | Owner | Consequence or response |
|---|---|---|---|
| _[Dependency, constraint, assumption, or risk]_ | _[Capability-local statement]_ | _[Owner]_ | _[Impact, validation, or response]_ |

Keep the categories explicit even when they share one compact table. Do not mix mandatory constraints with unverified assumptions or uncertain risks.

## 9. Cross-Cutting Concerns

Use this section only for information that genuinely spans multiple capabilities. Do not duplicate it inside every Capability Specification.

### Cross-Cutting Rules

| ID or external reference | Rule or policy | Applies to | Source and owner |
|---|---|---|---|
| `BR-CROSS-01` | _[Shared business rule]_ | _[Capability IDs]_ | _[Authority and owner]_ |
| _[Authoritative external ID]_ | _[Linked rule title, not a copied restatement]_ | _[Capability IDs]_ | _[Authoritative link and owner]_ |

### End-to-End Scenarios

| ID or name | Capabilities | Trigger and context | Business outcome and rules |
|---|---|---|---|
| `SC-E2E-01` | _[Capability IDs]_ | _[Cross-capability trigger or journey]_ | _[Observable outcome and rule references]_ |

### Shared Business Information and Events

| Information or event | Business meaning | Authority or owner | Validity or consequence |
|---|---|---|---|
| _[Shared information item or domain event]_ | _[Meaning independent of storage or transport]_ | _[Authoritative owner or source]_ | _[Effective period or resulting obligation]_ |

### Initiative-Wide Constraints, Assumptions, Dependencies, and Risks

| Type | Item | Authority or owner | Impact, validation, or response |
|---|---|---|---|
| _[Constraint, assumption, dependency, or risk]_ | _[Initiative-wide statement]_ | _[Authority or owner]_ | _[Consequence, status, or response]_ |

### Cross-Capability Decisions and Open Questions

| Type and ID | Item | Capabilities affected | Owner | Status or resolution |
|---|---|---|---|---|
| _[Decision or question]_ | _[Statement]_ | _[Capability IDs]_ | _[Owner]_ | _[Status, date, or link]_ |

Open questions may remain at baseline review when their impact, owner, and decision date are explicit. Questions that block the initiative boundary or required behavior must be resolved before downstream commitment.

## 10. Readiness and Approval

### Readiness Gate

- [ ] The original request and governing sources are preserved and linked.
- [ ] The problem is stated independently of a preferred technical solution.
- [ ] Desired outcomes have observable success evidence.
- [ ] In-scope and out-of-scope behavior is explicit.
- [ ] The Capability Map covers the in-scope business behavior without using screens, APIs, services, databases, or delivery tasks as capabilities.
- [ ] Each capability has a coherent outcome, boundary, owner, local rules, and material local scenarios.
- [ ] Initiative-level stakeholders and terms are not duplicated inside capabilities unless their local responsibility differs.
- [ ] Every rule is classified as capability, cross-cutting, or external; shared and external rules are not copied into local catalogs.
- [ ] Capability-local and end-to-end scenarios are separated, and material condition combinations use a decision table when needed.
- [ ] Constraints, assumptions, dependencies, and risks remain explicitly classified at capability or initiative scope.
- [ ] Blocking business questions are resolved; remaining questions have owners and dates.
- [ ] The business owner can approve, reject, or reshape the initiative using this baseline.
- [ ] Downstream stakeholder and solution requirements can trace through the relevant capability to a source, outcome, rule, constraint, or decision.

### Revision History

| Version | Date | Change | Author |
|---|---|---|---|
| 0.1 | _[Date]_ | Initial draft | _[Author]_ |

### Approval

| Role | Decision | Date | Comment |
|---|---|---|---|
| Business owner | _[Approve, reject, or revise]_ | _[Date]_ | _[Comment]_ |

---

## Conditional Modules

Add only the modules whose trigger applies. Every model must state whether its scope is one capability or the whole initiative. A linked artifact is acceptable when the information is identifiable, versioned, reviewable, and traceable to this baseline.

### Context or Process Model

Use when several business participants, external parties, capabilities, or handoffs must be understood together.

| Scope | Participant or element | Trigger or input | Responsibility or activity | Outcome or handoff |
|---|---|---|---|---|
| _[Capability ID or initiative-wide]_ | _[Role, party, capability, or boundary element]_ | _[Trigger or input]_ | _[Business-level responsibility]_ | _[Outcome or handoff]_ |

### Decision Table

Use when multiple conditions interact, exceptions overlap, or scenario enumeration would hide missing combinations.

| Scope | Condition set | Permitted or required outcome | Rule references | Unresolved case |
|---|---|---|---|---|
| _[Capability ID or initiative-wide]_ | _[Relevant condition values]_ | _[Business decision]_ | _[Rules]_ | _[Question or none]_ |

Replace this compact register with a domain-specific decision table or decision model when individual condition columns are required.

### State or Lifecycle Model

Use when permitted behavior depends on the lifecycle state of a policy, product, request, agreement, or another business object.

| Scope | State | Entry condition | Permitted behavior | Exit or transition |
|---|---|---|---|---|
| _[Capability ID or initiative-wide]_ | _[Business state]_ | _[Entry event or condition]_ | _[Allowed and prohibited behavior]_ | _[Valid transition]_ |

### Detailed Business Information or Event Model

Use when meaning, authority, time validity, or ownership of business information drives behavior.

| Scope | Information or event | Business meaning | Authority or owner | Validity or consequence |
|---|---|---|---|---|
| _[Capability ID or initiative-wide]_ | _[Information item or domain event]_ | _[Meaning independent of storage or transport]_ | _[Authoritative owner or source]_ | _[Effective period or obligation]_ |

Do not turn business information into a database design or a business event into a message-broker contract.

### Operational Modes, Quality, and Transition

Use when behavior changes during degradation, migration, continuity events, staged rollout, operation, support, or retirement.

| Scope | Concern | Expected business behavior | Measure or decision rule | Owner |
|---|---|---|---|---|
| _[Capability ID or initiative-wide]_ | _[Mode, quality, rollout, or retirement concern]_ | _[Expectation]_ | _[Target or governing rule]_ | _[Owner]_ |

Translate these expectations into measurable system qualities during system analysis.

### Formal Traceability

Use when external audit, regulation, contract, safety, organizational policy, or cross-artifact impact analysis requires explicit links.

| BRS element | Source | Downstream requirement or decision | Success or verification evidence |
|---|---|---|---|
| _[Outcome, rule, constraint, or scenario]_ | _[Authoritative source]_ | _[StRS, SyRS, SRS, backlog, or decision link]_ | _[Metric, review, test, or production evidence]_ |

### ISO Coverage Register

Use for high-assurance work. Review the licensed standard and record each applicable concern rather than assuming that this template alone establishes conformance.

| ISO concern | Evidence or linked artifact | Status | Rationale and owner |
|---|---|---|---|
| _[Section or concern]_ | _[Template section or authoritative link]_ | _[Covered, Partial, or Not applicable]_ | _[Reason and accountable reviewer]_ |

## ISO/IEC/IEEE 29148 Coverage Map

This map shows where the practical template normally addresses the public BRS outline. It is a tailoring aid, not a substitute for the standard.

| ISO/IEC/IEEE 29148:2018 content | Normal location | Tailoring note |
|---|---|---|
| 9.2.1 Identification | Baseline Identification and Sources | Core |
| 9.2.2 Front matter | Executive Summary, Revision History, Approval | Core; add navigation for large packages |
| 9.2.3 Definitions | Shared Terms; Capability Local Terms | Core when domain language is material |
| 9.2.4 References | Authoritative Sources | Core |
| 9.2.5 Acronyms and abbreviations | Terms and Business Concepts | Add when readers need them |
| 9.3.2 Business purpose | Problem and Current Context; Desired Outcome and Success | Core |
| 9.3.3 Business scope | Scope and Non-Goals | Core |
| 9.3.4 Business overview | Problem and Current Context; Capability Map; Context or Process Model | Core narrative and capability index; model when needed |
| 9.3.5 Major stakeholders | Initiative and Capability Stakeholders | Core |
| 9.3.6 Business environment | Cross-Cutting Concerns; Capability Dependencies and Risks | Core |
| 9.3.7 Mission, goals, and objectives | Desired Outcome and Success | Core |
| 9.3.8 Business model | Desired Outcome; Context or Process Model | Link to a business case or model when governed elsewhere |
| 9.3.9 Information environment | Shared Business Information and Events; detailed information models | Shared register or conditional model |
| 9.3.10 Business processes | Capability Models; Context or Process Model; End-to-End Scenarios | Conditional |
| 9.3.11 Operational policies and rules | Capability Rules; Cross-Cutting Rules; Decision Table | Core scoped rules; table when needed |
| 9.3.12 Operational constraints | Capability and Initiative-Wide Constraints | Core |
| 9.3.13 Operational modes | Operational Modes, Quality, and Transition | Conditional |
| 9.3.14 Operational quality | Desired Outcome; Operational Modes, Quality, and Transition | Core outcome or conditional detail |
| 9.3.15 Business structure | Initiative and Capability Decision Rights; Context or Process Model | Core responsibilities or conditional model |
| 9.3.16 High-level operational concept | Target State; Capability Map and Specifications | Core |
| 9.3.17 High-level operational scenarios | Capability Scenarios; End-to-End Scenarios | Core when scenarios materially clarify behavior |
| 9.3.18 Other lifecycle concepts | Operational Modes, Quality, and Transition | Conditional |
| 9.3.19 Project constraints | Initiative-Wide Constraints; Scope and Non-Goals | Core when applicable |

## Related Topics

- [Choosing the First Requirements Artifact](01-choosing-the-first-requirements-artifact.md)
- [Tailoring the Business Requirements Baseline](02-tailoring-the-business-requirements-baseline.md)
- [Working with BRS Deltas](04-working-with-brs-deltas.md)
- [Requirements discovery techniques](requirements-discovery-techniques.md)
- [System boundary checklist](system-boundary-checklist.md)
- [Product and Requirements index](README.md)
