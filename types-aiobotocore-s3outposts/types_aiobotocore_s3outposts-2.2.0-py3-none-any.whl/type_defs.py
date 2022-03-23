"""
Type annotations for s3outposts service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3outposts/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_s3outposts.type_defs import CreateEndpointRequestRequestTypeDef

    data: CreateEndpointRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from typing_extensions import NotRequired

from .literals import EndpointAccessTypeType, EndpointStatusType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateEndpointRequestRequestTypeDef",
    "CreateEndpointResultTypeDef",
    "DeleteEndpointRequestRequestTypeDef",
    "EndpointTypeDef",
    "ListEndpointsRequestRequestTypeDef",
    "ListEndpointsResultTypeDef",
    "ListSharedEndpointsRequestRequestTypeDef",
    "ListSharedEndpointsResultTypeDef",
    "NetworkInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
)

CreateEndpointRequestRequestTypeDef = TypedDict(
    "CreateEndpointRequestRequestTypeDef",
    {
        "OutpostId": str,
        "SubnetId": str,
        "SecurityGroupId": str,
        "AccessType": NotRequired[EndpointAccessTypeType],
        "CustomerOwnedIpv4Pool": NotRequired[str],
    },
)

CreateEndpointResultTypeDef = TypedDict(
    "CreateEndpointResultTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEndpointRequestRequestTypeDef = TypedDict(
    "DeleteEndpointRequestRequestTypeDef",
    {
        "EndpointId": str,
        "OutpostId": str,
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "EndpointArn": NotRequired[str],
        "OutpostsId": NotRequired[str],
        "CidrBlock": NotRequired[str],
        "Status": NotRequired[EndpointStatusType],
        "CreationTime": NotRequired[datetime],
        "NetworkInterfaces": NotRequired[List["NetworkInterfaceTypeDef"]],
        "VpcId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "SecurityGroupId": NotRequired[str],
        "AccessType": NotRequired[EndpointAccessTypeType],
        "CustomerOwnedIpv4Pool": NotRequired[str],
    },
)

ListEndpointsRequestRequestTypeDef = TypedDict(
    "ListEndpointsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListEndpointsResultTypeDef = TypedDict(
    "ListEndpointsResultTypeDef",
    {
        "Endpoints": List["EndpointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSharedEndpointsRequestRequestTypeDef = TypedDict(
    "ListSharedEndpointsRequestRequestTypeDef",
    {
        "OutpostId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListSharedEndpointsResultTypeDef = TypedDict(
    "ListSharedEndpointsResultTypeDef",
    {
        "Endpoints": List["EndpointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "NetworkInterfaceId": NotRequired[str],
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
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
