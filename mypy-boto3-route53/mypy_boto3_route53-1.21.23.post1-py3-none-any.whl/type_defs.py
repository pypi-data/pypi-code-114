"""
Type annotations for route53 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/type_defs.html)

Usage::

    ```python
    from mypy_boto3_route53.type_defs import AccountLimitTypeDef

    data: AccountLimitTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    AccountLimitTypeType,
    ChangeActionType,
    ChangeStatusType,
    CloudWatchRegionType,
    ComparisonOperatorType,
    HealthCheckRegionType,
    HealthCheckTypeType,
    HostedZoneLimitTypeType,
    InsufficientDataHealthStatusType,
    ResettableElementNameType,
    ResourceRecordSetFailoverType,
    ResourceRecordSetRegionType,
    RRTypeType,
    StatisticType,
    TagResourceTypeType,
    VPCRegionType,
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
    "AccountLimitTypeDef",
    "ActivateKeySigningKeyRequestRequestTypeDef",
    "ActivateKeySigningKeyResponseTypeDef",
    "AlarmIdentifierTypeDef",
    "AliasTargetTypeDef",
    "AssociateVPCWithHostedZoneRequestRequestTypeDef",
    "AssociateVPCWithHostedZoneResponseTypeDef",
    "ChangeBatchTypeDef",
    "ChangeInfoTypeDef",
    "ChangeResourceRecordSetsRequestRequestTypeDef",
    "ChangeResourceRecordSetsResponseTypeDef",
    "ChangeTagsForResourceRequestRequestTypeDef",
    "ChangeTypeDef",
    "CloudWatchAlarmConfigurationTypeDef",
    "CreateHealthCheckRequestRequestTypeDef",
    "CreateHealthCheckResponseTypeDef",
    "CreateHostedZoneRequestRequestTypeDef",
    "CreateHostedZoneResponseTypeDef",
    "CreateKeySigningKeyRequestRequestTypeDef",
    "CreateKeySigningKeyResponseTypeDef",
    "CreateQueryLoggingConfigRequestRequestTypeDef",
    "CreateQueryLoggingConfigResponseTypeDef",
    "CreateReusableDelegationSetRequestRequestTypeDef",
    "CreateReusableDelegationSetResponseTypeDef",
    "CreateTrafficPolicyInstanceRequestRequestTypeDef",
    "CreateTrafficPolicyInstanceResponseTypeDef",
    "CreateTrafficPolicyRequestRequestTypeDef",
    "CreateTrafficPolicyResponseTypeDef",
    "CreateTrafficPolicyVersionRequestRequestTypeDef",
    "CreateTrafficPolicyVersionResponseTypeDef",
    "CreateVPCAssociationAuthorizationRequestRequestTypeDef",
    "CreateVPCAssociationAuthorizationResponseTypeDef",
    "DNSSECStatusTypeDef",
    "DeactivateKeySigningKeyRequestRequestTypeDef",
    "DeactivateKeySigningKeyResponseTypeDef",
    "DelegationSetTypeDef",
    "DeleteHealthCheckRequestRequestTypeDef",
    "DeleteHostedZoneRequestRequestTypeDef",
    "DeleteHostedZoneResponseTypeDef",
    "DeleteKeySigningKeyRequestRequestTypeDef",
    "DeleteKeySigningKeyResponseTypeDef",
    "DeleteQueryLoggingConfigRequestRequestTypeDef",
    "DeleteReusableDelegationSetRequestRequestTypeDef",
    "DeleteTrafficPolicyInstanceRequestRequestTypeDef",
    "DeleteTrafficPolicyRequestRequestTypeDef",
    "DeleteVPCAssociationAuthorizationRequestRequestTypeDef",
    "DimensionTypeDef",
    "DisableHostedZoneDNSSECRequestRequestTypeDef",
    "DisableHostedZoneDNSSECResponseTypeDef",
    "DisassociateVPCFromHostedZoneRequestRequestTypeDef",
    "DisassociateVPCFromHostedZoneResponseTypeDef",
    "EnableHostedZoneDNSSECRequestRequestTypeDef",
    "EnableHostedZoneDNSSECResponseTypeDef",
    "GeoLocationDetailsTypeDef",
    "GeoLocationTypeDef",
    "GetAccountLimitRequestRequestTypeDef",
    "GetAccountLimitResponseTypeDef",
    "GetChangeRequestRequestTypeDef",
    "GetChangeResponseTypeDef",
    "GetCheckerIpRangesResponseTypeDef",
    "GetDNSSECRequestRequestTypeDef",
    "GetDNSSECResponseTypeDef",
    "GetGeoLocationRequestRequestTypeDef",
    "GetGeoLocationResponseTypeDef",
    "GetHealthCheckCountResponseTypeDef",
    "GetHealthCheckLastFailureReasonRequestRequestTypeDef",
    "GetHealthCheckLastFailureReasonResponseTypeDef",
    "GetHealthCheckRequestRequestTypeDef",
    "GetHealthCheckResponseTypeDef",
    "GetHealthCheckStatusRequestRequestTypeDef",
    "GetHealthCheckStatusResponseTypeDef",
    "GetHostedZoneCountResponseTypeDef",
    "GetHostedZoneLimitRequestRequestTypeDef",
    "GetHostedZoneLimitResponseTypeDef",
    "GetHostedZoneRequestRequestTypeDef",
    "GetHostedZoneResponseTypeDef",
    "GetQueryLoggingConfigRequestRequestTypeDef",
    "GetQueryLoggingConfigResponseTypeDef",
    "GetReusableDelegationSetLimitRequestRequestTypeDef",
    "GetReusableDelegationSetLimitResponseTypeDef",
    "GetReusableDelegationSetRequestRequestTypeDef",
    "GetReusableDelegationSetResponseTypeDef",
    "GetTrafficPolicyInstanceCountResponseTypeDef",
    "GetTrafficPolicyInstanceRequestRequestTypeDef",
    "GetTrafficPolicyInstanceResponseTypeDef",
    "GetTrafficPolicyRequestRequestTypeDef",
    "GetTrafficPolicyResponseTypeDef",
    "HealthCheckConfigTypeDef",
    "HealthCheckObservationTypeDef",
    "HealthCheckTypeDef",
    "HostedZoneConfigTypeDef",
    "HostedZoneLimitTypeDef",
    "HostedZoneOwnerTypeDef",
    "HostedZoneSummaryTypeDef",
    "HostedZoneTypeDef",
    "KeySigningKeyTypeDef",
    "LinkedServiceTypeDef",
    "ListGeoLocationsRequestRequestTypeDef",
    "ListGeoLocationsResponseTypeDef",
    "ListHealthChecksRequestRequestTypeDef",
    "ListHealthChecksResponseTypeDef",
    "ListHostedZonesByNameRequestRequestTypeDef",
    "ListHostedZonesByNameResponseTypeDef",
    "ListHostedZonesByVPCRequestRequestTypeDef",
    "ListHostedZonesByVPCResponseTypeDef",
    "ListHostedZonesRequestRequestTypeDef",
    "ListHostedZonesResponseTypeDef",
    "ListQueryLoggingConfigsRequestRequestTypeDef",
    "ListQueryLoggingConfigsResponseTypeDef",
    "ListResourceRecordSetsRequestRequestTypeDef",
    "ListResourceRecordSetsResponseTypeDef",
    "ListReusableDelegationSetsRequestRequestTypeDef",
    "ListReusableDelegationSetsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTagsForResourcesRequestRequestTypeDef",
    "ListTagsForResourcesResponseTypeDef",
    "ListTrafficPoliciesRequestRequestTypeDef",
    "ListTrafficPoliciesResponseTypeDef",
    "ListTrafficPolicyInstancesByHostedZoneRequestRequestTypeDef",
    "ListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    "ListTrafficPolicyInstancesByPolicyRequestRequestTypeDef",
    "ListTrafficPolicyInstancesByPolicyResponseTypeDef",
    "ListTrafficPolicyInstancesRequestRequestTypeDef",
    "ListTrafficPolicyInstancesResponseTypeDef",
    "ListTrafficPolicyVersionsRequestRequestTypeDef",
    "ListTrafficPolicyVersionsResponseTypeDef",
    "ListVPCAssociationAuthorizationsRequestRequestTypeDef",
    "ListVPCAssociationAuthorizationsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "QueryLoggingConfigTypeDef",
    "ResourceRecordSetTypeDef",
    "ResourceRecordTypeDef",
    "ResourceTagSetTypeDef",
    "ResponseMetadataTypeDef",
    "ReusableDelegationSetLimitTypeDef",
    "StatusReportTypeDef",
    "TagTypeDef",
    "TestDNSAnswerRequestRequestTypeDef",
    "TestDNSAnswerResponseTypeDef",
    "TrafficPolicyInstanceTypeDef",
    "TrafficPolicySummaryTypeDef",
    "TrafficPolicyTypeDef",
    "UpdateHealthCheckRequestRequestTypeDef",
    "UpdateHealthCheckResponseTypeDef",
    "UpdateHostedZoneCommentRequestRequestTypeDef",
    "UpdateHostedZoneCommentResponseTypeDef",
    "UpdateTrafficPolicyCommentRequestRequestTypeDef",
    "UpdateTrafficPolicyCommentResponseTypeDef",
    "UpdateTrafficPolicyInstanceRequestRequestTypeDef",
    "UpdateTrafficPolicyInstanceResponseTypeDef",
    "VPCTypeDef",
    "WaiterConfigTypeDef",
)

AccountLimitTypeDef = TypedDict(
    "AccountLimitTypeDef",
    {
        "Type": AccountLimitTypeType,
        "Value": int,
    },
)

ActivateKeySigningKeyRequestRequestTypeDef = TypedDict(
    "ActivateKeySigningKeyRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "Name": str,
    },
)

ActivateKeySigningKeyResponseTypeDef = TypedDict(
    "ActivateKeySigningKeyResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AlarmIdentifierTypeDef = TypedDict(
    "AlarmIdentifierTypeDef",
    {
        "Region": CloudWatchRegionType,
        "Name": str,
    },
)

AliasTargetTypeDef = TypedDict(
    "AliasTargetTypeDef",
    {
        "HostedZoneId": str,
        "DNSName": str,
        "EvaluateTargetHealth": bool,
    },
)

AssociateVPCWithHostedZoneRequestRequestTypeDef = TypedDict(
    "AssociateVPCWithHostedZoneRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "VPC": "VPCTypeDef",
        "Comment": NotRequired[str],
    },
)

AssociateVPCWithHostedZoneResponseTypeDef = TypedDict(
    "AssociateVPCWithHostedZoneResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChangeBatchTypeDef = TypedDict(
    "ChangeBatchTypeDef",
    {
        "Changes": Sequence["ChangeTypeDef"],
        "Comment": NotRequired[str],
    },
)

ChangeInfoTypeDef = TypedDict(
    "ChangeInfoTypeDef",
    {
        "Id": str,
        "Status": ChangeStatusType,
        "SubmittedAt": datetime,
        "Comment": NotRequired[str],
    },
)

ChangeResourceRecordSetsRequestRequestTypeDef = TypedDict(
    "ChangeResourceRecordSetsRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "ChangeBatch": "ChangeBatchTypeDef",
    },
)

ChangeResourceRecordSetsResponseTypeDef = TypedDict(
    "ChangeResourceRecordSetsResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChangeTagsForResourceRequestRequestTypeDef = TypedDict(
    "ChangeTagsForResourceRequestRequestTypeDef",
    {
        "ResourceType": TagResourceTypeType,
        "ResourceId": str,
        "AddTags": NotRequired[Sequence["TagTypeDef"]],
        "RemoveTagKeys": NotRequired[Sequence[str]],
    },
)

ChangeTypeDef = TypedDict(
    "ChangeTypeDef",
    {
        "Action": ChangeActionType,
        "ResourceRecordSet": "ResourceRecordSetTypeDef",
    },
)

CloudWatchAlarmConfigurationTypeDef = TypedDict(
    "CloudWatchAlarmConfigurationTypeDef",
    {
        "EvaluationPeriods": int,
        "Threshold": float,
        "ComparisonOperator": ComparisonOperatorType,
        "Period": int,
        "MetricName": str,
        "Namespace": str,
        "Statistic": StatisticType,
        "Dimensions": NotRequired[List["DimensionTypeDef"]],
    },
)

CreateHealthCheckRequestRequestTypeDef = TypedDict(
    "CreateHealthCheckRequestRequestTypeDef",
    {
        "CallerReference": str,
        "HealthCheckConfig": "HealthCheckConfigTypeDef",
    },
)

CreateHealthCheckResponseTypeDef = TypedDict(
    "CreateHealthCheckResponseTypeDef",
    {
        "HealthCheck": "HealthCheckTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateHostedZoneRequestRequestTypeDef = TypedDict(
    "CreateHostedZoneRequestRequestTypeDef",
    {
        "Name": str,
        "CallerReference": str,
        "VPC": NotRequired["VPCTypeDef"],
        "HostedZoneConfig": NotRequired["HostedZoneConfigTypeDef"],
        "DelegationSetId": NotRequired[str],
    },
)

CreateHostedZoneResponseTypeDef = TypedDict(
    "CreateHostedZoneResponseTypeDef",
    {
        "HostedZone": "HostedZoneTypeDef",
        "ChangeInfo": "ChangeInfoTypeDef",
        "DelegationSet": "DelegationSetTypeDef",
        "VPC": "VPCTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateKeySigningKeyRequestRequestTypeDef = TypedDict(
    "CreateKeySigningKeyRequestRequestTypeDef",
    {
        "CallerReference": str,
        "HostedZoneId": str,
        "KeyManagementServiceArn": str,
        "Name": str,
        "Status": str,
    },
)

CreateKeySigningKeyResponseTypeDef = TypedDict(
    "CreateKeySigningKeyResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "KeySigningKey": "KeySigningKeyTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateQueryLoggingConfigRequestRequestTypeDef = TypedDict(
    "CreateQueryLoggingConfigRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "CloudWatchLogsLogGroupArn": str,
    },
)

CreateQueryLoggingConfigResponseTypeDef = TypedDict(
    "CreateQueryLoggingConfigResponseTypeDef",
    {
        "QueryLoggingConfig": "QueryLoggingConfigTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateReusableDelegationSetRequestRequestTypeDef = TypedDict(
    "CreateReusableDelegationSetRequestRequestTypeDef",
    {
        "CallerReference": str,
        "HostedZoneId": NotRequired[str],
    },
)

CreateReusableDelegationSetResponseTypeDef = TypedDict(
    "CreateReusableDelegationSetResponseTypeDef",
    {
        "DelegationSet": "DelegationSetTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTrafficPolicyInstanceRequestRequestTypeDef = TypedDict(
    "CreateTrafficPolicyInstanceRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
    },
)

CreateTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "CreateTrafficPolicyInstanceResponseTypeDef",
    {
        "TrafficPolicyInstance": "TrafficPolicyInstanceTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTrafficPolicyRequestRequestTypeDef = TypedDict(
    "CreateTrafficPolicyRequestRequestTypeDef",
    {
        "Name": str,
        "Document": str,
        "Comment": NotRequired[str],
    },
)

CreateTrafficPolicyResponseTypeDef = TypedDict(
    "CreateTrafficPolicyResponseTypeDef",
    {
        "TrafficPolicy": "TrafficPolicyTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTrafficPolicyVersionRequestRequestTypeDef = TypedDict(
    "CreateTrafficPolicyVersionRequestRequestTypeDef",
    {
        "Id": str,
        "Document": str,
        "Comment": NotRequired[str],
    },
)

CreateTrafficPolicyVersionResponseTypeDef = TypedDict(
    "CreateTrafficPolicyVersionResponseTypeDef",
    {
        "TrafficPolicy": "TrafficPolicyTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVPCAssociationAuthorizationRequestRequestTypeDef = TypedDict(
    "CreateVPCAssociationAuthorizationRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "VPC": "VPCTypeDef",
    },
)

CreateVPCAssociationAuthorizationResponseTypeDef = TypedDict(
    "CreateVPCAssociationAuthorizationResponseTypeDef",
    {
        "HostedZoneId": str,
        "VPC": "VPCTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DNSSECStatusTypeDef = TypedDict(
    "DNSSECStatusTypeDef",
    {
        "ServeSignature": NotRequired[str],
        "StatusMessage": NotRequired[str],
    },
)

DeactivateKeySigningKeyRequestRequestTypeDef = TypedDict(
    "DeactivateKeySigningKeyRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "Name": str,
    },
)

DeactivateKeySigningKeyResponseTypeDef = TypedDict(
    "DeactivateKeySigningKeyResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DelegationSetTypeDef = TypedDict(
    "DelegationSetTypeDef",
    {
        "NameServers": List[str],
        "Id": NotRequired[str],
        "CallerReference": NotRequired[str],
    },
)

DeleteHealthCheckRequestRequestTypeDef = TypedDict(
    "DeleteHealthCheckRequestRequestTypeDef",
    {
        "HealthCheckId": str,
    },
)

DeleteHostedZoneRequestRequestTypeDef = TypedDict(
    "DeleteHostedZoneRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteHostedZoneResponseTypeDef = TypedDict(
    "DeleteHostedZoneResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteKeySigningKeyRequestRequestTypeDef = TypedDict(
    "DeleteKeySigningKeyRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "Name": str,
    },
)

DeleteKeySigningKeyResponseTypeDef = TypedDict(
    "DeleteKeySigningKeyResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteQueryLoggingConfigRequestRequestTypeDef = TypedDict(
    "DeleteQueryLoggingConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteReusableDelegationSetRequestRequestTypeDef = TypedDict(
    "DeleteReusableDelegationSetRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteTrafficPolicyInstanceRequestRequestTypeDef = TypedDict(
    "DeleteTrafficPolicyInstanceRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteTrafficPolicyRequestRequestTypeDef = TypedDict(
    "DeleteTrafficPolicyRequestRequestTypeDef",
    {
        "Id": str,
        "Version": int,
    },
)

DeleteVPCAssociationAuthorizationRequestRequestTypeDef = TypedDict(
    "DeleteVPCAssociationAuthorizationRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "VPC": "VPCTypeDef",
    },
)

DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

DisableHostedZoneDNSSECRequestRequestTypeDef = TypedDict(
    "DisableHostedZoneDNSSECRequestRequestTypeDef",
    {
        "HostedZoneId": str,
    },
)

DisableHostedZoneDNSSECResponseTypeDef = TypedDict(
    "DisableHostedZoneDNSSECResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateVPCFromHostedZoneRequestRequestTypeDef = TypedDict(
    "DisassociateVPCFromHostedZoneRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "VPC": "VPCTypeDef",
        "Comment": NotRequired[str],
    },
)

DisassociateVPCFromHostedZoneResponseTypeDef = TypedDict(
    "DisassociateVPCFromHostedZoneResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableHostedZoneDNSSECRequestRequestTypeDef = TypedDict(
    "EnableHostedZoneDNSSECRequestRequestTypeDef",
    {
        "HostedZoneId": str,
    },
)

EnableHostedZoneDNSSECResponseTypeDef = TypedDict(
    "EnableHostedZoneDNSSECResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GeoLocationDetailsTypeDef = TypedDict(
    "GeoLocationDetailsTypeDef",
    {
        "ContinentCode": NotRequired[str],
        "ContinentName": NotRequired[str],
        "CountryCode": NotRequired[str],
        "CountryName": NotRequired[str],
        "SubdivisionCode": NotRequired[str],
        "SubdivisionName": NotRequired[str],
    },
)

GeoLocationTypeDef = TypedDict(
    "GeoLocationTypeDef",
    {
        "ContinentCode": NotRequired[str],
        "CountryCode": NotRequired[str],
        "SubdivisionCode": NotRequired[str],
    },
)

GetAccountLimitRequestRequestTypeDef = TypedDict(
    "GetAccountLimitRequestRequestTypeDef",
    {
        "Type": AccountLimitTypeType,
    },
)

GetAccountLimitResponseTypeDef = TypedDict(
    "GetAccountLimitResponseTypeDef",
    {
        "Limit": "AccountLimitTypeDef",
        "Count": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChangeRequestRequestTypeDef = TypedDict(
    "GetChangeRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetChangeResponseTypeDef = TypedDict(
    "GetChangeResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCheckerIpRangesResponseTypeDef = TypedDict(
    "GetCheckerIpRangesResponseTypeDef",
    {
        "CheckerIpRanges": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDNSSECRequestRequestTypeDef = TypedDict(
    "GetDNSSECRequestRequestTypeDef",
    {
        "HostedZoneId": str,
    },
)

GetDNSSECResponseTypeDef = TypedDict(
    "GetDNSSECResponseTypeDef",
    {
        "Status": "DNSSECStatusTypeDef",
        "KeySigningKeys": List["KeySigningKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGeoLocationRequestRequestTypeDef = TypedDict(
    "GetGeoLocationRequestRequestTypeDef",
    {
        "ContinentCode": NotRequired[str],
        "CountryCode": NotRequired[str],
        "SubdivisionCode": NotRequired[str],
    },
)

GetGeoLocationResponseTypeDef = TypedDict(
    "GetGeoLocationResponseTypeDef",
    {
        "GeoLocationDetails": "GeoLocationDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHealthCheckCountResponseTypeDef = TypedDict(
    "GetHealthCheckCountResponseTypeDef",
    {
        "HealthCheckCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHealthCheckLastFailureReasonRequestRequestTypeDef = TypedDict(
    "GetHealthCheckLastFailureReasonRequestRequestTypeDef",
    {
        "HealthCheckId": str,
    },
)

GetHealthCheckLastFailureReasonResponseTypeDef = TypedDict(
    "GetHealthCheckLastFailureReasonResponseTypeDef",
    {
        "HealthCheckObservations": List["HealthCheckObservationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHealthCheckRequestRequestTypeDef = TypedDict(
    "GetHealthCheckRequestRequestTypeDef",
    {
        "HealthCheckId": str,
    },
)

GetHealthCheckResponseTypeDef = TypedDict(
    "GetHealthCheckResponseTypeDef",
    {
        "HealthCheck": "HealthCheckTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHealthCheckStatusRequestRequestTypeDef = TypedDict(
    "GetHealthCheckStatusRequestRequestTypeDef",
    {
        "HealthCheckId": str,
    },
)

GetHealthCheckStatusResponseTypeDef = TypedDict(
    "GetHealthCheckStatusResponseTypeDef",
    {
        "HealthCheckObservations": List["HealthCheckObservationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHostedZoneCountResponseTypeDef = TypedDict(
    "GetHostedZoneCountResponseTypeDef",
    {
        "HostedZoneCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHostedZoneLimitRequestRequestTypeDef = TypedDict(
    "GetHostedZoneLimitRequestRequestTypeDef",
    {
        "Type": HostedZoneLimitTypeType,
        "HostedZoneId": str,
    },
)

GetHostedZoneLimitResponseTypeDef = TypedDict(
    "GetHostedZoneLimitResponseTypeDef",
    {
        "Limit": "HostedZoneLimitTypeDef",
        "Count": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHostedZoneRequestRequestTypeDef = TypedDict(
    "GetHostedZoneRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetHostedZoneResponseTypeDef = TypedDict(
    "GetHostedZoneResponseTypeDef",
    {
        "HostedZone": "HostedZoneTypeDef",
        "DelegationSet": "DelegationSetTypeDef",
        "VPCs": List["VPCTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryLoggingConfigRequestRequestTypeDef = TypedDict(
    "GetQueryLoggingConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetQueryLoggingConfigResponseTypeDef = TypedDict(
    "GetQueryLoggingConfigResponseTypeDef",
    {
        "QueryLoggingConfig": "QueryLoggingConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReusableDelegationSetLimitRequestRequestTypeDef = TypedDict(
    "GetReusableDelegationSetLimitRequestRequestTypeDef",
    {
        "Type": Literal["MAX_ZONES_BY_REUSABLE_DELEGATION_SET"],
        "DelegationSetId": str,
    },
)

GetReusableDelegationSetLimitResponseTypeDef = TypedDict(
    "GetReusableDelegationSetLimitResponseTypeDef",
    {
        "Limit": "ReusableDelegationSetLimitTypeDef",
        "Count": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReusableDelegationSetRequestRequestTypeDef = TypedDict(
    "GetReusableDelegationSetRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetReusableDelegationSetResponseTypeDef = TypedDict(
    "GetReusableDelegationSetResponseTypeDef",
    {
        "DelegationSet": "DelegationSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrafficPolicyInstanceCountResponseTypeDef = TypedDict(
    "GetTrafficPolicyInstanceCountResponseTypeDef",
    {
        "TrafficPolicyInstanceCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrafficPolicyInstanceRequestRequestTypeDef = TypedDict(
    "GetTrafficPolicyInstanceRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "GetTrafficPolicyInstanceResponseTypeDef",
    {
        "TrafficPolicyInstance": "TrafficPolicyInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrafficPolicyRequestRequestTypeDef = TypedDict(
    "GetTrafficPolicyRequestRequestTypeDef",
    {
        "Id": str,
        "Version": int,
    },
)

GetTrafficPolicyResponseTypeDef = TypedDict(
    "GetTrafficPolicyResponseTypeDef",
    {
        "TrafficPolicy": "TrafficPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HealthCheckConfigTypeDef = TypedDict(
    "HealthCheckConfigTypeDef",
    {
        "Type": HealthCheckTypeType,
        "IPAddress": NotRequired[str],
        "Port": NotRequired[int],
        "ResourcePath": NotRequired[str],
        "FullyQualifiedDomainName": NotRequired[str],
        "SearchString": NotRequired[str],
        "RequestInterval": NotRequired[int],
        "FailureThreshold": NotRequired[int],
        "MeasureLatency": NotRequired[bool],
        "Inverted": NotRequired[bool],
        "Disabled": NotRequired[bool],
        "HealthThreshold": NotRequired[int],
        "ChildHealthChecks": NotRequired[Sequence[str]],
        "EnableSNI": NotRequired[bool],
        "Regions": NotRequired[Sequence[HealthCheckRegionType]],
        "AlarmIdentifier": NotRequired["AlarmIdentifierTypeDef"],
        "InsufficientDataHealthStatus": NotRequired[InsufficientDataHealthStatusType],
        "RoutingControlArn": NotRequired[str],
    },
)

HealthCheckObservationTypeDef = TypedDict(
    "HealthCheckObservationTypeDef",
    {
        "Region": NotRequired[HealthCheckRegionType],
        "IPAddress": NotRequired[str],
        "StatusReport": NotRequired["StatusReportTypeDef"],
    },
)

HealthCheckTypeDef = TypedDict(
    "HealthCheckTypeDef",
    {
        "Id": str,
        "CallerReference": str,
        "HealthCheckConfig": "HealthCheckConfigTypeDef",
        "HealthCheckVersion": int,
        "LinkedService": NotRequired["LinkedServiceTypeDef"],
        "CloudWatchAlarmConfiguration": NotRequired["CloudWatchAlarmConfigurationTypeDef"],
    },
)

HostedZoneConfigTypeDef = TypedDict(
    "HostedZoneConfigTypeDef",
    {
        "Comment": NotRequired[str],
        "PrivateZone": NotRequired[bool],
    },
)

HostedZoneLimitTypeDef = TypedDict(
    "HostedZoneLimitTypeDef",
    {
        "Type": HostedZoneLimitTypeType,
        "Value": int,
    },
)

HostedZoneOwnerTypeDef = TypedDict(
    "HostedZoneOwnerTypeDef",
    {
        "OwningAccount": NotRequired[str],
        "OwningService": NotRequired[str],
    },
)

HostedZoneSummaryTypeDef = TypedDict(
    "HostedZoneSummaryTypeDef",
    {
        "HostedZoneId": str,
        "Name": str,
        "Owner": "HostedZoneOwnerTypeDef",
    },
)

HostedZoneTypeDef = TypedDict(
    "HostedZoneTypeDef",
    {
        "Id": str,
        "Name": str,
        "CallerReference": str,
        "Config": NotRequired["HostedZoneConfigTypeDef"],
        "ResourceRecordSetCount": NotRequired[int],
        "LinkedService": NotRequired["LinkedServiceTypeDef"],
    },
)

KeySigningKeyTypeDef = TypedDict(
    "KeySigningKeyTypeDef",
    {
        "Name": NotRequired[str],
        "KmsArn": NotRequired[str],
        "Flag": NotRequired[int],
        "SigningAlgorithmMnemonic": NotRequired[str],
        "SigningAlgorithmType": NotRequired[int],
        "DigestAlgorithmMnemonic": NotRequired[str],
        "DigestAlgorithmType": NotRequired[int],
        "KeyTag": NotRequired[int],
        "DigestValue": NotRequired[str],
        "PublicKey": NotRequired[str],
        "DSRecord": NotRequired[str],
        "DNSKEYRecord": NotRequired[str],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "LastModifiedDate": NotRequired[datetime],
    },
)

LinkedServiceTypeDef = TypedDict(
    "LinkedServiceTypeDef",
    {
        "ServicePrincipal": NotRequired[str],
        "Description": NotRequired[str],
    },
)

ListGeoLocationsRequestRequestTypeDef = TypedDict(
    "ListGeoLocationsRequestRequestTypeDef",
    {
        "StartContinentCode": NotRequired[str],
        "StartCountryCode": NotRequired[str],
        "StartSubdivisionCode": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListGeoLocationsResponseTypeDef = TypedDict(
    "ListGeoLocationsResponseTypeDef",
    {
        "GeoLocationDetailsList": List["GeoLocationDetailsTypeDef"],
        "IsTruncated": bool,
        "NextContinentCode": str,
        "NextCountryCode": str,
        "NextSubdivisionCode": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHealthChecksRequestRequestTypeDef = TypedDict(
    "ListHealthChecksRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListHealthChecksResponseTypeDef = TypedDict(
    "ListHealthChecksResponseTypeDef",
    {
        "HealthChecks": List["HealthCheckTypeDef"],
        "Marker": str,
        "IsTruncated": bool,
        "NextMarker": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHostedZonesByNameRequestRequestTypeDef = TypedDict(
    "ListHostedZonesByNameRequestRequestTypeDef",
    {
        "DNSName": NotRequired[str],
        "HostedZoneId": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListHostedZonesByNameResponseTypeDef = TypedDict(
    "ListHostedZonesByNameResponseTypeDef",
    {
        "HostedZones": List["HostedZoneTypeDef"],
        "DNSName": str,
        "HostedZoneId": str,
        "IsTruncated": bool,
        "NextDNSName": str,
        "NextHostedZoneId": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHostedZonesByVPCRequestRequestTypeDef = TypedDict(
    "ListHostedZonesByVPCRequestRequestTypeDef",
    {
        "VPCId": str,
        "VPCRegion": VPCRegionType,
        "MaxItems": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

ListHostedZonesByVPCResponseTypeDef = TypedDict(
    "ListHostedZonesByVPCResponseTypeDef",
    {
        "HostedZoneSummaries": List["HostedZoneSummaryTypeDef"],
        "MaxItems": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHostedZonesRequestRequestTypeDef = TypedDict(
    "ListHostedZonesRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
        "DelegationSetId": NotRequired[str],
    },
)

ListHostedZonesResponseTypeDef = TypedDict(
    "ListHostedZonesResponseTypeDef",
    {
        "HostedZones": List["HostedZoneTypeDef"],
        "Marker": str,
        "IsTruncated": bool,
        "NextMarker": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQueryLoggingConfigsRequestRequestTypeDef = TypedDict(
    "ListQueryLoggingConfigsRequestRequestTypeDef",
    {
        "HostedZoneId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[str],
    },
)

ListQueryLoggingConfigsResponseTypeDef = TypedDict(
    "ListQueryLoggingConfigsResponseTypeDef",
    {
        "QueryLoggingConfigs": List["QueryLoggingConfigTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceRecordSetsRequestRequestTypeDef = TypedDict(
    "ListResourceRecordSetsRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "StartRecordName": NotRequired[str],
        "StartRecordType": NotRequired[RRTypeType],
        "StartRecordIdentifier": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListResourceRecordSetsResponseTypeDef = TypedDict(
    "ListResourceRecordSetsResponseTypeDef",
    {
        "ResourceRecordSets": List["ResourceRecordSetTypeDef"],
        "IsTruncated": bool,
        "NextRecordName": str,
        "NextRecordType": RRTypeType,
        "NextRecordIdentifier": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReusableDelegationSetsRequestRequestTypeDef = TypedDict(
    "ListReusableDelegationSetsRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListReusableDelegationSetsResponseTypeDef = TypedDict(
    "ListReusableDelegationSetsResponseTypeDef",
    {
        "DelegationSets": List["DelegationSetTypeDef"],
        "Marker": str,
        "IsTruncated": bool,
        "NextMarker": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceType": TagResourceTypeType,
        "ResourceId": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "ResourceTagSet": "ResourceTagSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourcesRequestRequestTypeDef = TypedDict(
    "ListTagsForResourcesRequestRequestTypeDef",
    {
        "ResourceType": TagResourceTypeType,
        "ResourceIds": Sequence[str],
    },
)

ListTagsForResourcesResponseTypeDef = TypedDict(
    "ListTagsForResourcesResponseTypeDef",
    {
        "ResourceTagSets": List["ResourceTagSetTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrafficPoliciesRequestRequestTypeDef = TypedDict(
    "ListTrafficPoliciesRequestRequestTypeDef",
    {
        "TrafficPolicyIdMarker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListTrafficPoliciesResponseTypeDef = TypedDict(
    "ListTrafficPoliciesResponseTypeDef",
    {
        "TrafficPolicySummaries": List["TrafficPolicySummaryTypeDef"],
        "IsTruncated": bool,
        "TrafficPolicyIdMarker": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrafficPolicyInstancesByHostedZoneRequestRequestTypeDef = TypedDict(
    "ListTrafficPolicyInstancesByHostedZoneRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "TrafficPolicyInstanceNameMarker": NotRequired[str],
        "TrafficPolicyInstanceTypeMarker": NotRequired[RRTypeType],
        "MaxItems": NotRequired[str],
    },
)

ListTrafficPolicyInstancesByHostedZoneResponseTypeDef = TypedDict(
    "ListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    {
        "TrafficPolicyInstances": List["TrafficPolicyInstanceTypeDef"],
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": RRTypeType,
        "IsTruncated": bool,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrafficPolicyInstancesByPolicyRequestRequestTypeDef = TypedDict(
    "ListTrafficPolicyInstancesByPolicyRequestRequestTypeDef",
    {
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "HostedZoneIdMarker": NotRequired[str],
        "TrafficPolicyInstanceNameMarker": NotRequired[str],
        "TrafficPolicyInstanceTypeMarker": NotRequired[RRTypeType],
        "MaxItems": NotRequired[str],
    },
)

ListTrafficPolicyInstancesByPolicyResponseTypeDef = TypedDict(
    "ListTrafficPolicyInstancesByPolicyResponseTypeDef",
    {
        "TrafficPolicyInstances": List["TrafficPolicyInstanceTypeDef"],
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": RRTypeType,
        "IsTruncated": bool,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrafficPolicyInstancesRequestRequestTypeDef = TypedDict(
    "ListTrafficPolicyInstancesRequestRequestTypeDef",
    {
        "HostedZoneIdMarker": NotRequired[str],
        "TrafficPolicyInstanceNameMarker": NotRequired[str],
        "TrafficPolicyInstanceTypeMarker": NotRequired[RRTypeType],
        "MaxItems": NotRequired[str],
    },
)

ListTrafficPolicyInstancesResponseTypeDef = TypedDict(
    "ListTrafficPolicyInstancesResponseTypeDef",
    {
        "TrafficPolicyInstances": List["TrafficPolicyInstanceTypeDef"],
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": RRTypeType,
        "IsTruncated": bool,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrafficPolicyVersionsRequestRequestTypeDef = TypedDict(
    "ListTrafficPolicyVersionsRequestRequestTypeDef",
    {
        "Id": str,
        "TrafficPolicyVersionMarker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)

ListTrafficPolicyVersionsResponseTypeDef = TypedDict(
    "ListTrafficPolicyVersionsResponseTypeDef",
    {
        "TrafficPolicies": List["TrafficPolicyTypeDef"],
        "IsTruncated": bool,
        "TrafficPolicyVersionMarker": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVPCAssociationAuthorizationsRequestRequestTypeDef = TypedDict(
    "ListVPCAssociationAuthorizationsRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[str],
    },
)

ListVPCAssociationAuthorizationsResponseTypeDef = TypedDict(
    "ListVPCAssociationAuthorizationsResponseTypeDef",
    {
        "HostedZoneId": str,
        "NextToken": str,
        "VPCs": List["VPCTypeDef"],
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

QueryLoggingConfigTypeDef = TypedDict(
    "QueryLoggingConfigTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "CloudWatchLogsLogGroupArn": str,
    },
)

ResourceRecordSetTypeDef = TypedDict(
    "ResourceRecordSetTypeDef",
    {
        "Name": str,
        "Type": RRTypeType,
        "SetIdentifier": NotRequired[str],
        "Weight": NotRequired[int],
        "Region": NotRequired[ResourceRecordSetRegionType],
        "GeoLocation": NotRequired["GeoLocationTypeDef"],
        "Failover": NotRequired[ResourceRecordSetFailoverType],
        "MultiValueAnswer": NotRequired[bool],
        "TTL": NotRequired[int],
        "ResourceRecords": NotRequired[Sequence["ResourceRecordTypeDef"]],
        "AliasTarget": NotRequired["AliasTargetTypeDef"],
        "HealthCheckId": NotRequired[str],
        "TrafficPolicyInstanceId": NotRequired[str],
    },
)

ResourceRecordTypeDef = TypedDict(
    "ResourceRecordTypeDef",
    {
        "Value": str,
    },
)

ResourceTagSetTypeDef = TypedDict(
    "ResourceTagSetTypeDef",
    {
        "ResourceType": NotRequired[TagResourceTypeType],
        "ResourceId": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
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

ReusableDelegationSetLimitTypeDef = TypedDict(
    "ReusableDelegationSetLimitTypeDef",
    {
        "Type": Literal["MAX_ZONES_BY_REUSABLE_DELEGATION_SET"],
        "Value": int,
    },
)

StatusReportTypeDef = TypedDict(
    "StatusReportTypeDef",
    {
        "Status": NotRequired[str],
        "CheckedTime": NotRequired[datetime],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

TestDNSAnswerRequestRequestTypeDef = TypedDict(
    "TestDNSAnswerRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "RecordName": str,
        "RecordType": RRTypeType,
        "ResolverIP": NotRequired[str],
        "EDNS0ClientSubnetIP": NotRequired[str],
        "EDNS0ClientSubnetMask": NotRequired[str],
    },
)

TestDNSAnswerResponseTypeDef = TypedDict(
    "TestDNSAnswerResponseTypeDef",
    {
        "Nameserver": str,
        "RecordName": str,
        "RecordType": RRTypeType,
        "RecordData": List[str],
        "ResponseCode": str,
        "Protocol": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TrafficPolicyInstanceTypeDef = TypedDict(
    "TrafficPolicyInstanceTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": RRTypeType,
    },
)

TrafficPolicySummaryTypeDef = TypedDict(
    "TrafficPolicySummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Type": RRTypeType,
        "LatestVersion": int,
        "TrafficPolicyCount": int,
    },
)

TrafficPolicyTypeDef = TypedDict(
    "TrafficPolicyTypeDef",
    {
        "Id": str,
        "Version": int,
        "Name": str,
        "Type": RRTypeType,
        "Document": str,
        "Comment": NotRequired[str],
    },
)

UpdateHealthCheckRequestRequestTypeDef = TypedDict(
    "UpdateHealthCheckRequestRequestTypeDef",
    {
        "HealthCheckId": str,
        "HealthCheckVersion": NotRequired[int],
        "IPAddress": NotRequired[str],
        "Port": NotRequired[int],
        "ResourcePath": NotRequired[str],
        "FullyQualifiedDomainName": NotRequired[str],
        "SearchString": NotRequired[str],
        "FailureThreshold": NotRequired[int],
        "Inverted": NotRequired[bool],
        "Disabled": NotRequired[bool],
        "HealthThreshold": NotRequired[int],
        "ChildHealthChecks": NotRequired[Sequence[str]],
        "EnableSNI": NotRequired[bool],
        "Regions": NotRequired[Sequence[HealthCheckRegionType]],
        "AlarmIdentifier": NotRequired["AlarmIdentifierTypeDef"],
        "InsufficientDataHealthStatus": NotRequired[InsufficientDataHealthStatusType],
        "ResetElements": NotRequired[Sequence[ResettableElementNameType]],
    },
)

UpdateHealthCheckResponseTypeDef = TypedDict(
    "UpdateHealthCheckResponseTypeDef",
    {
        "HealthCheck": "HealthCheckTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateHostedZoneCommentRequestRequestTypeDef = TypedDict(
    "UpdateHostedZoneCommentRequestRequestTypeDef",
    {
        "Id": str,
        "Comment": NotRequired[str],
    },
)

UpdateHostedZoneCommentResponseTypeDef = TypedDict(
    "UpdateHostedZoneCommentResponseTypeDef",
    {
        "HostedZone": "HostedZoneTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTrafficPolicyCommentRequestRequestTypeDef = TypedDict(
    "UpdateTrafficPolicyCommentRequestRequestTypeDef",
    {
        "Id": str,
        "Version": int,
        "Comment": str,
    },
)

UpdateTrafficPolicyCommentResponseTypeDef = TypedDict(
    "UpdateTrafficPolicyCommentResponseTypeDef",
    {
        "TrafficPolicy": "TrafficPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTrafficPolicyInstanceRequestRequestTypeDef = TypedDict(
    "UpdateTrafficPolicyInstanceRequestRequestTypeDef",
    {
        "Id": str,
        "TTL": int,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
    },
)

UpdateTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "UpdateTrafficPolicyInstanceResponseTypeDef",
    {
        "TrafficPolicyInstance": "TrafficPolicyInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VPCTypeDef = TypedDict(
    "VPCTypeDef",
    {
        "VPCRegion": NotRequired[VPCRegionType],
        "VPCId": NotRequired[str],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
