"""
Type annotations for macie2 service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_macie2/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_macie2.type_defs import AcceptInvitationRequestRequestTypeDef

    data: AcceptInvitationRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AdminStatusType,
    AllowsUnencryptedObjectUploadsType,
    DataIdentifierSeverityType,
    DayOfWeekType,
    EffectivePermissionType,
    EncryptionTypeType,
    ErrorCodeType,
    FindingCategoryType,
    FindingPublishingFrequencyType,
    FindingsFilterActionType,
    FindingStatisticsSortAttributeNameType,
    FindingTypeType,
    GroupByType,
    IsDefinedInJobType,
    IsMonitoredByJobType,
    JobComparatorType,
    JobStatusType,
    JobTypeType,
    LastRunErrorStatusCodeType,
    ListJobsFilterKeyType,
    ListJobsSortAttributeNameType,
    MacieStatusType,
    ManagedDataIdentifierSelectorType,
    OrderByType,
    RelationshipStatusType,
    ScopeFilterKeyType,
    SearchResourcesComparatorType,
    SearchResourcesSimpleCriterionKeyType,
    SearchResourcesSortAttributeNameType,
    SensitiveDataItemCategoryType,
    SeverityDescriptionType,
    SharedAccessType,
    SimpleCriterionKeyForJobType,
    StorageClassType,
    TimeRangeType,
    TypeType,
    UsageStatisticsFilterComparatorType,
    UsageStatisticsFilterKeyType,
    UsageStatisticsSortKeyType,
    UsageTypeType,
    UserIdentityTypeType,
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
    "AcceptInvitationRequestRequestTypeDef",
    "AccessControlListTypeDef",
    "AccountDetailTypeDef",
    "AccountLevelPermissionsTypeDef",
    "AdminAccountTypeDef",
    "ApiCallDetailsTypeDef",
    "AssumedRoleTypeDef",
    "AwsAccountTypeDef",
    "AwsServiceTypeDef",
    "BatchGetCustomDataIdentifierSummaryTypeDef",
    "BatchGetCustomDataIdentifiersRequestRequestTypeDef",
    "BatchGetCustomDataIdentifiersResponseTypeDef",
    "BlockPublicAccessTypeDef",
    "BucketCountByEffectivePermissionTypeDef",
    "BucketCountByEncryptionTypeTypeDef",
    "BucketCountBySharedAccessTypeTypeDef",
    "BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef",
    "BucketCriteriaAdditionalPropertiesTypeDef",
    "BucketLevelPermissionsTypeDef",
    "BucketMetadataTypeDef",
    "BucketPermissionConfigurationTypeDef",
    "BucketPolicyTypeDef",
    "BucketPublicAccessTypeDef",
    "BucketServerSideEncryptionTypeDef",
    "BucketSortCriteriaTypeDef",
    "CellTypeDef",
    "ClassificationDetailsTypeDef",
    "ClassificationExportConfigurationTypeDef",
    "ClassificationResultStatusTypeDef",
    "ClassificationResultTypeDef",
    "CreateClassificationJobRequestRequestTypeDef",
    "CreateClassificationJobResponseTypeDef",
    "CreateCustomDataIdentifierRequestRequestTypeDef",
    "CreateCustomDataIdentifierResponseTypeDef",
    "CreateFindingsFilterRequestRequestTypeDef",
    "CreateFindingsFilterResponseTypeDef",
    "CreateInvitationsRequestRequestTypeDef",
    "CreateInvitationsResponseTypeDef",
    "CreateMemberRequestRequestTypeDef",
    "CreateMemberResponseTypeDef",
    "CreateSampleFindingsRequestRequestTypeDef",
    "CriteriaBlockForJobTypeDef",
    "CriteriaForJobTypeDef",
    "CriterionAdditionalPropertiesTypeDef",
    "CustomDataIdentifierSummaryTypeDef",
    "CustomDataIdentifiersTypeDef",
    "CustomDetectionTypeDef",
    "DeclineInvitationsRequestRequestTypeDef",
    "DeclineInvitationsResponseTypeDef",
    "DefaultDetectionTypeDef",
    "DeleteCustomDataIdentifierRequestRequestTypeDef",
    "DeleteFindingsFilterRequestRequestTypeDef",
    "DeleteInvitationsRequestRequestTypeDef",
    "DeleteInvitationsResponseTypeDef",
    "DeleteMemberRequestRequestTypeDef",
    "DescribeBucketsRequestRequestTypeDef",
    "DescribeBucketsResponseTypeDef",
    "DescribeClassificationJobRequestRequestTypeDef",
    "DescribeClassificationJobResponseTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    "DisassociateMemberRequestRequestTypeDef",
    "DomainDetailsTypeDef",
    "EnableMacieRequestRequestTypeDef",
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    "FederatedUserTypeDef",
    "FindingActionTypeDef",
    "FindingActorTypeDef",
    "FindingCriteriaTypeDef",
    "FindingStatisticsSortCriteriaTypeDef",
    "FindingTypeDef",
    "FindingsFilterListItemTypeDef",
    "GetAdministratorAccountResponseTypeDef",
    "GetBucketStatisticsRequestRequestTypeDef",
    "GetBucketStatisticsResponseTypeDef",
    "GetClassificationExportConfigurationResponseTypeDef",
    "GetCustomDataIdentifierRequestRequestTypeDef",
    "GetCustomDataIdentifierResponseTypeDef",
    "GetFindingStatisticsRequestRequestTypeDef",
    "GetFindingStatisticsResponseTypeDef",
    "GetFindingsFilterRequestRequestTypeDef",
    "GetFindingsFilterResponseTypeDef",
    "GetFindingsPublicationConfigurationResponseTypeDef",
    "GetFindingsRequestRequestTypeDef",
    "GetFindingsResponseTypeDef",
    "GetInvitationsCountResponseTypeDef",
    "GetMacieSessionResponseTypeDef",
    "GetMasterAccountResponseTypeDef",
    "GetMemberRequestRequestTypeDef",
    "GetMemberResponseTypeDef",
    "GetUsageStatisticsRequestRequestTypeDef",
    "GetUsageStatisticsResponseTypeDef",
    "GetUsageTotalsRequestRequestTypeDef",
    "GetUsageTotalsResponseTypeDef",
    "GroupCountTypeDef",
    "IamUserTypeDef",
    "InvitationTypeDef",
    "IpAddressDetailsTypeDef",
    "IpCityTypeDef",
    "IpCountryTypeDef",
    "IpGeoLocationTypeDef",
    "IpOwnerTypeDef",
    "JobDetailsTypeDef",
    "JobScheduleFrequencyTypeDef",
    "JobScopeTermTypeDef",
    "JobScopingBlockTypeDef",
    "JobSummaryTypeDef",
    "KeyValuePairTypeDef",
    "LastRunErrorStatusTypeDef",
    "ListClassificationJobsRequestRequestTypeDef",
    "ListClassificationJobsResponseTypeDef",
    "ListCustomDataIdentifiersRequestRequestTypeDef",
    "ListCustomDataIdentifiersResponseTypeDef",
    "ListFindingsFiltersRequestRequestTypeDef",
    "ListFindingsFiltersResponseTypeDef",
    "ListFindingsRequestRequestTypeDef",
    "ListFindingsResponseTypeDef",
    "ListInvitationsRequestRequestTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListJobsFilterCriteriaTypeDef",
    "ListJobsFilterTermTypeDef",
    "ListJobsSortCriteriaTypeDef",
    "ListManagedDataIdentifiersRequestRequestTypeDef",
    "ListManagedDataIdentifiersResponseTypeDef",
    "ListMembersRequestRequestTypeDef",
    "ListMembersResponseTypeDef",
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ManagedDataIdentifierSummaryTypeDef",
    "MatchingBucketTypeDef",
    "MatchingResourceTypeDef",
    "MemberTypeDef",
    "MonthlyScheduleTypeDef",
    "ObjectCountByEncryptionTypeTypeDef",
    "ObjectLevelStatisticsTypeDef",
    "OccurrencesTypeDef",
    "PageTypeDef",
    "PaginatorConfigTypeDef",
    "PolicyDetailsTypeDef",
    "PutClassificationExportConfigurationRequestRequestTypeDef",
    "PutClassificationExportConfigurationResponseTypeDef",
    "PutFindingsPublicationConfigurationRequestRequestTypeDef",
    "RangeTypeDef",
    "RecordTypeDef",
    "ReplicationDetailsTypeDef",
    "ResourcesAffectedTypeDef",
    "ResponseMetadataTypeDef",
    "S3BucketCriteriaForJobTypeDef",
    "S3BucketDefinitionForJobTypeDef",
    "S3BucketOwnerTypeDef",
    "S3BucketTypeDef",
    "S3DestinationTypeDef",
    "S3JobDefinitionTypeDef",
    "S3ObjectTypeDef",
    "ScopingTypeDef",
    "SearchResourcesBucketCriteriaTypeDef",
    "SearchResourcesCriteriaBlockTypeDef",
    "SearchResourcesCriteriaTypeDef",
    "SearchResourcesRequestRequestTypeDef",
    "SearchResourcesResponseTypeDef",
    "SearchResourcesSimpleCriterionTypeDef",
    "SearchResourcesSortCriteriaTypeDef",
    "SearchResourcesTagCriterionPairTypeDef",
    "SearchResourcesTagCriterionTypeDef",
    "SecurityHubConfigurationTypeDef",
    "SensitiveDataItemTypeDef",
    "ServerSideEncryptionTypeDef",
    "ServiceLimitTypeDef",
    "SessionContextAttributesTypeDef",
    "SessionContextTypeDef",
    "SessionIssuerTypeDef",
    "SeverityLevelTypeDef",
    "SeverityTypeDef",
    "SimpleCriterionForJobTypeDef",
    "SimpleScopeTermTypeDef",
    "SortCriteriaTypeDef",
    "StatisticsTypeDef",
    "TagCriterionForJobTypeDef",
    "TagCriterionPairForJobTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagScopeTermTypeDef",
    "TagValuePairTypeDef",
    "TestCustomDataIdentifierRequestRequestTypeDef",
    "TestCustomDataIdentifierResponseTypeDef",
    "UnprocessedAccountTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateClassificationJobRequestRequestTypeDef",
    "UpdateFindingsFilterRequestRequestTypeDef",
    "UpdateFindingsFilterResponseTypeDef",
    "UpdateMacieSessionRequestRequestTypeDef",
    "UpdateMemberSessionRequestRequestTypeDef",
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    "UsageByAccountTypeDef",
    "UsageRecordTypeDef",
    "UsageStatisticsFilterTypeDef",
    "UsageStatisticsSortByTypeDef",
    "UsageTotalTypeDef",
    "UserIdentityRootTypeDef",
    "UserIdentityTypeDef",
    "UserPausedDetailsTypeDef",
    "WeeklyScheduleTypeDef",
)

AcceptInvitationRequestRequestTypeDef = TypedDict(
    "AcceptInvitationRequestRequestTypeDef",
    {
        "invitationId": str,
        "administratorAccountId": NotRequired[str],
        "masterAccount": NotRequired[str],
    },
)

AccessControlListTypeDef = TypedDict(
    "AccessControlListTypeDef",
    {
        "allowsPublicReadAccess": NotRequired[bool],
        "allowsPublicWriteAccess": NotRequired[bool],
    },
)

AccountDetailTypeDef = TypedDict(
    "AccountDetailTypeDef",
    {
        "accountId": str,
        "email": str,
    },
)

AccountLevelPermissionsTypeDef = TypedDict(
    "AccountLevelPermissionsTypeDef",
    {
        "blockPublicAccess": NotRequired["BlockPublicAccessTypeDef"],
    },
)

AdminAccountTypeDef = TypedDict(
    "AdminAccountTypeDef",
    {
        "accountId": NotRequired[str],
        "status": NotRequired[AdminStatusType],
    },
)

ApiCallDetailsTypeDef = TypedDict(
    "ApiCallDetailsTypeDef",
    {
        "api": NotRequired[str],
        "apiServiceName": NotRequired[str],
        "firstSeen": NotRequired[datetime],
        "lastSeen": NotRequired[datetime],
    },
)

AssumedRoleTypeDef = TypedDict(
    "AssumedRoleTypeDef",
    {
        "accessKeyId": NotRequired[str],
        "accountId": NotRequired[str],
        "arn": NotRequired[str],
        "principalId": NotRequired[str],
        "sessionContext": NotRequired["SessionContextTypeDef"],
    },
)

AwsAccountTypeDef = TypedDict(
    "AwsAccountTypeDef",
    {
        "accountId": NotRequired[str],
        "principalId": NotRequired[str],
    },
)

AwsServiceTypeDef = TypedDict(
    "AwsServiceTypeDef",
    {
        "invokedBy": NotRequired[str],
    },
)

BatchGetCustomDataIdentifierSummaryTypeDef = TypedDict(
    "BatchGetCustomDataIdentifierSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "deleted": NotRequired[bool],
        "description": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
    },
)

BatchGetCustomDataIdentifiersRequestRequestTypeDef = TypedDict(
    "BatchGetCustomDataIdentifiersRequestRequestTypeDef",
    {
        "ids": NotRequired[Sequence[str]],
    },
)

BatchGetCustomDataIdentifiersResponseTypeDef = TypedDict(
    "BatchGetCustomDataIdentifiersResponseTypeDef",
    {
        "customDataIdentifiers": List["BatchGetCustomDataIdentifierSummaryTypeDef"],
        "notFoundIdentifierIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BlockPublicAccessTypeDef = TypedDict(
    "BlockPublicAccessTypeDef",
    {
        "blockPublicAcls": NotRequired[bool],
        "blockPublicPolicy": NotRequired[bool],
        "ignorePublicAcls": NotRequired[bool],
        "restrictPublicBuckets": NotRequired[bool],
    },
)

BucketCountByEffectivePermissionTypeDef = TypedDict(
    "BucketCountByEffectivePermissionTypeDef",
    {
        "publiclyAccessible": NotRequired[int],
        "publiclyReadable": NotRequired[int],
        "publiclyWritable": NotRequired[int],
        "unknown": NotRequired[int],
    },
)

BucketCountByEncryptionTypeTypeDef = TypedDict(
    "BucketCountByEncryptionTypeTypeDef",
    {
        "kmsManaged": NotRequired[int],
        "s3Managed": NotRequired[int],
        "unencrypted": NotRequired[int],
        "unknown": NotRequired[int],
    },
)

BucketCountBySharedAccessTypeTypeDef = TypedDict(
    "BucketCountBySharedAccessTypeTypeDef",
    {
        "external": NotRequired[int],
        "internal": NotRequired[int],
        "notShared": NotRequired[int],
        "unknown": NotRequired[int],
    },
)

BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef = TypedDict(
    "BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef",
    {
        "allowsUnencryptedObjectUploads": NotRequired[int],
        "deniesUnencryptedObjectUploads": NotRequired[int],
        "unknown": NotRequired[int],
    },
)

BucketCriteriaAdditionalPropertiesTypeDef = TypedDict(
    "BucketCriteriaAdditionalPropertiesTypeDef",
    {
        "eq": NotRequired[Sequence[str]],
        "gt": NotRequired[int],
        "gte": NotRequired[int],
        "lt": NotRequired[int],
        "lte": NotRequired[int],
        "neq": NotRequired[Sequence[str]],
        "prefix": NotRequired[str],
    },
)

BucketLevelPermissionsTypeDef = TypedDict(
    "BucketLevelPermissionsTypeDef",
    {
        "accessControlList": NotRequired["AccessControlListTypeDef"],
        "blockPublicAccess": NotRequired["BlockPublicAccessTypeDef"],
        "bucketPolicy": NotRequired["BucketPolicyTypeDef"],
    },
)

BucketMetadataTypeDef = TypedDict(
    "BucketMetadataTypeDef",
    {
        "accountId": NotRequired[str],
        "allowsUnencryptedObjectUploads": NotRequired[AllowsUnencryptedObjectUploadsType],
        "bucketArn": NotRequired[str],
        "bucketCreatedAt": NotRequired[datetime],
        "bucketName": NotRequired[str],
        "classifiableObjectCount": NotRequired[int],
        "classifiableSizeInBytes": NotRequired[int],
        "errorCode": NotRequired[Literal["ACCESS_DENIED"]],
        "errorMessage": NotRequired[str],
        "jobDetails": NotRequired["JobDetailsTypeDef"],
        "lastUpdated": NotRequired[datetime],
        "objectCount": NotRequired[int],
        "objectCountByEncryptionType": NotRequired["ObjectCountByEncryptionTypeTypeDef"],
        "publicAccess": NotRequired["BucketPublicAccessTypeDef"],
        "region": NotRequired[str],
        "replicationDetails": NotRequired["ReplicationDetailsTypeDef"],
        "serverSideEncryption": NotRequired["BucketServerSideEncryptionTypeDef"],
        "sharedAccess": NotRequired[SharedAccessType],
        "sizeInBytes": NotRequired[int],
        "sizeInBytesCompressed": NotRequired[int],
        "tags": NotRequired[List["KeyValuePairTypeDef"]],
        "unclassifiableObjectCount": NotRequired["ObjectLevelStatisticsTypeDef"],
        "unclassifiableObjectSizeInBytes": NotRequired["ObjectLevelStatisticsTypeDef"],
        "versioning": NotRequired[bool],
    },
)

BucketPermissionConfigurationTypeDef = TypedDict(
    "BucketPermissionConfigurationTypeDef",
    {
        "accountLevelPermissions": NotRequired["AccountLevelPermissionsTypeDef"],
        "bucketLevelPermissions": NotRequired["BucketLevelPermissionsTypeDef"],
    },
)

BucketPolicyTypeDef = TypedDict(
    "BucketPolicyTypeDef",
    {
        "allowsPublicReadAccess": NotRequired[bool],
        "allowsPublicWriteAccess": NotRequired[bool],
    },
)

BucketPublicAccessTypeDef = TypedDict(
    "BucketPublicAccessTypeDef",
    {
        "effectivePermission": NotRequired[EffectivePermissionType],
        "permissionConfiguration": NotRequired["BucketPermissionConfigurationTypeDef"],
    },
)

BucketServerSideEncryptionTypeDef = TypedDict(
    "BucketServerSideEncryptionTypeDef",
    {
        "kmsMasterKeyId": NotRequired[str],
        "type": NotRequired[TypeType],
    },
)

BucketSortCriteriaTypeDef = TypedDict(
    "BucketSortCriteriaTypeDef",
    {
        "attributeName": NotRequired[str],
        "orderBy": NotRequired[OrderByType],
    },
)

CellTypeDef = TypedDict(
    "CellTypeDef",
    {
        "cellReference": NotRequired[str],
        "column": NotRequired[int],
        "columnName": NotRequired[str],
        "row": NotRequired[int],
    },
)

ClassificationDetailsTypeDef = TypedDict(
    "ClassificationDetailsTypeDef",
    {
        "detailedResultsLocation": NotRequired[str],
        "jobArn": NotRequired[str],
        "jobId": NotRequired[str],
        "result": NotRequired["ClassificationResultTypeDef"],
    },
)

ClassificationExportConfigurationTypeDef = TypedDict(
    "ClassificationExportConfigurationTypeDef",
    {
        "s3Destination": NotRequired["S3DestinationTypeDef"],
    },
)

ClassificationResultStatusTypeDef = TypedDict(
    "ClassificationResultStatusTypeDef",
    {
        "code": NotRequired[str],
        "reason": NotRequired[str],
    },
)

ClassificationResultTypeDef = TypedDict(
    "ClassificationResultTypeDef",
    {
        "additionalOccurrences": NotRequired[bool],
        "customDataIdentifiers": NotRequired["CustomDataIdentifiersTypeDef"],
        "mimeType": NotRequired[str],
        "sensitiveData": NotRequired[List["SensitiveDataItemTypeDef"]],
        "sizeClassified": NotRequired[int],
        "status": NotRequired["ClassificationResultStatusTypeDef"],
    },
)

CreateClassificationJobRequestRequestTypeDef = TypedDict(
    "CreateClassificationJobRequestRequestTypeDef",
    {
        "clientToken": str,
        "jobType": JobTypeType,
        "name": str,
        "s3JobDefinition": "S3JobDefinitionTypeDef",
        "customDataIdentifierIds": NotRequired[Sequence[str]],
        "description": NotRequired[str],
        "initialRun": NotRequired[bool],
        "managedDataIdentifierIds": NotRequired[Sequence[str]],
        "managedDataIdentifierSelector": NotRequired[ManagedDataIdentifierSelectorType],
        "samplingPercentage": NotRequired[int],
        "scheduleFrequency": NotRequired["JobScheduleFrequencyTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateClassificationJobResponseTypeDef = TypedDict(
    "CreateClassificationJobResponseTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCustomDataIdentifierRequestRequestTypeDef = TypedDict(
    "CreateCustomDataIdentifierRequestRequestTypeDef",
    {
        "name": str,
        "regex": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "ignoreWords": NotRequired[Sequence[str]],
        "keywords": NotRequired[Sequence[str]],
        "maximumMatchDistance": NotRequired[int],
        "severityLevels": NotRequired[Sequence["SeverityLevelTypeDef"]],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateCustomDataIdentifierResponseTypeDef = TypedDict(
    "CreateCustomDataIdentifierResponseTypeDef",
    {
        "customDataIdentifierId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFindingsFilterRequestRequestTypeDef = TypedDict(
    "CreateFindingsFilterRequestRequestTypeDef",
    {
        "action": FindingsFilterActionType,
        "findingCriteria": "FindingCriteriaTypeDef",
        "name": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "position": NotRequired[int],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateFindingsFilterResponseTypeDef = TypedDict(
    "CreateFindingsFilterResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInvitationsRequestRequestTypeDef = TypedDict(
    "CreateInvitationsRequestRequestTypeDef",
    {
        "accountIds": Sequence[str],
        "disableEmailNotification": NotRequired[bool],
        "message": NotRequired[str],
    },
)

CreateInvitationsResponseTypeDef = TypedDict(
    "CreateInvitationsResponseTypeDef",
    {
        "unprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMemberRequestRequestTypeDef = TypedDict(
    "CreateMemberRequestRequestTypeDef",
    {
        "account": "AccountDetailTypeDef",
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateMemberResponseTypeDef = TypedDict(
    "CreateMemberResponseTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSampleFindingsRequestRequestTypeDef = TypedDict(
    "CreateSampleFindingsRequestRequestTypeDef",
    {
        "findingTypes": NotRequired[Sequence[FindingTypeType]],
    },
)

CriteriaBlockForJobTypeDef = TypedDict(
    "CriteriaBlockForJobTypeDef",
    {
        "and": NotRequired[Sequence["CriteriaForJobTypeDef"]],
    },
)

CriteriaForJobTypeDef = TypedDict(
    "CriteriaForJobTypeDef",
    {
        "simpleCriterion": NotRequired["SimpleCriterionForJobTypeDef"],
        "tagCriterion": NotRequired["TagCriterionForJobTypeDef"],
    },
)

CriterionAdditionalPropertiesTypeDef = TypedDict(
    "CriterionAdditionalPropertiesTypeDef",
    {
        "eq": NotRequired[Sequence[str]],
        "eqExactMatch": NotRequired[Sequence[str]],
        "gt": NotRequired[int],
        "gte": NotRequired[int],
        "lt": NotRequired[int],
        "lte": NotRequired[int],
        "neq": NotRequired[Sequence[str]],
    },
)

CustomDataIdentifierSummaryTypeDef = TypedDict(
    "CustomDataIdentifierSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
    },
)

CustomDataIdentifiersTypeDef = TypedDict(
    "CustomDataIdentifiersTypeDef",
    {
        "detections": NotRequired[List["CustomDetectionTypeDef"]],
        "totalCount": NotRequired[int],
    },
)

CustomDetectionTypeDef = TypedDict(
    "CustomDetectionTypeDef",
    {
        "arn": NotRequired[str],
        "count": NotRequired[int],
        "name": NotRequired[str],
        "occurrences": NotRequired["OccurrencesTypeDef"],
    },
)

DeclineInvitationsRequestRequestTypeDef = TypedDict(
    "DeclineInvitationsRequestRequestTypeDef",
    {
        "accountIds": Sequence[str],
    },
)

DeclineInvitationsResponseTypeDef = TypedDict(
    "DeclineInvitationsResponseTypeDef",
    {
        "unprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefaultDetectionTypeDef = TypedDict(
    "DefaultDetectionTypeDef",
    {
        "count": NotRequired[int],
        "occurrences": NotRequired["OccurrencesTypeDef"],
        "type": NotRequired[str],
    },
)

DeleteCustomDataIdentifierRequestRequestTypeDef = TypedDict(
    "DeleteCustomDataIdentifierRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteFindingsFilterRequestRequestTypeDef = TypedDict(
    "DeleteFindingsFilterRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteInvitationsRequestRequestTypeDef = TypedDict(
    "DeleteInvitationsRequestRequestTypeDef",
    {
        "accountIds": Sequence[str],
    },
)

DeleteInvitationsResponseTypeDef = TypedDict(
    "DeleteInvitationsResponseTypeDef",
    {
        "unprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMemberRequestRequestTypeDef = TypedDict(
    "DeleteMemberRequestRequestTypeDef",
    {
        "id": str,
    },
)

DescribeBucketsRequestRequestTypeDef = TypedDict(
    "DescribeBucketsRequestRequestTypeDef",
    {
        "criteria": NotRequired[Mapping[str, "BucketCriteriaAdditionalPropertiesTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortCriteria": NotRequired["BucketSortCriteriaTypeDef"],
    },
)

DescribeBucketsResponseTypeDef = TypedDict(
    "DescribeBucketsResponseTypeDef",
    {
        "buckets": List["BucketMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClassificationJobRequestRequestTypeDef = TypedDict(
    "DescribeClassificationJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

DescribeClassificationJobResponseTypeDef = TypedDict(
    "DescribeClassificationJobResponseTypeDef",
    {
        "clientToken": str,
        "createdAt": datetime,
        "customDataIdentifierIds": List[str],
        "description": str,
        "initialRun": bool,
        "jobArn": str,
        "jobId": str,
        "jobStatus": JobStatusType,
        "jobType": JobTypeType,
        "lastRunErrorStatus": "LastRunErrorStatusTypeDef",
        "lastRunTime": datetime,
        "managedDataIdentifierIds": List[str],
        "managedDataIdentifierSelector": ManagedDataIdentifierSelectorType,
        "name": str,
        "s3JobDefinition": "S3JobDefinitionTypeDef",
        "samplingPercentage": int,
        "scheduleFrequency": "JobScheduleFrequencyTypeDef",
        "statistics": "StatisticsTypeDef",
        "tags": Dict[str, str],
        "userPausedDetails": "UserPausedDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {
        "autoEnable": bool,
        "maxAccountLimitReached": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "adminAccountId": str,
    },
)

DisassociateMemberRequestRequestTypeDef = TypedDict(
    "DisassociateMemberRequestRequestTypeDef",
    {
        "id": str,
    },
)

DomainDetailsTypeDef = TypedDict(
    "DomainDetailsTypeDef",
    {
        "domainName": NotRequired[str],
    },
)

EnableMacieRequestRequestTypeDef = TypedDict(
    "EnableMacieRequestRequestTypeDef",
    {
        "clientToken": NotRequired[str],
        "findingPublishingFrequency": NotRequired[FindingPublishingFrequencyType],
        "status": NotRequired[MacieStatusType],
    },
)

EnableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "adminAccountId": str,
        "clientToken": NotRequired[str],
    },
)

FederatedUserTypeDef = TypedDict(
    "FederatedUserTypeDef",
    {
        "accessKeyId": NotRequired[str],
        "accountId": NotRequired[str],
        "arn": NotRequired[str],
        "principalId": NotRequired[str],
        "sessionContext": NotRequired["SessionContextTypeDef"],
    },
)

FindingActionTypeDef = TypedDict(
    "FindingActionTypeDef",
    {
        "actionType": NotRequired[Literal["AWS_API_CALL"]],
        "apiCallDetails": NotRequired["ApiCallDetailsTypeDef"],
    },
)

FindingActorTypeDef = TypedDict(
    "FindingActorTypeDef",
    {
        "domainDetails": NotRequired["DomainDetailsTypeDef"],
        "ipAddressDetails": NotRequired["IpAddressDetailsTypeDef"],
        "userIdentity": NotRequired["UserIdentityTypeDef"],
    },
)

FindingCriteriaTypeDef = TypedDict(
    "FindingCriteriaTypeDef",
    {
        "criterion": NotRequired[Mapping[str, "CriterionAdditionalPropertiesTypeDef"]],
    },
)

FindingStatisticsSortCriteriaTypeDef = TypedDict(
    "FindingStatisticsSortCriteriaTypeDef",
    {
        "attributeName": NotRequired[FindingStatisticsSortAttributeNameType],
        "orderBy": NotRequired[OrderByType],
    },
)

FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "accountId": NotRequired[str],
        "archived": NotRequired[bool],
        "category": NotRequired[FindingCategoryType],
        "classificationDetails": NotRequired["ClassificationDetailsTypeDef"],
        "count": NotRequired[int],
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "id": NotRequired[str],
        "partition": NotRequired[str],
        "policyDetails": NotRequired["PolicyDetailsTypeDef"],
        "region": NotRequired[str],
        "resourcesAffected": NotRequired["ResourcesAffectedTypeDef"],
        "sample": NotRequired[bool],
        "schemaVersion": NotRequired[str],
        "severity": NotRequired["SeverityTypeDef"],
        "title": NotRequired[str],
        "type": NotRequired[FindingTypeType],
        "updatedAt": NotRequired[datetime],
    },
)

FindingsFilterListItemTypeDef = TypedDict(
    "FindingsFilterListItemTypeDef",
    {
        "action": NotRequired[FindingsFilterActionType],
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

GetAdministratorAccountResponseTypeDef = TypedDict(
    "GetAdministratorAccountResponseTypeDef",
    {
        "administrator": "InvitationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketStatisticsRequestRequestTypeDef = TypedDict(
    "GetBucketStatisticsRequestRequestTypeDef",
    {
        "accountId": NotRequired[str],
    },
)

GetBucketStatisticsResponseTypeDef = TypedDict(
    "GetBucketStatisticsResponseTypeDef",
    {
        "bucketCount": int,
        "bucketCountByEffectivePermission": "BucketCountByEffectivePermissionTypeDef",
        "bucketCountByEncryptionType": "BucketCountByEncryptionTypeTypeDef",
        "bucketCountByObjectEncryptionRequirement": (
            "BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef"
        ),
        "bucketCountBySharedAccessType": "BucketCountBySharedAccessTypeTypeDef",
        "classifiableObjectCount": int,
        "classifiableSizeInBytes": int,
        "lastUpdated": datetime,
        "objectCount": int,
        "sizeInBytes": int,
        "sizeInBytesCompressed": int,
        "unclassifiableObjectCount": "ObjectLevelStatisticsTypeDef",
        "unclassifiableObjectSizeInBytes": "ObjectLevelStatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetClassificationExportConfigurationResponseTypeDef = TypedDict(
    "GetClassificationExportConfigurationResponseTypeDef",
    {
        "configuration": "ClassificationExportConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCustomDataIdentifierRequestRequestTypeDef = TypedDict(
    "GetCustomDataIdentifierRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetCustomDataIdentifierResponseTypeDef = TypedDict(
    "GetCustomDataIdentifierResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deleted": bool,
        "description": str,
        "id": str,
        "ignoreWords": List[str],
        "keywords": List[str],
        "maximumMatchDistance": int,
        "name": str,
        "regex": str,
        "severityLevels": List["SeverityLevelTypeDef"],
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFindingStatisticsRequestRequestTypeDef = TypedDict(
    "GetFindingStatisticsRequestRequestTypeDef",
    {
        "groupBy": GroupByType,
        "findingCriteria": NotRequired["FindingCriteriaTypeDef"],
        "size": NotRequired[int],
        "sortCriteria": NotRequired["FindingStatisticsSortCriteriaTypeDef"],
    },
)

GetFindingStatisticsResponseTypeDef = TypedDict(
    "GetFindingStatisticsResponseTypeDef",
    {
        "countsByGroup": List["GroupCountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFindingsFilterRequestRequestTypeDef = TypedDict(
    "GetFindingsFilterRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetFindingsFilterResponseTypeDef = TypedDict(
    "GetFindingsFilterResponseTypeDef",
    {
        "action": FindingsFilterActionType,
        "arn": str,
        "description": str,
        "findingCriteria": "FindingCriteriaTypeDef",
        "id": str,
        "name": str,
        "position": int,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFindingsPublicationConfigurationResponseTypeDef = TypedDict(
    "GetFindingsPublicationConfigurationResponseTypeDef",
    {
        "securityHubConfiguration": "SecurityHubConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFindingsRequestRequestTypeDef = TypedDict(
    "GetFindingsRequestRequestTypeDef",
    {
        "findingIds": Sequence[str],
        "sortCriteria": NotRequired["SortCriteriaTypeDef"],
    },
)

GetFindingsResponseTypeDef = TypedDict(
    "GetFindingsResponseTypeDef",
    {
        "findings": List["FindingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInvitationsCountResponseTypeDef = TypedDict(
    "GetInvitationsCountResponseTypeDef",
    {
        "invitationsCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMacieSessionResponseTypeDef = TypedDict(
    "GetMacieSessionResponseTypeDef",
    {
        "createdAt": datetime,
        "findingPublishingFrequency": FindingPublishingFrequencyType,
        "serviceRole": str,
        "status": MacieStatusType,
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMasterAccountResponseTypeDef = TypedDict(
    "GetMasterAccountResponseTypeDef",
    {
        "master": "InvitationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMemberRequestRequestTypeDef = TypedDict(
    "GetMemberRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetMemberResponseTypeDef = TypedDict(
    "GetMemberResponseTypeDef",
    {
        "accountId": str,
        "administratorAccountId": str,
        "arn": str,
        "email": str,
        "invitedAt": datetime,
        "masterAccountId": str,
        "relationshipStatus": RelationshipStatusType,
        "tags": Dict[str, str],
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUsageStatisticsRequestRequestTypeDef = TypedDict(
    "GetUsageStatisticsRequestRequestTypeDef",
    {
        "filterBy": NotRequired[Sequence["UsageStatisticsFilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired["UsageStatisticsSortByTypeDef"],
        "timeRange": NotRequired[TimeRangeType],
    },
)

GetUsageStatisticsResponseTypeDef = TypedDict(
    "GetUsageStatisticsResponseTypeDef",
    {
        "nextToken": str,
        "records": List["UsageRecordTypeDef"],
        "timeRange": TimeRangeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUsageTotalsRequestRequestTypeDef = TypedDict(
    "GetUsageTotalsRequestRequestTypeDef",
    {
        "timeRange": NotRequired[str],
    },
)

GetUsageTotalsResponseTypeDef = TypedDict(
    "GetUsageTotalsResponseTypeDef",
    {
        "timeRange": TimeRangeType,
        "usageTotals": List["UsageTotalTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupCountTypeDef = TypedDict(
    "GroupCountTypeDef",
    {
        "count": NotRequired[int],
        "groupKey": NotRequired[str],
    },
)

IamUserTypeDef = TypedDict(
    "IamUserTypeDef",
    {
        "accountId": NotRequired[str],
        "arn": NotRequired[str],
        "principalId": NotRequired[str],
        "userName": NotRequired[str],
    },
)

InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {
        "accountId": NotRequired[str],
        "invitationId": NotRequired[str],
        "invitedAt": NotRequired[datetime],
        "relationshipStatus": NotRequired[RelationshipStatusType],
    },
)

IpAddressDetailsTypeDef = TypedDict(
    "IpAddressDetailsTypeDef",
    {
        "ipAddressV4": NotRequired[str],
        "ipCity": NotRequired["IpCityTypeDef"],
        "ipCountry": NotRequired["IpCountryTypeDef"],
        "ipGeoLocation": NotRequired["IpGeoLocationTypeDef"],
        "ipOwner": NotRequired["IpOwnerTypeDef"],
    },
)

IpCityTypeDef = TypedDict(
    "IpCityTypeDef",
    {
        "name": NotRequired[str],
    },
)

IpCountryTypeDef = TypedDict(
    "IpCountryTypeDef",
    {
        "code": NotRequired[str],
        "name": NotRequired[str],
    },
)

IpGeoLocationTypeDef = TypedDict(
    "IpGeoLocationTypeDef",
    {
        "lat": NotRequired[float],
        "lon": NotRequired[float],
    },
)

IpOwnerTypeDef = TypedDict(
    "IpOwnerTypeDef",
    {
        "asn": NotRequired[str],
        "asnOrg": NotRequired[str],
        "isp": NotRequired[str],
        "org": NotRequired[str],
    },
)

JobDetailsTypeDef = TypedDict(
    "JobDetailsTypeDef",
    {
        "isDefinedInJob": NotRequired[IsDefinedInJobType],
        "isMonitoredByJob": NotRequired[IsMonitoredByJobType],
        "lastJobId": NotRequired[str],
        "lastJobRunTime": NotRequired[datetime],
    },
)

JobScheduleFrequencyTypeDef = TypedDict(
    "JobScheduleFrequencyTypeDef",
    {
        "dailySchedule": NotRequired[Mapping[str, Any]],
        "monthlySchedule": NotRequired["MonthlyScheduleTypeDef"],
        "weeklySchedule": NotRequired["WeeklyScheduleTypeDef"],
    },
)

JobScopeTermTypeDef = TypedDict(
    "JobScopeTermTypeDef",
    {
        "simpleScopeTerm": NotRequired["SimpleScopeTermTypeDef"],
        "tagScopeTerm": NotRequired["TagScopeTermTypeDef"],
    },
)

JobScopingBlockTypeDef = TypedDict(
    "JobScopingBlockTypeDef",
    {
        "and": NotRequired[Sequence["JobScopeTermTypeDef"]],
    },
)

JobSummaryTypeDef = TypedDict(
    "JobSummaryTypeDef",
    {
        "bucketDefinitions": NotRequired[List["S3BucketDefinitionForJobTypeDef"]],
        "createdAt": NotRequired[datetime],
        "jobId": NotRequired[str],
        "jobStatus": NotRequired[JobStatusType],
        "jobType": NotRequired[JobTypeType],
        "lastRunErrorStatus": NotRequired["LastRunErrorStatusTypeDef"],
        "name": NotRequired[str],
        "userPausedDetails": NotRequired["UserPausedDetailsTypeDef"],
        "bucketCriteria": NotRequired["S3BucketCriteriaForJobTypeDef"],
    },
)

KeyValuePairTypeDef = TypedDict(
    "KeyValuePairTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
    },
)

LastRunErrorStatusTypeDef = TypedDict(
    "LastRunErrorStatusTypeDef",
    {
        "code": NotRequired[LastRunErrorStatusCodeType],
    },
)

ListClassificationJobsRequestRequestTypeDef = TypedDict(
    "ListClassificationJobsRequestRequestTypeDef",
    {
        "filterCriteria": NotRequired["ListJobsFilterCriteriaTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortCriteria": NotRequired["ListJobsSortCriteriaTypeDef"],
    },
)

ListClassificationJobsResponseTypeDef = TypedDict(
    "ListClassificationJobsResponseTypeDef",
    {
        "items": List["JobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomDataIdentifiersRequestRequestTypeDef = TypedDict(
    "ListCustomDataIdentifiersRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListCustomDataIdentifiersResponseTypeDef = TypedDict(
    "ListCustomDataIdentifiersResponseTypeDef",
    {
        "items": List["CustomDataIdentifierSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFindingsFiltersRequestRequestTypeDef = TypedDict(
    "ListFindingsFiltersRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListFindingsFiltersResponseTypeDef = TypedDict(
    "ListFindingsFiltersResponseTypeDef",
    {
        "findingsFilterListItems": List["FindingsFilterListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFindingsRequestRequestTypeDef = TypedDict(
    "ListFindingsRequestRequestTypeDef",
    {
        "findingCriteria": NotRequired["FindingCriteriaTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortCriteria": NotRequired["SortCriteriaTypeDef"],
    },
)

ListFindingsResponseTypeDef = TypedDict(
    "ListFindingsResponseTypeDef",
    {
        "findingIds": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInvitationsRequestRequestTypeDef = TypedDict(
    "ListInvitationsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {
        "invitations": List["InvitationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobsFilterCriteriaTypeDef = TypedDict(
    "ListJobsFilterCriteriaTypeDef",
    {
        "excludes": NotRequired[Sequence["ListJobsFilterTermTypeDef"]],
        "includes": NotRequired[Sequence["ListJobsFilterTermTypeDef"]],
    },
)

ListJobsFilterTermTypeDef = TypedDict(
    "ListJobsFilterTermTypeDef",
    {
        "comparator": NotRequired[JobComparatorType],
        "key": NotRequired[ListJobsFilterKeyType],
        "values": NotRequired[Sequence[str]],
    },
)

ListJobsSortCriteriaTypeDef = TypedDict(
    "ListJobsSortCriteriaTypeDef",
    {
        "attributeName": NotRequired[ListJobsSortAttributeNameType],
        "orderBy": NotRequired[OrderByType],
    },
)

ListManagedDataIdentifiersRequestRequestTypeDef = TypedDict(
    "ListManagedDataIdentifiersRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)

ListManagedDataIdentifiersResponseTypeDef = TypedDict(
    "ListManagedDataIdentifiersResponseTypeDef",
    {
        "items": List["ManagedDataIdentifierSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMembersRequestRequestTypeDef = TypedDict(
    "ListMembersRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "onlyAssociated": NotRequired[str],
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

ListOrganizationAdminAccountsRequestRequestTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListOrganizationAdminAccountsResponseTypeDef = TypedDict(
    "ListOrganizationAdminAccountsResponseTypeDef",
    {
        "adminAccounts": List["AdminAccountTypeDef"],
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

ManagedDataIdentifierSummaryTypeDef = TypedDict(
    "ManagedDataIdentifierSummaryTypeDef",
    {
        "category": NotRequired[SensitiveDataItemCategoryType],
        "id": NotRequired[str],
    },
)

MatchingBucketTypeDef = TypedDict(
    "MatchingBucketTypeDef",
    {
        "accountId": NotRequired[str],
        "bucketName": NotRequired[str],
        "classifiableObjectCount": NotRequired[int],
        "classifiableSizeInBytes": NotRequired[int],
        "errorCode": NotRequired[Literal["ACCESS_DENIED"]],
        "errorMessage": NotRequired[str],
        "jobDetails": NotRequired["JobDetailsTypeDef"],
        "objectCount": NotRequired[int],
        "objectCountByEncryptionType": NotRequired["ObjectCountByEncryptionTypeTypeDef"],
        "sizeInBytes": NotRequired[int],
        "sizeInBytesCompressed": NotRequired[int],
        "unclassifiableObjectCount": NotRequired["ObjectLevelStatisticsTypeDef"],
        "unclassifiableObjectSizeInBytes": NotRequired["ObjectLevelStatisticsTypeDef"],
    },
)

MatchingResourceTypeDef = TypedDict(
    "MatchingResourceTypeDef",
    {
        "matchingBucket": NotRequired["MatchingBucketTypeDef"],
    },
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "accountId": NotRequired[str],
        "administratorAccountId": NotRequired[str],
        "arn": NotRequired[str],
        "email": NotRequired[str],
        "invitedAt": NotRequired[datetime],
        "masterAccountId": NotRequired[str],
        "relationshipStatus": NotRequired[RelationshipStatusType],
        "tags": NotRequired[Dict[str, str]],
        "updatedAt": NotRequired[datetime],
    },
)

MonthlyScheduleTypeDef = TypedDict(
    "MonthlyScheduleTypeDef",
    {
        "dayOfMonth": NotRequired[int],
    },
)

ObjectCountByEncryptionTypeTypeDef = TypedDict(
    "ObjectCountByEncryptionTypeTypeDef",
    {
        "customerManaged": NotRequired[int],
        "kmsManaged": NotRequired[int],
        "s3Managed": NotRequired[int],
        "unencrypted": NotRequired[int],
        "unknown": NotRequired[int],
    },
)

ObjectLevelStatisticsTypeDef = TypedDict(
    "ObjectLevelStatisticsTypeDef",
    {
        "fileType": NotRequired[int],
        "storageClass": NotRequired[int],
        "total": NotRequired[int],
    },
)

OccurrencesTypeDef = TypedDict(
    "OccurrencesTypeDef",
    {
        "cells": NotRequired[List["CellTypeDef"]],
        "lineRanges": NotRequired[List["RangeTypeDef"]],
        "offsetRanges": NotRequired[List["RangeTypeDef"]],
        "pages": NotRequired[List["PageTypeDef"]],
        "records": NotRequired[List["RecordTypeDef"]],
    },
)

PageTypeDef = TypedDict(
    "PageTypeDef",
    {
        "lineRange": NotRequired["RangeTypeDef"],
        "offsetRange": NotRequired["RangeTypeDef"],
        "pageNumber": NotRequired[int],
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

PolicyDetailsTypeDef = TypedDict(
    "PolicyDetailsTypeDef",
    {
        "action": NotRequired["FindingActionTypeDef"],
        "actor": NotRequired["FindingActorTypeDef"],
    },
)

PutClassificationExportConfigurationRequestRequestTypeDef = TypedDict(
    "PutClassificationExportConfigurationRequestRequestTypeDef",
    {
        "configuration": "ClassificationExportConfigurationTypeDef",
    },
)

PutClassificationExportConfigurationResponseTypeDef = TypedDict(
    "PutClassificationExportConfigurationResponseTypeDef",
    {
        "configuration": "ClassificationExportConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutFindingsPublicationConfigurationRequestRequestTypeDef = TypedDict(
    "PutFindingsPublicationConfigurationRequestRequestTypeDef",
    {
        "clientToken": NotRequired[str],
        "securityHubConfiguration": NotRequired["SecurityHubConfigurationTypeDef"],
    },
)

RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "end": NotRequired[int],
        "start": NotRequired[int],
        "startColumn": NotRequired[int],
    },
)

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "jsonPath": NotRequired[str],
        "recordIndex": NotRequired[int],
    },
)

ReplicationDetailsTypeDef = TypedDict(
    "ReplicationDetailsTypeDef",
    {
        "replicated": NotRequired[bool],
        "replicatedExternally": NotRequired[bool],
        "replicationAccounts": NotRequired[List[str]],
    },
)

ResourcesAffectedTypeDef = TypedDict(
    "ResourcesAffectedTypeDef",
    {
        "s3Bucket": NotRequired["S3BucketTypeDef"],
        "s3Object": NotRequired["S3ObjectTypeDef"],
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

S3BucketCriteriaForJobTypeDef = TypedDict(
    "S3BucketCriteriaForJobTypeDef",
    {
        "excludes": NotRequired["CriteriaBlockForJobTypeDef"],
        "includes": NotRequired["CriteriaBlockForJobTypeDef"],
    },
)

S3BucketDefinitionForJobTypeDef = TypedDict(
    "S3BucketDefinitionForJobTypeDef",
    {
        "accountId": str,
        "buckets": Sequence[str],
    },
)

S3BucketOwnerTypeDef = TypedDict(
    "S3BucketOwnerTypeDef",
    {
        "displayName": NotRequired[str],
        "id": NotRequired[str],
    },
)

S3BucketTypeDef = TypedDict(
    "S3BucketTypeDef",
    {
        "allowsUnencryptedObjectUploads": NotRequired[AllowsUnencryptedObjectUploadsType],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "defaultServerSideEncryption": NotRequired["ServerSideEncryptionTypeDef"],
        "name": NotRequired[str],
        "owner": NotRequired["S3BucketOwnerTypeDef"],
        "publicAccess": NotRequired["BucketPublicAccessTypeDef"],
        "tags": NotRequired[List["KeyValuePairTypeDef"]],
    },
)

S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "bucketName": str,
        "kmsKeyArn": str,
        "keyPrefix": NotRequired[str],
    },
)

S3JobDefinitionTypeDef = TypedDict(
    "S3JobDefinitionTypeDef",
    {
        "bucketDefinitions": NotRequired[Sequence["S3BucketDefinitionForJobTypeDef"]],
        "scoping": NotRequired["ScopingTypeDef"],
        "bucketCriteria": NotRequired["S3BucketCriteriaForJobTypeDef"],
    },
)

S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "bucketArn": NotRequired[str],
        "eTag": NotRequired[str],
        "extension": NotRequired[str],
        "key": NotRequired[str],
        "lastModified": NotRequired[datetime],
        "path": NotRequired[str],
        "publicAccess": NotRequired[bool],
        "serverSideEncryption": NotRequired["ServerSideEncryptionTypeDef"],
        "size": NotRequired[int],
        "storageClass": NotRequired[StorageClassType],
        "tags": NotRequired[List["KeyValuePairTypeDef"]],
        "versionId": NotRequired[str],
    },
)

ScopingTypeDef = TypedDict(
    "ScopingTypeDef",
    {
        "excludes": NotRequired["JobScopingBlockTypeDef"],
        "includes": NotRequired["JobScopingBlockTypeDef"],
    },
)

SearchResourcesBucketCriteriaTypeDef = TypedDict(
    "SearchResourcesBucketCriteriaTypeDef",
    {
        "excludes": NotRequired["SearchResourcesCriteriaBlockTypeDef"],
        "includes": NotRequired["SearchResourcesCriteriaBlockTypeDef"],
    },
)

SearchResourcesCriteriaBlockTypeDef = TypedDict(
    "SearchResourcesCriteriaBlockTypeDef",
    {
        "and": NotRequired[Sequence["SearchResourcesCriteriaTypeDef"]],
    },
)

SearchResourcesCriteriaTypeDef = TypedDict(
    "SearchResourcesCriteriaTypeDef",
    {
        "simpleCriterion": NotRequired["SearchResourcesSimpleCriterionTypeDef"],
        "tagCriterion": NotRequired["SearchResourcesTagCriterionTypeDef"],
    },
)

SearchResourcesRequestRequestTypeDef = TypedDict(
    "SearchResourcesRequestRequestTypeDef",
    {
        "bucketCriteria": NotRequired["SearchResourcesBucketCriteriaTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortCriteria": NotRequired["SearchResourcesSortCriteriaTypeDef"],
    },
)

SearchResourcesResponseTypeDef = TypedDict(
    "SearchResourcesResponseTypeDef",
    {
        "matchingResources": List["MatchingResourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchResourcesSimpleCriterionTypeDef = TypedDict(
    "SearchResourcesSimpleCriterionTypeDef",
    {
        "comparator": NotRequired[SearchResourcesComparatorType],
        "key": NotRequired[SearchResourcesSimpleCriterionKeyType],
        "values": NotRequired[Sequence[str]],
    },
)

SearchResourcesSortCriteriaTypeDef = TypedDict(
    "SearchResourcesSortCriteriaTypeDef",
    {
        "attributeName": NotRequired[SearchResourcesSortAttributeNameType],
        "orderBy": NotRequired[OrderByType],
    },
)

SearchResourcesTagCriterionPairTypeDef = TypedDict(
    "SearchResourcesTagCriterionPairTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
    },
)

SearchResourcesTagCriterionTypeDef = TypedDict(
    "SearchResourcesTagCriterionTypeDef",
    {
        "comparator": NotRequired[SearchResourcesComparatorType],
        "tagValues": NotRequired[Sequence["SearchResourcesTagCriterionPairTypeDef"]],
    },
)

SecurityHubConfigurationTypeDef = TypedDict(
    "SecurityHubConfigurationTypeDef",
    {
        "publishClassificationFindings": bool,
        "publishPolicyFindings": bool,
    },
)

SensitiveDataItemTypeDef = TypedDict(
    "SensitiveDataItemTypeDef",
    {
        "category": NotRequired[SensitiveDataItemCategoryType],
        "detections": NotRequired[List["DefaultDetectionTypeDef"]],
        "totalCount": NotRequired[int],
    },
)

ServerSideEncryptionTypeDef = TypedDict(
    "ServerSideEncryptionTypeDef",
    {
        "encryptionType": NotRequired[EncryptionTypeType],
        "kmsMasterKeyId": NotRequired[str],
    },
)

ServiceLimitTypeDef = TypedDict(
    "ServiceLimitTypeDef",
    {
        "isServiceLimited": NotRequired[bool],
        "unit": NotRequired[Literal["TERABYTES"]],
        "value": NotRequired[int],
    },
)

SessionContextAttributesTypeDef = TypedDict(
    "SessionContextAttributesTypeDef",
    {
        "creationDate": NotRequired[datetime],
        "mfaAuthenticated": NotRequired[bool],
    },
)

SessionContextTypeDef = TypedDict(
    "SessionContextTypeDef",
    {
        "attributes": NotRequired["SessionContextAttributesTypeDef"],
        "sessionIssuer": NotRequired["SessionIssuerTypeDef"],
    },
)

SessionIssuerTypeDef = TypedDict(
    "SessionIssuerTypeDef",
    {
        "accountId": NotRequired[str],
        "arn": NotRequired[str],
        "principalId": NotRequired[str],
        "type": NotRequired[str],
        "userName": NotRequired[str],
    },
)

SeverityLevelTypeDef = TypedDict(
    "SeverityLevelTypeDef",
    {
        "occurrencesThreshold": int,
        "severity": DataIdentifierSeverityType,
    },
)

SeverityTypeDef = TypedDict(
    "SeverityTypeDef",
    {
        "description": NotRequired[SeverityDescriptionType],
        "score": NotRequired[int],
    },
)

SimpleCriterionForJobTypeDef = TypedDict(
    "SimpleCriterionForJobTypeDef",
    {
        "comparator": NotRequired[JobComparatorType],
        "key": NotRequired[SimpleCriterionKeyForJobType],
        "values": NotRequired[Sequence[str]],
    },
)

SimpleScopeTermTypeDef = TypedDict(
    "SimpleScopeTermTypeDef",
    {
        "comparator": NotRequired[JobComparatorType],
        "key": NotRequired[ScopeFilterKeyType],
        "values": NotRequired[Sequence[str]],
    },
)

SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef",
    {
        "attributeName": NotRequired[str],
        "orderBy": NotRequired[OrderByType],
    },
)

StatisticsTypeDef = TypedDict(
    "StatisticsTypeDef",
    {
        "approximateNumberOfObjectsToProcess": NotRequired[float],
        "numberOfRuns": NotRequired[float],
    },
)

TagCriterionForJobTypeDef = TypedDict(
    "TagCriterionForJobTypeDef",
    {
        "comparator": NotRequired[JobComparatorType],
        "tagValues": NotRequired[Sequence["TagCriterionPairForJobTypeDef"]],
    },
)

TagCriterionPairForJobTypeDef = TypedDict(
    "TagCriterionPairForJobTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

TagScopeTermTypeDef = TypedDict(
    "TagScopeTermTypeDef",
    {
        "comparator": NotRequired[JobComparatorType],
        "key": NotRequired[str],
        "tagValues": NotRequired[Sequence["TagValuePairTypeDef"]],
        "target": NotRequired[Literal["S3_OBJECT"]],
    },
)

TagValuePairTypeDef = TypedDict(
    "TagValuePairTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
    },
)

TestCustomDataIdentifierRequestRequestTypeDef = TypedDict(
    "TestCustomDataIdentifierRequestRequestTypeDef",
    {
        "regex": str,
        "sampleText": str,
        "ignoreWords": NotRequired[Sequence[str]],
        "keywords": NotRequired[Sequence[str]],
        "maximumMatchDistance": NotRequired[int],
    },
)

TestCustomDataIdentifierResponseTypeDef = TypedDict(
    "TestCustomDataIdentifierResponseTypeDef",
    {
        "matchCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UnprocessedAccountTypeDef = TypedDict(
    "UnprocessedAccountTypeDef",
    {
        "accountId": NotRequired[str],
        "errorCode": NotRequired[ErrorCodeType],
        "errorMessage": NotRequired[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateClassificationJobRequestRequestTypeDef = TypedDict(
    "UpdateClassificationJobRequestRequestTypeDef",
    {
        "jobId": str,
        "jobStatus": JobStatusType,
    },
)

UpdateFindingsFilterRequestRequestTypeDef = TypedDict(
    "UpdateFindingsFilterRequestRequestTypeDef",
    {
        "id": str,
        "action": NotRequired[FindingsFilterActionType],
        "description": NotRequired[str],
        "findingCriteria": NotRequired["FindingCriteriaTypeDef"],
        "name": NotRequired[str],
        "position": NotRequired[int],
        "clientToken": NotRequired[str],
    },
)

UpdateFindingsFilterResponseTypeDef = TypedDict(
    "UpdateFindingsFilterResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMacieSessionRequestRequestTypeDef = TypedDict(
    "UpdateMacieSessionRequestRequestTypeDef",
    {
        "findingPublishingFrequency": NotRequired[FindingPublishingFrequencyType],
        "status": NotRequired[MacieStatusType],
    },
)

UpdateMemberSessionRequestRequestTypeDef = TypedDict(
    "UpdateMemberSessionRequestRequestTypeDef",
    {
        "id": str,
        "status": MacieStatusType,
    },
)

UpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "autoEnable": bool,
    },
)

UsageByAccountTypeDef = TypedDict(
    "UsageByAccountTypeDef",
    {
        "currency": NotRequired[Literal["USD"]],
        "estimatedCost": NotRequired[str],
        "serviceLimit": NotRequired["ServiceLimitTypeDef"],
        "type": NotRequired[UsageTypeType],
    },
)

UsageRecordTypeDef = TypedDict(
    "UsageRecordTypeDef",
    {
        "accountId": NotRequired[str],
        "freeTrialStartDate": NotRequired[datetime],
        "usage": NotRequired[List["UsageByAccountTypeDef"]],
    },
)

UsageStatisticsFilterTypeDef = TypedDict(
    "UsageStatisticsFilterTypeDef",
    {
        "comparator": NotRequired[UsageStatisticsFilterComparatorType],
        "key": NotRequired[UsageStatisticsFilterKeyType],
        "values": NotRequired[Sequence[str]],
    },
)

UsageStatisticsSortByTypeDef = TypedDict(
    "UsageStatisticsSortByTypeDef",
    {
        "key": NotRequired[UsageStatisticsSortKeyType],
        "orderBy": NotRequired[OrderByType],
    },
)

UsageTotalTypeDef = TypedDict(
    "UsageTotalTypeDef",
    {
        "currency": NotRequired[Literal["USD"]],
        "estimatedCost": NotRequired[str],
        "type": NotRequired[UsageTypeType],
    },
)

UserIdentityRootTypeDef = TypedDict(
    "UserIdentityRootTypeDef",
    {
        "accountId": NotRequired[str],
        "arn": NotRequired[str],
        "principalId": NotRequired[str],
    },
)

UserIdentityTypeDef = TypedDict(
    "UserIdentityTypeDef",
    {
        "assumedRole": NotRequired["AssumedRoleTypeDef"],
        "awsAccount": NotRequired["AwsAccountTypeDef"],
        "awsService": NotRequired["AwsServiceTypeDef"],
        "federatedUser": NotRequired["FederatedUserTypeDef"],
        "iamUser": NotRequired["IamUserTypeDef"],
        "root": NotRequired["UserIdentityRootTypeDef"],
        "type": NotRequired[UserIdentityTypeType],
    },
)

UserPausedDetailsTypeDef = TypedDict(
    "UserPausedDetailsTypeDef",
    {
        "jobExpiresAt": NotRequired[datetime],
        "jobImminentExpirationHealthEventArn": NotRequired[str],
        "jobPausedAt": NotRequired[datetime],
    },
)

WeeklyScheduleTypeDef = TypedDict(
    "WeeklyScheduleTypeDef",
    {
        "dayOfWeek": NotRequired[DayOfWeekType],
    },
)
