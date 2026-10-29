# Requirements traceability

Each requirement from the report, the package that satisfies it, the diagram that explains it and the test that proves it. The picture form is diagrams/00-context/requirements-map. Keep the two in step.

| Requirement | Packages | Diagram | Test |
|---|---|---|---|
| FR1 Automated sourcing and harmonisation | data, adapters/stac, workers | 02-components/inference-service, 05-data/dataflow | tests/unit/data/test_tensor_contract.py |
| FR2 Plume segmentation and AI screening | models, training, evaluation, inference | 03-code/model-zoo, 02-components/ml-pipeline | tests/ml/test_model_zoo_shapes.py |
| FR3 Quantification and attribution | quantification, attribution, adapters/era5 | 02-components/science-chain | tests/unit/quantification, tests/unit/attribution |
| FR4 Case lifecycle and enforcement (Beta) | services, workers | 04-behaviour/flow-user-journey | scaffold only |
| FR5 Role-based access control | domain/roles, api/rbac, api/audit | 03-code/api-routes, 04-behaviour/seq-login-rbac | tests/unit/api/test_permission_matrix.py |
| FR6 Results dashboard | api, web | 02-components/web-portal | web/e2e/review-flow.spec.ts |
| FR7 Scientific verification | verification, domain/status, services | 04-behaviour/state-candidate-status | tests/unit/verification, tests/unit/domain/test_status_rules.py |
| NFR1 Performance (15 min per granule, 1.5 s p95 tiles) | inference, web | 04-behaviour/seq-detect-and-quantify | timing test on a 25-chip granule |
| NFR2 Reliability, false alarms, evidence vault | evaluation, evidence | 02-components/evidence-subsystem | tests/unit/evidence/test_tamper_detected.py |
| NFR3 Security, encryption, audit log | api, evidence/audit_chain, infra/security | 03-code/api-routes | tests/unit/evidence/test_audit_chain.py |
| NFR4 Scalability (Beta) | infra | 01-containers/deployment-aws | scaffold only |
| NFR5 Maintainability, reproducibility, rollback | core, data/manifest, services/promote_model | 06-mlops/lifecycle, 06-mlops/release-gate | tests/unit/evaluation/test_release_gate.py |
| NFR6 Usability (SUS at least 75) | web | 04-behaviour/flow-user-journey | usability session |

## Open points in the report to settle with the advisor

PB-22 is Must in Table 6.1 but Should in Section 7.2.3. PB-18 is Must in one place and Should in another (Section 7.2.2). PB-32 and PB-33 share the Jira key MWPMWP-64. The backlog source list names FR1 to FR6 although FR7 exists. Token lifetime, key custody and several permission cells in configs/permissions.yaml are not fixed by the report.
