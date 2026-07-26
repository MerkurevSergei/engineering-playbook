# AI Skills

Project-local source catalog for reusable AI workflows derived from this engineering playbook.

## Available Skills

- **Draft** — [Organize Project Requirements](organize-project-requirements/SKILL.md): create an evolvable `requirements/` package, classify and clarify statements, preserve source lineage, and route analyzed information to the correct artifact.

## Catalog Convention

Each skill lives in `skills/<skill-name>/` and contains a required `SKILL.md`, UI metadata under `agents/`, and only the scripts, references, or assets needed by the workflow.

This repository directory is the versioned source of each skill. If a Codex environment does not discover project-root `skills/` automatically, install or link the required skill into that environment's configured skills directory.
