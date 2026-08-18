# Create Mini BRS Skill

## Status

- Overall status: In progress
- Last confirmed runtime checkpoint: CP1 — routing behavior confirmed before state-model reopening
- Current review target: SC1 — Activation and Scope
- Next runtime checkpoint: CP2 — revised draft saved but not confirmed
- Updated: 2026-08-19

## Working Agreement

Develop Skill-Wide Contract blocks and runtime checkpoints separately. For each block or checkpoint:

1. Show the exact proposal.
2. Keep the exact proposal in this plan while its Status is `Draft` or `Reopened`.
3. Revise it until the user confirms it.
4. Implement only the confirmed version in `SKILL.md`.
5. Verify the implementation and dependent blocks and checkpoints for consistency.
6. Remove the implemented skill content from this plan and retain only its compact plan record.

Skill-Wide Contract blocks apply across the workflow but are not runtime steps and do not receive CP numbers. Do not implement a later block or runtime checkpoint silently. A user may explicitly return to an earlier block or checkpoint. When a confirmed change invalidates a dependency, mark the dependent block or checkpoint as reopened.

## Content Residency Rule

Keep one authoritative copy of skill content according to its lifecycle:

- `Draft`: keep the exact proposed skill content only in this plan; do not add it to `SKILL.md`.
- `Reopened`: keep the last confirmed version active in `SKILL.md`; copy the current baseline and proposed revision into this plan for review. This duplication is temporary.
- `Confirmed and implemented`: keep the exact skill content only in `SKILL.md`; remove `Exact Draft`, checkpoint algorithms, schemas, and other implemented skill text from this plan.

After implementation, retain only the compact plan record:

1. Status.
2. `Implemented at` location in `SKILL.md`.
3. Dependencies.
4. Acceptance Criteria.
5. Verification result.

When reopening implemented content, copy its current version from `SKILL.md` back into this plan as `Current Baseline`, add the proposed change, and mark the plan record `Reopened`. Do not remove or weaken the active version in `SKILL.md` until its replacement is confirmed and verified. Use Git history instead of duplicating old confirmed versions in this plan.

## Checkpoint Format

Give every runtime checkpoint four sections:

1. Purpose — explain its human-readable intent and boundary.
2. Input — list only information required to run it.
3. Algorithm — express every condition, persistence operation, and transition directly in pseudocode.
4. Result — show the state produced by the algorithm.

Prefer `5–9` peer elements in one cognitive block and use `7` as the default target. Count only elements at the same hierarchy level. Use nested control structures for subordinate actions. If splitting a block would harm meaning, completeness, traceability, or algorithm flow, allow more than `9` elements. Never add filler or merge distinct statements only to meet the preferred size.

## Product Goal

Create a compact standalone Codex skill named `$create-mini-brs` for developing a lightweight Mini Business Requirements Specification through confirmed Vision and Scope, a Capability Map, and capability-scoped Business Rule Sets and Business Rules.

The skill must remain separate from the repository's formal evidence-driven BRS workflow. It must create human-readable Markdown that is easy for an AI to process, with stable identifiers, explicit relationships, and no unnecessary registers or files.

## Confirmed Decisions

- Use the term **Mini BRS**, not BSR.
- Keep Vision, Scope, and Capability Map in one document.
- Keep every elaborated capability in a separate document.
- Keep `$create-mini-brs` self-contained; it never invokes another skill.
- Process interviews and fixed sources through the same top-to-bottom source cycle.
- Preserve quotations from laws and approved regulations verbatim.
- Keep exact Source Items separate from classified BRS Elements.
- Link each BRS Element to supporting Source Item IDs through `Based on`.
- Preview changes and persist only user-confirmed BRS content.
- Let the user change the interaction mode at any time.
- Place explicit terms and definitions before workflow instructions.

## Skill-Wide Contract

These blocks define the exact instructions that apply before and across all runtime checkpoints. Review and confirm them independently; do not execute them as sequential workflow steps.

### Contract Map

1. SC1 — Activation and Scope. **Reopened — current baseline copied for independent review.**
2. SC2 — Terms and Definitions. **Reopened — current baseline copied for independent review.**
3. SC3 — Interaction Modes. **Reopened — current baseline copied for independent review.**
4. SC4 — Persistent State Model. **Draft — reopened and not implemented.**
5. SC5 — Global Operating Rules. **Draft — rules moved out of SC1 for later review.**

## SC1 — Activation and Scope

Status: **Reopened — the current baseline remains active in `SKILL.md` and is copied here for independent review.**

### Responsibility

Define why the skill exists and when it should trigger. Do not place operating rules or workflow instructions here.

### Exact Draft

```yaml
---
name: create-mini-brs
description: Develop a Mini BRS. Use when the user requests a Mini BRS or Mini BSR.
---
```

### Acceptance Criteria

- The description states one purpose and one trigger condition.
- `Develop` covers creating, continuing, and revising without enumerating lifecycle actions.
- `Mini BSR` is included only as an activation alias.
- Quality attributes, artifact composition, operating rules, exclusions, and algorithms are absent from the description.
- The redundant `# Create Mini BRS` heading and introductory restatement are absent; the body starts with its first substantive instruction section.

## SC2 — Terms and Definitions

Status: **Reopened — the current baseline remains active in `SKILL.md` and is copied here for independent review.**

### Responsibility

Define the shared vocabulary used by the Skill-Wide Contract and every runtime checkpoint. Do not define checkpoint-specific algorithms here.

### Exact Draft

Use these terms consistently:

| Term | Definition |
|---|---|
| Mini BRS | A compact Business Requirements Specification developed through this skill's confirmed checkpoints. |
| User Request | The user's current instruction, answer, correction, confirmation, rejection, or supplied content. |
| Target BRS | The BRS selected for the current work. It is a role assigned to an existing BRS, not a duplicate artifact. Use `NEW` when no BRS exists. |
| Interaction Mode | The active `Creative`, `Standard`, or `Simple` behavior used while developing the Mini BRS. |
| Dialogue Element | One atomic request, answer, clarification, change, confirmation, or rejection together with the result of processing it. |
| Resume Point | The single persisted state saved after the latest processed Dialogue Element and used to continue from the next expected action. |
| Working Draft | An unconfirmed proposal stored as pending work. It may be restored from the Resume Point but is not confirmed BRS content. |
| Request Intent | Whether the User Request continues saved work (`CONTINUE`) or requests a change (`CHANGE`). It is a temporary CP1 variable and is not persisted. |
| Change Type | The kind of requested change used to choose the responsible checkpoint. It is a temporary CP1 variable and is not persisted. |
| Next Action | The single resumable action stored in `Resume Point.next.action`. |
| Destination | The checkpoint responsible for Next Action, stored in `Resume Point.next.destination`. |
| Routing Reason | A concise explanation of why Destination owns Next Action, stored in `Resume Point.next.routing_reason`. |
| Source Action | Whether CP2 creates a Source (`CREATE`) or continues the active Source (`CONTINUE`). |

### Acceptance Criteria

- Every persisted and temporary concept has one unambiguous definition.
- Definitions do not duplicate workflow algorithms.
- Field references match SC4 and the checkpoint Results.
- Temporary CP1 variables are not represented as persisted state.

## SC3 — Interaction Modes

Status: **Reopened — the current baseline remains active in `SKILL.md` and is copied here for independent review.**

### Responsibility

Define how the selected mode changes proposals without weakening source fidelity, confirmation, or traceability.

### Exact Draft

- `Creative`: maximize result quality and propose improvements, alternatives, and new opportunities.
- `Standard`: improve clarity, atomicity, and terminology without changing meaning.
- `Simple`: preserve the Source Item wording when placing it in the BRS; add only structure, classification, identifiers, and trace links.

Apply a mode change to the current Working Draft and subsequent work. Change confirmed BRS content only on an explicit request. Never change exact Source Item text because of Interaction Mode.

### Acceptance Criteria

- Each mode produces observably different proposal behavior.
- No mode changes exact Source Item text.
- A mode change affects unconfirmed and subsequent work by default.
- Confirmed BRS content changes only after an explicit user request.

## SC4 — Persistent State Model

Status: **Draft — proposed replacement for the implemented Resume Point Template; not confirmed or implemented.**

### Responsibility

Define the one persisted state used to resume work. CP1 creates and updates this structure; every destination checkpoint reads only the fields it needs. Do not create a separate `Session Context` or another persisted session-state object.

### Exact Draft

```yaml
resume_point:
  target_brs: NEW | <BRS identifier or path>
  active_mode: Creative | Standard | Simple
  active_source_id: SRC-NNN | null

  last_dialogue_element:
    type: request | answer | clarification | change | confirmation | rejection
    summary: <processed element>

  pending:
    type: none | question | working_draft
    value: <exact pending item or stable reference>

  next:
    action: <single resumable action>
    destination: CP1 | CP2 | CP3 | CP4 | CP5 | CP6 | CP7
    routing_reason: <why this checkpoint owns the action>
    source_action: CREATE | CONTINUE | null
```

### Acceptance Criteria

- `Resume Point` is the only persisted session state.
- `Session Context` does not exist as a second result or wrapper.
- `active_checkpoint` is absent because `next.destination` identifies the checkpoint to resume.
- `Request Intent` and `Change Type` remain temporary CP1 variables.
- `source_action` is non-null only when `next.destination = CP2`.
- Every checkpoint updates `last_dialogue_element`, `pending`, and `next` after processing a Dialogue Element.
- CP1 Result and every dependent checkpoint Input use this schema without copying its fields into another structure.

## SC5 — Global Operating Rules

Status: **Draft — rules removed from SC1 and collected here; not confirmed or implemented as one contract block.**

### Responsibility

Define cross-checkpoint operating rules that must be available after the skill triggers but do not belong to one runtime checkpoint.

### Exact Draft

- Work autonomously within this skill; do not invoke another skill.
- Use `Mini BRS` in all produced artifacts. Treat `Mini BSR` only as an activation alias.
- Process interviews and fixed Sources through the same top-to-bottom source cycle.
- Preserve exact Source Item text separately from interpreted or classified BRS Elements.
- Preserve quotations from laws and approved regulations verbatim.
- Link every BRS Element to its supporting Source Item IDs through `Based on`.
- Preview proposed BRS changes and persist them only after explicit user confirmation.

### Acceptance Criteria

- Every rule applies across multiple checkpoints and has no narrower owner.
- SC1 contains only purpose and trigger conditions.
- Source fidelity and traceability rules remain enforceable across CP2–CP7.
- Confirmation remains mandatory before generated or revised BRS content is persisted.
- No rule duplicates the detailed algorithm of a runtime checkpoint.

## Runtime Checkpoint Map

1. CP1 — Initialize the Session. **Reopened — routing confirmed; state Result must align with SC4.**
2. CP2 — Capture Atomic Source Items. **Draft — not confirmed.**
3. CP3 — Process Source Items Into the BRS. Pending.
4. CP4 — Form Vision and Scope. Pending.
5. CP5 — Form the Capability Map. Pending.
6. CP6 — Elaborate Capabilities and Business Rules. Pending.
7. CP7 — Verify and Finish the Mini BRS. Pending.

## CP1 — Initialize the Session

Status: **Reopened — routing remains active in `SKILL.md`; the current baseline is copied here because its state handling must be revised after SC4 confirmation.**

### Purpose

Prepare the context for the user's current request: determine the BRS, active interaction mode, relationship to previous work, and exactly one next action.

CP1 does not analyze a source or change BRS content. It only restores context, interprets the request, and routes control to the checkpoint responsible for the work.

### Input

1. `User Request`.
2. `BRS`, if one exists.
3. `Resume Point`, if previous work was saved.
4. `Active Mode`, if already set.

### Algorithm

```text
START CP1

1. READ User Request, BRS, Resume Point, and Active Mode.

2. SET Target BRS:
   IF one applicable BRS is provided or found
     THEN SET it as Target BRS;
   ELSE IF no BRS exists
     THEN SET Target BRS = NEW;
   ELSE
     ASK the user to select a BRS;
     SAVE the question in Resume Point;
     STOP CP1 until the answer arrives.

3. SET Active Mode:
   IF User Request explicitly changes the mode
     THEN SET the requested mode;
   ELSE IF Active Mode is already set
     THEN KEEP Active Mode;
   ELSE
     ASK the user to select Creative, Standard, or Simple;
     SAVE the question in Resume Point;
     STOP CP1 until the answer arrives.

   INFORM the user of Active Mode.

4. INTERPRET User Request:
   IF it answers a pending question,
      confirms or rejects a Working Draft,
      or asks to continue
     THEN SET Request Intent = CONTINUE;
   ELSE
     SET Request Intent = CHANGE.

5. IF Request Intent = CHANGE
   THEN CLASSIFY Change Type as one of:
     - REGISTER NEW SOURCE;
     - REVISE VISION OR SCOPE;
     - REVISE CAPABILITY MAP;
     - REVISE CAPABILITY OR RULE;
     - CHANGE MODE ONLY;
     - CHANGE TARGET BRS.

   IF Change Type is ambiguous
     THEN
       ASK one clarification question;
       SAVE the question in Resume Point;
       STOP CP1 until the answer arrives.

6. DETERMINE Next Action and Destination:
   IF Request Intent = CONTINUE
     THEN
       SET Next Action from Resume Point;
       SET Destination = the checkpoint that saved Next Action;
   ELSE IF Change Type = REGISTER NEW SOURCE
     THEN SET Next Action = CAPTURE SOURCE ITEMS
          AND Destination = CP2;
   ELSE IF Change Type = REVISE VISION OR SCOPE
     THEN SET Next Action = REVISE VISION OR SCOPE
          AND Destination = CP4;
   ELSE IF Change Type = REVISE CAPABILITY MAP
     THEN SET Next Action = REVISE CAPABILITY MAP
          AND Destination = CP5;
   ELSE IF Change Type = REVISE CAPABILITY OR RULE
     THEN SET Next Action = REVISE CAPABILITY OR RULE
          AND Destination = CP6;
   ELSE IF Change Type = CHANGE MODE ONLY
     THEN SET Next Action from Resume Point
          AND Destination = the active checkpoint before the mode change;
   ELSE IF Change Type = CHANGE TARGET BRS
     THEN SET Next Action = SELECT TARGET BRS
          AND Destination = CP1 step 2.

7. UPDATE Resume Point after processing the current Dialogue Element.

   SHOW:
     "Continuing with <Next Action>.
      Going to <Destination> because <Routing Reason>."

   IF Destination = CP1
     THEN RETURN TO the specified CP1 step;
   ELSE
     GO TO Destination.

END CP1
```

### Result

```yaml
session_context:
  target_brs: NEW | <BRS identifier or path>
  active_mode: Creative | Standard | Simple
  request_intent: CONTINUE | CHANGE
  next_action: <single next action>
  destination: CP1 | CP2 | CP3 | CP4 | CP5 | CP6 | CP7
  routing_reason: <why this destination owns the next action>
  resume_point:
    target_brs: NEW | <BRS identifier or path>
    active_mode: Creative | Standard | Simple
    active_checkpoint: CP1 | CP2 | CP3 | CP4 | CP5 | CP6 | CP7
    last_dialogue_element:
      type: request | answer | clarification | change | confirmation | rejection
      summary: <processed element>
    pending:
      type: none | question | working_draft
      value: <exact pending item or stable reference>
    next_expected_action: <single resumable action>
    destination: CP1 | CP2 | CP3 | CP4 | CP5 | CP6 | CP7
    routing_reason: <why this destination is next>
```

## CP2 — Capture Atomic Source Items

Status: **Draft — saved but not confirmed or implemented.**

Dependency before confirmation:

- CP1 must provide `source_action: CREATE | CONTINUE` and keep `active_source_id` in the single persisted Resume Point.
- CP1 owns source selection. CP2 operates on exactly one source and never scans all Source Records.

### Purpose

Transform the next unprocessed fragment of one selected Source into a confirmed block of atomic Source Items with unambiguous IDs and exact source text.

CP2 does not select a Source, read unrelated Source Records, interpret statements, classify them, change the BRS, or advance the Source Checkpoint. Its result is confirmed input for CP3.

### Input

1. `Session Context` from CP1 with Target BRS, Active Mode, and `source_action: CREATE | CONTINUE`.
2. `Resume Point` with `active_source_id` when `source_action = CONTINUE`.
3. `New Source Input` when `source_action = CREATE`:
   - `inline_source_text`: exact text supplied by the user; or
   - `source_locator`: a stable path, attachment, URL, or artifact reference;
   - Source identity: type, name, and optional version and authority.
4. `Active Source Record` loaded by `active_source_id` when `source_action = CONTINUE`.
5. Current `User Request` only when it contains new business content for the active interview or an answer to a saved question.

### Algorithm

```text
START CP2

1. READ Session Context, Resume Point, and the current User Request.

   IF source_action = CONTINUE AND active_source_id is absent
     THEN
       ASK which Source to continue;
       SAVE the question in Resume Point;
       STOP CP2.

   IF source_action = CREATE AND New Source Input is absent
     THEN
       ASK the user to provide a Source;
       SAVE the question in Resume Point;
       STOP CP2.

2. SET Active Source:
   IF source_action = CONTINUE
     THEN
       LOAD only `sources/<active_source_id>.md`;

       IF that Source Record is unavailable
         THEN
           IDENTIFY the missing Source Record;
           ASK the user to restore or provide the Source again;
           SAVE the question in Resume Point;
           STOP CP2.

   ELSE IF source_action = CREATE
     THEN
       FIND the next unused Source ID from filenames in `sources/`
       without reading their contents;
       PREPARE a new Source Record from New Source Input;
       DO NOT SAVE it before confirmation.

3. CHECK unfinished processing:
   IF Active Source contains Source Items with Status = CAPTURED
     THEN
       UPDATE Resume Point:
         active_source_id = Active Source ID;
         Next Action = PROCESS CAPTURED SOURCE ITEMS;
         Destination = CP3;
       GO TO CP3 without capturing another fragment.

4. SET Current Source Fragment as the next contiguous unprocessed part of Active Source sufficient for one reviewable Source Item block.

   IF the current User Request contains business content belonging to the active interview
     THEN USE that exact business content;
   ELSE IF Active Source contains `inline_source_text`
     THEN READ after the position of the last fully processed Source Item;
   ELSE IF Active Source contains `source_locator`
     THEN OPEN that Source and READ after the position of the last fully processed Source Item;
   ELSE
     ASK the user to provide the unavailable Source content;
     SAVE the question in Resume Point;
     STOP CP2.

   EXCLUDE control instructions unless they contain BRS business information.

5. SPLIT Current Source Fragment into atomic Source Items:
   - keep one independently confirmable assertion in each Source Item;
   - preserve exact Source text without interpretation or semantic rewriting;
   - separate conditions, exceptions, obligations, prohibitions, permissions, and definitions;
   - preserve quotations from laws and approved regulations verbatim;
   - record Source position when it can be determined;
   - prefer 5–9 Source Items when the content permits;
   - use fewer or more when required to preserve atomicity or meaning.

   Interaction Mode never changes Source Item text.

6. ASSIGN Source Item IDs:
   IF Active Source is new
     THEN START with `<Source ID>-SI-001`;
   ELSE
     FIND the next unused Source Item ID by reading only Active Source Record.

   PREPARE each Source Item with:
   - Source Item ID;
   - exact Source text;
   - Source position or null;
   - Status = PENDING CONFIRMATION.

7. SHOW Active Source identity and the prepared Source Item block.

   For a new Source, also SHOW its prepared metadata.

   ASK the user to confirm Source identity, item boundaries, exact text, order, and Source positions.

   IF the user requests a change
     THEN
       REVISE only the unconfirmed Working Draft;
       RETURN TO step 5.

   IF the user confirms the result
     THEN
       SAVE the new Source Record or UPDATE Active Source Record;
       SAVE confirmed Source Items with Status = CAPTURED;
       KEEP Source Checkpoint unchanged;
       UPDATE Resume Point:
         active_source_id = Active Source ID;
         active_checkpoint = CP3;
         pending.type = none;
         pending.value = null;
         Next Action = PROCESS CAPTURED SOURCE ITEMS;
         Destination = CP3;
         Routing Reason = Captured Source Items require BRS processing;
       SHOW:
         "Source Items saved.
          Source Checkpoint remains unchanged.
          Going to CP3.";
       GO TO CP3.

END CP2
```

### Result

```yaml
source_record:
  source_id: SRC-NNN
  identity:
    type: interview | document | law | approved_regulation | policy | existing_brs | other
    name: <source name>
    version: <version or null>
    authority: <issuer or responsible role or null>
  source_input:
    inline_source_text: <exact supplied text or null>
    source_locator: <stable path, attachment, URL, or artifact reference or null>
  status: IN_PROGRESS
  source_checkpoint:
    last_fully_processed_source_item_id: <Source Item ID or null>
  source_items:
    - source_item_id: SRC-NNN-SI-NNN
      source_text: <exact source text>
      source_position: <position in the Source or null>
      status: CAPTURED

resume_point:
  target_brs: <BRS identifier or path>
  active_mode: Creative | Standard | Simple
  active_checkpoint: CP3
  active_source_id: SRC-NNN
  last_dialogue_element:
    type: confirmation
    summary: <confirmed Source Item block>
  pending:
    type: none
    value: null
  next_expected_action: PROCESS CAPTURED SOURCE ITEMS
  destination: CP3
  routing_reason: Captured Source Items require BRS processing
```

## Pending Runtime Checkpoints

Define CP3 through CP7 only through the same proposal, confirmation, save, and verification cycle. Do not move CP2 into `SKILL.md` until its unresolved source-recognition and persistence rules are confirmed.

## Unnumbered Technical Implementation

Keep technical construction outside the runtime checkpoint sequence:

- Maintain `skills/create-mini-brs/SKILL.md` as the compact core workflow.
- Maintain matching UI metadata in `skills/create-mini-brs/agents/openai.yaml`.
- Add `skills/create-mini-brs/references/mini-brs-format.md` only when its format is approved; do not keep an empty placeholder.
- Keep the skill self-contained and free of unnecessary scripts, assets, dependencies, or local README files.
- Keep the catalog entry in Draft status until final validation passes.
- Run the official skill validator and forward tests after CP7 is implemented.

## Verification Record

| Check | Result | Notes |
|---|---|---|
| CP1 plan structure | Passed | Contains only Purpose, Input, Algorithm, and Result |
| CP1 routing | Passed | Every route is expressed in algorithm step 6 |
| Resume Point template | Passed | Included in CP1 Result |
| Full skill validation | Pending | Run after CP7 |
| Forward tests | Pending | Run after CP7 |
