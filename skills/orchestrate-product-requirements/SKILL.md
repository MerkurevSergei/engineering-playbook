---
name: orchestrate-product-requirements
description: Maintain a human-readable, evidence-driven requirements workflow from an initial need through an approved BRS and downstream specifications. Use when Codex must start or resume product requirements work, ingest stakeholder statements or documents, show what has been processed, identify gaps, select the next analytical activity, track BRS coverage, or coordinate elicitation, analysis, verification, validation, approval, and systems analysis. This skill owns Markdown workflow state, dispatch, and handoff checkpoints; it does not conduct interviews or author requirements content itself.
---

# Orchestrate Product Requirements

Coordinate work from explicit Markdown state. A human must be able to take over by reading and editing the repository without YAML, scripts, or hidden conversation memory.

Mirror the user's language in conversation. Keep stable IDs and controlled status values in English.

## Start From the Handoff Page

1. Read repository instructions and relevant conversation context.
2. Open `requirements/work-status.md` first.
3. Follow its links to the source, activity, evidence, question, analysis, decision, and traceability registers and to affected BRS sections.
4. If the page is missing, inspect existing requirements artifacts before using `$organize-project-requirements` to create or reconcile the Markdown package.
5. Maintain one requirements package per initiative. Do not create an Intake card or a competing route-state artifact.

Each entity has one authoritative Markdown table:

- sources -> `working/source-register.md`;
- elicitation and analysis activities -> `working/activity-register.md`;
- atomic source information -> `working/evidence-register.md`;
- knowledge gaps -> `working/research-questions.md`;
- normalized interpretations -> `working/analysis-register.md`;
- decisions and conflicts -> `working/decisions-and-conflicts.md`;
- relationships -> `working/traceability.md`;
- business content -> the applicable BRS or capability file.

`work-status.md` is a dashboard and handoff page. It summarizes current state and links to authoritative rows; it must not duplicate their full content.

## Keep Status Dimensions Separate

Do not apply one lifecycle to every entity.

- Source review: `Unreviewed`, `Partial`, `Complete`, `Unavailable`, `Superseded`.
- Activity: `Planned`, `In progress`, `Results captured`, `Results confirmed`, `Analyzed`, `Closed`, `Cancelled`.
- Evidence confirmation: `Unconfirmed`, `Confirmed`, `Authenticated`, `Not applicable`.
- Evidence processing: `New`, `In analysis`, `Routed`, `Closed`.
- Research question: `Open`, `Assigned`, `Answered`, `Resolved`, `Blocked`, `Cancelled`.
- BRS item: `Draft`, `Verified`, `Validated`, `Approved`, `Baselined`, `Disputed`, `Rejected`, `Deferred`, `Superseded`.
- Coverage: `Not started`, `Discovering`, `Drafted`, `Validated`, `Not applicable`.

An Evidence Item is `Closed` only when source and context, confirmation or authentication, classification, disposition, destination or terminal rationale, open questions, and trace links are recorded. Closing evidence never approves a derived requirement.

## Reconcile Before Dispatch

At every start and after every worker returns:

1. Register supplied but untracked people, documents, systems, datasets, and observations.
2. Find the single activity marked `In progress`; resolve multiple active activities before proceeding.
3. Find Evidence Items in `New` or `In analysis`, material unanswered questions, conflicts, and missing destinations.
4. Check that every `Closed` Evidence Item has a disposition and target IDs or a terminal rationale.
5. Check that every BRS item links to supporting analysis and evidence.
6. Recalculate source counts, activity state, BRS coverage, current phase, and the single next action on `work-status.md`.
7. Never mark an entire source `Complete` because one excerpt or one participant contribution was processed.

## Select the Next Action

Choose one action in this priority order:

1. register supplied but untracked input;
2. finish capture or confirmation for the activity already in progress;
3. analyze and route `New` or `In analysis` Evidence Items;
4. resolve blocking authority gaps, conflicts, and high-risk questions;
5. investigate the highest-risk BRS coverage gap;
6. investigate remaining coverage gaps;
7. verify drafted BRS content;
8. validate it with authorized business stakeholders;
9. obtain approval and baseline the BRS;
10. derive and validate downstream stakeholder, system, software, interface, data, quality, transition, and acceptance specifications.

Break ties by decision impact, risk, dependency, source availability, and cost of delay. Record the objective, target IDs, source, method, expected result, and rationale on `work-status.md`.

## Dispatch One Bounded Activity

- For a live stakeholder, use `$conduct-stakeholder-elicitation` with the objective, target questions, known facts, source authority, and expected result quality.
- For Evidence Item analysis, routing, and BRS persistence, use `$organize-project-requirements` with the affected IDs.
- For documents and other fixed artifacts, use `$analyze-fixed-requirements-source` with a declared source scope, target questions, and required result quality.
- For observations, verification, validation, or systems analysis, use the applicable dedicated skill when available. If a required worker is not yet defined, leave a precise pending action instead of performing uncontrolled work inside the orchestrator.

After a worker returns, update the authoritative rows, trace links, affected BRS coverage, and handoff page. Do not treat a prose summary as workflow state.

## Track BRS Coverage

Track at least purpose and need, value and success evidence, scope and context, stakeholders and authority, current state, future state, capabilities, processes and scenarios, information, rules, constraints and quality, risks and assumptions, lifecycle, and approval. Add capability-level rows when initiative-wide status hides local gaps.

A populated section is not necessarily covered. Use `Validated` only when material content is supported, internally consistent, and confirmed as fit for business use by the appropriate authority.

## Apply Phase Gates

Use these phases: `Orientation`, `Business discovery`, `BRS verification`, `BRS validation`, `BRS approval`, `BRS baselined`, `Systems analysis`, `Development ready`.

Do not advance because an interview ended. Advance only when applicable coverage, evidence processing, conflict, and authority conditions pass. Business and systems analysis may overlap by stable capability slice, but downstream requirements must remain traceable to approved or explicitly provisional business content.

## Leave a Human-Usable Checkpoint

At every natural handoff, update and report:

- current phase and activity;
- sources reviewed and their declared review scope;
- Evidence Items created, processed, and still open;
- artifacts and coverage changed;
- blocking questions or conflicts;
- one next action and its rationale;
- exact files and IDs a human should open to continue.

Stop only when user input, unavailable authority, an undefined worker capability, or the requested session boundary requires it. Preserve the restart point in `work-status.md`.
