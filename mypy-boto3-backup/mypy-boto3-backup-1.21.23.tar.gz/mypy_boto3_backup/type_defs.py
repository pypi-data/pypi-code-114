"""
Type annotations for backup service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/type_defs.html)

Usage::

    ```python
    from mypy_boto3_backup.type_defs import AdvancedBackupSettingTypeDef

    data: AdvancedBackupSettingTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    BackupJobStateType,
    BackupVaultEventType,
    CopyJobStateType,
    RecoveryPointStatusType,
    RestoreJobStatusType,
    StorageClassType,
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
    "AdvancedBackupSettingTypeDef",
    "BackupJobTypeDef",
    "BackupPlanInputTypeDef",
    "BackupPlanTemplatesListMemberTypeDef",
    "BackupPlanTypeDef",
    "BackupPlansListMemberTypeDef",
    "BackupRuleInputTypeDef",
    "BackupRuleTypeDef",
    "BackupSelectionTypeDef",
    "BackupSelectionsListMemberTypeDef",
    "BackupVaultListMemberTypeDef",
    "CalculatedLifecycleTypeDef",
    "ConditionParameterTypeDef",
    "ConditionTypeDef",
    "ConditionsTypeDef",
    "ControlInputParameterTypeDef",
    "ControlScopeTypeDef",
    "CopyActionTypeDef",
    "CopyJobTypeDef",
    "CreateBackupPlanInputRequestTypeDef",
    "CreateBackupPlanOutputTypeDef",
    "CreateBackupSelectionInputRequestTypeDef",
    "CreateBackupSelectionOutputTypeDef",
    "CreateBackupVaultInputRequestTypeDef",
    "CreateBackupVaultOutputTypeDef",
    "CreateFrameworkInputRequestTypeDef",
    "CreateFrameworkOutputTypeDef",
    "CreateReportPlanInputRequestTypeDef",
    "CreateReportPlanOutputTypeDef",
    "DeleteBackupPlanInputRequestTypeDef",
    "DeleteBackupPlanOutputTypeDef",
    "DeleteBackupSelectionInputRequestTypeDef",
    "DeleteBackupVaultAccessPolicyInputRequestTypeDef",
    "DeleteBackupVaultInputRequestTypeDef",
    "DeleteBackupVaultLockConfigurationInputRequestTypeDef",
    "DeleteBackupVaultNotificationsInputRequestTypeDef",
    "DeleteFrameworkInputRequestTypeDef",
    "DeleteRecoveryPointInputRequestTypeDef",
    "DeleteReportPlanInputRequestTypeDef",
    "DescribeBackupJobInputRequestTypeDef",
    "DescribeBackupJobOutputTypeDef",
    "DescribeBackupVaultInputRequestTypeDef",
    "DescribeBackupVaultOutputTypeDef",
    "DescribeCopyJobInputRequestTypeDef",
    "DescribeCopyJobOutputTypeDef",
    "DescribeFrameworkInputRequestTypeDef",
    "DescribeFrameworkOutputTypeDef",
    "DescribeGlobalSettingsOutputTypeDef",
    "DescribeProtectedResourceInputRequestTypeDef",
    "DescribeProtectedResourceOutputTypeDef",
    "DescribeRecoveryPointInputRequestTypeDef",
    "DescribeRecoveryPointOutputTypeDef",
    "DescribeRegionSettingsOutputTypeDef",
    "DescribeReportJobInputRequestTypeDef",
    "DescribeReportJobOutputTypeDef",
    "DescribeReportPlanInputRequestTypeDef",
    "DescribeReportPlanOutputTypeDef",
    "DescribeRestoreJobInputRequestTypeDef",
    "DescribeRestoreJobOutputTypeDef",
    "DisassociateRecoveryPointInputRequestTypeDef",
    "ExportBackupPlanTemplateInputRequestTypeDef",
    "ExportBackupPlanTemplateOutputTypeDef",
    "FrameworkControlTypeDef",
    "FrameworkTypeDef",
    "GetBackupPlanFromJSONInputRequestTypeDef",
    "GetBackupPlanFromJSONOutputTypeDef",
    "GetBackupPlanFromTemplateInputRequestTypeDef",
    "GetBackupPlanFromTemplateOutputTypeDef",
    "GetBackupPlanInputRequestTypeDef",
    "GetBackupPlanOutputTypeDef",
    "GetBackupSelectionInputRequestTypeDef",
    "GetBackupSelectionOutputTypeDef",
    "GetBackupVaultAccessPolicyInputRequestTypeDef",
    "GetBackupVaultAccessPolicyOutputTypeDef",
    "GetBackupVaultNotificationsInputRequestTypeDef",
    "GetBackupVaultNotificationsOutputTypeDef",
    "GetRecoveryPointRestoreMetadataInputRequestTypeDef",
    "GetRecoveryPointRestoreMetadataOutputTypeDef",
    "GetSupportedResourceTypesOutputTypeDef",
    "LifecycleTypeDef",
    "ListBackupJobsInputRequestTypeDef",
    "ListBackupJobsOutputTypeDef",
    "ListBackupPlanTemplatesInputRequestTypeDef",
    "ListBackupPlanTemplatesOutputTypeDef",
    "ListBackupPlanVersionsInputRequestTypeDef",
    "ListBackupPlanVersionsOutputTypeDef",
    "ListBackupPlansInputRequestTypeDef",
    "ListBackupPlansOutputTypeDef",
    "ListBackupSelectionsInputRequestTypeDef",
    "ListBackupSelectionsOutputTypeDef",
    "ListBackupVaultsInputRequestTypeDef",
    "ListBackupVaultsOutputTypeDef",
    "ListCopyJobsInputRequestTypeDef",
    "ListCopyJobsOutputTypeDef",
    "ListFrameworksInputRequestTypeDef",
    "ListFrameworksOutputTypeDef",
    "ListProtectedResourcesInputRequestTypeDef",
    "ListProtectedResourcesOutputTypeDef",
    "ListRecoveryPointsByBackupVaultInputRequestTypeDef",
    "ListRecoveryPointsByBackupVaultOutputTypeDef",
    "ListRecoveryPointsByResourceInputRequestTypeDef",
    "ListRecoveryPointsByResourceOutputTypeDef",
    "ListReportJobsInputRequestTypeDef",
    "ListReportJobsOutputTypeDef",
    "ListReportPlansInputRequestTypeDef",
    "ListReportPlansOutputTypeDef",
    "ListRestoreJobsInputRequestTypeDef",
    "ListRestoreJobsOutputTypeDef",
    "ListTagsInputRequestTypeDef",
    "ListTagsOutputTypeDef",
    "ProtectedResourceTypeDef",
    "PutBackupVaultAccessPolicyInputRequestTypeDef",
    "PutBackupVaultLockConfigurationInputRequestTypeDef",
    "PutBackupVaultNotificationsInputRequestTypeDef",
    "RecoveryPointByBackupVaultTypeDef",
    "RecoveryPointByResourceTypeDef",
    "RecoveryPointCreatorTypeDef",
    "ReportDeliveryChannelTypeDef",
    "ReportDestinationTypeDef",
    "ReportJobTypeDef",
    "ReportPlanTypeDef",
    "ReportSettingTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreJobsListMemberTypeDef",
    "StartBackupJobInputRequestTypeDef",
    "StartBackupJobOutputTypeDef",
    "StartCopyJobInputRequestTypeDef",
    "StartCopyJobOutputTypeDef",
    "StartReportJobInputRequestTypeDef",
    "StartReportJobOutputTypeDef",
    "StartRestoreJobInputRequestTypeDef",
    "StartRestoreJobOutputTypeDef",
    "StopBackupJobInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateBackupPlanInputRequestTypeDef",
    "UpdateBackupPlanOutputTypeDef",
    "UpdateFrameworkInputRequestTypeDef",
    "UpdateFrameworkOutputTypeDef",
    "UpdateGlobalSettingsInputRequestTypeDef",
    "UpdateRecoveryPointLifecycleInputRequestTypeDef",
    "UpdateRecoveryPointLifecycleOutputTypeDef",
    "UpdateRegionSettingsInputRequestTypeDef",
    "UpdateReportPlanInputRequestTypeDef",
    "UpdateReportPlanOutputTypeDef",
)

AdvancedBackupSettingTypeDef = TypedDict(
    "AdvancedBackupSettingTypeDef",
    {
        "ResourceType": NotRequired[str],
        "BackupOptions": NotRequired[Mapping[str, str]],
    },
)

BackupJobTypeDef = TypedDict(
    "BackupJobTypeDef",
    {
        "AccountId": NotRequired[str],
        "BackupJobId": NotRequired[str],
        "BackupVaultName": NotRequired[str],
        "BackupVaultArn": NotRequired[str],
        "RecoveryPointArn": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "CompletionDate": NotRequired[datetime],
        "State": NotRequired[BackupJobStateType],
        "StatusMessage": NotRequired[str],
        "PercentDone": NotRequired[str],
        "BackupSizeInBytes": NotRequired[int],
        "IamRoleArn": NotRequired[str],
        "CreatedBy": NotRequired["RecoveryPointCreatorTypeDef"],
        "ExpectedCompletionDate": NotRequired[datetime],
        "StartBy": NotRequired[datetime],
        "ResourceType": NotRequired[str],
        "BytesTransferred": NotRequired[int],
        "BackupOptions": NotRequired[Dict[str, str]],
        "BackupType": NotRequired[str],
    },
)

BackupPlanInputTypeDef = TypedDict(
    "BackupPlanInputTypeDef",
    {
        "BackupPlanName": str,
        "Rules": Sequence["BackupRuleInputTypeDef"],
        "AdvancedBackupSettings": NotRequired[Sequence["AdvancedBackupSettingTypeDef"]],
    },
)

BackupPlanTemplatesListMemberTypeDef = TypedDict(
    "BackupPlanTemplatesListMemberTypeDef",
    {
        "BackupPlanTemplateId": NotRequired[str],
        "BackupPlanTemplateName": NotRequired[str],
    },
)

BackupPlanTypeDef = TypedDict(
    "BackupPlanTypeDef",
    {
        "BackupPlanName": str,
        "Rules": List["BackupRuleTypeDef"],
        "AdvancedBackupSettings": NotRequired[List["AdvancedBackupSettingTypeDef"]],
    },
)

BackupPlansListMemberTypeDef = TypedDict(
    "BackupPlansListMemberTypeDef",
    {
        "BackupPlanArn": NotRequired[str],
        "BackupPlanId": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "DeletionDate": NotRequired[datetime],
        "VersionId": NotRequired[str],
        "BackupPlanName": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "LastExecutionDate": NotRequired[datetime],
        "AdvancedBackupSettings": NotRequired[List["AdvancedBackupSettingTypeDef"]],
    },
)

BackupRuleInputTypeDef = TypedDict(
    "BackupRuleInputTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
        "ScheduleExpression": NotRequired[str],
        "StartWindowMinutes": NotRequired[int],
        "CompletionWindowMinutes": NotRequired[int],
        "Lifecycle": NotRequired["LifecycleTypeDef"],
        "RecoveryPointTags": NotRequired[Mapping[str, str]],
        "CopyActions": NotRequired[Sequence["CopyActionTypeDef"]],
        "EnableContinuousBackup": NotRequired[bool],
    },
)

BackupRuleTypeDef = TypedDict(
    "BackupRuleTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
        "ScheduleExpression": NotRequired[str],
        "StartWindowMinutes": NotRequired[int],
        "CompletionWindowMinutes": NotRequired[int],
        "Lifecycle": NotRequired["LifecycleTypeDef"],
        "RecoveryPointTags": NotRequired[Dict[str, str]],
        "RuleId": NotRequired[str],
        "CopyActions": NotRequired[List["CopyActionTypeDef"]],
        "EnableContinuousBackup": NotRequired[bool],
    },
)

BackupSelectionTypeDef = TypedDict(
    "BackupSelectionTypeDef",
    {
        "SelectionName": str,
        "IamRoleArn": str,
        "Resources": NotRequired[Sequence[str]],
        "ListOfTags": NotRequired[Sequence["ConditionTypeDef"]],
        "NotResources": NotRequired[Sequence[str]],
        "Conditions": NotRequired["ConditionsTypeDef"],
    },
)

BackupSelectionsListMemberTypeDef = TypedDict(
    "BackupSelectionsListMemberTypeDef",
    {
        "SelectionId": NotRequired[str],
        "SelectionName": NotRequired[str],
        "BackupPlanId": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "CreatorRequestId": NotRequired[str],
        "IamRoleArn": NotRequired[str],
    },
)

BackupVaultListMemberTypeDef = TypedDict(
    "BackupVaultListMemberTypeDef",
    {
        "BackupVaultName": NotRequired[str],
        "BackupVaultArn": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "EncryptionKeyArn": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "NumberOfRecoveryPoints": NotRequired[int],
        "Locked": NotRequired[bool],
        "MinRetentionDays": NotRequired[int],
        "MaxRetentionDays": NotRequired[int],
        "LockDate": NotRequired[datetime],
    },
)

CalculatedLifecycleTypeDef = TypedDict(
    "CalculatedLifecycleTypeDef",
    {
        "MoveToColdStorageAt": NotRequired[datetime],
        "DeleteAt": NotRequired[datetime],
    },
)

ConditionParameterTypeDef = TypedDict(
    "ConditionParameterTypeDef",
    {
        "ConditionKey": NotRequired[str],
        "ConditionValue": NotRequired[str],
    },
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "ConditionType": Literal["STRINGEQUALS"],
        "ConditionKey": str,
        "ConditionValue": str,
    },
)

ConditionsTypeDef = TypedDict(
    "ConditionsTypeDef",
    {
        "StringEquals": NotRequired[Sequence["ConditionParameterTypeDef"]],
        "StringNotEquals": NotRequired[Sequence["ConditionParameterTypeDef"]],
        "StringLike": NotRequired[Sequence["ConditionParameterTypeDef"]],
        "StringNotLike": NotRequired[Sequence["ConditionParameterTypeDef"]],
    },
)

ControlInputParameterTypeDef = TypedDict(
    "ControlInputParameterTypeDef",
    {
        "ParameterName": NotRequired[str],
        "ParameterValue": NotRequired[str],
    },
)

ControlScopeTypeDef = TypedDict(
    "ControlScopeTypeDef",
    {
        "ComplianceResourceIds": NotRequired[Sequence[str]],
        "ComplianceResourceTypes": NotRequired[Sequence[str]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CopyActionTypeDef = TypedDict(
    "CopyActionTypeDef",
    {
        "DestinationBackupVaultArn": str,
        "Lifecycle": NotRequired["LifecycleTypeDef"],
    },
)

CopyJobTypeDef = TypedDict(
    "CopyJobTypeDef",
    {
        "AccountId": NotRequired[str],
        "CopyJobId": NotRequired[str],
        "SourceBackupVaultArn": NotRequired[str],
        "SourceRecoveryPointArn": NotRequired[str],
        "DestinationBackupVaultArn": NotRequired[str],
        "DestinationRecoveryPointArn": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "CompletionDate": NotRequired[datetime],
        "State": NotRequired[CopyJobStateType],
        "StatusMessage": NotRequired[str],
        "BackupSizeInBytes": NotRequired[int],
        "IamRoleArn": NotRequired[str],
        "CreatedBy": NotRequired["RecoveryPointCreatorTypeDef"],
        "ResourceType": NotRequired[str],
    },
)

CreateBackupPlanInputRequestTypeDef = TypedDict(
    "CreateBackupPlanInputRequestTypeDef",
    {
        "BackupPlan": "BackupPlanInputTypeDef",
        "BackupPlanTags": NotRequired[Mapping[str, str]],
        "CreatorRequestId": NotRequired[str],
    },
)

CreateBackupPlanOutputTypeDef = TypedDict(
    "CreateBackupPlanOutputTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "CreationDate": datetime,
        "VersionId": str,
        "AdvancedBackupSettings": List["AdvancedBackupSettingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBackupSelectionInputRequestTypeDef = TypedDict(
    "CreateBackupSelectionInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "BackupSelection": "BackupSelectionTypeDef",
        "CreatorRequestId": NotRequired[str],
    },
)

CreateBackupSelectionOutputTypeDef = TypedDict(
    "CreateBackupSelectionOutputTypeDef",
    {
        "SelectionId": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBackupVaultInputRequestTypeDef = TypedDict(
    "CreateBackupVaultInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultTags": NotRequired[Mapping[str, str]],
        "EncryptionKeyArn": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
    },
)

CreateBackupVaultOutputTypeDef = TypedDict(
    "CreateBackupVaultOutputTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "CreationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFrameworkInputRequestTypeDef = TypedDict(
    "CreateFrameworkInputRequestTypeDef",
    {
        "FrameworkName": str,
        "FrameworkControls": Sequence["FrameworkControlTypeDef"],
        "FrameworkDescription": NotRequired[str],
        "IdempotencyToken": NotRequired[str],
        "FrameworkTags": NotRequired[Mapping[str, str]],
    },
)

CreateFrameworkOutputTypeDef = TypedDict(
    "CreateFrameworkOutputTypeDef",
    {
        "FrameworkName": str,
        "FrameworkArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateReportPlanInputRequestTypeDef = TypedDict(
    "CreateReportPlanInputRequestTypeDef",
    {
        "ReportPlanName": str,
        "ReportDeliveryChannel": "ReportDeliveryChannelTypeDef",
        "ReportSetting": "ReportSettingTypeDef",
        "ReportPlanDescription": NotRequired[str],
        "ReportPlanTags": NotRequired[Mapping[str, str]],
        "IdempotencyToken": NotRequired[str],
    },
)

CreateReportPlanOutputTypeDef = TypedDict(
    "CreateReportPlanOutputTypeDef",
    {
        "ReportPlanName": str,
        "ReportPlanArn": str,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackupPlanInputRequestTypeDef = TypedDict(
    "DeleteBackupPlanInputRequestTypeDef",
    {
        "BackupPlanId": str,
    },
)

DeleteBackupPlanOutputTypeDef = TypedDict(
    "DeleteBackupPlanOutputTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "DeletionDate": datetime,
        "VersionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackupSelectionInputRequestTypeDef = TypedDict(
    "DeleteBackupSelectionInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "SelectionId": str,
    },
)

DeleteBackupVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "DeleteBackupVaultAccessPolicyInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)

DeleteBackupVaultInputRequestTypeDef = TypedDict(
    "DeleteBackupVaultInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)

DeleteBackupVaultLockConfigurationInputRequestTypeDef = TypedDict(
    "DeleteBackupVaultLockConfigurationInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)

DeleteBackupVaultNotificationsInputRequestTypeDef = TypedDict(
    "DeleteBackupVaultNotificationsInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)

DeleteFrameworkInputRequestTypeDef = TypedDict(
    "DeleteFrameworkInputRequestTypeDef",
    {
        "FrameworkName": str,
    },
)

DeleteRecoveryPointInputRequestTypeDef = TypedDict(
    "DeleteRecoveryPointInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)

DeleteReportPlanInputRequestTypeDef = TypedDict(
    "DeleteReportPlanInputRequestTypeDef",
    {
        "ReportPlanName": str,
    },
)

DescribeBackupJobInputRequestTypeDef = TypedDict(
    "DescribeBackupJobInputRequestTypeDef",
    {
        "BackupJobId": str,
    },
)

DescribeBackupJobOutputTypeDef = TypedDict(
    "DescribeBackupJobOutputTypeDef",
    {
        "AccountId": str,
        "BackupJobId": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "ResourceArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "State": BackupJobStateType,
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": "RecoveryPointCreatorTypeDef",
        "ResourceType": str,
        "BytesTransferred": int,
        "ExpectedCompletionDate": datetime,
        "StartBy": datetime,
        "BackupOptions": Dict[str, str],
        "BackupType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBackupVaultInputRequestTypeDef = TypedDict(
    "DescribeBackupVaultInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)

DescribeBackupVaultOutputTypeDef = TypedDict(
    "DescribeBackupVaultOutputTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "EncryptionKeyArn": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
        "NumberOfRecoveryPoints": int,
        "Locked": bool,
        "MinRetentionDays": int,
        "MaxRetentionDays": int,
        "LockDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCopyJobInputRequestTypeDef = TypedDict(
    "DescribeCopyJobInputRequestTypeDef",
    {
        "CopyJobId": str,
    },
)

DescribeCopyJobOutputTypeDef = TypedDict(
    "DescribeCopyJobOutputTypeDef",
    {
        "CopyJob": "CopyJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFrameworkInputRequestTypeDef = TypedDict(
    "DescribeFrameworkInputRequestTypeDef",
    {
        "FrameworkName": str,
    },
)

DescribeFrameworkOutputTypeDef = TypedDict(
    "DescribeFrameworkOutputTypeDef",
    {
        "FrameworkName": str,
        "FrameworkArn": str,
        "FrameworkDescription": str,
        "FrameworkControls": List["FrameworkControlTypeDef"],
        "CreationTime": datetime,
        "DeploymentStatus": str,
        "FrameworkStatus": str,
        "IdempotencyToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGlobalSettingsOutputTypeDef = TypedDict(
    "DescribeGlobalSettingsOutputTypeDef",
    {
        "GlobalSettings": Dict[str, str],
        "LastUpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProtectedResourceInputRequestTypeDef = TypedDict(
    "DescribeProtectedResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeProtectedResourceOutputTypeDef = TypedDict(
    "DescribeProtectedResourceOutputTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": str,
        "LastBackupTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRecoveryPointInputRequestTypeDef = TypedDict(
    "DescribeRecoveryPointInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)

DescribeRecoveryPointOutputTypeDef = TypedDict(
    "DescribeRecoveryPointOutputTypeDef",
    {
        "RecoveryPointArn": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "SourceBackupVaultArn": str,
        "ResourceArn": str,
        "ResourceType": str,
        "CreatedBy": "RecoveryPointCreatorTypeDef",
        "IamRoleArn": str,
        "Status": RecoveryPointStatusType,
        "StatusMessage": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "BackupSizeInBytes": int,
        "CalculatedLifecycle": "CalculatedLifecycleTypeDef",
        "Lifecycle": "LifecycleTypeDef",
        "EncryptionKeyArn": str,
        "IsEncrypted": bool,
        "StorageClass": StorageClassType,
        "LastRestoreTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRegionSettingsOutputTypeDef = TypedDict(
    "DescribeRegionSettingsOutputTypeDef",
    {
        "ResourceTypeOptInPreference": Dict[str, bool],
        "ResourceTypeManagementPreference": Dict[str, bool],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReportJobInputRequestTypeDef = TypedDict(
    "DescribeReportJobInputRequestTypeDef",
    {
        "ReportJobId": str,
    },
)

DescribeReportJobOutputTypeDef = TypedDict(
    "DescribeReportJobOutputTypeDef",
    {
        "ReportJob": "ReportJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReportPlanInputRequestTypeDef = TypedDict(
    "DescribeReportPlanInputRequestTypeDef",
    {
        "ReportPlanName": str,
    },
)

DescribeReportPlanOutputTypeDef = TypedDict(
    "DescribeReportPlanOutputTypeDef",
    {
        "ReportPlan": "ReportPlanTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRestoreJobInputRequestTypeDef = TypedDict(
    "DescribeRestoreJobInputRequestTypeDef",
    {
        "RestoreJobId": str,
    },
)

DescribeRestoreJobOutputTypeDef = TypedDict(
    "DescribeRestoreJobOutputTypeDef",
    {
        "AccountId": str,
        "RestoreJobId": str,
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "Status": RestoreJobStatusType,
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "ExpectedCompletionTimeMinutes": int,
        "CreatedResourceArn": str,
        "ResourceType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateRecoveryPointInputRequestTypeDef = TypedDict(
    "DisassociateRecoveryPointInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)

ExportBackupPlanTemplateInputRequestTypeDef = TypedDict(
    "ExportBackupPlanTemplateInputRequestTypeDef",
    {
        "BackupPlanId": str,
    },
)

ExportBackupPlanTemplateOutputTypeDef = TypedDict(
    "ExportBackupPlanTemplateOutputTypeDef",
    {
        "BackupPlanTemplateJson": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FrameworkControlTypeDef = TypedDict(
    "FrameworkControlTypeDef",
    {
        "ControlName": str,
        "ControlInputParameters": NotRequired[Sequence["ControlInputParameterTypeDef"]],
        "ControlScope": NotRequired["ControlScopeTypeDef"],
    },
)

FrameworkTypeDef = TypedDict(
    "FrameworkTypeDef",
    {
        "FrameworkName": NotRequired[str],
        "FrameworkArn": NotRequired[str],
        "FrameworkDescription": NotRequired[str],
        "NumberOfControls": NotRequired[int],
        "CreationTime": NotRequired[datetime],
        "DeploymentStatus": NotRequired[str],
    },
)

GetBackupPlanFromJSONInputRequestTypeDef = TypedDict(
    "GetBackupPlanFromJSONInputRequestTypeDef",
    {
        "BackupPlanTemplateJson": str,
    },
)

GetBackupPlanFromJSONOutputTypeDef = TypedDict(
    "GetBackupPlanFromJSONOutputTypeDef",
    {
        "BackupPlan": "BackupPlanTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackupPlanFromTemplateInputRequestTypeDef = TypedDict(
    "GetBackupPlanFromTemplateInputRequestTypeDef",
    {
        "BackupPlanTemplateId": str,
    },
)

GetBackupPlanFromTemplateOutputTypeDef = TypedDict(
    "GetBackupPlanFromTemplateOutputTypeDef",
    {
        "BackupPlanDocument": "BackupPlanTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackupPlanInputRequestTypeDef = TypedDict(
    "GetBackupPlanInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "VersionId": NotRequired[str],
    },
)

GetBackupPlanOutputTypeDef = TypedDict(
    "GetBackupPlanOutputTypeDef",
    {
        "BackupPlan": "BackupPlanTypeDef",
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "VersionId": str,
        "CreatorRequestId": str,
        "CreationDate": datetime,
        "DeletionDate": datetime,
        "LastExecutionDate": datetime,
        "AdvancedBackupSettings": List["AdvancedBackupSettingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackupSelectionInputRequestTypeDef = TypedDict(
    "GetBackupSelectionInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "SelectionId": str,
    },
)

GetBackupSelectionOutputTypeDef = TypedDict(
    "GetBackupSelectionOutputTypeDef",
    {
        "BackupSelection": "BackupSelectionTypeDef",
        "SelectionId": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackupVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "GetBackupVaultAccessPolicyInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)

GetBackupVaultAccessPolicyOutputTypeDef = TypedDict(
    "GetBackupVaultAccessPolicyOutputTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackupVaultNotificationsInputRequestTypeDef = TypedDict(
    "GetBackupVaultNotificationsInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)

GetBackupVaultNotificationsOutputTypeDef = TypedDict(
    "GetBackupVaultNotificationsOutputTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "SNSTopicArn": str,
        "BackupVaultEvents": List[BackupVaultEventType],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecoveryPointRestoreMetadataInputRequestTypeDef = TypedDict(
    "GetRecoveryPointRestoreMetadataInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)

GetRecoveryPointRestoreMetadataOutputTypeDef = TypedDict(
    "GetRecoveryPointRestoreMetadataOutputTypeDef",
    {
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "RestoreMetadata": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSupportedResourceTypesOutputTypeDef = TypedDict(
    "GetSupportedResourceTypesOutputTypeDef",
    {
        "ResourceTypes": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LifecycleTypeDef = TypedDict(
    "LifecycleTypeDef",
    {
        "MoveToColdStorageAfterDays": NotRequired[int],
        "DeleteAfterDays": NotRequired[int],
    },
)

ListBackupJobsInputRequestTypeDef = TypedDict(
    "ListBackupJobsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ByResourceArn": NotRequired[str],
        "ByState": NotRequired[BackupJobStateType],
        "ByBackupVaultName": NotRequired[str],
        "ByCreatedBefore": NotRequired[Union[datetime, str]],
        "ByCreatedAfter": NotRequired[Union[datetime, str]],
        "ByResourceType": NotRequired[str],
        "ByAccountId": NotRequired[str],
    },
)

ListBackupJobsOutputTypeDef = TypedDict(
    "ListBackupJobsOutputTypeDef",
    {
        "BackupJobs": List["BackupJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBackupPlanTemplatesInputRequestTypeDef = TypedDict(
    "ListBackupPlanTemplatesInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListBackupPlanTemplatesOutputTypeDef = TypedDict(
    "ListBackupPlanTemplatesOutputTypeDef",
    {
        "NextToken": str,
        "BackupPlanTemplatesList": List["BackupPlanTemplatesListMemberTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBackupPlanVersionsInputRequestTypeDef = TypedDict(
    "ListBackupPlanVersionsInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListBackupPlanVersionsOutputTypeDef = TypedDict(
    "ListBackupPlanVersionsOutputTypeDef",
    {
        "NextToken": str,
        "BackupPlanVersionsList": List["BackupPlansListMemberTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBackupPlansInputRequestTypeDef = TypedDict(
    "ListBackupPlansInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "IncludeDeleted": NotRequired[bool],
    },
)

ListBackupPlansOutputTypeDef = TypedDict(
    "ListBackupPlansOutputTypeDef",
    {
        "NextToken": str,
        "BackupPlansList": List["BackupPlansListMemberTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBackupSelectionsInputRequestTypeDef = TypedDict(
    "ListBackupSelectionsInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListBackupSelectionsOutputTypeDef = TypedDict(
    "ListBackupSelectionsOutputTypeDef",
    {
        "NextToken": str,
        "BackupSelectionsList": List["BackupSelectionsListMemberTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBackupVaultsInputRequestTypeDef = TypedDict(
    "ListBackupVaultsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListBackupVaultsOutputTypeDef = TypedDict(
    "ListBackupVaultsOutputTypeDef",
    {
        "BackupVaultList": List["BackupVaultListMemberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCopyJobsInputRequestTypeDef = TypedDict(
    "ListCopyJobsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ByResourceArn": NotRequired[str],
        "ByState": NotRequired[CopyJobStateType],
        "ByCreatedBefore": NotRequired[Union[datetime, str]],
        "ByCreatedAfter": NotRequired[Union[datetime, str]],
        "ByResourceType": NotRequired[str],
        "ByDestinationVaultArn": NotRequired[str],
        "ByAccountId": NotRequired[str],
    },
)

ListCopyJobsOutputTypeDef = TypedDict(
    "ListCopyJobsOutputTypeDef",
    {
        "CopyJobs": List["CopyJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFrameworksInputRequestTypeDef = TypedDict(
    "ListFrameworksInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListFrameworksOutputTypeDef = TypedDict(
    "ListFrameworksOutputTypeDef",
    {
        "Frameworks": List["FrameworkTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProtectedResourcesInputRequestTypeDef = TypedDict(
    "ListProtectedResourcesInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListProtectedResourcesOutputTypeDef = TypedDict(
    "ListProtectedResourcesOutputTypeDef",
    {
        "Results": List["ProtectedResourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecoveryPointsByBackupVaultInputRequestTypeDef = TypedDict(
    "ListRecoveryPointsByBackupVaultInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ByResourceArn": NotRequired[str],
        "ByResourceType": NotRequired[str],
        "ByBackupPlanId": NotRequired[str],
        "ByCreatedBefore": NotRequired[Union[datetime, str]],
        "ByCreatedAfter": NotRequired[Union[datetime, str]],
    },
)

ListRecoveryPointsByBackupVaultOutputTypeDef = TypedDict(
    "ListRecoveryPointsByBackupVaultOutputTypeDef",
    {
        "NextToken": str,
        "RecoveryPoints": List["RecoveryPointByBackupVaultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecoveryPointsByResourceInputRequestTypeDef = TypedDict(
    "ListRecoveryPointsByResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListRecoveryPointsByResourceOutputTypeDef = TypedDict(
    "ListRecoveryPointsByResourceOutputTypeDef",
    {
        "NextToken": str,
        "RecoveryPoints": List["RecoveryPointByResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReportJobsInputRequestTypeDef = TypedDict(
    "ListReportJobsInputRequestTypeDef",
    {
        "ByReportPlanName": NotRequired[str],
        "ByCreationBefore": NotRequired[Union[datetime, str]],
        "ByCreationAfter": NotRequired[Union[datetime, str]],
        "ByStatus": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListReportJobsOutputTypeDef = TypedDict(
    "ListReportJobsOutputTypeDef",
    {
        "ReportJobs": List["ReportJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReportPlansInputRequestTypeDef = TypedDict(
    "ListReportPlansInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListReportPlansOutputTypeDef = TypedDict(
    "ListReportPlansOutputTypeDef",
    {
        "ReportPlans": List["ReportPlanTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRestoreJobsInputRequestTypeDef = TypedDict(
    "ListRestoreJobsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ByAccountId": NotRequired[str],
        "ByCreatedBefore": NotRequired[Union[datetime, str]],
        "ByCreatedAfter": NotRequired[Union[datetime, str]],
        "ByStatus": NotRequired[RestoreJobStatusType],
    },
)

ListRestoreJobsOutputTypeDef = TypedDict(
    "ListRestoreJobsOutputTypeDef",
    {
        "RestoreJobs": List["RestoreJobsListMemberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsInputRequestTypeDef = TypedDict(
    "ListTagsInputRequestTypeDef",
    {
        "ResourceArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTagsOutputTypeDef = TypedDict(
    "ListTagsOutputTypeDef",
    {
        "NextToken": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ProtectedResourceTypeDef = TypedDict(
    "ProtectedResourceTypeDef",
    {
        "ResourceArn": NotRequired[str],
        "ResourceType": NotRequired[str],
        "LastBackupTime": NotRequired[datetime],
    },
)

PutBackupVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "PutBackupVaultAccessPolicyInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "Policy": NotRequired[str],
    },
)

PutBackupVaultLockConfigurationInputRequestTypeDef = TypedDict(
    "PutBackupVaultLockConfigurationInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "MinRetentionDays": NotRequired[int],
        "MaxRetentionDays": NotRequired[int],
        "ChangeableForDays": NotRequired[int],
    },
)

PutBackupVaultNotificationsInputRequestTypeDef = TypedDict(
    "PutBackupVaultNotificationsInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "SNSTopicArn": str,
        "BackupVaultEvents": Sequence[BackupVaultEventType],
    },
)

RecoveryPointByBackupVaultTypeDef = TypedDict(
    "RecoveryPointByBackupVaultTypeDef",
    {
        "RecoveryPointArn": NotRequired[str],
        "BackupVaultName": NotRequired[str],
        "BackupVaultArn": NotRequired[str],
        "SourceBackupVaultArn": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "ResourceType": NotRequired[str],
        "CreatedBy": NotRequired["RecoveryPointCreatorTypeDef"],
        "IamRoleArn": NotRequired[str],
        "Status": NotRequired[RecoveryPointStatusType],
        "StatusMessage": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "CompletionDate": NotRequired[datetime],
        "BackupSizeInBytes": NotRequired[int],
        "CalculatedLifecycle": NotRequired["CalculatedLifecycleTypeDef"],
        "Lifecycle": NotRequired["LifecycleTypeDef"],
        "EncryptionKeyArn": NotRequired[str],
        "IsEncrypted": NotRequired[bool],
        "LastRestoreTime": NotRequired[datetime],
    },
)

RecoveryPointByResourceTypeDef = TypedDict(
    "RecoveryPointByResourceTypeDef",
    {
        "RecoveryPointArn": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "Status": NotRequired[RecoveryPointStatusType],
        "StatusMessage": NotRequired[str],
        "EncryptionKeyArn": NotRequired[str],
        "BackupSizeBytes": NotRequired[int],
        "BackupVaultName": NotRequired[str],
    },
)

RecoveryPointCreatorTypeDef = TypedDict(
    "RecoveryPointCreatorTypeDef",
    {
        "BackupPlanId": NotRequired[str],
        "BackupPlanArn": NotRequired[str],
        "BackupPlanVersion": NotRequired[str],
        "BackupRuleId": NotRequired[str],
    },
)

ReportDeliveryChannelTypeDef = TypedDict(
    "ReportDeliveryChannelTypeDef",
    {
        "S3BucketName": str,
        "S3KeyPrefix": NotRequired[str],
        "Formats": NotRequired[Sequence[str]],
    },
)

ReportDestinationTypeDef = TypedDict(
    "ReportDestinationTypeDef",
    {
        "S3BucketName": NotRequired[str],
        "S3Keys": NotRequired[List[str]],
    },
)

ReportJobTypeDef = TypedDict(
    "ReportJobTypeDef",
    {
        "ReportJobId": NotRequired[str],
        "ReportPlanArn": NotRequired[str],
        "ReportTemplate": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "CompletionTime": NotRequired[datetime],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "ReportDestination": NotRequired["ReportDestinationTypeDef"],
    },
)

ReportPlanTypeDef = TypedDict(
    "ReportPlanTypeDef",
    {
        "ReportPlanArn": NotRequired[str],
        "ReportPlanName": NotRequired[str],
        "ReportPlanDescription": NotRequired[str],
        "ReportSetting": NotRequired["ReportSettingTypeDef"],
        "ReportDeliveryChannel": NotRequired["ReportDeliveryChannelTypeDef"],
        "DeploymentStatus": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastAttemptedExecutionTime": NotRequired[datetime],
        "LastSuccessfulExecutionTime": NotRequired[datetime],
    },
)

ReportSettingTypeDef = TypedDict(
    "ReportSettingTypeDef",
    {
        "ReportTemplate": str,
        "FrameworkArns": NotRequired[Sequence[str]],
        "NumberOfFrameworks": NotRequired[int],
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

RestoreJobsListMemberTypeDef = TypedDict(
    "RestoreJobsListMemberTypeDef",
    {
        "AccountId": NotRequired[str],
        "RestoreJobId": NotRequired[str],
        "RecoveryPointArn": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "CompletionDate": NotRequired[datetime],
        "Status": NotRequired[RestoreJobStatusType],
        "StatusMessage": NotRequired[str],
        "PercentDone": NotRequired[str],
        "BackupSizeInBytes": NotRequired[int],
        "IamRoleArn": NotRequired[str],
        "ExpectedCompletionTimeMinutes": NotRequired[int],
        "CreatedResourceArn": NotRequired[str],
        "ResourceType": NotRequired[str],
    },
)

StartBackupJobInputRequestTypeDef = TypedDict(
    "StartBackupJobInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "ResourceArn": str,
        "IamRoleArn": str,
        "IdempotencyToken": NotRequired[str],
        "StartWindowMinutes": NotRequired[int],
        "CompleteWindowMinutes": NotRequired[int],
        "Lifecycle": NotRequired["LifecycleTypeDef"],
        "RecoveryPointTags": NotRequired[Mapping[str, str]],
        "BackupOptions": NotRequired[Mapping[str, str]],
    },
)

StartBackupJobOutputTypeDef = TypedDict(
    "StartBackupJobOutputTypeDef",
    {
        "BackupJobId": str,
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartCopyJobInputRequestTypeDef = TypedDict(
    "StartCopyJobInputRequestTypeDef",
    {
        "RecoveryPointArn": str,
        "SourceBackupVaultName": str,
        "DestinationBackupVaultArn": str,
        "IamRoleArn": str,
        "IdempotencyToken": NotRequired[str],
        "Lifecycle": NotRequired["LifecycleTypeDef"],
    },
)

StartCopyJobOutputTypeDef = TypedDict(
    "StartCopyJobOutputTypeDef",
    {
        "CopyJobId": str,
        "CreationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartReportJobInputRequestTypeDef = TypedDict(
    "StartReportJobInputRequestTypeDef",
    {
        "ReportPlanName": str,
        "IdempotencyToken": NotRequired[str],
    },
)

StartReportJobOutputTypeDef = TypedDict(
    "StartReportJobOutputTypeDef",
    {
        "ReportJobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartRestoreJobInputRequestTypeDef = TypedDict(
    "StartRestoreJobInputRequestTypeDef",
    {
        "RecoveryPointArn": str,
        "Metadata": Mapping[str, str],
        "IamRoleArn": str,
        "IdempotencyToken": NotRequired[str],
        "ResourceType": NotRequired[str],
    },
)

StartRestoreJobOutputTypeDef = TypedDict(
    "StartRestoreJobOutputTypeDef",
    {
        "RestoreJobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopBackupJobInputRequestTypeDef = TypedDict(
    "StopBackupJobInputRequestTypeDef",
    {
        "BackupJobId": str,
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
        "TagKeyList": Sequence[str],
    },
)

UpdateBackupPlanInputRequestTypeDef = TypedDict(
    "UpdateBackupPlanInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlan": "BackupPlanInputTypeDef",
    },
)

UpdateBackupPlanOutputTypeDef = TypedDict(
    "UpdateBackupPlanOutputTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "CreationDate": datetime,
        "VersionId": str,
        "AdvancedBackupSettings": List["AdvancedBackupSettingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFrameworkInputRequestTypeDef = TypedDict(
    "UpdateFrameworkInputRequestTypeDef",
    {
        "FrameworkName": str,
        "FrameworkDescription": NotRequired[str],
        "FrameworkControls": NotRequired[Sequence["FrameworkControlTypeDef"]],
        "IdempotencyToken": NotRequired[str],
    },
)

UpdateFrameworkOutputTypeDef = TypedDict(
    "UpdateFrameworkOutputTypeDef",
    {
        "FrameworkName": str,
        "FrameworkArn": str,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGlobalSettingsInputRequestTypeDef = TypedDict(
    "UpdateGlobalSettingsInputRequestTypeDef",
    {
        "GlobalSettings": NotRequired[Mapping[str, str]],
    },
)

UpdateRecoveryPointLifecycleInputRequestTypeDef = TypedDict(
    "UpdateRecoveryPointLifecycleInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
        "Lifecycle": NotRequired["LifecycleTypeDef"],
    },
)

UpdateRecoveryPointLifecycleOutputTypeDef = TypedDict(
    "UpdateRecoveryPointLifecycleOutputTypeDef",
    {
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "Lifecycle": "LifecycleTypeDef",
        "CalculatedLifecycle": "CalculatedLifecycleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRegionSettingsInputRequestTypeDef = TypedDict(
    "UpdateRegionSettingsInputRequestTypeDef",
    {
        "ResourceTypeOptInPreference": NotRequired[Mapping[str, bool]],
        "ResourceTypeManagementPreference": NotRequired[Mapping[str, bool]],
    },
)

UpdateReportPlanInputRequestTypeDef = TypedDict(
    "UpdateReportPlanInputRequestTypeDef",
    {
        "ReportPlanName": str,
        "ReportPlanDescription": NotRequired[str],
        "ReportDeliveryChannel": NotRequired["ReportDeliveryChannelTypeDef"],
        "ReportSetting": NotRequired["ReportSettingTypeDef"],
        "IdempotencyToken": NotRequired[str],
    },
)

UpdateReportPlanOutputTypeDef = TypedDict(
    "UpdateReportPlanOutputTypeDef",
    {
        "ReportPlanName": str,
        "ReportPlanArn": str,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
