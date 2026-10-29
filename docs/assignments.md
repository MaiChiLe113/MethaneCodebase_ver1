# Who owns which folders and files

Proposed assignments, from the roles in report Table 1.3. Confirm and rebalance at sprint planning, then record the final names in the pull request that changes this file. For the purpose and requirements of each file see `work-breakdown.md`; the header inside each file says the same.

Rules: one owner per file; the owner writes the code and its test and is the first reviewer of changes to it; someone else reviews the owner's own changes. Files an owner shares a folder with are listed under the folder, so nothing is orphaned.

## Chi (68 files)

Lead architect and data engineer: architecture, data pipeline, domain/ports/adapters pattern, MLOps and infrastructure, configs, U-Net and classical baselines, inference, docs, ADRs and diagrams.

- repository root: `docker-compose.yml`, `dvc.yaml`
- `configs/data/`: `s2.yaml`, `splits.yaml`
- `configs/model/`: `classical.yaml`, `unet.yaml`
- `infra/terraform/`: `main.tf`, `outputs.tf`, `variables.tf`
- `infra/terraform/modules/data_pipeline/`: `main.tf`
- `infra/terraform/modules/mlops/`: `main.tf`
- `scripts/`: `build_work_breakdown.py`, `seed_demo_data.py`
- `src/methanewatch/adapters/aws/`: `dynamodb_repositories.py`, `s3_object_store.py`
- `src/methanewatch/adapters/local/`: `fs_object_store.py`, `mlflow_registry.py`
- `src/methanewatch/adapters/memory/`: `fakes.py`
- `src/methanewatch/adapters/stac/`: `stac_scene_source.py`
- `src/methanewatch/api/`: `deps.py`
- `src/methanewatch/cli/`: `main.py`
- `src/methanewatch/core/`: `clock.py`, `config.py`, `errors.py`, `ids.py`, `logging.py`, `units.py`
- `src/methanewatch/data/`: `dataset.py`, `ingest.py`, `loader.py`, `manifest.py`, `preprocess.py`, `schema.py`, `splits.py`, `stack.py`, `tiling.py`
- `src/methanewatch/domain/`: `entities.py`, `estimate.py`, `events.py`, `roles.py`, `status.py`, `value_objects.py`
- `src/methanewatch/inference/`: `candidates.py`, `pipeline.py`, `predictor.py`
- `src/methanewatch/models/classical/`: `threshold.py`
- `src/methanewatch/models/unet/`: `model.py`
- `src/methanewatch/ports/`: `audit_sink.py`, `auth_provider.py`, `detection_repository.py`, `evidence_store.py`, `facility_index.py`, `model_registry.py`, `object_store.py`, `region_repository.py`, `review_repository.py`, `scene_source.py`, `signer.py`, `user_repository.py`, `wind_provider.py`
- `src/methanewatch/workers/`: `detect_worker.py`, `ingest_worker.py`
- `tests/`: `conftest.py`
- `tests/integration/`: `test_dynamodb_localstack.py`
- `tests/unit/data/`: `test_splits_no_leak.py`, `test_tensor_contract.py`
- `tests/unit/domain/`: `test_estimate_types.py`, `test_status_rules.py`

## Hai (21 files)

Models and training research: Mamba family, ST-CM-UNet, trainer and losses; leads the benchmark.

- `configs/model/`: `cd_mamba.yaml`, `kmetha.yaml`, `st_cm_unet.yaml`, `vmamba.yaml`
- `configs/train/`: `pretrain.yaml`
- `docker/`: `trainer.Dockerfile`
- `src/methanewatch/models/`: `base.py`, `registry.py`
- `src/methanewatch/models/mamba/`: `cd_mamba.py`, `kmetha.py`, `scan_fallback.py`, `vmamba.py`
- `src/methanewatch/models/st_cm_unet/`: `model.py`
- `src/methanewatch/training/`: `callbacks.py`, `losses.py`, `optim.py`, `pretrain.py`, `seed.py`, `trainer.py`
- `tests/ml/`: `test_model_zoo_shapes.py`, `test_overfit_tiny_batch.py`

## Ha (30 files)

Security, evaluation and fine-tuning: metrics and benchmark, ViT-UNet and SAM4CH4, fine-tuning, MBMP and verification stage 2, evidence hashing, provenance and signing.

- `configs/eval/`: `benchmark.yaml`
- `configs/model/`: `sam4ch4.yaml`, `vit_unet.yaml`
- `configs/train/`: `finetune.yaml`
- `infra/terraform/modules/security/`: `main.tf`
- `src/methanewatch/adapters/aws/`: `dynamodb_audit_sink.py`, `s3_evidence_store.py`
- `src/methanewatch/adapters/local/`: `ed25519_signer.py`
- `src/methanewatch/evaluation/`: `benchmark.py`, `error_analysis.py`, `gates.py`, `metrics.py`, `report.py`
- `src/methanewatch/evidence/`: `audit_chain.py`, `hashing.py`, `provenance.py`, `signing.py`, `verify.py`
- `src/methanewatch/models/sam4ch4/`: `model.py`
- `src/methanewatch/models/vit_unet/`: `model.py`
- `src/methanewatch/training/`: `finetune.py`
- `src/methanewatch/verification/`: `mbmp.py`, `stage2_consistency.py`, `status.py`
- `tests/integration/`: `test_s3_object_lock.py`
- `tests/unit/evaluation/`: `test_metrics.py`, `test_release_gate.py`
- `tests/unit/evidence/`: `test_audit_chain.py`, `test_tamper_detected.py`
- `tests/unit/verification/`: `test_stages.py`

## Nam (58 files)

Delivery: API, RBAC, audit, services, Docker and CI, web portal, dossier PDF.

- `.github/workflows/`: `ci.yml`
- `docker/`: `api.Dockerfile`, `web.Dockerfile`
- `infra/terraform/modules/web_app/`: `main.tf`
- `scripts/`: `export_openapi.py`, `gen_ts_client.sh`
- `src/methanewatch/adapters/aws/`: `cognito_auth.py`
- `src/methanewatch/adapters/local/`: `jwt_auth.py`
- `src/methanewatch/api/`: `audit.py`, `auth.py`, `errors.py`, `main.py`, `rbac.py`, `schemas.py`
- `src/methanewatch/api/routers/`: `admin.py`, `detections.py`, `evidence.py`, `layers.py`, `regions.py`, `review.py`
- `src/methanewatch/evidence/`: `dossier.py`
- `src/methanewatch/services/`: `configure_region.py`, `export_dossier.py`, `promote_model.py`, `query_detections.py`, `review_detection.py`, `run_detection.py`, `verify_dossier.py`
- `src/methanewatch/workers/`: `alert_worker.py`
- `tests/integration/`: `test_api_end_to_end.py`
- `tests/unit/api/`: `test_permission_matrix.py`, `test_token_guard.py`
- `tests/unit/services/`: `test_export_requires_supported.py`, `test_review_append_only.py`
- `web/e2e/`: `permissions.spec.ts`, `review-flow.spec.ts`
- `web/src/`: `main.tsx`
- `web/src/api/`: `client.ts`
- `web/src/app/`: `App.tsx`, `auth.tsx`, `queryClient.ts`, `router.tsx`
- `web/src/components/`: `EmptyState.tsx`, `StatusBadge.tsx`, `UncertaintyBar.tsx`
- `web/src/features/access/`: `RoleGuard.tsx`
- `web/src/features/evidence/`: `DossierCard.tsx`
- `web/src/features/map/`: `MapView.tsx`
- `web/src/features/regions/`: `RegionEditor.tsx`
- `web/src/features/review/`: `ReviewPanel.tsx`
- `web/src/lib/`: `format.ts`
- `web/src/pages/`: `Admin.tsx`, `DetectionDetail.tsx`, `Dossier.tsx`, `Login.tsx`, `MapReview.tsx`, `Regions.tsx`, `SiteHistory.tsx`

## Chau (15 files)

Science: IME quantification, attribution, verification stage 1, polygonise, augmentation.

- `src/methanewatch/adapters/era5/`: `era5_wind.py`
- `src/methanewatch/adapters/local/`: `geojson_facilities.py`
- `src/methanewatch/attribution/`: `geometry.py`, `match.py`
- `src/methanewatch/data/`: `augment.py`
- `src/methanewatch/inference/`: `polygonise.py`, `postprocess.py`
- `src/methanewatch/quantification/`: `estimate.py`, `ime.py`, `uncertainty.py`, `wind.py`
- `src/methanewatch/verification/`: `stage1_quality.py`
- `tests/unit/attribution/`: `test_unresolved.py`
- `tests/unit/quantification/`: `test_ime.py`, `test_unavailable.py`

## Lam (9 files)

Physics and analysis: synthetic injection and recipes, verification stage 3 (plausibility), business analysis.

- `configs/data/`: `synthetic.yaml`
- `src/methanewatch/data/synthetic/`: `injection.py`, `labels.py`, `plume_bank.py`, `recipes.py`, `sampling.py`
- `src/methanewatch/verification/`: `stage3_plausibility.py`
- `tests/unit/data/`: `test_injection_physics.py`, `test_recipe_determinism.py`

## Files not in the placeholder list

- Chi: `README.md`, `CLAUDE.md`, `pyproject.toml`, `Makefile`, `.pre-commit-config.yaml`, `.gitignore`, `.env.example`, `docs/adr/`, `docs/requirements.md`, `docs/assignments.md`, `docs/work-breakdown.md`, `diagrams/`, `LICENSES.md`, `configs/release_gates.yaml`.
- Ha: `configs/permissions.yaml` (with Nam, who tests it).
- Nam: `.github/pull_request_template.md`, `web/package.json`, `web/README.md`.
- Model owners: `docs/model-card.md` (one section per model). Chi and Lam: `docs/dataset-card.md`. Chi and Nam: `docs/runbook.md`.

## Shared by everyone

Every member keeps `docs/work-breakdown.md` and the Jira key of each file current, and updates the diagram of any package they change (see `diagrams/06-mlops/change-workflow.pdf`).
