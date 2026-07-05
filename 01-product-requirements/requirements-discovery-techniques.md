# Requirements Discovery Techniques

Requirements discovery is the work of turning scattered signals into testable product and engineering decisions.

## Technique Map

| Technique | Use When | Output |
|---|---|---|
| Stakeholder interview | The problem is unclear or depends on expert knowledge | Goals, constraints, conflicts, vocabulary |
| User interview | You need to understand real behavior and pain | Jobs, scenarios, objections, edge cases |
| Observation | The stated process differs from the real process | Actual workflow, hidden manual steps, workarounds |
| Workshop | Multiple groups need shared alignment | Prioritized scope, decisions, open questions |
| Questionnaire | You need broad but shallow input | Patterns, segmentation, quantitative signals |
| Document analysis | Existing policies, contracts, or specs constrain the work | Business rules, compliance constraints, terms |
| Data analysis | Current system behavior is measurable | Volumes, frequencies, anomalies, conversion points |
| Process modeling | The workflow crosses roles or systems | States, handoffs, responsibility gaps |
| Prototype review | Stakeholders struggle to react to abstract requirements | UX feedback, missing states, misunderstood flows |
| Impact analysis | A change touches existing users, data, or integrations | Risks, migration needs, rollout constraints |

## Interview Prompts

- What decision are we trying to make?
- Who is affected if the process works well?
- Who is affected if it fails?
- What does success look like in observable terms?
- What rules are mandatory, and which are preferences?
- What exceptions happen often enough to design for?
- What is currently manual, duplicated, or delayed?
- What should never happen?
- What can be simplified, postponed, or removed?

## Discovery Outputs

A discovery pass should leave behind:

- Problem statement
- Stakeholder map
- System boundary
- Core scenarios and edge cases
- Business rules
- Functional requirements
- Quality attributes
- Acceptance criteria
- Risks and assumptions
- Open questions with owners

## Common Failure Modes

- Recording stakeholder wishes without identifying the underlying problem.
- Treating implementation ideas as requirements.
- Missing negative scenarios and operational failures.
- Ignoring data ownership and migration constraints.
- Accepting vague words such as fast, simple, reliable, flexible, or secure without measurable interpretation.
- Leaving open questions without owners or decision dates.
