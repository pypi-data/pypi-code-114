"""
Type annotations for greengrass service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_greengrass/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_greengrass.type_defs import AssociateRoleToGroupRequestRequestTypeDef

    data: AssociateRoleToGroupRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    BulkDeploymentStatusType,
    ConfigurationSyncStatusType,
    DeploymentTypeType,
    EncodingTypeType,
    FunctionIsolationModeType,
    LoggerComponentType,
    LoggerLevelType,
    LoggerTypeType,
    PermissionType,
    SoftwareToUpdateType,
    TelemetryType,
    UpdateAgentLogLevelType,
    UpdateTargetsArchitectureType,
    UpdateTargetsOperatingSystemType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateRoleToGroupRequestRequestTypeDef",
    "AssociateRoleToGroupResponseTypeDef",
    "AssociateServiceRoleToAccountRequestRequestTypeDef",
    "AssociateServiceRoleToAccountResponseTypeDef",
    "BulkDeploymentMetricsTypeDef",
    "BulkDeploymentResultTypeDef",
    "BulkDeploymentTypeDef",
    "ConnectivityInfoTypeDef",
    "ConnectorDefinitionVersionTypeDef",
    "ConnectorTypeDef",
    "CoreDefinitionVersionTypeDef",
    "CoreTypeDef",
    "CreateConnectorDefinitionRequestRequestTypeDef",
    "CreateConnectorDefinitionResponseTypeDef",
    "CreateConnectorDefinitionVersionRequestRequestTypeDef",
    "CreateConnectorDefinitionVersionResponseTypeDef",
    "CreateCoreDefinitionRequestRequestTypeDef",
    "CreateCoreDefinitionResponseTypeDef",
    "CreateCoreDefinitionVersionRequestRequestTypeDef",
    "CreateCoreDefinitionVersionResponseTypeDef",
    "CreateDeploymentRequestRequestTypeDef",
    "CreateDeploymentResponseTypeDef",
    "CreateDeviceDefinitionRequestRequestTypeDef",
    "CreateDeviceDefinitionResponseTypeDef",
    "CreateDeviceDefinitionVersionRequestRequestTypeDef",
    "CreateDeviceDefinitionVersionResponseTypeDef",
    "CreateFunctionDefinitionRequestRequestTypeDef",
    "CreateFunctionDefinitionResponseTypeDef",
    "CreateFunctionDefinitionVersionRequestRequestTypeDef",
    "CreateFunctionDefinitionVersionResponseTypeDef",
    "CreateGroupCertificateAuthorityRequestRequestTypeDef",
    "CreateGroupCertificateAuthorityResponseTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateGroupVersionRequestRequestTypeDef",
    "CreateGroupVersionResponseTypeDef",
    "CreateLoggerDefinitionRequestRequestTypeDef",
    "CreateLoggerDefinitionResponseTypeDef",
    "CreateLoggerDefinitionVersionRequestRequestTypeDef",
    "CreateLoggerDefinitionVersionResponseTypeDef",
    "CreateResourceDefinitionRequestRequestTypeDef",
    "CreateResourceDefinitionResponseTypeDef",
    "CreateResourceDefinitionVersionRequestRequestTypeDef",
    "CreateResourceDefinitionVersionResponseTypeDef",
    "CreateSoftwareUpdateJobRequestRequestTypeDef",
    "CreateSoftwareUpdateJobResponseTypeDef",
    "CreateSubscriptionDefinitionRequestRequestTypeDef",
    "CreateSubscriptionDefinitionResponseTypeDef",
    "CreateSubscriptionDefinitionVersionRequestRequestTypeDef",
    "CreateSubscriptionDefinitionVersionResponseTypeDef",
    "DefinitionInformationTypeDef",
    "DeleteConnectorDefinitionRequestRequestTypeDef",
    "DeleteCoreDefinitionRequestRequestTypeDef",
    "DeleteDeviceDefinitionRequestRequestTypeDef",
    "DeleteFunctionDefinitionRequestRequestTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteLoggerDefinitionRequestRequestTypeDef",
    "DeleteResourceDefinitionRequestRequestTypeDef",
    "DeleteSubscriptionDefinitionRequestRequestTypeDef",
    "DeploymentTypeDef",
    "DeviceDefinitionVersionTypeDef",
    "DeviceTypeDef",
    "DisassociateRoleFromGroupRequestRequestTypeDef",
    "DisassociateRoleFromGroupResponseTypeDef",
    "DisassociateServiceRoleFromAccountResponseTypeDef",
    "ErrorDetailTypeDef",
    "FunctionConfigurationEnvironmentTypeDef",
    "FunctionConfigurationTypeDef",
    "FunctionDefaultConfigTypeDef",
    "FunctionDefaultExecutionConfigTypeDef",
    "FunctionDefinitionVersionTypeDef",
    "FunctionExecutionConfigTypeDef",
    "FunctionRunAsConfigTypeDef",
    "FunctionTypeDef",
    "GetAssociatedRoleRequestRequestTypeDef",
    "GetAssociatedRoleResponseTypeDef",
    "GetBulkDeploymentStatusRequestRequestTypeDef",
    "GetBulkDeploymentStatusResponseTypeDef",
    "GetConnectivityInfoRequestRequestTypeDef",
    "GetConnectivityInfoResponseTypeDef",
    "GetConnectorDefinitionRequestRequestTypeDef",
    "GetConnectorDefinitionResponseTypeDef",
    "GetConnectorDefinitionVersionRequestRequestTypeDef",
    "GetConnectorDefinitionVersionResponseTypeDef",
    "GetCoreDefinitionRequestRequestTypeDef",
    "GetCoreDefinitionResponseTypeDef",
    "GetCoreDefinitionVersionRequestRequestTypeDef",
    "GetCoreDefinitionVersionResponseTypeDef",
    "GetDeploymentStatusRequestRequestTypeDef",
    "GetDeploymentStatusResponseTypeDef",
    "GetDeviceDefinitionRequestRequestTypeDef",
    "GetDeviceDefinitionResponseTypeDef",
    "GetDeviceDefinitionVersionRequestRequestTypeDef",
    "GetDeviceDefinitionVersionResponseTypeDef",
    "GetFunctionDefinitionRequestRequestTypeDef",
    "GetFunctionDefinitionResponseTypeDef",
    "GetFunctionDefinitionVersionRequestRequestTypeDef",
    "GetFunctionDefinitionVersionResponseTypeDef",
    "GetGroupCertificateAuthorityRequestRequestTypeDef",
    "GetGroupCertificateAuthorityResponseTypeDef",
    "GetGroupCertificateConfigurationRequestRequestTypeDef",
    "GetGroupCertificateConfigurationResponseTypeDef",
    "GetGroupRequestRequestTypeDef",
    "GetGroupResponseTypeDef",
    "GetGroupVersionRequestRequestTypeDef",
    "GetGroupVersionResponseTypeDef",
    "GetLoggerDefinitionRequestRequestTypeDef",
    "GetLoggerDefinitionResponseTypeDef",
    "GetLoggerDefinitionVersionRequestRequestTypeDef",
    "GetLoggerDefinitionVersionResponseTypeDef",
    "GetResourceDefinitionRequestRequestTypeDef",
    "GetResourceDefinitionResponseTypeDef",
    "GetResourceDefinitionVersionRequestRequestTypeDef",
    "GetResourceDefinitionVersionResponseTypeDef",
    "GetServiceRoleForAccountResponseTypeDef",
    "GetSubscriptionDefinitionRequestRequestTypeDef",
    "GetSubscriptionDefinitionResponseTypeDef",
    "GetSubscriptionDefinitionVersionRequestRequestTypeDef",
    "GetSubscriptionDefinitionVersionResponseTypeDef",
    "GetThingRuntimeConfigurationRequestRequestTypeDef",
    "GetThingRuntimeConfigurationResponseTypeDef",
    "GroupCertificateAuthorityPropertiesTypeDef",
    "GroupInformationTypeDef",
    "GroupOwnerSettingTypeDef",
    "GroupVersionTypeDef",
    "ListBulkDeploymentDetailedReportsRequestRequestTypeDef",
    "ListBulkDeploymentDetailedReportsResponseTypeDef",
    "ListBulkDeploymentsRequestRequestTypeDef",
    "ListBulkDeploymentsResponseTypeDef",
    "ListConnectorDefinitionVersionsRequestRequestTypeDef",
    "ListConnectorDefinitionVersionsResponseTypeDef",
    "ListConnectorDefinitionsRequestRequestTypeDef",
    "ListConnectorDefinitionsResponseTypeDef",
    "ListCoreDefinitionVersionsRequestRequestTypeDef",
    "ListCoreDefinitionVersionsResponseTypeDef",
    "ListCoreDefinitionsRequestRequestTypeDef",
    "ListCoreDefinitionsResponseTypeDef",
    "ListDeploymentsRequestRequestTypeDef",
    "ListDeploymentsResponseTypeDef",
    "ListDeviceDefinitionVersionsRequestRequestTypeDef",
    "ListDeviceDefinitionVersionsResponseTypeDef",
    "ListDeviceDefinitionsRequestRequestTypeDef",
    "ListDeviceDefinitionsResponseTypeDef",
    "ListFunctionDefinitionVersionsRequestRequestTypeDef",
    "ListFunctionDefinitionVersionsResponseTypeDef",
    "ListFunctionDefinitionsRequestRequestTypeDef",
    "ListFunctionDefinitionsResponseTypeDef",
    "ListGroupCertificateAuthoritiesRequestRequestTypeDef",
    "ListGroupCertificateAuthoritiesResponseTypeDef",
    "ListGroupVersionsRequestRequestTypeDef",
    "ListGroupVersionsResponseTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListGroupsResponseTypeDef",
    "ListLoggerDefinitionVersionsRequestRequestTypeDef",
    "ListLoggerDefinitionVersionsResponseTypeDef",
    "ListLoggerDefinitionsRequestRequestTypeDef",
    "ListLoggerDefinitionsResponseTypeDef",
    "ListResourceDefinitionVersionsRequestRequestTypeDef",
    "ListResourceDefinitionVersionsResponseTypeDef",
    "ListResourceDefinitionsRequestRequestTypeDef",
    "ListResourceDefinitionsResponseTypeDef",
    "ListSubscriptionDefinitionVersionsRequestRequestTypeDef",
    "ListSubscriptionDefinitionVersionsResponseTypeDef",
    "ListSubscriptionDefinitionsRequestRequestTypeDef",
    "ListSubscriptionDefinitionsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocalDeviceResourceDataTypeDef",
    "LocalVolumeResourceDataTypeDef",
    "LoggerDefinitionVersionTypeDef",
    "LoggerTypeDef",
    "PaginatorConfigTypeDef",
    "ResetDeploymentsRequestRequestTypeDef",
    "ResetDeploymentsResponseTypeDef",
    "ResourceAccessPolicyTypeDef",
    "ResourceDataContainerTypeDef",
    "ResourceDefinitionVersionTypeDef",
    "ResourceDownloadOwnerSettingTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RuntimeConfigurationTypeDef",
    "S3MachineLearningModelResourceDataTypeDef",
    "SageMakerMachineLearningModelResourceDataTypeDef",
    "SecretsManagerSecretResourceDataTypeDef",
    "StartBulkDeploymentRequestRequestTypeDef",
    "StartBulkDeploymentResponseTypeDef",
    "StopBulkDeploymentRequestRequestTypeDef",
    "SubscriptionDefinitionVersionTypeDef",
    "SubscriptionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TelemetryConfigurationTypeDef",
    "TelemetryConfigurationUpdateTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateConnectivityInfoRequestRequestTypeDef",
    "UpdateConnectivityInfoResponseTypeDef",
    "UpdateConnectorDefinitionRequestRequestTypeDef",
    "UpdateCoreDefinitionRequestRequestTypeDef",
    "UpdateDeviceDefinitionRequestRequestTypeDef",
    "UpdateFunctionDefinitionRequestRequestTypeDef",
    "UpdateGroupCertificateConfigurationRequestRequestTypeDef",
    "UpdateGroupCertificateConfigurationResponseTypeDef",
    "UpdateGroupRequestRequestTypeDef",
    "UpdateLoggerDefinitionRequestRequestTypeDef",
    "UpdateResourceDefinitionRequestRequestTypeDef",
    "UpdateSubscriptionDefinitionRequestRequestTypeDef",
    "UpdateThingRuntimeConfigurationRequestRequestTypeDef",
    "VersionInformationTypeDef",
)

AssociateRoleToGroupRequestRequestTypeDef = TypedDict(
    "AssociateRoleToGroupRequestRequestTypeDef",
    {
        "GroupId": str,
        "RoleArn": str,
    },
)

AssociateRoleToGroupResponseTypeDef = TypedDict(
    "AssociateRoleToGroupResponseTypeDef",
    {
        "AssociatedAt": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateServiceRoleToAccountRequestRequestTypeDef = TypedDict(
    "AssociateServiceRoleToAccountRequestRequestTypeDef",
    {
        "RoleArn": str,
    },
)

AssociateServiceRoleToAccountResponseTypeDef = TypedDict(
    "AssociateServiceRoleToAccountResponseTypeDef",
    {
        "AssociatedAt": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BulkDeploymentMetricsTypeDef = TypedDict(
    "BulkDeploymentMetricsTypeDef",
    {
        "InvalidInputRecords": NotRequired[int],
        "RecordsProcessed": NotRequired[int],
        "RetryAttempts": NotRequired[int],
    },
)

BulkDeploymentResultTypeDef = TypedDict(
    "BulkDeploymentResultTypeDef",
    {
        "CreatedAt": NotRequired[str],
        "DeploymentArn": NotRequired[str],
        "DeploymentId": NotRequired[str],
        "DeploymentStatus": NotRequired[str],
        "DeploymentType": NotRequired[DeploymentTypeType],
        "ErrorDetails": NotRequired[List["ErrorDetailTypeDef"]],
        "ErrorMessage": NotRequired[str],
        "GroupArn": NotRequired[str],
    },
)

BulkDeploymentTypeDef = TypedDict(
    "BulkDeploymentTypeDef",
    {
        "BulkDeploymentArn": NotRequired[str],
        "BulkDeploymentId": NotRequired[str],
        "CreatedAt": NotRequired[str],
    },
)

ConnectivityInfoTypeDef = TypedDict(
    "ConnectivityInfoTypeDef",
    {
        "HostAddress": NotRequired[str],
        "Id": NotRequired[str],
        "Metadata": NotRequired[str],
        "PortNumber": NotRequired[int],
    },
)

ConnectorDefinitionVersionTypeDef = TypedDict(
    "ConnectorDefinitionVersionTypeDef",
    {
        "Connectors": NotRequired[Sequence["ConnectorTypeDef"]],
    },
)

ConnectorTypeDef = TypedDict(
    "ConnectorTypeDef",
    {
        "ConnectorArn": str,
        "Id": str,
        "Parameters": NotRequired[Mapping[str, str]],
    },
)

CoreDefinitionVersionTypeDef = TypedDict(
    "CoreDefinitionVersionTypeDef",
    {
        "Cores": NotRequired[Sequence["CoreTypeDef"]],
    },
)

CoreTypeDef = TypedDict(
    "CoreTypeDef",
    {
        "CertificateArn": str,
        "Id": str,
        "ThingArn": str,
        "SyncShadow": NotRequired[bool],
    },
)

CreateConnectorDefinitionRequestRequestTypeDef = TypedDict(
    "CreateConnectorDefinitionRequestRequestTypeDef",
    {
        "AmznClientToken": NotRequired[str],
        "InitialVersion": NotRequired["ConnectorDefinitionVersionTypeDef"],
        "Name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateConnectorDefinitionResponseTypeDef = TypedDict(
    "CreateConnectorDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConnectorDefinitionVersionRequestRequestTypeDef = TypedDict(
    "CreateConnectorDefinitionVersionRequestRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
        "AmznClientToken": NotRequired[str],
        "Connectors": NotRequired[Sequence["ConnectorTypeDef"]],
    },
)

CreateConnectorDefinitionVersionResponseTypeDef = TypedDict(
    "CreateConnectorDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCoreDefinitionRequestRequestTypeDef = TypedDict(
    "CreateCoreDefinitionRequestRequestTypeDef",
    {
        "AmznClientToken": NotRequired[str],
        "InitialVersion": NotRequired["CoreDefinitionVersionTypeDef"],
        "Name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateCoreDefinitionResponseTypeDef = TypedDict(
    "CreateCoreDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCoreDefinitionVersionRequestRequestTypeDef = TypedDict(
    "CreateCoreDefinitionVersionRequestRequestTypeDef",
    {
        "CoreDefinitionId": str,
        "AmznClientToken": NotRequired[str],
        "Cores": NotRequired[Sequence["CoreTypeDef"]],
    },
)

CreateCoreDefinitionVersionResponseTypeDef = TypedDict(
    "CreateCoreDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDeploymentRequestRequestTypeDef = TypedDict(
    "CreateDeploymentRequestRequestTypeDef",
    {
        "DeploymentType": DeploymentTypeType,
        "GroupId": str,
        "AmznClientToken": NotRequired[str],
        "DeploymentId": NotRequired[str],
        "GroupVersionId": NotRequired[str],
    },
)

CreateDeploymentResponseTypeDef = TypedDict(
    "CreateDeploymentResponseTypeDef",
    {
        "DeploymentArn": str,
        "DeploymentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDeviceDefinitionRequestRequestTypeDef = TypedDict(
    "CreateDeviceDefinitionRequestRequestTypeDef",
    {
        "AmznClientToken": NotRequired[str],
        "InitialVersion": NotRequired["DeviceDefinitionVersionTypeDef"],
        "Name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateDeviceDefinitionResponseTypeDef = TypedDict(
    "CreateDeviceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDeviceDefinitionVersionRequestRequestTypeDef = TypedDict(
    "CreateDeviceDefinitionVersionRequestRequestTypeDef",
    {
        "DeviceDefinitionId": str,
        "AmznClientToken": NotRequired[str],
        "Devices": NotRequired[Sequence["DeviceTypeDef"]],
    },
)

CreateDeviceDefinitionVersionResponseTypeDef = TypedDict(
    "CreateDeviceDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFunctionDefinitionRequestRequestTypeDef = TypedDict(
    "CreateFunctionDefinitionRequestRequestTypeDef",
    {
        "AmznClientToken": NotRequired[str],
        "InitialVersion": NotRequired["FunctionDefinitionVersionTypeDef"],
        "Name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateFunctionDefinitionResponseTypeDef = TypedDict(
    "CreateFunctionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFunctionDefinitionVersionRequestRequestTypeDef = TypedDict(
    "CreateFunctionDefinitionVersionRequestRequestTypeDef",
    {
        "FunctionDefinitionId": str,
        "AmznClientToken": NotRequired[str],
        "DefaultConfig": NotRequired["FunctionDefaultConfigTypeDef"],
        "Functions": NotRequired[Sequence["FunctionTypeDef"]],
    },
)

CreateFunctionDefinitionVersionResponseTypeDef = TypedDict(
    "CreateFunctionDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGroupCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "CreateGroupCertificateAuthorityRequestRequestTypeDef",
    {
        "GroupId": str,
        "AmznClientToken": NotRequired[str],
    },
)

CreateGroupCertificateAuthorityResponseTypeDef = TypedDict(
    "CreateGroupCertificateAuthorityResponseTypeDef",
    {
        "GroupCertificateAuthorityArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGroupRequestRequestTypeDef = TypedDict(
    "CreateGroupRequestRequestTypeDef",
    {
        "Name": str,
        "AmznClientToken": NotRequired[str],
        "InitialVersion": NotRequired["GroupVersionTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGroupVersionRequestRequestTypeDef = TypedDict(
    "CreateGroupVersionRequestRequestTypeDef",
    {
        "GroupId": str,
        "AmznClientToken": NotRequired[str],
        "ConnectorDefinitionVersionArn": NotRequired[str],
        "CoreDefinitionVersionArn": NotRequired[str],
        "DeviceDefinitionVersionArn": NotRequired[str],
        "FunctionDefinitionVersionArn": NotRequired[str],
        "LoggerDefinitionVersionArn": NotRequired[str],
        "ResourceDefinitionVersionArn": NotRequired[str],
        "SubscriptionDefinitionVersionArn": NotRequired[str],
    },
)

CreateGroupVersionResponseTypeDef = TypedDict(
    "CreateGroupVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLoggerDefinitionRequestRequestTypeDef = TypedDict(
    "CreateLoggerDefinitionRequestRequestTypeDef",
    {
        "AmznClientToken": NotRequired[str],
        "InitialVersion": NotRequired["LoggerDefinitionVersionTypeDef"],
        "Name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateLoggerDefinitionResponseTypeDef = TypedDict(
    "CreateLoggerDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLoggerDefinitionVersionRequestRequestTypeDef = TypedDict(
    "CreateLoggerDefinitionVersionRequestRequestTypeDef",
    {
        "LoggerDefinitionId": str,
        "AmznClientToken": NotRequired[str],
        "Loggers": NotRequired[Sequence["LoggerTypeDef"]],
    },
)

CreateLoggerDefinitionVersionResponseTypeDef = TypedDict(
    "CreateLoggerDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResourceDefinitionRequestRequestTypeDef = TypedDict(
    "CreateResourceDefinitionRequestRequestTypeDef",
    {
        "AmznClientToken": NotRequired[str],
        "InitialVersion": NotRequired["ResourceDefinitionVersionTypeDef"],
        "Name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateResourceDefinitionResponseTypeDef = TypedDict(
    "CreateResourceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResourceDefinitionVersionRequestRequestTypeDef = TypedDict(
    "CreateResourceDefinitionVersionRequestRequestTypeDef",
    {
        "ResourceDefinitionId": str,
        "AmznClientToken": NotRequired[str],
        "Resources": NotRequired[Sequence["ResourceTypeDef"]],
    },
)

CreateResourceDefinitionVersionResponseTypeDef = TypedDict(
    "CreateResourceDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSoftwareUpdateJobRequestRequestTypeDef = TypedDict(
    "CreateSoftwareUpdateJobRequestRequestTypeDef",
    {
        "S3UrlSignerRole": str,
        "SoftwareToUpdate": SoftwareToUpdateType,
        "UpdateTargets": Sequence[str],
        "UpdateTargetsArchitecture": UpdateTargetsArchitectureType,
        "UpdateTargetsOperatingSystem": UpdateTargetsOperatingSystemType,
        "AmznClientToken": NotRequired[str],
        "UpdateAgentLogLevel": NotRequired[UpdateAgentLogLevelType],
    },
)

CreateSoftwareUpdateJobResponseTypeDef = TypedDict(
    "CreateSoftwareUpdateJobResponseTypeDef",
    {
        "IotJobArn": str,
        "IotJobId": str,
        "PlatformSoftwareVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSubscriptionDefinitionRequestRequestTypeDef = TypedDict(
    "CreateSubscriptionDefinitionRequestRequestTypeDef",
    {
        "AmznClientToken": NotRequired[str],
        "InitialVersion": NotRequired["SubscriptionDefinitionVersionTypeDef"],
        "Name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateSubscriptionDefinitionResponseTypeDef = TypedDict(
    "CreateSubscriptionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSubscriptionDefinitionVersionRequestRequestTypeDef = TypedDict(
    "CreateSubscriptionDefinitionVersionRequestRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
        "AmznClientToken": NotRequired[str],
        "Subscriptions": NotRequired[Sequence["SubscriptionTypeDef"]],
    },
)

CreateSubscriptionDefinitionVersionResponseTypeDef = TypedDict(
    "CreateSubscriptionDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefinitionInformationTypeDef = TypedDict(
    "DefinitionInformationTypeDef",
    {
        "Arn": NotRequired[str],
        "CreationTimestamp": NotRequired[str],
        "Id": NotRequired[str],
        "LastUpdatedTimestamp": NotRequired[str],
        "LatestVersion": NotRequired[str],
        "LatestVersionArn": NotRequired[str],
        "Name": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)

DeleteConnectorDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteConnectorDefinitionRequestRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
    },
)

DeleteCoreDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteCoreDefinitionRequestRequestTypeDef",
    {
        "CoreDefinitionId": str,
    },
)

DeleteDeviceDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteDeviceDefinitionRequestRequestTypeDef",
    {
        "DeviceDefinitionId": str,
    },
)

DeleteFunctionDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteFunctionDefinitionRequestRequestTypeDef",
    {
        "FunctionDefinitionId": str,
    },
)

DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)

DeleteLoggerDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteLoggerDefinitionRequestRequestTypeDef",
    {
        "LoggerDefinitionId": str,
    },
)

DeleteResourceDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteResourceDefinitionRequestRequestTypeDef",
    {
        "ResourceDefinitionId": str,
    },
)

DeleteSubscriptionDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteSubscriptionDefinitionRequestRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
    },
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "CreatedAt": NotRequired[str],
        "DeploymentArn": NotRequired[str],
        "DeploymentId": NotRequired[str],
        "DeploymentType": NotRequired[DeploymentTypeType],
        "GroupArn": NotRequired[str],
    },
)

DeviceDefinitionVersionTypeDef = TypedDict(
    "DeviceDefinitionVersionTypeDef",
    {
        "Devices": NotRequired[Sequence["DeviceTypeDef"]],
    },
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "CertificateArn": str,
        "Id": str,
        "ThingArn": str,
        "SyncShadow": NotRequired[bool],
    },
)

DisassociateRoleFromGroupRequestRequestTypeDef = TypedDict(
    "DisassociateRoleFromGroupRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)

DisassociateRoleFromGroupResponseTypeDef = TypedDict(
    "DisassociateRoleFromGroupResponseTypeDef",
    {
        "DisassociatedAt": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateServiceRoleFromAccountResponseTypeDef = TypedDict(
    "DisassociateServiceRoleFromAccountResponseTypeDef",
    {
        "DisassociatedAt": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "DetailedErrorCode": NotRequired[str],
        "DetailedErrorMessage": NotRequired[str],
    },
)

FunctionConfigurationEnvironmentTypeDef = TypedDict(
    "FunctionConfigurationEnvironmentTypeDef",
    {
        "AccessSysfs": NotRequired[bool],
        "Execution": NotRequired["FunctionExecutionConfigTypeDef"],
        "ResourceAccessPolicies": NotRequired[Sequence["ResourceAccessPolicyTypeDef"]],
        "Variables": NotRequired[Mapping[str, str]],
    },
)

FunctionConfigurationTypeDef = TypedDict(
    "FunctionConfigurationTypeDef",
    {
        "EncodingType": NotRequired[EncodingTypeType],
        "Environment": NotRequired["FunctionConfigurationEnvironmentTypeDef"],
        "ExecArgs": NotRequired[str],
        "Executable": NotRequired[str],
        "MemorySize": NotRequired[int],
        "Pinned": NotRequired[bool],
        "Timeout": NotRequired[int],
    },
)

FunctionDefaultConfigTypeDef = TypedDict(
    "FunctionDefaultConfigTypeDef",
    {
        "Execution": NotRequired["FunctionDefaultExecutionConfigTypeDef"],
    },
)

FunctionDefaultExecutionConfigTypeDef = TypedDict(
    "FunctionDefaultExecutionConfigTypeDef",
    {
        "IsolationMode": NotRequired[FunctionIsolationModeType],
        "RunAs": NotRequired["FunctionRunAsConfigTypeDef"],
    },
)

FunctionDefinitionVersionTypeDef = TypedDict(
    "FunctionDefinitionVersionTypeDef",
    {
        "DefaultConfig": NotRequired["FunctionDefaultConfigTypeDef"],
        "Functions": NotRequired[Sequence["FunctionTypeDef"]],
    },
)

FunctionExecutionConfigTypeDef = TypedDict(
    "FunctionExecutionConfigTypeDef",
    {
        "IsolationMode": NotRequired[FunctionIsolationModeType],
        "RunAs": NotRequired["FunctionRunAsConfigTypeDef"],
    },
)

FunctionRunAsConfigTypeDef = TypedDict(
    "FunctionRunAsConfigTypeDef",
    {
        "Gid": NotRequired[int],
        "Uid": NotRequired[int],
    },
)

FunctionTypeDef = TypedDict(
    "FunctionTypeDef",
    {
        "Id": str,
        "FunctionArn": NotRequired[str],
        "FunctionConfiguration": NotRequired["FunctionConfigurationTypeDef"],
    },
)

GetAssociatedRoleRequestRequestTypeDef = TypedDict(
    "GetAssociatedRoleRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)

GetAssociatedRoleResponseTypeDef = TypedDict(
    "GetAssociatedRoleResponseTypeDef",
    {
        "AssociatedAt": str,
        "RoleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBulkDeploymentStatusRequestRequestTypeDef = TypedDict(
    "GetBulkDeploymentStatusRequestRequestTypeDef",
    {
        "BulkDeploymentId": str,
    },
)

GetBulkDeploymentStatusResponseTypeDef = TypedDict(
    "GetBulkDeploymentStatusResponseTypeDef",
    {
        "BulkDeploymentMetrics": "BulkDeploymentMetricsTypeDef",
        "BulkDeploymentStatus": BulkDeploymentStatusType,
        "CreatedAt": str,
        "ErrorDetails": List["ErrorDetailTypeDef"],
        "ErrorMessage": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectivityInfoRequestRequestTypeDef = TypedDict(
    "GetConnectivityInfoRequestRequestTypeDef",
    {
        "ThingName": str,
    },
)

GetConnectivityInfoResponseTypeDef = TypedDict(
    "GetConnectivityInfoResponseTypeDef",
    {
        "ConnectivityInfo": List["ConnectivityInfoTypeDef"],
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectorDefinitionRequestRequestTypeDef = TypedDict(
    "GetConnectorDefinitionRequestRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
    },
)

GetConnectorDefinitionResponseTypeDef = TypedDict(
    "GetConnectorDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectorDefinitionVersionRequestRequestTypeDef = TypedDict(
    "GetConnectorDefinitionVersionRequestRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
        "ConnectorDefinitionVersionId": str,
        "NextToken": NotRequired[str],
    },
)

GetConnectorDefinitionVersionResponseTypeDef = TypedDict(
    "GetConnectorDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "ConnectorDefinitionVersionTypeDef",
        "Id": str,
        "NextToken": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCoreDefinitionRequestRequestTypeDef = TypedDict(
    "GetCoreDefinitionRequestRequestTypeDef",
    {
        "CoreDefinitionId": str,
    },
)

GetCoreDefinitionResponseTypeDef = TypedDict(
    "GetCoreDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCoreDefinitionVersionRequestRequestTypeDef = TypedDict(
    "GetCoreDefinitionVersionRequestRequestTypeDef",
    {
        "CoreDefinitionId": str,
        "CoreDefinitionVersionId": str,
    },
)

GetCoreDefinitionVersionResponseTypeDef = TypedDict(
    "GetCoreDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "CoreDefinitionVersionTypeDef",
        "Id": str,
        "NextToken": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentStatusRequestRequestTypeDef = TypedDict(
    "GetDeploymentStatusRequestRequestTypeDef",
    {
        "DeploymentId": str,
        "GroupId": str,
    },
)

GetDeploymentStatusResponseTypeDef = TypedDict(
    "GetDeploymentStatusResponseTypeDef",
    {
        "DeploymentStatus": str,
        "DeploymentType": DeploymentTypeType,
        "ErrorDetails": List["ErrorDetailTypeDef"],
        "ErrorMessage": str,
        "UpdatedAt": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeviceDefinitionRequestRequestTypeDef = TypedDict(
    "GetDeviceDefinitionRequestRequestTypeDef",
    {
        "DeviceDefinitionId": str,
    },
)

GetDeviceDefinitionResponseTypeDef = TypedDict(
    "GetDeviceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeviceDefinitionVersionRequestRequestTypeDef = TypedDict(
    "GetDeviceDefinitionVersionRequestRequestTypeDef",
    {
        "DeviceDefinitionId": str,
        "DeviceDefinitionVersionId": str,
        "NextToken": NotRequired[str],
    },
)

GetDeviceDefinitionVersionResponseTypeDef = TypedDict(
    "GetDeviceDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "DeviceDefinitionVersionTypeDef",
        "Id": str,
        "NextToken": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFunctionDefinitionRequestRequestTypeDef = TypedDict(
    "GetFunctionDefinitionRequestRequestTypeDef",
    {
        "FunctionDefinitionId": str,
    },
)

GetFunctionDefinitionResponseTypeDef = TypedDict(
    "GetFunctionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFunctionDefinitionVersionRequestRequestTypeDef = TypedDict(
    "GetFunctionDefinitionVersionRequestRequestTypeDef",
    {
        "FunctionDefinitionId": str,
        "FunctionDefinitionVersionId": str,
        "NextToken": NotRequired[str],
    },
)

GetFunctionDefinitionVersionResponseTypeDef = TypedDict(
    "GetFunctionDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "FunctionDefinitionVersionTypeDef",
        "Id": str,
        "NextToken": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "GetGroupCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityId": str,
        "GroupId": str,
    },
)

GetGroupCertificateAuthorityResponseTypeDef = TypedDict(
    "GetGroupCertificateAuthorityResponseTypeDef",
    {
        "GroupCertificateAuthorityArn": str,
        "GroupCertificateAuthorityId": str,
        "PemEncodedCertificate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupCertificateConfigurationRequestRequestTypeDef = TypedDict(
    "GetGroupCertificateConfigurationRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)

GetGroupCertificateConfigurationResponseTypeDef = TypedDict(
    "GetGroupCertificateConfigurationResponseTypeDef",
    {
        "CertificateAuthorityExpiryInMilliseconds": str,
        "CertificateExpiryInMilliseconds": str,
        "GroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupRequestRequestTypeDef = TypedDict(
    "GetGroupRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)

GetGroupResponseTypeDef = TypedDict(
    "GetGroupResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupVersionRequestRequestTypeDef = TypedDict(
    "GetGroupVersionRequestRequestTypeDef",
    {
        "GroupId": str,
        "GroupVersionId": str,
    },
)

GetGroupVersionResponseTypeDef = TypedDict(
    "GetGroupVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "GroupVersionTypeDef",
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoggerDefinitionRequestRequestTypeDef = TypedDict(
    "GetLoggerDefinitionRequestRequestTypeDef",
    {
        "LoggerDefinitionId": str,
    },
)

GetLoggerDefinitionResponseTypeDef = TypedDict(
    "GetLoggerDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoggerDefinitionVersionRequestRequestTypeDef = TypedDict(
    "GetLoggerDefinitionVersionRequestRequestTypeDef",
    {
        "LoggerDefinitionId": str,
        "LoggerDefinitionVersionId": str,
        "NextToken": NotRequired[str],
    },
)

GetLoggerDefinitionVersionResponseTypeDef = TypedDict(
    "GetLoggerDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "LoggerDefinitionVersionTypeDef",
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceDefinitionRequestRequestTypeDef = TypedDict(
    "GetResourceDefinitionRequestRequestTypeDef",
    {
        "ResourceDefinitionId": str,
    },
)

GetResourceDefinitionResponseTypeDef = TypedDict(
    "GetResourceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceDefinitionVersionRequestRequestTypeDef = TypedDict(
    "GetResourceDefinitionVersionRequestRequestTypeDef",
    {
        "ResourceDefinitionId": str,
        "ResourceDefinitionVersionId": str,
    },
)

GetResourceDefinitionVersionResponseTypeDef = TypedDict(
    "GetResourceDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "ResourceDefinitionVersionTypeDef",
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceRoleForAccountResponseTypeDef = TypedDict(
    "GetServiceRoleForAccountResponseTypeDef",
    {
        "AssociatedAt": str,
        "RoleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSubscriptionDefinitionRequestRequestTypeDef = TypedDict(
    "GetSubscriptionDefinitionRequestRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
    },
)

GetSubscriptionDefinitionResponseTypeDef = TypedDict(
    "GetSubscriptionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSubscriptionDefinitionVersionRequestRequestTypeDef = TypedDict(
    "GetSubscriptionDefinitionVersionRequestRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
        "SubscriptionDefinitionVersionId": str,
        "NextToken": NotRequired[str],
    },
)

GetSubscriptionDefinitionVersionResponseTypeDef = TypedDict(
    "GetSubscriptionDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "SubscriptionDefinitionVersionTypeDef",
        "Id": str,
        "NextToken": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetThingRuntimeConfigurationRequestRequestTypeDef = TypedDict(
    "GetThingRuntimeConfigurationRequestRequestTypeDef",
    {
        "ThingName": str,
    },
)

GetThingRuntimeConfigurationResponseTypeDef = TypedDict(
    "GetThingRuntimeConfigurationResponseTypeDef",
    {
        "RuntimeConfiguration": "RuntimeConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupCertificateAuthorityPropertiesTypeDef = TypedDict(
    "GroupCertificateAuthorityPropertiesTypeDef",
    {
        "GroupCertificateAuthorityArn": NotRequired[str],
        "GroupCertificateAuthorityId": NotRequired[str],
    },
)

GroupInformationTypeDef = TypedDict(
    "GroupInformationTypeDef",
    {
        "Arn": NotRequired[str],
        "CreationTimestamp": NotRequired[str],
        "Id": NotRequired[str],
        "LastUpdatedTimestamp": NotRequired[str],
        "LatestVersion": NotRequired[str],
        "LatestVersionArn": NotRequired[str],
        "Name": NotRequired[str],
    },
)

GroupOwnerSettingTypeDef = TypedDict(
    "GroupOwnerSettingTypeDef",
    {
        "AutoAddGroupOwner": NotRequired[bool],
        "GroupOwner": NotRequired[str],
    },
)

GroupVersionTypeDef = TypedDict(
    "GroupVersionTypeDef",
    {
        "ConnectorDefinitionVersionArn": NotRequired[str],
        "CoreDefinitionVersionArn": NotRequired[str],
        "DeviceDefinitionVersionArn": NotRequired[str],
        "FunctionDefinitionVersionArn": NotRequired[str],
        "LoggerDefinitionVersionArn": NotRequired[str],
        "ResourceDefinitionVersionArn": NotRequired[str],
        "SubscriptionDefinitionVersionArn": NotRequired[str],
    },
)

ListBulkDeploymentDetailedReportsRequestRequestTypeDef = TypedDict(
    "ListBulkDeploymentDetailedReportsRequestRequestTypeDef",
    {
        "BulkDeploymentId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

ListBulkDeploymentDetailedReportsResponseTypeDef = TypedDict(
    "ListBulkDeploymentDetailedReportsResponseTypeDef",
    {
        "Deployments": List["BulkDeploymentResultTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBulkDeploymentsRequestRequestTypeDef = TypedDict(
    "ListBulkDeploymentsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

ListBulkDeploymentsResponseTypeDef = TypedDict(
    "ListBulkDeploymentsResponseTypeDef",
    {
        "BulkDeployments": List["BulkDeploymentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConnectorDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "ListConnectorDefinitionVersionsRequestRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

ListConnectorDefinitionVersionsResponseTypeDef = TypedDict(
    "ListConnectorDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConnectorDefinitionsRequestRequestTypeDef = TypedDict(
    "ListConnectorDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

ListConnectorDefinitionsResponseTypeDef = TypedDict(
    "ListConnectorDefinitionsResponseTypeDef",
    {
        "Definitions": List["DefinitionInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCoreDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "ListCoreDefinitionVersionsRequestRequestTypeDef",
    {
        "CoreDefinitionId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

ListCoreDefinitionVersionsResponseTypeDef = TypedDict(
    "ListCoreDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCoreDefinitionsRequestRequestTypeDef = TypedDict(
    "ListCoreDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

ListCoreDefinitionsResponseTypeDef = TypedDict(
    "ListCoreDefinitionsResponseTypeDef",
    {
        "Definitions": List["DefinitionInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeploymentsRequestRequestTypeDef = TypedDict(
    "ListDeploymentsRequestRequestTypeDef",
    {
        "GroupId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

ListDeploymentsResponseTypeDef = TypedDict(
    "ListDeploymentsResponseTypeDef",
    {
        "Deployments": List["DeploymentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeviceDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "ListDeviceDefinitionVersionsRequestRequestTypeDef",
    {
        "DeviceDefinitionId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

ListDeviceDefinitionVersionsResponseTypeDef = TypedDict(
    "ListDeviceDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeviceDefinitionsRequestRequestTypeDef = TypedDict(
    "ListDeviceDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

ListDeviceDefinitionsResponseTypeDef = TypedDict(
    "ListDeviceDefinitionsResponseTypeDef",
    {
        "Definitions": List["DefinitionInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFunctionDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "ListFunctionDefinitionVersionsRequestRequestTypeDef",
    {
        "FunctionDefinitionId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

ListFunctionDefinitionVersionsResponseTypeDef = TypedDict(
    "ListFunctionDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFunctionDefinitionsRequestRequestTypeDef = TypedDict(
    "ListFunctionDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

ListFunctionDefinitionsResponseTypeDef = TypedDict(
    "ListFunctionDefinitionsResponseTypeDef",
    {
        "Definitions": List["DefinitionInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroupCertificateAuthoritiesRequestRequestTypeDef = TypedDict(
    "ListGroupCertificateAuthoritiesRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)

ListGroupCertificateAuthoritiesResponseTypeDef = TypedDict(
    "ListGroupCertificateAuthoritiesResponseTypeDef",
    {
        "GroupCertificateAuthorities": List["GroupCertificateAuthorityPropertiesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroupVersionsRequestRequestTypeDef = TypedDict(
    "ListGroupVersionsRequestRequestTypeDef",
    {
        "GroupId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

ListGroupVersionsResponseTypeDef = TypedDict(
    "ListGroupVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroupsRequestRequestTypeDef = TypedDict(
    "ListGroupsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "Groups": List["GroupInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLoggerDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "ListLoggerDefinitionVersionsRequestRequestTypeDef",
    {
        "LoggerDefinitionId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

ListLoggerDefinitionVersionsResponseTypeDef = TypedDict(
    "ListLoggerDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLoggerDefinitionsRequestRequestTypeDef = TypedDict(
    "ListLoggerDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

ListLoggerDefinitionsResponseTypeDef = TypedDict(
    "ListLoggerDefinitionsResponseTypeDef",
    {
        "Definitions": List["DefinitionInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "ListResourceDefinitionVersionsRequestRequestTypeDef",
    {
        "ResourceDefinitionId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

ListResourceDefinitionVersionsResponseTypeDef = TypedDict(
    "ListResourceDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceDefinitionsRequestRequestTypeDef = TypedDict(
    "ListResourceDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

ListResourceDefinitionsResponseTypeDef = TypedDict(
    "ListResourceDefinitionsResponseTypeDef",
    {
        "Definitions": List["DefinitionInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSubscriptionDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "ListSubscriptionDefinitionVersionsRequestRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

ListSubscriptionDefinitionVersionsResponseTypeDef = TypedDict(
    "ListSubscriptionDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSubscriptionDefinitionsRequestRequestTypeDef = TypedDict(
    "ListSubscriptionDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

ListSubscriptionDefinitionsResponseTypeDef = TypedDict(
    "ListSubscriptionDefinitionsResponseTypeDef",
    {
        "Definitions": List["DefinitionInformationTypeDef"],
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
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocalDeviceResourceDataTypeDef = TypedDict(
    "LocalDeviceResourceDataTypeDef",
    {
        "GroupOwnerSetting": NotRequired["GroupOwnerSettingTypeDef"],
        "SourcePath": NotRequired[str],
    },
)

LocalVolumeResourceDataTypeDef = TypedDict(
    "LocalVolumeResourceDataTypeDef",
    {
        "DestinationPath": NotRequired[str],
        "GroupOwnerSetting": NotRequired["GroupOwnerSettingTypeDef"],
        "SourcePath": NotRequired[str],
    },
)

LoggerDefinitionVersionTypeDef = TypedDict(
    "LoggerDefinitionVersionTypeDef",
    {
        "Loggers": NotRequired[Sequence["LoggerTypeDef"]],
    },
)

LoggerTypeDef = TypedDict(
    "LoggerTypeDef",
    {
        "Component": LoggerComponentType,
        "Id": str,
        "Level": LoggerLevelType,
        "Type": LoggerTypeType,
        "Space": NotRequired[int],
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

ResetDeploymentsRequestRequestTypeDef = TypedDict(
    "ResetDeploymentsRequestRequestTypeDef",
    {
        "GroupId": str,
        "AmznClientToken": NotRequired[str],
        "Force": NotRequired[bool],
    },
)

ResetDeploymentsResponseTypeDef = TypedDict(
    "ResetDeploymentsResponseTypeDef",
    {
        "DeploymentArn": str,
        "DeploymentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceAccessPolicyTypeDef = TypedDict(
    "ResourceAccessPolicyTypeDef",
    {
        "ResourceId": str,
        "Permission": NotRequired[PermissionType],
    },
)

ResourceDataContainerTypeDef = TypedDict(
    "ResourceDataContainerTypeDef",
    {
        "LocalDeviceResourceData": NotRequired["LocalDeviceResourceDataTypeDef"],
        "LocalVolumeResourceData": NotRequired["LocalVolumeResourceDataTypeDef"],
        "S3MachineLearningModelResourceData": NotRequired[
            "S3MachineLearningModelResourceDataTypeDef"
        ],
        "SageMakerMachineLearningModelResourceData": NotRequired[
            "SageMakerMachineLearningModelResourceDataTypeDef"
        ],
        "SecretsManagerSecretResourceData": NotRequired["SecretsManagerSecretResourceDataTypeDef"],
    },
)

ResourceDefinitionVersionTypeDef = TypedDict(
    "ResourceDefinitionVersionTypeDef",
    {
        "Resources": NotRequired[Sequence["ResourceTypeDef"]],
    },
)

ResourceDownloadOwnerSettingTypeDef = TypedDict(
    "ResourceDownloadOwnerSettingTypeDef",
    {
        "GroupOwner": str,
        "GroupPermission": PermissionType,
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Id": str,
        "Name": str,
        "ResourceDataContainer": "ResourceDataContainerTypeDef",
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

RuntimeConfigurationTypeDef = TypedDict(
    "RuntimeConfigurationTypeDef",
    {
        "TelemetryConfiguration": NotRequired["TelemetryConfigurationTypeDef"],
    },
)

S3MachineLearningModelResourceDataTypeDef = TypedDict(
    "S3MachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": NotRequired[str],
        "OwnerSetting": NotRequired["ResourceDownloadOwnerSettingTypeDef"],
        "S3Uri": NotRequired[str],
    },
)

SageMakerMachineLearningModelResourceDataTypeDef = TypedDict(
    "SageMakerMachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": NotRequired[str],
        "OwnerSetting": NotRequired["ResourceDownloadOwnerSettingTypeDef"],
        "SageMakerJobArn": NotRequired[str],
    },
)

SecretsManagerSecretResourceDataTypeDef = TypedDict(
    "SecretsManagerSecretResourceDataTypeDef",
    {
        "ARN": NotRequired[str],
        "AdditionalStagingLabelsToDownload": NotRequired[Sequence[str]],
    },
)

StartBulkDeploymentRequestRequestTypeDef = TypedDict(
    "StartBulkDeploymentRequestRequestTypeDef",
    {
        "ExecutionRoleArn": str,
        "InputFileUri": str,
        "AmznClientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

StartBulkDeploymentResponseTypeDef = TypedDict(
    "StartBulkDeploymentResponseTypeDef",
    {
        "BulkDeploymentArn": str,
        "BulkDeploymentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopBulkDeploymentRequestRequestTypeDef = TypedDict(
    "StopBulkDeploymentRequestRequestTypeDef",
    {
        "BulkDeploymentId": str,
    },
)

SubscriptionDefinitionVersionTypeDef = TypedDict(
    "SubscriptionDefinitionVersionTypeDef",
    {
        "Subscriptions": NotRequired[Sequence["SubscriptionTypeDef"]],
    },
)

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "Id": str,
        "Source": str,
        "Subject": str,
        "Target": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "tags": NotRequired[Mapping[str, str]],
    },
)

TelemetryConfigurationTypeDef = TypedDict(
    "TelemetryConfigurationTypeDef",
    {
        "Telemetry": TelemetryType,
        "ConfigurationSyncStatus": NotRequired[ConfigurationSyncStatusType],
    },
)

TelemetryConfigurationUpdateTypeDef = TypedDict(
    "TelemetryConfigurationUpdateTypeDef",
    {
        "Telemetry": TelemetryType,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateConnectivityInfoRequestRequestTypeDef = TypedDict(
    "UpdateConnectivityInfoRequestRequestTypeDef",
    {
        "ThingName": str,
        "ConnectivityInfo": NotRequired[Sequence["ConnectivityInfoTypeDef"]],
    },
)

UpdateConnectivityInfoResponseTypeDef = TypedDict(
    "UpdateConnectivityInfoResponseTypeDef",
    {
        "Message": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateConnectorDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateConnectorDefinitionRequestRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
        "Name": NotRequired[str],
    },
)

UpdateCoreDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateCoreDefinitionRequestRequestTypeDef",
    {
        "CoreDefinitionId": str,
        "Name": NotRequired[str],
    },
)

UpdateDeviceDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateDeviceDefinitionRequestRequestTypeDef",
    {
        "DeviceDefinitionId": str,
        "Name": NotRequired[str],
    },
)

UpdateFunctionDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateFunctionDefinitionRequestRequestTypeDef",
    {
        "FunctionDefinitionId": str,
        "Name": NotRequired[str],
    },
)

UpdateGroupCertificateConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateGroupCertificateConfigurationRequestRequestTypeDef",
    {
        "GroupId": str,
        "CertificateExpiryInMilliseconds": NotRequired[str],
    },
)

UpdateGroupCertificateConfigurationResponseTypeDef = TypedDict(
    "UpdateGroupCertificateConfigurationResponseTypeDef",
    {
        "CertificateAuthorityExpiryInMilliseconds": str,
        "CertificateExpiryInMilliseconds": str,
        "GroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGroupRequestRequestTypeDef = TypedDict(
    "UpdateGroupRequestRequestTypeDef",
    {
        "GroupId": str,
        "Name": NotRequired[str],
    },
)

UpdateLoggerDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateLoggerDefinitionRequestRequestTypeDef",
    {
        "LoggerDefinitionId": str,
        "Name": NotRequired[str],
    },
)

UpdateResourceDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateResourceDefinitionRequestRequestTypeDef",
    {
        "ResourceDefinitionId": str,
        "Name": NotRequired[str],
    },
)

UpdateSubscriptionDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateSubscriptionDefinitionRequestRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
        "Name": NotRequired[str],
    },
)

UpdateThingRuntimeConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateThingRuntimeConfigurationRequestRequestTypeDef",
    {
        "ThingName": str,
        "TelemetryConfiguration": NotRequired["TelemetryConfigurationUpdateTypeDef"],
    },
)

VersionInformationTypeDef = TypedDict(
    "VersionInformationTypeDef",
    {
        "Arn": NotRequired[str],
        "CreationTimestamp": NotRequired[str],
        "Id": NotRequired[str],
        "Version": NotRequired[str],
    },
)
