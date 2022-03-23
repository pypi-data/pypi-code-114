"""
Type annotations for proton service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_proton/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_proton.type_defs import AcceptEnvironmentAccountConnectionInputRequestTypeDef

    data: AcceptEnvironmentAccountConnectionInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    DeploymentStatusType,
    DeploymentUpdateTypeType,
    EnvironmentAccountConnectionRequesterAccountTypeType,
    EnvironmentAccountConnectionStatusType,
    ProvisionedResourceEngineType,
    RepositoryProviderType,
    RepositorySyncStatusType,
    ResourceDeploymentStatusType,
    ResourceSyncStatusType,
    ServiceStatusType,
    TemplateTypeType,
    TemplateVersionStatusType,
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
    "AcceptEnvironmentAccountConnectionInputRequestTypeDef",
    "AcceptEnvironmentAccountConnectionOutputTypeDef",
    "AccountSettingsTypeDef",
    "CancelEnvironmentDeploymentInputRequestTypeDef",
    "CancelEnvironmentDeploymentOutputTypeDef",
    "CancelServiceInstanceDeploymentInputRequestTypeDef",
    "CancelServiceInstanceDeploymentOutputTypeDef",
    "CancelServicePipelineDeploymentInputRequestTypeDef",
    "CancelServicePipelineDeploymentOutputTypeDef",
    "CompatibleEnvironmentTemplateInputTypeDef",
    "CompatibleEnvironmentTemplateTypeDef",
    "CreateEnvironmentAccountConnectionInputRequestTypeDef",
    "CreateEnvironmentAccountConnectionOutputTypeDef",
    "CreateEnvironmentInputRequestTypeDef",
    "CreateEnvironmentOutputTypeDef",
    "CreateEnvironmentTemplateInputRequestTypeDef",
    "CreateEnvironmentTemplateOutputTypeDef",
    "CreateEnvironmentTemplateVersionInputRequestTypeDef",
    "CreateEnvironmentTemplateVersionOutputTypeDef",
    "CreateRepositoryInputRequestTypeDef",
    "CreateRepositoryOutputTypeDef",
    "CreateServiceInputRequestTypeDef",
    "CreateServiceOutputTypeDef",
    "CreateServiceTemplateInputRequestTypeDef",
    "CreateServiceTemplateOutputTypeDef",
    "CreateServiceTemplateVersionInputRequestTypeDef",
    "CreateServiceTemplateVersionOutputTypeDef",
    "CreateTemplateSyncConfigInputRequestTypeDef",
    "CreateTemplateSyncConfigOutputTypeDef",
    "DeleteEnvironmentAccountConnectionInputRequestTypeDef",
    "DeleteEnvironmentAccountConnectionOutputTypeDef",
    "DeleteEnvironmentInputRequestTypeDef",
    "DeleteEnvironmentOutputTypeDef",
    "DeleteEnvironmentTemplateInputRequestTypeDef",
    "DeleteEnvironmentTemplateOutputTypeDef",
    "DeleteEnvironmentTemplateVersionInputRequestTypeDef",
    "DeleteEnvironmentTemplateVersionOutputTypeDef",
    "DeleteRepositoryInputRequestTypeDef",
    "DeleteRepositoryOutputTypeDef",
    "DeleteServiceInputRequestTypeDef",
    "DeleteServiceOutputTypeDef",
    "DeleteServiceTemplateInputRequestTypeDef",
    "DeleteServiceTemplateOutputTypeDef",
    "DeleteServiceTemplateVersionInputRequestTypeDef",
    "DeleteServiceTemplateVersionOutputTypeDef",
    "DeleteTemplateSyncConfigInputRequestTypeDef",
    "DeleteTemplateSyncConfigOutputTypeDef",
    "EnvironmentAccountConnectionSummaryTypeDef",
    "EnvironmentAccountConnectionTypeDef",
    "EnvironmentSummaryTypeDef",
    "EnvironmentTemplateFilterTypeDef",
    "EnvironmentTemplateSummaryTypeDef",
    "EnvironmentTemplateTypeDef",
    "EnvironmentTemplateVersionSummaryTypeDef",
    "EnvironmentTemplateVersionTypeDef",
    "EnvironmentTypeDef",
    "GetAccountSettingsOutputTypeDef",
    "GetEnvironmentAccountConnectionInputRequestTypeDef",
    "GetEnvironmentAccountConnectionOutputTypeDef",
    "GetEnvironmentInputRequestTypeDef",
    "GetEnvironmentOutputTypeDef",
    "GetEnvironmentTemplateInputRequestTypeDef",
    "GetEnvironmentTemplateOutputTypeDef",
    "GetEnvironmentTemplateVersionInputRequestTypeDef",
    "GetEnvironmentTemplateVersionOutputTypeDef",
    "GetRepositoryInputRequestTypeDef",
    "GetRepositoryOutputTypeDef",
    "GetRepositorySyncStatusInputRequestTypeDef",
    "GetRepositorySyncStatusOutputTypeDef",
    "GetServiceInputRequestTypeDef",
    "GetServiceInstanceInputRequestTypeDef",
    "GetServiceInstanceOutputTypeDef",
    "GetServiceOutputTypeDef",
    "GetServiceTemplateInputRequestTypeDef",
    "GetServiceTemplateOutputTypeDef",
    "GetServiceTemplateVersionInputRequestTypeDef",
    "GetServiceTemplateVersionOutputTypeDef",
    "GetTemplateSyncConfigInputRequestTypeDef",
    "GetTemplateSyncConfigOutputTypeDef",
    "GetTemplateSyncStatusInputRequestTypeDef",
    "GetTemplateSyncStatusOutputTypeDef",
    "ListEnvironmentAccountConnectionsInputRequestTypeDef",
    "ListEnvironmentAccountConnectionsOutputTypeDef",
    "ListEnvironmentOutputsInputRequestTypeDef",
    "ListEnvironmentOutputsOutputTypeDef",
    "ListEnvironmentProvisionedResourcesInputRequestTypeDef",
    "ListEnvironmentProvisionedResourcesOutputTypeDef",
    "ListEnvironmentTemplateVersionsInputRequestTypeDef",
    "ListEnvironmentTemplateVersionsOutputTypeDef",
    "ListEnvironmentTemplatesInputRequestTypeDef",
    "ListEnvironmentTemplatesOutputTypeDef",
    "ListEnvironmentsInputRequestTypeDef",
    "ListEnvironmentsOutputTypeDef",
    "ListRepositoriesInputRequestTypeDef",
    "ListRepositoriesOutputTypeDef",
    "ListRepositorySyncDefinitionsInputRequestTypeDef",
    "ListRepositorySyncDefinitionsOutputTypeDef",
    "ListServiceInstanceOutputsInputRequestTypeDef",
    "ListServiceInstanceOutputsOutputTypeDef",
    "ListServiceInstanceProvisionedResourcesInputRequestTypeDef",
    "ListServiceInstanceProvisionedResourcesOutputTypeDef",
    "ListServiceInstancesInputRequestTypeDef",
    "ListServiceInstancesOutputTypeDef",
    "ListServicePipelineOutputsInputRequestTypeDef",
    "ListServicePipelineOutputsOutputTypeDef",
    "ListServicePipelineProvisionedResourcesInputRequestTypeDef",
    "ListServicePipelineProvisionedResourcesOutputTypeDef",
    "ListServiceTemplateVersionsInputRequestTypeDef",
    "ListServiceTemplateVersionsOutputTypeDef",
    "ListServiceTemplatesInputRequestTypeDef",
    "ListServiceTemplatesOutputTypeDef",
    "ListServicesInputRequestTypeDef",
    "ListServicesOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "NotifyResourceDeploymentStatusChangeInputRequestTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "ProvisionedResourceTypeDef",
    "RejectEnvironmentAccountConnectionInputRequestTypeDef",
    "RejectEnvironmentAccountConnectionOutputTypeDef",
    "RepositoryBranchInputTypeDef",
    "RepositoryBranchTypeDef",
    "RepositorySummaryTypeDef",
    "RepositorySyncAttemptTypeDef",
    "RepositorySyncDefinitionTypeDef",
    "RepositorySyncEventTypeDef",
    "RepositoryTypeDef",
    "ResourceSyncAttemptTypeDef",
    "ResourceSyncEventTypeDef",
    "ResponseMetadataTypeDef",
    "RevisionTypeDef",
    "S3ObjectSourceTypeDef",
    "ServiceInstanceSummaryTypeDef",
    "ServiceInstanceTypeDef",
    "ServicePipelineTypeDef",
    "ServiceSummaryTypeDef",
    "ServiceTemplateSummaryTypeDef",
    "ServiceTemplateTypeDef",
    "ServiceTemplateVersionSummaryTypeDef",
    "ServiceTemplateVersionTypeDef",
    "ServiceTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagTypeDef",
    "TemplateSyncConfigTypeDef",
    "TemplateVersionSourceInputTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateAccountSettingsInputRequestTypeDef",
    "UpdateAccountSettingsOutputTypeDef",
    "UpdateEnvironmentAccountConnectionInputRequestTypeDef",
    "UpdateEnvironmentAccountConnectionOutputTypeDef",
    "UpdateEnvironmentInputRequestTypeDef",
    "UpdateEnvironmentOutputTypeDef",
    "UpdateEnvironmentTemplateInputRequestTypeDef",
    "UpdateEnvironmentTemplateOutputTypeDef",
    "UpdateEnvironmentTemplateVersionInputRequestTypeDef",
    "UpdateEnvironmentTemplateVersionOutputTypeDef",
    "UpdateServiceInputRequestTypeDef",
    "UpdateServiceInstanceInputRequestTypeDef",
    "UpdateServiceInstanceOutputTypeDef",
    "UpdateServiceOutputTypeDef",
    "UpdateServicePipelineInputRequestTypeDef",
    "UpdateServicePipelineOutputTypeDef",
    "UpdateServiceTemplateInputRequestTypeDef",
    "UpdateServiceTemplateOutputTypeDef",
    "UpdateServiceTemplateVersionInputRequestTypeDef",
    "UpdateServiceTemplateVersionOutputTypeDef",
    "UpdateTemplateSyncConfigInputRequestTypeDef",
    "UpdateTemplateSyncConfigOutputTypeDef",
    "WaiterConfigTypeDef",
)

AcceptEnvironmentAccountConnectionInputRequestTypeDef = TypedDict(
    "AcceptEnvironmentAccountConnectionInputRequestTypeDef",
    {
        "id": str,
    },
)

AcceptEnvironmentAccountConnectionOutputTypeDef = TypedDict(
    "AcceptEnvironmentAccountConnectionOutputTypeDef",
    {
        "environmentAccountConnection": "EnvironmentAccountConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "pipelineProvisioningRepository": NotRequired["RepositoryBranchTypeDef"],
        "pipelineServiceRoleArn": NotRequired[str],
    },
)

CancelEnvironmentDeploymentInputRequestTypeDef = TypedDict(
    "CancelEnvironmentDeploymentInputRequestTypeDef",
    {
        "environmentName": str,
    },
)

CancelEnvironmentDeploymentOutputTypeDef = TypedDict(
    "CancelEnvironmentDeploymentOutputTypeDef",
    {
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelServiceInstanceDeploymentInputRequestTypeDef = TypedDict(
    "CancelServiceInstanceDeploymentInputRequestTypeDef",
    {
        "serviceInstanceName": str,
        "serviceName": str,
    },
)

CancelServiceInstanceDeploymentOutputTypeDef = TypedDict(
    "CancelServiceInstanceDeploymentOutputTypeDef",
    {
        "serviceInstance": "ServiceInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelServicePipelineDeploymentInputRequestTypeDef = TypedDict(
    "CancelServicePipelineDeploymentInputRequestTypeDef",
    {
        "serviceName": str,
    },
)

CancelServicePipelineDeploymentOutputTypeDef = TypedDict(
    "CancelServicePipelineDeploymentOutputTypeDef",
    {
        "pipeline": "ServicePipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CompatibleEnvironmentTemplateInputTypeDef = TypedDict(
    "CompatibleEnvironmentTemplateInputTypeDef",
    {
        "majorVersion": str,
        "templateName": str,
    },
)

CompatibleEnvironmentTemplateTypeDef = TypedDict(
    "CompatibleEnvironmentTemplateTypeDef",
    {
        "majorVersion": str,
        "templateName": str,
    },
)

CreateEnvironmentAccountConnectionInputRequestTypeDef = TypedDict(
    "CreateEnvironmentAccountConnectionInputRequestTypeDef",
    {
        "environmentName": str,
        "managementAccountId": str,
        "roleArn": str,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateEnvironmentAccountConnectionOutputTypeDef = TypedDict(
    "CreateEnvironmentAccountConnectionOutputTypeDef",
    {
        "environmentAccountConnection": "EnvironmentAccountConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEnvironmentInputRequestTypeDef = TypedDict(
    "CreateEnvironmentInputRequestTypeDef",
    {
        "name": str,
        "spec": str,
        "templateMajorVersion": str,
        "templateName": str,
        "description": NotRequired[str],
        "environmentAccountConnectionId": NotRequired[str],
        "protonServiceRoleArn": NotRequired[str],
        "provisioningRepository": NotRequired["RepositoryBranchInputTypeDef"],
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "templateMinorVersion": NotRequired[str],
    },
)

CreateEnvironmentOutputTypeDef = TypedDict(
    "CreateEnvironmentOutputTypeDef",
    {
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEnvironmentTemplateInputRequestTypeDef = TypedDict(
    "CreateEnvironmentTemplateInputRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "encryptionKey": NotRequired[str],
        "provisioning": NotRequired[Literal["CUSTOMER_MANAGED"]],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateEnvironmentTemplateOutputTypeDef = TypedDict(
    "CreateEnvironmentTemplateOutputTypeDef",
    {
        "environmentTemplate": "EnvironmentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEnvironmentTemplateVersionInputRequestTypeDef = TypedDict(
    "CreateEnvironmentTemplateVersionInputRequestTypeDef",
    {
        "source": "TemplateVersionSourceInputTypeDef",
        "templateName": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "majorVersion": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateEnvironmentTemplateVersionOutputTypeDef = TypedDict(
    "CreateEnvironmentTemplateVersionOutputTypeDef",
    {
        "environmentTemplateVersion": "EnvironmentTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRepositoryInputRequestTypeDef = TypedDict(
    "CreateRepositoryInputRequestTypeDef",
    {
        "connectionArn": str,
        "name": str,
        "provider": RepositoryProviderType,
        "encryptionKey": NotRequired[str],
    },
)

CreateRepositoryOutputTypeDef = TypedDict(
    "CreateRepositoryOutputTypeDef",
    {
        "repository": "RepositoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateServiceInputRequestTypeDef = TypedDict(
    "CreateServiceInputRequestTypeDef",
    {
        "name": str,
        "spec": str,
        "templateMajorVersion": str,
        "templateName": str,
        "branchName": NotRequired[str],
        "description": NotRequired[str],
        "repositoryConnectionArn": NotRequired[str],
        "repositoryId": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "templateMinorVersion": NotRequired[str],
    },
)

CreateServiceOutputTypeDef = TypedDict(
    "CreateServiceOutputTypeDef",
    {
        "service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateServiceTemplateInputRequestTypeDef = TypedDict(
    "CreateServiceTemplateInputRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "encryptionKey": NotRequired[str],
        "pipelineProvisioning": NotRequired[Literal["CUSTOMER_MANAGED"]],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateServiceTemplateOutputTypeDef = TypedDict(
    "CreateServiceTemplateOutputTypeDef",
    {
        "serviceTemplate": "ServiceTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateServiceTemplateVersionInputRequestTypeDef = TypedDict(
    "CreateServiceTemplateVersionInputRequestTypeDef",
    {
        "compatibleEnvironmentTemplates": Sequence["CompatibleEnvironmentTemplateInputTypeDef"],
        "source": "TemplateVersionSourceInputTypeDef",
        "templateName": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "majorVersion": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateServiceTemplateVersionOutputTypeDef = TypedDict(
    "CreateServiceTemplateVersionOutputTypeDef",
    {
        "serviceTemplateVersion": "ServiceTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTemplateSyncConfigInputRequestTypeDef = TypedDict(
    "CreateTemplateSyncConfigInputRequestTypeDef",
    {
        "branch": str,
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "templateName": str,
        "templateType": TemplateTypeType,
        "subdirectory": NotRequired[str],
    },
)

CreateTemplateSyncConfigOutputTypeDef = TypedDict(
    "CreateTemplateSyncConfigOutputTypeDef",
    {
        "templateSyncConfig": "TemplateSyncConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentAccountConnectionInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentAccountConnectionInputRequestTypeDef",
    {
        "id": str,
    },
)

DeleteEnvironmentAccountConnectionOutputTypeDef = TypedDict(
    "DeleteEnvironmentAccountConnectionOutputTypeDef",
    {
        "environmentAccountConnection": "EnvironmentAccountConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentInputRequestTypeDef",
    {
        "name": str,
    },
)

DeleteEnvironmentOutputTypeDef = TypedDict(
    "DeleteEnvironmentOutputTypeDef",
    {
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentTemplateInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentTemplateInputRequestTypeDef",
    {
        "name": str,
    },
)

DeleteEnvironmentTemplateOutputTypeDef = TypedDict(
    "DeleteEnvironmentTemplateOutputTypeDef",
    {
        "environmentTemplate": "EnvironmentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentTemplateVersionInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentTemplateVersionInputRequestTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
    },
)

DeleteEnvironmentTemplateVersionOutputTypeDef = TypedDict(
    "DeleteEnvironmentTemplateVersionOutputTypeDef",
    {
        "environmentTemplateVersion": "EnvironmentTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRepositoryInputRequestTypeDef = TypedDict(
    "DeleteRepositoryInputRequestTypeDef",
    {
        "name": str,
        "provider": RepositoryProviderType,
    },
)

DeleteRepositoryOutputTypeDef = TypedDict(
    "DeleteRepositoryOutputTypeDef",
    {
        "repository": "RepositoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceInputRequestTypeDef = TypedDict(
    "DeleteServiceInputRequestTypeDef",
    {
        "name": str,
    },
)

DeleteServiceOutputTypeDef = TypedDict(
    "DeleteServiceOutputTypeDef",
    {
        "service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceTemplateInputRequestTypeDef = TypedDict(
    "DeleteServiceTemplateInputRequestTypeDef",
    {
        "name": str,
    },
)

DeleteServiceTemplateOutputTypeDef = TypedDict(
    "DeleteServiceTemplateOutputTypeDef",
    {
        "serviceTemplate": "ServiceTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceTemplateVersionInputRequestTypeDef = TypedDict(
    "DeleteServiceTemplateVersionInputRequestTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
    },
)

DeleteServiceTemplateVersionOutputTypeDef = TypedDict(
    "DeleteServiceTemplateVersionOutputTypeDef",
    {
        "serviceTemplateVersion": "ServiceTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTemplateSyncConfigInputRequestTypeDef = TypedDict(
    "DeleteTemplateSyncConfigInputRequestTypeDef",
    {
        "templateName": str,
        "templateType": TemplateTypeType,
    },
)

DeleteTemplateSyncConfigOutputTypeDef = TypedDict(
    "DeleteTemplateSyncConfigOutputTypeDef",
    {
        "templateSyncConfig": "TemplateSyncConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentAccountConnectionSummaryTypeDef = TypedDict(
    "EnvironmentAccountConnectionSummaryTypeDef",
    {
        "arn": str,
        "environmentAccountId": str,
        "environmentName": str,
        "id": str,
        "lastModifiedAt": datetime,
        "managementAccountId": str,
        "requestedAt": datetime,
        "roleArn": str,
        "status": EnvironmentAccountConnectionStatusType,
    },
)

EnvironmentAccountConnectionTypeDef = TypedDict(
    "EnvironmentAccountConnectionTypeDef",
    {
        "arn": str,
        "environmentAccountId": str,
        "environmentName": str,
        "id": str,
        "lastModifiedAt": datetime,
        "managementAccountId": str,
        "requestedAt": datetime,
        "roleArn": str,
        "status": EnvironmentAccountConnectionStatusType,
    },
)

EnvironmentSummaryTypeDef = TypedDict(
    "EnvironmentSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "name": str,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
        "deploymentStatusMessage": NotRequired[str],
        "description": NotRequired[str],
        "environmentAccountConnectionId": NotRequired[str],
        "environmentAccountId": NotRequired[str],
        "protonServiceRoleArn": NotRequired[str],
        "provisioning": NotRequired[Literal["CUSTOMER_MANAGED"]],
    },
)

EnvironmentTemplateFilterTypeDef = TypedDict(
    "EnvironmentTemplateFilterTypeDef",
    {
        "majorVersion": str,
        "templateName": str,
    },
)

EnvironmentTemplateSummaryTypeDef = TypedDict(
    "EnvironmentTemplateSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "provisioning": NotRequired[Literal["CUSTOMER_MANAGED"]],
        "recommendedVersion": NotRequired[str],
    },
)

EnvironmentTemplateTypeDef = TypedDict(
    "EnvironmentTemplateTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "encryptionKey": NotRequired[str],
        "provisioning": NotRequired[Literal["CUSTOMER_MANAGED"]],
        "recommendedVersion": NotRequired[str],
    },
)

EnvironmentTemplateVersionSummaryTypeDef = TypedDict(
    "EnvironmentTemplateVersionSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "majorVersion": str,
        "minorVersion": str,
        "status": TemplateVersionStatusType,
        "templateName": str,
        "description": NotRequired[str],
        "recommendedMinorVersion": NotRequired[str],
        "statusMessage": NotRequired[str],
    },
)

EnvironmentTemplateVersionTypeDef = TypedDict(
    "EnvironmentTemplateVersionTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "majorVersion": str,
        "minorVersion": str,
        "status": TemplateVersionStatusType,
        "templateName": str,
        "description": NotRequired[str],
        "recommendedMinorVersion": NotRequired[str],
        "schema": NotRequired[str],
        "statusMessage": NotRequired[str],
    },
)

EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "name": str,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
        "deploymentStatusMessage": NotRequired[str],
        "description": NotRequired[str],
        "environmentAccountConnectionId": NotRequired[str],
        "environmentAccountId": NotRequired[str],
        "protonServiceRoleArn": NotRequired[str],
        "provisioning": NotRequired[Literal["CUSTOMER_MANAGED"]],
        "provisioningRepository": NotRequired["RepositoryBranchTypeDef"],
        "spec": NotRequired[str],
    },
)

GetAccountSettingsOutputTypeDef = TypedDict(
    "GetAccountSettingsOutputTypeDef",
    {
        "accountSettings": "AccountSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnvironmentAccountConnectionInputRequestTypeDef = TypedDict(
    "GetEnvironmentAccountConnectionInputRequestTypeDef",
    {
        "id": str,
    },
)

GetEnvironmentAccountConnectionOutputTypeDef = TypedDict(
    "GetEnvironmentAccountConnectionOutputTypeDef",
    {
        "environmentAccountConnection": "EnvironmentAccountConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnvironmentInputRequestTypeDef = TypedDict(
    "GetEnvironmentInputRequestTypeDef",
    {
        "name": str,
    },
)

GetEnvironmentOutputTypeDef = TypedDict(
    "GetEnvironmentOutputTypeDef",
    {
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnvironmentTemplateInputRequestTypeDef = TypedDict(
    "GetEnvironmentTemplateInputRequestTypeDef",
    {
        "name": str,
    },
)

GetEnvironmentTemplateOutputTypeDef = TypedDict(
    "GetEnvironmentTemplateOutputTypeDef",
    {
        "environmentTemplate": "EnvironmentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnvironmentTemplateVersionInputRequestTypeDef = TypedDict(
    "GetEnvironmentTemplateVersionInputRequestTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
    },
)

GetEnvironmentTemplateVersionOutputTypeDef = TypedDict(
    "GetEnvironmentTemplateVersionOutputTypeDef",
    {
        "environmentTemplateVersion": "EnvironmentTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRepositoryInputRequestTypeDef = TypedDict(
    "GetRepositoryInputRequestTypeDef",
    {
        "name": str,
        "provider": RepositoryProviderType,
    },
)

GetRepositoryOutputTypeDef = TypedDict(
    "GetRepositoryOutputTypeDef",
    {
        "repository": "RepositoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRepositorySyncStatusInputRequestTypeDef = TypedDict(
    "GetRepositorySyncStatusInputRequestTypeDef",
    {
        "branch": str,
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "syncType": Literal["TEMPLATE_SYNC"],
    },
)

GetRepositorySyncStatusOutputTypeDef = TypedDict(
    "GetRepositorySyncStatusOutputTypeDef",
    {
        "latestSync": "RepositorySyncAttemptTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceInputRequestTypeDef = TypedDict(
    "GetServiceInputRequestTypeDef",
    {
        "name": str,
    },
)

GetServiceInstanceInputRequestTypeDef = TypedDict(
    "GetServiceInstanceInputRequestTypeDef",
    {
        "name": str,
        "serviceName": str,
    },
)

GetServiceInstanceOutputTypeDef = TypedDict(
    "GetServiceInstanceOutputTypeDef",
    {
        "serviceInstance": "ServiceInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceOutputTypeDef = TypedDict(
    "GetServiceOutputTypeDef",
    {
        "service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceTemplateInputRequestTypeDef = TypedDict(
    "GetServiceTemplateInputRequestTypeDef",
    {
        "name": str,
    },
)

GetServiceTemplateOutputTypeDef = TypedDict(
    "GetServiceTemplateOutputTypeDef",
    {
        "serviceTemplate": "ServiceTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceTemplateVersionInputRequestTypeDef = TypedDict(
    "GetServiceTemplateVersionInputRequestTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
    },
)

GetServiceTemplateVersionOutputTypeDef = TypedDict(
    "GetServiceTemplateVersionOutputTypeDef",
    {
        "serviceTemplateVersion": "ServiceTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTemplateSyncConfigInputRequestTypeDef = TypedDict(
    "GetTemplateSyncConfigInputRequestTypeDef",
    {
        "templateName": str,
        "templateType": TemplateTypeType,
    },
)

GetTemplateSyncConfigOutputTypeDef = TypedDict(
    "GetTemplateSyncConfigOutputTypeDef",
    {
        "templateSyncConfig": "TemplateSyncConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTemplateSyncStatusInputRequestTypeDef = TypedDict(
    "GetTemplateSyncStatusInputRequestTypeDef",
    {
        "templateName": str,
        "templateType": TemplateTypeType,
        "templateVersion": str,
    },
)

GetTemplateSyncStatusOutputTypeDef = TypedDict(
    "GetTemplateSyncStatusOutputTypeDef",
    {
        "desiredState": "RevisionTypeDef",
        "latestSuccessfulSync": "ResourceSyncAttemptTypeDef",
        "latestSync": "ResourceSyncAttemptTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEnvironmentAccountConnectionsInputRequestTypeDef = TypedDict(
    "ListEnvironmentAccountConnectionsInputRequestTypeDef",
    {
        "requestedBy": EnvironmentAccountConnectionRequesterAccountTypeType,
        "environmentName": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "statuses": NotRequired[Sequence[EnvironmentAccountConnectionStatusType]],
    },
)

ListEnvironmentAccountConnectionsOutputTypeDef = TypedDict(
    "ListEnvironmentAccountConnectionsOutputTypeDef",
    {
        "environmentAccountConnections": List["EnvironmentAccountConnectionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEnvironmentOutputsInputRequestTypeDef = TypedDict(
    "ListEnvironmentOutputsInputRequestTypeDef",
    {
        "environmentName": str,
        "nextToken": NotRequired[str],
    },
)

ListEnvironmentOutputsOutputTypeDef = TypedDict(
    "ListEnvironmentOutputsOutputTypeDef",
    {
        "nextToken": str,
        "outputs": List["OutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEnvironmentProvisionedResourcesInputRequestTypeDef = TypedDict(
    "ListEnvironmentProvisionedResourcesInputRequestTypeDef",
    {
        "environmentName": str,
        "nextToken": NotRequired[str],
    },
)

ListEnvironmentProvisionedResourcesOutputTypeDef = TypedDict(
    "ListEnvironmentProvisionedResourcesOutputTypeDef",
    {
        "nextToken": str,
        "provisionedResources": List["ProvisionedResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEnvironmentTemplateVersionsInputRequestTypeDef = TypedDict(
    "ListEnvironmentTemplateVersionsInputRequestTypeDef",
    {
        "templateName": str,
        "majorVersion": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListEnvironmentTemplateVersionsOutputTypeDef = TypedDict(
    "ListEnvironmentTemplateVersionsOutputTypeDef",
    {
        "nextToken": str,
        "templateVersions": List["EnvironmentTemplateVersionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEnvironmentTemplatesInputRequestTypeDef = TypedDict(
    "ListEnvironmentTemplatesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListEnvironmentTemplatesOutputTypeDef = TypedDict(
    "ListEnvironmentTemplatesOutputTypeDef",
    {
        "nextToken": str,
        "templates": List["EnvironmentTemplateSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEnvironmentsInputRequestTypeDef = TypedDict(
    "ListEnvironmentsInputRequestTypeDef",
    {
        "environmentTemplates": NotRequired[Sequence["EnvironmentTemplateFilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListEnvironmentsOutputTypeDef = TypedDict(
    "ListEnvironmentsOutputTypeDef",
    {
        "environments": List["EnvironmentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRepositoriesInputRequestTypeDef = TypedDict(
    "ListRepositoriesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListRepositoriesOutputTypeDef = TypedDict(
    "ListRepositoriesOutputTypeDef",
    {
        "nextToken": str,
        "repositories": List["RepositorySummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRepositorySyncDefinitionsInputRequestTypeDef = TypedDict(
    "ListRepositorySyncDefinitionsInputRequestTypeDef",
    {
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "syncType": Literal["TEMPLATE_SYNC"],
        "nextToken": NotRequired[str],
    },
)

ListRepositorySyncDefinitionsOutputTypeDef = TypedDict(
    "ListRepositorySyncDefinitionsOutputTypeDef",
    {
        "nextToken": str,
        "syncDefinitions": List["RepositorySyncDefinitionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceInstanceOutputsInputRequestTypeDef = TypedDict(
    "ListServiceInstanceOutputsInputRequestTypeDef",
    {
        "serviceInstanceName": str,
        "serviceName": str,
        "nextToken": NotRequired[str],
    },
)

ListServiceInstanceOutputsOutputTypeDef = TypedDict(
    "ListServiceInstanceOutputsOutputTypeDef",
    {
        "nextToken": str,
        "outputs": List["OutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceInstanceProvisionedResourcesInputRequestTypeDef = TypedDict(
    "ListServiceInstanceProvisionedResourcesInputRequestTypeDef",
    {
        "serviceInstanceName": str,
        "serviceName": str,
        "nextToken": NotRequired[str],
    },
)

ListServiceInstanceProvisionedResourcesOutputTypeDef = TypedDict(
    "ListServiceInstanceProvisionedResourcesOutputTypeDef",
    {
        "nextToken": str,
        "provisionedResources": List["ProvisionedResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceInstancesInputRequestTypeDef = TypedDict(
    "ListServiceInstancesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "serviceName": NotRequired[str],
    },
)

ListServiceInstancesOutputTypeDef = TypedDict(
    "ListServiceInstancesOutputTypeDef",
    {
        "nextToken": str,
        "serviceInstances": List["ServiceInstanceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServicePipelineOutputsInputRequestTypeDef = TypedDict(
    "ListServicePipelineOutputsInputRequestTypeDef",
    {
        "serviceName": str,
        "nextToken": NotRequired[str],
    },
)

ListServicePipelineOutputsOutputTypeDef = TypedDict(
    "ListServicePipelineOutputsOutputTypeDef",
    {
        "nextToken": str,
        "outputs": List["OutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServicePipelineProvisionedResourcesInputRequestTypeDef = TypedDict(
    "ListServicePipelineProvisionedResourcesInputRequestTypeDef",
    {
        "serviceName": str,
        "nextToken": NotRequired[str],
    },
)

ListServicePipelineProvisionedResourcesOutputTypeDef = TypedDict(
    "ListServicePipelineProvisionedResourcesOutputTypeDef",
    {
        "nextToken": str,
        "provisionedResources": List["ProvisionedResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceTemplateVersionsInputRequestTypeDef = TypedDict(
    "ListServiceTemplateVersionsInputRequestTypeDef",
    {
        "templateName": str,
        "majorVersion": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListServiceTemplateVersionsOutputTypeDef = TypedDict(
    "ListServiceTemplateVersionsOutputTypeDef",
    {
        "nextToken": str,
        "templateVersions": List["ServiceTemplateVersionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceTemplatesInputRequestTypeDef = TypedDict(
    "ListServiceTemplatesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListServiceTemplatesOutputTypeDef = TypedDict(
    "ListServiceTemplatesOutputTypeDef",
    {
        "nextToken": str,
        "templates": List["ServiceTemplateSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServicesInputRequestTypeDef = TypedDict(
    "ListServicesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListServicesOutputTypeDef = TypedDict(
    "ListServicesOutputTypeDef",
    {
        "nextToken": str,
        "services": List["ServiceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "nextToken": str,
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotifyResourceDeploymentStatusChangeInputRequestTypeDef = TypedDict(
    "NotifyResourceDeploymentStatusChangeInputRequestTypeDef",
    {
        "resourceArn": str,
        "status": ResourceDeploymentStatusType,
        "deploymentId": NotRequired[str],
        "outputs": NotRequired[Sequence["OutputTypeDef"]],
        "statusMessage": NotRequired[str],
    },
)

OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "key": NotRequired[str],
        "valueString": NotRequired[str],
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

ProvisionedResourceTypeDef = TypedDict(
    "ProvisionedResourceTypeDef",
    {
        "identifier": NotRequired[str],
        "name": NotRequired[str],
        "provisioningEngine": NotRequired[ProvisionedResourceEngineType],
    },
)

RejectEnvironmentAccountConnectionInputRequestTypeDef = TypedDict(
    "RejectEnvironmentAccountConnectionInputRequestTypeDef",
    {
        "id": str,
    },
)

RejectEnvironmentAccountConnectionOutputTypeDef = TypedDict(
    "RejectEnvironmentAccountConnectionOutputTypeDef",
    {
        "environmentAccountConnection": "EnvironmentAccountConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RepositoryBranchInputTypeDef = TypedDict(
    "RepositoryBranchInputTypeDef",
    {
        "branch": str,
        "name": str,
        "provider": RepositoryProviderType,
    },
)

RepositoryBranchTypeDef = TypedDict(
    "RepositoryBranchTypeDef",
    {
        "arn": str,
        "branch": str,
        "name": str,
        "provider": RepositoryProviderType,
    },
)

RepositorySummaryTypeDef = TypedDict(
    "RepositorySummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "provider": RepositoryProviderType,
    },
)

RepositorySyncAttemptTypeDef = TypedDict(
    "RepositorySyncAttemptTypeDef",
    {
        "events": List["RepositorySyncEventTypeDef"],
        "startedAt": datetime,
        "status": RepositorySyncStatusType,
    },
)

RepositorySyncDefinitionTypeDef = TypedDict(
    "RepositorySyncDefinitionTypeDef",
    {
        "branch": str,
        "directory": str,
        "parent": str,
        "target": str,
    },
)

RepositorySyncEventTypeDef = TypedDict(
    "RepositorySyncEventTypeDef",
    {
        "event": str,
        "time": datetime,
        "type": str,
        "externalId": NotRequired[str],
    },
)

RepositoryTypeDef = TypedDict(
    "RepositoryTypeDef",
    {
        "arn": str,
        "connectionArn": str,
        "name": str,
        "provider": RepositoryProviderType,
        "encryptionKey": NotRequired[str],
    },
)

ResourceSyncAttemptTypeDef = TypedDict(
    "ResourceSyncAttemptTypeDef",
    {
        "events": List["ResourceSyncEventTypeDef"],
        "initialRevision": "RevisionTypeDef",
        "startedAt": datetime,
        "status": ResourceSyncStatusType,
        "target": str,
        "targetRevision": "RevisionTypeDef",
    },
)

ResourceSyncEventTypeDef = TypedDict(
    "ResourceSyncEventTypeDef",
    {
        "event": str,
        "time": datetime,
        "type": str,
        "externalId": NotRequired[str],
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

RevisionTypeDef = TypedDict(
    "RevisionTypeDef",
    {
        "branch": str,
        "directory": str,
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "sha": str,
    },
)

S3ObjectSourceTypeDef = TypedDict(
    "S3ObjectSourceTypeDef",
    {
        "bucket": str,
        "key": str,
    },
)

ServiceInstanceSummaryTypeDef = TypedDict(
    "ServiceInstanceSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "environmentName": str,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "name": str,
        "serviceName": str,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
        "deploymentStatusMessage": NotRequired[str],
    },
)

ServiceInstanceTypeDef = TypedDict(
    "ServiceInstanceTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "environmentName": str,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "name": str,
        "serviceName": str,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
        "deploymentStatusMessage": NotRequired[str],
        "spec": NotRequired[str],
    },
)

ServicePipelineTypeDef = TypedDict(
    "ServicePipelineTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
        "deploymentStatusMessage": NotRequired[str],
        "spec": NotRequired[str],
    },
)

ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
        "status": ServiceStatusType,
        "templateName": str,
        "description": NotRequired[str],
        "statusMessage": NotRequired[str],
    },
)

ServiceTemplateSummaryTypeDef = TypedDict(
    "ServiceTemplateSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "pipelineProvisioning": NotRequired[Literal["CUSTOMER_MANAGED"]],
        "recommendedVersion": NotRequired[str],
    },
)

ServiceTemplateTypeDef = TypedDict(
    "ServiceTemplateTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "encryptionKey": NotRequired[str],
        "pipelineProvisioning": NotRequired[Literal["CUSTOMER_MANAGED"]],
        "recommendedVersion": NotRequired[str],
    },
)

ServiceTemplateVersionSummaryTypeDef = TypedDict(
    "ServiceTemplateVersionSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "majorVersion": str,
        "minorVersion": str,
        "status": TemplateVersionStatusType,
        "templateName": str,
        "description": NotRequired[str],
        "recommendedMinorVersion": NotRequired[str],
        "statusMessage": NotRequired[str],
    },
)

ServiceTemplateVersionTypeDef = TypedDict(
    "ServiceTemplateVersionTypeDef",
    {
        "arn": str,
        "compatibleEnvironmentTemplates": List["CompatibleEnvironmentTemplateTypeDef"],
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "majorVersion": str,
        "minorVersion": str,
        "status": TemplateVersionStatusType,
        "templateName": str,
        "description": NotRequired[str],
        "recommendedMinorVersion": NotRequired[str],
        "schema": NotRequired[str],
        "statusMessage": NotRequired[str],
    },
)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
        "spec": str,
        "status": ServiceStatusType,
        "templateName": str,
        "branchName": NotRequired[str],
        "description": NotRequired[str],
        "pipeline": NotRequired["ServicePipelineTypeDef"],
        "repositoryConnectionArn": NotRequired[str],
        "repositoryId": NotRequired[str],
        "statusMessage": NotRequired[str],
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

TemplateSyncConfigTypeDef = TypedDict(
    "TemplateSyncConfigTypeDef",
    {
        "branch": str,
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "templateName": str,
        "templateType": TemplateTypeType,
        "subdirectory": NotRequired[str],
    },
)

TemplateVersionSourceInputTypeDef = TypedDict(
    "TemplateVersionSourceInputTypeDef",
    {
        "s3": NotRequired["S3ObjectSourceTypeDef"],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateAccountSettingsInputRequestTypeDef = TypedDict(
    "UpdateAccountSettingsInputRequestTypeDef",
    {
        "pipelineProvisioningRepository": NotRequired["RepositoryBranchInputTypeDef"],
        "pipelineServiceRoleArn": NotRequired[str],
    },
)

UpdateAccountSettingsOutputTypeDef = TypedDict(
    "UpdateAccountSettingsOutputTypeDef",
    {
        "accountSettings": "AccountSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEnvironmentAccountConnectionInputRequestTypeDef = TypedDict(
    "UpdateEnvironmentAccountConnectionInputRequestTypeDef",
    {
        "id": str,
        "roleArn": str,
    },
)

UpdateEnvironmentAccountConnectionOutputTypeDef = TypedDict(
    "UpdateEnvironmentAccountConnectionOutputTypeDef",
    {
        "environmentAccountConnection": "EnvironmentAccountConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEnvironmentInputRequestTypeDef = TypedDict(
    "UpdateEnvironmentInputRequestTypeDef",
    {
        "deploymentType": DeploymentUpdateTypeType,
        "name": str,
        "description": NotRequired[str],
        "environmentAccountConnectionId": NotRequired[str],
        "protonServiceRoleArn": NotRequired[str],
        "provisioningRepository": NotRequired["RepositoryBranchInputTypeDef"],
        "spec": NotRequired[str],
        "templateMajorVersion": NotRequired[str],
        "templateMinorVersion": NotRequired[str],
    },
)

UpdateEnvironmentOutputTypeDef = TypedDict(
    "UpdateEnvironmentOutputTypeDef",
    {
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEnvironmentTemplateInputRequestTypeDef = TypedDict(
    "UpdateEnvironmentTemplateInputRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "displayName": NotRequired[str],
    },
)

UpdateEnvironmentTemplateOutputTypeDef = TypedDict(
    "UpdateEnvironmentTemplateOutputTypeDef",
    {
        "environmentTemplate": "EnvironmentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEnvironmentTemplateVersionInputRequestTypeDef = TypedDict(
    "UpdateEnvironmentTemplateVersionInputRequestTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
        "description": NotRequired[str],
        "status": NotRequired[TemplateVersionStatusType],
    },
)

UpdateEnvironmentTemplateVersionOutputTypeDef = TypedDict(
    "UpdateEnvironmentTemplateVersionOutputTypeDef",
    {
        "environmentTemplateVersion": "EnvironmentTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServiceInputRequestTypeDef = TypedDict(
    "UpdateServiceInputRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "spec": NotRequired[str],
    },
)

UpdateServiceInstanceInputRequestTypeDef = TypedDict(
    "UpdateServiceInstanceInputRequestTypeDef",
    {
        "deploymentType": DeploymentUpdateTypeType,
        "name": str,
        "serviceName": str,
        "spec": NotRequired[str],
        "templateMajorVersion": NotRequired[str],
        "templateMinorVersion": NotRequired[str],
    },
)

UpdateServiceInstanceOutputTypeDef = TypedDict(
    "UpdateServiceInstanceOutputTypeDef",
    {
        "serviceInstance": "ServiceInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServiceOutputTypeDef = TypedDict(
    "UpdateServiceOutputTypeDef",
    {
        "service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServicePipelineInputRequestTypeDef = TypedDict(
    "UpdateServicePipelineInputRequestTypeDef",
    {
        "deploymentType": DeploymentUpdateTypeType,
        "serviceName": str,
        "spec": str,
        "templateMajorVersion": NotRequired[str],
        "templateMinorVersion": NotRequired[str],
    },
)

UpdateServicePipelineOutputTypeDef = TypedDict(
    "UpdateServicePipelineOutputTypeDef",
    {
        "pipeline": "ServicePipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServiceTemplateInputRequestTypeDef = TypedDict(
    "UpdateServiceTemplateInputRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "displayName": NotRequired[str],
    },
)

UpdateServiceTemplateOutputTypeDef = TypedDict(
    "UpdateServiceTemplateOutputTypeDef",
    {
        "serviceTemplate": "ServiceTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServiceTemplateVersionInputRequestTypeDef = TypedDict(
    "UpdateServiceTemplateVersionInputRequestTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
        "compatibleEnvironmentTemplates": NotRequired[
            Sequence["CompatibleEnvironmentTemplateInputTypeDef"]
        ],
        "description": NotRequired[str],
        "status": NotRequired[TemplateVersionStatusType],
    },
)

UpdateServiceTemplateVersionOutputTypeDef = TypedDict(
    "UpdateServiceTemplateVersionOutputTypeDef",
    {
        "serviceTemplateVersion": "ServiceTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTemplateSyncConfigInputRequestTypeDef = TypedDict(
    "UpdateTemplateSyncConfigInputRequestTypeDef",
    {
        "branch": str,
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "templateName": str,
        "templateType": TemplateTypeType,
        "subdirectory": NotRequired[str],
    },
)

UpdateTemplateSyncConfigOutputTypeDef = TypedDict(
    "UpdateTemplateSyncConfigOutputTypeDef",
    {
        "templateSyncConfig": "TemplateSyncConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
