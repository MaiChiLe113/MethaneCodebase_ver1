# infra/terraform

Beta scaffold. Four modules, one reason to change each: data_pipeline (serverless ingestion and detection), mlops (training storage and registry), web_app (EC2, load balancer, DynamoDB), security (identity, keys, write-once evidence bucket, logging). Everything here must be destroyable in one command so the $200 credit lasts; set a budget alarm in variables.tf first.
