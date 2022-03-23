"""
Type annotations for inspector2 service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_inspector2.type_defs import AccountAggregationResponseTypeDef

    data: AccountAggregationResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AccountSortByType,
    AggregationFindingTypeType,
    AggregationResourceTypeType,
    AggregationTypeType,
    AmiSortByType,
    AwsEcrContainerSortByType,
    CoverageResourceTypeType,
    CoverageStringComparisonType,
    DelegatedAdminStatusType,
    Ec2InstanceSortByType,
    Ec2PlatformType,
    EcrScanFrequencyType,
    ErrorCodeType,
    ExternalReportStatusType,
    FilterActionType,
    FindingStatusType,
    FindingTypeSortByType,
    FindingTypeType,
    FreeTrialInfoErrorCodeType,
    FreeTrialStatusType,
    FreeTrialTypeType,
    GroupKeyType,
    ImageLayerSortByType,
    NetworkProtocolType,
    OperationType,
    PackageManagerType,
    PackageSortByType,
    RelationshipStatusType,
    ReportFormatType,
    ReportingErrorCodeType,
    RepositorySortByType,
    ResourceScanTypeType,
    ResourceTypeType,
    ScanStatusCodeType,
    ScanStatusReasonType,
    ScanTypeType,
    ServiceType,
    SeverityType,
    SortFieldType,
    SortOrderType,
    StatusType,
    StringComparisonType,
    TitleSortByType,
    UsageTypeType,
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
    "AccountAggregationResponseTypeDef",
    "AccountAggregationTypeDef",
    "AccountStateTypeDef",
    "AccountTypeDef",
    "AggregationRequestTypeDef",
    "AggregationResponseTypeDef",
    "AmiAggregationResponseTypeDef",
    "AmiAggregationTypeDef",
    "AssociateMemberRequestRequestTypeDef",
    "AssociateMemberResponseTypeDef",
    "AutoEnableTypeDef",
    "AwsEc2InstanceDetailsTypeDef",
    "AwsEcrContainerAggregationResponseTypeDef",
    "AwsEcrContainerAggregationTypeDef",
    "AwsEcrContainerImageDetailsTypeDef",
    "BatchGetAccountStatusRequestRequestTypeDef",
    "BatchGetAccountStatusResponseTypeDef",
    "BatchGetFreeTrialInfoRequestRequestTypeDef",
    "BatchGetFreeTrialInfoResponseTypeDef",
    "CancelFindingsReportRequestRequestTypeDef",
    "CancelFindingsReportResponseTypeDef",
    "CountsTypeDef",
    "CoverageFilterCriteriaTypeDef",
    "CoverageMapFilterTypeDef",
    "CoverageStringFilterTypeDef",
    "CoveredResourceTypeDef",
    "CreateFilterRequestRequestTypeDef",
    "CreateFilterResponseTypeDef",
    "CreateFindingsReportRequestRequestTypeDef",
    "CreateFindingsReportResponseTypeDef",
    "CvssScoreAdjustmentTypeDef",
    "CvssScoreDetailsTypeDef",
    "CvssScoreTypeDef",
    "DateFilterTypeDef",
    "DelegatedAdminAccountTypeDef",
    "DelegatedAdminTypeDef",
    "DeleteFilterRequestRequestTypeDef",
    "DeleteFilterResponseTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "DestinationTypeDef",
    "DisableDelegatedAdminAccountRequestRequestTypeDef",
    "DisableDelegatedAdminAccountResponseTypeDef",
    "DisableRequestRequestTypeDef",
    "DisableResponseTypeDef",
    "DisassociateMemberRequestRequestTypeDef",
    "DisassociateMemberResponseTypeDef",
    "Ec2InstanceAggregationResponseTypeDef",
    "Ec2InstanceAggregationTypeDef",
    "Ec2MetadataTypeDef",
    "EcrContainerImageMetadataTypeDef",
    "EcrRepositoryMetadataTypeDef",
    "EnableDelegatedAdminAccountRequestRequestTypeDef",
    "EnableDelegatedAdminAccountResponseTypeDef",
    "EnableRequestRequestTypeDef",
    "EnableResponseTypeDef",
    "FailedAccountTypeDef",
    "FilterCriteriaTypeDef",
    "FilterTypeDef",
    "FindingTypeAggregationResponseTypeDef",
    "FindingTypeAggregationTypeDef",
    "FindingTypeDef",
    "FreeTrialAccountInfoTypeDef",
    "FreeTrialInfoErrorTypeDef",
    "FreeTrialInfoTypeDef",
    "GetDelegatedAdminAccountResponseTypeDef",
    "GetFindingsReportStatusRequestRequestTypeDef",
    "GetFindingsReportStatusResponseTypeDef",
    "GetMemberRequestRequestTypeDef",
    "GetMemberResponseTypeDef",
    "ImageLayerAggregationResponseTypeDef",
    "ImageLayerAggregationTypeDef",
    "InspectorScoreDetailsTypeDef",
    "ListAccountPermissionsRequestRequestTypeDef",
    "ListAccountPermissionsResponseTypeDef",
    "ListCoverageRequestRequestTypeDef",
    "ListCoverageResponseTypeDef",
    "ListCoverageStatisticsRequestRequestTypeDef",
    "ListCoverageStatisticsResponseTypeDef",
    "ListDelegatedAdminAccountsRequestRequestTypeDef",
    "ListDelegatedAdminAccountsResponseTypeDef",
    "ListFiltersRequestRequestTypeDef",
    "ListFiltersResponseTypeDef",
    "ListFindingAggregationsRequestRequestTypeDef",
    "ListFindingAggregationsResponseTypeDef",
    "ListFindingsRequestRequestTypeDef",
    "ListFindingsResponseTypeDef",
    "ListMembersRequestRequestTypeDef",
    "ListMembersResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUsageTotalsRequestRequestTypeDef",
    "ListUsageTotalsResponseTypeDef",
    "MapFilterTypeDef",
    "MemberTypeDef",
    "NetworkPathTypeDef",
    "NetworkReachabilityDetailsTypeDef",
    "NumberFilterTypeDef",
    "PackageAggregationResponseTypeDef",
    "PackageAggregationTypeDef",
    "PackageFilterTypeDef",
    "PackageVulnerabilityDetailsTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "PortRangeFilterTypeDef",
    "PortRangeTypeDef",
    "RecommendationTypeDef",
    "RemediationTypeDef",
    "RepositoryAggregationResponseTypeDef",
    "RepositoryAggregationTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceScanMetadataTypeDef",
    "ResourceStateTypeDef",
    "ResourceStatusTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "ScanStatusTypeDef",
    "SeverityCountsTypeDef",
    "SortCriteriaTypeDef",
    "StateTypeDef",
    "StepTypeDef",
    "StringFilterTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TitleAggregationResponseTypeDef",
    "TitleAggregationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateFilterRequestRequestTypeDef",
    "UpdateFilterResponseTypeDef",
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    "UpdateOrganizationConfigurationResponseTypeDef",
    "UsageTotalTypeDef",
    "UsageTypeDef",
    "VulnerablePackageTypeDef",
)

AccountAggregationResponseTypeDef = TypedDict(
    "AccountAggregationResponseTypeDef",
    {
        "accountId": NotRequired[str],
        "severityCounts": NotRequired["SeverityCountsTypeDef"],
    },
)

AccountAggregationTypeDef = TypedDict(
    "AccountAggregationTypeDef",
    {
        "findingType": NotRequired[AggregationFindingTypeType],
        "resourceType": NotRequired[AggregationResourceTypeType],
        "sortBy": NotRequired[AccountSortByType],
        "sortOrder": NotRequired[SortOrderType],
    },
)

AccountStateTypeDef = TypedDict(
    "AccountStateTypeDef",
    {
        "accountId": str,
        "resourceState": "ResourceStateTypeDef",
        "state": "StateTypeDef",
    },
)

AccountTypeDef = TypedDict(
    "AccountTypeDef",
    {
        "accountId": str,
        "resourceStatus": "ResourceStatusTypeDef",
        "status": StatusType,
    },
)

AggregationRequestTypeDef = TypedDict(
    "AggregationRequestTypeDef",
    {
        "accountAggregation": NotRequired["AccountAggregationTypeDef"],
        "amiAggregation": NotRequired["AmiAggregationTypeDef"],
        "awsEcrContainerAggregation": NotRequired["AwsEcrContainerAggregationTypeDef"],
        "ec2InstanceAggregation": NotRequired["Ec2InstanceAggregationTypeDef"],
        "findingTypeAggregation": NotRequired["FindingTypeAggregationTypeDef"],
        "imageLayerAggregation": NotRequired["ImageLayerAggregationTypeDef"],
        "packageAggregation": NotRequired["PackageAggregationTypeDef"],
        "repositoryAggregation": NotRequired["RepositoryAggregationTypeDef"],
        "titleAggregation": NotRequired["TitleAggregationTypeDef"],
    },
)

AggregationResponseTypeDef = TypedDict(
    "AggregationResponseTypeDef",
    {
        "accountAggregation": NotRequired["AccountAggregationResponseTypeDef"],
        "amiAggregation": NotRequired["AmiAggregationResponseTypeDef"],
        "awsEcrContainerAggregation": NotRequired["AwsEcrContainerAggregationResponseTypeDef"],
        "ec2InstanceAggregation": NotRequired["Ec2InstanceAggregationResponseTypeDef"],
        "findingTypeAggregation": NotRequired["FindingTypeAggregationResponseTypeDef"],
        "imageLayerAggregation": NotRequired["ImageLayerAggregationResponseTypeDef"],
        "packageAggregation": NotRequired["PackageAggregationResponseTypeDef"],
        "repositoryAggregation": NotRequired["RepositoryAggregationResponseTypeDef"],
        "titleAggregation": NotRequired["TitleAggregationResponseTypeDef"],
    },
)

AmiAggregationResponseTypeDef = TypedDict(
    "AmiAggregationResponseTypeDef",
    {
        "ami": str,
        "accountId": NotRequired[str],
        "affectedInstances": NotRequired[int],
        "severityCounts": NotRequired["SeverityCountsTypeDef"],
    },
)

AmiAggregationTypeDef = TypedDict(
    "AmiAggregationTypeDef",
    {
        "amis": NotRequired[Sequence["StringFilterTypeDef"]],
        "sortBy": NotRequired[AmiSortByType],
        "sortOrder": NotRequired[SortOrderType],
    },
)

AssociateMemberRequestRequestTypeDef = TypedDict(
    "AssociateMemberRequestRequestTypeDef",
    {
        "accountId": str,
    },
)

AssociateMemberResponseTypeDef = TypedDict(
    "AssociateMemberResponseTypeDef",
    {
        "accountId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AutoEnableTypeDef = TypedDict(
    "AutoEnableTypeDef",
    {
        "ec2": bool,
        "ecr": bool,
    },
)

AwsEc2InstanceDetailsTypeDef = TypedDict(
    "AwsEc2InstanceDetailsTypeDef",
    {
        "iamInstanceProfileArn": NotRequired[str],
        "imageId": NotRequired[str],
        "ipV4Addresses": NotRequired[List[str]],
        "ipV6Addresses": NotRequired[List[str]],
        "keyName": NotRequired[str],
        "launchedAt": NotRequired[datetime],
        "platform": NotRequired[str],
        "subnetId": NotRequired[str],
        "type": NotRequired[str],
        "vpcId": NotRequired[str],
    },
)

AwsEcrContainerAggregationResponseTypeDef = TypedDict(
    "AwsEcrContainerAggregationResponseTypeDef",
    {
        "resourceId": str,
        "accountId": NotRequired[str],
        "architecture": NotRequired[str],
        "imageSha": NotRequired[str],
        "imageTags": NotRequired[List[str]],
        "repository": NotRequired[str],
        "severityCounts": NotRequired["SeverityCountsTypeDef"],
    },
)

AwsEcrContainerAggregationTypeDef = TypedDict(
    "AwsEcrContainerAggregationTypeDef",
    {
        "architectures": NotRequired[Sequence["StringFilterTypeDef"]],
        "imageShas": NotRequired[Sequence["StringFilterTypeDef"]],
        "imageTags": NotRequired[Sequence["StringFilterTypeDef"]],
        "repositories": NotRequired[Sequence["StringFilterTypeDef"]],
        "resourceIds": NotRequired[Sequence["StringFilterTypeDef"]],
        "sortBy": NotRequired[AwsEcrContainerSortByType],
        "sortOrder": NotRequired[SortOrderType],
    },
)

AwsEcrContainerImageDetailsTypeDef = TypedDict(
    "AwsEcrContainerImageDetailsTypeDef",
    {
        "imageHash": str,
        "registry": str,
        "repositoryName": str,
        "architecture": NotRequired[str],
        "author": NotRequired[str],
        "imageTags": NotRequired[List[str]],
        "platform": NotRequired[str],
        "pushedAt": NotRequired[datetime],
    },
)

BatchGetAccountStatusRequestRequestTypeDef = TypedDict(
    "BatchGetAccountStatusRequestRequestTypeDef",
    {
        "accountIds": NotRequired[Sequence[str]],
    },
)

BatchGetAccountStatusResponseTypeDef = TypedDict(
    "BatchGetAccountStatusResponseTypeDef",
    {
        "accounts": List["AccountStateTypeDef"],
        "failedAccounts": List["FailedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetFreeTrialInfoRequestRequestTypeDef = TypedDict(
    "BatchGetFreeTrialInfoRequestRequestTypeDef",
    {
        "accountIds": Sequence[str],
    },
)

BatchGetFreeTrialInfoResponseTypeDef = TypedDict(
    "BatchGetFreeTrialInfoResponseTypeDef",
    {
        "accounts": List["FreeTrialAccountInfoTypeDef"],
        "failedAccounts": List["FreeTrialInfoErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelFindingsReportRequestRequestTypeDef = TypedDict(
    "CancelFindingsReportRequestRequestTypeDef",
    {
        "reportId": str,
    },
)

CancelFindingsReportResponseTypeDef = TypedDict(
    "CancelFindingsReportResponseTypeDef",
    {
        "reportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CountsTypeDef = TypedDict(
    "CountsTypeDef",
    {
        "count": NotRequired[int],
        "groupKey": NotRequired[GroupKeyType],
    },
)

CoverageFilterCriteriaTypeDef = TypedDict(
    "CoverageFilterCriteriaTypeDef",
    {
        "accountId": NotRequired[Sequence["CoverageStringFilterTypeDef"]],
        "ec2InstanceTags": NotRequired[Sequence["CoverageMapFilterTypeDef"]],
        "ecrImageTags": NotRequired[Sequence["CoverageStringFilterTypeDef"]],
        "ecrRepositoryName": NotRequired[Sequence["CoverageStringFilterTypeDef"]],
        "resourceId": NotRequired[Sequence["CoverageStringFilterTypeDef"]],
        "resourceType": NotRequired[Sequence["CoverageStringFilterTypeDef"]],
        "scanStatusCode": NotRequired[Sequence["CoverageStringFilterTypeDef"]],
        "scanStatusReason": NotRequired[Sequence["CoverageStringFilterTypeDef"]],
        "scanType": NotRequired[Sequence["CoverageStringFilterTypeDef"]],
    },
)

CoverageMapFilterTypeDef = TypedDict(
    "CoverageMapFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "key": str,
        "value": NotRequired[str],
    },
)

CoverageStringFilterTypeDef = TypedDict(
    "CoverageStringFilterTypeDef",
    {
        "comparison": CoverageStringComparisonType,
        "value": str,
    },
)

CoveredResourceTypeDef = TypedDict(
    "CoveredResourceTypeDef",
    {
        "accountId": str,
        "resourceId": str,
        "resourceType": CoverageResourceTypeType,
        "scanType": ScanTypeType,
        "resourceMetadata": NotRequired["ResourceScanMetadataTypeDef"],
        "scanStatus": NotRequired["ScanStatusTypeDef"],
    },
)

CreateFilterRequestRequestTypeDef = TypedDict(
    "CreateFilterRequestRequestTypeDef",
    {
        "action": FilterActionType,
        "filterCriteria": "FilterCriteriaTypeDef",
        "name": str,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateFilterResponseTypeDef = TypedDict(
    "CreateFilterResponseTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFindingsReportRequestRequestTypeDef = TypedDict(
    "CreateFindingsReportRequestRequestTypeDef",
    {
        "reportFormat": ReportFormatType,
        "s3Destination": "DestinationTypeDef",
        "filterCriteria": NotRequired["FilterCriteriaTypeDef"],
    },
)

CreateFindingsReportResponseTypeDef = TypedDict(
    "CreateFindingsReportResponseTypeDef",
    {
        "reportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CvssScoreAdjustmentTypeDef = TypedDict(
    "CvssScoreAdjustmentTypeDef",
    {
        "metric": str,
        "reason": str,
    },
)

CvssScoreDetailsTypeDef = TypedDict(
    "CvssScoreDetailsTypeDef",
    {
        "score": float,
        "scoreSource": str,
        "scoringVector": str,
        "version": str,
        "adjustments": NotRequired[List["CvssScoreAdjustmentTypeDef"]],
        "cvssSource": NotRequired[str],
    },
)

CvssScoreTypeDef = TypedDict(
    "CvssScoreTypeDef",
    {
        "baseScore": float,
        "scoringVector": str,
        "source": str,
        "version": str,
    },
)

DateFilterTypeDef = TypedDict(
    "DateFilterTypeDef",
    {
        "endInclusive": NotRequired[Union[datetime, str]],
        "startInclusive": NotRequired[Union[datetime, str]],
    },
)

DelegatedAdminAccountTypeDef = TypedDict(
    "DelegatedAdminAccountTypeDef",
    {
        "accountId": NotRequired[str],
        "status": NotRequired[DelegatedAdminStatusType],
    },
)

DelegatedAdminTypeDef = TypedDict(
    "DelegatedAdminTypeDef",
    {
        "accountId": NotRequired[str],
        "relationshipStatus": NotRequired[RelationshipStatusType],
    },
)

DeleteFilterRequestRequestTypeDef = TypedDict(
    "DeleteFilterRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteFilterResponseTypeDef = TypedDict(
    "DeleteFilterResponseTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {
        "autoEnable": "AutoEnableTypeDef",
        "maxAccountLimitReached": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "bucketName": str,
        "kmsKeyArn": str,
        "keyPrefix": NotRequired[str],
    },
)

DisableDelegatedAdminAccountRequestRequestTypeDef = TypedDict(
    "DisableDelegatedAdminAccountRequestRequestTypeDef",
    {
        "delegatedAdminAccountId": str,
    },
)

DisableDelegatedAdminAccountResponseTypeDef = TypedDict(
    "DisableDelegatedAdminAccountResponseTypeDef",
    {
        "delegatedAdminAccountId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableRequestRequestTypeDef = TypedDict(
    "DisableRequestRequestTypeDef",
    {
        "accountIds": NotRequired[Sequence[str]],
        "resourceTypes": NotRequired[Sequence[ResourceScanTypeType]],
    },
)

DisableResponseTypeDef = TypedDict(
    "DisableResponseTypeDef",
    {
        "accounts": List["AccountTypeDef"],
        "failedAccounts": List["FailedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateMemberRequestRequestTypeDef = TypedDict(
    "DisassociateMemberRequestRequestTypeDef",
    {
        "accountId": str,
    },
)

DisassociateMemberResponseTypeDef = TypedDict(
    "DisassociateMemberResponseTypeDef",
    {
        "accountId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

Ec2InstanceAggregationResponseTypeDef = TypedDict(
    "Ec2InstanceAggregationResponseTypeDef",
    {
        "instanceId": str,
        "accountId": NotRequired[str],
        "ami": NotRequired[str],
        "instanceTags": NotRequired[Dict[str, str]],
        "networkFindings": NotRequired[int],
        "operatingSystem": NotRequired[str],
        "severityCounts": NotRequired["SeverityCountsTypeDef"],
    },
)

Ec2InstanceAggregationTypeDef = TypedDict(
    "Ec2InstanceAggregationTypeDef",
    {
        "amis": NotRequired[Sequence["StringFilterTypeDef"]],
        "instanceIds": NotRequired[Sequence["StringFilterTypeDef"]],
        "instanceTags": NotRequired[Sequence["MapFilterTypeDef"]],
        "operatingSystems": NotRequired[Sequence["StringFilterTypeDef"]],
        "sortBy": NotRequired[Ec2InstanceSortByType],
        "sortOrder": NotRequired[SortOrderType],
    },
)

Ec2MetadataTypeDef = TypedDict(
    "Ec2MetadataTypeDef",
    {
        "amiId": NotRequired[str],
        "platform": NotRequired[Ec2PlatformType],
        "tags": NotRequired[Dict[str, str]],
    },
)

EcrContainerImageMetadataTypeDef = TypedDict(
    "EcrContainerImageMetadataTypeDef",
    {
        "tags": NotRequired[List[str]],
    },
)

EcrRepositoryMetadataTypeDef = TypedDict(
    "EcrRepositoryMetadataTypeDef",
    {
        "name": NotRequired[str],
        "scanFrequency": NotRequired[EcrScanFrequencyType],
    },
)

EnableDelegatedAdminAccountRequestRequestTypeDef = TypedDict(
    "EnableDelegatedAdminAccountRequestRequestTypeDef",
    {
        "delegatedAdminAccountId": str,
        "clientToken": NotRequired[str],
    },
)

EnableDelegatedAdminAccountResponseTypeDef = TypedDict(
    "EnableDelegatedAdminAccountResponseTypeDef",
    {
        "delegatedAdminAccountId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableRequestRequestTypeDef = TypedDict(
    "EnableRequestRequestTypeDef",
    {
        "resourceTypes": Sequence[ResourceScanTypeType],
        "accountIds": NotRequired[Sequence[str]],
        "clientToken": NotRequired[str],
    },
)

EnableResponseTypeDef = TypedDict(
    "EnableResponseTypeDef",
    {
        "accounts": List["AccountTypeDef"],
        "failedAccounts": List["FailedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailedAccountTypeDef = TypedDict(
    "FailedAccountTypeDef",
    {
        "accountId": str,
        "errorCode": ErrorCodeType,
        "errorMessage": str,
        "resourceStatus": NotRequired["ResourceStatusTypeDef"],
        "status": NotRequired[StatusType],
    },
)

FilterCriteriaTypeDef = TypedDict(
    "FilterCriteriaTypeDef",
    {
        "awsAccountId": NotRequired[Sequence["StringFilterTypeDef"]],
        "componentId": NotRequired[Sequence["StringFilterTypeDef"]],
        "componentType": NotRequired[Sequence["StringFilterTypeDef"]],
        "ec2InstanceImageId": NotRequired[Sequence["StringFilterTypeDef"]],
        "ec2InstanceSubnetId": NotRequired[Sequence["StringFilterTypeDef"]],
        "ec2InstanceVpcId": NotRequired[Sequence["StringFilterTypeDef"]],
        "ecrImageArchitecture": NotRequired[Sequence["StringFilterTypeDef"]],
        "ecrImageHash": NotRequired[Sequence["StringFilterTypeDef"]],
        "ecrImagePushedAt": NotRequired[Sequence["DateFilterTypeDef"]],
        "ecrImageRegistry": NotRequired[Sequence["StringFilterTypeDef"]],
        "ecrImageRepositoryName": NotRequired[Sequence["StringFilterTypeDef"]],
        "ecrImageTags": NotRequired[Sequence["StringFilterTypeDef"]],
        "findingArn": NotRequired[Sequence["StringFilterTypeDef"]],
        "findingStatus": NotRequired[Sequence["StringFilterTypeDef"]],
        "findingType": NotRequired[Sequence["StringFilterTypeDef"]],
        "firstObservedAt": NotRequired[Sequence["DateFilterTypeDef"]],
        "inspectorScore": NotRequired[Sequence["NumberFilterTypeDef"]],
        "lastObservedAt": NotRequired[Sequence["DateFilterTypeDef"]],
        "networkProtocol": NotRequired[Sequence["StringFilterTypeDef"]],
        "portRange": NotRequired[Sequence["PortRangeFilterTypeDef"]],
        "relatedVulnerabilities": NotRequired[Sequence["StringFilterTypeDef"]],
        "resourceId": NotRequired[Sequence["StringFilterTypeDef"]],
        "resourceTags": NotRequired[Sequence["MapFilterTypeDef"]],
        "resourceType": NotRequired[Sequence["StringFilterTypeDef"]],
        "severity": NotRequired[Sequence["StringFilterTypeDef"]],
        "title": NotRequired[Sequence["StringFilterTypeDef"]],
        "updatedAt": NotRequired[Sequence["DateFilterTypeDef"]],
        "vendorSeverity": NotRequired[Sequence["StringFilterTypeDef"]],
        "vulnerabilityId": NotRequired[Sequence["StringFilterTypeDef"]],
        "vulnerabilitySource": NotRequired[Sequence["StringFilterTypeDef"]],
        "vulnerablePackages": NotRequired[Sequence["PackageFilterTypeDef"]],
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "action": FilterActionType,
        "arn": str,
        "createdAt": datetime,
        "criteria": "FilterCriteriaTypeDef",
        "name": str,
        "ownerId": str,
        "updatedAt": datetime,
        "description": NotRequired[str],
        "reason": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

FindingTypeAggregationResponseTypeDef = TypedDict(
    "FindingTypeAggregationResponseTypeDef",
    {
        "accountId": NotRequired[str],
        "severityCounts": NotRequired["SeverityCountsTypeDef"],
    },
)

FindingTypeAggregationTypeDef = TypedDict(
    "FindingTypeAggregationTypeDef",
    {
        "findingType": NotRequired[AggregationFindingTypeType],
        "resourceType": NotRequired[AggregationResourceTypeType],
        "sortBy": NotRequired[FindingTypeSortByType],
        "sortOrder": NotRequired[SortOrderType],
    },
)

FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "awsAccountId": str,
        "description": str,
        "findingArn": str,
        "firstObservedAt": datetime,
        "lastObservedAt": datetime,
        "remediation": "RemediationTypeDef",
        "resources": List["ResourceTypeDef"],
        "severity": SeverityType,
        "status": FindingStatusType,
        "type": FindingTypeType,
        "inspectorScore": NotRequired[float],
        "inspectorScoreDetails": NotRequired["InspectorScoreDetailsTypeDef"],
        "networkReachabilityDetails": NotRequired["NetworkReachabilityDetailsTypeDef"],
        "packageVulnerabilityDetails": NotRequired["PackageVulnerabilityDetailsTypeDef"],
        "title": NotRequired[str],
        "updatedAt": NotRequired[datetime],
    },
)

FreeTrialAccountInfoTypeDef = TypedDict(
    "FreeTrialAccountInfoTypeDef",
    {
        "accountId": str,
        "freeTrialInfo": List["FreeTrialInfoTypeDef"],
    },
)

FreeTrialInfoErrorTypeDef = TypedDict(
    "FreeTrialInfoErrorTypeDef",
    {
        "accountId": str,
        "code": FreeTrialInfoErrorCodeType,
        "message": str,
    },
)

FreeTrialInfoTypeDef = TypedDict(
    "FreeTrialInfoTypeDef",
    {
        "end": datetime,
        "start": datetime,
        "status": FreeTrialStatusType,
        "type": FreeTrialTypeType,
    },
)

GetDelegatedAdminAccountResponseTypeDef = TypedDict(
    "GetDelegatedAdminAccountResponseTypeDef",
    {
        "delegatedAdmin": "DelegatedAdminTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFindingsReportStatusRequestRequestTypeDef = TypedDict(
    "GetFindingsReportStatusRequestRequestTypeDef",
    {
        "reportId": NotRequired[str],
    },
)

GetFindingsReportStatusResponseTypeDef = TypedDict(
    "GetFindingsReportStatusResponseTypeDef",
    {
        "destination": "DestinationTypeDef",
        "errorCode": ReportingErrorCodeType,
        "errorMessage": str,
        "filterCriteria": "FilterCriteriaTypeDef",
        "reportId": str,
        "status": ExternalReportStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMemberRequestRequestTypeDef = TypedDict(
    "GetMemberRequestRequestTypeDef",
    {
        "accountId": str,
    },
)

GetMemberResponseTypeDef = TypedDict(
    "GetMemberResponseTypeDef",
    {
        "member": "MemberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImageLayerAggregationResponseTypeDef = TypedDict(
    "ImageLayerAggregationResponseTypeDef",
    {
        "accountId": str,
        "layerHash": str,
        "repository": str,
        "resourceId": str,
        "severityCounts": NotRequired["SeverityCountsTypeDef"],
    },
)

ImageLayerAggregationTypeDef = TypedDict(
    "ImageLayerAggregationTypeDef",
    {
        "layerHashes": NotRequired[Sequence["StringFilterTypeDef"]],
        "repositories": NotRequired[Sequence["StringFilterTypeDef"]],
        "resourceIds": NotRequired[Sequence["StringFilterTypeDef"]],
        "sortBy": NotRequired[ImageLayerSortByType],
        "sortOrder": NotRequired[SortOrderType],
    },
)

InspectorScoreDetailsTypeDef = TypedDict(
    "InspectorScoreDetailsTypeDef",
    {
        "adjustedCvss": NotRequired["CvssScoreDetailsTypeDef"],
    },
)

ListAccountPermissionsRequestRequestTypeDef = TypedDict(
    "ListAccountPermissionsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "service": NotRequired[ServiceType],
    },
)

ListAccountPermissionsResponseTypeDef = TypedDict(
    "ListAccountPermissionsResponseTypeDef",
    {
        "nextToken": str,
        "permissions": List["PermissionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCoverageRequestRequestTypeDef = TypedDict(
    "ListCoverageRequestRequestTypeDef",
    {
        "filterCriteria": NotRequired["CoverageFilterCriteriaTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListCoverageResponseTypeDef = TypedDict(
    "ListCoverageResponseTypeDef",
    {
        "coveredResources": List["CoveredResourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCoverageStatisticsRequestRequestTypeDef = TypedDict(
    "ListCoverageStatisticsRequestRequestTypeDef",
    {
        "filterCriteria": NotRequired["CoverageFilterCriteriaTypeDef"],
        "groupBy": NotRequired[GroupKeyType],
        "nextToken": NotRequired[str],
    },
)

ListCoverageStatisticsResponseTypeDef = TypedDict(
    "ListCoverageStatisticsResponseTypeDef",
    {
        "countsByGroup": List["CountsTypeDef"],
        "nextToken": str,
        "totalCounts": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDelegatedAdminAccountsRequestRequestTypeDef = TypedDict(
    "ListDelegatedAdminAccountsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListDelegatedAdminAccountsResponseTypeDef = TypedDict(
    "ListDelegatedAdminAccountsResponseTypeDef",
    {
        "delegatedAdminAccounts": List["DelegatedAdminAccountTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFiltersRequestRequestTypeDef = TypedDict(
    "ListFiltersRequestRequestTypeDef",
    {
        "action": NotRequired[FilterActionType],
        "arns": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListFiltersResponseTypeDef = TypedDict(
    "ListFiltersResponseTypeDef",
    {
        "filters": List["FilterTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFindingAggregationsRequestRequestTypeDef = TypedDict(
    "ListFindingAggregationsRequestRequestTypeDef",
    {
        "aggregationType": AggregationTypeType,
        "accountIds": NotRequired[Sequence["StringFilterTypeDef"]],
        "aggregationRequest": NotRequired["AggregationRequestTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListFindingAggregationsResponseTypeDef = TypedDict(
    "ListFindingAggregationsResponseTypeDef",
    {
        "aggregationType": AggregationTypeType,
        "nextToken": str,
        "responses": List["AggregationResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFindingsRequestRequestTypeDef = TypedDict(
    "ListFindingsRequestRequestTypeDef",
    {
        "filterCriteria": NotRequired["FilterCriteriaTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortCriteria": NotRequired["SortCriteriaTypeDef"],
    },
)

ListFindingsResponseTypeDef = TypedDict(
    "ListFindingsResponseTypeDef",
    {
        "findings": List["FindingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMembersRequestRequestTypeDef = TypedDict(
    "ListMembersRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "onlyAssociated": NotRequired[bool],
    },
)

ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef",
    {
        "members": List["MemberTypeDef"],
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

ListUsageTotalsRequestRequestTypeDef = TypedDict(
    "ListUsageTotalsRequestRequestTypeDef",
    {
        "accountIds": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListUsageTotalsResponseTypeDef = TypedDict(
    "ListUsageTotalsResponseTypeDef",
    {
        "nextToken": str,
        "totals": List["UsageTotalTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MapFilterTypeDef = TypedDict(
    "MapFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "key": str,
        "value": NotRequired[str],
    },
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "accountId": NotRequired[str],
        "delegatedAdminAccountId": NotRequired[str],
        "relationshipStatus": NotRequired[RelationshipStatusType],
        "updatedAt": NotRequired[datetime],
    },
)

NetworkPathTypeDef = TypedDict(
    "NetworkPathTypeDef",
    {
        "steps": NotRequired[List["StepTypeDef"]],
    },
)

NetworkReachabilityDetailsTypeDef = TypedDict(
    "NetworkReachabilityDetailsTypeDef",
    {
        "networkPath": "NetworkPathTypeDef",
        "openPortRange": "PortRangeTypeDef",
        "protocol": NetworkProtocolType,
    },
)

NumberFilterTypeDef = TypedDict(
    "NumberFilterTypeDef",
    {
        "lowerInclusive": NotRequired[float],
        "upperInclusive": NotRequired[float],
    },
)

PackageAggregationResponseTypeDef = TypedDict(
    "PackageAggregationResponseTypeDef",
    {
        "packageName": str,
        "accountId": NotRequired[str],
        "severityCounts": NotRequired["SeverityCountsTypeDef"],
    },
)

PackageAggregationTypeDef = TypedDict(
    "PackageAggregationTypeDef",
    {
        "packageNames": NotRequired[Sequence["StringFilterTypeDef"]],
        "sortBy": NotRequired[PackageSortByType],
        "sortOrder": NotRequired[SortOrderType],
    },
)

PackageFilterTypeDef = TypedDict(
    "PackageFilterTypeDef",
    {
        "architecture": NotRequired["StringFilterTypeDef"],
        "epoch": NotRequired["NumberFilterTypeDef"],
        "name": NotRequired["StringFilterTypeDef"],
        "release": NotRequired["StringFilterTypeDef"],
        "sourceLayerHash": NotRequired["StringFilterTypeDef"],
        "version": NotRequired["StringFilterTypeDef"],
    },
)

PackageVulnerabilityDetailsTypeDef = TypedDict(
    "PackageVulnerabilityDetailsTypeDef",
    {
        "source": str,
        "vulnerabilityId": str,
        "vulnerablePackages": List["VulnerablePackageTypeDef"],
        "cvss": NotRequired[List["CvssScoreTypeDef"]],
        "referenceUrls": NotRequired[List[str]],
        "relatedVulnerabilities": NotRequired[List[str]],
        "sourceUrl": NotRequired[str],
        "vendorCreatedAt": NotRequired[datetime],
        "vendorSeverity": NotRequired[str],
        "vendorUpdatedAt": NotRequired[datetime],
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

PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {
        "operation": OperationType,
        "service": ServiceType,
    },
)

PortRangeFilterTypeDef = TypedDict(
    "PortRangeFilterTypeDef",
    {
        "beginInclusive": NotRequired[int],
        "endInclusive": NotRequired[int],
    },
)

PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "begin": int,
        "end": int,
    },
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "Url": NotRequired[str],
        "text": NotRequired[str],
    },
)

RemediationTypeDef = TypedDict(
    "RemediationTypeDef",
    {
        "recommendation": NotRequired["RecommendationTypeDef"],
    },
)

RepositoryAggregationResponseTypeDef = TypedDict(
    "RepositoryAggregationResponseTypeDef",
    {
        "repository": str,
        "accountId": NotRequired[str],
        "affectedImages": NotRequired[int],
        "severityCounts": NotRequired["SeverityCountsTypeDef"],
    },
)

RepositoryAggregationTypeDef = TypedDict(
    "RepositoryAggregationTypeDef",
    {
        "repositories": NotRequired[Sequence["StringFilterTypeDef"]],
        "sortBy": NotRequired[RepositorySortByType],
        "sortOrder": NotRequired[SortOrderType],
    },
)

ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "awsEc2Instance": NotRequired["AwsEc2InstanceDetailsTypeDef"],
        "awsEcrContainerImage": NotRequired["AwsEcrContainerImageDetailsTypeDef"],
    },
)

ResourceScanMetadataTypeDef = TypedDict(
    "ResourceScanMetadataTypeDef",
    {
        "ec2": NotRequired["Ec2MetadataTypeDef"],
        "ecrImage": NotRequired["EcrContainerImageMetadataTypeDef"],
        "ecrRepository": NotRequired["EcrRepositoryMetadataTypeDef"],
    },
)

ResourceStateTypeDef = TypedDict(
    "ResourceStateTypeDef",
    {
        "ec2": "StateTypeDef",
        "ecr": "StateTypeDef",
    },
)

ResourceStatusTypeDef = TypedDict(
    "ResourceStatusTypeDef",
    {
        "ec2": StatusType,
        "ecr": StatusType,
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "id": str,
        "type": ResourceTypeType,
        "details": NotRequired["ResourceDetailsTypeDef"],
        "partition": NotRequired[str],
        "region": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
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

ScanStatusTypeDef = TypedDict(
    "ScanStatusTypeDef",
    {
        "reason": ScanStatusReasonType,
        "statusCode": ScanStatusCodeType,
    },
)

SeverityCountsTypeDef = TypedDict(
    "SeverityCountsTypeDef",
    {
        "all": NotRequired[int],
        "critical": NotRequired[int],
        "high": NotRequired[int],
        "medium": NotRequired[int],
    },
)

SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef",
    {
        "field": SortFieldType,
        "sortOrder": SortOrderType,
    },
)

StateTypeDef = TypedDict(
    "StateTypeDef",
    {
        "errorCode": ErrorCodeType,
        "errorMessage": str,
        "status": StatusType,
    },
)

StepTypeDef = TypedDict(
    "StepTypeDef",
    {
        "componentId": str,
        "componentType": str,
    },
)

StringFilterTypeDef = TypedDict(
    "StringFilterTypeDef",
    {
        "comparison": StringComparisonType,
        "value": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

TitleAggregationResponseTypeDef = TypedDict(
    "TitleAggregationResponseTypeDef",
    {
        "title": str,
        "accountId": NotRequired[str],
        "severityCounts": NotRequired["SeverityCountsTypeDef"],
        "vulnerabilityId": NotRequired[str],
    },
)

TitleAggregationTypeDef = TypedDict(
    "TitleAggregationTypeDef",
    {
        "resourceType": NotRequired[AggregationResourceTypeType],
        "sortBy": NotRequired[TitleSortByType],
        "sortOrder": NotRequired[SortOrderType],
        "titles": NotRequired[Sequence["StringFilterTypeDef"]],
        "vulnerabilityIds": NotRequired[Sequence["StringFilterTypeDef"]],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateFilterRequestRequestTypeDef = TypedDict(
    "UpdateFilterRequestRequestTypeDef",
    {
        "filterArn": str,
        "action": NotRequired[FilterActionType],
        "description": NotRequired[str],
        "filterCriteria": NotRequired["FilterCriteriaTypeDef"],
        "name": NotRequired[str],
    },
)

UpdateFilterResponseTypeDef = TypedDict(
    "UpdateFilterResponseTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "autoEnable": "AutoEnableTypeDef",
    },
)

UpdateOrganizationConfigurationResponseTypeDef = TypedDict(
    "UpdateOrganizationConfigurationResponseTypeDef",
    {
        "autoEnable": "AutoEnableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsageTotalTypeDef = TypedDict(
    "UsageTotalTypeDef",
    {
        "accountId": NotRequired[str],
        "usage": NotRequired[List["UsageTypeDef"]],
    },
)

UsageTypeDef = TypedDict(
    "UsageTypeDef",
    {
        "currency": NotRequired[Literal["USD"]],
        "estimatedMonthlyCost": NotRequired[float],
        "total": NotRequired[float],
        "type": NotRequired[UsageTypeType],
    },
)

VulnerablePackageTypeDef = TypedDict(
    "VulnerablePackageTypeDef",
    {
        "name": str,
        "version": str,
        "arch": NotRequired[str],
        "epoch": NotRequired[int],
        "filePath": NotRequired[str],
        "fixedInVersion": NotRequired[str],
        "packageManager": NotRequired[PackageManagerType],
        "release": NotRequired[str],
        "sourceLayerHash": NotRequired[str],
    },
)
