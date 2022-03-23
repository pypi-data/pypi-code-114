"""
Type annotations for sms service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sms.type_defs import AppSummaryTypeDef

    data: AppSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AppLaunchConfigurationStatusType,
    AppLaunchStatusType,
    AppReplicationConfigurationStatusType,
    AppReplicationStatusType,
    AppStatusType,
    ConnectorCapabilityType,
    ConnectorStatusType,
    LicenseTypeType,
    OutputFormatType,
    ReplicationJobStateType,
    ReplicationRunStateType,
    ReplicationRunTypeType,
    ScriptTypeType,
    ServerCatalogStatusType,
    ValidationStatusType,
    VmManagerTypeType,
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
    "AppSummaryTypeDef",
    "AppValidationConfigurationTypeDef",
    "AppValidationOutputTypeDef",
    "ConnectorTypeDef",
    "CreateAppRequestRequestTypeDef",
    "CreateAppResponseTypeDef",
    "CreateReplicationJobRequestRequestTypeDef",
    "CreateReplicationJobResponseTypeDef",
    "DeleteAppLaunchConfigurationRequestRequestTypeDef",
    "DeleteAppReplicationConfigurationRequestRequestTypeDef",
    "DeleteAppRequestRequestTypeDef",
    "DeleteAppValidationConfigurationRequestRequestTypeDef",
    "DeleteReplicationJobRequestRequestTypeDef",
    "DisassociateConnectorRequestRequestTypeDef",
    "GenerateChangeSetRequestRequestTypeDef",
    "GenerateChangeSetResponseTypeDef",
    "GenerateTemplateRequestRequestTypeDef",
    "GenerateTemplateResponseTypeDef",
    "GetAppLaunchConfigurationRequestRequestTypeDef",
    "GetAppLaunchConfigurationResponseTypeDef",
    "GetAppReplicationConfigurationRequestRequestTypeDef",
    "GetAppReplicationConfigurationResponseTypeDef",
    "GetAppRequestRequestTypeDef",
    "GetAppResponseTypeDef",
    "GetAppValidationConfigurationRequestRequestTypeDef",
    "GetAppValidationConfigurationResponseTypeDef",
    "GetAppValidationOutputRequestRequestTypeDef",
    "GetAppValidationOutputResponseTypeDef",
    "GetConnectorsRequestRequestTypeDef",
    "GetConnectorsResponseTypeDef",
    "GetReplicationJobsRequestRequestTypeDef",
    "GetReplicationJobsResponseTypeDef",
    "GetReplicationRunsRequestRequestTypeDef",
    "GetReplicationRunsResponseTypeDef",
    "GetServersRequestRequestTypeDef",
    "GetServersResponseTypeDef",
    "ImportAppCatalogRequestRequestTypeDef",
    "LaunchAppRequestRequestTypeDef",
    "LaunchDetailsTypeDef",
    "ListAppsRequestRequestTypeDef",
    "ListAppsResponseTypeDef",
    "NotificationContextTypeDef",
    "NotifyAppValidationOutputRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "PutAppLaunchConfigurationRequestRequestTypeDef",
    "PutAppReplicationConfigurationRequestRequestTypeDef",
    "PutAppValidationConfigurationRequestRequestTypeDef",
    "ReplicationJobTypeDef",
    "ReplicationRunStageDetailsTypeDef",
    "ReplicationRunTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "SSMOutputTypeDef",
    "SSMValidationParametersTypeDef",
    "ServerGroupLaunchConfigurationTypeDef",
    "ServerGroupReplicationConfigurationTypeDef",
    "ServerGroupTypeDef",
    "ServerGroupValidationConfigurationTypeDef",
    "ServerLaunchConfigurationTypeDef",
    "ServerReplicationConfigurationTypeDef",
    "ServerReplicationParametersTypeDef",
    "ServerTypeDef",
    "ServerValidationConfigurationTypeDef",
    "ServerValidationOutputTypeDef",
    "SourceTypeDef",
    "StartAppReplicationRequestRequestTypeDef",
    "StartOnDemandAppReplicationRequestRequestTypeDef",
    "StartOnDemandReplicationRunRequestRequestTypeDef",
    "StartOnDemandReplicationRunResponseTypeDef",
    "StopAppReplicationRequestRequestTypeDef",
    "TagTypeDef",
    "TerminateAppRequestRequestTypeDef",
    "UpdateAppRequestRequestTypeDef",
    "UpdateAppResponseTypeDef",
    "UpdateReplicationJobRequestRequestTypeDef",
    "UserDataTypeDef",
    "UserDataValidationParametersTypeDef",
    "ValidationOutputTypeDef",
    "VmServerAddressTypeDef",
    "VmServerTypeDef",
)

AppSummaryTypeDef = TypedDict(
    "AppSummaryTypeDef",
    {
        "appId": NotRequired[str],
        "importedAppId": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "status": NotRequired[AppStatusType],
        "statusMessage": NotRequired[str],
        "replicationConfigurationStatus": NotRequired[AppReplicationConfigurationStatusType],
        "replicationStatus": NotRequired[AppReplicationStatusType],
        "replicationStatusMessage": NotRequired[str],
        "latestReplicationTime": NotRequired[datetime],
        "launchConfigurationStatus": NotRequired[AppLaunchConfigurationStatusType],
        "launchStatus": NotRequired[AppLaunchStatusType],
        "launchStatusMessage": NotRequired[str],
        "launchDetails": NotRequired["LaunchDetailsTypeDef"],
        "creationTime": NotRequired[datetime],
        "lastModified": NotRequired[datetime],
        "roleName": NotRequired[str],
        "totalServerGroups": NotRequired[int],
        "totalServers": NotRequired[int],
    },
)

AppValidationConfigurationTypeDef = TypedDict(
    "AppValidationConfigurationTypeDef",
    {
        "validationId": NotRequired[str],
        "name": NotRequired[str],
        "appValidationStrategy": NotRequired[Literal["SSM"]],
        "ssmValidationParameters": NotRequired["SSMValidationParametersTypeDef"],
    },
)

AppValidationOutputTypeDef = TypedDict(
    "AppValidationOutputTypeDef",
    {
        "ssmOutput": NotRequired["SSMOutputTypeDef"],
    },
)

ConnectorTypeDef = TypedDict(
    "ConnectorTypeDef",
    {
        "connectorId": NotRequired[str],
        "version": NotRequired[str],
        "status": NotRequired[ConnectorStatusType],
        "capabilityList": NotRequired[List[ConnectorCapabilityType]],
        "vmManagerName": NotRequired[str],
        "vmManagerType": NotRequired[VmManagerTypeType],
        "vmManagerId": NotRequired[str],
        "ipAddress": NotRequired[str],
        "macAddress": NotRequired[str],
        "associatedOn": NotRequired[datetime],
    },
)

CreateAppRequestRequestTypeDef = TypedDict(
    "CreateAppRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "roleName": NotRequired[str],
        "clientToken": NotRequired[str],
        "serverGroups": NotRequired[Sequence["ServerGroupTypeDef"]],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateAppResponseTypeDef = TypedDict(
    "CreateAppResponseTypeDef",
    {
        "appSummary": "AppSummaryTypeDef",
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateReplicationJobRequestRequestTypeDef = TypedDict(
    "CreateReplicationJobRequestRequestTypeDef",
    {
        "serverId": str,
        "seedReplicationTime": Union[datetime, str],
        "frequency": NotRequired[int],
        "runOnce": NotRequired[bool],
        "licenseType": NotRequired[LicenseTypeType],
        "roleName": NotRequired[str],
        "description": NotRequired[str],
        "numberOfRecentAmisToKeep": NotRequired[int],
        "encrypted": NotRequired[bool],
        "kmsKeyId": NotRequired[str],
    },
)

CreateReplicationJobResponseTypeDef = TypedDict(
    "CreateReplicationJobResponseTypeDef",
    {
        "replicationJobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAppLaunchConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAppLaunchConfigurationRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
    },
)

DeleteAppReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAppReplicationConfigurationRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
    },
)

DeleteAppRequestRequestTypeDef = TypedDict(
    "DeleteAppRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
        "forceStopAppReplication": NotRequired[bool],
        "forceTerminateApp": NotRequired[bool],
    },
)

DeleteAppValidationConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAppValidationConfigurationRequestRequestTypeDef",
    {
        "appId": str,
    },
)

DeleteReplicationJobRequestRequestTypeDef = TypedDict(
    "DeleteReplicationJobRequestRequestTypeDef",
    {
        "replicationJobId": str,
    },
)

DisassociateConnectorRequestRequestTypeDef = TypedDict(
    "DisassociateConnectorRequestRequestTypeDef",
    {
        "connectorId": str,
    },
)

GenerateChangeSetRequestRequestTypeDef = TypedDict(
    "GenerateChangeSetRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
        "changesetFormat": NotRequired[OutputFormatType],
    },
)

GenerateChangeSetResponseTypeDef = TypedDict(
    "GenerateChangeSetResponseTypeDef",
    {
        "s3Location": "S3LocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GenerateTemplateRequestRequestTypeDef = TypedDict(
    "GenerateTemplateRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
        "templateFormat": NotRequired[OutputFormatType],
    },
)

GenerateTemplateResponseTypeDef = TypedDict(
    "GenerateTemplateResponseTypeDef",
    {
        "s3Location": "S3LocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppLaunchConfigurationRequestRequestTypeDef = TypedDict(
    "GetAppLaunchConfigurationRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
    },
)

GetAppLaunchConfigurationResponseTypeDef = TypedDict(
    "GetAppLaunchConfigurationResponseTypeDef",
    {
        "appId": str,
        "roleName": str,
        "autoLaunch": bool,
        "serverGroupLaunchConfigurations": List["ServerGroupLaunchConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "GetAppReplicationConfigurationRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
    },
)

GetAppReplicationConfigurationResponseTypeDef = TypedDict(
    "GetAppReplicationConfigurationResponseTypeDef",
    {
        "serverGroupReplicationConfigurations": List["ServerGroupReplicationConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppRequestRequestTypeDef = TypedDict(
    "GetAppRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
    },
)

GetAppResponseTypeDef = TypedDict(
    "GetAppResponseTypeDef",
    {
        "appSummary": "AppSummaryTypeDef",
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppValidationConfigurationRequestRequestTypeDef = TypedDict(
    "GetAppValidationConfigurationRequestRequestTypeDef",
    {
        "appId": str,
    },
)

GetAppValidationConfigurationResponseTypeDef = TypedDict(
    "GetAppValidationConfigurationResponseTypeDef",
    {
        "appValidationConfigurations": List["AppValidationConfigurationTypeDef"],
        "serverGroupValidationConfigurations": List["ServerGroupValidationConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppValidationOutputRequestRequestTypeDef = TypedDict(
    "GetAppValidationOutputRequestRequestTypeDef",
    {
        "appId": str,
    },
)

GetAppValidationOutputResponseTypeDef = TypedDict(
    "GetAppValidationOutputResponseTypeDef",
    {
        "validationOutputList": List["ValidationOutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectorsRequestRequestTypeDef = TypedDict(
    "GetConnectorsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetConnectorsResponseTypeDef = TypedDict(
    "GetConnectorsResponseTypeDef",
    {
        "connectorList": List["ConnectorTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReplicationJobsRequestRequestTypeDef = TypedDict(
    "GetReplicationJobsRequestRequestTypeDef",
    {
        "replicationJobId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetReplicationJobsResponseTypeDef = TypedDict(
    "GetReplicationJobsResponseTypeDef",
    {
        "replicationJobList": List["ReplicationJobTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReplicationRunsRequestRequestTypeDef = TypedDict(
    "GetReplicationRunsRequestRequestTypeDef",
    {
        "replicationJobId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetReplicationRunsResponseTypeDef = TypedDict(
    "GetReplicationRunsResponseTypeDef",
    {
        "replicationJob": "ReplicationJobTypeDef",
        "replicationRunList": List["ReplicationRunTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServersRequestRequestTypeDef = TypedDict(
    "GetServersRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "vmServerAddressList": NotRequired[Sequence["VmServerAddressTypeDef"]],
    },
)

GetServersResponseTypeDef = TypedDict(
    "GetServersResponseTypeDef",
    {
        "lastModifiedOn": datetime,
        "serverCatalogStatus": ServerCatalogStatusType,
        "serverList": List["ServerTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportAppCatalogRequestRequestTypeDef = TypedDict(
    "ImportAppCatalogRequestRequestTypeDef",
    {
        "roleName": NotRequired[str],
    },
)

LaunchAppRequestRequestTypeDef = TypedDict(
    "LaunchAppRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
    },
)

LaunchDetailsTypeDef = TypedDict(
    "LaunchDetailsTypeDef",
    {
        "latestLaunchTime": NotRequired[datetime],
        "stackName": NotRequired[str],
        "stackId": NotRequired[str],
    },
)

ListAppsRequestRequestTypeDef = TypedDict(
    "ListAppsRequestRequestTypeDef",
    {
        "appIds": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAppsResponseTypeDef = TypedDict(
    "ListAppsResponseTypeDef",
    {
        "apps": List["AppSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotificationContextTypeDef = TypedDict(
    "NotificationContextTypeDef",
    {
        "validationId": NotRequired[str],
        "status": NotRequired[ValidationStatusType],
        "statusMessage": NotRequired[str],
    },
)

NotifyAppValidationOutputRequestRequestTypeDef = TypedDict(
    "NotifyAppValidationOutputRequestRequestTypeDef",
    {
        "appId": str,
        "notificationContext": NotRequired["NotificationContextTypeDef"],
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

PutAppLaunchConfigurationRequestRequestTypeDef = TypedDict(
    "PutAppLaunchConfigurationRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
        "roleName": NotRequired[str],
        "autoLaunch": NotRequired[bool],
        "serverGroupLaunchConfigurations": NotRequired[
            Sequence["ServerGroupLaunchConfigurationTypeDef"]
        ],
    },
)

PutAppReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "PutAppReplicationConfigurationRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
        "serverGroupReplicationConfigurations": NotRequired[
            Sequence["ServerGroupReplicationConfigurationTypeDef"]
        ],
    },
)

PutAppValidationConfigurationRequestRequestTypeDef = TypedDict(
    "PutAppValidationConfigurationRequestRequestTypeDef",
    {
        "appId": str,
        "appValidationConfigurations": NotRequired[Sequence["AppValidationConfigurationTypeDef"]],
        "serverGroupValidationConfigurations": NotRequired[
            Sequence["ServerGroupValidationConfigurationTypeDef"]
        ],
    },
)

ReplicationJobTypeDef = TypedDict(
    "ReplicationJobTypeDef",
    {
        "replicationJobId": NotRequired[str],
        "serverId": NotRequired[str],
        "serverType": NotRequired[Literal["VIRTUAL_MACHINE"]],
        "vmServer": NotRequired["VmServerTypeDef"],
        "seedReplicationTime": NotRequired[datetime],
        "frequency": NotRequired[int],
        "runOnce": NotRequired[bool],
        "nextReplicationRunStartTime": NotRequired[datetime],
        "licenseType": NotRequired[LicenseTypeType],
        "roleName": NotRequired[str],
        "latestAmiId": NotRequired[str],
        "state": NotRequired[ReplicationJobStateType],
        "statusMessage": NotRequired[str],
        "description": NotRequired[str],
        "numberOfRecentAmisToKeep": NotRequired[int],
        "encrypted": NotRequired[bool],
        "kmsKeyId": NotRequired[str],
        "replicationRunList": NotRequired[List["ReplicationRunTypeDef"]],
    },
)

ReplicationRunStageDetailsTypeDef = TypedDict(
    "ReplicationRunStageDetailsTypeDef",
    {
        "stage": NotRequired[str],
        "stageProgress": NotRequired[str],
    },
)

ReplicationRunTypeDef = TypedDict(
    "ReplicationRunTypeDef",
    {
        "replicationRunId": NotRequired[str],
        "state": NotRequired[ReplicationRunStateType],
        "type": NotRequired[ReplicationRunTypeType],
        "stageDetails": NotRequired["ReplicationRunStageDetailsTypeDef"],
        "statusMessage": NotRequired[str],
        "amiId": NotRequired[str],
        "scheduledStartTime": NotRequired[datetime],
        "completedTime": NotRequired[datetime],
        "description": NotRequired[str],
        "encrypted": NotRequired[bool],
        "kmsKeyId": NotRequired[str],
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

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": NotRequired[str],
        "key": NotRequired[str],
    },
)

SSMOutputTypeDef = TypedDict(
    "SSMOutputTypeDef",
    {
        "s3Location": NotRequired["S3LocationTypeDef"],
    },
)

SSMValidationParametersTypeDef = TypedDict(
    "SSMValidationParametersTypeDef",
    {
        "source": NotRequired["SourceTypeDef"],
        "instanceId": NotRequired[str],
        "scriptType": NotRequired[ScriptTypeType],
        "command": NotRequired[str],
        "executionTimeoutSeconds": NotRequired[int],
        "outputS3BucketName": NotRequired[str],
    },
)

ServerGroupLaunchConfigurationTypeDef = TypedDict(
    "ServerGroupLaunchConfigurationTypeDef",
    {
        "serverGroupId": NotRequired[str],
        "launchOrder": NotRequired[int],
        "serverLaunchConfigurations": NotRequired[List["ServerLaunchConfigurationTypeDef"]],
    },
)

ServerGroupReplicationConfigurationTypeDef = TypedDict(
    "ServerGroupReplicationConfigurationTypeDef",
    {
        "serverGroupId": NotRequired[str],
        "serverReplicationConfigurations": NotRequired[
            List["ServerReplicationConfigurationTypeDef"]
        ],
    },
)

ServerGroupTypeDef = TypedDict(
    "ServerGroupTypeDef",
    {
        "serverGroupId": NotRequired[str],
        "name": NotRequired[str],
        "serverList": NotRequired[Sequence["ServerTypeDef"]],
    },
)

ServerGroupValidationConfigurationTypeDef = TypedDict(
    "ServerGroupValidationConfigurationTypeDef",
    {
        "serverGroupId": NotRequired[str],
        "serverValidationConfigurations": NotRequired[List["ServerValidationConfigurationTypeDef"]],
    },
)

ServerLaunchConfigurationTypeDef = TypedDict(
    "ServerLaunchConfigurationTypeDef",
    {
        "server": NotRequired["ServerTypeDef"],
        "logicalId": NotRequired[str],
        "vpc": NotRequired[str],
        "subnet": NotRequired[str],
        "securityGroup": NotRequired[str],
        "ec2KeyName": NotRequired[str],
        "userData": NotRequired["UserDataTypeDef"],
        "instanceType": NotRequired[str],
        "associatePublicIpAddress": NotRequired[bool],
        "iamInstanceProfileName": NotRequired[str],
        "configureScript": NotRequired["S3LocationTypeDef"],
        "configureScriptType": NotRequired[ScriptTypeType],
    },
)

ServerReplicationConfigurationTypeDef = TypedDict(
    "ServerReplicationConfigurationTypeDef",
    {
        "server": NotRequired["ServerTypeDef"],
        "serverReplicationParameters": NotRequired["ServerReplicationParametersTypeDef"],
    },
)

ServerReplicationParametersTypeDef = TypedDict(
    "ServerReplicationParametersTypeDef",
    {
        "seedTime": NotRequired[datetime],
        "frequency": NotRequired[int],
        "runOnce": NotRequired[bool],
        "licenseType": NotRequired[LicenseTypeType],
        "numberOfRecentAmisToKeep": NotRequired[int],
        "encrypted": NotRequired[bool],
        "kmsKeyId": NotRequired[str],
    },
)

ServerTypeDef = TypedDict(
    "ServerTypeDef",
    {
        "serverId": NotRequired[str],
        "serverType": NotRequired[Literal["VIRTUAL_MACHINE"]],
        "vmServer": NotRequired["VmServerTypeDef"],
        "replicationJobId": NotRequired[str],
        "replicationJobTerminated": NotRequired[bool],
    },
)

ServerValidationConfigurationTypeDef = TypedDict(
    "ServerValidationConfigurationTypeDef",
    {
        "server": NotRequired["ServerTypeDef"],
        "validationId": NotRequired[str],
        "name": NotRequired[str],
        "serverValidationStrategy": NotRequired[Literal["USERDATA"]],
        "userDataValidationParameters": NotRequired["UserDataValidationParametersTypeDef"],
    },
)

ServerValidationOutputTypeDef = TypedDict(
    "ServerValidationOutputTypeDef",
    {
        "server": NotRequired["ServerTypeDef"],
    },
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "s3Location": NotRequired["S3LocationTypeDef"],
    },
)

StartAppReplicationRequestRequestTypeDef = TypedDict(
    "StartAppReplicationRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
    },
)

StartOnDemandAppReplicationRequestRequestTypeDef = TypedDict(
    "StartOnDemandAppReplicationRequestRequestTypeDef",
    {
        "appId": str,
        "description": NotRequired[str],
    },
)

StartOnDemandReplicationRunRequestRequestTypeDef = TypedDict(
    "StartOnDemandReplicationRunRequestRequestTypeDef",
    {
        "replicationJobId": str,
        "description": NotRequired[str],
    },
)

StartOnDemandReplicationRunResponseTypeDef = TypedDict(
    "StartOnDemandReplicationRunResponseTypeDef",
    {
        "replicationRunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopAppReplicationRequestRequestTypeDef = TypedDict(
    "StopAppReplicationRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
    },
)

TerminateAppRequestRequestTypeDef = TypedDict(
    "TerminateAppRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
    },
)

UpdateAppRequestRequestTypeDef = TypedDict(
    "UpdateAppRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "roleName": NotRequired[str],
        "serverGroups": NotRequired[Sequence["ServerGroupTypeDef"]],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

UpdateAppResponseTypeDef = TypedDict(
    "UpdateAppResponseTypeDef",
    {
        "appSummary": "AppSummaryTypeDef",
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateReplicationJobRequestRequestTypeDef = TypedDict(
    "UpdateReplicationJobRequestRequestTypeDef",
    {
        "replicationJobId": str,
        "frequency": NotRequired[int],
        "nextReplicationRunStartTime": NotRequired[Union[datetime, str]],
        "licenseType": NotRequired[LicenseTypeType],
        "roleName": NotRequired[str],
        "description": NotRequired[str],
        "numberOfRecentAmisToKeep": NotRequired[int],
        "encrypted": NotRequired[bool],
        "kmsKeyId": NotRequired[str],
    },
)

UserDataTypeDef = TypedDict(
    "UserDataTypeDef",
    {
        "s3Location": NotRequired["S3LocationTypeDef"],
    },
)

UserDataValidationParametersTypeDef = TypedDict(
    "UserDataValidationParametersTypeDef",
    {
        "source": NotRequired["SourceTypeDef"],
        "scriptType": NotRequired[ScriptTypeType],
    },
)

ValidationOutputTypeDef = TypedDict(
    "ValidationOutputTypeDef",
    {
        "validationId": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[ValidationStatusType],
        "statusMessage": NotRequired[str],
        "latestValidationTime": NotRequired[datetime],
        "appValidationOutput": NotRequired["AppValidationOutputTypeDef"],
        "serverValidationOutput": NotRequired["ServerValidationOutputTypeDef"],
    },
)

VmServerAddressTypeDef = TypedDict(
    "VmServerAddressTypeDef",
    {
        "vmManagerId": NotRequired[str],
        "vmId": NotRequired[str],
    },
)

VmServerTypeDef = TypedDict(
    "VmServerTypeDef",
    {
        "vmServerAddress": NotRequired["VmServerAddressTypeDef"],
        "vmName": NotRequired[str],
        "vmManagerName": NotRequired[str],
        "vmManagerType": NotRequired[VmManagerTypeType],
        "vmPath": NotRequired[str],
    },
)
