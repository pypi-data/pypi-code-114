import enum
import boto3
import os
class Environment(enum.Enum):
    localhost = {
        'host': "http://localhost",
        's3_host': 'http://localhost:4566',
        's3_bucket_name': 'predictor-bucket',
    }
    staging = {
        'host': "http://54.83.236.20",
        's3_host': 'https://autodl-staging.s3-accelerate.amazonaws.com',
        's3_bucket_name': 'autodl-staging',
    }
    production = {
        'host': "https://autodl.autumn8.ai",
        's3_host': 'https://autodl-staging.s3-accelerate.amazonaws.com',
        's3_bucket_name': 'autodl-production',
    }

environment = Environment.production
if os.environ.get('TARGET_ENV_MODE') == 'staging':
    environment = Environment.staging
if os.environ.get('TARGET_ENV_MODE') == 'development':
    environment = Environment.localhost

autodl_host = environment.value['host']
s3_host = environment.value['s3_host']
s3_bucket_name = environment.value['s3_bucket_name']


AUTODL_S3_REGION = 'us-east-1'

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

def init_s3():
    return boto3.resource('s3',
        region_name=AUTODL_S3_REGION,
        endpoint_url=s3_host,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

s3 = init_s3()
