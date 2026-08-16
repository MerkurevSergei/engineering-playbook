# Create Mini BRS Skill

## Status

- Overall status: In progress
- Last completed runtime checkpoint: CP1 — Initialize the Session
- Current runtime checkpoint: CP2 — Capture Atomic Source Items; source recognition under clarification
- Updated: 2026-08-16

## Working Agreement

Develop runtime checkpoints from top to bottom. For each checkpoint:

1. Show the exact proposal.
2. Revise it until the user confirms it.
3. Save and verify only the confirmed checkpoint.
4. Mark it complete and continue to the next checkpoint.

Do not implement a later runtime checkpoint silently. A user may explicitly return to an earlier checkpoint.

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

## Runtime Checkpoint Map

1. CP1 — Initialize the Session. **Complete.**
2. CP2 — Capture Atomic Source Items. **Draft — not confirmed.**
3. CP3 — Process Source Items Into the BRS. Pending.
4. CP4 — Form Vision and Scope. Pending.
5. CP5 — Form the Capability Map. Pending.
6. CP6 — Elaborate Capabilities and Business Rules. Pending.
7. CP7 — Verify and Finish the Mini BRS. Pending.

## CP1 — Initialize the Session

Status: **Confirmed, saved, and implemented.**

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

Unresolved before confirmation:

- Define deterministic evidence that an input is a new Source rather than a continuation of a registered Source.
- Define where the Source record and Source Checkpoint are persisted and how CP2 finds them.

### Purpose

Transform the next unprocessed source fragment into a confirmed block of atomic Source Items with unambiguous IDs and exact source text.

CP2 does not interpret statements, classify them, or change the BRS. Its result is confirmed input for CP3.

### Input

1. `Session Context` from CP1.
2. A new Source or a saved Source Checkpoint.
3. Source content.
4. Existing Source IDs and Source Item IDs.

### Algorithm

```text
START CP2

1. READ Session Context, Source, Resume Point, and existing Source records.

2. SET Active Source:
   IF Resume Point identifies an incomplete Source
     THEN
       LOAD its Source ID and Source Checkpoint;
       VERIFY the Source identity and version;
   ELSE IF a new Source is received
     THEN
       ASSIGN the next unused Source ID;
       SAVE its type, name, version, and Authority;
   ELSE
       ASK the user to provide or select a Source;
       SAVE the question in Resume Point;
       STOP CP2 until the answer arrives.

   IF a registered Source changed materially
     THEN REGISTER the changed version with a new Source ID.

3. SELECT the next unprocessed fragment:
   - move from top to bottom;
   - continue after the last processed position;
   - do not repeat confirmed Source Items;
   - exclude control instructions unless they contain BRS business information.

4. SPLIT the fragment into atomic Source Items:
   - keep one independently confirmable assertion in each Source Item;
   - separate conditions, exceptions, obligations, prohibitions, permissions, and definitions;
   - do not add interpretation or rewrite meaning;
   - preserve exact Source text;
   - preserve quotations from laws and approved regulations verbatim;
   - use 5–9 Source Items when the content permits;
   - use fewer or more when required to preserve atomicity or meaning.

5. ASSIGN each Source Item the next unused ID in the form `SRC-NNN-SI-NNN`.

   PREPARE:
   - Source Item ID;
   - Source text;
   - optional Source position;
   - Status = PENDING CONFIRMATION.

6. SHOW the prepared Source Item block.

   ASK the user to confirm boundaries, exact Source text, order, and Source position.

   IF the user requests a change
     THEN
       REVISE only the unconfirmed block;
       RETURN TO step 4.

7. IF the user confirms the block
   THEN
     SAVE the Source record;
     SAVE the Source Items with Status = CAPTURED;
     KEEP Source Checkpoint unchanged;
     UPDATE Resume Point:
       Next Action = PROCESS CAPTURED SOURCE ITEMS;
       Destination = CP3;
     SHOW:
       "Source Items saved.
        Source Checkpoint will advance after CP3 processing.
        Going to CP3.";
     GO TO CP3.

END CP2
```

### Result

```yaml
source:
  source_id: SRC-NNN
  type: interview | document | law | approved_regulation | policy | existing_brs | other
  name: <source name>
  version: <version or date if available>
  authority: <issuer or responsible role if applicable>
  status: IN_PROGRESS
  source_checkpoint:
    source_id: SRC-NNN
    last_fully_processed_source_item_id: <Source Item ID or null>

captured_source_items:
  - source_item_id: SRC-NNN-SI-NNN
    source_text: <exact source text>
    source_position: <optional position in the source>
    status: CAPTURED

resume_point:
  active_checkpoint: CP3
  pending:
    type: none
    value: null
  next_expected_action: PROCESS CAPTURED SOURCE ITEMS
  destination: CP3
  routing_reason: Captured Source Items require classification and BRS placement
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
