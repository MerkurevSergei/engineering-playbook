# AI Skills

Project-local source catalog for reusable AI workflows derived from this engineering playbook.

## Available Skills

- **Draft** — [Orchestrate Product Requirements](orchestrate-product-requirements/SKILL.md): maintain a human-readable work status, track BRS coverage, and select the next requirements-engineering activity from current gaps and risk.
- **Draft** — [Conduct Stakeholder Elicitation](conduct-stakeholder-elicitation/SKILL.md): conduct one goal-driven activity with a live stakeholder and return atomic confirmed Evidence Items.
- **Draft** — [Analyze Fixed Requirements Source](analyze-fixed-requirements-source/SKILL.md): review a declared scope of a document or artifact and return traceable authenticated Evidence Items.
- **Draft** — [Organize Project Requirements](organize-project-requirements/SKILL.md): create the requirements package, analyze Evidence Items, preserve lineage, and route derived content to BRS or downstream artifacts.
- **Draft** — [Create Mini BRS](create-mini-brs/SKILL.md): guide a lightweight Vision/Scope, Capability Map, and capability-level Business Rules workflow through confirmed, traceable checkpoints.

## Catalog Convention

Each skill lives in `skills/<skill-name>/` and contains a required `SKILL.md`, UI metadata under `agents/`, and only the references or assets needed by the workflow.

This repository directory is the versioned source of each skill. If a Codex environment does not discover project-root `skills/` automatically, install or link the required skill into that environment's configured skills directory.
