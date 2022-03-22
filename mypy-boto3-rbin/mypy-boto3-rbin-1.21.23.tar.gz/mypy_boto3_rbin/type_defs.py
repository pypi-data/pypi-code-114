"""
Type annotations for rbin service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/type_defs.html)

Usage::

    ```python
    from mypy_boto3_rbin.type_defs import CreateRuleRequestRequestTypeDef

    data: CreateRuleRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import ResourceTypeType, RuleStatusType

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateRuleRequestRequestTypeDef",
    "CreateRuleResponseTypeDef",
    "DeleteRuleRequestRequestTypeDef",
    "GetRuleRequestRequestTypeDef",
    "GetRuleResponseTypeDef",
    "ListRulesRequestRequestTypeDef",
    "ListRulesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceTagTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionPeriodTypeDef",
    "RuleSummaryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateRuleRequestRequestTypeDef",
    "UpdateRuleResponseTypeDef",
)

CreateRuleRequestRequestTypeDef = TypedDict(
    "CreateRuleRequestRequestTypeDef",
    {
        "RetentionPeriod": "RetentionPeriodTypeDef",
        "ResourceType": ResourceTypeType,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ResourceTags": NotRequired[Sequence["ResourceTagTypeDef"]],
    },
)

CreateRuleResponseTypeDef = TypedDict(
    "CreateRuleResponseTypeDef",
    {
        "Identifier": str,
        "RetentionPeriod": "RetentionPeriodTypeDef",
        "Description": str,
        "Tags": List["TagTypeDef"],
        "ResourceType": ResourceTypeType,
        "ResourceTags": List["ResourceTagTypeDef"],
        "Status": RuleStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRuleRequestRequestTypeDef = TypedDict(
    "DeleteRuleRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetRuleRequestRequestTypeDef = TypedDict(
    "GetRuleRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetRuleResponseTypeDef = TypedDict(
    "GetRuleResponseTypeDef",
    {
        "Identifier": str,
        "Description": str,
        "ResourceType": ResourceTypeType,
        "RetentionPeriod": "RetentionPeriodTypeDef",
        "ResourceTags": List["ResourceTagTypeDef"],
        "Status": RuleStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRulesRequestRequestTypeDef = TypedDict(
    "ListRulesRequestRequestTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ResourceTags": NotRequired[Sequence["ResourceTagTypeDef"]],
    },
)

ListRulesResponseTypeDef = TypedDict(
    "ListRulesResponseTypeDef",
    {
        "Rules": List["RuleSummaryTypeDef"],
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
        "Tags": List["TagTypeDef"],
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

ResourceTagTypeDef = TypedDict(
    "ResourceTagTypeDef",
    {
        "ResourceTagKey": str,
        "ResourceTagValue": NotRequired[str],
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

RetentionPeriodTypeDef = TypedDict(
    "RetentionPeriodTypeDef",
    {
        "RetentionPeriodValue": int,
        "RetentionPeriodUnit": Literal["DAYS"],
    },
)

RuleSummaryTypeDef = TypedDict(
    "RuleSummaryTypeDef",
    {
        "Identifier": NotRequired[str],
        "Description": NotRequired[str],
        "RetentionPeriod": NotRequired["RetentionPeriodTypeDef"],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
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

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateRuleRequestRequestTypeDef = TypedDict(
    "UpdateRuleRequestRequestTypeDef",
    {
        "Identifier": str,
        "RetentionPeriod": NotRequired["RetentionPeriodTypeDef"],
        "Description": NotRequired[str],
        "ResourceType": NotRequired[ResourceTypeType],
        "ResourceTags": NotRequired[Sequence["ResourceTagTypeDef"]],
    },
)

UpdateRuleResponseTypeDef = TypedDict(
    "UpdateRuleResponseTypeDef",
    {
        "Identifier": str,
        "RetentionPeriod": "RetentionPeriodTypeDef",
        "Description": str,
        "ResourceType": ResourceTypeType,
        "ResourceTags": List["ResourceTagTypeDef"],
        "Status": RuleStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
