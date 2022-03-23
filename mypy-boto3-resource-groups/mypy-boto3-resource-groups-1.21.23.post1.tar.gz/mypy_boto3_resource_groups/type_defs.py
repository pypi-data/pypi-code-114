"""
Type annotations for resource-groups service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/type_defs.html)

Usage::

    ```python
    from mypy_boto3_resource_groups.type_defs import CreateGroupInputRequestTypeDef

    data: CreateGroupInputRequestTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    GroupConfigurationStatusType,
    GroupFilterNameType,
    QueryErrorCodeType,
    QueryTypeType,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateGroupInputRequestTypeDef",
    "CreateGroupOutputTypeDef",
    "DeleteGroupInputRequestTypeDef",
    "DeleteGroupOutputTypeDef",
    "FailedResourceTypeDef",
    "GetGroupConfigurationInputRequestTypeDef",
    "GetGroupConfigurationOutputTypeDef",
    "GetGroupInputRequestTypeDef",
    "GetGroupOutputTypeDef",
    "GetGroupQueryInputRequestTypeDef",
    "GetGroupQueryOutputTypeDef",
    "GetTagsInputRequestTypeDef",
    "GetTagsOutputTypeDef",
    "GroupConfigurationItemTypeDef",
    "GroupConfigurationParameterTypeDef",
    "GroupConfigurationTypeDef",
    "GroupFilterTypeDef",
    "GroupIdentifierTypeDef",
    "GroupQueryTypeDef",
    "GroupResourcesInputRequestTypeDef",
    "GroupResourcesOutputTypeDef",
    "GroupTypeDef",
    "ListGroupResourcesInputRequestTypeDef",
    "ListGroupResourcesItemTypeDef",
    "ListGroupResourcesOutputTypeDef",
    "ListGroupsInputRequestTypeDef",
    "ListGroupsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PendingResourceTypeDef",
    "PutGroupConfigurationInputRequestTypeDef",
    "QueryErrorTypeDef",
    "ResourceFilterTypeDef",
    "ResourceIdentifierTypeDef",
    "ResourceQueryTypeDef",
    "ResourceStatusTypeDef",
    "ResponseMetadataTypeDef",
    "SearchResourcesInputRequestTypeDef",
    "SearchResourcesOutputTypeDef",
    "TagInputRequestTypeDef",
    "TagOutputTypeDef",
    "UngroupResourcesInputRequestTypeDef",
    "UngroupResourcesOutputTypeDef",
    "UntagInputRequestTypeDef",
    "UntagOutputTypeDef",
    "UpdateGroupInputRequestTypeDef",
    "UpdateGroupOutputTypeDef",
    "UpdateGroupQueryInputRequestTypeDef",
    "UpdateGroupQueryOutputTypeDef",
)

CreateGroupInputRequestTypeDef = TypedDict(
    "CreateGroupInputRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "ResourceQuery": NotRequired["ResourceQueryTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
        "Configuration": NotRequired[Sequence["GroupConfigurationItemTypeDef"]],
    },
)

CreateGroupOutputTypeDef = TypedDict(
    "CreateGroupOutputTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResourceQuery": "ResourceQueryTypeDef",
        "Tags": Dict[str, str],
        "GroupConfiguration": "GroupConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGroupInputRequestTypeDef = TypedDict(
    "DeleteGroupInputRequestTypeDef",
    {
        "GroupName": NotRequired[str],
        "Group": NotRequired[str],
    },
)

DeleteGroupOutputTypeDef = TypedDict(
    "DeleteGroupOutputTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailedResourceTypeDef = TypedDict(
    "FailedResourceTypeDef",
    {
        "ResourceArn": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "ErrorCode": NotRequired[str],
    },
)

GetGroupConfigurationInputRequestTypeDef = TypedDict(
    "GetGroupConfigurationInputRequestTypeDef",
    {
        "Group": NotRequired[str],
    },
)

GetGroupConfigurationOutputTypeDef = TypedDict(
    "GetGroupConfigurationOutputTypeDef",
    {
        "GroupConfiguration": "GroupConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupInputRequestTypeDef = TypedDict(
    "GetGroupInputRequestTypeDef",
    {
        "GroupName": NotRequired[str],
        "Group": NotRequired[str],
    },
)

GetGroupOutputTypeDef = TypedDict(
    "GetGroupOutputTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupQueryInputRequestTypeDef = TypedDict(
    "GetGroupQueryInputRequestTypeDef",
    {
        "GroupName": NotRequired[str],
        "Group": NotRequired[str],
    },
)

GetGroupQueryOutputTypeDef = TypedDict(
    "GetGroupQueryOutputTypeDef",
    {
        "GroupQuery": "GroupQueryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTagsInputRequestTypeDef = TypedDict(
    "GetTagsInputRequestTypeDef",
    {
        "Arn": str,
    },
)

GetTagsOutputTypeDef = TypedDict(
    "GetTagsOutputTypeDef",
    {
        "Arn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupConfigurationItemTypeDef = TypedDict(
    "GroupConfigurationItemTypeDef",
    {
        "Type": str,
        "Parameters": NotRequired[Sequence["GroupConfigurationParameterTypeDef"]],
    },
)

GroupConfigurationParameterTypeDef = TypedDict(
    "GroupConfigurationParameterTypeDef",
    {
        "Name": str,
        "Values": NotRequired[Sequence[str]],
    },
)

GroupConfigurationTypeDef = TypedDict(
    "GroupConfigurationTypeDef",
    {
        "Configuration": NotRequired[List["GroupConfigurationItemTypeDef"]],
        "ProposedConfiguration": NotRequired[List["GroupConfigurationItemTypeDef"]],
        "Status": NotRequired[GroupConfigurationStatusType],
        "FailureReason": NotRequired[str],
    },
)

GroupFilterTypeDef = TypedDict(
    "GroupFilterTypeDef",
    {
        "Name": GroupFilterNameType,
        "Values": Sequence[str],
    },
)

GroupIdentifierTypeDef = TypedDict(
    "GroupIdentifierTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupArn": NotRequired[str],
    },
)

GroupQueryTypeDef = TypedDict(
    "GroupQueryTypeDef",
    {
        "GroupName": str,
        "ResourceQuery": "ResourceQueryTypeDef",
    },
)

GroupResourcesInputRequestTypeDef = TypedDict(
    "GroupResourcesInputRequestTypeDef",
    {
        "Group": str,
        "ResourceArns": Sequence[str],
    },
)

GroupResourcesOutputTypeDef = TypedDict(
    "GroupResourcesOutputTypeDef",
    {
        "Succeeded": List[str],
        "Failed": List["FailedResourceTypeDef"],
        "Pending": List["PendingResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "GroupArn": str,
        "Name": str,
        "Description": NotRequired[str],
    },
)

ListGroupResourcesInputRequestTypeDef = TypedDict(
    "ListGroupResourcesInputRequestTypeDef",
    {
        "GroupName": NotRequired[str],
        "Group": NotRequired[str],
        "Filters": NotRequired[Sequence["ResourceFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListGroupResourcesItemTypeDef = TypedDict(
    "ListGroupResourcesItemTypeDef",
    {
        "Identifier": NotRequired["ResourceIdentifierTypeDef"],
        "Status": NotRequired["ResourceStatusTypeDef"],
    },
)

ListGroupResourcesOutputTypeDef = TypedDict(
    "ListGroupResourcesOutputTypeDef",
    {
        "Resources": List["ListGroupResourcesItemTypeDef"],
        "ResourceIdentifiers": List["ResourceIdentifierTypeDef"],
        "NextToken": str,
        "QueryErrors": List["QueryErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroupsInputRequestTypeDef = TypedDict(
    "ListGroupsInputRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["GroupFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListGroupsOutputTypeDef = TypedDict(
    "ListGroupsOutputTypeDef",
    {
        "GroupIdentifiers": List["GroupIdentifierTypeDef"],
        "Groups": List["GroupTypeDef"],
        "NextToken": str,
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

PendingResourceTypeDef = TypedDict(
    "PendingResourceTypeDef",
    {
        "ResourceArn": NotRequired[str],
    },
)

PutGroupConfigurationInputRequestTypeDef = TypedDict(
    "PutGroupConfigurationInputRequestTypeDef",
    {
        "Group": NotRequired[str],
        "Configuration": NotRequired[Sequence["GroupConfigurationItemTypeDef"]],
    },
)

QueryErrorTypeDef = TypedDict(
    "QueryErrorTypeDef",
    {
        "ErrorCode": NotRequired[QueryErrorCodeType],
        "Message": NotRequired[str],
    },
)

ResourceFilterTypeDef = TypedDict(
    "ResourceFilterTypeDef",
    {
        "Name": Literal["resource-type"],
        "Values": Sequence[str],
    },
)

ResourceIdentifierTypeDef = TypedDict(
    "ResourceIdentifierTypeDef",
    {
        "ResourceArn": NotRequired[str],
        "ResourceType": NotRequired[str],
    },
)

ResourceQueryTypeDef = TypedDict(
    "ResourceQueryTypeDef",
    {
        "Type": QueryTypeType,
        "Query": str,
    },
)

ResourceStatusTypeDef = TypedDict(
    "ResourceStatusTypeDef",
    {
        "Name": NotRequired[Literal["PENDING"]],
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

SearchResourcesInputRequestTypeDef = TypedDict(
    "SearchResourcesInputRequestTypeDef",
    {
        "ResourceQuery": "ResourceQueryTypeDef",
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

SearchResourcesOutputTypeDef = TypedDict(
    "SearchResourcesOutputTypeDef",
    {
        "ResourceIdentifiers": List["ResourceIdentifierTypeDef"],
        "NextToken": str,
        "QueryErrors": List["QueryErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagInputRequestTypeDef = TypedDict(
    "TagInputRequestTypeDef",
    {
        "Arn": str,
        "Tags": Mapping[str, str],
    },
)

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "Arn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UngroupResourcesInputRequestTypeDef = TypedDict(
    "UngroupResourcesInputRequestTypeDef",
    {
        "Group": str,
        "ResourceArns": Sequence[str],
    },
)

UngroupResourcesOutputTypeDef = TypedDict(
    "UngroupResourcesOutputTypeDef",
    {
        "Succeeded": List[str],
        "Failed": List["FailedResourceTypeDef"],
        "Pending": List["PendingResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagInputRequestTypeDef = TypedDict(
    "UntagInputRequestTypeDef",
    {
        "Arn": str,
        "Keys": Sequence[str],
    },
)

UntagOutputTypeDef = TypedDict(
    "UntagOutputTypeDef",
    {
        "Arn": str,
        "Keys": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGroupInputRequestTypeDef = TypedDict(
    "UpdateGroupInputRequestTypeDef",
    {
        "GroupName": NotRequired[str],
        "Group": NotRequired[str],
        "Description": NotRequired[str],
    },
)

UpdateGroupOutputTypeDef = TypedDict(
    "UpdateGroupOutputTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGroupQueryInputRequestTypeDef = TypedDict(
    "UpdateGroupQueryInputRequestTypeDef",
    {
        "ResourceQuery": "ResourceQueryTypeDef",
        "GroupName": NotRequired[str],
        "Group": NotRequired[str],
    },
)

UpdateGroupQueryOutputTypeDef = TypedDict(
    "UpdateGroupQueryOutputTypeDef",
    {
        "GroupQuery": "GroupQueryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
