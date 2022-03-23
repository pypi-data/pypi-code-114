"""
Type annotations for opensearch service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_opensearch.type_defs import AWSDomainInformationTypeDef

    data: AWSDomainInformationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AutoTuneDesiredStateType,
    AutoTuneStateType,
    DeploymentStatusType,
    DescribePackagesFilterNameType,
    DomainPackageStatusType,
    EngineTypeType,
    InboundConnectionStatusCodeType,
    LogTypeType,
    OpenSearchPartitionInstanceTypeType,
    OpenSearchWarmPartitionInstanceTypeType,
    OptionStateType,
    OutboundConnectionStatusCodeType,
    OverallChangeStatusType,
    PackageStatusType,
    ReservedInstancePaymentOptionType,
    RollbackOnDisableType,
    ScheduledAutoTuneActionTypeType,
    ScheduledAutoTuneSeverityTypeType,
    TLSSecurityPolicyType,
    UpgradeStatusType,
    UpgradeStepType,
    VolumeTypeType,
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
    "AWSDomainInformationTypeDef",
    "AcceptInboundConnectionRequestRequestTypeDef",
    "AcceptInboundConnectionResponseTypeDef",
    "AccessPoliciesStatusTypeDef",
    "AddTagsRequestRequestTypeDef",
    "AdditionalLimitTypeDef",
    "AdvancedOptionsStatusTypeDef",
    "AdvancedSecurityOptionsInputTypeDef",
    "AdvancedSecurityOptionsStatusTypeDef",
    "AdvancedSecurityOptionsTypeDef",
    "AssociatePackageRequestRequestTypeDef",
    "AssociatePackageResponseTypeDef",
    "AutoTuneDetailsTypeDef",
    "AutoTuneMaintenanceScheduleTypeDef",
    "AutoTuneOptionsInputTypeDef",
    "AutoTuneOptionsOutputTypeDef",
    "AutoTuneOptionsStatusTypeDef",
    "AutoTuneOptionsTypeDef",
    "AutoTuneStatusTypeDef",
    "AutoTuneTypeDef",
    "CancelServiceSoftwareUpdateRequestRequestTypeDef",
    "CancelServiceSoftwareUpdateResponseTypeDef",
    "ChangeProgressDetailsTypeDef",
    "ChangeProgressStageTypeDef",
    "ChangeProgressStatusDetailsTypeDef",
    "ClusterConfigStatusTypeDef",
    "ClusterConfigTypeDef",
    "CognitoOptionsStatusTypeDef",
    "CognitoOptionsTypeDef",
    "ColdStorageOptionsTypeDef",
    "CompatibleVersionsMapTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "CreateDomainResponseTypeDef",
    "CreateOutboundConnectionRequestRequestTypeDef",
    "CreateOutboundConnectionResponseTypeDef",
    "CreatePackageRequestRequestTypeDef",
    "CreatePackageResponseTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteDomainResponseTypeDef",
    "DeleteInboundConnectionRequestRequestTypeDef",
    "DeleteInboundConnectionResponseTypeDef",
    "DeleteOutboundConnectionRequestRequestTypeDef",
    "DeleteOutboundConnectionResponseTypeDef",
    "DeletePackageRequestRequestTypeDef",
    "DeletePackageResponseTypeDef",
    "DescribeDomainAutoTunesRequestRequestTypeDef",
    "DescribeDomainAutoTunesResponseTypeDef",
    "DescribeDomainChangeProgressRequestRequestTypeDef",
    "DescribeDomainChangeProgressResponseTypeDef",
    "DescribeDomainConfigRequestRequestTypeDef",
    "DescribeDomainConfigResponseTypeDef",
    "DescribeDomainRequestRequestTypeDef",
    "DescribeDomainResponseTypeDef",
    "DescribeDomainsRequestRequestTypeDef",
    "DescribeDomainsResponseTypeDef",
    "DescribeInboundConnectionsRequestRequestTypeDef",
    "DescribeInboundConnectionsResponseTypeDef",
    "DescribeInstanceTypeLimitsRequestRequestTypeDef",
    "DescribeInstanceTypeLimitsResponseTypeDef",
    "DescribeOutboundConnectionsRequestRequestTypeDef",
    "DescribeOutboundConnectionsResponseTypeDef",
    "DescribePackagesFilterTypeDef",
    "DescribePackagesRequestRequestTypeDef",
    "DescribePackagesResponseTypeDef",
    "DescribeReservedInstanceOfferingsRequestRequestTypeDef",
    "DescribeReservedInstanceOfferingsResponseTypeDef",
    "DescribeReservedInstancesRequestRequestTypeDef",
    "DescribeReservedInstancesResponseTypeDef",
    "DissociatePackageRequestRequestTypeDef",
    "DissociatePackageResponseTypeDef",
    "DomainConfigTypeDef",
    "DomainEndpointOptionsStatusTypeDef",
    "DomainEndpointOptionsTypeDef",
    "DomainInfoTypeDef",
    "DomainInformationContainerTypeDef",
    "DomainPackageDetailsTypeDef",
    "DomainStatusTypeDef",
    "DryRunResultsTypeDef",
    "DurationTypeDef",
    "EBSOptionsStatusTypeDef",
    "EBSOptionsTypeDef",
    "EncryptionAtRestOptionsStatusTypeDef",
    "EncryptionAtRestOptionsTypeDef",
    "ErrorDetailsTypeDef",
    "FilterTypeDef",
    "GetCompatibleVersionsRequestRequestTypeDef",
    "GetCompatibleVersionsResponseTypeDef",
    "GetPackageVersionHistoryRequestRequestTypeDef",
    "GetPackageVersionHistoryResponseTypeDef",
    "GetUpgradeHistoryRequestRequestTypeDef",
    "GetUpgradeHistoryResponseTypeDef",
    "GetUpgradeStatusRequestRequestTypeDef",
    "GetUpgradeStatusResponseTypeDef",
    "InboundConnectionStatusTypeDef",
    "InboundConnectionTypeDef",
    "InstanceCountLimitsTypeDef",
    "InstanceLimitsTypeDef",
    "InstanceTypeDetailsTypeDef",
    "LimitsTypeDef",
    "ListDomainNamesRequestRequestTypeDef",
    "ListDomainNamesResponseTypeDef",
    "ListDomainsForPackageRequestRequestTypeDef",
    "ListDomainsForPackageResponseTypeDef",
    "ListInstanceTypeDetailsRequestRequestTypeDef",
    "ListInstanceTypeDetailsResponseTypeDef",
    "ListPackagesForDomainRequestRequestTypeDef",
    "ListPackagesForDomainResponseTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "ListVersionsRequestRequestTypeDef",
    "ListVersionsResponseTypeDef",
    "LogPublishingOptionTypeDef",
    "LogPublishingOptionsStatusTypeDef",
    "MasterUserOptionsTypeDef",
    "NodeToNodeEncryptionOptionsStatusTypeDef",
    "NodeToNodeEncryptionOptionsTypeDef",
    "OptionStatusTypeDef",
    "OutboundConnectionStatusTypeDef",
    "OutboundConnectionTypeDef",
    "PackageDetailsTypeDef",
    "PackageSourceTypeDef",
    "PackageVersionHistoryTypeDef",
    "PurchaseReservedInstanceOfferingRequestRequestTypeDef",
    "PurchaseReservedInstanceOfferingResponseTypeDef",
    "RecurringChargeTypeDef",
    "RejectInboundConnectionRequestRequestTypeDef",
    "RejectInboundConnectionResponseTypeDef",
    "RemoveTagsRequestRequestTypeDef",
    "ReservedInstanceOfferingTypeDef",
    "ReservedInstanceTypeDef",
    "ResponseMetadataTypeDef",
    "SAMLIdpTypeDef",
    "SAMLOptionsInputTypeDef",
    "SAMLOptionsOutputTypeDef",
    "ScheduledAutoTuneDetailsTypeDef",
    "ServiceSoftwareOptionsTypeDef",
    "SnapshotOptionsStatusTypeDef",
    "SnapshotOptionsTypeDef",
    "StartServiceSoftwareUpdateRequestRequestTypeDef",
    "StartServiceSoftwareUpdateResponseTypeDef",
    "StorageTypeLimitTypeDef",
    "StorageTypeTypeDef",
    "TagTypeDef",
    "UpdateDomainConfigRequestRequestTypeDef",
    "UpdateDomainConfigResponseTypeDef",
    "UpdatePackageRequestRequestTypeDef",
    "UpdatePackageResponseTypeDef",
    "UpgradeDomainRequestRequestTypeDef",
    "UpgradeDomainResponseTypeDef",
    "UpgradeHistoryTypeDef",
    "UpgradeStepItemTypeDef",
    "VPCDerivedInfoStatusTypeDef",
    "VPCDerivedInfoTypeDef",
    "VPCOptionsTypeDef",
    "VersionStatusTypeDef",
    "ZoneAwarenessConfigTypeDef",
)

AWSDomainInformationTypeDef = TypedDict(
    "AWSDomainInformationTypeDef",
    {
        "DomainName": str,
        "OwnerId": NotRequired[str],
        "Region": NotRequired[str],
    },
)

AcceptInboundConnectionRequestRequestTypeDef = TypedDict(
    "AcceptInboundConnectionRequestRequestTypeDef",
    {
        "ConnectionId": str,
    },
)

AcceptInboundConnectionResponseTypeDef = TypedDict(
    "AcceptInboundConnectionResponseTypeDef",
    {
        "Connection": "InboundConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccessPoliciesStatusTypeDef = TypedDict(
    "AccessPoliciesStatusTypeDef",
    {
        "Options": str,
        "Status": "OptionStatusTypeDef",
    },
)

AddTagsRequestRequestTypeDef = TypedDict(
    "AddTagsRequestRequestTypeDef",
    {
        "ARN": str,
        "TagList": Sequence["TagTypeDef"],
    },
)

AdditionalLimitTypeDef = TypedDict(
    "AdditionalLimitTypeDef",
    {
        "LimitName": NotRequired[str],
        "LimitValues": NotRequired[List[str]],
    },
)

AdvancedOptionsStatusTypeDef = TypedDict(
    "AdvancedOptionsStatusTypeDef",
    {
        "Options": Dict[str, str],
        "Status": "OptionStatusTypeDef",
    },
)

AdvancedSecurityOptionsInputTypeDef = TypedDict(
    "AdvancedSecurityOptionsInputTypeDef",
    {
        "Enabled": NotRequired[bool],
        "InternalUserDatabaseEnabled": NotRequired[bool],
        "MasterUserOptions": NotRequired["MasterUserOptionsTypeDef"],
        "SAMLOptions": NotRequired["SAMLOptionsInputTypeDef"],
        "AnonymousAuthEnabled": NotRequired[bool],
    },
)

AdvancedSecurityOptionsStatusTypeDef = TypedDict(
    "AdvancedSecurityOptionsStatusTypeDef",
    {
        "Options": "AdvancedSecurityOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

AdvancedSecurityOptionsTypeDef = TypedDict(
    "AdvancedSecurityOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "InternalUserDatabaseEnabled": NotRequired[bool],
        "SAMLOptions": NotRequired["SAMLOptionsOutputTypeDef"],
        "AnonymousAuthDisableDate": NotRequired[datetime],
        "AnonymousAuthEnabled": NotRequired[bool],
    },
)

AssociatePackageRequestRequestTypeDef = TypedDict(
    "AssociatePackageRequestRequestTypeDef",
    {
        "PackageID": str,
        "DomainName": str,
    },
)

AssociatePackageResponseTypeDef = TypedDict(
    "AssociatePackageResponseTypeDef",
    {
        "DomainPackageDetails": "DomainPackageDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AutoTuneDetailsTypeDef = TypedDict(
    "AutoTuneDetailsTypeDef",
    {
        "ScheduledAutoTuneDetails": NotRequired["ScheduledAutoTuneDetailsTypeDef"],
    },
)

AutoTuneMaintenanceScheduleTypeDef = TypedDict(
    "AutoTuneMaintenanceScheduleTypeDef",
    {
        "StartAt": NotRequired[Union[datetime, str]],
        "Duration": NotRequired["DurationTypeDef"],
        "CronExpressionForRecurrence": NotRequired[str],
    },
)

AutoTuneOptionsInputTypeDef = TypedDict(
    "AutoTuneOptionsInputTypeDef",
    {
        "DesiredState": NotRequired[AutoTuneDesiredStateType],
        "MaintenanceSchedules": NotRequired[Sequence["AutoTuneMaintenanceScheduleTypeDef"]],
    },
)

AutoTuneOptionsOutputTypeDef = TypedDict(
    "AutoTuneOptionsOutputTypeDef",
    {
        "State": NotRequired[AutoTuneStateType],
        "ErrorMessage": NotRequired[str],
    },
)

AutoTuneOptionsStatusTypeDef = TypedDict(
    "AutoTuneOptionsStatusTypeDef",
    {
        "Options": NotRequired["AutoTuneOptionsTypeDef"],
        "Status": NotRequired["AutoTuneStatusTypeDef"],
    },
)

AutoTuneOptionsTypeDef = TypedDict(
    "AutoTuneOptionsTypeDef",
    {
        "DesiredState": NotRequired[AutoTuneDesiredStateType],
        "RollbackOnDisable": NotRequired[RollbackOnDisableType],
        "MaintenanceSchedules": NotRequired[List["AutoTuneMaintenanceScheduleTypeDef"]],
    },
)

AutoTuneStatusTypeDef = TypedDict(
    "AutoTuneStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "State": AutoTuneStateType,
        "UpdateVersion": NotRequired[int],
        "ErrorMessage": NotRequired[str],
        "PendingDeletion": NotRequired[bool],
    },
)

AutoTuneTypeDef = TypedDict(
    "AutoTuneTypeDef",
    {
        "AutoTuneType": NotRequired[Literal["SCHEDULED_ACTION"]],
        "AutoTuneDetails": NotRequired["AutoTuneDetailsTypeDef"],
    },
)

CancelServiceSoftwareUpdateRequestRequestTypeDef = TypedDict(
    "CancelServiceSoftwareUpdateRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

CancelServiceSoftwareUpdateResponseTypeDef = TypedDict(
    "CancelServiceSoftwareUpdateResponseTypeDef",
    {
        "ServiceSoftwareOptions": "ServiceSoftwareOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChangeProgressDetailsTypeDef = TypedDict(
    "ChangeProgressDetailsTypeDef",
    {
        "ChangeId": NotRequired[str],
        "Message": NotRequired[str],
    },
)

ChangeProgressStageTypeDef = TypedDict(
    "ChangeProgressStageTypeDef",
    {
        "Name": NotRequired[str],
        "Status": NotRequired[str],
        "Description": NotRequired[str],
        "LastUpdated": NotRequired[datetime],
    },
)

ChangeProgressStatusDetailsTypeDef = TypedDict(
    "ChangeProgressStatusDetailsTypeDef",
    {
        "ChangeId": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "Status": NotRequired[OverallChangeStatusType],
        "PendingProperties": NotRequired[List[str]],
        "CompletedProperties": NotRequired[List[str]],
        "TotalNumberOfStages": NotRequired[int],
        "ChangeProgressStages": NotRequired[List["ChangeProgressStageTypeDef"]],
    },
)

ClusterConfigStatusTypeDef = TypedDict(
    "ClusterConfigStatusTypeDef",
    {
        "Options": "ClusterConfigTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

ClusterConfigTypeDef = TypedDict(
    "ClusterConfigTypeDef",
    {
        "InstanceType": NotRequired[OpenSearchPartitionInstanceTypeType],
        "InstanceCount": NotRequired[int],
        "DedicatedMasterEnabled": NotRequired[bool],
        "ZoneAwarenessEnabled": NotRequired[bool],
        "ZoneAwarenessConfig": NotRequired["ZoneAwarenessConfigTypeDef"],
        "DedicatedMasterType": NotRequired[OpenSearchPartitionInstanceTypeType],
        "DedicatedMasterCount": NotRequired[int],
        "WarmEnabled": NotRequired[bool],
        "WarmType": NotRequired[OpenSearchWarmPartitionInstanceTypeType],
        "WarmCount": NotRequired[int],
        "ColdStorageOptions": NotRequired["ColdStorageOptionsTypeDef"],
    },
)

CognitoOptionsStatusTypeDef = TypedDict(
    "CognitoOptionsStatusTypeDef",
    {
        "Options": "CognitoOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

CognitoOptionsTypeDef = TypedDict(
    "CognitoOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "UserPoolId": NotRequired[str],
        "IdentityPoolId": NotRequired[str],
        "RoleArn": NotRequired[str],
    },
)

ColdStorageOptionsTypeDef = TypedDict(
    "ColdStorageOptionsTypeDef",
    {
        "Enabled": bool,
    },
)

CompatibleVersionsMapTypeDef = TypedDict(
    "CompatibleVersionsMapTypeDef",
    {
        "SourceVersion": NotRequired[str],
        "TargetVersions": NotRequired[List[str]],
    },
)

CreateDomainRequestRequestTypeDef = TypedDict(
    "CreateDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "EngineVersion": NotRequired[str],
        "ClusterConfig": NotRequired["ClusterConfigTypeDef"],
        "EBSOptions": NotRequired["EBSOptionsTypeDef"],
        "AccessPolicies": NotRequired[str],
        "SnapshotOptions": NotRequired["SnapshotOptionsTypeDef"],
        "VPCOptions": NotRequired["VPCOptionsTypeDef"],
        "CognitoOptions": NotRequired["CognitoOptionsTypeDef"],
        "EncryptionAtRestOptions": NotRequired["EncryptionAtRestOptionsTypeDef"],
        "NodeToNodeEncryptionOptions": NotRequired["NodeToNodeEncryptionOptionsTypeDef"],
        "AdvancedOptions": NotRequired[Mapping[str, str]],
        "LogPublishingOptions": NotRequired[Mapping[LogTypeType, "LogPublishingOptionTypeDef"]],
        "DomainEndpointOptions": NotRequired["DomainEndpointOptionsTypeDef"],
        "AdvancedSecurityOptions": NotRequired["AdvancedSecurityOptionsInputTypeDef"],
        "TagList": NotRequired[Sequence["TagTypeDef"]],
        "AutoTuneOptions": NotRequired["AutoTuneOptionsInputTypeDef"],
    },
)

CreateDomainResponseTypeDef = TypedDict(
    "CreateDomainResponseTypeDef",
    {
        "DomainStatus": "DomainStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateOutboundConnectionRequestRequestTypeDef = TypedDict(
    "CreateOutboundConnectionRequestRequestTypeDef",
    {
        "LocalDomainInfo": "DomainInformationContainerTypeDef",
        "RemoteDomainInfo": "DomainInformationContainerTypeDef",
        "ConnectionAlias": str,
    },
)

CreateOutboundConnectionResponseTypeDef = TypedDict(
    "CreateOutboundConnectionResponseTypeDef",
    {
        "LocalDomainInfo": "DomainInformationContainerTypeDef",
        "RemoteDomainInfo": "DomainInformationContainerTypeDef",
        "ConnectionAlias": str,
        "ConnectionStatus": "OutboundConnectionStatusTypeDef",
        "ConnectionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePackageRequestRequestTypeDef = TypedDict(
    "CreatePackageRequestRequestTypeDef",
    {
        "PackageName": str,
        "PackageType": Literal["TXT-DICTIONARY"],
        "PackageSource": "PackageSourceTypeDef",
        "PackageDescription": NotRequired[str],
    },
)

CreatePackageResponseTypeDef = TypedDict(
    "CreatePackageResponseTypeDef",
    {
        "PackageDetails": "PackageDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DeleteDomainResponseTypeDef = TypedDict(
    "DeleteDomainResponseTypeDef",
    {
        "DomainStatus": "DomainStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInboundConnectionRequestRequestTypeDef = TypedDict(
    "DeleteInboundConnectionRequestRequestTypeDef",
    {
        "ConnectionId": str,
    },
)

DeleteInboundConnectionResponseTypeDef = TypedDict(
    "DeleteInboundConnectionResponseTypeDef",
    {
        "Connection": "InboundConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteOutboundConnectionRequestRequestTypeDef = TypedDict(
    "DeleteOutboundConnectionRequestRequestTypeDef",
    {
        "ConnectionId": str,
    },
)

DeleteOutboundConnectionResponseTypeDef = TypedDict(
    "DeleteOutboundConnectionResponseTypeDef",
    {
        "Connection": "OutboundConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePackageRequestRequestTypeDef = TypedDict(
    "DeletePackageRequestRequestTypeDef",
    {
        "PackageID": str,
    },
)

DeletePackageResponseTypeDef = TypedDict(
    "DeletePackageResponseTypeDef",
    {
        "PackageDetails": "PackageDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainAutoTunesRequestRequestTypeDef = TypedDict(
    "DescribeDomainAutoTunesRequestRequestTypeDef",
    {
        "DomainName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeDomainAutoTunesResponseTypeDef = TypedDict(
    "DescribeDomainAutoTunesResponseTypeDef",
    {
        "AutoTunes": List["AutoTuneTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainChangeProgressRequestRequestTypeDef = TypedDict(
    "DescribeDomainChangeProgressRequestRequestTypeDef",
    {
        "DomainName": str,
        "ChangeId": NotRequired[str],
    },
)

DescribeDomainChangeProgressResponseTypeDef = TypedDict(
    "DescribeDomainChangeProgressResponseTypeDef",
    {
        "ChangeProgressStatus": "ChangeProgressStatusDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainConfigRequestRequestTypeDef = TypedDict(
    "DescribeDomainConfigRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DescribeDomainConfigResponseTypeDef = TypedDict(
    "DescribeDomainConfigResponseTypeDef",
    {
        "DomainConfig": "DomainConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainRequestRequestTypeDef = TypedDict(
    "DescribeDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DescribeDomainResponseTypeDef = TypedDict(
    "DescribeDomainResponseTypeDef",
    {
        "DomainStatus": "DomainStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainsRequestRequestTypeDef = TypedDict(
    "DescribeDomainsRequestRequestTypeDef",
    {
        "DomainNames": Sequence[str],
    },
)

DescribeDomainsResponseTypeDef = TypedDict(
    "DescribeDomainsResponseTypeDef",
    {
        "DomainStatusList": List["DomainStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInboundConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeInboundConnectionsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeInboundConnectionsResponseTypeDef = TypedDict(
    "DescribeInboundConnectionsResponseTypeDef",
    {
        "Connections": List["InboundConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceTypeLimitsRequestRequestTypeDef = TypedDict(
    "DescribeInstanceTypeLimitsRequestRequestTypeDef",
    {
        "InstanceType": OpenSearchPartitionInstanceTypeType,
        "EngineVersion": str,
        "DomainName": NotRequired[str],
    },
)

DescribeInstanceTypeLimitsResponseTypeDef = TypedDict(
    "DescribeInstanceTypeLimitsResponseTypeDef",
    {
        "LimitsByRole": Dict[str, "LimitsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOutboundConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeOutboundConnectionsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeOutboundConnectionsResponseTypeDef = TypedDict(
    "DescribeOutboundConnectionsResponseTypeDef",
    {
        "Connections": List["OutboundConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePackagesFilterTypeDef = TypedDict(
    "DescribePackagesFilterTypeDef",
    {
        "Name": NotRequired[DescribePackagesFilterNameType],
        "Value": NotRequired[Sequence[str]],
    },
)

DescribePackagesRequestRequestTypeDef = TypedDict(
    "DescribePackagesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["DescribePackagesFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribePackagesResponseTypeDef = TypedDict(
    "DescribePackagesResponseTypeDef",
    {
        "PackageDetailsList": List["PackageDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedInstanceOfferingsRequestRequestTypeDef = TypedDict(
    "DescribeReservedInstanceOfferingsRequestRequestTypeDef",
    {
        "ReservedInstanceOfferingId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeReservedInstanceOfferingsResponseTypeDef = TypedDict(
    "DescribeReservedInstanceOfferingsResponseTypeDef",
    {
        "NextToken": str,
        "ReservedInstanceOfferings": List["ReservedInstanceOfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedInstancesRequestRequestTypeDef = TypedDict(
    "DescribeReservedInstancesRequestRequestTypeDef",
    {
        "ReservedInstanceId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeReservedInstancesResponseTypeDef = TypedDict(
    "DescribeReservedInstancesResponseTypeDef",
    {
        "NextToken": str,
        "ReservedInstances": List["ReservedInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DissociatePackageRequestRequestTypeDef = TypedDict(
    "DissociatePackageRequestRequestTypeDef",
    {
        "PackageID": str,
        "DomainName": str,
    },
)

DissociatePackageResponseTypeDef = TypedDict(
    "DissociatePackageResponseTypeDef",
    {
        "DomainPackageDetails": "DomainPackageDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainConfigTypeDef = TypedDict(
    "DomainConfigTypeDef",
    {
        "EngineVersion": NotRequired["VersionStatusTypeDef"],
        "ClusterConfig": NotRequired["ClusterConfigStatusTypeDef"],
        "EBSOptions": NotRequired["EBSOptionsStatusTypeDef"],
        "AccessPolicies": NotRequired["AccessPoliciesStatusTypeDef"],
        "SnapshotOptions": NotRequired["SnapshotOptionsStatusTypeDef"],
        "VPCOptions": NotRequired["VPCDerivedInfoStatusTypeDef"],
        "CognitoOptions": NotRequired["CognitoOptionsStatusTypeDef"],
        "EncryptionAtRestOptions": NotRequired["EncryptionAtRestOptionsStatusTypeDef"],
        "NodeToNodeEncryptionOptions": NotRequired["NodeToNodeEncryptionOptionsStatusTypeDef"],
        "AdvancedOptions": NotRequired["AdvancedOptionsStatusTypeDef"],
        "LogPublishingOptions": NotRequired["LogPublishingOptionsStatusTypeDef"],
        "DomainEndpointOptions": NotRequired["DomainEndpointOptionsStatusTypeDef"],
        "AdvancedSecurityOptions": NotRequired["AdvancedSecurityOptionsStatusTypeDef"],
        "AutoTuneOptions": NotRequired["AutoTuneOptionsStatusTypeDef"],
        "ChangeProgressDetails": NotRequired["ChangeProgressDetailsTypeDef"],
    },
)

DomainEndpointOptionsStatusTypeDef = TypedDict(
    "DomainEndpointOptionsStatusTypeDef",
    {
        "Options": "DomainEndpointOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

DomainEndpointOptionsTypeDef = TypedDict(
    "DomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": NotRequired[bool],
        "TLSSecurityPolicy": NotRequired[TLSSecurityPolicyType],
        "CustomEndpointEnabled": NotRequired[bool],
        "CustomEndpoint": NotRequired[str],
        "CustomEndpointCertificateArn": NotRequired[str],
    },
)

DomainInfoTypeDef = TypedDict(
    "DomainInfoTypeDef",
    {
        "DomainName": NotRequired[str],
        "EngineType": NotRequired[EngineTypeType],
    },
)

DomainInformationContainerTypeDef = TypedDict(
    "DomainInformationContainerTypeDef",
    {
        "AWSDomainInformation": NotRequired["AWSDomainInformationTypeDef"],
    },
)

DomainPackageDetailsTypeDef = TypedDict(
    "DomainPackageDetailsTypeDef",
    {
        "PackageID": NotRequired[str],
        "PackageName": NotRequired[str],
        "PackageType": NotRequired[Literal["TXT-DICTIONARY"]],
        "LastUpdated": NotRequired[datetime],
        "DomainName": NotRequired[str],
        "DomainPackageStatus": NotRequired[DomainPackageStatusType],
        "PackageVersion": NotRequired[str],
        "ReferencePath": NotRequired[str],
        "ErrorDetails": NotRequired["ErrorDetailsTypeDef"],
    },
)

DomainStatusTypeDef = TypedDict(
    "DomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "ClusterConfig": "ClusterConfigTypeDef",
        "Created": NotRequired[bool],
        "Deleted": NotRequired[bool],
        "Endpoint": NotRequired[str],
        "Endpoints": NotRequired[Dict[str, str]],
        "Processing": NotRequired[bool],
        "UpgradeProcessing": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "EBSOptions": NotRequired["EBSOptionsTypeDef"],
        "AccessPolicies": NotRequired[str],
        "SnapshotOptions": NotRequired["SnapshotOptionsTypeDef"],
        "VPCOptions": NotRequired["VPCDerivedInfoTypeDef"],
        "CognitoOptions": NotRequired["CognitoOptionsTypeDef"],
        "EncryptionAtRestOptions": NotRequired["EncryptionAtRestOptionsTypeDef"],
        "NodeToNodeEncryptionOptions": NotRequired["NodeToNodeEncryptionOptionsTypeDef"],
        "AdvancedOptions": NotRequired[Dict[str, str]],
        "LogPublishingOptions": NotRequired[Dict[LogTypeType, "LogPublishingOptionTypeDef"]],
        "ServiceSoftwareOptions": NotRequired["ServiceSoftwareOptionsTypeDef"],
        "DomainEndpointOptions": NotRequired["DomainEndpointOptionsTypeDef"],
        "AdvancedSecurityOptions": NotRequired["AdvancedSecurityOptionsTypeDef"],
        "AutoTuneOptions": NotRequired["AutoTuneOptionsOutputTypeDef"],
        "ChangeProgressDetails": NotRequired["ChangeProgressDetailsTypeDef"],
    },
)

DryRunResultsTypeDef = TypedDict(
    "DryRunResultsTypeDef",
    {
        "DeploymentType": NotRequired[str],
        "Message": NotRequired[str],
    },
)

DurationTypeDef = TypedDict(
    "DurationTypeDef",
    {
        "Value": NotRequired[int],
        "Unit": NotRequired[Literal["HOURS"]],
    },
)

EBSOptionsStatusTypeDef = TypedDict(
    "EBSOptionsStatusTypeDef",
    {
        "Options": "EBSOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

EBSOptionsTypeDef = TypedDict(
    "EBSOptionsTypeDef",
    {
        "EBSEnabled": NotRequired[bool],
        "VolumeType": NotRequired[VolumeTypeType],
        "VolumeSize": NotRequired[int],
        "Iops": NotRequired[int],
    },
)

EncryptionAtRestOptionsStatusTypeDef = TypedDict(
    "EncryptionAtRestOptionsStatusTypeDef",
    {
        "Options": "EncryptionAtRestOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

EncryptionAtRestOptionsTypeDef = TypedDict(
    "EncryptionAtRestOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
    },
)

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "ErrorType": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)

GetCompatibleVersionsRequestRequestTypeDef = TypedDict(
    "GetCompatibleVersionsRequestRequestTypeDef",
    {
        "DomainName": NotRequired[str],
    },
)

GetCompatibleVersionsResponseTypeDef = TypedDict(
    "GetCompatibleVersionsResponseTypeDef",
    {
        "CompatibleVersions": List["CompatibleVersionsMapTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPackageVersionHistoryRequestRequestTypeDef = TypedDict(
    "GetPackageVersionHistoryRequestRequestTypeDef",
    {
        "PackageID": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetPackageVersionHistoryResponseTypeDef = TypedDict(
    "GetPackageVersionHistoryResponseTypeDef",
    {
        "PackageID": str,
        "PackageVersionHistoryList": List["PackageVersionHistoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUpgradeHistoryRequestRequestTypeDef = TypedDict(
    "GetUpgradeHistoryRequestRequestTypeDef",
    {
        "DomainName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetUpgradeHistoryResponseTypeDef = TypedDict(
    "GetUpgradeHistoryResponseTypeDef",
    {
        "UpgradeHistories": List["UpgradeHistoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUpgradeStatusRequestRequestTypeDef = TypedDict(
    "GetUpgradeStatusRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

GetUpgradeStatusResponseTypeDef = TypedDict(
    "GetUpgradeStatusResponseTypeDef",
    {
        "UpgradeStep": UpgradeStepType,
        "StepStatus": UpgradeStatusType,
        "UpgradeName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InboundConnectionStatusTypeDef = TypedDict(
    "InboundConnectionStatusTypeDef",
    {
        "StatusCode": NotRequired[InboundConnectionStatusCodeType],
        "Message": NotRequired[str],
    },
)

InboundConnectionTypeDef = TypedDict(
    "InboundConnectionTypeDef",
    {
        "LocalDomainInfo": NotRequired["DomainInformationContainerTypeDef"],
        "RemoteDomainInfo": NotRequired["DomainInformationContainerTypeDef"],
        "ConnectionId": NotRequired[str],
        "ConnectionStatus": NotRequired["InboundConnectionStatusTypeDef"],
    },
)

InstanceCountLimitsTypeDef = TypedDict(
    "InstanceCountLimitsTypeDef",
    {
        "MinimumInstanceCount": NotRequired[int],
        "MaximumInstanceCount": NotRequired[int],
    },
)

InstanceLimitsTypeDef = TypedDict(
    "InstanceLimitsTypeDef",
    {
        "InstanceCountLimits": NotRequired["InstanceCountLimitsTypeDef"],
    },
)

InstanceTypeDetailsTypeDef = TypedDict(
    "InstanceTypeDetailsTypeDef",
    {
        "InstanceType": NotRequired[OpenSearchPartitionInstanceTypeType],
        "EncryptionEnabled": NotRequired[bool],
        "CognitoEnabled": NotRequired[bool],
        "AppLogsEnabled": NotRequired[bool],
        "AdvancedSecurityEnabled": NotRequired[bool],
        "WarmEnabled": NotRequired[bool],
        "InstanceRole": NotRequired[List[str]],
    },
)

LimitsTypeDef = TypedDict(
    "LimitsTypeDef",
    {
        "StorageTypes": NotRequired[List["StorageTypeTypeDef"]],
        "InstanceLimits": NotRequired["InstanceLimitsTypeDef"],
        "AdditionalLimits": NotRequired[List["AdditionalLimitTypeDef"]],
    },
)

ListDomainNamesRequestRequestTypeDef = TypedDict(
    "ListDomainNamesRequestRequestTypeDef",
    {
        "EngineType": NotRequired[EngineTypeType],
    },
)

ListDomainNamesResponseTypeDef = TypedDict(
    "ListDomainNamesResponseTypeDef",
    {
        "DomainNames": List["DomainInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDomainsForPackageRequestRequestTypeDef = TypedDict(
    "ListDomainsForPackageRequestRequestTypeDef",
    {
        "PackageID": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListDomainsForPackageResponseTypeDef = TypedDict(
    "ListDomainsForPackageResponseTypeDef",
    {
        "DomainPackageDetailsList": List["DomainPackageDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstanceTypeDetailsRequestRequestTypeDef = TypedDict(
    "ListInstanceTypeDetailsRequestRequestTypeDef",
    {
        "EngineVersion": str,
        "DomainName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListInstanceTypeDetailsResponseTypeDef = TypedDict(
    "ListInstanceTypeDetailsResponseTypeDef",
    {
        "InstanceTypeDetails": List["InstanceTypeDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPackagesForDomainRequestRequestTypeDef = TypedDict(
    "ListPackagesForDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListPackagesForDomainResponseTypeDef = TypedDict(
    "ListPackagesForDomainResponseTypeDef",
    {
        "DomainPackageDetailsList": List["DomainPackageDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "ARN": str,
    },
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVersionsRequestRequestTypeDef = TypedDict(
    "ListVersionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListVersionsResponseTypeDef = TypedDict(
    "ListVersionsResponseTypeDef",
    {
        "Versions": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogPublishingOptionTypeDef = TypedDict(
    "LogPublishingOptionTypeDef",
    {
        "CloudWatchLogsLogGroupArn": NotRequired[str],
        "Enabled": NotRequired[bool],
    },
)

LogPublishingOptionsStatusTypeDef = TypedDict(
    "LogPublishingOptionsStatusTypeDef",
    {
        "Options": NotRequired[Dict[LogTypeType, "LogPublishingOptionTypeDef"]],
        "Status": NotRequired["OptionStatusTypeDef"],
    },
)

MasterUserOptionsTypeDef = TypedDict(
    "MasterUserOptionsTypeDef",
    {
        "MasterUserARN": NotRequired[str],
        "MasterUserName": NotRequired[str],
        "MasterUserPassword": NotRequired[str],
    },
)

NodeToNodeEncryptionOptionsStatusTypeDef = TypedDict(
    "NodeToNodeEncryptionOptionsStatusTypeDef",
    {
        "Options": "NodeToNodeEncryptionOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

NodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "NodeToNodeEncryptionOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)

OptionStatusTypeDef = TypedDict(
    "OptionStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "State": OptionStateType,
        "UpdateVersion": NotRequired[int],
        "PendingDeletion": NotRequired[bool],
    },
)

OutboundConnectionStatusTypeDef = TypedDict(
    "OutboundConnectionStatusTypeDef",
    {
        "StatusCode": NotRequired[OutboundConnectionStatusCodeType],
        "Message": NotRequired[str],
    },
)

OutboundConnectionTypeDef = TypedDict(
    "OutboundConnectionTypeDef",
    {
        "LocalDomainInfo": NotRequired["DomainInformationContainerTypeDef"],
        "RemoteDomainInfo": NotRequired["DomainInformationContainerTypeDef"],
        "ConnectionId": NotRequired[str],
        "ConnectionAlias": NotRequired[str],
        "ConnectionStatus": NotRequired["OutboundConnectionStatusTypeDef"],
    },
)

PackageDetailsTypeDef = TypedDict(
    "PackageDetailsTypeDef",
    {
        "PackageID": NotRequired[str],
        "PackageName": NotRequired[str],
        "PackageType": NotRequired[Literal["TXT-DICTIONARY"]],
        "PackageDescription": NotRequired[str],
        "PackageStatus": NotRequired[PackageStatusType],
        "CreatedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "AvailablePackageVersion": NotRequired[str],
        "ErrorDetails": NotRequired["ErrorDetailsTypeDef"],
    },
)

PackageSourceTypeDef = TypedDict(
    "PackageSourceTypeDef",
    {
        "S3BucketName": NotRequired[str],
        "S3Key": NotRequired[str],
    },
)

PackageVersionHistoryTypeDef = TypedDict(
    "PackageVersionHistoryTypeDef",
    {
        "PackageVersion": NotRequired[str],
        "CommitMessage": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
    },
)

PurchaseReservedInstanceOfferingRequestRequestTypeDef = TypedDict(
    "PurchaseReservedInstanceOfferingRequestRequestTypeDef",
    {
        "ReservedInstanceOfferingId": str,
        "ReservationName": str,
        "InstanceCount": NotRequired[int],
    },
)

PurchaseReservedInstanceOfferingResponseTypeDef = TypedDict(
    "PurchaseReservedInstanceOfferingResponseTypeDef",
    {
        "ReservedInstanceId": str,
        "ReservationName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {
        "RecurringChargeAmount": NotRequired[float],
        "RecurringChargeFrequency": NotRequired[str],
    },
)

RejectInboundConnectionRequestRequestTypeDef = TypedDict(
    "RejectInboundConnectionRequestRequestTypeDef",
    {
        "ConnectionId": str,
    },
)

RejectInboundConnectionResponseTypeDef = TypedDict(
    "RejectInboundConnectionResponseTypeDef",
    {
        "Connection": "InboundConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTagsRequestRequestTypeDef = TypedDict(
    "RemoveTagsRequestRequestTypeDef",
    {
        "ARN": str,
        "TagKeys": Sequence[str],
    },
)

ReservedInstanceOfferingTypeDef = TypedDict(
    "ReservedInstanceOfferingTypeDef",
    {
        "ReservedInstanceOfferingId": NotRequired[str],
        "InstanceType": NotRequired[OpenSearchPartitionInstanceTypeType],
        "Duration": NotRequired[int],
        "FixedPrice": NotRequired[float],
        "UsagePrice": NotRequired[float],
        "CurrencyCode": NotRequired[str],
        "PaymentOption": NotRequired[ReservedInstancePaymentOptionType],
        "RecurringCharges": NotRequired[List["RecurringChargeTypeDef"]],
    },
)

ReservedInstanceTypeDef = TypedDict(
    "ReservedInstanceTypeDef",
    {
        "ReservationName": NotRequired[str],
        "ReservedInstanceId": NotRequired[str],
        "BillingSubscriptionId": NotRequired[int],
        "ReservedInstanceOfferingId": NotRequired[str],
        "InstanceType": NotRequired[OpenSearchPartitionInstanceTypeType],
        "StartTime": NotRequired[datetime],
        "Duration": NotRequired[int],
        "FixedPrice": NotRequired[float],
        "UsagePrice": NotRequired[float],
        "CurrencyCode": NotRequired[str],
        "InstanceCount": NotRequired[int],
        "State": NotRequired[str],
        "PaymentOption": NotRequired[ReservedInstancePaymentOptionType],
        "RecurringCharges": NotRequired[List["RecurringChargeTypeDef"]],
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

SAMLIdpTypeDef = TypedDict(
    "SAMLIdpTypeDef",
    {
        "MetadataContent": str,
        "EntityId": str,
    },
)

SAMLOptionsInputTypeDef = TypedDict(
    "SAMLOptionsInputTypeDef",
    {
        "Enabled": NotRequired[bool],
        "Idp": NotRequired["SAMLIdpTypeDef"],
        "MasterUserName": NotRequired[str],
        "MasterBackendRole": NotRequired[str],
        "SubjectKey": NotRequired[str],
        "RolesKey": NotRequired[str],
        "SessionTimeoutMinutes": NotRequired[int],
    },
)

SAMLOptionsOutputTypeDef = TypedDict(
    "SAMLOptionsOutputTypeDef",
    {
        "Enabled": NotRequired[bool],
        "Idp": NotRequired["SAMLIdpTypeDef"],
        "SubjectKey": NotRequired[str],
        "RolesKey": NotRequired[str],
        "SessionTimeoutMinutes": NotRequired[int],
    },
)

ScheduledAutoTuneDetailsTypeDef = TypedDict(
    "ScheduledAutoTuneDetailsTypeDef",
    {
        "Date": NotRequired[datetime],
        "ActionType": NotRequired[ScheduledAutoTuneActionTypeType],
        "Action": NotRequired[str],
        "Severity": NotRequired[ScheduledAutoTuneSeverityTypeType],
    },
)

ServiceSoftwareOptionsTypeDef = TypedDict(
    "ServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": NotRequired[str],
        "NewVersion": NotRequired[str],
        "UpdateAvailable": NotRequired[bool],
        "Cancellable": NotRequired[bool],
        "UpdateStatus": NotRequired[DeploymentStatusType],
        "Description": NotRequired[str],
        "AutomatedUpdateDate": NotRequired[datetime],
        "OptionalDeployment": NotRequired[bool],
    },
)

SnapshotOptionsStatusTypeDef = TypedDict(
    "SnapshotOptionsStatusTypeDef",
    {
        "Options": "SnapshotOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

SnapshotOptionsTypeDef = TypedDict(
    "SnapshotOptionsTypeDef",
    {
        "AutomatedSnapshotStartHour": NotRequired[int],
    },
)

StartServiceSoftwareUpdateRequestRequestTypeDef = TypedDict(
    "StartServiceSoftwareUpdateRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

StartServiceSoftwareUpdateResponseTypeDef = TypedDict(
    "StartServiceSoftwareUpdateResponseTypeDef",
    {
        "ServiceSoftwareOptions": "ServiceSoftwareOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StorageTypeLimitTypeDef = TypedDict(
    "StorageTypeLimitTypeDef",
    {
        "LimitName": NotRequired[str],
        "LimitValues": NotRequired[List[str]],
    },
)

StorageTypeTypeDef = TypedDict(
    "StorageTypeTypeDef",
    {
        "StorageTypeName": NotRequired[str],
        "StorageSubTypeName": NotRequired[str],
        "StorageTypeLimits": NotRequired[List["StorageTypeLimitTypeDef"]],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UpdateDomainConfigRequestRequestTypeDef = TypedDict(
    "UpdateDomainConfigRequestRequestTypeDef",
    {
        "DomainName": str,
        "ClusterConfig": NotRequired["ClusterConfigTypeDef"],
        "EBSOptions": NotRequired["EBSOptionsTypeDef"],
        "SnapshotOptions": NotRequired["SnapshotOptionsTypeDef"],
        "VPCOptions": NotRequired["VPCOptionsTypeDef"],
        "CognitoOptions": NotRequired["CognitoOptionsTypeDef"],
        "AdvancedOptions": NotRequired[Mapping[str, str]],
        "AccessPolicies": NotRequired[str],
        "LogPublishingOptions": NotRequired[Mapping[LogTypeType, "LogPublishingOptionTypeDef"]],
        "EncryptionAtRestOptions": NotRequired["EncryptionAtRestOptionsTypeDef"],
        "DomainEndpointOptions": NotRequired["DomainEndpointOptionsTypeDef"],
        "NodeToNodeEncryptionOptions": NotRequired["NodeToNodeEncryptionOptionsTypeDef"],
        "AdvancedSecurityOptions": NotRequired["AdvancedSecurityOptionsInputTypeDef"],
        "AutoTuneOptions": NotRequired["AutoTuneOptionsTypeDef"],
        "DryRun": NotRequired[bool],
    },
)

UpdateDomainConfigResponseTypeDef = TypedDict(
    "UpdateDomainConfigResponseTypeDef",
    {
        "DomainConfig": "DomainConfigTypeDef",
        "DryRunResults": "DryRunResultsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePackageRequestRequestTypeDef = TypedDict(
    "UpdatePackageRequestRequestTypeDef",
    {
        "PackageID": str,
        "PackageSource": "PackageSourceTypeDef",
        "PackageDescription": NotRequired[str],
        "CommitMessage": NotRequired[str],
    },
)

UpdatePackageResponseTypeDef = TypedDict(
    "UpdatePackageResponseTypeDef",
    {
        "PackageDetails": "PackageDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpgradeDomainRequestRequestTypeDef = TypedDict(
    "UpgradeDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "TargetVersion": str,
        "PerformCheckOnly": NotRequired[bool],
        "AdvancedOptions": NotRequired[Mapping[str, str]],
    },
)

UpgradeDomainResponseTypeDef = TypedDict(
    "UpgradeDomainResponseTypeDef",
    {
        "UpgradeId": str,
        "DomainName": str,
        "TargetVersion": str,
        "PerformCheckOnly": bool,
        "AdvancedOptions": Dict[str, str],
        "ChangeProgressDetails": "ChangeProgressDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpgradeHistoryTypeDef = TypedDict(
    "UpgradeHistoryTypeDef",
    {
        "UpgradeName": NotRequired[str],
        "StartTimestamp": NotRequired[datetime],
        "UpgradeStatus": NotRequired[UpgradeStatusType],
        "StepsList": NotRequired[List["UpgradeStepItemTypeDef"]],
    },
)

UpgradeStepItemTypeDef = TypedDict(
    "UpgradeStepItemTypeDef",
    {
        "UpgradeStep": NotRequired[UpgradeStepType],
        "UpgradeStepStatus": NotRequired[UpgradeStatusType],
        "Issues": NotRequired[List[str]],
        "ProgressPercent": NotRequired[float],
    },
)

VPCDerivedInfoStatusTypeDef = TypedDict(
    "VPCDerivedInfoStatusTypeDef",
    {
        "Options": "VPCDerivedInfoTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

VPCDerivedInfoTypeDef = TypedDict(
    "VPCDerivedInfoTypeDef",
    {
        "VPCId": NotRequired[str],
        "SubnetIds": NotRequired[List[str]],
        "AvailabilityZones": NotRequired[List[str]],
        "SecurityGroupIds": NotRequired[List[str]],
    },
)

VPCOptionsTypeDef = TypedDict(
    "VPCOptionsTypeDef",
    {
        "SubnetIds": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
    },
)

VersionStatusTypeDef = TypedDict(
    "VersionStatusTypeDef",
    {
        "Options": str,
        "Status": "OptionStatusTypeDef",
    },
)

ZoneAwarenessConfigTypeDef = TypedDict(
    "ZoneAwarenessConfigTypeDef",
    {
        "AvailabilityZoneCount": NotRequired[int],
    },
)
