# Documentation As Code

Documentation as Code means treating important engineering documentation like the code it supports: versioned, reviewed, searchable, close to the system, and changed through the same delivery culture.

## Use It For

- Architecture decisions
- API and event contracts
- Runbooks
- Production readiness checklists
- Engineering standards
- Design docs
- Migration plans
- Incident learnings

## Principles

- Keep docs close to the code or repository they describe.
- Prefer Markdown and plain text formats when possible.
- Review documentation changes in pull requests.
- Use templates for repeated decisions and operational procedures.
- Link from high-level indexes to detailed notes.
- Archive or mark stale docs instead of letting them silently rot.
- Optimize for future readers who were not in the meeting.

## Minimal Repository Structure

```text
docs/
  README.md
  decisions/
  runbooks/
  architecture/
  operations/
```

## Documentation Review Checklist

- The document has one clear purpose.
- The intended reader is obvious.
- The status is visible: draft, active, deprecated, or archived.
- The owner or maintaining team is named where useful.
- The document links to related code, tickets, dashboards, ADRs, or runbooks.
- The content describes current reality or explicitly labels future intent.
- The document says what changed when a decision or process evolved.

## Template For Reusable Docs

```markdown
# <Document Title>

Status:

Owner:

Last reviewed:

## Purpose

## Context

## Current Decision Or Process

## Operational Notes

## Risks And Open Questions

## Links
```

## Culture Rules

- A decision that matters should leave a trace.
- A runbook that saves an incident should be reviewed after the incident.
- A stale doc is worse than a missing doc if readers trust it.
- Documentation work should be part of delivery, not a separate heroic cleanup.
- Good docs reduce meetings, onboarding time, production confusion, and repeated explanations.
