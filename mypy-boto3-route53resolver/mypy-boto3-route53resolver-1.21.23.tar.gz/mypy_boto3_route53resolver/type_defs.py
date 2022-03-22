"""
Type annotations for route53resolver service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/type_defs.html)

Usage::

    ```python
    from mypy_boto3_route53resolver.type_defs import AssociateFirewallRuleGroupRequestRequestTypeDef

    data: AssociateFirewallRuleGroupRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    ActionType,
    AutodefinedReverseFlagType,
    BlockResponseType,
    FirewallDomainListStatusType,
    FirewallDomainUpdateOperationType,
    FirewallFailOpenStatusType,
    FirewallRuleGroupAssociationStatusType,
    FirewallRuleGroupStatusType,
    IpAddressStatusType,
    MutationProtectionStatusType,
    ResolverAutodefinedReverseStatusType,
    ResolverDNSSECValidationStatusType,
    ResolverEndpointDirectionType,
    ResolverEndpointStatusType,
    ResolverQueryLogConfigAssociationErrorType,
    ResolverQueryLogConfigAssociationStatusType,
    ResolverQueryLogConfigStatusType,
    ResolverRuleAssociationStatusType,
    ResolverRuleStatusType,
    RuleTypeOptionType,
    ShareStatusType,
    SortOrderType,
    ValidationType,
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
    "AssociateFirewallRuleGroupRequestRequestTypeDef",
    "AssociateFirewallRuleGroupResponseTypeDef",
    "AssociateResolverEndpointIpAddressRequestRequestTypeDef",
    "AssociateResolverEndpointIpAddressResponseTypeDef",
    "AssociateResolverQueryLogConfigRequestRequestTypeDef",
    "AssociateResolverQueryLogConfigResponseTypeDef",
    "AssociateResolverRuleRequestRequestTypeDef",
    "AssociateResolverRuleResponseTypeDef",
    "CreateFirewallDomainListRequestRequestTypeDef",
    "CreateFirewallDomainListResponseTypeDef",
    "CreateFirewallRuleGroupRequestRequestTypeDef",
    "CreateFirewallRuleGroupResponseTypeDef",
    "CreateFirewallRuleRequestRequestTypeDef",
    "CreateFirewallRuleResponseTypeDef",
    "CreateResolverEndpointRequestRequestTypeDef",
    "CreateResolverEndpointResponseTypeDef",
    "CreateResolverQueryLogConfigRequestRequestTypeDef",
    "CreateResolverQueryLogConfigResponseTypeDef",
    "CreateResolverRuleRequestRequestTypeDef",
    "CreateResolverRuleResponseTypeDef",
    "DeleteFirewallDomainListRequestRequestTypeDef",
    "DeleteFirewallDomainListResponseTypeDef",
    "DeleteFirewallRuleGroupRequestRequestTypeDef",
    "DeleteFirewallRuleGroupResponseTypeDef",
    "DeleteFirewallRuleRequestRequestTypeDef",
    "DeleteFirewallRuleResponseTypeDef",
    "DeleteResolverEndpointRequestRequestTypeDef",
    "DeleteResolverEndpointResponseTypeDef",
    "DeleteResolverQueryLogConfigRequestRequestTypeDef",
    "DeleteResolverQueryLogConfigResponseTypeDef",
    "DeleteResolverRuleRequestRequestTypeDef",
    "DeleteResolverRuleResponseTypeDef",
    "DisassociateFirewallRuleGroupRequestRequestTypeDef",
    "DisassociateFirewallRuleGroupResponseTypeDef",
    "DisassociateResolverEndpointIpAddressRequestRequestTypeDef",
    "DisassociateResolverEndpointIpAddressResponseTypeDef",
    "DisassociateResolverQueryLogConfigRequestRequestTypeDef",
    "DisassociateResolverQueryLogConfigResponseTypeDef",
    "DisassociateResolverRuleRequestRequestTypeDef",
    "DisassociateResolverRuleResponseTypeDef",
    "FilterTypeDef",
    "FirewallConfigTypeDef",
    "FirewallDomainListMetadataTypeDef",
    "FirewallDomainListTypeDef",
    "FirewallRuleGroupAssociationTypeDef",
    "FirewallRuleGroupMetadataTypeDef",
    "FirewallRuleGroupTypeDef",
    "FirewallRuleTypeDef",
    "GetFirewallConfigRequestRequestTypeDef",
    "GetFirewallConfigResponseTypeDef",
    "GetFirewallDomainListRequestRequestTypeDef",
    "GetFirewallDomainListResponseTypeDef",
    "GetFirewallRuleGroupAssociationRequestRequestTypeDef",
    "GetFirewallRuleGroupAssociationResponseTypeDef",
    "GetFirewallRuleGroupPolicyRequestRequestTypeDef",
    "GetFirewallRuleGroupPolicyResponseTypeDef",
    "GetFirewallRuleGroupRequestRequestTypeDef",
    "GetFirewallRuleGroupResponseTypeDef",
    "GetResolverConfigRequestRequestTypeDef",
    "GetResolverConfigResponseTypeDef",
    "GetResolverDnssecConfigRequestRequestTypeDef",
    "GetResolverDnssecConfigResponseTypeDef",
    "GetResolverEndpointRequestRequestTypeDef",
    "GetResolverEndpointResponseTypeDef",
    "GetResolverQueryLogConfigAssociationRequestRequestTypeDef",
    "GetResolverQueryLogConfigAssociationResponseTypeDef",
    "GetResolverQueryLogConfigPolicyRequestRequestTypeDef",
    "GetResolverQueryLogConfigPolicyResponseTypeDef",
    "GetResolverQueryLogConfigRequestRequestTypeDef",
    "GetResolverQueryLogConfigResponseTypeDef",
    "GetResolverRuleAssociationRequestRequestTypeDef",
    "GetResolverRuleAssociationResponseTypeDef",
    "GetResolverRulePolicyRequestRequestTypeDef",
    "GetResolverRulePolicyResponseTypeDef",
    "GetResolverRuleRequestRequestTypeDef",
    "GetResolverRuleResponseTypeDef",
    "ImportFirewallDomainsRequestRequestTypeDef",
    "ImportFirewallDomainsResponseTypeDef",
    "IpAddressRequestTypeDef",
    "IpAddressResponseTypeDef",
    "IpAddressUpdateTypeDef",
    "ListFirewallConfigsRequestRequestTypeDef",
    "ListFirewallConfigsResponseTypeDef",
    "ListFirewallDomainListsRequestRequestTypeDef",
    "ListFirewallDomainListsResponseTypeDef",
    "ListFirewallDomainsRequestRequestTypeDef",
    "ListFirewallDomainsResponseTypeDef",
    "ListFirewallRuleGroupAssociationsRequestRequestTypeDef",
    "ListFirewallRuleGroupAssociationsResponseTypeDef",
    "ListFirewallRuleGroupsRequestRequestTypeDef",
    "ListFirewallRuleGroupsResponseTypeDef",
    "ListFirewallRulesRequestRequestTypeDef",
    "ListFirewallRulesResponseTypeDef",
    "ListResolverConfigsRequestRequestTypeDef",
    "ListResolverConfigsResponseTypeDef",
    "ListResolverDnssecConfigsRequestRequestTypeDef",
    "ListResolverDnssecConfigsResponseTypeDef",
    "ListResolverEndpointIpAddressesRequestRequestTypeDef",
    "ListResolverEndpointIpAddressesResponseTypeDef",
    "ListResolverEndpointsRequestRequestTypeDef",
    "ListResolverEndpointsResponseTypeDef",
    "ListResolverQueryLogConfigAssociationsRequestRequestTypeDef",
    "ListResolverQueryLogConfigAssociationsResponseTypeDef",
    "ListResolverQueryLogConfigsRequestRequestTypeDef",
    "ListResolverQueryLogConfigsResponseTypeDef",
    "ListResolverRuleAssociationsRequestRequestTypeDef",
    "ListResolverRuleAssociationsResponseTypeDef",
    "ListResolverRulesRequestRequestTypeDef",
    "ListResolverRulesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutFirewallRuleGroupPolicyRequestRequestTypeDef",
    "PutFirewallRuleGroupPolicyResponseTypeDef",
    "PutResolverQueryLogConfigPolicyRequestRequestTypeDef",
    "PutResolverQueryLogConfigPolicyResponseTypeDef",
    "PutResolverRulePolicyRequestRequestTypeDef",
    "PutResolverRulePolicyResponseTypeDef",
    "ResolverConfigTypeDef",
    "ResolverDnssecConfigTypeDef",
    "ResolverEndpointTypeDef",
    "ResolverQueryLogConfigAssociationTypeDef",
    "ResolverQueryLogConfigTypeDef",
    "ResolverRuleAssociationTypeDef",
    "ResolverRuleConfigTypeDef",
    "ResolverRuleTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TargetAddressTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateFirewallConfigRequestRequestTypeDef",
    "UpdateFirewallConfigResponseTypeDef",
    "UpdateFirewallDomainsRequestRequestTypeDef",
    "UpdateFirewallDomainsResponseTypeDef",
    "UpdateFirewallRuleGroupAssociationRequestRequestTypeDef",
    "UpdateFirewallRuleGroupAssociationResponseTypeDef",
    "UpdateFirewallRuleRequestRequestTypeDef",
    "UpdateFirewallRuleResponseTypeDef",
    "UpdateResolverConfigRequestRequestTypeDef",
    "UpdateResolverConfigResponseTypeDef",
    "UpdateResolverDnssecConfigRequestRequestTypeDef",
    "UpdateResolverDnssecConfigResponseTypeDef",
    "UpdateResolverEndpointRequestRequestTypeDef",
    "UpdateResolverEndpointResponseTypeDef",
    "UpdateResolverRuleRequestRequestTypeDef",
    "UpdateResolverRuleResponseTypeDef",
)

AssociateFirewallRuleGroupRequestRequestTypeDef = TypedDict(
    "AssociateFirewallRuleGroupRequestRequestTypeDef",
    {
        "CreatorRequestId": str,
        "FirewallRuleGroupId": str,
        "VpcId": str,
        "Priority": int,
        "Name": str,
        "MutationProtection": NotRequired[MutationProtectionStatusType],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

AssociateFirewallRuleGroupResponseTypeDef = TypedDict(
    "AssociateFirewallRuleGroupResponseTypeDef",
    {
        "FirewallRuleGroupAssociation": "FirewallRuleGroupAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateResolverEndpointIpAddressRequestRequestTypeDef = TypedDict(
    "AssociateResolverEndpointIpAddressRequestRequestTypeDef",
    {
        "ResolverEndpointId": str,
        "IpAddress": "IpAddressUpdateTypeDef",
    },
)

AssociateResolverEndpointIpAddressResponseTypeDef = TypedDict(
    "AssociateResolverEndpointIpAddressResponseTypeDef",
    {
        "ResolverEndpoint": "ResolverEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateResolverQueryLogConfigRequestRequestTypeDef = TypedDict(
    "AssociateResolverQueryLogConfigRequestRequestTypeDef",
    {
        "ResolverQueryLogConfigId": str,
        "ResourceId": str,
    },
)

AssociateResolverQueryLogConfigResponseTypeDef = TypedDict(
    "AssociateResolverQueryLogConfigResponseTypeDef",
    {
        "ResolverQueryLogConfigAssociation": "ResolverQueryLogConfigAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateResolverRuleRequestRequestTypeDef = TypedDict(
    "AssociateResolverRuleRequestRequestTypeDef",
    {
        "ResolverRuleId": str,
        "VPCId": str,
        "Name": NotRequired[str],
    },
)

AssociateResolverRuleResponseTypeDef = TypedDict(
    "AssociateResolverRuleResponseTypeDef",
    {
        "ResolverRuleAssociation": "ResolverRuleAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFirewallDomainListRequestRequestTypeDef = TypedDict(
    "CreateFirewallDomainListRequestRequestTypeDef",
    {
        "CreatorRequestId": str,
        "Name": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateFirewallDomainListResponseTypeDef = TypedDict(
    "CreateFirewallDomainListResponseTypeDef",
    {
        "FirewallDomainList": "FirewallDomainListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFirewallRuleGroupRequestRequestTypeDef = TypedDict(
    "CreateFirewallRuleGroupRequestRequestTypeDef",
    {
        "CreatorRequestId": str,
        "Name": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateFirewallRuleGroupResponseTypeDef = TypedDict(
    "CreateFirewallRuleGroupResponseTypeDef",
    {
        "FirewallRuleGroup": "FirewallRuleGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFirewallRuleRequestRequestTypeDef = TypedDict(
    "CreateFirewallRuleRequestRequestTypeDef",
    {
        "CreatorRequestId": str,
        "FirewallRuleGroupId": str,
        "FirewallDomainListId": str,
        "Priority": int,
        "Action": ActionType,
        "Name": str,
        "BlockResponse": NotRequired[BlockResponseType],
        "BlockOverrideDomain": NotRequired[str],
        "BlockOverrideDnsType": NotRequired[Literal["CNAME"]],
        "BlockOverrideTtl": NotRequired[int],
    },
)

CreateFirewallRuleResponseTypeDef = TypedDict(
    "CreateFirewallRuleResponseTypeDef",
    {
        "FirewallRule": "FirewallRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResolverEndpointRequestRequestTypeDef = TypedDict(
    "CreateResolverEndpointRequestRequestTypeDef",
    {
        "CreatorRequestId": str,
        "SecurityGroupIds": Sequence[str],
        "Direction": ResolverEndpointDirectionType,
        "IpAddresses": Sequence["IpAddressRequestTypeDef"],
        "Name": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateResolverEndpointResponseTypeDef = TypedDict(
    "CreateResolverEndpointResponseTypeDef",
    {
        "ResolverEndpoint": "ResolverEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResolverQueryLogConfigRequestRequestTypeDef = TypedDict(
    "CreateResolverQueryLogConfigRequestRequestTypeDef",
    {
        "Name": str,
        "DestinationArn": str,
        "CreatorRequestId": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateResolverQueryLogConfigResponseTypeDef = TypedDict(
    "CreateResolverQueryLogConfigResponseTypeDef",
    {
        "ResolverQueryLogConfig": "ResolverQueryLogConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResolverRuleRequestRequestTypeDef = TypedDict(
    "CreateResolverRuleRequestRequestTypeDef",
    {
        "CreatorRequestId": str,
        "RuleType": RuleTypeOptionType,
        "DomainName": str,
        "Name": NotRequired[str],
        "TargetIps": NotRequired[Sequence["TargetAddressTypeDef"]],
        "ResolverEndpointId": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateResolverRuleResponseTypeDef = TypedDict(
    "CreateResolverRuleResponseTypeDef",
    {
        "ResolverRule": "ResolverRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFirewallDomainListRequestRequestTypeDef = TypedDict(
    "DeleteFirewallDomainListRequestRequestTypeDef",
    {
        "FirewallDomainListId": str,
    },
)

DeleteFirewallDomainListResponseTypeDef = TypedDict(
    "DeleteFirewallDomainListResponseTypeDef",
    {
        "FirewallDomainList": "FirewallDomainListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFirewallRuleGroupRequestRequestTypeDef = TypedDict(
    "DeleteFirewallRuleGroupRequestRequestTypeDef",
    {
        "FirewallRuleGroupId": str,
    },
)

DeleteFirewallRuleGroupResponseTypeDef = TypedDict(
    "DeleteFirewallRuleGroupResponseTypeDef",
    {
        "FirewallRuleGroup": "FirewallRuleGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFirewallRuleRequestRequestTypeDef = TypedDict(
    "DeleteFirewallRuleRequestRequestTypeDef",
    {
        "FirewallRuleGroupId": str,
        "FirewallDomainListId": str,
    },
)

DeleteFirewallRuleResponseTypeDef = TypedDict(
    "DeleteFirewallRuleResponseTypeDef",
    {
        "FirewallRule": "FirewallRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResolverEndpointRequestRequestTypeDef = TypedDict(
    "DeleteResolverEndpointRequestRequestTypeDef",
    {
        "ResolverEndpointId": str,
    },
)

DeleteResolverEndpointResponseTypeDef = TypedDict(
    "DeleteResolverEndpointResponseTypeDef",
    {
        "ResolverEndpoint": "ResolverEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResolverQueryLogConfigRequestRequestTypeDef = TypedDict(
    "DeleteResolverQueryLogConfigRequestRequestTypeDef",
    {
        "ResolverQueryLogConfigId": str,
    },
)

DeleteResolverQueryLogConfigResponseTypeDef = TypedDict(
    "DeleteResolverQueryLogConfigResponseTypeDef",
    {
        "ResolverQueryLogConfig": "ResolverQueryLogConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResolverRuleRequestRequestTypeDef = TypedDict(
    "DeleteResolverRuleRequestRequestTypeDef",
    {
        "ResolverRuleId": str,
    },
)

DeleteResolverRuleResponseTypeDef = TypedDict(
    "DeleteResolverRuleResponseTypeDef",
    {
        "ResolverRule": "ResolverRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateFirewallRuleGroupRequestRequestTypeDef = TypedDict(
    "DisassociateFirewallRuleGroupRequestRequestTypeDef",
    {
        "FirewallRuleGroupAssociationId": str,
    },
)

DisassociateFirewallRuleGroupResponseTypeDef = TypedDict(
    "DisassociateFirewallRuleGroupResponseTypeDef",
    {
        "FirewallRuleGroupAssociation": "FirewallRuleGroupAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateResolverEndpointIpAddressRequestRequestTypeDef = TypedDict(
    "DisassociateResolverEndpointIpAddressRequestRequestTypeDef",
    {
        "ResolverEndpointId": str,
        "IpAddress": "IpAddressUpdateTypeDef",
    },
)

DisassociateResolverEndpointIpAddressResponseTypeDef = TypedDict(
    "DisassociateResolverEndpointIpAddressResponseTypeDef",
    {
        "ResolverEndpoint": "ResolverEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateResolverQueryLogConfigRequestRequestTypeDef = TypedDict(
    "DisassociateResolverQueryLogConfigRequestRequestTypeDef",
    {
        "ResolverQueryLogConfigId": str,
        "ResourceId": str,
    },
)

DisassociateResolverQueryLogConfigResponseTypeDef = TypedDict(
    "DisassociateResolverQueryLogConfigResponseTypeDef",
    {
        "ResolverQueryLogConfigAssociation": "ResolverQueryLogConfigAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateResolverRuleRequestRequestTypeDef = TypedDict(
    "DisassociateResolverRuleRequestRequestTypeDef",
    {
        "VPCId": str,
        "ResolverRuleId": str,
    },
)

DisassociateResolverRuleResponseTypeDef = TypedDict(
    "DisassociateResolverRuleResponseTypeDef",
    {
        "ResolverRuleAssociation": "ResolverRuleAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)

FirewallConfigTypeDef = TypedDict(
    "FirewallConfigTypeDef",
    {
        "Id": NotRequired[str],
        "ResourceId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "FirewallFailOpen": NotRequired[FirewallFailOpenStatusType],
    },
)

FirewallDomainListMetadataTypeDef = TypedDict(
    "FirewallDomainListMetadataTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "ManagedOwnerName": NotRequired[str],
    },
)

FirewallDomainListTypeDef = TypedDict(
    "FirewallDomainListTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "DomainCount": NotRequired[int],
        "Status": NotRequired[FirewallDomainListStatusType],
        "StatusMessage": NotRequired[str],
        "ManagedOwnerName": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "CreationTime": NotRequired[str],
        "ModificationTime": NotRequired[str],
    },
)

FirewallRuleGroupAssociationTypeDef = TypedDict(
    "FirewallRuleGroupAssociationTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "FirewallRuleGroupId": NotRequired[str],
        "VpcId": NotRequired[str],
        "Name": NotRequired[str],
        "Priority": NotRequired[int],
        "MutationProtection": NotRequired[MutationProtectionStatusType],
        "ManagedOwnerName": NotRequired[str],
        "Status": NotRequired[FirewallRuleGroupAssociationStatusType],
        "StatusMessage": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "CreationTime": NotRequired[str],
        "ModificationTime": NotRequired[str],
    },
)

FirewallRuleGroupMetadataTypeDef = TypedDict(
    "FirewallRuleGroupMetadataTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "OwnerId": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "ShareStatus": NotRequired[ShareStatusType],
    },
)

FirewallRuleGroupTypeDef = TypedDict(
    "FirewallRuleGroupTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "RuleCount": NotRequired[int],
        "Status": NotRequired[FirewallRuleGroupStatusType],
        "StatusMessage": NotRequired[str],
        "OwnerId": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "ShareStatus": NotRequired[ShareStatusType],
        "CreationTime": NotRequired[str],
        "ModificationTime": NotRequired[str],
    },
)

FirewallRuleTypeDef = TypedDict(
    "FirewallRuleTypeDef",
    {
        "FirewallRuleGroupId": NotRequired[str],
        "FirewallDomainListId": NotRequired[str],
        "Name": NotRequired[str],
        "Priority": NotRequired[int],
        "Action": NotRequired[ActionType],
        "BlockResponse": NotRequired[BlockResponseType],
        "BlockOverrideDomain": NotRequired[str],
        "BlockOverrideDnsType": NotRequired[Literal["CNAME"]],
        "BlockOverrideTtl": NotRequired[int],
        "CreatorRequestId": NotRequired[str],
        "CreationTime": NotRequired[str],
        "ModificationTime": NotRequired[str],
    },
)

GetFirewallConfigRequestRequestTypeDef = TypedDict(
    "GetFirewallConfigRequestRequestTypeDef",
    {
        "ResourceId": str,
    },
)

GetFirewallConfigResponseTypeDef = TypedDict(
    "GetFirewallConfigResponseTypeDef",
    {
        "FirewallConfig": "FirewallConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFirewallDomainListRequestRequestTypeDef = TypedDict(
    "GetFirewallDomainListRequestRequestTypeDef",
    {
        "FirewallDomainListId": str,
    },
)

GetFirewallDomainListResponseTypeDef = TypedDict(
    "GetFirewallDomainListResponseTypeDef",
    {
        "FirewallDomainList": "FirewallDomainListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFirewallRuleGroupAssociationRequestRequestTypeDef = TypedDict(
    "GetFirewallRuleGroupAssociationRequestRequestTypeDef",
    {
        "FirewallRuleGroupAssociationId": str,
    },
)

GetFirewallRuleGroupAssociationResponseTypeDef = TypedDict(
    "GetFirewallRuleGroupAssociationResponseTypeDef",
    {
        "FirewallRuleGroupAssociation": "FirewallRuleGroupAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFirewallRuleGroupPolicyRequestRequestTypeDef = TypedDict(
    "GetFirewallRuleGroupPolicyRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

GetFirewallRuleGroupPolicyResponseTypeDef = TypedDict(
    "GetFirewallRuleGroupPolicyResponseTypeDef",
    {
        "FirewallRuleGroupPolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFirewallRuleGroupRequestRequestTypeDef = TypedDict(
    "GetFirewallRuleGroupRequestRequestTypeDef",
    {
        "FirewallRuleGroupId": str,
    },
)

GetFirewallRuleGroupResponseTypeDef = TypedDict(
    "GetFirewallRuleGroupResponseTypeDef",
    {
        "FirewallRuleGroup": "FirewallRuleGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverConfigRequestRequestTypeDef = TypedDict(
    "GetResolverConfigRequestRequestTypeDef",
    {
        "ResourceId": str,
    },
)

GetResolverConfigResponseTypeDef = TypedDict(
    "GetResolverConfigResponseTypeDef",
    {
        "ResolverConfig": "ResolverConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverDnssecConfigRequestRequestTypeDef = TypedDict(
    "GetResolverDnssecConfigRequestRequestTypeDef",
    {
        "ResourceId": str,
    },
)

GetResolverDnssecConfigResponseTypeDef = TypedDict(
    "GetResolverDnssecConfigResponseTypeDef",
    {
        "ResolverDNSSECConfig": "ResolverDnssecConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverEndpointRequestRequestTypeDef = TypedDict(
    "GetResolverEndpointRequestRequestTypeDef",
    {
        "ResolverEndpointId": str,
    },
)

GetResolverEndpointResponseTypeDef = TypedDict(
    "GetResolverEndpointResponseTypeDef",
    {
        "ResolverEndpoint": "ResolverEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverQueryLogConfigAssociationRequestRequestTypeDef = TypedDict(
    "GetResolverQueryLogConfigAssociationRequestRequestTypeDef",
    {
        "ResolverQueryLogConfigAssociationId": str,
    },
)

GetResolverQueryLogConfigAssociationResponseTypeDef = TypedDict(
    "GetResolverQueryLogConfigAssociationResponseTypeDef",
    {
        "ResolverQueryLogConfigAssociation": "ResolverQueryLogConfigAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverQueryLogConfigPolicyRequestRequestTypeDef = TypedDict(
    "GetResolverQueryLogConfigPolicyRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

GetResolverQueryLogConfigPolicyResponseTypeDef = TypedDict(
    "GetResolverQueryLogConfigPolicyResponseTypeDef",
    {
        "ResolverQueryLogConfigPolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverQueryLogConfigRequestRequestTypeDef = TypedDict(
    "GetResolverQueryLogConfigRequestRequestTypeDef",
    {
        "ResolverQueryLogConfigId": str,
    },
)

GetResolverQueryLogConfigResponseTypeDef = TypedDict(
    "GetResolverQueryLogConfigResponseTypeDef",
    {
        "ResolverQueryLogConfig": "ResolverQueryLogConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverRuleAssociationRequestRequestTypeDef = TypedDict(
    "GetResolverRuleAssociationRequestRequestTypeDef",
    {
        "ResolverRuleAssociationId": str,
    },
)

GetResolverRuleAssociationResponseTypeDef = TypedDict(
    "GetResolverRuleAssociationResponseTypeDef",
    {
        "ResolverRuleAssociation": "ResolverRuleAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverRulePolicyRequestRequestTypeDef = TypedDict(
    "GetResolverRulePolicyRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

GetResolverRulePolicyResponseTypeDef = TypedDict(
    "GetResolverRulePolicyResponseTypeDef",
    {
        "ResolverRulePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverRuleRequestRequestTypeDef = TypedDict(
    "GetResolverRuleRequestRequestTypeDef",
    {
        "ResolverRuleId": str,
    },
)

GetResolverRuleResponseTypeDef = TypedDict(
    "GetResolverRuleResponseTypeDef",
    {
        "ResolverRule": "ResolverRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportFirewallDomainsRequestRequestTypeDef = TypedDict(
    "ImportFirewallDomainsRequestRequestTypeDef",
    {
        "FirewallDomainListId": str,
        "Operation": Literal["REPLACE"],
        "DomainFileUrl": str,
    },
)

ImportFirewallDomainsResponseTypeDef = TypedDict(
    "ImportFirewallDomainsResponseTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": FirewallDomainListStatusType,
        "StatusMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IpAddressRequestTypeDef = TypedDict(
    "IpAddressRequestTypeDef",
    {
        "SubnetId": str,
        "Ip": NotRequired[str],
    },
)

IpAddressResponseTypeDef = TypedDict(
    "IpAddressResponseTypeDef",
    {
        "IpId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "Ip": NotRequired[str],
        "Status": NotRequired[IpAddressStatusType],
        "StatusMessage": NotRequired[str],
        "CreationTime": NotRequired[str],
        "ModificationTime": NotRequired[str],
    },
)

IpAddressUpdateTypeDef = TypedDict(
    "IpAddressUpdateTypeDef",
    {
        "IpId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "Ip": NotRequired[str],
    },
)

ListFirewallConfigsRequestRequestTypeDef = TypedDict(
    "ListFirewallConfigsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListFirewallConfigsResponseTypeDef = TypedDict(
    "ListFirewallConfigsResponseTypeDef",
    {
        "NextToken": str,
        "FirewallConfigs": List["FirewallConfigTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFirewallDomainListsRequestRequestTypeDef = TypedDict(
    "ListFirewallDomainListsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListFirewallDomainListsResponseTypeDef = TypedDict(
    "ListFirewallDomainListsResponseTypeDef",
    {
        "NextToken": str,
        "FirewallDomainLists": List["FirewallDomainListMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFirewallDomainsRequestRequestTypeDef = TypedDict(
    "ListFirewallDomainsRequestRequestTypeDef",
    {
        "FirewallDomainListId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListFirewallDomainsResponseTypeDef = TypedDict(
    "ListFirewallDomainsResponseTypeDef",
    {
        "NextToken": str,
        "Domains": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFirewallRuleGroupAssociationsRequestRequestTypeDef = TypedDict(
    "ListFirewallRuleGroupAssociationsRequestRequestTypeDef",
    {
        "FirewallRuleGroupId": NotRequired[str],
        "VpcId": NotRequired[str],
        "Priority": NotRequired[int],
        "Status": NotRequired[FirewallRuleGroupAssociationStatusType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListFirewallRuleGroupAssociationsResponseTypeDef = TypedDict(
    "ListFirewallRuleGroupAssociationsResponseTypeDef",
    {
        "NextToken": str,
        "FirewallRuleGroupAssociations": List["FirewallRuleGroupAssociationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFirewallRuleGroupsRequestRequestTypeDef = TypedDict(
    "ListFirewallRuleGroupsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListFirewallRuleGroupsResponseTypeDef = TypedDict(
    "ListFirewallRuleGroupsResponseTypeDef",
    {
        "NextToken": str,
        "FirewallRuleGroups": List["FirewallRuleGroupMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFirewallRulesRequestRequestTypeDef = TypedDict(
    "ListFirewallRulesRequestRequestTypeDef",
    {
        "FirewallRuleGroupId": str,
        "Priority": NotRequired[int],
        "Action": NotRequired[ActionType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListFirewallRulesResponseTypeDef = TypedDict(
    "ListFirewallRulesResponseTypeDef",
    {
        "NextToken": str,
        "FirewallRules": List["FirewallRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResolverConfigsRequestRequestTypeDef = TypedDict(
    "ListResolverConfigsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListResolverConfigsResponseTypeDef = TypedDict(
    "ListResolverConfigsResponseTypeDef",
    {
        "NextToken": str,
        "ResolverConfigs": List["ResolverConfigTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResolverDnssecConfigsRequestRequestTypeDef = TypedDict(
    "ListResolverDnssecConfigsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

ListResolverDnssecConfigsResponseTypeDef = TypedDict(
    "ListResolverDnssecConfigsResponseTypeDef",
    {
        "NextToken": str,
        "ResolverDnssecConfigs": List["ResolverDnssecConfigTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResolverEndpointIpAddressesRequestRequestTypeDef = TypedDict(
    "ListResolverEndpointIpAddressesRequestRequestTypeDef",
    {
        "ResolverEndpointId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListResolverEndpointIpAddressesResponseTypeDef = TypedDict(
    "ListResolverEndpointIpAddressesResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "IpAddresses": List["IpAddressResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResolverEndpointsRequestRequestTypeDef = TypedDict(
    "ListResolverEndpointsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

ListResolverEndpointsResponseTypeDef = TypedDict(
    "ListResolverEndpointsResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResolverEndpoints": List["ResolverEndpointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResolverQueryLogConfigAssociationsRequestRequestTypeDef = TypedDict(
    "ListResolverQueryLogConfigAssociationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "SortBy": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
    },
)

ListResolverQueryLogConfigAssociationsResponseTypeDef = TypedDict(
    "ListResolverQueryLogConfigAssociationsResponseTypeDef",
    {
        "NextToken": str,
        "TotalCount": int,
        "TotalFilteredCount": int,
        "ResolverQueryLogConfigAssociations": List["ResolverQueryLogConfigAssociationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResolverQueryLogConfigsRequestRequestTypeDef = TypedDict(
    "ListResolverQueryLogConfigsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "SortBy": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
    },
)

ListResolverQueryLogConfigsResponseTypeDef = TypedDict(
    "ListResolverQueryLogConfigsResponseTypeDef",
    {
        "NextToken": str,
        "TotalCount": int,
        "TotalFilteredCount": int,
        "ResolverQueryLogConfigs": List["ResolverQueryLogConfigTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResolverRuleAssociationsRequestRequestTypeDef = TypedDict(
    "ListResolverRuleAssociationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

ListResolverRuleAssociationsResponseTypeDef = TypedDict(
    "ListResolverRuleAssociationsResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResolverRuleAssociations": List["ResolverRuleAssociationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResolverRulesRequestRequestTypeDef = TypedDict(
    "ListResolverRulesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

ListResolverRulesResponseTypeDef = TypedDict(
    "ListResolverRulesResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResolverRules": List["ResolverRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
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

PutFirewallRuleGroupPolicyRequestRequestTypeDef = TypedDict(
    "PutFirewallRuleGroupPolicyRequestRequestTypeDef",
    {
        "Arn": str,
        "FirewallRuleGroupPolicy": str,
    },
)

PutFirewallRuleGroupPolicyResponseTypeDef = TypedDict(
    "PutFirewallRuleGroupPolicyResponseTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutResolverQueryLogConfigPolicyRequestRequestTypeDef = TypedDict(
    "PutResolverQueryLogConfigPolicyRequestRequestTypeDef",
    {
        "Arn": str,
        "ResolverQueryLogConfigPolicy": str,
    },
)

PutResolverQueryLogConfigPolicyResponseTypeDef = TypedDict(
    "PutResolverQueryLogConfigPolicyResponseTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutResolverRulePolicyRequestRequestTypeDef = TypedDict(
    "PutResolverRulePolicyRequestRequestTypeDef",
    {
        "Arn": str,
        "ResolverRulePolicy": str,
    },
)

PutResolverRulePolicyResponseTypeDef = TypedDict(
    "PutResolverRulePolicyResponseTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResolverConfigTypeDef = TypedDict(
    "ResolverConfigTypeDef",
    {
        "Id": NotRequired[str],
        "ResourceId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "AutodefinedReverse": NotRequired[ResolverAutodefinedReverseStatusType],
    },
)

ResolverDnssecConfigTypeDef = TypedDict(
    "ResolverDnssecConfigTypeDef",
    {
        "Id": NotRequired[str],
        "OwnerId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ValidationStatus": NotRequired[ResolverDNSSECValidationStatusType],
    },
)

ResolverEndpointTypeDef = TypedDict(
    "ResolverEndpointTypeDef",
    {
        "Id": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "SecurityGroupIds": NotRequired[List[str]],
        "Direction": NotRequired[ResolverEndpointDirectionType],
        "IpAddressCount": NotRequired[int],
        "HostVPCId": NotRequired[str],
        "Status": NotRequired[ResolverEndpointStatusType],
        "StatusMessage": NotRequired[str],
        "CreationTime": NotRequired[str],
        "ModificationTime": NotRequired[str],
    },
)

ResolverQueryLogConfigAssociationTypeDef = TypedDict(
    "ResolverQueryLogConfigAssociationTypeDef",
    {
        "Id": NotRequired[str],
        "ResolverQueryLogConfigId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "Status": NotRequired[ResolverQueryLogConfigAssociationStatusType],
        "Error": NotRequired[ResolverQueryLogConfigAssociationErrorType],
        "ErrorMessage": NotRequired[str],
        "CreationTime": NotRequired[str],
    },
)

ResolverQueryLogConfigTypeDef = TypedDict(
    "ResolverQueryLogConfigTypeDef",
    {
        "Id": NotRequired[str],
        "OwnerId": NotRequired[str],
        "Status": NotRequired[ResolverQueryLogConfigStatusType],
        "ShareStatus": NotRequired[ShareStatusType],
        "AssociationCount": NotRequired[int],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "DestinationArn": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "CreationTime": NotRequired[str],
    },
)

ResolverRuleAssociationTypeDef = TypedDict(
    "ResolverRuleAssociationTypeDef",
    {
        "Id": NotRequired[str],
        "ResolverRuleId": NotRequired[str],
        "Name": NotRequired[str],
        "VPCId": NotRequired[str],
        "Status": NotRequired[ResolverRuleAssociationStatusType],
        "StatusMessage": NotRequired[str],
    },
)

ResolverRuleConfigTypeDef = TypedDict(
    "ResolverRuleConfigTypeDef",
    {
        "Name": NotRequired[str],
        "TargetIps": NotRequired[Sequence["TargetAddressTypeDef"]],
        "ResolverEndpointId": NotRequired[str],
    },
)

ResolverRuleTypeDef = TypedDict(
    "ResolverRuleTypeDef",
    {
        "Id": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "Arn": NotRequired[str],
        "DomainName": NotRequired[str],
        "Status": NotRequired[ResolverRuleStatusType],
        "StatusMessage": NotRequired[str],
        "RuleType": NotRequired[RuleTypeOptionType],
        "Name": NotRequired[str],
        "TargetIps": NotRequired[List["TargetAddressTypeDef"]],
        "ResolverEndpointId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "ShareStatus": NotRequired[ShareStatusType],
        "CreationTime": NotRequired[str],
        "ModificationTime": NotRequired[str],
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

TargetAddressTypeDef = TypedDict(
    "TargetAddressTypeDef",
    {
        "Ip": str,
        "Port": NotRequired[int],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateFirewallConfigRequestRequestTypeDef = TypedDict(
    "UpdateFirewallConfigRequestRequestTypeDef",
    {
        "ResourceId": str,
        "FirewallFailOpen": FirewallFailOpenStatusType,
    },
)

UpdateFirewallConfigResponseTypeDef = TypedDict(
    "UpdateFirewallConfigResponseTypeDef",
    {
        "FirewallConfig": "FirewallConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFirewallDomainsRequestRequestTypeDef = TypedDict(
    "UpdateFirewallDomainsRequestRequestTypeDef",
    {
        "FirewallDomainListId": str,
        "Operation": FirewallDomainUpdateOperationType,
        "Domains": Sequence[str],
    },
)

UpdateFirewallDomainsResponseTypeDef = TypedDict(
    "UpdateFirewallDomainsResponseTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": FirewallDomainListStatusType,
        "StatusMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFirewallRuleGroupAssociationRequestRequestTypeDef = TypedDict(
    "UpdateFirewallRuleGroupAssociationRequestRequestTypeDef",
    {
        "FirewallRuleGroupAssociationId": str,
        "Priority": NotRequired[int],
        "MutationProtection": NotRequired[MutationProtectionStatusType],
        "Name": NotRequired[str],
    },
)

UpdateFirewallRuleGroupAssociationResponseTypeDef = TypedDict(
    "UpdateFirewallRuleGroupAssociationResponseTypeDef",
    {
        "FirewallRuleGroupAssociation": "FirewallRuleGroupAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFirewallRuleRequestRequestTypeDef = TypedDict(
    "UpdateFirewallRuleRequestRequestTypeDef",
    {
        "FirewallRuleGroupId": str,
        "FirewallDomainListId": str,
        "Priority": NotRequired[int],
        "Action": NotRequired[ActionType],
        "BlockResponse": NotRequired[BlockResponseType],
        "BlockOverrideDomain": NotRequired[str],
        "BlockOverrideDnsType": NotRequired[Literal["CNAME"]],
        "BlockOverrideTtl": NotRequired[int],
        "Name": NotRequired[str],
    },
)

UpdateFirewallRuleResponseTypeDef = TypedDict(
    "UpdateFirewallRuleResponseTypeDef",
    {
        "FirewallRule": "FirewallRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateResolverConfigRequestRequestTypeDef = TypedDict(
    "UpdateResolverConfigRequestRequestTypeDef",
    {
        "ResourceId": str,
        "AutodefinedReverseFlag": AutodefinedReverseFlagType,
    },
)

UpdateResolverConfigResponseTypeDef = TypedDict(
    "UpdateResolverConfigResponseTypeDef",
    {
        "ResolverConfig": "ResolverConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateResolverDnssecConfigRequestRequestTypeDef = TypedDict(
    "UpdateResolverDnssecConfigRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Validation": ValidationType,
    },
)

UpdateResolverDnssecConfigResponseTypeDef = TypedDict(
    "UpdateResolverDnssecConfigResponseTypeDef",
    {
        "ResolverDNSSECConfig": "ResolverDnssecConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateResolverEndpointRequestRequestTypeDef = TypedDict(
    "UpdateResolverEndpointRequestRequestTypeDef",
    {
        "ResolverEndpointId": str,
        "Name": NotRequired[str],
    },
)

UpdateResolverEndpointResponseTypeDef = TypedDict(
    "UpdateResolverEndpointResponseTypeDef",
    {
        "ResolverEndpoint": "ResolverEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateResolverRuleRequestRequestTypeDef = TypedDict(
    "UpdateResolverRuleRequestRequestTypeDef",
    {
        "ResolverRuleId": str,
        "Config": "ResolverRuleConfigTypeDef",
    },
)

UpdateResolverRuleResponseTypeDef = TypedDict(
    "UpdateResolverRuleResponseTypeDef",
    {
        "ResolverRule": "ResolverRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
