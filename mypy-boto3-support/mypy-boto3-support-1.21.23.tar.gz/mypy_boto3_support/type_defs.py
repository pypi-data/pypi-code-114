"""
Type annotations for support service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support/type_defs.html)

Usage::

    ```python
    from mypy_boto3_support.type_defs import AddAttachmentsToSetRequestRequestTypeDef

    data: AddAttachmentsToSetRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import IO, Dict, List, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddAttachmentsToSetRequestRequestTypeDef",
    "AddAttachmentsToSetResponseTypeDef",
    "AddCommunicationToCaseRequestRequestTypeDef",
    "AddCommunicationToCaseResponseTypeDef",
    "AttachmentDetailsTypeDef",
    "AttachmentTypeDef",
    "CaseDetailsTypeDef",
    "CategoryTypeDef",
    "CommunicationTypeDef",
    "CreateCaseRequestRequestTypeDef",
    "CreateCaseResponseTypeDef",
    "DescribeAttachmentRequestRequestTypeDef",
    "DescribeAttachmentResponseTypeDef",
    "DescribeCasesRequestRequestTypeDef",
    "DescribeCasesResponseTypeDef",
    "DescribeCommunicationsRequestRequestTypeDef",
    "DescribeCommunicationsResponseTypeDef",
    "DescribeServicesRequestRequestTypeDef",
    "DescribeServicesResponseTypeDef",
    "DescribeSeverityLevelsRequestRequestTypeDef",
    "DescribeSeverityLevelsResponseTypeDef",
    "DescribeTrustedAdvisorCheckRefreshStatusesRequestRequestTypeDef",
    "DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef",
    "DescribeTrustedAdvisorCheckResultRequestRequestTypeDef",
    "DescribeTrustedAdvisorCheckResultResponseTypeDef",
    "DescribeTrustedAdvisorCheckSummariesRequestRequestTypeDef",
    "DescribeTrustedAdvisorCheckSummariesResponseTypeDef",
    "DescribeTrustedAdvisorChecksRequestRequestTypeDef",
    "DescribeTrustedAdvisorChecksResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RecentCaseCommunicationsTypeDef",
    "RefreshTrustedAdvisorCheckRequestRequestTypeDef",
    "RefreshTrustedAdvisorCheckResponseTypeDef",
    "ResolveCaseRequestRequestTypeDef",
    "ResolveCaseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "ServiceTypeDef",
    "SeverityLevelTypeDef",
    "TrustedAdvisorCategorySpecificSummaryTypeDef",
    "TrustedAdvisorCheckDescriptionTypeDef",
    "TrustedAdvisorCheckRefreshStatusTypeDef",
    "TrustedAdvisorCheckResultTypeDef",
    "TrustedAdvisorCheckSummaryTypeDef",
    "TrustedAdvisorCostOptimizingSummaryTypeDef",
    "TrustedAdvisorResourceDetailTypeDef",
    "TrustedAdvisorResourcesSummaryTypeDef",
)

AddAttachmentsToSetRequestRequestTypeDef = TypedDict(
    "AddAttachmentsToSetRequestRequestTypeDef",
    {
        "attachments": Sequence["AttachmentTypeDef"],
        "attachmentSetId": NotRequired[str],
    },
)

AddAttachmentsToSetResponseTypeDef = TypedDict(
    "AddAttachmentsToSetResponseTypeDef",
    {
        "attachmentSetId": str,
        "expiryTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddCommunicationToCaseRequestRequestTypeDef = TypedDict(
    "AddCommunicationToCaseRequestRequestTypeDef",
    {
        "communicationBody": str,
        "caseId": NotRequired[str],
        "ccEmailAddresses": NotRequired[Sequence[str]],
        "attachmentSetId": NotRequired[str],
    },
)

AddCommunicationToCaseResponseTypeDef = TypedDict(
    "AddCommunicationToCaseResponseTypeDef",
    {
        "result": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachmentDetailsTypeDef = TypedDict(
    "AttachmentDetailsTypeDef",
    {
        "attachmentId": NotRequired[str],
        "fileName": NotRequired[str],
    },
)

AttachmentTypeDef = TypedDict(
    "AttachmentTypeDef",
    {
        "fileName": NotRequired[str],
        "data": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
    },
)

CaseDetailsTypeDef = TypedDict(
    "CaseDetailsTypeDef",
    {
        "caseId": NotRequired[str],
        "displayId": NotRequired[str],
        "subject": NotRequired[str],
        "status": NotRequired[str],
        "serviceCode": NotRequired[str],
        "categoryCode": NotRequired[str],
        "severityCode": NotRequired[str],
        "submittedBy": NotRequired[str],
        "timeCreated": NotRequired[str],
        "recentCommunications": NotRequired["RecentCaseCommunicationsTypeDef"],
        "ccEmailAddresses": NotRequired[List[str]],
        "language": NotRequired[str],
    },
)

CategoryTypeDef = TypedDict(
    "CategoryTypeDef",
    {
        "code": NotRequired[str],
        "name": NotRequired[str],
    },
)

CommunicationTypeDef = TypedDict(
    "CommunicationTypeDef",
    {
        "caseId": NotRequired[str],
        "body": NotRequired[str],
        "submittedBy": NotRequired[str],
        "timeCreated": NotRequired[str],
        "attachmentSet": NotRequired[List["AttachmentDetailsTypeDef"]],
    },
)

CreateCaseRequestRequestTypeDef = TypedDict(
    "CreateCaseRequestRequestTypeDef",
    {
        "subject": str,
        "communicationBody": str,
        "serviceCode": NotRequired[str],
        "severityCode": NotRequired[str],
        "categoryCode": NotRequired[str],
        "ccEmailAddresses": NotRequired[Sequence[str]],
        "language": NotRequired[str],
        "issueType": NotRequired[str],
        "attachmentSetId": NotRequired[str],
    },
)

CreateCaseResponseTypeDef = TypedDict(
    "CreateCaseResponseTypeDef",
    {
        "caseId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAttachmentRequestRequestTypeDef = TypedDict(
    "DescribeAttachmentRequestRequestTypeDef",
    {
        "attachmentId": str,
    },
)

DescribeAttachmentResponseTypeDef = TypedDict(
    "DescribeAttachmentResponseTypeDef",
    {
        "attachment": "AttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCasesRequestRequestTypeDef = TypedDict(
    "DescribeCasesRequestRequestTypeDef",
    {
        "caseIdList": NotRequired[Sequence[str]],
        "displayId": NotRequired[str],
        "afterTime": NotRequired[str],
        "beforeTime": NotRequired[str],
        "includeResolvedCases": NotRequired[bool],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "language": NotRequired[str],
        "includeCommunications": NotRequired[bool],
    },
)

DescribeCasesResponseTypeDef = TypedDict(
    "DescribeCasesResponseTypeDef",
    {
        "cases": List["CaseDetailsTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCommunicationsRequestRequestTypeDef = TypedDict(
    "DescribeCommunicationsRequestRequestTypeDef",
    {
        "caseId": str,
        "beforeTime": NotRequired[str],
        "afterTime": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

DescribeCommunicationsResponseTypeDef = TypedDict(
    "DescribeCommunicationsResponseTypeDef",
    {
        "communications": List["CommunicationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServicesRequestRequestTypeDef = TypedDict(
    "DescribeServicesRequestRequestTypeDef",
    {
        "serviceCodeList": NotRequired[Sequence[str]],
        "language": NotRequired[str],
    },
)

DescribeServicesResponseTypeDef = TypedDict(
    "DescribeServicesResponseTypeDef",
    {
        "services": List["ServiceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSeverityLevelsRequestRequestTypeDef = TypedDict(
    "DescribeSeverityLevelsRequestRequestTypeDef",
    {
        "language": NotRequired[str],
    },
)

DescribeSeverityLevelsResponseTypeDef = TypedDict(
    "DescribeSeverityLevelsResponseTypeDef",
    {
        "severityLevels": List["SeverityLevelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrustedAdvisorCheckRefreshStatusesRequestRequestTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckRefreshStatusesRequestRequestTypeDef",
    {
        "checkIds": Sequence[str],
    },
)

DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef",
    {
        "statuses": List["TrustedAdvisorCheckRefreshStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrustedAdvisorCheckResultRequestRequestTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckResultRequestRequestTypeDef",
    {
        "checkId": str,
        "language": NotRequired[str],
    },
)

DescribeTrustedAdvisorCheckResultResponseTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckResultResponseTypeDef",
    {
        "result": "TrustedAdvisorCheckResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrustedAdvisorCheckSummariesRequestRequestTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckSummariesRequestRequestTypeDef",
    {
        "checkIds": Sequence[str],
    },
)

DescribeTrustedAdvisorCheckSummariesResponseTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckSummariesResponseTypeDef",
    {
        "summaries": List["TrustedAdvisorCheckSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrustedAdvisorChecksRequestRequestTypeDef = TypedDict(
    "DescribeTrustedAdvisorChecksRequestRequestTypeDef",
    {
        "language": str,
    },
)

DescribeTrustedAdvisorChecksResponseTypeDef = TypedDict(
    "DescribeTrustedAdvisorChecksResponseTypeDef",
    {
        "checks": List["TrustedAdvisorCheckDescriptionTypeDef"],
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

RecentCaseCommunicationsTypeDef = TypedDict(
    "RecentCaseCommunicationsTypeDef",
    {
        "communications": NotRequired[List["CommunicationTypeDef"]],
        "nextToken": NotRequired[str],
    },
)

RefreshTrustedAdvisorCheckRequestRequestTypeDef = TypedDict(
    "RefreshTrustedAdvisorCheckRequestRequestTypeDef",
    {
        "checkId": str,
    },
)

RefreshTrustedAdvisorCheckResponseTypeDef = TypedDict(
    "RefreshTrustedAdvisorCheckResponseTypeDef",
    {
        "status": "TrustedAdvisorCheckRefreshStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResolveCaseRequestRequestTypeDef = TypedDict(
    "ResolveCaseRequestRequestTypeDef",
    {
        "caseId": NotRequired[str],
    },
)

ResolveCaseResponseTypeDef = TypedDict(
    "ResolveCaseResponseTypeDef",
    {
        "initialCaseStatus": str,
        "finalCaseStatus": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "code": NotRequired[str],
        "name": NotRequired[str],
        "categories": NotRequired[List["CategoryTypeDef"]],
    },
)

SeverityLevelTypeDef = TypedDict(
    "SeverityLevelTypeDef",
    {
        "code": NotRequired[str],
        "name": NotRequired[str],
    },
)

TrustedAdvisorCategorySpecificSummaryTypeDef = TypedDict(
    "TrustedAdvisorCategorySpecificSummaryTypeDef",
    {
        "costOptimizing": NotRequired["TrustedAdvisorCostOptimizingSummaryTypeDef"],
    },
)

TrustedAdvisorCheckDescriptionTypeDef = TypedDict(
    "TrustedAdvisorCheckDescriptionTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "category": str,
        "metadata": List[str],
    },
)

TrustedAdvisorCheckRefreshStatusTypeDef = TypedDict(
    "TrustedAdvisorCheckRefreshStatusTypeDef",
    {
        "checkId": str,
        "status": str,
        "millisUntilNextRefreshable": int,
    },
)

TrustedAdvisorCheckResultTypeDef = TypedDict(
    "TrustedAdvisorCheckResultTypeDef",
    {
        "checkId": str,
        "timestamp": str,
        "status": str,
        "resourcesSummary": "TrustedAdvisorResourcesSummaryTypeDef",
        "categorySpecificSummary": "TrustedAdvisorCategorySpecificSummaryTypeDef",
        "flaggedResources": List["TrustedAdvisorResourceDetailTypeDef"],
    },
)

TrustedAdvisorCheckSummaryTypeDef = TypedDict(
    "TrustedAdvisorCheckSummaryTypeDef",
    {
        "checkId": str,
        "timestamp": str,
        "status": str,
        "resourcesSummary": "TrustedAdvisorResourcesSummaryTypeDef",
        "categorySpecificSummary": "TrustedAdvisorCategorySpecificSummaryTypeDef",
        "hasFlaggedResources": NotRequired[bool],
    },
)

TrustedAdvisorCostOptimizingSummaryTypeDef = TypedDict(
    "TrustedAdvisorCostOptimizingSummaryTypeDef",
    {
        "estimatedMonthlySavings": float,
        "estimatedPercentMonthlySavings": float,
    },
)

TrustedAdvisorResourceDetailTypeDef = TypedDict(
    "TrustedAdvisorResourceDetailTypeDef",
    {
        "status": str,
        "resourceId": str,
        "metadata": List[str],
        "region": NotRequired[str],
        "isSuppressed": NotRequired[bool],
    },
)

TrustedAdvisorResourcesSummaryTypeDef = TypedDict(
    "TrustedAdvisorResourcesSummaryTypeDef",
    {
        "resourcesProcessed": int,
        "resourcesFlagged": int,
        "resourcesIgnored": int,
        "resourcesSuppressed": int,
    },
)
