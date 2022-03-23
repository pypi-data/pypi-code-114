"""
Type annotations for cognito-sync service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_cognito_sync/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_cognito_sync.type_defs import BulkPublishRequestRequestTypeDef

    data: BulkPublishRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import BulkPublishStatusType, OperationType, PlatformType, StreamingStatusType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BulkPublishRequestRequestTypeDef",
    "BulkPublishResponseTypeDef",
    "CognitoStreamsTypeDef",
    "DatasetTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteDatasetResponseTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeIdentityPoolUsageRequestRequestTypeDef",
    "DescribeIdentityPoolUsageResponseTypeDef",
    "DescribeIdentityUsageRequestRequestTypeDef",
    "DescribeIdentityUsageResponseTypeDef",
    "GetBulkPublishDetailsRequestRequestTypeDef",
    "GetBulkPublishDetailsResponseTypeDef",
    "GetCognitoEventsRequestRequestTypeDef",
    "GetCognitoEventsResponseTypeDef",
    "GetIdentityPoolConfigurationRequestRequestTypeDef",
    "GetIdentityPoolConfigurationResponseTypeDef",
    "IdentityPoolUsageTypeDef",
    "IdentityUsageTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListIdentityPoolUsageRequestRequestTypeDef",
    "ListIdentityPoolUsageResponseTypeDef",
    "ListRecordsRequestRequestTypeDef",
    "ListRecordsResponseTypeDef",
    "PushSyncTypeDef",
    "RecordPatchTypeDef",
    "RecordTypeDef",
    "RegisterDeviceRequestRequestTypeDef",
    "RegisterDeviceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SetCognitoEventsRequestRequestTypeDef",
    "SetIdentityPoolConfigurationRequestRequestTypeDef",
    "SetIdentityPoolConfigurationResponseTypeDef",
    "SubscribeToDatasetRequestRequestTypeDef",
    "UnsubscribeFromDatasetRequestRequestTypeDef",
    "UpdateRecordsRequestRequestTypeDef",
    "UpdateRecordsResponseTypeDef",
)

BulkPublishRequestRequestTypeDef = TypedDict(
    "BulkPublishRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

BulkPublishResponseTypeDef = TypedDict(
    "BulkPublishResponseTypeDef",
    {
        "IdentityPoolId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CognitoStreamsTypeDef = TypedDict(
    "CognitoStreamsTypeDef",
    {
        "StreamName": NotRequired[str],
        "RoleArn": NotRequired[str],
        "StreamingStatus": NotRequired[StreamingStatusType],
    },
)

DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "IdentityId": NotRequired[str],
        "DatasetName": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "LastModifiedDate": NotRequired[datetime],
        "LastModifiedBy": NotRequired[str],
        "DataStorage": NotRequired[int],
        "NumRecords": NotRequired[int],
    },
)

DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
    },
)

DeleteDatasetResponseTypeDef = TypedDict(
    "DeleteDatasetResponseTypeDef",
    {
        "Dataset": "DatasetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
    },
)

DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "Dataset": "DatasetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIdentityPoolUsageRequestRequestTypeDef = TypedDict(
    "DescribeIdentityPoolUsageRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

DescribeIdentityPoolUsageResponseTypeDef = TypedDict(
    "DescribeIdentityPoolUsageResponseTypeDef",
    {
        "IdentityPoolUsage": "IdentityPoolUsageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIdentityUsageRequestRequestTypeDef = TypedDict(
    "DescribeIdentityUsageRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
    },
)

DescribeIdentityUsageResponseTypeDef = TypedDict(
    "DescribeIdentityUsageResponseTypeDef",
    {
        "IdentityUsage": "IdentityUsageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBulkPublishDetailsRequestRequestTypeDef = TypedDict(
    "GetBulkPublishDetailsRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

GetBulkPublishDetailsResponseTypeDef = TypedDict(
    "GetBulkPublishDetailsResponseTypeDef",
    {
        "IdentityPoolId": str,
        "BulkPublishStartTime": datetime,
        "BulkPublishCompleteTime": datetime,
        "BulkPublishStatus": BulkPublishStatusType,
        "FailureMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCognitoEventsRequestRequestTypeDef = TypedDict(
    "GetCognitoEventsRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

GetCognitoEventsResponseTypeDef = TypedDict(
    "GetCognitoEventsResponseTypeDef",
    {
        "Events": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityPoolConfigurationRequestRequestTypeDef = TypedDict(
    "GetIdentityPoolConfigurationRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

GetIdentityPoolConfigurationResponseTypeDef = TypedDict(
    "GetIdentityPoolConfigurationResponseTypeDef",
    {
        "IdentityPoolId": str,
        "PushSync": "PushSyncTypeDef",
        "CognitoStreams": "CognitoStreamsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityPoolUsageTypeDef = TypedDict(
    "IdentityPoolUsageTypeDef",
    {
        "IdentityPoolId": NotRequired[str],
        "SyncSessionsCount": NotRequired[int],
        "DataStorage": NotRequired[int],
        "LastModifiedDate": NotRequired[datetime],
    },
)

IdentityUsageTypeDef = TypedDict(
    "IdentityUsageTypeDef",
    {
        "IdentityId": NotRequired[str],
        "IdentityPoolId": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "DatasetCount": NotRequired[int],
        "DataStorage": NotRequired[int],
    },
)

ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "Datasets": List["DatasetTypeDef"],
        "Count": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIdentityPoolUsageRequestRequestTypeDef = TypedDict(
    "ListIdentityPoolUsageRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListIdentityPoolUsageResponseTypeDef = TypedDict(
    "ListIdentityPoolUsageResponseTypeDef",
    {
        "IdentityPoolUsages": List["IdentityPoolUsageTypeDef"],
        "MaxResults": int,
        "Count": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecordsRequestRequestTypeDef = TypedDict(
    "ListRecordsRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
        "LastSyncCount": NotRequired[int],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "SyncSessionToken": NotRequired[str],
    },
)

ListRecordsResponseTypeDef = TypedDict(
    "ListRecordsResponseTypeDef",
    {
        "Records": List["RecordTypeDef"],
        "NextToken": str,
        "Count": int,
        "DatasetSyncCount": int,
        "LastModifiedBy": str,
        "MergedDatasetNames": List[str],
        "DatasetExists": bool,
        "DatasetDeletedAfterRequestedSyncCount": bool,
        "SyncSessionToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PushSyncTypeDef = TypedDict(
    "PushSyncTypeDef",
    {
        "ApplicationArns": NotRequired[List[str]],
        "RoleArn": NotRequired[str],
    },
)

RecordPatchTypeDef = TypedDict(
    "RecordPatchTypeDef",
    {
        "Op": OperationType,
        "Key": str,
        "SyncCount": int,
        "Value": NotRequired[str],
        "DeviceLastModifiedDate": NotRequired[Union[datetime, str]],
    },
)

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "SyncCount": NotRequired[int],
        "LastModifiedDate": NotRequired[datetime],
        "LastModifiedBy": NotRequired[str],
        "DeviceLastModifiedDate": NotRequired[datetime],
    },
)

RegisterDeviceRequestRequestTypeDef = TypedDict(
    "RegisterDeviceRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "Platform": PlatformType,
        "Token": str,
    },
)

RegisterDeviceResponseTypeDef = TypedDict(
    "RegisterDeviceResponseTypeDef",
    {
        "DeviceId": str,
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

SetCognitoEventsRequestRequestTypeDef = TypedDict(
    "SetCognitoEventsRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "Events": Mapping[str, str],
    },
)

SetIdentityPoolConfigurationRequestRequestTypeDef = TypedDict(
    "SetIdentityPoolConfigurationRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "PushSync": NotRequired["PushSyncTypeDef"],
        "CognitoStreams": NotRequired["CognitoStreamsTypeDef"],
    },
)

SetIdentityPoolConfigurationResponseTypeDef = TypedDict(
    "SetIdentityPoolConfigurationResponseTypeDef",
    {
        "IdentityPoolId": str,
        "PushSync": "PushSyncTypeDef",
        "CognitoStreams": "CognitoStreamsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubscribeToDatasetRequestRequestTypeDef = TypedDict(
    "SubscribeToDatasetRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
        "DeviceId": str,
    },
)

UnsubscribeFromDatasetRequestRequestTypeDef = TypedDict(
    "UnsubscribeFromDatasetRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
        "DeviceId": str,
    },
)

UpdateRecordsRequestRequestTypeDef = TypedDict(
    "UpdateRecordsRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
        "SyncSessionToken": str,
        "DeviceId": NotRequired[str],
        "RecordPatches": NotRequired[Sequence["RecordPatchTypeDef"]],
        "ClientContext": NotRequired[str],
    },
)

UpdateRecordsResponseTypeDef = TypedDict(
    "UpdateRecordsResponseTypeDef",
    {
        "Records": List["RecordTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
