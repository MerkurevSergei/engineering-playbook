# Knowledge Base Structure

> Status: Draft  
> Source: synthesized from a shared planning chat; personal details removed.

This repository is a public engineering playbook, not a full personal knowledge base. It should contain cleaned, generalized materials: patterns, checklists, templates, examples, and decision guides that are safe to publish.

## Core Principle

Build the knowledge base as a working engineering system, not as a technology catalog.

Use this flow for each topic:

```text
Why it matters -> principles -> decisions -> implementation -> verification -> interview/English explanation
```

Example:

```text
Asynchronous integration -> delivery guarantees -> Kafka as one tool -> outbox/retry/idempotency/DLQ -> operations -> interview case
```

## Public vs Private

Use two repositories with different purposes:

```text
engineering-playbook       public, polished or clearly marked draft material
engineering-knowledge-base private, raw notes and personal/work-specific material
```

Put material into `engineering-playbook` when it is:

- generalized and safe to publish;
- based on your own synthesis, not copied course/book notes;
- free of company data, internal processes, sensitive examples, and personal career details;
- useful as a reusable engineering artifact.

Put material into `engineering-knowledge-base` when it is raw, personal, company-specific, interview-private, career-private, or contains details that need sanitization.

## Recommended Areas

```text
01-product-requirements/
02-architecture-design/
03-backend-engineering/
04-data-integration-reliability/
05-delivery-quality-operations/
06-technical-leadership/
90-career-packaging/
91-english-for-engineering/
99-archive/
```

## Area Boundaries

Use these questions to place a topic:

| Question | Area |
|---|---|
| What does the business need? | `01-product-requirements` |
| Which solution should we choose and why? | `02-architecture-design` |
| How should we write the code? | `03-backend-engineering` |
| How do systems interact and preserve consistency? | `04-data-integration-reliability` |
| How do we test, release, observe, and operate it? | `05-delivery-quality-operations` |
| How do we influence engineering work across people and teams? | `06-technical-leadership` |
| How do we package experience for career use? | `90-career-packaging` |
| How do we explain it in English? | `91-english-for-engineering` |

## Suggested Substructure

```text
01-product-requirements/
  problem-statement.md
  stakeholders-and-goals.md
  scope.md
  functional-requirements.md
  business-rules.md
  non-functional-requirements.md
  acceptance-criteria.md
  definition-of-ready.md
  requirements-review-checklist.md

02-architecture-design/
  architecture-drivers.md
  quality-attributes.md
  architecture-styles.md
  ddd-strategic-design.md
  ddd-tactical-design.md
  service-boundaries.md
  architecture-documentation.md
  adr-template.md

03-backend-engineering/
  java-core.md
  spring.md
  hibernate-jpa.md
  application-layer.md
  validation-error-handling.md
  security-basics.md
  code-quality.md
  refactoring.md

04-data-integration-reliability/
  databases.md
  transactions-consistency.md
  api-contracts.md
  messaging-kafka.md
  async-patterns.md
  reliability-patterns.md
  performance.md
  observability-for-integration.md

05-delivery-quality-operations/
  testing-strategy.md
  contract-testing.md
  ci-cd.md
  release-management.md
  production-readiness.md
  incident-management.md
  security-audit-compliance.md

06-technical-leadership/
  engineering-standards.md
  code-review-culture.md
  mentoring.md
  hiring-interviewing.md
  decision-making.md
  cross-team-communication.md
  planning-decomposition.md
```

## Topic Note Template

Use one main location per topic and links from related areas to avoid duplicates.

```markdown
# Topic Name

> Status: Draft
> Area: data-integration-reliability

## Essence

What this is in plain language.

## Problem

What problem this solves.

## When To Use

Typical situations where it fits.

## When Not To Use

Limitations, trade-offs, and anti-patterns.

## Implementation

Practical details, examples, and constraints.

## Risks

Common mistakes and failure modes.

## Related Topics

Links to neighboring notes.

## Artifact

Template, checklist, ADR, example, or review guide.

## Interview Angle

How to explain the topic in an interview.

## English Version

Short English explanation.
```

## Example Placement: Outbox

Primary location:

```text
04-data-integration-reliability/async-patterns.md
```

Related links:

```text
04-data-integration-reliability/transactions-consistency.md
04-data-integration-reliability/messaging-kafka.md
04-data-integration-reliability/observability-for-integration.md
05-delivery-quality-operations/testing-strategy.md
90-career-packaging/interview-cases.md
91-english-for-engineering/interview-answers.md
```

Kafka is a messaging technology. Outbox, retry, DLQ, idempotency, deduplication, and saga are reliability patterns. Keep those concepts separate so one folder does not become a dump for every async topic.

## Workflow

```text
raw notes -> private knowledge base -> synthesis -> public playbook
```

Publish directly to this repository only when the material is already general, safe, and written in your own words.

Use simple statuses:

| Status | Meaning |
|---|---|
| Draft | Useful but unfinished |
| Review | Needs cleanup or validation |
| Stable | Good enough to reference |
