# Diagrams

Thirty-four diagrams, from abstract to detailed, written as LaTeX and TikZ so they can be reviewed in pull requests. Each level answers a different question for a different reader. All rendered PDF and SVG files are in one folder, `output/`, named `<level>_<diagram>` (for example `output/03-code_domain-model.pdf`).

## Reading order

| Level | Folder | Question it answers | Diagrams |
|---|---|---|---|
| 00 Context | `00-context/` | What is the system, who uses it, what must it do, and what is each folder for? | system-context, use-cases, requirements-map, repository-map |
| 01 Containers | `01-containers/` | What runs where, and what may depend on what? | containers, layers-and-dependencies, deployment-local, deployment-aws |
| 02 Components | `02-components/` | What is inside each container? | ml-pipeline, inference-service, science-chain, evidence-subsystem, api-service, web-portal |
| 03 Code | `03-code/` | Which entities, interfaces, models and routes exist? | domain-model, ports-adapters, model-zoo, package-dependencies, api-routes |
| 04 Behaviour | `04-behaviour/` | In what order do things happen, and what states can a result be in? | seq-detect-and-quantify, seq-analyst-review, seq-export-dossier, seq-login-rbac, state-candidate-status, flow-user-journey |
| 05 Data | `05-data/` | What does the data look like and where does it live? | tensor-contract, split-policy, synthetic-recipe-flow, er-model, dataflow |
| 06 MLOps and delivery | `06-mlops/` | How does a model get trained, judged, promoted and watched, and what do I do every time I change something? | lifecycle, release-gate, change-workflow, environments-promotion |

Who owns which folder and file is not drawn; it is in `../docs/assignments.md`. Start with 00-context/system-context, then 01-containers/layers-and-dependencies, then the folder of the package you will edit.

## Build

`make` in this folder builds every diagram to `output/*.pdf` and `output/*.svg` (needs TeX Live with TikZ, latexmk, and poppler-utils for pdftocairo). `make clean` removes the `build/` byproducts; `make distclean` also removes `output/`. Shared style is `_common/mwstyle.tex` and sequence macros are `_common/mwseq.tex`; a colour change is one edit.

## What is fact and what is proposal

Facts come from the project report (requirements, targets, decisions, the three verification stages, the four statuses) and from the team's synthetic-data notes (counts, ranges, thresholds). Proposals are marked in the diagram source: the port list, DynamoDB keys, API paths, permission cells shown as an open circle, owners, and the user-journey step numbering, which should be checked against report Figure 5.2.4.
