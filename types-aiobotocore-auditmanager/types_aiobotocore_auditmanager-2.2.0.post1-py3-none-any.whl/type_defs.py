"""
Type annotations for auditmanager service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_auditmanager/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_auditmanager.type_defs import AWSAccountTypeDef

    data: AWSAccountTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AccountStatusType,
    ActionEnumType,
    AssessmentReportStatusType,
    AssessmentStatusType,
    ControlResponseType,
    ControlSetStatusType,
    ControlStatusType,
    ControlTypeType,
    DelegationStatusType,
    FrameworkTypeType,
    ObjectTypeEnumType,
    RoleTypeType,
    SettingAttributeType,
    ShareRequestActionType,
    ShareRequestStatusType,
    ShareRequestTypeType,
    SourceFrequencyType,
    SourceSetUpOptionType,
    SourceTypeType,
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
    "AWSAccountTypeDef",
    "AWSServiceTypeDef",
    "AssessmentControlSetTypeDef",
    "AssessmentControlTypeDef",
    "AssessmentEvidenceFolderTypeDef",
    "AssessmentFrameworkMetadataTypeDef",
    "AssessmentFrameworkShareRequestTypeDef",
    "AssessmentFrameworkTypeDef",
    "AssessmentMetadataItemTypeDef",
    "AssessmentMetadataTypeDef",
    "AssessmentReportEvidenceErrorTypeDef",
    "AssessmentReportMetadataTypeDef",
    "AssessmentReportTypeDef",
    "AssessmentReportsDestinationTypeDef",
    "AssessmentTypeDef",
    "AssociateAssessmentReportEvidenceFolderRequestRequestTypeDef",
    "BatchAssociateAssessmentReportEvidenceRequestRequestTypeDef",
    "BatchAssociateAssessmentReportEvidenceResponseTypeDef",
    "BatchCreateDelegationByAssessmentErrorTypeDef",
    "BatchCreateDelegationByAssessmentRequestRequestTypeDef",
    "BatchCreateDelegationByAssessmentResponseTypeDef",
    "BatchDeleteDelegationByAssessmentErrorTypeDef",
    "BatchDeleteDelegationByAssessmentRequestRequestTypeDef",
    "BatchDeleteDelegationByAssessmentResponseTypeDef",
    "BatchDisassociateAssessmentReportEvidenceRequestRequestTypeDef",
    "BatchDisassociateAssessmentReportEvidenceResponseTypeDef",
    "BatchImportEvidenceToAssessmentControlErrorTypeDef",
    "BatchImportEvidenceToAssessmentControlRequestRequestTypeDef",
    "BatchImportEvidenceToAssessmentControlResponseTypeDef",
    "ChangeLogTypeDef",
    "ControlCommentTypeDef",
    "ControlDomainInsightsTypeDef",
    "ControlInsightsMetadataByAssessmentItemTypeDef",
    "ControlInsightsMetadataItemTypeDef",
    "ControlMappingSourceTypeDef",
    "ControlMetadataTypeDef",
    "ControlSetTypeDef",
    "ControlTypeDef",
    "CreateAssessmentFrameworkControlSetTypeDef",
    "CreateAssessmentFrameworkControlTypeDef",
    "CreateAssessmentFrameworkRequestRequestTypeDef",
    "CreateAssessmentFrameworkResponseTypeDef",
    "CreateAssessmentReportRequestRequestTypeDef",
    "CreateAssessmentReportResponseTypeDef",
    "CreateAssessmentRequestRequestTypeDef",
    "CreateAssessmentResponseTypeDef",
    "CreateControlMappingSourceTypeDef",
    "CreateControlRequestRequestTypeDef",
    "CreateControlResponseTypeDef",
    "CreateDelegationRequestTypeDef",
    "DelegationMetadataTypeDef",
    "DelegationTypeDef",
    "DeleteAssessmentFrameworkRequestRequestTypeDef",
    "DeleteAssessmentFrameworkShareRequestRequestTypeDef",
    "DeleteAssessmentReportRequestRequestTypeDef",
    "DeleteAssessmentRequestRequestTypeDef",
    "DeleteControlRequestRequestTypeDef",
    "DeregisterAccountResponseTypeDef",
    "DeregisterOrganizationAdminAccountRequestRequestTypeDef",
    "DisassociateAssessmentReportEvidenceFolderRequestRequestTypeDef",
    "EvidenceInsightsTypeDef",
    "EvidenceTypeDef",
    "FrameworkMetadataTypeDef",
    "FrameworkTypeDef",
    "GetAccountStatusResponseTypeDef",
    "GetAssessmentFrameworkRequestRequestTypeDef",
    "GetAssessmentFrameworkResponseTypeDef",
    "GetAssessmentReportUrlRequestRequestTypeDef",
    "GetAssessmentReportUrlResponseTypeDef",
    "GetAssessmentRequestRequestTypeDef",
    "GetAssessmentResponseTypeDef",
    "GetChangeLogsRequestRequestTypeDef",
    "GetChangeLogsResponseTypeDef",
    "GetControlRequestRequestTypeDef",
    "GetControlResponseTypeDef",
    "GetDelegationsRequestRequestTypeDef",
    "GetDelegationsResponseTypeDef",
    "GetEvidenceByEvidenceFolderRequestRequestTypeDef",
    "GetEvidenceByEvidenceFolderResponseTypeDef",
    "GetEvidenceFolderRequestRequestTypeDef",
    "GetEvidenceFolderResponseTypeDef",
    "GetEvidenceFoldersByAssessmentControlRequestRequestTypeDef",
    "GetEvidenceFoldersByAssessmentControlResponseTypeDef",
    "GetEvidenceFoldersByAssessmentRequestRequestTypeDef",
    "GetEvidenceFoldersByAssessmentResponseTypeDef",
    "GetEvidenceRequestRequestTypeDef",
    "GetEvidenceResponseTypeDef",
    "GetInsightsByAssessmentRequestRequestTypeDef",
    "GetInsightsByAssessmentResponseTypeDef",
    "GetInsightsResponseTypeDef",
    "GetOrganizationAdminAccountResponseTypeDef",
    "GetServicesInScopeResponseTypeDef",
    "GetSettingsRequestRequestTypeDef",
    "GetSettingsResponseTypeDef",
    "InsightsByAssessmentTypeDef",
    "InsightsTypeDef",
    "ListAssessmentControlInsightsByControlDomainRequestRequestTypeDef",
    "ListAssessmentControlInsightsByControlDomainResponseTypeDef",
    "ListAssessmentFrameworkShareRequestsRequestRequestTypeDef",
    "ListAssessmentFrameworkShareRequestsResponseTypeDef",
    "ListAssessmentFrameworksRequestRequestTypeDef",
    "ListAssessmentFrameworksResponseTypeDef",
    "ListAssessmentReportsRequestRequestTypeDef",
    "ListAssessmentReportsResponseTypeDef",
    "ListAssessmentsRequestRequestTypeDef",
    "ListAssessmentsResponseTypeDef",
    "ListControlDomainInsightsByAssessmentRequestRequestTypeDef",
    "ListControlDomainInsightsByAssessmentResponseTypeDef",
    "ListControlDomainInsightsRequestRequestTypeDef",
    "ListControlDomainInsightsResponseTypeDef",
    "ListControlInsightsByControlDomainRequestRequestTypeDef",
    "ListControlInsightsByControlDomainResponseTypeDef",
    "ListControlsRequestRequestTypeDef",
    "ListControlsResponseTypeDef",
    "ListKeywordsForDataSourceRequestRequestTypeDef",
    "ListKeywordsForDataSourceResponseTypeDef",
    "ListNotificationsRequestRequestTypeDef",
    "ListNotificationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ManualEvidenceTypeDef",
    "NotificationTypeDef",
    "RegisterAccountRequestRequestTypeDef",
    "RegisterAccountResponseTypeDef",
    "RegisterOrganizationAdminAccountRequestRequestTypeDef",
    "RegisterOrganizationAdminAccountResponseTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RoleTypeDef",
    "ScopeTypeDef",
    "ServiceMetadataTypeDef",
    "SettingsTypeDef",
    "SourceKeywordTypeDef",
    "StartAssessmentFrameworkShareRequestRequestTypeDef",
    "StartAssessmentFrameworkShareResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "URLTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAssessmentControlRequestRequestTypeDef",
    "UpdateAssessmentControlResponseTypeDef",
    "UpdateAssessmentControlSetStatusRequestRequestTypeDef",
    "UpdateAssessmentControlSetStatusResponseTypeDef",
    "UpdateAssessmentFrameworkControlSetTypeDef",
    "UpdateAssessmentFrameworkRequestRequestTypeDef",
    "UpdateAssessmentFrameworkResponseTypeDef",
    "UpdateAssessmentFrameworkShareRequestRequestTypeDef",
    "UpdateAssessmentFrameworkShareResponseTypeDef",
    "UpdateAssessmentRequestRequestTypeDef",
    "UpdateAssessmentResponseTypeDef",
    "UpdateAssessmentStatusRequestRequestTypeDef",
    "UpdateAssessmentStatusResponseTypeDef",
    "UpdateControlRequestRequestTypeDef",
    "UpdateControlResponseTypeDef",
    "UpdateSettingsRequestRequestTypeDef",
    "UpdateSettingsResponseTypeDef",
    "ValidateAssessmentReportIntegrityRequestRequestTypeDef",
    "ValidateAssessmentReportIntegrityResponseTypeDef",
)

AWSAccountTypeDef = TypedDict(
    "AWSAccountTypeDef",
    {
        "id": NotRequired[str],
        "emailAddress": NotRequired[str],
        "name": NotRequired[str],
    },
)

AWSServiceTypeDef = TypedDict(
    "AWSServiceTypeDef",
    {
        "serviceName": NotRequired[str],
    },
)

AssessmentControlSetTypeDef = TypedDict(
    "AssessmentControlSetTypeDef",
    {
        "id": NotRequired[str],
        "description": NotRequired[str],
        "status": NotRequired[ControlSetStatusType],
        "roles": NotRequired[List["RoleTypeDef"]],
        "controls": NotRequired[List["AssessmentControlTypeDef"]],
        "delegations": NotRequired[List["DelegationTypeDef"]],
        "systemEvidenceCount": NotRequired[int],
        "manualEvidenceCount": NotRequired[int],
    },
)

AssessmentControlTypeDef = TypedDict(
    "AssessmentControlTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "status": NotRequired[ControlStatusType],
        "response": NotRequired[ControlResponseType],
        "comments": NotRequired[List["ControlCommentTypeDef"]],
        "evidenceSources": NotRequired[List[str]],
        "evidenceCount": NotRequired[int],
        "assessmentReportEvidenceCount": NotRequired[int],
    },
)

AssessmentEvidenceFolderTypeDef = TypedDict(
    "AssessmentEvidenceFolderTypeDef",
    {
        "name": NotRequired[str],
        "date": NotRequired[datetime],
        "assessmentId": NotRequired[str],
        "controlSetId": NotRequired[str],
        "controlId": NotRequired[str],
        "id": NotRequired[str],
        "dataSource": NotRequired[str],
        "author": NotRequired[str],
        "totalEvidence": NotRequired[int],
        "assessmentReportSelectionCount": NotRequired[int],
        "controlName": NotRequired[str],
        "evidenceResourcesIncludedCount": NotRequired[int],
        "evidenceByTypeConfigurationDataCount": NotRequired[int],
        "evidenceByTypeManualCount": NotRequired[int],
        "evidenceByTypeComplianceCheckCount": NotRequired[int],
        "evidenceByTypeComplianceCheckIssuesCount": NotRequired[int],
        "evidenceByTypeUserActivityCount": NotRequired[int],
        "evidenceAwsServiceSourceCount": NotRequired[int],
    },
)

AssessmentFrameworkMetadataTypeDef = TypedDict(
    "AssessmentFrameworkMetadataTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "type": NotRequired[FrameworkTypeType],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "logo": NotRequired[str],
        "complianceType": NotRequired[str],
        "controlsCount": NotRequired[int],
        "controlSetsCount": NotRequired[int],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
    },
)

AssessmentFrameworkShareRequestTypeDef = TypedDict(
    "AssessmentFrameworkShareRequestTypeDef",
    {
        "id": NotRequired[str],
        "frameworkId": NotRequired[str],
        "frameworkName": NotRequired[str],
        "frameworkDescription": NotRequired[str],
        "status": NotRequired[ShareRequestStatusType],
        "sourceAccount": NotRequired[str],
        "destinationAccount": NotRequired[str],
        "destinationRegion": NotRequired[str],
        "expirationTime": NotRequired[datetime],
        "creationTime": NotRequired[datetime],
        "lastUpdated": NotRequired[datetime],
        "comment": NotRequired[str],
        "standardControlsCount": NotRequired[int],
        "customControlsCount": NotRequired[int],
        "complianceType": NotRequired[str],
    },
)

AssessmentFrameworkTypeDef = TypedDict(
    "AssessmentFrameworkTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "metadata": NotRequired["FrameworkMetadataTypeDef"],
        "controlSets": NotRequired[List["AssessmentControlSetTypeDef"]],
    },
)

AssessmentMetadataItemTypeDef = TypedDict(
    "AssessmentMetadataItemTypeDef",
    {
        "name": NotRequired[str],
        "id": NotRequired[str],
        "complianceType": NotRequired[str],
        "status": NotRequired[AssessmentStatusType],
        "roles": NotRequired[List["RoleTypeDef"]],
        "delegations": NotRequired[List["DelegationTypeDef"]],
        "creationTime": NotRequired[datetime],
        "lastUpdated": NotRequired[datetime],
    },
)

AssessmentMetadataTypeDef = TypedDict(
    "AssessmentMetadataTypeDef",
    {
        "name": NotRequired[str],
        "id": NotRequired[str],
        "description": NotRequired[str],
        "complianceType": NotRequired[str],
        "status": NotRequired[AssessmentStatusType],
        "assessmentReportsDestination": NotRequired["AssessmentReportsDestinationTypeDef"],
        "scope": NotRequired["ScopeTypeDef"],
        "roles": NotRequired[List["RoleTypeDef"]],
        "delegations": NotRequired[List["DelegationTypeDef"]],
        "creationTime": NotRequired[datetime],
        "lastUpdated": NotRequired[datetime],
    },
)

AssessmentReportEvidenceErrorTypeDef = TypedDict(
    "AssessmentReportEvidenceErrorTypeDef",
    {
        "evidenceId": NotRequired[str],
        "errorCode": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)

AssessmentReportMetadataTypeDef = TypedDict(
    "AssessmentReportMetadataTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "assessmentId": NotRequired[str],
        "assessmentName": NotRequired[str],
        "author": NotRequired[str],
        "status": NotRequired[AssessmentReportStatusType],
        "creationTime": NotRequired[datetime],
    },
)

AssessmentReportTypeDef = TypedDict(
    "AssessmentReportTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "awsAccountId": NotRequired[str],
        "assessmentId": NotRequired[str],
        "assessmentName": NotRequired[str],
        "author": NotRequired[str],
        "status": NotRequired[AssessmentReportStatusType],
        "creationTime": NotRequired[datetime],
    },
)

AssessmentReportsDestinationTypeDef = TypedDict(
    "AssessmentReportsDestinationTypeDef",
    {
        "destinationType": NotRequired[Literal["S3"]],
        "destination": NotRequired[str],
    },
)

AssessmentTypeDef = TypedDict(
    "AssessmentTypeDef",
    {
        "arn": NotRequired[str],
        "awsAccount": NotRequired["AWSAccountTypeDef"],
        "metadata": NotRequired["AssessmentMetadataTypeDef"],
        "framework": NotRequired["AssessmentFrameworkTypeDef"],
        "tags": NotRequired[Dict[str, str]],
    },
)

AssociateAssessmentReportEvidenceFolderRequestRequestTypeDef = TypedDict(
    "AssociateAssessmentReportEvidenceFolderRequestRequestTypeDef",
    {
        "assessmentId": str,
        "evidenceFolderId": str,
    },
)

BatchAssociateAssessmentReportEvidenceRequestRequestTypeDef = TypedDict(
    "BatchAssociateAssessmentReportEvidenceRequestRequestTypeDef",
    {
        "assessmentId": str,
        "evidenceFolderId": str,
        "evidenceIds": Sequence[str],
    },
)

BatchAssociateAssessmentReportEvidenceResponseTypeDef = TypedDict(
    "BatchAssociateAssessmentReportEvidenceResponseTypeDef",
    {
        "evidenceIds": List[str],
        "errors": List["AssessmentReportEvidenceErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchCreateDelegationByAssessmentErrorTypeDef = TypedDict(
    "BatchCreateDelegationByAssessmentErrorTypeDef",
    {
        "createDelegationRequest": NotRequired["CreateDelegationRequestTypeDef"],
        "errorCode": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)

BatchCreateDelegationByAssessmentRequestRequestTypeDef = TypedDict(
    "BatchCreateDelegationByAssessmentRequestRequestTypeDef",
    {
        "createDelegationRequests": Sequence["CreateDelegationRequestTypeDef"],
        "assessmentId": str,
    },
)

BatchCreateDelegationByAssessmentResponseTypeDef = TypedDict(
    "BatchCreateDelegationByAssessmentResponseTypeDef",
    {
        "delegations": List["DelegationTypeDef"],
        "errors": List["BatchCreateDelegationByAssessmentErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteDelegationByAssessmentErrorTypeDef = TypedDict(
    "BatchDeleteDelegationByAssessmentErrorTypeDef",
    {
        "delegationId": NotRequired[str],
        "errorCode": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)

BatchDeleteDelegationByAssessmentRequestRequestTypeDef = TypedDict(
    "BatchDeleteDelegationByAssessmentRequestRequestTypeDef",
    {
        "delegationIds": Sequence[str],
        "assessmentId": str,
    },
)

BatchDeleteDelegationByAssessmentResponseTypeDef = TypedDict(
    "BatchDeleteDelegationByAssessmentResponseTypeDef",
    {
        "errors": List["BatchDeleteDelegationByAssessmentErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDisassociateAssessmentReportEvidenceRequestRequestTypeDef = TypedDict(
    "BatchDisassociateAssessmentReportEvidenceRequestRequestTypeDef",
    {
        "assessmentId": str,
        "evidenceFolderId": str,
        "evidenceIds": Sequence[str],
    },
)

BatchDisassociateAssessmentReportEvidenceResponseTypeDef = TypedDict(
    "BatchDisassociateAssessmentReportEvidenceResponseTypeDef",
    {
        "evidenceIds": List[str],
        "errors": List["AssessmentReportEvidenceErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchImportEvidenceToAssessmentControlErrorTypeDef = TypedDict(
    "BatchImportEvidenceToAssessmentControlErrorTypeDef",
    {
        "manualEvidence": NotRequired["ManualEvidenceTypeDef"],
        "errorCode": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)

BatchImportEvidenceToAssessmentControlRequestRequestTypeDef = TypedDict(
    "BatchImportEvidenceToAssessmentControlRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "controlId": str,
        "manualEvidence": Sequence["ManualEvidenceTypeDef"],
    },
)

BatchImportEvidenceToAssessmentControlResponseTypeDef = TypedDict(
    "BatchImportEvidenceToAssessmentControlResponseTypeDef",
    {
        "errors": List["BatchImportEvidenceToAssessmentControlErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChangeLogTypeDef = TypedDict(
    "ChangeLogTypeDef",
    {
        "objectType": NotRequired[ObjectTypeEnumType],
        "objectName": NotRequired[str],
        "action": NotRequired[ActionEnumType],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
    },
)

ControlCommentTypeDef = TypedDict(
    "ControlCommentTypeDef",
    {
        "authorName": NotRequired[str],
        "commentBody": NotRequired[str],
        "postedDate": NotRequired[datetime],
    },
)

ControlDomainInsightsTypeDef = TypedDict(
    "ControlDomainInsightsTypeDef",
    {
        "name": NotRequired[str],
        "id": NotRequired[str],
        "controlsCountByNoncompliantEvidence": NotRequired[int],
        "totalControlsCount": NotRequired[int],
        "evidenceInsights": NotRequired["EvidenceInsightsTypeDef"],
        "lastUpdated": NotRequired[datetime],
    },
)

ControlInsightsMetadataByAssessmentItemTypeDef = TypedDict(
    "ControlInsightsMetadataByAssessmentItemTypeDef",
    {
        "name": NotRequired[str],
        "id": NotRequired[str],
        "evidenceInsights": NotRequired["EvidenceInsightsTypeDef"],
        "controlSetName": NotRequired[str],
        "lastUpdated": NotRequired[datetime],
    },
)

ControlInsightsMetadataItemTypeDef = TypedDict(
    "ControlInsightsMetadataItemTypeDef",
    {
        "name": NotRequired[str],
        "id": NotRequired[str],
        "evidenceInsights": NotRequired["EvidenceInsightsTypeDef"],
        "lastUpdated": NotRequired[datetime],
    },
)

ControlMappingSourceTypeDef = TypedDict(
    "ControlMappingSourceTypeDef",
    {
        "sourceId": NotRequired[str],
        "sourceName": NotRequired[str],
        "sourceDescription": NotRequired[str],
        "sourceSetUpOption": NotRequired[SourceSetUpOptionType],
        "sourceType": NotRequired[SourceTypeType],
        "sourceKeyword": NotRequired["SourceKeywordTypeDef"],
        "sourceFrequency": NotRequired[SourceFrequencyType],
        "troubleshootingText": NotRequired[str],
    },
)

ControlMetadataTypeDef = TypedDict(
    "ControlMetadataTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "controlSources": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
    },
)

ControlSetTypeDef = TypedDict(
    "ControlSetTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "controls": NotRequired[List["ControlTypeDef"]],
    },
)

ControlTypeDef = TypedDict(
    "ControlTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "type": NotRequired[ControlTypeType],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "testingInformation": NotRequired[str],
        "actionPlanTitle": NotRequired[str],
        "actionPlanInstructions": NotRequired[str],
        "controlSources": NotRequired[str],
        "controlMappingSources": NotRequired[List["ControlMappingSourceTypeDef"]],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "lastUpdatedBy": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

CreateAssessmentFrameworkControlSetTypeDef = TypedDict(
    "CreateAssessmentFrameworkControlSetTypeDef",
    {
        "name": str,
        "controls": NotRequired[Sequence["CreateAssessmentFrameworkControlTypeDef"]],
    },
)

CreateAssessmentFrameworkControlTypeDef = TypedDict(
    "CreateAssessmentFrameworkControlTypeDef",
    {
        "id": str,
    },
)

CreateAssessmentFrameworkRequestRequestTypeDef = TypedDict(
    "CreateAssessmentFrameworkRequestRequestTypeDef",
    {
        "name": str,
        "controlSets": Sequence["CreateAssessmentFrameworkControlSetTypeDef"],
        "description": NotRequired[str],
        "complianceType": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateAssessmentFrameworkResponseTypeDef = TypedDict(
    "CreateAssessmentFrameworkResponseTypeDef",
    {
        "framework": "FrameworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAssessmentReportRequestRequestTypeDef = TypedDict(
    "CreateAssessmentReportRequestRequestTypeDef",
    {
        "name": str,
        "assessmentId": str,
        "description": NotRequired[str],
    },
)

CreateAssessmentReportResponseTypeDef = TypedDict(
    "CreateAssessmentReportResponseTypeDef",
    {
        "assessmentReport": "AssessmentReportTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAssessmentRequestRequestTypeDef = TypedDict(
    "CreateAssessmentRequestRequestTypeDef",
    {
        "name": str,
        "assessmentReportsDestination": "AssessmentReportsDestinationTypeDef",
        "scope": "ScopeTypeDef",
        "roles": Sequence["RoleTypeDef"],
        "frameworkId": str,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateAssessmentResponseTypeDef = TypedDict(
    "CreateAssessmentResponseTypeDef",
    {
        "assessment": "AssessmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateControlMappingSourceTypeDef = TypedDict(
    "CreateControlMappingSourceTypeDef",
    {
        "sourceName": NotRequired[str],
        "sourceDescription": NotRequired[str],
        "sourceSetUpOption": NotRequired[SourceSetUpOptionType],
        "sourceType": NotRequired[SourceTypeType],
        "sourceKeyword": NotRequired["SourceKeywordTypeDef"],
        "sourceFrequency": NotRequired[SourceFrequencyType],
        "troubleshootingText": NotRequired[str],
    },
)

CreateControlRequestRequestTypeDef = TypedDict(
    "CreateControlRequestRequestTypeDef",
    {
        "name": str,
        "controlMappingSources": Sequence["CreateControlMappingSourceTypeDef"],
        "description": NotRequired[str],
        "testingInformation": NotRequired[str],
        "actionPlanTitle": NotRequired[str],
        "actionPlanInstructions": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateControlResponseTypeDef = TypedDict(
    "CreateControlResponseTypeDef",
    {
        "control": "ControlTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDelegationRequestTypeDef = TypedDict(
    "CreateDelegationRequestTypeDef",
    {
        "comment": NotRequired[str],
        "controlSetId": NotRequired[str],
        "roleArn": NotRequired[str],
        "roleType": NotRequired[RoleTypeType],
    },
)

DelegationMetadataTypeDef = TypedDict(
    "DelegationMetadataTypeDef",
    {
        "id": NotRequired[str],
        "assessmentName": NotRequired[str],
        "assessmentId": NotRequired[str],
        "status": NotRequired[DelegationStatusType],
        "roleArn": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "controlSetName": NotRequired[str],
    },
)

DelegationTypeDef = TypedDict(
    "DelegationTypeDef",
    {
        "id": NotRequired[str],
        "assessmentName": NotRequired[str],
        "assessmentId": NotRequired[str],
        "status": NotRequired[DelegationStatusType],
        "roleArn": NotRequired[str],
        "roleType": NotRequired[RoleTypeType],
        "creationTime": NotRequired[datetime],
        "lastUpdated": NotRequired[datetime],
        "controlSetId": NotRequired[str],
        "comment": NotRequired[str],
        "createdBy": NotRequired[str],
    },
)

DeleteAssessmentFrameworkRequestRequestTypeDef = TypedDict(
    "DeleteAssessmentFrameworkRequestRequestTypeDef",
    {
        "frameworkId": str,
    },
)

DeleteAssessmentFrameworkShareRequestRequestTypeDef = TypedDict(
    "DeleteAssessmentFrameworkShareRequestRequestTypeDef",
    {
        "requestId": str,
        "requestType": ShareRequestTypeType,
    },
)

DeleteAssessmentReportRequestRequestTypeDef = TypedDict(
    "DeleteAssessmentReportRequestRequestTypeDef",
    {
        "assessmentId": str,
        "assessmentReportId": str,
    },
)

DeleteAssessmentRequestRequestTypeDef = TypedDict(
    "DeleteAssessmentRequestRequestTypeDef",
    {
        "assessmentId": str,
    },
)

DeleteControlRequestRequestTypeDef = TypedDict(
    "DeleteControlRequestRequestTypeDef",
    {
        "controlId": str,
    },
)

DeregisterAccountResponseTypeDef = TypedDict(
    "DeregisterAccountResponseTypeDef",
    {
        "status": AccountStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "DeregisterOrganizationAdminAccountRequestRequestTypeDef",
    {
        "adminAccountId": NotRequired[str],
    },
)

DisassociateAssessmentReportEvidenceFolderRequestRequestTypeDef = TypedDict(
    "DisassociateAssessmentReportEvidenceFolderRequestRequestTypeDef",
    {
        "assessmentId": str,
        "evidenceFolderId": str,
    },
)

EvidenceInsightsTypeDef = TypedDict(
    "EvidenceInsightsTypeDef",
    {
        "noncompliantEvidenceCount": NotRequired[int],
        "compliantEvidenceCount": NotRequired[int],
        "inconclusiveEvidenceCount": NotRequired[int],
    },
)

EvidenceTypeDef = TypedDict(
    "EvidenceTypeDef",
    {
        "dataSource": NotRequired[str],
        "evidenceAwsAccountId": NotRequired[str],
        "time": NotRequired[datetime],
        "eventSource": NotRequired[str],
        "eventName": NotRequired[str],
        "evidenceByType": NotRequired[str],
        "resourcesIncluded": NotRequired[List["ResourceTypeDef"]],
        "attributes": NotRequired[Dict[str, str]],
        "iamId": NotRequired[str],
        "complianceCheck": NotRequired[str],
        "awsOrganization": NotRequired[str],
        "awsAccountId": NotRequired[str],
        "evidenceFolderId": NotRequired[str],
        "id": NotRequired[str],
        "assessmentReportSelection": NotRequired[str],
    },
)

FrameworkMetadataTypeDef = TypedDict(
    "FrameworkMetadataTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "logo": NotRequired[str],
        "complianceType": NotRequired[str],
    },
)

FrameworkTypeDef = TypedDict(
    "FrameworkTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[FrameworkTypeType],
        "complianceType": NotRequired[str],
        "description": NotRequired[str],
        "logo": NotRequired[str],
        "controlSources": NotRequired[str],
        "controlSets": NotRequired[List["ControlSetTypeDef"]],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "lastUpdatedBy": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

GetAccountStatusResponseTypeDef = TypedDict(
    "GetAccountStatusResponseTypeDef",
    {
        "status": AccountStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssessmentFrameworkRequestRequestTypeDef = TypedDict(
    "GetAssessmentFrameworkRequestRequestTypeDef",
    {
        "frameworkId": str,
    },
)

GetAssessmentFrameworkResponseTypeDef = TypedDict(
    "GetAssessmentFrameworkResponseTypeDef",
    {
        "framework": "FrameworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssessmentReportUrlRequestRequestTypeDef = TypedDict(
    "GetAssessmentReportUrlRequestRequestTypeDef",
    {
        "assessmentReportId": str,
        "assessmentId": str,
    },
)

GetAssessmentReportUrlResponseTypeDef = TypedDict(
    "GetAssessmentReportUrlResponseTypeDef",
    {
        "preSignedUrl": "URLTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssessmentRequestRequestTypeDef = TypedDict(
    "GetAssessmentRequestRequestTypeDef",
    {
        "assessmentId": str,
    },
)

GetAssessmentResponseTypeDef = TypedDict(
    "GetAssessmentResponseTypeDef",
    {
        "assessment": "AssessmentTypeDef",
        "userRole": "RoleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChangeLogsRequestRequestTypeDef = TypedDict(
    "GetChangeLogsRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": NotRequired[str],
        "controlId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetChangeLogsResponseTypeDef = TypedDict(
    "GetChangeLogsResponseTypeDef",
    {
        "changeLogs": List["ChangeLogTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetControlRequestRequestTypeDef = TypedDict(
    "GetControlRequestRequestTypeDef",
    {
        "controlId": str,
    },
)

GetControlResponseTypeDef = TypedDict(
    "GetControlResponseTypeDef",
    {
        "control": "ControlTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDelegationsRequestRequestTypeDef = TypedDict(
    "GetDelegationsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetDelegationsResponseTypeDef = TypedDict(
    "GetDelegationsResponseTypeDef",
    {
        "delegations": List["DelegationMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEvidenceByEvidenceFolderRequestRequestTypeDef = TypedDict(
    "GetEvidenceByEvidenceFolderRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "evidenceFolderId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetEvidenceByEvidenceFolderResponseTypeDef = TypedDict(
    "GetEvidenceByEvidenceFolderResponseTypeDef",
    {
        "evidence": List["EvidenceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEvidenceFolderRequestRequestTypeDef = TypedDict(
    "GetEvidenceFolderRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "evidenceFolderId": str,
    },
)

GetEvidenceFolderResponseTypeDef = TypedDict(
    "GetEvidenceFolderResponseTypeDef",
    {
        "evidenceFolder": "AssessmentEvidenceFolderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEvidenceFoldersByAssessmentControlRequestRequestTypeDef = TypedDict(
    "GetEvidenceFoldersByAssessmentControlRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "controlId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetEvidenceFoldersByAssessmentControlResponseTypeDef = TypedDict(
    "GetEvidenceFoldersByAssessmentControlResponseTypeDef",
    {
        "evidenceFolders": List["AssessmentEvidenceFolderTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEvidenceFoldersByAssessmentRequestRequestTypeDef = TypedDict(
    "GetEvidenceFoldersByAssessmentRequestRequestTypeDef",
    {
        "assessmentId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetEvidenceFoldersByAssessmentResponseTypeDef = TypedDict(
    "GetEvidenceFoldersByAssessmentResponseTypeDef",
    {
        "evidenceFolders": List["AssessmentEvidenceFolderTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEvidenceRequestRequestTypeDef = TypedDict(
    "GetEvidenceRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "evidenceFolderId": str,
        "evidenceId": str,
    },
)

GetEvidenceResponseTypeDef = TypedDict(
    "GetEvidenceResponseTypeDef",
    {
        "evidence": "EvidenceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInsightsByAssessmentRequestRequestTypeDef = TypedDict(
    "GetInsightsByAssessmentRequestRequestTypeDef",
    {
        "assessmentId": str,
    },
)

GetInsightsByAssessmentResponseTypeDef = TypedDict(
    "GetInsightsByAssessmentResponseTypeDef",
    {
        "insights": "InsightsByAssessmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInsightsResponseTypeDef = TypedDict(
    "GetInsightsResponseTypeDef",
    {
        "insights": "InsightsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOrganizationAdminAccountResponseTypeDef = TypedDict(
    "GetOrganizationAdminAccountResponseTypeDef",
    {
        "adminAccountId": str,
        "organizationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServicesInScopeResponseTypeDef = TypedDict(
    "GetServicesInScopeResponseTypeDef",
    {
        "serviceMetadata": List["ServiceMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSettingsRequestRequestTypeDef = TypedDict(
    "GetSettingsRequestRequestTypeDef",
    {
        "attribute": SettingAttributeType,
    },
)

GetSettingsResponseTypeDef = TypedDict(
    "GetSettingsResponseTypeDef",
    {
        "settings": "SettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InsightsByAssessmentTypeDef = TypedDict(
    "InsightsByAssessmentTypeDef",
    {
        "noncompliantEvidenceCount": NotRequired[int],
        "compliantEvidenceCount": NotRequired[int],
        "inconclusiveEvidenceCount": NotRequired[int],
        "assessmentControlsCountByNoncompliantEvidence": NotRequired[int],
        "totalAssessmentControlsCount": NotRequired[int],
        "lastUpdated": NotRequired[datetime],
    },
)

InsightsTypeDef = TypedDict(
    "InsightsTypeDef",
    {
        "activeAssessmentsCount": NotRequired[int],
        "noncompliantEvidenceCount": NotRequired[int],
        "compliantEvidenceCount": NotRequired[int],
        "inconclusiveEvidenceCount": NotRequired[int],
        "assessmentControlsCountByNoncompliantEvidence": NotRequired[int],
        "totalAssessmentControlsCount": NotRequired[int],
        "lastUpdated": NotRequired[datetime],
    },
)

ListAssessmentControlInsightsByControlDomainRequestRequestTypeDef = TypedDict(
    "ListAssessmentControlInsightsByControlDomainRequestRequestTypeDef",
    {
        "controlDomainId": str,
        "assessmentId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAssessmentControlInsightsByControlDomainResponseTypeDef = TypedDict(
    "ListAssessmentControlInsightsByControlDomainResponseTypeDef",
    {
        "controlInsightsByAssessment": List["ControlInsightsMetadataByAssessmentItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssessmentFrameworkShareRequestsRequestRequestTypeDef = TypedDict(
    "ListAssessmentFrameworkShareRequestsRequestRequestTypeDef",
    {
        "requestType": ShareRequestTypeType,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAssessmentFrameworkShareRequestsResponseTypeDef = TypedDict(
    "ListAssessmentFrameworkShareRequestsResponseTypeDef",
    {
        "assessmentFrameworkShareRequests": List["AssessmentFrameworkShareRequestTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssessmentFrameworksRequestRequestTypeDef = TypedDict(
    "ListAssessmentFrameworksRequestRequestTypeDef",
    {
        "frameworkType": FrameworkTypeType,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAssessmentFrameworksResponseTypeDef = TypedDict(
    "ListAssessmentFrameworksResponseTypeDef",
    {
        "frameworkMetadataList": List["AssessmentFrameworkMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssessmentReportsRequestRequestTypeDef = TypedDict(
    "ListAssessmentReportsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAssessmentReportsResponseTypeDef = TypedDict(
    "ListAssessmentReportsResponseTypeDef",
    {
        "assessmentReports": List["AssessmentReportMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssessmentsRequestRequestTypeDef = TypedDict(
    "ListAssessmentsRequestRequestTypeDef",
    {
        "status": NotRequired[AssessmentStatusType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAssessmentsResponseTypeDef = TypedDict(
    "ListAssessmentsResponseTypeDef",
    {
        "assessmentMetadata": List["AssessmentMetadataItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListControlDomainInsightsByAssessmentRequestRequestTypeDef = TypedDict(
    "ListControlDomainInsightsByAssessmentRequestRequestTypeDef",
    {
        "assessmentId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListControlDomainInsightsByAssessmentResponseTypeDef = TypedDict(
    "ListControlDomainInsightsByAssessmentResponseTypeDef",
    {
        "controlDomainInsights": List["ControlDomainInsightsTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListControlDomainInsightsRequestRequestTypeDef = TypedDict(
    "ListControlDomainInsightsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListControlDomainInsightsResponseTypeDef = TypedDict(
    "ListControlDomainInsightsResponseTypeDef",
    {
        "controlDomainInsights": List["ControlDomainInsightsTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListControlInsightsByControlDomainRequestRequestTypeDef = TypedDict(
    "ListControlInsightsByControlDomainRequestRequestTypeDef",
    {
        "controlDomainId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListControlInsightsByControlDomainResponseTypeDef = TypedDict(
    "ListControlInsightsByControlDomainResponseTypeDef",
    {
        "controlInsightsMetadata": List["ControlInsightsMetadataItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListControlsRequestRequestTypeDef = TypedDict(
    "ListControlsRequestRequestTypeDef",
    {
        "controlType": ControlTypeType,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListControlsResponseTypeDef = TypedDict(
    "ListControlsResponseTypeDef",
    {
        "controlMetadataList": List["ControlMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKeywordsForDataSourceRequestRequestTypeDef = TypedDict(
    "ListKeywordsForDataSourceRequestRequestTypeDef",
    {
        "source": SourceTypeType,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListKeywordsForDataSourceResponseTypeDef = TypedDict(
    "ListKeywordsForDataSourceResponseTypeDef",
    {
        "keywords": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNotificationsRequestRequestTypeDef = TypedDict(
    "ListNotificationsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListNotificationsResponseTypeDef = TypedDict(
    "ListNotificationsResponseTypeDef",
    {
        "notifications": List["NotificationTypeDef"],
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

ManualEvidenceTypeDef = TypedDict(
    "ManualEvidenceTypeDef",
    {
        "s3ResourcePath": NotRequired[str],
    },
)

NotificationTypeDef = TypedDict(
    "NotificationTypeDef",
    {
        "id": NotRequired[str],
        "assessmentId": NotRequired[str],
        "assessmentName": NotRequired[str],
        "controlSetId": NotRequired[str],
        "controlSetName": NotRequired[str],
        "description": NotRequired[str],
        "eventTime": NotRequired[datetime],
        "source": NotRequired[str],
    },
)

RegisterAccountRequestRequestTypeDef = TypedDict(
    "RegisterAccountRequestRequestTypeDef",
    {
        "kmsKey": NotRequired[str],
        "delegatedAdminAccount": NotRequired[str],
    },
)

RegisterAccountResponseTypeDef = TypedDict(
    "RegisterAccountResponseTypeDef",
    {
        "status": AccountStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "RegisterOrganizationAdminAccountRequestRequestTypeDef",
    {
        "adminAccountId": str,
    },
)

RegisterOrganizationAdminAccountResponseTypeDef = TypedDict(
    "RegisterOrganizationAdminAccountResponseTypeDef",
    {
        "adminAccountId": str,
        "organizationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "arn": NotRequired[str],
        "value": NotRequired[str],
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

RoleTypeDef = TypedDict(
    "RoleTypeDef",
    {
        "roleType": NotRequired[RoleTypeType],
        "roleArn": NotRequired[str],
    },
)

ScopeTypeDef = TypedDict(
    "ScopeTypeDef",
    {
        "awsAccounts": NotRequired[Sequence["AWSAccountTypeDef"]],
        "awsServices": NotRequired[Sequence["AWSServiceTypeDef"]],
    },
)

ServiceMetadataTypeDef = TypedDict(
    "ServiceMetadataTypeDef",
    {
        "name": NotRequired[str],
        "displayName": NotRequired[str],
        "description": NotRequired[str],
        "category": NotRequired[str],
    },
)

SettingsTypeDef = TypedDict(
    "SettingsTypeDef",
    {
        "isAwsOrgEnabled": NotRequired[bool],
        "snsTopic": NotRequired[str],
        "defaultAssessmentReportsDestination": NotRequired["AssessmentReportsDestinationTypeDef"],
        "defaultProcessOwners": NotRequired[List["RoleTypeDef"]],
        "kmsKey": NotRequired[str],
    },
)

SourceKeywordTypeDef = TypedDict(
    "SourceKeywordTypeDef",
    {
        "keywordInputType": NotRequired[Literal["SELECT_FROM_LIST"]],
        "keywordValue": NotRequired[str],
    },
)

StartAssessmentFrameworkShareRequestRequestTypeDef = TypedDict(
    "StartAssessmentFrameworkShareRequestRequestTypeDef",
    {
        "frameworkId": str,
        "destinationAccount": str,
        "destinationRegion": str,
        "comment": NotRequired[str],
    },
)

StartAssessmentFrameworkShareResponseTypeDef = TypedDict(
    "StartAssessmentFrameworkShareResponseTypeDef",
    {
        "assessmentFrameworkShareRequest": "AssessmentFrameworkShareRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

URLTypeDef = TypedDict(
    "URLTypeDef",
    {
        "hyperlinkName": NotRequired[str],
        "link": NotRequired[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateAssessmentControlRequestRequestTypeDef = TypedDict(
    "UpdateAssessmentControlRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "controlId": str,
        "controlStatus": NotRequired[ControlStatusType],
        "commentBody": NotRequired[str],
    },
)

UpdateAssessmentControlResponseTypeDef = TypedDict(
    "UpdateAssessmentControlResponseTypeDef",
    {
        "control": "AssessmentControlTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAssessmentControlSetStatusRequestRequestTypeDef = TypedDict(
    "UpdateAssessmentControlSetStatusRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "status": ControlSetStatusType,
        "comment": str,
    },
)

UpdateAssessmentControlSetStatusResponseTypeDef = TypedDict(
    "UpdateAssessmentControlSetStatusResponseTypeDef",
    {
        "controlSet": "AssessmentControlSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAssessmentFrameworkControlSetTypeDef = TypedDict(
    "UpdateAssessmentFrameworkControlSetTypeDef",
    {
        "name": str,
        "controls": Sequence["CreateAssessmentFrameworkControlTypeDef"],
        "id": NotRequired[str],
    },
)

UpdateAssessmentFrameworkRequestRequestTypeDef = TypedDict(
    "UpdateAssessmentFrameworkRequestRequestTypeDef",
    {
        "frameworkId": str,
        "name": str,
        "controlSets": Sequence["UpdateAssessmentFrameworkControlSetTypeDef"],
        "description": NotRequired[str],
        "complianceType": NotRequired[str],
    },
)

UpdateAssessmentFrameworkResponseTypeDef = TypedDict(
    "UpdateAssessmentFrameworkResponseTypeDef",
    {
        "framework": "FrameworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAssessmentFrameworkShareRequestRequestTypeDef = TypedDict(
    "UpdateAssessmentFrameworkShareRequestRequestTypeDef",
    {
        "requestId": str,
        "requestType": ShareRequestTypeType,
        "action": ShareRequestActionType,
    },
)

UpdateAssessmentFrameworkShareResponseTypeDef = TypedDict(
    "UpdateAssessmentFrameworkShareResponseTypeDef",
    {
        "assessmentFrameworkShareRequest": "AssessmentFrameworkShareRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAssessmentRequestRequestTypeDef = TypedDict(
    "UpdateAssessmentRequestRequestTypeDef",
    {
        "assessmentId": str,
        "scope": "ScopeTypeDef",
        "assessmentName": NotRequired[str],
        "assessmentDescription": NotRequired[str],
        "assessmentReportsDestination": NotRequired["AssessmentReportsDestinationTypeDef"],
        "roles": NotRequired[Sequence["RoleTypeDef"]],
    },
)

UpdateAssessmentResponseTypeDef = TypedDict(
    "UpdateAssessmentResponseTypeDef",
    {
        "assessment": "AssessmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAssessmentStatusRequestRequestTypeDef = TypedDict(
    "UpdateAssessmentStatusRequestRequestTypeDef",
    {
        "assessmentId": str,
        "status": AssessmentStatusType,
    },
)

UpdateAssessmentStatusResponseTypeDef = TypedDict(
    "UpdateAssessmentStatusResponseTypeDef",
    {
        "assessment": "AssessmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateControlRequestRequestTypeDef = TypedDict(
    "UpdateControlRequestRequestTypeDef",
    {
        "controlId": str,
        "name": str,
        "controlMappingSources": Sequence["ControlMappingSourceTypeDef"],
        "description": NotRequired[str],
        "testingInformation": NotRequired[str],
        "actionPlanTitle": NotRequired[str],
        "actionPlanInstructions": NotRequired[str],
    },
)

UpdateControlResponseTypeDef = TypedDict(
    "UpdateControlResponseTypeDef",
    {
        "control": "ControlTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSettingsRequestRequestTypeDef = TypedDict(
    "UpdateSettingsRequestRequestTypeDef",
    {
        "snsTopic": NotRequired[str],
        "defaultAssessmentReportsDestination": NotRequired["AssessmentReportsDestinationTypeDef"],
        "defaultProcessOwners": NotRequired[Sequence["RoleTypeDef"]],
        "kmsKey": NotRequired[str],
    },
)

UpdateSettingsResponseTypeDef = TypedDict(
    "UpdateSettingsResponseTypeDef",
    {
        "settings": "SettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidateAssessmentReportIntegrityRequestRequestTypeDef = TypedDict(
    "ValidateAssessmentReportIntegrityRequestRequestTypeDef",
    {
        "s3RelativePath": str,
    },
)

ValidateAssessmentReportIntegrityResponseTypeDef = TypedDict(
    "ValidateAssessmentReportIntegrityResponseTypeDef",
    {
        "signatureValid": bool,
        "signatureAlgorithm": str,
        "signatureDateTime": str,
        "signatureKeyId": str,
        "validationErrors": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
