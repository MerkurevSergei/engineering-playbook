# Working with BRS Deltas

> Status: Draft
> Area: product-requirements

## Problem

A long-lived product or business domain may already have an approved Business Requirements Specification. New work then arrives as emails, tickets, policies, presentations, or business statements that propose changes to only part of that baseline.

Two common approaches fail:

- creating another complete BRS for every initiative duplicates the current business model and makes conflicts difficult to see;
- editing the canonical BRS directly hides the source, rationale, rejected alternatives, approval state, and downstream progress of the change.

Teams need a controlled working artifact that answers:

> What changes relative to the approved BRS, which capabilities and elements are affected, what has been approved and applied, and what work remains before the change is verified?

## Core Idea

Use a **BRS Delta** as an initiative-scoped change set proposed against a specific version of a canonical BRS.

`BRS Delta` is a declared local convention, not an ISO/IEC/IEEE 29148 or IIBA artifact name. The standards and practices support requirements identification, maintenance, traceability, impact assessment, approval, and lifecycle control. The delta packages those activities into a reviewable business change set.

Keep three artifacts distinct:

1. preserve the raw business request as an immutable source;
2. analyze and approve the proposed change in the BRS Delta;
3. apply approved normative content to the canonical BRS and retain the delta as the change record.

The canonical BRS describes current business truth. The delta describes why and how that truth is proposed to change.

## Sources and Standards

| Source | Contribution | Use Here |
|---|---|---|
| [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) and the [IEEE record](https://standards.ieee.org/ieee/29148/6937/) | Requirements information items, identification, content, traceability, and iterative requirements processes | Normative context for controlling BRS information, not a definition of `BRS Delta` |
| IIBA [Requirements and Designs Life Cycle Management](https://www.iiba.org/knowledgehub/the-business-analysis-standard/5-applying-business-analysis-tasks/5-3-business-analysis-knowledge-areas/requirements-and-designs-life-cycle-management/) | Trace, maintain, prioritize, assess changes, and approve requirements and designs | Change lifecycle behind the delta workflow |
| IIBA [Assess Requirements and Designs Changes](https://www.iiba.org/contentassets/f9bf5368925b4ceb8f29a246ae6bd9e5/task-card-assess-req-and-designs-changes.pdf) | Impact analysis and recommendations for proposed changes | Capability and element impact assessment |
| IIBA [Trace Requirements and Designs](https://production.iiba.org/contentassets/7d0078edc4b842649ce8f91f1155268f/all-task-cards-req-and-designs-life-cycle-mgmt.pdf) | Backward and forward lineage and change-impact analysis | Links from source through BRS elements to delivery and evidence |
| IIBA [Maintain Requirements and Designs](https://www.iiba.org/contentassets/8fafb55e5fd44f3284c50eeead23acc4/task-card-maintain-req-and-designs.pdf) | Keeping requirements accurate and current beyond one initiative | Canonical BRS maintenance |
| Karl Wiegers and Joy Beatty, [Software Requirements, Third Edition](https://www.microsoftpressstore.com/store/software-requirements-9780735679610) | Practical requirements management, baselining, traceability, and change control | Authoring and review discipline |

The physical structure, identifiers, status vocabulary, and merge workflow below are local playbook conventions.

## Vocabulary and Boundaries

| Artifact | Purpose | Lifecycle |
|---|---|---|
| Raw business request | Preserve the original language, evidence, and authority | Immutable source |
| BRS Delta | Analyze, approve, apply, and track a coherent business change | Working change set, then retained record |
| Canonical BRS | Describe the approved current business model for a bounded product or domain | Long-lived, versioned baseline |
| Downstream requirements and delivery | Realize the approved business change through stakeholder and solution work | Managed by their own repositories and trackers |

A delta is not necessarily one-to-one with a raw request. Several source statements may form one coherent change, and one broad source may require several independently governed deltas.

## When to Use

Use a BRS Delta when:

- a canonical BRS already exists for the affected product or domain;
- the change affects a subset of existing capabilities, rules, scenarios, or constraints;
- several initiatives may change the same baseline concurrently;
- approval, audit, or impact analysis must preserve the reason for a change;
- downstream requirements and delivery need traceability to individual business changes;
- the team needs to distinguish BRS merge progress from implementation progress.

## When Not to Use

Do not create a separate BRS Delta when:

- no canonical BRS exists and the work is creating the initial `BRS v1.0`; the first delta may be the working draft of that baseline;
- the BRS itself is initiative-specific and will not be maintained after the initiative, so a separate change set would duplicate it;
- an incident correction does not change business intent;
- the authoritative change belongs to an external policy, regulation, or shared rule catalog that must be updated at its source and only referenced from the BRS.

Do not create one unbounded enterprise BRS merely to enable deltas. The canonical BRS must have a stable product, domain, or other governed business boundary.

## How It Works

```text
Raw request, policy, evidence
              |
              v
       BRS Delta change set
              |
       analysis and approval
              |
              v
Canonical BRS vN  -------->  Canonical BRS vN+1
                                   |
                                   v
                       StRS / SyRS / SRS deltas
                                   |
                                   v
                        delivery and verification
```

### 1. Identify the Base and Change Boundary

Every delta names:

- the canonical BRS and exact base version;
- the intended target version or release;
- the raw sources and governing authorities;
- the coherent business outcome being changed;
- the affected and explicitly reviewed capabilities;
- the delta owner, approvers, and target decision date.

Do not begin with a copy of the complete BRS. Begin with the change boundary and links to the current baseline.

### 2. Create the Delta Header

| Field | Value |
|---|---|
| Delta ID | _[Local stable identifier]_ |
| Target BRS and base version | _[Canonical baseline link and version]_ |
| Intended target version | _[Version or release after application]_ |
| Business owner | _[Accountable role]_ |
| Status | _[Draft, In Review, Approved, Applied, Rejected, or Superseded]_ |
| Sources | _[Raw request and authoritative references]_ |
| Decision date | _[Target or actual date]_ |

The base version is part of the meaning of the delta. If the canonical BRS changes before application, reassess the delta against the new version.

### 3. Maintain Capability Progress Views

The first view shows whether the business change is understood and merged.

| Capability | Analysis status | BRS merge status | Blocker | Next action |
|---|---|---|---|---|
| _[Capability or cross-cutting scope]_ | _[Draft, In Review, or Approved]_ | _[Not Applied, Applied, or Conflict]_ | _[Question or none]_ | _[Action and owner]_ |

The second view shows downstream realization without copying delivery tasks.

| Capability | Downstream status | Delivery status | Verification status | Next action |
|---|---|---|---|---|
| _[Capability or cross-cutting scope]_ | _[Not Analyzed, Draft, or Requirements Ready]_ | _[Not Planned, Planned, In Progress, Implemented, or Released]_ | _[Not Started, Planned, In Progress, or Verified]_ | _[Action and owner]_ |

These views are summaries. The linked requirements repository, delivery tracker, and verification system remain authoritative for their own details.

### 4. Build the Change Manifest

The Change Manifest is the complete index of semantic changes proposed by the delta.

| Change ID | Capability | Element and operation | Baseline status | Detail |
|---|---|---|---|---|
| `CHG-001` | `CAP-01` | Modify `BR-CAP01-04` | In Review | _[Section or link]_ |
| `CHG-002` | `CAP-02` | Add `SC-CAP02-07` | Approved | _[Section or link]_ |
| `CHG-003` | `CAP-03` | Impact check `BR-CAP03-01` | Confirmed unchanged | _[Evidence or rationale]_ |

Use four operations:

- **Add** — create a new canonical element;
- **Modify** — replace the normative meaning of an existing element;
- **Retire** — remove an element from the current baseline while preserving history;
- **Impact check** — record that an affected element or capability was reviewed and intentionally remains unchanged.

`Impact check` distinguishes a conscious no-change decision from an area that was never analyzed.

### 5. Describe Detailed Changes by Capability

Organize detailed changes using the capability structure of the target BRS. Include only changed or impact-checked content, not a copy of the complete capability.

For each change item record:

- current canonical state or absence of an element;
- proposed normative state;
- rationale and source;
- affected rules, scenarios, decisions, and models;
- local dependencies, risks, and open questions;
- target canonical element and version;
- downstream impact.

A detailed change can use this form:

```text
CHG-002 — Add BR-CAP02-03

Current state:
No canonical rule defines the behavior.

Proposed state:
[Normative business rule.]

Rationale:
[Why this change is required.]

Target:
BRS-CATALOG v3.3 / CAP-02
```

Keep rules that affect several capabilities in a Cross-Cutting Changes section. Keep external rules under their authoritative identifiers and link them without copying their text into the delta.

### 6. Approve and Apply the Delta

Use a business-baseline lifecycle distinct from delivery:

```text
Draft -> In Review -> Approved -> Applied
                    \-> Confirmed Unchanged
                    \-> Rejected

Applied -> Superseded
```

`Applied` means the approved normative change has been incorporated into a new canonical BRS version. It does not mean the solution has been implemented.

`Confirmed Unchanged` is the terminal baseline disposition for an approved Impact Check and requires no canonical edit. A delta reaches `Applied` when all approved manifest items are either applied or confirmed unchanged and the resulting BRS version is recorded.

Before application:

- verify that the base BRS version still matches;
- resolve concurrent changes to the same capability or element;
- approve every manifest item's final operation and wording;
- allocate stable identifiers for new canonical elements;
- record the resulting BRS version and element links.

Apply changes semantically rather than by copying the complete delta into the BRS.

| Apply to canonical BRS | Retain in delta record |
|---|---|
| Approved current capabilities, outcomes, rules, scenarios, terms, and durable constraints | Raw sources, analysis notes, rejected alternatives, temporary assumptions, discussions, and change history |
| Decisions required to understand the current business model | Closed questions and the rationale for this specific change |
| Durable cross-cutting business behavior | One-time delivery or transition details governed elsewhere |

### 7. Track Downstream Coverage

After approval, connect each semantic change to downstream work.

| Change ID | Requirement links | Delivery link and status | Evidence | Next action |
|---|---|---|---|---|
| _[Manifest item]_ | _[StRS, SyRS, SRS, or backlog link]_ | _[Epic or work item summary]_ | _[Test, review, or production evidence]_ | _[Action and owner]_ |

Use a realization lifecycle separate from baseline control:

```text
Not Analyzed
-> Downstream Requirements Ready
-> Planned
-> Implemented
-> Released
-> Outcome Verified
```

The BRS Delta records coverage, aggregated status, blockers, and links. It does not replace the source-of-truth systems for requirements, delivery, or verification.

### 8. Report Progress Without a False Percentage

Do not calculate one completion percentage by counting change items. One rule may require a small clarification while another changes several systems and operating processes.

Report:

- manifest items by baseline status;
- manifest items by realization status;
- capability-level progress;
- unresolved blockers and owners;
- the next decision or delivery milestone.

Example:

```text
Business changes: 8 of 10 approved, 6 applied
Downstream requirements: 5 ready
Delivery: 3 implemented, 2 in progress, 5 not started
Verification: 1 verified
Blockers: OQ-03, OQ-07
Next milestone: approve CAP-02 rules
```

### 9. Close Two Milestones

Treat completion as two explicit milestones:

- **Baseline Applied** — every manifest item has a final disposition, approved changes are present in the canonical BRS, and the resulting version is recorded;
- **Realization Verified** — downstream requirements are covered and each change is released and verified, or has an approved exclusion or deferral; required success evidence is available.

The delta remains as an immutable change record after both milestones.

## Trade-offs

| Choice | Benefit | Cost |
|---|---|---|
| Edit canonical BRS directly | Minimal process overhead | Weak provenance, review isolation, and concurrent-change control |
| Complete BRS per initiative | Self-contained initiative view | Duplicated current state and difficult reconciliation |
| BRS Delta plus canonical BRS | Clear change scope, history, review, and downstream tracking | Requires stable identifiers, versions, and an application workflow |
| BRS Delta as delivery tracker | One visible page | Rapidly becomes stale and duplicates specialized systems |

## Common Mistakes

- Presenting `BRS Delta` as an ISO or IIBA artifact rather than a local convention.
- Creating exactly one delta for every incoming document instead of one coherent business change.
- Copying the entire canonical BRS into the delta.
- Omitting the target BRS and exact base version.
- Recording only additions and missing modifications, retirements, or deliberate impact checks.
- Applying raw discussion, rejected alternatives, and temporary project details to the canonical BRS.
- Using one ambiguous `In Progress` status for analysis, BRS application, delivery, and verification.
- Calculating progress as an unweighted percentage of manifest rows.
- Reproducing Jira tasks or test cases instead of linking their authoritative records.
- Marking the delta complete when the BRS is updated without distinguishing downstream realization.
- Leaving a delta open indefinitely because baseline and realization closure were not defined separately.

## Practical Checklist

A BRS Delta is controlled when:

- [ ] The raw request and authoritative sources are preserved.
- [ ] The canonical BRS, base version, and target scope are explicit.
- [ ] The delta represents one coherent business change.
- [ ] Affected capabilities include both proposed changes and deliberate impact checks.
- [ ] Every semantic change has a stable Change ID and Add, Modify, Retire, or Impact Check operation.
- [ ] Local, cross-cutting, and external rules are distinguished.
- [ ] The Change Manifest links to detailed capability or cross-cutting changes.
- [ ] Business analysis and BRS merge status are separate from realization status.
- [ ] Open questions, conflicts, blockers, owners, and next actions are visible.
- [ ] Concurrent changes against the same BRS elements are resolved before application.
- [ ] Only approved durable business content is applied to the canonical BRS.
- [ ] The resulting BRS version and canonical element links are recorded.
- [ ] Downstream requirements, delivery, and evidence are linked without duplicating their source-of-truth systems.
- [ ] Baseline Applied and Realization Verified are closed independently.

## Example

Assume the canonical baseline is `BRS-CATALOG v3.2` and the source request states:

> Add an availability flag to every catalog item and hide unavailable items in all customer channels. Existing owners must still see their items and history.

### Delta Header

| Field | Value |
|---|---|
| Delta ID | `DELTA-CATALOG-017` |
| Target BRS | `BRS-CATALOG v3.2` |
| Intended target | `BRS-CATALOG v3.3` |
| Business owner | Catalog product owner |
| Status | In Review |
| Source | `SRC-CATALOG-042` |

### Baseline Progress

| Capability | Analysis status | BRS merge status | Blocker | Next action |
|---|---|---|---|---|
| `CAP-01 Product Discovery` | Approved | Not Applied | None | Apply `CHG-001` |
| `CAP-02 Transaction Eligibility` | In Review | Not Applied | `OQ-03` | Approve transaction rule |
| `CAP-03 Owner Access and History` | Approved | Not Applied | None | Record impact check |
| Cross-cutting | Draft | Not Applied | Effective-time decision | Resolve `OQ-04` |

### Change Manifest

| Change ID | Capability | Element and operation | Baseline status | Detail |
|---|---|---|---|---|
| `CHG-001` | `CAP-01` | Modify `BR-CAP01-04` | Approved | Channel availability affects discovery |
| `CHG-002` | `CAP-02` | Add `BR-CAP02-03` | In Review | Prohibit a new unavailable transaction |
| `CHG-003` | `CAP-03` | Impact check `BR-CAP03-01` | Confirmed unchanged | Owner access remains valid |
| `CHG-004` | Cross-cutting | Add `BR-CROSS-02` | Draft | Define policy-effective time |

### Detailed Change

#### `CHG-002` — Add `BR-CAP02-03`

Current state:

> No canonical rule defines transaction behavior when an item is unavailable in the current channel.

Proposed state:

> An item unavailable in the current channel must not be accepted for a new transaction in that channel.

Rationale:

> Prevent different channels from making inconsistent transaction decisions.

Target:

> `BRS-CATALOG v3.3 / CAP-02 Transaction Eligibility`

### Downstream Coverage

| Change ID | Requirement links | Delivery link and status | Evidence | Next action |
|---|---|---|---|---|
| `CHG-001` | `SyRS-142` | `EPIC-81` — In progress | Test plan pending | Complete channel adoption |
| `CHG-002` | `SyRS-146` — Draft | Not planned | Not defined | Approve business rule |
| `CHG-003` | No change required | No change required | Regression suite | Execute regression |
| `CHG-004` | Blocked | Not started | Not defined | Resolve effective-time decision |

After approval, `CHG-001` through `CHG-004` receive final dispositions. Approved normative changes are applied to `BRS-CATALOG v3.3`; the raw source, analysis, questions, and rejected alternatives remain in `DELTA-CATALOG-017`.

## Interview Angle

> I keep the canonical BRS as the current business truth and use a BRS Delta as a reviewable local change set against a specific baseline version. The delta contains a capability progress view, an atomic Change Manifest, detailed Add/Modify/Retire/Impact Check items, and downstream coverage. Approved normative content is applied to the next BRS version, while the delta remains as provenance and tracks baseline application separately from delivery and verification.

## Related Topics

- [Choosing the First Requirements Artifact](01-choosing-the-first-requirements-artifact.md)
- [Tailoring the Business Requirements Baseline](02-tailoring-the-business-requirements-baseline.md)
- [Business Requirements Specification template](03-business-requirements-specification-template.md)
- [Requirements discovery techniques](requirements-discovery-techniques.md)
- [Product and Requirements index](README.md)
