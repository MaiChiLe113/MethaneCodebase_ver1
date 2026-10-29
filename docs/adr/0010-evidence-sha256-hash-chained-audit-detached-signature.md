# ADR 0010: Evidence: SHA-256, hash-chained audit, detached signature

Status: Proposed. Confirm at the first sprint review, then change to Accepted.

## Context

The report requires tamper evidence for results and an immutable audit log, and says integrity is not scientific correctness.

## Decision

Streamed SHA-256 per artefact in a manifest; PROV-style provenance; Ed25519 detached signature over the manifest; hash-chained audit entries; write-once storage (S3 Object Lock) in Beta. A test modifies a protected artefact and expects Tampered. Key custody for Beta is a separate ADR.

## Consequences

Tampering is detectable by anyone with the public key. Cost: key management becomes a real task.

## Related

diagrams/02-components/evidence-subsystem, diagrams/04-behaviour/seq-export-dossier
