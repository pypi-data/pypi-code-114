"""
Type annotations for guardduty service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/type_defs.html)

Usage::

    ```python
    from mypy_boto3_guardduty.type_defs import AcceptInvitationRequestRequestTypeDef

    data: AcceptInvitationRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AdminStatusType,
    DataSourceStatusType,
    DataSourceType,
    DetectorStatusType,
    FeedbackType,
    FilterActionType,
    FindingPublishingFrequencyType,
    IpSetFormatType,
    IpSetStatusType,
    OrderByType,
    PublishingStatusType,
    ThreatIntelSetFormatType,
    ThreatIntelSetStatusType,
    UsageStatisticTypeType,
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
    "AccessKeyDetailsTypeDef",
    "AccountDetailTypeDef",
    "AccountLevelPermissionsTypeDef",
    "ActionTypeDef",
    "AdminAccountTypeDef",
    "ArchiveFindingsRequestRequestTypeDef",
    "AwsApiCallActionTypeDef",
    "BlockPublicAccessTypeDef",
    "BucketLevelPermissionsTypeDef",
    "BucketPolicyTypeDef",
    "CityTypeDef",
    "CloudTrailConfigurationResultTypeDef",
    "ConditionTypeDef",
    "ContainerTypeDef",
    "CountryTypeDef",
    "CreateDetectorRequestRequestTypeDef",
    "CreateDetectorResponseTypeDef",
    "CreateFilterRequestRequestTypeDef",
    "CreateFilterResponseTypeDef",
    "CreateIPSetRequestRequestTypeDef",
    "CreateIPSetResponseTypeDef",
    "CreateMembersRequestRequestTypeDef",
    "CreateMembersResponseTypeDef",
    "CreatePublishingDestinationRequestRequestTypeDef",
    "CreatePublishingDestinationResponseTypeDef",
    "CreateSampleFindingsRequestRequestTypeDef",
    "CreateThreatIntelSetRequestRequestTypeDef",
    "CreateThreatIntelSetResponseTypeDef",
    "DNSLogsConfigurationResultTypeDef",
    "DataSourceConfigurationsResultTypeDef",
    "DataSourceConfigurationsTypeDef",
    "DeclineInvitationsRequestRequestTypeDef",
    "DeclineInvitationsResponseTypeDef",
    "DefaultServerSideEncryptionTypeDef",
    "DeleteDetectorRequestRequestTypeDef",
    "DeleteFilterRequestRequestTypeDef",
    "DeleteIPSetRequestRequestTypeDef",
    "DeleteInvitationsRequestRequestTypeDef",
    "DeleteInvitationsResponseTypeDef",
    "DeleteMembersRequestRequestTypeDef",
    "DeleteMembersResponseTypeDef",
    "DeletePublishingDestinationRequestRequestTypeDef",
    "DeleteThreatIntelSetRequestRequestTypeDef",
    "DescribeOrganizationConfigurationRequestRequestTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "DescribePublishingDestinationRequestRequestTypeDef",
    "DescribePublishingDestinationResponseTypeDef",
    "DestinationPropertiesTypeDef",
    "DestinationTypeDef",
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    "DisassociateFromMasterAccountRequestRequestTypeDef",
    "DisassociateMembersRequestRequestTypeDef",
    "DisassociateMembersResponseTypeDef",
    "DnsRequestActionTypeDef",
    "DomainDetailsTypeDef",
    "EksClusterDetailsTypeDef",
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    "EvidenceTypeDef",
    "FindingCriteriaTypeDef",
    "FindingStatisticsTypeDef",
    "FindingTypeDef",
    "FlowLogsConfigurationResultTypeDef",
    "GeoLocationTypeDef",
    "GetDetectorRequestRequestTypeDef",
    "GetDetectorResponseTypeDef",
    "GetFilterRequestRequestTypeDef",
    "GetFilterResponseTypeDef",
    "GetFindingsRequestRequestTypeDef",
    "GetFindingsResponseTypeDef",
    "GetFindingsStatisticsRequestRequestTypeDef",
    "GetFindingsStatisticsResponseTypeDef",
    "GetIPSetRequestRequestTypeDef",
    "GetIPSetResponseTypeDef",
    "GetInvitationsCountResponseTypeDef",
    "GetMasterAccountRequestRequestTypeDef",
    "GetMasterAccountResponseTypeDef",
    "GetMemberDetectorsRequestRequestTypeDef",
    "GetMemberDetectorsResponseTypeDef",
    "GetMembersRequestRequestTypeDef",
    "GetMembersResponseTypeDef",
    "GetThreatIntelSetRequestRequestTypeDef",
    "GetThreatIntelSetResponseTypeDef",
    "GetUsageStatisticsRequestRequestTypeDef",
    "GetUsageStatisticsResponseTypeDef",
    "HostPathTypeDef",
    "IamInstanceProfileTypeDef",
    "InstanceDetailsTypeDef",
    "InvitationTypeDef",
    "InviteMembersRequestRequestTypeDef",
    "InviteMembersResponseTypeDef",
    "KubernetesApiCallActionTypeDef",
    "KubernetesAuditLogsConfigurationResultTypeDef",
    "KubernetesAuditLogsConfigurationTypeDef",
    "KubernetesConfigurationResultTypeDef",
    "KubernetesConfigurationTypeDef",
    "KubernetesDetailsTypeDef",
    "KubernetesUserDetailsTypeDef",
    "KubernetesWorkloadDetailsTypeDef",
    "ListDetectorsRequestRequestTypeDef",
    "ListDetectorsResponseTypeDef",
    "ListFiltersRequestRequestTypeDef",
    "ListFiltersResponseTypeDef",
    "ListFindingsRequestRequestTypeDef",
    "ListFindingsResponseTypeDef",
    "ListIPSetsRequestRequestTypeDef",
    "ListIPSetsResponseTypeDef",
    "ListInvitationsRequestRequestTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListMembersRequestRequestTypeDef",
    "ListMembersResponseTypeDef",
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListPublishingDestinationsRequestRequestTypeDef",
    "ListPublishingDestinationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListThreatIntelSetsRequestRequestTypeDef",
    "ListThreatIntelSetsResponseTypeDef",
    "LocalIpDetailsTypeDef",
    "LocalPortDetailsTypeDef",
    "MasterTypeDef",
    "MemberDataSourceConfigurationTypeDef",
    "MemberTypeDef",
    "NetworkConnectionActionTypeDef",
    "NetworkInterfaceTypeDef",
    "OrganizationDataSourceConfigurationsResultTypeDef",
    "OrganizationDataSourceConfigurationsTypeDef",
    "OrganizationKubernetesAuditLogsConfigurationResultTypeDef",
    "OrganizationKubernetesAuditLogsConfigurationTypeDef",
    "OrganizationKubernetesConfigurationResultTypeDef",
    "OrganizationKubernetesConfigurationTypeDef",
    "OrganizationS3LogsConfigurationResultTypeDef",
    "OrganizationS3LogsConfigurationTypeDef",
    "OrganizationTypeDef",
    "OwnerTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionConfigurationTypeDef",
    "PortProbeActionTypeDef",
    "PortProbeDetailTypeDef",
    "PrivateIpAddressDetailsTypeDef",
    "ProductCodeTypeDef",
    "PublicAccessTypeDef",
    "RemoteAccountDetailsTypeDef",
    "RemoteIpDetailsTypeDef",
    "RemotePortDetailsTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "S3BucketDetailTypeDef",
    "S3LogsConfigurationResultTypeDef",
    "S3LogsConfigurationTypeDef",
    "SecurityContextTypeDef",
    "SecurityGroupTypeDef",
    "ServiceTypeDef",
    "SortCriteriaTypeDef",
    "StartMonitoringMembersRequestRequestTypeDef",
    "StartMonitoringMembersResponseTypeDef",
    "StopMonitoringMembersRequestRequestTypeDef",
    "StopMonitoringMembersResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "ThreatIntelligenceDetailTypeDef",
    "TotalTypeDef",
    "UnarchiveFindingsRequestRequestTypeDef",
    "UnprocessedAccountTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDetectorRequestRequestTypeDef",
    "UpdateFilterRequestRequestTypeDef",
    "UpdateFilterResponseTypeDef",
    "UpdateFindingsFeedbackRequestRequestTypeDef",
    "UpdateIPSetRequestRequestTypeDef",
    "UpdateMemberDetectorsRequestRequestTypeDef",
    "UpdateMemberDetectorsResponseTypeDef",
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    "UpdatePublishingDestinationRequestRequestTypeDef",
    "UpdateThreatIntelSetRequestRequestTypeDef",
    "UsageAccountResultTypeDef",
    "UsageCriteriaTypeDef",
    "UsageDataSourceResultTypeDef",
    "UsageResourceResultTypeDef",
    "UsageStatisticsTypeDef",
    "VolumeMountTypeDef",
    "VolumeTypeDef",
)

AcceptInvitationRequestRequestTypeDef = TypedDict(
    "AcceptInvitationRequestRequestTypeDef",
    {
        "DetectorId": str,
        "MasterId": str,
        "InvitationId": str,
    },
)

AccessControlListTypeDef = TypedDict(
    "AccessControlListTypeDef",
    {
        "AllowsPublicReadAccess": NotRequired[bool],
        "AllowsPublicWriteAccess": NotRequired[bool],
    },
)

AccessKeyDetailsTypeDef = TypedDict(
    "AccessKeyDetailsTypeDef",
    {
        "AccessKeyId": NotRequired[str],
        "PrincipalId": NotRequired[str],
        "UserName": NotRequired[str],
        "UserType": NotRequired[str],
    },
)

AccountDetailTypeDef = TypedDict(
    "AccountDetailTypeDef",
    {
        "AccountId": str,
        "Email": str,
    },
)

AccountLevelPermissionsTypeDef = TypedDict(
    "AccountLevelPermissionsTypeDef",
    {
        "BlockPublicAccess": NotRequired["BlockPublicAccessTypeDef"],
    },
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ActionType": NotRequired[str],
        "AwsApiCallAction": NotRequired["AwsApiCallActionTypeDef"],
        "DnsRequestAction": NotRequired["DnsRequestActionTypeDef"],
        "NetworkConnectionAction": NotRequired["NetworkConnectionActionTypeDef"],
        "PortProbeAction": NotRequired["PortProbeActionTypeDef"],
        "KubernetesApiCallAction": NotRequired["KubernetesApiCallActionTypeDef"],
    },
)

AdminAccountTypeDef = TypedDict(
    "AdminAccountTypeDef",
    {
        "AdminAccountId": NotRequired[str],
        "AdminStatus": NotRequired[AdminStatusType],
    },
)

ArchiveFindingsRequestRequestTypeDef = TypedDict(
    "ArchiveFindingsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FindingIds": Sequence[str],
    },
)

AwsApiCallActionTypeDef = TypedDict(
    "AwsApiCallActionTypeDef",
    {
        "Api": NotRequired[str],
        "CallerType": NotRequired[str],
        "DomainDetails": NotRequired["DomainDetailsTypeDef"],
        "ErrorCode": NotRequired[str],
        "UserAgent": NotRequired[str],
        "RemoteIpDetails": NotRequired["RemoteIpDetailsTypeDef"],
        "ServiceName": NotRequired[str],
        "RemoteAccountDetails": NotRequired["RemoteAccountDetailsTypeDef"],
    },
)

BlockPublicAccessTypeDef = TypedDict(
    "BlockPublicAccessTypeDef",
    {
        "IgnorePublicAcls": NotRequired[bool],
        "RestrictPublicBuckets": NotRequired[bool],
        "BlockPublicAcls": NotRequired[bool],
        "BlockPublicPolicy": NotRequired[bool],
    },
)

BucketLevelPermissionsTypeDef = TypedDict(
    "BucketLevelPermissionsTypeDef",
    {
        "AccessControlList": NotRequired["AccessControlListTypeDef"],
        "BucketPolicy": NotRequired["BucketPolicyTypeDef"],
        "BlockPublicAccess": NotRequired["BlockPublicAccessTypeDef"],
    },
)

BucketPolicyTypeDef = TypedDict(
    "BucketPolicyTypeDef",
    {
        "AllowsPublicReadAccess": NotRequired[bool],
        "AllowsPublicWriteAccess": NotRequired[bool],
    },
)

CityTypeDef = TypedDict(
    "CityTypeDef",
    {
        "CityName": NotRequired[str],
    },
)

CloudTrailConfigurationResultTypeDef = TypedDict(
    "CloudTrailConfigurationResultTypeDef",
    {
        "Status": DataSourceStatusType,
    },
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "Eq": NotRequired[Sequence[str]],
        "Neq": NotRequired[Sequence[str]],
        "Gt": NotRequired[int],
        "Gte": NotRequired[int],
        "Lt": NotRequired[int],
        "Lte": NotRequired[int],
        "Equals": NotRequired[Sequence[str]],
        "NotEquals": NotRequired[Sequence[str]],
        "GreaterThan": NotRequired[int],
        "GreaterThanOrEqual": NotRequired[int],
        "LessThan": NotRequired[int],
        "LessThanOrEqual": NotRequired[int],
    },
)

ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "ContainerRuntime": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Image": NotRequired[str],
        "ImagePrefix": NotRequired[str],
        "VolumeMounts": NotRequired[List["VolumeMountTypeDef"]],
        "SecurityContext": NotRequired["SecurityContextTypeDef"],
    },
)

CountryTypeDef = TypedDict(
    "CountryTypeDef",
    {
        "CountryCode": NotRequired[str],
        "CountryName": NotRequired[str],
    },
)

CreateDetectorRequestRequestTypeDef = TypedDict(
    "CreateDetectorRequestRequestTypeDef",
    {
        "Enable": bool,
        "ClientToken": NotRequired[str],
        "FindingPublishingFrequency": NotRequired[FindingPublishingFrequencyType],
        "DataSources": NotRequired["DataSourceConfigurationsTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateDetectorResponseTypeDef = TypedDict(
    "CreateDetectorResponseTypeDef",
    {
        "DetectorId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFilterRequestRequestTypeDef = TypedDict(
    "CreateFilterRequestRequestTypeDef",
    {
        "DetectorId": str,
        "Name": str,
        "FindingCriteria": "FindingCriteriaTypeDef",
        "Description": NotRequired[str],
        "Action": NotRequired[FilterActionType],
        "Rank": NotRequired[int],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateFilterResponseTypeDef = TypedDict(
    "CreateFilterResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIPSetRequestRequestTypeDef = TypedDict(
    "CreateIPSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "Name": str,
        "Format": IpSetFormatType,
        "Location": str,
        "Activate": bool,
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateIPSetResponseTypeDef = TypedDict(
    "CreateIPSetResponseTypeDef",
    {
        "IpSetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMembersRequestRequestTypeDef = TypedDict(
    "CreateMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountDetails": Sequence["AccountDetailTypeDef"],
    },
)

CreateMembersResponseTypeDef = TypedDict(
    "CreateMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePublishingDestinationRequestRequestTypeDef = TypedDict(
    "CreatePublishingDestinationRequestRequestTypeDef",
    {
        "DetectorId": str,
        "DestinationType": Literal["S3"],
        "DestinationProperties": "DestinationPropertiesTypeDef",
        "ClientToken": NotRequired[str],
    },
)

CreatePublishingDestinationResponseTypeDef = TypedDict(
    "CreatePublishingDestinationResponseTypeDef",
    {
        "DestinationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSampleFindingsRequestRequestTypeDef = TypedDict(
    "CreateSampleFindingsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FindingTypes": NotRequired[Sequence[str]],
    },
)

CreateThreatIntelSetRequestRequestTypeDef = TypedDict(
    "CreateThreatIntelSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "Name": str,
        "Format": ThreatIntelSetFormatType,
        "Location": str,
        "Activate": bool,
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateThreatIntelSetResponseTypeDef = TypedDict(
    "CreateThreatIntelSetResponseTypeDef",
    {
        "ThreatIntelSetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DNSLogsConfigurationResultTypeDef = TypedDict(
    "DNSLogsConfigurationResultTypeDef",
    {
        "Status": DataSourceStatusType,
    },
)

DataSourceConfigurationsResultTypeDef = TypedDict(
    "DataSourceConfigurationsResultTypeDef",
    {
        "CloudTrail": "CloudTrailConfigurationResultTypeDef",
        "DNSLogs": "DNSLogsConfigurationResultTypeDef",
        "FlowLogs": "FlowLogsConfigurationResultTypeDef",
        "S3Logs": "S3LogsConfigurationResultTypeDef",
        "Kubernetes": NotRequired["KubernetesConfigurationResultTypeDef"],
    },
)

DataSourceConfigurationsTypeDef = TypedDict(
    "DataSourceConfigurationsTypeDef",
    {
        "S3Logs": NotRequired["S3LogsConfigurationTypeDef"],
        "Kubernetes": NotRequired["KubernetesConfigurationTypeDef"],
    },
)

DeclineInvitationsRequestRequestTypeDef = TypedDict(
    "DeclineInvitationsRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)

DeclineInvitationsResponseTypeDef = TypedDict(
    "DeclineInvitationsResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefaultServerSideEncryptionTypeDef = TypedDict(
    "DefaultServerSideEncryptionTypeDef",
    {
        "EncryptionType": NotRequired[str],
        "KmsMasterKeyArn": NotRequired[str],
    },
)

DeleteDetectorRequestRequestTypeDef = TypedDict(
    "DeleteDetectorRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)

DeleteFilterRequestRequestTypeDef = TypedDict(
    "DeleteFilterRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FilterName": str,
    },
)

DeleteIPSetRequestRequestTypeDef = TypedDict(
    "DeleteIPSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "IpSetId": str,
    },
)

DeleteInvitationsRequestRequestTypeDef = TypedDict(
    "DeleteInvitationsRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)

DeleteInvitationsResponseTypeDef = TypedDict(
    "DeleteInvitationsResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMembersRequestRequestTypeDef = TypedDict(
    "DeleteMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": Sequence[str],
    },
)

DeleteMembersResponseTypeDef = TypedDict(
    "DeleteMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePublishingDestinationRequestRequestTypeDef = TypedDict(
    "DeletePublishingDestinationRequestRequestTypeDef",
    {
        "DetectorId": str,
        "DestinationId": str,
    },
)

DeleteThreatIntelSetRequestRequestTypeDef = TypedDict(
    "DeleteThreatIntelSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "ThreatIntelSetId": str,
    },
)

DescribeOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConfigurationRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)

DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {
        "AutoEnable": bool,
        "MemberAccountLimitReached": bool,
        "DataSources": "OrganizationDataSourceConfigurationsResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePublishingDestinationRequestRequestTypeDef = TypedDict(
    "DescribePublishingDestinationRequestRequestTypeDef",
    {
        "DetectorId": str,
        "DestinationId": str,
    },
)

DescribePublishingDestinationResponseTypeDef = TypedDict(
    "DescribePublishingDestinationResponseTypeDef",
    {
        "DestinationId": str,
        "DestinationType": Literal["S3"],
        "Status": PublishingStatusType,
        "PublishingFailureStartTimestamp": int,
        "DestinationProperties": "DestinationPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationPropertiesTypeDef = TypedDict(
    "DestinationPropertiesTypeDef",
    {
        "DestinationArn": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
    },
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "DestinationId": str,
        "DestinationType": Literal["S3"],
        "Status": PublishingStatusType,
    },
)

DisableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "AdminAccountId": str,
    },
)

DisassociateFromMasterAccountRequestRequestTypeDef = TypedDict(
    "DisassociateFromMasterAccountRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)

DisassociateMembersRequestRequestTypeDef = TypedDict(
    "DisassociateMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": Sequence[str],
    },
)

DisassociateMembersResponseTypeDef = TypedDict(
    "DisassociateMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DnsRequestActionTypeDef = TypedDict(
    "DnsRequestActionTypeDef",
    {
        "Domain": NotRequired[str],
    },
)

DomainDetailsTypeDef = TypedDict(
    "DomainDetailsTypeDef",
    {
        "Domain": NotRequired[str],
    },
)

EksClusterDetailsTypeDef = TypedDict(
    "EksClusterDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "VpcId": NotRequired[str],
        "Status": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "CreatedAt": NotRequired[datetime],
    },
)

EnableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "AdminAccountId": str,
    },
)

EvidenceTypeDef = TypedDict(
    "EvidenceTypeDef",
    {
        "ThreatIntelligenceDetails": NotRequired[List["ThreatIntelligenceDetailTypeDef"]],
    },
)

FindingCriteriaTypeDef = TypedDict(
    "FindingCriteriaTypeDef",
    {
        "Criterion": NotRequired[Mapping[str, "ConditionTypeDef"]],
    },
)

FindingStatisticsTypeDef = TypedDict(
    "FindingStatisticsTypeDef",
    {
        "CountBySeverity": NotRequired[Dict[str, int]],
    },
)

FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "AccountId": str,
        "Arn": str,
        "CreatedAt": str,
        "Id": str,
        "Region": str,
        "Resource": "ResourceTypeDef",
        "SchemaVersion": str,
        "Severity": float,
        "Type": str,
        "UpdatedAt": str,
        "Confidence": NotRequired[float],
        "Description": NotRequired[str],
        "Partition": NotRequired[str],
        "Service": NotRequired["ServiceTypeDef"],
        "Title": NotRequired[str],
    },
)

FlowLogsConfigurationResultTypeDef = TypedDict(
    "FlowLogsConfigurationResultTypeDef",
    {
        "Status": DataSourceStatusType,
    },
)

GeoLocationTypeDef = TypedDict(
    "GeoLocationTypeDef",
    {
        "Lat": NotRequired[float],
        "Lon": NotRequired[float],
    },
)

GetDetectorRequestRequestTypeDef = TypedDict(
    "GetDetectorRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)

GetDetectorResponseTypeDef = TypedDict(
    "GetDetectorResponseTypeDef",
    {
        "CreatedAt": str,
        "FindingPublishingFrequency": FindingPublishingFrequencyType,
        "ServiceRole": str,
        "Status": DetectorStatusType,
        "UpdatedAt": str,
        "DataSources": "DataSourceConfigurationsResultTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFilterRequestRequestTypeDef = TypedDict(
    "GetFilterRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FilterName": str,
    },
)

GetFilterResponseTypeDef = TypedDict(
    "GetFilterResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "Action": FilterActionType,
        "Rank": int,
        "FindingCriteria": "FindingCriteriaTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFindingsRequestRequestTypeDef = TypedDict(
    "GetFindingsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FindingIds": Sequence[str],
        "SortCriteria": NotRequired["SortCriteriaTypeDef"],
    },
)

GetFindingsResponseTypeDef = TypedDict(
    "GetFindingsResponseTypeDef",
    {
        "Findings": List["FindingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFindingsStatisticsRequestRequestTypeDef = TypedDict(
    "GetFindingsStatisticsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FindingStatisticTypes": Sequence[Literal["COUNT_BY_SEVERITY"]],
        "FindingCriteria": NotRequired["FindingCriteriaTypeDef"],
    },
)

GetFindingsStatisticsResponseTypeDef = TypedDict(
    "GetFindingsStatisticsResponseTypeDef",
    {
        "FindingStatistics": "FindingStatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIPSetRequestRequestTypeDef = TypedDict(
    "GetIPSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "IpSetId": str,
    },
)

GetIPSetResponseTypeDef = TypedDict(
    "GetIPSetResponseTypeDef",
    {
        "Name": str,
        "Format": IpSetFormatType,
        "Location": str,
        "Status": IpSetStatusType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInvitationsCountResponseTypeDef = TypedDict(
    "GetInvitationsCountResponseTypeDef",
    {
        "InvitationsCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMasterAccountRequestRequestTypeDef = TypedDict(
    "GetMasterAccountRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)

GetMasterAccountResponseTypeDef = TypedDict(
    "GetMasterAccountResponseTypeDef",
    {
        "Master": "MasterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMemberDetectorsRequestRequestTypeDef = TypedDict(
    "GetMemberDetectorsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": Sequence[str],
    },
)

GetMemberDetectorsResponseTypeDef = TypedDict(
    "GetMemberDetectorsResponseTypeDef",
    {
        "MemberDataSourceConfigurations": List["MemberDataSourceConfigurationTypeDef"],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMembersRequestRequestTypeDef = TypedDict(
    "GetMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": Sequence[str],
    },
)

GetMembersResponseTypeDef = TypedDict(
    "GetMembersResponseTypeDef",
    {
        "Members": List["MemberTypeDef"],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetThreatIntelSetRequestRequestTypeDef = TypedDict(
    "GetThreatIntelSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "ThreatIntelSetId": str,
    },
)

GetThreatIntelSetResponseTypeDef = TypedDict(
    "GetThreatIntelSetResponseTypeDef",
    {
        "Name": str,
        "Format": ThreatIntelSetFormatType,
        "Location": str,
        "Status": ThreatIntelSetStatusType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUsageStatisticsRequestRequestTypeDef = TypedDict(
    "GetUsageStatisticsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "UsageStatisticType": UsageStatisticTypeType,
        "UsageCriteria": "UsageCriteriaTypeDef",
        "Unit": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetUsageStatisticsResponseTypeDef = TypedDict(
    "GetUsageStatisticsResponseTypeDef",
    {
        "UsageStatistics": "UsageStatisticsTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HostPathTypeDef = TypedDict(
    "HostPathTypeDef",
    {
        "Path": NotRequired[str],
    },
)

IamInstanceProfileTypeDef = TypedDict(
    "IamInstanceProfileTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
    },
)

InstanceDetailsTypeDef = TypedDict(
    "InstanceDetailsTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "IamInstanceProfile": NotRequired["IamInstanceProfileTypeDef"],
        "ImageDescription": NotRequired[str],
        "ImageId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "InstanceState": NotRequired[str],
        "InstanceType": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "LaunchTime": NotRequired[str],
        "NetworkInterfaces": NotRequired[List["NetworkInterfaceTypeDef"]],
        "Platform": NotRequired[str],
        "ProductCodes": NotRequired[List["ProductCodeTypeDef"]],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {
        "AccountId": NotRequired[str],
        "InvitationId": NotRequired[str],
        "RelationshipStatus": NotRequired[str],
        "InvitedAt": NotRequired[str],
    },
)

InviteMembersRequestRequestTypeDef = TypedDict(
    "InviteMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": Sequence[str],
        "DisableEmailNotification": NotRequired[bool],
        "Message": NotRequired[str],
    },
)

InviteMembersResponseTypeDef = TypedDict(
    "InviteMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KubernetesApiCallActionTypeDef = TypedDict(
    "KubernetesApiCallActionTypeDef",
    {
        "RequestUri": NotRequired[str],
        "Verb": NotRequired[str],
        "SourceIps": NotRequired[List[str]],
        "UserAgent": NotRequired[str],
        "RemoteIpDetails": NotRequired["RemoteIpDetailsTypeDef"],
        "StatusCode": NotRequired[int],
        "Parameters": NotRequired[str],
    },
)

KubernetesAuditLogsConfigurationResultTypeDef = TypedDict(
    "KubernetesAuditLogsConfigurationResultTypeDef",
    {
        "Status": DataSourceStatusType,
    },
)

KubernetesAuditLogsConfigurationTypeDef = TypedDict(
    "KubernetesAuditLogsConfigurationTypeDef",
    {
        "Enable": bool,
    },
)

KubernetesConfigurationResultTypeDef = TypedDict(
    "KubernetesConfigurationResultTypeDef",
    {
        "AuditLogs": "KubernetesAuditLogsConfigurationResultTypeDef",
    },
)

KubernetesConfigurationTypeDef = TypedDict(
    "KubernetesConfigurationTypeDef",
    {
        "AuditLogs": "KubernetesAuditLogsConfigurationTypeDef",
    },
)

KubernetesDetailsTypeDef = TypedDict(
    "KubernetesDetailsTypeDef",
    {
        "KubernetesUserDetails": NotRequired["KubernetesUserDetailsTypeDef"],
        "KubernetesWorkloadDetails": NotRequired["KubernetesWorkloadDetailsTypeDef"],
    },
)

KubernetesUserDetailsTypeDef = TypedDict(
    "KubernetesUserDetailsTypeDef",
    {
        "Username": NotRequired[str],
        "Uid": NotRequired[str],
        "Groups": NotRequired[List[str]],
    },
)

KubernetesWorkloadDetailsTypeDef = TypedDict(
    "KubernetesWorkloadDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "Uid": NotRequired[str],
        "Namespace": NotRequired[str],
        "HostNetwork": NotRequired[bool],
        "Containers": NotRequired[List["ContainerTypeDef"]],
        "Volumes": NotRequired[List["VolumeTypeDef"]],
    },
)

ListDetectorsRequestRequestTypeDef = TypedDict(
    "ListDetectorsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListDetectorsResponseTypeDef = TypedDict(
    "ListDetectorsResponseTypeDef",
    {
        "DetectorIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFiltersRequestRequestTypeDef = TypedDict(
    "ListFiltersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListFiltersResponseTypeDef = TypedDict(
    "ListFiltersResponseTypeDef",
    {
        "FilterNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFindingsRequestRequestTypeDef = TypedDict(
    "ListFindingsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FindingCriteria": NotRequired["FindingCriteriaTypeDef"],
        "SortCriteria": NotRequired["SortCriteriaTypeDef"],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListFindingsResponseTypeDef = TypedDict(
    "ListFindingsResponseTypeDef",
    {
        "FindingIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIPSetsRequestRequestTypeDef = TypedDict(
    "ListIPSetsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListIPSetsResponseTypeDef = TypedDict(
    "ListIPSetsResponseTypeDef",
    {
        "IpSetIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInvitationsRequestRequestTypeDef = TypedDict(
    "ListInvitationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {
        "Invitations": List["InvitationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMembersRequestRequestTypeDef = TypedDict(
    "ListMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "OnlyAssociated": NotRequired[str],
    },
)

ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef",
    {
        "Members": List["MemberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOrganizationAdminAccountsRequestRequestTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListOrganizationAdminAccountsResponseTypeDef = TypedDict(
    "ListOrganizationAdminAccountsResponseTypeDef",
    {
        "AdminAccounts": List["AdminAccountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPublishingDestinationsRequestRequestTypeDef = TypedDict(
    "ListPublishingDestinationsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListPublishingDestinationsResponseTypeDef = TypedDict(
    "ListPublishingDestinationsResponseTypeDef",
    {
        "Destinations": List["DestinationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListThreatIntelSetsRequestRequestTypeDef = TypedDict(
    "ListThreatIntelSetsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListThreatIntelSetsResponseTypeDef = TypedDict(
    "ListThreatIntelSetsResponseTypeDef",
    {
        "ThreatIntelSetIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocalIpDetailsTypeDef = TypedDict(
    "LocalIpDetailsTypeDef",
    {
        "IpAddressV4": NotRequired[str],
    },
)

LocalPortDetailsTypeDef = TypedDict(
    "LocalPortDetailsTypeDef",
    {
        "Port": NotRequired[int],
        "PortName": NotRequired[str],
    },
)

MasterTypeDef = TypedDict(
    "MasterTypeDef",
    {
        "AccountId": NotRequired[str],
        "InvitationId": NotRequired[str],
        "RelationshipStatus": NotRequired[str],
        "InvitedAt": NotRequired[str],
    },
)

MemberDataSourceConfigurationTypeDef = TypedDict(
    "MemberDataSourceConfigurationTypeDef",
    {
        "AccountId": str,
        "DataSources": "DataSourceConfigurationsResultTypeDef",
    },
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "AccountId": str,
        "MasterId": str,
        "Email": str,
        "RelationshipStatus": str,
        "UpdatedAt": str,
        "DetectorId": NotRequired[str],
        "InvitedAt": NotRequired[str],
    },
)

NetworkConnectionActionTypeDef = TypedDict(
    "NetworkConnectionActionTypeDef",
    {
        "Blocked": NotRequired[bool],
        "ConnectionDirection": NotRequired[str],
        "LocalPortDetails": NotRequired["LocalPortDetailsTypeDef"],
        "Protocol": NotRequired[str],
        "LocalIpDetails": NotRequired["LocalIpDetailsTypeDef"],
        "RemoteIpDetails": NotRequired["RemoteIpDetailsTypeDef"],
        "RemotePortDetails": NotRequired["RemotePortDetailsTypeDef"],
    },
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "Ipv6Addresses": NotRequired[List[str]],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateDnsName": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[List["PrivateIpAddressDetailsTypeDef"]],
        "PublicDnsName": NotRequired[str],
        "PublicIp": NotRequired[str],
        "SecurityGroups": NotRequired[List["SecurityGroupTypeDef"]],
        "SubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
    },
)

OrganizationDataSourceConfigurationsResultTypeDef = TypedDict(
    "OrganizationDataSourceConfigurationsResultTypeDef",
    {
        "S3Logs": "OrganizationS3LogsConfigurationResultTypeDef",
        "Kubernetes": NotRequired["OrganizationKubernetesConfigurationResultTypeDef"],
    },
)

OrganizationDataSourceConfigurationsTypeDef = TypedDict(
    "OrganizationDataSourceConfigurationsTypeDef",
    {
        "S3Logs": NotRequired["OrganizationS3LogsConfigurationTypeDef"],
        "Kubernetes": NotRequired["OrganizationKubernetesConfigurationTypeDef"],
    },
)

OrganizationKubernetesAuditLogsConfigurationResultTypeDef = TypedDict(
    "OrganizationKubernetesAuditLogsConfigurationResultTypeDef",
    {
        "AutoEnable": bool,
    },
)

OrganizationKubernetesAuditLogsConfigurationTypeDef = TypedDict(
    "OrganizationKubernetesAuditLogsConfigurationTypeDef",
    {
        "AutoEnable": bool,
    },
)

OrganizationKubernetesConfigurationResultTypeDef = TypedDict(
    "OrganizationKubernetesConfigurationResultTypeDef",
    {
        "AuditLogs": "OrganizationKubernetesAuditLogsConfigurationResultTypeDef",
    },
)

OrganizationKubernetesConfigurationTypeDef = TypedDict(
    "OrganizationKubernetesConfigurationTypeDef",
    {
        "AuditLogs": "OrganizationKubernetesAuditLogsConfigurationTypeDef",
    },
)

OrganizationS3LogsConfigurationResultTypeDef = TypedDict(
    "OrganizationS3LogsConfigurationResultTypeDef",
    {
        "AutoEnable": bool,
    },
)

OrganizationS3LogsConfigurationTypeDef = TypedDict(
    "OrganizationS3LogsConfigurationTypeDef",
    {
        "AutoEnable": bool,
    },
)

OrganizationTypeDef = TypedDict(
    "OrganizationTypeDef",
    {
        "Asn": NotRequired[str],
        "AsnOrg": NotRequired[str],
        "Isp": NotRequired[str],
        "Org": NotRequired[str],
    },
)

OwnerTypeDef = TypedDict(
    "OwnerTypeDef",
    {
        "Id": NotRequired[str],
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

PermissionConfigurationTypeDef = TypedDict(
    "PermissionConfigurationTypeDef",
    {
        "BucketLevelPermissions": NotRequired["BucketLevelPermissionsTypeDef"],
        "AccountLevelPermissions": NotRequired["AccountLevelPermissionsTypeDef"],
    },
)

PortProbeActionTypeDef = TypedDict(
    "PortProbeActionTypeDef",
    {
        "Blocked": NotRequired[bool],
        "PortProbeDetails": NotRequired[List["PortProbeDetailTypeDef"]],
    },
)

PortProbeDetailTypeDef = TypedDict(
    "PortProbeDetailTypeDef",
    {
        "LocalPortDetails": NotRequired["LocalPortDetailsTypeDef"],
        "LocalIpDetails": NotRequired["LocalIpDetailsTypeDef"],
        "RemoteIpDetails": NotRequired["RemoteIpDetailsTypeDef"],
    },
)

PrivateIpAddressDetailsTypeDef = TypedDict(
    "PrivateIpAddressDetailsTypeDef",
    {
        "PrivateDnsName": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
    },
)

ProductCodeTypeDef = TypedDict(
    "ProductCodeTypeDef",
    {
        "Code": NotRequired[str],
        "ProductType": NotRequired[str],
    },
)

PublicAccessTypeDef = TypedDict(
    "PublicAccessTypeDef",
    {
        "PermissionConfiguration": NotRequired["PermissionConfigurationTypeDef"],
        "EffectivePermission": NotRequired[str],
    },
)

RemoteAccountDetailsTypeDef = TypedDict(
    "RemoteAccountDetailsTypeDef",
    {
        "AccountId": NotRequired[str],
        "Affiliated": NotRequired[bool],
    },
)

RemoteIpDetailsTypeDef = TypedDict(
    "RemoteIpDetailsTypeDef",
    {
        "City": NotRequired["CityTypeDef"],
        "Country": NotRequired["CountryTypeDef"],
        "GeoLocation": NotRequired["GeoLocationTypeDef"],
        "IpAddressV4": NotRequired[str],
        "Organization": NotRequired["OrganizationTypeDef"],
    },
)

RemotePortDetailsTypeDef = TypedDict(
    "RemotePortDetailsTypeDef",
    {
        "Port": NotRequired[int],
        "PortName": NotRequired[str],
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "AccessKeyDetails": NotRequired["AccessKeyDetailsTypeDef"],
        "S3BucketDetails": NotRequired[List["S3BucketDetailTypeDef"]],
        "InstanceDetails": NotRequired["InstanceDetailsTypeDef"],
        "EksClusterDetails": NotRequired["EksClusterDetailsTypeDef"],
        "KubernetesDetails": NotRequired["KubernetesDetailsTypeDef"],
        "ResourceType": NotRequired[str],
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

S3BucketDetailTypeDef = TypedDict(
    "S3BucketDetailTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "Owner": NotRequired["OwnerTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
        "DefaultServerSideEncryption": NotRequired["DefaultServerSideEncryptionTypeDef"],
        "PublicAccess": NotRequired["PublicAccessTypeDef"],
    },
)

S3LogsConfigurationResultTypeDef = TypedDict(
    "S3LogsConfigurationResultTypeDef",
    {
        "Status": DataSourceStatusType,
    },
)

S3LogsConfigurationTypeDef = TypedDict(
    "S3LogsConfigurationTypeDef",
    {
        "Enable": bool,
    },
)

SecurityContextTypeDef = TypedDict(
    "SecurityContextTypeDef",
    {
        "Privileged": NotRequired[bool],
    },
)

SecurityGroupTypeDef = TypedDict(
    "SecurityGroupTypeDef",
    {
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
    },
)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "Action": NotRequired["ActionTypeDef"],
        "Evidence": NotRequired["EvidenceTypeDef"],
        "Archived": NotRequired[bool],
        "Count": NotRequired[int],
        "DetectorId": NotRequired[str],
        "EventFirstSeen": NotRequired[str],
        "EventLastSeen": NotRequired[str],
        "ResourceRole": NotRequired[str],
        "ServiceName": NotRequired[str],
        "UserFeedback": NotRequired[str],
    },
)

SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef",
    {
        "AttributeName": NotRequired[str],
        "OrderBy": NotRequired[OrderByType],
    },
)

StartMonitoringMembersRequestRequestTypeDef = TypedDict(
    "StartMonitoringMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": Sequence[str],
    },
)

StartMonitoringMembersResponseTypeDef = TypedDict(
    "StartMonitoringMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopMonitoringMembersRequestRequestTypeDef = TypedDict(
    "StopMonitoringMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": Sequence[str],
    },
)

StopMonitoringMembersResponseTypeDef = TypedDict(
    "StopMonitoringMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

ThreatIntelligenceDetailTypeDef = TypedDict(
    "ThreatIntelligenceDetailTypeDef",
    {
        "ThreatListName": NotRequired[str],
        "ThreatNames": NotRequired[List[str]],
    },
)

TotalTypeDef = TypedDict(
    "TotalTypeDef",
    {
        "Amount": NotRequired[str],
        "Unit": NotRequired[str],
    },
)

UnarchiveFindingsRequestRequestTypeDef = TypedDict(
    "UnarchiveFindingsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FindingIds": Sequence[str],
    },
)

UnprocessedAccountTypeDef = TypedDict(
    "UnprocessedAccountTypeDef",
    {
        "AccountId": str,
        "Result": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateDetectorRequestRequestTypeDef = TypedDict(
    "UpdateDetectorRequestRequestTypeDef",
    {
        "DetectorId": str,
        "Enable": NotRequired[bool],
        "FindingPublishingFrequency": NotRequired[FindingPublishingFrequencyType],
        "DataSources": NotRequired["DataSourceConfigurationsTypeDef"],
    },
)

UpdateFilterRequestRequestTypeDef = TypedDict(
    "UpdateFilterRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FilterName": str,
        "Description": NotRequired[str],
        "Action": NotRequired[FilterActionType],
        "Rank": NotRequired[int],
        "FindingCriteria": NotRequired["FindingCriteriaTypeDef"],
    },
)

UpdateFilterResponseTypeDef = TypedDict(
    "UpdateFilterResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFindingsFeedbackRequestRequestTypeDef = TypedDict(
    "UpdateFindingsFeedbackRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FindingIds": Sequence[str],
        "Feedback": FeedbackType,
        "Comments": NotRequired[str],
    },
)

UpdateIPSetRequestRequestTypeDef = TypedDict(
    "UpdateIPSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "IpSetId": str,
        "Name": NotRequired[str],
        "Location": NotRequired[str],
        "Activate": NotRequired[bool],
    },
)

UpdateMemberDetectorsRequestRequestTypeDef = TypedDict(
    "UpdateMemberDetectorsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": Sequence[str],
        "DataSources": NotRequired["DataSourceConfigurationsTypeDef"],
    },
)

UpdateMemberDetectorsResponseTypeDef = TypedDict(
    "UpdateMemberDetectorsResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AutoEnable": bool,
        "DataSources": NotRequired["OrganizationDataSourceConfigurationsTypeDef"],
    },
)

UpdatePublishingDestinationRequestRequestTypeDef = TypedDict(
    "UpdatePublishingDestinationRequestRequestTypeDef",
    {
        "DetectorId": str,
        "DestinationId": str,
        "DestinationProperties": NotRequired["DestinationPropertiesTypeDef"],
    },
)

UpdateThreatIntelSetRequestRequestTypeDef = TypedDict(
    "UpdateThreatIntelSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "ThreatIntelSetId": str,
        "Name": NotRequired[str],
        "Location": NotRequired[str],
        "Activate": NotRequired[bool],
    },
)

UsageAccountResultTypeDef = TypedDict(
    "UsageAccountResultTypeDef",
    {
        "AccountId": NotRequired[str],
        "Total": NotRequired["TotalTypeDef"],
    },
)

UsageCriteriaTypeDef = TypedDict(
    "UsageCriteriaTypeDef",
    {
        "DataSources": Sequence[DataSourceType],
        "AccountIds": NotRequired[Sequence[str]],
        "Resources": NotRequired[Sequence[str]],
    },
)

UsageDataSourceResultTypeDef = TypedDict(
    "UsageDataSourceResultTypeDef",
    {
        "DataSource": NotRequired[DataSourceType],
        "Total": NotRequired["TotalTypeDef"],
    },
)

UsageResourceResultTypeDef = TypedDict(
    "UsageResourceResultTypeDef",
    {
        "Resource": NotRequired[str],
        "Total": NotRequired["TotalTypeDef"],
    },
)

UsageStatisticsTypeDef = TypedDict(
    "UsageStatisticsTypeDef",
    {
        "SumByAccount": NotRequired[List["UsageAccountResultTypeDef"]],
        "SumByDataSource": NotRequired[List["UsageDataSourceResultTypeDef"]],
        "SumByResource": NotRequired[List["UsageResourceResultTypeDef"]],
        "TopResources": NotRequired[List["UsageResourceResultTypeDef"]],
    },
)

VolumeMountTypeDef = TypedDict(
    "VolumeMountTypeDef",
    {
        "Name": NotRequired[str],
        "MountPath": NotRequired[str],
    },
)

VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "Name": NotRequired[str],
        "HostPath": NotRequired["HostPathTypeDef"],
    },
)
