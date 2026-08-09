---
name: organize-project-requirements
description: Create and evolve a project's evidence-driven requirements package, atomize and analyze confirmed source information, update workflow state, preserve lineage, and route derived content to BRS files, capability modules, research questions, decisions, downstream specifications, or evidence. Use when Codex must initialize requirements artifacts, process Evidence Items, show where a stakeholder statement or document finding went, update BRS coverage, organize or update a BRS, or classify and place a rule, scenario, constraint, decision, source note, or open question.
---

# Organize Project Requirements

> Status: Draft. The structure and routing model are intentionally incomplete and expected to evolve through real project use.

Build an evolvable requirements package and keep source evidence separate from analyzed and approved business content. Preserve enough source meaning, context, and location to support confirmation and traceability. Keep verbatim live-source wording only when audit, legal, research, or user instructions require it.

## Load the Domain Model

Read both references before creating a package or filing content:

- [references/structure-and-routing.md](references/structure-and-routing.md) for the directory model, lifecycle, classification, placement rules, and identifiers.
- [references/brs-section-map.md](references/brs-section-map.md) for the mapping from BRS sections to project-wide files and capability-local content.

Treat these references as the current v0.1 model. Extend them when the repository adds a governed artifact type or a proven routing rule.

Treat `requirements/work-status.md` as the human handoff page. Each source, activity, Evidence Item, question, analysis item, decision, trace link, and BRS item keeps one authoritative Markdown home. The handoff page summarizes coverage and the next action without duplicating full content.

## Create the Requirements Package

1. Inspect the target repository for an existing `requirements/` package and local instructions.
2. Start with the smallest form that meets the request. Use the Markdown starter in `assets/requirements-template/` when a modular BRS package and working registers are justified.
3. Preview the list of files and destinations in conversation or tool output.
4. Create only missing Markdown files and directories. Never overwrite existing content during initialization.
5. Replace placeholders only with known facts. Leave an explicit `TBD` and create a research question for material unknowns; do not invent owners, authority, scope, measures, or approval.
6. Reconcile `work-status.md` and every register with pre-existing artifacts before treating the handoff page as current.
7. Do not create empty optional model, rule, or scenario directories until a tailoring trigger justifies them.

Use `assets/capability-template.md` for a new capability. Inspect existing capability IDs, allocate the next monotonic ID, create its Markdown page, and update `capability-map.md`, `capabilities/README.md`, the coverage table, and applicable traceability rows. Name capabilities as stable business abilities, not processes, screens, APIs, databases, services, or technical actions.

## File a Statement

### 1. Inspect Before Editing

Read the package `README.md`, working registers, capability map, relevant capability pages, and candidate destination. Search stable IDs and distinctive wording to avoid duplicates.

### 2. Preserve the Evidence

If the item is not already traceable, add or link its source in `working/source-register.md` and record an atomic Evidence Item in `working/evidence-register.md`.

- For a live source, preserve confirmed normalized meaning, participant, authority, activity, and context. Keep rejected drafts transient unless retention is required.
- For a fixed source, preserve the stable artifact identity, version, exact locator, and faithful finding or permitted excerpt.

Do not silently convert source evidence into an approved requirement.

### 3. Split and Classify

Split compound evidence into atomic items. Give each derived Analysis Item one primary classification from the routing reference. Preserve relationships between evidence, split items, questions, and destinations.

Distinguish at least:

- business outcome or other project-wide BRS information;
- capability-local outcome, rule, scenario, information, event, constraint, or evidence;
- stakeholder requirement;
- functional or non-functional solution requirement;
- transition requirement;
- design decision or candidate;
- raw statement, observation, assumption, conflict, decision, or open question.

### 4. Clarify Only What Changes the Route or Meaning

Resolve, when material:

- exact source, date, and context;
- governing authority or accountable owner;
- intended outcome and observable measure;
- initiative-wide, cross-capability, or capability-local scope;
- applicability, trigger, conditions, exceptions, and time horizon;
- lifecycle state and approval status;
- whether solution wording is a real constraint or merely a proposed implementation.

If the missing answer blocks classification, scope, authority, or normative meaning, keep the item in `working/`, add a research question with owner/date when known, and report what must be resolved. Continue filing non-blocking facts safely.

### 5. Route by State, Type, and Scope

Apply this order:

1. **Processing state:** evidence remains in `working/` even after it is processed; its disposition points to the derived destination or terminal rationale.
2. **Requirement level:** stakeholder, solution, transition, and design items route outside the BRS through `downstream/README.md` or the repository's owning artifact.
3. **Scope:** accepted business information goes to a project-wide root file, a capability page, or a project-wide cross-cutting section.
4. **Evidence:** approval, verification, delivery, and outcome evidence is linked from `evidence/README.md`; do not copy an authoritative external record by default.

Never promote an item to `Accepted` or `Baselined` without the required business authority. Never treat the file location itself as approval.

### 6. Write a Traceable Result

For an analyzed item, retain or add:

- stable item ID;
- concise normalized statement;
- source ID or link to the elicitation entry;
- rationale and primary classification;
- capability or project-wide scope;
- lifecycle status;
- owner or authority when required;
- relationships to outcomes, rules, scenarios, downstream requirements, and evidence.

Set the Evidence Item to `closed` only when confirmation or authentication, classification, disposition, target IDs or terminal rationale, open questions, and trace links are present. Apply `draft` through `baselined` only to derived BRS items, never to source evidence.

Use declarative wording for business rules. State outcomes without prescribing system design. Keep observations separate from interpretations.

### 7. Verify the Change

Check that:

- the confirmed source meaning or fixed-source locator remains traceable;
- the normalized item has one primary home;
- no project-wide content was copied into every capability;
- no capability was named after a technical component;
- no raw or disputed item appears as approved baseline content;
- no stakeholder, solution, transition, or design requirement was mislabeled as a business requirement;
- links and stable IDs resolve;
- changed Markdown tables remain valid.

Update affected authoritative rows and `work-status.md`, recalculate coverage, and summarize the classification, disposition, destination, remaining questions, and exact next action for the orchestrator.

## Evolve the Model Safely

Add structure only for a concrete trigger such as independent ownership, reuse, approval, tooling, assurance, access control, or review size. Prefer links to existing authoritative sources over copies. When a new artifact type appears repeatedly, update the routing reference and starter assets together, then validate the skill again.
