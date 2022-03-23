"""
Type annotations for ssm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ssm.type_defs import AccountSharingInfoTypeDef

    data: AccountSharingInfoTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AssociationComplianceSeverityType,
    AssociationExecutionFilterKeyType,
    AssociationExecutionTargetsFilterKeyType,
    AssociationFilterKeyType,
    AssociationFilterOperatorTypeType,
    AssociationStatusNameType,
    AssociationSyncComplianceType,
    AttachmentsSourceKeyType,
    AutomationExecutionFilterKeyType,
    AutomationExecutionStatusType,
    AutomationTypeType,
    CalendarStateType,
    CommandFilterKeyType,
    CommandInvocationStatusType,
    CommandPluginStatusType,
    CommandStatusType,
    ComplianceQueryOperatorTypeType,
    ComplianceSeverityType,
    ComplianceStatusType,
    ComplianceUploadTypeType,
    ConnectionStatusType,
    DescribeActivationsFilterKeysType,
    DocumentFilterKeyType,
    DocumentFormatType,
    DocumentHashTypeType,
    DocumentParameterTypeType,
    DocumentReviewActionType,
    DocumentStatusType,
    DocumentTypeType,
    ExecutionModeType,
    FaultType,
    InstanceInformationFilterKeyType,
    InstancePatchStateOperatorTypeType,
    InventoryAttributeDataTypeType,
    InventoryDeletionStatusType,
    InventoryQueryOperatorTypeType,
    InventorySchemaDeleteOptionType,
    LastResourceDataSyncStatusType,
    MaintenanceWindowExecutionStatusType,
    MaintenanceWindowResourceTypeType,
    MaintenanceWindowTaskCutoffBehaviorType,
    MaintenanceWindowTaskTypeType,
    NotificationEventType,
    NotificationTypeType,
    OperatingSystemType,
    OpsFilterOperatorTypeType,
    OpsItemDataTypeType,
    OpsItemFilterKeyType,
    OpsItemFilterOperatorType,
    OpsItemRelatedItemsFilterKeyType,
    OpsItemStatusType,
    ParametersFilterKeyType,
    ParameterTierType,
    ParameterTypeType,
    PatchActionType,
    PatchComplianceDataStateType,
    PatchComplianceLevelType,
    PatchDeploymentStatusType,
    PatchFilterKeyType,
    PatchOperationTypeType,
    PatchPropertyType,
    PatchSetType,
    PingStatusType,
    PlatformTypeType,
    RebootOptionType,
    ResourceTypeForTaggingType,
    ResourceTypeType,
    ReviewStatusType,
    SessionFilterKeyType,
    SessionStateType,
    SessionStatusType,
    SignalTypeType,
    SourceTypeType,
    StepExecutionFilterKeyType,
    StopTypeType,
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
    "AccountSharingInfoTypeDef",
    "ActivationTypeDef",
    "AddTagsToResourceRequestRequestTypeDef",
    "AssociateOpsItemRelatedItemRequestRequestTypeDef",
    "AssociateOpsItemRelatedItemResponseTypeDef",
    "AssociationDescriptionTypeDef",
    "AssociationExecutionFilterTypeDef",
    "AssociationExecutionTargetTypeDef",
    "AssociationExecutionTargetsFilterTypeDef",
    "AssociationExecutionTypeDef",
    "AssociationFilterTypeDef",
    "AssociationOverviewTypeDef",
    "AssociationStatusTypeDef",
    "AssociationTypeDef",
    "AssociationVersionInfoTypeDef",
    "AttachmentContentTypeDef",
    "AttachmentInformationTypeDef",
    "AttachmentsSourceTypeDef",
    "AutomationExecutionFilterTypeDef",
    "AutomationExecutionMetadataTypeDef",
    "AutomationExecutionTypeDef",
    "BaselineOverrideTypeDef",
    "CancelCommandRequestRequestTypeDef",
    "CancelMaintenanceWindowExecutionRequestRequestTypeDef",
    "CancelMaintenanceWindowExecutionResultTypeDef",
    "CloudWatchOutputConfigTypeDef",
    "CommandFilterTypeDef",
    "CommandInvocationTypeDef",
    "CommandPluginTypeDef",
    "CommandTypeDef",
    "ComplianceExecutionSummaryTypeDef",
    "ComplianceItemEntryTypeDef",
    "ComplianceItemTypeDef",
    "ComplianceStringFilterTypeDef",
    "ComplianceSummaryItemTypeDef",
    "CompliantSummaryTypeDef",
    "CreateActivationRequestRequestTypeDef",
    "CreateActivationResultTypeDef",
    "CreateAssociationBatchRequestEntryTypeDef",
    "CreateAssociationBatchRequestRequestTypeDef",
    "CreateAssociationBatchResultTypeDef",
    "CreateAssociationRequestRequestTypeDef",
    "CreateAssociationResultTypeDef",
    "CreateDocumentRequestRequestTypeDef",
    "CreateDocumentResultTypeDef",
    "CreateMaintenanceWindowRequestRequestTypeDef",
    "CreateMaintenanceWindowResultTypeDef",
    "CreateOpsItemRequestRequestTypeDef",
    "CreateOpsItemResponseTypeDef",
    "CreateOpsMetadataRequestRequestTypeDef",
    "CreateOpsMetadataResultTypeDef",
    "CreatePatchBaselineRequestRequestTypeDef",
    "CreatePatchBaselineResultTypeDef",
    "CreateResourceDataSyncRequestRequestTypeDef",
    "DeleteActivationRequestRequestTypeDef",
    "DeleteAssociationRequestRequestTypeDef",
    "DeleteDocumentRequestRequestTypeDef",
    "DeleteInventoryRequestRequestTypeDef",
    "DeleteInventoryResultTypeDef",
    "DeleteMaintenanceWindowRequestRequestTypeDef",
    "DeleteMaintenanceWindowResultTypeDef",
    "DeleteOpsMetadataRequestRequestTypeDef",
    "DeleteParameterRequestRequestTypeDef",
    "DeleteParametersRequestRequestTypeDef",
    "DeleteParametersResultTypeDef",
    "DeletePatchBaselineRequestRequestTypeDef",
    "DeletePatchBaselineResultTypeDef",
    "DeleteResourceDataSyncRequestRequestTypeDef",
    "DeregisterManagedInstanceRequestRequestTypeDef",
    "DeregisterPatchBaselineForPatchGroupRequestRequestTypeDef",
    "DeregisterPatchBaselineForPatchGroupResultTypeDef",
    "DeregisterTargetFromMaintenanceWindowRequestRequestTypeDef",
    "DeregisterTargetFromMaintenanceWindowResultTypeDef",
    "DeregisterTaskFromMaintenanceWindowRequestRequestTypeDef",
    "DeregisterTaskFromMaintenanceWindowResultTypeDef",
    "DescribeActivationsFilterTypeDef",
    "DescribeActivationsRequestRequestTypeDef",
    "DescribeActivationsResultTypeDef",
    "DescribeAssociationExecutionTargetsRequestRequestTypeDef",
    "DescribeAssociationExecutionTargetsResultTypeDef",
    "DescribeAssociationExecutionsRequestRequestTypeDef",
    "DescribeAssociationExecutionsResultTypeDef",
    "DescribeAssociationRequestRequestTypeDef",
    "DescribeAssociationResultTypeDef",
    "DescribeAutomationExecutionsRequestRequestTypeDef",
    "DescribeAutomationExecutionsResultTypeDef",
    "DescribeAutomationStepExecutionsRequestRequestTypeDef",
    "DescribeAutomationStepExecutionsResultTypeDef",
    "DescribeAvailablePatchesRequestRequestTypeDef",
    "DescribeAvailablePatchesResultTypeDef",
    "DescribeDocumentPermissionRequestRequestTypeDef",
    "DescribeDocumentPermissionResponseTypeDef",
    "DescribeDocumentRequestRequestTypeDef",
    "DescribeDocumentResultTypeDef",
    "DescribeEffectiveInstanceAssociationsRequestRequestTypeDef",
    "DescribeEffectiveInstanceAssociationsResultTypeDef",
    "DescribeEffectivePatchesForPatchBaselineRequestRequestTypeDef",
    "DescribeEffectivePatchesForPatchBaselineResultTypeDef",
    "DescribeInstanceAssociationsStatusRequestRequestTypeDef",
    "DescribeInstanceAssociationsStatusResultTypeDef",
    "DescribeInstanceInformationRequestRequestTypeDef",
    "DescribeInstanceInformationResultTypeDef",
    "DescribeInstancePatchStatesForPatchGroupRequestRequestTypeDef",
    "DescribeInstancePatchStatesForPatchGroupResultTypeDef",
    "DescribeInstancePatchStatesRequestRequestTypeDef",
    "DescribeInstancePatchStatesResultTypeDef",
    "DescribeInstancePatchesRequestRequestTypeDef",
    "DescribeInstancePatchesResultTypeDef",
    "DescribeInventoryDeletionsRequestRequestTypeDef",
    "DescribeInventoryDeletionsResultTypeDef",
    "DescribeMaintenanceWindowExecutionTaskInvocationsRequestRequestTypeDef",
    "DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef",
    "DescribeMaintenanceWindowExecutionTasksRequestRequestTypeDef",
    "DescribeMaintenanceWindowExecutionTasksResultTypeDef",
    "DescribeMaintenanceWindowExecutionsRequestRequestTypeDef",
    "DescribeMaintenanceWindowExecutionsResultTypeDef",
    "DescribeMaintenanceWindowScheduleRequestRequestTypeDef",
    "DescribeMaintenanceWindowScheduleResultTypeDef",
    "DescribeMaintenanceWindowTargetsRequestRequestTypeDef",
    "DescribeMaintenanceWindowTargetsResultTypeDef",
    "DescribeMaintenanceWindowTasksRequestRequestTypeDef",
    "DescribeMaintenanceWindowTasksResultTypeDef",
    "DescribeMaintenanceWindowsForTargetRequestRequestTypeDef",
    "DescribeMaintenanceWindowsForTargetResultTypeDef",
    "DescribeMaintenanceWindowsRequestRequestTypeDef",
    "DescribeMaintenanceWindowsResultTypeDef",
    "DescribeOpsItemsRequestRequestTypeDef",
    "DescribeOpsItemsResponseTypeDef",
    "DescribeParametersRequestRequestTypeDef",
    "DescribeParametersResultTypeDef",
    "DescribePatchBaselinesRequestRequestTypeDef",
    "DescribePatchBaselinesResultTypeDef",
    "DescribePatchGroupStateRequestRequestTypeDef",
    "DescribePatchGroupStateResultTypeDef",
    "DescribePatchGroupsRequestRequestTypeDef",
    "DescribePatchGroupsResultTypeDef",
    "DescribePatchPropertiesRequestRequestTypeDef",
    "DescribePatchPropertiesResultTypeDef",
    "DescribeSessionsRequestRequestTypeDef",
    "DescribeSessionsResponseTypeDef",
    "DisassociateOpsItemRelatedItemRequestRequestTypeDef",
    "DocumentDefaultVersionDescriptionTypeDef",
    "DocumentDescriptionTypeDef",
    "DocumentFilterTypeDef",
    "DocumentIdentifierTypeDef",
    "DocumentKeyValuesFilterTypeDef",
    "DocumentMetadataResponseInfoTypeDef",
    "DocumentParameterTypeDef",
    "DocumentRequiresTypeDef",
    "DocumentReviewCommentSourceTypeDef",
    "DocumentReviewerResponseSourceTypeDef",
    "DocumentReviewsTypeDef",
    "DocumentVersionInfoTypeDef",
    "EffectivePatchTypeDef",
    "FailedCreateAssociationTypeDef",
    "FailureDetailsTypeDef",
    "GetAutomationExecutionRequestRequestTypeDef",
    "GetAutomationExecutionResultTypeDef",
    "GetCalendarStateRequestRequestTypeDef",
    "GetCalendarStateResponseTypeDef",
    "GetCommandInvocationRequestRequestTypeDef",
    "GetCommandInvocationResultTypeDef",
    "GetConnectionStatusRequestRequestTypeDef",
    "GetConnectionStatusResponseTypeDef",
    "GetDefaultPatchBaselineRequestRequestTypeDef",
    "GetDefaultPatchBaselineResultTypeDef",
    "GetDeployablePatchSnapshotForInstanceRequestRequestTypeDef",
    "GetDeployablePatchSnapshotForInstanceResultTypeDef",
    "GetDocumentRequestRequestTypeDef",
    "GetDocumentResultTypeDef",
    "GetInventoryRequestRequestTypeDef",
    "GetInventoryResultTypeDef",
    "GetInventorySchemaRequestRequestTypeDef",
    "GetInventorySchemaResultTypeDef",
    "GetMaintenanceWindowExecutionRequestRequestTypeDef",
    "GetMaintenanceWindowExecutionResultTypeDef",
    "GetMaintenanceWindowExecutionTaskInvocationRequestRequestTypeDef",
    "GetMaintenanceWindowExecutionTaskInvocationResultTypeDef",
    "GetMaintenanceWindowExecutionTaskRequestRequestTypeDef",
    "GetMaintenanceWindowExecutionTaskResultTypeDef",
    "GetMaintenanceWindowRequestRequestTypeDef",
    "GetMaintenanceWindowResultTypeDef",
    "GetMaintenanceWindowTaskRequestRequestTypeDef",
    "GetMaintenanceWindowTaskResultTypeDef",
    "GetOpsItemRequestRequestTypeDef",
    "GetOpsItemResponseTypeDef",
    "GetOpsMetadataRequestRequestTypeDef",
    "GetOpsMetadataResultTypeDef",
    "GetOpsSummaryRequestRequestTypeDef",
    "GetOpsSummaryResultTypeDef",
    "GetParameterHistoryRequestRequestTypeDef",
    "GetParameterHistoryResultTypeDef",
    "GetParameterRequestRequestTypeDef",
    "GetParameterResultTypeDef",
    "GetParametersByPathRequestRequestTypeDef",
    "GetParametersByPathResultTypeDef",
    "GetParametersRequestRequestTypeDef",
    "GetParametersResultTypeDef",
    "GetPatchBaselineForPatchGroupRequestRequestTypeDef",
    "GetPatchBaselineForPatchGroupResultTypeDef",
    "GetPatchBaselineRequestRequestTypeDef",
    "GetPatchBaselineResultTypeDef",
    "GetServiceSettingRequestRequestTypeDef",
    "GetServiceSettingResultTypeDef",
    "InstanceAggregatedAssociationOverviewTypeDef",
    "InstanceAssociationOutputLocationTypeDef",
    "InstanceAssociationOutputUrlTypeDef",
    "InstanceAssociationStatusInfoTypeDef",
    "InstanceAssociationTypeDef",
    "InstanceInformationFilterTypeDef",
    "InstanceInformationStringFilterTypeDef",
    "InstanceInformationTypeDef",
    "InstancePatchStateFilterTypeDef",
    "InstancePatchStateTypeDef",
    "InventoryAggregatorTypeDef",
    "InventoryDeletionStatusItemTypeDef",
    "InventoryDeletionSummaryItemTypeDef",
    "InventoryDeletionSummaryTypeDef",
    "InventoryFilterTypeDef",
    "InventoryGroupTypeDef",
    "InventoryItemAttributeTypeDef",
    "InventoryItemSchemaTypeDef",
    "InventoryItemTypeDef",
    "InventoryResultEntityTypeDef",
    "InventoryResultItemTypeDef",
    "LabelParameterVersionRequestRequestTypeDef",
    "LabelParameterVersionResultTypeDef",
    "ListAssociationVersionsRequestRequestTypeDef",
    "ListAssociationVersionsResultTypeDef",
    "ListAssociationsRequestRequestTypeDef",
    "ListAssociationsResultTypeDef",
    "ListCommandInvocationsRequestRequestTypeDef",
    "ListCommandInvocationsResultTypeDef",
    "ListCommandsRequestRequestTypeDef",
    "ListCommandsResultTypeDef",
    "ListComplianceItemsRequestRequestTypeDef",
    "ListComplianceItemsResultTypeDef",
    "ListComplianceSummariesRequestRequestTypeDef",
    "ListComplianceSummariesResultTypeDef",
    "ListDocumentMetadataHistoryRequestRequestTypeDef",
    "ListDocumentMetadataHistoryResponseTypeDef",
    "ListDocumentVersionsRequestRequestTypeDef",
    "ListDocumentVersionsResultTypeDef",
    "ListDocumentsRequestRequestTypeDef",
    "ListDocumentsResultTypeDef",
    "ListInventoryEntriesRequestRequestTypeDef",
    "ListInventoryEntriesResultTypeDef",
    "ListOpsItemEventsRequestRequestTypeDef",
    "ListOpsItemEventsResponseTypeDef",
    "ListOpsItemRelatedItemsRequestRequestTypeDef",
    "ListOpsItemRelatedItemsResponseTypeDef",
    "ListOpsMetadataRequestRequestTypeDef",
    "ListOpsMetadataResultTypeDef",
    "ListResourceComplianceSummariesRequestRequestTypeDef",
    "ListResourceComplianceSummariesResultTypeDef",
    "ListResourceDataSyncRequestRequestTypeDef",
    "ListResourceDataSyncResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "LoggingInfoTypeDef",
    "MaintenanceWindowAutomationParametersTypeDef",
    "MaintenanceWindowExecutionTaskIdentityTypeDef",
    "MaintenanceWindowExecutionTaskInvocationIdentityTypeDef",
    "MaintenanceWindowExecutionTypeDef",
    "MaintenanceWindowFilterTypeDef",
    "MaintenanceWindowIdentityForTargetTypeDef",
    "MaintenanceWindowIdentityTypeDef",
    "MaintenanceWindowLambdaParametersTypeDef",
    "MaintenanceWindowRunCommandParametersTypeDef",
    "MaintenanceWindowStepFunctionsParametersTypeDef",
    "MaintenanceWindowTargetTypeDef",
    "MaintenanceWindowTaskInvocationParametersTypeDef",
    "MaintenanceWindowTaskParameterValueExpressionTypeDef",
    "MaintenanceWindowTaskTypeDef",
    "MetadataValueTypeDef",
    "ModifyDocumentPermissionRequestRequestTypeDef",
    "NonCompliantSummaryTypeDef",
    "NotificationConfigTypeDef",
    "OpsAggregatorTypeDef",
    "OpsEntityItemTypeDef",
    "OpsEntityTypeDef",
    "OpsFilterTypeDef",
    "OpsItemDataValueTypeDef",
    "OpsItemEventFilterTypeDef",
    "OpsItemEventSummaryTypeDef",
    "OpsItemFilterTypeDef",
    "OpsItemIdentityTypeDef",
    "OpsItemNotificationTypeDef",
    "OpsItemRelatedItemSummaryTypeDef",
    "OpsItemRelatedItemsFilterTypeDef",
    "OpsItemSummaryTypeDef",
    "OpsItemTypeDef",
    "OpsMetadataFilterTypeDef",
    "OpsMetadataTypeDef",
    "OpsResultAttributeTypeDef",
    "OutputSourceTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterHistoryTypeDef",
    "ParameterInlinePolicyTypeDef",
    "ParameterMetadataTypeDef",
    "ParameterStringFilterTypeDef",
    "ParameterTypeDef",
    "ParametersFilterTypeDef",
    "PatchBaselineIdentityTypeDef",
    "PatchComplianceDataTypeDef",
    "PatchFilterGroupTypeDef",
    "PatchFilterTypeDef",
    "PatchGroupPatchBaselineMappingTypeDef",
    "PatchOrchestratorFilterTypeDef",
    "PatchRuleGroupTypeDef",
    "PatchRuleTypeDef",
    "PatchSourceTypeDef",
    "PatchStatusTypeDef",
    "PatchTypeDef",
    "ProgressCountersTypeDef",
    "PutComplianceItemsRequestRequestTypeDef",
    "PutInventoryRequestRequestTypeDef",
    "PutInventoryResultTypeDef",
    "PutParameterRequestRequestTypeDef",
    "PutParameterResultTypeDef",
    "RegisterDefaultPatchBaselineRequestRequestTypeDef",
    "RegisterDefaultPatchBaselineResultTypeDef",
    "RegisterPatchBaselineForPatchGroupRequestRequestTypeDef",
    "RegisterPatchBaselineForPatchGroupResultTypeDef",
    "RegisterTargetWithMaintenanceWindowRequestRequestTypeDef",
    "RegisterTargetWithMaintenanceWindowResultTypeDef",
    "RegisterTaskWithMaintenanceWindowRequestRequestTypeDef",
    "RegisterTaskWithMaintenanceWindowResultTypeDef",
    "RegistrationMetadataItemTypeDef",
    "RelatedOpsItemTypeDef",
    "RemoveTagsFromResourceRequestRequestTypeDef",
    "ResetServiceSettingRequestRequestTypeDef",
    "ResetServiceSettingResultTypeDef",
    "ResolvedTargetsTypeDef",
    "ResourceComplianceSummaryItemTypeDef",
    "ResourceDataSyncAwsOrganizationsSourceTypeDef",
    "ResourceDataSyncDestinationDataSharingTypeDef",
    "ResourceDataSyncItemTypeDef",
    "ResourceDataSyncOrganizationalUnitTypeDef",
    "ResourceDataSyncS3DestinationTypeDef",
    "ResourceDataSyncSourceTypeDef",
    "ResourceDataSyncSourceWithStateTypeDef",
    "ResponseMetadataTypeDef",
    "ResultAttributeTypeDef",
    "ResumeSessionRequestRequestTypeDef",
    "ResumeSessionResponseTypeDef",
    "ReviewInformationTypeDef",
    "RunbookTypeDef",
    "S3OutputLocationTypeDef",
    "S3OutputUrlTypeDef",
    "ScheduledWindowExecutionTypeDef",
    "SendAutomationSignalRequestRequestTypeDef",
    "SendCommandRequestRequestTypeDef",
    "SendCommandResultTypeDef",
    "ServiceSettingTypeDef",
    "SessionFilterTypeDef",
    "SessionManagerOutputUrlTypeDef",
    "SessionTypeDef",
    "SeveritySummaryTypeDef",
    "StartAssociationsOnceRequestRequestTypeDef",
    "StartAutomationExecutionRequestRequestTypeDef",
    "StartAutomationExecutionResultTypeDef",
    "StartChangeRequestExecutionRequestRequestTypeDef",
    "StartChangeRequestExecutionResultTypeDef",
    "StartSessionRequestRequestTypeDef",
    "StartSessionResponseTypeDef",
    "StepExecutionFilterTypeDef",
    "StepExecutionTypeDef",
    "StopAutomationExecutionRequestRequestTypeDef",
    "TagTypeDef",
    "TargetLocationTypeDef",
    "TargetTypeDef",
    "TerminateSessionRequestRequestTypeDef",
    "TerminateSessionResponseTypeDef",
    "UnlabelParameterVersionRequestRequestTypeDef",
    "UnlabelParameterVersionResultTypeDef",
    "UpdateAssociationRequestRequestTypeDef",
    "UpdateAssociationResultTypeDef",
    "UpdateAssociationStatusRequestRequestTypeDef",
    "UpdateAssociationStatusResultTypeDef",
    "UpdateDocumentDefaultVersionRequestRequestTypeDef",
    "UpdateDocumentDefaultVersionResultTypeDef",
    "UpdateDocumentMetadataRequestRequestTypeDef",
    "UpdateDocumentRequestRequestTypeDef",
    "UpdateDocumentResultTypeDef",
    "UpdateMaintenanceWindowRequestRequestTypeDef",
    "UpdateMaintenanceWindowResultTypeDef",
    "UpdateMaintenanceWindowTargetRequestRequestTypeDef",
    "UpdateMaintenanceWindowTargetResultTypeDef",
    "UpdateMaintenanceWindowTaskRequestRequestTypeDef",
    "UpdateMaintenanceWindowTaskResultTypeDef",
    "UpdateManagedInstanceRoleRequestRequestTypeDef",
    "UpdateOpsItemRequestRequestTypeDef",
    "UpdateOpsMetadataRequestRequestTypeDef",
    "UpdateOpsMetadataResultTypeDef",
    "UpdatePatchBaselineRequestRequestTypeDef",
    "UpdatePatchBaselineResultTypeDef",
    "UpdateResourceDataSyncRequestRequestTypeDef",
    "UpdateServiceSettingRequestRequestTypeDef",
    "WaiterConfigTypeDef",
)

AccountSharingInfoTypeDef = TypedDict(
    "AccountSharingInfoTypeDef",
    {
        "AccountId": NotRequired[str],
        "SharedDocumentVersion": NotRequired[str],
    },
)

ActivationTypeDef = TypedDict(
    "ActivationTypeDef",
    {
        "ActivationId": NotRequired[str],
        "Description": NotRequired[str],
        "DefaultInstanceName": NotRequired[str],
        "IamRole": NotRequired[str],
        "RegistrationLimit": NotRequired[int],
        "RegistrationsCount": NotRequired[int],
        "ExpirationDate": NotRequired[datetime],
        "Expired": NotRequired[bool],
        "CreatedDate": NotRequired[datetime],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

AddTagsToResourceRequestRequestTypeDef = TypedDict(
    "AddTagsToResourceRequestRequestTypeDef",
    {
        "ResourceType": ResourceTypeForTaggingType,
        "ResourceId": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

AssociateOpsItemRelatedItemRequestRequestTypeDef = TypedDict(
    "AssociateOpsItemRelatedItemRequestRequestTypeDef",
    {
        "OpsItemId": str,
        "AssociationType": str,
        "ResourceType": str,
        "ResourceUri": str,
    },
)

AssociateOpsItemRelatedItemResponseTypeDef = TypedDict(
    "AssociateOpsItemRelatedItemResponseTypeDef",
    {
        "AssociationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociationDescriptionTypeDef = TypedDict(
    "AssociationDescriptionTypeDef",
    {
        "Name": NotRequired[str],
        "InstanceId": NotRequired[str],
        "AssociationVersion": NotRequired[str],
        "Date": NotRequired[datetime],
        "LastUpdateAssociationDate": NotRequired[datetime],
        "Status": NotRequired["AssociationStatusTypeDef"],
        "Overview": NotRequired["AssociationOverviewTypeDef"],
        "DocumentVersion": NotRequired[str],
        "AutomationTargetParameterName": NotRequired[str],
        "Parameters": NotRequired[Dict[str, List[str]]],
        "AssociationId": NotRequired[str],
        "Targets": NotRequired[List["TargetTypeDef"]],
        "ScheduleExpression": NotRequired[str],
        "OutputLocation": NotRequired["InstanceAssociationOutputLocationTypeDef"],
        "LastExecutionDate": NotRequired[datetime],
        "LastSuccessfulExecutionDate": NotRequired[datetime],
        "AssociationName": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "MaxConcurrency": NotRequired[str],
        "ComplianceSeverity": NotRequired[AssociationComplianceSeverityType],
        "SyncCompliance": NotRequired[AssociationSyncComplianceType],
        "ApplyOnlyAtCronInterval": NotRequired[bool],
        "CalendarNames": NotRequired[List[str]],
        "TargetLocations": NotRequired[List["TargetLocationTypeDef"]],
    },
)

AssociationExecutionFilterTypeDef = TypedDict(
    "AssociationExecutionFilterTypeDef",
    {
        "Key": AssociationExecutionFilterKeyType,
        "Value": str,
        "Type": AssociationFilterOperatorTypeType,
    },
)

AssociationExecutionTargetTypeDef = TypedDict(
    "AssociationExecutionTargetTypeDef",
    {
        "AssociationId": NotRequired[str],
        "AssociationVersion": NotRequired[str],
        "ExecutionId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "Status": NotRequired[str],
        "DetailedStatus": NotRequired[str],
        "LastExecutionDate": NotRequired[datetime],
        "OutputSource": NotRequired["OutputSourceTypeDef"],
    },
)

AssociationExecutionTargetsFilterTypeDef = TypedDict(
    "AssociationExecutionTargetsFilterTypeDef",
    {
        "Key": AssociationExecutionTargetsFilterKeyType,
        "Value": str,
    },
)

AssociationExecutionTypeDef = TypedDict(
    "AssociationExecutionTypeDef",
    {
        "AssociationId": NotRequired[str],
        "AssociationVersion": NotRequired[str],
        "ExecutionId": NotRequired[str],
        "Status": NotRequired[str],
        "DetailedStatus": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LastExecutionDate": NotRequired[datetime],
        "ResourceCountByStatus": NotRequired[str],
    },
)

AssociationFilterTypeDef = TypedDict(
    "AssociationFilterTypeDef",
    {
        "key": AssociationFilterKeyType,
        "value": str,
    },
)

AssociationOverviewTypeDef = TypedDict(
    "AssociationOverviewTypeDef",
    {
        "Status": NotRequired[str],
        "DetailedStatus": NotRequired[str],
        "AssociationStatusAggregatedCount": NotRequired[Dict[str, int]],
    },
)

AssociationStatusTypeDef = TypedDict(
    "AssociationStatusTypeDef",
    {
        "Date": datetime,
        "Name": AssociationStatusNameType,
        "Message": str,
        "AdditionalInfo": NotRequired[str],
    },
)

AssociationTypeDef = TypedDict(
    "AssociationTypeDef",
    {
        "Name": NotRequired[str],
        "InstanceId": NotRequired[str],
        "AssociationId": NotRequired[str],
        "AssociationVersion": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "Targets": NotRequired[List["TargetTypeDef"]],
        "LastExecutionDate": NotRequired[datetime],
        "Overview": NotRequired["AssociationOverviewTypeDef"],
        "ScheduleExpression": NotRequired[str],
        "AssociationName": NotRequired[str],
    },
)

AssociationVersionInfoTypeDef = TypedDict(
    "AssociationVersionInfoTypeDef",
    {
        "AssociationId": NotRequired[str],
        "AssociationVersion": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "Name": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "Parameters": NotRequired[Dict[str, List[str]]],
        "Targets": NotRequired[List["TargetTypeDef"]],
        "ScheduleExpression": NotRequired[str],
        "OutputLocation": NotRequired["InstanceAssociationOutputLocationTypeDef"],
        "AssociationName": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "MaxConcurrency": NotRequired[str],
        "ComplianceSeverity": NotRequired[AssociationComplianceSeverityType],
        "SyncCompliance": NotRequired[AssociationSyncComplianceType],
        "ApplyOnlyAtCronInterval": NotRequired[bool],
        "CalendarNames": NotRequired[List[str]],
        "TargetLocations": NotRequired[List["TargetLocationTypeDef"]],
    },
)

AttachmentContentTypeDef = TypedDict(
    "AttachmentContentTypeDef",
    {
        "Name": NotRequired[str],
        "Size": NotRequired[int],
        "Hash": NotRequired[str],
        "HashType": NotRequired[Literal["Sha256"]],
        "Url": NotRequired[str],
    },
)

AttachmentInformationTypeDef = TypedDict(
    "AttachmentInformationTypeDef",
    {
        "Name": NotRequired[str],
    },
)

AttachmentsSourceTypeDef = TypedDict(
    "AttachmentsSourceTypeDef",
    {
        "Key": NotRequired[AttachmentsSourceKeyType],
        "Values": NotRequired[Sequence[str]],
        "Name": NotRequired[str],
    },
)

AutomationExecutionFilterTypeDef = TypedDict(
    "AutomationExecutionFilterTypeDef",
    {
        "Key": AutomationExecutionFilterKeyType,
        "Values": Sequence[str],
    },
)

AutomationExecutionMetadataTypeDef = TypedDict(
    "AutomationExecutionMetadataTypeDef",
    {
        "AutomationExecutionId": NotRequired[str],
        "DocumentName": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "AutomationExecutionStatus": NotRequired[AutomationExecutionStatusType],
        "ExecutionStartTime": NotRequired[datetime],
        "ExecutionEndTime": NotRequired[datetime],
        "ExecutedBy": NotRequired[str],
        "LogFile": NotRequired[str],
        "Outputs": NotRequired[Dict[str, List[str]]],
        "Mode": NotRequired[ExecutionModeType],
        "ParentAutomationExecutionId": NotRequired[str],
        "CurrentStepName": NotRequired[str],
        "CurrentAction": NotRequired[str],
        "FailureMessage": NotRequired[str],
        "TargetParameterName": NotRequired[str],
        "Targets": NotRequired[List["TargetTypeDef"]],
        "TargetMaps": NotRequired[List[Dict[str, List[str]]]],
        "ResolvedTargets": NotRequired["ResolvedTargetsTypeDef"],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "Target": NotRequired[str],
        "AutomationType": NotRequired[AutomationTypeType],
        "AutomationSubtype": NotRequired[Literal["ChangeRequest"]],
        "ScheduledTime": NotRequired[datetime],
        "Runbooks": NotRequired[List["RunbookTypeDef"]],
        "OpsItemId": NotRequired[str],
        "AssociationId": NotRequired[str],
        "ChangeRequestName": NotRequired[str],
    },
)

AutomationExecutionTypeDef = TypedDict(
    "AutomationExecutionTypeDef",
    {
        "AutomationExecutionId": NotRequired[str],
        "DocumentName": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "ExecutionStartTime": NotRequired[datetime],
        "ExecutionEndTime": NotRequired[datetime],
        "AutomationExecutionStatus": NotRequired[AutomationExecutionStatusType],
        "StepExecutions": NotRequired[List["StepExecutionTypeDef"]],
        "StepExecutionsTruncated": NotRequired[bool],
        "Parameters": NotRequired[Dict[str, List[str]]],
        "Outputs": NotRequired[Dict[str, List[str]]],
        "FailureMessage": NotRequired[str],
        "Mode": NotRequired[ExecutionModeType],
        "ParentAutomationExecutionId": NotRequired[str],
        "ExecutedBy": NotRequired[str],
        "CurrentStepName": NotRequired[str],
        "CurrentAction": NotRequired[str],
        "TargetParameterName": NotRequired[str],
        "Targets": NotRequired[List["TargetTypeDef"]],
        "TargetMaps": NotRequired[List[Dict[str, List[str]]]],
        "ResolvedTargets": NotRequired["ResolvedTargetsTypeDef"],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "Target": NotRequired[str],
        "TargetLocations": NotRequired[List["TargetLocationTypeDef"]],
        "ProgressCounters": NotRequired["ProgressCountersTypeDef"],
        "AutomationSubtype": NotRequired[Literal["ChangeRequest"]],
        "ScheduledTime": NotRequired[datetime],
        "Runbooks": NotRequired[List["RunbookTypeDef"]],
        "OpsItemId": NotRequired[str],
        "AssociationId": NotRequired[str],
        "ChangeRequestName": NotRequired[str],
    },
)

BaselineOverrideTypeDef = TypedDict(
    "BaselineOverrideTypeDef",
    {
        "OperatingSystem": NotRequired[OperatingSystemType],
        "GlobalFilters": NotRequired["PatchFilterGroupTypeDef"],
        "ApprovalRules": NotRequired["PatchRuleGroupTypeDef"],
        "ApprovedPatches": NotRequired[Sequence[str]],
        "ApprovedPatchesComplianceLevel": NotRequired[PatchComplianceLevelType],
        "RejectedPatches": NotRequired[Sequence[str]],
        "RejectedPatchesAction": NotRequired[PatchActionType],
        "ApprovedPatchesEnableNonSecurity": NotRequired[bool],
        "Sources": NotRequired[Sequence["PatchSourceTypeDef"]],
    },
)

CancelCommandRequestRequestTypeDef = TypedDict(
    "CancelCommandRequestRequestTypeDef",
    {
        "CommandId": str,
        "InstanceIds": NotRequired[Sequence[str]],
    },
)

CancelMaintenanceWindowExecutionRequestRequestTypeDef = TypedDict(
    "CancelMaintenanceWindowExecutionRequestRequestTypeDef",
    {
        "WindowExecutionId": str,
    },
)

CancelMaintenanceWindowExecutionResultTypeDef = TypedDict(
    "CancelMaintenanceWindowExecutionResultTypeDef",
    {
        "WindowExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CloudWatchOutputConfigTypeDef = TypedDict(
    "CloudWatchOutputConfigTypeDef",
    {
        "CloudWatchLogGroupName": NotRequired[str],
        "CloudWatchOutputEnabled": NotRequired[bool],
    },
)

CommandFilterTypeDef = TypedDict(
    "CommandFilterTypeDef",
    {
        "key": CommandFilterKeyType,
        "value": str,
    },
)

CommandInvocationTypeDef = TypedDict(
    "CommandInvocationTypeDef",
    {
        "CommandId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "InstanceName": NotRequired[str],
        "Comment": NotRequired[str],
        "DocumentName": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "RequestedDateTime": NotRequired[datetime],
        "Status": NotRequired[CommandInvocationStatusType],
        "StatusDetails": NotRequired[str],
        "TraceOutput": NotRequired[str],
        "StandardOutputUrl": NotRequired[str],
        "StandardErrorUrl": NotRequired[str],
        "CommandPlugins": NotRequired[List["CommandPluginTypeDef"]],
        "ServiceRole": NotRequired[str],
        "NotificationConfig": NotRequired["NotificationConfigTypeDef"],
        "CloudWatchOutputConfig": NotRequired["CloudWatchOutputConfigTypeDef"],
    },
)

CommandPluginTypeDef = TypedDict(
    "CommandPluginTypeDef",
    {
        "Name": NotRequired[str],
        "Status": NotRequired[CommandPluginStatusType],
        "StatusDetails": NotRequired[str],
        "ResponseCode": NotRequired[int],
        "ResponseStartDateTime": NotRequired[datetime],
        "ResponseFinishDateTime": NotRequired[datetime],
        "Output": NotRequired[str],
        "StandardOutputUrl": NotRequired[str],
        "StandardErrorUrl": NotRequired[str],
        "OutputS3Region": NotRequired[str],
        "OutputS3BucketName": NotRequired[str],
        "OutputS3KeyPrefix": NotRequired[str],
    },
)

CommandTypeDef = TypedDict(
    "CommandTypeDef",
    {
        "CommandId": NotRequired[str],
        "DocumentName": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "Comment": NotRequired[str],
        "ExpiresAfter": NotRequired[datetime],
        "Parameters": NotRequired[Dict[str, List[str]]],
        "InstanceIds": NotRequired[List[str]],
        "Targets": NotRequired[List["TargetTypeDef"]],
        "RequestedDateTime": NotRequired[datetime],
        "Status": NotRequired[CommandStatusType],
        "StatusDetails": NotRequired[str],
        "OutputS3Region": NotRequired[str],
        "OutputS3BucketName": NotRequired[str],
        "OutputS3KeyPrefix": NotRequired[str],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "TargetCount": NotRequired[int],
        "CompletedCount": NotRequired[int],
        "ErrorCount": NotRequired[int],
        "DeliveryTimedOutCount": NotRequired[int],
        "ServiceRole": NotRequired[str],
        "NotificationConfig": NotRequired["NotificationConfigTypeDef"],
        "CloudWatchOutputConfig": NotRequired["CloudWatchOutputConfigTypeDef"],
        "TimeoutSeconds": NotRequired[int],
    },
)

ComplianceExecutionSummaryTypeDef = TypedDict(
    "ComplianceExecutionSummaryTypeDef",
    {
        "ExecutionTime": datetime,
        "ExecutionId": NotRequired[str],
        "ExecutionType": NotRequired[str],
    },
)

ComplianceItemEntryTypeDef = TypedDict(
    "ComplianceItemEntryTypeDef",
    {
        "Severity": ComplianceSeverityType,
        "Status": ComplianceStatusType,
        "Id": NotRequired[str],
        "Title": NotRequired[str],
        "Details": NotRequired[Mapping[str, str]],
    },
)

ComplianceItemTypeDef = TypedDict(
    "ComplianceItemTypeDef",
    {
        "ComplianceType": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
        "Id": NotRequired[str],
        "Title": NotRequired[str],
        "Status": NotRequired[ComplianceStatusType],
        "Severity": NotRequired[ComplianceSeverityType],
        "ExecutionSummary": NotRequired["ComplianceExecutionSummaryTypeDef"],
        "Details": NotRequired[Dict[str, str]],
    },
)

ComplianceStringFilterTypeDef = TypedDict(
    "ComplianceStringFilterTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
        "Type": NotRequired[ComplianceQueryOperatorTypeType],
    },
)

ComplianceSummaryItemTypeDef = TypedDict(
    "ComplianceSummaryItemTypeDef",
    {
        "ComplianceType": NotRequired[str],
        "CompliantSummary": NotRequired["CompliantSummaryTypeDef"],
        "NonCompliantSummary": NotRequired["NonCompliantSummaryTypeDef"],
    },
)

CompliantSummaryTypeDef = TypedDict(
    "CompliantSummaryTypeDef",
    {
        "CompliantCount": NotRequired[int],
        "SeveritySummary": NotRequired["SeveritySummaryTypeDef"],
    },
)

CreateActivationRequestRequestTypeDef = TypedDict(
    "CreateActivationRequestRequestTypeDef",
    {
        "IamRole": str,
        "Description": NotRequired[str],
        "DefaultInstanceName": NotRequired[str],
        "RegistrationLimit": NotRequired[int],
        "ExpirationDate": NotRequired[Union[datetime, str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "RegistrationMetadata": NotRequired[Sequence["RegistrationMetadataItemTypeDef"]],
    },
)

CreateActivationResultTypeDef = TypedDict(
    "CreateActivationResultTypeDef",
    {
        "ActivationId": str,
        "ActivationCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAssociationBatchRequestEntryTypeDef = TypedDict(
    "CreateAssociationBatchRequestEntryTypeDef",
    {
        "Name": str,
        "InstanceId": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, Sequence[str]]],
        "AutomationTargetParameterName": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "Targets": NotRequired[Sequence["TargetTypeDef"]],
        "ScheduleExpression": NotRequired[str],
        "OutputLocation": NotRequired["InstanceAssociationOutputLocationTypeDef"],
        "AssociationName": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "MaxConcurrency": NotRequired[str],
        "ComplianceSeverity": NotRequired[AssociationComplianceSeverityType],
        "SyncCompliance": NotRequired[AssociationSyncComplianceType],
        "ApplyOnlyAtCronInterval": NotRequired[bool],
        "CalendarNames": NotRequired[Sequence[str]],
        "TargetLocations": NotRequired[Sequence["TargetLocationTypeDef"]],
    },
)

CreateAssociationBatchRequestRequestTypeDef = TypedDict(
    "CreateAssociationBatchRequestRequestTypeDef",
    {
        "Entries": Sequence["CreateAssociationBatchRequestEntryTypeDef"],
    },
)

CreateAssociationBatchResultTypeDef = TypedDict(
    "CreateAssociationBatchResultTypeDef",
    {
        "Successful": List["AssociationDescriptionTypeDef"],
        "Failed": List["FailedCreateAssociationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAssociationRequestRequestTypeDef = TypedDict(
    "CreateAssociationRequestRequestTypeDef",
    {
        "Name": str,
        "DocumentVersion": NotRequired[str],
        "InstanceId": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, Sequence[str]]],
        "Targets": NotRequired[Sequence["TargetTypeDef"]],
        "ScheduleExpression": NotRequired[str],
        "OutputLocation": NotRequired["InstanceAssociationOutputLocationTypeDef"],
        "AssociationName": NotRequired[str],
        "AutomationTargetParameterName": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "MaxConcurrency": NotRequired[str],
        "ComplianceSeverity": NotRequired[AssociationComplianceSeverityType],
        "SyncCompliance": NotRequired[AssociationSyncComplianceType],
        "ApplyOnlyAtCronInterval": NotRequired[bool],
        "CalendarNames": NotRequired[Sequence[str]],
        "TargetLocations": NotRequired[Sequence["TargetLocationTypeDef"]],
    },
)

CreateAssociationResultTypeDef = TypedDict(
    "CreateAssociationResultTypeDef",
    {
        "AssociationDescription": "AssociationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDocumentRequestRequestTypeDef = TypedDict(
    "CreateDocumentRequestRequestTypeDef",
    {
        "Content": str,
        "Name": str,
        "Requires": NotRequired[Sequence["DocumentRequiresTypeDef"]],
        "Attachments": NotRequired[Sequence["AttachmentsSourceTypeDef"]],
        "DisplayName": NotRequired[str],
        "VersionName": NotRequired[str],
        "DocumentType": NotRequired[DocumentTypeType],
        "DocumentFormat": NotRequired[DocumentFormatType],
        "TargetType": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDocumentResultTypeDef = TypedDict(
    "CreateDocumentResultTypeDef",
    {
        "DocumentDescription": "DocumentDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "CreateMaintenanceWindowRequestRequestTypeDef",
    {
        "Name": str,
        "Schedule": str,
        "Duration": int,
        "Cutoff": int,
        "AllowUnassociatedTargets": bool,
        "Description": NotRequired[str],
        "StartDate": NotRequired[str],
        "EndDate": NotRequired[str],
        "ScheduleTimezone": NotRequired[str],
        "ScheduleOffset": NotRequired[int],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateMaintenanceWindowResultTypeDef = TypedDict(
    "CreateMaintenanceWindowResultTypeDef",
    {
        "WindowId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateOpsItemRequestRequestTypeDef = TypedDict(
    "CreateOpsItemRequestRequestTypeDef",
    {
        "Description": str,
        "Source": str,
        "Title": str,
        "OpsItemType": NotRequired[str],
        "OperationalData": NotRequired[Mapping[str, "OpsItemDataValueTypeDef"]],
        "Notifications": NotRequired[Sequence["OpsItemNotificationTypeDef"]],
        "Priority": NotRequired[int],
        "RelatedOpsItems": NotRequired[Sequence["RelatedOpsItemTypeDef"]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "Category": NotRequired[str],
        "Severity": NotRequired[str],
        "ActualStartTime": NotRequired[Union[datetime, str]],
        "ActualEndTime": NotRequired[Union[datetime, str]],
        "PlannedStartTime": NotRequired[Union[datetime, str]],
        "PlannedEndTime": NotRequired[Union[datetime, str]],
    },
)

CreateOpsItemResponseTypeDef = TypedDict(
    "CreateOpsItemResponseTypeDef",
    {
        "OpsItemId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateOpsMetadataRequestRequestTypeDef = TypedDict(
    "CreateOpsMetadataRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Metadata": NotRequired[Mapping[str, "MetadataValueTypeDef"]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateOpsMetadataResultTypeDef = TypedDict(
    "CreateOpsMetadataResultTypeDef",
    {
        "OpsMetadataArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePatchBaselineRequestRequestTypeDef = TypedDict(
    "CreatePatchBaselineRequestRequestTypeDef",
    {
        "Name": str,
        "OperatingSystem": NotRequired[OperatingSystemType],
        "GlobalFilters": NotRequired["PatchFilterGroupTypeDef"],
        "ApprovalRules": NotRequired["PatchRuleGroupTypeDef"],
        "ApprovedPatches": NotRequired[Sequence[str]],
        "ApprovedPatchesComplianceLevel": NotRequired[PatchComplianceLevelType],
        "ApprovedPatchesEnableNonSecurity": NotRequired[bool],
        "RejectedPatches": NotRequired[Sequence[str]],
        "RejectedPatchesAction": NotRequired[PatchActionType],
        "Description": NotRequired[str],
        "Sources": NotRequired[Sequence["PatchSourceTypeDef"]],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreatePatchBaselineResultTypeDef = TypedDict(
    "CreatePatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResourceDataSyncRequestRequestTypeDef = TypedDict(
    "CreateResourceDataSyncRequestRequestTypeDef",
    {
        "SyncName": str,
        "S3Destination": NotRequired["ResourceDataSyncS3DestinationTypeDef"],
        "SyncType": NotRequired[str],
        "SyncSource": NotRequired["ResourceDataSyncSourceTypeDef"],
    },
)

DeleteActivationRequestRequestTypeDef = TypedDict(
    "DeleteActivationRequestRequestTypeDef",
    {
        "ActivationId": str,
    },
)

DeleteAssociationRequestRequestTypeDef = TypedDict(
    "DeleteAssociationRequestRequestTypeDef",
    {
        "Name": NotRequired[str],
        "InstanceId": NotRequired[str],
        "AssociationId": NotRequired[str],
    },
)

DeleteDocumentRequestRequestTypeDef = TypedDict(
    "DeleteDocumentRequestRequestTypeDef",
    {
        "Name": str,
        "DocumentVersion": NotRequired[str],
        "VersionName": NotRequired[str],
        "Force": NotRequired[bool],
    },
)

DeleteInventoryRequestRequestTypeDef = TypedDict(
    "DeleteInventoryRequestRequestTypeDef",
    {
        "TypeName": str,
        "SchemaDeleteOption": NotRequired[InventorySchemaDeleteOptionType],
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
    },
)

DeleteInventoryResultTypeDef = TypedDict(
    "DeleteInventoryResultTypeDef",
    {
        "DeletionId": str,
        "TypeName": str,
        "DeletionSummary": "InventoryDeletionSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "DeleteMaintenanceWindowRequestRequestTypeDef",
    {
        "WindowId": str,
    },
)

DeleteMaintenanceWindowResultTypeDef = TypedDict(
    "DeleteMaintenanceWindowResultTypeDef",
    {
        "WindowId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteOpsMetadataRequestRequestTypeDef = TypedDict(
    "DeleteOpsMetadataRequestRequestTypeDef",
    {
        "OpsMetadataArn": str,
    },
)

DeleteParameterRequestRequestTypeDef = TypedDict(
    "DeleteParameterRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteParametersRequestRequestTypeDef = TypedDict(
    "DeleteParametersRequestRequestTypeDef",
    {
        "Names": Sequence[str],
    },
)

DeleteParametersResultTypeDef = TypedDict(
    "DeleteParametersResultTypeDef",
    {
        "DeletedParameters": List[str],
        "InvalidParameters": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePatchBaselineRequestRequestTypeDef = TypedDict(
    "DeletePatchBaselineRequestRequestTypeDef",
    {
        "BaselineId": str,
    },
)

DeletePatchBaselineResultTypeDef = TypedDict(
    "DeletePatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourceDataSyncRequestRequestTypeDef = TypedDict(
    "DeleteResourceDataSyncRequestRequestTypeDef",
    {
        "SyncName": str,
        "SyncType": NotRequired[str],
    },
)

DeregisterManagedInstanceRequestRequestTypeDef = TypedDict(
    "DeregisterManagedInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

DeregisterPatchBaselineForPatchGroupRequestRequestTypeDef = TypedDict(
    "DeregisterPatchBaselineForPatchGroupRequestRequestTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
    },
)

DeregisterPatchBaselineForPatchGroupResultTypeDef = TypedDict(
    "DeregisterPatchBaselineForPatchGroupResultTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterTargetFromMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "DeregisterTargetFromMaintenanceWindowRequestRequestTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "Safe": NotRequired[bool],
    },
)

DeregisterTargetFromMaintenanceWindowResultTypeDef = TypedDict(
    "DeregisterTargetFromMaintenanceWindowResultTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterTaskFromMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "DeregisterTaskFromMaintenanceWindowRequestRequestTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
    },
)

DeregisterTaskFromMaintenanceWindowResultTypeDef = TypedDict(
    "DeregisterTaskFromMaintenanceWindowResultTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeActivationsFilterTypeDef = TypedDict(
    "DescribeActivationsFilterTypeDef",
    {
        "FilterKey": NotRequired[DescribeActivationsFilterKeysType],
        "FilterValues": NotRequired[Sequence[str]],
    },
)

DescribeActivationsRequestRequestTypeDef = TypedDict(
    "DescribeActivationsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["DescribeActivationsFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeActivationsResultTypeDef = TypedDict(
    "DescribeActivationsResultTypeDef",
    {
        "ActivationList": List["ActivationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAssociationExecutionTargetsRequestRequestTypeDef = TypedDict(
    "DescribeAssociationExecutionTargetsRequestRequestTypeDef",
    {
        "AssociationId": str,
        "ExecutionId": str,
        "Filters": NotRequired[Sequence["AssociationExecutionTargetsFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeAssociationExecutionTargetsResultTypeDef = TypedDict(
    "DescribeAssociationExecutionTargetsResultTypeDef",
    {
        "AssociationExecutionTargets": List["AssociationExecutionTargetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAssociationExecutionsRequestRequestTypeDef = TypedDict(
    "DescribeAssociationExecutionsRequestRequestTypeDef",
    {
        "AssociationId": str,
        "Filters": NotRequired[Sequence["AssociationExecutionFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeAssociationExecutionsResultTypeDef = TypedDict(
    "DescribeAssociationExecutionsResultTypeDef",
    {
        "AssociationExecutions": List["AssociationExecutionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAssociationRequestRequestTypeDef = TypedDict(
    "DescribeAssociationRequestRequestTypeDef",
    {
        "Name": NotRequired[str],
        "InstanceId": NotRequired[str],
        "AssociationId": NotRequired[str],
        "AssociationVersion": NotRequired[str],
    },
)

DescribeAssociationResultTypeDef = TypedDict(
    "DescribeAssociationResultTypeDef",
    {
        "AssociationDescription": "AssociationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAutomationExecutionsRequestRequestTypeDef = TypedDict(
    "DescribeAutomationExecutionsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["AutomationExecutionFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeAutomationExecutionsResultTypeDef = TypedDict(
    "DescribeAutomationExecutionsResultTypeDef",
    {
        "AutomationExecutionMetadataList": List["AutomationExecutionMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAutomationStepExecutionsRequestRequestTypeDef = TypedDict(
    "DescribeAutomationStepExecutionsRequestRequestTypeDef",
    {
        "AutomationExecutionId": str,
        "Filters": NotRequired[Sequence["StepExecutionFilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ReverseOrder": NotRequired[bool],
    },
)

DescribeAutomationStepExecutionsResultTypeDef = TypedDict(
    "DescribeAutomationStepExecutionsResultTypeDef",
    {
        "StepExecutions": List["StepExecutionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAvailablePatchesRequestRequestTypeDef = TypedDict(
    "DescribeAvailablePatchesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["PatchOrchestratorFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeAvailablePatchesResultTypeDef = TypedDict(
    "DescribeAvailablePatchesResultTypeDef",
    {
        "Patches": List["PatchTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDocumentPermissionRequestRequestTypeDef = TypedDict(
    "DescribeDocumentPermissionRequestRequestTypeDef",
    {
        "Name": str,
        "PermissionType": Literal["Share"],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeDocumentPermissionResponseTypeDef = TypedDict(
    "DescribeDocumentPermissionResponseTypeDef",
    {
        "AccountIds": List[str],
        "AccountSharingInfoList": List["AccountSharingInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDocumentRequestRequestTypeDef = TypedDict(
    "DescribeDocumentRequestRequestTypeDef",
    {
        "Name": str,
        "DocumentVersion": NotRequired[str],
        "VersionName": NotRequired[str],
    },
)

DescribeDocumentResultTypeDef = TypedDict(
    "DescribeDocumentResultTypeDef",
    {
        "Document": "DocumentDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEffectiveInstanceAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeEffectiveInstanceAssociationsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeEffectiveInstanceAssociationsResultTypeDef = TypedDict(
    "DescribeEffectiveInstanceAssociationsResultTypeDef",
    {
        "Associations": List["InstanceAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEffectivePatchesForPatchBaselineRequestRequestTypeDef = TypedDict(
    "DescribeEffectivePatchesForPatchBaselineRequestRequestTypeDef",
    {
        "BaselineId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeEffectivePatchesForPatchBaselineResultTypeDef = TypedDict(
    "DescribeEffectivePatchesForPatchBaselineResultTypeDef",
    {
        "EffectivePatches": List["EffectivePatchTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceAssociationsStatusRequestRequestTypeDef = TypedDict(
    "DescribeInstanceAssociationsStatusRequestRequestTypeDef",
    {
        "InstanceId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeInstanceAssociationsStatusResultTypeDef = TypedDict(
    "DescribeInstanceAssociationsStatusResultTypeDef",
    {
        "InstanceAssociationStatusInfos": List["InstanceAssociationStatusInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceInformationRequestRequestTypeDef = TypedDict(
    "DescribeInstanceInformationRequestRequestTypeDef",
    {
        "InstanceInformationFilterList": NotRequired[Sequence["InstanceInformationFilterTypeDef"]],
        "Filters": NotRequired[Sequence["InstanceInformationStringFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeInstanceInformationResultTypeDef = TypedDict(
    "DescribeInstanceInformationResultTypeDef",
    {
        "InstanceInformationList": List["InstanceInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstancePatchStatesForPatchGroupRequestRequestTypeDef = TypedDict(
    "DescribeInstancePatchStatesForPatchGroupRequestRequestTypeDef",
    {
        "PatchGroup": str,
        "Filters": NotRequired[Sequence["InstancePatchStateFilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeInstancePatchStatesForPatchGroupResultTypeDef = TypedDict(
    "DescribeInstancePatchStatesForPatchGroupResultTypeDef",
    {
        "InstancePatchStates": List["InstancePatchStateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstancePatchStatesRequestRequestTypeDef = TypedDict(
    "DescribeInstancePatchStatesRequestRequestTypeDef",
    {
        "InstanceIds": Sequence[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeInstancePatchStatesResultTypeDef = TypedDict(
    "DescribeInstancePatchStatesResultTypeDef",
    {
        "InstancePatchStates": List["InstancePatchStateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstancePatchesRequestRequestTypeDef = TypedDict(
    "DescribeInstancePatchesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Filters": NotRequired[Sequence["PatchOrchestratorFilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeInstancePatchesResultTypeDef = TypedDict(
    "DescribeInstancePatchesResultTypeDef",
    {
        "Patches": List["PatchComplianceDataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInventoryDeletionsRequestRequestTypeDef = TypedDict(
    "DescribeInventoryDeletionsRequestRequestTypeDef",
    {
        "DeletionId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeInventoryDeletionsResultTypeDef = TypedDict(
    "DescribeInventoryDeletionsResultTypeDef",
    {
        "InventoryDeletions": List["InventoryDeletionStatusItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMaintenanceWindowExecutionTaskInvocationsRequestRequestTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTaskInvocationsRequestRequestTypeDef",
    {
        "WindowExecutionId": str,
        "TaskId": str,
        "Filters": NotRequired[Sequence["MaintenanceWindowFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef",
    {
        "WindowExecutionTaskInvocationIdentities": List[
            "MaintenanceWindowExecutionTaskInvocationIdentityTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMaintenanceWindowExecutionTasksRequestRequestTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTasksRequestRequestTypeDef",
    {
        "WindowExecutionId": str,
        "Filters": NotRequired[Sequence["MaintenanceWindowFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeMaintenanceWindowExecutionTasksResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTasksResultTypeDef",
    {
        "WindowExecutionTaskIdentities": List["MaintenanceWindowExecutionTaskIdentityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMaintenanceWindowExecutionsRequestRequestTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionsRequestRequestTypeDef",
    {
        "WindowId": str,
        "Filters": NotRequired[Sequence["MaintenanceWindowFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeMaintenanceWindowExecutionsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionsResultTypeDef",
    {
        "WindowExecutions": List["MaintenanceWindowExecutionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMaintenanceWindowScheduleRequestRequestTypeDef = TypedDict(
    "DescribeMaintenanceWindowScheduleRequestRequestTypeDef",
    {
        "WindowId": NotRequired[str],
        "Targets": NotRequired[Sequence["TargetTypeDef"]],
        "ResourceType": NotRequired[MaintenanceWindowResourceTypeType],
        "Filters": NotRequired[Sequence["PatchOrchestratorFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeMaintenanceWindowScheduleResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowScheduleResultTypeDef",
    {
        "ScheduledWindowExecutions": List["ScheduledWindowExecutionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMaintenanceWindowTargetsRequestRequestTypeDef = TypedDict(
    "DescribeMaintenanceWindowTargetsRequestRequestTypeDef",
    {
        "WindowId": str,
        "Filters": NotRequired[Sequence["MaintenanceWindowFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeMaintenanceWindowTargetsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowTargetsResultTypeDef",
    {
        "Targets": List["MaintenanceWindowTargetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMaintenanceWindowTasksRequestRequestTypeDef = TypedDict(
    "DescribeMaintenanceWindowTasksRequestRequestTypeDef",
    {
        "WindowId": str,
        "Filters": NotRequired[Sequence["MaintenanceWindowFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeMaintenanceWindowTasksResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowTasksResultTypeDef",
    {
        "Tasks": List["MaintenanceWindowTaskTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMaintenanceWindowsForTargetRequestRequestTypeDef = TypedDict(
    "DescribeMaintenanceWindowsForTargetRequestRequestTypeDef",
    {
        "Targets": Sequence["TargetTypeDef"],
        "ResourceType": MaintenanceWindowResourceTypeType,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeMaintenanceWindowsForTargetResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowsForTargetResultTypeDef",
    {
        "WindowIdentities": List["MaintenanceWindowIdentityForTargetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMaintenanceWindowsRequestRequestTypeDef = TypedDict(
    "DescribeMaintenanceWindowsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["MaintenanceWindowFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeMaintenanceWindowsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowsResultTypeDef",
    {
        "WindowIdentities": List["MaintenanceWindowIdentityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOpsItemsRequestRequestTypeDef = TypedDict(
    "DescribeOpsItemsRequestRequestTypeDef",
    {
        "OpsItemFilters": NotRequired[Sequence["OpsItemFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeOpsItemsResponseTypeDef = TypedDict(
    "DescribeOpsItemsResponseTypeDef",
    {
        "NextToken": str,
        "OpsItemSummaries": List["OpsItemSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeParametersRequestRequestTypeDef = TypedDict(
    "DescribeParametersRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["ParametersFilterTypeDef"]],
        "ParameterFilters": NotRequired[Sequence["ParameterStringFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeParametersResultTypeDef = TypedDict(
    "DescribeParametersResultTypeDef",
    {
        "Parameters": List["ParameterMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePatchBaselinesRequestRequestTypeDef = TypedDict(
    "DescribePatchBaselinesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["PatchOrchestratorFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribePatchBaselinesResultTypeDef = TypedDict(
    "DescribePatchBaselinesResultTypeDef",
    {
        "BaselineIdentities": List["PatchBaselineIdentityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePatchGroupStateRequestRequestTypeDef = TypedDict(
    "DescribePatchGroupStateRequestRequestTypeDef",
    {
        "PatchGroup": str,
    },
)

DescribePatchGroupStateResultTypeDef = TypedDict(
    "DescribePatchGroupStateResultTypeDef",
    {
        "Instances": int,
        "InstancesWithInstalledPatches": int,
        "InstancesWithInstalledOtherPatches": int,
        "InstancesWithInstalledPendingRebootPatches": int,
        "InstancesWithInstalledRejectedPatches": int,
        "InstancesWithMissingPatches": int,
        "InstancesWithFailedPatches": int,
        "InstancesWithNotApplicablePatches": int,
        "InstancesWithUnreportedNotApplicablePatches": int,
        "InstancesWithCriticalNonCompliantPatches": int,
        "InstancesWithSecurityNonCompliantPatches": int,
        "InstancesWithOtherNonCompliantPatches": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePatchGroupsRequestRequestTypeDef = TypedDict(
    "DescribePatchGroupsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence["PatchOrchestratorFilterTypeDef"]],
        "NextToken": NotRequired[str],
    },
)

DescribePatchGroupsResultTypeDef = TypedDict(
    "DescribePatchGroupsResultTypeDef",
    {
        "Mappings": List["PatchGroupPatchBaselineMappingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePatchPropertiesRequestRequestTypeDef = TypedDict(
    "DescribePatchPropertiesRequestRequestTypeDef",
    {
        "OperatingSystem": OperatingSystemType,
        "Property": PatchPropertyType,
        "PatchSet": NotRequired[PatchSetType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribePatchPropertiesResultTypeDef = TypedDict(
    "DescribePatchPropertiesResultTypeDef",
    {
        "Properties": List[Dict[str, str]],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSessionsRequestRequestTypeDef = TypedDict(
    "DescribeSessionsRequestRequestTypeDef",
    {
        "State": SessionStateType,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence["SessionFilterTypeDef"]],
    },
)

DescribeSessionsResponseTypeDef = TypedDict(
    "DescribeSessionsResponseTypeDef",
    {
        "Sessions": List["SessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateOpsItemRelatedItemRequestRequestTypeDef = TypedDict(
    "DisassociateOpsItemRelatedItemRequestRequestTypeDef",
    {
        "OpsItemId": str,
        "AssociationId": str,
    },
)

DocumentDefaultVersionDescriptionTypeDef = TypedDict(
    "DocumentDefaultVersionDescriptionTypeDef",
    {
        "Name": NotRequired[str],
        "DefaultVersion": NotRequired[str],
        "DefaultVersionName": NotRequired[str],
    },
)

DocumentDescriptionTypeDef = TypedDict(
    "DocumentDescriptionTypeDef",
    {
        "Sha1": NotRequired[str],
        "Hash": NotRequired[str],
        "HashType": NotRequired[DocumentHashTypeType],
        "Name": NotRequired[str],
        "DisplayName": NotRequired[str],
        "VersionName": NotRequired[str],
        "Owner": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "Status": NotRequired[DocumentStatusType],
        "StatusInformation": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "Description": NotRequired[str],
        "Parameters": NotRequired[List["DocumentParameterTypeDef"]],
        "PlatformTypes": NotRequired[List[PlatformTypeType]],
        "DocumentType": NotRequired[DocumentTypeType],
        "SchemaVersion": NotRequired[str],
        "LatestVersion": NotRequired[str],
        "DefaultVersion": NotRequired[str],
        "DocumentFormat": NotRequired[DocumentFormatType],
        "TargetType": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "AttachmentsInformation": NotRequired[List["AttachmentInformationTypeDef"]],
        "Requires": NotRequired[List["DocumentRequiresTypeDef"]],
        "Author": NotRequired[str],
        "ReviewInformation": NotRequired[List["ReviewInformationTypeDef"]],
        "ApprovedVersion": NotRequired[str],
        "PendingReviewVersion": NotRequired[str],
        "ReviewStatus": NotRequired[ReviewStatusType],
        "Category": NotRequired[List[str]],
        "CategoryEnum": NotRequired[List[str]],
    },
)

DocumentFilterTypeDef = TypedDict(
    "DocumentFilterTypeDef",
    {
        "key": DocumentFilterKeyType,
        "value": str,
    },
)

DocumentIdentifierTypeDef = TypedDict(
    "DocumentIdentifierTypeDef",
    {
        "Name": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "DisplayName": NotRequired[str],
        "Owner": NotRequired[str],
        "VersionName": NotRequired[str],
        "PlatformTypes": NotRequired[List[PlatformTypeType]],
        "DocumentVersion": NotRequired[str],
        "DocumentType": NotRequired[DocumentTypeType],
        "SchemaVersion": NotRequired[str],
        "DocumentFormat": NotRequired[DocumentFormatType],
        "TargetType": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "Requires": NotRequired[List["DocumentRequiresTypeDef"]],
        "ReviewStatus": NotRequired[ReviewStatusType],
        "Author": NotRequired[str],
    },
)

DocumentKeyValuesFilterTypeDef = TypedDict(
    "DocumentKeyValuesFilterTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)

DocumentMetadataResponseInfoTypeDef = TypedDict(
    "DocumentMetadataResponseInfoTypeDef",
    {
        "ReviewerResponse": NotRequired[List["DocumentReviewerResponseSourceTypeDef"]],
    },
)

DocumentParameterTypeDef = TypedDict(
    "DocumentParameterTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[DocumentParameterTypeType],
        "Description": NotRequired[str],
        "DefaultValue": NotRequired[str],
    },
)

DocumentRequiresTypeDef = TypedDict(
    "DocumentRequiresTypeDef",
    {
        "Name": str,
        "Version": NotRequired[str],
    },
)

DocumentReviewCommentSourceTypeDef = TypedDict(
    "DocumentReviewCommentSourceTypeDef",
    {
        "Type": NotRequired[Literal["Comment"]],
        "Content": NotRequired[str],
    },
)

DocumentReviewerResponseSourceTypeDef = TypedDict(
    "DocumentReviewerResponseSourceTypeDef",
    {
        "CreateTime": NotRequired[datetime],
        "UpdatedTime": NotRequired[datetime],
        "ReviewStatus": NotRequired[ReviewStatusType],
        "Comment": NotRequired[List["DocumentReviewCommentSourceTypeDef"]],
        "Reviewer": NotRequired[str],
    },
)

DocumentReviewsTypeDef = TypedDict(
    "DocumentReviewsTypeDef",
    {
        "Action": DocumentReviewActionType,
        "Comment": NotRequired[Sequence["DocumentReviewCommentSourceTypeDef"]],
    },
)

DocumentVersionInfoTypeDef = TypedDict(
    "DocumentVersionInfoTypeDef",
    {
        "Name": NotRequired[str],
        "DisplayName": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "VersionName": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "IsDefaultVersion": NotRequired[bool],
        "DocumentFormat": NotRequired[DocumentFormatType],
        "Status": NotRequired[DocumentStatusType],
        "StatusInformation": NotRequired[str],
        "ReviewStatus": NotRequired[ReviewStatusType],
    },
)

EffectivePatchTypeDef = TypedDict(
    "EffectivePatchTypeDef",
    {
        "Patch": NotRequired["PatchTypeDef"],
        "PatchStatus": NotRequired["PatchStatusTypeDef"],
    },
)

FailedCreateAssociationTypeDef = TypedDict(
    "FailedCreateAssociationTypeDef",
    {
        "Entry": NotRequired["CreateAssociationBatchRequestEntryTypeDef"],
        "Message": NotRequired[str],
        "Fault": NotRequired[FaultType],
    },
)

FailureDetailsTypeDef = TypedDict(
    "FailureDetailsTypeDef",
    {
        "FailureStage": NotRequired[str],
        "FailureType": NotRequired[str],
        "Details": NotRequired[Dict[str, List[str]]],
    },
)

GetAutomationExecutionRequestRequestTypeDef = TypedDict(
    "GetAutomationExecutionRequestRequestTypeDef",
    {
        "AutomationExecutionId": str,
    },
)

GetAutomationExecutionResultTypeDef = TypedDict(
    "GetAutomationExecutionResultTypeDef",
    {
        "AutomationExecution": "AutomationExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCalendarStateRequestRequestTypeDef = TypedDict(
    "GetCalendarStateRequestRequestTypeDef",
    {
        "CalendarNames": Sequence[str],
        "AtTime": NotRequired[str],
    },
)

GetCalendarStateResponseTypeDef = TypedDict(
    "GetCalendarStateResponseTypeDef",
    {
        "State": CalendarStateType,
        "AtTime": str,
        "NextTransitionTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCommandInvocationRequestRequestTypeDef = TypedDict(
    "GetCommandInvocationRequestRequestTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "PluginName": NotRequired[str],
    },
)

GetCommandInvocationResultTypeDef = TypedDict(
    "GetCommandInvocationResultTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "Comment": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "PluginName": str,
        "ResponseCode": int,
        "ExecutionStartDateTime": str,
        "ExecutionElapsedTime": str,
        "ExecutionEndDateTime": str,
        "Status": CommandInvocationStatusType,
        "StatusDetails": str,
        "StandardOutputContent": str,
        "StandardOutputUrl": str,
        "StandardErrorContent": str,
        "StandardErrorUrl": str,
        "CloudWatchOutputConfig": "CloudWatchOutputConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectionStatusRequestRequestTypeDef = TypedDict(
    "GetConnectionStatusRequestRequestTypeDef",
    {
        "Target": str,
    },
)

GetConnectionStatusResponseTypeDef = TypedDict(
    "GetConnectionStatusResponseTypeDef",
    {
        "Target": str,
        "Status": ConnectionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDefaultPatchBaselineRequestRequestTypeDef = TypedDict(
    "GetDefaultPatchBaselineRequestRequestTypeDef",
    {
        "OperatingSystem": NotRequired[OperatingSystemType],
    },
)

GetDefaultPatchBaselineResultTypeDef = TypedDict(
    "GetDefaultPatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "OperatingSystem": OperatingSystemType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeployablePatchSnapshotForInstanceRequestRequestTypeDef = TypedDict(
    "GetDeployablePatchSnapshotForInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
        "SnapshotId": str,
        "BaselineOverride": NotRequired["BaselineOverrideTypeDef"],
    },
)

GetDeployablePatchSnapshotForInstanceResultTypeDef = TypedDict(
    "GetDeployablePatchSnapshotForInstanceResultTypeDef",
    {
        "InstanceId": str,
        "SnapshotId": str,
        "SnapshotDownloadUrl": str,
        "Product": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDocumentRequestRequestTypeDef = TypedDict(
    "GetDocumentRequestRequestTypeDef",
    {
        "Name": str,
        "VersionName": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "DocumentFormat": NotRequired[DocumentFormatType],
    },
)

GetDocumentResultTypeDef = TypedDict(
    "GetDocumentResultTypeDef",
    {
        "Name": str,
        "CreatedDate": datetime,
        "DisplayName": str,
        "VersionName": str,
        "DocumentVersion": str,
        "Status": DocumentStatusType,
        "StatusInformation": str,
        "Content": str,
        "DocumentType": DocumentTypeType,
        "DocumentFormat": DocumentFormatType,
        "Requires": List["DocumentRequiresTypeDef"],
        "AttachmentsContent": List["AttachmentContentTypeDef"],
        "ReviewStatus": ReviewStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInventoryRequestRequestTypeDef = TypedDict(
    "GetInventoryRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["InventoryFilterTypeDef"]],
        "Aggregators": NotRequired[Sequence["InventoryAggregatorTypeDef"]],
        "ResultAttributes": NotRequired[Sequence["ResultAttributeTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetInventoryResultTypeDef = TypedDict(
    "GetInventoryResultTypeDef",
    {
        "Entities": List["InventoryResultEntityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInventorySchemaRequestRequestTypeDef = TypedDict(
    "GetInventorySchemaRequestRequestTypeDef",
    {
        "TypeName": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Aggregator": NotRequired[bool],
        "SubType": NotRequired[bool],
    },
)

GetInventorySchemaResultTypeDef = TypedDict(
    "GetInventorySchemaResultTypeDef",
    {
        "Schemas": List["InventoryItemSchemaTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMaintenanceWindowExecutionRequestRequestTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionRequestRequestTypeDef",
    {
        "WindowExecutionId": str,
    },
)

GetMaintenanceWindowExecutionResultTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionResultTypeDef",
    {
        "WindowExecutionId": str,
        "TaskIds": List[str],
        "Status": MaintenanceWindowExecutionStatusType,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMaintenanceWindowExecutionTaskInvocationRequestRequestTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionTaskInvocationRequestRequestTypeDef",
    {
        "WindowExecutionId": str,
        "TaskId": str,
        "InvocationId": str,
    },
)

GetMaintenanceWindowExecutionTaskInvocationResultTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionTaskInvocationResultTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "InvocationId": str,
        "ExecutionId": str,
        "TaskType": MaintenanceWindowTaskTypeType,
        "Parameters": str,
        "Status": MaintenanceWindowExecutionStatusType,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "OwnerInformation": str,
        "WindowTargetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMaintenanceWindowExecutionTaskRequestRequestTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionTaskRequestRequestTypeDef",
    {
        "WindowExecutionId": str,
        "TaskId": str,
    },
)

GetMaintenanceWindowExecutionTaskResultTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionTaskResultTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "TaskArn": str,
        "ServiceRole": str,
        "Type": MaintenanceWindowTaskTypeType,
        "TaskParameters": List[Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"]],
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Status": MaintenanceWindowExecutionStatusType,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "GetMaintenanceWindowRequestRequestTypeDef",
    {
        "WindowId": str,
    },
)

GetMaintenanceWindowResultTypeDef = TypedDict(
    "GetMaintenanceWindowResultTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "StartDate": str,
        "EndDate": str,
        "Schedule": str,
        "ScheduleTimezone": str,
        "ScheduleOffset": int,
        "NextExecutionTime": str,
        "Duration": int,
        "Cutoff": int,
        "AllowUnassociatedTargets": bool,
        "Enabled": bool,
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMaintenanceWindowTaskRequestRequestTypeDef = TypedDict(
    "GetMaintenanceWindowTaskRequestRequestTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
    },
)

GetMaintenanceWindowTaskResultTypeDef = TypedDict(
    "GetMaintenanceWindowTaskResultTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "Targets": List["TargetTypeDef"],
        "TaskArn": str,
        "ServiceRoleArn": str,
        "TaskType": MaintenanceWindowTaskTypeType,
        "TaskParameters": Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"],
        "TaskInvocationParameters": "MaintenanceWindowTaskInvocationParametersTypeDef",
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "LoggingInfo": "LoggingInfoTypeDef",
        "Name": str,
        "Description": str,
        "CutoffBehavior": MaintenanceWindowTaskCutoffBehaviorType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOpsItemRequestRequestTypeDef = TypedDict(
    "GetOpsItemRequestRequestTypeDef",
    {
        "OpsItemId": str,
    },
)

GetOpsItemResponseTypeDef = TypedDict(
    "GetOpsItemResponseTypeDef",
    {
        "OpsItem": "OpsItemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOpsMetadataRequestRequestTypeDef = TypedDict(
    "GetOpsMetadataRequestRequestTypeDef",
    {
        "OpsMetadataArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetOpsMetadataResultTypeDef = TypedDict(
    "GetOpsMetadataResultTypeDef",
    {
        "ResourceId": str,
        "Metadata": Dict[str, "MetadataValueTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOpsSummaryRequestRequestTypeDef = TypedDict(
    "GetOpsSummaryRequestRequestTypeDef",
    {
        "SyncName": NotRequired[str],
        "Filters": NotRequired[Sequence["OpsFilterTypeDef"]],
        "Aggregators": NotRequired[Sequence["OpsAggregatorTypeDef"]],
        "ResultAttributes": NotRequired[Sequence["OpsResultAttributeTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetOpsSummaryResultTypeDef = TypedDict(
    "GetOpsSummaryResultTypeDef",
    {
        "Entities": List["OpsEntityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetParameterHistoryRequestRequestTypeDef = TypedDict(
    "GetParameterHistoryRequestRequestTypeDef",
    {
        "Name": str,
        "WithDecryption": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetParameterHistoryResultTypeDef = TypedDict(
    "GetParameterHistoryResultTypeDef",
    {
        "Parameters": List["ParameterHistoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetParameterRequestRequestTypeDef = TypedDict(
    "GetParameterRequestRequestTypeDef",
    {
        "Name": str,
        "WithDecryption": NotRequired[bool],
    },
)

GetParameterResultTypeDef = TypedDict(
    "GetParameterResultTypeDef",
    {
        "Parameter": "ParameterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetParametersByPathRequestRequestTypeDef = TypedDict(
    "GetParametersByPathRequestRequestTypeDef",
    {
        "Path": str,
        "Recursive": NotRequired[bool],
        "ParameterFilters": NotRequired[Sequence["ParameterStringFilterTypeDef"]],
        "WithDecryption": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetParametersByPathResultTypeDef = TypedDict(
    "GetParametersByPathResultTypeDef",
    {
        "Parameters": List["ParameterTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetParametersRequestRequestTypeDef = TypedDict(
    "GetParametersRequestRequestTypeDef",
    {
        "Names": Sequence[str],
        "WithDecryption": NotRequired[bool],
    },
)

GetParametersResultTypeDef = TypedDict(
    "GetParametersResultTypeDef",
    {
        "Parameters": List["ParameterTypeDef"],
        "InvalidParameters": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPatchBaselineForPatchGroupRequestRequestTypeDef = TypedDict(
    "GetPatchBaselineForPatchGroupRequestRequestTypeDef",
    {
        "PatchGroup": str,
        "OperatingSystem": NotRequired[OperatingSystemType],
    },
)

GetPatchBaselineForPatchGroupResultTypeDef = TypedDict(
    "GetPatchBaselineForPatchGroupResultTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
        "OperatingSystem": OperatingSystemType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPatchBaselineRequestRequestTypeDef = TypedDict(
    "GetPatchBaselineRequestRequestTypeDef",
    {
        "BaselineId": str,
    },
)

GetPatchBaselineResultTypeDef = TypedDict(
    "GetPatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "Name": str,
        "OperatingSystem": OperatingSystemType,
        "GlobalFilters": "PatchFilterGroupTypeDef",
        "ApprovalRules": "PatchRuleGroupTypeDef",
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": PatchComplianceLevelType,
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": PatchActionType,
        "PatchGroups": List[str],
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
        "Description": str,
        "Sources": List["PatchSourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceSettingRequestRequestTypeDef = TypedDict(
    "GetServiceSettingRequestRequestTypeDef",
    {
        "SettingId": str,
    },
)

GetServiceSettingResultTypeDef = TypedDict(
    "GetServiceSettingResultTypeDef",
    {
        "ServiceSetting": "ServiceSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceAggregatedAssociationOverviewTypeDef = TypedDict(
    "InstanceAggregatedAssociationOverviewTypeDef",
    {
        "DetailedStatus": NotRequired[str],
        "InstanceAssociationStatusAggregatedCount": NotRequired[Dict[str, int]],
    },
)

InstanceAssociationOutputLocationTypeDef = TypedDict(
    "InstanceAssociationOutputLocationTypeDef",
    {
        "S3Location": NotRequired["S3OutputLocationTypeDef"],
    },
)

InstanceAssociationOutputUrlTypeDef = TypedDict(
    "InstanceAssociationOutputUrlTypeDef",
    {
        "S3OutputUrl": NotRequired["S3OutputUrlTypeDef"],
    },
)

InstanceAssociationStatusInfoTypeDef = TypedDict(
    "InstanceAssociationStatusInfoTypeDef",
    {
        "AssociationId": NotRequired[str],
        "Name": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "AssociationVersion": NotRequired[str],
        "InstanceId": NotRequired[str],
        "ExecutionDate": NotRequired[datetime],
        "Status": NotRequired[str],
        "DetailedStatus": NotRequired[str],
        "ExecutionSummary": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "OutputUrl": NotRequired["InstanceAssociationOutputUrlTypeDef"],
        "AssociationName": NotRequired[str],
    },
)

InstanceAssociationTypeDef = TypedDict(
    "InstanceAssociationTypeDef",
    {
        "AssociationId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "Content": NotRequired[str],
        "AssociationVersion": NotRequired[str],
    },
)

InstanceInformationFilterTypeDef = TypedDict(
    "InstanceInformationFilterTypeDef",
    {
        "key": InstanceInformationFilterKeyType,
        "valueSet": Sequence[str],
    },
)

InstanceInformationStringFilterTypeDef = TypedDict(
    "InstanceInformationStringFilterTypeDef",
    {
        "Key": str,
        "Values": Sequence[str],
    },
)

InstanceInformationTypeDef = TypedDict(
    "InstanceInformationTypeDef",
    {
        "InstanceId": NotRequired[str],
        "PingStatus": NotRequired[PingStatusType],
        "LastPingDateTime": NotRequired[datetime],
        "AgentVersion": NotRequired[str],
        "IsLatestVersion": NotRequired[bool],
        "PlatformType": NotRequired[PlatformTypeType],
        "PlatformName": NotRequired[str],
        "PlatformVersion": NotRequired[str],
        "ActivationId": NotRequired[str],
        "IamRole": NotRequired[str],
        "RegistrationDate": NotRequired[datetime],
        "ResourceType": NotRequired[ResourceTypeType],
        "Name": NotRequired[str],
        "IPAddress": NotRequired[str],
        "ComputerName": NotRequired[str],
        "AssociationStatus": NotRequired[str],
        "LastAssociationExecutionDate": NotRequired[datetime],
        "LastSuccessfulAssociationExecutionDate": NotRequired[datetime],
        "AssociationOverview": NotRequired["InstanceAggregatedAssociationOverviewTypeDef"],
        "SourceId": NotRequired[str],
        "SourceType": NotRequired[SourceTypeType],
    },
)

InstancePatchStateFilterTypeDef = TypedDict(
    "InstancePatchStateFilterTypeDef",
    {
        "Key": str,
        "Values": Sequence[str],
        "Type": InstancePatchStateOperatorTypeType,
    },
)

InstancePatchStateTypeDef = TypedDict(
    "InstancePatchStateTypeDef",
    {
        "InstanceId": str,
        "PatchGroup": str,
        "BaselineId": str,
        "OperationStartTime": datetime,
        "OperationEndTime": datetime,
        "Operation": PatchOperationTypeType,
        "SnapshotId": NotRequired[str],
        "InstallOverrideList": NotRequired[str],
        "OwnerInformation": NotRequired[str],
        "InstalledCount": NotRequired[int],
        "InstalledOtherCount": NotRequired[int],
        "InstalledPendingRebootCount": NotRequired[int],
        "InstalledRejectedCount": NotRequired[int],
        "MissingCount": NotRequired[int],
        "FailedCount": NotRequired[int],
        "UnreportedNotApplicableCount": NotRequired[int],
        "NotApplicableCount": NotRequired[int],
        "LastNoRebootInstallOperationTime": NotRequired[datetime],
        "RebootOption": NotRequired[RebootOptionType],
        "CriticalNonCompliantCount": NotRequired[int],
        "SecurityNonCompliantCount": NotRequired[int],
        "OtherNonCompliantCount": NotRequired[int],
    },
)

InventoryAggregatorTypeDef = TypedDict(
    "InventoryAggregatorTypeDef",
    {
        "Expression": NotRequired[str],
        "Aggregators": NotRequired[Sequence[Dict[str, Any]]],
        "Groups": NotRequired[Sequence["InventoryGroupTypeDef"]],
    },
)

InventoryDeletionStatusItemTypeDef = TypedDict(
    "InventoryDeletionStatusItemTypeDef",
    {
        "DeletionId": NotRequired[str],
        "TypeName": NotRequired[str],
        "DeletionStartTime": NotRequired[datetime],
        "LastStatus": NotRequired[InventoryDeletionStatusType],
        "LastStatusMessage": NotRequired[str],
        "DeletionSummary": NotRequired["InventoryDeletionSummaryTypeDef"],
        "LastStatusUpdateTime": NotRequired[datetime],
    },
)

InventoryDeletionSummaryItemTypeDef = TypedDict(
    "InventoryDeletionSummaryItemTypeDef",
    {
        "Version": NotRequired[str],
        "Count": NotRequired[int],
        "RemainingCount": NotRequired[int],
    },
)

InventoryDeletionSummaryTypeDef = TypedDict(
    "InventoryDeletionSummaryTypeDef",
    {
        "TotalCount": NotRequired[int],
        "RemainingCount": NotRequired[int],
        "SummaryItems": NotRequired[List["InventoryDeletionSummaryItemTypeDef"]],
    },
)

InventoryFilterTypeDef = TypedDict(
    "InventoryFilterTypeDef",
    {
        "Key": str,
        "Values": Sequence[str],
        "Type": NotRequired[InventoryQueryOperatorTypeType],
    },
)

InventoryGroupTypeDef = TypedDict(
    "InventoryGroupTypeDef",
    {
        "Name": str,
        "Filters": Sequence["InventoryFilterTypeDef"],
    },
)

InventoryItemAttributeTypeDef = TypedDict(
    "InventoryItemAttributeTypeDef",
    {
        "Name": str,
        "DataType": InventoryAttributeDataTypeType,
    },
)

InventoryItemSchemaTypeDef = TypedDict(
    "InventoryItemSchemaTypeDef",
    {
        "TypeName": str,
        "Attributes": List["InventoryItemAttributeTypeDef"],
        "Version": NotRequired[str],
        "DisplayName": NotRequired[str],
    },
)

InventoryItemTypeDef = TypedDict(
    "InventoryItemTypeDef",
    {
        "TypeName": str,
        "SchemaVersion": str,
        "CaptureTime": str,
        "ContentHash": NotRequired[str],
        "Content": NotRequired[Sequence[Mapping[str, str]]],
        "Context": NotRequired[Mapping[str, str]],
    },
)

InventoryResultEntityTypeDef = TypedDict(
    "InventoryResultEntityTypeDef",
    {
        "Id": NotRequired[str],
        "Data": NotRequired[Dict[str, "InventoryResultItemTypeDef"]],
    },
)

InventoryResultItemTypeDef = TypedDict(
    "InventoryResultItemTypeDef",
    {
        "TypeName": str,
        "SchemaVersion": str,
        "Content": List[Dict[str, str]],
        "CaptureTime": NotRequired[str],
        "ContentHash": NotRequired[str],
    },
)

LabelParameterVersionRequestRequestTypeDef = TypedDict(
    "LabelParameterVersionRequestRequestTypeDef",
    {
        "Name": str,
        "Labels": Sequence[str],
        "ParameterVersion": NotRequired[int],
    },
)

LabelParameterVersionResultTypeDef = TypedDict(
    "LabelParameterVersionResultTypeDef",
    {
        "InvalidLabels": List[str],
        "ParameterVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssociationVersionsRequestRequestTypeDef = TypedDict(
    "ListAssociationVersionsRequestRequestTypeDef",
    {
        "AssociationId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAssociationVersionsResultTypeDef = TypedDict(
    "ListAssociationVersionsResultTypeDef",
    {
        "AssociationVersions": List["AssociationVersionInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssociationsRequestRequestTypeDef = TypedDict(
    "ListAssociationsRequestRequestTypeDef",
    {
        "AssociationFilterList": NotRequired[Sequence["AssociationFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAssociationsResultTypeDef = TypedDict(
    "ListAssociationsResultTypeDef",
    {
        "Associations": List["AssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCommandInvocationsRequestRequestTypeDef = TypedDict(
    "ListCommandInvocationsRequestRequestTypeDef",
    {
        "CommandId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence["CommandFilterTypeDef"]],
        "Details": NotRequired[bool],
    },
)

ListCommandInvocationsResultTypeDef = TypedDict(
    "ListCommandInvocationsResultTypeDef",
    {
        "CommandInvocations": List["CommandInvocationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCommandsRequestRequestTypeDef = TypedDict(
    "ListCommandsRequestRequestTypeDef",
    {
        "CommandId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence["CommandFilterTypeDef"]],
    },
)

ListCommandsResultTypeDef = TypedDict(
    "ListCommandsResultTypeDef",
    {
        "Commands": List["CommandTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListComplianceItemsRequestRequestTypeDef = TypedDict(
    "ListComplianceItemsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["ComplianceStringFilterTypeDef"]],
        "ResourceIds": NotRequired[Sequence[str]],
        "ResourceTypes": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListComplianceItemsResultTypeDef = TypedDict(
    "ListComplianceItemsResultTypeDef",
    {
        "ComplianceItems": List["ComplianceItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListComplianceSummariesRequestRequestTypeDef = TypedDict(
    "ListComplianceSummariesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["ComplianceStringFilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListComplianceSummariesResultTypeDef = TypedDict(
    "ListComplianceSummariesResultTypeDef",
    {
        "ComplianceSummaryItems": List["ComplianceSummaryItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDocumentMetadataHistoryRequestRequestTypeDef = TypedDict(
    "ListDocumentMetadataHistoryRequestRequestTypeDef",
    {
        "Name": str,
        "Metadata": Literal["DocumentReviews"],
        "DocumentVersion": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDocumentMetadataHistoryResponseTypeDef = TypedDict(
    "ListDocumentMetadataHistoryResponseTypeDef",
    {
        "Name": str,
        "DocumentVersion": str,
        "Author": str,
        "Metadata": "DocumentMetadataResponseInfoTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDocumentVersionsRequestRequestTypeDef = TypedDict(
    "ListDocumentVersionsRequestRequestTypeDef",
    {
        "Name": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListDocumentVersionsResultTypeDef = TypedDict(
    "ListDocumentVersionsResultTypeDef",
    {
        "DocumentVersions": List["DocumentVersionInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDocumentsRequestRequestTypeDef = TypedDict(
    "ListDocumentsRequestRequestTypeDef",
    {
        "DocumentFilterList": NotRequired[Sequence["DocumentFilterTypeDef"]],
        "Filters": NotRequired[Sequence["DocumentKeyValuesFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListDocumentsResultTypeDef = TypedDict(
    "ListDocumentsResultTypeDef",
    {
        "DocumentIdentifiers": List["DocumentIdentifierTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInventoryEntriesRequestRequestTypeDef = TypedDict(
    "ListInventoryEntriesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "TypeName": str,
        "Filters": NotRequired[Sequence["InventoryFilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListInventoryEntriesResultTypeDef = TypedDict(
    "ListInventoryEntriesResultTypeDef",
    {
        "TypeName": str,
        "InstanceId": str,
        "SchemaVersion": str,
        "CaptureTime": str,
        "Entries": List[Dict[str, str]],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOpsItemEventsRequestRequestTypeDef = TypedDict(
    "ListOpsItemEventsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["OpsItemEventFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListOpsItemEventsResponseTypeDef = TypedDict(
    "ListOpsItemEventsResponseTypeDef",
    {
        "NextToken": str,
        "Summaries": List["OpsItemEventSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOpsItemRelatedItemsRequestRequestTypeDef = TypedDict(
    "ListOpsItemRelatedItemsRequestRequestTypeDef",
    {
        "OpsItemId": NotRequired[str],
        "Filters": NotRequired[Sequence["OpsItemRelatedItemsFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListOpsItemRelatedItemsResponseTypeDef = TypedDict(
    "ListOpsItemRelatedItemsResponseTypeDef",
    {
        "NextToken": str,
        "Summaries": List["OpsItemRelatedItemSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOpsMetadataRequestRequestTypeDef = TypedDict(
    "ListOpsMetadataRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["OpsMetadataFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListOpsMetadataResultTypeDef = TypedDict(
    "ListOpsMetadataResultTypeDef",
    {
        "OpsMetadataList": List["OpsMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceComplianceSummariesRequestRequestTypeDef = TypedDict(
    "ListResourceComplianceSummariesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["ComplianceStringFilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListResourceComplianceSummariesResultTypeDef = TypedDict(
    "ListResourceComplianceSummariesResultTypeDef",
    {
        "ResourceComplianceSummaryItems": List["ResourceComplianceSummaryItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceDataSyncRequestRequestTypeDef = TypedDict(
    "ListResourceDataSyncRequestRequestTypeDef",
    {
        "SyncType": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListResourceDataSyncResultTypeDef = TypedDict(
    "ListResourceDataSyncResultTypeDef",
    {
        "ResourceDataSyncItems": List["ResourceDataSyncItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceType": ResourceTypeForTaggingType,
        "ResourceId": str,
    },
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingInfoTypeDef = TypedDict(
    "LoggingInfoTypeDef",
    {
        "S3BucketName": str,
        "S3Region": str,
        "S3KeyPrefix": NotRequired[str],
    },
)

MaintenanceWindowAutomationParametersTypeDef = TypedDict(
    "MaintenanceWindowAutomationParametersTypeDef",
    {
        "DocumentVersion": NotRequired[str],
        "Parameters": NotRequired[Dict[str, List[str]]],
    },
)

MaintenanceWindowExecutionTaskIdentityTypeDef = TypedDict(
    "MaintenanceWindowExecutionTaskIdentityTypeDef",
    {
        "WindowExecutionId": NotRequired[str],
        "TaskExecutionId": NotRequired[str],
        "Status": NotRequired[MaintenanceWindowExecutionStatusType],
        "StatusDetails": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "TaskArn": NotRequired[str],
        "TaskType": NotRequired[MaintenanceWindowTaskTypeType],
    },
)

MaintenanceWindowExecutionTaskInvocationIdentityTypeDef = TypedDict(
    "MaintenanceWindowExecutionTaskInvocationIdentityTypeDef",
    {
        "WindowExecutionId": NotRequired[str],
        "TaskExecutionId": NotRequired[str],
        "InvocationId": NotRequired[str],
        "ExecutionId": NotRequired[str],
        "TaskType": NotRequired[MaintenanceWindowTaskTypeType],
        "Parameters": NotRequired[str],
        "Status": NotRequired[MaintenanceWindowExecutionStatusType],
        "StatusDetails": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "OwnerInformation": NotRequired[str],
        "WindowTargetId": NotRequired[str],
    },
)

MaintenanceWindowExecutionTypeDef = TypedDict(
    "MaintenanceWindowExecutionTypeDef",
    {
        "WindowId": NotRequired[str],
        "WindowExecutionId": NotRequired[str],
        "Status": NotRequired[MaintenanceWindowExecutionStatusType],
        "StatusDetails": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
    },
)

MaintenanceWindowFilterTypeDef = TypedDict(
    "MaintenanceWindowFilterTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)

MaintenanceWindowIdentityForTargetTypeDef = TypedDict(
    "MaintenanceWindowIdentityForTargetTypeDef",
    {
        "WindowId": NotRequired[str],
        "Name": NotRequired[str],
    },
)

MaintenanceWindowIdentityTypeDef = TypedDict(
    "MaintenanceWindowIdentityTypeDef",
    {
        "WindowId": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Enabled": NotRequired[bool],
        "Duration": NotRequired[int],
        "Cutoff": NotRequired[int],
        "Schedule": NotRequired[str],
        "ScheduleTimezone": NotRequired[str],
        "ScheduleOffset": NotRequired[int],
        "EndDate": NotRequired[str],
        "StartDate": NotRequired[str],
        "NextExecutionTime": NotRequired[str],
    },
)

MaintenanceWindowLambdaParametersTypeDef = TypedDict(
    "MaintenanceWindowLambdaParametersTypeDef",
    {
        "ClientContext": NotRequired[str],
        "Qualifier": NotRequired[str],
        "Payload": NotRequired[bytes],
    },
)

MaintenanceWindowRunCommandParametersTypeDef = TypedDict(
    "MaintenanceWindowRunCommandParametersTypeDef",
    {
        "Comment": NotRequired[str],
        "CloudWatchOutputConfig": NotRequired["CloudWatchOutputConfigTypeDef"],
        "DocumentHash": NotRequired[str],
        "DocumentHashType": NotRequired[DocumentHashTypeType],
        "DocumentVersion": NotRequired[str],
        "NotificationConfig": NotRequired["NotificationConfigTypeDef"],
        "OutputS3BucketName": NotRequired[str],
        "OutputS3KeyPrefix": NotRequired[str],
        "Parameters": NotRequired[Dict[str, List[str]]],
        "ServiceRoleArn": NotRequired[str],
        "TimeoutSeconds": NotRequired[int],
    },
)

MaintenanceWindowStepFunctionsParametersTypeDef = TypedDict(
    "MaintenanceWindowStepFunctionsParametersTypeDef",
    {
        "Input": NotRequired[str],
        "Name": NotRequired[str],
    },
)

MaintenanceWindowTargetTypeDef = TypedDict(
    "MaintenanceWindowTargetTypeDef",
    {
        "WindowId": NotRequired[str],
        "WindowTargetId": NotRequired[str],
        "ResourceType": NotRequired[MaintenanceWindowResourceTypeType],
        "Targets": NotRequired[List["TargetTypeDef"]],
        "OwnerInformation": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)

MaintenanceWindowTaskInvocationParametersTypeDef = TypedDict(
    "MaintenanceWindowTaskInvocationParametersTypeDef",
    {
        "RunCommand": NotRequired["MaintenanceWindowRunCommandParametersTypeDef"],
        "Automation": NotRequired["MaintenanceWindowAutomationParametersTypeDef"],
        "StepFunctions": NotRequired["MaintenanceWindowStepFunctionsParametersTypeDef"],
        "Lambda": NotRequired["MaintenanceWindowLambdaParametersTypeDef"],
    },
)

MaintenanceWindowTaskParameterValueExpressionTypeDef = TypedDict(
    "MaintenanceWindowTaskParameterValueExpressionTypeDef",
    {
        "Values": NotRequired[List[str]],
    },
)

MaintenanceWindowTaskTypeDef = TypedDict(
    "MaintenanceWindowTaskTypeDef",
    {
        "WindowId": NotRequired[str],
        "WindowTaskId": NotRequired[str],
        "TaskArn": NotRequired[str],
        "Type": NotRequired[MaintenanceWindowTaskTypeType],
        "Targets": NotRequired[List["TargetTypeDef"]],
        "TaskParameters": NotRequired[
            Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"]
        ],
        "Priority": NotRequired[int],
        "LoggingInfo": NotRequired["LoggingInfoTypeDef"],
        "ServiceRoleArn": NotRequired[str],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CutoffBehavior": NotRequired[MaintenanceWindowTaskCutoffBehaviorType],
    },
)

MetadataValueTypeDef = TypedDict(
    "MetadataValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)

ModifyDocumentPermissionRequestRequestTypeDef = TypedDict(
    "ModifyDocumentPermissionRequestRequestTypeDef",
    {
        "Name": str,
        "PermissionType": Literal["Share"],
        "AccountIdsToAdd": NotRequired[Sequence[str]],
        "AccountIdsToRemove": NotRequired[Sequence[str]],
        "SharedDocumentVersion": NotRequired[str],
    },
)

NonCompliantSummaryTypeDef = TypedDict(
    "NonCompliantSummaryTypeDef",
    {
        "NonCompliantCount": NotRequired[int],
        "SeveritySummary": NotRequired["SeveritySummaryTypeDef"],
    },
)

NotificationConfigTypeDef = TypedDict(
    "NotificationConfigTypeDef",
    {
        "NotificationArn": NotRequired[str],
        "NotificationEvents": NotRequired[List[NotificationEventType]],
        "NotificationType": NotRequired[NotificationTypeType],
    },
)

OpsAggregatorTypeDef = TypedDict(
    "OpsAggregatorTypeDef",
    {
        "AggregatorType": NotRequired[str],
        "TypeName": NotRequired[str],
        "AttributeName": NotRequired[str],
        "Values": NotRequired[Mapping[str, str]],
        "Filters": NotRequired[Sequence["OpsFilterTypeDef"]],
        "Aggregators": NotRequired[Sequence[Dict[str, Any]]],
    },
)

OpsEntityItemTypeDef = TypedDict(
    "OpsEntityItemTypeDef",
    {
        "CaptureTime": NotRequired[str],
        "Content": NotRequired[List[Dict[str, str]]],
    },
)

OpsEntityTypeDef = TypedDict(
    "OpsEntityTypeDef",
    {
        "Id": NotRequired[str],
        "Data": NotRequired[Dict[str, "OpsEntityItemTypeDef"]],
    },
)

OpsFilterTypeDef = TypedDict(
    "OpsFilterTypeDef",
    {
        "Key": str,
        "Values": Sequence[str],
        "Type": NotRequired[OpsFilterOperatorTypeType],
    },
)

OpsItemDataValueTypeDef = TypedDict(
    "OpsItemDataValueTypeDef",
    {
        "Value": NotRequired[str],
        "Type": NotRequired[OpsItemDataTypeType],
    },
)

OpsItemEventFilterTypeDef = TypedDict(
    "OpsItemEventFilterTypeDef",
    {
        "Key": Literal["OpsItemId"],
        "Values": Sequence[str],
        "Operator": Literal["Equal"],
    },
)

OpsItemEventSummaryTypeDef = TypedDict(
    "OpsItemEventSummaryTypeDef",
    {
        "OpsItemId": NotRequired[str],
        "EventId": NotRequired[str],
        "Source": NotRequired[str],
        "DetailType": NotRequired[str],
        "Detail": NotRequired[str],
        "CreatedBy": NotRequired["OpsItemIdentityTypeDef"],
        "CreatedTime": NotRequired[datetime],
    },
)

OpsItemFilterTypeDef = TypedDict(
    "OpsItemFilterTypeDef",
    {
        "Key": OpsItemFilterKeyType,
        "Values": Sequence[str],
        "Operator": OpsItemFilterOperatorType,
    },
)

OpsItemIdentityTypeDef = TypedDict(
    "OpsItemIdentityTypeDef",
    {
        "Arn": NotRequired[str],
    },
)

OpsItemNotificationTypeDef = TypedDict(
    "OpsItemNotificationTypeDef",
    {
        "Arn": NotRequired[str],
    },
)

OpsItemRelatedItemSummaryTypeDef = TypedDict(
    "OpsItemRelatedItemSummaryTypeDef",
    {
        "OpsItemId": NotRequired[str],
        "AssociationId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "AssociationType": NotRequired[str],
        "ResourceUri": NotRequired[str],
        "CreatedBy": NotRequired["OpsItemIdentityTypeDef"],
        "CreatedTime": NotRequired[datetime],
        "LastModifiedBy": NotRequired["OpsItemIdentityTypeDef"],
        "LastModifiedTime": NotRequired[datetime],
    },
)

OpsItemRelatedItemsFilterTypeDef = TypedDict(
    "OpsItemRelatedItemsFilterTypeDef",
    {
        "Key": OpsItemRelatedItemsFilterKeyType,
        "Values": Sequence[str],
        "Operator": Literal["Equal"],
    },
)

OpsItemSummaryTypeDef = TypedDict(
    "OpsItemSummaryTypeDef",
    {
        "CreatedBy": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedTime": NotRequired[datetime],
        "Priority": NotRequired[int],
        "Source": NotRequired[str],
        "Status": NotRequired[OpsItemStatusType],
        "OpsItemId": NotRequired[str],
        "Title": NotRequired[str],
        "OperationalData": NotRequired[Dict[str, "OpsItemDataValueTypeDef"]],
        "Category": NotRequired[str],
        "Severity": NotRequired[str],
        "OpsItemType": NotRequired[str],
        "ActualStartTime": NotRequired[datetime],
        "ActualEndTime": NotRequired[datetime],
        "PlannedStartTime": NotRequired[datetime],
        "PlannedEndTime": NotRequired[datetime],
    },
)

OpsItemTypeDef = TypedDict(
    "OpsItemTypeDef",
    {
        "CreatedBy": NotRequired[str],
        "OpsItemType": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "Description": NotRequired[str],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedTime": NotRequired[datetime],
        "Notifications": NotRequired[List["OpsItemNotificationTypeDef"]],
        "Priority": NotRequired[int],
        "RelatedOpsItems": NotRequired[List["RelatedOpsItemTypeDef"]],
        "Status": NotRequired[OpsItemStatusType],
        "OpsItemId": NotRequired[str],
        "Version": NotRequired[str],
        "Title": NotRequired[str],
        "Source": NotRequired[str],
        "OperationalData": NotRequired[Dict[str, "OpsItemDataValueTypeDef"]],
        "Category": NotRequired[str],
        "Severity": NotRequired[str],
        "ActualStartTime": NotRequired[datetime],
        "ActualEndTime": NotRequired[datetime],
        "PlannedStartTime": NotRequired[datetime],
        "PlannedEndTime": NotRequired[datetime],
    },
)

OpsMetadataFilterTypeDef = TypedDict(
    "OpsMetadataFilterTypeDef",
    {
        "Key": str,
        "Values": Sequence[str],
    },
)

OpsMetadataTypeDef = TypedDict(
    "OpsMetadataTypeDef",
    {
        "ResourceId": NotRequired[str],
        "OpsMetadataArn": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "LastModifiedUser": NotRequired[str],
        "CreationDate": NotRequired[datetime],
    },
)

OpsResultAttributeTypeDef = TypedDict(
    "OpsResultAttributeTypeDef",
    {
        "TypeName": str,
    },
)

OutputSourceTypeDef = TypedDict(
    "OutputSourceTypeDef",
    {
        "OutputSourceId": NotRequired[str],
        "OutputSourceType": NotRequired[str],
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

ParameterHistoryTypeDef = TypedDict(
    "ParameterHistoryTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[ParameterTypeType],
        "KeyId": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "LastModifiedUser": NotRequired[str],
        "Description": NotRequired[str],
        "Value": NotRequired[str],
        "AllowedPattern": NotRequired[str],
        "Version": NotRequired[int],
        "Labels": NotRequired[List[str]],
        "Tier": NotRequired[ParameterTierType],
        "Policies": NotRequired[List["ParameterInlinePolicyTypeDef"]],
        "DataType": NotRequired[str],
    },
)

ParameterInlinePolicyTypeDef = TypedDict(
    "ParameterInlinePolicyTypeDef",
    {
        "PolicyText": NotRequired[str],
        "PolicyType": NotRequired[str],
        "PolicyStatus": NotRequired[str],
    },
)

ParameterMetadataTypeDef = TypedDict(
    "ParameterMetadataTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[ParameterTypeType],
        "KeyId": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "LastModifiedUser": NotRequired[str],
        "Description": NotRequired[str],
        "AllowedPattern": NotRequired[str],
        "Version": NotRequired[int],
        "Tier": NotRequired[ParameterTierType],
        "Policies": NotRequired[List["ParameterInlinePolicyTypeDef"]],
        "DataType": NotRequired[str],
    },
)

ParameterStringFilterTypeDef = TypedDict(
    "ParameterStringFilterTypeDef",
    {
        "Key": str,
        "Option": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[ParameterTypeType],
        "Value": NotRequired[str],
        "Version": NotRequired[int],
        "Selector": NotRequired[str],
        "SourceResult": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "ARN": NotRequired[str],
        "DataType": NotRequired[str],
    },
)

ParametersFilterTypeDef = TypedDict(
    "ParametersFilterTypeDef",
    {
        "Key": ParametersFilterKeyType,
        "Values": Sequence[str],
    },
)

PatchBaselineIdentityTypeDef = TypedDict(
    "PatchBaselineIdentityTypeDef",
    {
        "BaselineId": NotRequired[str],
        "BaselineName": NotRequired[str],
        "OperatingSystem": NotRequired[OperatingSystemType],
        "BaselineDescription": NotRequired[str],
        "DefaultBaseline": NotRequired[bool],
    },
)

PatchComplianceDataTypeDef = TypedDict(
    "PatchComplianceDataTypeDef",
    {
        "Title": str,
        "KBId": str,
        "Classification": str,
        "Severity": str,
        "State": PatchComplianceDataStateType,
        "InstalledTime": datetime,
        "CVEIds": NotRequired[str],
    },
)

PatchFilterGroupTypeDef = TypedDict(
    "PatchFilterGroupTypeDef",
    {
        "PatchFilters": Sequence["PatchFilterTypeDef"],
    },
)

PatchFilterTypeDef = TypedDict(
    "PatchFilterTypeDef",
    {
        "Key": PatchFilterKeyType,
        "Values": Sequence[str],
    },
)

PatchGroupPatchBaselineMappingTypeDef = TypedDict(
    "PatchGroupPatchBaselineMappingTypeDef",
    {
        "PatchGroup": NotRequired[str],
        "BaselineIdentity": NotRequired["PatchBaselineIdentityTypeDef"],
    },
)

PatchOrchestratorFilterTypeDef = TypedDict(
    "PatchOrchestratorFilterTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)

PatchRuleGroupTypeDef = TypedDict(
    "PatchRuleGroupTypeDef",
    {
        "PatchRules": Sequence["PatchRuleTypeDef"],
    },
)

PatchRuleTypeDef = TypedDict(
    "PatchRuleTypeDef",
    {
        "PatchFilterGroup": "PatchFilterGroupTypeDef",
        "ComplianceLevel": NotRequired[PatchComplianceLevelType],
        "ApproveAfterDays": NotRequired[int],
        "ApproveUntilDate": NotRequired[str],
        "EnableNonSecurity": NotRequired[bool],
    },
)

PatchSourceTypeDef = TypedDict(
    "PatchSourceTypeDef",
    {
        "Name": str,
        "Products": Sequence[str],
        "Configuration": str,
    },
)

PatchStatusTypeDef = TypedDict(
    "PatchStatusTypeDef",
    {
        "DeploymentStatus": NotRequired[PatchDeploymentStatusType],
        "ComplianceLevel": NotRequired[PatchComplianceLevelType],
        "ApprovalDate": NotRequired[datetime],
    },
)

PatchTypeDef = TypedDict(
    "PatchTypeDef",
    {
        "Id": NotRequired[str],
        "ReleaseDate": NotRequired[datetime],
        "Title": NotRequired[str],
        "Description": NotRequired[str],
        "ContentUrl": NotRequired[str],
        "Vendor": NotRequired[str],
        "ProductFamily": NotRequired[str],
        "Product": NotRequired[str],
        "Classification": NotRequired[str],
        "MsrcSeverity": NotRequired[str],
        "KbNumber": NotRequired[str],
        "MsrcNumber": NotRequired[str],
        "Language": NotRequired[str],
        "AdvisoryIds": NotRequired[List[str]],
        "BugzillaIds": NotRequired[List[str]],
        "CVEIds": NotRequired[List[str]],
        "Name": NotRequired[str],
        "Epoch": NotRequired[int],
        "Version": NotRequired[str],
        "Release": NotRequired[str],
        "Arch": NotRequired[str],
        "Severity": NotRequired[str],
        "Repository": NotRequired[str],
    },
)

ProgressCountersTypeDef = TypedDict(
    "ProgressCountersTypeDef",
    {
        "TotalSteps": NotRequired[int],
        "SuccessSteps": NotRequired[int],
        "FailedSteps": NotRequired[int],
        "CancelledSteps": NotRequired[int],
        "TimedOutSteps": NotRequired[int],
    },
)

PutComplianceItemsRequestRequestTypeDef = TypedDict(
    "PutComplianceItemsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "ResourceType": str,
        "ComplianceType": str,
        "ExecutionSummary": "ComplianceExecutionSummaryTypeDef",
        "Items": Sequence["ComplianceItemEntryTypeDef"],
        "ItemContentHash": NotRequired[str],
        "UploadType": NotRequired[ComplianceUploadTypeType],
    },
)

PutInventoryRequestRequestTypeDef = TypedDict(
    "PutInventoryRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Items": Sequence["InventoryItemTypeDef"],
    },
)

PutInventoryResultTypeDef = TypedDict(
    "PutInventoryResultTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutParameterRequestRequestTypeDef = TypedDict(
    "PutParameterRequestRequestTypeDef",
    {
        "Name": str,
        "Value": str,
        "Description": NotRequired[str],
        "Type": NotRequired[ParameterTypeType],
        "KeyId": NotRequired[str],
        "Overwrite": NotRequired[bool],
        "AllowedPattern": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "Tier": NotRequired[ParameterTierType],
        "Policies": NotRequired[str],
        "DataType": NotRequired[str],
    },
)

PutParameterResultTypeDef = TypedDict(
    "PutParameterResultTypeDef",
    {
        "Version": int,
        "Tier": ParameterTierType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterDefaultPatchBaselineRequestRequestTypeDef = TypedDict(
    "RegisterDefaultPatchBaselineRequestRequestTypeDef",
    {
        "BaselineId": str,
    },
)

RegisterDefaultPatchBaselineResultTypeDef = TypedDict(
    "RegisterDefaultPatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterPatchBaselineForPatchGroupRequestRequestTypeDef = TypedDict(
    "RegisterPatchBaselineForPatchGroupRequestRequestTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
    },
)

RegisterPatchBaselineForPatchGroupResultTypeDef = TypedDict(
    "RegisterPatchBaselineForPatchGroupResultTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterTargetWithMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "RegisterTargetWithMaintenanceWindowRequestRequestTypeDef",
    {
        "WindowId": str,
        "ResourceType": MaintenanceWindowResourceTypeType,
        "Targets": Sequence["TargetTypeDef"],
        "OwnerInformation": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)

RegisterTargetWithMaintenanceWindowResultTypeDef = TypedDict(
    "RegisterTargetWithMaintenanceWindowResultTypeDef",
    {
        "WindowTargetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterTaskWithMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "RegisterTaskWithMaintenanceWindowRequestRequestTypeDef",
    {
        "WindowId": str,
        "TaskArn": str,
        "TaskType": MaintenanceWindowTaskTypeType,
        "Targets": NotRequired[Sequence["TargetTypeDef"]],
        "ServiceRoleArn": NotRequired[str],
        "TaskParameters": NotRequired[
            Mapping[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"]
        ],
        "TaskInvocationParameters": NotRequired["MaintenanceWindowTaskInvocationParametersTypeDef"],
        "Priority": NotRequired[int],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "LoggingInfo": NotRequired["LoggingInfoTypeDef"],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
        "CutoffBehavior": NotRequired[MaintenanceWindowTaskCutoffBehaviorType],
    },
)

RegisterTaskWithMaintenanceWindowResultTypeDef = TypedDict(
    "RegisterTaskWithMaintenanceWindowResultTypeDef",
    {
        "WindowTaskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegistrationMetadataItemTypeDef = TypedDict(
    "RegistrationMetadataItemTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

RelatedOpsItemTypeDef = TypedDict(
    "RelatedOpsItemTypeDef",
    {
        "OpsItemId": str,
    },
)

RemoveTagsFromResourceRequestRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceRequestRequestTypeDef",
    {
        "ResourceType": ResourceTypeForTaggingType,
        "ResourceId": str,
        "TagKeys": Sequence[str],
    },
)

ResetServiceSettingRequestRequestTypeDef = TypedDict(
    "ResetServiceSettingRequestRequestTypeDef",
    {
        "SettingId": str,
    },
)

ResetServiceSettingResultTypeDef = TypedDict(
    "ResetServiceSettingResultTypeDef",
    {
        "ServiceSetting": "ServiceSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResolvedTargetsTypeDef = TypedDict(
    "ResolvedTargetsTypeDef",
    {
        "ParameterValues": NotRequired[List[str]],
        "Truncated": NotRequired[bool],
    },
)

ResourceComplianceSummaryItemTypeDef = TypedDict(
    "ResourceComplianceSummaryItemTypeDef",
    {
        "ComplianceType": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
        "Status": NotRequired[ComplianceStatusType],
        "OverallSeverity": NotRequired[ComplianceSeverityType],
        "ExecutionSummary": NotRequired["ComplianceExecutionSummaryTypeDef"],
        "CompliantSummary": NotRequired["CompliantSummaryTypeDef"],
        "NonCompliantSummary": NotRequired["NonCompliantSummaryTypeDef"],
    },
)

ResourceDataSyncAwsOrganizationsSourceTypeDef = TypedDict(
    "ResourceDataSyncAwsOrganizationsSourceTypeDef",
    {
        "OrganizationSourceType": str,
        "OrganizationalUnits": NotRequired[Sequence["ResourceDataSyncOrganizationalUnitTypeDef"]],
    },
)

ResourceDataSyncDestinationDataSharingTypeDef = TypedDict(
    "ResourceDataSyncDestinationDataSharingTypeDef",
    {
        "DestinationDataSharingType": NotRequired[str],
    },
)

ResourceDataSyncItemTypeDef = TypedDict(
    "ResourceDataSyncItemTypeDef",
    {
        "SyncName": NotRequired[str],
        "SyncType": NotRequired[str],
        "SyncSource": NotRequired["ResourceDataSyncSourceWithStateTypeDef"],
        "S3Destination": NotRequired["ResourceDataSyncS3DestinationTypeDef"],
        "LastSyncTime": NotRequired[datetime],
        "LastSuccessfulSyncTime": NotRequired[datetime],
        "SyncLastModifiedTime": NotRequired[datetime],
        "LastStatus": NotRequired[LastResourceDataSyncStatusType],
        "SyncCreatedTime": NotRequired[datetime],
        "LastSyncStatusMessage": NotRequired[str],
    },
)

ResourceDataSyncOrganizationalUnitTypeDef = TypedDict(
    "ResourceDataSyncOrganizationalUnitTypeDef",
    {
        "OrganizationalUnitId": NotRequired[str],
    },
)

ResourceDataSyncS3DestinationTypeDef = TypedDict(
    "ResourceDataSyncS3DestinationTypeDef",
    {
        "BucketName": str,
        "SyncFormat": Literal["JsonSerDe"],
        "Region": str,
        "Prefix": NotRequired[str],
        "AWSKMSKeyARN": NotRequired[str],
        "DestinationDataSharing": NotRequired["ResourceDataSyncDestinationDataSharingTypeDef"],
    },
)

ResourceDataSyncSourceTypeDef = TypedDict(
    "ResourceDataSyncSourceTypeDef",
    {
        "SourceType": str,
        "SourceRegions": Sequence[str],
        "AwsOrganizationsSource": NotRequired["ResourceDataSyncAwsOrganizationsSourceTypeDef"],
        "IncludeFutureRegions": NotRequired[bool],
        "EnableAllOpsDataSources": NotRequired[bool],
    },
)

ResourceDataSyncSourceWithStateTypeDef = TypedDict(
    "ResourceDataSyncSourceWithStateTypeDef",
    {
        "SourceType": NotRequired[str],
        "AwsOrganizationsSource": NotRequired["ResourceDataSyncAwsOrganizationsSourceTypeDef"],
        "SourceRegions": NotRequired[List[str]],
        "IncludeFutureRegions": NotRequired[bool],
        "State": NotRequired[str],
        "EnableAllOpsDataSources": NotRequired[bool],
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

ResultAttributeTypeDef = TypedDict(
    "ResultAttributeTypeDef",
    {
        "TypeName": str,
    },
)

ResumeSessionRequestRequestTypeDef = TypedDict(
    "ResumeSessionRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)

ResumeSessionResponseTypeDef = TypedDict(
    "ResumeSessionResponseTypeDef",
    {
        "SessionId": str,
        "TokenValue": str,
        "StreamUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReviewInformationTypeDef = TypedDict(
    "ReviewInformationTypeDef",
    {
        "ReviewedTime": NotRequired[datetime],
        "Status": NotRequired[ReviewStatusType],
        "Reviewer": NotRequired[str],
    },
)

RunbookTypeDef = TypedDict(
    "RunbookTypeDef",
    {
        "DocumentName": str,
        "DocumentVersion": NotRequired[str],
        "Parameters": NotRequired[Dict[str, List[str]]],
        "TargetParameterName": NotRequired[str],
        "Targets": NotRequired[List["TargetTypeDef"]],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "TargetLocations": NotRequired[List["TargetLocationTypeDef"]],
    },
)

S3OutputLocationTypeDef = TypedDict(
    "S3OutputLocationTypeDef",
    {
        "OutputS3Region": NotRequired[str],
        "OutputS3BucketName": NotRequired[str],
        "OutputS3KeyPrefix": NotRequired[str],
    },
)

S3OutputUrlTypeDef = TypedDict(
    "S3OutputUrlTypeDef",
    {
        "OutputUrl": NotRequired[str],
    },
)

ScheduledWindowExecutionTypeDef = TypedDict(
    "ScheduledWindowExecutionTypeDef",
    {
        "WindowId": NotRequired[str],
        "Name": NotRequired[str],
        "ExecutionTime": NotRequired[str],
    },
)

SendAutomationSignalRequestRequestTypeDef = TypedDict(
    "SendAutomationSignalRequestRequestTypeDef",
    {
        "AutomationExecutionId": str,
        "SignalType": SignalTypeType,
        "Payload": NotRequired[Mapping[str, Sequence[str]]],
    },
)

SendCommandRequestRequestTypeDef = TypedDict(
    "SendCommandRequestRequestTypeDef",
    {
        "DocumentName": str,
        "InstanceIds": NotRequired[Sequence[str]],
        "Targets": NotRequired[Sequence["TargetTypeDef"]],
        "DocumentVersion": NotRequired[str],
        "DocumentHash": NotRequired[str],
        "DocumentHashType": NotRequired[DocumentHashTypeType],
        "TimeoutSeconds": NotRequired[int],
        "Comment": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, Sequence[str]]],
        "OutputS3Region": NotRequired[str],
        "OutputS3BucketName": NotRequired[str],
        "OutputS3KeyPrefix": NotRequired[str],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "ServiceRoleArn": NotRequired[str],
        "NotificationConfig": NotRequired["NotificationConfigTypeDef"],
        "CloudWatchOutputConfig": NotRequired["CloudWatchOutputConfigTypeDef"],
    },
)

SendCommandResultTypeDef = TypedDict(
    "SendCommandResultTypeDef",
    {
        "Command": "CommandTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceSettingTypeDef = TypedDict(
    "ServiceSettingTypeDef",
    {
        "SettingId": NotRequired[str],
        "SettingValue": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "LastModifiedUser": NotRequired[str],
        "ARN": NotRequired[str],
        "Status": NotRequired[str],
    },
)

SessionFilterTypeDef = TypedDict(
    "SessionFilterTypeDef",
    {
        "key": SessionFilterKeyType,
        "value": str,
    },
)

SessionManagerOutputUrlTypeDef = TypedDict(
    "SessionManagerOutputUrlTypeDef",
    {
        "S3OutputUrl": NotRequired[str],
        "CloudWatchOutputUrl": NotRequired[str],
    },
)

SessionTypeDef = TypedDict(
    "SessionTypeDef",
    {
        "SessionId": NotRequired[str],
        "Target": NotRequired[str],
        "Status": NotRequired[SessionStatusType],
        "StartDate": NotRequired[datetime],
        "EndDate": NotRequired[datetime],
        "DocumentName": NotRequired[str],
        "Owner": NotRequired[str],
        "Reason": NotRequired[str],
        "Details": NotRequired[str],
        "OutputUrl": NotRequired["SessionManagerOutputUrlTypeDef"],
        "MaxSessionDuration": NotRequired[str],
    },
)

SeveritySummaryTypeDef = TypedDict(
    "SeveritySummaryTypeDef",
    {
        "CriticalCount": NotRequired[int],
        "HighCount": NotRequired[int],
        "MediumCount": NotRequired[int],
        "LowCount": NotRequired[int],
        "InformationalCount": NotRequired[int],
        "UnspecifiedCount": NotRequired[int],
    },
)

StartAssociationsOnceRequestRequestTypeDef = TypedDict(
    "StartAssociationsOnceRequestRequestTypeDef",
    {
        "AssociationIds": Sequence[str],
    },
)

StartAutomationExecutionRequestRequestTypeDef = TypedDict(
    "StartAutomationExecutionRequestRequestTypeDef",
    {
        "DocumentName": str,
        "DocumentVersion": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, Sequence[str]]],
        "ClientToken": NotRequired[str],
        "Mode": NotRequired[ExecutionModeType],
        "TargetParameterName": NotRequired[str],
        "Targets": NotRequired[Sequence["TargetTypeDef"]],
        "TargetMaps": NotRequired[Sequence[Mapping[str, Sequence[str]]]],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "TargetLocations": NotRequired[Sequence["TargetLocationTypeDef"]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

StartAutomationExecutionResultTypeDef = TypedDict(
    "StartAutomationExecutionResultTypeDef",
    {
        "AutomationExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartChangeRequestExecutionRequestRequestTypeDef = TypedDict(
    "StartChangeRequestExecutionRequestRequestTypeDef",
    {
        "DocumentName": str,
        "Runbooks": Sequence["RunbookTypeDef"],
        "ScheduledTime": NotRequired[Union[datetime, str]],
        "DocumentVersion": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, Sequence[str]]],
        "ChangeRequestName": NotRequired[str],
        "ClientToken": NotRequired[str],
        "AutoApprove": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ScheduledEndTime": NotRequired[Union[datetime, str]],
        "ChangeDetails": NotRequired[str],
    },
)

StartChangeRequestExecutionResultTypeDef = TypedDict(
    "StartChangeRequestExecutionResultTypeDef",
    {
        "AutomationExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartSessionRequestRequestTypeDef = TypedDict(
    "StartSessionRequestRequestTypeDef",
    {
        "Target": str,
        "DocumentName": NotRequired[str],
        "Reason": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, Sequence[str]]],
    },
)

StartSessionResponseTypeDef = TypedDict(
    "StartSessionResponseTypeDef",
    {
        "SessionId": str,
        "TokenValue": str,
        "StreamUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StepExecutionFilterTypeDef = TypedDict(
    "StepExecutionFilterTypeDef",
    {
        "Key": StepExecutionFilterKeyType,
        "Values": Sequence[str],
    },
)

StepExecutionTypeDef = TypedDict(
    "StepExecutionTypeDef",
    {
        "StepName": NotRequired[str],
        "Action": NotRequired[str],
        "TimeoutSeconds": NotRequired[int],
        "OnFailure": NotRequired[str],
        "MaxAttempts": NotRequired[int],
        "ExecutionStartTime": NotRequired[datetime],
        "ExecutionEndTime": NotRequired[datetime],
        "StepStatus": NotRequired[AutomationExecutionStatusType],
        "ResponseCode": NotRequired[str],
        "Inputs": NotRequired[Dict[str, str]],
        "Outputs": NotRequired[Dict[str, List[str]]],
        "Response": NotRequired[str],
        "FailureMessage": NotRequired[str],
        "FailureDetails": NotRequired["FailureDetailsTypeDef"],
        "StepExecutionId": NotRequired[str],
        "OverriddenParameters": NotRequired[Dict[str, List[str]]],
        "IsEnd": NotRequired[bool],
        "NextStep": NotRequired[str],
        "IsCritical": NotRequired[bool],
        "ValidNextSteps": NotRequired[List[str]],
        "Targets": NotRequired[List["TargetTypeDef"]],
        "TargetLocation": NotRequired["TargetLocationTypeDef"],
    },
)

StopAutomationExecutionRequestRequestTypeDef = TypedDict(
    "StopAutomationExecutionRequestRequestTypeDef",
    {
        "AutomationExecutionId": str,
        "Type": NotRequired[StopTypeType],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TargetLocationTypeDef = TypedDict(
    "TargetLocationTypeDef",
    {
        "Accounts": NotRequired[Sequence[str]],
        "Regions": NotRequired[Sequence[str]],
        "TargetLocationMaxConcurrency": NotRequired[str],
        "TargetLocationMaxErrors": NotRequired[str],
        "ExecutionRoleName": NotRequired[str],
    },
)

TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)

TerminateSessionRequestRequestTypeDef = TypedDict(
    "TerminateSessionRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)

TerminateSessionResponseTypeDef = TypedDict(
    "TerminateSessionResponseTypeDef",
    {
        "SessionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UnlabelParameterVersionRequestRequestTypeDef = TypedDict(
    "UnlabelParameterVersionRequestRequestTypeDef",
    {
        "Name": str,
        "ParameterVersion": int,
        "Labels": Sequence[str],
    },
)

UnlabelParameterVersionResultTypeDef = TypedDict(
    "UnlabelParameterVersionResultTypeDef",
    {
        "RemovedLabels": List[str],
        "InvalidLabels": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAssociationRequestRequestTypeDef = TypedDict(
    "UpdateAssociationRequestRequestTypeDef",
    {
        "AssociationId": str,
        "Parameters": NotRequired[Mapping[str, Sequence[str]]],
        "DocumentVersion": NotRequired[str],
        "ScheduleExpression": NotRequired[str],
        "OutputLocation": NotRequired["InstanceAssociationOutputLocationTypeDef"],
        "Name": NotRequired[str],
        "Targets": NotRequired[Sequence["TargetTypeDef"]],
        "AssociationName": NotRequired[str],
        "AssociationVersion": NotRequired[str],
        "AutomationTargetParameterName": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "MaxConcurrency": NotRequired[str],
        "ComplianceSeverity": NotRequired[AssociationComplianceSeverityType],
        "SyncCompliance": NotRequired[AssociationSyncComplianceType],
        "ApplyOnlyAtCronInterval": NotRequired[bool],
        "CalendarNames": NotRequired[Sequence[str]],
        "TargetLocations": NotRequired[Sequence["TargetLocationTypeDef"]],
    },
)

UpdateAssociationResultTypeDef = TypedDict(
    "UpdateAssociationResultTypeDef",
    {
        "AssociationDescription": "AssociationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAssociationStatusRequestRequestTypeDef = TypedDict(
    "UpdateAssociationStatusRequestRequestTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationStatus": "AssociationStatusTypeDef",
    },
)

UpdateAssociationStatusResultTypeDef = TypedDict(
    "UpdateAssociationStatusResultTypeDef",
    {
        "AssociationDescription": "AssociationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDocumentDefaultVersionRequestRequestTypeDef = TypedDict(
    "UpdateDocumentDefaultVersionRequestRequestTypeDef",
    {
        "Name": str,
        "DocumentVersion": str,
    },
)

UpdateDocumentDefaultVersionResultTypeDef = TypedDict(
    "UpdateDocumentDefaultVersionResultTypeDef",
    {
        "Description": "DocumentDefaultVersionDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDocumentMetadataRequestRequestTypeDef = TypedDict(
    "UpdateDocumentMetadataRequestRequestTypeDef",
    {
        "Name": str,
        "DocumentReviews": "DocumentReviewsTypeDef",
        "DocumentVersion": NotRequired[str],
    },
)

UpdateDocumentRequestRequestTypeDef = TypedDict(
    "UpdateDocumentRequestRequestTypeDef",
    {
        "Content": str,
        "Name": str,
        "Attachments": NotRequired[Sequence["AttachmentsSourceTypeDef"]],
        "DisplayName": NotRequired[str],
        "VersionName": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "DocumentFormat": NotRequired[DocumentFormatType],
        "TargetType": NotRequired[str],
    },
)

UpdateDocumentResultTypeDef = TypedDict(
    "UpdateDocumentResultTypeDef",
    {
        "DocumentDescription": "DocumentDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "UpdateMaintenanceWindowRequestRequestTypeDef",
    {
        "WindowId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "StartDate": NotRequired[str],
        "EndDate": NotRequired[str],
        "Schedule": NotRequired[str],
        "ScheduleTimezone": NotRequired[str],
        "ScheduleOffset": NotRequired[int],
        "Duration": NotRequired[int],
        "Cutoff": NotRequired[int],
        "AllowUnassociatedTargets": NotRequired[bool],
        "Enabled": NotRequired[bool],
        "Replace": NotRequired[bool],
    },
)

UpdateMaintenanceWindowResultTypeDef = TypedDict(
    "UpdateMaintenanceWindowResultTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "StartDate": str,
        "EndDate": str,
        "Schedule": str,
        "ScheduleTimezone": str,
        "ScheduleOffset": int,
        "Duration": int,
        "Cutoff": int,
        "AllowUnassociatedTargets": bool,
        "Enabled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMaintenanceWindowTargetRequestRequestTypeDef = TypedDict(
    "UpdateMaintenanceWindowTargetRequestRequestTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "Targets": NotRequired[Sequence["TargetTypeDef"]],
        "OwnerInformation": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Replace": NotRequired[bool],
    },
)

UpdateMaintenanceWindowTargetResultTypeDef = TypedDict(
    "UpdateMaintenanceWindowTargetResultTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "Targets": List["TargetTypeDef"],
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMaintenanceWindowTaskRequestRequestTypeDef = TypedDict(
    "UpdateMaintenanceWindowTaskRequestRequestTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "Targets": NotRequired[Sequence["TargetTypeDef"]],
        "TaskArn": NotRequired[str],
        "ServiceRoleArn": NotRequired[str],
        "TaskParameters": NotRequired[
            Mapping[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"]
        ],
        "TaskInvocationParameters": NotRequired["MaintenanceWindowTaskInvocationParametersTypeDef"],
        "Priority": NotRequired[int],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "LoggingInfo": NotRequired["LoggingInfoTypeDef"],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Replace": NotRequired[bool],
        "CutoffBehavior": NotRequired[MaintenanceWindowTaskCutoffBehaviorType],
    },
)

UpdateMaintenanceWindowTaskResultTypeDef = TypedDict(
    "UpdateMaintenanceWindowTaskResultTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "Targets": List["TargetTypeDef"],
        "TaskArn": str,
        "ServiceRoleArn": str,
        "TaskParameters": Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"],
        "TaskInvocationParameters": "MaintenanceWindowTaskInvocationParametersTypeDef",
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "LoggingInfo": "LoggingInfoTypeDef",
        "Name": str,
        "Description": str,
        "CutoffBehavior": MaintenanceWindowTaskCutoffBehaviorType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateManagedInstanceRoleRequestRequestTypeDef = TypedDict(
    "UpdateManagedInstanceRoleRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IamRole": str,
    },
)

UpdateOpsItemRequestRequestTypeDef = TypedDict(
    "UpdateOpsItemRequestRequestTypeDef",
    {
        "OpsItemId": str,
        "Description": NotRequired[str],
        "OperationalData": NotRequired[Mapping[str, "OpsItemDataValueTypeDef"]],
        "OperationalDataToDelete": NotRequired[Sequence[str]],
        "Notifications": NotRequired[Sequence["OpsItemNotificationTypeDef"]],
        "Priority": NotRequired[int],
        "RelatedOpsItems": NotRequired[Sequence["RelatedOpsItemTypeDef"]],
        "Status": NotRequired[OpsItemStatusType],
        "Title": NotRequired[str],
        "Category": NotRequired[str],
        "Severity": NotRequired[str],
        "ActualStartTime": NotRequired[Union[datetime, str]],
        "ActualEndTime": NotRequired[Union[datetime, str]],
        "PlannedStartTime": NotRequired[Union[datetime, str]],
        "PlannedEndTime": NotRequired[Union[datetime, str]],
    },
)

UpdateOpsMetadataRequestRequestTypeDef = TypedDict(
    "UpdateOpsMetadataRequestRequestTypeDef",
    {
        "OpsMetadataArn": str,
        "MetadataToUpdate": NotRequired[Mapping[str, "MetadataValueTypeDef"]],
        "KeysToDelete": NotRequired[Sequence[str]],
    },
)

UpdateOpsMetadataResultTypeDef = TypedDict(
    "UpdateOpsMetadataResultTypeDef",
    {
        "OpsMetadataArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePatchBaselineRequestRequestTypeDef = TypedDict(
    "UpdatePatchBaselineRequestRequestTypeDef",
    {
        "BaselineId": str,
        "Name": NotRequired[str],
        "GlobalFilters": NotRequired["PatchFilterGroupTypeDef"],
        "ApprovalRules": NotRequired["PatchRuleGroupTypeDef"],
        "ApprovedPatches": NotRequired[Sequence[str]],
        "ApprovedPatchesComplianceLevel": NotRequired[PatchComplianceLevelType],
        "ApprovedPatchesEnableNonSecurity": NotRequired[bool],
        "RejectedPatches": NotRequired[Sequence[str]],
        "RejectedPatchesAction": NotRequired[PatchActionType],
        "Description": NotRequired[str],
        "Sources": NotRequired[Sequence["PatchSourceTypeDef"]],
        "Replace": NotRequired[bool],
    },
)

UpdatePatchBaselineResultTypeDef = TypedDict(
    "UpdatePatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "Name": str,
        "OperatingSystem": OperatingSystemType,
        "GlobalFilters": "PatchFilterGroupTypeDef",
        "ApprovalRules": "PatchRuleGroupTypeDef",
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": PatchComplianceLevelType,
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": PatchActionType,
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
        "Description": str,
        "Sources": List["PatchSourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateResourceDataSyncRequestRequestTypeDef = TypedDict(
    "UpdateResourceDataSyncRequestRequestTypeDef",
    {
        "SyncName": str,
        "SyncType": str,
        "SyncSource": "ResourceDataSyncSourceTypeDef",
    },
)

UpdateServiceSettingRequestRequestTypeDef = TypedDict(
    "UpdateServiceSettingRequestRequestTypeDef",
    {
        "SettingId": str,
        "SettingValue": str,
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
