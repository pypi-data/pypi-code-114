import os

import boto3

AUTODL_S3_REGION = "us-east-1"

# TODO - we need to somehow include these in CLI without hardcoding
# AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
# AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_ACCESS_KEY_ID = "AKIASO72NKUYW7ONNRFO"
AWS_SECRET_ACCESS_KEY = "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"


def init_s3(s3_host):
    return boto3.resource(
        "s3",
        region_name=AUTODL_S3_REGION,
        endpoint_url=s3_host,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )


S3 = init_s3(os.environ.get("AWS_S3_ENDPOINT"))
