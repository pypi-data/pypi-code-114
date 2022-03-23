"""
Type annotations for rum service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/type_defs.html)

Usage::

    ```python
    from mypy_boto3_rum.type_defs import AppMonitorConfigurationTypeDef

    data: AppMonitorConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import StateEnumType, TelemetryType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AppMonitorConfigurationTypeDef",
    "AppMonitorDetailsTypeDef",
    "AppMonitorSummaryTypeDef",
    "AppMonitorTypeDef",
    "CreateAppMonitorRequestRequestTypeDef",
    "CreateAppMonitorResponseTypeDef",
    "CwLogTypeDef",
    "DataStorageTypeDef",
    "DeleteAppMonitorRequestRequestTypeDef",
    "GetAppMonitorDataRequestRequestTypeDef",
    "GetAppMonitorDataResponseTypeDef",
    "GetAppMonitorRequestRequestTypeDef",
    "GetAppMonitorResponseTypeDef",
    "ListAppMonitorsRequestRequestTypeDef",
    "ListAppMonitorsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutRumEventsRequestRequestTypeDef",
    "QueryFilterTypeDef",
    "ResponseMetadataTypeDef",
    "RumEventTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TimeRangeTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAppMonitorRequestRequestTypeDef",
    "UserDetailsTypeDef",
)

AppMonitorConfigurationTypeDef = TypedDict(
    "AppMonitorConfigurationTypeDef",
    {
        "AllowCookies": NotRequired[bool],
        "EnableXRay": NotRequired[bool],
        "ExcludedPages": NotRequired[Sequence[str]],
        "FavoritePages": NotRequired[Sequence[str]],
        "GuestRoleArn": NotRequired[str],
        "IdentityPoolId": NotRequired[str],
        "IncludedPages": NotRequired[Sequence[str]],
        "SessionSampleRate": NotRequired[float],
        "Telemetries": NotRequired[Sequence[TelemetryType]],
    },
)

AppMonitorDetailsTypeDef = TypedDict(
    "AppMonitorDetailsTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "version": NotRequired[str],
    },
)

AppMonitorSummaryTypeDef = TypedDict(
    "AppMonitorSummaryTypeDef",
    {
        "Created": NotRequired[str],
        "Id": NotRequired[str],
        "LastModified": NotRequired[str],
        "Name": NotRequired[str],
        "State": NotRequired[StateEnumType],
    },
)

AppMonitorTypeDef = TypedDict(
    "AppMonitorTypeDef",
    {
        "AppMonitorConfiguration": NotRequired["AppMonitorConfigurationTypeDef"],
        "Created": NotRequired[str],
        "DataStorage": NotRequired["DataStorageTypeDef"],
        "Domain": NotRequired[str],
        "Id": NotRequired[str],
        "LastModified": NotRequired[str],
        "Name": NotRequired[str],
        "State": NotRequired[StateEnumType],
        "Tags": NotRequired[Dict[str, str]],
    },
)

CreateAppMonitorRequestRequestTypeDef = TypedDict(
    "CreateAppMonitorRequestRequestTypeDef",
    {
        "Domain": str,
        "Name": str,
        "AppMonitorConfiguration": NotRequired["AppMonitorConfigurationTypeDef"],
        "CwLogEnabled": NotRequired[bool],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateAppMonitorResponseTypeDef = TypedDict(
    "CreateAppMonitorResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CwLogTypeDef = TypedDict(
    "CwLogTypeDef",
    {
        "CwLogEnabled": NotRequired[bool],
        "CwLogGroup": NotRequired[str],
    },
)

DataStorageTypeDef = TypedDict(
    "DataStorageTypeDef",
    {
        "CwLog": NotRequired["CwLogTypeDef"],
    },
)

DeleteAppMonitorRequestRequestTypeDef = TypedDict(
    "DeleteAppMonitorRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetAppMonitorDataRequestRequestTypeDef = TypedDict(
    "GetAppMonitorDataRequestRequestTypeDef",
    {
        "Name": str,
        "TimeRange": "TimeRangeTypeDef",
        "Filters": NotRequired[Sequence["QueryFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetAppMonitorDataResponseTypeDef = TypedDict(
    "GetAppMonitorDataResponseTypeDef",
    {
        "Events": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppMonitorRequestRequestTypeDef = TypedDict(
    "GetAppMonitorRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetAppMonitorResponseTypeDef = TypedDict(
    "GetAppMonitorResponseTypeDef",
    {
        "AppMonitor": "AppMonitorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppMonitorsRequestRequestTypeDef = TypedDict(
    "ListAppMonitorsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAppMonitorsResponseTypeDef = TypedDict(
    "ListAppMonitorsResponseTypeDef",
    {
        "AppMonitorSummaries": List["AppMonitorSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
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

PutRumEventsRequestRequestTypeDef = TypedDict(
    "PutRumEventsRequestRequestTypeDef",
    {
        "AppMonitorDetails": "AppMonitorDetailsTypeDef",
        "BatchId": str,
        "Id": str,
        "RumEvents": Sequence["RumEventTypeDef"],
        "UserDetails": "UserDetailsTypeDef",
    },
)

QueryFilterTypeDef = TypedDict(
    "QueryFilterTypeDef",
    {
        "Name": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
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

RumEventTypeDef = TypedDict(
    "RumEventTypeDef",
    {
        "details": str,
        "id": str,
        "timestamp": Union[datetime, str],
        "type": str,
        "metadata": NotRequired[str],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "After": int,
        "Before": NotRequired[int],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateAppMonitorRequestRequestTypeDef = TypedDict(
    "UpdateAppMonitorRequestRequestTypeDef",
    {
        "Name": str,
        "AppMonitorConfiguration": NotRequired["AppMonitorConfigurationTypeDef"],
        "CwLogEnabled": NotRequired[bool],
        "Domain": NotRequired[str],
    },
)

UserDetailsTypeDef = TypedDict(
    "UserDetailsTypeDef",
    {
        "sessionId": NotRequired[str],
        "userId": NotRequired[str],
    },
)
