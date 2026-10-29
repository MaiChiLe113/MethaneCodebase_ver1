# MethaneWatch developer commands. Run `make help`.
.DEFAULT_GOAL := help
.PHONY: help setup lint contracts test test-ml web-install web-dev api up down diagrams clean

help:  ## list commands
	@grep -E '^[a-zA-Z_-]+:.*##' $(MAKEFILE_LIST) | sed 's/:.*##/\t/'

setup:  ## create the Python environment (uv) and install git hooks
	uv sync --extra dev --extra api --extra ml
	uv run pre-commit install

lint:  ## style and types
	uv run ruff check src tests
	uv run mypy src

contracts:  ## import rules from diagrams/01-containers/layers-and-dependencies
	uv run lint-imports

test:  ## fast tests, no cloud, no GPU
	uv run pytest -m "not integration and not ml"

test-ml:  ## model zoo shape and tiny-overfit tests (CPU is enough)
	uv run pytest tests/ml

web-install:  ## portal dependencies
	cd web && npm install

web-dev:  ## portal with hot reload
	cd web && npm run dev

api:  ## API on the local adapters
	uv run uvicorn methanewatch.api.main:create_app --factory --reload

up:  ## local stack: LocalStack, MLflow, API, web
	docker compose up -d

down:
	docker compose down

diagrams:  ## rebuild every diagram to PDF and SVG
	$(MAKE) -C diagrams

clean:
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
