"""
Type annotations for greengrassv2 service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_greengrassv2/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_greengrassv2.type_defs import AssociateClientDeviceWithCoreDeviceEntryTypeDef

    data: AssociateClientDeviceWithCoreDeviceEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    CloudComponentStateType,
    ComponentDependencyTypeType,
    ComponentVisibilityScopeType,
    CoreDeviceStatusType,
    DeploymentComponentUpdatePolicyActionType,
    DeploymentFailureHandlingPolicyType,
    DeploymentHistoryFilterType,
    DeploymentStatusType,
    EffectiveDeploymentExecutionStatusType,
    InstalledComponentLifecycleStateType,
    IoTJobExecutionFailureTypeType,
    LambdaEventSourceTypeType,
    LambdaFilesystemPermissionType,
    LambdaInputPayloadEncodingTypeType,
    LambdaIsolationModeType,
    RecipeOutputFormatType,
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
    "AssociateClientDeviceWithCoreDeviceEntryTypeDef",
    "AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef",
    "AssociateServiceRoleToAccountRequestRequestTypeDef",
    "AssociateServiceRoleToAccountResponseTypeDef",
    "AssociatedClientDeviceTypeDef",
    "BatchAssociateClientDeviceWithCoreDeviceRequestRequestTypeDef",
    "BatchAssociateClientDeviceWithCoreDeviceResponseTypeDef",
    "BatchDisassociateClientDeviceFromCoreDeviceRequestRequestTypeDef",
    "BatchDisassociateClientDeviceFromCoreDeviceResponseTypeDef",
    "CancelDeploymentRequestRequestTypeDef",
    "CancelDeploymentResponseTypeDef",
    "CloudComponentStatusTypeDef",
    "ComponentCandidateTypeDef",
    "ComponentConfigurationUpdateTypeDef",
    "ComponentDependencyRequirementTypeDef",
    "ComponentDeploymentSpecificationTypeDef",
    "ComponentLatestVersionTypeDef",
    "ComponentPlatformTypeDef",
    "ComponentRunWithTypeDef",
    "ComponentTypeDef",
    "ComponentVersionListItemTypeDef",
    "ConnectivityInfoTypeDef",
    "CoreDeviceTypeDef",
    "CreateComponentVersionRequestRequestTypeDef",
    "CreateComponentVersionResponseTypeDef",
    "CreateDeploymentRequestRequestTypeDef",
    "CreateDeploymentResponseTypeDef",
    "DeleteComponentRequestRequestTypeDef",
    "DeleteCoreDeviceRequestRequestTypeDef",
    "DeploymentComponentUpdatePolicyTypeDef",
    "DeploymentConfigurationValidationPolicyTypeDef",
    "DeploymentIoTJobConfigurationTypeDef",
    "DeploymentPoliciesTypeDef",
    "DeploymentTypeDef",
    "DescribeComponentRequestRequestTypeDef",
    "DescribeComponentResponseTypeDef",
    "DisassociateClientDeviceFromCoreDeviceEntryTypeDef",
    "DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef",
    "DisassociateServiceRoleFromAccountResponseTypeDef",
    "EffectiveDeploymentTypeDef",
    "GetComponentRequestRequestTypeDef",
    "GetComponentResponseTypeDef",
    "GetComponentVersionArtifactRequestRequestTypeDef",
    "GetComponentVersionArtifactResponseTypeDef",
    "GetConnectivityInfoRequestRequestTypeDef",
    "GetConnectivityInfoResponseTypeDef",
    "GetCoreDeviceRequestRequestTypeDef",
    "GetCoreDeviceResponseTypeDef",
    "GetDeploymentRequestRequestTypeDef",
    "GetDeploymentResponseTypeDef",
    "GetServiceRoleForAccountResponseTypeDef",
    "InstalledComponentTypeDef",
    "IoTJobAbortConfigTypeDef",
    "IoTJobAbortCriteriaTypeDef",
    "IoTJobExecutionsRolloutConfigTypeDef",
    "IoTJobExponentialRolloutRateTypeDef",
    "IoTJobRateIncreaseCriteriaTypeDef",
    "IoTJobTimeoutConfigTypeDef",
    "LambdaContainerParamsTypeDef",
    "LambdaDeviceMountTypeDef",
    "LambdaEventSourceTypeDef",
    "LambdaExecutionParametersTypeDef",
    "LambdaFunctionRecipeSourceTypeDef",
    "LambdaLinuxProcessParamsTypeDef",
    "LambdaVolumeMountTypeDef",
    "ListClientDevicesAssociatedWithCoreDeviceRequestRequestTypeDef",
    "ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef",
    "ListComponentVersionsRequestRequestTypeDef",
    "ListComponentVersionsResponseTypeDef",
    "ListComponentsRequestRequestTypeDef",
    "ListComponentsResponseTypeDef",
    "ListCoreDevicesRequestRequestTypeDef",
    "ListCoreDevicesResponseTypeDef",
    "ListDeploymentsRequestRequestTypeDef",
    "ListDeploymentsResponseTypeDef",
    "ListEffectiveDeploymentsRequestRequestTypeDef",
    "ListEffectiveDeploymentsResponseTypeDef",
    "ListInstalledComponentsRequestRequestTypeDef",
    "ListInstalledComponentsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResolveComponentCandidatesRequestRequestTypeDef",
    "ResolveComponentCandidatesResponseTypeDef",
    "ResolvedComponentVersionTypeDef",
    "ResponseMetadataTypeDef",
    "SystemResourceLimitsTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateConnectivityInfoRequestRequestTypeDef",
    "UpdateConnectivityInfoResponseTypeDef",
)

AssociateClientDeviceWithCoreDeviceEntryTypeDef = TypedDict(
    "AssociateClientDeviceWithCoreDeviceEntryTypeDef",
    {
        "thingName": str,
    },
)

AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef = TypedDict(
    "AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef",
    {
        "thingName": NotRequired[str],
        "code": NotRequired[str],
        "message": NotRequired[str],
    },
)

AssociateServiceRoleToAccountRequestRequestTypeDef = TypedDict(
    "AssociateServiceRoleToAccountRequestRequestTypeDef",
    {
        "roleArn": str,
    },
)

AssociateServiceRoleToAccountResponseTypeDef = TypedDict(
    "AssociateServiceRoleToAccountResponseTypeDef",
    {
        "associatedAt": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociatedClientDeviceTypeDef = TypedDict(
    "AssociatedClientDeviceTypeDef",
    {
        "thingName": NotRequired[str],
        "associationTimestamp": NotRequired[datetime],
    },
)

BatchAssociateClientDeviceWithCoreDeviceRequestRequestTypeDef = TypedDict(
    "BatchAssociateClientDeviceWithCoreDeviceRequestRequestTypeDef",
    {
        "coreDeviceThingName": str,
        "entries": NotRequired[Sequence["AssociateClientDeviceWithCoreDeviceEntryTypeDef"]],
    },
)

BatchAssociateClientDeviceWithCoreDeviceResponseTypeDef = TypedDict(
    "BatchAssociateClientDeviceWithCoreDeviceResponseTypeDef",
    {
        "errorEntries": List["AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDisassociateClientDeviceFromCoreDeviceRequestRequestTypeDef = TypedDict(
    "BatchDisassociateClientDeviceFromCoreDeviceRequestRequestTypeDef",
    {
        "coreDeviceThingName": str,
        "entries": NotRequired[Sequence["DisassociateClientDeviceFromCoreDeviceEntryTypeDef"]],
    },
)

BatchDisassociateClientDeviceFromCoreDeviceResponseTypeDef = TypedDict(
    "BatchDisassociateClientDeviceFromCoreDeviceResponseTypeDef",
    {
        "errorEntries": List["DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelDeploymentRequestRequestTypeDef = TypedDict(
    "CancelDeploymentRequestRequestTypeDef",
    {
        "deploymentId": str,
    },
)

CancelDeploymentResponseTypeDef = TypedDict(
    "CancelDeploymentResponseTypeDef",
    {
        "message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CloudComponentStatusTypeDef = TypedDict(
    "CloudComponentStatusTypeDef",
    {
        "componentState": NotRequired[CloudComponentStateType],
        "message": NotRequired[str],
        "errors": NotRequired[Dict[str, str]],
    },
)

ComponentCandidateTypeDef = TypedDict(
    "ComponentCandidateTypeDef",
    {
        "componentName": NotRequired[str],
        "componentVersion": NotRequired[str],
        "versionRequirements": NotRequired[Mapping[str, str]],
    },
)

ComponentConfigurationUpdateTypeDef = TypedDict(
    "ComponentConfigurationUpdateTypeDef",
    {
        "merge": NotRequired[str],
        "reset": NotRequired[Sequence[str]],
    },
)

ComponentDependencyRequirementTypeDef = TypedDict(
    "ComponentDependencyRequirementTypeDef",
    {
        "versionRequirement": NotRequired[str],
        "dependencyType": NotRequired[ComponentDependencyTypeType],
    },
)

ComponentDeploymentSpecificationTypeDef = TypedDict(
    "ComponentDeploymentSpecificationTypeDef",
    {
        "componentVersion": NotRequired[str],
        "configurationUpdate": NotRequired["ComponentConfigurationUpdateTypeDef"],
        "runWith": NotRequired["ComponentRunWithTypeDef"],
    },
)

ComponentLatestVersionTypeDef = TypedDict(
    "ComponentLatestVersionTypeDef",
    {
        "arn": NotRequired[str],
        "componentVersion": NotRequired[str],
        "creationTimestamp": NotRequired[datetime],
        "description": NotRequired[str],
        "publisher": NotRequired[str],
        "platforms": NotRequired[List["ComponentPlatformTypeDef"]],
    },
)

ComponentPlatformTypeDef = TypedDict(
    "ComponentPlatformTypeDef",
    {
        "name": NotRequired[str],
        "attributes": NotRequired[Mapping[str, str]],
    },
)

ComponentRunWithTypeDef = TypedDict(
    "ComponentRunWithTypeDef",
    {
        "posixUser": NotRequired[str],
        "systemResourceLimits": NotRequired["SystemResourceLimitsTypeDef"],
        "windowsUser": NotRequired[str],
    },
)

ComponentTypeDef = TypedDict(
    "ComponentTypeDef",
    {
        "arn": NotRequired[str],
        "componentName": NotRequired[str],
        "latestVersion": NotRequired["ComponentLatestVersionTypeDef"],
    },
)

ComponentVersionListItemTypeDef = TypedDict(
    "ComponentVersionListItemTypeDef",
    {
        "componentName": NotRequired[str],
        "componentVersion": NotRequired[str],
        "arn": NotRequired[str],
    },
)

ConnectivityInfoTypeDef = TypedDict(
    "ConnectivityInfoTypeDef",
    {
        "id": NotRequired[str],
        "hostAddress": NotRequired[str],
        "portNumber": NotRequired[int],
        "metadata": NotRequired[str],
    },
)

CoreDeviceTypeDef = TypedDict(
    "CoreDeviceTypeDef",
    {
        "coreDeviceThingName": NotRequired[str],
        "status": NotRequired[CoreDeviceStatusType],
        "lastStatusUpdateTimestamp": NotRequired[datetime],
    },
)

CreateComponentVersionRequestRequestTypeDef = TypedDict(
    "CreateComponentVersionRequestRequestTypeDef",
    {
        "inlineRecipe": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "lambdaFunction": NotRequired["LambdaFunctionRecipeSourceTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
        "clientToken": NotRequired[str],
    },
)

CreateComponentVersionResponseTypeDef = TypedDict(
    "CreateComponentVersionResponseTypeDef",
    {
        "arn": str,
        "componentName": str,
        "componentVersion": str,
        "creationTimestamp": datetime,
        "status": "CloudComponentStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDeploymentRequestRequestTypeDef = TypedDict(
    "CreateDeploymentRequestRequestTypeDef",
    {
        "targetArn": str,
        "deploymentName": NotRequired[str],
        "components": NotRequired[Mapping[str, "ComponentDeploymentSpecificationTypeDef"]],
        "iotJobConfiguration": NotRequired["DeploymentIoTJobConfigurationTypeDef"],
        "deploymentPolicies": NotRequired["DeploymentPoliciesTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
        "clientToken": NotRequired[str],
    },
)

CreateDeploymentResponseTypeDef = TypedDict(
    "CreateDeploymentResponseTypeDef",
    {
        "deploymentId": str,
        "iotJobId": str,
        "iotJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteComponentRequestRequestTypeDef = TypedDict(
    "DeleteComponentRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteCoreDeviceRequestRequestTypeDef = TypedDict(
    "DeleteCoreDeviceRequestRequestTypeDef",
    {
        "coreDeviceThingName": str,
    },
)

DeploymentComponentUpdatePolicyTypeDef = TypedDict(
    "DeploymentComponentUpdatePolicyTypeDef",
    {
        "timeoutInSeconds": NotRequired[int],
        "action": NotRequired[DeploymentComponentUpdatePolicyActionType],
    },
)

DeploymentConfigurationValidationPolicyTypeDef = TypedDict(
    "DeploymentConfigurationValidationPolicyTypeDef",
    {
        "timeoutInSeconds": NotRequired[int],
    },
)

DeploymentIoTJobConfigurationTypeDef = TypedDict(
    "DeploymentIoTJobConfigurationTypeDef",
    {
        "jobExecutionsRolloutConfig": NotRequired["IoTJobExecutionsRolloutConfigTypeDef"],
        "abortConfig": NotRequired["IoTJobAbortConfigTypeDef"],
        "timeoutConfig": NotRequired["IoTJobTimeoutConfigTypeDef"],
    },
)

DeploymentPoliciesTypeDef = TypedDict(
    "DeploymentPoliciesTypeDef",
    {
        "failureHandlingPolicy": NotRequired[DeploymentFailureHandlingPolicyType],
        "componentUpdatePolicy": NotRequired["DeploymentComponentUpdatePolicyTypeDef"],
        "configurationValidationPolicy": NotRequired[
            "DeploymentConfigurationValidationPolicyTypeDef"
        ],
    },
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "targetArn": NotRequired[str],
        "revisionId": NotRequired[str],
        "deploymentId": NotRequired[str],
        "deploymentName": NotRequired[str],
        "creationTimestamp": NotRequired[datetime],
        "deploymentStatus": NotRequired[DeploymentStatusType],
        "isLatestForTarget": NotRequired[bool],
    },
)

DescribeComponentRequestRequestTypeDef = TypedDict(
    "DescribeComponentRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DescribeComponentResponseTypeDef = TypedDict(
    "DescribeComponentResponseTypeDef",
    {
        "arn": str,
        "componentName": str,
        "componentVersion": str,
        "creationTimestamp": datetime,
        "publisher": str,
        "description": str,
        "status": "CloudComponentStatusTypeDef",
        "platforms": List["ComponentPlatformTypeDef"],
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateClientDeviceFromCoreDeviceEntryTypeDef = TypedDict(
    "DisassociateClientDeviceFromCoreDeviceEntryTypeDef",
    {
        "thingName": str,
    },
)

DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef = TypedDict(
    "DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef",
    {
        "thingName": NotRequired[str],
        "code": NotRequired[str],
        "message": NotRequired[str],
    },
)

DisassociateServiceRoleFromAccountResponseTypeDef = TypedDict(
    "DisassociateServiceRoleFromAccountResponseTypeDef",
    {
        "disassociatedAt": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EffectiveDeploymentTypeDef = TypedDict(
    "EffectiveDeploymentTypeDef",
    {
        "deploymentId": str,
        "deploymentName": str,
        "targetArn": str,
        "coreDeviceExecutionStatus": EffectiveDeploymentExecutionStatusType,
        "creationTimestamp": datetime,
        "modifiedTimestamp": datetime,
        "iotJobId": NotRequired[str],
        "iotJobArn": NotRequired[str],
        "description": NotRequired[str],
        "reason": NotRequired[str],
    },
)

GetComponentRequestRequestTypeDef = TypedDict(
    "GetComponentRequestRequestTypeDef",
    {
        "arn": str,
        "recipeOutputFormat": NotRequired[RecipeOutputFormatType],
    },
)

GetComponentResponseTypeDef = TypedDict(
    "GetComponentResponseTypeDef",
    {
        "recipeOutputFormat": RecipeOutputFormatType,
        "recipe": bytes,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComponentVersionArtifactRequestRequestTypeDef = TypedDict(
    "GetComponentVersionArtifactRequestRequestTypeDef",
    {
        "arn": str,
        "artifactName": str,
    },
)

GetComponentVersionArtifactResponseTypeDef = TypedDict(
    "GetComponentVersionArtifactResponseTypeDef",
    {
        "preSignedUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectivityInfoRequestRequestTypeDef = TypedDict(
    "GetConnectivityInfoRequestRequestTypeDef",
    {
        "thingName": str,
    },
)

GetConnectivityInfoResponseTypeDef = TypedDict(
    "GetConnectivityInfoResponseTypeDef",
    {
        "connectivityInfo": List["ConnectivityInfoTypeDef"],
        "message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCoreDeviceRequestRequestTypeDef = TypedDict(
    "GetCoreDeviceRequestRequestTypeDef",
    {
        "coreDeviceThingName": str,
    },
)

GetCoreDeviceResponseTypeDef = TypedDict(
    "GetCoreDeviceResponseTypeDef",
    {
        "coreDeviceThingName": str,
        "coreVersion": str,
        "platform": str,
        "architecture": str,
        "status": CoreDeviceStatusType,
        "lastStatusUpdateTimestamp": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentRequestRequestTypeDef = TypedDict(
    "GetDeploymentRequestRequestTypeDef",
    {
        "deploymentId": str,
    },
)

GetDeploymentResponseTypeDef = TypedDict(
    "GetDeploymentResponseTypeDef",
    {
        "targetArn": str,
        "revisionId": str,
        "deploymentId": str,
        "deploymentName": str,
        "deploymentStatus": DeploymentStatusType,
        "iotJobId": str,
        "iotJobArn": str,
        "components": Dict[str, "ComponentDeploymentSpecificationTypeDef"],
        "deploymentPolicies": "DeploymentPoliciesTypeDef",
        "iotJobConfiguration": "DeploymentIoTJobConfigurationTypeDef",
        "creationTimestamp": datetime,
        "isLatestForTarget": bool,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceRoleForAccountResponseTypeDef = TypedDict(
    "GetServiceRoleForAccountResponseTypeDef",
    {
        "associatedAt": str,
        "roleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstalledComponentTypeDef = TypedDict(
    "InstalledComponentTypeDef",
    {
        "componentName": NotRequired[str],
        "componentVersion": NotRequired[str],
        "lifecycleState": NotRequired[InstalledComponentLifecycleStateType],
        "lifecycleStateDetails": NotRequired[str],
        "isRoot": NotRequired[bool],
    },
)

IoTJobAbortConfigTypeDef = TypedDict(
    "IoTJobAbortConfigTypeDef",
    {
        "criteriaList": Sequence["IoTJobAbortCriteriaTypeDef"],
    },
)

IoTJobAbortCriteriaTypeDef = TypedDict(
    "IoTJobAbortCriteriaTypeDef",
    {
        "failureType": IoTJobExecutionFailureTypeType,
        "action": Literal["CANCEL"],
        "thresholdPercentage": float,
        "minNumberOfExecutedThings": int,
    },
)

IoTJobExecutionsRolloutConfigTypeDef = TypedDict(
    "IoTJobExecutionsRolloutConfigTypeDef",
    {
        "exponentialRate": NotRequired["IoTJobExponentialRolloutRateTypeDef"],
        "maximumPerMinute": NotRequired[int],
    },
)

IoTJobExponentialRolloutRateTypeDef = TypedDict(
    "IoTJobExponentialRolloutRateTypeDef",
    {
        "baseRatePerMinute": int,
        "incrementFactor": float,
        "rateIncreaseCriteria": "IoTJobRateIncreaseCriteriaTypeDef",
    },
)

IoTJobRateIncreaseCriteriaTypeDef = TypedDict(
    "IoTJobRateIncreaseCriteriaTypeDef",
    {
        "numberOfNotifiedThings": NotRequired[int],
        "numberOfSucceededThings": NotRequired[int],
    },
)

IoTJobTimeoutConfigTypeDef = TypedDict(
    "IoTJobTimeoutConfigTypeDef",
    {
        "inProgressTimeoutInMinutes": NotRequired[int],
    },
)

LambdaContainerParamsTypeDef = TypedDict(
    "LambdaContainerParamsTypeDef",
    {
        "memorySizeInKB": NotRequired[int],
        "mountROSysfs": NotRequired[bool],
        "volumes": NotRequired[Sequence["LambdaVolumeMountTypeDef"]],
        "devices": NotRequired[Sequence["LambdaDeviceMountTypeDef"]],
    },
)

LambdaDeviceMountTypeDef = TypedDict(
    "LambdaDeviceMountTypeDef",
    {
        "path": str,
        "permission": NotRequired[LambdaFilesystemPermissionType],
        "addGroupOwner": NotRequired[bool],
    },
)

LambdaEventSourceTypeDef = TypedDict(
    "LambdaEventSourceTypeDef",
    {
        "topic": str,
        "type": LambdaEventSourceTypeType,
    },
)

LambdaExecutionParametersTypeDef = TypedDict(
    "LambdaExecutionParametersTypeDef",
    {
        "eventSources": NotRequired[Sequence["LambdaEventSourceTypeDef"]],
        "maxQueueSize": NotRequired[int],
        "maxInstancesCount": NotRequired[int],
        "maxIdleTimeInSeconds": NotRequired[int],
        "timeoutInSeconds": NotRequired[int],
        "statusTimeoutInSeconds": NotRequired[int],
        "pinned": NotRequired[bool],
        "inputPayloadEncodingType": NotRequired[LambdaInputPayloadEncodingTypeType],
        "execArgs": NotRequired[Sequence[str]],
        "environmentVariables": NotRequired[Mapping[str, str]],
        "linuxProcessParams": NotRequired["LambdaLinuxProcessParamsTypeDef"],
    },
)

LambdaFunctionRecipeSourceTypeDef = TypedDict(
    "LambdaFunctionRecipeSourceTypeDef",
    {
        "lambdaArn": str,
        "componentName": NotRequired[str],
        "componentVersion": NotRequired[str],
        "componentPlatforms": NotRequired[Sequence["ComponentPlatformTypeDef"]],
        "componentDependencies": NotRequired[Mapping[str, "ComponentDependencyRequirementTypeDef"]],
        "componentLambdaParameters": NotRequired["LambdaExecutionParametersTypeDef"],
    },
)

LambdaLinuxProcessParamsTypeDef = TypedDict(
    "LambdaLinuxProcessParamsTypeDef",
    {
        "isolationMode": NotRequired[LambdaIsolationModeType],
        "containerParams": NotRequired["LambdaContainerParamsTypeDef"],
    },
)

LambdaVolumeMountTypeDef = TypedDict(
    "LambdaVolumeMountTypeDef",
    {
        "sourcePath": str,
        "destinationPath": str,
        "permission": NotRequired[LambdaFilesystemPermissionType],
        "addGroupOwner": NotRequired[bool],
    },
)

ListClientDevicesAssociatedWithCoreDeviceRequestRequestTypeDef = TypedDict(
    "ListClientDevicesAssociatedWithCoreDeviceRequestRequestTypeDef",
    {
        "coreDeviceThingName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef = TypedDict(
    "ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef",
    {
        "associatedClientDevices": List["AssociatedClientDeviceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListComponentVersionsRequestRequestTypeDef = TypedDict(
    "ListComponentVersionsRequestRequestTypeDef",
    {
        "arn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListComponentVersionsResponseTypeDef = TypedDict(
    "ListComponentVersionsResponseTypeDef",
    {
        "componentVersions": List["ComponentVersionListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListComponentsRequestRequestTypeDef = TypedDict(
    "ListComponentsRequestRequestTypeDef",
    {
        "scope": NotRequired[ComponentVisibilityScopeType],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListComponentsResponseTypeDef = TypedDict(
    "ListComponentsResponseTypeDef",
    {
        "components": List["ComponentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCoreDevicesRequestRequestTypeDef = TypedDict(
    "ListCoreDevicesRequestRequestTypeDef",
    {
        "thingGroupArn": NotRequired[str],
        "status": NotRequired[CoreDeviceStatusType],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListCoreDevicesResponseTypeDef = TypedDict(
    "ListCoreDevicesResponseTypeDef",
    {
        "coreDevices": List["CoreDeviceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeploymentsRequestRequestTypeDef = TypedDict(
    "ListDeploymentsRequestRequestTypeDef",
    {
        "targetArn": NotRequired[str],
        "historyFilter": NotRequired[DeploymentHistoryFilterType],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListDeploymentsResponseTypeDef = TypedDict(
    "ListDeploymentsResponseTypeDef",
    {
        "deployments": List["DeploymentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEffectiveDeploymentsRequestRequestTypeDef = TypedDict(
    "ListEffectiveDeploymentsRequestRequestTypeDef",
    {
        "coreDeviceThingName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListEffectiveDeploymentsResponseTypeDef = TypedDict(
    "ListEffectiveDeploymentsResponseTypeDef",
    {
        "effectiveDeployments": List["EffectiveDeploymentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstalledComponentsRequestRequestTypeDef = TypedDict(
    "ListInstalledComponentsRequestRequestTypeDef",
    {
        "coreDeviceThingName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListInstalledComponentsResponseTypeDef = TypedDict(
    "ListInstalledComponentsResponseTypeDef",
    {
        "installedComponents": List["InstalledComponentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
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

ResolveComponentCandidatesRequestRequestTypeDef = TypedDict(
    "ResolveComponentCandidatesRequestRequestTypeDef",
    {
        "platform": "ComponentPlatformTypeDef",
        "componentCandidates": Sequence["ComponentCandidateTypeDef"],
    },
)

ResolveComponentCandidatesResponseTypeDef = TypedDict(
    "ResolveComponentCandidatesResponseTypeDef",
    {
        "resolvedComponentVersions": List["ResolvedComponentVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResolvedComponentVersionTypeDef = TypedDict(
    "ResolvedComponentVersionTypeDef",
    {
        "arn": NotRequired[str],
        "componentName": NotRequired[str],
        "componentVersion": NotRequired[str],
        "recipe": NotRequired[bytes],
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

SystemResourceLimitsTypeDef = TypedDict(
    "SystemResourceLimitsTypeDef",
    {
        "memory": NotRequired[int],
        "cpus": NotRequired[float],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateConnectivityInfoRequestRequestTypeDef = TypedDict(
    "UpdateConnectivityInfoRequestRequestTypeDef",
    {
        "thingName": str,
        "connectivityInfo": Sequence["ConnectivityInfoTypeDef"],
    },
)

UpdateConnectivityInfoResponseTypeDef = TypedDict(
    "UpdateConnectivityInfoResponseTypeDef",
    {
        "version": str,
        "message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
