---
name: analyze-fixed-requirements-source
description: Review one fixed requirements source within a declared scope and record traceable atomic Evidence Items, exact locators, coverage, and follow-up questions in human-readable Markdown registers. Use when Codex must analyze a policy, regulation, contract, specification, report, dataset, existing system artifact, exported correspondence, or other source whose author cannot be interviewed in the current activity. This skill authenticates and decomposes source content but does not accept it as a requirement, synthesize BRS content, or choose the initiative-wide route.
---

# Analyze Fixed Requirements Source

Analyze one fixed source as a bounded activity. Preserve source identity and exact locators; do not rewrite the whole artifact into the requirements package.

Mirror the user's language in conversation. Keep stable IDs and controlled status values in English.

## Establish the Activity Contract

Read `requirements/work-status.md` and the working registers. Obtain or establish:

- one source ID and one activity ID;
- source type, title, owner or publisher, stable path or link, version, and date when known;
- declared review scope;
- target research-question or coverage IDs;
- expected result quality and decision affected;
- applicable access, confidentiality, citation, and quotation constraints.

If the source identity or review scope is materially ambiguous, register it as `Unreviewed` and clarify that ambiguity before claiming coverage.

## Verify Identity, Not Truth

Check that the artifact inspected matches the recorded title, version, location, and relevant scope. Record known authority and jurisdiction separately.

`Authenticated` means that the finding is traceable to the inspected artifact and locator. It does not mean that the content is current, legally authoritative, internally consistent, accepted by the business, or a requirement. Create questions for those uncertainties.

## Review the Declared Scope

1. Read enough context to interpret the relevant section correctly.
2. Identify material statements, facts, rules, constraints, definitions, decisions, assumptions, risks, scenarios, measures, and solution descriptions.
3. Ignore purely editorial text and duplication unless it creates ambiguity or conflict.
4. Split compound content into atomic findings without losing conditions, exceptions, applicability, or normative strength.
5. Record every material finding in `working/evidence-register.md` with its exact page, section, paragraph, row, field, timestamp, or other stable locator.
6. Use a faithful paraphrase by default. Include only a short necessary excerpt when exact wording governs interpretation and quotation is permitted.
7. Mark each finding `Confirmation: Authenticated`, `Processing: New`, and `Disposition: Pending`.

Use this minimum row shape:

```markdown
| Evidence ID | Source / activity | Locator or context | Confirmed statement, finding, or observation | Confirmation | Processing | Analysis IDs | Disposition | Target IDs or terminal rationale |
| EI-### | SRC-### / EA-### | section, page, row, or field | faithful atomic finding | Authenticated | New | — | Pending | — |
```

Do not decide whether a finding belongs in the BRS, a downstream specification, a question, or a rejection. That disposition belongs to the analysis worker.

## Track Source Coverage

Set source review status by declared scope:

- `Unreviewed`: relevant content has not been examined;
- `Partial`: only part of the declared scope is examined or material findings remain uncaptured;
- `Complete`: the declared scope is examined and every identified material finding has an Evidence Item;
- `Unavailable`: the source cannot be accessed sufficiently;
- `Superseded`: a controlled successor replaces it for the declared purpose.

Record open versus total material item counts. `Complete` source review does not require all Evidence Items to be analyzed, but the handoff page must show how many remain open. Never extrapolate `Complete` beyond the recorded review scope.

## Handle Conflicts and Gaps

- Record internal contradictions as separate Evidence Items and create a conflict candidate.
- Record missing referenced attachments, definitions, tables, or versions as research questions or source leads.
- When the artifact refers to another authority, register that authority as a candidate source rather than treating the citation as reviewed.
- When tables, figures, calculations, or examples change the meaning, preserve their locator and interpretation uncertainty.
- Do not silently repair source errors.

## Close and Hand Off

Update the source row, activity row, Evidence Item rows, research questions, and `work-status.md`. Set the activity to `Results captured`; fixed-source findings need no participant confirmation. The orchestrator or analysis worker moves the activity to `Analyzed` or `Closed` after all findings receive dispositions.

Report:

- source identity and declared review scope;
- coverage status and portions not reviewed;
- created Evidence Item IDs and exact locators;
- missing dependencies, contradictions, and questions;
- open versus total material item count;
- exact files and IDs to process next.
