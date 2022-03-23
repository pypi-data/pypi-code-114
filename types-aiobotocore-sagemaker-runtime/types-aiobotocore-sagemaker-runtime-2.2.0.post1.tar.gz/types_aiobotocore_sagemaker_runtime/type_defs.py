"""
Type annotations for sagemaker-runtime service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_runtime/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_sagemaker_runtime.type_defs import InvokeEndpointAsyncInputRequestTypeDef

    data: InvokeEndpointAsyncInputRequestTypeDef = {...}
    ```
"""
import sys
from typing import IO, Dict, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "InvokeEndpointAsyncInputRequestTypeDef",
    "InvokeEndpointAsyncOutputTypeDef",
    "InvokeEndpointInputRequestTypeDef",
    "InvokeEndpointOutputTypeDef",
    "ResponseMetadataTypeDef",
)

InvokeEndpointAsyncInputRequestTypeDef = TypedDict(
    "InvokeEndpointAsyncInputRequestTypeDef",
    {
        "EndpointName": str,
        "InputLocation": str,
        "ContentType": NotRequired[str],
        "Accept": NotRequired[str],
        "CustomAttributes": NotRequired[str],
        "InferenceId": NotRequired[str],
        "RequestTTLSeconds": NotRequired[int],
    },
)

InvokeEndpointAsyncOutputTypeDef = TypedDict(
    "InvokeEndpointAsyncOutputTypeDef",
    {
        "InferenceId": str,
        "OutputLocation": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InvokeEndpointInputRequestTypeDef = TypedDict(
    "InvokeEndpointInputRequestTypeDef",
    {
        "EndpointName": str,
        "Body": Union[bytes, IO[bytes], StreamingBody],
        "ContentType": NotRequired[str],
        "Accept": NotRequired[str],
        "CustomAttributes": NotRequired[str],
        "TargetModel": NotRequired[str],
        "TargetVariant": NotRequired[str],
        "TargetContainerHostname": NotRequired[str],
        "InferenceId": NotRequired[str],
    },
)

InvokeEndpointOutputTypeDef = TypedDict(
    "InvokeEndpointOutputTypeDef",
    {
        "Body": StreamingBody,
        "ContentType": str,
        "InvokedProductionVariant": str,
        "CustomAttributes": str,
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
