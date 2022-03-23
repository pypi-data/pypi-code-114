"""
Type annotations for ds service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_ds/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_ds.type_defs import AcceptSharedDirectoryRequestRequestTypeDef

    data: AcceptSharedDirectoryRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    CertificateStateType,
    CertificateTypeType,
    ClientAuthenticationStatusType,
    DirectoryEditionType,
    DirectorySizeType,
    DirectoryStageType,
    DirectoryTypeType,
    DomainControllerStatusType,
    IpRouteStatusMsgType,
    LDAPSStatusType,
    RadiusAuthenticationProtocolType,
    RadiusStatusType,
    RegionTypeType,
    SchemaExtensionStatusType,
    SelectiveAuthType,
    ShareMethodType,
    ShareStatusType,
    SnapshotStatusType,
    SnapshotTypeType,
    TopicStatusType,
    TrustDirectionType,
    TrustStateType,
    TrustTypeType,
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
    "AcceptSharedDirectoryRequestRequestTypeDef",
    "AcceptSharedDirectoryResultTypeDef",
    "AddIpRoutesRequestRequestTypeDef",
    "AddRegionRequestRequestTypeDef",
    "AddTagsToResourceRequestRequestTypeDef",
    "AttributeTypeDef",
    "CancelSchemaExtensionRequestRequestTypeDef",
    "CertificateInfoTypeDef",
    "CertificateTypeDef",
    "ClientAuthenticationSettingInfoTypeDef",
    "ClientCertAuthSettingsTypeDef",
    "ComputerTypeDef",
    "ConditionalForwarderTypeDef",
    "ConnectDirectoryRequestRequestTypeDef",
    "ConnectDirectoryResultTypeDef",
    "CreateAliasRequestRequestTypeDef",
    "CreateAliasResultTypeDef",
    "CreateComputerRequestRequestTypeDef",
    "CreateComputerResultTypeDef",
    "CreateConditionalForwarderRequestRequestTypeDef",
    "CreateDirectoryRequestRequestTypeDef",
    "CreateDirectoryResultTypeDef",
    "CreateLogSubscriptionRequestRequestTypeDef",
    "CreateMicrosoftADRequestRequestTypeDef",
    "CreateMicrosoftADResultTypeDef",
    "CreateSnapshotRequestRequestTypeDef",
    "CreateSnapshotResultTypeDef",
    "CreateTrustRequestRequestTypeDef",
    "CreateTrustResultTypeDef",
    "DeleteConditionalForwarderRequestRequestTypeDef",
    "DeleteDirectoryRequestRequestTypeDef",
    "DeleteDirectoryResultTypeDef",
    "DeleteLogSubscriptionRequestRequestTypeDef",
    "DeleteSnapshotRequestRequestTypeDef",
    "DeleteSnapshotResultTypeDef",
    "DeleteTrustRequestRequestTypeDef",
    "DeleteTrustResultTypeDef",
    "DeregisterCertificateRequestRequestTypeDef",
    "DeregisterEventTopicRequestRequestTypeDef",
    "DescribeCertificateRequestRequestTypeDef",
    "DescribeCertificateResultTypeDef",
    "DescribeClientAuthenticationSettingsRequestRequestTypeDef",
    "DescribeClientAuthenticationSettingsResultTypeDef",
    "DescribeConditionalForwardersRequestRequestTypeDef",
    "DescribeConditionalForwardersResultTypeDef",
    "DescribeDirectoriesRequestRequestTypeDef",
    "DescribeDirectoriesResultTypeDef",
    "DescribeDomainControllersRequestRequestTypeDef",
    "DescribeDomainControllersResultTypeDef",
    "DescribeEventTopicsRequestRequestTypeDef",
    "DescribeEventTopicsResultTypeDef",
    "DescribeLDAPSSettingsRequestRequestTypeDef",
    "DescribeLDAPSSettingsResultTypeDef",
    "DescribeRegionsRequestRequestTypeDef",
    "DescribeRegionsResultTypeDef",
    "DescribeSharedDirectoriesRequestRequestTypeDef",
    "DescribeSharedDirectoriesResultTypeDef",
    "DescribeSnapshotsRequestRequestTypeDef",
    "DescribeSnapshotsResultTypeDef",
    "DescribeTrustsRequestRequestTypeDef",
    "DescribeTrustsResultTypeDef",
    "DirectoryConnectSettingsDescriptionTypeDef",
    "DirectoryConnectSettingsTypeDef",
    "DirectoryDescriptionTypeDef",
    "DirectoryLimitsTypeDef",
    "DirectoryVpcSettingsDescriptionTypeDef",
    "DirectoryVpcSettingsTypeDef",
    "DisableClientAuthenticationRequestRequestTypeDef",
    "DisableLDAPSRequestRequestTypeDef",
    "DisableRadiusRequestRequestTypeDef",
    "DisableSsoRequestRequestTypeDef",
    "DomainControllerTypeDef",
    "EnableClientAuthenticationRequestRequestTypeDef",
    "EnableLDAPSRequestRequestTypeDef",
    "EnableRadiusRequestRequestTypeDef",
    "EnableSsoRequestRequestTypeDef",
    "EventTopicTypeDef",
    "GetDirectoryLimitsResultTypeDef",
    "GetSnapshotLimitsRequestRequestTypeDef",
    "GetSnapshotLimitsResultTypeDef",
    "IpRouteInfoTypeDef",
    "IpRouteTypeDef",
    "LDAPSSettingInfoTypeDef",
    "ListCertificatesRequestRequestTypeDef",
    "ListCertificatesResultTypeDef",
    "ListIpRoutesRequestRequestTypeDef",
    "ListIpRoutesResultTypeDef",
    "ListLogSubscriptionsRequestRequestTypeDef",
    "ListLogSubscriptionsResultTypeDef",
    "ListSchemaExtensionsRequestRequestTypeDef",
    "ListSchemaExtensionsResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "LogSubscriptionTypeDef",
    "OwnerDirectoryDescriptionTypeDef",
    "PaginatorConfigTypeDef",
    "RadiusSettingsTypeDef",
    "RegionDescriptionTypeDef",
    "RegionsInfoTypeDef",
    "RegisterCertificateRequestRequestTypeDef",
    "RegisterCertificateResultTypeDef",
    "RegisterEventTopicRequestRequestTypeDef",
    "RejectSharedDirectoryRequestRequestTypeDef",
    "RejectSharedDirectoryResultTypeDef",
    "RemoveIpRoutesRequestRequestTypeDef",
    "RemoveRegionRequestRequestTypeDef",
    "RemoveTagsFromResourceRequestRequestTypeDef",
    "ResetUserPasswordRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreFromSnapshotRequestRequestTypeDef",
    "SchemaExtensionInfoTypeDef",
    "ShareDirectoryRequestRequestTypeDef",
    "ShareDirectoryResultTypeDef",
    "ShareTargetTypeDef",
    "SharedDirectoryTypeDef",
    "SnapshotLimitsTypeDef",
    "SnapshotTypeDef",
    "StartSchemaExtensionRequestRequestTypeDef",
    "StartSchemaExtensionResultTypeDef",
    "TagTypeDef",
    "TrustTypeDef",
    "UnshareDirectoryRequestRequestTypeDef",
    "UnshareDirectoryResultTypeDef",
    "UnshareTargetTypeDef",
    "UpdateConditionalForwarderRequestRequestTypeDef",
    "UpdateNumberOfDomainControllersRequestRequestTypeDef",
    "UpdateRadiusRequestRequestTypeDef",
    "UpdateTrustRequestRequestTypeDef",
    "UpdateTrustResultTypeDef",
    "VerifyTrustRequestRequestTypeDef",
    "VerifyTrustResultTypeDef",
)

AcceptSharedDirectoryRequestRequestTypeDef = TypedDict(
    "AcceptSharedDirectoryRequestRequestTypeDef",
    {
        "SharedDirectoryId": str,
    },
)

AcceptSharedDirectoryResultTypeDef = TypedDict(
    "AcceptSharedDirectoryResultTypeDef",
    {
        "SharedDirectory": "SharedDirectoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddIpRoutesRequestRequestTypeDef = TypedDict(
    "AddIpRoutesRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "IpRoutes": Sequence["IpRouteTypeDef"],
        "UpdateSecurityGroupForDirectoryControllers": NotRequired[bool],
    },
)

AddRegionRequestRequestTypeDef = TypedDict(
    "AddRegionRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RegionName": str,
        "VPCSettings": "DirectoryVpcSettingsTypeDef",
    },
)

AddTagsToResourceRequestRequestTypeDef = TypedDict(
    "AddTagsToResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)

CancelSchemaExtensionRequestRequestTypeDef = TypedDict(
    "CancelSchemaExtensionRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "SchemaExtensionId": str,
    },
)

CertificateInfoTypeDef = TypedDict(
    "CertificateInfoTypeDef",
    {
        "CertificateId": NotRequired[str],
        "CommonName": NotRequired[str],
        "State": NotRequired[CertificateStateType],
        "ExpiryDateTime": NotRequired[datetime],
        "Type": NotRequired[CertificateTypeType],
    },
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateId": NotRequired[str],
        "State": NotRequired[CertificateStateType],
        "StateReason": NotRequired[str],
        "CommonName": NotRequired[str],
        "RegisteredDateTime": NotRequired[datetime],
        "ExpiryDateTime": NotRequired[datetime],
        "Type": NotRequired[CertificateTypeType],
        "ClientCertAuthSettings": NotRequired["ClientCertAuthSettingsTypeDef"],
    },
)

ClientAuthenticationSettingInfoTypeDef = TypedDict(
    "ClientAuthenticationSettingInfoTypeDef",
    {
        "Type": NotRequired[Literal["SmartCard"]],
        "Status": NotRequired[ClientAuthenticationStatusType],
        "LastUpdatedDateTime": NotRequired[datetime],
    },
)

ClientCertAuthSettingsTypeDef = TypedDict(
    "ClientCertAuthSettingsTypeDef",
    {
        "OCSPUrl": NotRequired[str],
    },
)

ComputerTypeDef = TypedDict(
    "ComputerTypeDef",
    {
        "ComputerId": NotRequired[str],
        "ComputerName": NotRequired[str],
        "ComputerAttributes": NotRequired[List["AttributeTypeDef"]],
    },
)

ConditionalForwarderTypeDef = TypedDict(
    "ConditionalForwarderTypeDef",
    {
        "RemoteDomainName": NotRequired[str],
        "DnsIpAddrs": NotRequired[List[str]],
        "ReplicationScope": NotRequired[Literal["Domain"]],
    },
)

ConnectDirectoryRequestRequestTypeDef = TypedDict(
    "ConnectDirectoryRequestRequestTypeDef",
    {
        "Name": str,
        "Password": str,
        "Size": DirectorySizeType,
        "ConnectSettings": "DirectoryConnectSettingsTypeDef",
        "ShortName": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

ConnectDirectoryResultTypeDef = TypedDict(
    "ConnectDirectoryResultTypeDef",
    {
        "DirectoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAliasRequestRequestTypeDef = TypedDict(
    "CreateAliasRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Alias": str,
    },
)

CreateAliasResultTypeDef = TypedDict(
    "CreateAliasResultTypeDef",
    {
        "DirectoryId": str,
        "Alias": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateComputerRequestRequestTypeDef = TypedDict(
    "CreateComputerRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "ComputerName": str,
        "Password": str,
        "OrganizationalUnitDistinguishedName": NotRequired[str],
        "ComputerAttributes": NotRequired[Sequence["AttributeTypeDef"]],
    },
)

CreateComputerResultTypeDef = TypedDict(
    "CreateComputerResultTypeDef",
    {
        "Computer": "ComputerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConditionalForwarderRequestRequestTypeDef = TypedDict(
    "CreateConditionalForwarderRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RemoteDomainName": str,
        "DnsIpAddrs": Sequence[str],
    },
)

CreateDirectoryRequestRequestTypeDef = TypedDict(
    "CreateDirectoryRequestRequestTypeDef",
    {
        "Name": str,
        "Password": str,
        "Size": DirectorySizeType,
        "ShortName": NotRequired[str],
        "Description": NotRequired[str],
        "VpcSettings": NotRequired["DirectoryVpcSettingsTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDirectoryResultTypeDef = TypedDict(
    "CreateDirectoryResultTypeDef",
    {
        "DirectoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLogSubscriptionRequestRequestTypeDef = TypedDict(
    "CreateLogSubscriptionRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "LogGroupName": str,
    },
)

CreateMicrosoftADRequestRequestTypeDef = TypedDict(
    "CreateMicrosoftADRequestRequestTypeDef",
    {
        "Name": str,
        "Password": str,
        "VpcSettings": "DirectoryVpcSettingsTypeDef",
        "ShortName": NotRequired[str],
        "Description": NotRequired[str],
        "Edition": NotRequired[DirectoryEditionType],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateMicrosoftADResultTypeDef = TypedDict(
    "CreateMicrosoftADResultTypeDef",
    {
        "DirectoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSnapshotRequestRequestTypeDef = TypedDict(
    "CreateSnapshotRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Name": NotRequired[str],
    },
)

CreateSnapshotResultTypeDef = TypedDict(
    "CreateSnapshotResultTypeDef",
    {
        "SnapshotId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTrustRequestRequestTypeDef = TypedDict(
    "CreateTrustRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RemoteDomainName": str,
        "TrustPassword": str,
        "TrustDirection": TrustDirectionType,
        "TrustType": NotRequired[TrustTypeType],
        "ConditionalForwarderIpAddrs": NotRequired[Sequence[str]],
        "SelectiveAuth": NotRequired[SelectiveAuthType],
    },
)

CreateTrustResultTypeDef = TypedDict(
    "CreateTrustResultTypeDef",
    {
        "TrustId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConditionalForwarderRequestRequestTypeDef = TypedDict(
    "DeleteConditionalForwarderRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RemoteDomainName": str,
    },
)

DeleteDirectoryRequestRequestTypeDef = TypedDict(
    "DeleteDirectoryRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)

DeleteDirectoryResultTypeDef = TypedDict(
    "DeleteDirectoryResultTypeDef",
    {
        "DirectoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLogSubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteLogSubscriptionRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)

DeleteSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteSnapshotRequestRequestTypeDef",
    {
        "SnapshotId": str,
    },
)

DeleteSnapshotResultTypeDef = TypedDict(
    "DeleteSnapshotResultTypeDef",
    {
        "SnapshotId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTrustRequestRequestTypeDef = TypedDict(
    "DeleteTrustRequestRequestTypeDef",
    {
        "TrustId": str,
        "DeleteAssociatedConditionalForwarder": NotRequired[bool],
    },
)

DeleteTrustResultTypeDef = TypedDict(
    "DeleteTrustResultTypeDef",
    {
        "TrustId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterCertificateRequestRequestTypeDef = TypedDict(
    "DeregisterCertificateRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "CertificateId": str,
    },
)

DeregisterEventTopicRequestRequestTypeDef = TypedDict(
    "DeregisterEventTopicRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "TopicName": str,
    },
)

DescribeCertificateRequestRequestTypeDef = TypedDict(
    "DescribeCertificateRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "CertificateId": str,
    },
)

DescribeCertificateResultTypeDef = TypedDict(
    "DescribeCertificateResultTypeDef",
    {
        "Certificate": "CertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClientAuthenticationSettingsRequestRequestTypeDef = TypedDict(
    "DescribeClientAuthenticationSettingsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": NotRequired[Literal["SmartCard"]],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

DescribeClientAuthenticationSettingsResultTypeDef = TypedDict(
    "DescribeClientAuthenticationSettingsResultTypeDef",
    {
        "ClientAuthenticationSettingsInfo": List["ClientAuthenticationSettingInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConditionalForwardersRequestRequestTypeDef = TypedDict(
    "DescribeConditionalForwardersRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RemoteDomainNames": NotRequired[Sequence[str]],
    },
)

DescribeConditionalForwardersResultTypeDef = TypedDict(
    "DescribeConditionalForwardersResultTypeDef",
    {
        "ConditionalForwarders": List["ConditionalForwarderTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDirectoriesRequestRequestTypeDef = TypedDict(
    "DescribeDirectoriesRequestRequestTypeDef",
    {
        "DirectoryIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

DescribeDirectoriesResultTypeDef = TypedDict(
    "DescribeDirectoriesResultTypeDef",
    {
        "DirectoryDescriptions": List["DirectoryDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainControllersRequestRequestTypeDef = TypedDict(
    "DescribeDomainControllersRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "DomainControllerIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

DescribeDomainControllersResultTypeDef = TypedDict(
    "DescribeDomainControllersResultTypeDef",
    {
        "DomainControllers": List["DomainControllerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventTopicsRequestRequestTypeDef = TypedDict(
    "DescribeEventTopicsRequestRequestTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "TopicNames": NotRequired[Sequence[str]],
    },
)

DescribeEventTopicsResultTypeDef = TypedDict(
    "DescribeEventTopicsResultTypeDef",
    {
        "EventTopics": List["EventTopicTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLDAPSSettingsRequestRequestTypeDef = TypedDict(
    "DescribeLDAPSSettingsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": NotRequired[Literal["Client"]],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

DescribeLDAPSSettingsResultTypeDef = TypedDict(
    "DescribeLDAPSSettingsResultTypeDef",
    {
        "LDAPSSettingsInfo": List["LDAPSSettingInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRegionsRequestRequestTypeDef = TypedDict(
    "DescribeRegionsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RegionName": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

DescribeRegionsResultTypeDef = TypedDict(
    "DescribeRegionsResultTypeDef",
    {
        "RegionsDescription": List["RegionDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSharedDirectoriesRequestRequestTypeDef = TypedDict(
    "DescribeSharedDirectoriesRequestRequestTypeDef",
    {
        "OwnerDirectoryId": str,
        "SharedDirectoryIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

DescribeSharedDirectoriesResultTypeDef = TypedDict(
    "DescribeSharedDirectoriesResultTypeDef",
    {
        "SharedDirectories": List["SharedDirectoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSnapshotsRequestRequestTypeDef = TypedDict(
    "DescribeSnapshotsRequestRequestTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "SnapshotIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

DescribeSnapshotsResultTypeDef = TypedDict(
    "DescribeSnapshotsResultTypeDef",
    {
        "Snapshots": List["SnapshotTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrustsRequestRequestTypeDef = TypedDict(
    "DescribeTrustsRequestRequestTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "TrustIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

DescribeTrustsResultTypeDef = TypedDict(
    "DescribeTrustsResultTypeDef",
    {
        "Trusts": List["TrustTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DirectoryConnectSettingsDescriptionTypeDef = TypedDict(
    "DirectoryConnectSettingsDescriptionTypeDef",
    {
        "VpcId": NotRequired[str],
        "SubnetIds": NotRequired[List[str]],
        "CustomerUserName": NotRequired[str],
        "SecurityGroupId": NotRequired[str],
        "AvailabilityZones": NotRequired[List[str]],
        "ConnectIps": NotRequired[List[str]],
    },
)

DirectoryConnectSettingsTypeDef = TypedDict(
    "DirectoryConnectSettingsTypeDef",
    {
        "VpcId": str,
        "SubnetIds": Sequence[str],
        "CustomerDnsIps": Sequence[str],
        "CustomerUserName": str,
    },
)

DirectoryDescriptionTypeDef = TypedDict(
    "DirectoryDescriptionTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "Name": NotRequired[str],
        "ShortName": NotRequired[str],
        "Size": NotRequired[DirectorySizeType],
        "Edition": NotRequired[DirectoryEditionType],
        "Alias": NotRequired[str],
        "AccessUrl": NotRequired[str],
        "Description": NotRequired[str],
        "DnsIpAddrs": NotRequired[List[str]],
        "Stage": NotRequired[DirectoryStageType],
        "ShareStatus": NotRequired[ShareStatusType],
        "ShareMethod": NotRequired[ShareMethodType],
        "ShareNotes": NotRequired[str],
        "LaunchTime": NotRequired[datetime],
        "StageLastUpdatedDateTime": NotRequired[datetime],
        "Type": NotRequired[DirectoryTypeType],
        "VpcSettings": NotRequired["DirectoryVpcSettingsDescriptionTypeDef"],
        "ConnectSettings": NotRequired["DirectoryConnectSettingsDescriptionTypeDef"],
        "RadiusSettings": NotRequired["RadiusSettingsTypeDef"],
        "RadiusStatus": NotRequired[RadiusStatusType],
        "StageReason": NotRequired[str],
        "SsoEnabled": NotRequired[bool],
        "DesiredNumberOfDomainControllers": NotRequired[int],
        "OwnerDirectoryDescription": NotRequired["OwnerDirectoryDescriptionTypeDef"],
        "RegionsInfo": NotRequired["RegionsInfoTypeDef"],
    },
)

DirectoryLimitsTypeDef = TypedDict(
    "DirectoryLimitsTypeDef",
    {
        "CloudOnlyDirectoriesLimit": NotRequired[int],
        "CloudOnlyDirectoriesCurrentCount": NotRequired[int],
        "CloudOnlyDirectoriesLimitReached": NotRequired[bool],
        "CloudOnlyMicrosoftADLimit": NotRequired[int],
        "CloudOnlyMicrosoftADCurrentCount": NotRequired[int],
        "CloudOnlyMicrosoftADLimitReached": NotRequired[bool],
        "ConnectedDirectoriesLimit": NotRequired[int],
        "ConnectedDirectoriesCurrentCount": NotRequired[int],
        "ConnectedDirectoriesLimitReached": NotRequired[bool],
    },
)

DirectoryVpcSettingsDescriptionTypeDef = TypedDict(
    "DirectoryVpcSettingsDescriptionTypeDef",
    {
        "VpcId": NotRequired[str],
        "SubnetIds": NotRequired[List[str]],
        "SecurityGroupId": NotRequired[str],
        "AvailabilityZones": NotRequired[List[str]],
    },
)

DirectoryVpcSettingsTypeDef = TypedDict(
    "DirectoryVpcSettingsTypeDef",
    {
        "VpcId": str,
        "SubnetIds": Sequence[str],
    },
)

DisableClientAuthenticationRequestRequestTypeDef = TypedDict(
    "DisableClientAuthenticationRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": Literal["SmartCard"],
    },
)

DisableLDAPSRequestRequestTypeDef = TypedDict(
    "DisableLDAPSRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": Literal["Client"],
    },
)

DisableRadiusRequestRequestTypeDef = TypedDict(
    "DisableRadiusRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)

DisableSsoRequestRequestTypeDef = TypedDict(
    "DisableSsoRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "UserName": NotRequired[str],
        "Password": NotRequired[str],
    },
)

DomainControllerTypeDef = TypedDict(
    "DomainControllerTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "DomainControllerId": NotRequired[str],
        "DnsIpAddr": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "Status": NotRequired[DomainControllerStatusType],
        "StatusReason": NotRequired[str],
        "LaunchTime": NotRequired[datetime],
        "StatusLastUpdatedDateTime": NotRequired[datetime],
    },
)

EnableClientAuthenticationRequestRequestTypeDef = TypedDict(
    "EnableClientAuthenticationRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": Literal["SmartCard"],
    },
)

EnableLDAPSRequestRequestTypeDef = TypedDict(
    "EnableLDAPSRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": Literal["Client"],
    },
)

EnableRadiusRequestRequestTypeDef = TypedDict(
    "EnableRadiusRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RadiusSettings": "RadiusSettingsTypeDef",
    },
)

EnableSsoRequestRequestTypeDef = TypedDict(
    "EnableSsoRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "UserName": NotRequired[str],
        "Password": NotRequired[str],
    },
)

EventTopicTypeDef = TypedDict(
    "EventTopicTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "TopicName": NotRequired[str],
        "TopicArn": NotRequired[str],
        "CreatedDateTime": NotRequired[datetime],
        "Status": NotRequired[TopicStatusType],
    },
)

GetDirectoryLimitsResultTypeDef = TypedDict(
    "GetDirectoryLimitsResultTypeDef",
    {
        "DirectoryLimits": "DirectoryLimitsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSnapshotLimitsRequestRequestTypeDef = TypedDict(
    "GetSnapshotLimitsRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)

GetSnapshotLimitsResultTypeDef = TypedDict(
    "GetSnapshotLimitsResultTypeDef",
    {
        "SnapshotLimits": "SnapshotLimitsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IpRouteInfoTypeDef = TypedDict(
    "IpRouteInfoTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "CidrIp": NotRequired[str],
        "IpRouteStatusMsg": NotRequired[IpRouteStatusMsgType],
        "AddedDateTime": NotRequired[datetime],
        "IpRouteStatusReason": NotRequired[str],
        "Description": NotRequired[str],
    },
)

IpRouteTypeDef = TypedDict(
    "IpRouteTypeDef",
    {
        "CidrIp": NotRequired[str],
        "Description": NotRequired[str],
    },
)

LDAPSSettingInfoTypeDef = TypedDict(
    "LDAPSSettingInfoTypeDef",
    {
        "LDAPSStatus": NotRequired[LDAPSStatusType],
        "LDAPSStatusReason": NotRequired[str],
        "LastUpdatedDateTime": NotRequired[datetime],
    },
)

ListCertificatesRequestRequestTypeDef = TypedDict(
    "ListCertificatesRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListCertificatesResultTypeDef = TypedDict(
    "ListCertificatesResultTypeDef",
    {
        "NextToken": str,
        "CertificatesInfo": List["CertificateInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIpRoutesRequestRequestTypeDef = TypedDict(
    "ListIpRoutesRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListIpRoutesResultTypeDef = TypedDict(
    "ListIpRoutesResultTypeDef",
    {
        "IpRoutesInfo": List["IpRouteInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLogSubscriptionsRequestRequestTypeDef = TypedDict(
    "ListLogSubscriptionsRequestRequestTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListLogSubscriptionsResultTypeDef = TypedDict(
    "ListLogSubscriptionsResultTypeDef",
    {
        "LogSubscriptions": List["LogSubscriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSchemaExtensionsRequestRequestTypeDef = TypedDict(
    "ListSchemaExtensionsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListSchemaExtensionsResultTypeDef = TypedDict(
    "ListSchemaExtensionsResultTypeDef",
    {
        "SchemaExtensionsInfo": List["SchemaExtensionInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogSubscriptionTypeDef = TypedDict(
    "LogSubscriptionTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "LogGroupName": NotRequired[str],
        "SubscriptionCreatedDateTime": NotRequired[datetime],
    },
)

OwnerDirectoryDescriptionTypeDef = TypedDict(
    "OwnerDirectoryDescriptionTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "AccountId": NotRequired[str],
        "DnsIpAddrs": NotRequired[List[str]],
        "VpcSettings": NotRequired["DirectoryVpcSettingsDescriptionTypeDef"],
        "RadiusSettings": NotRequired["RadiusSettingsTypeDef"],
        "RadiusStatus": NotRequired[RadiusStatusType],
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

RadiusSettingsTypeDef = TypedDict(
    "RadiusSettingsTypeDef",
    {
        "RadiusServers": NotRequired[List[str]],
        "RadiusPort": NotRequired[int],
        "RadiusTimeout": NotRequired[int],
        "RadiusRetries": NotRequired[int],
        "SharedSecret": NotRequired[str],
        "AuthenticationProtocol": NotRequired[RadiusAuthenticationProtocolType],
        "DisplayLabel": NotRequired[str],
        "UseSameUsername": NotRequired[bool],
    },
)

RegionDescriptionTypeDef = TypedDict(
    "RegionDescriptionTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "RegionName": NotRequired[str],
        "RegionType": NotRequired[RegionTypeType],
        "Status": NotRequired[DirectoryStageType],
        "VpcSettings": NotRequired["DirectoryVpcSettingsTypeDef"],
        "DesiredNumberOfDomainControllers": NotRequired[int],
        "LaunchTime": NotRequired[datetime],
        "StatusLastUpdatedDateTime": NotRequired[datetime],
        "LastUpdatedDateTime": NotRequired[datetime],
    },
)

RegionsInfoTypeDef = TypedDict(
    "RegionsInfoTypeDef",
    {
        "PrimaryRegion": NotRequired[str],
        "AdditionalRegions": NotRequired[List[str]],
    },
)

RegisterCertificateRequestRequestTypeDef = TypedDict(
    "RegisterCertificateRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "CertificateData": str,
        "Type": NotRequired[CertificateTypeType],
        "ClientCertAuthSettings": NotRequired["ClientCertAuthSettingsTypeDef"],
    },
)

RegisterCertificateResultTypeDef = TypedDict(
    "RegisterCertificateResultTypeDef",
    {
        "CertificateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterEventTopicRequestRequestTypeDef = TypedDict(
    "RegisterEventTopicRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "TopicName": str,
    },
)

RejectSharedDirectoryRequestRequestTypeDef = TypedDict(
    "RejectSharedDirectoryRequestRequestTypeDef",
    {
        "SharedDirectoryId": str,
    },
)

RejectSharedDirectoryResultTypeDef = TypedDict(
    "RejectSharedDirectoryResultTypeDef",
    {
        "SharedDirectoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveIpRoutesRequestRequestTypeDef = TypedDict(
    "RemoveIpRoutesRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "CidrIps": Sequence[str],
    },
)

RemoveRegionRequestRequestTypeDef = TypedDict(
    "RemoveRegionRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)

RemoveTagsFromResourceRequestRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagKeys": Sequence[str],
    },
)

ResetUserPasswordRequestRequestTypeDef = TypedDict(
    "ResetUserPasswordRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "UserName": str,
        "NewPassword": str,
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

RestoreFromSnapshotRequestRequestTypeDef = TypedDict(
    "RestoreFromSnapshotRequestRequestTypeDef",
    {
        "SnapshotId": str,
    },
)

SchemaExtensionInfoTypeDef = TypedDict(
    "SchemaExtensionInfoTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "SchemaExtensionId": NotRequired[str],
        "Description": NotRequired[str],
        "SchemaExtensionStatus": NotRequired[SchemaExtensionStatusType],
        "SchemaExtensionStatusReason": NotRequired[str],
        "StartDateTime": NotRequired[datetime],
        "EndDateTime": NotRequired[datetime],
    },
)

ShareDirectoryRequestRequestTypeDef = TypedDict(
    "ShareDirectoryRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "ShareTarget": "ShareTargetTypeDef",
        "ShareMethod": ShareMethodType,
        "ShareNotes": NotRequired[str],
    },
)

ShareDirectoryResultTypeDef = TypedDict(
    "ShareDirectoryResultTypeDef",
    {
        "SharedDirectoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ShareTargetTypeDef = TypedDict(
    "ShareTargetTypeDef",
    {
        "Id": str,
        "Type": Literal["ACCOUNT"],
    },
)

SharedDirectoryTypeDef = TypedDict(
    "SharedDirectoryTypeDef",
    {
        "OwnerAccountId": NotRequired[str],
        "OwnerDirectoryId": NotRequired[str],
        "ShareMethod": NotRequired[ShareMethodType],
        "SharedAccountId": NotRequired[str],
        "SharedDirectoryId": NotRequired[str],
        "ShareStatus": NotRequired[ShareStatusType],
        "ShareNotes": NotRequired[str],
        "CreatedDateTime": NotRequired[datetime],
        "LastUpdatedDateTime": NotRequired[datetime],
    },
)

SnapshotLimitsTypeDef = TypedDict(
    "SnapshotLimitsTypeDef",
    {
        "ManualSnapshotsLimit": NotRequired[int],
        "ManualSnapshotsCurrentCount": NotRequired[int],
        "ManualSnapshotsLimitReached": NotRequired[bool],
    },
)

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "Type": NotRequired[SnapshotTypeType],
        "Name": NotRequired[str],
        "Status": NotRequired[SnapshotStatusType],
        "StartTime": NotRequired[datetime],
    },
)

StartSchemaExtensionRequestRequestTypeDef = TypedDict(
    "StartSchemaExtensionRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "CreateSnapshotBeforeSchemaExtension": bool,
        "LdifContent": str,
        "Description": str,
    },
)

StartSchemaExtensionResultTypeDef = TypedDict(
    "StartSchemaExtensionResultTypeDef",
    {
        "SchemaExtensionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TrustTypeDef = TypedDict(
    "TrustTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "TrustId": NotRequired[str],
        "RemoteDomainName": NotRequired[str],
        "TrustType": NotRequired[TrustTypeType],
        "TrustDirection": NotRequired[TrustDirectionType],
        "TrustState": NotRequired[TrustStateType],
        "CreatedDateTime": NotRequired[datetime],
        "LastUpdatedDateTime": NotRequired[datetime],
        "StateLastUpdatedDateTime": NotRequired[datetime],
        "TrustStateReason": NotRequired[str],
        "SelectiveAuth": NotRequired[SelectiveAuthType],
    },
)

UnshareDirectoryRequestRequestTypeDef = TypedDict(
    "UnshareDirectoryRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "UnshareTarget": "UnshareTargetTypeDef",
    },
)

UnshareDirectoryResultTypeDef = TypedDict(
    "UnshareDirectoryResultTypeDef",
    {
        "SharedDirectoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UnshareTargetTypeDef = TypedDict(
    "UnshareTargetTypeDef",
    {
        "Id": str,
        "Type": Literal["ACCOUNT"],
    },
)

UpdateConditionalForwarderRequestRequestTypeDef = TypedDict(
    "UpdateConditionalForwarderRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RemoteDomainName": str,
        "DnsIpAddrs": Sequence[str],
    },
)

UpdateNumberOfDomainControllersRequestRequestTypeDef = TypedDict(
    "UpdateNumberOfDomainControllersRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "DesiredNumber": int,
    },
)

UpdateRadiusRequestRequestTypeDef = TypedDict(
    "UpdateRadiusRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "RadiusSettings": "RadiusSettingsTypeDef",
    },
)

UpdateTrustRequestRequestTypeDef = TypedDict(
    "UpdateTrustRequestRequestTypeDef",
    {
        "TrustId": str,
        "SelectiveAuth": NotRequired[SelectiveAuthType],
    },
)

UpdateTrustResultTypeDef = TypedDict(
    "UpdateTrustResultTypeDef",
    {
        "RequestId": str,
        "TrustId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VerifyTrustRequestRequestTypeDef = TypedDict(
    "VerifyTrustRequestRequestTypeDef",
    {
        "TrustId": str,
    },
)

VerifyTrustResultTypeDef = TypedDict(
    "VerifyTrustResultTypeDef",
    {
        "TrustId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
