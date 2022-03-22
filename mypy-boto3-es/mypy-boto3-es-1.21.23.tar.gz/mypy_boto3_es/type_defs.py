"""
Type annotations for es service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/type_defs.html)

Usage::

    ```python
    from mypy_boto3_es.type_defs import AcceptInboundCrossClusterSearchConnectionRequestRequestTypeDef

    data: AcceptInboundCrossClusterSearchConnectionRequestRequestTypeDef = {...}
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
    ESPartitionInstanceTypeType,
    ESWarmPartitionInstanceTypeType,
    InboundCrossClusterSearchConnectionStatusCodeType,
    LogTypeType,
    OptionStateType,
    OutboundCrossClusterSearchConnectionStatusCodeType,
    OverallChangeStatusType,
    PackageStatusType,
    ReservedElasticsearchInstancePaymentOptionType,
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
    "AcceptInboundCrossClusterSearchConnectionRequestRequestTypeDef",
    "AcceptInboundCrossClusterSearchConnectionResponseTypeDef",
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
    "CancelElasticsearchServiceSoftwareUpdateRequestRequestTypeDef",
    "CancelElasticsearchServiceSoftwareUpdateResponseTypeDef",
    "ChangeProgressDetailsTypeDef",
    "ChangeProgressStageTypeDef",
    "ChangeProgressStatusDetailsTypeDef",
    "CognitoOptionsStatusTypeDef",
    "CognitoOptionsTypeDef",
    "ColdStorageOptionsTypeDef",
    "CompatibleVersionsMapTypeDef",
    "CreateElasticsearchDomainRequestRequestTypeDef",
    "CreateElasticsearchDomainResponseTypeDef",
    "CreateOutboundCrossClusterSearchConnectionRequestRequestTypeDef",
    "CreateOutboundCrossClusterSearchConnectionResponseTypeDef",
    "CreatePackageRequestRequestTypeDef",
    "CreatePackageResponseTypeDef",
    "DeleteElasticsearchDomainRequestRequestTypeDef",
    "DeleteElasticsearchDomainResponseTypeDef",
    "DeleteInboundCrossClusterSearchConnectionRequestRequestTypeDef",
    "DeleteInboundCrossClusterSearchConnectionResponseTypeDef",
    "DeleteOutboundCrossClusterSearchConnectionRequestRequestTypeDef",
    "DeleteOutboundCrossClusterSearchConnectionResponseTypeDef",
    "DeletePackageRequestRequestTypeDef",
    "DeletePackageResponseTypeDef",
    "DescribeDomainAutoTunesRequestRequestTypeDef",
    "DescribeDomainAutoTunesResponseTypeDef",
    "DescribeDomainChangeProgressRequestRequestTypeDef",
    "DescribeDomainChangeProgressResponseTypeDef",
    "DescribeElasticsearchDomainConfigRequestRequestTypeDef",
    "DescribeElasticsearchDomainConfigResponseTypeDef",
    "DescribeElasticsearchDomainRequestRequestTypeDef",
    "DescribeElasticsearchDomainResponseTypeDef",
    "DescribeElasticsearchDomainsRequestRequestTypeDef",
    "DescribeElasticsearchDomainsResponseTypeDef",
    "DescribeElasticsearchInstanceTypeLimitsRequestRequestTypeDef",
    "DescribeElasticsearchInstanceTypeLimitsResponseTypeDef",
    "DescribeInboundCrossClusterSearchConnectionsRequestRequestTypeDef",
    "DescribeInboundCrossClusterSearchConnectionsResponseTypeDef",
    "DescribeOutboundCrossClusterSearchConnectionsRequestRequestTypeDef",
    "DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef",
    "DescribePackagesFilterTypeDef",
    "DescribePackagesRequestRequestTypeDef",
    "DescribePackagesResponseTypeDef",
    "DescribeReservedElasticsearchInstanceOfferingsRequestRequestTypeDef",
    "DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef",
    "DescribeReservedElasticsearchInstancesRequestRequestTypeDef",
    "DescribeReservedElasticsearchInstancesResponseTypeDef",
    "DissociatePackageRequestRequestTypeDef",
    "DissociatePackageResponseTypeDef",
    "DomainEndpointOptionsStatusTypeDef",
    "DomainEndpointOptionsTypeDef",
    "DomainInfoTypeDef",
    "DomainInformationTypeDef",
    "DomainPackageDetailsTypeDef",
    "DryRunResultsTypeDef",
    "DurationTypeDef",
    "EBSOptionsStatusTypeDef",
    "EBSOptionsTypeDef",
    "ElasticsearchClusterConfigStatusTypeDef",
    "ElasticsearchClusterConfigTypeDef",
    "ElasticsearchDomainConfigTypeDef",
    "ElasticsearchDomainStatusTypeDef",
    "ElasticsearchVersionStatusTypeDef",
    "EncryptionAtRestOptionsStatusTypeDef",
    "EncryptionAtRestOptionsTypeDef",
    "ErrorDetailsTypeDef",
    "FilterTypeDef",
    "GetCompatibleElasticsearchVersionsRequestRequestTypeDef",
    "GetCompatibleElasticsearchVersionsResponseTypeDef",
    "GetPackageVersionHistoryRequestRequestTypeDef",
    "GetPackageVersionHistoryResponseTypeDef",
    "GetUpgradeHistoryRequestRequestTypeDef",
    "GetUpgradeHistoryResponseTypeDef",
    "GetUpgradeStatusRequestRequestTypeDef",
    "GetUpgradeStatusResponseTypeDef",
    "InboundCrossClusterSearchConnectionStatusTypeDef",
    "InboundCrossClusterSearchConnectionTypeDef",
    "InstanceCountLimitsTypeDef",
    "InstanceLimitsTypeDef",
    "LimitsTypeDef",
    "ListDomainNamesRequestRequestTypeDef",
    "ListDomainNamesResponseTypeDef",
    "ListDomainsForPackageRequestRequestTypeDef",
    "ListDomainsForPackageResponseTypeDef",
    "ListElasticsearchInstanceTypesRequestRequestTypeDef",
    "ListElasticsearchInstanceTypesResponseTypeDef",
    "ListElasticsearchVersionsRequestRequestTypeDef",
    "ListElasticsearchVersionsResponseTypeDef",
    "ListPackagesForDomainRequestRequestTypeDef",
    "ListPackagesForDomainResponseTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "LogPublishingOptionTypeDef",
    "LogPublishingOptionsStatusTypeDef",
    "MasterUserOptionsTypeDef",
    "NodeToNodeEncryptionOptionsStatusTypeDef",
    "NodeToNodeEncryptionOptionsTypeDef",
    "OptionStatusTypeDef",
    "OutboundCrossClusterSearchConnectionStatusTypeDef",
    "OutboundCrossClusterSearchConnectionTypeDef",
    "PackageDetailsTypeDef",
    "PackageSourceTypeDef",
    "PackageVersionHistoryTypeDef",
    "PaginatorConfigTypeDef",
    "PurchaseReservedElasticsearchInstanceOfferingRequestRequestTypeDef",
    "PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef",
    "RecurringChargeTypeDef",
    "RejectInboundCrossClusterSearchConnectionRequestRequestTypeDef",
    "RejectInboundCrossClusterSearchConnectionResponseTypeDef",
    "RemoveTagsRequestRequestTypeDef",
    "ReservedElasticsearchInstanceOfferingTypeDef",
    "ReservedElasticsearchInstanceTypeDef",
    "ResponseMetadataTypeDef",
    "SAMLIdpTypeDef",
    "SAMLOptionsInputTypeDef",
    "SAMLOptionsOutputTypeDef",
    "ScheduledAutoTuneDetailsTypeDef",
    "ServiceSoftwareOptionsTypeDef",
    "SnapshotOptionsStatusTypeDef",
    "SnapshotOptionsTypeDef",
    "StartElasticsearchServiceSoftwareUpdateRequestRequestTypeDef",
    "StartElasticsearchServiceSoftwareUpdateResponseTypeDef",
    "StorageTypeLimitTypeDef",
    "StorageTypeTypeDef",
    "TagTypeDef",
    "UpdateElasticsearchDomainConfigRequestRequestTypeDef",
    "UpdateElasticsearchDomainConfigResponseTypeDef",
    "UpdatePackageRequestRequestTypeDef",
    "UpdatePackageResponseTypeDef",
    "UpgradeElasticsearchDomainRequestRequestTypeDef",
    "UpgradeElasticsearchDomainResponseTypeDef",
    "UpgradeHistoryTypeDef",
    "UpgradeStepItemTypeDef",
    "VPCDerivedInfoStatusTypeDef",
    "VPCDerivedInfoTypeDef",
    "VPCOptionsTypeDef",
    "ZoneAwarenessConfigTypeDef",
)

AcceptInboundCrossClusterSearchConnectionRequestRequestTypeDef = TypedDict(
    "AcceptInboundCrossClusterSearchConnectionRequestRequestTypeDef",
    {
        "CrossClusterSearchConnectionId": str,
    },
)

AcceptInboundCrossClusterSearchConnectionResponseTypeDef = TypedDict(
    "AcceptInboundCrossClusterSearchConnectionResponseTypeDef",
    {
        "CrossClusterSearchConnection": "InboundCrossClusterSearchConnectionTypeDef",
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

CancelElasticsearchServiceSoftwareUpdateRequestRequestTypeDef = TypedDict(
    "CancelElasticsearchServiceSoftwareUpdateRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

CancelElasticsearchServiceSoftwareUpdateResponseTypeDef = TypedDict(
    "CancelElasticsearchServiceSoftwareUpdateResponseTypeDef",
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

CreateElasticsearchDomainRequestRequestTypeDef = TypedDict(
    "CreateElasticsearchDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "ElasticsearchVersion": NotRequired[str],
        "ElasticsearchClusterConfig": NotRequired["ElasticsearchClusterConfigTypeDef"],
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
        "AutoTuneOptions": NotRequired["AutoTuneOptionsInputTypeDef"],
        "TagList": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateElasticsearchDomainResponseTypeDef = TypedDict(
    "CreateElasticsearchDomainResponseTypeDef",
    {
        "DomainStatus": "ElasticsearchDomainStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateOutboundCrossClusterSearchConnectionRequestRequestTypeDef = TypedDict(
    "CreateOutboundCrossClusterSearchConnectionRequestRequestTypeDef",
    {
        "SourceDomainInfo": "DomainInformationTypeDef",
        "DestinationDomainInfo": "DomainInformationTypeDef",
        "ConnectionAlias": str,
    },
)

CreateOutboundCrossClusterSearchConnectionResponseTypeDef = TypedDict(
    "CreateOutboundCrossClusterSearchConnectionResponseTypeDef",
    {
        "SourceDomainInfo": "DomainInformationTypeDef",
        "DestinationDomainInfo": "DomainInformationTypeDef",
        "ConnectionAlias": str,
        "ConnectionStatus": "OutboundCrossClusterSearchConnectionStatusTypeDef",
        "CrossClusterSearchConnectionId": str,
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

DeleteElasticsearchDomainRequestRequestTypeDef = TypedDict(
    "DeleteElasticsearchDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DeleteElasticsearchDomainResponseTypeDef = TypedDict(
    "DeleteElasticsearchDomainResponseTypeDef",
    {
        "DomainStatus": "ElasticsearchDomainStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInboundCrossClusterSearchConnectionRequestRequestTypeDef = TypedDict(
    "DeleteInboundCrossClusterSearchConnectionRequestRequestTypeDef",
    {
        "CrossClusterSearchConnectionId": str,
    },
)

DeleteInboundCrossClusterSearchConnectionResponseTypeDef = TypedDict(
    "DeleteInboundCrossClusterSearchConnectionResponseTypeDef",
    {
        "CrossClusterSearchConnection": "InboundCrossClusterSearchConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteOutboundCrossClusterSearchConnectionRequestRequestTypeDef = TypedDict(
    "DeleteOutboundCrossClusterSearchConnectionRequestRequestTypeDef",
    {
        "CrossClusterSearchConnectionId": str,
    },
)

DeleteOutboundCrossClusterSearchConnectionResponseTypeDef = TypedDict(
    "DeleteOutboundCrossClusterSearchConnectionResponseTypeDef",
    {
        "CrossClusterSearchConnection": "OutboundCrossClusterSearchConnectionTypeDef",
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

DescribeElasticsearchDomainConfigRequestRequestTypeDef = TypedDict(
    "DescribeElasticsearchDomainConfigRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DescribeElasticsearchDomainConfigResponseTypeDef = TypedDict(
    "DescribeElasticsearchDomainConfigResponseTypeDef",
    {
        "DomainConfig": "ElasticsearchDomainConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeElasticsearchDomainRequestRequestTypeDef = TypedDict(
    "DescribeElasticsearchDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DescribeElasticsearchDomainResponseTypeDef = TypedDict(
    "DescribeElasticsearchDomainResponseTypeDef",
    {
        "DomainStatus": "ElasticsearchDomainStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeElasticsearchDomainsRequestRequestTypeDef = TypedDict(
    "DescribeElasticsearchDomainsRequestRequestTypeDef",
    {
        "DomainNames": Sequence[str],
    },
)

DescribeElasticsearchDomainsResponseTypeDef = TypedDict(
    "DescribeElasticsearchDomainsResponseTypeDef",
    {
        "DomainStatusList": List["ElasticsearchDomainStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeElasticsearchInstanceTypeLimitsRequestRequestTypeDef = TypedDict(
    "DescribeElasticsearchInstanceTypeLimitsRequestRequestTypeDef",
    {
        "InstanceType": ESPartitionInstanceTypeType,
        "ElasticsearchVersion": str,
        "DomainName": NotRequired[str],
    },
)

DescribeElasticsearchInstanceTypeLimitsResponseTypeDef = TypedDict(
    "DescribeElasticsearchInstanceTypeLimitsResponseTypeDef",
    {
        "LimitsByRole": Dict[str, "LimitsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInboundCrossClusterSearchConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeInboundCrossClusterSearchConnectionsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeInboundCrossClusterSearchConnectionsResponseTypeDef = TypedDict(
    "DescribeInboundCrossClusterSearchConnectionsResponseTypeDef",
    {
        "CrossClusterSearchConnections": List["InboundCrossClusterSearchConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOutboundCrossClusterSearchConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeOutboundCrossClusterSearchConnectionsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef = TypedDict(
    "DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef",
    {
        "CrossClusterSearchConnections": List["OutboundCrossClusterSearchConnectionTypeDef"],
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

DescribeReservedElasticsearchInstanceOfferingsRequestRequestTypeDef = TypedDict(
    "DescribeReservedElasticsearchInstanceOfferingsRequestRequestTypeDef",
    {
        "ReservedElasticsearchInstanceOfferingId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef = TypedDict(
    "DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef",
    {
        "NextToken": str,
        "ReservedElasticsearchInstanceOfferings": List[
            "ReservedElasticsearchInstanceOfferingTypeDef"
        ],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedElasticsearchInstancesRequestRequestTypeDef = TypedDict(
    "DescribeReservedElasticsearchInstancesRequestRequestTypeDef",
    {
        "ReservedElasticsearchInstanceId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeReservedElasticsearchInstancesResponseTypeDef = TypedDict(
    "DescribeReservedElasticsearchInstancesResponseTypeDef",
    {
        "NextToken": str,
        "ReservedElasticsearchInstances": List["ReservedElasticsearchInstanceTypeDef"],
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

DomainInformationTypeDef = TypedDict(
    "DomainInformationTypeDef",
    {
        "DomainName": str,
        "OwnerId": NotRequired[str],
        "Region": NotRequired[str],
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

ElasticsearchClusterConfigStatusTypeDef = TypedDict(
    "ElasticsearchClusterConfigStatusTypeDef",
    {
        "Options": "ElasticsearchClusterConfigTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

ElasticsearchClusterConfigTypeDef = TypedDict(
    "ElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": NotRequired[ESPartitionInstanceTypeType],
        "InstanceCount": NotRequired[int],
        "DedicatedMasterEnabled": NotRequired[bool],
        "ZoneAwarenessEnabled": NotRequired[bool],
        "ZoneAwarenessConfig": NotRequired["ZoneAwarenessConfigTypeDef"],
        "DedicatedMasterType": NotRequired[ESPartitionInstanceTypeType],
        "DedicatedMasterCount": NotRequired[int],
        "WarmEnabled": NotRequired[bool],
        "WarmType": NotRequired[ESWarmPartitionInstanceTypeType],
        "WarmCount": NotRequired[int],
        "ColdStorageOptions": NotRequired["ColdStorageOptionsTypeDef"],
    },
)

ElasticsearchDomainConfigTypeDef = TypedDict(
    "ElasticsearchDomainConfigTypeDef",
    {
        "ElasticsearchVersion": NotRequired["ElasticsearchVersionStatusTypeDef"],
        "ElasticsearchClusterConfig": NotRequired["ElasticsearchClusterConfigStatusTypeDef"],
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

ElasticsearchDomainStatusTypeDef = TypedDict(
    "ElasticsearchDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "ElasticsearchClusterConfig": "ElasticsearchClusterConfigTypeDef",
        "Created": NotRequired[bool],
        "Deleted": NotRequired[bool],
        "Endpoint": NotRequired[str],
        "Endpoints": NotRequired[Dict[str, str]],
        "Processing": NotRequired[bool],
        "UpgradeProcessing": NotRequired[bool],
        "ElasticsearchVersion": NotRequired[str],
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

ElasticsearchVersionStatusTypeDef = TypedDict(
    "ElasticsearchVersionStatusTypeDef",
    {
        "Options": str,
        "Status": "OptionStatusTypeDef",
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

GetCompatibleElasticsearchVersionsRequestRequestTypeDef = TypedDict(
    "GetCompatibleElasticsearchVersionsRequestRequestTypeDef",
    {
        "DomainName": NotRequired[str],
    },
)

GetCompatibleElasticsearchVersionsResponseTypeDef = TypedDict(
    "GetCompatibleElasticsearchVersionsResponseTypeDef",
    {
        "CompatibleElasticsearchVersions": List["CompatibleVersionsMapTypeDef"],
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

InboundCrossClusterSearchConnectionStatusTypeDef = TypedDict(
    "InboundCrossClusterSearchConnectionStatusTypeDef",
    {
        "StatusCode": NotRequired[InboundCrossClusterSearchConnectionStatusCodeType],
        "Message": NotRequired[str],
    },
)

InboundCrossClusterSearchConnectionTypeDef = TypedDict(
    "InboundCrossClusterSearchConnectionTypeDef",
    {
        "SourceDomainInfo": NotRequired["DomainInformationTypeDef"],
        "DestinationDomainInfo": NotRequired["DomainInformationTypeDef"],
        "CrossClusterSearchConnectionId": NotRequired[str],
        "ConnectionStatus": NotRequired["InboundCrossClusterSearchConnectionStatusTypeDef"],
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

ListElasticsearchInstanceTypesRequestRequestTypeDef = TypedDict(
    "ListElasticsearchInstanceTypesRequestRequestTypeDef",
    {
        "ElasticsearchVersion": str,
        "DomainName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListElasticsearchInstanceTypesResponseTypeDef = TypedDict(
    "ListElasticsearchInstanceTypesResponseTypeDef",
    {
        "ElasticsearchInstanceTypes": List[ESPartitionInstanceTypeType],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListElasticsearchVersionsRequestRequestTypeDef = TypedDict(
    "ListElasticsearchVersionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListElasticsearchVersionsResponseTypeDef = TypedDict(
    "ListElasticsearchVersionsResponseTypeDef",
    {
        "ElasticsearchVersions": List[str],
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

OutboundCrossClusterSearchConnectionStatusTypeDef = TypedDict(
    "OutboundCrossClusterSearchConnectionStatusTypeDef",
    {
        "StatusCode": NotRequired[OutboundCrossClusterSearchConnectionStatusCodeType],
        "Message": NotRequired[str],
    },
)

OutboundCrossClusterSearchConnectionTypeDef = TypedDict(
    "OutboundCrossClusterSearchConnectionTypeDef",
    {
        "SourceDomainInfo": NotRequired["DomainInformationTypeDef"],
        "DestinationDomainInfo": NotRequired["DomainInformationTypeDef"],
        "CrossClusterSearchConnectionId": NotRequired[str],
        "ConnectionAlias": NotRequired[str],
        "ConnectionStatus": NotRequired["OutboundCrossClusterSearchConnectionStatusTypeDef"],
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)

PurchaseReservedElasticsearchInstanceOfferingRequestRequestTypeDef = TypedDict(
    "PurchaseReservedElasticsearchInstanceOfferingRequestRequestTypeDef",
    {
        "ReservedElasticsearchInstanceOfferingId": str,
        "ReservationName": str,
        "InstanceCount": NotRequired[int],
    },
)

PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef = TypedDict(
    "PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef",
    {
        "ReservedElasticsearchInstanceId": str,
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

RejectInboundCrossClusterSearchConnectionRequestRequestTypeDef = TypedDict(
    "RejectInboundCrossClusterSearchConnectionRequestRequestTypeDef",
    {
        "CrossClusterSearchConnectionId": str,
    },
)

RejectInboundCrossClusterSearchConnectionResponseTypeDef = TypedDict(
    "RejectInboundCrossClusterSearchConnectionResponseTypeDef",
    {
        "CrossClusterSearchConnection": "InboundCrossClusterSearchConnectionTypeDef",
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

ReservedElasticsearchInstanceOfferingTypeDef = TypedDict(
    "ReservedElasticsearchInstanceOfferingTypeDef",
    {
        "ReservedElasticsearchInstanceOfferingId": NotRequired[str],
        "ElasticsearchInstanceType": NotRequired[ESPartitionInstanceTypeType],
        "Duration": NotRequired[int],
        "FixedPrice": NotRequired[float],
        "UsagePrice": NotRequired[float],
        "CurrencyCode": NotRequired[str],
        "PaymentOption": NotRequired[ReservedElasticsearchInstancePaymentOptionType],
        "RecurringCharges": NotRequired[List["RecurringChargeTypeDef"]],
    },
)

ReservedElasticsearchInstanceTypeDef = TypedDict(
    "ReservedElasticsearchInstanceTypeDef",
    {
        "ReservationName": NotRequired[str],
        "ReservedElasticsearchInstanceId": NotRequired[str],
        "ReservedElasticsearchInstanceOfferingId": NotRequired[str],
        "ElasticsearchInstanceType": NotRequired[ESPartitionInstanceTypeType],
        "StartTime": NotRequired[datetime],
        "Duration": NotRequired[int],
        "FixedPrice": NotRequired[float],
        "UsagePrice": NotRequired[float],
        "CurrencyCode": NotRequired[str],
        "ElasticsearchInstanceCount": NotRequired[int],
        "State": NotRequired[str],
        "PaymentOption": NotRequired[ReservedElasticsearchInstancePaymentOptionType],
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

StartElasticsearchServiceSoftwareUpdateRequestRequestTypeDef = TypedDict(
    "StartElasticsearchServiceSoftwareUpdateRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

StartElasticsearchServiceSoftwareUpdateResponseTypeDef = TypedDict(
    "StartElasticsearchServiceSoftwareUpdateResponseTypeDef",
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

UpdateElasticsearchDomainConfigRequestRequestTypeDef = TypedDict(
    "UpdateElasticsearchDomainConfigRequestRequestTypeDef",
    {
        "DomainName": str,
        "ElasticsearchClusterConfig": NotRequired["ElasticsearchClusterConfigTypeDef"],
        "EBSOptions": NotRequired["EBSOptionsTypeDef"],
        "SnapshotOptions": NotRequired["SnapshotOptionsTypeDef"],
        "VPCOptions": NotRequired["VPCOptionsTypeDef"],
        "CognitoOptions": NotRequired["CognitoOptionsTypeDef"],
        "AdvancedOptions": NotRequired[Mapping[str, str]],
        "AccessPolicies": NotRequired[str],
        "LogPublishingOptions": NotRequired[Mapping[LogTypeType, "LogPublishingOptionTypeDef"]],
        "DomainEndpointOptions": NotRequired["DomainEndpointOptionsTypeDef"],
        "AdvancedSecurityOptions": NotRequired["AdvancedSecurityOptionsInputTypeDef"],
        "NodeToNodeEncryptionOptions": NotRequired["NodeToNodeEncryptionOptionsTypeDef"],
        "EncryptionAtRestOptions": NotRequired["EncryptionAtRestOptionsTypeDef"],
        "AutoTuneOptions": NotRequired["AutoTuneOptionsTypeDef"],
        "DryRun": NotRequired[bool],
    },
)

UpdateElasticsearchDomainConfigResponseTypeDef = TypedDict(
    "UpdateElasticsearchDomainConfigResponseTypeDef",
    {
        "DomainConfig": "ElasticsearchDomainConfigTypeDef",
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

UpgradeElasticsearchDomainRequestRequestTypeDef = TypedDict(
    "UpgradeElasticsearchDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "TargetVersion": str,
        "PerformCheckOnly": NotRequired[bool],
    },
)

UpgradeElasticsearchDomainResponseTypeDef = TypedDict(
    "UpgradeElasticsearchDomainResponseTypeDef",
    {
        "DomainName": str,
        "TargetVersion": str,
        "PerformCheckOnly": bool,
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

ZoneAwarenessConfigTypeDef = TypedDict(
    "ZoneAwarenessConfigTypeDef",
    {
        "AvailabilityZoneCount": NotRequired[int],
    },
)
