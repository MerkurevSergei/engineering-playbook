---
name: develop-mini-brs
description: Develop a Mini Business Requirements Specification (Mini BRS). Use when the user requests a Mini BRS or uses the transposed abbreviation Mini BSR.
---

## Terms and Definitions

Use these terms consistently:

| Term | Definition |
|---|---|
| Mini BRS | A compact Business Requirements Specification developed through this skill's confirmed checkpoints. |
| User Request | The user's current instruction, answer, correction, confirmation, rejection, or supplied content. |
| Target BRS | The BRS selected for the current work. It is a role assigned to an existing BRS, not a duplicate artifact. Use `NEW` when no BRS exists. |
| Interaction Mode | The active `Creative`, `Standard`, or `Simple` behavior used while developing the Mini BRS. |
| Dialogue Element | One atomic request, answer, clarification, change, confirmation, or rejection together with the result of processing it. |
| Resume Point | The state saved after the latest processed Dialogue Element and used to continue from the next expected action. Update it after every processed Dialogue Element. |
| Working Draft | An unconfirmed proposal stored as pending work. It may be restored from the Resume Point but is not confirmed BRS content. |
| Request Intent | Whether the User Request continues saved work (`CONTINUE`) or requests a change (`CHANGE`). |
| Change Type | The kind of requested change used to choose the checkpoint responsible for it. |
| Next Action | The single action to perform after session initialization. |
| Destination | The checkpoint responsible for Next Action. |
| Routing Reason | A concise explanation of why Destination owns Next Action. |

## Interaction Modes

- `Creative`: maximize result quality and propose improvements, alternatives, and new opportunities.
- `Standard`: improve clarity, atomicity, and terminology without changing meaning.
- `Simple`: preserve the Source Item wording when placing it in the BRS; add only structure, classification, identifiers, and trace links.

Apply a mode change to the current Working Draft and subsequent work. Change confirmed BRS content only on an explicit request.

## Resume Point Template

```yaml
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

## CP1 — Initialize the Session

### Purpose

Prepare the context for the user's current request: determine the BRS, active interaction mode, relationship to previous work, and exactly one next action.

Do not analyze a source or change BRS content in CP1. Restore context, interpret the request, and route control to the checkpoint responsible for the work.

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
  resume_point: <updated Resume Point>
```
