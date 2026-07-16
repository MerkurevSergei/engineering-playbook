# Tailoring the Business Requirements Baseline

> Status: Draft
> Area: product-requirements

## Problem

A standards-based BRS can become difficult to use when a team treats its complete coverage model as a mandatory physical outline. The opposite reaction is equally risky: reducing the baseline to a vision paragraph can leave rules, exceptions, ownership, and boundaries implicit.

The practical question is:

> What is the smallest controlled business baseline that makes the initiative safe to refine, and which additional models are justified by its complexity and risk?

## Core Idea

Treat the BRS as one logical baseline and tailor its physical form through progressive disclosure.

Start with one readable page containing the source, problem, outcome, scope, stakeholders, terms, target behavior, rules, scenarios, constraints, questions, and approval. When flat rule and scenario lists become difficult to navigate, introduce a Capability Map and group local behavior into Capability Specifications. Add decision, lifecycle, process, information, or traceability models only when a concrete trigger makes them useful.

Business analysis defines the required outcomes, observable behavior, rules, and business constraints. System analysis turns that intent into system responsibilities, data, interfaces, and responses. Architecture allocates those responsibilities to components and selects implementation mechanisms.

## Sources and Standards

| Source | Contribution |
|---|---|
| [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) and the [IEEE record](https://standards.ieee.org/ieee/29148/6937/) | BRS content model, requirements levels, information-item control, and iterative requirements processes |
| Karl Wiegers and Joy Beatty, [Software Requirements, Third Edition](https://www.microsoftpressstore.com/store/software-requirements-9780735679610) | Practical Vision and Scope framing, measurable objectives, stakeholder profiles, risks, features, and scope |
| [IIBA Business Analysis Standard](https://www.iiba.org/knowledgehub/the-business-analysis-standard/4-implementing-business-analysis/4-4-understanding-requirements-and-designs/) | Separation of business, stakeholder, solution, and transition requirements and the use of multiple models |

ISO supplies the coverage model. Wiegers supplies practical authoring techniques. IIBA helps keep requirements levels and models distinct. The physical packaging described here is a local playbook convention.

## When to Use

Use this tailoring approach when:

- the raw request mixes business intent with a proposed technical solution;
- the initiative affects several roles, channels, products, processes, or systems;
- rules contain exceptions or interacting conditions;
- the team needs a shared baseline before system analysis or architecture;
- a complete ISO-shaped document would discourage meaningful review;
- assurance obligations require more control than an informal one-pager provides.

## When Not to Use

Do not create a new standalone package when:

- an approved parent baseline already governs the work and only a controlled delta is needed;
- the change is a local incident correction with no change to business intent;
- the information belongs to an authoritative policy, business case, glossary, or rule catalog that should be linked rather than copied.

Tailoring removes unnecessary duplication. It does not remove information that is material to a business decision.

## How It Works

### 1. Choose the Practical Form

| Situation | Form |
|---|---|
| Small governed change | [BRS Delta](04-working-with-brs-deltas.md) linked to the existing baseline |
| Typical initiative | Core [BRS template](03-business-requirements-specification-template.md), normally with one inline capability |
| Large initiative | Capability Map, scoped Capability Specifications, and Cross-Cutting Concerns |
| Complex or high-assurance initiative | Capability-centered baseline plus triggered models, formal traceability, and explicit ISO coverage review |

Avoid presenting these forms as separate industry artifacts. They are tailored representations of one logical baseline.

### 2. Preserve the Requirements Levels

| Level | Example |
|---|---|
| Business analysis | An ineligible customer must not complete a restricted transaction |
| Stakeholder or usage analysis | The customer can view the item but cannot initiate the transaction and receives an appropriate explanation |
| System analysis | The system must determine eligibility before accepting a new transaction and reject the request when eligibility is not confirmed |
| Architecture | A selected component obtains eligibility data and applies the decision through a chosen integration mechanism |

The BRS may link stakeholder scenarios or models, but it must not disguise system responsibilities or architecture decisions as business rules.

### 3. Start with the Core Baseline

The first useful baseline should answer:

- What source initiated the change?
- What problem or opportunity exists now?
- What observable outcome is required?
- What is in scope and explicitly outside it?
- Who receives value, owns the rules, and makes decisions?
- Which terms and business concepts must be unambiguous?
- What target behavior, rules, and material exceptions are required?
- Which assumptions, constraints, dependencies, risks, and questions remain?
- Who can approve, reject, or reshape the initiative?

An open question is acceptable when its impact, owner, and decision date are visible. A question that prevents agreement on the boundary or required behavior blocks the baseline.

### 4. Decompose Large Baselines by Business Capability

A capability is a stable business slice with its own outcome, boundary, decision ownership, and coherent cluster of rules and scenarios. It describes what the business must be able to accomplish or govern. It is not a screen, API, service, database change, or delivery task.

Use capabilities as navigation when global tables would mix unrelated functional areas:

```text
Initiative BRS
├── Initiative context
├── Capability Map
├── Capability Specifications
└── Cross-Cutting Concerns
```

| Initiative level | Capability level |
|---|---|
| Problem and reason for change | Concrete business outcome |
| Initiative objectives and metrics | Capability success evidence |
| Overall scope and non-goals | Capability boundary |
| Sponsor and final approvers | Local participants and rule owners |
| Shared terms and concepts | Capability-specific language |
| Initiative-wide constraints and dependencies | Local dependencies and risks |
| Cross-cutting rules | Capability rules |
| End-to-end scenarios | Capability-local scenarios |

Create a capability when several of these signals are present:

- a coherent result can be explained independently;
- one owner or decision group governs its rules;
- a distinct cluster of rules and scenarios changes together;
- the behavior has a meaningful boundary from other business behavior;
- it can be reviewed or evolved without restating the whole initiative.

Good capability candidates include `Product Discovery`, `Transaction Eligibility`, `Owner Access and History`, `Policy Management`, and `Explanation and Audit`.

Names such as `Mobile UI`, `Availability API`, `Database Changes`, and `Backend Service` describe solution elements, not business capabilities.

For one small capability, keep the specification inline and omit a separate map when it adds no navigation value. For several capabilities, use the map as an index and repeat the same compact specification block for each capability.

Classify rules by scope:

- **Capability rule** — applies inside one Capability Specification.
- **Cross-cutting rule** — governs several capabilities and is recorded once in Cross-Cutting Concerns.
- **External rule** — belongs to an authoritative policy or catalog; retain its authoritative identifier and link instead of copying it.

Apply the same discipline to scenarios. Keep local scenarios with one capability, keep journeys spanning several capabilities as end-to-end scenarios, and use a decision table inside the owning capability when combinations of conditions become the main source of complexity.

### 5. Add Models Only When Triggered

| Model or artifact | Add it when | Do not use it for |
|---|---|---|
| Context or process model | Several participants, handoffs, approvals, or external parties shape the outcome | Component orchestration or deployment topology |
| Decision table or decision model | Conditions interact, exceptions overlap, or combinations are easy to miss | Repeating a simple rule in tabular form |
| State or lifecycle model | Permitted behavior depends on a business object's state or valid transition | Describing technical job or service states |
| Separate rule catalog | Rules are reused, independently owned, regulated, or have their own lifecycle | Splitting a short initiative into many pages |
| Conceptual information model | Meaning, ownership, validity, or relationships between business concepts drive decisions | Database tables, schemas, or serialization |
| Business event catalog | The occurrence and business consequence matter before a transport mechanism is selected | Defining message topics or payload contracts |
| Detailed scenarios | Important positive, negative, ownership, continuity, or transition paths clarify outcomes | Enumerating every condition combination |

State the scope of every model: one capability or the whole initiative. A decision or state model normally belongs to the capability whose behavior it clarifies; an end-to-end process model may be initiative-wide.

### 6. Split the Physical Package Only When It Helps Control

Keep the baseline in one page by default. Extract a linked artifact when at least one condition applies:

- it is reused by more than one initiative;
- it has a separate owner or approval lifecycle;
- it requires a specialized modeling tool;
- it changes independently from the initiative page;
- its size makes stakeholder review materially harder.

There is no required folder tree and no required `traceability.yaml`. A document, wiki page, repository folder, model, or register is acceptable when the logical baseline remains identifiable, versioned, accessible, and traceable.

A Capability Specification follows the same rule: keep it inline until reuse, ownership, independent change, tooling, or readability justifies a linked page.

### 7. Hand Off Without Jumping to Architecture

The business baseline is ready to drive downstream analysis when the team can state the required behavior without knowing:

- which service performs a check;
- which component calls another;
- whether integration is synchronous or asynchronous;
- the API payload, database schema, cache policy, timeout, retry, or deployment topology.

Those decisions belong to system analysis and architecture unless an external business constraint fixes them in advance.

## Trade-offs

| Choice | Benefit | Cost |
|---|---|---|
| One-page core baseline | Fast to review, easy to maintain, low duplication | Requires discipline to add models when ambiguity grows |
| Capability-centered baseline | Keeps owners, rules, scenarios, and questions close to one business outcome | Requires careful separation of local and cross-cutting behavior |
| Linked business package | Supports reuse, separate ownership, and specialized models | Navigation and version control become more important |
| Full high-assurance coverage | Strong auditability and impact analysis | More review effort and explicit applicability decisions |
| Informal vision only | Very fast initial alignment | Rules, exceptions, scope, and decision ownership can remain hidden |

## Common Mistakes

- Copying the complete ISO outline into every initiative without a tailoring decision.
- Calling a local reduced template `BRS-lite` as though it were a recognized standard.
- Treating one page as a reason to omit material rules, exceptions, or dependencies.
- Keeping all rules, scenarios, and owners in flat initiative-wide tables after distinct business capabilities have emerged.
- Naming capabilities after screens, APIs, services, databases, teams, or delivery tasks.
- Copying cross-cutting and external rules into every capability instead of recording one authoritative reference.
- Creating separate files for every rule and scenario before reuse or ownership justifies it.
- Using scenarios as the only requirements model when decision logic or lifecycle behavior is central.
- Writing API fields, services, queues, tables, retries, and caches into business rules.
- Hiding unresolved product decisions in meeting notes instead of the baseline.
- Copying authoritative policies or business cases instead of linking to them.

## Practical Checklist

A tailored business baseline is ready when:

- [ ] The original request and authoritative sources are preserved.
- [ ] The problem is separated from the proposed solution.
- [ ] The outcome and success evidence are observable.
- [ ] Scope, non-goals, stakeholders, and decision rights are explicit.
- [ ] Key terms and business concepts are unambiguous enough for the initiative.
- [ ] Large baselines have a Capability Map whose entries are business outcomes rather than solution components.
- [ ] Each capability has a coherent boundary, owner, local rules, local scenarios, and success evidence.
- [ ] Rules are classified as capability, cross-cutting, or external and are not duplicated across scopes.
- [ ] Capability-local and end-to-end scenarios are separated.
- [ ] A decision table or lifecycle model covers material combinations or states when needed.
- [ ] Models, constraints, assumptions, dependencies, and risks have an explicit capability or initiative scope.
- [ ] Open questions have owners and dates; blocking questions are resolved.
- [ ] The physical package is no more fragmented than ownership, reuse, tooling, or readability requires.
- [ ] Downstream requirements can trace to a source, outcome, rule, constraint, or decision.
- [ ] The business owner can approve, reject, or reshape the initiative.

## Example

Consider this fictional source request:

> Add an availability flag to every catalog item and hide unavailable items in all customer channels. Existing owners must still see their items and history.

The request proposes a data field before the business behavior is unambiguous.

### Problem

Customer channels interpret catalog availability independently. The same item can therefore be offered differently across channels, and a change in policy requires separate channel changes.

### Desired Outcome

All supported channels apply one governed business policy for offering new transactions while preserving access required by existing ownership and history.

### Scope

In scope:

- offering an item for a new transaction;
- access to owned items and historical records;
- management and effective use of a business-owned availability policy across supported channels.

Out of scope:

- channel UI redesign;
- definition of customer-eligibility and pricing policies;
- API, database, and component design.

### Capability Map

| ID | Capability | Business outcome | Owner | Specification |
|---|---|---|---|---|
| `CAP-01` | Product Discovery | Customers receive a consistent catalog offer | Product owner | Inline |
| `CAP-02` | Transaction Eligibility | Unavailable items cannot be used for new transactions | Policy owner | Detailed below |
| `CAP-03` | Owner Access and History | Existing ownership and history remain accessible | Asset domain owner | Inline |
| `CAP-04` | Policy Management | Availability policies have controlled ownership and effective timing | Policy owner | Inline |

### Capability: `CAP-02` — Transaction Eligibility

#### Outcome and Boundary

This capability determines whether a new transaction may be initiated under the catalog-availability policy. It does not define customer eligibility, pricing, settlement, or the technical mechanism used to evaluate the policy.

#### Capability Stakeholders and Decision Rights

| Participant or owner | Need or responsibility | Concern | Decision rights |
|---|---|---|---|
| Customer | Initiate only available transactions | Consistent and understandable restriction | Informed |
| Policy owner | Define transaction-availability rules | Rules remain consistent across channels | Decides rules |
| Channel teams | Apply one governed result | No channel-specific reinterpretation | Consulted |

#### Capability Rules

| ID | Rule | Source and owner | Exceptions |
|---|---|---|---|
| `BR-CAP02-01` | An item unavailable in the current channel must not be offered for a new transaction in that channel | Availability policy; policy owner | Existing ownership is governed by `CAP-03` |

An authoritative customer-eligibility rule would remain under its external policy identifier and be linked here rather than copied into `BR-CAP02-01`.

#### Capability Scenarios

| ID | Trigger and context | Business outcome | Rules or questions |
|---|---|---|---|
| `SC-CAP02-01` | Customer initiates a transaction for an available item | The transaction may proceed to later business checks | `BR-CAP02-01` |
| `SC-CAP02-02` | Customer initiates a transaction for an unavailable item | The new transaction is not offered or accepted | `BR-CAP02-01` |

#### Local Dependencies and Success Evidence

| Type | Item | Owner | Consequence or evidence |
|---|---|---|---|
| Dependency | Current channel-availability policy | Policy owner | A transaction decision cannot be made without an applicable policy |
| Success evidence | Supported channels produce the same availability decision for the same context | Product owner | Cross-channel consistency review |

### Cross-Cutting Rule

`BR-CROSS-01` — A new availability policy applies to affected discovery and transaction behavior from its approved business-effective time.

This rule is recorded once because it governs `CAP-01`, `CAP-02`, and `CAP-04`.

### End-to-End Scenario

| ID | Capabilities | Trigger and context | Business outcome and rules |
|---|---|---|---|
| `SC-E2E-01` | `CAP-04`, `CAP-01`, `CAP-02` | Availability changes after a customer opens an item but before a new transaction is initiated | Discovery and transaction behavior use the policy applicable at the agreed decision point; `BR-CROSS-01` |

### Cross-Capability Open Questions

- Is an unavailable item hidden completely or visible with restricted actions across `CAP-01` and `CAP-02`?
- Which explanation can be shown to the customer?
- What happens to a transaction created before the policy changed?
- At what business moment does a new policy become effective?

### Downstream Transition

Business rule:

> An item unavailable in a channel must not be offered for a new transaction in that channel.

Candidate system requirement:

> Before accepting a new transaction, the system shall determine whether the item is available in the current channel under the policy effective for that transaction.

Later architecture work decides where the policy is evaluated, how data is obtained, and which interfaces or storage mechanisms are used.

## Interview Angle

> I use the BRS as a logical coverage model and tailor its physical form to the initiative. I start with one controlled page. When flat catalogs become hard to navigate, I introduce a Capability Map, keep local rules and scenarios with their business capability, and record shared behavior once as a cross-cutting concern. I add models or split pages only for concrete complexity, ownership, reuse, tooling, or readability needs.

## Related Topics

- [Choosing the First Requirements Artifact](01-choosing-the-first-requirements-artifact.md)
- [Business Requirements Specification template](03-business-requirements-specification-template.md)
- [Working with BRS Deltas](04-working-with-brs-deltas.md)
- [Requirements discovery techniques](requirements-discovery-techniques.md)
- [System boundary checklist](system-boundary-checklist.md)
- [Product and Requirements index](README.md)
