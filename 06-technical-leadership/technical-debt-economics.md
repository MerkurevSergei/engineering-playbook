# Technical Debt Economics

Technical debt is not just ugly code. It is any accumulated design, code, process, tooling, documentation, or requirements problem that makes future change slower, riskier, or more expensive.

## Debt Signals

- The same change repeatedly takes longer than expected.
- Teams avoid touching a module because it is fragile.
- Releases require manual steps that only a few people understand.
- Incidents repeat because the root cause is not removed.
- Tests are slow, flaky, or missing around critical behavior.
- Documentation exists but does not help decisions or operations.
- Integration failures require manual reconciliation.

## Interest

Debt interest is the extra cost paid repeatedly because the debt remains.

```text
interest rate = (actual effort - pure implementation effort) / pure implementation effort
```

Example:

```text
Pure implementation effort: 2 days
Actual effort with debt: 5 days
Debt interest: (5 - 2) / 2 = 150%
```

The exact number is less important than the conversation it creates: debt should be discussed as recurring cost, risk, and opportunity loss.

## Economic Case Template

```markdown
## Technical Debt Case

Debt item:

Where it appears:

Current recurring cost:

- Extra development effort:
- Incident or support effort:
- Waiting time:
- Release risk:

Expected future cost if ignored:

Proposed fix:

Fix cost:

Expected payback:

Risks of fixing:

Risks of not fixing:

Decision needed:
```

## Prioritization Questions

- How often does this debt create extra work?
- Which team or business outcome pays the interest?
- Is the debt blocking strategic work or only annoying engineers?
- Can the fix be delivered incrementally?
- Does the fix reduce incident risk, lead time, or onboarding cost?
- What is the cost of doing nothing for one quarter?
- What evidence would convince non-engineering stakeholders?

## Repayment Patterns

- Fix while touching the area for a related feature.
- Reserve explicit capacity for debt with visible outcomes.
- Convert repeated manual work into automation.
- Add missing tests before risky refactoring.
- Break large rewrites into risk-reducing slices.
- Retire unused paths before redesigning active ones.
- Document the decision when debt is accepted intentionally.

## Anti-Patterns

- Calling every disliked implementation detail technical debt.
- Asking for a rewrite without a cost model.
- Hiding debt work inside feature estimates without visibility.
- Paying debt that does not reduce risk, delay, or operational cost.
- Treating debt as a one-time cleanup instead of a portfolio.
