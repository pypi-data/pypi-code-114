"""
Type annotations for elb service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_elb/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_elb.type_defs import AccessLogTypeDef

    data: AccessLogTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessLogTypeDef",
    "AddAvailabilityZonesInputRequestTypeDef",
    "AddAvailabilityZonesOutputTypeDef",
    "AddTagsInputRequestTypeDef",
    "AdditionalAttributeTypeDef",
    "AppCookieStickinessPolicyTypeDef",
    "ApplySecurityGroupsToLoadBalancerInputRequestTypeDef",
    "ApplySecurityGroupsToLoadBalancerOutputTypeDef",
    "AttachLoadBalancerToSubnetsInputRequestTypeDef",
    "AttachLoadBalancerToSubnetsOutputTypeDef",
    "BackendServerDescriptionTypeDef",
    "ConfigureHealthCheckInputRequestTypeDef",
    "ConfigureHealthCheckOutputTypeDef",
    "ConnectionDrainingTypeDef",
    "ConnectionSettingsTypeDef",
    "CreateAccessPointInputRequestTypeDef",
    "CreateAccessPointOutputTypeDef",
    "CreateAppCookieStickinessPolicyInputRequestTypeDef",
    "CreateLBCookieStickinessPolicyInputRequestTypeDef",
    "CreateLoadBalancerListenerInputRequestTypeDef",
    "CreateLoadBalancerPolicyInputRequestTypeDef",
    "CrossZoneLoadBalancingTypeDef",
    "DeleteAccessPointInputRequestTypeDef",
    "DeleteLoadBalancerListenerInputRequestTypeDef",
    "DeleteLoadBalancerPolicyInputRequestTypeDef",
    "DeregisterEndPointsInputRequestTypeDef",
    "DeregisterEndPointsOutputTypeDef",
    "DescribeAccessPointsInputRequestTypeDef",
    "DescribeAccessPointsOutputTypeDef",
    "DescribeAccountLimitsInputRequestTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "DescribeEndPointStateInputRequestTypeDef",
    "DescribeEndPointStateOutputTypeDef",
    "DescribeLoadBalancerAttributesInputRequestTypeDef",
    "DescribeLoadBalancerAttributesOutputTypeDef",
    "DescribeLoadBalancerPoliciesInputRequestTypeDef",
    "DescribeLoadBalancerPoliciesOutputTypeDef",
    "DescribeLoadBalancerPolicyTypesInputRequestTypeDef",
    "DescribeLoadBalancerPolicyTypesOutputTypeDef",
    "DescribeTagsInputRequestTypeDef",
    "DescribeTagsOutputTypeDef",
    "DetachLoadBalancerFromSubnetsInputRequestTypeDef",
    "DetachLoadBalancerFromSubnetsOutputTypeDef",
    "HealthCheckTypeDef",
    "InstanceStateTypeDef",
    "InstanceTypeDef",
    "LBCookieStickinessPolicyTypeDef",
    "LimitTypeDef",
    "ListenerDescriptionTypeDef",
    "ListenerTypeDef",
    "LoadBalancerAttributesTypeDef",
    "LoadBalancerDescriptionTypeDef",
    "ModifyLoadBalancerAttributesInputRequestTypeDef",
    "ModifyLoadBalancerAttributesOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PoliciesTypeDef",
    "PolicyAttributeDescriptionTypeDef",
    "PolicyAttributeTypeDef",
    "PolicyAttributeTypeDescriptionTypeDef",
    "PolicyDescriptionTypeDef",
    "PolicyTypeDescriptionTypeDef",
    "RegisterEndPointsInputRequestTypeDef",
    "RegisterEndPointsOutputTypeDef",
    "RemoveAvailabilityZonesInputRequestTypeDef",
    "RemoveAvailabilityZonesOutputTypeDef",
    "RemoveTagsInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SetLoadBalancerListenerSSLCertificateInputRequestTypeDef",
    "SetLoadBalancerPoliciesForBackendServerInputRequestTypeDef",
    "SetLoadBalancerPoliciesOfListenerInputRequestTypeDef",
    "SourceSecurityGroupTypeDef",
    "TagDescriptionTypeDef",
    "TagKeyOnlyTypeDef",
    "TagTypeDef",
    "WaiterConfigTypeDef",
)

AccessLogTypeDef = TypedDict(
    "AccessLogTypeDef",
    {
        "Enabled": bool,
        "S3BucketName": NotRequired[str],
        "EmitInterval": NotRequired[int],
        "S3BucketPrefix": NotRequired[str],
    },
)

AddAvailabilityZonesInputRequestTypeDef = TypedDict(
    "AddAvailabilityZonesInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "AvailabilityZones": Sequence[str],
    },
)

AddAvailabilityZonesOutputTypeDef = TypedDict(
    "AddAvailabilityZonesOutputTypeDef",
    {
        "AvailabilityZones": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsInputRequestTypeDef = TypedDict(
    "AddTagsInputRequestTypeDef",
    {
        "LoadBalancerNames": Sequence[str],
        "Tags": Sequence["TagTypeDef"],
    },
)

AdditionalAttributeTypeDef = TypedDict(
    "AdditionalAttributeTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

AppCookieStickinessPolicyTypeDef = TypedDict(
    "AppCookieStickinessPolicyTypeDef",
    {
        "PolicyName": NotRequired[str],
        "CookieName": NotRequired[str],
    },
)

ApplySecurityGroupsToLoadBalancerInputRequestTypeDef = TypedDict(
    "ApplySecurityGroupsToLoadBalancerInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "SecurityGroups": Sequence[str],
    },
)

ApplySecurityGroupsToLoadBalancerOutputTypeDef = TypedDict(
    "ApplySecurityGroupsToLoadBalancerOutputTypeDef",
    {
        "SecurityGroups": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachLoadBalancerToSubnetsInputRequestTypeDef = TypedDict(
    "AttachLoadBalancerToSubnetsInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "Subnets": Sequence[str],
    },
)

AttachLoadBalancerToSubnetsOutputTypeDef = TypedDict(
    "AttachLoadBalancerToSubnetsOutputTypeDef",
    {
        "Subnets": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BackendServerDescriptionTypeDef = TypedDict(
    "BackendServerDescriptionTypeDef",
    {
        "InstancePort": NotRequired[int],
        "PolicyNames": NotRequired[List[str]],
    },
)

ConfigureHealthCheckInputRequestTypeDef = TypedDict(
    "ConfigureHealthCheckInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "HealthCheck": "HealthCheckTypeDef",
    },
)

ConfigureHealthCheckOutputTypeDef = TypedDict(
    "ConfigureHealthCheckOutputTypeDef",
    {
        "HealthCheck": "HealthCheckTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConnectionDrainingTypeDef = TypedDict(
    "ConnectionDrainingTypeDef",
    {
        "Enabled": bool,
        "Timeout": NotRequired[int],
    },
)

ConnectionSettingsTypeDef = TypedDict(
    "ConnectionSettingsTypeDef",
    {
        "IdleTimeout": int,
    },
)

CreateAccessPointInputRequestTypeDef = TypedDict(
    "CreateAccessPointInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "Listeners": Sequence["ListenerTypeDef"],
        "AvailabilityZones": NotRequired[Sequence[str]],
        "Subnets": NotRequired[Sequence[str]],
        "SecurityGroups": NotRequired[Sequence[str]],
        "Scheme": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateAccessPointOutputTypeDef = TypedDict(
    "CreateAccessPointOutputTypeDef",
    {
        "DNSName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAppCookieStickinessPolicyInputRequestTypeDef = TypedDict(
    "CreateAppCookieStickinessPolicyInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "PolicyName": str,
        "CookieName": str,
    },
)

CreateLBCookieStickinessPolicyInputRequestTypeDef = TypedDict(
    "CreateLBCookieStickinessPolicyInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "PolicyName": str,
        "CookieExpirationPeriod": NotRequired[int],
    },
)

CreateLoadBalancerListenerInputRequestTypeDef = TypedDict(
    "CreateLoadBalancerListenerInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "Listeners": Sequence["ListenerTypeDef"],
    },
)

CreateLoadBalancerPolicyInputRequestTypeDef = TypedDict(
    "CreateLoadBalancerPolicyInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "PolicyName": str,
        "PolicyTypeName": str,
        "PolicyAttributes": NotRequired[Sequence["PolicyAttributeTypeDef"]],
    },
)

CrossZoneLoadBalancingTypeDef = TypedDict(
    "CrossZoneLoadBalancingTypeDef",
    {
        "Enabled": bool,
    },
)

DeleteAccessPointInputRequestTypeDef = TypedDict(
    "DeleteAccessPointInputRequestTypeDef",
    {
        "LoadBalancerName": str,
    },
)

DeleteLoadBalancerListenerInputRequestTypeDef = TypedDict(
    "DeleteLoadBalancerListenerInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerPorts": Sequence[int],
    },
)

DeleteLoadBalancerPolicyInputRequestTypeDef = TypedDict(
    "DeleteLoadBalancerPolicyInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "PolicyName": str,
    },
)

DeregisterEndPointsInputRequestTypeDef = TypedDict(
    "DeregisterEndPointsInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "Instances": Sequence["InstanceTypeDef"],
    },
)

DeregisterEndPointsOutputTypeDef = TypedDict(
    "DeregisterEndPointsOutputTypeDef",
    {
        "Instances": List["InstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccessPointsInputRequestTypeDef = TypedDict(
    "DescribeAccessPointsInputRequestTypeDef",
    {
        "LoadBalancerNames": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

DescribeAccessPointsOutputTypeDef = TypedDict(
    "DescribeAccessPointsOutputTypeDef",
    {
        "LoadBalancerDescriptions": List["LoadBalancerDescriptionTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountLimitsInputRequestTypeDef = TypedDict(
    "DescribeAccountLimitsInputRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

DescribeAccountLimitsOutputTypeDef = TypedDict(
    "DescribeAccountLimitsOutputTypeDef",
    {
        "Limits": List["LimitTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndPointStateInputRequestTypeDef = TypedDict(
    "DescribeEndPointStateInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "Instances": NotRequired[Sequence["InstanceTypeDef"]],
    },
)

DescribeEndPointStateOutputTypeDef = TypedDict(
    "DescribeEndPointStateOutputTypeDef",
    {
        "InstanceStates": List["InstanceStateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancerAttributesInputRequestTypeDef = TypedDict(
    "DescribeLoadBalancerAttributesInputRequestTypeDef",
    {
        "LoadBalancerName": str,
    },
)

DescribeLoadBalancerAttributesOutputTypeDef = TypedDict(
    "DescribeLoadBalancerAttributesOutputTypeDef",
    {
        "LoadBalancerAttributes": "LoadBalancerAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancerPoliciesInputRequestTypeDef = TypedDict(
    "DescribeLoadBalancerPoliciesInputRequestTypeDef",
    {
        "LoadBalancerName": NotRequired[str],
        "PolicyNames": NotRequired[Sequence[str]],
    },
)

DescribeLoadBalancerPoliciesOutputTypeDef = TypedDict(
    "DescribeLoadBalancerPoliciesOutputTypeDef",
    {
        "PolicyDescriptions": List["PolicyDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancerPolicyTypesInputRequestTypeDef = TypedDict(
    "DescribeLoadBalancerPolicyTypesInputRequestTypeDef",
    {
        "PolicyTypeNames": NotRequired[Sequence[str]],
    },
)

DescribeLoadBalancerPolicyTypesOutputTypeDef = TypedDict(
    "DescribeLoadBalancerPolicyTypesOutputTypeDef",
    {
        "PolicyTypeDescriptions": List["PolicyTypeDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagsInputRequestTypeDef = TypedDict(
    "DescribeTagsInputRequestTypeDef",
    {
        "LoadBalancerNames": Sequence[str],
    },
)

DescribeTagsOutputTypeDef = TypedDict(
    "DescribeTagsOutputTypeDef",
    {
        "TagDescriptions": List["TagDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachLoadBalancerFromSubnetsInputRequestTypeDef = TypedDict(
    "DetachLoadBalancerFromSubnetsInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "Subnets": Sequence[str],
    },
)

DetachLoadBalancerFromSubnetsOutputTypeDef = TypedDict(
    "DetachLoadBalancerFromSubnetsOutputTypeDef",
    {
        "Subnets": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HealthCheckTypeDef = TypedDict(
    "HealthCheckTypeDef",
    {
        "Target": str,
        "Interval": int,
        "Timeout": int,
        "UnhealthyThreshold": int,
        "HealthyThreshold": int,
    },
)

InstanceStateTypeDef = TypedDict(
    "InstanceStateTypeDef",
    {
        "InstanceId": NotRequired[str],
        "State": NotRequired[str],
        "ReasonCode": NotRequired[str],
        "Description": NotRequired[str],
    },
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "InstanceId": NotRequired[str],
    },
)

LBCookieStickinessPolicyTypeDef = TypedDict(
    "LBCookieStickinessPolicyTypeDef",
    {
        "PolicyName": NotRequired[str],
        "CookieExpirationPeriod": NotRequired[int],
    },
)

LimitTypeDef = TypedDict(
    "LimitTypeDef",
    {
        "Name": NotRequired[str],
        "Max": NotRequired[str],
    },
)

ListenerDescriptionTypeDef = TypedDict(
    "ListenerDescriptionTypeDef",
    {
        "Listener": NotRequired["ListenerTypeDef"],
        "PolicyNames": NotRequired[List[str]],
    },
)

ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "Protocol": str,
        "LoadBalancerPort": int,
        "InstancePort": int,
        "InstanceProtocol": NotRequired[str],
        "SSLCertificateId": NotRequired[str],
    },
)

LoadBalancerAttributesTypeDef = TypedDict(
    "LoadBalancerAttributesTypeDef",
    {
        "CrossZoneLoadBalancing": NotRequired["CrossZoneLoadBalancingTypeDef"],
        "AccessLog": NotRequired["AccessLogTypeDef"],
        "ConnectionDraining": NotRequired["ConnectionDrainingTypeDef"],
        "ConnectionSettings": NotRequired["ConnectionSettingsTypeDef"],
        "AdditionalAttributes": NotRequired[List["AdditionalAttributeTypeDef"]],
    },
)

LoadBalancerDescriptionTypeDef = TypedDict(
    "LoadBalancerDescriptionTypeDef",
    {
        "LoadBalancerName": NotRequired[str],
        "DNSName": NotRequired[str],
        "CanonicalHostedZoneName": NotRequired[str],
        "CanonicalHostedZoneNameID": NotRequired[str],
        "ListenerDescriptions": NotRequired[List["ListenerDescriptionTypeDef"]],
        "Policies": NotRequired["PoliciesTypeDef"],
        "BackendServerDescriptions": NotRequired[List["BackendServerDescriptionTypeDef"]],
        "AvailabilityZones": NotRequired[List[str]],
        "Subnets": NotRequired[List[str]],
        "VPCId": NotRequired[str],
        "Instances": NotRequired[List["InstanceTypeDef"]],
        "HealthCheck": NotRequired["HealthCheckTypeDef"],
        "SourceSecurityGroup": NotRequired["SourceSecurityGroupTypeDef"],
        "SecurityGroups": NotRequired[List[str]],
        "CreatedTime": NotRequired[datetime],
        "Scheme": NotRequired[str],
    },
)

ModifyLoadBalancerAttributesInputRequestTypeDef = TypedDict(
    "ModifyLoadBalancerAttributesInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerAttributes": "LoadBalancerAttributesTypeDef",
    },
)

ModifyLoadBalancerAttributesOutputTypeDef = TypedDict(
    "ModifyLoadBalancerAttributesOutputTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerAttributes": "LoadBalancerAttributesTypeDef",
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

PoliciesTypeDef = TypedDict(
    "PoliciesTypeDef",
    {
        "AppCookieStickinessPolicies": NotRequired[List["AppCookieStickinessPolicyTypeDef"]],
        "LBCookieStickinessPolicies": NotRequired[List["LBCookieStickinessPolicyTypeDef"]],
        "OtherPolicies": NotRequired[List[str]],
    },
)

PolicyAttributeDescriptionTypeDef = TypedDict(
    "PolicyAttributeDescriptionTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeValue": NotRequired[str],
    },
)

PolicyAttributeTypeDef = TypedDict(
    "PolicyAttributeTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeValue": NotRequired[str],
    },
)

PolicyAttributeTypeDescriptionTypeDef = TypedDict(
    "PolicyAttributeTypeDescriptionTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeType": NotRequired[str],
        "Description": NotRequired[str],
        "DefaultValue": NotRequired[str],
        "Cardinality": NotRequired[str],
    },
)

PolicyDescriptionTypeDef = TypedDict(
    "PolicyDescriptionTypeDef",
    {
        "PolicyName": NotRequired[str],
        "PolicyTypeName": NotRequired[str],
        "PolicyAttributeDescriptions": NotRequired[List["PolicyAttributeDescriptionTypeDef"]],
    },
)

PolicyTypeDescriptionTypeDef = TypedDict(
    "PolicyTypeDescriptionTypeDef",
    {
        "PolicyTypeName": NotRequired[str],
        "Description": NotRequired[str],
        "PolicyAttributeTypeDescriptions": NotRequired[
            List["PolicyAttributeTypeDescriptionTypeDef"]
        ],
    },
)

RegisterEndPointsInputRequestTypeDef = TypedDict(
    "RegisterEndPointsInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "Instances": Sequence["InstanceTypeDef"],
    },
)

RegisterEndPointsOutputTypeDef = TypedDict(
    "RegisterEndPointsOutputTypeDef",
    {
        "Instances": List["InstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveAvailabilityZonesInputRequestTypeDef = TypedDict(
    "RemoveAvailabilityZonesInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "AvailabilityZones": Sequence[str],
    },
)

RemoveAvailabilityZonesOutputTypeDef = TypedDict(
    "RemoveAvailabilityZonesOutputTypeDef",
    {
        "AvailabilityZones": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTagsInputRequestTypeDef = TypedDict(
    "RemoveTagsInputRequestTypeDef",
    {
        "LoadBalancerNames": Sequence[str],
        "Tags": Sequence["TagKeyOnlyTypeDef"],
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

SetLoadBalancerListenerSSLCertificateInputRequestTypeDef = TypedDict(
    "SetLoadBalancerListenerSSLCertificateInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerPort": int,
        "SSLCertificateId": str,
    },
)

SetLoadBalancerPoliciesForBackendServerInputRequestTypeDef = TypedDict(
    "SetLoadBalancerPoliciesForBackendServerInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "InstancePort": int,
        "PolicyNames": Sequence[str],
    },
)

SetLoadBalancerPoliciesOfListenerInputRequestTypeDef = TypedDict(
    "SetLoadBalancerPoliciesOfListenerInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerPort": int,
        "PolicyNames": Sequence[str],
    },
)

SourceSecurityGroupTypeDef = TypedDict(
    "SourceSecurityGroupTypeDef",
    {
        "OwnerAlias": NotRequired[str],
        "GroupName": NotRequired[str],
    },
)

TagDescriptionTypeDef = TypedDict(
    "TagDescriptionTypeDef",
    {
        "LoadBalancerName": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

TagKeyOnlyTypeDef = TypedDict(
    "TagKeyOnlyTypeDef",
    {
        "Key": NotRequired[str],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
