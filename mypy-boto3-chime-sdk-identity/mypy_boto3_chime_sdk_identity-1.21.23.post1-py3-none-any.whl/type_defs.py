"""
Type annotations for chime-sdk-identity service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/type_defs.html)

Usage::

    ```python
    from mypy_boto3_chime_sdk_identity.type_defs import AppInstanceAdminSummaryTypeDef

    data: AppInstanceAdminSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    AllowMessagesType,
    AppInstanceUserEndpointTypeType,
    EndpointStatusReasonType,
    EndpointStatusType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AppInstanceAdminSummaryTypeDef",
    "AppInstanceAdminTypeDef",
    "AppInstanceRetentionSettingsTypeDef",
    "AppInstanceSummaryTypeDef",
    "AppInstanceTypeDef",
    "AppInstanceUserEndpointSummaryTypeDef",
    "AppInstanceUserEndpointTypeDef",
    "AppInstanceUserSummaryTypeDef",
    "AppInstanceUserTypeDef",
    "ChannelRetentionSettingsTypeDef",
    "CreateAppInstanceAdminRequestRequestTypeDef",
    "CreateAppInstanceAdminResponseTypeDef",
    "CreateAppInstanceRequestRequestTypeDef",
    "CreateAppInstanceResponseTypeDef",
    "CreateAppInstanceUserRequestRequestTypeDef",
    "CreateAppInstanceUserResponseTypeDef",
    "DeleteAppInstanceAdminRequestRequestTypeDef",
    "DeleteAppInstanceRequestRequestTypeDef",
    "DeleteAppInstanceUserRequestRequestTypeDef",
    "DeregisterAppInstanceUserEndpointRequestRequestTypeDef",
    "DescribeAppInstanceAdminRequestRequestTypeDef",
    "DescribeAppInstanceAdminResponseTypeDef",
    "DescribeAppInstanceRequestRequestTypeDef",
    "DescribeAppInstanceResponseTypeDef",
    "DescribeAppInstanceUserEndpointRequestRequestTypeDef",
    "DescribeAppInstanceUserEndpointResponseTypeDef",
    "DescribeAppInstanceUserRequestRequestTypeDef",
    "DescribeAppInstanceUserResponseTypeDef",
    "EndpointAttributesTypeDef",
    "EndpointStateTypeDef",
    "GetAppInstanceRetentionSettingsRequestRequestTypeDef",
    "GetAppInstanceRetentionSettingsResponseTypeDef",
    "IdentityTypeDef",
    "ListAppInstanceAdminsRequestRequestTypeDef",
    "ListAppInstanceAdminsResponseTypeDef",
    "ListAppInstanceUserEndpointsRequestRequestTypeDef",
    "ListAppInstanceUserEndpointsResponseTypeDef",
    "ListAppInstanceUsersRequestRequestTypeDef",
    "ListAppInstanceUsersResponseTypeDef",
    "ListAppInstancesRequestRequestTypeDef",
    "ListAppInstancesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutAppInstanceRetentionSettingsRequestRequestTypeDef",
    "PutAppInstanceRetentionSettingsResponseTypeDef",
    "RegisterAppInstanceUserEndpointRequestRequestTypeDef",
    "RegisterAppInstanceUserEndpointResponseTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAppInstanceRequestRequestTypeDef",
    "UpdateAppInstanceResponseTypeDef",
    "UpdateAppInstanceUserEndpointRequestRequestTypeDef",
    "UpdateAppInstanceUserEndpointResponseTypeDef",
    "UpdateAppInstanceUserRequestRequestTypeDef",
    "UpdateAppInstanceUserResponseTypeDef",
)

AppInstanceAdminSummaryTypeDef = TypedDict(
    "AppInstanceAdminSummaryTypeDef",
    {
        "Admin": NotRequired["IdentityTypeDef"],
    },
)

AppInstanceAdminTypeDef = TypedDict(
    "AppInstanceAdminTypeDef",
    {
        "Admin": NotRequired["IdentityTypeDef"],
        "AppInstanceArn": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
    },
)

AppInstanceRetentionSettingsTypeDef = TypedDict(
    "AppInstanceRetentionSettingsTypeDef",
    {
        "ChannelRetentionSettings": NotRequired["ChannelRetentionSettingsTypeDef"],
    },
)

AppInstanceSummaryTypeDef = TypedDict(
    "AppInstanceSummaryTypeDef",
    {
        "AppInstanceArn": NotRequired[str],
        "Name": NotRequired[str],
        "Metadata": NotRequired[str],
    },
)

AppInstanceTypeDef = TypedDict(
    "AppInstanceTypeDef",
    {
        "AppInstanceArn": NotRequired[str],
        "Name": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "Metadata": NotRequired[str],
    },
)

AppInstanceUserEndpointSummaryTypeDef = TypedDict(
    "AppInstanceUserEndpointSummaryTypeDef",
    {
        "AppInstanceUserArn": NotRequired[str],
        "EndpointId": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[AppInstanceUserEndpointTypeType],
        "AllowMessages": NotRequired[AllowMessagesType],
        "EndpointState": NotRequired["EndpointStateTypeDef"],
    },
)

AppInstanceUserEndpointTypeDef = TypedDict(
    "AppInstanceUserEndpointTypeDef",
    {
        "AppInstanceUserArn": NotRequired[str],
        "EndpointId": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[AppInstanceUserEndpointTypeType],
        "ResourceArn": NotRequired[str],
        "EndpointAttributes": NotRequired["EndpointAttributesTypeDef"],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "AllowMessages": NotRequired[AllowMessagesType],
        "EndpointState": NotRequired["EndpointStateTypeDef"],
    },
)

AppInstanceUserSummaryTypeDef = TypedDict(
    "AppInstanceUserSummaryTypeDef",
    {
        "AppInstanceUserArn": NotRequired[str],
        "Name": NotRequired[str],
        "Metadata": NotRequired[str],
    },
)

AppInstanceUserTypeDef = TypedDict(
    "AppInstanceUserTypeDef",
    {
        "AppInstanceUserArn": NotRequired[str],
        "Name": NotRequired[str],
        "Metadata": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
    },
)

ChannelRetentionSettingsTypeDef = TypedDict(
    "ChannelRetentionSettingsTypeDef",
    {
        "RetentionDays": NotRequired[int],
    },
)

CreateAppInstanceAdminRequestRequestTypeDef = TypedDict(
    "CreateAppInstanceAdminRequestRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)

CreateAppInstanceAdminResponseTypeDef = TypedDict(
    "CreateAppInstanceAdminResponseTypeDef",
    {
        "AppInstanceAdmin": "IdentityTypeDef",
        "AppInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAppInstanceRequestRequestTypeDef = TypedDict(
    "CreateAppInstanceRequestRequestTypeDef",
    {
        "Name": str,
        "ClientRequestToken": str,
        "Metadata": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateAppInstanceResponseTypeDef = TypedDict(
    "CreateAppInstanceResponseTypeDef",
    {
        "AppInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAppInstanceUserRequestRequestTypeDef = TypedDict(
    "CreateAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceUserId": str,
        "Name": str,
        "ClientRequestToken": str,
        "Metadata": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateAppInstanceUserResponseTypeDef = TypedDict(
    "CreateAppInstanceUserResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAppInstanceAdminRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceAdminRequestRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)

DeleteAppInstanceRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

DeleteAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
    },
)

DeregisterAppInstanceUserEndpointRequestRequestTypeDef = TypedDict(
    "DeregisterAppInstanceUserEndpointRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
    },
)

DescribeAppInstanceAdminRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceAdminRequestRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)

DescribeAppInstanceAdminResponseTypeDef = TypedDict(
    "DescribeAppInstanceAdminResponseTypeDef",
    {
        "AppInstanceAdmin": "AppInstanceAdminTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppInstanceRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

DescribeAppInstanceResponseTypeDef = TypedDict(
    "DescribeAppInstanceResponseTypeDef",
    {
        "AppInstance": "AppInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppInstanceUserEndpointRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceUserEndpointRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
    },
)

DescribeAppInstanceUserEndpointResponseTypeDef = TypedDict(
    "DescribeAppInstanceUserEndpointResponseTypeDef",
    {
        "AppInstanceUserEndpoint": "AppInstanceUserEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
    },
)

DescribeAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeAppInstanceUserResponseTypeDef",
    {
        "AppInstanceUser": "AppInstanceUserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointAttributesTypeDef = TypedDict(
    "EndpointAttributesTypeDef",
    {
        "DeviceToken": str,
        "VoipDeviceToken": NotRequired[str],
    },
)

EndpointStateTypeDef = TypedDict(
    "EndpointStateTypeDef",
    {
        "Status": EndpointStatusType,
        "StatusReason": NotRequired[EndpointStatusReasonType],
    },
)

GetAppInstanceRetentionSettingsRequestRequestTypeDef = TypedDict(
    "GetAppInstanceRetentionSettingsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

GetAppInstanceRetentionSettingsResponseTypeDef = TypedDict(
    "GetAppInstanceRetentionSettingsResponseTypeDef",
    {
        "AppInstanceRetentionSettings": "AppInstanceRetentionSettingsTypeDef",
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)

ListAppInstanceAdminsRequestRequestTypeDef = TypedDict(
    "ListAppInstanceAdminsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAppInstanceAdminsResponseTypeDef = TypedDict(
    "ListAppInstanceAdminsResponseTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceAdmins": List["AppInstanceAdminSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppInstanceUserEndpointsRequestRequestTypeDef = TypedDict(
    "ListAppInstanceUserEndpointsRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAppInstanceUserEndpointsResponseTypeDef = TypedDict(
    "ListAppInstanceUserEndpointsResponseTypeDef",
    {
        "AppInstanceUserEndpoints": List["AppInstanceUserEndpointSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppInstanceUsersRequestRequestTypeDef = TypedDict(
    "ListAppInstanceUsersRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAppInstanceUsersResponseTypeDef = TypedDict(
    "ListAppInstanceUsersResponseTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceUsers": List["AppInstanceUserSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppInstancesRequestRequestTypeDef = TypedDict(
    "ListAppInstancesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAppInstancesResponseTypeDef = TypedDict(
    "ListAppInstancesResponseTypeDef",
    {
        "AppInstances": List["AppInstanceSummaryTypeDef"],
        "NextToken": str,
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

PutAppInstanceRetentionSettingsRequestRequestTypeDef = TypedDict(
    "PutAppInstanceRetentionSettingsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceRetentionSettings": "AppInstanceRetentionSettingsTypeDef",
    },
)

PutAppInstanceRetentionSettingsResponseTypeDef = TypedDict(
    "PutAppInstanceRetentionSettingsResponseTypeDef",
    {
        "AppInstanceRetentionSettings": "AppInstanceRetentionSettingsTypeDef",
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterAppInstanceUserEndpointRequestRequestTypeDef = TypedDict(
    "RegisterAppInstanceUserEndpointRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "Type": AppInstanceUserEndpointTypeType,
        "ResourceArn": str,
        "EndpointAttributes": "EndpointAttributesTypeDef",
        "ClientRequestToken": str,
        "Name": NotRequired[str],
        "AllowMessages": NotRequired[AllowMessagesType],
    },
)

RegisterAppInstanceUserEndpointResponseTypeDef = TypedDict(
    "RegisterAppInstanceUserEndpointResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
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

UpdateAppInstanceRequestRequestTypeDef = TypedDict(
    "UpdateAppInstanceRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
        "Metadata": str,
    },
)

UpdateAppInstanceResponseTypeDef = TypedDict(
    "UpdateAppInstanceResponseTypeDef",
    {
        "AppInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAppInstanceUserEndpointRequestRequestTypeDef = TypedDict(
    "UpdateAppInstanceUserEndpointRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
        "Name": NotRequired[str],
        "AllowMessages": NotRequired[AllowMessagesType],
    },
)

UpdateAppInstanceUserEndpointResponseTypeDef = TypedDict(
    "UpdateAppInstanceUserEndpointResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAppInstanceUserRequestRequestTypeDef = TypedDict(
    "UpdateAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "Name": str,
        "Metadata": str,
    },
)

UpdateAppInstanceUserResponseTypeDef = TypedDict(
    "UpdateAppInstanceUserResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
