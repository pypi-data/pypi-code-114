import gzip
import base64
import boto3
import json

from .settings import settings


client = boto3.client(
    'sns',
    region_name=settings.AWS_REGION,
    aws_access_key_id=settings.AWS_SNS_KEY,
    aws_secret_access_key=settings.AWS_SNS_SECRET,
)


def publish(topic, body=None, path=None, json_encoder=None, compression=None) -> None:
    message_raw, message = _make_message(body, compression, json_encoder, path)
    topic_arn = _make_topic_arn(topic)

    print('SNS publishing:', topic_arn, message_raw)
    resp = client.publish(
        TopicArn=topic_arn,
        Message=message,
        MessageStructure="json",
    )
    print('SNS response:', resp)


def _make_message(body, compression, json_encoder, path):
    message = {
        'body': body,
        'path': path,
    }
    message_raw = message = json.dumps(message, cls=json_encoder)
    if compression == 'gzip':
        message = _gzip_utf8_compress(message)
    message = json.dumps({"default": message})

    return message_raw, message


def _make_topic_arn(topic):
    env = 'dev' if settings.ENVIRONMENT == 'local' else settings.ENVIRONMENT
    topic_arn = f'{settings.AWS_SNS_PATH}{env}-{topic}'
    return topic_arn


def _gzip_utf8_compress(data):
    compressed_bytes = gzip.compress(bytes(data, 'utf-8'))
    compressed_string = base64.b64encode(compressed_bytes).decode('utf-8')
    return compressed_string
