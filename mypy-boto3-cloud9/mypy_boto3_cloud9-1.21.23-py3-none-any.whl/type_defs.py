"""
Type annotations for cloud9 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloud9.type_defs import CreateEnvironmentEC2RequestRequestTypeDef

    data: CreateEnvironmentEC2RequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    ConnectionTypeType,
    EnvironmentLifecycleStatusType,
    EnvironmentStatusType,
    EnvironmentTypeType,
    ManagedCredentialsActionType,
    ManagedCredentialsStatusType,
    MemberPermissionsType,
    PermissionsType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateEnvironmentEC2RequestRequestTypeDef",
    "CreateEnvironmentEC2ResultTypeDef",
    "CreateEnvironmentMembershipRequestRequestTypeDef",
    "CreateEnvironmentMembershipResultTypeDef",
    "DeleteEnvironmentMembershipRequestRequestTypeDef",
    "DeleteEnvironmentRequestRequestTypeDef",
    "DescribeEnvironmentMembershipsRequestRequestTypeDef",
    "DescribeEnvironmentMembershipsResultTypeDef",
    "DescribeEnvironmentStatusRequestRequestTypeDef",
    "DescribeEnvironmentStatusResultTypeDef",
    "DescribeEnvironmentsRequestRequestTypeDef",
    "DescribeEnvironmentsResultTypeDef",
    "EnvironmentLifecycleTypeDef",
    "EnvironmentMemberTypeDef",
    "EnvironmentTypeDef",
    "ListEnvironmentsRequestRequestTypeDef",
    "ListEnvironmentsResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateEnvironmentMembershipRequestRequestTypeDef",
    "UpdateEnvironmentMembershipResultTypeDef",
    "UpdateEnvironmentRequestRequestTypeDef",
)

CreateEnvironmentEC2RequestRequestTypeDef = TypedDict(
    "CreateEnvironmentEC2RequestRequestTypeDef",
    {
        "name": str,
        "instanceType": str,
        "description": NotRequired[str],
        "clientRequestToken": NotRequired[str],
        "subnetId": NotRequired[str],
        "imageId": NotRequired[str],
        "automaticStopTimeMinutes": NotRequired[int],
        "ownerArn": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "connectionType": NotRequired[ConnectionTypeType],
        "dryRun": NotRequired[bool],
    },
)

CreateEnvironmentEC2ResultTypeDef = TypedDict(
    "CreateEnvironmentEC2ResultTypeDef",
    {
        "environmentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEnvironmentMembershipRequestRequestTypeDef = TypedDict(
    "CreateEnvironmentMembershipRequestRequestTypeDef",
    {
        "environmentId": str,
        "userArn": str,
        "permissions": MemberPermissionsType,
    },
)

CreateEnvironmentMembershipResultTypeDef = TypedDict(
    "CreateEnvironmentMembershipResultTypeDef",
    {
        "membership": "EnvironmentMemberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentMembershipRequestRequestTypeDef = TypedDict(
    "DeleteEnvironmentMembershipRequestRequestTypeDef",
    {
        "environmentId": str,
        "userArn": str,
    },
)

DeleteEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteEnvironmentRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)

DescribeEnvironmentMembershipsRequestRequestTypeDef = TypedDict(
    "DescribeEnvironmentMembershipsRequestRequestTypeDef",
    {
        "userArn": NotRequired[str],
        "environmentId": NotRequired[str],
        "permissions": NotRequired[Sequence[PermissionsType]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

DescribeEnvironmentMembershipsResultTypeDef = TypedDict(
    "DescribeEnvironmentMembershipsResultTypeDef",
    {
        "memberships": List["EnvironmentMemberTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEnvironmentStatusRequestRequestTypeDef = TypedDict(
    "DescribeEnvironmentStatusRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)

DescribeEnvironmentStatusResultTypeDef = TypedDict(
    "DescribeEnvironmentStatusResultTypeDef",
    {
        "status": EnvironmentStatusType,
        "message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEnvironmentsRequestRequestTypeDef = TypedDict(
    "DescribeEnvironmentsRequestRequestTypeDef",
    {
        "environmentIds": Sequence[str],
    },
)

DescribeEnvironmentsResultTypeDef = TypedDict(
    "DescribeEnvironmentsResultTypeDef",
    {
        "environments": List["EnvironmentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentLifecycleTypeDef = TypedDict(
    "EnvironmentLifecycleTypeDef",
    {
        "status": NotRequired[EnvironmentLifecycleStatusType],
        "reason": NotRequired[str],
        "failureResource": NotRequired[str],
    },
)

EnvironmentMemberTypeDef = TypedDict(
    "EnvironmentMemberTypeDef",
    {
        "permissions": PermissionsType,
        "userId": str,
        "userArn": str,
        "environmentId": str,
        "lastAccess": NotRequired[datetime],
    },
)

EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "type": EnvironmentTypeType,
        "arn": str,
        "ownerArn": str,
        "id": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "connectionType": NotRequired[ConnectionTypeType],
        "lifecycle": NotRequired["EnvironmentLifecycleTypeDef"],
        "managedCredentialsStatus": NotRequired[ManagedCredentialsStatusType],
    },
)

ListEnvironmentsRequestRequestTypeDef = TypedDict(
    "ListEnvironmentsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListEnvironmentsResultTypeDef = TypedDict(
    "ListEnvironmentsResultTypeDef",
    {
        "nextToken": str,
        "environmentIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateEnvironmentMembershipRequestRequestTypeDef = TypedDict(
    "UpdateEnvironmentMembershipRequestRequestTypeDef",
    {
        "environmentId": str,
        "userArn": str,
        "permissions": MemberPermissionsType,
    },
)

UpdateEnvironmentMembershipResultTypeDef = TypedDict(
    "UpdateEnvironmentMembershipResultTypeDef",
    {
        "membership": "EnvironmentMemberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEnvironmentRequestRequestTypeDef = TypedDict(
    "UpdateEnvironmentRequestRequestTypeDef",
    {
        "environmentId": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "managedCredentialsAction": NotRequired[ManagedCredentialsActionType],
    },
)
