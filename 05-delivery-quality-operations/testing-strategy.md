# Testing Strategy

A testing strategy explains where confidence should come from. It should reduce expensive late feedback and make the riskiest behavior visible early.

## Test Layers

| Layer | Purpose | Good For | Avoid |
|---|---|---|---|
| Unit | Verify isolated business logic | Rules, calculations, branching, pure functions | Framework-heavy tests with little behavior |
| Integration | Verify integration with real infrastructure or libraries | Database mappings, transactions, serialization, external client behavior | Rebuilding full end-to-end flows |
| Contract | Verify producer and consumer expectations | APIs, events, compatibility, microservice boundaries | Treating contracts as full business tests |
| Component | Verify one service with controlled dependencies | Service behavior, adapters, persistence, messaging edges | Too many mocked internals |
| End-to-end | Verify critical user journeys across systems | Release smoke, happy-path confidence, critical flows | Covering every edge case |
| Exploratory | Find unknown risks through human investigation | UX, unusual workflows, operational surprises | Replacing repeatable checks |

## Microservice Testing Rules

- Put business rules as low in the test pyramid as possible.
- Use contract tests for service boundaries.
- Use Testcontainers or equivalent tools when infrastructure behavior matters.
- Keep end-to-end tests few, stable, and business-critical.
- Verify failure scenarios: timeouts, retries, duplicate messages, invalid payloads, missing permissions.
- Test migration and rollback paths when data shape changes.
- Treat test data setup as production-like engineering, not incidental scripting.

## CI Ordering

1. Static checks and formatting.
2. Unit tests.
3. Integration and component tests.
4. Contract verification.
5. Build artifact and image.
6. Security and dependency checks.
7. Deployment to test environment.
8. Smoke and selected end-to-end checks.

## Strategy Template

```markdown
## Testing Strategy

Critical risks:

- ...

Test layers used:

- Unit:
- Integration:
- Contract:
- Component:
- End-to-end:

Required test data:

- ...

CI gates:

- ...

Known gaps:

- ...
```

## Review Questions

- What bug would be most expensive to discover in production?
- Which tests fail fast when business rules break?
- Which tests prove integration contracts still match?
- Which checks protect database migrations?
- Which tests are flaky, slow, or redundant?
- Which production signals complement automated tests?
