# Quality Attributes Checklist

Quality attributes describe how the system must behave, not only what it must do. Use this checklist during requirements review, architecture design, and production-readiness review.

## Attribute Map

| Attribute | Questions | Useful Evidence |
|---|---|---|
| Availability | How much downtime is acceptable? Which user journeys must keep working? | SLO, uptime target, failure budget |
| Reliability | What failures must the system tolerate? What must be retried, compensated, or reconciled? | Failure scenarios, retry policy, recovery test |
| Performance | Which operations have latency limits? What is acceptable p95 or p99 behavior? | Load test, production metrics, latency budget |
| Scalability | What growth is expected in users, traffic, data, tenants, or integrations? | Capacity model, scaling trigger, bottleneck analysis |
| Consistency | Where is strong consistency required? Where is eventual consistency acceptable? | Data ownership map, reconciliation strategy |
| Security | What assets need protection? Who can access which operation and data? | Threat model, access matrix, audit log |
| Privacy | Which personal or sensitive data is collected, stored, exported, or deleted? | Data classification, retention policy |
| Maintainability | How easy is it to change business rules, contracts, or integrations? | Module boundaries, test coverage, change history |
| Testability | Can the system be verified without fragile end-to-end tests? | Test pyramid, contract tests, test data strategy |
| Deployability | Can changes be released safely and reversed when needed? | CI/CD checks, rollback plan, feature flags |
| Observability | Can operators understand health, failures, and user impact? | Logs, metrics, traces, dashboards, alerts |
| Operability | Can support teams diagnose and repair common problems? | Runbook, admin tools, incident playbook |

## Attribute Scenario Template

```markdown
## Quality Attribute Scenario

Attribute:

Stimulus:

Source of stimulus:

System state:

Expected response:

Response measure:

Operational owner:
```

## Review Questions

- Which attributes are truly business-critical?
- Which attributes conflict with each other?
- Which attributes can be measured before production?
- Which attributes require architecture decisions now?
- Which attributes can be deferred safely?
- What failure or abuse scenario would embarrass the system if ignored?

## Common Traps

- Listing quality attributes without measurable scenarios.
- Saying the system must be scalable without a growth model.
- Over-designing for theoretical scale while ignoring operational visibility.
- Treating security as a final review instead of a design input.
- Relying on end-to-end tests for behavior that should be checked earlier.
