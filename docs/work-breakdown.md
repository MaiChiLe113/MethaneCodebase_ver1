# Work breakdown: file by file

Generated from the headers of the placeholder files. Owners are proposals from the roles in report Table 1.3; confirm and rebalance at sprint planning. The Backlog and Jira columns are left blank on purpose: the report's backlog (Table 6.1) is the source, and the titles were not copied here so that nothing is mis-mapped. Fill them in when each person takes a file, and put the Jira key (MWPMWP-n) in every commit and pull request title.

## Summary

| Member | Files | Alpha | Beta scaffold |
|---|---|---|---|
| Chi | 68 | 61 | 7 |
| Hai | 21 | 21 | 0 |
| Ha | 30 | 27 | 3 |
| Nam | 58 | 51 | 7 |
| Chau | 15 | 15 | 0 |
| Lam | 9 | 9 | 0 |

Total placeholder files: 201 (plus package markers and tooling).

These are file counts, not effort. Chi and Nam hold the most files because the 13 ports, the configs, the tests and the whole web portal are many small files; Hai and Lam hold fewer because the Mamba family, ST-CM-UNet and the injection physics are research-heavy. If the load looks uneven at sprint planning, the first moves to consider are handing the thirteen ports/ files out by theme (data ports to Chau, evidence ports to Ha, model registry to Hai) and splitting web/ between Nam and Lam.

## Chi

| File | Purpose | Requirements | Stage | Backlog | Jira |
|---|---|---|---|---|---|
| `configs/data/s2.yaml` | Sentinel-2 settings: bands, GSD 20 m, chip 100, references up to 6, cloud limits. | FR1 | Alpha | | |
| `configs/data/splits.yaml` | Split grouping keys and seeds. | FR2 | Alpha | | |
| `configs/model/classical.yaml` | Hyper-parameters for classical. | FR2 | Alpha | | |
| `configs/model/unet.yaml` | Hyper-parameters for unet. | FR2 | Alpha | | |
| `docker-compose.yml` | Local stack: web, api, LocalStack, MLflow, inference worker. | NFR5 | Alpha | | |
| `dvc.yaml` | DVC stages: recipes, splits, manifests. | FR2, NFR5 | Alpha | | |
| `infra/terraform/main.tf` | Root module: wires the four modules. | NFR4, NFR5 | Beta scaffold | | |
| `infra/terraform/modules/data_pipeline/main.tf` | Serverless ingestion and detection: event rule, queue, function, data lake bucket. | FR1, NFR1 | Beta scaffold | | |
| `infra/terraform/modules/mlops/main.tf` | Training storage, MLflow artefact bucket, container registry. | FR2, NFR5 | Beta scaffold | | |
| `infra/terraform/outputs.tf` | Outputs: endpoints and bucket names. | NFR5 | Beta scaffold | | |
| `infra/terraform/variables.tf` | Input variables: region, environment, budget alarm. | NFR5 | Beta scaffold | | |
| `scripts/build_work_breakdown.py` | Regenerate docs/work-breakdown.md from the file headers. | NFR5 | Alpha | | |
| `scripts/seed_demo_data.py` | Create a tiny demo region with candidates for the portal and the tutor demo. | FR6 | Alpha | | |
| `src/methanewatch/adapters/aws/dynamodb_repositories.py` | Detection, Review, Region, User and ModelVersion repositories on DynamoDB. | FR2, FR5, FR6 | Alpha | | |
| `src/methanewatch/adapters/aws/s3_object_store.py` | ObjectStore on S3, with LocalStack for development. | NFR2 | Alpha | | |
| `src/methanewatch/adapters/local/fs_object_store.py` | ObjectStore on the local disk. | NFR5 | Alpha | | |
| `src/methanewatch/adapters/local/mlflow_registry.py` | ModelRegistry on a local MLflow server. | FR2, NFR5 | Alpha | | |
| `src/methanewatch/adapters/memory/fakes.py` | In-memory implementations of every port for unit tests. | NFR5 | Alpha | | |
| `src/methanewatch/adapters/stac/stac_scene_source.py` | SceneSource for Sentinel-2 L1C through STAC (pystac-client). | FR1 | Alpha | | |
| `src/methanewatch/api/deps.py` | Composition root: builds adapters from settings and injects them into services. | NFR5 | Alpha | | |
| `src/methanewatch/cli/main.py` | Command line: train, evaluate, detect, seed-demo, verify-dossier. | NFR5 | Alpha | | |
| `src/methanewatch/core/clock.py` | Clock Protocol with SystemClock and FixedClock. | NFR2 | Alpha | | |
| `src/methanewatch/core/config.py` | Typed configuration (Pydantic v2) loaded from configs/*.yaml and environment. | NFR5 | Alpha | | |
| `src/methanewatch/core/errors.py` | The small set of typed errors every layer raises: NotFound, PermissionDenied, Invalid, Unavailable, Conflict. | NFR3, NFR5 | Alpha | | |
| `src/methanewatch/core/ids.py` | Typed identifiers (DetectionId, SceneId, RegionId, UserId) and their string forms. | NFR2 | Alpha | | |
| `src/methanewatch/core/logging.py` | Structured logging with a request or run id on every line. | NFR5 | Alpha | | |
| `src/methanewatch/core/units.py` | Unit conversions with explicit names: kg/h, ppb, mol/m2, m/s, km, pixels at 20 m. | FR3, NFR2 | Alpha | | |
| `src/methanewatch/data/dataset.py` | PyTorch Dataset over recipes (synthetic) or real samples. | FR2 | Alpha | | |
| `src/methanewatch/data/ingest.py` | Find and fetch Sentinel-2 L1C scenes for a region and date, recording checksums. | FR1 | Alpha | | |
| `src/methanewatch/data/loader.py` | DataLoader factory with collate function and worker seeding. | FR2, NFR1 | Alpha | | |
| `src/methanewatch/data/manifest.py` | Hashed manifest: every sample id, its split and a content hash. | NFR2, NFR5 | Alpha | | |
| `src/methanewatch/data/preprocess.py` | Harmonise bands B11 and B12 to 20 m, apply the harmonised-DN offset, mask invalid pixels, record the preprocessing version. | FR1, NFR2 | Alpha | | |
| `src/methanewatch/data/schema.py` | Constants and checks for the tensor contract: bands (B11, B12), chip size 100, GSD 20 m, up to 6 references, shape (B,7,2,100,100) and ref_valid (B,7). | FR1, FR2 | Alpha | | |
| `src/methanewatch/data/splits.py` | Grouped splits by event, site and date; refuses to put a synthetic id in the benchmark set. | FR2, NFR2 | Alpha | | |
| `src/methanewatch/data/stack.py` | Build one sample: target plus up to 6 references, padded and masked with ref_valid. | FR1, FR2 | Alpha | | |
| `src/methanewatch/data/tiling.py` | Cut a scene into 100 x 100 chips (a 10 km granule gives 25) and stitch predictions back. | FR1, NFR1 | Alpha | | |
| `src/methanewatch/domain/entities.py` | Dataclasses for the entities in diagrams/03-code/domain-model: Region, Scene, Detection, Review, VerificationResult, FacilityMatch, EvidenceDossier, User, AuditEntry, ModelVersion. | FR2, FR3, FR5, FR7 | Alpha | | |
| `src/methanewatch/domain/estimate.py` | EmissionEstimate as a sum type: Estimate(rate, low, high, wind_source, wind_version, preliminary) / Unavailable(reason) / Uncertain(reason). | FR3, FR7 | Alpha | | |
| `src/methanewatch/domain/events.py` | Domain events (DetectionCreated, ReviewRecorded, DossierExported, ModelPromoted). | NFR3 | Alpha | | |
| `src/methanewatch/domain/roles.py` | Role and Action enumerations (analyst, inspector, regulator, ml_engineer, admin). | FR5, NFR3 | Alpha | | |
| `src/methanewatch/domain/status.py` | The four statuses (Supported, Rejected, Uncertain, Unreviewable) and the rule that an emission is confirmed only when an analyst sets Supported and evidence is complete. | FR7 | Alpha | | |
| `src/methanewatch/domain/value_objects.py` | Small immutable types: Point, Polygon, DateRange, Tile, Sha256, Confidence. | FR1, FR2 | Alpha | | |
| `src/methanewatch/inference/candidates.py` | Candidate object: mask, polygon, confidence, model version. | FR2 | Alpha | | |
| `src/methanewatch/inference/pipeline.py` | Scene stack to ranked candidates; the unit that must finish within 15 minutes per granule. | FR2, NFR1 | Alpha | | |
| `src/methanewatch/inference/predictor.py` | Load an approved model and predict logits for a scene stack, tile by tile. | FR2, NFR1 | Alpha | | |
| `src/methanewatch/models/classical/threshold.py` | Classical band-ratio or threshold baseline on B11 and B12 (no training). | FR2 | Alpha | | |
| `src/methanewatch/models/unet/model.py` | U-Net baseline; references stacked as channels. | FR2 | Alpha | | |
| `src/methanewatch/ports/audit_sink.py` | AuditSink Protocol. | NFR3 | Alpha | | |
| `src/methanewatch/ports/auth_provider.py` | AuthProvider Protocol. | FR5, NFR3 | Alpha | | |
| `src/methanewatch/ports/detection_repository.py` | DetectionRepository Protocol. | FR2, FR6 | Alpha | | |
| `src/methanewatch/ports/evidence_store.py` | EvidenceStore Protocol. | NFR2 | Alpha | | |
| `src/methanewatch/ports/facility_index.py` | FacilityIndex Protocol. | FR3 | Alpha | | |
| `src/methanewatch/ports/model_registry.py` | ModelRegistry Protocol. | FR2, NFR5 | Alpha | | |
| `src/methanewatch/ports/object_store.py` | ObjectStore Protocol. | FR1, NFR2 | Alpha | | |
| `src/methanewatch/ports/region_repository.py` | RegionRepository Protocol. | FR1, FR6 | Alpha | | |
| `src/methanewatch/ports/review_repository.py` | ReviewRepository Protocol. | FR5, FR7 | Alpha | | |
| `src/methanewatch/ports/scene_source.py` | SceneSource Protocol. | FR1 | Alpha | | |
| `src/methanewatch/ports/signer.py` | Signer Protocol. | NFR2, NFR3 | Alpha | | |
| `src/methanewatch/ports/user_repository.py` | UserRepository Protocol. | FR5 | Alpha | | |
| `src/methanewatch/ports/wind_provider.py` | WindProvider Protocol. | FR3 | Alpha | | |
| `src/methanewatch/workers/detect_worker.py` | Process one scene or one region and date by calling RunDetection. | FR1, FR2, NFR1 | Alpha | | |
| `src/methanewatch/workers/ingest_worker.py` | Triggered by a new Sentinel-2 pass (serverless in Beta). | FR1, NFR1 | Beta scaffold | | |
| `tests/conftest.py` | Shared fixtures: in-memory adapters, fixed clock, tiny synthetic stacks. | NFR5 | Alpha | | |
| `tests/integration/test_dynamodb_localstack.py` | Repositories against LocalStack with the keys from er-model. | FR2, NFR5 | Beta scaffold | | |
| `tests/unit/data/test_splits_no_leak.py` | Grouped splits leave no event, site or date in two splits; no synthetic id in the benchmark. | FR2, NFR2 | Alpha | | |
| `tests/unit/data/test_tensor_contract.py` | Shapes (B,7,2,100,100) and (B,7); padding and ref_valid with 4 real references. | FR2 | Alpha | | |
| `tests/unit/domain/test_estimate_types.py` | No code path can produce a bare rate; Unavailable and Uncertain carry reasons. | FR3, FR7 | Alpha | | |
| `tests/unit/domain/test_status_rules.py` | An emission is confirmed only when an analyst sets Supported and evidence is complete; every other combination is not. | FR7 | Alpha | | |

## Hai

| File | Purpose | Requirements | Stage | Backlog | Jira |
|---|---|---|---|---|---|
| `configs/model/cd_mamba.yaml` | Hyper-parameters for cd_mamba. | FR2 | Alpha | | |
| `configs/model/kmetha.yaml` | Hyper-parameters for kmetha. | FR2 | Alpha | | |
| `configs/model/st_cm_unet.yaml` | Hyper-parameters for st_cm_unet. | FR2 | Alpha | | |
| `configs/model/vmamba.yaml` | Hyper-parameters for vmamba. | FR2 | Alpha | | |
| `configs/train/pretrain.yaml` | Synthetic pretraining: data, optimiser, schedule, seed. | FR2 | Alpha | | |
| `docker/trainer.Dockerfile` | CUDA image for training with mamba-ssm. | FR2 | Alpha | | |
| `src/methanewatch/models/base.py` | SegmentationModel Protocol: forward(x, ref_valid) -> logits (B,1,100,100). | FR2 | Alpha | | |
| `src/methanewatch/models/mamba/cd_mamba.py` | Change-detection Mamba comparing target and references. | FR2 | Alpha | | |
| `src/methanewatch/models/mamba/kmetha.py` | Methane-specific Mamba variant. | FR2 | Alpha | | |
| `src/methanewatch/models/mamba/scan_fallback.py` | Pure PyTorch selective scan used when mamba-ssm or CUDA is missing. | FR2, NFR5 | Alpha | | |
| `src/methanewatch/models/mamba/vmamba.py` | Vision Mamba segmentation model. | FR2 | Alpha | | |
| `src/methanewatch/models/registry.py` | Name-to-class registry and build_model(cfg). | FR2 | Alpha | | |
| `src/methanewatch/models/st_cm_unet/model.py` | ST-CM-UNet: proposed hybrid CNN and Mamba U-Net. | FR2 | Alpha | | |
| `src/methanewatch/training/callbacks.py` | Checkpointing, early stopping, MLflow logging. | FR2, NFR5 | Alpha | | |
| `src/methanewatch/training/losses.py` | Segmentation losses chosen by config (for example BCE with Dice). | FR2 | Alpha | | |
| `src/methanewatch/training/optim.py` | Optimiser and scheduler factories. | FR2 | Alpha | | |
| `src/methanewatch/training/pretrain.py` | Entry point for synthetic pretraining. | FR2 | Alpha | | |
| `src/methanewatch/training/seed.py` | Global seeding and deterministic-mode switch. | NFR5 | Alpha | | |
| `src/methanewatch/training/trainer.py` | Small hand-written training loop: epochs, mixed precision, gradient clipping, resume. | FR2, NFR5 | Alpha | | |
| `tests/ml/test_model_zoo_shapes.py` | Every registered model accepts (B,7,2,100,100) plus ref_valid and returns (B,1,100,100). | FR2 | Alpha | | |
| `tests/ml/test_overfit_tiny_batch.py` | Each trainable model can overfit eight samples on CPU. | FR2 | Alpha | | |

## Ha

| File | Purpose | Requirements | Stage | Backlog | Jira |
|---|---|---|---|---|---|
| `configs/eval/benchmark.yaml` | Models and splits in the benchmark; includes the zero-shot pretrained model. | FR2 | Alpha | | |
| `configs/model/sam4ch4.yaml` | Hyper-parameters for sam4ch4. | FR2 | Alpha | | |
| `configs/model/vit_unet.yaml` | Hyper-parameters for vit_unet. | FR2 | Alpha | | |
| `configs/train/finetune.yaml` | Fine-tuning: checkpoint, real splits, learning rate. | FR2 | Alpha | | |
| `infra/terraform/modules/security/main.tf` | Identity pool or Cognito, key management, evidence bucket with Object Lock, logging. | NFR3 | Beta scaffold | | |
| `src/methanewatch/adapters/aws/dynamodb_audit_sink.py` | AuditSink with conditional writes (refuse overwrite). | NFR3 | Alpha | | |
| `src/methanewatch/adapters/aws/s3_evidence_store.py` | EvidenceStore on S3 Object Lock (write once). | NFR2 | Beta scaffold | | |
| `src/methanewatch/adapters/local/ed25519_signer.py` | Signer using an Ed25519 key from an untracked file. | NFR2, NFR3 | Alpha | | |
| `src/methanewatch/evaluation/benchmark.py` | Run every model on the sealed real test and write one results table; also score the zero-shot pretrained model. | FR2 | Alpha | | |
| `src/methanewatch/evaluation/error_analysis.py` | Errors by site, cloud level and emission rate. | FR2, NFR2 | Alpha | | |
| `src/methanewatch/evaluation/gates.py` | Release gate function: Beta needs F1 >= 0.80 and FPR < 0.03 percent; Alpha targets are reported only. | NFR2, NFR5 | Alpha | | |
| `src/methanewatch/evaluation/metrics.py` | IoU, F1, precision, recall, false-positive rate at pixel and object level. | FR2, NFR2 | Alpha | | |
| `src/methanewatch/evaluation/report.py` | Tables and figures from a BenchmarkResult. | FR2 | Alpha | | |
| `src/methanewatch/evidence/audit_chain.py` | Hash-chained audit entries: each holds the hash of the previous one. | NFR3 | Alpha | | |
| `src/methanewatch/evidence/hashing.py` | Streamed SHA-256 of every artefact and a manifest of digests. | NFR2, NFR3 | Alpha | | |
| `src/methanewatch/evidence/provenance.py` | PROV-style lineage: data, code version, model, person. | NFR2 | Alpha | | |
| `src/methanewatch/evidence/signing.py` | Ed25519 detached signature over the manifest through the Signer port. | NFR2, NFR3 | Alpha | | |
| `src/methanewatch/evidence/verify.py` | Recompute digests and check the signature; return Intact or Tampered with the changed artefact. | NFR2 | Alpha | | |
| `src/methanewatch/models/sam4ch4/model.py` | Zero-shot SAM-based reference wrapper (inference only). | FR2 | Alpha | | |
| `src/methanewatch/models/vit_unet/model.py` | ViT encoder with U-Net decoder. | FR2 | Alpha | | |
| `src/methanewatch/training/finetune.py` | Entry point for fine-tuning on real data. | FR2 | Alpha | | |
| `src/methanewatch/verification/mbmp.py` | Multi-band multi-pass enhancement product used for consistency checks. | FR7 | Alpha | | |
| `src/methanewatch/verification/stage2_consistency.py` | Stage 2: compare the mask with the MBMP product and with history to find persistent surface features. | FR7 | Alpha | | |
| `src/methanewatch/verification/status.py` | Combine stage results into a proposed status with evidence references. | FR7 | Alpha | | |
| `tests/integration/test_s3_object_lock.py` | Overwriting an evidence object is refused. | NFR2 | Beta scaffold | | |
| `tests/unit/evaluation/test_metrics.py` | IoU, F1, FPR on hand-made masks including empty masks. | FR2 | Alpha | | |
| `tests/unit/evaluation/test_release_gate.py` | Beta gate passes and fails at boundary values; Alpha targets never block. | NFR5 | Alpha | | |
| `tests/unit/evidence/test_audit_chain.py` | Editing or removing an entry breaks the chain. | NFR3 | Alpha | | |
| `tests/unit/evidence/test_tamper_detected.py` | Change one byte of a protected artefact in a test copy; verify returns Tampered and names it. | NFR2 | Alpha | | |
| `tests/unit/verification/test_stages.py` | Each stage on constructed cases: cloud gives Unreviewable; persistent feature gives Rejected. | FR7 | Alpha | | |

## Nam

| File | Purpose | Requirements | Stage | Backlog | Jira |
|---|---|---|---|---|---|
| `.github/workflows/ci.yml` | CI: ruff, mypy, import-linter, pytest, web build and tests, diagram build check. | NFR5 | Alpha | | |
| `docker/api.Dockerfile` | Image for the API and workers (no CUDA). | NFR5 | Alpha | | |
| `docker/web.Dockerfile` | Build and serve the React portal. | FR6 | Alpha | | |
| `infra/terraform/modules/web_app/main.tf` | EC2 web app, load balancer with TLS, DynamoDB tables. | FR6, NFR1 | Beta scaffold | | |
| `scripts/export_openapi.py` | Write the OpenAPI JSON used to generate the TypeScript client. | FR6 | Alpha | | |
| `scripts/gen_ts_client.sh` | Generate web/src/api/client.ts from the OpenAPI JSON. | FR6 | Alpha | | |
| `src/methanewatch/adapters/aws/cognito_auth.py` | AuthProvider on Amazon Cognito. | FR5, NFR3 | Beta scaffold | | |
| `src/methanewatch/adapters/local/jwt_auth.py` | AuthProvider with JWT tokens and argon2 password hashes. | FR5, NFR3 | Alpha | | |
| `src/methanewatch/api/audit.py` | Audit middleware: state changes, exports and denied requests. | NFR3 | Alpha | | |
| `src/methanewatch/api/auth.py` | Token to user and role; reject unknown tokens. | FR5, NFR3 | Alpha | | |
| `src/methanewatch/api/errors.py` | Map core errors to HTTP responses. | NFR5 | Alpha | | |
| `src/methanewatch/api/main.py` | FastAPI app: request id, error mapping, router registration. | FR5, FR6, NFR3 | Alpha | | |
| `src/methanewatch/api/rbac.py` | Role by action check from configs/permissions.yaml; deny by default. | FR5, NFR3 | Alpha | | |
| `src/methanewatch/api/routers/admin.py` | Router: users, roles, model metrics and promotion. | FR5, FR2 | Alpha | | |
| `src/methanewatch/api/routers/detections.py` | Router: list, filter and site history. | FR6 | Alpha | | |
| `src/methanewatch/api/routers/evidence.py` | Router: build, download and verify a dossier. | FR6, NFR2 | Alpha | | |
| `src/methanewatch/api/routers/layers.py` | Router: satellite images and enhancement tiles for the map. | FR6, NFR1 | Alpha | | |
| `src/methanewatch/api/routers/regions.py` | Router: regions and alert settings. | FR1, FR4 | Beta scaffold | | |
| `src/methanewatch/api/routers/review.py` | Router: confirm, reject, correct mask. | FR5, FR7 | Alpha | | |
| `src/methanewatch/api/schemas.py` | Pydantic request and response models; source of the OpenAPI contract. | FR6 | Alpha | | |
| `src/methanewatch/evidence/dossier.py` | Render the readable PDF and the manifest.json. | NFR2, FR6 | Alpha | | |
| `src/methanewatch/services/configure_region.py` | Use case: create or change a monitored region and alert cadence. | FR1, FR4 | Beta scaffold | | |
| `src/methanewatch/services/export_dossier.py` | Use case: seal, sign and store a dossier, then audit the export. | FR6, NFR2, NFR3 | Alpha | | |
| `src/methanewatch/services/promote_model.py` | Use case: promote a model only if the Beta gate passes; roll back to the previous version. | FR2, NFR5 | Alpha | | |
| `src/methanewatch/services/query_detections.py` | Use case: list, filter and site history. | FR6 | Alpha | | |
| `src/methanewatch/services/review_detection.py` | Use case: record a review (append-only) and audit it. | FR5, FR7, NFR3 | Alpha | | |
| `src/methanewatch/services/run_detection.py` | Use case: scenes to a saved detection with proposal, estimate and match. | FR1, FR2, FR3, FR7, NFR1 | Alpha | | |
| `src/methanewatch/services/verify_dossier.py` | Use case: verify a stored dossier. | NFR2 | Alpha | | |
| `src/methanewatch/workers/alert_worker.py` | Send alerts for confirmed detections in monitored regions. | FR4, FR6 | Beta scaffold | | |
| `tests/integration/test_api_end_to_end.py` | Sign in, list, review, export and verify through HTTP with in-memory adapters. | FR5, FR6, FR7 | Alpha | | |
| `tests/unit/api/test_permission_matrix.py` | Every role by every action against configs/permissions.yaml; every refusal is 403 and audited. | FR5, NFR3 | Alpha | | |
| `tests/unit/api/test_token_guard.py` | Missing, malformed and expired tokens give 401. | FR5, NFR3 | Alpha | | |
| `tests/unit/services/test_export_requires_supported.py` | Export is refused unless the latest review is Supported and evidence complete. | FR6, NFR2 | Alpha | | |
| `tests/unit/services/test_review_append_only.py` | A second review adds a record; the first stays; each writes an audit entry. | FR5, FR7, NFR3 | Alpha | | |
| `web/e2e/permissions.spec.ts` | Playwright test: each role sees only what it may use. | FR5 | Alpha | | |
| `web/e2e/review-flow.spec.ts` | Playwright test: locate a candidate, read evidence, record a review. | FR6, FR7, NFR6 | Alpha | | |
| `web/src/api/client.ts` | Typed API client generated from the OpenAPI contract (do not edit by hand). | FR6 | Alpha | | |
| `web/src/app/App.tsx` | Layout shell: navigation limited by role. | FR6 | Alpha | | |
| `web/src/app/auth.tsx` | Sign-in state; token held in memory, not localStorage. | FR5, NFR3 | Alpha | | |
| `web/src/app/queryClient.ts` | TanStack Query client with caching rules. | NFR1 | Alpha | | |
| `web/src/app/router.tsx` | Route table and role guards. | FR5, FR6 | Alpha | | |
| `web/src/components/EmptyState.tsx` | Empty and error states. | NFR6 | Alpha | | |
| `web/src/components/StatusBadge.tsx` | Status chip using the four statuses with distinct shapes and text, not colour only. | NFR6 | Alpha | | |
| `web/src/components/UncertaintyBar.tsx` | Range display for an Estimate or the reason for Unavailable. | NFR6 | Alpha | | |
| `web/src/features/access/RoleGuard.tsx` | Hide actions the API would refuse. | FR5 | Alpha | | |
| `web/src/features/evidence/DossierCard.tsx` | Dossier state, integrity result, download. | NFR2 | Alpha | | |
| `web/src/features/map/MapView.tsx` | MapLibre map with layers: change in CH4, RGB, wind vectors, plume polygons, facilities. | FR6, NFR1 | Alpha | | |
| `web/src/features/regions/RegionEditor.tsx` | Polygon or country picker and cadence. | FR1 | Beta scaffold | | |
| `web/src/features/review/ReviewPanel.tsx` | Four statuses, reason, evidence references. | FR7, NFR6 | Alpha | | |
| `web/src/lib/format.ts` | Formatting for rates, dates and uncertainty. | NFR6 | Alpha | | |
| `web/src/main.tsx` | Entry point: mounts the app with router and query client. | FR6 | Alpha | | |
| `web/src/pages/Admin.tsx` | Page: Users, roles and model metrics. | FR5, FR2 | Alpha | | |
| `web/src/pages/DetectionDetail.tsx` | Page: Mask, enhancement, wind, past scenes for one detection. | FR6, FR7 | Alpha | | |
| `web/src/pages/Dossier.tsx` | Page: Build, download and verify an evidence dossier. | FR6, NFR2 | Alpha | | |
| `web/src/pages/Login.tsx` | Page: Sign-in page. | FR5 | Alpha | | |
| `web/src/pages/MapReview.tsx` | Page: Map and review queue: ranked candidates beside the map. | FR6 | Alpha | | |
| `web/src/pages/Regions.tsx` | Page: Draw a region and choose alert cadence. | FR1, FR4 | Beta scaffold | | |
| `web/src/pages/SiteHistory.tsx` | Page: All passes over one site. | FR6 | Alpha | | |

## Chau

| File | Purpose | Requirements | Stage | Backlog | Jira |
|---|---|---|---|---|---|
| `src/methanewatch/adapters/era5/era5_wind.py` | WindProvider reading ERA5 or ERA5T through the CDS API with a file cache. | FR3 | Alpha | | |
| `src/methanewatch/adapters/local/geojson_facilities.py` | FacilityIndex over a GeoJSON or Parquet file. | FR3 | Alpha | | |
| `src/methanewatch/attribution/geometry.py` | Distance and upwind tests between plume polygons and facility locations. | FR3 | Alpha | | |
| `src/methanewatch/attribution/match.py` | Rank plausible sources; return Match or Unresolved. | FR3 | Alpha | | |
| `src/methanewatch/data/augment.py` | Flips, rotations and radiometric jitter applied identically to all slices of a stack. | FR2 | Alpha | | |
| `src/methanewatch/inference/polygonise.py` | Raster components to georeferenced polygons. | FR2, FR6 | Alpha | | |
| `src/methanewatch/inference/postprocess.py` | Threshold, clean small blobs, find connected components. | FR2 | Alpha | | |
| `src/methanewatch/quantification/estimate.py` | Return Estimate, Unavailable or Uncertain; never a bare number. | FR3, FR7 | Alpha | | |
| `src/methanewatch/quantification/ime.py` | Integrated mass enhancement: Q = IME x U_eff / L. | FR3 | Alpha | | |
| `src/methanewatch/quantification/uncertainty.py` | Rate range from wind, mask and plume-length uncertainty; mark preliminary until final ERA5. | FR3 | Alpha | | |
| `src/methanewatch/quantification/wind.py` | Effective wind from ERA5 wind at the source location and time. | FR3 | Alpha | | |
| `src/methanewatch/verification/stage1_quality.py` | Stage 1: observation quality (cloud, invalid pixels, alignment, suitability of references). | FR7 | Alpha | | |
| `tests/unit/attribution/test_unresolved.py` | Several candidates or none give Unresolved. | FR3 | Alpha | | |
| `tests/unit/quantification/test_ime.py` | Q = IME x U_eff / L on a synthetic plume with a known rate; unit checks. | FR3 | Alpha | | |
| `tests/unit/quantification/test_unavailable.py` | Missing or implausible wind yields Unavailable with a reason. | FR3, FR7 | Alpha | | |

## Lam

| File | Purpose | Requirements | Stage | Backlog | Jira |
|---|---|---|---|---|---|
| `configs/data/synthetic.yaml` | Recipe settings: sampling weight, Q range 500 to 20,000 kg/h, rotation jitter 15 degrees, negatives 30 percent, label threshold 150 ppb. | FR2 | Alpha | | |
| `src/methanewatch/data/synthetic/injection.py` | Beer-Lambert injection of a plume into B11 and B12, with air-mass factor and elevation pressure factor. | FR2, FR3 | Alpha | | |
| `src/methanewatch/data/synthetic/labels.py` | Mask where delta XCH4 exceeds 150 ppb; keep the continuous map as a second target. | FR2 | Alpha | | |
| `src/methanewatch/data/synthetic/plume_bank.py` | Index of simulated plumes and nearest match by wind speed, solar zenith and relative azimuth. | FR2 | Alpha | | |
| `src/methanewatch/data/synthetic/recipes.py` | Deterministic recipes (ids, rotation, rate, negatives) stored as parquet and rebuilt on the fly. | FR2, NFR5 | Alpha | | |
| `src/methanewatch/data/synthetic/sampling.py` | Location-balanced target sampling with weight 1/sqrt(targets per location); choose up to 6 references. | FR2 | Alpha | | |
| `src/methanewatch/verification/stage3_plausibility.py` | Stage 3: plume shape and orientation against wind and nearby sources (supporting, not proof). | FR7 | Alpha | | |
| `tests/unit/data/test_injection_physics.py` | Injected absorption matches the calibrated doubling sensitivities for S2A and S2B. | FR2 | Alpha | | |
| `tests/unit/data/test_recipe_determinism.py` | The same recipe rebuilds the same sample on any machine. | FR2, NFR5 | Alpha | | |

## Backlog item to Jira key map (from the report)

PB-01: 23, 24, 25. PB-02: 27, 30. PB-03: 26. PB-04: 43. PB-05: 29. PB-06: 28, 44. PB-07: 45 to 48. PB-08: 36, 37. PB-09: 38. PB-10: 39. PB-11: 49. PB-12: 31. PB-13: 32. PB-14: 40, 41. PB-16: 50. PB-17: 51. PB-18: 52. PB-19: 53. PB-20: 54. PB-21: 55. PB-22: 56. PB-23: 57. PB-24: 12. PB-26: 58. PB-27: 59. PB-28: 60. PB-29: 61. PB-30: 62. PB-31: 63. PB-33: 64. All keys are written MWPMWP-n.

Report inconsistencies to settle with the advisor: PB-22 is Must in Table 6.1 but Should in Section 7.2.3; PB-18 is Must in one place and Should in another (Section 7.2.2); PB-32 and PB-33 share Jira key MWPMWP-64; the backlog source list names FR1 to FR6 although FR7 exists.
