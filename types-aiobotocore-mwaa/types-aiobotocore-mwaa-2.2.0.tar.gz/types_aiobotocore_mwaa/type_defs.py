"""
Type annotations for mwaa service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mwaa/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_mwaa.type_defs import CreateCliTokenRequestRequestTypeDef

    data: CreateCliTokenRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    EnvironmentStatusType,
    LoggingLevelType,
    UnitType,
    UpdateStatusType,
    WebserverAccessModeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateCliTokenRequestRequestTypeDef",
    "CreateCliTokenResponseTypeDef",
    "CreateEnvironmentInputRequestTypeDef",
    "CreateEnvironmentOutputTypeDef",
    "CreateWebLoginTokenRequestRequestTypeDef",
    "CreateWebLoginTokenResponseTypeDef",
    "DeleteEnvironmentInputRequestTypeDef",
    "DimensionTypeDef",
    "EnvironmentTypeDef",
    "GetEnvironmentInputRequestTypeDef",
    "GetEnvironmentOutputTypeDef",
    "LastUpdateTypeDef",
    "ListEnvironmentsInputRequestTypeDef",
    "ListEnvironmentsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LoggingConfigurationInputTypeDef",
    "LoggingConfigurationTypeDef",
    "MetricDatumTypeDef",
    "ModuleLoggingConfigurationInputTypeDef",
    "ModuleLoggingConfigurationTypeDef",
    "NetworkConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PublishMetricsInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "StatisticSetTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateEnvironmentInputRequestTypeDef",
    "UpdateEnvironmentOutputTypeDef",
    "UpdateErrorTypeDef",
    "UpdateNetworkConfigurationInputTypeDef",
)

CreateCliTokenRequestRequestTypeDef = TypedDict(
    "CreateCliTokenRequestRequestTypeDef",
    {
        "Name": str,
    },
)

CreateCliTokenResponseTypeDef = TypedDict(
    "CreateCliTokenResponseTypeDef",
    {
        "CliToken": str,
        "WebServerHostname": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEnvironmentInputRequestTypeDef = TypedDict(
    "CreateEnvironmentInputRequestTypeDef",
    {
        "DagS3Path": str,
        "ExecutionRoleArn": str,
        "Name": str,
        "NetworkConfiguration": "NetworkConfigurationTypeDef",
        "SourceBucketArn": str,
        "AirflowConfigurationOptions": NotRequired[Mapping[str, str]],
        "AirflowVersion": NotRequired[str],
        "EnvironmentClass": NotRequired[str],
        "KmsKey": NotRequired[str],
        "LoggingConfiguration": NotRequired["LoggingConfigurationInputTypeDef"],
        "MaxWorkers": NotRequired[int],
        "MinWorkers": NotRequired[int],
        "PluginsS3ObjectVersion": NotRequired[str],
        "PluginsS3Path": NotRequired[str],
        "RequirementsS3ObjectVersion": NotRequired[str],
        "RequirementsS3Path": NotRequired[str],
        "Schedulers": NotRequired[int],
        "Tags": NotRequired[Mapping[str, str]],
        "WebserverAccessMode": NotRequired[WebserverAccessModeType],
        "WeeklyMaintenanceWindowStart": NotRequired[str],
    },
)

CreateEnvironmentOutputTypeDef = TypedDict(
    "CreateEnvironmentOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWebLoginTokenRequestRequestTypeDef = TypedDict(
    "CreateWebLoginTokenRequestRequestTypeDef",
    {
        "Name": str,
    },
)

CreateWebLoginTokenResponseTypeDef = TypedDict(
    "CreateWebLoginTokenResponseTypeDef",
    {
        "WebServerHostname": str,
        "WebToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentInputRequestTypeDef",
    {
        "Name": str,
    },
)

DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "AirflowConfigurationOptions": NotRequired[Dict[str, str]],
        "AirflowVersion": NotRequired[str],
        "Arn": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "DagS3Path": NotRequired[str],
        "EnvironmentClass": NotRequired[str],
        "ExecutionRoleArn": NotRequired[str],
        "KmsKey": NotRequired[str],
        "LastUpdate": NotRequired["LastUpdateTypeDef"],
        "LoggingConfiguration": NotRequired["LoggingConfigurationTypeDef"],
        "MaxWorkers": NotRequired[int],
        "MinWorkers": NotRequired[int],
        "Name": NotRequired[str],
        "NetworkConfiguration": NotRequired["NetworkConfigurationTypeDef"],
        "PluginsS3ObjectVersion": NotRequired[str],
        "PluginsS3Path": NotRequired[str],
        "RequirementsS3ObjectVersion": NotRequired[str],
        "RequirementsS3Path": NotRequired[str],
        "Schedulers": NotRequired[int],
        "ServiceRoleArn": NotRequired[str],
        "SourceBucketArn": NotRequired[str],
        "Status": NotRequired[EnvironmentStatusType],
        "Tags": NotRequired[Dict[str, str]],
        "WebserverAccessMode": NotRequired[WebserverAccessModeType],
        "WebserverUrl": NotRequired[str],
        "WeeklyMaintenanceWindowStart": NotRequired[str],
    },
)

GetEnvironmentInputRequestTypeDef = TypedDict(
    "GetEnvironmentInputRequestTypeDef",
    {
        "Name": str,
    },
)

GetEnvironmentOutputTypeDef = TypedDict(
    "GetEnvironmentOutputTypeDef",
    {
        "Environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LastUpdateTypeDef = TypedDict(
    "LastUpdateTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "Error": NotRequired["UpdateErrorTypeDef"],
        "Source": NotRequired[str],
        "Status": NotRequired[UpdateStatusType],
    },
)

ListEnvironmentsInputRequestTypeDef = TypedDict(
    "ListEnvironmentsInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListEnvironmentsOutputTypeDef = TypedDict(
    "ListEnvironmentsOutputTypeDef",
    {
        "Environments": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingConfigurationInputTypeDef = TypedDict(
    "LoggingConfigurationInputTypeDef",
    {
        "DagProcessingLogs": NotRequired["ModuleLoggingConfigurationInputTypeDef"],
        "SchedulerLogs": NotRequired["ModuleLoggingConfigurationInputTypeDef"],
        "TaskLogs": NotRequired["ModuleLoggingConfigurationInputTypeDef"],
        "WebserverLogs": NotRequired["ModuleLoggingConfigurationInputTypeDef"],
        "WorkerLogs": NotRequired["ModuleLoggingConfigurationInputTypeDef"],
    },
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "DagProcessingLogs": NotRequired["ModuleLoggingConfigurationTypeDef"],
        "SchedulerLogs": NotRequired["ModuleLoggingConfigurationTypeDef"],
        "TaskLogs": NotRequired["ModuleLoggingConfigurationTypeDef"],
        "WebserverLogs": NotRequired["ModuleLoggingConfigurationTypeDef"],
        "WorkerLogs": NotRequired["ModuleLoggingConfigurationTypeDef"],
    },
)

MetricDatumTypeDef = TypedDict(
    "MetricDatumTypeDef",
    {
        "MetricName": str,
        "Timestamp": Union[datetime, str],
        "Dimensions": NotRequired[Sequence["DimensionTypeDef"]],
        "StatisticValues": NotRequired["StatisticSetTypeDef"],
        "Unit": NotRequired[UnitType],
        "Value": NotRequired[float],
    },
)

ModuleLoggingConfigurationInputTypeDef = TypedDict(
    "ModuleLoggingConfigurationInputTypeDef",
    {
        "Enabled": bool,
        "LogLevel": LoggingLevelType,
    },
)

ModuleLoggingConfigurationTypeDef = TypedDict(
    "ModuleLoggingConfigurationTypeDef",
    {
        "CloudWatchLogGroupArn": NotRequired[str],
        "Enabled": NotRequired[bool],
        "LogLevel": NotRequired[LoggingLevelType],
    },
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SubnetIds": NotRequired[Sequence[str]],
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

PublishMetricsInputRequestTypeDef = TypedDict(
    "PublishMetricsInputRequestTypeDef",
    {
        "EnvironmentName": str,
        "MetricData": Sequence["MetricDatumTypeDef"],
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

StatisticSetTypeDef = TypedDict(
    "StatisticSetTypeDef",
    {
        "Maximum": NotRequired[float],
        "Minimum": NotRequired[float],
        "SampleCount": NotRequired[int],
        "Sum": NotRequired[float],
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateEnvironmentInputRequestTypeDef = TypedDict(
    "UpdateEnvironmentInputRequestTypeDef",
    {
        "Name": str,
        "AirflowConfigurationOptions": NotRequired[Mapping[str, str]],
        "AirflowVersion": NotRequired[str],
        "DagS3Path": NotRequired[str],
        "EnvironmentClass": NotRequired[str],
        "ExecutionRoleArn": NotRequired[str],
        "LoggingConfiguration": NotRequired["LoggingConfigurationInputTypeDef"],
        "MaxWorkers": NotRequired[int],
        "MinWorkers": NotRequired[int],
        "NetworkConfiguration": NotRequired["UpdateNetworkConfigurationInputTypeDef"],
        "PluginsS3ObjectVersion": NotRequired[str],
        "PluginsS3Path": NotRequired[str],
        "RequirementsS3ObjectVersion": NotRequired[str],
        "RequirementsS3Path": NotRequired[str],
        "Schedulers": NotRequired[int],
        "SourceBucketArn": NotRequired[str],
        "WebserverAccessMode": NotRequired[WebserverAccessModeType],
        "WeeklyMaintenanceWindowStart": NotRequired[str],
    },
)

UpdateEnvironmentOutputTypeDef = TypedDict(
    "UpdateEnvironmentOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateErrorTypeDef = TypedDict(
    "UpdateErrorTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

UpdateNetworkConfigurationInputTypeDef = TypedDict(
    "UpdateNetworkConfigurationInputTypeDef",
    {
        "SecurityGroupIds": Sequence[str],
    },
)
