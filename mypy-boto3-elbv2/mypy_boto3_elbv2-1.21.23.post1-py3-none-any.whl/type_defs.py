"""
Type annotations for elbv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_elbv2.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    ActionTypeEnumType,
    AuthenticateCognitoActionConditionalBehaviorEnumType,
    AuthenticateOidcActionConditionalBehaviorEnumType,
    IpAddressTypeType,
    LoadBalancerSchemeEnumType,
    LoadBalancerStateEnumType,
    LoadBalancerTypeEnumType,
    ProtocolEnumType,
    RedirectActionStatusCodeEnumType,
    TargetGroupIpAddressTypeEnumType,
    TargetHealthReasonEnumType,
    TargetHealthStateEnumType,
    TargetTypeEnumType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionTypeDef",
    "AddListenerCertificatesInputRequestTypeDef",
    "AddListenerCertificatesOutputTypeDef",
    "AddTagsInputRequestTypeDef",
    "AuthenticateCognitoActionConfigTypeDef",
    "AuthenticateOidcActionConfigTypeDef",
    "AvailabilityZoneTypeDef",
    "CertificateTypeDef",
    "CipherTypeDef",
    "CreateListenerInputRequestTypeDef",
    "CreateListenerOutputTypeDef",
    "CreateLoadBalancerInputRequestTypeDef",
    "CreateLoadBalancerOutputTypeDef",
    "CreateRuleInputRequestTypeDef",
    "CreateRuleOutputTypeDef",
    "CreateTargetGroupInputRequestTypeDef",
    "CreateTargetGroupOutputTypeDef",
    "DeleteListenerInputRequestTypeDef",
    "DeleteLoadBalancerInputRequestTypeDef",
    "DeleteRuleInputRequestTypeDef",
    "DeleteTargetGroupInputRequestTypeDef",
    "DeregisterTargetsInputRequestTypeDef",
    "DescribeAccountLimitsInputRequestTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "DescribeListenerCertificatesInputRequestTypeDef",
    "DescribeListenerCertificatesOutputTypeDef",
    "DescribeListenersInputRequestTypeDef",
    "DescribeListenersOutputTypeDef",
    "DescribeLoadBalancerAttributesInputRequestTypeDef",
    "DescribeLoadBalancerAttributesOutputTypeDef",
    "DescribeLoadBalancersInputRequestTypeDef",
    "DescribeLoadBalancersOutputTypeDef",
    "DescribeRulesInputRequestTypeDef",
    "DescribeRulesOutputTypeDef",
    "DescribeSSLPoliciesInputRequestTypeDef",
    "DescribeSSLPoliciesOutputTypeDef",
    "DescribeTagsInputRequestTypeDef",
    "DescribeTagsOutputTypeDef",
    "DescribeTargetGroupAttributesInputRequestTypeDef",
    "DescribeTargetGroupAttributesOutputTypeDef",
    "DescribeTargetGroupsInputRequestTypeDef",
    "DescribeTargetGroupsOutputTypeDef",
    "DescribeTargetHealthInputRequestTypeDef",
    "DescribeTargetHealthOutputTypeDef",
    "FixedResponseActionConfigTypeDef",
    "ForwardActionConfigTypeDef",
    "HostHeaderConditionConfigTypeDef",
    "HttpHeaderConditionConfigTypeDef",
    "HttpRequestMethodConditionConfigTypeDef",
    "LimitTypeDef",
    "ListenerTypeDef",
    "LoadBalancerAddressTypeDef",
    "LoadBalancerAttributeTypeDef",
    "LoadBalancerStateTypeDef",
    "LoadBalancerTypeDef",
    "MatcherTypeDef",
    "ModifyListenerInputRequestTypeDef",
    "ModifyListenerOutputTypeDef",
    "ModifyLoadBalancerAttributesInputRequestTypeDef",
    "ModifyLoadBalancerAttributesOutputTypeDef",
    "ModifyRuleInputRequestTypeDef",
    "ModifyRuleOutputTypeDef",
    "ModifyTargetGroupAttributesInputRequestTypeDef",
    "ModifyTargetGroupAttributesOutputTypeDef",
    "ModifyTargetGroupInputRequestTypeDef",
    "ModifyTargetGroupOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PathPatternConditionConfigTypeDef",
    "QueryStringConditionConfigTypeDef",
    "QueryStringKeyValuePairTypeDef",
    "RedirectActionConfigTypeDef",
    "RegisterTargetsInputRequestTypeDef",
    "RemoveListenerCertificatesInputRequestTypeDef",
    "RemoveTagsInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RuleConditionTypeDef",
    "RulePriorityPairTypeDef",
    "RuleTypeDef",
    "SetIpAddressTypeInputRequestTypeDef",
    "SetIpAddressTypeOutputTypeDef",
    "SetRulePrioritiesInputRequestTypeDef",
    "SetRulePrioritiesOutputTypeDef",
    "SetSecurityGroupsInputRequestTypeDef",
    "SetSecurityGroupsOutputTypeDef",
    "SetSubnetsInputRequestTypeDef",
    "SetSubnetsOutputTypeDef",
    "SourceIpConditionConfigTypeDef",
    "SslPolicyTypeDef",
    "SubnetMappingTypeDef",
    "TagDescriptionTypeDef",
    "TagTypeDef",
    "TargetDescriptionTypeDef",
    "TargetGroupAttributeTypeDef",
    "TargetGroupStickinessConfigTypeDef",
    "TargetGroupTupleTypeDef",
    "TargetGroupTypeDef",
    "TargetHealthDescriptionTypeDef",
    "TargetHealthTypeDef",
    "WaiterConfigTypeDef",
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "Type": ActionTypeEnumType,
        "TargetGroupArn": NotRequired[str],
        "AuthenticateOidcConfig": NotRequired["AuthenticateOidcActionConfigTypeDef"],
        "AuthenticateCognitoConfig": NotRequired["AuthenticateCognitoActionConfigTypeDef"],
        "Order": NotRequired[int],
        "RedirectConfig": NotRequired["RedirectActionConfigTypeDef"],
        "FixedResponseConfig": NotRequired["FixedResponseActionConfigTypeDef"],
        "ForwardConfig": NotRequired["ForwardActionConfigTypeDef"],
    },
)

AddListenerCertificatesInputRequestTypeDef = TypedDict(
    "AddListenerCertificatesInputRequestTypeDef",
    {
        "ListenerArn": str,
        "Certificates": Sequence["CertificateTypeDef"],
    },
)

AddListenerCertificatesOutputTypeDef = TypedDict(
    "AddListenerCertificatesOutputTypeDef",
    {
        "Certificates": List["CertificateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsInputRequestTypeDef = TypedDict(
    "AddTagsInputRequestTypeDef",
    {
        "ResourceArns": Sequence[str],
        "Tags": Sequence["TagTypeDef"],
    },
)

AuthenticateCognitoActionConfigTypeDef = TypedDict(
    "AuthenticateCognitoActionConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": NotRequired[str],
        "Scope": NotRequired[str],
        "SessionTimeout": NotRequired[int],
        "AuthenticationRequestExtraParams": NotRequired[Mapping[str, str]],
        "OnUnauthenticatedRequest": NotRequired[
            AuthenticateCognitoActionConditionalBehaviorEnumType
        ],
    },
)

AuthenticateOidcActionConfigTypeDef = TypedDict(
    "AuthenticateOidcActionConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": NotRequired[str],
        "SessionCookieName": NotRequired[str],
        "Scope": NotRequired[str],
        "SessionTimeout": NotRequired[int],
        "AuthenticationRequestExtraParams": NotRequired[Mapping[str, str]],
        "OnUnauthenticatedRequest": NotRequired[AuthenticateOidcActionConditionalBehaviorEnumType],
        "UseExistingClientSecret": NotRequired[bool],
    },
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "ZoneName": NotRequired[str],
        "SubnetId": NotRequired[str],
        "OutpostId": NotRequired[str],
        "LoadBalancerAddresses": NotRequired[List["LoadBalancerAddressTypeDef"]],
    },
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateArn": NotRequired[str],
        "IsDefault": NotRequired[bool],
    },
)

CipherTypeDef = TypedDict(
    "CipherTypeDef",
    {
        "Name": NotRequired[str],
        "Priority": NotRequired[int],
    },
)

CreateListenerInputRequestTypeDef = TypedDict(
    "CreateListenerInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "DefaultActions": Sequence["ActionTypeDef"],
        "Protocol": NotRequired[ProtocolEnumType],
        "Port": NotRequired[int],
        "SslPolicy": NotRequired[str],
        "Certificates": NotRequired[Sequence["CertificateTypeDef"]],
        "AlpnPolicy": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateListenerOutputTypeDef = TypedDict(
    "CreateListenerOutputTypeDef",
    {
        "Listeners": List["ListenerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLoadBalancerInputRequestTypeDef = TypedDict(
    "CreateLoadBalancerInputRequestTypeDef",
    {
        "Name": str,
        "Subnets": NotRequired[Sequence[str]],
        "SubnetMappings": NotRequired[Sequence["SubnetMappingTypeDef"]],
        "SecurityGroups": NotRequired[Sequence[str]],
        "Scheme": NotRequired[LoadBalancerSchemeEnumType],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "Type": NotRequired[LoadBalancerTypeEnumType],
        "IpAddressType": NotRequired[IpAddressTypeType],
        "CustomerOwnedIpv4Pool": NotRequired[str],
    },
)

CreateLoadBalancerOutputTypeDef = TypedDict(
    "CreateLoadBalancerOutputTypeDef",
    {
        "LoadBalancers": List["LoadBalancerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRuleInputRequestTypeDef = TypedDict(
    "CreateRuleInputRequestTypeDef",
    {
        "ListenerArn": str,
        "Conditions": Sequence["RuleConditionTypeDef"],
        "Priority": int,
        "Actions": Sequence["ActionTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateRuleOutputTypeDef = TypedDict(
    "CreateRuleOutputTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTargetGroupInputRequestTypeDef = TypedDict(
    "CreateTargetGroupInputRequestTypeDef",
    {
        "Name": str,
        "Protocol": NotRequired[ProtocolEnumType],
        "ProtocolVersion": NotRequired[str],
        "Port": NotRequired[int],
        "VpcId": NotRequired[str],
        "HealthCheckProtocol": NotRequired[ProtocolEnumType],
        "HealthCheckPort": NotRequired[str],
        "HealthCheckEnabled": NotRequired[bool],
        "HealthCheckPath": NotRequired[str],
        "HealthCheckIntervalSeconds": NotRequired[int],
        "HealthCheckTimeoutSeconds": NotRequired[int],
        "HealthyThresholdCount": NotRequired[int],
        "UnhealthyThresholdCount": NotRequired[int],
        "Matcher": NotRequired["MatcherTypeDef"],
        "TargetType": NotRequired[TargetTypeEnumType],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "IpAddressType": NotRequired[TargetGroupIpAddressTypeEnumType],
    },
)

CreateTargetGroupOutputTypeDef = TypedDict(
    "CreateTargetGroupOutputTypeDef",
    {
        "TargetGroups": List["TargetGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteListenerInputRequestTypeDef = TypedDict(
    "DeleteListenerInputRequestTypeDef",
    {
        "ListenerArn": str,
    },
)

DeleteLoadBalancerInputRequestTypeDef = TypedDict(
    "DeleteLoadBalancerInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
    },
)

DeleteRuleInputRequestTypeDef = TypedDict(
    "DeleteRuleInputRequestTypeDef",
    {
        "RuleArn": str,
    },
)

DeleteTargetGroupInputRequestTypeDef = TypedDict(
    "DeleteTargetGroupInputRequestTypeDef",
    {
        "TargetGroupArn": str,
    },
)

DeregisterTargetsInputRequestTypeDef = TypedDict(
    "DeregisterTargetsInputRequestTypeDef",
    {
        "TargetGroupArn": str,
        "Targets": Sequence["TargetDescriptionTypeDef"],
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

DescribeListenerCertificatesInputRequestTypeDef = TypedDict(
    "DescribeListenerCertificatesInputRequestTypeDef",
    {
        "ListenerArn": str,
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

DescribeListenerCertificatesOutputTypeDef = TypedDict(
    "DescribeListenerCertificatesOutputTypeDef",
    {
        "Certificates": List["CertificateTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeListenersInputRequestTypeDef = TypedDict(
    "DescribeListenersInputRequestTypeDef",
    {
        "LoadBalancerArn": NotRequired[str],
        "ListenerArns": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

DescribeListenersOutputTypeDef = TypedDict(
    "DescribeListenersOutputTypeDef",
    {
        "Listeners": List["ListenerTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancerAttributesInputRequestTypeDef = TypedDict(
    "DescribeLoadBalancerAttributesInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
    },
)

DescribeLoadBalancerAttributesOutputTypeDef = TypedDict(
    "DescribeLoadBalancerAttributesOutputTypeDef",
    {
        "Attributes": List["LoadBalancerAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancersInputRequestTypeDef = TypedDict(
    "DescribeLoadBalancersInputRequestTypeDef",
    {
        "LoadBalancerArns": NotRequired[Sequence[str]],
        "Names": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

DescribeLoadBalancersOutputTypeDef = TypedDict(
    "DescribeLoadBalancersOutputTypeDef",
    {
        "LoadBalancers": List["LoadBalancerTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRulesInputRequestTypeDef = TypedDict(
    "DescribeRulesInputRequestTypeDef",
    {
        "ListenerArn": NotRequired[str],
        "RuleArns": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

DescribeRulesOutputTypeDef = TypedDict(
    "DescribeRulesOutputTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSSLPoliciesInputRequestTypeDef = TypedDict(
    "DescribeSSLPoliciesInputRequestTypeDef",
    {
        "Names": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
        "LoadBalancerType": NotRequired[LoadBalancerTypeEnumType],
    },
)

DescribeSSLPoliciesOutputTypeDef = TypedDict(
    "DescribeSSLPoliciesOutputTypeDef",
    {
        "SslPolicies": List["SslPolicyTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagsInputRequestTypeDef = TypedDict(
    "DescribeTagsInputRequestTypeDef",
    {
        "ResourceArns": Sequence[str],
    },
)

DescribeTagsOutputTypeDef = TypedDict(
    "DescribeTagsOutputTypeDef",
    {
        "TagDescriptions": List["TagDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTargetGroupAttributesInputRequestTypeDef = TypedDict(
    "DescribeTargetGroupAttributesInputRequestTypeDef",
    {
        "TargetGroupArn": str,
    },
)

DescribeTargetGroupAttributesOutputTypeDef = TypedDict(
    "DescribeTargetGroupAttributesOutputTypeDef",
    {
        "Attributes": List["TargetGroupAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTargetGroupsInputRequestTypeDef = TypedDict(
    "DescribeTargetGroupsInputRequestTypeDef",
    {
        "LoadBalancerArn": NotRequired[str],
        "TargetGroupArns": NotRequired[Sequence[str]],
        "Names": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

DescribeTargetGroupsOutputTypeDef = TypedDict(
    "DescribeTargetGroupsOutputTypeDef",
    {
        "TargetGroups": List["TargetGroupTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTargetHealthInputRequestTypeDef = TypedDict(
    "DescribeTargetHealthInputRequestTypeDef",
    {
        "TargetGroupArn": str,
        "Targets": NotRequired[Sequence["TargetDescriptionTypeDef"]],
    },
)

DescribeTargetHealthOutputTypeDef = TypedDict(
    "DescribeTargetHealthOutputTypeDef",
    {
        "TargetHealthDescriptions": List["TargetHealthDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FixedResponseActionConfigTypeDef = TypedDict(
    "FixedResponseActionConfigTypeDef",
    {
        "StatusCode": str,
        "MessageBody": NotRequired[str],
        "ContentType": NotRequired[str],
    },
)

ForwardActionConfigTypeDef = TypedDict(
    "ForwardActionConfigTypeDef",
    {
        "TargetGroups": NotRequired[Sequence["TargetGroupTupleTypeDef"]],
        "TargetGroupStickinessConfig": NotRequired["TargetGroupStickinessConfigTypeDef"],
    },
)

HostHeaderConditionConfigTypeDef = TypedDict(
    "HostHeaderConditionConfigTypeDef",
    {
        "Values": NotRequired[Sequence[str]],
    },
)

HttpHeaderConditionConfigTypeDef = TypedDict(
    "HttpHeaderConditionConfigTypeDef",
    {
        "HttpHeaderName": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)

HttpRequestMethodConditionConfigTypeDef = TypedDict(
    "HttpRequestMethodConditionConfigTypeDef",
    {
        "Values": NotRequired[Sequence[str]],
    },
)

LimitTypeDef = TypedDict(
    "LimitTypeDef",
    {
        "Name": NotRequired[str],
        "Max": NotRequired[str],
    },
)

ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "ListenerArn": NotRequired[str],
        "LoadBalancerArn": NotRequired[str],
        "Port": NotRequired[int],
        "Protocol": NotRequired[ProtocolEnumType],
        "Certificates": NotRequired[List["CertificateTypeDef"]],
        "SslPolicy": NotRequired[str],
        "DefaultActions": NotRequired[List["ActionTypeDef"]],
        "AlpnPolicy": NotRequired[List[str]],
    },
)

LoadBalancerAddressTypeDef = TypedDict(
    "LoadBalancerAddressTypeDef",
    {
        "IpAddress": NotRequired[str],
        "AllocationId": NotRequired[str],
        "PrivateIPv4Address": NotRequired[str],
        "IPv6Address": NotRequired[str],
    },
)

LoadBalancerAttributeTypeDef = TypedDict(
    "LoadBalancerAttributeTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

LoadBalancerStateTypeDef = TypedDict(
    "LoadBalancerStateTypeDef",
    {
        "Code": NotRequired[LoadBalancerStateEnumType],
        "Reason": NotRequired[str],
    },
)

LoadBalancerTypeDef = TypedDict(
    "LoadBalancerTypeDef",
    {
        "LoadBalancerArn": NotRequired[str],
        "DNSName": NotRequired[str],
        "CanonicalHostedZoneId": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LoadBalancerName": NotRequired[str],
        "Scheme": NotRequired[LoadBalancerSchemeEnumType],
        "VpcId": NotRequired[str],
        "State": NotRequired["LoadBalancerStateTypeDef"],
        "Type": NotRequired[LoadBalancerTypeEnumType],
        "AvailabilityZones": NotRequired[List["AvailabilityZoneTypeDef"]],
        "SecurityGroups": NotRequired[List[str]],
        "IpAddressType": NotRequired[IpAddressTypeType],
        "CustomerOwnedIpv4Pool": NotRequired[str],
    },
)

MatcherTypeDef = TypedDict(
    "MatcherTypeDef",
    {
        "HttpCode": NotRequired[str],
        "GrpcCode": NotRequired[str],
    },
)

ModifyListenerInputRequestTypeDef = TypedDict(
    "ModifyListenerInputRequestTypeDef",
    {
        "ListenerArn": str,
        "Port": NotRequired[int],
        "Protocol": NotRequired[ProtocolEnumType],
        "SslPolicy": NotRequired[str],
        "Certificates": NotRequired[Sequence["CertificateTypeDef"]],
        "DefaultActions": NotRequired[Sequence["ActionTypeDef"]],
        "AlpnPolicy": NotRequired[Sequence[str]],
    },
)

ModifyListenerOutputTypeDef = TypedDict(
    "ModifyListenerOutputTypeDef",
    {
        "Listeners": List["ListenerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyLoadBalancerAttributesInputRequestTypeDef = TypedDict(
    "ModifyLoadBalancerAttributesInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "Attributes": Sequence["LoadBalancerAttributeTypeDef"],
    },
)

ModifyLoadBalancerAttributesOutputTypeDef = TypedDict(
    "ModifyLoadBalancerAttributesOutputTypeDef",
    {
        "Attributes": List["LoadBalancerAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyRuleInputRequestTypeDef = TypedDict(
    "ModifyRuleInputRequestTypeDef",
    {
        "RuleArn": str,
        "Conditions": NotRequired[Sequence["RuleConditionTypeDef"]],
        "Actions": NotRequired[Sequence["ActionTypeDef"]],
    },
)

ModifyRuleOutputTypeDef = TypedDict(
    "ModifyRuleOutputTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyTargetGroupAttributesInputRequestTypeDef = TypedDict(
    "ModifyTargetGroupAttributesInputRequestTypeDef",
    {
        "TargetGroupArn": str,
        "Attributes": Sequence["TargetGroupAttributeTypeDef"],
    },
)

ModifyTargetGroupAttributesOutputTypeDef = TypedDict(
    "ModifyTargetGroupAttributesOutputTypeDef",
    {
        "Attributes": List["TargetGroupAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyTargetGroupInputRequestTypeDef = TypedDict(
    "ModifyTargetGroupInputRequestTypeDef",
    {
        "TargetGroupArn": str,
        "HealthCheckProtocol": NotRequired[ProtocolEnumType],
        "HealthCheckPort": NotRequired[str],
        "HealthCheckPath": NotRequired[str],
        "HealthCheckEnabled": NotRequired[bool],
        "HealthCheckIntervalSeconds": NotRequired[int],
        "HealthCheckTimeoutSeconds": NotRequired[int],
        "HealthyThresholdCount": NotRequired[int],
        "UnhealthyThresholdCount": NotRequired[int],
        "Matcher": NotRequired["MatcherTypeDef"],
    },
)

ModifyTargetGroupOutputTypeDef = TypedDict(
    "ModifyTargetGroupOutputTypeDef",
    {
        "TargetGroups": List["TargetGroupTypeDef"],
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

PathPatternConditionConfigTypeDef = TypedDict(
    "PathPatternConditionConfigTypeDef",
    {
        "Values": NotRequired[Sequence[str]],
    },
)

QueryStringConditionConfigTypeDef = TypedDict(
    "QueryStringConditionConfigTypeDef",
    {
        "Values": NotRequired[Sequence["QueryStringKeyValuePairTypeDef"]],
    },
)

QueryStringKeyValuePairTypeDef = TypedDict(
    "QueryStringKeyValuePairTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

RedirectActionConfigTypeDef = TypedDict(
    "RedirectActionConfigTypeDef",
    {
        "StatusCode": RedirectActionStatusCodeEnumType,
        "Protocol": NotRequired[str],
        "Port": NotRequired[str],
        "Host": NotRequired[str],
        "Path": NotRequired[str],
        "Query": NotRequired[str],
    },
)

RegisterTargetsInputRequestTypeDef = TypedDict(
    "RegisterTargetsInputRequestTypeDef",
    {
        "TargetGroupArn": str,
        "Targets": Sequence["TargetDescriptionTypeDef"],
    },
)

RemoveListenerCertificatesInputRequestTypeDef = TypedDict(
    "RemoveListenerCertificatesInputRequestTypeDef",
    {
        "ListenerArn": str,
        "Certificates": Sequence["CertificateTypeDef"],
    },
)

RemoveTagsInputRequestTypeDef = TypedDict(
    "RemoveTagsInputRequestTypeDef",
    {
        "ResourceArns": Sequence[str],
        "TagKeys": Sequence[str],
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

RuleConditionTypeDef = TypedDict(
    "RuleConditionTypeDef",
    {
        "Field": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
        "HostHeaderConfig": NotRequired["HostHeaderConditionConfigTypeDef"],
        "PathPatternConfig": NotRequired["PathPatternConditionConfigTypeDef"],
        "HttpHeaderConfig": NotRequired["HttpHeaderConditionConfigTypeDef"],
        "QueryStringConfig": NotRequired["QueryStringConditionConfigTypeDef"],
        "HttpRequestMethodConfig": NotRequired["HttpRequestMethodConditionConfigTypeDef"],
        "SourceIpConfig": NotRequired["SourceIpConditionConfigTypeDef"],
    },
)

RulePriorityPairTypeDef = TypedDict(
    "RulePriorityPairTypeDef",
    {
        "RuleArn": NotRequired[str],
        "Priority": NotRequired[int],
    },
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "RuleArn": NotRequired[str],
        "Priority": NotRequired[str],
        "Conditions": NotRequired[List["RuleConditionTypeDef"]],
        "Actions": NotRequired[List["ActionTypeDef"]],
        "IsDefault": NotRequired[bool],
    },
)

SetIpAddressTypeInputRequestTypeDef = TypedDict(
    "SetIpAddressTypeInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "IpAddressType": IpAddressTypeType,
    },
)

SetIpAddressTypeOutputTypeDef = TypedDict(
    "SetIpAddressTypeOutputTypeDef",
    {
        "IpAddressType": IpAddressTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetRulePrioritiesInputRequestTypeDef = TypedDict(
    "SetRulePrioritiesInputRequestTypeDef",
    {
        "RulePriorities": Sequence["RulePriorityPairTypeDef"],
    },
)

SetRulePrioritiesOutputTypeDef = TypedDict(
    "SetRulePrioritiesOutputTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetSecurityGroupsInputRequestTypeDef = TypedDict(
    "SetSecurityGroupsInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "SecurityGroups": Sequence[str],
    },
)

SetSecurityGroupsOutputTypeDef = TypedDict(
    "SetSecurityGroupsOutputTypeDef",
    {
        "SecurityGroupIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetSubnetsInputRequestTypeDef = TypedDict(
    "SetSubnetsInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "Subnets": NotRequired[Sequence[str]],
        "SubnetMappings": NotRequired[Sequence["SubnetMappingTypeDef"]],
        "IpAddressType": NotRequired[IpAddressTypeType],
    },
)

SetSubnetsOutputTypeDef = TypedDict(
    "SetSubnetsOutputTypeDef",
    {
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
        "IpAddressType": IpAddressTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SourceIpConditionConfigTypeDef = TypedDict(
    "SourceIpConditionConfigTypeDef",
    {
        "Values": NotRequired[Sequence[str]],
    },
)

SslPolicyTypeDef = TypedDict(
    "SslPolicyTypeDef",
    {
        "SslProtocols": NotRequired[List[str]],
        "Ciphers": NotRequired[List["CipherTypeDef"]],
        "Name": NotRequired[str],
        "SupportedLoadBalancerTypes": NotRequired[List[str]],
    },
)

SubnetMappingTypeDef = TypedDict(
    "SubnetMappingTypeDef",
    {
        "SubnetId": NotRequired[str],
        "AllocationId": NotRequired[str],
        "PrivateIPv4Address": NotRequired[str],
        "IPv6Address": NotRequired[str],
    },
)

TagDescriptionTypeDef = TypedDict(
    "TagDescriptionTypeDef",
    {
        "ResourceArn": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)

TargetDescriptionTypeDef = TypedDict(
    "TargetDescriptionTypeDef",
    {
        "Id": str,
        "Port": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
    },
)

TargetGroupAttributeTypeDef = TypedDict(
    "TargetGroupAttributeTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

TargetGroupStickinessConfigTypeDef = TypedDict(
    "TargetGroupStickinessConfigTypeDef",
    {
        "Enabled": NotRequired[bool],
        "DurationSeconds": NotRequired[int],
    },
)

TargetGroupTupleTypeDef = TypedDict(
    "TargetGroupTupleTypeDef",
    {
        "TargetGroupArn": NotRequired[str],
        "Weight": NotRequired[int],
    },
)

TargetGroupTypeDef = TypedDict(
    "TargetGroupTypeDef",
    {
        "TargetGroupArn": NotRequired[str],
        "TargetGroupName": NotRequired[str],
        "Protocol": NotRequired[ProtocolEnumType],
        "Port": NotRequired[int],
        "VpcId": NotRequired[str],
        "HealthCheckProtocol": NotRequired[ProtocolEnumType],
        "HealthCheckPort": NotRequired[str],
        "HealthCheckEnabled": NotRequired[bool],
        "HealthCheckIntervalSeconds": NotRequired[int],
        "HealthCheckTimeoutSeconds": NotRequired[int],
        "HealthyThresholdCount": NotRequired[int],
        "UnhealthyThresholdCount": NotRequired[int],
        "HealthCheckPath": NotRequired[str],
        "Matcher": NotRequired["MatcherTypeDef"],
        "LoadBalancerArns": NotRequired[List[str]],
        "TargetType": NotRequired[TargetTypeEnumType],
        "ProtocolVersion": NotRequired[str],
        "IpAddressType": NotRequired[TargetGroupIpAddressTypeEnumType],
    },
)

TargetHealthDescriptionTypeDef = TypedDict(
    "TargetHealthDescriptionTypeDef",
    {
        "Target": NotRequired["TargetDescriptionTypeDef"],
        "HealthCheckPort": NotRequired[str],
        "TargetHealth": NotRequired["TargetHealthTypeDef"],
    },
)

TargetHealthTypeDef = TypedDict(
    "TargetHealthTypeDef",
    {
        "State": NotRequired[TargetHealthStateEnumType],
        "Reason": NotRequired[TargetHealthReasonEnumType],
        "Description": NotRequired[str],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
