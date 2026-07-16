# Choosing the First Requirements Artifact

> Status: Draft  
> Area: product-requirements

## Problem

The first input to a software initiative is rarely a clean requirements artifact. It may be an email, a ticket, a business presentation, a regulatory request, or a document that mixes:

- the business problem;
- a proposed solution;
- business rules;
- UI and API ideas;
- constraints and assumptions;
- acceptance criteria or a local Definition of Done.

Teams then give the first document different names: BRD, BRS, Vision and Scope, Product Goal, PRD, one-pager, project charter, ConOps, use case, or user story. These names are not interchangeable. Some are standardized information items, some are methods, some are framework concepts, and some are only local or vendor conventions.

The decision is not "Which acronym is most popular?" It is:

> What is the first controlled baseline that explains why the change exists, where its boundaries are, and which business outcomes and rules must guide all later requirements?

## Core Idea

Use a **Business Requirements Specification (BRS)** as the first controlled requirements baseline when an initiative needs an explicit business-level foundation.

[ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) standardizes BRS as a business-level requirements information item. It does not prescribe a universal first physical file, nor does it require requirements work to be strictly linear. The standard explicitly supports iterative and recursive application of requirements processes and allows information to be organized according to project information-management policies.

Treat the raw business request as an immutable source, not as the analyzed baseline. Build the BRS from that source, preserving traceability back to it.

Use Karl Wiegers's **Vision and Scope** approach as a practical authoring and communication layer for the BRS. It adds useful ways to express measurable objectives, success metrics, risks, major features, release boundaries, stakeholder profiles, and priorities. Vision and Scope does not replace the ISO BRS and is not itself an ISO-standard artifact.

## Sources and Standards

| Source | What It Defines | How It Is Used Here |
|---|---|---|
| [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) and the [IEEE record](https://standards.ieee.org/ieee/29148/6937/) | Requirements-engineering processes, requirement characteristics, and BRS, StRS, SyRS, and SRS information items | Normative content model for the BRS |
| [DIN Media standard outline](https://www.dinmedia.de/en/standard/iso-iec-ieee-29148/299567544) | Published table of contents for the ISO BRS, StRS, SyRS, and SRS sections | Verifiable outline for the template structure |
| Karl Wiegers and Joy Beatty, [Software Requirements, Third Edition](https://www.microsoftpressstore.com/store/software-requirements-9780735679610) | Practical requirements-development guidance and the Vision and Scope approach | Authoring enhancements and practical identifiers such as BO, SM, RI, and FE |
| [Wiegers's requirements resources](https://softwarereqs.com/) and [requirements-engineering handout](https://www.re18.cpsc.ucalgary.ca/assets/downloads/industryDay/Karl%20Wiegers%20RE18%20handout.pdf) | Vision and Scope template and the separation of business, user, and functional requirements | Practical structure and requirements-level separation |
| [IIBA Business Analysis Standard](https://www.iiba.org/knowledgehub/the-business-analysis-standard/4-implementing-business-analysis/4-4-understanding-requirements-and-designs/) and [BABOK glossary](https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/glossary/) | Business, stakeholder, solution, and transition requirement categories; requirements artifacts and packages | Classification, validation, and traceability guidance, not a mandatory first document |
| [Scrum Guide](https://scrumguides.org/scrum-guide.html) | Product Goal as the commitment associated with the Product Backlog | Explains why Product Goal is useful but not a replacement for a BRS |
| [NASA Systems Engineering Handbook guidance](https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/) | Concept of Operations as an early systems-engineering description of how a system will be used to meet stakeholder expectations | Explains the operational purpose of ConOps and why it is not a complete business-level baseline |
| Atlassian [BRD](https://www.atlassian.com/software/confluence/resources/guides/how-to/business-requirements) and [PRD](https://www.atlassian.com/software/confluence/templates/product-requirements) templates | Common vendor and product-management practices | Evidence of industry usage, not normative definitions |

The ISO standard is the normative reference in this decision. Wiegers supplies a practical method. IIBA supplies a conceptual classification. Scrum supplies a product-delivery framework. Vendor templates demonstrate common usage only.

## Candidate Artifacts

The alternatives below are not inherently bad. Most of them answer a different question or do not have a stable, standards-based meaning.

| Candidate | Origin | Standardized? | Useful For | Why It Is Not the Default First Baseline |
|---|---|---:|---|---|
| Raw business request | Stakeholder or organizational input | No | Preserving the original request, language, evidence, and source | It is usually stated rather than analyzed: it may mix needs, solutions, rules, assumptions, and acceptance ideas |
| BRD — Business Requirements Document | Organizational and vendor practice | No single normative definition | Stakeholder alignment and project documentation | Its content varies widely; some BRDs contain only business goals, while others include functional and non-functional solution requirements |
| BRS — Business Requirements Specification | ISO/IEC/IEEE 29148:2018 | Yes | Business purpose, scope, stakeholders, environment, processes, rules, constraints, and high-level operational concepts | This is the selected baseline; it must still be tailored and kept usable rather than copied mechanically |
| Vision and Scope | Karl Wiegers's requirements method | Method, not standard | Concise business objectives, success measures, vision, features, scope, risks, and stakeholder alignment | It is practical but does not, by itself, guarantee coverage of all applicable ISO BRS content such as business processes, operational modes, and lifecycle concepts |
| Business Case / Project Charter | Investment and project-governance practice | Depends on the governance framework | Funding, authorization, ownership, expected value, schedule, and project constraints | It may justify or authorize work without providing a requirements baseline; reuse it as a BRS source instead of duplicating it |
| Product Goal | Scrum Guide | Standard within Scrum, but not a separate Scrum artifact | A future product state that focuses the Product Backlog | It is a commitment inside the Product Backlog and is intentionally too concise to cover the complete business baseline |
| Product Vision / one-pager | IIBA terminology and general product practice | Product vision is defined conceptually; one-pager is not standardized | Fast communication and executive alignment | A short vision omits the business environment, rules, processes, constraints, risks, and traceability needed for a controlled baseline |
| PRD — Product Requirements Document | Product-management and vendor practice | No single normative definition | Describing a product or feature, often including user stories, UX, features, and release scope | It commonly moves into solution and delivery detail before business-level requirements have been separated and validated |
| [ConOps — Concept of Operations](https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/) | Systems-engineering practice | Defined in systems-engineering contexts | Explaining how a system will be used and operated in important scenarios | It provides an operational viewpoint, not a complete business-management baseline; it is especially useful as a linked model for operationally complex systems |
| Use Case / User Story | Requirements and agile techniques | Defined techniques, not complete business baselines | Describing actor goals, observable interactions, or a small unit of stakeholder value | They sit at the stakeholder or usage level and cannot carry the full business purpose, process, rule, scope, and constraint model |

## When to Use

Use a BRS as the first controlled baseline when:

- the incoming request mixes business and solution detail;
- several teams, systems, business units, or channels are affected;
- the initiative contains many rules, exceptions, or operational modes;
- scope and non-goals need explicit agreement;
- regulatory, contractual, or audit traceability matters;
- later StRS, SyRS, SRS, backlog, and test artifacts need a stable source;
- the initiative can be stopped or reshaped if the business case is not valid.

## When Not to Use

Do not create a large standalone BRS merely to satisfy a document checklist when:

- the change is small, local, reversible, and already has an agreed business objective and boundary;
- an existing approved artifact already covers the applicable BRS content;
- the initiative is an operational incident fix with no change to business intent;
- a higher-level BRS already governs the work and the current task only needs stakeholder or solution-level refinement.

In these cases, link to the existing baseline and document only the delta. The goal is controlled information, not document proliferation.

## How It Works

Separate the source from the baseline and separate requirements levels:

```text
Raw request, policy, business case, evidence
                    |
                    v
        BRS — business-management baseline
                    |
                    v
        StRS — stakeholder needs and usage
                    |
                    v
         SyRS — system requirements
                    |
                    v
        SRS — software requirements
                    |
                    v
       backlog, acceptance, and tests
```

This is a requirements-level dependency map, not a mandatory waterfall. ISO/IEC/IEEE 29148 allows the processes and information items to be developed iteratively and recursively. A discovery finding at the SRS or test level can reveal a missing business rule and trigger a controlled update to the BRS.

The BRS also does not have to be one Word document. It can be a logically organized set of linked pages, models, registers, and tables if the required content is identifiable, accessible, versioned, and traceable.

## ISO and Wiegers Mapping

Use the ISO BRS as the coverage model and Vision and Scope as a usability overlay.

| ISO BRS Concern | Wiegers Contribution | Practical Result |
|---|---|---|
| Business purpose | Background and business opportunity | A clear explanation of the problem, opportunity, and reason to act now |
| Mission, goals, and objectives | Business Objectives (`BO`) and Success Metrics (`SM`) | Outcomes become measurable instead of aspirational |
| Major stakeholders | Stakeholder profiles | Stakeholder value, interests, attitudes, and constraints become explicit |
| Business environment and project constraints | Assumptions, dependencies, Business Risks (`RI`), and project priorities | Uncertainty and decision constraints become visible |
| High-level operational concept | Vision statement and major Features (`FE`) | The proposed direction is understandable without becoming a system design |
| Business scope and lifecycle concepts | Initial-release scope, subsequent-release scope, exclusions, and deployment considerations | Boundaries and sequencing become concrete |
| Business policies and rules | Traceable rule identifiers and linked rule or decision models | Rules remain reusable and do not disappear inside prose or use cases |

The prefixes `BO`, `SM`, `RI`, and `FE` are practical identifiers associated with Wiegers-style examples. They are not ISO identifiers. A document key such as `BRS-<initiative-key>` and rule prefixes such as `BR-` are local conventions and must be declared as such.

## Trade-offs

| Choice | Advantages | Costs and Limitations |
|---|---|---|
| ISO BRS without practical tailoring | Strong coverage, shared standards vocabulary, good auditability | Can become formal, verbose, and hard for stakeholders to review |
| Vision and Scope alone | Concise, outcome-oriented, easy to discuss | May leave gaps against the applicable ISO BRS content |
| ISO BRS with Wiegers enhancements | Standards-based coverage plus measurable and readable business framing | Requires an explicit mapping so contributors know what is normative, methodological, or local |
| One mixed BRD/PRD | Fewer pages and familiar product workflow | Requirements levels blur, traceability weakens, and the document can become a solution specification prematurely |

## Common Mistakes

- Calling every statement supplied by a business stakeholder a business requirement. A requested screen, field, or API is usually a solution idea, not a business outcome.
- Treating BRD and BRS as universal synonyms without defining the local vocabulary.
- Claiming that Vision and Scope is an ISO artifact or that it is identical to a BRS.
- Saying that ISO requires every initiative to begin with one physical BRS document.
- Treating Product Goal as a standalone Scrum artifact or as a complete business baseline.
- Using invented terms such as `BRS-lite` or `BP-XXX` without identifying them as local conventions.
- Filling the BRS with database, API, service, and UI design before stakeholder and system requirements have been separated.
- Removing business processes, rules, constraints, or operational modes merely to make the document "lean."
- Copying information from a business case or policy instead of linking to the authoritative source.
- Baseline approval without measurable objectives, explicit exclusions, or owners for open questions.

## Practical Checklist

A first controlled baseline is ready for review when:

- [ ] The original request and every authoritative source are preserved and linked.
- [ ] The business purpose explains why the change exists without relying on implementation detail.
- [ ] Business objectives have observable success metrics.
- [ ] The business domain, included scope, exclusions, and later-release scope are explicit.
- [ ] Major stakeholders and their decision rights are known.
- [ ] Relevant business processes, policies, and rules are named and traceable.
- [ ] Assumptions, dependencies, constraints, risks, and operational modes are separated.
- [ ] The high-level operational concept explains the intended direction without becoming a technical design.
- [ ] Every non-applicable BRS section has a reason or a link to the governing artifact.
- [ ] Open questions have owners and decision dates.
- [ ] The business owner can approve, reject, or reshape the initiative using this baseline.
- [ ] Downstream stakeholder and solution requirements can trace back to a business objective, rule, or constraint.

Use the [Business Requirements Specification template](business-requirements-specification-template.md) to apply this checklist.

## Example

Consider this fictional and deliberately simplified request:

> Add an availability flag to each catalog item and hide unavailable items in all customer channels. Existing owners must still see their items and history.

This is valuable source material, but it is not yet a business-level baseline. It already proposes a data field and combines a general visibility rule with ownership and history exceptions.

An analyzed BRS fragment could look like this:

### Business Purpose

Provide one governed way to control whether catalog items are offered in each customer channel while preserving access required for existing ownership and historical records.

### Business Objective and Success Metric

`BO-1` — Eliminate inconsistent channel-specific handling of catalog-item availability.

`SM-1` — Within three months of rollout, 100% of supported customer channels use the governed availability decision, and configuration-related visibility incidents decrease by at least 80% from the agreed baseline.

These numbers are illustrative. A real BRS must establish the baseline, measurement source, owner, and target date with stakeholders.

### Scope

In scope:

- business decisions that determine whether an item is offered in a customer channel;
- exceptions required for existing ownership and historical records;
- business ownership of the availability policy.

Out of scope:

- channel UI redesign;
- database schema and API contract design;
- unrelated eligibility and pricing policies.

### Business Rules

`BR-1` — An item that is not available in a channel must not be offered for a new transaction in that channel.

`BR-2` — Availability for new transactions must not remove an existing owner's access to owned items or historical records.

The `BR-` prefix is a declared local convention, not an ISO or Wiegers requirement.

### Risk and Major Feature

`RI-1` — Channels may interpret the availability policy differently during migration, producing inconsistent customer outcomes.

`FE-1` — Govern catalog-item availability by customer channel through one business-owned policy.

The later StRS, SyRS, and SRS determine user interactions, system behavior, data, interfaces, errors, and implementation constraints. The BRS remains the source of the business intent and boundary.

## Interview Angle

A concise explanation:

> I separate the raw request from the first analyzed baseline. If the initiative needs a formal business-level foundation, I use the BRS information model from ISO/IEC/IEEE 29148. I apply Wiegers's Vision and Scope practices to make objectives measurable and boundaries readable, but I do not treat Vision and Scope as an ISO artifact. Stakeholder, system, software, backlog, and test artifacts then trace back to that baseline.

## Related Topics

- [Business Requirements Specification template](business-requirements-specification-template.md)
- [Requirements discovery techniques](requirements-discovery-techniques.md)
- [System boundary checklist](system-boundary-checklist.md)
- [Product and Requirements index](README.md)
