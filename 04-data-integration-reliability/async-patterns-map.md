# Async Patterns Map

Asynchronous design is not one decision. It combines contracts, delivery semantics, state ownership, retries, idempotency, ordering, and operations.

## First Decision Questions

- What business event or command is being communicated?
- Who owns the source of truth?
- Does the producer need to know whether the consumer completed the work?
- Is duplicate delivery acceptable if consumers are idempotent?
- Does message order matter globally, per entity, or not at all?
- How will failures be detected, retried, parked, and repaired?
- What is the operational signal when the workflow is stuck?

## Pattern Map

| Pattern | Use When | Watch For |
|---|---|---|
| Event notification | Consumers only need to know that something changed | Consumers may need extra reads; schema must stay stable |
| Event-carried state transfer | Consumers need enough data to act without synchronous calls | Payload growth, stale data, privacy exposure |
| Command message | One service asks another to perform work asynchronously | Ownership confusion, retry side effects |
| Outbox | Database change and message publication must not diverge | Relay lag, duplicate messages, table cleanup |
| Inbox | Consumer must record processed messages transactionally | Storage growth, poison messages |
| Idempotency key | The same request or message may arrive more than once | Key scope, retention, conflict response |
| Retry with backoff | Failure is often temporary | Retry storms, hidden permanent failures |
| Dead letter queue | Messages need manual or automated quarantine | DLQ without ownership becomes a silent graveyard |
| Saga | A business transaction spans multiple services | Compensation complexity, partial visibility |
| CDC | Existing data changes need to feed downstream systems | Schema drift, replay semantics, source load |
| Request-reply over messaging | Caller needs a response but synchronous coupling is risky | Correlation IDs, timeouts, state cleanup |

## Delivery Semantics

| Semantic | Meaning | Design Implication |
|---|---|---|
| At most once | A message may be lost but is not redelivered | Useful only when loss is acceptable |
| At least once | A message is delivered one or more times | Consumers must be idempotent |
| Effectively once | The business effect is applied once despite retries | Requires idempotency, transactions, or deduplication |

## Reliability Checklist

- Producer and consumer schemas are versioned.
- Message identity and business identity are both clear.
- Consumers are idempotent for expected duplicate scenarios.
- Retry rules distinguish temporary and permanent failures.
- DLQ ownership, alerting, and repair process are documented.
- Ordering assumptions are explicit and tested.
- Backpressure behavior is known.
- Replay and reprocessing procedures are safe.
- Metrics expose lag, failures, retries, DLQ size, and processing latency.
- Runbooks explain how to repair stuck messages.

## Anti-Patterns

- Using async messaging to hide unclear ownership.
- Publishing events before the database transaction commits.
- Depending on exactly-once marketing language without business-level idempotency.
- Creating a DLQ with no owner, alert, or replay path.
- Sending huge events because service boundaries are not clear.
- Treating Kafka mechanics as a replacement for domain design.
