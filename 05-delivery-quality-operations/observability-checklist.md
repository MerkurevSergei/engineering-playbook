# Observability Checklist

Observability is the ability to understand system behavior from its external signals: logs, metrics, traces, events, alerts, and dashboards.

## Core Signals

| Signal | Purpose | Examples |
|---|---|---|
| Logs | Explain discrete events and decisions | Request failures, validation errors, state transitions |
| Metrics | Track numeric behavior over time | Latency, error rate, throughput, queue lag |
| Traces | Follow work across service boundaries | API call chain, message processing, database calls |
| Events | Capture important business or operational milestones | Order created, payment failed, message parked |
| Alerts | Notify humans about action-worthy problems | SLO burn, DLQ growth, dependency outage |
| Dashboards | Support investigation and situational awareness | Service health, release impact, user journey view |

## Checklist

### Logs

- Logs include correlation or trace IDs.
- Logs include stable event names, not only free text.
- Sensitive data is not logged.
- Business failures and technical failures can be distinguished.
- Important state transitions are logged once in a predictable place.

### Metrics

- Service exposes request rate, error rate, duration, and saturation where relevant.
- Business-critical workflows have success, failure, and delay metrics.
- Async consumers expose lag, retry count, DLQ count, and processing latency.
- Metrics have labels that help diagnosis without causing high-cardinality damage.
- SLOs or operational thresholds are documented for critical flows.

### Tracing

- Incoming requests start or continue a trace.
- Outgoing calls propagate trace context.
- Message producers and consumers connect traces where the tooling supports it.
- Slow dependencies are visible in traces.
- Trace sampling strategy is known.

### Alerts

- Alerts are tied to user impact or required operator action.
- Alert thresholds are tested against historical behavior.
- Every alert has an owner and a runbook.
- Alerts distinguish symptoms from causes when possible.
- Warning alerts do not drown out urgent alerts.

### Dashboards And Runbooks

- Dashboards answer "is it healthy?", "what changed?", and "who is affected?".
- Release markers are visible on operational dashboards.
- Runbooks explain first checks, rollback steps, and escalation paths.
- Known failure modes have repair or reconciliation steps.

## Production Readiness Questions

- Can we tell whether users are affected before they report the problem?
- Can we connect a user issue to logs, metrics, and traces?
- Can we detect stuck asynchronous workflows?
- Can we see whether a release improved or degraded the system?
- Can an on-call engineer act without knowing all implementation details?
