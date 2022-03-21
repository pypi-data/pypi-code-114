import boto3
import os
from .settings import Environment


environment = Environment.production

if os.environ.get('TARGET_ENV_MODE') == 'staging':
    environment = Environment.staging
if os.environ.get('TARGET_ENV_MODE') == 'development':
    environment = Environment.localhost

autodl_host = environment.value['host']
s3_host = environment.value['s3_host']
s3_bucket_name = environment.value['s3_bucket_name']

AUTODL_S3_REGION = 'us-east-1'

# TODO - we need to somehow include these in CLI without hardcoding
# AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
# AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

AWS_ACCESS_KEY_ID = 'AKIASO72NKUYW7ONNRFO'
AWS_SECRET_ACCESS_KEY = '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'

def init_s3():
    return boto3.resource('s3',
        region_name=AUTODL_S3_REGION,
        endpoint_url=s3_host,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

s3 = init_s3()

def use_environment(new_environment):
    global autodl_host, environment, s3_host, s3_bucket_name, s3
    environment = new_environment

    autodl_host = environment.value['host']
    s3_host = environment.value['s3_host']
    s3_bucket_name = environment.value['s3_bucket_name']
    s3 = init_s3()
