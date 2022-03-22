"""
Type annotations for network-firewall service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/type_defs.html)

Usage::

    ```python
    from mypy_boto3_network_firewall.type_defs import ActionDefinitionTypeDef

    data: ActionDefinitionTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AttachmentStatusType,
    ConfigurationSyncStateType,
    FirewallStatusValueType,
    GeneratedRulesTypeType,
    LogDestinationTypeType,
    LogTypeType,
    PerObjectSyncStatusType,
    ResourceManagedStatusType,
    ResourceStatusType,
    RuleGroupTypeType,
    RuleOrderType,
    StatefulActionType,
    StatefulRuleDirectionType,
    StatefulRuleProtocolType,
    TargetTypeType,
    TCPFlagType,
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
    "ActionDefinitionTypeDef",
    "AddressTypeDef",
    "AssociateFirewallPolicyRequestRequestTypeDef",
    "AssociateFirewallPolicyResponseTypeDef",
    "AssociateSubnetsRequestRequestTypeDef",
    "AssociateSubnetsResponseTypeDef",
    "AttachmentTypeDef",
    "CreateFirewallPolicyRequestRequestTypeDef",
    "CreateFirewallPolicyResponseTypeDef",
    "CreateFirewallRequestRequestTypeDef",
    "CreateFirewallResponseTypeDef",
    "CreateRuleGroupRequestRequestTypeDef",
    "CreateRuleGroupResponseTypeDef",
    "CustomActionTypeDef",
    "DeleteFirewallPolicyRequestRequestTypeDef",
    "DeleteFirewallPolicyResponseTypeDef",
    "DeleteFirewallRequestRequestTypeDef",
    "DeleteFirewallResponseTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteRuleGroupRequestRequestTypeDef",
    "DeleteRuleGroupResponseTypeDef",
    "DescribeFirewallPolicyRequestRequestTypeDef",
    "DescribeFirewallPolicyResponseTypeDef",
    "DescribeFirewallRequestRequestTypeDef",
    "DescribeFirewallResponseTypeDef",
    "DescribeLoggingConfigurationRequestRequestTypeDef",
    "DescribeLoggingConfigurationResponseTypeDef",
    "DescribeResourcePolicyRequestRequestTypeDef",
    "DescribeResourcePolicyResponseTypeDef",
    "DescribeRuleGroupMetadataRequestRequestTypeDef",
    "DescribeRuleGroupMetadataResponseTypeDef",
    "DescribeRuleGroupRequestRequestTypeDef",
    "DescribeRuleGroupResponseTypeDef",
    "DimensionTypeDef",
    "DisassociateSubnetsRequestRequestTypeDef",
    "DisassociateSubnetsResponseTypeDef",
    "FirewallMetadataTypeDef",
    "FirewallPolicyMetadataTypeDef",
    "FirewallPolicyResponseTypeDef",
    "FirewallPolicyTypeDef",
    "FirewallStatusTypeDef",
    "FirewallTypeDef",
    "HeaderTypeDef",
    "IPSetTypeDef",
    "ListFirewallPoliciesRequestRequestTypeDef",
    "ListFirewallPoliciesResponseTypeDef",
    "ListFirewallsRequestRequestTypeDef",
    "ListFirewallsResponseTypeDef",
    "ListRuleGroupsRequestRequestTypeDef",
    "ListRuleGroupsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogDestinationConfigTypeDef",
    "LoggingConfigurationTypeDef",
    "MatchAttributesTypeDef",
    "PaginatorConfigTypeDef",
    "PerObjectStatusTypeDef",
    "PortRangeTypeDef",
    "PortSetTypeDef",
    "PublishMetricActionTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RuleDefinitionTypeDef",
    "RuleGroupMetadataTypeDef",
    "RuleGroupResponseTypeDef",
    "RuleGroupTypeDef",
    "RuleOptionTypeDef",
    "RuleVariablesTypeDef",
    "RulesSourceListTypeDef",
    "RulesSourceTypeDef",
    "StatefulEngineOptionsTypeDef",
    "StatefulRuleGroupOverrideTypeDef",
    "StatefulRuleGroupReferenceTypeDef",
    "StatefulRuleOptionsTypeDef",
    "StatefulRuleTypeDef",
    "StatelessRuleGroupReferenceTypeDef",
    "StatelessRuleTypeDef",
    "StatelessRulesAndCustomActionsTypeDef",
    "SubnetMappingTypeDef",
    "SyncStateTypeDef",
    "TCPFlagFieldTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateFirewallDeleteProtectionRequestRequestTypeDef",
    "UpdateFirewallDeleteProtectionResponseTypeDef",
    "UpdateFirewallDescriptionRequestRequestTypeDef",
    "UpdateFirewallDescriptionResponseTypeDef",
    "UpdateFirewallPolicyChangeProtectionRequestRequestTypeDef",
    "UpdateFirewallPolicyChangeProtectionResponseTypeDef",
    "UpdateFirewallPolicyRequestRequestTypeDef",
    "UpdateFirewallPolicyResponseTypeDef",
    "UpdateLoggingConfigurationRequestRequestTypeDef",
    "UpdateLoggingConfigurationResponseTypeDef",
    "UpdateRuleGroupRequestRequestTypeDef",
    "UpdateRuleGroupResponseTypeDef",
    "UpdateSubnetChangeProtectionRequestRequestTypeDef",
    "UpdateSubnetChangeProtectionResponseTypeDef",
)

ActionDefinitionTypeDef = TypedDict(
    "ActionDefinitionTypeDef",
    {
        "PublishMetricAction": NotRequired["PublishMetricActionTypeDef"],
    },
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "AddressDefinition": str,
    },
)

AssociateFirewallPolicyRequestRequestTypeDef = TypedDict(
    "AssociateFirewallPolicyRequestRequestTypeDef",
    {
        "FirewallPolicyArn": str,
        "UpdateToken": NotRequired[str],
        "FirewallArn": NotRequired[str],
        "FirewallName": NotRequired[str],
    },
)

AssociateFirewallPolicyResponseTypeDef = TypedDict(
    "AssociateFirewallPolicyResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "FirewallPolicyArn": str,
        "UpdateToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateSubnetsRequestRequestTypeDef = TypedDict(
    "AssociateSubnetsRequestRequestTypeDef",
    {
        "SubnetMappings": Sequence["SubnetMappingTypeDef"],
        "UpdateToken": NotRequired[str],
        "FirewallArn": NotRequired[str],
        "FirewallName": NotRequired[str],
    },
)

AssociateSubnetsResponseTypeDef = TypedDict(
    "AssociateSubnetsResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "SubnetMappings": List["SubnetMappingTypeDef"],
        "UpdateToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachmentTypeDef = TypedDict(
    "AttachmentTypeDef",
    {
        "SubnetId": NotRequired[str],
        "EndpointId": NotRequired[str],
        "Status": NotRequired[AttachmentStatusType],
    },
)

CreateFirewallPolicyRequestRequestTypeDef = TypedDict(
    "CreateFirewallPolicyRequestRequestTypeDef",
    {
        "FirewallPolicyName": str,
        "FirewallPolicy": "FirewallPolicyTypeDef",
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateFirewallPolicyResponseTypeDef = TypedDict(
    "CreateFirewallPolicyResponseTypeDef",
    {
        "UpdateToken": str,
        "FirewallPolicyResponse": "FirewallPolicyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFirewallRequestRequestTypeDef = TypedDict(
    "CreateFirewallRequestRequestTypeDef",
    {
        "FirewallName": str,
        "FirewallPolicyArn": str,
        "VpcId": str,
        "SubnetMappings": Sequence["SubnetMappingTypeDef"],
        "DeleteProtection": NotRequired[bool],
        "SubnetChangeProtection": NotRequired[bool],
        "FirewallPolicyChangeProtection": NotRequired[bool],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateFirewallResponseTypeDef = TypedDict(
    "CreateFirewallResponseTypeDef",
    {
        "Firewall": "FirewallTypeDef",
        "FirewallStatus": "FirewallStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRuleGroupRequestRequestTypeDef = TypedDict(
    "CreateRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupName": str,
        "Type": RuleGroupTypeType,
        "Capacity": int,
        "RuleGroup": NotRequired["RuleGroupTypeDef"],
        "Rules": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "DryRun": NotRequired[bool],
    },
)

CreateRuleGroupResponseTypeDef = TypedDict(
    "CreateRuleGroupResponseTypeDef",
    {
        "UpdateToken": str,
        "RuleGroupResponse": "RuleGroupResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomActionTypeDef = TypedDict(
    "CustomActionTypeDef",
    {
        "ActionName": str,
        "ActionDefinition": "ActionDefinitionTypeDef",
    },
)

DeleteFirewallPolicyRequestRequestTypeDef = TypedDict(
    "DeleteFirewallPolicyRequestRequestTypeDef",
    {
        "FirewallPolicyName": NotRequired[str],
        "FirewallPolicyArn": NotRequired[str],
    },
)

DeleteFirewallPolicyResponseTypeDef = TypedDict(
    "DeleteFirewallPolicyResponseTypeDef",
    {
        "FirewallPolicyResponse": "FirewallPolicyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFirewallRequestRequestTypeDef = TypedDict(
    "DeleteFirewallRequestRequestTypeDef",
    {
        "FirewallName": NotRequired[str],
        "FirewallArn": NotRequired[str],
    },
)

DeleteFirewallResponseTypeDef = TypedDict(
    "DeleteFirewallResponseTypeDef",
    {
        "Firewall": "FirewallTypeDef",
        "FirewallStatus": "FirewallStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DeleteRuleGroupRequestRequestTypeDef = TypedDict(
    "DeleteRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupName": NotRequired[str],
        "RuleGroupArn": NotRequired[str],
        "Type": NotRequired[RuleGroupTypeType],
    },
)

DeleteRuleGroupResponseTypeDef = TypedDict(
    "DeleteRuleGroupResponseTypeDef",
    {
        "RuleGroupResponse": "RuleGroupResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFirewallPolicyRequestRequestTypeDef = TypedDict(
    "DescribeFirewallPolicyRequestRequestTypeDef",
    {
        "FirewallPolicyName": NotRequired[str],
        "FirewallPolicyArn": NotRequired[str],
    },
)

DescribeFirewallPolicyResponseTypeDef = TypedDict(
    "DescribeFirewallPolicyResponseTypeDef",
    {
        "UpdateToken": str,
        "FirewallPolicyResponse": "FirewallPolicyResponseTypeDef",
        "FirewallPolicy": "FirewallPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFirewallRequestRequestTypeDef = TypedDict(
    "DescribeFirewallRequestRequestTypeDef",
    {
        "FirewallName": NotRequired[str],
        "FirewallArn": NotRequired[str],
    },
)

DescribeFirewallResponseTypeDef = TypedDict(
    "DescribeFirewallResponseTypeDef",
    {
        "UpdateToken": str,
        "Firewall": "FirewallTypeDef",
        "FirewallStatus": "FirewallStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeLoggingConfigurationRequestRequestTypeDef",
    {
        "FirewallArn": NotRequired[str],
        "FirewallName": NotRequired[str],
    },
)

DescribeLoggingConfigurationResponseTypeDef = TypedDict(
    "DescribeLoggingConfigurationResponseTypeDef",
    {
        "FirewallArn": str,
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourcePolicyRequestRequestTypeDef = TypedDict(
    "DescribeResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeResourcePolicyResponseTypeDef = TypedDict(
    "DescribeResourcePolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRuleGroupMetadataRequestRequestTypeDef = TypedDict(
    "DescribeRuleGroupMetadataRequestRequestTypeDef",
    {
        "RuleGroupName": NotRequired[str],
        "RuleGroupArn": NotRequired[str],
        "Type": NotRequired[RuleGroupTypeType],
    },
)

DescribeRuleGroupMetadataResponseTypeDef = TypedDict(
    "DescribeRuleGroupMetadataResponseTypeDef",
    {
        "RuleGroupArn": str,
        "RuleGroupName": str,
        "Description": str,
        "Type": RuleGroupTypeType,
        "Capacity": int,
        "StatefulRuleOptions": "StatefulRuleOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRuleGroupRequestRequestTypeDef = TypedDict(
    "DescribeRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupName": NotRequired[str],
        "RuleGroupArn": NotRequired[str],
        "Type": NotRequired[RuleGroupTypeType],
    },
)

DescribeRuleGroupResponseTypeDef = TypedDict(
    "DescribeRuleGroupResponseTypeDef",
    {
        "UpdateToken": str,
        "RuleGroup": "RuleGroupTypeDef",
        "RuleGroupResponse": "RuleGroupResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Value": str,
    },
)

DisassociateSubnetsRequestRequestTypeDef = TypedDict(
    "DisassociateSubnetsRequestRequestTypeDef",
    {
        "SubnetIds": Sequence[str],
        "UpdateToken": NotRequired[str],
        "FirewallArn": NotRequired[str],
        "FirewallName": NotRequired[str],
    },
)

DisassociateSubnetsResponseTypeDef = TypedDict(
    "DisassociateSubnetsResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "SubnetMappings": List["SubnetMappingTypeDef"],
        "UpdateToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FirewallMetadataTypeDef = TypedDict(
    "FirewallMetadataTypeDef",
    {
        "FirewallName": NotRequired[str],
        "FirewallArn": NotRequired[str],
    },
)

FirewallPolicyMetadataTypeDef = TypedDict(
    "FirewallPolicyMetadataTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
    },
)

FirewallPolicyResponseTypeDef = TypedDict(
    "FirewallPolicyResponseTypeDef",
    {
        "FirewallPolicyName": str,
        "FirewallPolicyArn": str,
        "FirewallPolicyId": str,
        "Description": NotRequired[str],
        "FirewallPolicyStatus": NotRequired[ResourceStatusType],
        "Tags": NotRequired[List["TagTypeDef"]],
        "ConsumedStatelessRuleCapacity": NotRequired[int],
        "ConsumedStatefulRuleCapacity": NotRequired[int],
        "NumberOfAssociations": NotRequired[int],
    },
)

FirewallPolicyTypeDef = TypedDict(
    "FirewallPolicyTypeDef",
    {
        "StatelessDefaultActions": Sequence[str],
        "StatelessFragmentDefaultActions": Sequence[str],
        "StatelessRuleGroupReferences": NotRequired[Sequence["StatelessRuleGroupReferenceTypeDef"]],
        "StatelessCustomActions": NotRequired[Sequence["CustomActionTypeDef"]],
        "StatefulRuleGroupReferences": NotRequired[Sequence["StatefulRuleGroupReferenceTypeDef"]],
        "StatefulDefaultActions": NotRequired[Sequence[str]],
        "StatefulEngineOptions": NotRequired["StatefulEngineOptionsTypeDef"],
    },
)

FirewallStatusTypeDef = TypedDict(
    "FirewallStatusTypeDef",
    {
        "Status": FirewallStatusValueType,
        "ConfigurationSyncStateSummary": ConfigurationSyncStateType,
        "SyncStates": NotRequired[Dict[str, "SyncStateTypeDef"]],
    },
)

FirewallTypeDef = TypedDict(
    "FirewallTypeDef",
    {
        "FirewallPolicyArn": str,
        "VpcId": str,
        "SubnetMappings": List["SubnetMappingTypeDef"],
        "FirewallId": str,
        "FirewallName": NotRequired[str],
        "FirewallArn": NotRequired[str],
        "DeleteProtection": NotRequired[bool],
        "SubnetChangeProtection": NotRequired[bool],
        "FirewallPolicyChangeProtection": NotRequired[bool],
        "Description": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

HeaderTypeDef = TypedDict(
    "HeaderTypeDef",
    {
        "Protocol": StatefulRuleProtocolType,
        "Source": str,
        "SourcePort": str,
        "Direction": StatefulRuleDirectionType,
        "Destination": str,
        "DestinationPort": str,
    },
)

IPSetTypeDef = TypedDict(
    "IPSetTypeDef",
    {
        "Definition": Sequence[str],
    },
)

ListFirewallPoliciesRequestRequestTypeDef = TypedDict(
    "ListFirewallPoliciesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListFirewallPoliciesResponseTypeDef = TypedDict(
    "ListFirewallPoliciesResponseTypeDef",
    {
        "NextToken": str,
        "FirewallPolicies": List["FirewallPolicyMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFirewallsRequestRequestTypeDef = TypedDict(
    "ListFirewallsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "VpcIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
    },
)

ListFirewallsResponseTypeDef = TypedDict(
    "ListFirewallsResponseTypeDef",
    {
        "NextToken": str,
        "Firewalls": List["FirewallMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRuleGroupsRequestRequestTypeDef = TypedDict(
    "ListRuleGroupsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Scope": NotRequired[ResourceManagedStatusType],
    },
)

ListRuleGroupsResponseTypeDef = TypedDict(
    "ListRuleGroupsResponseTypeDef",
    {
        "NextToken": str,
        "RuleGroups": List["RuleGroupMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "NextToken": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogDestinationConfigTypeDef = TypedDict(
    "LogDestinationConfigTypeDef",
    {
        "LogType": LogTypeType,
        "LogDestinationType": LogDestinationTypeType,
        "LogDestination": Dict[str, str],
    },
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "LogDestinationConfigs": List["LogDestinationConfigTypeDef"],
    },
)

MatchAttributesTypeDef = TypedDict(
    "MatchAttributesTypeDef",
    {
        "Sources": NotRequired[Sequence["AddressTypeDef"]],
        "Destinations": NotRequired[Sequence["AddressTypeDef"]],
        "SourcePorts": NotRequired[Sequence["PortRangeTypeDef"]],
        "DestinationPorts": NotRequired[Sequence["PortRangeTypeDef"]],
        "Protocols": NotRequired[Sequence[int]],
        "TCPFlags": NotRequired[Sequence["TCPFlagFieldTypeDef"]],
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

PerObjectStatusTypeDef = TypedDict(
    "PerObjectStatusTypeDef",
    {
        "SyncStatus": NotRequired[PerObjectSyncStatusType],
        "UpdateToken": NotRequired[str],
    },
)

PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
    },
)

PortSetTypeDef = TypedDict(
    "PortSetTypeDef",
    {
        "Definition": NotRequired[Sequence[str]],
    },
)

PublishMetricActionTypeDef = TypedDict(
    "PublishMetricActionTypeDef",
    {
        "Dimensions": Sequence["DimensionTypeDef"],
    },
)

PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
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

RuleDefinitionTypeDef = TypedDict(
    "RuleDefinitionTypeDef",
    {
        "MatchAttributes": "MatchAttributesTypeDef",
        "Actions": Sequence[str],
    },
)

RuleGroupMetadataTypeDef = TypedDict(
    "RuleGroupMetadataTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
    },
)

RuleGroupResponseTypeDef = TypedDict(
    "RuleGroupResponseTypeDef",
    {
        "RuleGroupArn": str,
        "RuleGroupName": str,
        "RuleGroupId": str,
        "Description": NotRequired[str],
        "Type": NotRequired[RuleGroupTypeType],
        "Capacity": NotRequired[int],
        "RuleGroupStatus": NotRequired[ResourceStatusType],
        "Tags": NotRequired[List["TagTypeDef"]],
        "ConsumedCapacity": NotRequired[int],
        "NumberOfAssociations": NotRequired[int],
    },
)

RuleGroupTypeDef = TypedDict(
    "RuleGroupTypeDef",
    {
        "RulesSource": "RulesSourceTypeDef",
        "RuleVariables": NotRequired["RuleVariablesTypeDef"],
        "StatefulRuleOptions": NotRequired["StatefulRuleOptionsTypeDef"],
    },
)

RuleOptionTypeDef = TypedDict(
    "RuleOptionTypeDef",
    {
        "Keyword": str,
        "Settings": NotRequired[Sequence[str]],
    },
)

RuleVariablesTypeDef = TypedDict(
    "RuleVariablesTypeDef",
    {
        "IPSets": NotRequired[Mapping[str, "IPSetTypeDef"]],
        "PortSets": NotRequired[Mapping[str, "PortSetTypeDef"]],
    },
)

RulesSourceListTypeDef = TypedDict(
    "RulesSourceListTypeDef",
    {
        "Targets": Sequence[str],
        "TargetTypes": Sequence[TargetTypeType],
        "GeneratedRulesType": GeneratedRulesTypeType,
    },
)

RulesSourceTypeDef = TypedDict(
    "RulesSourceTypeDef",
    {
        "RulesString": NotRequired[str],
        "RulesSourceList": NotRequired["RulesSourceListTypeDef"],
        "StatefulRules": NotRequired[Sequence["StatefulRuleTypeDef"]],
        "StatelessRulesAndCustomActions": NotRequired["StatelessRulesAndCustomActionsTypeDef"],
    },
)

StatefulEngineOptionsTypeDef = TypedDict(
    "StatefulEngineOptionsTypeDef",
    {
        "RuleOrder": NotRequired[RuleOrderType],
    },
)

StatefulRuleGroupOverrideTypeDef = TypedDict(
    "StatefulRuleGroupOverrideTypeDef",
    {
        "Action": NotRequired[Literal["DROP_TO_ALERT"]],
    },
)

StatefulRuleGroupReferenceTypeDef = TypedDict(
    "StatefulRuleGroupReferenceTypeDef",
    {
        "ResourceArn": str,
        "Priority": NotRequired[int],
        "Override": NotRequired["StatefulRuleGroupOverrideTypeDef"],
    },
)

StatefulRuleOptionsTypeDef = TypedDict(
    "StatefulRuleOptionsTypeDef",
    {
        "RuleOrder": NotRequired[RuleOrderType],
    },
)

StatefulRuleTypeDef = TypedDict(
    "StatefulRuleTypeDef",
    {
        "Action": StatefulActionType,
        "Header": "HeaderTypeDef",
        "RuleOptions": Sequence["RuleOptionTypeDef"],
    },
)

StatelessRuleGroupReferenceTypeDef = TypedDict(
    "StatelessRuleGroupReferenceTypeDef",
    {
        "ResourceArn": str,
        "Priority": int,
    },
)

StatelessRuleTypeDef = TypedDict(
    "StatelessRuleTypeDef",
    {
        "RuleDefinition": "RuleDefinitionTypeDef",
        "Priority": int,
    },
)

StatelessRulesAndCustomActionsTypeDef = TypedDict(
    "StatelessRulesAndCustomActionsTypeDef",
    {
        "StatelessRules": Sequence["StatelessRuleTypeDef"],
        "CustomActions": NotRequired[Sequence["CustomActionTypeDef"]],
    },
)

SubnetMappingTypeDef = TypedDict(
    "SubnetMappingTypeDef",
    {
        "SubnetId": str,
    },
)

SyncStateTypeDef = TypedDict(
    "SyncStateTypeDef",
    {
        "Attachment": NotRequired["AttachmentTypeDef"],
        "Config": NotRequired[Dict[str, "PerObjectStatusTypeDef"]],
    },
)

TCPFlagFieldTypeDef = TypedDict(
    "TCPFlagFieldTypeDef",
    {
        "Flags": Sequence[TCPFlagType],
        "Masks": NotRequired[Sequence[TCPFlagType]],
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

UpdateFirewallDeleteProtectionRequestRequestTypeDef = TypedDict(
    "UpdateFirewallDeleteProtectionRequestRequestTypeDef",
    {
        "DeleteProtection": bool,
        "UpdateToken": NotRequired[str],
        "FirewallArn": NotRequired[str],
        "FirewallName": NotRequired[str],
    },
)

UpdateFirewallDeleteProtectionResponseTypeDef = TypedDict(
    "UpdateFirewallDeleteProtectionResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "DeleteProtection": bool,
        "UpdateToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFirewallDescriptionRequestRequestTypeDef = TypedDict(
    "UpdateFirewallDescriptionRequestRequestTypeDef",
    {
        "UpdateToken": NotRequired[str],
        "FirewallArn": NotRequired[str],
        "FirewallName": NotRequired[str],
        "Description": NotRequired[str],
    },
)

UpdateFirewallDescriptionResponseTypeDef = TypedDict(
    "UpdateFirewallDescriptionResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "Description": str,
        "UpdateToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFirewallPolicyChangeProtectionRequestRequestTypeDef = TypedDict(
    "UpdateFirewallPolicyChangeProtectionRequestRequestTypeDef",
    {
        "FirewallPolicyChangeProtection": bool,
        "UpdateToken": NotRequired[str],
        "FirewallArn": NotRequired[str],
        "FirewallName": NotRequired[str],
    },
)

UpdateFirewallPolicyChangeProtectionResponseTypeDef = TypedDict(
    "UpdateFirewallPolicyChangeProtectionResponseTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
        "FirewallPolicyChangeProtection": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFirewallPolicyRequestRequestTypeDef = TypedDict(
    "UpdateFirewallPolicyRequestRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallPolicy": "FirewallPolicyTypeDef",
        "FirewallPolicyArn": NotRequired[str],
        "FirewallPolicyName": NotRequired[str],
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

UpdateFirewallPolicyResponseTypeDef = TypedDict(
    "UpdateFirewallPolicyResponseTypeDef",
    {
        "UpdateToken": str,
        "FirewallPolicyResponse": "FirewallPolicyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateLoggingConfigurationRequestRequestTypeDef",
    {
        "FirewallArn": NotRequired[str],
        "FirewallName": NotRequired[str],
        "LoggingConfiguration": NotRequired["LoggingConfigurationTypeDef"],
    },
)

UpdateLoggingConfigurationResponseTypeDef = TypedDict(
    "UpdateLoggingConfigurationResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRuleGroupRequestRequestTypeDef = TypedDict(
    "UpdateRuleGroupRequestRequestTypeDef",
    {
        "UpdateToken": str,
        "RuleGroupArn": NotRequired[str],
        "RuleGroupName": NotRequired[str],
        "RuleGroup": NotRequired["RuleGroupTypeDef"],
        "Rules": NotRequired[str],
        "Type": NotRequired[RuleGroupTypeType],
        "Description": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)

UpdateRuleGroupResponseTypeDef = TypedDict(
    "UpdateRuleGroupResponseTypeDef",
    {
        "UpdateToken": str,
        "RuleGroupResponse": "RuleGroupResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSubnetChangeProtectionRequestRequestTypeDef = TypedDict(
    "UpdateSubnetChangeProtectionRequestRequestTypeDef",
    {
        "SubnetChangeProtection": bool,
        "UpdateToken": NotRequired[str],
        "FirewallArn": NotRequired[str],
        "FirewallName": NotRequired[str],
    },
)

UpdateSubnetChangeProtectionResponseTypeDef = TypedDict(
    "UpdateSubnetChangeProtectionResponseTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
        "SubnetChangeProtection": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
