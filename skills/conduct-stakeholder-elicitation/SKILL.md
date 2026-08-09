---
name: conduct-stakeholder-elicitation
description: Prepare, conduct, and confirm one goal-driven requirements elicitation activity with a live stakeholder, producing atomic confirmed Evidence Items and follow-up sources or questions in human-readable Markdown registers. Use when an orchestrator or user asks Codex to interview a sponsor, business owner, domain expert, user, compliance owner, operations representative, or other live source. This skill conducts the conversation but does not analyze fixed artifacts, synthesize BRS content, approve requirements, or choose the initiative-wide route.
---

# Conduct Stakeholder Elicitation

Conduct one bounded live-source activity. The activity may span several conversational turns, but every question must serve its stated objective.

Mirror the participant's language. Keep controlled IDs and status values in English.

## Establish the Activity Contract

Read the current requirements state and use facts already known. Obtain or establish:

- one activity ID and objective;
- the participant's identity or role, knowledge area, and decision authority;
- target research-question or coverage IDs;
- required result quality and material decisions affected;
- known facts, existing conflicts, and supplied sources.

If invoked without an orchestrator, create only the minimum row in `working/activity-register.md` needed to proceed and return it for later reconciliation. Do not create an Intake card.

## Prepare Questions

Choose questions from the activity objective, not from BRS section order. Ask at most three short related questions at a time. Prefer open questions first, then use probes for boundaries, examples, exceptions, evidence, measures, authority, and terminology.

Do not ask for facts already established. Do not treat a participant as authoritative outside their stated jurisdiction. When the participant identifies another person, document, dataset, system, or observed process, register it as a candidate source; never claim that the initiative-wide source inventory is complete.

## Conduct the Conversation

- Separate current facts, desired outcomes, problems, rules, constraints, assumptions, risks, stakeholder needs, and solution ideas.
- Challenge leading, ambiguous, compound, unverifiable, or prematurely technical statements professionally.
- Ask what evidence or authority supports consequential claims.
- Keep rough wording and conversational filler transient unless audit, legal, research, or user instructions require a transcript.
- Do not turn a proposed screen, API, workflow, or technology into a business requirement without establishing the underlying need and any genuine constraint.

## Form Evidence Items

After each coherent topic or before context may be lost:

1. Split material information into atomic items without recording every sentence.
2. Normalize each item while preserving the participant's intended meaning.
3. Retain its source, activity, topic or locator, date when material, and affected question IDs.
4. Present the normalized items to the participant and request explicit correction or confirmation.
5. Replace corrected unconfirmed wording; do not preserve rejected drafts as competing evidence.
6. Add confirmed items to `working/evidence-register.md` with `Confirmation: Confirmed` and `Processing: New`.

Confirmation means only that the participant agrees the meaning was captured accurately. It is not analysis, acceptance, approval, or baseline inclusion.

Use this minimum Markdown row shape:

```markdown
| Evidence ID | Source / activity | Locator or context | Confirmed statement | Confirmation | Processing | Analysis IDs | Disposition | Target IDs |
| EI-### | SRC-### / EA-### | topic or context | confirmed atomic meaning | Confirmed | New | — | Pending | — |
```

## Handle Disagreement and Authority

- If the participant rejects the normalization, revise and reconfirm it.
- If two sources disagree, preserve both confirmed meanings and create a conflict; do not average them.
- If a participant changes an earlier statement, determine whether it is a correction, refinement, supersession, or separate concern and preserve traceable relationships.
- If the participant lacks authority, record the contribution as evidence and create a question or source lead for the authorized owner.

## Close the Activity

Set the activity to `results_confirmed` when all captured material results are confirmed or explicitly disputed. Record new sources, open questions, unavailable evidence, and scope not covered by the activity.

Update the activity row and return control to the orchestrator. The orchestrator or analysis worker decides how evidence is classified, routed, reflected in BRS coverage, and prioritized. Do not continue into source analysis or BRS authoring within this skill.

Report:

- activity objective and participant;
- confirmed Evidence Item IDs;
- corrections or disputes;
- newly identified sources and questions;
- uncovered parts of the objective;
- the exact Markdown rows and handoff-page updates required.
