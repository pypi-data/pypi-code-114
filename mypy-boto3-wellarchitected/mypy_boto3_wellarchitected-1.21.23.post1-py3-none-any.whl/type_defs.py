"""
Type annotations for wellarchitected service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/type_defs.html)

Usage::

    ```python
    from mypy_boto3_wellarchitected.type_defs import AnswerSummaryTypeDef

    data: AnswerSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AnswerReasonType,
    ChoiceReasonType,
    ChoiceStatusType,
    DifferenceStatusType,
    ImportLensStatusType,
    LensStatusType,
    LensStatusTypeType,
    LensTypeType,
    NotificationTypeType,
    PermissionTypeType,
    RiskType,
    ShareInvitationActionType,
    ShareResourceTypeType,
    ShareStatusType,
    WorkloadEnvironmentType,
    WorkloadImprovementStatusType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AnswerSummaryTypeDef",
    "AnswerTypeDef",
    "AssociateLensesInputRequestTypeDef",
    "ChoiceAnswerSummaryTypeDef",
    "ChoiceAnswerTypeDef",
    "ChoiceContentTypeDef",
    "ChoiceImprovementPlanTypeDef",
    "ChoiceTypeDef",
    "ChoiceUpdateTypeDef",
    "CreateLensShareInputRequestTypeDef",
    "CreateLensShareOutputTypeDef",
    "CreateLensVersionInputRequestTypeDef",
    "CreateLensVersionOutputTypeDef",
    "CreateMilestoneInputRequestTypeDef",
    "CreateMilestoneOutputTypeDef",
    "CreateWorkloadInputRequestTypeDef",
    "CreateWorkloadOutputTypeDef",
    "CreateWorkloadShareInputRequestTypeDef",
    "CreateWorkloadShareOutputTypeDef",
    "DeleteLensInputRequestTypeDef",
    "DeleteLensShareInputRequestTypeDef",
    "DeleteWorkloadInputRequestTypeDef",
    "DeleteWorkloadShareInputRequestTypeDef",
    "DisassociateLensesInputRequestTypeDef",
    "ExportLensInputRequestTypeDef",
    "ExportLensOutputTypeDef",
    "GetAnswerInputRequestTypeDef",
    "GetAnswerOutputTypeDef",
    "GetLensInputRequestTypeDef",
    "GetLensOutputTypeDef",
    "GetLensReviewInputRequestTypeDef",
    "GetLensReviewOutputTypeDef",
    "GetLensReviewReportInputRequestTypeDef",
    "GetLensReviewReportOutputTypeDef",
    "GetLensVersionDifferenceInputRequestTypeDef",
    "GetLensVersionDifferenceOutputTypeDef",
    "GetMilestoneInputRequestTypeDef",
    "GetMilestoneOutputTypeDef",
    "GetWorkloadInputRequestTypeDef",
    "GetWorkloadOutputTypeDef",
    "ImportLensInputRequestTypeDef",
    "ImportLensOutputTypeDef",
    "ImprovementSummaryTypeDef",
    "LensReviewReportTypeDef",
    "LensReviewSummaryTypeDef",
    "LensReviewTypeDef",
    "LensShareSummaryTypeDef",
    "LensSummaryTypeDef",
    "LensTypeDef",
    "LensUpgradeSummaryTypeDef",
    "ListAnswersInputRequestTypeDef",
    "ListAnswersOutputTypeDef",
    "ListLensReviewImprovementsInputRequestTypeDef",
    "ListLensReviewImprovementsOutputTypeDef",
    "ListLensReviewsInputRequestTypeDef",
    "ListLensReviewsOutputTypeDef",
    "ListLensSharesInputRequestTypeDef",
    "ListLensSharesOutputTypeDef",
    "ListLensesInputRequestTypeDef",
    "ListLensesOutputTypeDef",
    "ListMilestonesInputRequestTypeDef",
    "ListMilestonesOutputTypeDef",
    "ListNotificationsInputRequestTypeDef",
    "ListNotificationsOutputTypeDef",
    "ListShareInvitationsInputRequestTypeDef",
    "ListShareInvitationsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListWorkloadSharesInputRequestTypeDef",
    "ListWorkloadSharesOutputTypeDef",
    "ListWorkloadsInputRequestTypeDef",
    "ListWorkloadsOutputTypeDef",
    "MilestoneSummaryTypeDef",
    "MilestoneTypeDef",
    "NotificationSummaryTypeDef",
    "PillarDifferenceTypeDef",
    "PillarReviewSummaryTypeDef",
    "QuestionDifferenceTypeDef",
    "ResponseMetadataTypeDef",
    "ShareInvitationSummaryTypeDef",
    "ShareInvitationTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateAnswerInputRequestTypeDef",
    "UpdateAnswerOutputTypeDef",
    "UpdateLensReviewInputRequestTypeDef",
    "UpdateLensReviewOutputTypeDef",
    "UpdateShareInvitationInputRequestTypeDef",
    "UpdateShareInvitationOutputTypeDef",
    "UpdateWorkloadInputRequestTypeDef",
    "UpdateWorkloadOutputTypeDef",
    "UpdateWorkloadShareInputRequestTypeDef",
    "UpdateWorkloadShareOutputTypeDef",
    "UpgradeLensReviewInputRequestTypeDef",
    "VersionDifferencesTypeDef",
    "WorkloadShareSummaryTypeDef",
    "WorkloadShareTypeDef",
    "WorkloadSummaryTypeDef",
    "WorkloadTypeDef",
)

AnswerSummaryTypeDef = TypedDict(
    "AnswerSummaryTypeDef",
    {
        "QuestionId": NotRequired[str],
        "PillarId": NotRequired[str],
        "QuestionTitle": NotRequired[str],
        "Choices": NotRequired[List["ChoiceTypeDef"]],
        "SelectedChoices": NotRequired[List[str]],
        "ChoiceAnswerSummaries": NotRequired[List["ChoiceAnswerSummaryTypeDef"]],
        "IsApplicable": NotRequired[bool],
        "Risk": NotRequired[RiskType],
        "Reason": NotRequired[AnswerReasonType],
    },
)

AnswerTypeDef = TypedDict(
    "AnswerTypeDef",
    {
        "QuestionId": NotRequired[str],
        "PillarId": NotRequired[str],
        "QuestionTitle": NotRequired[str],
        "QuestionDescription": NotRequired[str],
        "ImprovementPlanUrl": NotRequired[str],
        "HelpfulResourceUrl": NotRequired[str],
        "HelpfulResourceDisplayText": NotRequired[str],
        "Choices": NotRequired[List["ChoiceTypeDef"]],
        "SelectedChoices": NotRequired[List[str]],
        "ChoiceAnswers": NotRequired[List["ChoiceAnswerTypeDef"]],
        "IsApplicable": NotRequired[bool],
        "Risk": NotRequired[RiskType],
        "Notes": NotRequired[str],
        "Reason": NotRequired[AnswerReasonType],
    },
)

AssociateLensesInputRequestTypeDef = TypedDict(
    "AssociateLensesInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAliases": Sequence[str],
    },
)

ChoiceAnswerSummaryTypeDef = TypedDict(
    "ChoiceAnswerSummaryTypeDef",
    {
        "ChoiceId": NotRequired[str],
        "Status": NotRequired[ChoiceStatusType],
        "Reason": NotRequired[ChoiceReasonType],
    },
)

ChoiceAnswerTypeDef = TypedDict(
    "ChoiceAnswerTypeDef",
    {
        "ChoiceId": NotRequired[str],
        "Status": NotRequired[ChoiceStatusType],
        "Reason": NotRequired[ChoiceReasonType],
        "Notes": NotRequired[str],
    },
)

ChoiceContentTypeDef = TypedDict(
    "ChoiceContentTypeDef",
    {
        "DisplayText": NotRequired[str],
        "Url": NotRequired[str],
    },
)

ChoiceImprovementPlanTypeDef = TypedDict(
    "ChoiceImprovementPlanTypeDef",
    {
        "ChoiceId": NotRequired[str],
        "DisplayText": NotRequired[str],
        "ImprovementPlanUrl": NotRequired[str],
    },
)

ChoiceTypeDef = TypedDict(
    "ChoiceTypeDef",
    {
        "ChoiceId": NotRequired[str],
        "Title": NotRequired[str],
        "Description": NotRequired[str],
        "HelpfulResource": NotRequired["ChoiceContentTypeDef"],
        "ImprovementPlan": NotRequired["ChoiceContentTypeDef"],
    },
)

ChoiceUpdateTypeDef = TypedDict(
    "ChoiceUpdateTypeDef",
    {
        "Status": ChoiceStatusType,
        "Reason": NotRequired[ChoiceReasonType],
        "Notes": NotRequired[str],
    },
)

CreateLensShareInputRequestTypeDef = TypedDict(
    "CreateLensShareInputRequestTypeDef",
    {
        "LensAlias": str,
        "SharedWith": str,
        "ClientRequestToken": str,
    },
)

CreateLensShareOutputTypeDef = TypedDict(
    "CreateLensShareOutputTypeDef",
    {
        "ShareId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLensVersionInputRequestTypeDef = TypedDict(
    "CreateLensVersionInputRequestTypeDef",
    {
        "LensAlias": str,
        "LensVersion": str,
        "ClientRequestToken": str,
        "IsMajorVersion": NotRequired[bool],
    },
)

CreateLensVersionOutputTypeDef = TypedDict(
    "CreateLensVersionOutputTypeDef",
    {
        "LensArn": str,
        "LensVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMilestoneInputRequestTypeDef = TypedDict(
    "CreateMilestoneInputRequestTypeDef",
    {
        "WorkloadId": str,
        "MilestoneName": str,
        "ClientRequestToken": str,
    },
)

CreateMilestoneOutputTypeDef = TypedDict(
    "CreateMilestoneOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorkloadInputRequestTypeDef = TypedDict(
    "CreateWorkloadInputRequestTypeDef",
    {
        "WorkloadName": str,
        "Description": str,
        "Environment": WorkloadEnvironmentType,
        "ReviewOwner": str,
        "Lenses": Sequence[str],
        "ClientRequestToken": str,
        "AccountIds": NotRequired[Sequence[str]],
        "AwsRegions": NotRequired[Sequence[str]],
        "NonAwsRegions": NotRequired[Sequence[str]],
        "PillarPriorities": NotRequired[Sequence[str]],
        "ArchitecturalDesign": NotRequired[str],
        "IndustryType": NotRequired[str],
        "Industry": NotRequired[str],
        "Notes": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateWorkloadOutputTypeDef = TypedDict(
    "CreateWorkloadOutputTypeDef",
    {
        "WorkloadId": str,
        "WorkloadArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorkloadShareInputRequestTypeDef = TypedDict(
    "CreateWorkloadShareInputRequestTypeDef",
    {
        "WorkloadId": str,
        "SharedWith": str,
        "PermissionType": PermissionTypeType,
        "ClientRequestToken": str,
    },
)

CreateWorkloadShareOutputTypeDef = TypedDict(
    "CreateWorkloadShareOutputTypeDef",
    {
        "WorkloadId": str,
        "ShareId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLensInputRequestTypeDef = TypedDict(
    "DeleteLensInputRequestTypeDef",
    {
        "LensAlias": str,
        "ClientRequestToken": str,
        "LensStatus": LensStatusTypeType,
    },
)

DeleteLensShareInputRequestTypeDef = TypedDict(
    "DeleteLensShareInputRequestTypeDef",
    {
        "ShareId": str,
        "LensAlias": str,
        "ClientRequestToken": str,
    },
)

DeleteWorkloadInputRequestTypeDef = TypedDict(
    "DeleteWorkloadInputRequestTypeDef",
    {
        "WorkloadId": str,
        "ClientRequestToken": str,
    },
)

DeleteWorkloadShareInputRequestTypeDef = TypedDict(
    "DeleteWorkloadShareInputRequestTypeDef",
    {
        "ShareId": str,
        "WorkloadId": str,
        "ClientRequestToken": str,
    },
)

DisassociateLensesInputRequestTypeDef = TypedDict(
    "DisassociateLensesInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAliases": Sequence[str],
    },
)

ExportLensInputRequestTypeDef = TypedDict(
    "ExportLensInputRequestTypeDef",
    {
        "LensAlias": str,
        "LensVersion": NotRequired[str],
    },
)

ExportLensOutputTypeDef = TypedDict(
    "ExportLensOutputTypeDef",
    {
        "LensJSON": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAnswerInputRequestTypeDef = TypedDict(
    "GetAnswerInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "QuestionId": str,
        "MilestoneNumber": NotRequired[int],
    },
)

GetAnswerOutputTypeDef = TypedDict(
    "GetAnswerOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensAlias": str,
        "LensArn": str,
        "Answer": "AnswerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLensInputRequestTypeDef = TypedDict(
    "GetLensInputRequestTypeDef",
    {
        "LensAlias": str,
        "LensVersion": NotRequired[str],
    },
)

GetLensOutputTypeDef = TypedDict(
    "GetLensOutputTypeDef",
    {
        "Lens": "LensTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLensReviewInputRequestTypeDef = TypedDict(
    "GetLensReviewInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "MilestoneNumber": NotRequired[int],
    },
)

GetLensReviewOutputTypeDef = TypedDict(
    "GetLensReviewOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensReview": "LensReviewTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLensReviewReportInputRequestTypeDef = TypedDict(
    "GetLensReviewReportInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "MilestoneNumber": NotRequired[int],
    },
)

GetLensReviewReportOutputTypeDef = TypedDict(
    "GetLensReviewReportOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensReviewReport": "LensReviewReportTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLensVersionDifferenceInputRequestTypeDef = TypedDict(
    "GetLensVersionDifferenceInputRequestTypeDef",
    {
        "LensAlias": str,
        "BaseLensVersion": NotRequired[str],
        "TargetLensVersion": NotRequired[str],
    },
)

GetLensVersionDifferenceOutputTypeDef = TypedDict(
    "GetLensVersionDifferenceOutputTypeDef",
    {
        "LensAlias": str,
        "LensArn": str,
        "BaseLensVersion": str,
        "TargetLensVersion": str,
        "LatestLensVersion": str,
        "VersionDifferences": "VersionDifferencesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMilestoneInputRequestTypeDef = TypedDict(
    "GetMilestoneInputRequestTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
    },
)

GetMilestoneOutputTypeDef = TypedDict(
    "GetMilestoneOutputTypeDef",
    {
        "WorkloadId": str,
        "Milestone": "MilestoneTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkloadInputRequestTypeDef = TypedDict(
    "GetWorkloadInputRequestTypeDef",
    {
        "WorkloadId": str,
    },
)

GetWorkloadOutputTypeDef = TypedDict(
    "GetWorkloadOutputTypeDef",
    {
        "Workload": "WorkloadTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportLensInputRequestTypeDef = TypedDict(
    "ImportLensInputRequestTypeDef",
    {
        "JSONString": str,
        "ClientRequestToken": str,
        "LensAlias": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

ImportLensOutputTypeDef = TypedDict(
    "ImportLensOutputTypeDef",
    {
        "LensArn": str,
        "Status": ImportLensStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImprovementSummaryTypeDef = TypedDict(
    "ImprovementSummaryTypeDef",
    {
        "QuestionId": NotRequired[str],
        "PillarId": NotRequired[str],
        "QuestionTitle": NotRequired[str],
        "Risk": NotRequired[RiskType],
        "ImprovementPlanUrl": NotRequired[str],
        "ImprovementPlans": NotRequired[List["ChoiceImprovementPlanTypeDef"]],
    },
)

LensReviewReportTypeDef = TypedDict(
    "LensReviewReportTypeDef",
    {
        "LensAlias": NotRequired[str],
        "LensArn": NotRequired[str],
        "Base64String": NotRequired[str],
    },
)

LensReviewSummaryTypeDef = TypedDict(
    "LensReviewSummaryTypeDef",
    {
        "LensAlias": NotRequired[str],
        "LensArn": NotRequired[str],
        "LensVersion": NotRequired[str],
        "LensName": NotRequired[str],
        "LensStatus": NotRequired[LensStatusType],
        "UpdatedAt": NotRequired[datetime],
        "RiskCounts": NotRequired[Dict[RiskType, int]],
    },
)

LensReviewTypeDef = TypedDict(
    "LensReviewTypeDef",
    {
        "LensAlias": NotRequired[str],
        "LensArn": NotRequired[str],
        "LensVersion": NotRequired[str],
        "LensName": NotRequired[str],
        "LensStatus": NotRequired[LensStatusType],
        "PillarReviewSummaries": NotRequired[List["PillarReviewSummaryTypeDef"]],
        "UpdatedAt": NotRequired[datetime],
        "Notes": NotRequired[str],
        "RiskCounts": NotRequired[Dict[RiskType, int]],
        "NextToken": NotRequired[str],
    },
)

LensShareSummaryTypeDef = TypedDict(
    "LensShareSummaryTypeDef",
    {
        "ShareId": NotRequired[str],
        "SharedWith": NotRequired[str],
        "Status": NotRequired[ShareStatusType],
    },
)

LensSummaryTypeDef = TypedDict(
    "LensSummaryTypeDef",
    {
        "LensArn": NotRequired[str],
        "LensAlias": NotRequired[str],
        "LensName": NotRequired[str],
        "LensType": NotRequired[LensTypeType],
        "Description": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
        "LensVersion": NotRequired[str],
        "Owner": NotRequired[str],
        "LensStatus": NotRequired[LensStatusType],
    },
)

LensTypeDef = TypedDict(
    "LensTypeDef",
    {
        "LensArn": NotRequired[str],
        "LensVersion": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Owner": NotRequired[str],
        "ShareInvitationId": NotRequired[str],
    },
)

LensUpgradeSummaryTypeDef = TypedDict(
    "LensUpgradeSummaryTypeDef",
    {
        "WorkloadId": NotRequired[str],
        "WorkloadName": NotRequired[str],
        "LensAlias": NotRequired[str],
        "LensArn": NotRequired[str],
        "CurrentLensVersion": NotRequired[str],
        "LatestLensVersion": NotRequired[str],
    },
)

ListAnswersInputRequestTypeDef = TypedDict(
    "ListAnswersInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "PillarId": NotRequired[str],
        "MilestoneNumber": NotRequired[int],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListAnswersOutputTypeDef = TypedDict(
    "ListAnswersOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensAlias": str,
        "LensArn": str,
        "AnswerSummaries": List["AnswerSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLensReviewImprovementsInputRequestTypeDef = TypedDict(
    "ListLensReviewImprovementsInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "PillarId": NotRequired[str],
        "MilestoneNumber": NotRequired[int],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListLensReviewImprovementsOutputTypeDef = TypedDict(
    "ListLensReviewImprovementsOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensAlias": str,
        "LensArn": str,
        "ImprovementSummaries": List["ImprovementSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLensReviewsInputRequestTypeDef = TypedDict(
    "ListLensReviewsInputRequestTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": NotRequired[int],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListLensReviewsOutputTypeDef = TypedDict(
    "ListLensReviewsOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensReviewSummaries": List["LensReviewSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLensSharesInputRequestTypeDef = TypedDict(
    "ListLensSharesInputRequestTypeDef",
    {
        "LensAlias": str,
        "SharedWithPrefix": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListLensSharesOutputTypeDef = TypedDict(
    "ListLensSharesOutputTypeDef",
    {
        "LensShareSummaries": List["LensShareSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLensesInputRequestTypeDef = TypedDict(
    "ListLensesInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "LensType": NotRequired[LensTypeType],
        "LensStatus": NotRequired[LensStatusTypeType],
        "LensName": NotRequired[str],
    },
)

ListLensesOutputTypeDef = TypedDict(
    "ListLensesOutputTypeDef",
    {
        "LensSummaries": List["LensSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMilestonesInputRequestTypeDef = TypedDict(
    "ListMilestonesInputRequestTypeDef",
    {
        "WorkloadId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListMilestonesOutputTypeDef = TypedDict(
    "ListMilestonesOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneSummaries": List["MilestoneSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNotificationsInputRequestTypeDef = TypedDict(
    "ListNotificationsInputRequestTypeDef",
    {
        "WorkloadId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListNotificationsOutputTypeDef = TypedDict(
    "ListNotificationsOutputTypeDef",
    {
        "NotificationSummaries": List["NotificationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListShareInvitationsInputRequestTypeDef = TypedDict(
    "ListShareInvitationsInputRequestTypeDef",
    {
        "WorkloadNamePrefix": NotRequired[str],
        "LensNamePrefix": NotRequired[str],
        "ShareResourceType": NotRequired[ShareResourceTypeType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListShareInvitationsOutputTypeDef = TypedDict(
    "ListShareInvitationsOutputTypeDef",
    {
        "ShareInvitationSummaries": List["ShareInvitationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "WorkloadArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkloadSharesInputRequestTypeDef = TypedDict(
    "ListWorkloadSharesInputRequestTypeDef",
    {
        "WorkloadId": str,
        "SharedWithPrefix": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListWorkloadSharesOutputTypeDef = TypedDict(
    "ListWorkloadSharesOutputTypeDef",
    {
        "WorkloadId": str,
        "WorkloadShareSummaries": List["WorkloadShareSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkloadsInputRequestTypeDef = TypedDict(
    "ListWorkloadsInputRequestTypeDef",
    {
        "WorkloadNamePrefix": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListWorkloadsOutputTypeDef = TypedDict(
    "ListWorkloadsOutputTypeDef",
    {
        "WorkloadSummaries": List["WorkloadSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MilestoneSummaryTypeDef = TypedDict(
    "MilestoneSummaryTypeDef",
    {
        "MilestoneNumber": NotRequired[int],
        "MilestoneName": NotRequired[str],
        "RecordedAt": NotRequired[datetime],
        "WorkloadSummary": NotRequired["WorkloadSummaryTypeDef"],
    },
)

MilestoneTypeDef = TypedDict(
    "MilestoneTypeDef",
    {
        "MilestoneNumber": NotRequired[int],
        "MilestoneName": NotRequired[str],
        "RecordedAt": NotRequired[datetime],
        "Workload": NotRequired["WorkloadTypeDef"],
    },
)

NotificationSummaryTypeDef = TypedDict(
    "NotificationSummaryTypeDef",
    {
        "Type": NotRequired[NotificationTypeType],
        "LensUpgradeSummary": NotRequired["LensUpgradeSummaryTypeDef"],
    },
)

PillarDifferenceTypeDef = TypedDict(
    "PillarDifferenceTypeDef",
    {
        "PillarId": NotRequired[str],
        "PillarName": NotRequired[str],
        "DifferenceStatus": NotRequired[DifferenceStatusType],
        "QuestionDifferences": NotRequired[List["QuestionDifferenceTypeDef"]],
    },
)

PillarReviewSummaryTypeDef = TypedDict(
    "PillarReviewSummaryTypeDef",
    {
        "PillarId": NotRequired[str],
        "PillarName": NotRequired[str],
        "Notes": NotRequired[str],
        "RiskCounts": NotRequired[Dict[RiskType, int]],
    },
)

QuestionDifferenceTypeDef = TypedDict(
    "QuestionDifferenceTypeDef",
    {
        "QuestionId": NotRequired[str],
        "QuestionTitle": NotRequired[str],
        "DifferenceStatus": NotRequired[DifferenceStatusType],
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

ShareInvitationSummaryTypeDef = TypedDict(
    "ShareInvitationSummaryTypeDef",
    {
        "ShareInvitationId": NotRequired[str],
        "SharedBy": NotRequired[str],
        "SharedWith": NotRequired[str],
        "PermissionType": NotRequired[PermissionTypeType],
        "ShareResourceType": NotRequired[ShareResourceTypeType],
        "WorkloadName": NotRequired[str],
        "WorkloadId": NotRequired[str],
        "LensName": NotRequired[str],
        "LensArn": NotRequired[str],
    },
)

ShareInvitationTypeDef = TypedDict(
    "ShareInvitationTypeDef",
    {
        "ShareInvitationId": NotRequired[str],
        "ShareResourceType": NotRequired[ShareResourceTypeType],
        "WorkloadId": NotRequired[str],
        "LensAlias": NotRequired[str],
        "LensArn": NotRequired[str],
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "WorkloadArn": str,
        "Tags": Mapping[str, str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "WorkloadArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateAnswerInputRequestTypeDef = TypedDict(
    "UpdateAnswerInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "QuestionId": str,
        "SelectedChoices": NotRequired[Sequence[str]],
        "ChoiceUpdates": NotRequired[Mapping[str, "ChoiceUpdateTypeDef"]],
        "Notes": NotRequired[str],
        "IsApplicable": NotRequired[bool],
        "Reason": NotRequired[AnswerReasonType],
    },
)

UpdateAnswerOutputTypeDef = TypedDict(
    "UpdateAnswerOutputTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "LensArn": str,
        "Answer": "AnswerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateLensReviewInputRequestTypeDef = TypedDict(
    "UpdateLensReviewInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "LensNotes": NotRequired[str],
        "PillarNotes": NotRequired[Mapping[str, str]],
    },
)

UpdateLensReviewOutputTypeDef = TypedDict(
    "UpdateLensReviewOutputTypeDef",
    {
        "WorkloadId": str,
        "LensReview": "LensReviewTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateShareInvitationInputRequestTypeDef = TypedDict(
    "UpdateShareInvitationInputRequestTypeDef",
    {
        "ShareInvitationId": str,
        "ShareInvitationAction": ShareInvitationActionType,
    },
)

UpdateShareInvitationOutputTypeDef = TypedDict(
    "UpdateShareInvitationOutputTypeDef",
    {
        "ShareInvitation": "ShareInvitationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateWorkloadInputRequestTypeDef = TypedDict(
    "UpdateWorkloadInputRequestTypeDef",
    {
        "WorkloadId": str,
        "WorkloadName": NotRequired[str],
        "Description": NotRequired[str],
        "Environment": NotRequired[WorkloadEnvironmentType],
        "AccountIds": NotRequired[Sequence[str]],
        "AwsRegions": NotRequired[Sequence[str]],
        "NonAwsRegions": NotRequired[Sequence[str]],
        "PillarPriorities": NotRequired[Sequence[str]],
        "ArchitecturalDesign": NotRequired[str],
        "ReviewOwner": NotRequired[str],
        "IsReviewOwnerUpdateAcknowledged": NotRequired[bool],
        "IndustryType": NotRequired[str],
        "Industry": NotRequired[str],
        "Notes": NotRequired[str],
        "ImprovementStatus": NotRequired[WorkloadImprovementStatusType],
    },
)

UpdateWorkloadOutputTypeDef = TypedDict(
    "UpdateWorkloadOutputTypeDef",
    {
        "Workload": "WorkloadTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateWorkloadShareInputRequestTypeDef = TypedDict(
    "UpdateWorkloadShareInputRequestTypeDef",
    {
        "ShareId": str,
        "WorkloadId": str,
        "PermissionType": PermissionTypeType,
    },
)

UpdateWorkloadShareOutputTypeDef = TypedDict(
    "UpdateWorkloadShareOutputTypeDef",
    {
        "WorkloadId": str,
        "WorkloadShare": "WorkloadShareTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpgradeLensReviewInputRequestTypeDef = TypedDict(
    "UpgradeLensReviewInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "MilestoneName": str,
        "ClientRequestToken": NotRequired[str],
    },
)

VersionDifferencesTypeDef = TypedDict(
    "VersionDifferencesTypeDef",
    {
        "PillarDifferences": NotRequired[List["PillarDifferenceTypeDef"]],
    },
)

WorkloadShareSummaryTypeDef = TypedDict(
    "WorkloadShareSummaryTypeDef",
    {
        "ShareId": NotRequired[str],
        "SharedWith": NotRequired[str],
        "PermissionType": NotRequired[PermissionTypeType],
        "Status": NotRequired[ShareStatusType],
    },
)

WorkloadShareTypeDef = TypedDict(
    "WorkloadShareTypeDef",
    {
        "ShareId": NotRequired[str],
        "SharedBy": NotRequired[str],
        "SharedWith": NotRequired[str],
        "PermissionType": NotRequired[PermissionTypeType],
        "Status": NotRequired[ShareStatusType],
        "WorkloadName": NotRequired[str],
        "WorkloadId": NotRequired[str],
    },
)

WorkloadSummaryTypeDef = TypedDict(
    "WorkloadSummaryTypeDef",
    {
        "WorkloadId": NotRequired[str],
        "WorkloadArn": NotRequired[str],
        "WorkloadName": NotRequired[str],
        "Owner": NotRequired[str],
        "UpdatedAt": NotRequired[datetime],
        "Lenses": NotRequired[List[str]],
        "RiskCounts": NotRequired[Dict[RiskType, int]],
        "ImprovementStatus": NotRequired[WorkloadImprovementStatusType],
    },
)

WorkloadTypeDef = TypedDict(
    "WorkloadTypeDef",
    {
        "WorkloadId": NotRequired[str],
        "WorkloadArn": NotRequired[str],
        "WorkloadName": NotRequired[str],
        "Description": NotRequired[str],
        "Environment": NotRequired[WorkloadEnvironmentType],
        "UpdatedAt": NotRequired[datetime],
        "AccountIds": NotRequired[List[str]],
        "AwsRegions": NotRequired[List[str]],
        "NonAwsRegions": NotRequired[List[str]],
        "ArchitecturalDesign": NotRequired[str],
        "ReviewOwner": NotRequired[str],
        "ReviewRestrictionDate": NotRequired[datetime],
        "IsReviewOwnerUpdateAcknowledged": NotRequired[bool],
        "IndustryType": NotRequired[str],
        "Industry": NotRequired[str],
        "Notes": NotRequired[str],
        "ImprovementStatus": NotRequired[WorkloadImprovementStatusType],
        "RiskCounts": NotRequired[Dict[RiskType, int]],
        "PillarPriorities": NotRequired[List[str]],
        "Lenses": NotRequired[List[str]],
        "Owner": NotRequired[str],
        "ShareInvitationId": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
