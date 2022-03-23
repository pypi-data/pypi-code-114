"""
Type annotations for route53-recovery-control-config service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_route53_recovery_control_config.type_defs import AssertionRuleTypeDef

    data: AssertionRuleTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import RuleTypeType, StatusType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssertionRuleTypeDef",
    "AssertionRuleUpdateTypeDef",
    "ClusterEndpointTypeDef",
    "ClusterTypeDef",
    "ControlPanelTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateControlPanelRequestRequestTypeDef",
    "CreateControlPanelResponseTypeDef",
    "CreateRoutingControlRequestRequestTypeDef",
    "CreateRoutingControlResponseTypeDef",
    "CreateSafetyRuleRequestRequestTypeDef",
    "CreateSafetyRuleResponseTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteControlPanelRequestRequestTypeDef",
    "DeleteRoutingControlRequestRequestTypeDef",
    "DeleteSafetyRuleRequestRequestTypeDef",
    "DescribeClusterRequestRequestTypeDef",
    "DescribeClusterResponseTypeDef",
    "DescribeControlPanelRequestRequestTypeDef",
    "DescribeControlPanelResponseTypeDef",
    "DescribeRoutingControlRequestRequestTypeDef",
    "DescribeRoutingControlResponseTypeDef",
    "DescribeSafetyRuleRequestRequestTypeDef",
    "DescribeSafetyRuleResponseTypeDef",
    "GatingRuleTypeDef",
    "GatingRuleUpdateTypeDef",
    "ListAssociatedRoute53HealthChecksRequestRequestTypeDef",
    "ListAssociatedRoute53HealthChecksResponseTypeDef",
    "ListClustersRequestRequestTypeDef",
    "ListClustersResponseTypeDef",
    "ListControlPanelsRequestRequestTypeDef",
    "ListControlPanelsResponseTypeDef",
    "ListRoutingControlsRequestRequestTypeDef",
    "ListRoutingControlsResponseTypeDef",
    "ListSafetyRulesRequestRequestTypeDef",
    "ListSafetyRulesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NewAssertionRuleTypeDef",
    "NewGatingRuleTypeDef",
    "ResponseMetadataTypeDef",
    "RoutingControlTypeDef",
    "RuleConfigTypeDef",
    "RuleTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateControlPanelRequestRequestTypeDef",
    "UpdateControlPanelResponseTypeDef",
    "UpdateRoutingControlRequestRequestTypeDef",
    "UpdateRoutingControlResponseTypeDef",
    "UpdateSafetyRuleRequestRequestTypeDef",
    "UpdateSafetyRuleResponseTypeDef",
    "WaiterConfigTypeDef",
)

AssertionRuleTypeDef = TypedDict(
    "AssertionRuleTypeDef",
    {
        "AssertedControls": List[str],
        "ControlPanelArn": str,
        "Name": str,
        "RuleConfig": "RuleConfigTypeDef",
        "SafetyRuleArn": str,
        "Status": StatusType,
        "WaitPeriodMs": int,
    },
)

AssertionRuleUpdateTypeDef = TypedDict(
    "AssertionRuleUpdateTypeDef",
    {
        "Name": str,
        "SafetyRuleArn": str,
        "WaitPeriodMs": int,
    },
)

ClusterEndpointTypeDef = TypedDict(
    "ClusterEndpointTypeDef",
    {
        "Endpoint": NotRequired[str],
        "Region": NotRequired[str],
    },
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "ClusterArn": NotRequired[str],
        "ClusterEndpoints": NotRequired[List["ClusterEndpointTypeDef"]],
        "Name": NotRequired[str],
        "Status": NotRequired[StatusType],
    },
)

ControlPanelTypeDef = TypedDict(
    "ControlPanelTypeDef",
    {
        "ClusterArn": NotRequired[str],
        "ControlPanelArn": NotRequired[str],
        "DefaultControlPanel": NotRequired[bool],
        "Name": NotRequired[str],
        "RoutingControlCount": NotRequired[int],
        "Status": NotRequired[StatusType],
    },
)

CreateClusterRequestRequestTypeDef = TypedDict(
    "CreateClusterRequestRequestTypeDef",
    {
        "ClusterName": str,
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateControlPanelRequestRequestTypeDef = TypedDict(
    "CreateControlPanelRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "ControlPanelName": str,
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateControlPanelResponseTypeDef = TypedDict(
    "CreateControlPanelResponseTypeDef",
    {
        "ControlPanel": "ControlPanelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRoutingControlRequestRequestTypeDef = TypedDict(
    "CreateRoutingControlRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "RoutingControlName": str,
        "ClientToken": NotRequired[str],
        "ControlPanelArn": NotRequired[str],
    },
)

CreateRoutingControlResponseTypeDef = TypedDict(
    "CreateRoutingControlResponseTypeDef",
    {
        "RoutingControl": "RoutingControlTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSafetyRuleRequestRequestTypeDef = TypedDict(
    "CreateSafetyRuleRequestRequestTypeDef",
    {
        "AssertionRule": NotRequired["NewAssertionRuleTypeDef"],
        "ClientToken": NotRequired[str],
        "GatingRule": NotRequired["NewGatingRuleTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateSafetyRuleResponseTypeDef = TypedDict(
    "CreateSafetyRuleResponseTypeDef",
    {
        "AssertionRule": "AssertionRuleTypeDef",
        "GatingRule": "GatingRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterRequestRequestTypeDef = TypedDict(
    "DeleteClusterRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)

DeleteControlPanelRequestRequestTypeDef = TypedDict(
    "DeleteControlPanelRequestRequestTypeDef",
    {
        "ControlPanelArn": str,
    },
)

DeleteRoutingControlRequestRequestTypeDef = TypedDict(
    "DeleteRoutingControlRequestRequestTypeDef",
    {
        "RoutingControlArn": str,
    },
)

DeleteSafetyRuleRequestRequestTypeDef = TypedDict(
    "DeleteSafetyRuleRequestRequestTypeDef",
    {
        "SafetyRuleArn": str,
    },
)

DescribeClusterRequestRequestTypeDef = TypedDict(
    "DescribeClusterRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)

DescribeClusterResponseTypeDef = TypedDict(
    "DescribeClusterResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeControlPanelRequestRequestTypeDef = TypedDict(
    "DescribeControlPanelRequestRequestTypeDef",
    {
        "ControlPanelArn": str,
    },
)

DescribeControlPanelResponseTypeDef = TypedDict(
    "DescribeControlPanelResponseTypeDef",
    {
        "ControlPanel": "ControlPanelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRoutingControlRequestRequestTypeDef = TypedDict(
    "DescribeRoutingControlRequestRequestTypeDef",
    {
        "RoutingControlArn": str,
    },
)

DescribeRoutingControlResponseTypeDef = TypedDict(
    "DescribeRoutingControlResponseTypeDef",
    {
        "RoutingControl": "RoutingControlTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSafetyRuleRequestRequestTypeDef = TypedDict(
    "DescribeSafetyRuleRequestRequestTypeDef",
    {
        "SafetyRuleArn": str,
    },
)

DescribeSafetyRuleResponseTypeDef = TypedDict(
    "DescribeSafetyRuleResponseTypeDef",
    {
        "AssertionRule": "AssertionRuleTypeDef",
        "GatingRule": "GatingRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GatingRuleTypeDef = TypedDict(
    "GatingRuleTypeDef",
    {
        "ControlPanelArn": str,
        "GatingControls": List[str],
        "Name": str,
        "RuleConfig": "RuleConfigTypeDef",
        "SafetyRuleArn": str,
        "Status": StatusType,
        "TargetControls": List[str],
        "WaitPeriodMs": int,
    },
)

GatingRuleUpdateTypeDef = TypedDict(
    "GatingRuleUpdateTypeDef",
    {
        "Name": str,
        "SafetyRuleArn": str,
        "WaitPeriodMs": int,
    },
)

ListAssociatedRoute53HealthChecksRequestRequestTypeDef = TypedDict(
    "ListAssociatedRoute53HealthChecksRequestRequestTypeDef",
    {
        "RoutingControlArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAssociatedRoute53HealthChecksResponseTypeDef = TypedDict(
    "ListAssociatedRoute53HealthChecksResponseTypeDef",
    {
        "HealthCheckIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClustersRequestRequestTypeDef = TypedDict(
    "ListClustersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef",
    {
        "Clusters": List["ClusterTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListControlPanelsRequestRequestTypeDef = TypedDict(
    "ListControlPanelsRequestRequestTypeDef",
    {
        "ClusterArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListControlPanelsResponseTypeDef = TypedDict(
    "ListControlPanelsResponseTypeDef",
    {
        "ControlPanels": List["ControlPanelTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRoutingControlsRequestRequestTypeDef = TypedDict(
    "ListRoutingControlsRequestRequestTypeDef",
    {
        "ControlPanelArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListRoutingControlsResponseTypeDef = TypedDict(
    "ListRoutingControlsResponseTypeDef",
    {
        "NextToken": str,
        "RoutingControls": List["RoutingControlTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSafetyRulesRequestRequestTypeDef = TypedDict(
    "ListSafetyRulesRequestRequestTypeDef",
    {
        "ControlPanelArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListSafetyRulesResponseTypeDef = TypedDict(
    "ListSafetyRulesResponseTypeDef",
    {
        "NextToken": str,
        "SafetyRules": List["RuleTypeDef"],
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

NewAssertionRuleTypeDef = TypedDict(
    "NewAssertionRuleTypeDef",
    {
        "AssertedControls": Sequence[str],
        "ControlPanelArn": str,
        "Name": str,
        "RuleConfig": "RuleConfigTypeDef",
        "WaitPeriodMs": int,
    },
)

NewGatingRuleTypeDef = TypedDict(
    "NewGatingRuleTypeDef",
    {
        "ControlPanelArn": str,
        "GatingControls": Sequence[str],
        "Name": str,
        "RuleConfig": "RuleConfigTypeDef",
        "TargetControls": Sequence[str],
        "WaitPeriodMs": int,
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

RoutingControlTypeDef = TypedDict(
    "RoutingControlTypeDef",
    {
        "ControlPanelArn": NotRequired[str],
        "Name": NotRequired[str],
        "RoutingControlArn": NotRequired[str],
        "Status": NotRequired[StatusType],
    },
)

RuleConfigTypeDef = TypedDict(
    "RuleConfigTypeDef",
    {
        "Inverted": bool,
        "Threshold": int,
        "Type": RuleTypeType,
    },
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "ASSERTION": NotRequired["AssertionRuleTypeDef"],
        "GATING": NotRequired["GatingRuleTypeDef"],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateControlPanelRequestRequestTypeDef = TypedDict(
    "UpdateControlPanelRequestRequestTypeDef",
    {
        "ControlPanelArn": str,
        "ControlPanelName": str,
    },
)

UpdateControlPanelResponseTypeDef = TypedDict(
    "UpdateControlPanelResponseTypeDef",
    {
        "ControlPanel": "ControlPanelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRoutingControlRequestRequestTypeDef = TypedDict(
    "UpdateRoutingControlRequestRequestTypeDef",
    {
        "RoutingControlArn": str,
        "RoutingControlName": str,
    },
)

UpdateRoutingControlResponseTypeDef = TypedDict(
    "UpdateRoutingControlResponseTypeDef",
    {
        "RoutingControl": "RoutingControlTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSafetyRuleRequestRequestTypeDef = TypedDict(
    "UpdateSafetyRuleRequestRequestTypeDef",
    {
        "AssertionRuleUpdate": NotRequired["AssertionRuleUpdateTypeDef"],
        "GatingRuleUpdate": NotRequired["GatingRuleUpdateTypeDef"],
    },
)

UpdateSafetyRuleResponseTypeDef = TypedDict(
    "UpdateSafetyRuleResponseTypeDef",
    {
        "AssertionRule": "AssertionRuleTypeDef",
        "GatingRule": "GatingRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
