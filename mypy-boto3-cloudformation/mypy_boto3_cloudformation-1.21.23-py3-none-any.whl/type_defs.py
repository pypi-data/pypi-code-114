"""
Type annotations for cloudformation service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudformation.type_defs import AccountGateResultTypeDef

    data: AccountGateResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AccountGateStatusType,
    CallAsType,
    CapabilityType,
    CategoryType,
    ChangeActionType,
    ChangeSetHooksStatusType,
    ChangeSetStatusType,
    ChangeSetTypeType,
    ChangeSourceType,
    DeprecatedStatusType,
    DifferenceTypeType,
    EvaluationTypeType,
    ExecutionStatusType,
    HandlerErrorCodeType,
    HookFailureModeType,
    HookStatusType,
    IdentityProviderType,
    OnFailureType,
    OperationStatusType,
    PermissionModelsType,
    ProvisioningTypeType,
    PublisherStatusType,
    RegionConcurrencyTypeType,
    RegistrationStatusType,
    RegistryTypeType,
    ReplacementType,
    RequiresRecreationType,
    ResourceAttributeType,
    ResourceSignalStatusType,
    ResourceStatusType,
    StackDriftDetectionStatusType,
    StackDriftStatusType,
    StackInstanceDetailedStatusType,
    StackInstanceStatusType,
    StackResourceDriftStatusType,
    StackSetDriftDetectionStatusType,
    StackSetDriftStatusType,
    StackSetOperationActionType,
    StackSetOperationResultStatusType,
    StackSetOperationStatusType,
    StackSetStatusType,
    StackStatusType,
    TemplateStageType,
    ThirdPartyTypeType,
    TypeTestsStatusType,
    VersionBumpType,
    VisibilityType,
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
    "AccountGateResultTypeDef",
    "AccountLimitTypeDef",
    "ActivateTypeInputRequestTypeDef",
    "ActivateTypeOutputTypeDef",
    "AutoDeploymentTypeDef",
    "BatchDescribeTypeConfigurationsErrorTypeDef",
    "BatchDescribeTypeConfigurationsInputRequestTypeDef",
    "BatchDescribeTypeConfigurationsOutputTypeDef",
    "CancelUpdateStackInputRequestTypeDef",
    "CancelUpdateStackInputStackCancelUpdateTypeDef",
    "ChangeSetHookResourceTargetDetailsTypeDef",
    "ChangeSetHookTargetDetailsTypeDef",
    "ChangeSetHookTypeDef",
    "ChangeSetSummaryTypeDef",
    "ChangeTypeDef",
    "ContinueUpdateRollbackInputRequestTypeDef",
    "CreateChangeSetInputRequestTypeDef",
    "CreateChangeSetOutputTypeDef",
    "CreateStackInputRequestTypeDef",
    "CreateStackInputServiceResourceCreateStackTypeDef",
    "CreateStackInstancesInputRequestTypeDef",
    "CreateStackInstancesOutputTypeDef",
    "CreateStackOutputTypeDef",
    "CreateStackSetInputRequestTypeDef",
    "CreateStackSetOutputTypeDef",
    "DeactivateTypeInputRequestTypeDef",
    "DeleteChangeSetInputRequestTypeDef",
    "DeleteStackInputRequestTypeDef",
    "DeleteStackInputStackDeleteTypeDef",
    "DeleteStackInstancesInputRequestTypeDef",
    "DeleteStackInstancesOutputTypeDef",
    "DeleteStackSetInputRequestTypeDef",
    "DeploymentTargetsTypeDef",
    "DeregisterTypeInputRequestTypeDef",
    "DescribeAccountLimitsInputRequestTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "DescribeChangeSetHooksInputRequestTypeDef",
    "DescribeChangeSetHooksOutputTypeDef",
    "DescribeChangeSetInputRequestTypeDef",
    "DescribeChangeSetOutputTypeDef",
    "DescribePublisherInputRequestTypeDef",
    "DescribePublisherOutputTypeDef",
    "DescribeStackDriftDetectionStatusInputRequestTypeDef",
    "DescribeStackDriftDetectionStatusOutputTypeDef",
    "DescribeStackEventsInputRequestTypeDef",
    "DescribeStackEventsOutputTypeDef",
    "DescribeStackInstanceInputRequestTypeDef",
    "DescribeStackInstanceOutputTypeDef",
    "DescribeStackResourceDriftsInputRequestTypeDef",
    "DescribeStackResourceDriftsOutputTypeDef",
    "DescribeStackResourceInputRequestTypeDef",
    "DescribeStackResourceOutputTypeDef",
    "DescribeStackResourcesInputRequestTypeDef",
    "DescribeStackResourcesOutputTypeDef",
    "DescribeStackSetInputRequestTypeDef",
    "DescribeStackSetOperationInputRequestTypeDef",
    "DescribeStackSetOperationOutputTypeDef",
    "DescribeStackSetOutputTypeDef",
    "DescribeStacksInputRequestTypeDef",
    "DescribeStacksOutputTypeDef",
    "DescribeTypeInputRequestTypeDef",
    "DescribeTypeOutputTypeDef",
    "DescribeTypeRegistrationInputRequestTypeDef",
    "DescribeTypeRegistrationOutputTypeDef",
    "DetectStackDriftInputRequestTypeDef",
    "DetectStackDriftOutputTypeDef",
    "DetectStackResourceDriftInputRequestTypeDef",
    "DetectStackResourceDriftOutputTypeDef",
    "DetectStackSetDriftInputRequestTypeDef",
    "DetectStackSetDriftOutputTypeDef",
    "EstimateTemplateCostInputRequestTypeDef",
    "EstimateTemplateCostOutputTypeDef",
    "ExecuteChangeSetInputRequestTypeDef",
    "ExportTypeDef",
    "GetStackPolicyInputRequestTypeDef",
    "GetStackPolicyOutputTypeDef",
    "GetTemplateInputRequestTypeDef",
    "GetTemplateOutputTypeDef",
    "GetTemplateSummaryInputRequestTypeDef",
    "GetTemplateSummaryOutputTypeDef",
    "ImportStacksToStackSetInputRequestTypeDef",
    "ImportStacksToStackSetOutputTypeDef",
    "ListChangeSetsInputRequestTypeDef",
    "ListChangeSetsOutputTypeDef",
    "ListExportsInputRequestTypeDef",
    "ListExportsOutputTypeDef",
    "ListImportsInputRequestTypeDef",
    "ListImportsOutputTypeDef",
    "ListStackInstancesInputRequestTypeDef",
    "ListStackInstancesOutputTypeDef",
    "ListStackResourcesInputRequestTypeDef",
    "ListStackResourcesOutputTypeDef",
    "ListStackSetOperationResultsInputRequestTypeDef",
    "ListStackSetOperationResultsOutputTypeDef",
    "ListStackSetOperationsInputRequestTypeDef",
    "ListStackSetOperationsOutputTypeDef",
    "ListStackSetsInputRequestTypeDef",
    "ListStackSetsOutputTypeDef",
    "ListStacksInputRequestTypeDef",
    "ListStacksOutputTypeDef",
    "ListTypeRegistrationsInputRequestTypeDef",
    "ListTypeRegistrationsOutputTypeDef",
    "ListTypeVersionsInputRequestTypeDef",
    "ListTypeVersionsOutputTypeDef",
    "ListTypesInputRequestTypeDef",
    "ListTypesOutputTypeDef",
    "LoggingConfigTypeDef",
    "ManagedExecutionTypeDef",
    "ModuleInfoResponseMetadataTypeDef",
    "ModuleInfoTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterConstraintsTypeDef",
    "ParameterDeclarationTypeDef",
    "ParameterTypeDef",
    "PhysicalResourceIdContextKeyValuePairTypeDef",
    "PropertyDifferenceTypeDef",
    "PublishTypeInputRequestTypeDef",
    "PublishTypeOutputTypeDef",
    "RecordHandlerProgressInputRequestTypeDef",
    "RegisterPublisherInputRequestTypeDef",
    "RegisterPublisherOutputTypeDef",
    "RegisterTypeInputRequestTypeDef",
    "RegisterTypeOutputTypeDef",
    "RequiredActivatedTypeTypeDef",
    "ResourceChangeDetailTypeDef",
    "ResourceChangeTypeDef",
    "ResourceIdentifierSummaryTypeDef",
    "ResourceTargetDefinitionTypeDef",
    "ResourceToImportTypeDef",
    "ResponseMetadataTypeDef",
    "RollbackConfigurationResponseMetadataTypeDef",
    "RollbackConfigurationTypeDef",
    "RollbackStackInputRequestTypeDef",
    "RollbackStackOutputTypeDef",
    "RollbackTriggerTypeDef",
    "ServiceResourceEventRequestTypeDef",
    "ServiceResourceStackRequestTypeDef",
    "ServiceResourceStackResourceRequestTypeDef",
    "ServiceResourceStackResourceSummaryRequestTypeDef",
    "SetStackPolicyInputRequestTypeDef",
    "SetTypeConfigurationInputRequestTypeDef",
    "SetTypeConfigurationOutputTypeDef",
    "SetTypeDefaultVersionInputRequestTypeDef",
    "SignalResourceInputRequestTypeDef",
    "StackDriftInformationResponseMetadataTypeDef",
    "StackDriftInformationSummaryTypeDef",
    "StackDriftInformationTypeDef",
    "StackEventTypeDef",
    "StackInstanceComprehensiveStatusTypeDef",
    "StackInstanceFilterTypeDef",
    "StackInstanceSummaryTypeDef",
    "StackInstanceTypeDef",
    "StackResourceDetailTypeDef",
    "StackResourceDriftInformationResponseMetadataTypeDef",
    "StackResourceDriftInformationSummaryResponseMetadataTypeDef",
    "StackResourceDriftInformationSummaryTypeDef",
    "StackResourceDriftInformationTypeDef",
    "StackResourceDriftTypeDef",
    "StackResourceRequestTypeDef",
    "StackResourceSummaryTypeDef",
    "StackResourceTypeDef",
    "StackSetDriftDetectionDetailsTypeDef",
    "StackSetOperationPreferencesTypeDef",
    "StackSetOperationResultSummaryTypeDef",
    "StackSetOperationSummaryTypeDef",
    "StackSetOperationTypeDef",
    "StackSetSummaryTypeDef",
    "StackSetTypeDef",
    "StackSummaryTypeDef",
    "StackTypeDef",
    "StopStackSetOperationInputRequestTypeDef",
    "TagTypeDef",
    "TemplateParameterTypeDef",
    "TestTypeInputRequestTypeDef",
    "TestTypeOutputTypeDef",
    "TypeConfigurationDetailsTypeDef",
    "TypeConfigurationIdentifierTypeDef",
    "TypeFiltersTypeDef",
    "TypeSummaryTypeDef",
    "TypeVersionSummaryTypeDef",
    "UpdateStackInputRequestTypeDef",
    "UpdateStackInputStackUpdateTypeDef",
    "UpdateStackInstancesInputRequestTypeDef",
    "UpdateStackInstancesOutputTypeDef",
    "UpdateStackOutputTypeDef",
    "UpdateStackSetInputRequestTypeDef",
    "UpdateStackSetOutputTypeDef",
    "UpdateTerminationProtectionInputRequestTypeDef",
    "UpdateTerminationProtectionOutputTypeDef",
    "ValidateTemplateInputRequestTypeDef",
    "ValidateTemplateOutputTypeDef",
    "WaiterConfigTypeDef",
)

AccountGateResultTypeDef = TypedDict(
    "AccountGateResultTypeDef",
    {
        "Status": NotRequired[AccountGateStatusType],
        "StatusReason": NotRequired[str],
    },
)

AccountLimitTypeDef = TypedDict(
    "AccountLimitTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[int],
    },
)

ActivateTypeInputRequestTypeDef = TypedDict(
    "ActivateTypeInputRequestTypeDef",
    {
        "Type": NotRequired[ThirdPartyTypeType],
        "PublicTypeArn": NotRequired[str],
        "PublisherId": NotRequired[str],
        "TypeName": NotRequired[str],
        "TypeNameAlias": NotRequired[str],
        "AutoUpdate": NotRequired[bool],
        "LoggingConfig": NotRequired["LoggingConfigTypeDef"],
        "ExecutionRoleArn": NotRequired[str],
        "VersionBump": NotRequired[VersionBumpType],
        "MajorVersion": NotRequired[int],
    },
)

ActivateTypeOutputTypeDef = TypedDict(
    "ActivateTypeOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AutoDeploymentTypeDef = TypedDict(
    "AutoDeploymentTypeDef",
    {
        "Enabled": NotRequired[bool],
        "RetainStacksOnAccountRemoval": NotRequired[bool],
    },
)

BatchDescribeTypeConfigurationsErrorTypeDef = TypedDict(
    "BatchDescribeTypeConfigurationsErrorTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "TypeConfigurationIdentifier": NotRequired["TypeConfigurationIdentifierTypeDef"],
    },
)

BatchDescribeTypeConfigurationsInputRequestTypeDef = TypedDict(
    "BatchDescribeTypeConfigurationsInputRequestTypeDef",
    {
        "TypeConfigurationIdentifiers": Sequence["TypeConfigurationIdentifierTypeDef"],
    },
)

BatchDescribeTypeConfigurationsOutputTypeDef = TypedDict(
    "BatchDescribeTypeConfigurationsOutputTypeDef",
    {
        "Errors": List["BatchDescribeTypeConfigurationsErrorTypeDef"],
        "UnprocessedTypeConfigurations": List["TypeConfigurationIdentifierTypeDef"],
        "TypeConfigurations": List["TypeConfigurationDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelUpdateStackInputRequestTypeDef = TypedDict(
    "CancelUpdateStackInputRequestTypeDef",
    {
        "StackName": str,
        "ClientRequestToken": NotRequired[str],
    },
)

CancelUpdateStackInputStackCancelUpdateTypeDef = TypedDict(
    "CancelUpdateStackInputStackCancelUpdateTypeDef",
    {
        "ClientRequestToken": NotRequired[str],
    },
)

ChangeSetHookResourceTargetDetailsTypeDef = TypedDict(
    "ChangeSetHookResourceTargetDetailsTypeDef",
    {
        "LogicalResourceId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceAction": NotRequired[ChangeActionType],
    },
)

ChangeSetHookTargetDetailsTypeDef = TypedDict(
    "ChangeSetHookTargetDetailsTypeDef",
    {
        "TargetType": NotRequired[Literal["RESOURCE"]],
        "ResourceTargetDetails": NotRequired["ChangeSetHookResourceTargetDetailsTypeDef"],
    },
)

ChangeSetHookTypeDef = TypedDict(
    "ChangeSetHookTypeDef",
    {
        "InvocationPoint": NotRequired[Literal["PRE_PROVISION"]],
        "FailureMode": NotRequired[HookFailureModeType],
        "TypeName": NotRequired[str],
        "TypeVersionId": NotRequired[str],
        "TypeConfigurationVersionId": NotRequired[str],
        "TargetDetails": NotRequired["ChangeSetHookTargetDetailsTypeDef"],
    },
)

ChangeSetSummaryTypeDef = TypedDict(
    "ChangeSetSummaryTypeDef",
    {
        "StackId": NotRequired[str],
        "StackName": NotRequired[str],
        "ChangeSetId": NotRequired[str],
        "ChangeSetName": NotRequired[str],
        "ExecutionStatus": NotRequired[ExecutionStatusType],
        "Status": NotRequired[ChangeSetStatusType],
        "StatusReason": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "Description": NotRequired[str],
        "IncludeNestedStacks": NotRequired[bool],
        "ParentChangeSetId": NotRequired[str],
        "RootChangeSetId": NotRequired[str],
    },
)

ChangeTypeDef = TypedDict(
    "ChangeTypeDef",
    {
        "Type": NotRequired[Literal["Resource"]],
        "HookInvocationCount": NotRequired[int],
        "ResourceChange": NotRequired["ResourceChangeTypeDef"],
    },
)

ContinueUpdateRollbackInputRequestTypeDef = TypedDict(
    "ContinueUpdateRollbackInputRequestTypeDef",
    {
        "StackName": str,
        "RoleARN": NotRequired[str],
        "ResourcesToSkip": NotRequired[Sequence[str]],
        "ClientRequestToken": NotRequired[str],
    },
)

CreateChangeSetInputRequestTypeDef = TypedDict(
    "CreateChangeSetInputRequestTypeDef",
    {
        "StackName": str,
        "ChangeSetName": str,
        "TemplateBody": NotRequired[str],
        "TemplateURL": NotRequired[str],
        "UsePreviousTemplate": NotRequired[bool],
        "Parameters": NotRequired[Sequence["ParameterTypeDef"]],
        "Capabilities": NotRequired[Sequence[CapabilityType]],
        "ResourceTypes": NotRequired[Sequence[str]],
        "RoleARN": NotRequired[str],
        "RollbackConfiguration": NotRequired["RollbackConfigurationTypeDef"],
        "NotificationARNs": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "ChangeSetType": NotRequired[ChangeSetTypeType],
        "ResourcesToImport": NotRequired[Sequence["ResourceToImportTypeDef"]],
        "IncludeNestedStacks": NotRequired[bool],
    },
)

CreateChangeSetOutputTypeDef = TypedDict(
    "CreateChangeSetOutputTypeDef",
    {
        "Id": str,
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStackInputRequestTypeDef = TypedDict(
    "CreateStackInputRequestTypeDef",
    {
        "StackName": str,
        "TemplateBody": NotRequired[str],
        "TemplateURL": NotRequired[str],
        "Parameters": NotRequired[Sequence["ParameterTypeDef"]],
        "DisableRollback": NotRequired[bool],
        "RollbackConfiguration": NotRequired["RollbackConfigurationTypeDef"],
        "TimeoutInMinutes": NotRequired[int],
        "NotificationARNs": NotRequired[Sequence[str]],
        "Capabilities": NotRequired[Sequence[CapabilityType]],
        "ResourceTypes": NotRequired[Sequence[str]],
        "RoleARN": NotRequired[str],
        "OnFailure": NotRequired[OnFailureType],
        "StackPolicyBody": NotRequired[str],
        "StackPolicyURL": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ClientRequestToken": NotRequired[str],
        "EnableTerminationProtection": NotRequired[bool],
    },
)

CreateStackInputServiceResourceCreateStackTypeDef = TypedDict(
    "CreateStackInputServiceResourceCreateStackTypeDef",
    {
        "StackName": str,
        "TemplateBody": NotRequired[str],
        "TemplateURL": NotRequired[str],
        "Parameters": NotRequired[Sequence["ParameterTypeDef"]],
        "DisableRollback": NotRequired[bool],
        "RollbackConfiguration": NotRequired["RollbackConfigurationTypeDef"],
        "TimeoutInMinutes": NotRequired[int],
        "NotificationARNs": NotRequired[Sequence[str]],
        "Capabilities": NotRequired[Sequence[CapabilityType]],
        "ResourceTypes": NotRequired[Sequence[str]],
        "RoleARN": NotRequired[str],
        "OnFailure": NotRequired[OnFailureType],
        "StackPolicyBody": NotRequired[str],
        "StackPolicyURL": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ClientRequestToken": NotRequired[str],
        "EnableTerminationProtection": NotRequired[bool],
    },
)

CreateStackInstancesInputRequestTypeDef = TypedDict(
    "CreateStackInstancesInputRequestTypeDef",
    {
        "StackSetName": str,
        "Regions": Sequence[str],
        "Accounts": NotRequired[Sequence[str]],
        "DeploymentTargets": NotRequired["DeploymentTargetsTypeDef"],
        "ParameterOverrides": NotRequired[Sequence["ParameterTypeDef"]],
        "OperationPreferences": NotRequired["StackSetOperationPreferencesTypeDef"],
        "OperationId": NotRequired[str],
        "CallAs": NotRequired[CallAsType],
    },
)

CreateStackInstancesOutputTypeDef = TypedDict(
    "CreateStackInstancesOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStackOutputTypeDef = TypedDict(
    "CreateStackOutputTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStackSetInputRequestTypeDef = TypedDict(
    "CreateStackSetInputRequestTypeDef",
    {
        "StackSetName": str,
        "Description": NotRequired[str],
        "TemplateBody": NotRequired[str],
        "TemplateURL": NotRequired[str],
        "StackId": NotRequired[str],
        "Parameters": NotRequired[Sequence["ParameterTypeDef"]],
        "Capabilities": NotRequired[Sequence[CapabilityType]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "AdministrationRoleARN": NotRequired[str],
        "ExecutionRoleName": NotRequired[str],
        "PermissionModel": NotRequired[PermissionModelsType],
        "AutoDeployment": NotRequired["AutoDeploymentTypeDef"],
        "CallAs": NotRequired[CallAsType],
        "ClientRequestToken": NotRequired[str],
        "ManagedExecution": NotRequired["ManagedExecutionTypeDef"],
    },
)

CreateStackSetOutputTypeDef = TypedDict(
    "CreateStackSetOutputTypeDef",
    {
        "StackSetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeactivateTypeInputRequestTypeDef = TypedDict(
    "DeactivateTypeInputRequestTypeDef",
    {
        "TypeName": NotRequired[str],
        "Type": NotRequired[ThirdPartyTypeType],
        "Arn": NotRequired[str],
    },
)

DeleteChangeSetInputRequestTypeDef = TypedDict(
    "DeleteChangeSetInputRequestTypeDef",
    {
        "ChangeSetName": str,
        "StackName": NotRequired[str],
    },
)

DeleteStackInputRequestTypeDef = TypedDict(
    "DeleteStackInputRequestTypeDef",
    {
        "StackName": str,
        "RetainResources": NotRequired[Sequence[str]],
        "RoleARN": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
    },
)

DeleteStackInputStackDeleteTypeDef = TypedDict(
    "DeleteStackInputStackDeleteTypeDef",
    {
        "RetainResources": NotRequired[Sequence[str]],
        "RoleARN": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
    },
)

DeleteStackInstancesInputRequestTypeDef = TypedDict(
    "DeleteStackInstancesInputRequestTypeDef",
    {
        "StackSetName": str,
        "Regions": Sequence[str],
        "RetainStacks": bool,
        "Accounts": NotRequired[Sequence[str]],
        "DeploymentTargets": NotRequired["DeploymentTargetsTypeDef"],
        "OperationPreferences": NotRequired["StackSetOperationPreferencesTypeDef"],
        "OperationId": NotRequired[str],
        "CallAs": NotRequired[CallAsType],
    },
)

DeleteStackInstancesOutputTypeDef = TypedDict(
    "DeleteStackInstancesOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteStackSetInputRequestTypeDef = TypedDict(
    "DeleteStackSetInputRequestTypeDef",
    {
        "StackSetName": str,
        "CallAs": NotRequired[CallAsType],
    },
)

DeploymentTargetsTypeDef = TypedDict(
    "DeploymentTargetsTypeDef",
    {
        "Accounts": NotRequired[Sequence[str]],
        "AccountsUrl": NotRequired[str],
        "OrganizationalUnitIds": NotRequired[Sequence[str]],
    },
)

DeregisterTypeInputRequestTypeDef = TypedDict(
    "DeregisterTypeInputRequestTypeDef",
    {
        "Arn": NotRequired[str],
        "Type": NotRequired[RegistryTypeType],
        "TypeName": NotRequired[str],
        "VersionId": NotRequired[str],
    },
)

DescribeAccountLimitsInputRequestTypeDef = TypedDict(
    "DescribeAccountLimitsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)

DescribeAccountLimitsOutputTypeDef = TypedDict(
    "DescribeAccountLimitsOutputTypeDef",
    {
        "AccountLimits": List["AccountLimitTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChangeSetHooksInputRequestTypeDef = TypedDict(
    "DescribeChangeSetHooksInputRequestTypeDef",
    {
        "ChangeSetName": str,
        "StackName": NotRequired[str],
        "NextToken": NotRequired[str],
        "LogicalResourceId": NotRequired[str],
    },
)

DescribeChangeSetHooksOutputTypeDef = TypedDict(
    "DescribeChangeSetHooksOutputTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetName": str,
        "Hooks": List["ChangeSetHookTypeDef"],
        "Status": ChangeSetHooksStatusType,
        "NextToken": str,
        "StackId": str,
        "StackName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChangeSetInputRequestTypeDef = TypedDict(
    "DescribeChangeSetInputRequestTypeDef",
    {
        "ChangeSetName": str,
        "StackName": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

DescribeChangeSetOutputTypeDef = TypedDict(
    "DescribeChangeSetOutputTypeDef",
    {
        "ChangeSetName": str,
        "ChangeSetId": str,
        "StackId": str,
        "StackName": str,
        "Description": str,
        "Parameters": List["ParameterTypeDef"],
        "CreationTime": datetime,
        "ExecutionStatus": ExecutionStatusType,
        "Status": ChangeSetStatusType,
        "StatusReason": str,
        "NotificationARNs": List[str],
        "RollbackConfiguration": "RollbackConfigurationTypeDef",
        "Capabilities": List[CapabilityType],
        "Tags": List["TagTypeDef"],
        "Changes": List["ChangeTypeDef"],
        "NextToken": str,
        "IncludeNestedStacks": bool,
        "ParentChangeSetId": str,
        "RootChangeSetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePublisherInputRequestTypeDef = TypedDict(
    "DescribePublisherInputRequestTypeDef",
    {
        "PublisherId": NotRequired[str],
    },
)

DescribePublisherOutputTypeDef = TypedDict(
    "DescribePublisherOutputTypeDef",
    {
        "PublisherId": str,
        "PublisherStatus": PublisherStatusType,
        "IdentityProvider": IdentityProviderType,
        "PublisherProfile": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackDriftDetectionStatusInputRequestTypeDef = TypedDict(
    "DescribeStackDriftDetectionStatusInputRequestTypeDef",
    {
        "StackDriftDetectionId": str,
    },
)

DescribeStackDriftDetectionStatusOutputTypeDef = TypedDict(
    "DescribeStackDriftDetectionStatusOutputTypeDef",
    {
        "StackId": str,
        "StackDriftDetectionId": str,
        "StackDriftStatus": StackDriftStatusType,
        "DetectionStatus": StackDriftDetectionStatusType,
        "DetectionStatusReason": str,
        "DriftedStackResourceCount": int,
        "Timestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackEventsInputRequestTypeDef = TypedDict(
    "DescribeStackEventsInputRequestTypeDef",
    {
        "StackName": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

DescribeStackEventsOutputTypeDef = TypedDict(
    "DescribeStackEventsOutputTypeDef",
    {
        "StackEvents": List["StackEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackInstanceInputRequestTypeDef = TypedDict(
    "DescribeStackInstanceInputRequestTypeDef",
    {
        "StackSetName": str,
        "StackInstanceAccount": str,
        "StackInstanceRegion": str,
        "CallAs": NotRequired[CallAsType],
    },
)

DescribeStackInstanceOutputTypeDef = TypedDict(
    "DescribeStackInstanceOutputTypeDef",
    {
        "StackInstance": "StackInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackResourceDriftsInputRequestTypeDef = TypedDict(
    "DescribeStackResourceDriftsInputRequestTypeDef",
    {
        "StackName": str,
        "StackResourceDriftStatusFilters": NotRequired[Sequence[StackResourceDriftStatusType]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeStackResourceDriftsOutputTypeDef = TypedDict(
    "DescribeStackResourceDriftsOutputTypeDef",
    {
        "StackResourceDrifts": List["StackResourceDriftTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackResourceInputRequestTypeDef = TypedDict(
    "DescribeStackResourceInputRequestTypeDef",
    {
        "StackName": str,
        "LogicalResourceId": str,
    },
)

DescribeStackResourceOutputTypeDef = TypedDict(
    "DescribeStackResourceOutputTypeDef",
    {
        "StackResourceDetail": "StackResourceDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackResourcesInputRequestTypeDef = TypedDict(
    "DescribeStackResourcesInputRequestTypeDef",
    {
        "StackName": NotRequired[str],
        "LogicalResourceId": NotRequired[str],
        "PhysicalResourceId": NotRequired[str],
    },
)

DescribeStackResourcesOutputTypeDef = TypedDict(
    "DescribeStackResourcesOutputTypeDef",
    {
        "StackResources": List["StackResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackSetInputRequestTypeDef = TypedDict(
    "DescribeStackSetInputRequestTypeDef",
    {
        "StackSetName": str,
        "CallAs": NotRequired[CallAsType],
    },
)

DescribeStackSetOperationInputRequestTypeDef = TypedDict(
    "DescribeStackSetOperationInputRequestTypeDef",
    {
        "StackSetName": str,
        "OperationId": str,
        "CallAs": NotRequired[CallAsType],
    },
)

DescribeStackSetOperationOutputTypeDef = TypedDict(
    "DescribeStackSetOperationOutputTypeDef",
    {
        "StackSetOperation": "StackSetOperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackSetOutputTypeDef = TypedDict(
    "DescribeStackSetOutputTypeDef",
    {
        "StackSet": "StackSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStacksInputRequestTypeDef = TypedDict(
    "DescribeStacksInputRequestTypeDef",
    {
        "StackName": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

DescribeStacksOutputTypeDef = TypedDict(
    "DescribeStacksOutputTypeDef",
    {
        "Stacks": List["StackTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTypeInputRequestTypeDef = TypedDict(
    "DescribeTypeInputRequestTypeDef",
    {
        "Type": NotRequired[RegistryTypeType],
        "TypeName": NotRequired[str],
        "Arn": NotRequired[str],
        "VersionId": NotRequired[str],
        "PublisherId": NotRequired[str],
        "PublicVersionNumber": NotRequired[str],
    },
)

DescribeTypeOutputTypeDef = TypedDict(
    "DescribeTypeOutputTypeDef",
    {
        "Arn": str,
        "Type": RegistryTypeType,
        "TypeName": str,
        "DefaultVersionId": str,
        "IsDefaultVersion": bool,
        "TypeTestsStatus": TypeTestsStatusType,
        "TypeTestsStatusDescription": str,
        "Description": str,
        "Schema": str,
        "ProvisioningType": ProvisioningTypeType,
        "DeprecatedStatus": DeprecatedStatusType,
        "LoggingConfig": "LoggingConfigTypeDef",
        "RequiredActivatedTypes": List["RequiredActivatedTypeTypeDef"],
        "ExecutionRoleArn": str,
        "Visibility": VisibilityType,
        "SourceUrl": str,
        "DocumentationUrl": str,
        "LastUpdated": datetime,
        "TimeCreated": datetime,
        "ConfigurationSchema": str,
        "PublisherId": str,
        "OriginalTypeName": str,
        "OriginalTypeArn": str,
        "PublicVersionNumber": str,
        "LatestPublicVersion": str,
        "IsActivated": bool,
        "AutoUpdate": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTypeRegistrationInputRequestTypeDef = TypedDict(
    "DescribeTypeRegistrationInputRequestTypeDef",
    {
        "RegistrationToken": str,
    },
)

DescribeTypeRegistrationOutputTypeDef = TypedDict(
    "DescribeTypeRegistrationOutputTypeDef",
    {
        "ProgressStatus": RegistrationStatusType,
        "Description": str,
        "TypeArn": str,
        "TypeVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectStackDriftInputRequestTypeDef = TypedDict(
    "DetectStackDriftInputRequestTypeDef",
    {
        "StackName": str,
        "LogicalResourceIds": NotRequired[Sequence[str]],
    },
)

DetectStackDriftOutputTypeDef = TypedDict(
    "DetectStackDriftOutputTypeDef",
    {
        "StackDriftDetectionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectStackResourceDriftInputRequestTypeDef = TypedDict(
    "DetectStackResourceDriftInputRequestTypeDef",
    {
        "StackName": str,
        "LogicalResourceId": str,
    },
)

DetectStackResourceDriftOutputTypeDef = TypedDict(
    "DetectStackResourceDriftOutputTypeDef",
    {
        "StackResourceDrift": "StackResourceDriftTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectStackSetDriftInputRequestTypeDef = TypedDict(
    "DetectStackSetDriftInputRequestTypeDef",
    {
        "StackSetName": str,
        "OperationPreferences": NotRequired["StackSetOperationPreferencesTypeDef"],
        "OperationId": NotRequired[str],
        "CallAs": NotRequired[CallAsType],
    },
)

DetectStackSetDriftOutputTypeDef = TypedDict(
    "DetectStackSetDriftOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EstimateTemplateCostInputRequestTypeDef = TypedDict(
    "EstimateTemplateCostInputRequestTypeDef",
    {
        "TemplateBody": NotRequired[str],
        "TemplateURL": NotRequired[str],
        "Parameters": NotRequired[Sequence["ParameterTypeDef"]],
    },
)

EstimateTemplateCostOutputTypeDef = TypedDict(
    "EstimateTemplateCostOutputTypeDef",
    {
        "Url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExecuteChangeSetInputRequestTypeDef = TypedDict(
    "ExecuteChangeSetInputRequestTypeDef",
    {
        "ChangeSetName": str,
        "StackName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "DisableRollback": NotRequired[bool],
    },
)

ExportTypeDef = TypedDict(
    "ExportTypeDef",
    {
        "ExportingStackId": NotRequired[str],
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)

GetStackPolicyInputRequestTypeDef = TypedDict(
    "GetStackPolicyInputRequestTypeDef",
    {
        "StackName": str,
    },
)

GetStackPolicyOutputTypeDef = TypedDict(
    "GetStackPolicyOutputTypeDef",
    {
        "StackPolicyBody": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTemplateInputRequestTypeDef = TypedDict(
    "GetTemplateInputRequestTypeDef",
    {
        "StackName": NotRequired[str],
        "ChangeSetName": NotRequired[str],
        "TemplateStage": NotRequired[TemplateStageType],
    },
)

GetTemplateOutputTypeDef = TypedDict(
    "GetTemplateOutputTypeDef",
    {
        "TemplateBody": str,
        "StagesAvailable": List[TemplateStageType],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTemplateSummaryInputRequestTypeDef = TypedDict(
    "GetTemplateSummaryInputRequestTypeDef",
    {
        "TemplateBody": NotRequired[str],
        "TemplateURL": NotRequired[str],
        "StackName": NotRequired[str],
        "StackSetName": NotRequired[str],
        "CallAs": NotRequired[CallAsType],
    },
)

GetTemplateSummaryOutputTypeDef = TypedDict(
    "GetTemplateSummaryOutputTypeDef",
    {
        "Parameters": List["ParameterDeclarationTypeDef"],
        "Description": str,
        "Capabilities": List[CapabilityType],
        "CapabilitiesReason": str,
        "ResourceTypes": List[str],
        "Version": str,
        "Metadata": str,
        "DeclaredTransforms": List[str],
        "ResourceIdentifierSummaries": List["ResourceIdentifierSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportStacksToStackSetInputRequestTypeDef = TypedDict(
    "ImportStacksToStackSetInputRequestTypeDef",
    {
        "StackSetName": str,
        "StackIds": NotRequired[Sequence[str]],
        "StackIdsUrl": NotRequired[str],
        "OrganizationalUnitIds": NotRequired[Sequence[str]],
        "OperationPreferences": NotRequired["StackSetOperationPreferencesTypeDef"],
        "OperationId": NotRequired[str],
        "CallAs": NotRequired[CallAsType],
    },
)

ImportStacksToStackSetOutputTypeDef = TypedDict(
    "ImportStacksToStackSetOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChangeSetsInputRequestTypeDef = TypedDict(
    "ListChangeSetsInputRequestTypeDef",
    {
        "StackName": str,
        "NextToken": NotRequired[str],
    },
)

ListChangeSetsOutputTypeDef = TypedDict(
    "ListChangeSetsOutputTypeDef",
    {
        "Summaries": List["ChangeSetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExportsInputRequestTypeDef = TypedDict(
    "ListExportsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)

ListExportsOutputTypeDef = TypedDict(
    "ListExportsOutputTypeDef",
    {
        "Exports": List["ExportTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImportsInputRequestTypeDef = TypedDict(
    "ListImportsInputRequestTypeDef",
    {
        "ExportName": str,
        "NextToken": NotRequired[str],
    },
)

ListImportsOutputTypeDef = TypedDict(
    "ListImportsOutputTypeDef",
    {
        "Imports": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStackInstancesInputRequestTypeDef = TypedDict(
    "ListStackInstancesInputRequestTypeDef",
    {
        "StackSetName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence["StackInstanceFilterTypeDef"]],
        "StackInstanceAccount": NotRequired[str],
        "StackInstanceRegion": NotRequired[str],
        "CallAs": NotRequired[CallAsType],
    },
)

ListStackInstancesOutputTypeDef = TypedDict(
    "ListStackInstancesOutputTypeDef",
    {
        "Summaries": List["StackInstanceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStackResourcesInputRequestTypeDef = TypedDict(
    "ListStackResourcesInputRequestTypeDef",
    {
        "StackName": str,
        "NextToken": NotRequired[str],
    },
)

ListStackResourcesOutputTypeDef = TypedDict(
    "ListStackResourcesOutputTypeDef",
    {
        "StackResourceSummaries": List["StackResourceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStackSetOperationResultsInputRequestTypeDef = TypedDict(
    "ListStackSetOperationResultsInputRequestTypeDef",
    {
        "StackSetName": str,
        "OperationId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "CallAs": NotRequired[CallAsType],
    },
)

ListStackSetOperationResultsOutputTypeDef = TypedDict(
    "ListStackSetOperationResultsOutputTypeDef",
    {
        "Summaries": List["StackSetOperationResultSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStackSetOperationsInputRequestTypeDef = TypedDict(
    "ListStackSetOperationsInputRequestTypeDef",
    {
        "StackSetName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "CallAs": NotRequired[CallAsType],
    },
)

ListStackSetOperationsOutputTypeDef = TypedDict(
    "ListStackSetOperationsOutputTypeDef",
    {
        "Summaries": List["StackSetOperationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStackSetsInputRequestTypeDef = TypedDict(
    "ListStackSetsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Status": NotRequired[StackSetStatusType],
        "CallAs": NotRequired[CallAsType],
    },
)

ListStackSetsOutputTypeDef = TypedDict(
    "ListStackSetsOutputTypeDef",
    {
        "Summaries": List["StackSetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStacksInputRequestTypeDef = TypedDict(
    "ListStacksInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "StackStatusFilter": NotRequired[Sequence[StackStatusType]],
    },
)

ListStacksOutputTypeDef = TypedDict(
    "ListStacksOutputTypeDef",
    {
        "StackSummaries": List["StackSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTypeRegistrationsInputRequestTypeDef = TypedDict(
    "ListTypeRegistrationsInputRequestTypeDef",
    {
        "Type": NotRequired[RegistryTypeType],
        "TypeName": NotRequired[str],
        "TypeArn": NotRequired[str],
        "RegistrationStatusFilter": NotRequired[RegistrationStatusType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListTypeRegistrationsOutputTypeDef = TypedDict(
    "ListTypeRegistrationsOutputTypeDef",
    {
        "RegistrationTokenList": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTypeVersionsInputRequestTypeDef = TypedDict(
    "ListTypeVersionsInputRequestTypeDef",
    {
        "Type": NotRequired[RegistryTypeType],
        "TypeName": NotRequired[str],
        "Arn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DeprecatedStatus": NotRequired[DeprecatedStatusType],
        "PublisherId": NotRequired[str],
    },
)

ListTypeVersionsOutputTypeDef = TypedDict(
    "ListTypeVersionsOutputTypeDef",
    {
        "TypeVersionSummaries": List["TypeVersionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTypesInputRequestTypeDef = TypedDict(
    "ListTypesInputRequestTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
        "ProvisioningType": NotRequired[ProvisioningTypeType],
        "DeprecatedStatus": NotRequired[DeprecatedStatusType],
        "Type": NotRequired[RegistryTypeType],
        "Filters": NotRequired["TypeFiltersTypeDef"],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListTypesOutputTypeDef = TypedDict(
    "ListTypesOutputTypeDef",
    {
        "TypeSummaries": List["TypeSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingConfigTypeDef = TypedDict(
    "LoggingConfigTypeDef",
    {
        "LogRoleArn": str,
        "LogGroupName": str,
    },
)

ManagedExecutionTypeDef = TypedDict(
    "ManagedExecutionTypeDef",
    {
        "Active": NotRequired[bool],
    },
)

ModuleInfoResponseMetadataTypeDef = TypedDict(
    "ModuleInfoResponseMetadataTypeDef",
    {
        "TypeHierarchy": str,
        "LogicalIdHierarchy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModuleInfoTypeDef = TypedDict(
    "ModuleInfoTypeDef",
    {
        "TypeHierarchy": NotRequired[str],
        "LogicalIdHierarchy": NotRequired[str],
    },
)

OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "OutputKey": NotRequired[str],
        "OutputValue": NotRequired[str],
        "Description": NotRequired[str],
        "ExportName": NotRequired[str],
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

ParameterConstraintsTypeDef = TypedDict(
    "ParameterConstraintsTypeDef",
    {
        "AllowedValues": NotRequired[List[str]],
    },
)

ParameterDeclarationTypeDef = TypedDict(
    "ParameterDeclarationTypeDef",
    {
        "ParameterKey": NotRequired[str],
        "DefaultValue": NotRequired[str],
        "ParameterType": NotRequired[str],
        "NoEcho": NotRequired[bool],
        "Description": NotRequired[str],
        "ParameterConstraints": NotRequired["ParameterConstraintsTypeDef"],
    },
)

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "ParameterKey": NotRequired[str],
        "ParameterValue": NotRequired[str],
        "UsePreviousValue": NotRequired[bool],
        "ResolvedValue": NotRequired[str],
    },
)

PhysicalResourceIdContextKeyValuePairTypeDef = TypedDict(
    "PhysicalResourceIdContextKeyValuePairTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

PropertyDifferenceTypeDef = TypedDict(
    "PropertyDifferenceTypeDef",
    {
        "PropertyPath": str,
        "ExpectedValue": str,
        "ActualValue": str,
        "DifferenceType": DifferenceTypeType,
    },
)

PublishTypeInputRequestTypeDef = TypedDict(
    "PublishTypeInputRequestTypeDef",
    {
        "Type": NotRequired[ThirdPartyTypeType],
        "Arn": NotRequired[str],
        "TypeName": NotRequired[str],
        "PublicVersionNumber": NotRequired[str],
    },
)

PublishTypeOutputTypeDef = TypedDict(
    "PublishTypeOutputTypeDef",
    {
        "PublicTypeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecordHandlerProgressInputRequestTypeDef = TypedDict(
    "RecordHandlerProgressInputRequestTypeDef",
    {
        "BearerToken": str,
        "OperationStatus": OperationStatusType,
        "CurrentOperationStatus": NotRequired[OperationStatusType],
        "StatusMessage": NotRequired[str],
        "ErrorCode": NotRequired[HandlerErrorCodeType],
        "ResourceModel": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
    },
)

RegisterPublisherInputRequestTypeDef = TypedDict(
    "RegisterPublisherInputRequestTypeDef",
    {
        "AcceptTermsAndConditions": NotRequired[bool],
        "ConnectionArn": NotRequired[str],
    },
)

RegisterPublisherOutputTypeDef = TypedDict(
    "RegisterPublisherOutputTypeDef",
    {
        "PublisherId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterTypeInputRequestTypeDef = TypedDict(
    "RegisterTypeInputRequestTypeDef",
    {
        "TypeName": str,
        "SchemaHandlerPackage": str,
        "Type": NotRequired[RegistryTypeType],
        "LoggingConfig": NotRequired["LoggingConfigTypeDef"],
        "ExecutionRoleArn": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
    },
)

RegisterTypeOutputTypeDef = TypedDict(
    "RegisterTypeOutputTypeDef",
    {
        "RegistrationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequiredActivatedTypeTypeDef = TypedDict(
    "RequiredActivatedTypeTypeDef",
    {
        "TypeNameAlias": NotRequired[str],
        "OriginalTypeName": NotRequired[str],
        "PublisherId": NotRequired[str],
        "SupportedMajorVersions": NotRequired[List[int]],
    },
)

ResourceChangeDetailTypeDef = TypedDict(
    "ResourceChangeDetailTypeDef",
    {
        "Target": NotRequired["ResourceTargetDefinitionTypeDef"],
        "Evaluation": NotRequired[EvaluationTypeType],
        "ChangeSource": NotRequired[ChangeSourceType],
        "CausingEntity": NotRequired[str],
    },
)

ResourceChangeTypeDef = TypedDict(
    "ResourceChangeTypeDef",
    {
        "Action": NotRequired[ChangeActionType],
        "LogicalResourceId": NotRequired[str],
        "PhysicalResourceId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "Replacement": NotRequired[ReplacementType],
        "Scope": NotRequired[List[ResourceAttributeType]],
        "Details": NotRequired[List["ResourceChangeDetailTypeDef"]],
        "ChangeSetId": NotRequired[str],
        "ModuleInfo": NotRequired["ModuleInfoTypeDef"],
    },
)

ResourceIdentifierSummaryTypeDef = TypedDict(
    "ResourceIdentifierSummaryTypeDef",
    {
        "ResourceType": NotRequired[str],
        "LogicalResourceIds": NotRequired[List[str]],
        "ResourceIdentifiers": NotRequired[List[str]],
    },
)

ResourceTargetDefinitionTypeDef = TypedDict(
    "ResourceTargetDefinitionTypeDef",
    {
        "Attribute": NotRequired[ResourceAttributeType],
        "Name": NotRequired[str],
        "RequiresRecreation": NotRequired[RequiresRecreationType],
    },
)

ResourceToImportTypeDef = TypedDict(
    "ResourceToImportTypeDef",
    {
        "ResourceType": str,
        "LogicalResourceId": str,
        "ResourceIdentifier": Mapping[str, str],
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

RollbackConfigurationResponseMetadataTypeDef = TypedDict(
    "RollbackConfigurationResponseMetadataTypeDef",
    {
        "RollbackTriggers": List["RollbackTriggerTypeDef"],
        "MonitoringTimeInMinutes": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RollbackConfigurationTypeDef = TypedDict(
    "RollbackConfigurationTypeDef",
    {
        "RollbackTriggers": NotRequired[Sequence["RollbackTriggerTypeDef"]],
        "MonitoringTimeInMinutes": NotRequired[int],
    },
)

RollbackStackInputRequestTypeDef = TypedDict(
    "RollbackStackInputRequestTypeDef",
    {
        "StackName": str,
        "RoleARN": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
    },
)

RollbackStackOutputTypeDef = TypedDict(
    "RollbackStackOutputTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RollbackTriggerTypeDef = TypedDict(
    "RollbackTriggerTypeDef",
    {
        "Arn": str,
        "Type": str,
    },
)

ServiceResourceEventRequestTypeDef = TypedDict(
    "ServiceResourceEventRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceStackRequestTypeDef = TypedDict(
    "ServiceResourceStackRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceStackResourceRequestTypeDef = TypedDict(
    "ServiceResourceStackResourceRequestTypeDef",
    {
        "stack_name": str,
        "logical_id": str,
    },
)

ServiceResourceStackResourceSummaryRequestTypeDef = TypedDict(
    "ServiceResourceStackResourceSummaryRequestTypeDef",
    {
        "stack_name": str,
        "logical_id": str,
    },
)

SetStackPolicyInputRequestTypeDef = TypedDict(
    "SetStackPolicyInputRequestTypeDef",
    {
        "StackName": str,
        "StackPolicyBody": NotRequired[str],
        "StackPolicyURL": NotRequired[str],
    },
)

SetTypeConfigurationInputRequestTypeDef = TypedDict(
    "SetTypeConfigurationInputRequestTypeDef",
    {
        "Configuration": str,
        "TypeArn": NotRequired[str],
        "ConfigurationAlias": NotRequired[str],
        "TypeName": NotRequired[str],
        "Type": NotRequired[ThirdPartyTypeType],
    },
)

SetTypeConfigurationOutputTypeDef = TypedDict(
    "SetTypeConfigurationOutputTypeDef",
    {
        "ConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetTypeDefaultVersionInputRequestTypeDef = TypedDict(
    "SetTypeDefaultVersionInputRequestTypeDef",
    {
        "Arn": NotRequired[str],
        "Type": NotRequired[RegistryTypeType],
        "TypeName": NotRequired[str],
        "VersionId": NotRequired[str],
    },
)

SignalResourceInputRequestTypeDef = TypedDict(
    "SignalResourceInputRequestTypeDef",
    {
        "StackName": str,
        "LogicalResourceId": str,
        "UniqueId": str,
        "Status": ResourceSignalStatusType,
    },
)

StackDriftInformationResponseMetadataTypeDef = TypedDict(
    "StackDriftInformationResponseMetadataTypeDef",
    {
        "StackDriftStatus": StackDriftStatusType,
        "LastCheckTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StackDriftInformationSummaryTypeDef = TypedDict(
    "StackDriftInformationSummaryTypeDef",
    {
        "StackDriftStatus": StackDriftStatusType,
        "LastCheckTimestamp": NotRequired[datetime],
    },
)

StackDriftInformationTypeDef = TypedDict(
    "StackDriftInformationTypeDef",
    {
        "StackDriftStatus": StackDriftStatusType,
        "LastCheckTimestamp": NotRequired[datetime],
    },
)

StackEventTypeDef = TypedDict(
    "StackEventTypeDef",
    {
        "StackId": str,
        "EventId": str,
        "StackName": str,
        "Timestamp": datetime,
        "LogicalResourceId": NotRequired[str],
        "PhysicalResourceId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceStatus": NotRequired[ResourceStatusType],
        "ResourceStatusReason": NotRequired[str],
        "ResourceProperties": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "HookType": NotRequired[str],
        "HookStatus": NotRequired[HookStatusType],
        "HookStatusReason": NotRequired[str],
        "HookInvocationPoint": NotRequired[Literal["PRE_PROVISION"]],
        "HookFailureMode": NotRequired[HookFailureModeType],
    },
)

StackInstanceComprehensiveStatusTypeDef = TypedDict(
    "StackInstanceComprehensiveStatusTypeDef",
    {
        "DetailedStatus": NotRequired[StackInstanceDetailedStatusType],
    },
)

StackInstanceFilterTypeDef = TypedDict(
    "StackInstanceFilterTypeDef",
    {
        "Name": NotRequired[Literal["DETAILED_STATUS"]],
        "Values": NotRequired[str],
    },
)

StackInstanceSummaryTypeDef = TypedDict(
    "StackInstanceSummaryTypeDef",
    {
        "StackSetId": NotRequired[str],
        "Region": NotRequired[str],
        "Account": NotRequired[str],
        "StackId": NotRequired[str],
        "Status": NotRequired[StackInstanceStatusType],
        "StatusReason": NotRequired[str],
        "StackInstanceStatus": NotRequired["StackInstanceComprehensiveStatusTypeDef"],
        "OrganizationalUnitId": NotRequired[str],
        "DriftStatus": NotRequired[StackDriftStatusType],
        "LastDriftCheckTimestamp": NotRequired[datetime],
    },
)

StackInstanceTypeDef = TypedDict(
    "StackInstanceTypeDef",
    {
        "StackSetId": NotRequired[str],
        "Region": NotRequired[str],
        "Account": NotRequired[str],
        "StackId": NotRequired[str],
        "ParameterOverrides": NotRequired[List["ParameterTypeDef"]],
        "Status": NotRequired[StackInstanceStatusType],
        "StackInstanceStatus": NotRequired["StackInstanceComprehensiveStatusTypeDef"],
        "StatusReason": NotRequired[str],
        "OrganizationalUnitId": NotRequired[str],
        "DriftStatus": NotRequired[StackDriftStatusType],
        "LastDriftCheckTimestamp": NotRequired[datetime],
    },
)

StackResourceDetailTypeDef = TypedDict(
    "StackResourceDetailTypeDef",
    {
        "LogicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": ResourceStatusType,
        "StackName": NotRequired[str],
        "StackId": NotRequired[str],
        "PhysicalResourceId": NotRequired[str],
        "ResourceStatusReason": NotRequired[str],
        "Description": NotRequired[str],
        "Metadata": NotRequired[str],
        "DriftInformation": NotRequired["StackResourceDriftInformationTypeDef"],
        "ModuleInfo": NotRequired["ModuleInfoTypeDef"],
    },
)

StackResourceDriftInformationResponseMetadataTypeDef = TypedDict(
    "StackResourceDriftInformationResponseMetadataTypeDef",
    {
        "StackResourceDriftStatus": StackResourceDriftStatusType,
        "LastCheckTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StackResourceDriftInformationSummaryResponseMetadataTypeDef = TypedDict(
    "StackResourceDriftInformationSummaryResponseMetadataTypeDef",
    {
        "StackResourceDriftStatus": StackResourceDriftStatusType,
        "LastCheckTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StackResourceDriftInformationSummaryTypeDef = TypedDict(
    "StackResourceDriftInformationSummaryTypeDef",
    {
        "StackResourceDriftStatus": StackResourceDriftStatusType,
        "LastCheckTimestamp": NotRequired[datetime],
    },
)

StackResourceDriftInformationTypeDef = TypedDict(
    "StackResourceDriftInformationTypeDef",
    {
        "StackResourceDriftStatus": StackResourceDriftStatusType,
        "LastCheckTimestamp": NotRequired[datetime],
    },
)

StackResourceDriftTypeDef = TypedDict(
    "StackResourceDriftTypeDef",
    {
        "StackId": str,
        "LogicalResourceId": str,
        "ResourceType": str,
        "StackResourceDriftStatus": StackResourceDriftStatusType,
        "Timestamp": datetime,
        "PhysicalResourceId": NotRequired[str],
        "PhysicalResourceIdContext": NotRequired[
            List["PhysicalResourceIdContextKeyValuePairTypeDef"]
        ],
        "ExpectedProperties": NotRequired[str],
        "ActualProperties": NotRequired[str],
        "PropertyDifferences": NotRequired[List["PropertyDifferenceTypeDef"]],
        "ModuleInfo": NotRequired["ModuleInfoTypeDef"],
    },
)

StackResourceRequestTypeDef = TypedDict(
    "StackResourceRequestTypeDef",
    {
        "logical_id": str,
    },
)

StackResourceSummaryTypeDef = TypedDict(
    "StackResourceSummaryTypeDef",
    {
        "LogicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": ResourceStatusType,
        "PhysicalResourceId": NotRequired[str],
        "ResourceStatusReason": NotRequired[str],
        "DriftInformation": NotRequired["StackResourceDriftInformationSummaryTypeDef"],
        "ModuleInfo": NotRequired["ModuleInfoTypeDef"],
    },
)

StackResourceTypeDef = TypedDict(
    "StackResourceTypeDef",
    {
        "LogicalResourceId": str,
        "ResourceType": str,
        "Timestamp": datetime,
        "ResourceStatus": ResourceStatusType,
        "StackName": NotRequired[str],
        "StackId": NotRequired[str],
        "PhysicalResourceId": NotRequired[str],
        "ResourceStatusReason": NotRequired[str],
        "Description": NotRequired[str],
        "DriftInformation": NotRequired["StackResourceDriftInformationTypeDef"],
        "ModuleInfo": NotRequired["ModuleInfoTypeDef"],
    },
)

StackSetDriftDetectionDetailsTypeDef = TypedDict(
    "StackSetDriftDetectionDetailsTypeDef",
    {
        "DriftStatus": NotRequired[StackSetDriftStatusType],
        "DriftDetectionStatus": NotRequired[StackSetDriftDetectionStatusType],
        "LastDriftCheckTimestamp": NotRequired[datetime],
        "TotalStackInstancesCount": NotRequired[int],
        "DriftedStackInstancesCount": NotRequired[int],
        "InSyncStackInstancesCount": NotRequired[int],
        "InProgressStackInstancesCount": NotRequired[int],
        "FailedStackInstancesCount": NotRequired[int],
    },
)

StackSetOperationPreferencesTypeDef = TypedDict(
    "StackSetOperationPreferencesTypeDef",
    {
        "RegionConcurrencyType": NotRequired[RegionConcurrencyTypeType],
        "RegionOrder": NotRequired[Sequence[str]],
        "FailureToleranceCount": NotRequired[int],
        "FailureTolerancePercentage": NotRequired[int],
        "MaxConcurrentCount": NotRequired[int],
        "MaxConcurrentPercentage": NotRequired[int],
    },
)

StackSetOperationResultSummaryTypeDef = TypedDict(
    "StackSetOperationResultSummaryTypeDef",
    {
        "Account": NotRequired[str],
        "Region": NotRequired[str],
        "Status": NotRequired[StackSetOperationResultStatusType],
        "StatusReason": NotRequired[str],
        "AccountGateResult": NotRequired["AccountGateResultTypeDef"],
        "OrganizationalUnitId": NotRequired[str],
    },
)

StackSetOperationSummaryTypeDef = TypedDict(
    "StackSetOperationSummaryTypeDef",
    {
        "OperationId": NotRequired[str],
        "Action": NotRequired[StackSetOperationActionType],
        "Status": NotRequired[StackSetOperationStatusType],
        "CreationTimestamp": NotRequired[datetime],
        "EndTimestamp": NotRequired[datetime],
    },
)

StackSetOperationTypeDef = TypedDict(
    "StackSetOperationTypeDef",
    {
        "OperationId": NotRequired[str],
        "StackSetId": NotRequired[str],
        "Action": NotRequired[StackSetOperationActionType],
        "Status": NotRequired[StackSetOperationStatusType],
        "OperationPreferences": NotRequired["StackSetOperationPreferencesTypeDef"],
        "RetainStacks": NotRequired[bool],
        "AdministrationRoleARN": NotRequired[str],
        "ExecutionRoleName": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
        "EndTimestamp": NotRequired[datetime],
        "DeploymentTargets": NotRequired["DeploymentTargetsTypeDef"],
        "StackSetDriftDetectionDetails": NotRequired["StackSetDriftDetectionDetailsTypeDef"],
    },
)

StackSetSummaryTypeDef = TypedDict(
    "StackSetSummaryTypeDef",
    {
        "StackSetName": NotRequired[str],
        "StackSetId": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[StackSetStatusType],
        "AutoDeployment": NotRequired["AutoDeploymentTypeDef"],
        "PermissionModel": NotRequired[PermissionModelsType],
        "DriftStatus": NotRequired[StackDriftStatusType],
        "LastDriftCheckTimestamp": NotRequired[datetime],
        "ManagedExecution": NotRequired["ManagedExecutionTypeDef"],
    },
)

StackSetTypeDef = TypedDict(
    "StackSetTypeDef",
    {
        "StackSetName": NotRequired[str],
        "StackSetId": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[StackSetStatusType],
        "TemplateBody": NotRequired[str],
        "Parameters": NotRequired[List["ParameterTypeDef"]],
        "Capabilities": NotRequired[List[CapabilityType]],
        "Tags": NotRequired[List["TagTypeDef"]],
        "StackSetARN": NotRequired[str],
        "AdministrationRoleARN": NotRequired[str],
        "ExecutionRoleName": NotRequired[str],
        "StackSetDriftDetectionDetails": NotRequired["StackSetDriftDetectionDetailsTypeDef"],
        "AutoDeployment": NotRequired["AutoDeploymentTypeDef"],
        "PermissionModel": NotRequired[PermissionModelsType],
        "OrganizationalUnitIds": NotRequired[List[str]],
        "ManagedExecution": NotRequired["ManagedExecutionTypeDef"],
    },
)

StackSummaryTypeDef = TypedDict(
    "StackSummaryTypeDef",
    {
        "StackName": str,
        "CreationTime": datetime,
        "StackStatus": StackStatusType,
        "StackId": NotRequired[str],
        "TemplateDescription": NotRequired[str],
        "LastUpdatedTime": NotRequired[datetime],
        "DeletionTime": NotRequired[datetime],
        "StackStatusReason": NotRequired[str],
        "ParentId": NotRequired[str],
        "RootId": NotRequired[str],
        "DriftInformation": NotRequired["StackDriftInformationSummaryTypeDef"],
    },
)

StackTypeDef = TypedDict(
    "StackTypeDef",
    {
        "StackName": str,
        "CreationTime": datetime,
        "StackStatus": StackStatusType,
        "StackId": NotRequired[str],
        "ChangeSetId": NotRequired[str],
        "Description": NotRequired[str],
        "Parameters": NotRequired[List["ParameterTypeDef"]],
        "DeletionTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "RollbackConfiguration": NotRequired["RollbackConfigurationTypeDef"],
        "StackStatusReason": NotRequired[str],
        "DisableRollback": NotRequired[bool],
        "NotificationARNs": NotRequired[List[str]],
        "TimeoutInMinutes": NotRequired[int],
        "Capabilities": NotRequired[List[CapabilityType]],
        "Outputs": NotRequired[List["OutputTypeDef"]],
        "RoleARN": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "EnableTerminationProtection": NotRequired[bool],
        "ParentId": NotRequired[str],
        "RootId": NotRequired[str],
        "DriftInformation": NotRequired["StackDriftInformationTypeDef"],
    },
)

StopStackSetOperationInputRequestTypeDef = TypedDict(
    "StopStackSetOperationInputRequestTypeDef",
    {
        "StackSetName": str,
        "OperationId": str,
        "CallAs": NotRequired[CallAsType],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TemplateParameterTypeDef = TypedDict(
    "TemplateParameterTypeDef",
    {
        "ParameterKey": NotRequired[str],
        "DefaultValue": NotRequired[str],
        "NoEcho": NotRequired[bool],
        "Description": NotRequired[str],
    },
)

TestTypeInputRequestTypeDef = TypedDict(
    "TestTypeInputRequestTypeDef",
    {
        "Arn": NotRequired[str],
        "Type": NotRequired[ThirdPartyTypeType],
        "TypeName": NotRequired[str],
        "VersionId": NotRequired[str],
        "LogDeliveryBucket": NotRequired[str],
    },
)

TestTypeOutputTypeDef = TypedDict(
    "TestTypeOutputTypeDef",
    {
        "TypeVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TypeConfigurationDetailsTypeDef = TypedDict(
    "TypeConfigurationDetailsTypeDef",
    {
        "Arn": NotRequired[str],
        "Alias": NotRequired[str],
        "Configuration": NotRequired[str],
        "LastUpdated": NotRequired[datetime],
        "TypeArn": NotRequired[str],
        "TypeName": NotRequired[str],
        "IsDefaultConfiguration": NotRequired[bool],
    },
)

TypeConfigurationIdentifierTypeDef = TypedDict(
    "TypeConfigurationIdentifierTypeDef",
    {
        "TypeArn": NotRequired[str],
        "TypeConfigurationAlias": NotRequired[str],
        "TypeConfigurationArn": NotRequired[str],
        "Type": NotRequired[ThirdPartyTypeType],
        "TypeName": NotRequired[str],
    },
)

TypeFiltersTypeDef = TypedDict(
    "TypeFiltersTypeDef",
    {
        "Category": NotRequired[CategoryType],
        "PublisherId": NotRequired[str],
        "TypeNamePrefix": NotRequired[str],
    },
)

TypeSummaryTypeDef = TypedDict(
    "TypeSummaryTypeDef",
    {
        "Type": NotRequired[RegistryTypeType],
        "TypeName": NotRequired[str],
        "DefaultVersionId": NotRequired[str],
        "TypeArn": NotRequired[str],
        "LastUpdated": NotRequired[datetime],
        "Description": NotRequired[str],
        "PublisherId": NotRequired[str],
        "OriginalTypeName": NotRequired[str],
        "PublicVersionNumber": NotRequired[str],
        "LatestPublicVersion": NotRequired[str],
        "PublisherIdentity": NotRequired[IdentityProviderType],
        "PublisherName": NotRequired[str],
        "IsActivated": NotRequired[bool],
    },
)

TypeVersionSummaryTypeDef = TypedDict(
    "TypeVersionSummaryTypeDef",
    {
        "Type": NotRequired[RegistryTypeType],
        "TypeName": NotRequired[str],
        "VersionId": NotRequired[str],
        "IsDefaultVersion": NotRequired[bool],
        "Arn": NotRequired[str],
        "TimeCreated": NotRequired[datetime],
        "Description": NotRequired[str],
        "PublicVersionNumber": NotRequired[str],
    },
)

UpdateStackInputRequestTypeDef = TypedDict(
    "UpdateStackInputRequestTypeDef",
    {
        "StackName": str,
        "TemplateBody": NotRequired[str],
        "TemplateURL": NotRequired[str],
        "UsePreviousTemplate": NotRequired[bool],
        "StackPolicyDuringUpdateBody": NotRequired[str],
        "StackPolicyDuringUpdateURL": NotRequired[str],
        "Parameters": NotRequired[Sequence["ParameterTypeDef"]],
        "Capabilities": NotRequired[Sequence[CapabilityType]],
        "ResourceTypes": NotRequired[Sequence[str]],
        "RoleARN": NotRequired[str],
        "RollbackConfiguration": NotRequired["RollbackConfigurationTypeDef"],
        "StackPolicyBody": NotRequired[str],
        "StackPolicyURL": NotRequired[str],
        "NotificationARNs": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "DisableRollback": NotRequired[bool],
        "ClientRequestToken": NotRequired[str],
    },
)

UpdateStackInputStackUpdateTypeDef = TypedDict(
    "UpdateStackInputStackUpdateTypeDef",
    {
        "TemplateBody": NotRequired[str],
        "TemplateURL": NotRequired[str],
        "UsePreviousTemplate": NotRequired[bool],
        "StackPolicyDuringUpdateBody": NotRequired[str],
        "StackPolicyDuringUpdateURL": NotRequired[str],
        "Parameters": NotRequired[Sequence["ParameterTypeDef"]],
        "Capabilities": NotRequired[Sequence[CapabilityType]],
        "ResourceTypes": NotRequired[Sequence[str]],
        "RoleARN": NotRequired[str],
        "RollbackConfiguration": NotRequired["RollbackConfigurationTypeDef"],
        "StackPolicyBody": NotRequired[str],
        "StackPolicyURL": NotRequired[str],
        "NotificationARNs": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "DisableRollback": NotRequired[bool],
        "ClientRequestToken": NotRequired[str],
    },
)

UpdateStackInstancesInputRequestTypeDef = TypedDict(
    "UpdateStackInstancesInputRequestTypeDef",
    {
        "StackSetName": str,
        "Regions": Sequence[str],
        "Accounts": NotRequired[Sequence[str]],
        "DeploymentTargets": NotRequired["DeploymentTargetsTypeDef"],
        "ParameterOverrides": NotRequired[Sequence["ParameterTypeDef"]],
        "OperationPreferences": NotRequired["StackSetOperationPreferencesTypeDef"],
        "OperationId": NotRequired[str],
        "CallAs": NotRequired[CallAsType],
    },
)

UpdateStackInstancesOutputTypeDef = TypedDict(
    "UpdateStackInstancesOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateStackOutputTypeDef = TypedDict(
    "UpdateStackOutputTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateStackSetInputRequestTypeDef = TypedDict(
    "UpdateStackSetInputRequestTypeDef",
    {
        "StackSetName": str,
        "Description": NotRequired[str],
        "TemplateBody": NotRequired[str],
        "TemplateURL": NotRequired[str],
        "UsePreviousTemplate": NotRequired[bool],
        "Parameters": NotRequired[Sequence["ParameterTypeDef"]],
        "Capabilities": NotRequired[Sequence[CapabilityType]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "OperationPreferences": NotRequired["StackSetOperationPreferencesTypeDef"],
        "AdministrationRoleARN": NotRequired[str],
        "ExecutionRoleName": NotRequired[str],
        "DeploymentTargets": NotRequired["DeploymentTargetsTypeDef"],
        "PermissionModel": NotRequired[PermissionModelsType],
        "AutoDeployment": NotRequired["AutoDeploymentTypeDef"],
        "OperationId": NotRequired[str],
        "Accounts": NotRequired[Sequence[str]],
        "Regions": NotRequired[Sequence[str]],
        "CallAs": NotRequired[CallAsType],
        "ManagedExecution": NotRequired["ManagedExecutionTypeDef"],
    },
)

UpdateStackSetOutputTypeDef = TypedDict(
    "UpdateStackSetOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTerminationProtectionInputRequestTypeDef = TypedDict(
    "UpdateTerminationProtectionInputRequestTypeDef",
    {
        "EnableTerminationProtection": bool,
        "StackName": str,
    },
)

UpdateTerminationProtectionOutputTypeDef = TypedDict(
    "UpdateTerminationProtectionOutputTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidateTemplateInputRequestTypeDef = TypedDict(
    "ValidateTemplateInputRequestTypeDef",
    {
        "TemplateBody": NotRequired[str],
        "TemplateURL": NotRequired[str],
    },
)

ValidateTemplateOutputTypeDef = TypedDict(
    "ValidateTemplateOutputTypeDef",
    {
        "Parameters": List["TemplateParameterTypeDef"],
        "Description": str,
        "Capabilities": List[CapabilityType],
        "CapabilitiesReason": str,
        "DeclaredTransforms": List[str],
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
