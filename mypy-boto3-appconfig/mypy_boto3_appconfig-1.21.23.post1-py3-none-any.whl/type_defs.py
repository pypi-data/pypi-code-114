"""
Type annotations for appconfig service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appconfig.type_defs import ApplicationResponseMetadataTypeDef

    data: ApplicationResponseMetadataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    DeploymentEventTypeType,
    DeploymentStateType,
    EnvironmentStateType,
    GrowthTypeType,
    ReplicateToType,
    TriggeredByType,
    ValidatorTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationResponseMetadataTypeDef",
    "ApplicationTypeDef",
    "ApplicationsTypeDef",
    "ConfigurationProfileSummaryTypeDef",
    "ConfigurationProfileTypeDef",
    "ConfigurationProfilesTypeDef",
    "ConfigurationTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateConfigurationProfileRequestRequestTypeDef",
    "CreateDeploymentStrategyRequestRequestTypeDef",
    "CreateEnvironmentRequestRequestTypeDef",
    "CreateHostedConfigurationVersionRequestRequestTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteConfigurationProfileRequestRequestTypeDef",
    "DeleteDeploymentStrategyRequestRequestTypeDef",
    "DeleteEnvironmentRequestRequestTypeDef",
    "DeleteHostedConfigurationVersionRequestRequestTypeDef",
    "DeploymentEventTypeDef",
    "DeploymentStrategiesTypeDef",
    "DeploymentStrategyResponseMetadataTypeDef",
    "DeploymentStrategyTypeDef",
    "DeploymentSummaryTypeDef",
    "DeploymentTypeDef",
    "DeploymentsTypeDef",
    "EnvironmentResponseMetadataTypeDef",
    "EnvironmentTypeDef",
    "EnvironmentsTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "GetConfigurationProfileRequestRequestTypeDef",
    "GetConfigurationRequestRequestTypeDef",
    "GetDeploymentRequestRequestTypeDef",
    "GetDeploymentStrategyRequestRequestTypeDef",
    "GetEnvironmentRequestRequestTypeDef",
    "GetHostedConfigurationVersionRequestRequestTypeDef",
    "HostedConfigurationVersionSummaryTypeDef",
    "HostedConfigurationVersionTypeDef",
    "HostedConfigurationVersionsTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListConfigurationProfilesRequestRequestTypeDef",
    "ListDeploymentStrategiesRequestRequestTypeDef",
    "ListDeploymentsRequestRequestTypeDef",
    "ListEnvironmentsRequestRequestTypeDef",
    "ListHostedConfigurationVersionsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "MonitorTypeDef",
    "ResourceTagsTypeDef",
    "ResponseMetadataTypeDef",
    "StartDeploymentRequestRequestTypeDef",
    "StopDeploymentRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "UpdateConfigurationProfileRequestRequestTypeDef",
    "UpdateDeploymentStrategyRequestRequestTypeDef",
    "UpdateEnvironmentRequestRequestTypeDef",
    "ValidateConfigurationRequestRequestTypeDef",
    "ValidatorTypeDef",
)

ApplicationResponseMetadataTypeDef = TypedDict(
    "ApplicationResponseMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)

ApplicationsTypeDef = TypedDict(
    "ApplicationsTypeDef",
    {
        "Items": List["ApplicationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigurationProfileSummaryTypeDef = TypedDict(
    "ConfigurationProfileSummaryTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "LocationUri": NotRequired[str],
        "ValidatorTypes": NotRequired[List[ValidatorTypeType]],
        "Type": NotRequired[str],
    },
)

ConfigurationProfileTypeDef = TypedDict(
    "ConfigurationProfileTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "LocationUri": str,
        "RetrievalRoleArn": str,
        "Validators": List["ValidatorTypeDef"],
        "Type": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigurationProfilesTypeDef = TypedDict(
    "ConfigurationProfilesTypeDef",
    {
        "Items": List["ConfigurationProfileSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Content": StreamingBody,
        "ConfigurationVersion": str,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateConfigurationProfileRequestRequestTypeDef = TypedDict(
    "CreateConfigurationProfileRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "Name": str,
        "LocationUri": str,
        "Description": NotRequired[str],
        "RetrievalRoleArn": NotRequired[str],
        "Validators": NotRequired[Sequence["ValidatorTypeDef"]],
        "Tags": NotRequired[Mapping[str, str]],
        "Type": NotRequired[str],
    },
)

CreateDeploymentStrategyRequestRequestTypeDef = TypedDict(
    "CreateDeploymentStrategyRequestRequestTypeDef",
    {
        "Name": str,
        "DeploymentDurationInMinutes": int,
        "GrowthFactor": float,
        "ReplicateTo": ReplicateToType,
        "Description": NotRequired[str],
        "FinalBakeTimeInMinutes": NotRequired[int],
        "GrowthType": NotRequired[GrowthTypeType],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateEnvironmentRequestRequestTypeDef = TypedDict(
    "CreateEnvironmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "Name": str,
        "Description": NotRequired[str],
        "Monitors": NotRequired[Sequence["MonitorTypeDef"]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateHostedConfigurationVersionRequestRequestTypeDef = TypedDict(
    "CreateHostedConfigurationVersionRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "Content": Union[bytes, IO[bytes], StreamingBody],
        "ContentType": str,
        "Description": NotRequired[str],
        "LatestVersionNumber": NotRequired[int],
    },
)

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteConfigurationProfileRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationProfileRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
    },
)

DeleteDeploymentStrategyRequestRequestTypeDef = TypedDict(
    "DeleteDeploymentStrategyRequestRequestTypeDef",
    {
        "DeploymentStrategyId": str,
    },
)

DeleteEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteEnvironmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
    },
)

DeleteHostedConfigurationVersionRequestRequestTypeDef = TypedDict(
    "DeleteHostedConfigurationVersionRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "VersionNumber": int,
    },
)

DeploymentEventTypeDef = TypedDict(
    "DeploymentEventTypeDef",
    {
        "EventType": NotRequired[DeploymentEventTypeType],
        "TriggeredBy": NotRequired[TriggeredByType],
        "Description": NotRequired[str],
        "OccurredAt": NotRequired[datetime],
    },
)

DeploymentStrategiesTypeDef = TypedDict(
    "DeploymentStrategiesTypeDef",
    {
        "Items": List["DeploymentStrategyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeploymentStrategyResponseMetadataTypeDef = TypedDict(
    "DeploymentStrategyResponseMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "DeploymentDurationInMinutes": int,
        "GrowthType": GrowthTypeType,
        "GrowthFactor": float,
        "FinalBakeTimeInMinutes": int,
        "ReplicateTo": ReplicateToType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeploymentStrategyTypeDef = TypedDict(
    "DeploymentStrategyTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "DeploymentDurationInMinutes": NotRequired[int],
        "GrowthType": NotRequired[GrowthTypeType],
        "GrowthFactor": NotRequired[float],
        "FinalBakeTimeInMinutes": NotRequired[int],
        "ReplicateTo": NotRequired[ReplicateToType],
    },
)

DeploymentSummaryTypeDef = TypedDict(
    "DeploymentSummaryTypeDef",
    {
        "DeploymentNumber": NotRequired[int],
        "ConfigurationName": NotRequired[str],
        "ConfigurationVersion": NotRequired[str],
        "DeploymentDurationInMinutes": NotRequired[int],
        "GrowthType": NotRequired[GrowthTypeType],
        "GrowthFactor": NotRequired[float],
        "FinalBakeTimeInMinutes": NotRequired[int],
        "State": NotRequired[DeploymentStateType],
        "PercentageComplete": NotRequired[float],
        "StartedAt": NotRequired[datetime],
        "CompletedAt": NotRequired[datetime],
    },
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "DeploymentStrategyId": str,
        "ConfigurationProfileId": str,
        "DeploymentNumber": int,
        "ConfigurationName": str,
        "ConfigurationLocationUri": str,
        "ConfigurationVersion": str,
        "Description": str,
        "DeploymentDurationInMinutes": int,
        "GrowthType": GrowthTypeType,
        "GrowthFactor": float,
        "FinalBakeTimeInMinutes": int,
        "State": DeploymentStateType,
        "EventLog": List["DeploymentEventTypeDef"],
        "PercentageComplete": float,
        "StartedAt": datetime,
        "CompletedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeploymentsTypeDef = TypedDict(
    "DeploymentsTypeDef",
    {
        "Items": List["DeploymentSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentResponseMetadataTypeDef = TypedDict(
    "EnvironmentResponseMetadataTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "State": EnvironmentStateType,
        "Monitors": List["MonitorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "State": NotRequired[EnvironmentStateType],
        "Monitors": NotRequired[List["MonitorTypeDef"]],
    },
)

EnvironmentsTypeDef = TypedDict(
    "EnvironmentsTypeDef",
    {
        "Items": List["EnvironmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApplicationRequestRequestTypeDef = TypedDict(
    "GetApplicationRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetConfigurationProfileRequestRequestTypeDef = TypedDict(
    "GetConfigurationProfileRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
    },
)

GetConfigurationRequestRequestTypeDef = TypedDict(
    "GetConfigurationRequestRequestTypeDef",
    {
        "Application": str,
        "Environment": str,
        "Configuration": str,
        "ClientId": str,
        "ClientConfigurationVersion": NotRequired[str],
    },
)

GetDeploymentRequestRequestTypeDef = TypedDict(
    "GetDeploymentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "DeploymentNumber": int,
    },
)

GetDeploymentStrategyRequestRequestTypeDef = TypedDict(
    "GetDeploymentStrategyRequestRequestTypeDef",
    {
        "DeploymentStrategyId": str,
    },
)

GetEnvironmentRequestRequestTypeDef = TypedDict(
    "GetEnvironmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
    },
)

GetHostedConfigurationVersionRequestRequestTypeDef = TypedDict(
    "GetHostedConfigurationVersionRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "VersionNumber": int,
    },
)

HostedConfigurationVersionSummaryTypeDef = TypedDict(
    "HostedConfigurationVersionSummaryTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "ConfigurationProfileId": NotRequired[str],
        "VersionNumber": NotRequired[int],
        "Description": NotRequired[str],
        "ContentType": NotRequired[str],
    },
)

HostedConfigurationVersionTypeDef = TypedDict(
    "HostedConfigurationVersionTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "VersionNumber": int,
        "Description": str,
        "Content": StreamingBody,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HostedConfigurationVersionsTypeDef = TypedDict(
    "HostedConfigurationVersionsTypeDef",
    {
        "Items": List["HostedConfigurationVersionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListConfigurationProfilesRequestRequestTypeDef = TypedDict(
    "ListConfigurationProfilesRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Type": NotRequired[str],
    },
)

ListDeploymentStrategiesRequestRequestTypeDef = TypedDict(
    "ListDeploymentStrategiesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListDeploymentsRequestRequestTypeDef = TypedDict(
    "ListDeploymentsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListEnvironmentsRequestRequestTypeDef = TypedDict(
    "ListEnvironmentsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListHostedConfigurationVersionsRequestRequestTypeDef = TypedDict(
    "ListHostedConfigurationVersionsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

MonitorTypeDef = TypedDict(
    "MonitorTypeDef",
    {
        "AlarmArn": str,
        "AlarmRoleArn": NotRequired[str],
    },
)

ResourceTagsTypeDef = TypedDict(
    "ResourceTagsTypeDef",
    {
        "Tags": Dict[str, str],
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

StartDeploymentRequestRequestTypeDef = TypedDict(
    "StartDeploymentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "DeploymentStrategyId": str,
        "ConfigurationProfileId": str,
        "ConfigurationVersion": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

StopDeploymentRequestRequestTypeDef = TypedDict(
    "StopDeploymentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "DeploymentNumber": int,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)

UpdateConfigurationProfileRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationProfileRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "RetrievalRoleArn": NotRequired[str],
        "Validators": NotRequired[Sequence["ValidatorTypeDef"]],
    },
)

UpdateDeploymentStrategyRequestRequestTypeDef = TypedDict(
    "UpdateDeploymentStrategyRequestRequestTypeDef",
    {
        "DeploymentStrategyId": str,
        "Description": NotRequired[str],
        "DeploymentDurationInMinutes": NotRequired[int],
        "FinalBakeTimeInMinutes": NotRequired[int],
        "GrowthFactor": NotRequired[float],
        "GrowthType": NotRequired[GrowthTypeType],
    },
)

UpdateEnvironmentRequestRequestTypeDef = TypedDict(
    "UpdateEnvironmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Monitors": NotRequired[Sequence["MonitorTypeDef"]],
    },
)

ValidateConfigurationRequestRequestTypeDef = TypedDict(
    "ValidateConfigurationRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "ConfigurationVersion": str,
    },
)

ValidatorTypeDef = TypedDict(
    "ValidatorTypeDef",
    {
        "Type": ValidatorTypeType,
        "Content": str,
    },
)
