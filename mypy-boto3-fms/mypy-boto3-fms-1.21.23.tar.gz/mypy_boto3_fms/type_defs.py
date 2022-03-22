"""
Type annotations for fms service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/type_defs.html)

Usage::

    ```python
    from mypy_boto3_fms.type_defs import ActionTargetTypeDef

    data: ActionTargetTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AccountRoleStatusType,
    CustomerPolicyScopeIdTypeType,
    DependentServiceNameType,
    DestinationTypeType,
    PolicyComplianceStatusTypeType,
    RemediationActionTypeType,
    SecurityServiceTypeType,
    TargetTypeType,
    ViolationReasonType,
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
    "ActionTargetTypeDef",
    "AppTypeDef",
    "AppsListDataSummaryTypeDef",
    "AppsListDataTypeDef",
    "AssociateAdminAccountRequestRequestTypeDef",
    "AwsEc2InstanceViolationTypeDef",
    "AwsEc2NetworkInterfaceViolationTypeDef",
    "AwsVPCSecurityGroupViolationTypeDef",
    "ComplianceViolatorTypeDef",
    "DeleteAppsListRequestRequestTypeDef",
    "DeletePolicyRequestRequestTypeDef",
    "DeleteProtocolsListRequestRequestTypeDef",
    "DnsDuplicateRuleGroupViolationTypeDef",
    "DnsRuleGroupLimitExceededViolationTypeDef",
    "DnsRuleGroupPriorityConflictViolationTypeDef",
    "EC2AssociateRouteTableActionTypeDef",
    "EC2CopyRouteTableActionTypeDef",
    "EC2CreateRouteActionTypeDef",
    "EC2CreateRouteTableActionTypeDef",
    "EC2DeleteRouteActionTypeDef",
    "EC2ReplaceRouteActionTypeDef",
    "EC2ReplaceRouteTableAssociationActionTypeDef",
    "EvaluationResultTypeDef",
    "ExpectedRouteTypeDef",
    "FMSPolicyUpdateFirewallCreationConfigActionTypeDef",
    "FirewallSubnetIsOutOfScopeViolationTypeDef",
    "GetAdminAccountResponseTypeDef",
    "GetAppsListRequestRequestTypeDef",
    "GetAppsListResponseTypeDef",
    "GetComplianceDetailRequestRequestTypeDef",
    "GetComplianceDetailResponseTypeDef",
    "GetNotificationChannelResponseTypeDef",
    "GetPolicyRequestRequestTypeDef",
    "GetPolicyResponseTypeDef",
    "GetProtectionStatusRequestRequestTypeDef",
    "GetProtectionStatusResponseTypeDef",
    "GetProtocolsListRequestRequestTypeDef",
    "GetProtocolsListResponseTypeDef",
    "GetViolationDetailsRequestRequestTypeDef",
    "GetViolationDetailsResponseTypeDef",
    "ListAppsListsRequestRequestTypeDef",
    "ListAppsListsResponseTypeDef",
    "ListComplianceStatusRequestRequestTypeDef",
    "ListComplianceStatusResponseTypeDef",
    "ListMemberAccountsRequestRequestTypeDef",
    "ListMemberAccountsResponseTypeDef",
    "ListPoliciesRequestRequestTypeDef",
    "ListPoliciesResponseTypeDef",
    "ListProtocolsListsRequestRequestTypeDef",
    "ListProtocolsListsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NetworkFirewallBlackHoleRouteDetectedViolationTypeDef",
    "NetworkFirewallInternetTrafficNotInspectedViolationTypeDef",
    "NetworkFirewallInvalidRouteConfigurationViolationTypeDef",
    "NetworkFirewallMissingExpectedRTViolationTypeDef",
    "NetworkFirewallMissingExpectedRoutesViolationTypeDef",
    "NetworkFirewallMissingFirewallViolationTypeDef",
    "NetworkFirewallMissingSubnetViolationTypeDef",
    "NetworkFirewallPolicyDescriptionTypeDef",
    "NetworkFirewallPolicyModifiedViolationTypeDef",
    "NetworkFirewallPolicyTypeDef",
    "NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef",
    "NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef",
    "PaginatorConfigTypeDef",
    "PartialMatchTypeDef",
    "PolicyComplianceDetailTypeDef",
    "PolicyComplianceStatusTypeDef",
    "PolicyOptionTypeDef",
    "PolicySummaryTypeDef",
    "PolicyTypeDef",
    "PossibleRemediationActionTypeDef",
    "PossibleRemediationActionsTypeDef",
    "ProtocolsListDataSummaryTypeDef",
    "ProtocolsListDataTypeDef",
    "PutAppsListRequestRequestTypeDef",
    "PutAppsListResponseTypeDef",
    "PutNotificationChannelRequestRequestTypeDef",
    "PutPolicyRequestRequestTypeDef",
    "PutPolicyResponseTypeDef",
    "PutProtocolsListRequestRequestTypeDef",
    "PutProtocolsListResponseTypeDef",
    "RemediationActionTypeDef",
    "RemediationActionWithOrderTypeDef",
    "ResourceTagTypeDef",
    "ResourceViolationTypeDef",
    "ResponseMetadataTypeDef",
    "RouteHasOutOfScopeEndpointViolationTypeDef",
    "RouteTypeDef",
    "SecurityGroupRemediationActionTypeDef",
    "SecurityGroupRuleDescriptionTypeDef",
    "SecurityServicePolicyDataTypeDef",
    "StatefulRuleGroupTypeDef",
    "StatelessRuleGroupTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ViolationDetailTypeDef",
)

ActionTargetTypeDef = TypedDict(
    "ActionTargetTypeDef",
    {
        "ResourceId": NotRequired[str],
        "Description": NotRequired[str],
    },
)

AppTypeDef = TypedDict(
    "AppTypeDef",
    {
        "AppName": str,
        "Protocol": str,
        "Port": int,
    },
)

AppsListDataSummaryTypeDef = TypedDict(
    "AppsListDataSummaryTypeDef",
    {
        "ListArn": NotRequired[str],
        "ListId": NotRequired[str],
        "ListName": NotRequired[str],
        "AppsList": NotRequired[List["AppTypeDef"]],
    },
)

AppsListDataTypeDef = TypedDict(
    "AppsListDataTypeDef",
    {
        "ListName": str,
        "AppsList": List["AppTypeDef"],
        "ListId": NotRequired[str],
        "ListUpdateToken": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "LastUpdateTime": NotRequired[datetime],
        "PreviousAppsList": NotRequired[Dict[str, List["AppTypeDef"]]],
    },
)

AssociateAdminAccountRequestRequestTypeDef = TypedDict(
    "AssociateAdminAccountRequestRequestTypeDef",
    {
        "AdminAccount": str,
    },
)

AwsEc2InstanceViolationTypeDef = TypedDict(
    "AwsEc2InstanceViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "AwsEc2NetworkInterfaceViolations": NotRequired[
            List["AwsEc2NetworkInterfaceViolationTypeDef"]
        ],
    },
)

AwsEc2NetworkInterfaceViolationTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "ViolatingSecurityGroups": NotRequired[List[str]],
    },
)

AwsVPCSecurityGroupViolationTypeDef = TypedDict(
    "AwsVPCSecurityGroupViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "ViolationTargetDescription": NotRequired[str],
        "PartialMatches": NotRequired[List["PartialMatchTypeDef"]],
        "PossibleSecurityGroupRemediationActions": NotRequired[
            List["SecurityGroupRemediationActionTypeDef"]
        ],
    },
)

ComplianceViolatorTypeDef = TypedDict(
    "ComplianceViolatorTypeDef",
    {
        "ResourceId": NotRequired[str],
        "ViolationReason": NotRequired[ViolationReasonType],
        "ResourceType": NotRequired[str],
        "Metadata": NotRequired[Dict[str, str]],
    },
)

DeleteAppsListRequestRequestTypeDef = TypedDict(
    "DeleteAppsListRequestRequestTypeDef",
    {
        "ListId": str,
    },
)

DeletePolicyRequestRequestTypeDef = TypedDict(
    "DeletePolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
        "DeleteAllPolicyResources": NotRequired[bool],
    },
)

DeleteProtocolsListRequestRequestTypeDef = TypedDict(
    "DeleteProtocolsListRequestRequestTypeDef",
    {
        "ListId": str,
    },
)

DnsDuplicateRuleGroupViolationTypeDef = TypedDict(
    "DnsDuplicateRuleGroupViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "ViolationTargetDescription": NotRequired[str],
    },
)

DnsRuleGroupLimitExceededViolationTypeDef = TypedDict(
    "DnsRuleGroupLimitExceededViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "ViolationTargetDescription": NotRequired[str],
        "NumberOfRuleGroupsAlreadyAssociated": NotRequired[int],
    },
)

DnsRuleGroupPriorityConflictViolationTypeDef = TypedDict(
    "DnsRuleGroupPriorityConflictViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "ViolationTargetDescription": NotRequired[str],
        "ConflictingPriority": NotRequired[int],
        "ConflictingPolicyId": NotRequired[str],
        "UnavailablePriorities": NotRequired[List[int]],
    },
)

EC2AssociateRouteTableActionTypeDef = TypedDict(
    "EC2AssociateRouteTableActionTypeDef",
    {
        "RouteTableId": "ActionTargetTypeDef",
        "Description": NotRequired[str],
        "SubnetId": NotRequired["ActionTargetTypeDef"],
        "GatewayId": NotRequired["ActionTargetTypeDef"],
    },
)

EC2CopyRouteTableActionTypeDef = TypedDict(
    "EC2CopyRouteTableActionTypeDef",
    {
        "VpcId": "ActionTargetTypeDef",
        "RouteTableId": "ActionTargetTypeDef",
        "Description": NotRequired[str],
    },
)

EC2CreateRouteActionTypeDef = TypedDict(
    "EC2CreateRouteActionTypeDef",
    {
        "RouteTableId": "ActionTargetTypeDef",
        "Description": NotRequired[str],
        "DestinationCidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "DestinationIpv6CidrBlock": NotRequired[str],
        "VpcEndpointId": NotRequired["ActionTargetTypeDef"],
        "GatewayId": NotRequired["ActionTargetTypeDef"],
    },
)

EC2CreateRouteTableActionTypeDef = TypedDict(
    "EC2CreateRouteTableActionTypeDef",
    {
        "VpcId": "ActionTargetTypeDef",
        "Description": NotRequired[str],
    },
)

EC2DeleteRouteActionTypeDef = TypedDict(
    "EC2DeleteRouteActionTypeDef",
    {
        "RouteTableId": "ActionTargetTypeDef",
        "Description": NotRequired[str],
        "DestinationCidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "DestinationIpv6CidrBlock": NotRequired[str],
    },
)

EC2ReplaceRouteActionTypeDef = TypedDict(
    "EC2ReplaceRouteActionTypeDef",
    {
        "RouteTableId": "ActionTargetTypeDef",
        "Description": NotRequired[str],
        "DestinationCidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "DestinationIpv6CidrBlock": NotRequired[str],
        "GatewayId": NotRequired["ActionTargetTypeDef"],
    },
)

EC2ReplaceRouteTableAssociationActionTypeDef = TypedDict(
    "EC2ReplaceRouteTableAssociationActionTypeDef",
    {
        "AssociationId": "ActionTargetTypeDef",
        "RouteTableId": "ActionTargetTypeDef",
        "Description": NotRequired[str],
    },
)

EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "ComplianceStatus": NotRequired[PolicyComplianceStatusTypeType],
        "ViolatorCount": NotRequired[int],
        "EvaluationLimitExceeded": NotRequired[bool],
    },
)

ExpectedRouteTypeDef = TypedDict(
    "ExpectedRouteTypeDef",
    {
        "IpV4Cidr": NotRequired[str],
        "PrefixListId": NotRequired[str],
        "IpV6Cidr": NotRequired[str],
        "ContributingSubnets": NotRequired[List[str]],
        "AllowedTargets": NotRequired[List[str]],
        "RouteTableId": NotRequired[str],
    },
)

FMSPolicyUpdateFirewallCreationConfigActionTypeDef = TypedDict(
    "FMSPolicyUpdateFirewallCreationConfigActionTypeDef",
    {
        "Description": NotRequired[str],
        "FirewallCreationConfig": NotRequired[str],
    },
)

FirewallSubnetIsOutOfScopeViolationTypeDef = TypedDict(
    "FirewallSubnetIsOutOfScopeViolationTypeDef",
    {
        "FirewallSubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetAvailabilityZone": NotRequired[str],
        "SubnetAvailabilityZoneId": NotRequired[str],
        "VpcEndpointId": NotRequired[str],
    },
)

GetAdminAccountResponseTypeDef = TypedDict(
    "GetAdminAccountResponseTypeDef",
    {
        "AdminAccount": str,
        "RoleStatus": AccountRoleStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppsListRequestRequestTypeDef = TypedDict(
    "GetAppsListRequestRequestTypeDef",
    {
        "ListId": str,
        "DefaultList": NotRequired[bool],
    },
)

GetAppsListResponseTypeDef = TypedDict(
    "GetAppsListResponseTypeDef",
    {
        "AppsList": "AppsListDataTypeDef",
        "AppsListArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComplianceDetailRequestRequestTypeDef = TypedDict(
    "GetComplianceDetailRequestRequestTypeDef",
    {
        "PolicyId": str,
        "MemberAccount": str,
    },
)

GetComplianceDetailResponseTypeDef = TypedDict(
    "GetComplianceDetailResponseTypeDef",
    {
        "PolicyComplianceDetail": "PolicyComplianceDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNotificationChannelResponseTypeDef = TypedDict(
    "GetNotificationChannelResponseTypeDef",
    {
        "SnsTopicArn": str,
        "SnsRoleName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyRequestRequestTypeDef = TypedDict(
    "GetPolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)

GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef",
    {
        "Policy": "PolicyTypeDef",
        "PolicyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProtectionStatusRequestRequestTypeDef = TypedDict(
    "GetProtectionStatusRequestRequestTypeDef",
    {
        "PolicyId": str,
        "MemberAccountId": NotRequired[str],
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetProtectionStatusResponseTypeDef = TypedDict(
    "GetProtectionStatusResponseTypeDef",
    {
        "AdminAccountId": str,
        "ServiceType": SecurityServiceTypeType,
        "Data": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProtocolsListRequestRequestTypeDef = TypedDict(
    "GetProtocolsListRequestRequestTypeDef",
    {
        "ListId": str,
        "DefaultList": NotRequired[bool],
    },
)

GetProtocolsListResponseTypeDef = TypedDict(
    "GetProtocolsListResponseTypeDef",
    {
        "ProtocolsList": "ProtocolsListDataTypeDef",
        "ProtocolsListArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetViolationDetailsRequestRequestTypeDef = TypedDict(
    "GetViolationDetailsRequestRequestTypeDef",
    {
        "PolicyId": str,
        "MemberAccount": str,
        "ResourceId": str,
        "ResourceType": str,
    },
)

GetViolationDetailsResponseTypeDef = TypedDict(
    "GetViolationDetailsResponseTypeDef",
    {
        "ViolationDetail": "ViolationDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppsListsRequestRequestTypeDef = TypedDict(
    "ListAppsListsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "DefaultLists": NotRequired[bool],
        "NextToken": NotRequired[str],
    },
)

ListAppsListsResponseTypeDef = TypedDict(
    "ListAppsListsResponseTypeDef",
    {
        "AppsLists": List["AppsListDataSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListComplianceStatusRequestRequestTypeDef = TypedDict(
    "ListComplianceStatusRequestRequestTypeDef",
    {
        "PolicyId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListComplianceStatusResponseTypeDef = TypedDict(
    "ListComplianceStatusResponseTypeDef",
    {
        "PolicyComplianceStatusList": List["PolicyComplianceStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMemberAccountsRequestRequestTypeDef = TypedDict(
    "ListMemberAccountsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListMemberAccountsResponseTypeDef = TypedDict(
    "ListMemberAccountsResponseTypeDef",
    {
        "MemberAccounts": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPoliciesRequestRequestTypeDef = TypedDict(
    "ListPoliciesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListPoliciesResponseTypeDef = TypedDict(
    "ListPoliciesResponseTypeDef",
    {
        "PolicyList": List["PolicySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProtocolsListsRequestRequestTypeDef = TypedDict(
    "ListProtocolsListsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "DefaultLists": NotRequired[bool],
        "NextToken": NotRequired[str],
    },
)

ListProtocolsListsResponseTypeDef = TypedDict(
    "ListProtocolsListsResponseTypeDef",
    {
        "ProtocolsLists": List["ProtocolsListDataSummaryTypeDef"],
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
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkFirewallBlackHoleRouteDetectedViolationTypeDef = TypedDict(
    "NetworkFirewallBlackHoleRouteDetectedViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "RouteTableId": NotRequired[str],
        "VpcId": NotRequired[str],
        "ViolatingRoutes": NotRequired[List["RouteTypeDef"]],
    },
)

NetworkFirewallInternetTrafficNotInspectedViolationTypeDef = TypedDict(
    "NetworkFirewallInternetTrafficNotInspectedViolationTypeDef",
    {
        "SubnetId": NotRequired[str],
        "SubnetAvailabilityZone": NotRequired[str],
        "RouteTableId": NotRequired[str],
        "ViolatingRoutes": NotRequired[List["RouteTypeDef"]],
        "IsRouteTableUsedInDifferentAZ": NotRequired[bool],
        "CurrentFirewallSubnetRouteTable": NotRequired[str],
        "ExpectedFirewallEndpoint": NotRequired[str],
        "FirewallSubnetId": NotRequired[str],
        "ExpectedFirewallSubnetRoutes": NotRequired[List["ExpectedRouteTypeDef"]],
        "ActualFirewallSubnetRoutes": NotRequired[List["RouteTypeDef"]],
        "InternetGatewayId": NotRequired[str],
        "CurrentInternetGatewayRouteTable": NotRequired[str],
        "ExpectedInternetGatewayRoutes": NotRequired[List["ExpectedRouteTypeDef"]],
        "ActualInternetGatewayRoutes": NotRequired[List["RouteTypeDef"]],
        "VpcId": NotRequired[str],
    },
)

NetworkFirewallInvalidRouteConfigurationViolationTypeDef = TypedDict(
    "NetworkFirewallInvalidRouteConfigurationViolationTypeDef",
    {
        "AffectedSubnets": NotRequired[List[str]],
        "RouteTableId": NotRequired[str],
        "IsRouteTableUsedInDifferentAZ": NotRequired[bool],
        "ViolatingRoute": NotRequired["RouteTypeDef"],
        "CurrentFirewallSubnetRouteTable": NotRequired[str],
        "ExpectedFirewallEndpoint": NotRequired[str],
        "ActualFirewallEndpoint": NotRequired[str],
        "ExpectedFirewallSubnetId": NotRequired[str],
        "ActualFirewallSubnetId": NotRequired[str],
        "ExpectedFirewallSubnetRoutes": NotRequired[List["ExpectedRouteTypeDef"]],
        "ActualFirewallSubnetRoutes": NotRequired[List["RouteTypeDef"]],
        "InternetGatewayId": NotRequired[str],
        "CurrentInternetGatewayRouteTable": NotRequired[str],
        "ExpectedInternetGatewayRoutes": NotRequired[List["ExpectedRouteTypeDef"]],
        "ActualInternetGatewayRoutes": NotRequired[List["RouteTypeDef"]],
        "VpcId": NotRequired[str],
    },
)

NetworkFirewallMissingExpectedRTViolationTypeDef = TypedDict(
    "NetworkFirewallMissingExpectedRTViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "VPC": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "CurrentRouteTable": NotRequired[str],
        "ExpectedRouteTable": NotRequired[str],
    },
)

NetworkFirewallMissingExpectedRoutesViolationTypeDef = TypedDict(
    "NetworkFirewallMissingExpectedRoutesViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "ExpectedRoutes": NotRequired[List["ExpectedRouteTypeDef"]],
        "VpcId": NotRequired[str],
    },
)

NetworkFirewallMissingFirewallViolationTypeDef = TypedDict(
    "NetworkFirewallMissingFirewallViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "VPC": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "TargetViolationReason": NotRequired[str],
    },
)

NetworkFirewallMissingSubnetViolationTypeDef = TypedDict(
    "NetworkFirewallMissingSubnetViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "VPC": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "TargetViolationReason": NotRequired[str],
    },
)

NetworkFirewallPolicyDescriptionTypeDef = TypedDict(
    "NetworkFirewallPolicyDescriptionTypeDef",
    {
        "StatelessRuleGroups": NotRequired[List["StatelessRuleGroupTypeDef"]],
        "StatelessDefaultActions": NotRequired[List[str]],
        "StatelessFragmentDefaultActions": NotRequired[List[str]],
        "StatelessCustomActions": NotRequired[List[str]],
        "StatefulRuleGroups": NotRequired[List["StatefulRuleGroupTypeDef"]],
    },
)

NetworkFirewallPolicyModifiedViolationTypeDef = TypedDict(
    "NetworkFirewallPolicyModifiedViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "CurrentPolicyDescription": NotRequired["NetworkFirewallPolicyDescriptionTypeDef"],
        "ExpectedPolicyDescription": NotRequired["NetworkFirewallPolicyDescriptionTypeDef"],
    },
)

NetworkFirewallPolicyTypeDef = TypedDict(
    "NetworkFirewallPolicyTypeDef",
    {
        "FirewallDeploymentModel": NotRequired[Literal["CENTRALIZED"]],
    },
)

NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef = TypedDict(
    "NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef",
    {
        "FirewallSubnetId": NotRequired[str],
        "ViolatingRoutes": NotRequired[List["RouteTypeDef"]],
        "RouteTableId": NotRequired[str],
        "FirewallEndpoint": NotRequired[str],
        "VpcId": NotRequired[str],
    },
)

NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef = TypedDict(
    "NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef",
    {
        "GatewayId": NotRequired[str],
        "ViolatingRoutes": NotRequired[List["RouteTypeDef"]],
        "RouteTableId": NotRequired[str],
        "VpcId": NotRequired[str],
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

PartialMatchTypeDef = TypedDict(
    "PartialMatchTypeDef",
    {
        "Reference": NotRequired[str],
        "TargetViolationReasons": NotRequired[List[str]],
    },
)

PolicyComplianceDetailTypeDef = TypedDict(
    "PolicyComplianceDetailTypeDef",
    {
        "PolicyOwner": NotRequired[str],
        "PolicyId": NotRequired[str],
        "MemberAccount": NotRequired[str],
        "Violators": NotRequired[List["ComplianceViolatorTypeDef"]],
        "EvaluationLimitExceeded": NotRequired[bool],
        "ExpiredAt": NotRequired[datetime],
        "IssueInfoMap": NotRequired[Dict[DependentServiceNameType, str]],
    },
)

PolicyComplianceStatusTypeDef = TypedDict(
    "PolicyComplianceStatusTypeDef",
    {
        "PolicyOwner": NotRequired[str],
        "PolicyId": NotRequired[str],
        "PolicyName": NotRequired[str],
        "MemberAccount": NotRequired[str],
        "EvaluationResults": NotRequired[List["EvaluationResultTypeDef"]],
        "LastUpdated": NotRequired[datetime],
        "IssueInfoMap": NotRequired[Dict[DependentServiceNameType, str]],
    },
)

PolicyOptionTypeDef = TypedDict(
    "PolicyOptionTypeDef",
    {
        "NetworkFirewallPolicy": NotRequired["NetworkFirewallPolicyTypeDef"],
    },
)

PolicySummaryTypeDef = TypedDict(
    "PolicySummaryTypeDef",
    {
        "PolicyArn": NotRequired[str],
        "PolicyId": NotRequired[str],
        "PolicyName": NotRequired[str],
        "ResourceType": NotRequired[str],
        "SecurityServiceType": NotRequired[SecurityServiceTypeType],
        "RemediationEnabled": NotRequired[bool],
        "DeleteUnusedFMManagedResources": NotRequired[bool],
    },
)

PolicyTypeDef = TypedDict(
    "PolicyTypeDef",
    {
        "PolicyName": str,
        "SecurityServicePolicyData": "SecurityServicePolicyDataTypeDef",
        "ResourceType": str,
        "ExcludeResourceTags": bool,
        "RemediationEnabled": bool,
        "PolicyId": NotRequired[str],
        "PolicyUpdateToken": NotRequired[str],
        "ResourceTypeList": NotRequired[List[str]],
        "ResourceTags": NotRequired[List["ResourceTagTypeDef"]],
        "DeleteUnusedFMManagedResources": NotRequired[bool],
        "IncludeMap": NotRequired[Dict[CustomerPolicyScopeIdTypeType, List[str]]],
        "ExcludeMap": NotRequired[Dict[CustomerPolicyScopeIdTypeType, List[str]]],
    },
)

PossibleRemediationActionTypeDef = TypedDict(
    "PossibleRemediationActionTypeDef",
    {
        "OrderedRemediationActions": List["RemediationActionWithOrderTypeDef"],
        "Description": NotRequired[str],
        "IsDefaultAction": NotRequired[bool],
    },
)

PossibleRemediationActionsTypeDef = TypedDict(
    "PossibleRemediationActionsTypeDef",
    {
        "Description": NotRequired[str],
        "Actions": NotRequired[List["PossibleRemediationActionTypeDef"]],
    },
)

ProtocolsListDataSummaryTypeDef = TypedDict(
    "ProtocolsListDataSummaryTypeDef",
    {
        "ListArn": NotRequired[str],
        "ListId": NotRequired[str],
        "ListName": NotRequired[str],
        "ProtocolsList": NotRequired[List[str]],
    },
)

ProtocolsListDataTypeDef = TypedDict(
    "ProtocolsListDataTypeDef",
    {
        "ListName": str,
        "ProtocolsList": List[str],
        "ListId": NotRequired[str],
        "ListUpdateToken": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "LastUpdateTime": NotRequired[datetime],
        "PreviousProtocolsList": NotRequired[Dict[str, List[str]]],
    },
)

PutAppsListRequestRequestTypeDef = TypedDict(
    "PutAppsListRequestRequestTypeDef",
    {
        "AppsList": "AppsListDataTypeDef",
        "TagList": NotRequired[Sequence["TagTypeDef"]],
    },
)

PutAppsListResponseTypeDef = TypedDict(
    "PutAppsListResponseTypeDef",
    {
        "AppsList": "AppsListDataTypeDef",
        "AppsListArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutNotificationChannelRequestRequestTypeDef = TypedDict(
    "PutNotificationChannelRequestRequestTypeDef",
    {
        "SnsTopicArn": str,
        "SnsRoleName": str,
    },
)

PutPolicyRequestRequestTypeDef = TypedDict(
    "PutPolicyRequestRequestTypeDef",
    {
        "Policy": "PolicyTypeDef",
        "TagList": NotRequired[Sequence["TagTypeDef"]],
    },
)

PutPolicyResponseTypeDef = TypedDict(
    "PutPolicyResponseTypeDef",
    {
        "Policy": "PolicyTypeDef",
        "PolicyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutProtocolsListRequestRequestTypeDef = TypedDict(
    "PutProtocolsListRequestRequestTypeDef",
    {
        "ProtocolsList": "ProtocolsListDataTypeDef",
        "TagList": NotRequired[Sequence["TagTypeDef"]],
    },
)

PutProtocolsListResponseTypeDef = TypedDict(
    "PutProtocolsListResponseTypeDef",
    {
        "ProtocolsList": "ProtocolsListDataTypeDef",
        "ProtocolsListArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemediationActionTypeDef = TypedDict(
    "RemediationActionTypeDef",
    {
        "Description": NotRequired[str],
        "EC2CreateRouteAction": NotRequired["EC2CreateRouteActionTypeDef"],
        "EC2ReplaceRouteAction": NotRequired["EC2ReplaceRouteActionTypeDef"],
        "EC2DeleteRouteAction": NotRequired["EC2DeleteRouteActionTypeDef"],
        "EC2CopyRouteTableAction": NotRequired["EC2CopyRouteTableActionTypeDef"],
        "EC2ReplaceRouteTableAssociationAction": NotRequired[
            "EC2ReplaceRouteTableAssociationActionTypeDef"
        ],
        "EC2AssociateRouteTableAction": NotRequired["EC2AssociateRouteTableActionTypeDef"],
        "EC2CreateRouteTableAction": NotRequired["EC2CreateRouteTableActionTypeDef"],
        "FMSPolicyUpdateFirewallCreationConfigAction": NotRequired[
            "FMSPolicyUpdateFirewallCreationConfigActionTypeDef"
        ],
    },
)

RemediationActionWithOrderTypeDef = TypedDict(
    "RemediationActionWithOrderTypeDef",
    {
        "RemediationAction": NotRequired["RemediationActionTypeDef"],
        "Order": NotRequired[int],
    },
)

ResourceTagTypeDef = TypedDict(
    "ResourceTagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)

ResourceViolationTypeDef = TypedDict(
    "ResourceViolationTypeDef",
    {
        "AwsVPCSecurityGroupViolation": NotRequired["AwsVPCSecurityGroupViolationTypeDef"],
        "AwsEc2NetworkInterfaceViolation": NotRequired["AwsEc2NetworkInterfaceViolationTypeDef"],
        "AwsEc2InstanceViolation": NotRequired["AwsEc2InstanceViolationTypeDef"],
        "NetworkFirewallMissingFirewallViolation": NotRequired[
            "NetworkFirewallMissingFirewallViolationTypeDef"
        ],
        "NetworkFirewallMissingSubnetViolation": NotRequired[
            "NetworkFirewallMissingSubnetViolationTypeDef"
        ],
        "NetworkFirewallMissingExpectedRTViolation": NotRequired[
            "NetworkFirewallMissingExpectedRTViolationTypeDef"
        ],
        "NetworkFirewallPolicyModifiedViolation": NotRequired[
            "NetworkFirewallPolicyModifiedViolationTypeDef"
        ],
        "NetworkFirewallInternetTrafficNotInspectedViolation": NotRequired[
            "NetworkFirewallInternetTrafficNotInspectedViolationTypeDef"
        ],
        "NetworkFirewallInvalidRouteConfigurationViolation": NotRequired[
            "NetworkFirewallInvalidRouteConfigurationViolationTypeDef"
        ],
        "NetworkFirewallBlackHoleRouteDetectedViolation": NotRequired[
            "NetworkFirewallBlackHoleRouteDetectedViolationTypeDef"
        ],
        "NetworkFirewallUnexpectedFirewallRoutesViolation": NotRequired[
            "NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef"
        ],
        "NetworkFirewallUnexpectedGatewayRoutesViolation": NotRequired[
            "NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef"
        ],
        "NetworkFirewallMissingExpectedRoutesViolation": NotRequired[
            "NetworkFirewallMissingExpectedRoutesViolationTypeDef"
        ],
        "DnsRuleGroupPriorityConflictViolation": NotRequired[
            "DnsRuleGroupPriorityConflictViolationTypeDef"
        ],
        "DnsDuplicateRuleGroupViolation": NotRequired["DnsDuplicateRuleGroupViolationTypeDef"],
        "DnsRuleGroupLimitExceededViolation": NotRequired[
            "DnsRuleGroupLimitExceededViolationTypeDef"
        ],
        "PossibleRemediationActions": NotRequired["PossibleRemediationActionsTypeDef"],
        "FirewallSubnetIsOutOfScopeViolation": NotRequired[
            "FirewallSubnetIsOutOfScopeViolationTypeDef"
        ],
        "RouteHasOutOfScopeEndpointViolation": NotRequired[
            "RouteHasOutOfScopeEndpointViolationTypeDef"
        ],
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

RouteHasOutOfScopeEndpointViolationTypeDef = TypedDict(
    "RouteHasOutOfScopeEndpointViolationTypeDef",
    {
        "SubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
        "RouteTableId": NotRequired[str],
        "ViolatingRoutes": NotRequired[List["RouteTypeDef"]],
        "SubnetAvailabilityZone": NotRequired[str],
        "SubnetAvailabilityZoneId": NotRequired[str],
        "CurrentFirewallSubnetRouteTable": NotRequired[str],
        "FirewallSubnetId": NotRequired[str],
        "FirewallSubnetRoutes": NotRequired[List["RouteTypeDef"]],
        "InternetGatewayId": NotRequired[str],
        "CurrentInternetGatewayRouteTable": NotRequired[str],
        "InternetGatewayRoutes": NotRequired[List["RouteTypeDef"]],
    },
)

RouteTypeDef = TypedDict(
    "RouteTypeDef",
    {
        "DestinationType": NotRequired[DestinationTypeType],
        "TargetType": NotRequired[TargetTypeType],
        "Destination": NotRequired[str],
        "Target": NotRequired[str],
    },
)

SecurityGroupRemediationActionTypeDef = TypedDict(
    "SecurityGroupRemediationActionTypeDef",
    {
        "RemediationActionType": NotRequired[RemediationActionTypeType],
        "Description": NotRequired[str],
        "RemediationResult": NotRequired["SecurityGroupRuleDescriptionTypeDef"],
        "IsDefaultAction": NotRequired[bool],
    },
)

SecurityGroupRuleDescriptionTypeDef = TypedDict(
    "SecurityGroupRuleDescriptionTypeDef",
    {
        "IPV4Range": NotRequired[str],
        "IPV6Range": NotRequired[str],
        "PrefixListId": NotRequired[str],
        "Protocol": NotRequired[str],
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
    },
)

SecurityServicePolicyDataTypeDef = TypedDict(
    "SecurityServicePolicyDataTypeDef",
    {
        "Type": SecurityServiceTypeType,
        "ManagedServiceData": NotRequired[str],
        "PolicyOption": NotRequired["PolicyOptionTypeDef"],
    },
)

StatefulRuleGroupTypeDef = TypedDict(
    "StatefulRuleGroupTypeDef",
    {
        "RuleGroupName": NotRequired[str],
        "ResourceId": NotRequired[str],
    },
)

StatelessRuleGroupTypeDef = TypedDict(
    "StatelessRuleGroupTypeDef",
    {
        "RuleGroupName": NotRequired[str],
        "ResourceId": NotRequired[str],
        "Priority": NotRequired[int],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagList": Sequence["TagTypeDef"],
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

ViolationDetailTypeDef = TypedDict(
    "ViolationDetailTypeDef",
    {
        "PolicyId": str,
        "MemberAccount": str,
        "ResourceId": str,
        "ResourceType": str,
        "ResourceViolations": List["ResourceViolationTypeDef"],
        "ResourceTags": NotRequired[List["TagTypeDef"]],
        "ResourceDescription": NotRequired[str],
    },
)
