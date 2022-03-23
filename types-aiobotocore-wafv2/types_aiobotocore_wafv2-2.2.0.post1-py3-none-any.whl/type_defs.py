"""
Type annotations for wafv2 service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_wafv2.type_defs import ActionConditionTypeDef

    data: ActionConditionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    ActionValueType,
    BodyParsingFallbackBehaviorType,
    ComparisonOperatorType,
    CountryCodeType,
    FailureReasonType,
    FallbackBehaviorType,
    FilterBehaviorType,
    FilterRequirementType,
    ForwardedIPPositionType,
    IPAddressVersionType,
    JsonMatchScopeType,
    LabelMatchScopeType,
    PayloadTypeType,
    PlatformType,
    PositionalConstraintType,
    RateBasedStatementAggregateKeyTypeType,
    ResourceTypeType,
    ResponseContentTypeType,
    ScopeType,
    TextTransformationTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionConditionTypeDef",
    "AllowActionTypeDef",
    "AndStatementTypeDef",
    "AssociateWebACLRequestRequestTypeDef",
    "BlockActionTypeDef",
    "ByteMatchStatementTypeDef",
    "CaptchaActionTypeDef",
    "CaptchaConfigTypeDef",
    "CaptchaResponseTypeDef",
    "CheckCapacityRequestRequestTypeDef",
    "CheckCapacityResponseTypeDef",
    "ConditionTypeDef",
    "CountActionTypeDef",
    "CreateIPSetRequestRequestTypeDef",
    "CreateIPSetResponseTypeDef",
    "CreateRegexPatternSetRequestRequestTypeDef",
    "CreateRegexPatternSetResponseTypeDef",
    "CreateRuleGroupRequestRequestTypeDef",
    "CreateRuleGroupResponseTypeDef",
    "CreateWebACLRequestRequestTypeDef",
    "CreateWebACLResponseTypeDef",
    "CustomHTTPHeaderTypeDef",
    "CustomRequestHandlingTypeDef",
    "CustomResponseBodyTypeDef",
    "CustomResponseTypeDef",
    "DefaultActionTypeDef",
    "DeleteFirewallManagerRuleGroupsRequestRequestTypeDef",
    "DeleteFirewallManagerRuleGroupsResponseTypeDef",
    "DeleteIPSetRequestRequestTypeDef",
    "DeleteLoggingConfigurationRequestRequestTypeDef",
    "DeletePermissionPolicyRequestRequestTypeDef",
    "DeleteRegexPatternSetRequestRequestTypeDef",
    "DeleteRuleGroupRequestRequestTypeDef",
    "DeleteWebACLRequestRequestTypeDef",
    "DescribeManagedRuleGroupRequestRequestTypeDef",
    "DescribeManagedRuleGroupResponseTypeDef",
    "DisassociateWebACLRequestRequestTypeDef",
    "ExcludedRuleTypeDef",
    "FieldToMatchTypeDef",
    "FilterTypeDef",
    "FirewallManagerRuleGroupTypeDef",
    "FirewallManagerStatementTypeDef",
    "ForwardedIPConfigTypeDef",
    "GenerateMobileSdkReleaseUrlRequestRequestTypeDef",
    "GenerateMobileSdkReleaseUrlResponseTypeDef",
    "GeoMatchStatementTypeDef",
    "GetIPSetRequestRequestTypeDef",
    "GetIPSetResponseTypeDef",
    "GetLoggingConfigurationRequestRequestTypeDef",
    "GetLoggingConfigurationResponseTypeDef",
    "GetManagedRuleSetRequestRequestTypeDef",
    "GetManagedRuleSetResponseTypeDef",
    "GetMobileSdkReleaseRequestRequestTypeDef",
    "GetMobileSdkReleaseResponseTypeDef",
    "GetPermissionPolicyRequestRequestTypeDef",
    "GetPermissionPolicyResponseTypeDef",
    "GetRateBasedStatementManagedKeysRequestRequestTypeDef",
    "GetRateBasedStatementManagedKeysResponseTypeDef",
    "GetRegexPatternSetRequestRequestTypeDef",
    "GetRegexPatternSetResponseTypeDef",
    "GetRuleGroupRequestRequestTypeDef",
    "GetRuleGroupResponseTypeDef",
    "GetSampledRequestsRequestRequestTypeDef",
    "GetSampledRequestsResponseTypeDef",
    "GetWebACLForResourceRequestRequestTypeDef",
    "GetWebACLForResourceResponseTypeDef",
    "GetWebACLRequestRequestTypeDef",
    "GetWebACLResponseTypeDef",
    "HTTPHeaderTypeDef",
    "HTTPRequestTypeDef",
    "IPSetForwardedIPConfigTypeDef",
    "IPSetReferenceStatementTypeDef",
    "IPSetSummaryTypeDef",
    "IPSetTypeDef",
    "ImmunityTimePropertyTypeDef",
    "JsonBodyTypeDef",
    "JsonMatchPatternTypeDef",
    "LabelMatchStatementTypeDef",
    "LabelNameConditionTypeDef",
    "LabelSummaryTypeDef",
    "LabelTypeDef",
    "ListAvailableManagedRuleGroupVersionsRequestRequestTypeDef",
    "ListAvailableManagedRuleGroupVersionsResponseTypeDef",
    "ListAvailableManagedRuleGroupsRequestRequestTypeDef",
    "ListAvailableManagedRuleGroupsResponseTypeDef",
    "ListIPSetsRequestRequestTypeDef",
    "ListIPSetsResponseTypeDef",
    "ListLoggingConfigurationsRequestRequestTypeDef",
    "ListLoggingConfigurationsResponseTypeDef",
    "ListManagedRuleSetsRequestRequestTypeDef",
    "ListManagedRuleSetsResponseTypeDef",
    "ListMobileSdkReleasesRequestRequestTypeDef",
    "ListMobileSdkReleasesResponseTypeDef",
    "ListRegexPatternSetsRequestRequestTypeDef",
    "ListRegexPatternSetsResponseTypeDef",
    "ListResourcesForWebACLRequestRequestTypeDef",
    "ListResourcesForWebACLResponseTypeDef",
    "ListRuleGroupsRequestRequestTypeDef",
    "ListRuleGroupsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWebACLsRequestRequestTypeDef",
    "ListWebACLsResponseTypeDef",
    "LoggingConfigurationTypeDef",
    "LoggingFilterTypeDef",
    "ManagedRuleGroupConfigTypeDef",
    "ManagedRuleGroupStatementTypeDef",
    "ManagedRuleGroupSummaryTypeDef",
    "ManagedRuleGroupVersionTypeDef",
    "ManagedRuleSetSummaryTypeDef",
    "ManagedRuleSetTypeDef",
    "ManagedRuleSetVersionTypeDef",
    "MobileSdkReleaseTypeDef",
    "NotStatementTypeDef",
    "OrStatementTypeDef",
    "OverrideActionTypeDef",
    "PasswordFieldTypeDef",
    "PutLoggingConfigurationRequestRequestTypeDef",
    "PutLoggingConfigurationResponseTypeDef",
    "PutManagedRuleSetVersionsRequestRequestTypeDef",
    "PutManagedRuleSetVersionsResponseTypeDef",
    "PutPermissionPolicyRequestRequestTypeDef",
    "RateBasedStatementManagedKeysIPSetTypeDef",
    "RateBasedStatementTypeDef",
    "RegexMatchStatementTypeDef",
    "RegexPatternSetReferenceStatementTypeDef",
    "RegexPatternSetSummaryTypeDef",
    "RegexPatternSetTypeDef",
    "RegexTypeDef",
    "ReleaseSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "RuleActionTypeDef",
    "RuleGroupReferenceStatementTypeDef",
    "RuleGroupSummaryTypeDef",
    "RuleGroupTypeDef",
    "RuleSummaryTypeDef",
    "RuleTypeDef",
    "SampledHTTPRequestTypeDef",
    "SingleHeaderTypeDef",
    "SingleQueryArgumentTypeDef",
    "SizeConstraintStatementTypeDef",
    "SqliMatchStatementTypeDef",
    "StatementTypeDef",
    "TagInfoForResourceTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TextTransformationTypeDef",
    "TimeWindowTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateIPSetRequestRequestTypeDef",
    "UpdateIPSetResponseTypeDef",
    "UpdateManagedRuleSetVersionExpiryDateRequestRequestTypeDef",
    "UpdateManagedRuleSetVersionExpiryDateResponseTypeDef",
    "UpdateRegexPatternSetRequestRequestTypeDef",
    "UpdateRegexPatternSetResponseTypeDef",
    "UpdateRuleGroupRequestRequestTypeDef",
    "UpdateRuleGroupResponseTypeDef",
    "UpdateWebACLRequestRequestTypeDef",
    "UpdateWebACLResponseTypeDef",
    "UsernameFieldTypeDef",
    "VersionToPublishTypeDef",
    "VisibilityConfigTypeDef",
    "WebACLSummaryTypeDef",
    "WebACLTypeDef",
    "XssMatchStatementTypeDef",
)

ActionConditionTypeDef = TypedDict(
    "ActionConditionTypeDef",
    {
        "Action": ActionValueType,
    },
)

AllowActionTypeDef = TypedDict(
    "AllowActionTypeDef",
    {
        "CustomRequestHandling": NotRequired["CustomRequestHandlingTypeDef"],
    },
)

AndStatementTypeDef = TypedDict(
    "AndStatementTypeDef",
    {
        "Statements": Sequence["StatementTypeDef"],
    },
)

AssociateWebACLRequestRequestTypeDef = TypedDict(
    "AssociateWebACLRequestRequestTypeDef",
    {
        "WebACLArn": str,
        "ResourceArn": str,
    },
)

BlockActionTypeDef = TypedDict(
    "BlockActionTypeDef",
    {
        "CustomResponse": NotRequired["CustomResponseTypeDef"],
    },
)

ByteMatchStatementTypeDef = TypedDict(
    "ByteMatchStatementTypeDef",
    {
        "SearchString": Union[bytes, IO[bytes], StreamingBody],
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformations": Sequence["TextTransformationTypeDef"],
        "PositionalConstraint": PositionalConstraintType,
    },
)

CaptchaActionTypeDef = TypedDict(
    "CaptchaActionTypeDef",
    {
        "CustomRequestHandling": NotRequired["CustomRequestHandlingTypeDef"],
    },
)

CaptchaConfigTypeDef = TypedDict(
    "CaptchaConfigTypeDef",
    {
        "ImmunityTimeProperty": NotRequired["ImmunityTimePropertyTypeDef"],
    },
)

CaptchaResponseTypeDef = TypedDict(
    "CaptchaResponseTypeDef",
    {
        "ResponseCode": NotRequired[int],
        "SolveTimestamp": NotRequired[int],
        "FailureReason": NotRequired[FailureReasonType],
    },
)

CheckCapacityRequestRequestTypeDef = TypedDict(
    "CheckCapacityRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "Rules": Sequence["RuleTypeDef"],
    },
)

CheckCapacityResponseTypeDef = TypedDict(
    "CheckCapacityResponseTypeDef",
    {
        "Capacity": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "ActionCondition": NotRequired["ActionConditionTypeDef"],
        "LabelNameCondition": NotRequired["LabelNameConditionTypeDef"],
    },
)

CountActionTypeDef = TypedDict(
    "CountActionTypeDef",
    {
        "CustomRequestHandling": NotRequired["CustomRequestHandlingTypeDef"],
    },
)

CreateIPSetRequestRequestTypeDef = TypedDict(
    "CreateIPSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "IPAddressVersion": IPAddressVersionType,
        "Addresses": Sequence[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateIPSetResponseTypeDef = TypedDict(
    "CreateIPSetResponseTypeDef",
    {
        "Summary": "IPSetSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRegexPatternSetRequestRequestTypeDef = TypedDict(
    "CreateRegexPatternSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "RegularExpressionList": Sequence["RegexTypeDef"],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateRegexPatternSetResponseTypeDef = TypedDict(
    "CreateRegexPatternSetResponseTypeDef",
    {
        "Summary": "RegexPatternSetSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRuleGroupRequestRequestTypeDef = TypedDict(
    "CreateRuleGroupRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Capacity": int,
        "VisibilityConfig": "VisibilityConfigTypeDef",
        "Description": NotRequired[str],
        "Rules": NotRequired[Sequence["RuleTypeDef"]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "CustomResponseBodies": NotRequired[Mapping[str, "CustomResponseBodyTypeDef"]],
    },
)

CreateRuleGroupResponseTypeDef = TypedDict(
    "CreateRuleGroupResponseTypeDef",
    {
        "Summary": "RuleGroupSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWebACLRequestRequestTypeDef = TypedDict(
    "CreateWebACLRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "DefaultAction": "DefaultActionTypeDef",
        "VisibilityConfig": "VisibilityConfigTypeDef",
        "Description": NotRequired[str],
        "Rules": NotRequired[Sequence["RuleTypeDef"]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "CustomResponseBodies": NotRequired[Mapping[str, "CustomResponseBodyTypeDef"]],
        "CaptchaConfig": NotRequired["CaptchaConfigTypeDef"],
    },
)

CreateWebACLResponseTypeDef = TypedDict(
    "CreateWebACLResponseTypeDef",
    {
        "Summary": "WebACLSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomHTTPHeaderTypeDef = TypedDict(
    "CustomHTTPHeaderTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

CustomRequestHandlingTypeDef = TypedDict(
    "CustomRequestHandlingTypeDef",
    {
        "InsertHeaders": Sequence["CustomHTTPHeaderTypeDef"],
    },
)

CustomResponseBodyTypeDef = TypedDict(
    "CustomResponseBodyTypeDef",
    {
        "ContentType": ResponseContentTypeType,
        "Content": str,
    },
)

CustomResponseTypeDef = TypedDict(
    "CustomResponseTypeDef",
    {
        "ResponseCode": int,
        "CustomResponseBodyKey": NotRequired[str],
        "ResponseHeaders": NotRequired[Sequence["CustomHTTPHeaderTypeDef"]],
    },
)

DefaultActionTypeDef = TypedDict(
    "DefaultActionTypeDef",
    {
        "Block": NotRequired["BlockActionTypeDef"],
        "Allow": NotRequired["AllowActionTypeDef"],
    },
)

DeleteFirewallManagerRuleGroupsRequestRequestTypeDef = TypedDict(
    "DeleteFirewallManagerRuleGroupsRequestRequestTypeDef",
    {
        "WebACLArn": str,
        "WebACLLockToken": str,
    },
)

DeleteFirewallManagerRuleGroupsResponseTypeDef = TypedDict(
    "DeleteFirewallManagerRuleGroupsResponseTypeDef",
    {
        "NextWebACLLockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIPSetRequestRequestTypeDef = TypedDict(
    "DeleteIPSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
    },
)

DeleteLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteLoggingConfigurationRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DeletePermissionPolicyRequestRequestTypeDef = TypedDict(
    "DeletePermissionPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DeleteRegexPatternSetRequestRequestTypeDef = TypedDict(
    "DeleteRegexPatternSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
    },
)

DeleteRuleGroupRequestRequestTypeDef = TypedDict(
    "DeleteRuleGroupRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
    },
)

DeleteWebACLRequestRequestTypeDef = TypedDict(
    "DeleteWebACLRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
    },
)

DescribeManagedRuleGroupRequestRequestTypeDef = TypedDict(
    "DescribeManagedRuleGroupRequestRequestTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "Scope": ScopeType,
        "VersionName": NotRequired[str],
    },
)

DescribeManagedRuleGroupResponseTypeDef = TypedDict(
    "DescribeManagedRuleGroupResponseTypeDef",
    {
        "VersionName": str,
        "SnsTopicArn": str,
        "Capacity": int,
        "Rules": List["RuleSummaryTypeDef"],
        "LabelNamespace": str,
        "AvailableLabels": List["LabelSummaryTypeDef"],
        "ConsumedLabels": List["LabelSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateWebACLRequestRequestTypeDef = TypedDict(
    "DisassociateWebACLRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ExcludedRuleTypeDef = TypedDict(
    "ExcludedRuleTypeDef",
    {
        "Name": str,
    },
)

FieldToMatchTypeDef = TypedDict(
    "FieldToMatchTypeDef",
    {
        "SingleHeader": NotRequired["SingleHeaderTypeDef"],
        "SingleQueryArgument": NotRequired["SingleQueryArgumentTypeDef"],
        "AllQueryArguments": NotRequired[Mapping[str, Any]],
        "UriPath": NotRequired[Mapping[str, Any]],
        "QueryString": NotRequired[Mapping[str, Any]],
        "Body": NotRequired[Mapping[str, Any]],
        "Method": NotRequired[Mapping[str, Any]],
        "JsonBody": NotRequired["JsonBodyTypeDef"],
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Behavior": FilterBehaviorType,
        "Requirement": FilterRequirementType,
        "Conditions": List["ConditionTypeDef"],
    },
)

FirewallManagerRuleGroupTypeDef = TypedDict(
    "FirewallManagerRuleGroupTypeDef",
    {
        "Name": str,
        "Priority": int,
        "FirewallManagerStatement": "FirewallManagerStatementTypeDef",
        "OverrideAction": "OverrideActionTypeDef",
        "VisibilityConfig": "VisibilityConfigTypeDef",
    },
)

FirewallManagerStatementTypeDef = TypedDict(
    "FirewallManagerStatementTypeDef",
    {
        "ManagedRuleGroupStatement": NotRequired["ManagedRuleGroupStatementTypeDef"],
        "RuleGroupReferenceStatement": NotRequired["RuleGroupReferenceStatementTypeDef"],
    },
)

ForwardedIPConfigTypeDef = TypedDict(
    "ForwardedIPConfigTypeDef",
    {
        "HeaderName": str,
        "FallbackBehavior": FallbackBehaviorType,
    },
)

GenerateMobileSdkReleaseUrlRequestRequestTypeDef = TypedDict(
    "GenerateMobileSdkReleaseUrlRequestRequestTypeDef",
    {
        "Platform": PlatformType,
        "ReleaseVersion": str,
    },
)

GenerateMobileSdkReleaseUrlResponseTypeDef = TypedDict(
    "GenerateMobileSdkReleaseUrlResponseTypeDef",
    {
        "Url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GeoMatchStatementTypeDef = TypedDict(
    "GeoMatchStatementTypeDef",
    {
        "CountryCodes": NotRequired[Sequence[CountryCodeType]],
        "ForwardedIPConfig": NotRequired["ForwardedIPConfigTypeDef"],
    },
)

GetIPSetRequestRequestTypeDef = TypedDict(
    "GetIPSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
    },
)

GetIPSetResponseTypeDef = TypedDict(
    "GetIPSetResponseTypeDef",
    {
        "IPSet": "IPSetTypeDef",
        "LockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "GetLoggingConfigurationRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetLoggingConfigurationResponseTypeDef = TypedDict(
    "GetLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetManagedRuleSetRequestRequestTypeDef = TypedDict(
    "GetManagedRuleSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
    },
)

GetManagedRuleSetResponseTypeDef = TypedDict(
    "GetManagedRuleSetResponseTypeDef",
    {
        "ManagedRuleSet": "ManagedRuleSetTypeDef",
        "LockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMobileSdkReleaseRequestRequestTypeDef = TypedDict(
    "GetMobileSdkReleaseRequestRequestTypeDef",
    {
        "Platform": PlatformType,
        "ReleaseVersion": str,
    },
)

GetMobileSdkReleaseResponseTypeDef = TypedDict(
    "GetMobileSdkReleaseResponseTypeDef",
    {
        "MobileSdkRelease": "MobileSdkReleaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPermissionPolicyRequestRequestTypeDef = TypedDict(
    "GetPermissionPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetPermissionPolicyResponseTypeDef = TypedDict(
    "GetPermissionPolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRateBasedStatementManagedKeysRequestRequestTypeDef = TypedDict(
    "GetRateBasedStatementManagedKeysRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "WebACLName": str,
        "WebACLId": str,
        "RuleName": str,
        "RuleGroupRuleName": NotRequired[str],
    },
)

GetRateBasedStatementManagedKeysResponseTypeDef = TypedDict(
    "GetRateBasedStatementManagedKeysResponseTypeDef",
    {
        "ManagedKeysIPV4": "RateBasedStatementManagedKeysIPSetTypeDef",
        "ManagedKeysIPV6": "RateBasedStatementManagedKeysIPSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegexPatternSetRequestRequestTypeDef = TypedDict(
    "GetRegexPatternSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
    },
)

GetRegexPatternSetResponseTypeDef = TypedDict(
    "GetRegexPatternSetResponseTypeDef",
    {
        "RegexPatternSet": "RegexPatternSetTypeDef",
        "LockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRuleGroupRequestRequestTypeDef = TypedDict(
    "GetRuleGroupRequestRequestTypeDef",
    {
        "Name": NotRequired[str],
        "Scope": NotRequired[ScopeType],
        "Id": NotRequired[str],
        "ARN": NotRequired[str],
    },
)

GetRuleGroupResponseTypeDef = TypedDict(
    "GetRuleGroupResponseTypeDef",
    {
        "RuleGroup": "RuleGroupTypeDef",
        "LockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSampledRequestsRequestRequestTypeDef = TypedDict(
    "GetSampledRequestsRequestRequestTypeDef",
    {
        "WebAclArn": str,
        "RuleMetricName": str,
        "Scope": ScopeType,
        "TimeWindow": "TimeWindowTypeDef",
        "MaxItems": int,
    },
)

GetSampledRequestsResponseTypeDef = TypedDict(
    "GetSampledRequestsResponseTypeDef",
    {
        "SampledRequests": List["SampledHTTPRequestTypeDef"],
        "PopulationSize": int,
        "TimeWindow": "TimeWindowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWebACLForResourceRequestRequestTypeDef = TypedDict(
    "GetWebACLForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetWebACLForResourceResponseTypeDef = TypedDict(
    "GetWebACLForResourceResponseTypeDef",
    {
        "WebACL": "WebACLTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWebACLRequestRequestTypeDef = TypedDict(
    "GetWebACLRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
    },
)

GetWebACLResponseTypeDef = TypedDict(
    "GetWebACLResponseTypeDef",
    {
        "WebACL": "WebACLTypeDef",
        "LockToken": str,
        "ApplicationIntegrationURL": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HTTPHeaderTypeDef = TypedDict(
    "HTTPHeaderTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)

HTTPRequestTypeDef = TypedDict(
    "HTTPRequestTypeDef",
    {
        "ClientIP": NotRequired[str],
        "Country": NotRequired[str],
        "URI": NotRequired[str],
        "Method": NotRequired[str],
        "HTTPVersion": NotRequired[str],
        "Headers": NotRequired[List["HTTPHeaderTypeDef"]],
    },
)

IPSetForwardedIPConfigTypeDef = TypedDict(
    "IPSetForwardedIPConfigTypeDef",
    {
        "HeaderName": str,
        "FallbackBehavior": FallbackBehaviorType,
        "Position": ForwardedIPPositionType,
    },
)

IPSetReferenceStatementTypeDef = TypedDict(
    "IPSetReferenceStatementTypeDef",
    {
        "ARN": str,
        "IPSetForwardedIPConfig": NotRequired["IPSetForwardedIPConfigTypeDef"],
    },
)

IPSetSummaryTypeDef = TypedDict(
    "IPSetSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "Description": NotRequired[str],
        "LockToken": NotRequired[str],
        "ARN": NotRequired[str],
    },
)

IPSetTypeDef = TypedDict(
    "IPSetTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
        "IPAddressVersion": IPAddressVersionType,
        "Addresses": List[str],
        "Description": NotRequired[str],
    },
)

ImmunityTimePropertyTypeDef = TypedDict(
    "ImmunityTimePropertyTypeDef",
    {
        "ImmunityTime": int,
    },
)

JsonBodyTypeDef = TypedDict(
    "JsonBodyTypeDef",
    {
        "MatchPattern": "JsonMatchPatternTypeDef",
        "MatchScope": JsonMatchScopeType,
        "InvalidFallbackBehavior": NotRequired[BodyParsingFallbackBehaviorType],
    },
)

JsonMatchPatternTypeDef = TypedDict(
    "JsonMatchPatternTypeDef",
    {
        "All": NotRequired[Mapping[str, Any]],
        "IncludedPaths": NotRequired[Sequence[str]],
    },
)

LabelMatchStatementTypeDef = TypedDict(
    "LabelMatchStatementTypeDef",
    {
        "Scope": LabelMatchScopeType,
        "Key": str,
    },
)

LabelNameConditionTypeDef = TypedDict(
    "LabelNameConditionTypeDef",
    {
        "LabelName": str,
    },
)

LabelSummaryTypeDef = TypedDict(
    "LabelSummaryTypeDef",
    {
        "Name": NotRequired[str],
    },
)

LabelTypeDef = TypedDict(
    "LabelTypeDef",
    {
        "Name": str,
    },
)

ListAvailableManagedRuleGroupVersionsRequestRequestTypeDef = TypedDict(
    "ListAvailableManagedRuleGroupVersionsRequestRequestTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "Scope": ScopeType,
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListAvailableManagedRuleGroupVersionsResponseTypeDef = TypedDict(
    "ListAvailableManagedRuleGroupVersionsResponseTypeDef",
    {
        "NextMarker": str,
        "Versions": List["ManagedRuleGroupVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAvailableManagedRuleGroupsRequestRequestTypeDef = TypedDict(
    "ListAvailableManagedRuleGroupsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListAvailableManagedRuleGroupsResponseTypeDef = TypedDict(
    "ListAvailableManagedRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "ManagedRuleGroups": List["ManagedRuleGroupSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIPSetsRequestRequestTypeDef = TypedDict(
    "ListIPSetsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListIPSetsResponseTypeDef = TypedDict(
    "ListIPSetsResponseTypeDef",
    {
        "NextMarker": str,
        "IPSets": List["IPSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLoggingConfigurationsRequestRequestTypeDef = TypedDict(
    "ListLoggingConfigurationsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListLoggingConfigurationsResponseTypeDef = TypedDict(
    "ListLoggingConfigurationsResponseTypeDef",
    {
        "LoggingConfigurations": List["LoggingConfigurationTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListManagedRuleSetsRequestRequestTypeDef = TypedDict(
    "ListManagedRuleSetsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListManagedRuleSetsResponseTypeDef = TypedDict(
    "ListManagedRuleSetsResponseTypeDef",
    {
        "NextMarker": str,
        "ManagedRuleSets": List["ManagedRuleSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMobileSdkReleasesRequestRequestTypeDef = TypedDict(
    "ListMobileSdkReleasesRequestRequestTypeDef",
    {
        "Platform": PlatformType,
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListMobileSdkReleasesResponseTypeDef = TypedDict(
    "ListMobileSdkReleasesResponseTypeDef",
    {
        "ReleaseSummaries": List["ReleaseSummaryTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRegexPatternSetsRequestRequestTypeDef = TypedDict(
    "ListRegexPatternSetsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListRegexPatternSetsResponseTypeDef = TypedDict(
    "ListRegexPatternSetsResponseTypeDef",
    {
        "NextMarker": str,
        "RegexPatternSets": List["RegexPatternSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourcesForWebACLRequestRequestTypeDef = TypedDict(
    "ListResourcesForWebACLRequestRequestTypeDef",
    {
        "WebACLArn": str,
        "ResourceType": NotRequired[ResourceTypeType],
    },
)

ListResourcesForWebACLResponseTypeDef = TypedDict(
    "ListResourcesForWebACLResponseTypeDef",
    {
        "ResourceArns": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRuleGroupsRequestRequestTypeDef = TypedDict(
    "ListRuleGroupsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListRuleGroupsResponseTypeDef = TypedDict(
    "ListRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "RuleGroups": List["RuleGroupSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "NextMarker": str,
        "TagInfoForResource": "TagInfoForResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWebACLsRequestRequestTypeDef = TypedDict(
    "ListWebACLsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListWebACLsResponseTypeDef = TypedDict(
    "ListWebACLsResponseTypeDef",
    {
        "NextMarker": str,
        "WebACLs": List["WebACLSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": List[str],
        "RedactedFields": NotRequired[List["FieldToMatchTypeDef"]],
        "ManagedByFirewallManager": NotRequired[bool],
        "LoggingFilter": NotRequired["LoggingFilterTypeDef"],
    },
)

LoggingFilterTypeDef = TypedDict(
    "LoggingFilterTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DefaultBehavior": FilterBehaviorType,
    },
)

ManagedRuleGroupConfigTypeDef = TypedDict(
    "ManagedRuleGroupConfigTypeDef",
    {
        "LoginPath": NotRequired[str],
        "PayloadType": NotRequired[PayloadTypeType],
        "UsernameField": NotRequired["UsernameFieldTypeDef"],
        "PasswordField": NotRequired["PasswordFieldTypeDef"],
    },
)

ManagedRuleGroupStatementTypeDef = TypedDict(
    "ManagedRuleGroupStatementTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "Version": NotRequired[str],
        "ExcludedRules": NotRequired[Sequence["ExcludedRuleTypeDef"]],
        "ScopeDownStatement": NotRequired["StatementTypeDef"],
        "ManagedRuleGroupConfigs": NotRequired[Sequence["ManagedRuleGroupConfigTypeDef"]],
    },
)

ManagedRuleGroupSummaryTypeDef = TypedDict(
    "ManagedRuleGroupSummaryTypeDef",
    {
        "VendorName": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)

ManagedRuleGroupVersionTypeDef = TypedDict(
    "ManagedRuleGroupVersionTypeDef",
    {
        "Name": NotRequired[str],
        "LastUpdateTimestamp": NotRequired[datetime],
    },
)

ManagedRuleSetSummaryTypeDef = TypedDict(
    "ManagedRuleSetSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "Description": NotRequired[str],
        "LockToken": NotRequired[str],
        "ARN": NotRequired[str],
        "LabelNamespace": NotRequired[str],
    },
)

ManagedRuleSetTypeDef = TypedDict(
    "ManagedRuleSetTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
        "Description": NotRequired[str],
        "PublishedVersions": NotRequired[Dict[str, "ManagedRuleSetVersionTypeDef"]],
        "RecommendedVersion": NotRequired[str],
        "LabelNamespace": NotRequired[str],
    },
)

ManagedRuleSetVersionTypeDef = TypedDict(
    "ManagedRuleSetVersionTypeDef",
    {
        "AssociatedRuleGroupArn": NotRequired[str],
        "Capacity": NotRequired[int],
        "ForecastedLifetime": NotRequired[int],
        "PublishTimestamp": NotRequired[datetime],
        "LastUpdateTimestamp": NotRequired[datetime],
        "ExpiryTimestamp": NotRequired[datetime],
    },
)

MobileSdkReleaseTypeDef = TypedDict(
    "MobileSdkReleaseTypeDef",
    {
        "ReleaseVersion": NotRequired[str],
        "Timestamp": NotRequired[datetime],
        "ReleaseNotes": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

NotStatementTypeDef = TypedDict(
    "NotStatementTypeDef",
    {
        "Statement": "StatementTypeDef",
    },
)

OrStatementTypeDef = TypedDict(
    "OrStatementTypeDef",
    {
        "Statements": Sequence[Dict[str, Any]],
    },
)

OverrideActionTypeDef = TypedDict(
    "OverrideActionTypeDef",
    {
        "Count": NotRequired["CountActionTypeDef"],
        "None": NotRequired[Mapping[str, Any]],
    },
)

PasswordFieldTypeDef = TypedDict(
    "PasswordFieldTypeDef",
    {
        "Identifier": str,
    },
)

PutLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "PutLoggingConfigurationRequestRequestTypeDef",
    {
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
    },
)

PutLoggingConfigurationResponseTypeDef = TypedDict(
    "PutLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutManagedRuleSetVersionsRequestRequestTypeDef = TypedDict(
    "PutManagedRuleSetVersionsRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
        "RecommendedVersion": NotRequired[str],
        "VersionsToPublish": NotRequired[Mapping[str, "VersionToPublishTypeDef"]],
    },
)

PutManagedRuleSetVersionsResponseTypeDef = TypedDict(
    "PutManagedRuleSetVersionsResponseTypeDef",
    {
        "NextLockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutPermissionPolicyRequestRequestTypeDef = TypedDict(
    "PutPermissionPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
    },
)

RateBasedStatementManagedKeysIPSetTypeDef = TypedDict(
    "RateBasedStatementManagedKeysIPSetTypeDef",
    {
        "IPAddressVersion": NotRequired[IPAddressVersionType],
        "Addresses": NotRequired[List[str]],
    },
)

RateBasedStatementTypeDef = TypedDict(
    "RateBasedStatementTypeDef",
    {
        "Limit": int,
        "AggregateKeyType": RateBasedStatementAggregateKeyTypeType,
        "ScopeDownStatement": NotRequired["StatementTypeDef"],
        "ForwardedIPConfig": NotRequired["ForwardedIPConfigTypeDef"],
    },
)

RegexMatchStatementTypeDef = TypedDict(
    "RegexMatchStatementTypeDef",
    {
        "RegexString": str,
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformations": Sequence["TextTransformationTypeDef"],
    },
)

RegexPatternSetReferenceStatementTypeDef = TypedDict(
    "RegexPatternSetReferenceStatementTypeDef",
    {
        "ARN": str,
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformations": Sequence["TextTransformationTypeDef"],
    },
)

RegexPatternSetSummaryTypeDef = TypedDict(
    "RegexPatternSetSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "Description": NotRequired[str],
        "LockToken": NotRequired[str],
        "ARN": NotRequired[str],
    },
)

RegexPatternSetTypeDef = TypedDict(
    "RegexPatternSetTypeDef",
    {
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "ARN": NotRequired[str],
        "Description": NotRequired[str],
        "RegularExpressionList": NotRequired[List["RegexTypeDef"]],
    },
)

RegexTypeDef = TypedDict(
    "RegexTypeDef",
    {
        "RegexString": NotRequired[str],
    },
)

ReleaseSummaryTypeDef = TypedDict(
    "ReleaseSummaryTypeDef",
    {
        "ReleaseVersion": NotRequired[str],
        "Timestamp": NotRequired[datetime],
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

RuleActionTypeDef = TypedDict(
    "RuleActionTypeDef",
    {
        "Block": NotRequired["BlockActionTypeDef"],
        "Allow": NotRequired["AllowActionTypeDef"],
        "Count": NotRequired["CountActionTypeDef"],
        "Captcha": NotRequired["CaptchaActionTypeDef"],
    },
)

RuleGroupReferenceStatementTypeDef = TypedDict(
    "RuleGroupReferenceStatementTypeDef",
    {
        "ARN": str,
        "ExcludedRules": NotRequired[Sequence["ExcludedRuleTypeDef"]],
    },
)

RuleGroupSummaryTypeDef = TypedDict(
    "RuleGroupSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "Description": NotRequired[str],
        "LockToken": NotRequired[str],
        "ARN": NotRequired[str],
    },
)

RuleGroupTypeDef = TypedDict(
    "RuleGroupTypeDef",
    {
        "Name": str,
        "Id": str,
        "Capacity": int,
        "ARN": str,
        "VisibilityConfig": "VisibilityConfigTypeDef",
        "Description": NotRequired[str],
        "Rules": NotRequired[List["RuleTypeDef"]],
        "LabelNamespace": NotRequired[str],
        "CustomResponseBodies": NotRequired[Dict[str, "CustomResponseBodyTypeDef"]],
        "AvailableLabels": NotRequired[List["LabelSummaryTypeDef"]],
        "ConsumedLabels": NotRequired[List["LabelSummaryTypeDef"]],
    },
)

RuleSummaryTypeDef = TypedDict(
    "RuleSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "Action": NotRequired["RuleActionTypeDef"],
    },
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Name": str,
        "Priority": int,
        "Statement": "StatementTypeDef",
        "VisibilityConfig": "VisibilityConfigTypeDef",
        "Action": NotRequired["RuleActionTypeDef"],
        "OverrideAction": NotRequired["OverrideActionTypeDef"],
        "RuleLabels": NotRequired[Sequence["LabelTypeDef"]],
        "CaptchaConfig": NotRequired["CaptchaConfigTypeDef"],
    },
)

SampledHTTPRequestTypeDef = TypedDict(
    "SampledHTTPRequestTypeDef",
    {
        "Request": "HTTPRequestTypeDef",
        "Weight": int,
        "Timestamp": NotRequired[datetime],
        "Action": NotRequired[str],
        "RuleNameWithinRuleGroup": NotRequired[str],
        "RequestHeadersInserted": NotRequired[List["HTTPHeaderTypeDef"]],
        "ResponseCodeSent": NotRequired[int],
        "Labels": NotRequired[List["LabelTypeDef"]],
        "CaptchaResponse": NotRequired["CaptchaResponseTypeDef"],
    },
)

SingleHeaderTypeDef = TypedDict(
    "SingleHeaderTypeDef",
    {
        "Name": str,
    },
)

SingleQueryArgumentTypeDef = TypedDict(
    "SingleQueryArgumentTypeDef",
    {
        "Name": str,
    },
)

SizeConstraintStatementTypeDef = TypedDict(
    "SizeConstraintStatementTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "ComparisonOperator": ComparisonOperatorType,
        "Size": int,
        "TextTransformations": Sequence["TextTransformationTypeDef"],
    },
)

SqliMatchStatementTypeDef = TypedDict(
    "SqliMatchStatementTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformations": Sequence["TextTransformationTypeDef"],
    },
)

StatementTypeDef = TypedDict(
    "StatementTypeDef",
    {
        "ByteMatchStatement": NotRequired["ByteMatchStatementTypeDef"],
        "SqliMatchStatement": NotRequired["SqliMatchStatementTypeDef"],
        "XssMatchStatement": NotRequired["XssMatchStatementTypeDef"],
        "SizeConstraintStatement": NotRequired["SizeConstraintStatementTypeDef"],
        "GeoMatchStatement": NotRequired["GeoMatchStatementTypeDef"],
        "RuleGroupReferenceStatement": NotRequired["RuleGroupReferenceStatementTypeDef"],
        "IPSetReferenceStatement": NotRequired["IPSetReferenceStatementTypeDef"],
        "RegexPatternSetReferenceStatement": NotRequired[
            "RegexPatternSetReferenceStatementTypeDef"
        ],
        "RateBasedStatement": NotRequired[Dict[str, Any]],
        "AndStatement": NotRequired[Dict[str, Any]],
        "OrStatement": NotRequired[Dict[str, Any]],
        "NotStatement": NotRequired[Dict[str, Any]],
        "ManagedRuleGroupStatement": NotRequired[Dict[str, Any]],
        "LabelMatchStatement": NotRequired["LabelMatchStatementTypeDef"],
        "RegexMatchStatement": NotRequired["RegexMatchStatementTypeDef"],
    },
)

TagInfoForResourceTypeDef = TypedDict(
    "TagInfoForResourceTypeDef",
    {
        "ResourceARN": NotRequired[str],
        "TagList": NotRequired[List["TagTypeDef"]],
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
        "Key": str,
        "Value": str,
    },
)

TextTransformationTypeDef = TypedDict(
    "TextTransformationTypeDef",
    {
        "Priority": int,
        "Type": TextTransformationTypeType,
    },
)

TimeWindowTypeDef = TypedDict(
    "TimeWindowTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateIPSetRequestRequestTypeDef = TypedDict(
    "UpdateIPSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "Addresses": Sequence[str],
        "LockToken": str,
        "Description": NotRequired[str],
    },
)

UpdateIPSetResponseTypeDef = TypedDict(
    "UpdateIPSetResponseTypeDef",
    {
        "NextLockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateManagedRuleSetVersionExpiryDateRequestRequestTypeDef = TypedDict(
    "UpdateManagedRuleSetVersionExpiryDateRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
        "VersionToExpire": str,
        "ExpiryTimestamp": Union[datetime, str],
    },
)

UpdateManagedRuleSetVersionExpiryDateResponseTypeDef = TypedDict(
    "UpdateManagedRuleSetVersionExpiryDateResponseTypeDef",
    {
        "ExpiringVersion": str,
        "ExpiryTimestamp": datetime,
        "NextLockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRegexPatternSetRequestRequestTypeDef = TypedDict(
    "UpdateRegexPatternSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "RegularExpressionList": Sequence["RegexTypeDef"],
        "LockToken": str,
        "Description": NotRequired[str],
    },
)

UpdateRegexPatternSetResponseTypeDef = TypedDict(
    "UpdateRegexPatternSetResponseTypeDef",
    {
        "NextLockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRuleGroupRequestRequestTypeDef = TypedDict(
    "UpdateRuleGroupRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "VisibilityConfig": "VisibilityConfigTypeDef",
        "LockToken": str,
        "Description": NotRequired[str],
        "Rules": NotRequired[Sequence["RuleTypeDef"]],
        "CustomResponseBodies": NotRequired[Mapping[str, "CustomResponseBodyTypeDef"]],
    },
)

UpdateRuleGroupResponseTypeDef = TypedDict(
    "UpdateRuleGroupResponseTypeDef",
    {
        "NextLockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateWebACLRequestRequestTypeDef = TypedDict(
    "UpdateWebACLRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "DefaultAction": "DefaultActionTypeDef",
        "VisibilityConfig": "VisibilityConfigTypeDef",
        "LockToken": str,
        "Description": NotRequired[str],
        "Rules": NotRequired[Sequence["RuleTypeDef"]],
        "CustomResponseBodies": NotRequired[Mapping[str, "CustomResponseBodyTypeDef"]],
        "CaptchaConfig": NotRequired["CaptchaConfigTypeDef"],
    },
)

UpdateWebACLResponseTypeDef = TypedDict(
    "UpdateWebACLResponseTypeDef",
    {
        "NextLockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsernameFieldTypeDef = TypedDict(
    "UsernameFieldTypeDef",
    {
        "Identifier": str,
    },
)

VersionToPublishTypeDef = TypedDict(
    "VersionToPublishTypeDef",
    {
        "AssociatedRuleGroupArn": NotRequired[str],
        "ForecastedLifetime": NotRequired[int],
    },
)

VisibilityConfigTypeDef = TypedDict(
    "VisibilityConfigTypeDef",
    {
        "SampledRequestsEnabled": bool,
        "CloudWatchMetricsEnabled": bool,
        "MetricName": str,
    },
)

WebACLSummaryTypeDef = TypedDict(
    "WebACLSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "Description": NotRequired[str],
        "LockToken": NotRequired[str],
        "ARN": NotRequired[str],
    },
)

WebACLTypeDef = TypedDict(
    "WebACLTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
        "DefaultAction": "DefaultActionTypeDef",
        "VisibilityConfig": "VisibilityConfigTypeDef",
        "Description": NotRequired[str],
        "Rules": NotRequired[List["RuleTypeDef"]],
        "Capacity": NotRequired[int],
        "PreProcessFirewallManagerRuleGroups": NotRequired[List["FirewallManagerRuleGroupTypeDef"]],
        "PostProcessFirewallManagerRuleGroups": NotRequired[
            List["FirewallManagerRuleGroupTypeDef"]
        ],
        "ManagedByFirewallManager": NotRequired[bool],
        "LabelNamespace": NotRequired[str],
        "CustomResponseBodies": NotRequired[Dict[str, "CustomResponseBodyTypeDef"]],
        "CaptchaConfig": NotRequired["CaptchaConfigTypeDef"],
    },
)

XssMatchStatementTypeDef = TypedDict(
    "XssMatchStatementTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformations": Sequence["TextTransformationTypeDef"],
    },
)
