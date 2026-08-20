---
name: develop-mini-brs
description: Develop a Mini Business Requirements Specification (Mini BRS). Use when the user requests a Mini BRS or uses the transposed abbreviation Mini BSR.
---

## Terms and Definitions

Use these terms consistently:

### Business Concepts

| Term | Definition |
|---|---|
| Mini BRS | A compact set of linked Markdown documents that together form a Business Requirements Specification. |
| Vision | The required section of the Mini BRS overview document that states the desired future business state or outcome. |
| Scope | The required section of the Mini BRS overview document that defines the included and excluded business outcomes and Capabilities. |
| Capability Map | The required structured section of the Mini BRS overview document that records the Capabilities within Scope and organizes their elaboration and traceability. |
| Capability | An identified organizational ability required to produce or ensure a specific business outcome within Scope. The Capability Map represents it as one entry. |
| Business Rule Set | A named grouping section in one Capability document that contains related Business Rules. |
| Business Rule | An identified atomic declarative statement within one Business Rule Set that governs or constrains business behavior or a decision. |

### Interaction

| Term | Definition |
|---|---|
| User Request | The current user input that starts, continues, or changes work on the Mini BRS. |
| Target BRS | The Mini BRS selected for the current work and for receiving Confirmed BRS Elements. |
| Interaction Mode | The active `Creative`, `Standard`, or `Simple` mode used while forming and revising Draft BRS Elements. |

### Source and BRS Content Lifecycle

| Term | Definition |
|---|---|
| Source | One identified origin of business information, such as an interview or document, processed from top to bottom. |
| Active Source | The Source selected as the current context for source processing. |
| Source Item | One atomic unit of exact Source content preserved separately from interpreted BRS content. |
| BRS Element | One identified unit of interpreted business content intended for or stored in a specific Mini BRS section. |
| Draft BRS Element | A BRS Element derived from one or more Source Items of the Active Source and revised while it awaits explicit user confirmation. |
| Confirmed BRS Element | A Draft BRS Element that the user explicitly confirms and the responsible Workflow Stage persists in the Target BRS. |

### Execution, Resumption, and Routing

| Term | Definition |
|---|---|
| Workflow Stage | An instruction section identified as `WS1`–`WS7` whose Algorithm performs one coherent kind of processing and produces its Result. |
| Resume Point | The single persisted execution-state record that identifies the pending item and the next operation together with its responsible Workflow Stage and Routing Reason. |
| Next Action | The Resume Point field that identifies the single operation from which work must continue. |
| Destination | The Resume Point field that identifies the Workflow Stage whose Algorithm executes Next Action. |
| Routing Reason | The Resume Point field that explains why Destination is responsible for Next Action. |

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
  active_checkpoint: WS1 | WS2 | WS3 | WS4 | WS5 | WS6 | WS7
  last_dialogue_element:
    type: request | answer | clarification | change | confirmation | rejection
    summary: <processed element>
  pending:
    type: none | question | working_draft
    value: <exact pending item or stable reference>
  next_expected_action: <single resumable action>
  destination: WS1 | WS2 | WS3 | WS4 | WS5 | WS6 | WS7
  routing_reason: <why this destination is next>
```

## WS1 — Initialize the Session

### Purpose

Prepare the context for the user's current request: determine the BRS, active interaction mode, relationship to previous work, and exactly one next action.

Do not analyze a source or change BRS content in WS1. Restore context, interpret the request, and route control to the Workflow Stage responsible for the work.

### Local Definitions

| Term | Definition |
|---|---|
| Request Intent | Whether the current User Request continues the action saved in Resume Point (`CONTINUE`) or introduces work that must be routed independently (`CHANGE`). This variable exists only while WS1 processes the request. |
| Change Type | The routing category assigned to a `CHANGE` request. This variable exists only while WS1 selects the responsible Workflow Stage. |

### Input

1. `User Request`.
2. `BRS`, if one exists.
3. `Resume Point`, if previous work was saved.
4. `Active Mode`, if already set.

### Algorithm

```text
START WS1

1. READ User Request, BRS, Resume Point, and Active Mode.

2. SET Target BRS:
   IF one applicable BRS is provided or found
     THEN SET it as Target BRS;
   ELSE IF no BRS exists
     THEN SET Target BRS = NEW;
   ELSE
     ASK the user to select a BRS;
     SAVE the question in Resume Point;
     STOP WS1 until the answer arrives.

3. SET Active Mode:
   IF User Request explicitly changes the mode
     THEN SET the requested mode;
   ELSE IF Active Mode is already set
     THEN KEEP Active Mode;
   ELSE
     ASK the user to select Creative, Standard, or Simple;
     SAVE the question in Resume Point;
     STOP WS1 until the answer arrives.

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
       STOP WS1 until the answer arrives.

6. DETERMINE Next Action and Destination:
   IF Request Intent = CONTINUE
     THEN
       SET Next Action from Resume Point;
       SET Destination = the Workflow Stage that saved Next Action;
   ELSE IF Change Type = REGISTER NEW SOURCE
     THEN SET Next Action = CAPTURE SOURCE ITEMS
          AND Destination = WS2;
   ELSE IF Change Type = REVISE VISION OR SCOPE
     THEN SET Next Action = REVISE VISION OR SCOPE
          AND Destination = WS4;
   ELSE IF Change Type = REVISE CAPABILITY MAP
     THEN SET Next Action = REVISE CAPABILITY MAP
          AND Destination = WS5;
   ELSE IF Change Type = REVISE CAPABILITY OR RULE
     THEN SET Next Action = REVISE CAPABILITY OR RULE
          AND Destination = WS6;
   ELSE IF Change Type = CHANGE MODE ONLY
     THEN SET Next Action from Resume Point
          AND Destination = the Workflow Stage identified by Resume Point.active_checkpoint before the mode change;
   ELSE IF Change Type = CHANGE TARGET BRS
     THEN SET Next Action = SELECT TARGET BRS
          AND Destination = WS1 step 2.

7. UPDATE Resume Point after processing the current User Request.

   SHOW:
     "Continuing with <Next Action>.
      Going to <Destination> because <Routing Reason>."

   IF Destination = WS1
     THEN RETURN TO the specified WS1 step;
   ELSE
     GO TO Destination.

END WS1
```

### Result

```yaml
session_context:
  target_brs: NEW | <BRS identifier or path>
  active_mode: Creative | Standard | Simple
  request_intent: CONTINUE | CHANGE
  next_action: <single next action>
  destination: WS1 | WS2 | WS3 | WS4 | WS5 | WS6 | WS7
  routing_reason: <why this destination owns the next action>
  resume_point: <updated Resume Point>
```
