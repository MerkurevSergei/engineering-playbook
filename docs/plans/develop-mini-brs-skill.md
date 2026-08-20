# Develop Mini BRS Skill

## Status

- Overall status: In progress
- Last confirmed workflow stage: WS1 — routing behavior confirmed before state-model reopening
- Current review target: SC3 — Interaction Modes
- Next workflow stage: WS2 — revised draft saved but not confirmed
- Updated: 2026-08-21

## Working Agreement

Develop Skill-Wide Contract blocks and workflow stages separately. For each block or stage definition:

1. Show the exact proposal.
2. Keep the exact proposal in this plan while its Status is `Draft` or `Reopened`.
3. Revise it until the user confirms it.
4. After the user confirms a workflow-stage definition, review its local terms. Move a term to SC2 only when the Skill-Wide Contract or multiple stages use it; otherwise keep it local. Reopen SC2 when this review changes confirmed definitions.
5. Implement only the confirmed version in `SKILL.md`.
6. Verify the implementation and dependent blocks and stages for consistency.
7. Remove the implemented skill content from this plan and retain only its compact plan record.

Each workflow stage may define terms used only within that stage. Keep those definitions local until the post-confirmation review establishes that they are shared vocabulary.

Skill-Wide Contract blocks apply across the workflow but are not runtime stages and do not receive WS numbers. Do not implement a later block or workflow stage silently. A user may explicitly return to an earlier block or stage. When a confirmed change invalidates a dependency, mark the dependent block or stage as reopened.

## Definition Writing Rule

Apply this rule to shared terms, local definitions, schema fields, artifacts, states, workflow stages, and every other named element:

1. Write the exact wording proposed for the skill rather than a placeholder, approximation, or explanation of what might be written.
2. Begin with a precise positive statement of what the element is.
3. State the element's function and, when needed for unambiguous use, its structure, owner, lifecycle, or storage location.
4. Use the shortest formulation that preserves the element's full meaning, function, and necessary boundaries.
5. Before using `not`, `does not`, `is absent`, or an equivalent negative construction, rewrite the definition positively and check whether the positive wording establishes the boundary by itself.
6. Add a negative or exclusion statement only when a likely competing interpretation cannot be ruled out from the positive definition.
7. Never use a negative statement as a substitute for the positive definition.

## Definition and Structure Ownership Rule

Separate semantic identity from structural specification:

1. Use a definition to state what an element is, what role it serves, and the stable characteristics needed to distinguish it.
2. Define the element's complete composition, including required documents, sections, fields, and relationships, in exactly one owning schema or template.
3. Mention structure in a definition only at the highest stable level needed for clarity, such as `multi-document`.
4. Refer to the owning schema or template whenever another block needs structural details.
5. When the structure changes, update its owner and verify every reference to it.

## Specification Ownership Map

This plan-level map identifies the single owner of each structural specification. It is development navigation and is not runtime skill content.

| Structure | Owner |
|---|---|
| Shared vocabulary | SC2 |
| Interaction Mode variants and behavior | SC3 |
| Resume Point fields | SC4 |
| Workflow Stage sections | Workflow Stage Format |
| Mini BRS documents and sections | `skills/develop-mini-brs/references/mini-brs-format.md` after format approval |

## Content Residency Rule

Keep one authoritative copy of skill content according to its lifecycle:

- `Draft`: keep the exact proposed skill content only in this plan; do not add it to `SKILL.md`.
- `Reopened`: keep the last confirmed version active in `SKILL.md`; copy the current baseline and proposed revision into this plan for review. This duplication is temporary.
- `Confirmed and implemented`: keep the exact skill content only in `SKILL.md`; remove `Exact Draft`, stage algorithms, schemas, and other implemented skill text from this plan.

After implementation, retain only the compact plan record:

1. Status.
2. `Implemented at` location in `SKILL.md`.
3. Dependencies.
4. Acceptance Criteria.
5. Verification result.

When reopening implemented content, copy its current version from `SKILL.md` back into this plan as `Current Baseline`, add the proposed change, and mark the plan record `Reopened`. Do not remove or weaken the active version in `SKILL.md` until its replacement is confirmed and verified. Use Git history instead of duplicating old confirmed versions in this plan.

## Workflow Stage Format

Give every workflow stage four required sections:

1. Purpose — explain its human-readable intent and boundary.
2. Input — list only information required to run it.
3. Algorithm — express every condition, persistence operation, and transition directly in pseudocode.
4. Result — show the state produced by the algorithm.

Add an optional `Local Definitions` section between Purpose and Input when a stage uses terms that are not yet shared vocabulary. Review those terms after stage confirmation according to the Working Agreement.

Prefer `5–9` peer elements in one cognitive block and use `7` as the default target. Count only elements at the same hierarchy level. Use nested control structures for subordinate actions. If splitting a block would harm meaning, completeness, traceability, or algorithm flow, allow more than `9` elements. Never add filler or merge distinct statements only to meet the preferred size.

## Product Goal

Create a compact standalone Codex skill named `$develop-mini-brs` for developing a lightweight Mini Business Requirements Specification through confirmed Vision and Scope, a Capability Map, and capability-scoped Business Rule Sets and Business Rules.

The skill must remain separate from the repository's formal evidence-driven BRS workflow. It must create human-readable Markdown that is easy for an AI to process, with stable identifiers, explicit relationships, and no unnecessary registers or files.

## Confirmed Decisions

- Use the term **Mini BRS**, not BSR.
- Keep Vision, Scope, and Capability Map in one document.
- Keep every elaborated capability in a separate document.
- Keep `$develop-mini-brs` self-contained; it never invokes another skill.
- Process interviews and fixed sources through the same top-to-bottom source cycle.
- Preserve quotations from laws and approved regulations verbatim.
- Keep exact Source Items separate from classified BRS Elements.
- Link each BRS Element to supporting Source Item IDs through `Based on`.
- Preview Draft BRS Elements and persist them in the Target BRS only as Confirmed BRS Elements.
- Let the user change the interaction mode at any time.
- Place explicit terms and definitions before workflow instructions.

## Skill-Wide Contract

These blocks define the exact instructions that apply before and across all workflow stages. Review and confirm them independently; do not execute them as sequential workflow steps.

### Contract Map

1. SC1 — Activation and Scope. **Confirmed and implemented.**
2. SC2 — Terms and Definitions. **Confirmed and implemented.**
3. SC3 — Interaction Modes. **Reopened — revised after SC2 confirmation and not confirmed.**
4. SC4 — Persistent State Model. **Draft — requires revision after SC2 and is not implemented.**
5. SC5 — Global Operating Rules. **Draft — rules moved out of SC1 for later review.**

## SC1 — Activation and Scope

Status: **Confirmed and implemented.**

Implemented at: `skills/develop-mini-brs/SKILL.md` frontmatter.

Dependencies: None.

### Acceptance Criteria

- The description states one purpose and one trigger condition.
- The skill name and description use the same action: `develop`.
- `Mini BRS` is expanded as `Mini Business Requirements Specification` on first use.
- `Develop` covers creating, continuing, and revising without enumerating lifecycle actions.
- `Mini BSR` is included only as an activation alias.
- Quality attributes, artifact composition, operating rules, exclusions, and algorithms are absent from the description.
- The redundant title heading and introductory restatement are absent; the body starts with its first substantive instruction section.

### Verification Result

Passed — the folder, frontmatter, catalog entry, and UI metadata use `develop-mini-brs`; the description expands `Mini BRS`; the body starts with Terms and Definitions; and no stale prior-name references remain.

## SC2 — Terms and Definitions

Status: **Confirmed and implemented.**

Implemented at: `skills/develop-mini-brs/SKILL.md` under `Terms and Definitions`.

Dependencies:

- SC3 is reopened for replacement of `Working Draft` and `Confirmed Content` with the confirmed BRS Element lifecycle.
- SC4 remains draft because its `pending` schema must represent questions, unconfirmed Source Items, and Draft BRS Elements without restoring a second generic draft concept.
- WS1 remains reopened for alignment with the confirmed Workflow Stage and Resume Point terminology after SC4 confirmation.
- WS2 remains draft; its local definitions must retain only stage-local Source Record and Source Cursor semantics after shared Source terms moved to SC2.

### Acceptance Criteria

- SC2 contains only vocabulary used by the Skill-Wide Contract or multiple workflow stages.
- Every shared concept has one unambiguous definition.
- Each Business Concept definition identifies whether the term denotes the document set, a section, an organizational ability represented by a map entry, a grouping section, or an atomic statement.
- Definitions contain only element meaning and stable distinguishing characteristics.
- Every complete composition has exactly one owning schema or template.
- Interaction Mode is defined as a mode rather than as the rules that specify its behavior.
- Source, Active Source, Source Item, Draft BRS Element, and Confirmed BRS Element distinguish the current source context, exact source content, interpreted draft content, and content persisted in the Target BRS.
- Source Items remain exact source content when a derived Draft BRS Element becomes a Confirmed BRS Element.
- Workflow Stage, Next Action, and Destination unambiguously identify what to execute and where to resume it.
- Resume Point, Next Action, Destination, and Routing Reason are defined together as one execution-state and routing model.
- Stage-local concepts remain in their owning stage until the post-confirmation terminology review.
- Definitions state element semantics while stage Algorithms retain procedural behavior.
- Every definition follows the Definition Writing Rule and Definition and Structure Ownership Rule.
- Definitions remain consistent with their owning schemas, templates, and workflow-stage Results.
- Structural ownership remains plan-level development navigation rather than runtime vocabulary in SC2.

### Verification Result

Passed — the confirmed definitions are implemented in `SKILL.md`; Business Concepts identify their content kinds; Source Items remain separate from Draft and Confirmed BRS Elements; Workflow Stage identifiers use `WS1`–`WS7`; Request Intent and Change Type are local to WS1; and the dependency audit recorded every block or stage that still requires separate review.

## SC3 — Interaction Modes

Status: **Reopened — revised after SC2 confirmation but not confirmed; the current baseline remains active in `SKILL.md`.**

### Responsibility

Define how the selected mode changes proposals without weakening source fidelity, confirmation, or traceability.

### Exact Draft

- `Creative`: maximize result quality and propose improvements, alternatives, and new opportunities.
- `Standard`: improve clarity, atomicity, and terminology without changing meaning.
- `Simple`: preserve the Source Item wording when placing it in the BRS; add only structure, classification, identifiers, and trace links.

Apply a mode change to current Draft BRS Elements and subsequent work. Change Confirmed BRS Elements in the Target BRS only on an explicit request. Never change exact Source Item text because of Interaction Mode.

### Acceptance Criteria

- Each mode produces observably different proposal behavior.
- No mode changes exact Source Item text.
- A mode change affects current Draft BRS Elements and subsequent work by default.
- Confirmed BRS Elements in the Target BRS change only after an explicit user request.

## SC4 — Persistent State Model

Status: **Draft — must revise `pending` after SC2 confirmation; the proposed replacement for the implemented Resume Point Template is not confirmed or implemented.**

### Responsibility

Define the one persisted state used to resume work. WS1 creates and updates this structure; every destination stage reads only the fields it needs. Do not create a separate `Session Context` or another persisted session-state object.

### Exact Draft

```yaml
resume_point:
  target_brs: NEW | <BRS identifier or path>
  active_mode: Creative | Standard | Simple
  active_source_id: SRC-NNN | null

  pending:
    type: none | question | working_draft
    value: <exact pending item or stable reference>

  next:
    action: <single resumable action>
    destination: WS1 | WS2 | WS3 | WS4 | WS5 | WS6 | WS7
    routing_reason: <why this stage owns the action>
```

### Acceptance Criteria

- `Resume Point` is the only persisted session state.
- `Session Context` does not exist as a second result or wrapper.
- A separate active-stage field is absent because `next.destination` identifies the stage to resume.
- Dialogue history is not persisted because it is not required to resume work.
- `Request Intent` and `Change Type` remain local temporary variables in WS1 and are not persisted.
- `next.action` distinguishes registering a new Source from continuing the active Source without a separate create-or-continue flag.
- Every stage updates `pending` and `next` after processing the current User Request.
- WS1 Result and every dependent stage Input use this schema without copying its fields into another structure.

## SC5 — Global Operating Rules

Status: **Draft — rules removed from SC1 and collected here; not confirmed or implemented as one contract block.**

### Responsibility

Define cross-stage operating rules that must be available after the skill triggers but do not belong to one workflow stage.

### Exact Draft

- Work autonomously within this skill; do not invoke another skill.
- Use `Mini BRS` in all produced artifacts. Treat `Mini BSR` only as an activation alias.
- Process interviews and fixed Sources through the same top-to-bottom source cycle.
- Preserve exact Source Item text separately from interpreted or classified BRS Elements.
- Preserve quotations from laws and approved regulations verbatim.
- Link every BRS Element to its supporting Source Item IDs through `Based on`.
- Preview proposed BRS changes and persist them only after explicit user confirmation.

### Acceptance Criteria

- Every rule applies across multiple stages and has no narrower owner.
- SC1 contains only purpose and trigger conditions.
- Source fidelity and traceability rules remain enforceable across WS2–WS7.
- Only Confirmed BRS Elements may be persisted in the Target BRS.
- No rule duplicates the detailed algorithm of a workflow stage.

## Workflow Stage Map

1. WS1 — Initialize the Session. **Reopened — routing confirmed; state Result must align with SC4.**
2. WS2 — Capture Atomic Source Items. **Draft — not confirmed.**
3. WS3 — Process Source Items Into the BRS. Pending.
4. WS4 — Form Vision and Scope. Pending.
5. WS5 — Form the Capability Map. Pending.
6. WS6 — Elaborate Capabilities and Business Rules. Pending.
7. WS7 — Verify and Finish the Mini BRS. Pending.

## WS1 — Initialize the Session

Status: **Reopened — routing remains active in `SKILL.md`; the current baseline is copied here because its terminology and state handling must be revised after SC2 and SC4 confirmation.**

### Purpose

Prepare the context for the user's current request: determine the BRS, active interaction mode, relationship to previous work, and exactly one next action.

WS1 does not analyze a source or change BRS content. It only restores context, interprets the request, and routes control to the stage responsible for the work.

### Local Definitions

| Term | Definition |
|---|---|
| Request Intent | Whether the current User Request continues the action saved in Resume Point (`CONTINUE`) or introduces work that must be routed independently (`CHANGE`). This variable exists only while WS1 processes the request. |
| Change Type | The routing category assigned to a `CHANGE` request. This variable exists only while WS1 selects the responsible stage. |

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
       SET Next Action = Resume Point.next.action;
       SET Destination = Resume Point.next.destination;
   ELSE IF Change Type = REGISTER NEW SOURCE
     THEN SET Next Action = REGISTER NEW SOURCE
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
     THEN SET Next Action = Resume Point.next.action
          AND Destination = Resume Point.next.destination;
   ELSE IF Change Type = CHANGE TARGET BRS
     THEN SET Next Action = SELECT TARGET BRS
          AND Destination = WS1 step 2.

7. UPDATE Resume Point after processing the current User Request:
   - SET target_brs = Target BRS;
   - SET active_mode = Active Mode;
   - SET pending to the unresolved question or Working Draft, otherwise none;
   - SET next.action = Next Action;
   - SET next.destination = Destination;
   - SET next.routing_reason = Routing Reason.

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
resume_point:
  target_brs: NEW | <BRS identifier or path>
  active_mode: Creative | Standard | Simple
  active_source_id: SRC-NNN | null
  pending:
    type: none | question | working_draft
    value: <exact pending item or stable reference>
  next:
    action: <single resumable action>
    destination: WS1 | WS2 | WS3 | WS4 | WS5 | WS6 | WS7
    routing_reason: <why this stage owns the action>
```

## WS2 — Capture Atomic Source Items

Status: **Draft — saved but not confirmed or implemented.**

Dependency before confirmation:

- WS1 must route WS2 with `next.action = REGISTER NEW SOURCE` or `next.action = CAPTURE SOURCE ITEMS` and keep `active_source_id` when continuing an existing Source.
- WS1 owns source selection. WS2 operates on exactly one source and never scans all Source Records.

### Purpose

Transform the next unprocessed fragment of one selected Source into a confirmed block of atomic Source Items with unambiguous IDs and exact source text.

WS2 does not select a Source, read unrelated Source Records, interpret statements, classify them, change the BRS, or advance the Source Cursor. Its result is confirmed input for WS3.

### Local Definitions

| Term | Definition |
|---|---|
| Source | One identified origin of business information processed from top to bottom. |
| Source Record | The persisted record for one Source, including its identity, content or locator, Source Cursor, and Source Items. |
| Source Item | One atomic, independently confirmable unit of exact Source content. Before confirmation it exists only inside the Working Draft with status `PENDING CONFIRMATION`. After the user confirms the block, it is persisted with status `CAPTURED` and becomes input to WS3. |
| Source Cursor | The progress marker identifying the last Source Item fully processed into the BRS by WS3. WS2 reads this position but does not advance it. |

### Input

1. `Resume Point` with Target BRS, Active Mode, Next Action, and `active_source_id` when continuing an existing Source.
2. `New Source Input` when `next.action = REGISTER NEW SOURCE`:
   - `inline_source_text`: exact text supplied by the user; or
   - `source_locator`: a stable path, attachment, URL, or artifact reference;
   - Source identity: type, name, and optional version and authority.
3. `Active Source Record` loaded by `active_source_id` when `next.action = CAPTURE SOURCE ITEMS`.
4. Current `User Request` only when it contains new business content for the active interview or an answer to a saved question.

### Algorithm

```text
START WS2

1. READ Resume Point and the current User Request.

   IF next.action = CAPTURE SOURCE ITEMS AND active_source_id is absent
     THEN
       ASK which Source to continue;
       SAVE the question in Resume Point;
       STOP WS2.

   IF next.action = REGISTER NEW SOURCE AND New Source Input is absent
     THEN
       ASK the user to provide a Source;
       SAVE the question in Resume Point;
       STOP WS2.

2. SET Active Source:
   IF next.action = CAPTURE SOURCE ITEMS
     THEN
       LOAD only `sources/<active_source_id>.md`;

       IF that Source Record is unavailable
         THEN
           IDENTIFY the missing Source Record;
           ASK the user to restore or provide the Source again;
           SAVE the question in Resume Point;
           STOP WS2.

   ELSE IF next.action = REGISTER NEW SOURCE
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
         next.action = PROCESS CAPTURED SOURCE ITEMS;
         next.destination = WS3;
         next.routing_reason = Captured Source Items require BRS processing;
       GO TO WS3 without capturing another fragment.

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
     STOP WS2.

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
       KEEP Source Cursor unchanged;
       UPDATE Resume Point:
         active_source_id = Active Source ID;
         pending.type = none;
         pending.value = null;
         next.action = PROCESS CAPTURED SOURCE ITEMS;
         next.destination = WS3;
         next.routing_reason = Captured Source Items require BRS processing;
       SHOW:
         "Source Items saved.
          Source Cursor remains unchanged.
          Going to WS3.";
       GO TO WS3.

END WS2
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
  source_cursor:
    last_fully_processed_source_item_id: <Source Item ID or null>
  source_items:
    - source_item_id: SRC-NNN-SI-NNN
      source_text: <exact source text>
      source_position: <position in the Source or null>
      status: CAPTURED

resume_point:
  target_brs: NEW | <BRS identifier or path>
  active_mode: Creative | Standard | Simple
  active_source_id: SRC-NNN
  pending:
    type: none
    value: null
  next:
    action: PROCESS CAPTURED SOURCE ITEMS
    destination: WS3
    routing_reason: Captured Source Items require BRS processing
```

## Pending Workflow Stages

Define WS3 through WS7 only through the same proposal, confirmation, save, and verification cycle. Do not move WS2 into `SKILL.md` until its unresolved source-recognition and persistence rules are confirmed.

## Unnumbered Technical Implementation

Keep technical construction outside the workflow-stage sequence:

- Maintain `skills/develop-mini-brs/SKILL.md` as the compact core workflow.
- Maintain matching UI metadata in `skills/develop-mini-brs/agents/openai.yaml`.
- Add `skills/develop-mini-brs/references/mini-brs-format.md` only when its format is approved; do not keep an empty placeholder.
- Keep the skill self-contained and free of unnecessary scripts, assets, dependencies, or local README files.
- Keep the catalog entry in Draft status until final validation passes.
- Run the official skill validator and forward tests after WS7 is implemented.

## Verification Record

| Check | Result | Notes |
|---|---|---|
| WS1 plan structure | Passed | Contains the four required sections and allowed Local Definitions |
| WS1 routing | Passed | Every route is expressed in algorithm step 6 |
| Resume Point template | Passed | Included in WS1 Result |
| Full skill validation | Pending | Run after WS7 |
| Forward tests | Pending | Run after WS7 |
