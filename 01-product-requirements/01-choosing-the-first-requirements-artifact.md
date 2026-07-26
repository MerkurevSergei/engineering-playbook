# Choosing the First Requirements Artifact

> Status: Draft
> Area: product-requirements

## Problem

The first input to an initiative is rarely a controlled requirements artifact. It may be an email, a ticket, a business presentation, a regulatory request, or a document that mixes:

- the business problem;
- a proposed solution;
- business rules;
- UI and API ideas;
- constraints and assumptions;
- acceptance ideas or a local Definition of Done.

Teams then give the first document different names: BRD, BRS, Vision and Scope, Product Goal, PRD, one-pager, project charter, ConOps, use case, or user story. These names are not interchangeable. Some are standardized information items, some are methods or framework concepts, and some are only local or vendor conventions.

The decision is not "Which acronym is most popular?" It is:

> Which controlled artifact is needed to establish the business purpose, authority, boundary, and expected outcome of this initiative?

## Core Idea

Use a **Business Requirements Specification (BRS)** as the first controlled requirements baseline when an initiative needs an explicit business-level foundation.

[ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) defines the BRS as a business-level requirements information item. The standard defines its required information concerns but does not require every initiative to begin with one physical file.

The incoming request remains a source. Do not rename an unanalyzed email, ticket, presentation, or proposed design to `BRS` merely because the initiative needs a formal baseline.

Selecting a BRS is not automatic. A smaller or differently governed artifact can be sufficient when it already establishes the required business intent and decision authority.

## Decision Rule

Choose the first artifact by the decision it must support:

| Decision need | Suitable first artifact |
|---|---|
| Establish a controlled business purpose, scope, stakeholders, environment, policies, rules, constraints, and operational concept | BRS |
| Justify investment, authorize a project, or assign funding and accountability | Business Case or Project Charter |
| Communicate a concise product direction without establishing a complete business baseline | Product Vision, one-pager, or Product Goal |
| Explain how a system will be used and operated in its environment | ConOps |
| Preserve an initial request for later analysis | Raw request, source record, or intake ticket |
| Work within an existing approved business baseline | Reference the governing baseline instead of creating a competing first artifact |

When several rows apply, keep the authoritative artifacts distinct and link them. Do not combine every concern into a document with an ambiguous local name.

## Sources and Standards

| Source | Contribution to the decision |
|---|---|
| [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) and the [IEEE record](https://standards.ieee.org/ieee/29148/6937/) | Defines the standardized BRS information item and its business-level content |
| Karl Wiegers and Joy Beatty, [Software Requirements, Third Edition](https://www.microsoftpressstore.com/store/software-requirements-9780735679610) | Defines the practical Vision and Scope approach used as a candidate method, not an ISO artifact |
| [Scrum Guide](https://scrumguides.org/scrum-guide.html) | Defines Product Goal as the commitment associated with the Product Backlog, not as a standalone business baseline |
| [NASA Stakeholder Expectations Definition](https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/) | Describes Concept of Operations as an operational representation of intended system use |
| Atlassian [BRD](https://www.atlassian.com/software/confluence/resources/guides/how-to/business-requirements) and [PRD](https://www.atlassian.com/software/confluence/templates/product-requirements) templates | Demonstrate common vendor usage without establishing normative definitions |

ISO is the normative reference for the BRS decision. The other sources define alternative practices or illustrate common industry terminology.

## Candidate Artifacts

The alternatives below are not inherently weak. They answer different questions or have different authority.

| Candidate | Origin | Standardized? | Useful for | Why it is not always the first business baseline |
|---|---|---:|---|---|
| Raw business request | Stakeholder or organizational input | No | Preserving the original language, evidence, and source | It may mix needs, proposed solutions, assumptions, and acceptance ideas without analysis or approval |
| BRD — Business Requirements Document | Organizational and vendor practice | No single normative definition | Stakeholder alignment and project documentation | Its content varies widely between organizations |
| BRS — Business Requirements Specification | ISO/IEC/IEEE 29148:2018 | Yes | Establishing a controlled business-level requirements baseline | It is appropriate only when the initiative needs this level of business coverage and control |
| Vision and Scope | Requirements method associated with Karl Wiegers | Method, not standard | Concise objectives, success measures, vision, scope, risks, and stakeholder alignment | It does not by itself guarantee coverage of every applicable BRS concern |
| Business Case or Project Charter | Investment and project-governance practice | Depends on the governance framework | Funding, authorization, ownership, expected value, schedule, and project constraints | It can authorize work without specifying the complete business behavior to be governed |
| Product Goal | Scrum Guide | Standard within Scrum, but not a separate Scrum artifact | Focusing the Product Backlog on a future product state | It is intentionally more concise than a controlled business baseline |
| Product Vision or one-pager | Product practice | No single normative definition | Fast communication and executive alignment | It can omit material rules, processes, constraints, and decision authority |
| PRD — Product Requirements Document | Product-management and vendor practice | No single normative definition | Describing a product or feature | Its scope and requirements level vary by organization and template |
| ConOps — Concept of Operations | Systems-engineering practice | Defined in systems-engineering contexts | Explaining intended system use and operation | It provides an operational viewpoint rather than the complete business-management baseline |
| Use Case or User Story | Requirements and agile techniques | Defined techniques, not complete business baselines | Describing an actor goal, interaction, or small unit of value | It cannot establish the full initiative purpose, authority, scope, policies, and constraints |

## When to Use a BRS

Choose a BRS as the first controlled artifact when:

- the incoming request mixes business intent and proposed implementation;
- several business units, teams, systems, channels, or external parties are affected;
- material policies, rules, exceptions, constraints, or operational modes must be governed;
- scope and exclusions require explicit agreement;
- regulatory, contractual, safety, or audit assurance matters;
- no existing approved artifact establishes the required business baseline;
- the approving authority must be able to stop or reshape the initiative at the business level.

## When Not to Create a New BRS

Do not create a standalone BRS merely to satisfy a document checklist when:

- the change is small, local, reversible, and already has an agreed business objective and boundary;
- an existing approved BRS or equivalent governed artifact covers the initiative;
- the work restores already-approved behavior without changing business intent;
- the immediate decision concerns investment authorization, product direction, or operational use and the corresponding governed artifact is sufficient;
- the organization uses another named artifact that demonstrably covers the applicable BRS concerns and has clear ownership and approval.

The goal is controlled business information and unambiguous authority, not document proliferation.

## Trade-offs

| Choice | Advantage | Limitation |
|---|---|---|
| New BRS | Explicit business coverage, ownership, and review boundary | Unnecessary overhead when a governing baseline already exists or the change is trivial |
| Existing governed baseline | Avoids duplication and competing sources of truth | Requires confidence that the existing artifact covers the initiative and remains current |
| Business Case or Project Charter | Clear investment and authorization decision | May not establish governed business behavior |
| Product Vision, one-pager, or Product Goal | Fast alignment around direction | May leave scope, rules, constraints, and authority implicit |
| ConOps | Strong operational viewpoint | Does not replace the broader business baseline |
| Local BRD or PRD | Familiar organizational workflow | Meaning and coverage must be declared because the names are not universal standards |

## Common Mistakes

- Treating every statement supplied by a business stakeholder as a business requirement.
- Treating BRD, BRS, and PRD as universal synonyms without defining the local vocabulary.
- Claiming that Vision and Scope is an ISO artifact or is identical to a BRS.
- Treating Product Goal as a standalone Scrum artifact or a complete business baseline.
- Assuming every initiative must start with a large standalone BRS.
- Renaming a raw request or proposed solution to `BRS` without analysis and approval.
- Creating a second baseline when an authoritative one already covers the initiative.
- Selecting an artifact because a template is familiar rather than because it supports the required decision.
- Treating a vendor template as a normative industry definition.

## Selection Checklist

Before selecting the first controlled artifact, confirm:

- [ ] The decision that the artifact must support is explicit.
- [ ] The original request and authoritative sources are identifiable.
- [ ] The required level is business purpose and governance rather than product, operational, interaction, or implementation detail.
- [ ] The affected business boundary and number of participating authorities are understood well enough to judge the needed control.
- [ ] Regulatory, contractual, safety, audit, or other assurance obligations are known.
- [ ] Existing governed artifacts have been checked before creating a new baseline.
- [ ] The selected artifact has a declared owner, approver, scope, and meaning in the organization.
- [ ] Local or vendor terminology is not presented as an ISO or framework standard.

## Example

Consider this fictional source request:

> Add an availability flag to each catalog item and hide unavailable items in all customer channels. Existing owners must still see their items and history.

Choose a BRS as the first controlled artifact because the request:

- affects several customer channels;
- proposes implementation before the governed business behavior is agreed;
- contains a general restriction and material ownership exceptions;
- requires an explicit business boundary and policy authority;
- can produce inconsistent business outcomes if interpreted independently.

The proposed flag remains part of the source request. Selecting the BRS establishes which artifact must resolve the business-level ambiguity; it does not approve the proposed data field or technical approach.

## Interview Angle

> I choose the first requirements artifact by the decision and authority it must support, not by the most familiar acronym. When a new initiative needs a controlled business-level foundation, I use the BRS information item defined by ISO/IEC/IEEE 29148. When an existing baseline or a narrower governed artifact is sufficient, I reference that instead of creating a competing document.

## Related Topics

- [Business Requirements Specification template](02-business-requirements-specification-standard.md)
- [Product and Requirements index](README.md)
