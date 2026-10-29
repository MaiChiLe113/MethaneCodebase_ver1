# ADR 0009: DynamoDB and S3, LocalStack first

Status: Proposed. Confirm at the first sprint review, then change to Accepted.

## Context

The report fixes DynamoDB on demand (D12) and a serverless pipeline with an EC2 web app (D13) within a $200 AWS credit.

## Decision

Repositories on DynamoDB, files on S3. Development and CI run the same adapters against LocalStack; unit tests use in-memory fakes. Key design is a proposal to confirm with a spike.

## Consequences

Cloud spend only for the Beta demonstration. Cost: LocalStack differs from AWS in corners (for example Object Lock), so a few tests are marked integration and run on demand.

## Related

diagrams/05-data/er-model, diagrams/01-containers/deployment-aws
