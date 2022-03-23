"""
Type annotations for kinesis-video-media service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_media/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesis_video_media.type_defs import GetMediaInputRequestTypeDef

    data: GetMediaInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import StartSelectorTypeType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "GetMediaInputRequestTypeDef",
    "GetMediaOutputTypeDef",
    "ResponseMetadataTypeDef",
    "StartSelectorTypeDef",
)

GetMediaInputRequestTypeDef = TypedDict(
    "GetMediaInputRequestTypeDef",
    {
        "StartSelector": "StartSelectorTypeDef",
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)

GetMediaOutputTypeDef = TypedDict(
    "GetMediaOutputTypeDef",
    {
        "ContentType": str,
        "Payload": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)

StartSelectorTypeDef = TypedDict(
    "StartSelectorTypeDef",
    {
        "StartSelectorType": StartSelectorTypeType,
        "AfterFragmentNumber": NotRequired[str],
        "StartTimestamp": NotRequired[Union[datetime, str]],
        "ContinuationToken": NotRequired[str],
    },
)
