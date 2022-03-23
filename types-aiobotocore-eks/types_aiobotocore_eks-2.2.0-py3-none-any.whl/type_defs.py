"""
Type annotations for eks service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_eks/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_eks.type_defs import AddonHealthTypeDef

    data: AddonHealthTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AddonIssueCodeType,
    AddonStatusType,
    AMITypesType,
    CapacityTypesType,
    ClusterStatusType,
    ConnectorConfigProviderType,
    ErrorCodeType,
    FargateProfileStatusType,
    IpFamilyType,
    LogTypeType,
    NodegroupIssueCodeType,
    NodegroupStatusType,
    ResolveConflictsType,
    TaintEffectType,
    UpdateParamTypeType,
    UpdateStatusType,
    UpdateTypeType,
    configStatusType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddonHealthTypeDef",
    "AddonInfoTypeDef",
    "AddonIssueTypeDef",
    "AddonTypeDef",
    "AddonVersionInfoTypeDef",
    "AssociateEncryptionConfigRequestRequestTypeDef",
    "AssociateEncryptionConfigResponseTypeDef",
    "AssociateIdentityProviderConfigRequestRequestTypeDef",
    "AssociateIdentityProviderConfigResponseTypeDef",
    "AutoScalingGroupTypeDef",
    "CertificateTypeDef",
    "ClusterTypeDef",
    "CompatibilityTypeDef",
    "ConnectorConfigRequestTypeDef",
    "ConnectorConfigResponseTypeDef",
    "CreateAddonRequestRequestTypeDef",
    "CreateAddonResponseTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateFargateProfileRequestRequestTypeDef",
    "CreateFargateProfileResponseTypeDef",
    "CreateNodegroupRequestRequestTypeDef",
    "CreateNodegroupResponseTypeDef",
    "DeleteAddonRequestRequestTypeDef",
    "DeleteAddonResponseTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteFargateProfileRequestRequestTypeDef",
    "DeleteFargateProfileResponseTypeDef",
    "DeleteNodegroupRequestRequestTypeDef",
    "DeleteNodegroupResponseTypeDef",
    "DeregisterClusterRequestRequestTypeDef",
    "DeregisterClusterResponseTypeDef",
    "DescribeAddonRequestRequestTypeDef",
    "DescribeAddonResponseTypeDef",
    "DescribeAddonVersionsRequestRequestTypeDef",
    "DescribeAddonVersionsResponseTypeDef",
    "DescribeClusterRequestRequestTypeDef",
    "DescribeClusterResponseTypeDef",
    "DescribeFargateProfileRequestRequestTypeDef",
    "DescribeFargateProfileResponseTypeDef",
    "DescribeIdentityProviderConfigRequestRequestTypeDef",
    "DescribeIdentityProviderConfigResponseTypeDef",
    "DescribeNodegroupRequestRequestTypeDef",
    "DescribeNodegroupResponseTypeDef",
    "DescribeUpdateRequestRequestTypeDef",
    "DescribeUpdateResponseTypeDef",
    "DisassociateIdentityProviderConfigRequestRequestTypeDef",
    "DisassociateIdentityProviderConfigResponseTypeDef",
    "EncryptionConfigTypeDef",
    "ErrorDetailTypeDef",
    "FargateProfileSelectorTypeDef",
    "FargateProfileTypeDef",
    "IdentityProviderConfigResponseTypeDef",
    "IdentityProviderConfigTypeDef",
    "IdentityTypeDef",
    "IssueTypeDef",
    "KubernetesNetworkConfigRequestTypeDef",
    "KubernetesNetworkConfigResponseTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "ListAddonsRequestRequestTypeDef",
    "ListAddonsResponseTypeDef",
    "ListClustersRequestRequestTypeDef",
    "ListClustersResponseTypeDef",
    "ListFargateProfilesRequestRequestTypeDef",
    "ListFargateProfilesResponseTypeDef",
    "ListIdentityProviderConfigsRequestRequestTypeDef",
    "ListIdentityProviderConfigsResponseTypeDef",
    "ListNodegroupsRequestRequestTypeDef",
    "ListNodegroupsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUpdatesRequestRequestTypeDef",
    "ListUpdatesResponseTypeDef",
    "LogSetupTypeDef",
    "LoggingTypeDef",
    "NodegroupHealthTypeDef",
    "NodegroupResourcesTypeDef",
    "NodegroupScalingConfigTypeDef",
    "NodegroupTypeDef",
    "NodegroupUpdateConfigTypeDef",
    "OIDCTypeDef",
    "OidcIdentityProviderConfigRequestTypeDef",
    "OidcIdentityProviderConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ProviderTypeDef",
    "RegisterClusterRequestRequestTypeDef",
    "RegisterClusterResponseTypeDef",
    "RemoteAccessConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TaintTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAddonRequestRequestTypeDef",
    "UpdateAddonResponseTypeDef",
    "UpdateClusterConfigRequestRequestTypeDef",
    "UpdateClusterConfigResponseTypeDef",
    "UpdateClusterVersionRequestRequestTypeDef",
    "UpdateClusterVersionResponseTypeDef",
    "UpdateLabelsPayloadTypeDef",
    "UpdateNodegroupConfigRequestRequestTypeDef",
    "UpdateNodegroupConfigResponseTypeDef",
    "UpdateNodegroupVersionRequestRequestTypeDef",
    "UpdateNodegroupVersionResponseTypeDef",
    "UpdateParamTypeDef",
    "UpdateTaintsPayloadTypeDef",
    "UpdateTypeDef",
    "VpcConfigRequestTypeDef",
    "VpcConfigResponseTypeDef",
    "WaiterConfigTypeDef",
)

AddonHealthTypeDef = TypedDict(
    "AddonHealthTypeDef",
    {
        "issues": NotRequired[List["AddonIssueTypeDef"]],
    },
)

AddonInfoTypeDef = TypedDict(
    "AddonInfoTypeDef",
    {
        "addonName": NotRequired[str],
        "type": NotRequired[str],
        "addonVersions": NotRequired[List["AddonVersionInfoTypeDef"]],
    },
)

AddonIssueTypeDef = TypedDict(
    "AddonIssueTypeDef",
    {
        "code": NotRequired[AddonIssueCodeType],
        "message": NotRequired[str],
        "resourceIds": NotRequired[List[str]],
    },
)

AddonTypeDef = TypedDict(
    "AddonTypeDef",
    {
        "addonName": NotRequired[str],
        "clusterName": NotRequired[str],
        "status": NotRequired[AddonStatusType],
        "addonVersion": NotRequired[str],
        "health": NotRequired["AddonHealthTypeDef"],
        "addonArn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "modifiedAt": NotRequired[datetime],
        "serviceAccountRoleArn": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

AddonVersionInfoTypeDef = TypedDict(
    "AddonVersionInfoTypeDef",
    {
        "addonVersion": NotRequired[str],
        "architecture": NotRequired[List[str]],
        "compatibilities": NotRequired[List["CompatibilityTypeDef"]],
    },
)

AssociateEncryptionConfigRequestRequestTypeDef = TypedDict(
    "AssociateEncryptionConfigRequestRequestTypeDef",
    {
        "clusterName": str,
        "encryptionConfig": Sequence["EncryptionConfigTypeDef"],
        "clientRequestToken": NotRequired[str],
    },
)

AssociateEncryptionConfigResponseTypeDef = TypedDict(
    "AssociateEncryptionConfigResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateIdentityProviderConfigRequestRequestTypeDef = TypedDict(
    "AssociateIdentityProviderConfigRequestRequestTypeDef",
    {
        "clusterName": str,
        "oidc": "OidcIdentityProviderConfigRequestTypeDef",
        "tags": NotRequired[Mapping[str, str]],
        "clientRequestToken": NotRequired[str],
    },
)

AssociateIdentityProviderConfigResponseTypeDef = TypedDict(
    "AssociateIdentityProviderConfigResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AutoScalingGroupTypeDef = TypedDict(
    "AutoScalingGroupTypeDef",
    {
        "name": NotRequired[str],
    },
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "data": NotRequired[str],
    },
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "version": NotRequired[str],
        "endpoint": NotRequired[str],
        "roleArn": NotRequired[str],
        "resourcesVpcConfig": NotRequired["VpcConfigResponseTypeDef"],
        "kubernetesNetworkConfig": NotRequired["KubernetesNetworkConfigResponseTypeDef"],
        "logging": NotRequired["LoggingTypeDef"],
        "identity": NotRequired["IdentityTypeDef"],
        "status": NotRequired[ClusterStatusType],
        "certificateAuthority": NotRequired["CertificateTypeDef"],
        "clientRequestToken": NotRequired[str],
        "platformVersion": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "encryptionConfig": NotRequired[List["EncryptionConfigTypeDef"]],
        "connectorConfig": NotRequired["ConnectorConfigResponseTypeDef"],
    },
)

CompatibilityTypeDef = TypedDict(
    "CompatibilityTypeDef",
    {
        "clusterVersion": NotRequired[str],
        "platformVersions": NotRequired[List[str]],
        "defaultVersion": NotRequired[bool],
    },
)

ConnectorConfigRequestTypeDef = TypedDict(
    "ConnectorConfigRequestTypeDef",
    {
        "roleArn": str,
        "provider": ConnectorConfigProviderType,
    },
)

ConnectorConfigResponseTypeDef = TypedDict(
    "ConnectorConfigResponseTypeDef",
    {
        "activationId": NotRequired[str],
        "activationCode": NotRequired[str],
        "activationExpiry": NotRequired[datetime],
        "provider": NotRequired[str],
        "roleArn": NotRequired[str],
    },
)

CreateAddonRequestRequestTypeDef = TypedDict(
    "CreateAddonRequestRequestTypeDef",
    {
        "clusterName": str,
        "addonName": str,
        "addonVersion": NotRequired[str],
        "serviceAccountRoleArn": NotRequired[str],
        "resolveConflicts": NotRequired[ResolveConflictsType],
        "clientRequestToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateAddonResponseTypeDef = TypedDict(
    "CreateAddonResponseTypeDef",
    {
        "addon": "AddonTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateClusterRequestRequestTypeDef = TypedDict(
    "CreateClusterRequestRequestTypeDef",
    {
        "name": str,
        "roleArn": str,
        "resourcesVpcConfig": "VpcConfigRequestTypeDef",
        "version": NotRequired[str],
        "kubernetesNetworkConfig": NotRequired["KubernetesNetworkConfigRequestTypeDef"],
        "logging": NotRequired["LoggingTypeDef"],
        "clientRequestToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "encryptionConfig": NotRequired[Sequence["EncryptionConfigTypeDef"]],
    },
)

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFargateProfileRequestRequestTypeDef = TypedDict(
    "CreateFargateProfileRequestRequestTypeDef",
    {
        "fargateProfileName": str,
        "clusterName": str,
        "podExecutionRoleArn": str,
        "subnets": NotRequired[Sequence[str]],
        "selectors": NotRequired[Sequence["FargateProfileSelectorTypeDef"]],
        "clientRequestToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateFargateProfileResponseTypeDef = TypedDict(
    "CreateFargateProfileResponseTypeDef",
    {
        "fargateProfile": "FargateProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateNodegroupRequestRequestTypeDef = TypedDict(
    "CreateNodegroupRequestRequestTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
        "subnets": Sequence[str],
        "nodeRole": str,
        "scalingConfig": NotRequired["NodegroupScalingConfigTypeDef"],
        "diskSize": NotRequired[int],
        "instanceTypes": NotRequired[Sequence[str]],
        "amiType": NotRequired[AMITypesType],
        "remoteAccess": NotRequired["RemoteAccessConfigTypeDef"],
        "labels": NotRequired[Mapping[str, str]],
        "taints": NotRequired[Sequence["TaintTypeDef"]],
        "tags": NotRequired[Mapping[str, str]],
        "clientRequestToken": NotRequired[str],
        "launchTemplate": NotRequired["LaunchTemplateSpecificationTypeDef"],
        "updateConfig": NotRequired["NodegroupUpdateConfigTypeDef"],
        "capacityType": NotRequired[CapacityTypesType],
        "version": NotRequired[str],
        "releaseVersion": NotRequired[str],
    },
)

CreateNodegroupResponseTypeDef = TypedDict(
    "CreateNodegroupResponseTypeDef",
    {
        "nodegroup": "NodegroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAddonRequestRequestTypeDef = TypedDict(
    "DeleteAddonRequestRequestTypeDef",
    {
        "clusterName": str,
        "addonName": str,
        "preserve": NotRequired[bool],
    },
)

DeleteAddonResponseTypeDef = TypedDict(
    "DeleteAddonResponseTypeDef",
    {
        "addon": "AddonTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterRequestRequestTypeDef = TypedDict(
    "DeleteClusterRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFargateProfileRequestRequestTypeDef = TypedDict(
    "DeleteFargateProfileRequestRequestTypeDef",
    {
        "clusterName": str,
        "fargateProfileName": str,
    },
)

DeleteFargateProfileResponseTypeDef = TypedDict(
    "DeleteFargateProfileResponseTypeDef",
    {
        "fargateProfile": "FargateProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteNodegroupRequestRequestTypeDef = TypedDict(
    "DeleteNodegroupRequestRequestTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
    },
)

DeleteNodegroupResponseTypeDef = TypedDict(
    "DeleteNodegroupResponseTypeDef",
    {
        "nodegroup": "NodegroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterClusterRequestRequestTypeDef = TypedDict(
    "DeregisterClusterRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeregisterClusterResponseTypeDef = TypedDict(
    "DeregisterClusterResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAddonRequestRequestTypeDef = TypedDict(
    "DescribeAddonRequestRequestTypeDef",
    {
        "clusterName": str,
        "addonName": str,
    },
)

DescribeAddonResponseTypeDef = TypedDict(
    "DescribeAddonResponseTypeDef",
    {
        "addon": "AddonTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAddonVersionsRequestRequestTypeDef = TypedDict(
    "DescribeAddonVersionsRequestRequestTypeDef",
    {
        "kubernetesVersion": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "addonName": NotRequired[str],
    },
)

DescribeAddonVersionsResponseTypeDef = TypedDict(
    "DescribeAddonVersionsResponseTypeDef",
    {
        "addons": List["AddonInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClusterRequestRequestTypeDef = TypedDict(
    "DescribeClusterRequestRequestTypeDef",
    {
        "name": str,
    },
)

DescribeClusterResponseTypeDef = TypedDict(
    "DescribeClusterResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFargateProfileRequestRequestTypeDef = TypedDict(
    "DescribeFargateProfileRequestRequestTypeDef",
    {
        "clusterName": str,
        "fargateProfileName": str,
    },
)

DescribeFargateProfileResponseTypeDef = TypedDict(
    "DescribeFargateProfileResponseTypeDef",
    {
        "fargateProfile": "FargateProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIdentityProviderConfigRequestRequestTypeDef = TypedDict(
    "DescribeIdentityProviderConfigRequestRequestTypeDef",
    {
        "clusterName": str,
        "identityProviderConfig": "IdentityProviderConfigTypeDef",
    },
)

DescribeIdentityProviderConfigResponseTypeDef = TypedDict(
    "DescribeIdentityProviderConfigResponseTypeDef",
    {
        "identityProviderConfig": "IdentityProviderConfigResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNodegroupRequestRequestTypeDef = TypedDict(
    "DescribeNodegroupRequestRequestTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
    },
)

DescribeNodegroupResponseTypeDef = TypedDict(
    "DescribeNodegroupResponseTypeDef",
    {
        "nodegroup": "NodegroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUpdateRequestRequestTypeDef = TypedDict(
    "DescribeUpdateRequestRequestTypeDef",
    {
        "name": str,
        "updateId": str,
        "nodegroupName": NotRequired[str],
        "addonName": NotRequired[str],
    },
)

DescribeUpdateResponseTypeDef = TypedDict(
    "DescribeUpdateResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateIdentityProviderConfigRequestRequestTypeDef = TypedDict(
    "DisassociateIdentityProviderConfigRequestRequestTypeDef",
    {
        "clusterName": str,
        "identityProviderConfig": "IdentityProviderConfigTypeDef",
        "clientRequestToken": NotRequired[str],
    },
)

DisassociateIdentityProviderConfigResponseTypeDef = TypedDict(
    "DisassociateIdentityProviderConfigResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef",
    {
        "resources": NotRequired[Sequence[str]],
        "provider": NotRequired["ProviderTypeDef"],
    },
)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "errorCode": NotRequired[ErrorCodeType],
        "errorMessage": NotRequired[str],
        "resourceIds": NotRequired[List[str]],
    },
)

FargateProfileSelectorTypeDef = TypedDict(
    "FargateProfileSelectorTypeDef",
    {
        "namespace": NotRequired[str],
        "labels": NotRequired[Mapping[str, str]],
    },
)

FargateProfileTypeDef = TypedDict(
    "FargateProfileTypeDef",
    {
        "fargateProfileName": NotRequired[str],
        "fargateProfileArn": NotRequired[str],
        "clusterName": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "podExecutionRoleArn": NotRequired[str],
        "subnets": NotRequired[List[str]],
        "selectors": NotRequired[List["FargateProfileSelectorTypeDef"]],
        "status": NotRequired[FargateProfileStatusType],
        "tags": NotRequired[Dict[str, str]],
    },
)

IdentityProviderConfigResponseTypeDef = TypedDict(
    "IdentityProviderConfigResponseTypeDef",
    {
        "oidc": NotRequired["OidcIdentityProviderConfigTypeDef"],
    },
)

IdentityProviderConfigTypeDef = TypedDict(
    "IdentityProviderConfigTypeDef",
    {
        "type": str,
        "name": str,
    },
)

IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "oidc": NotRequired["OIDCTypeDef"],
    },
)

IssueTypeDef = TypedDict(
    "IssueTypeDef",
    {
        "code": NotRequired[NodegroupIssueCodeType],
        "message": NotRequired[str],
        "resourceIds": NotRequired[List[str]],
    },
)

KubernetesNetworkConfigRequestTypeDef = TypedDict(
    "KubernetesNetworkConfigRequestTypeDef",
    {
        "serviceIpv4Cidr": NotRequired[str],
        "ipFamily": NotRequired[IpFamilyType],
    },
)

KubernetesNetworkConfigResponseTypeDef = TypedDict(
    "KubernetesNetworkConfigResponseTypeDef",
    {
        "serviceIpv4Cidr": NotRequired[str],
        "serviceIpv6Cidr": NotRequired[str],
        "ipFamily": NotRequired[IpFamilyType],
    },
)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "name": NotRequired[str],
        "version": NotRequired[str],
        "id": NotRequired[str],
    },
)

ListAddonsRequestRequestTypeDef = TypedDict(
    "ListAddonsRequestRequestTypeDef",
    {
        "clusterName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListAddonsResponseTypeDef = TypedDict(
    "ListAddonsResponseTypeDef",
    {
        "addons": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClustersRequestRequestTypeDef = TypedDict(
    "ListClustersRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "include": NotRequired[Sequence[str]],
    },
)

ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef",
    {
        "clusters": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFargateProfilesRequestRequestTypeDef = TypedDict(
    "ListFargateProfilesRequestRequestTypeDef",
    {
        "clusterName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListFargateProfilesResponseTypeDef = TypedDict(
    "ListFargateProfilesResponseTypeDef",
    {
        "fargateProfileNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIdentityProviderConfigsRequestRequestTypeDef = TypedDict(
    "ListIdentityProviderConfigsRequestRequestTypeDef",
    {
        "clusterName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListIdentityProviderConfigsResponseTypeDef = TypedDict(
    "ListIdentityProviderConfigsResponseTypeDef",
    {
        "identityProviderConfigs": List["IdentityProviderConfigTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNodegroupsRequestRequestTypeDef = TypedDict(
    "ListNodegroupsRequestRequestTypeDef",
    {
        "clusterName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListNodegroupsResponseTypeDef = TypedDict(
    "ListNodegroupsResponseTypeDef",
    {
        "nodegroups": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUpdatesRequestRequestTypeDef = TypedDict(
    "ListUpdatesRequestRequestTypeDef",
    {
        "name": str,
        "nodegroupName": NotRequired[str],
        "addonName": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListUpdatesResponseTypeDef = TypedDict(
    "ListUpdatesResponseTypeDef",
    {
        "updateIds": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogSetupTypeDef = TypedDict(
    "LogSetupTypeDef",
    {
        "types": NotRequired[Sequence[LogTypeType]],
        "enabled": NotRequired[bool],
    },
)

LoggingTypeDef = TypedDict(
    "LoggingTypeDef",
    {
        "clusterLogging": NotRequired[Sequence["LogSetupTypeDef"]],
    },
)

NodegroupHealthTypeDef = TypedDict(
    "NodegroupHealthTypeDef",
    {
        "issues": NotRequired[List["IssueTypeDef"]],
    },
)

NodegroupResourcesTypeDef = TypedDict(
    "NodegroupResourcesTypeDef",
    {
        "autoScalingGroups": NotRequired[List["AutoScalingGroupTypeDef"]],
        "remoteAccessSecurityGroup": NotRequired[str],
    },
)

NodegroupScalingConfigTypeDef = TypedDict(
    "NodegroupScalingConfigTypeDef",
    {
        "minSize": NotRequired[int],
        "maxSize": NotRequired[int],
        "desiredSize": NotRequired[int],
    },
)

NodegroupTypeDef = TypedDict(
    "NodegroupTypeDef",
    {
        "nodegroupName": NotRequired[str],
        "nodegroupArn": NotRequired[str],
        "clusterName": NotRequired[str],
        "version": NotRequired[str],
        "releaseVersion": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "modifiedAt": NotRequired[datetime],
        "status": NotRequired[NodegroupStatusType],
        "capacityType": NotRequired[CapacityTypesType],
        "scalingConfig": NotRequired["NodegroupScalingConfigTypeDef"],
        "instanceTypes": NotRequired[List[str]],
        "subnets": NotRequired[List[str]],
        "remoteAccess": NotRequired["RemoteAccessConfigTypeDef"],
        "amiType": NotRequired[AMITypesType],
        "nodeRole": NotRequired[str],
        "labels": NotRequired[Dict[str, str]],
        "taints": NotRequired[List["TaintTypeDef"]],
        "resources": NotRequired["NodegroupResourcesTypeDef"],
        "diskSize": NotRequired[int],
        "health": NotRequired["NodegroupHealthTypeDef"],
        "updateConfig": NotRequired["NodegroupUpdateConfigTypeDef"],
        "launchTemplate": NotRequired["LaunchTemplateSpecificationTypeDef"],
        "tags": NotRequired[Dict[str, str]],
    },
)

NodegroupUpdateConfigTypeDef = TypedDict(
    "NodegroupUpdateConfigTypeDef",
    {
        "maxUnavailable": NotRequired[int],
        "maxUnavailablePercentage": NotRequired[int],
    },
)

OIDCTypeDef = TypedDict(
    "OIDCTypeDef",
    {
        "issuer": NotRequired[str],
    },
)

OidcIdentityProviderConfigRequestTypeDef = TypedDict(
    "OidcIdentityProviderConfigRequestTypeDef",
    {
        "identityProviderConfigName": str,
        "issuerUrl": str,
        "clientId": str,
        "usernameClaim": NotRequired[str],
        "usernamePrefix": NotRequired[str],
        "groupsClaim": NotRequired[str],
        "groupsPrefix": NotRequired[str],
        "requiredClaims": NotRequired[Mapping[str, str]],
    },
)

OidcIdentityProviderConfigTypeDef = TypedDict(
    "OidcIdentityProviderConfigTypeDef",
    {
        "identityProviderConfigName": NotRequired[str],
        "identityProviderConfigArn": NotRequired[str],
        "clusterName": NotRequired[str],
        "issuerUrl": NotRequired[str],
        "clientId": NotRequired[str],
        "usernameClaim": NotRequired[str],
        "usernamePrefix": NotRequired[str],
        "groupsClaim": NotRequired[str],
        "groupsPrefix": NotRequired[str],
        "requiredClaims": NotRequired[Dict[str, str]],
        "tags": NotRequired[Dict[str, str]],
        "status": NotRequired[configStatusType],
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

ProviderTypeDef = TypedDict(
    "ProviderTypeDef",
    {
        "keyArn": NotRequired[str],
    },
)

RegisterClusterRequestRequestTypeDef = TypedDict(
    "RegisterClusterRequestRequestTypeDef",
    {
        "name": str,
        "connectorConfig": "ConnectorConfigRequestTypeDef",
        "clientRequestToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

RegisterClusterResponseTypeDef = TypedDict(
    "RegisterClusterResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoteAccessConfigTypeDef = TypedDict(
    "RemoteAccessConfigTypeDef",
    {
        "ec2SshKey": NotRequired[str],
        "sourceSecurityGroups": NotRequired[Sequence[str]],
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
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

TaintTypeDef = TypedDict(
    "TaintTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
        "effect": NotRequired[TaintEffectType],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateAddonRequestRequestTypeDef = TypedDict(
    "UpdateAddonRequestRequestTypeDef",
    {
        "clusterName": str,
        "addonName": str,
        "addonVersion": NotRequired[str],
        "serviceAccountRoleArn": NotRequired[str],
        "resolveConflicts": NotRequired[ResolveConflictsType],
        "clientRequestToken": NotRequired[str],
    },
)

UpdateAddonResponseTypeDef = TypedDict(
    "UpdateAddonResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateClusterConfigRequestRequestTypeDef = TypedDict(
    "UpdateClusterConfigRequestRequestTypeDef",
    {
        "name": str,
        "resourcesVpcConfig": NotRequired["VpcConfigRequestTypeDef"],
        "logging": NotRequired["LoggingTypeDef"],
        "clientRequestToken": NotRequired[str],
    },
)

UpdateClusterConfigResponseTypeDef = TypedDict(
    "UpdateClusterConfigResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateClusterVersionRequestRequestTypeDef = TypedDict(
    "UpdateClusterVersionRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
        "clientRequestToken": NotRequired[str],
    },
)

UpdateClusterVersionResponseTypeDef = TypedDict(
    "UpdateClusterVersionResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateLabelsPayloadTypeDef = TypedDict(
    "UpdateLabelsPayloadTypeDef",
    {
        "addOrUpdateLabels": NotRequired[Mapping[str, str]],
        "removeLabels": NotRequired[Sequence[str]],
    },
)

UpdateNodegroupConfigRequestRequestTypeDef = TypedDict(
    "UpdateNodegroupConfigRequestRequestTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
        "labels": NotRequired["UpdateLabelsPayloadTypeDef"],
        "taints": NotRequired["UpdateTaintsPayloadTypeDef"],
        "scalingConfig": NotRequired["NodegroupScalingConfigTypeDef"],
        "updateConfig": NotRequired["NodegroupUpdateConfigTypeDef"],
        "clientRequestToken": NotRequired[str],
    },
)

UpdateNodegroupConfigResponseTypeDef = TypedDict(
    "UpdateNodegroupConfigResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateNodegroupVersionRequestRequestTypeDef = TypedDict(
    "UpdateNodegroupVersionRequestRequestTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
        "version": NotRequired[str],
        "releaseVersion": NotRequired[str],
        "launchTemplate": NotRequired["LaunchTemplateSpecificationTypeDef"],
        "force": NotRequired[bool],
        "clientRequestToken": NotRequired[str],
    },
)

UpdateNodegroupVersionResponseTypeDef = TypedDict(
    "UpdateNodegroupVersionResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateParamTypeDef = TypedDict(
    "UpdateParamTypeDef",
    {
        "type": NotRequired[UpdateParamTypeType],
        "value": NotRequired[str],
    },
)

UpdateTaintsPayloadTypeDef = TypedDict(
    "UpdateTaintsPayloadTypeDef",
    {
        "addOrUpdateTaints": NotRequired[Sequence["TaintTypeDef"]],
        "removeTaints": NotRequired[Sequence["TaintTypeDef"]],
    },
)

UpdateTypeDef = TypedDict(
    "UpdateTypeDef",
    {
        "id": NotRequired[str],
        "status": NotRequired[UpdateStatusType],
        "type": NotRequired[UpdateTypeType],
        "params": NotRequired[List["UpdateParamTypeDef"]],
        "createdAt": NotRequired[datetime],
        "errors": NotRequired[List["ErrorDetailTypeDef"]],
    },
)

VpcConfigRequestTypeDef = TypedDict(
    "VpcConfigRequestTypeDef",
    {
        "subnetIds": NotRequired[Sequence[str]],
        "securityGroupIds": NotRequired[Sequence[str]],
        "endpointPublicAccess": NotRequired[bool],
        "endpointPrivateAccess": NotRequired[bool],
        "publicAccessCidrs": NotRequired[Sequence[str]],
    },
)

VpcConfigResponseTypeDef = TypedDict(
    "VpcConfigResponseTypeDef",
    {
        "subnetIds": NotRequired[List[str]],
        "securityGroupIds": NotRequired[List[str]],
        "clusterSecurityGroupId": NotRequired[str],
        "vpcId": NotRequired[str],
        "endpointPublicAccess": NotRequired[bool],
        "endpointPrivateAccess": NotRequired[bool],
        "publicAccessCidrs": NotRequired[List[str]],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
