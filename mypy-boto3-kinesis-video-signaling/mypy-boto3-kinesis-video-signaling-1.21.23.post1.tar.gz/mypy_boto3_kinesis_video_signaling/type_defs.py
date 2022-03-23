"""
Type annotations for kinesis-video-signaling service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_signaling/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesis_video_signaling.type_defs import GetIceServerConfigRequestRequestTypeDef

    data: GetIceServerConfigRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from typing_extensions import NotRequired

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "GetIceServerConfigRequestRequestTypeDef",
    "GetIceServerConfigResponseTypeDef",
    "IceServerTypeDef",
    "ResponseMetadataTypeDef",
    "SendAlexaOfferToMasterRequestRequestTypeDef",
    "SendAlexaOfferToMasterResponseTypeDef",
)

GetIceServerConfigRequestRequestTypeDef = TypedDict(
    "GetIceServerConfigRequestRequestTypeDef",
    {
        "ChannelARN": str,
        "ClientId": NotRequired[str],
        "Service": NotRequired[Literal["TURN"]],
        "Username": NotRequired[str],
    },
)

GetIceServerConfigResponseTypeDef = TypedDict(
    "GetIceServerConfigResponseTypeDef",
    {
        "IceServerList": List["IceServerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IceServerTypeDef = TypedDict(
    "IceServerTypeDef",
    {
        "Uris": NotRequired[List[str]],
        "Username": NotRequired[str],
        "Password": NotRequired[str],
        "Ttl": NotRequired[int],
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

SendAlexaOfferToMasterRequestRequestTypeDef = TypedDict(
    "SendAlexaOfferToMasterRequestRequestTypeDef",
    {
        "ChannelARN": str,
        "SenderClientId": str,
        "MessagePayload": str,
    },
)

SendAlexaOfferToMasterResponseTypeDef = TypedDict(
    "SendAlexaOfferToMasterResponseTypeDef",
    {
        "Answer": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
