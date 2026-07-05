# System Boundary Checklist

Use this checklist when a product, feature, integration, or service boundary is still blurry.

## Good Boundary Outcome

A good boundary makes it clear what the system is responsible for, what it depends on, what it refuses to own, and how teams can verify that the boundary works in production.

## Checklist

### Purpose

- What user or business outcome does this system support?
- What problem would remain unsolved if this system did not exist?
- What decisions does the system make on its own?
- What decisions are made outside the system?

### Actors

- Who initiates work in the system?
- Who receives output from the system?
- Which internal teams operate, support, or consume it?
- Which external systems or third parties interact with it?

### Inputs And Outputs

- What commands, events, files, API calls, or manual actions enter the system?
- What data does the system return, publish, store, or export?
- Which inputs are trusted, partially trusted, or untrusted?
- Which outputs must be stable contracts?

### Included Responsibilities

- Which capabilities are explicitly in scope?
- Which business rules are owned here?
- Which data is created or mastered here?
- Which operational responsibilities belong here: monitoring, alerts, support, retries, reconciliation?

### Excluded Responsibilities

- Which capabilities are intentionally out of scope?
- Which data belongs to another system of record?
- Which validations or decisions are delegated elsewhere?
- Which future ideas should be parked as non-goals?

### External Dependencies

- Which upstream systems can block this system?
- Which downstream consumers can be broken by this system?
- What happens when a dependency is slow, unavailable, or returns inconsistent data?
- Which dependency contracts need versioning, compatibility rules, or fallbacks?

### Data Ownership

- What entities does this system own?
- What entities does it only cache, mirror, enrich, or reference?
- What is the source of truth for each critical field?
- What data retention, privacy, audit, or compliance constraints apply?

### State And Lifecycle

- What are the main states of the business object?
- Which transitions are allowed, forbidden, or manual-only?
- What creates, updates, completes, cancels, archives, or deletes the object?
- How are partial failures and repeated requests handled?

### Quality Attributes

- What availability, latency, throughput, consistency, security, and observability expectations shape this boundary?
- Which failure modes must be visible to operators?
- Which operations need idempotency, retries, deduplication, or compensation?
- What is the smallest useful production-readiness definition?

## Boundary Statement Template

```markdown
## System Boundary

This system exists to ...

It is responsible for:

- ...

It is not responsible for:

- ...

Primary actors:

- ...

Owned data:

- ...

External dependencies:

- ...

Open boundary questions:

- ...
```

## Review Questions

- Can a new engineer explain what this system does not own?
- Can a product owner explain the business outcome without naming implementation details?
- Can an operator identify who is responsible during an incident?
- Can an API or event consumer understand which contract is stable?
