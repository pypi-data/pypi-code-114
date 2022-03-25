"""Plugin to load CSV and Parquet files from AWS S3 into atoti tables.

This package is required to load files with paths starting with ``s3://``.

Authentication is handled by the underlying AWS SDK for Java library.
Refer to their `documentation <https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html#setup-credentials-setting>`__  for the available options.
"""

from ._client_side_encryption import *
from .client_side_encryption import (
    AwsKeyPair as AwsKeyPair,
    AwsKmsConfig as AwsKmsConfig,
)
