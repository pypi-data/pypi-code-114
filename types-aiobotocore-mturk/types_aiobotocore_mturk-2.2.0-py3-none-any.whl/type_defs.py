"""
Type annotations for mturk service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mturk/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_mturk.type_defs import AcceptQualificationRequestRequestRequestTypeDef

    data: AcceptQualificationRequestRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AssignmentStatusType,
    ComparatorType,
    EventTypeType,
    HITAccessActionsType,
    HITReviewStatusType,
    HITStatusType,
    NotificationTransportType,
    NotifyWorkersFailureCodeType,
    QualificationStatusType,
    QualificationTypeStatusType,
    ReviewableHITStatusType,
    ReviewActionStatusType,
    ReviewPolicyLevelType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceptQualificationRequestRequestRequestTypeDef",
    "ApproveAssignmentRequestRequestTypeDef",
    "AssignmentTypeDef",
    "AssociateQualificationWithWorkerRequestRequestTypeDef",
    "BonusPaymentTypeDef",
    "CreateAdditionalAssignmentsForHITRequestRequestTypeDef",
    "CreateHITRequestRequestTypeDef",
    "CreateHITResponseTypeDef",
    "CreateHITTypeRequestRequestTypeDef",
    "CreateHITTypeResponseTypeDef",
    "CreateHITWithHITTypeRequestRequestTypeDef",
    "CreateHITWithHITTypeResponseTypeDef",
    "CreateQualificationTypeRequestRequestTypeDef",
    "CreateQualificationTypeResponseTypeDef",
    "CreateWorkerBlockRequestRequestTypeDef",
    "DeleteHITRequestRequestTypeDef",
    "DeleteQualificationTypeRequestRequestTypeDef",
    "DeleteWorkerBlockRequestRequestTypeDef",
    "DisassociateQualificationFromWorkerRequestRequestTypeDef",
    "GetAccountBalanceResponseTypeDef",
    "GetAssignmentRequestRequestTypeDef",
    "GetAssignmentResponseTypeDef",
    "GetFileUploadURLRequestRequestTypeDef",
    "GetFileUploadURLResponseTypeDef",
    "GetHITRequestRequestTypeDef",
    "GetHITResponseTypeDef",
    "GetQualificationScoreRequestRequestTypeDef",
    "GetQualificationScoreResponseTypeDef",
    "GetQualificationTypeRequestRequestTypeDef",
    "GetQualificationTypeResponseTypeDef",
    "HITLayoutParameterTypeDef",
    "HITTypeDef",
    "ListAssignmentsForHITRequestRequestTypeDef",
    "ListAssignmentsForHITResponseTypeDef",
    "ListBonusPaymentsRequestRequestTypeDef",
    "ListBonusPaymentsResponseTypeDef",
    "ListHITsForQualificationTypeRequestRequestTypeDef",
    "ListHITsForQualificationTypeResponseTypeDef",
    "ListHITsRequestRequestTypeDef",
    "ListHITsResponseTypeDef",
    "ListQualificationRequestsRequestRequestTypeDef",
    "ListQualificationRequestsResponseTypeDef",
    "ListQualificationTypesRequestRequestTypeDef",
    "ListQualificationTypesResponseTypeDef",
    "ListReviewPolicyResultsForHITRequestRequestTypeDef",
    "ListReviewPolicyResultsForHITResponseTypeDef",
    "ListReviewableHITsRequestRequestTypeDef",
    "ListReviewableHITsResponseTypeDef",
    "ListWorkerBlocksRequestRequestTypeDef",
    "ListWorkerBlocksResponseTypeDef",
    "ListWorkersWithQualificationTypeRequestRequestTypeDef",
    "ListWorkersWithQualificationTypeResponseTypeDef",
    "LocaleTypeDef",
    "NotificationSpecificationTypeDef",
    "NotifyWorkersFailureStatusTypeDef",
    "NotifyWorkersRequestRequestTypeDef",
    "NotifyWorkersResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterMapEntryTypeDef",
    "PolicyParameterTypeDef",
    "QualificationRequestTypeDef",
    "QualificationRequirementTypeDef",
    "QualificationTypeDef",
    "QualificationTypeTypeDef",
    "RejectAssignmentRequestRequestTypeDef",
    "RejectQualificationRequestRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ReviewActionDetailTypeDef",
    "ReviewPolicyTypeDef",
    "ReviewReportTypeDef",
    "ReviewResultDetailTypeDef",
    "SendBonusRequestRequestTypeDef",
    "SendTestEventNotificationRequestRequestTypeDef",
    "UpdateExpirationForHITRequestRequestTypeDef",
    "UpdateHITReviewStatusRequestRequestTypeDef",
    "UpdateHITTypeOfHITRequestRequestTypeDef",
    "UpdateNotificationSettingsRequestRequestTypeDef",
    "UpdateQualificationTypeRequestRequestTypeDef",
    "UpdateQualificationTypeResponseTypeDef",
    "WorkerBlockTypeDef",
)

AcceptQualificationRequestRequestRequestTypeDef = TypedDict(
    "AcceptQualificationRequestRequestRequestTypeDef",
    {
        "QualificationRequestId": str,
        "IntegerValue": NotRequired[int],
    },
)

ApproveAssignmentRequestRequestTypeDef = TypedDict(
    "ApproveAssignmentRequestRequestTypeDef",
    {
        "AssignmentId": str,
        "RequesterFeedback": NotRequired[str],
        "OverrideRejection": NotRequired[bool],
    },
)

AssignmentTypeDef = TypedDict(
    "AssignmentTypeDef",
    {
        "AssignmentId": NotRequired[str],
        "WorkerId": NotRequired[str],
        "HITId": NotRequired[str],
        "AssignmentStatus": NotRequired[AssignmentStatusType],
        "AutoApprovalTime": NotRequired[datetime],
        "AcceptTime": NotRequired[datetime],
        "SubmitTime": NotRequired[datetime],
        "ApprovalTime": NotRequired[datetime],
        "RejectionTime": NotRequired[datetime],
        "Deadline": NotRequired[datetime],
        "Answer": NotRequired[str],
        "RequesterFeedback": NotRequired[str],
    },
)

AssociateQualificationWithWorkerRequestRequestTypeDef = TypedDict(
    "AssociateQualificationWithWorkerRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
        "WorkerId": str,
        "IntegerValue": NotRequired[int],
        "SendNotification": NotRequired[bool],
    },
)

BonusPaymentTypeDef = TypedDict(
    "BonusPaymentTypeDef",
    {
        "WorkerId": NotRequired[str],
        "BonusAmount": NotRequired[str],
        "AssignmentId": NotRequired[str],
        "Reason": NotRequired[str],
        "GrantTime": NotRequired[datetime],
    },
)

CreateAdditionalAssignmentsForHITRequestRequestTypeDef = TypedDict(
    "CreateAdditionalAssignmentsForHITRequestRequestTypeDef",
    {
        "HITId": str,
        "NumberOfAdditionalAssignments": int,
        "UniqueRequestToken": NotRequired[str],
    },
)

CreateHITRequestRequestTypeDef = TypedDict(
    "CreateHITRequestRequestTypeDef",
    {
        "LifetimeInSeconds": int,
        "AssignmentDurationInSeconds": int,
        "Reward": str,
        "Title": str,
        "Description": str,
        "MaxAssignments": NotRequired[int],
        "AutoApprovalDelayInSeconds": NotRequired[int],
        "Keywords": NotRequired[str],
        "Question": NotRequired[str],
        "RequesterAnnotation": NotRequired[str],
        "QualificationRequirements": NotRequired[Sequence["QualificationRequirementTypeDef"]],
        "UniqueRequestToken": NotRequired[str],
        "AssignmentReviewPolicy": NotRequired["ReviewPolicyTypeDef"],
        "HITReviewPolicy": NotRequired["ReviewPolicyTypeDef"],
        "HITLayoutId": NotRequired[str],
        "HITLayoutParameters": NotRequired[Sequence["HITLayoutParameterTypeDef"]],
    },
)

CreateHITResponseTypeDef = TypedDict(
    "CreateHITResponseTypeDef",
    {
        "HIT": "HITTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateHITTypeRequestRequestTypeDef = TypedDict(
    "CreateHITTypeRequestRequestTypeDef",
    {
        "AssignmentDurationInSeconds": int,
        "Reward": str,
        "Title": str,
        "Description": str,
        "AutoApprovalDelayInSeconds": NotRequired[int],
        "Keywords": NotRequired[str],
        "QualificationRequirements": NotRequired[Sequence["QualificationRequirementTypeDef"]],
    },
)

CreateHITTypeResponseTypeDef = TypedDict(
    "CreateHITTypeResponseTypeDef",
    {
        "HITTypeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateHITWithHITTypeRequestRequestTypeDef = TypedDict(
    "CreateHITWithHITTypeRequestRequestTypeDef",
    {
        "HITTypeId": str,
        "LifetimeInSeconds": int,
        "MaxAssignments": NotRequired[int],
        "Question": NotRequired[str],
        "RequesterAnnotation": NotRequired[str],
        "UniqueRequestToken": NotRequired[str],
        "AssignmentReviewPolicy": NotRequired["ReviewPolicyTypeDef"],
        "HITReviewPolicy": NotRequired["ReviewPolicyTypeDef"],
        "HITLayoutId": NotRequired[str],
        "HITLayoutParameters": NotRequired[Sequence["HITLayoutParameterTypeDef"]],
    },
)

CreateHITWithHITTypeResponseTypeDef = TypedDict(
    "CreateHITWithHITTypeResponseTypeDef",
    {
        "HIT": "HITTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateQualificationTypeRequestRequestTypeDef = TypedDict(
    "CreateQualificationTypeRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "QualificationTypeStatus": QualificationTypeStatusType,
        "Keywords": NotRequired[str],
        "RetryDelayInSeconds": NotRequired[int],
        "Test": NotRequired[str],
        "AnswerKey": NotRequired[str],
        "TestDurationInSeconds": NotRequired[int],
        "AutoGranted": NotRequired[bool],
        "AutoGrantedValue": NotRequired[int],
    },
)

CreateQualificationTypeResponseTypeDef = TypedDict(
    "CreateQualificationTypeResponseTypeDef",
    {
        "QualificationType": "QualificationTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorkerBlockRequestRequestTypeDef = TypedDict(
    "CreateWorkerBlockRequestRequestTypeDef",
    {
        "WorkerId": str,
        "Reason": str,
    },
)

DeleteHITRequestRequestTypeDef = TypedDict(
    "DeleteHITRequestRequestTypeDef",
    {
        "HITId": str,
    },
)

DeleteQualificationTypeRequestRequestTypeDef = TypedDict(
    "DeleteQualificationTypeRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
    },
)

DeleteWorkerBlockRequestRequestTypeDef = TypedDict(
    "DeleteWorkerBlockRequestRequestTypeDef",
    {
        "WorkerId": str,
        "Reason": NotRequired[str],
    },
)

DisassociateQualificationFromWorkerRequestRequestTypeDef = TypedDict(
    "DisassociateQualificationFromWorkerRequestRequestTypeDef",
    {
        "WorkerId": str,
        "QualificationTypeId": str,
        "Reason": NotRequired[str],
    },
)

GetAccountBalanceResponseTypeDef = TypedDict(
    "GetAccountBalanceResponseTypeDef",
    {
        "AvailableBalance": str,
        "OnHoldBalance": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssignmentRequestRequestTypeDef = TypedDict(
    "GetAssignmentRequestRequestTypeDef",
    {
        "AssignmentId": str,
    },
)

GetAssignmentResponseTypeDef = TypedDict(
    "GetAssignmentResponseTypeDef",
    {
        "Assignment": "AssignmentTypeDef",
        "HIT": "HITTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFileUploadURLRequestRequestTypeDef = TypedDict(
    "GetFileUploadURLRequestRequestTypeDef",
    {
        "AssignmentId": str,
        "QuestionIdentifier": str,
    },
)

GetFileUploadURLResponseTypeDef = TypedDict(
    "GetFileUploadURLResponseTypeDef",
    {
        "FileUploadURL": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHITRequestRequestTypeDef = TypedDict(
    "GetHITRequestRequestTypeDef",
    {
        "HITId": str,
    },
)

GetHITResponseTypeDef = TypedDict(
    "GetHITResponseTypeDef",
    {
        "HIT": "HITTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQualificationScoreRequestRequestTypeDef = TypedDict(
    "GetQualificationScoreRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
        "WorkerId": str,
    },
)

GetQualificationScoreResponseTypeDef = TypedDict(
    "GetQualificationScoreResponseTypeDef",
    {
        "Qualification": "QualificationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQualificationTypeRequestRequestTypeDef = TypedDict(
    "GetQualificationTypeRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
    },
)

GetQualificationTypeResponseTypeDef = TypedDict(
    "GetQualificationTypeResponseTypeDef",
    {
        "QualificationType": "QualificationTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HITLayoutParameterTypeDef = TypedDict(
    "HITLayoutParameterTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

HITTypeDef = TypedDict(
    "HITTypeDef",
    {
        "HITId": NotRequired[str],
        "HITTypeId": NotRequired[str],
        "HITGroupId": NotRequired[str],
        "HITLayoutId": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "Title": NotRequired[str],
        "Description": NotRequired[str],
        "Question": NotRequired[str],
        "Keywords": NotRequired[str],
        "HITStatus": NotRequired[HITStatusType],
        "MaxAssignments": NotRequired[int],
        "Reward": NotRequired[str],
        "AutoApprovalDelayInSeconds": NotRequired[int],
        "Expiration": NotRequired[datetime],
        "AssignmentDurationInSeconds": NotRequired[int],
        "RequesterAnnotation": NotRequired[str],
        "QualificationRequirements": NotRequired[List["QualificationRequirementTypeDef"]],
        "HITReviewStatus": NotRequired[HITReviewStatusType],
        "NumberOfAssignmentsPending": NotRequired[int],
        "NumberOfAssignmentsAvailable": NotRequired[int],
        "NumberOfAssignmentsCompleted": NotRequired[int],
    },
)

ListAssignmentsForHITRequestRequestTypeDef = TypedDict(
    "ListAssignmentsForHITRequestRequestTypeDef",
    {
        "HITId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "AssignmentStatuses": NotRequired[Sequence[AssignmentStatusType]],
    },
)

ListAssignmentsForHITResponseTypeDef = TypedDict(
    "ListAssignmentsForHITResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "Assignments": List["AssignmentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBonusPaymentsRequestRequestTypeDef = TypedDict(
    "ListBonusPaymentsRequestRequestTypeDef",
    {
        "HITId": NotRequired[str],
        "AssignmentId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListBonusPaymentsResponseTypeDef = TypedDict(
    "ListBonusPaymentsResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "BonusPayments": List["BonusPaymentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHITsForQualificationTypeRequestRequestTypeDef = TypedDict(
    "ListHITsForQualificationTypeRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListHITsForQualificationTypeResponseTypeDef = TypedDict(
    "ListHITsForQualificationTypeResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List["HITTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHITsRequestRequestTypeDef = TypedDict(
    "ListHITsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListHITsResponseTypeDef = TypedDict(
    "ListHITsResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List["HITTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQualificationRequestsRequestRequestTypeDef = TypedDict(
    "ListQualificationRequestsRequestRequestTypeDef",
    {
        "QualificationTypeId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListQualificationRequestsResponseTypeDef = TypedDict(
    "ListQualificationRequestsResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "QualificationRequests": List["QualificationRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQualificationTypesRequestRequestTypeDef = TypedDict(
    "ListQualificationTypesRequestRequestTypeDef",
    {
        "MustBeRequestable": bool,
        "Query": NotRequired[str],
        "MustBeOwnedByCaller": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListQualificationTypesResponseTypeDef = TypedDict(
    "ListQualificationTypesResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "QualificationTypes": List["QualificationTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReviewPolicyResultsForHITRequestRequestTypeDef = TypedDict(
    "ListReviewPolicyResultsForHITRequestRequestTypeDef",
    {
        "HITId": str,
        "PolicyLevels": NotRequired[Sequence[ReviewPolicyLevelType]],
        "RetrieveActions": NotRequired[bool],
        "RetrieveResults": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListReviewPolicyResultsForHITResponseTypeDef = TypedDict(
    "ListReviewPolicyResultsForHITResponseTypeDef",
    {
        "HITId": str,
        "AssignmentReviewPolicy": "ReviewPolicyTypeDef",
        "HITReviewPolicy": "ReviewPolicyTypeDef",
        "AssignmentReviewReport": "ReviewReportTypeDef",
        "HITReviewReport": "ReviewReportTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReviewableHITsRequestRequestTypeDef = TypedDict(
    "ListReviewableHITsRequestRequestTypeDef",
    {
        "HITTypeId": NotRequired[str],
        "Status": NotRequired[ReviewableHITStatusType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListReviewableHITsResponseTypeDef = TypedDict(
    "ListReviewableHITsResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List["HITTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkerBlocksRequestRequestTypeDef = TypedDict(
    "ListWorkerBlocksRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListWorkerBlocksResponseTypeDef = TypedDict(
    "ListWorkerBlocksResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "WorkerBlocks": List["WorkerBlockTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkersWithQualificationTypeRequestRequestTypeDef = TypedDict(
    "ListWorkersWithQualificationTypeRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
        "Status": NotRequired[QualificationStatusType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListWorkersWithQualificationTypeResponseTypeDef = TypedDict(
    "ListWorkersWithQualificationTypeResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "Qualifications": List["QualificationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocaleTypeDef = TypedDict(
    "LocaleTypeDef",
    {
        "Country": str,
        "Subdivision": NotRequired[str],
    },
)

NotificationSpecificationTypeDef = TypedDict(
    "NotificationSpecificationTypeDef",
    {
        "Destination": str,
        "Transport": NotificationTransportType,
        "Version": str,
        "EventTypes": Sequence[EventTypeType],
    },
)

NotifyWorkersFailureStatusTypeDef = TypedDict(
    "NotifyWorkersFailureStatusTypeDef",
    {
        "NotifyWorkersFailureCode": NotRequired[NotifyWorkersFailureCodeType],
        "NotifyWorkersFailureMessage": NotRequired[str],
        "WorkerId": NotRequired[str],
    },
)

NotifyWorkersRequestRequestTypeDef = TypedDict(
    "NotifyWorkersRequestRequestTypeDef",
    {
        "Subject": str,
        "MessageText": str,
        "WorkerIds": Sequence[str],
    },
)

NotifyWorkersResponseTypeDef = TypedDict(
    "NotifyWorkersResponseTypeDef",
    {
        "NotifyWorkersFailureStatuses": List["NotifyWorkersFailureStatusTypeDef"],
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

ParameterMapEntryTypeDef = TypedDict(
    "ParameterMapEntryTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)

PolicyParameterTypeDef = TypedDict(
    "PolicyParameterTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
        "MapEntries": NotRequired[Sequence["ParameterMapEntryTypeDef"]],
    },
)

QualificationRequestTypeDef = TypedDict(
    "QualificationRequestTypeDef",
    {
        "QualificationRequestId": NotRequired[str],
        "QualificationTypeId": NotRequired[str],
        "WorkerId": NotRequired[str],
        "Test": NotRequired[str],
        "Answer": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
    },
)

QualificationRequirementTypeDef = TypedDict(
    "QualificationRequirementTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": ComparatorType,
        "IntegerValues": NotRequired[Sequence[int]],
        "LocaleValues": NotRequired[Sequence["LocaleTypeDef"]],
        "RequiredToPreview": NotRequired[bool],
        "ActionsGuarded": NotRequired[HITAccessActionsType],
    },
)

QualificationTypeDef = TypedDict(
    "QualificationTypeDef",
    {
        "QualificationTypeId": NotRequired[str],
        "WorkerId": NotRequired[str],
        "GrantTime": NotRequired[datetime],
        "IntegerValue": NotRequired[int],
        "LocaleValue": NotRequired["LocaleTypeDef"],
        "Status": NotRequired[QualificationStatusType],
    },
)

QualificationTypeTypeDef = TypedDict(
    "QualificationTypeTypeDef",
    {
        "QualificationTypeId": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Keywords": NotRequired[str],
        "QualificationTypeStatus": NotRequired[QualificationTypeStatusType],
        "Test": NotRequired[str],
        "TestDurationInSeconds": NotRequired[int],
        "AnswerKey": NotRequired[str],
        "RetryDelayInSeconds": NotRequired[int],
        "IsRequestable": NotRequired[bool],
        "AutoGranted": NotRequired[bool],
        "AutoGrantedValue": NotRequired[int],
    },
)

RejectAssignmentRequestRequestTypeDef = TypedDict(
    "RejectAssignmentRequestRequestTypeDef",
    {
        "AssignmentId": str,
        "RequesterFeedback": str,
    },
)

RejectQualificationRequestRequestRequestTypeDef = TypedDict(
    "RejectQualificationRequestRequestRequestTypeDef",
    {
        "QualificationRequestId": str,
        "Reason": NotRequired[str],
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

ReviewActionDetailTypeDef = TypedDict(
    "ReviewActionDetailTypeDef",
    {
        "ActionId": NotRequired[str],
        "ActionName": NotRequired[str],
        "TargetId": NotRequired[str],
        "TargetType": NotRequired[str],
        "Status": NotRequired[ReviewActionStatusType],
        "CompleteTime": NotRequired[datetime],
        "Result": NotRequired[str],
        "ErrorCode": NotRequired[str],
    },
)

ReviewPolicyTypeDef = TypedDict(
    "ReviewPolicyTypeDef",
    {
        "PolicyName": str,
        "Parameters": NotRequired[Sequence["PolicyParameterTypeDef"]],
    },
)

ReviewReportTypeDef = TypedDict(
    "ReviewReportTypeDef",
    {
        "ReviewResults": NotRequired[List["ReviewResultDetailTypeDef"]],
        "ReviewActions": NotRequired[List["ReviewActionDetailTypeDef"]],
    },
)

ReviewResultDetailTypeDef = TypedDict(
    "ReviewResultDetailTypeDef",
    {
        "ActionId": NotRequired[str],
        "SubjectId": NotRequired[str],
        "SubjectType": NotRequired[str],
        "QuestionId": NotRequired[str],
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

SendBonusRequestRequestTypeDef = TypedDict(
    "SendBonusRequestRequestTypeDef",
    {
        "WorkerId": str,
        "BonusAmount": str,
        "AssignmentId": str,
        "Reason": str,
        "UniqueRequestToken": NotRequired[str],
    },
)

SendTestEventNotificationRequestRequestTypeDef = TypedDict(
    "SendTestEventNotificationRequestRequestTypeDef",
    {
        "Notification": "NotificationSpecificationTypeDef",
        "TestEventType": EventTypeType,
    },
)

UpdateExpirationForHITRequestRequestTypeDef = TypedDict(
    "UpdateExpirationForHITRequestRequestTypeDef",
    {
        "HITId": str,
        "ExpireAt": Union[datetime, str],
    },
)

UpdateHITReviewStatusRequestRequestTypeDef = TypedDict(
    "UpdateHITReviewStatusRequestRequestTypeDef",
    {
        "HITId": str,
        "Revert": NotRequired[bool],
    },
)

UpdateHITTypeOfHITRequestRequestTypeDef = TypedDict(
    "UpdateHITTypeOfHITRequestRequestTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
    },
)

UpdateNotificationSettingsRequestRequestTypeDef = TypedDict(
    "UpdateNotificationSettingsRequestRequestTypeDef",
    {
        "HITTypeId": str,
        "Notification": NotRequired["NotificationSpecificationTypeDef"],
        "Active": NotRequired[bool],
    },
)

UpdateQualificationTypeRequestRequestTypeDef = TypedDict(
    "UpdateQualificationTypeRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
        "Description": NotRequired[str],
        "QualificationTypeStatus": NotRequired[QualificationTypeStatusType],
        "Test": NotRequired[str],
        "AnswerKey": NotRequired[str],
        "TestDurationInSeconds": NotRequired[int],
        "RetryDelayInSeconds": NotRequired[int],
        "AutoGranted": NotRequired[bool],
        "AutoGrantedValue": NotRequired[int],
    },
)

UpdateQualificationTypeResponseTypeDef = TypedDict(
    "UpdateQualificationTypeResponseTypeDef",
    {
        "QualificationType": "QualificationTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WorkerBlockTypeDef = TypedDict(
    "WorkerBlockTypeDef",
    {
        "WorkerId": NotRequired[str],
        "Reason": NotRequired[str],
    },
)
