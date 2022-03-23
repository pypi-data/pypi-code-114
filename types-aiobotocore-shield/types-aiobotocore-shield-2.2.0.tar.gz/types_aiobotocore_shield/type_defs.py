"""
Type annotations for shield service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_shield/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_shield.type_defs import ApplicationLayerAutomaticResponseConfigurationTypeDef

    data: ApplicationLayerAutomaticResponseConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    ApplicationLayerAutomaticResponseStatusType,
    AttackLayerType,
    AttackPropertyIdentifierType,
    AutoRenewType,
    ProactiveEngagementStatusType,
    ProtectedResourceTypeType,
    ProtectionGroupAggregationType,
    ProtectionGroupPatternType,
    SubResourceTypeType,
    SubscriptionStateType,
    UnitType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationLayerAutomaticResponseConfigurationTypeDef",
    "AssociateDRTLogBucketRequestRequestTypeDef",
    "AssociateDRTRoleRequestRequestTypeDef",
    "AssociateHealthCheckRequestRequestTypeDef",
    "AssociateProactiveEngagementDetailsRequestRequestTypeDef",
    "AttackDetailTypeDef",
    "AttackPropertyTypeDef",
    "AttackStatisticsDataItemTypeDef",
    "AttackSummaryTypeDef",
    "AttackVectorDescriptionTypeDef",
    "AttackVolumeStatisticsTypeDef",
    "AttackVolumeTypeDef",
    "ContributorTypeDef",
    "CreateProtectionGroupRequestRequestTypeDef",
    "CreateProtectionRequestRequestTypeDef",
    "CreateProtectionResponseTypeDef",
    "DeleteProtectionGroupRequestRequestTypeDef",
    "DeleteProtectionRequestRequestTypeDef",
    "DescribeAttackRequestRequestTypeDef",
    "DescribeAttackResponseTypeDef",
    "DescribeAttackStatisticsResponseTypeDef",
    "DescribeDRTAccessResponseTypeDef",
    "DescribeEmergencyContactSettingsResponseTypeDef",
    "DescribeProtectionGroupRequestRequestTypeDef",
    "DescribeProtectionGroupResponseTypeDef",
    "DescribeProtectionRequestRequestTypeDef",
    "DescribeProtectionResponseTypeDef",
    "DescribeSubscriptionResponseTypeDef",
    "DisableApplicationLayerAutomaticResponseRequestRequestTypeDef",
    "DisassociateDRTLogBucketRequestRequestTypeDef",
    "DisassociateHealthCheckRequestRequestTypeDef",
    "EmergencyContactTypeDef",
    "EnableApplicationLayerAutomaticResponseRequestRequestTypeDef",
    "GetSubscriptionStateResponseTypeDef",
    "LimitTypeDef",
    "ListAttacksRequestRequestTypeDef",
    "ListAttacksResponseTypeDef",
    "ListProtectionGroupsRequestRequestTypeDef",
    "ListProtectionGroupsResponseTypeDef",
    "ListProtectionsRequestRequestTypeDef",
    "ListProtectionsResponseTypeDef",
    "ListResourcesInProtectionGroupRequestRequestTypeDef",
    "ListResourcesInProtectionGroupResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MitigationTypeDef",
    "PaginatorConfigTypeDef",
    "ProtectionGroupArbitraryPatternLimitsTypeDef",
    "ProtectionGroupLimitsTypeDef",
    "ProtectionGroupPatternTypeLimitsTypeDef",
    "ProtectionGroupTypeDef",
    "ProtectionLimitsTypeDef",
    "ProtectionTypeDef",
    "ResponseActionTypeDef",
    "ResponseMetadataTypeDef",
    "SubResourceSummaryTypeDef",
    "SubscriptionLimitsTypeDef",
    "SubscriptionTypeDef",
    "SummarizedAttackVectorTypeDef",
    "SummarizedCounterTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TimeRangeTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationLayerAutomaticResponseRequestRequestTypeDef",
    "UpdateEmergencyContactSettingsRequestRequestTypeDef",
    "UpdateProtectionGroupRequestRequestTypeDef",
    "UpdateSubscriptionRequestRequestTypeDef",
)

ApplicationLayerAutomaticResponseConfigurationTypeDef = TypedDict(
    "ApplicationLayerAutomaticResponseConfigurationTypeDef",
    {
        "Status": ApplicationLayerAutomaticResponseStatusType,
        "Action": "ResponseActionTypeDef",
    },
)

AssociateDRTLogBucketRequestRequestTypeDef = TypedDict(
    "AssociateDRTLogBucketRequestRequestTypeDef",
    {
        "LogBucket": str,
    },
)

AssociateDRTRoleRequestRequestTypeDef = TypedDict(
    "AssociateDRTRoleRequestRequestTypeDef",
    {
        "RoleArn": str,
    },
)

AssociateHealthCheckRequestRequestTypeDef = TypedDict(
    "AssociateHealthCheckRequestRequestTypeDef",
    {
        "ProtectionId": str,
        "HealthCheckArn": str,
    },
)

AssociateProactiveEngagementDetailsRequestRequestTypeDef = TypedDict(
    "AssociateProactiveEngagementDetailsRequestRequestTypeDef",
    {
        "EmergencyContactList": Sequence["EmergencyContactTypeDef"],
    },
)

AttackDetailTypeDef = TypedDict(
    "AttackDetailTypeDef",
    {
        "AttackId": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "SubResources": NotRequired[List["SubResourceSummaryTypeDef"]],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "AttackCounters": NotRequired[List["SummarizedCounterTypeDef"]],
        "AttackProperties": NotRequired[List["AttackPropertyTypeDef"]],
        "Mitigations": NotRequired[List["MitigationTypeDef"]],
    },
)

AttackPropertyTypeDef = TypedDict(
    "AttackPropertyTypeDef",
    {
        "AttackLayer": NotRequired[AttackLayerType],
        "AttackPropertyIdentifier": NotRequired[AttackPropertyIdentifierType],
        "TopContributors": NotRequired[List["ContributorTypeDef"]],
        "Unit": NotRequired[UnitType],
        "Total": NotRequired[int],
    },
)

AttackStatisticsDataItemTypeDef = TypedDict(
    "AttackStatisticsDataItemTypeDef",
    {
        "AttackCount": int,
        "AttackVolume": NotRequired["AttackVolumeTypeDef"],
    },
)

AttackSummaryTypeDef = TypedDict(
    "AttackSummaryTypeDef",
    {
        "AttackId": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "AttackVectors": NotRequired[List["AttackVectorDescriptionTypeDef"]],
    },
)

AttackVectorDescriptionTypeDef = TypedDict(
    "AttackVectorDescriptionTypeDef",
    {
        "VectorType": str,
    },
)

AttackVolumeStatisticsTypeDef = TypedDict(
    "AttackVolumeStatisticsTypeDef",
    {
        "Max": float,
    },
)

AttackVolumeTypeDef = TypedDict(
    "AttackVolumeTypeDef",
    {
        "BitsPerSecond": NotRequired["AttackVolumeStatisticsTypeDef"],
        "PacketsPerSecond": NotRequired["AttackVolumeStatisticsTypeDef"],
        "RequestsPerSecond": NotRequired["AttackVolumeStatisticsTypeDef"],
    },
)

ContributorTypeDef = TypedDict(
    "ContributorTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[int],
    },
)

CreateProtectionGroupRequestRequestTypeDef = TypedDict(
    "CreateProtectionGroupRequestRequestTypeDef",
    {
        "ProtectionGroupId": str,
        "Aggregation": ProtectionGroupAggregationType,
        "Pattern": ProtectionGroupPatternType,
        "ResourceType": NotRequired[ProtectedResourceTypeType],
        "Members": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateProtectionRequestRequestTypeDef = TypedDict(
    "CreateProtectionRequestRequestTypeDef",
    {
        "Name": str,
        "ResourceArn": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateProtectionResponseTypeDef = TypedDict(
    "CreateProtectionResponseTypeDef",
    {
        "ProtectionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProtectionGroupRequestRequestTypeDef = TypedDict(
    "DeleteProtectionGroupRequestRequestTypeDef",
    {
        "ProtectionGroupId": str,
    },
)

DeleteProtectionRequestRequestTypeDef = TypedDict(
    "DeleteProtectionRequestRequestTypeDef",
    {
        "ProtectionId": str,
    },
)

DescribeAttackRequestRequestTypeDef = TypedDict(
    "DescribeAttackRequestRequestTypeDef",
    {
        "AttackId": str,
    },
)

DescribeAttackResponseTypeDef = TypedDict(
    "DescribeAttackResponseTypeDef",
    {
        "Attack": "AttackDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAttackStatisticsResponseTypeDef = TypedDict(
    "DescribeAttackStatisticsResponseTypeDef",
    {
        "TimeRange": "TimeRangeTypeDef",
        "DataItems": List["AttackStatisticsDataItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDRTAccessResponseTypeDef = TypedDict(
    "DescribeDRTAccessResponseTypeDef",
    {
        "RoleArn": str,
        "LogBucketList": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEmergencyContactSettingsResponseTypeDef = TypedDict(
    "DescribeEmergencyContactSettingsResponseTypeDef",
    {
        "EmergencyContactList": List["EmergencyContactTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProtectionGroupRequestRequestTypeDef = TypedDict(
    "DescribeProtectionGroupRequestRequestTypeDef",
    {
        "ProtectionGroupId": str,
    },
)

DescribeProtectionGroupResponseTypeDef = TypedDict(
    "DescribeProtectionGroupResponseTypeDef",
    {
        "ProtectionGroup": "ProtectionGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProtectionRequestRequestTypeDef = TypedDict(
    "DescribeProtectionRequestRequestTypeDef",
    {
        "ProtectionId": NotRequired[str],
        "ResourceArn": NotRequired[str],
    },
)

DescribeProtectionResponseTypeDef = TypedDict(
    "DescribeProtectionResponseTypeDef",
    {
        "Protection": "ProtectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSubscriptionResponseTypeDef = TypedDict(
    "DescribeSubscriptionResponseTypeDef",
    {
        "Subscription": "SubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableApplicationLayerAutomaticResponseRequestRequestTypeDef = TypedDict(
    "DisableApplicationLayerAutomaticResponseRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DisassociateDRTLogBucketRequestRequestTypeDef = TypedDict(
    "DisassociateDRTLogBucketRequestRequestTypeDef",
    {
        "LogBucket": str,
    },
)

DisassociateHealthCheckRequestRequestTypeDef = TypedDict(
    "DisassociateHealthCheckRequestRequestTypeDef",
    {
        "ProtectionId": str,
        "HealthCheckArn": str,
    },
)

EmergencyContactTypeDef = TypedDict(
    "EmergencyContactTypeDef",
    {
        "EmailAddress": str,
        "PhoneNumber": NotRequired[str],
        "ContactNotes": NotRequired[str],
    },
)

EnableApplicationLayerAutomaticResponseRequestRequestTypeDef = TypedDict(
    "EnableApplicationLayerAutomaticResponseRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Action": "ResponseActionTypeDef",
    },
)

GetSubscriptionStateResponseTypeDef = TypedDict(
    "GetSubscriptionStateResponseTypeDef",
    {
        "SubscriptionState": SubscriptionStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LimitTypeDef = TypedDict(
    "LimitTypeDef",
    {
        "Type": NotRequired[str],
        "Max": NotRequired[int],
    },
)

ListAttacksRequestRequestTypeDef = TypedDict(
    "ListAttacksRequestRequestTypeDef",
    {
        "ResourceArns": NotRequired[Sequence[str]],
        "StartTime": NotRequired["TimeRangeTypeDef"],
        "EndTime": NotRequired["TimeRangeTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListAttacksResponseTypeDef = TypedDict(
    "ListAttacksResponseTypeDef",
    {
        "AttackSummaries": List["AttackSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProtectionGroupsRequestRequestTypeDef = TypedDict(
    "ListProtectionGroupsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListProtectionGroupsResponseTypeDef = TypedDict(
    "ListProtectionGroupsResponseTypeDef",
    {
        "ProtectionGroups": List["ProtectionGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProtectionsRequestRequestTypeDef = TypedDict(
    "ListProtectionsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListProtectionsResponseTypeDef = TypedDict(
    "ListProtectionsResponseTypeDef",
    {
        "Protections": List["ProtectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourcesInProtectionGroupRequestRequestTypeDef = TypedDict(
    "ListResourcesInProtectionGroupRequestRequestTypeDef",
    {
        "ProtectionGroupId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListResourcesInProtectionGroupResponseTypeDef = TypedDict(
    "ListResourcesInProtectionGroupResponseTypeDef",
    {
        "ResourceArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MitigationTypeDef = TypedDict(
    "MitigationTypeDef",
    {
        "MitigationName": NotRequired[str],
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

ProtectionGroupArbitraryPatternLimitsTypeDef = TypedDict(
    "ProtectionGroupArbitraryPatternLimitsTypeDef",
    {
        "MaxMembers": int,
    },
)

ProtectionGroupLimitsTypeDef = TypedDict(
    "ProtectionGroupLimitsTypeDef",
    {
        "MaxProtectionGroups": int,
        "PatternTypeLimits": "ProtectionGroupPatternTypeLimitsTypeDef",
    },
)

ProtectionGroupPatternTypeLimitsTypeDef = TypedDict(
    "ProtectionGroupPatternTypeLimitsTypeDef",
    {
        "ArbitraryPatternLimits": "ProtectionGroupArbitraryPatternLimitsTypeDef",
    },
)

ProtectionGroupTypeDef = TypedDict(
    "ProtectionGroupTypeDef",
    {
        "ProtectionGroupId": str,
        "Aggregation": ProtectionGroupAggregationType,
        "Pattern": ProtectionGroupPatternType,
        "Members": List[str],
        "ResourceType": NotRequired[ProtectedResourceTypeType],
        "ProtectionGroupArn": NotRequired[str],
    },
)

ProtectionLimitsTypeDef = TypedDict(
    "ProtectionLimitsTypeDef",
    {
        "ProtectedResourceTypeLimits": List["LimitTypeDef"],
    },
)

ProtectionTypeDef = TypedDict(
    "ProtectionTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "HealthCheckIds": NotRequired[List[str]],
        "ProtectionArn": NotRequired[str],
        "ApplicationLayerAutomaticResponseConfiguration": NotRequired[
            "ApplicationLayerAutomaticResponseConfigurationTypeDef"
        ],
    },
)

ResponseActionTypeDef = TypedDict(
    "ResponseActionTypeDef",
    {
        "Block": NotRequired[Dict[str, Any]],
        "Count": NotRequired[Dict[str, Any]],
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

SubResourceSummaryTypeDef = TypedDict(
    "SubResourceSummaryTypeDef",
    {
        "Type": NotRequired[SubResourceTypeType],
        "Id": NotRequired[str],
        "AttackVectors": NotRequired[List["SummarizedAttackVectorTypeDef"]],
        "Counters": NotRequired[List["SummarizedCounterTypeDef"]],
    },
)

SubscriptionLimitsTypeDef = TypedDict(
    "SubscriptionLimitsTypeDef",
    {
        "ProtectionLimits": "ProtectionLimitsTypeDef",
        "ProtectionGroupLimits": "ProtectionGroupLimitsTypeDef",
    },
)

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "SubscriptionLimits": "SubscriptionLimitsTypeDef",
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "TimeCommitmentInSeconds": NotRequired[int],
        "AutoRenew": NotRequired[AutoRenewType],
        "Limits": NotRequired[List["LimitTypeDef"]],
        "ProactiveEngagementStatus": NotRequired[ProactiveEngagementStatusType],
        "SubscriptionArn": NotRequired[str],
    },
)

SummarizedAttackVectorTypeDef = TypedDict(
    "SummarizedAttackVectorTypeDef",
    {
        "VectorType": str,
        "VectorCounters": NotRequired[List["SummarizedCounterTypeDef"]],
    },
)

SummarizedCounterTypeDef = TypedDict(
    "SummarizedCounterTypeDef",
    {
        "Name": NotRequired[str],
        "Max": NotRequired[float],
        "Average": NotRequired[float],
        "Sum": NotRequired[float],
        "N": NotRequired[int],
        "Unit": NotRequired[str],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "FromInclusive": NotRequired[datetime],
        "ToExclusive": NotRequired[datetime],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateApplicationLayerAutomaticResponseRequestRequestTypeDef = TypedDict(
    "UpdateApplicationLayerAutomaticResponseRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Action": "ResponseActionTypeDef",
    },
)

UpdateEmergencyContactSettingsRequestRequestTypeDef = TypedDict(
    "UpdateEmergencyContactSettingsRequestRequestTypeDef",
    {
        "EmergencyContactList": NotRequired[Sequence["EmergencyContactTypeDef"]],
    },
)

UpdateProtectionGroupRequestRequestTypeDef = TypedDict(
    "UpdateProtectionGroupRequestRequestTypeDef",
    {
        "ProtectionGroupId": str,
        "Aggregation": ProtectionGroupAggregationType,
        "Pattern": ProtectionGroupPatternType,
        "ResourceType": NotRequired[ProtectedResourceTypeType],
        "Members": NotRequired[Sequence[str]],
    },
)

UpdateSubscriptionRequestRequestTypeDef = TypedDict(
    "UpdateSubscriptionRequestRequestTypeDef",
    {
        "AutoRenew": NotRequired[AutoRenewType],
    },
)
