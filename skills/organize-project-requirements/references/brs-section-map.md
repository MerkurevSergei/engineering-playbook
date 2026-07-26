# BRS Section Map

This v0.1 map derives from the repository's:

- `01-product-requirements/02-business-requirements-specification-standard.md`
- `01-product-requirements/03-discovering-and-building-a-business-requirements-baseline.md`

Read the current repository versions when changing the model. They are authoritative for this skill; this file is an operational routing summary.

| Project requirements file | BRS content | Scope rule |
|---|---|---|
| `README.md` | Package identity, owner, version, status, navigation, access notes | Navigation and control only; no detailed requirements |
| `00-governance.md` | Identification; approval; revision history | Whole baseline |
| `glossary.md` | Definitions; acronyms and abbreviations | Shared vocabulary only; keep capability-local terms local when they are not reused |
| `references.md` | Applicable laws, policies, contracts, strategies, standards, controlled documents | Link stable identifier/version; avoid copies |
| `01-purpose-scope-and-overview.md` | Business Purpose; Business Scope; Business Overview | Initiative-wide problem, boundary, and summary |
| `02-stakeholders-and-business-structure.md` | Major Stakeholders; Business Structure | Initiative-wide stakeholder classes, governance, decision rights, and relationships |
| `03-environment-and-business-model.md` | Business Environment; Business Model | Internal/external context and value model |
| `04-mission-goals-and-objectives.md` | Mission, Goals, and Objectives | Initiative mission and measurable outcomes; capability-local evidence stays with its capability |
| `05-information-and-processes.md` | Information Environment; Business Processes | Shared business information, end-to-end processes, handoffs, and ownership |
| `06-cross-cutting-rules-constraints-and-quality.md` | Operational Policies and Rules; Operational Constraints; Operational Quality | Only rules, constraints, and quality conditions spanning the initiative or several capabilities |
| `07-operational-concept-and-scenarios.md` | Operational Modes; High-Level Operational Concept; High-Level Operational Scenarios | End-to-end operation and modes; local scenarios stay with capabilities |
| `08-lifecycle-and-project-constraints.md` | Other Lifecycle Concepts; Project Constraints | Acquisition through retirement and initiative delivery boundaries |
| `09-readiness-and-approval.md` | Tailoring record, verification, validation, readiness, and approval summary | Local control layer supporting baseline approval |
| `capability-map.md` | Capability-centered decomposition used to organize BRS behavior and traceability | One row per coherent business ability |
| `capabilities/CAP-.../README.md` | Local outcome and boundary, stakeholders, terms, information, events, rules, scenarios, constraints, risks, evidence, downstream links | Exactly one owning capability; link shared items |

The numbered root files group related BRS sections rather than creating one physical file per heading. This keeps project-wide content reviewable while preserving the logical BRS coverage model.

Do not infer authoring order from the BRS heading order. Build source lineage and working registers first, then establish problem and outcome, provisional scope, stakeholders, current/future context, capabilities, rules, scenarios, verification, validation, and approval iteratively.
