# ADR Template

Use an Architecture Decision Record when a decision is hard to reverse, affects multiple teams, changes operational risk, or becomes part of the system's long-term shape.

## Template

```markdown
# ADR: <Decision Name>

## Status

Proposed | Accepted | Superseded | Deprecated

## Date

YYYY-MM-DD

## Context

What problem are we solving?
What constraints, requirements, and assumptions shape the decision?
What has changed that makes the decision necessary now?

## Decision Drivers

- Driver 1
- Driver 2
- Driver 3

## Options Considered

### Option A

Summary:

Pros:

- ...

Cons:

- ...

### Option B

Summary:

Pros:

- ...

Cons:

- ...

## Decision

We decided to ...

## Consequences

Positive:

- ...

Negative:

- ...

Trade-offs accepted:

- ...

## Validation

How will we know this decision works?

- Metric, test, review, production signal, or migration milestone

## Follow-ups

- ...

## Links

- Related requirements
- Related diagrams
- Related ADRs
```

## Decision Quality Checklist

- The decision is written as a concrete choice, not a vague preference.
- The options are realistic and comparable.
- The trade-offs are explicit.
- The negative consequences are not hidden.
- The validation criteria are observable.
- The record can be understood by someone who was not in the meeting.
