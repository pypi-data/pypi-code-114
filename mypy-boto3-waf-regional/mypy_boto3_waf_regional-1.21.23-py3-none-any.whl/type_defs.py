"""
Type annotations for waf-regional service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf_regional/type_defs.html)

Usage::

    ```python
    from mypy_boto3_waf_regional.type_defs import ActivatedRuleTypeDef

    data: ActivatedRuleTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    ChangeActionType,
    ChangeTokenStatusType,
    ComparisonOperatorType,
    GeoMatchConstraintValueType,
    IPSetDescriptorTypeType,
    MatchFieldTypeType,
    PositionalConstraintType,
    PredicateTypeType,
    ResourceTypeType,
    TextTransformationType,
    WafActionTypeType,
    WafOverrideActionTypeType,
    WafRuleTypeType,
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
    "ActivatedRuleTypeDef",
    "AssociateWebACLRequestRequestTypeDef",
    "ByteMatchSetSummaryTypeDef",
    "ByteMatchSetTypeDef",
    "ByteMatchSetUpdateTypeDef",
    "ByteMatchTupleTypeDef",
    "CreateByteMatchSetRequestRequestTypeDef",
    "CreateByteMatchSetResponseTypeDef",
    "CreateGeoMatchSetRequestRequestTypeDef",
    "CreateGeoMatchSetResponseTypeDef",
    "CreateIPSetRequestRequestTypeDef",
    "CreateIPSetResponseTypeDef",
    "CreateRateBasedRuleRequestRequestTypeDef",
    "CreateRateBasedRuleResponseTypeDef",
    "CreateRegexMatchSetRequestRequestTypeDef",
    "CreateRegexMatchSetResponseTypeDef",
    "CreateRegexPatternSetRequestRequestTypeDef",
    "CreateRegexPatternSetResponseTypeDef",
    "CreateRuleGroupRequestRequestTypeDef",
    "CreateRuleGroupResponseTypeDef",
    "CreateRuleRequestRequestTypeDef",
    "CreateRuleResponseTypeDef",
    "CreateSizeConstraintSetRequestRequestTypeDef",
    "CreateSizeConstraintSetResponseTypeDef",
    "CreateSqlInjectionMatchSetRequestRequestTypeDef",
    "CreateSqlInjectionMatchSetResponseTypeDef",
    "CreateWebACLMigrationStackRequestRequestTypeDef",
    "CreateWebACLMigrationStackResponseTypeDef",
    "CreateWebACLRequestRequestTypeDef",
    "CreateWebACLResponseTypeDef",
    "CreateXssMatchSetRequestRequestTypeDef",
    "CreateXssMatchSetResponseTypeDef",
    "DeleteByteMatchSetRequestRequestTypeDef",
    "DeleteByteMatchSetResponseTypeDef",
    "DeleteGeoMatchSetRequestRequestTypeDef",
    "DeleteGeoMatchSetResponseTypeDef",
    "DeleteIPSetRequestRequestTypeDef",
    "DeleteIPSetResponseTypeDef",
    "DeleteLoggingConfigurationRequestRequestTypeDef",
    "DeletePermissionPolicyRequestRequestTypeDef",
    "DeleteRateBasedRuleRequestRequestTypeDef",
    "DeleteRateBasedRuleResponseTypeDef",
    "DeleteRegexMatchSetRequestRequestTypeDef",
    "DeleteRegexMatchSetResponseTypeDef",
    "DeleteRegexPatternSetRequestRequestTypeDef",
    "DeleteRegexPatternSetResponseTypeDef",
    "DeleteRuleGroupRequestRequestTypeDef",
    "DeleteRuleGroupResponseTypeDef",
    "DeleteRuleRequestRequestTypeDef",
    "DeleteRuleResponseTypeDef",
    "DeleteSizeConstraintSetRequestRequestTypeDef",
    "DeleteSizeConstraintSetResponseTypeDef",
    "DeleteSqlInjectionMatchSetRequestRequestTypeDef",
    "DeleteSqlInjectionMatchSetResponseTypeDef",
    "DeleteWebACLRequestRequestTypeDef",
    "DeleteWebACLResponseTypeDef",
    "DeleteXssMatchSetRequestRequestTypeDef",
    "DeleteXssMatchSetResponseTypeDef",
    "DisassociateWebACLRequestRequestTypeDef",
    "ExcludedRuleTypeDef",
    "FieldToMatchTypeDef",
    "GeoMatchConstraintTypeDef",
    "GeoMatchSetSummaryTypeDef",
    "GeoMatchSetTypeDef",
    "GeoMatchSetUpdateTypeDef",
    "GetByteMatchSetRequestRequestTypeDef",
    "GetByteMatchSetResponseTypeDef",
    "GetChangeTokenResponseTypeDef",
    "GetChangeTokenStatusRequestRequestTypeDef",
    "GetChangeTokenStatusResponseTypeDef",
    "GetGeoMatchSetRequestRequestTypeDef",
    "GetGeoMatchSetResponseTypeDef",
    "GetIPSetRequestRequestTypeDef",
    "GetIPSetResponseTypeDef",
    "GetLoggingConfigurationRequestRequestTypeDef",
    "GetLoggingConfigurationResponseTypeDef",
    "GetPermissionPolicyRequestRequestTypeDef",
    "GetPermissionPolicyResponseTypeDef",
    "GetRateBasedRuleManagedKeysRequestRequestTypeDef",
    "GetRateBasedRuleManagedKeysResponseTypeDef",
    "GetRateBasedRuleRequestRequestTypeDef",
    "GetRateBasedRuleResponseTypeDef",
    "GetRegexMatchSetRequestRequestTypeDef",
    "GetRegexMatchSetResponseTypeDef",
    "GetRegexPatternSetRequestRequestTypeDef",
    "GetRegexPatternSetResponseTypeDef",
    "GetRuleGroupRequestRequestTypeDef",
    "GetRuleGroupResponseTypeDef",
    "GetRuleRequestRequestTypeDef",
    "GetRuleResponseTypeDef",
    "GetSampledRequestsRequestRequestTypeDef",
    "GetSampledRequestsResponseTypeDef",
    "GetSizeConstraintSetRequestRequestTypeDef",
    "GetSizeConstraintSetResponseTypeDef",
    "GetSqlInjectionMatchSetRequestRequestTypeDef",
    "GetSqlInjectionMatchSetResponseTypeDef",
    "GetWebACLForResourceRequestRequestTypeDef",
    "GetWebACLForResourceResponseTypeDef",
    "GetWebACLRequestRequestTypeDef",
    "GetWebACLResponseTypeDef",
    "GetXssMatchSetRequestRequestTypeDef",
    "GetXssMatchSetResponseTypeDef",
    "HTTPHeaderTypeDef",
    "HTTPRequestTypeDef",
    "IPSetDescriptorTypeDef",
    "IPSetSummaryTypeDef",
    "IPSetTypeDef",
    "IPSetUpdateTypeDef",
    "ListActivatedRulesInRuleGroupRequestRequestTypeDef",
    "ListActivatedRulesInRuleGroupResponseTypeDef",
    "ListByteMatchSetsRequestRequestTypeDef",
    "ListByteMatchSetsResponseTypeDef",
    "ListGeoMatchSetsRequestRequestTypeDef",
    "ListGeoMatchSetsResponseTypeDef",
    "ListIPSetsRequestRequestTypeDef",
    "ListIPSetsResponseTypeDef",
    "ListLoggingConfigurationsRequestRequestTypeDef",
    "ListLoggingConfigurationsResponseTypeDef",
    "ListRateBasedRulesRequestRequestTypeDef",
    "ListRateBasedRulesResponseTypeDef",
    "ListRegexMatchSetsRequestRequestTypeDef",
    "ListRegexMatchSetsResponseTypeDef",
    "ListRegexPatternSetsRequestRequestTypeDef",
    "ListRegexPatternSetsResponseTypeDef",
    "ListResourcesForWebACLRequestRequestTypeDef",
    "ListResourcesForWebACLResponseTypeDef",
    "ListRuleGroupsRequestRequestTypeDef",
    "ListRuleGroupsResponseTypeDef",
    "ListRulesRequestRequestTypeDef",
    "ListRulesResponseTypeDef",
    "ListSizeConstraintSetsRequestRequestTypeDef",
    "ListSizeConstraintSetsResponseTypeDef",
    "ListSqlInjectionMatchSetsRequestRequestTypeDef",
    "ListSqlInjectionMatchSetsResponseTypeDef",
    "ListSubscribedRuleGroupsRequestRequestTypeDef",
    "ListSubscribedRuleGroupsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWebACLsRequestRequestTypeDef",
    "ListWebACLsResponseTypeDef",
    "ListXssMatchSetsRequestRequestTypeDef",
    "ListXssMatchSetsResponseTypeDef",
    "LoggingConfigurationTypeDef",
    "PredicateTypeDef",
    "PutLoggingConfigurationRequestRequestTypeDef",
    "PutLoggingConfigurationResponseTypeDef",
    "PutPermissionPolicyRequestRequestTypeDef",
    "RateBasedRuleTypeDef",
    "RegexMatchSetSummaryTypeDef",
    "RegexMatchSetTypeDef",
    "RegexMatchSetUpdateTypeDef",
    "RegexMatchTupleTypeDef",
    "RegexPatternSetSummaryTypeDef",
    "RegexPatternSetTypeDef",
    "RegexPatternSetUpdateTypeDef",
    "ResponseMetadataTypeDef",
    "RuleGroupSummaryTypeDef",
    "RuleGroupTypeDef",
    "RuleGroupUpdateTypeDef",
    "RuleSummaryTypeDef",
    "RuleTypeDef",
    "RuleUpdateTypeDef",
    "SampledHTTPRequestTypeDef",
    "SizeConstraintSetSummaryTypeDef",
    "SizeConstraintSetTypeDef",
    "SizeConstraintSetUpdateTypeDef",
    "SizeConstraintTypeDef",
    "SqlInjectionMatchSetSummaryTypeDef",
    "SqlInjectionMatchSetTypeDef",
    "SqlInjectionMatchSetUpdateTypeDef",
    "SqlInjectionMatchTupleTypeDef",
    "SubscribedRuleGroupSummaryTypeDef",
    "TagInfoForResourceTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TimeWindowTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateByteMatchSetRequestRequestTypeDef",
    "UpdateByteMatchSetResponseTypeDef",
    "UpdateGeoMatchSetRequestRequestTypeDef",
    "UpdateGeoMatchSetResponseTypeDef",
    "UpdateIPSetRequestRequestTypeDef",
    "UpdateIPSetResponseTypeDef",
    "UpdateRateBasedRuleRequestRequestTypeDef",
    "UpdateRateBasedRuleResponseTypeDef",
    "UpdateRegexMatchSetRequestRequestTypeDef",
    "UpdateRegexMatchSetResponseTypeDef",
    "UpdateRegexPatternSetRequestRequestTypeDef",
    "UpdateRegexPatternSetResponseTypeDef",
    "UpdateRuleGroupRequestRequestTypeDef",
    "UpdateRuleGroupResponseTypeDef",
    "UpdateRuleRequestRequestTypeDef",
    "UpdateRuleResponseTypeDef",
    "UpdateSizeConstraintSetRequestRequestTypeDef",
    "UpdateSizeConstraintSetResponseTypeDef",
    "UpdateSqlInjectionMatchSetRequestRequestTypeDef",
    "UpdateSqlInjectionMatchSetResponseTypeDef",
    "UpdateWebACLRequestRequestTypeDef",
    "UpdateWebACLResponseTypeDef",
    "UpdateXssMatchSetRequestRequestTypeDef",
    "UpdateXssMatchSetResponseTypeDef",
    "WafActionTypeDef",
    "WafOverrideActionTypeDef",
    "WebACLSummaryTypeDef",
    "WebACLTypeDef",
    "WebACLUpdateTypeDef",
    "XssMatchSetSummaryTypeDef",
    "XssMatchSetTypeDef",
    "XssMatchSetUpdateTypeDef",
    "XssMatchTupleTypeDef",
)

ActivatedRuleTypeDef = TypedDict(
    "ActivatedRuleTypeDef",
    {
        "Priority": int,
        "RuleId": str,
        "Action": NotRequired["WafActionTypeDef"],
        "OverrideAction": NotRequired["WafOverrideActionTypeDef"],
        "Type": NotRequired[WafRuleTypeType],
        "ExcludedRules": NotRequired[List["ExcludedRuleTypeDef"]],
    },
)

AssociateWebACLRequestRequestTypeDef = TypedDict(
    "AssociateWebACLRequestRequestTypeDef",
    {
        "WebACLId": str,
        "ResourceArn": str,
    },
)

ByteMatchSetSummaryTypeDef = TypedDict(
    "ByteMatchSetSummaryTypeDef",
    {
        "ByteMatchSetId": str,
        "Name": str,
    },
)

ByteMatchSetTypeDef = TypedDict(
    "ByteMatchSetTypeDef",
    {
        "ByteMatchSetId": str,
        "ByteMatchTuples": List["ByteMatchTupleTypeDef"],
        "Name": NotRequired[str],
    },
)

ByteMatchSetUpdateTypeDef = TypedDict(
    "ByteMatchSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "ByteMatchTuple": "ByteMatchTupleTypeDef",
    },
)

ByteMatchTupleTypeDef = TypedDict(
    "ByteMatchTupleTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TargetString": bytes,
        "TextTransformation": TextTransformationType,
        "PositionalConstraint": PositionalConstraintType,
    },
)

CreateByteMatchSetRequestRequestTypeDef = TypedDict(
    "CreateByteMatchSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateByteMatchSetResponseTypeDef = TypedDict(
    "CreateByteMatchSetResponseTypeDef",
    {
        "ByteMatchSet": "ByteMatchSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGeoMatchSetRequestRequestTypeDef = TypedDict(
    "CreateGeoMatchSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateGeoMatchSetResponseTypeDef = TypedDict(
    "CreateGeoMatchSetResponseTypeDef",
    {
        "GeoMatchSet": "GeoMatchSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIPSetRequestRequestTypeDef = TypedDict(
    "CreateIPSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateIPSetResponseTypeDef = TypedDict(
    "CreateIPSetResponseTypeDef",
    {
        "IPSet": "IPSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRateBasedRuleRequestRequestTypeDef = TypedDict(
    "CreateRateBasedRuleRequestRequestTypeDef",
    {
        "Name": str,
        "MetricName": str,
        "RateKey": Literal["IP"],
        "RateLimit": int,
        "ChangeToken": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateRateBasedRuleResponseTypeDef = TypedDict(
    "CreateRateBasedRuleResponseTypeDef",
    {
        "Rule": "RateBasedRuleTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRegexMatchSetRequestRequestTypeDef = TypedDict(
    "CreateRegexMatchSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateRegexMatchSetResponseTypeDef = TypedDict(
    "CreateRegexMatchSetResponseTypeDef",
    {
        "RegexMatchSet": "RegexMatchSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRegexPatternSetRequestRequestTypeDef = TypedDict(
    "CreateRegexPatternSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateRegexPatternSetResponseTypeDef = TypedDict(
    "CreateRegexPatternSetResponseTypeDef",
    {
        "RegexPatternSet": "RegexPatternSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRuleGroupRequestRequestTypeDef = TypedDict(
    "CreateRuleGroupRequestRequestTypeDef",
    {
        "Name": str,
        "MetricName": str,
        "ChangeToken": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateRuleGroupResponseTypeDef = TypedDict(
    "CreateRuleGroupResponseTypeDef",
    {
        "RuleGroup": "RuleGroupTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRuleRequestRequestTypeDef = TypedDict(
    "CreateRuleRequestRequestTypeDef",
    {
        "Name": str,
        "MetricName": str,
        "ChangeToken": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateRuleResponseTypeDef = TypedDict(
    "CreateRuleResponseTypeDef",
    {
        "Rule": "RuleTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSizeConstraintSetRequestRequestTypeDef = TypedDict(
    "CreateSizeConstraintSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateSizeConstraintSetResponseTypeDef = TypedDict(
    "CreateSizeConstraintSetResponseTypeDef",
    {
        "SizeConstraintSet": "SizeConstraintSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSqlInjectionMatchSetRequestRequestTypeDef = TypedDict(
    "CreateSqlInjectionMatchSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "CreateSqlInjectionMatchSetResponseTypeDef",
    {
        "SqlInjectionMatchSet": "SqlInjectionMatchSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWebACLMigrationStackRequestRequestTypeDef = TypedDict(
    "CreateWebACLMigrationStackRequestRequestTypeDef",
    {
        "WebACLId": str,
        "S3BucketName": str,
        "IgnoreUnsupportedType": bool,
    },
)

CreateWebACLMigrationStackResponseTypeDef = TypedDict(
    "CreateWebACLMigrationStackResponseTypeDef",
    {
        "S3ObjectUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWebACLRequestRequestTypeDef = TypedDict(
    "CreateWebACLRequestRequestTypeDef",
    {
        "Name": str,
        "MetricName": str,
        "DefaultAction": "WafActionTypeDef",
        "ChangeToken": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateWebACLResponseTypeDef = TypedDict(
    "CreateWebACLResponseTypeDef",
    {
        "WebACL": "WebACLTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateXssMatchSetRequestRequestTypeDef = TypedDict(
    "CreateXssMatchSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateXssMatchSetResponseTypeDef = TypedDict(
    "CreateXssMatchSetResponseTypeDef",
    {
        "XssMatchSet": "XssMatchSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteByteMatchSetRequestRequestTypeDef = TypedDict(
    "DeleteByteMatchSetRequestRequestTypeDef",
    {
        "ByteMatchSetId": str,
        "ChangeToken": str,
    },
)

DeleteByteMatchSetResponseTypeDef = TypedDict(
    "DeleteByteMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGeoMatchSetRequestRequestTypeDef = TypedDict(
    "DeleteGeoMatchSetRequestRequestTypeDef",
    {
        "GeoMatchSetId": str,
        "ChangeToken": str,
    },
)

DeleteGeoMatchSetResponseTypeDef = TypedDict(
    "DeleteGeoMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIPSetRequestRequestTypeDef = TypedDict(
    "DeleteIPSetRequestRequestTypeDef",
    {
        "IPSetId": str,
        "ChangeToken": str,
    },
)

DeleteIPSetResponseTypeDef = TypedDict(
    "DeleteIPSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

DeleteRateBasedRuleRequestRequestTypeDef = TypedDict(
    "DeleteRateBasedRuleRequestRequestTypeDef",
    {
        "RuleId": str,
        "ChangeToken": str,
    },
)

DeleteRateBasedRuleResponseTypeDef = TypedDict(
    "DeleteRateBasedRuleResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRegexMatchSetRequestRequestTypeDef = TypedDict(
    "DeleteRegexMatchSetRequestRequestTypeDef",
    {
        "RegexMatchSetId": str,
        "ChangeToken": str,
    },
)

DeleteRegexMatchSetResponseTypeDef = TypedDict(
    "DeleteRegexMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRegexPatternSetRequestRequestTypeDef = TypedDict(
    "DeleteRegexPatternSetRequestRequestTypeDef",
    {
        "RegexPatternSetId": str,
        "ChangeToken": str,
    },
)

DeleteRegexPatternSetResponseTypeDef = TypedDict(
    "DeleteRegexPatternSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRuleGroupRequestRequestTypeDef = TypedDict(
    "DeleteRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupId": str,
        "ChangeToken": str,
    },
)

DeleteRuleGroupResponseTypeDef = TypedDict(
    "DeleteRuleGroupResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRuleRequestRequestTypeDef = TypedDict(
    "DeleteRuleRequestRequestTypeDef",
    {
        "RuleId": str,
        "ChangeToken": str,
    },
)

DeleteRuleResponseTypeDef = TypedDict(
    "DeleteRuleResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSizeConstraintSetRequestRequestTypeDef = TypedDict(
    "DeleteSizeConstraintSetRequestRequestTypeDef",
    {
        "SizeConstraintSetId": str,
        "ChangeToken": str,
    },
)

DeleteSizeConstraintSetResponseTypeDef = TypedDict(
    "DeleteSizeConstraintSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSqlInjectionMatchSetRequestRequestTypeDef = TypedDict(
    "DeleteSqlInjectionMatchSetRequestRequestTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "ChangeToken": str,
    },
)

DeleteSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "DeleteSqlInjectionMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteWebACLRequestRequestTypeDef = TypedDict(
    "DeleteWebACLRequestRequestTypeDef",
    {
        "WebACLId": str,
        "ChangeToken": str,
    },
)

DeleteWebACLResponseTypeDef = TypedDict(
    "DeleteWebACLResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteXssMatchSetRequestRequestTypeDef = TypedDict(
    "DeleteXssMatchSetRequestRequestTypeDef",
    {
        "XssMatchSetId": str,
        "ChangeToken": str,
    },
)

DeleteXssMatchSetResponseTypeDef = TypedDict(
    "DeleteXssMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
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
        "RuleId": str,
    },
)

FieldToMatchTypeDef = TypedDict(
    "FieldToMatchTypeDef",
    {
        "Type": MatchFieldTypeType,
        "Data": NotRequired[str],
    },
)

GeoMatchConstraintTypeDef = TypedDict(
    "GeoMatchConstraintTypeDef",
    {
        "Type": Literal["Country"],
        "Value": GeoMatchConstraintValueType,
    },
)

GeoMatchSetSummaryTypeDef = TypedDict(
    "GeoMatchSetSummaryTypeDef",
    {
        "GeoMatchSetId": str,
        "Name": str,
    },
)

GeoMatchSetTypeDef = TypedDict(
    "GeoMatchSetTypeDef",
    {
        "GeoMatchSetId": str,
        "GeoMatchConstraints": List["GeoMatchConstraintTypeDef"],
        "Name": NotRequired[str],
    },
)

GeoMatchSetUpdateTypeDef = TypedDict(
    "GeoMatchSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "GeoMatchConstraint": "GeoMatchConstraintTypeDef",
    },
)

GetByteMatchSetRequestRequestTypeDef = TypedDict(
    "GetByteMatchSetRequestRequestTypeDef",
    {
        "ByteMatchSetId": str,
    },
)

GetByteMatchSetResponseTypeDef = TypedDict(
    "GetByteMatchSetResponseTypeDef",
    {
        "ByteMatchSet": "ByteMatchSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChangeTokenResponseTypeDef = TypedDict(
    "GetChangeTokenResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChangeTokenStatusRequestRequestTypeDef = TypedDict(
    "GetChangeTokenStatusRequestRequestTypeDef",
    {
        "ChangeToken": str,
    },
)

GetChangeTokenStatusResponseTypeDef = TypedDict(
    "GetChangeTokenStatusResponseTypeDef",
    {
        "ChangeTokenStatus": ChangeTokenStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGeoMatchSetRequestRequestTypeDef = TypedDict(
    "GetGeoMatchSetRequestRequestTypeDef",
    {
        "GeoMatchSetId": str,
    },
)

GetGeoMatchSetResponseTypeDef = TypedDict(
    "GetGeoMatchSetResponseTypeDef",
    {
        "GeoMatchSet": "GeoMatchSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIPSetRequestRequestTypeDef = TypedDict(
    "GetIPSetRequestRequestTypeDef",
    {
        "IPSetId": str,
    },
)

GetIPSetResponseTypeDef = TypedDict(
    "GetIPSetResponseTypeDef",
    {
        "IPSet": "IPSetTypeDef",
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

GetRateBasedRuleManagedKeysRequestRequestTypeDef = TypedDict(
    "GetRateBasedRuleManagedKeysRequestRequestTypeDef",
    {
        "RuleId": str,
        "NextMarker": NotRequired[str],
    },
)

GetRateBasedRuleManagedKeysResponseTypeDef = TypedDict(
    "GetRateBasedRuleManagedKeysResponseTypeDef",
    {
        "ManagedKeys": List[str],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRateBasedRuleRequestRequestTypeDef = TypedDict(
    "GetRateBasedRuleRequestRequestTypeDef",
    {
        "RuleId": str,
    },
)

GetRateBasedRuleResponseTypeDef = TypedDict(
    "GetRateBasedRuleResponseTypeDef",
    {
        "Rule": "RateBasedRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegexMatchSetRequestRequestTypeDef = TypedDict(
    "GetRegexMatchSetRequestRequestTypeDef",
    {
        "RegexMatchSetId": str,
    },
)

GetRegexMatchSetResponseTypeDef = TypedDict(
    "GetRegexMatchSetResponseTypeDef",
    {
        "RegexMatchSet": "RegexMatchSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegexPatternSetRequestRequestTypeDef = TypedDict(
    "GetRegexPatternSetRequestRequestTypeDef",
    {
        "RegexPatternSetId": str,
    },
)

GetRegexPatternSetResponseTypeDef = TypedDict(
    "GetRegexPatternSetResponseTypeDef",
    {
        "RegexPatternSet": "RegexPatternSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRuleGroupRequestRequestTypeDef = TypedDict(
    "GetRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupId": str,
    },
)

GetRuleGroupResponseTypeDef = TypedDict(
    "GetRuleGroupResponseTypeDef",
    {
        "RuleGroup": "RuleGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRuleRequestRequestTypeDef = TypedDict(
    "GetRuleRequestRequestTypeDef",
    {
        "RuleId": str,
    },
)

GetRuleResponseTypeDef = TypedDict(
    "GetRuleResponseTypeDef",
    {
        "Rule": "RuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSampledRequestsRequestRequestTypeDef = TypedDict(
    "GetSampledRequestsRequestRequestTypeDef",
    {
        "WebAclId": str,
        "RuleId": str,
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

GetSizeConstraintSetRequestRequestTypeDef = TypedDict(
    "GetSizeConstraintSetRequestRequestTypeDef",
    {
        "SizeConstraintSetId": str,
    },
)

GetSizeConstraintSetResponseTypeDef = TypedDict(
    "GetSizeConstraintSetResponseTypeDef",
    {
        "SizeConstraintSet": "SizeConstraintSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSqlInjectionMatchSetRequestRequestTypeDef = TypedDict(
    "GetSqlInjectionMatchSetRequestRequestTypeDef",
    {
        "SqlInjectionMatchSetId": str,
    },
)

GetSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "GetSqlInjectionMatchSetResponseTypeDef",
    {
        "SqlInjectionMatchSet": "SqlInjectionMatchSetTypeDef",
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
        "WebACLSummary": "WebACLSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWebACLRequestRequestTypeDef = TypedDict(
    "GetWebACLRequestRequestTypeDef",
    {
        "WebACLId": str,
    },
)

GetWebACLResponseTypeDef = TypedDict(
    "GetWebACLResponseTypeDef",
    {
        "WebACL": "WebACLTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetXssMatchSetRequestRequestTypeDef = TypedDict(
    "GetXssMatchSetRequestRequestTypeDef",
    {
        "XssMatchSetId": str,
    },
)

GetXssMatchSetResponseTypeDef = TypedDict(
    "GetXssMatchSetResponseTypeDef",
    {
        "XssMatchSet": "XssMatchSetTypeDef",
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

IPSetDescriptorTypeDef = TypedDict(
    "IPSetDescriptorTypeDef",
    {
        "Type": IPSetDescriptorTypeType,
        "Value": str,
    },
)

IPSetSummaryTypeDef = TypedDict(
    "IPSetSummaryTypeDef",
    {
        "IPSetId": str,
        "Name": str,
    },
)

IPSetTypeDef = TypedDict(
    "IPSetTypeDef",
    {
        "IPSetId": str,
        "IPSetDescriptors": List["IPSetDescriptorTypeDef"],
        "Name": NotRequired[str],
    },
)

IPSetUpdateTypeDef = TypedDict(
    "IPSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "IPSetDescriptor": "IPSetDescriptorTypeDef",
    },
)

ListActivatedRulesInRuleGroupRequestRequestTypeDef = TypedDict(
    "ListActivatedRulesInRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupId": NotRequired[str],
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListActivatedRulesInRuleGroupResponseTypeDef = TypedDict(
    "ListActivatedRulesInRuleGroupResponseTypeDef",
    {
        "NextMarker": str,
        "ActivatedRules": List["ActivatedRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListByteMatchSetsRequestRequestTypeDef = TypedDict(
    "ListByteMatchSetsRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListByteMatchSetsResponseTypeDef = TypedDict(
    "ListByteMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "ByteMatchSets": List["ByteMatchSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGeoMatchSetsRequestRequestTypeDef = TypedDict(
    "ListGeoMatchSetsRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListGeoMatchSetsResponseTypeDef = TypedDict(
    "ListGeoMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "GeoMatchSets": List["GeoMatchSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIPSetsRequestRequestTypeDef = TypedDict(
    "ListIPSetsRequestRequestTypeDef",
    {
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

ListRateBasedRulesRequestRequestTypeDef = TypedDict(
    "ListRateBasedRulesRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListRateBasedRulesResponseTypeDef = TypedDict(
    "ListRateBasedRulesResponseTypeDef",
    {
        "NextMarker": str,
        "Rules": List["RuleSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRegexMatchSetsRequestRequestTypeDef = TypedDict(
    "ListRegexMatchSetsRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListRegexMatchSetsResponseTypeDef = TypedDict(
    "ListRegexMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "RegexMatchSets": List["RegexMatchSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRegexPatternSetsRequestRequestTypeDef = TypedDict(
    "ListRegexPatternSetsRequestRequestTypeDef",
    {
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
        "WebACLId": str,
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

ListRulesRequestRequestTypeDef = TypedDict(
    "ListRulesRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListRulesResponseTypeDef = TypedDict(
    "ListRulesResponseTypeDef",
    {
        "NextMarker": str,
        "Rules": List["RuleSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSizeConstraintSetsRequestRequestTypeDef = TypedDict(
    "ListSizeConstraintSetsRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListSizeConstraintSetsResponseTypeDef = TypedDict(
    "ListSizeConstraintSetsResponseTypeDef",
    {
        "NextMarker": str,
        "SizeConstraintSets": List["SizeConstraintSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSqlInjectionMatchSetsRequestRequestTypeDef = TypedDict(
    "ListSqlInjectionMatchSetsRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListSqlInjectionMatchSetsResponseTypeDef = TypedDict(
    "ListSqlInjectionMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "SqlInjectionMatchSets": List["SqlInjectionMatchSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSubscribedRuleGroupsRequestRequestTypeDef = TypedDict(
    "ListSubscribedRuleGroupsRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListSubscribedRuleGroupsResponseTypeDef = TypedDict(
    "ListSubscribedRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "RuleGroups": List["SubscribedRuleGroupSummaryTypeDef"],
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

ListXssMatchSetsRequestRequestTypeDef = TypedDict(
    "ListXssMatchSetsRequestRequestTypeDef",
    {
        "NextMarker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListXssMatchSetsResponseTypeDef = TypedDict(
    "ListXssMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "XssMatchSets": List["XssMatchSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": List[str],
        "RedactedFields": NotRequired[List["FieldToMatchTypeDef"]],
    },
)

PredicateTypeDef = TypedDict(
    "PredicateTypeDef",
    {
        "Negated": bool,
        "Type": PredicateTypeType,
        "DataId": str,
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

PutPermissionPolicyRequestRequestTypeDef = TypedDict(
    "PutPermissionPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
    },
)

RateBasedRuleTypeDef = TypedDict(
    "RateBasedRuleTypeDef",
    {
        "RuleId": str,
        "MatchPredicates": List["PredicateTypeDef"],
        "RateKey": Literal["IP"],
        "RateLimit": int,
        "Name": NotRequired[str],
        "MetricName": NotRequired[str],
    },
)

RegexMatchSetSummaryTypeDef = TypedDict(
    "RegexMatchSetSummaryTypeDef",
    {
        "RegexMatchSetId": str,
        "Name": str,
    },
)

RegexMatchSetTypeDef = TypedDict(
    "RegexMatchSetTypeDef",
    {
        "RegexMatchSetId": NotRequired[str],
        "Name": NotRequired[str],
        "RegexMatchTuples": NotRequired[List["RegexMatchTupleTypeDef"]],
    },
)

RegexMatchSetUpdateTypeDef = TypedDict(
    "RegexMatchSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "RegexMatchTuple": "RegexMatchTupleTypeDef",
    },
)

RegexMatchTupleTypeDef = TypedDict(
    "RegexMatchTupleTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformation": TextTransformationType,
        "RegexPatternSetId": str,
    },
)

RegexPatternSetSummaryTypeDef = TypedDict(
    "RegexPatternSetSummaryTypeDef",
    {
        "RegexPatternSetId": str,
        "Name": str,
    },
)

RegexPatternSetTypeDef = TypedDict(
    "RegexPatternSetTypeDef",
    {
        "RegexPatternSetId": str,
        "RegexPatternStrings": List[str],
        "Name": NotRequired[str],
    },
)

RegexPatternSetUpdateTypeDef = TypedDict(
    "RegexPatternSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "RegexPatternString": str,
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

RuleGroupSummaryTypeDef = TypedDict(
    "RuleGroupSummaryTypeDef",
    {
        "RuleGroupId": str,
        "Name": str,
    },
)

RuleGroupTypeDef = TypedDict(
    "RuleGroupTypeDef",
    {
        "RuleGroupId": str,
        "Name": NotRequired[str],
        "MetricName": NotRequired[str],
    },
)

RuleGroupUpdateTypeDef = TypedDict(
    "RuleGroupUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "ActivatedRule": "ActivatedRuleTypeDef",
    },
)

RuleSummaryTypeDef = TypedDict(
    "RuleSummaryTypeDef",
    {
        "RuleId": str,
        "Name": str,
    },
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "RuleId": str,
        "Predicates": List["PredicateTypeDef"],
        "Name": NotRequired[str],
        "MetricName": NotRequired[str],
    },
)

RuleUpdateTypeDef = TypedDict(
    "RuleUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "Predicate": "PredicateTypeDef",
    },
)

SampledHTTPRequestTypeDef = TypedDict(
    "SampledHTTPRequestTypeDef",
    {
        "Request": "HTTPRequestTypeDef",
        "Weight": int,
        "Timestamp": NotRequired[datetime],
        "Action": NotRequired[str],
        "RuleWithinRuleGroup": NotRequired[str],
    },
)

SizeConstraintSetSummaryTypeDef = TypedDict(
    "SizeConstraintSetSummaryTypeDef",
    {
        "SizeConstraintSetId": str,
        "Name": str,
    },
)

SizeConstraintSetTypeDef = TypedDict(
    "SizeConstraintSetTypeDef",
    {
        "SizeConstraintSetId": str,
        "SizeConstraints": List["SizeConstraintTypeDef"],
        "Name": NotRequired[str],
    },
)

SizeConstraintSetUpdateTypeDef = TypedDict(
    "SizeConstraintSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "SizeConstraint": "SizeConstraintTypeDef",
    },
)

SizeConstraintTypeDef = TypedDict(
    "SizeConstraintTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformation": TextTransformationType,
        "ComparisonOperator": ComparisonOperatorType,
        "Size": int,
    },
)

SqlInjectionMatchSetSummaryTypeDef = TypedDict(
    "SqlInjectionMatchSetSummaryTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "Name": str,
    },
)

SqlInjectionMatchSetTypeDef = TypedDict(
    "SqlInjectionMatchSetTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "SqlInjectionMatchTuples": List["SqlInjectionMatchTupleTypeDef"],
        "Name": NotRequired[str],
    },
)

SqlInjectionMatchSetUpdateTypeDef = TypedDict(
    "SqlInjectionMatchSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "SqlInjectionMatchTuple": "SqlInjectionMatchTupleTypeDef",
    },
)

SqlInjectionMatchTupleTypeDef = TypedDict(
    "SqlInjectionMatchTupleTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformation": TextTransformationType,
    },
)

SubscribedRuleGroupSummaryTypeDef = TypedDict(
    "SubscribedRuleGroupSummaryTypeDef",
    {
        "RuleGroupId": str,
        "Name": str,
        "MetricName": str,
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

UpdateByteMatchSetRequestRequestTypeDef = TypedDict(
    "UpdateByteMatchSetRequestRequestTypeDef",
    {
        "ByteMatchSetId": str,
        "ChangeToken": str,
        "Updates": Sequence["ByteMatchSetUpdateTypeDef"],
    },
)

UpdateByteMatchSetResponseTypeDef = TypedDict(
    "UpdateByteMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGeoMatchSetRequestRequestTypeDef = TypedDict(
    "UpdateGeoMatchSetRequestRequestTypeDef",
    {
        "GeoMatchSetId": str,
        "ChangeToken": str,
        "Updates": Sequence["GeoMatchSetUpdateTypeDef"],
    },
)

UpdateGeoMatchSetResponseTypeDef = TypedDict(
    "UpdateGeoMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateIPSetRequestRequestTypeDef = TypedDict(
    "UpdateIPSetRequestRequestTypeDef",
    {
        "IPSetId": str,
        "ChangeToken": str,
        "Updates": Sequence["IPSetUpdateTypeDef"],
    },
)

UpdateIPSetResponseTypeDef = TypedDict(
    "UpdateIPSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRateBasedRuleRequestRequestTypeDef = TypedDict(
    "UpdateRateBasedRuleRequestRequestTypeDef",
    {
        "RuleId": str,
        "ChangeToken": str,
        "Updates": Sequence["RuleUpdateTypeDef"],
        "RateLimit": int,
    },
)

UpdateRateBasedRuleResponseTypeDef = TypedDict(
    "UpdateRateBasedRuleResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRegexMatchSetRequestRequestTypeDef = TypedDict(
    "UpdateRegexMatchSetRequestRequestTypeDef",
    {
        "RegexMatchSetId": str,
        "Updates": Sequence["RegexMatchSetUpdateTypeDef"],
        "ChangeToken": str,
    },
)

UpdateRegexMatchSetResponseTypeDef = TypedDict(
    "UpdateRegexMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRegexPatternSetRequestRequestTypeDef = TypedDict(
    "UpdateRegexPatternSetRequestRequestTypeDef",
    {
        "RegexPatternSetId": str,
        "Updates": Sequence["RegexPatternSetUpdateTypeDef"],
        "ChangeToken": str,
    },
)

UpdateRegexPatternSetResponseTypeDef = TypedDict(
    "UpdateRegexPatternSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRuleGroupRequestRequestTypeDef = TypedDict(
    "UpdateRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupId": str,
        "Updates": Sequence["RuleGroupUpdateTypeDef"],
        "ChangeToken": str,
    },
)

UpdateRuleGroupResponseTypeDef = TypedDict(
    "UpdateRuleGroupResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRuleRequestRequestTypeDef = TypedDict(
    "UpdateRuleRequestRequestTypeDef",
    {
        "RuleId": str,
        "ChangeToken": str,
        "Updates": Sequence["RuleUpdateTypeDef"],
    },
)

UpdateRuleResponseTypeDef = TypedDict(
    "UpdateRuleResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSizeConstraintSetRequestRequestTypeDef = TypedDict(
    "UpdateSizeConstraintSetRequestRequestTypeDef",
    {
        "SizeConstraintSetId": str,
        "ChangeToken": str,
        "Updates": Sequence["SizeConstraintSetUpdateTypeDef"],
    },
)

UpdateSizeConstraintSetResponseTypeDef = TypedDict(
    "UpdateSizeConstraintSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSqlInjectionMatchSetRequestRequestTypeDef = TypedDict(
    "UpdateSqlInjectionMatchSetRequestRequestTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "ChangeToken": str,
        "Updates": Sequence["SqlInjectionMatchSetUpdateTypeDef"],
    },
)

UpdateSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "UpdateSqlInjectionMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateWebACLRequestRequestTypeDef = TypedDict(
    "UpdateWebACLRequestRequestTypeDef",
    {
        "WebACLId": str,
        "ChangeToken": str,
        "Updates": NotRequired[Sequence["WebACLUpdateTypeDef"]],
        "DefaultAction": NotRequired["WafActionTypeDef"],
    },
)

UpdateWebACLResponseTypeDef = TypedDict(
    "UpdateWebACLResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateXssMatchSetRequestRequestTypeDef = TypedDict(
    "UpdateXssMatchSetRequestRequestTypeDef",
    {
        "XssMatchSetId": str,
        "ChangeToken": str,
        "Updates": Sequence["XssMatchSetUpdateTypeDef"],
    },
)

UpdateXssMatchSetResponseTypeDef = TypedDict(
    "UpdateXssMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WafActionTypeDef = TypedDict(
    "WafActionTypeDef",
    {
        "Type": WafActionTypeType,
    },
)

WafOverrideActionTypeDef = TypedDict(
    "WafOverrideActionTypeDef",
    {
        "Type": WafOverrideActionTypeType,
    },
)

WebACLSummaryTypeDef = TypedDict(
    "WebACLSummaryTypeDef",
    {
        "WebACLId": str,
        "Name": str,
    },
)

WebACLTypeDef = TypedDict(
    "WebACLTypeDef",
    {
        "WebACLId": str,
        "DefaultAction": "WafActionTypeDef",
        "Rules": List["ActivatedRuleTypeDef"],
        "Name": NotRequired[str],
        "MetricName": NotRequired[str],
        "WebACLArn": NotRequired[str],
    },
)

WebACLUpdateTypeDef = TypedDict(
    "WebACLUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "ActivatedRule": "ActivatedRuleTypeDef",
    },
)

XssMatchSetSummaryTypeDef = TypedDict(
    "XssMatchSetSummaryTypeDef",
    {
        "XssMatchSetId": str,
        "Name": str,
    },
)

XssMatchSetTypeDef = TypedDict(
    "XssMatchSetTypeDef",
    {
        "XssMatchSetId": str,
        "XssMatchTuples": List["XssMatchTupleTypeDef"],
        "Name": NotRequired[str],
    },
)

XssMatchSetUpdateTypeDef = TypedDict(
    "XssMatchSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "XssMatchTuple": "XssMatchTupleTypeDef",
    },
)

XssMatchTupleTypeDef = TypedDict(
    "XssMatchTupleTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformation": TextTransformationType,
    },
)
