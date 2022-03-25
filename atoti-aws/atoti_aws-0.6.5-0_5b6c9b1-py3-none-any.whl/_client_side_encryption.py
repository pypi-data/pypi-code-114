from atoti_core import deprecated

from .client_side_encryption import AwsKeyPair, AwsKmsConfig


def create_aws_kms_config(*, region: str, key_id: str) -> AwsKmsConfig:
    deprecated("`create_aws_kms_config()` is deprecated, use `AwsKmsConfig()` instead.")
    return AwsKmsConfig(region=region, key_id=key_id)


def create_aws_key_pair(
    *, region: str, private_key: str, public_key: str
) -> AwsKeyPair:
    deprecated("`create_aws_key_pair()` is deprecated, use `AwsKeyPair()` instead.")
    return AwsKeyPair(region=region, public_key=public_key, private_key=private_key)
