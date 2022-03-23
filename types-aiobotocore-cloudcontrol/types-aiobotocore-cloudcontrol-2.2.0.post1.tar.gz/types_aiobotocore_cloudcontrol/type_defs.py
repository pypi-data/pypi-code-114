"""
Type annotations for cloudcontrol service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_cloudcontrol/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_cloudcontrol.type_defs import CancelResourceRequestInputRequestTypeDef

    data: CancelResourceRequestInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import HandlerErrorCodeType, OperationStatusType, OperationType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CancelResourceRequestInputRequestTypeDef",
    "CancelResourceRequestOutputTypeDef",
    "CreateResourceInputRequestTypeDef",
    "CreateResourceOutputTypeDef",
    "DeleteResourceInputRequestTypeDef",
    "DeleteResourceOutputTypeDef",
    "GetResourceInputRequestTypeDef",
    "GetResourceOutputTypeDef",
    "GetResourceRequestStatusInputRequestTypeDef",
    "GetResourceRequestStatusOutputTypeDef",
    "ListResourceRequestsInputRequestTypeDef",
    "ListResourceRequestsOutputTypeDef",
    "ListResourcesInputRequestTypeDef",
    "ListResourcesOutputTypeDef",
    "ProgressEventTypeDef",
    "ResourceDescriptionTypeDef",
    "ResourceRequestStatusFilterTypeDef",
    "ResponseMetadataTypeDef",
    "UpdateResourceInputRequestTypeDef",
    "UpdateResourceOutputTypeDef",
    "WaiterConfigTypeDef",
)

CancelResourceRequestInputRequestTypeDef = TypedDict(
    "CancelResourceRequestInputRequestTypeDef",
    {
        "RequestToken": str,
    },
)

CancelResourceRequestOutputTypeDef = TypedDict(
    "CancelResourceRequestOutputTypeDef",
    {
        "ProgressEvent": "ProgressEventTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResourceInputRequestTypeDef = TypedDict(
    "CreateResourceInputRequestTypeDef",
    {
        "TypeName": str,
        "DesiredState": str,
        "TypeVersionId": NotRequired[str],
        "RoleArn": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)

CreateResourceOutputTypeDef = TypedDict(
    "CreateResourceOutputTypeDef",
    {
        "ProgressEvent": "ProgressEventTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourceInputRequestTypeDef = TypedDict(
    "DeleteResourceInputRequestTypeDef",
    {
        "TypeName": str,
        "Identifier": str,
        "TypeVersionId": NotRequired[str],
        "RoleArn": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)

DeleteResourceOutputTypeDef = TypedDict(
    "DeleteResourceOutputTypeDef",
    {
        "ProgressEvent": "ProgressEventTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceInputRequestTypeDef = TypedDict(
    "GetResourceInputRequestTypeDef",
    {
        "TypeName": str,
        "Identifier": str,
        "TypeVersionId": NotRequired[str],
        "RoleArn": NotRequired[str],
    },
)

GetResourceOutputTypeDef = TypedDict(
    "GetResourceOutputTypeDef",
    {
        "TypeName": str,
        "ResourceDescription": "ResourceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceRequestStatusInputRequestTypeDef = TypedDict(
    "GetResourceRequestStatusInputRequestTypeDef",
    {
        "RequestToken": str,
    },
)

GetResourceRequestStatusOutputTypeDef = TypedDict(
    "GetResourceRequestStatusOutputTypeDef",
    {
        "ProgressEvent": "ProgressEventTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceRequestsInputRequestTypeDef = TypedDict(
    "ListResourceRequestsInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ResourceRequestStatusFilter": NotRequired["ResourceRequestStatusFilterTypeDef"],
    },
)

ListResourceRequestsOutputTypeDef = TypedDict(
    "ListResourceRequestsOutputTypeDef",
    {
        "ResourceRequestStatusSummaries": List["ProgressEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourcesInputRequestTypeDef = TypedDict(
    "ListResourcesInputRequestTypeDef",
    {
        "TypeName": str,
        "TypeVersionId": NotRequired[str],
        "RoleArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ResourceModel": NotRequired[str],
    },
)

ListResourcesOutputTypeDef = TypedDict(
    "ListResourcesOutputTypeDef",
    {
        "TypeName": str,
        "ResourceDescriptions": List["ResourceDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ProgressEventTypeDef = TypedDict(
    "ProgressEventTypeDef",
    {
        "TypeName": NotRequired[str],
        "Identifier": NotRequired[str],
        "RequestToken": NotRequired[str],
        "Operation": NotRequired[OperationType],
        "OperationStatus": NotRequired[OperationStatusType],
        "EventTime": NotRequired[datetime],
        "ResourceModel": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "ErrorCode": NotRequired[HandlerErrorCodeType],
        "RetryAfter": NotRequired[datetime],
    },
)

ResourceDescriptionTypeDef = TypedDict(
    "ResourceDescriptionTypeDef",
    {
        "Identifier": NotRequired[str],
        "Properties": NotRequired[str],
    },
)

ResourceRequestStatusFilterTypeDef = TypedDict(
    "ResourceRequestStatusFilterTypeDef",
    {
        "Operations": NotRequired[Sequence[OperationType]],
        "OperationStatuses": NotRequired[Sequence[OperationStatusType]],
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

UpdateResourceInputRequestTypeDef = TypedDict(
    "UpdateResourceInputRequestTypeDef",
    {
        "TypeName": str,
        "Identifier": str,
        "PatchDocument": str,
        "TypeVersionId": NotRequired[str],
        "RoleArn": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)

UpdateResourceOutputTypeDef = TypedDict(
    "UpdateResourceOutputTypeDef",
    {
        "ProgressEvent": "ProgressEventTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
