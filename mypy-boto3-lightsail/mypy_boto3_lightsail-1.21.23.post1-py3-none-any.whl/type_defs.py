"""
Type annotations for lightsail service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lightsail.type_defs import AccessKeyLastUsedTypeDef

    data: AccessKeyLastUsedTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AccessDirectionType,
    AccessTypeType,
    AlarmStateType,
    AutoSnapshotStatusType,
    BehaviorEnumType,
    BlueprintTypeType,
    BucketMetricNameType,
    CertificateStatusType,
    ComparisonOperatorType,
    ContactMethodStatusType,
    ContactProtocolType,
    ContainerServiceDeploymentStateType,
    ContainerServiceMetricNameType,
    ContainerServicePowerNameType,
    ContainerServiceProtocolType,
    ContainerServiceStateDetailCodeType,
    ContainerServiceStateType,
    DiskSnapshotStateType,
    DiskStateType,
    DistributionMetricNameType,
    ExportSnapshotRecordSourceTypeType,
    ForwardValuesType,
    HeaderEnumType,
    InstanceAccessProtocolType,
    InstanceHealthReasonType,
    InstanceHealthStateType,
    InstanceMetricNameType,
    InstancePlatformType,
    InstanceSnapshotStateType,
    IpAddressTypeType,
    LoadBalancerAttributeNameType,
    LoadBalancerMetricNameType,
    LoadBalancerProtocolType,
    LoadBalancerStateType,
    LoadBalancerTlsCertificateDomainStatusType,
    LoadBalancerTlsCertificateFailureReasonType,
    LoadBalancerTlsCertificateRenewalStatusType,
    LoadBalancerTlsCertificateRevocationReasonType,
    LoadBalancerTlsCertificateStatusType,
    MetricNameType,
    MetricStatisticType,
    MetricUnitType,
    NetworkProtocolType,
    OperationStatusType,
    OperationTypeType,
    OriginProtocolPolicyEnumType,
    PortAccessTypeType,
    PortInfoSourceTypeType,
    PortStateType,
    RecordStateType,
    RegionNameType,
    RelationalDatabaseMetricNameType,
    RelationalDatabasePasswordVersionType,
    RenewalStatusType,
    ResourceBucketAccessType,
    ResourceTypeType,
    StatusTypeType,
    TreatMissingDataType,
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
    "AccessKeyLastUsedTypeDef",
    "AccessKeyTypeDef",
    "AccessRulesTypeDef",
    "AddOnRequestTypeDef",
    "AddOnTypeDef",
    "AlarmTypeDef",
    "AllocateStaticIpRequestRequestTypeDef",
    "AllocateStaticIpResultTypeDef",
    "AttachCertificateToDistributionRequestRequestTypeDef",
    "AttachCertificateToDistributionResultTypeDef",
    "AttachDiskRequestRequestTypeDef",
    "AttachDiskResultTypeDef",
    "AttachInstancesToLoadBalancerRequestRequestTypeDef",
    "AttachInstancesToLoadBalancerResultTypeDef",
    "AttachLoadBalancerTlsCertificateRequestRequestTypeDef",
    "AttachLoadBalancerTlsCertificateResultTypeDef",
    "AttachStaticIpRequestRequestTypeDef",
    "AttachStaticIpResultTypeDef",
    "AttachedDiskTypeDef",
    "AutoSnapshotAddOnRequestTypeDef",
    "AutoSnapshotDetailsTypeDef",
    "AvailabilityZoneTypeDef",
    "BlueprintTypeDef",
    "BucketAccessLogConfigTypeDef",
    "BucketBundleTypeDef",
    "BucketStateTypeDef",
    "BucketTypeDef",
    "BundleTypeDef",
    "CacheBehaviorPerPathTypeDef",
    "CacheBehaviorTypeDef",
    "CacheSettingsTypeDef",
    "CertificateSummaryTypeDef",
    "CertificateTypeDef",
    "CloseInstancePublicPortsRequestRequestTypeDef",
    "CloseInstancePublicPortsResultTypeDef",
    "CloudFormationStackRecordSourceInfoTypeDef",
    "CloudFormationStackRecordTypeDef",
    "ContactMethodTypeDef",
    "ContainerImageTypeDef",
    "ContainerServiceDeploymentRequestTypeDef",
    "ContainerServiceDeploymentTypeDef",
    "ContainerServiceEndpointTypeDef",
    "ContainerServiceHealthCheckConfigTypeDef",
    "ContainerServiceLogEventTypeDef",
    "ContainerServicePowerTypeDef",
    "ContainerServiceRegistryLoginTypeDef",
    "ContainerServiceStateDetailTypeDef",
    "ContainerServiceTypeDef",
    "ContainerServicesListResultTypeDef",
    "ContainerTypeDef",
    "CookieObjectTypeDef",
    "CopySnapshotRequestRequestTypeDef",
    "CopySnapshotResultTypeDef",
    "CreateBucketAccessKeyRequestRequestTypeDef",
    "CreateBucketAccessKeyResultTypeDef",
    "CreateBucketRequestRequestTypeDef",
    "CreateBucketResultTypeDef",
    "CreateCertificateRequestRequestTypeDef",
    "CreateCertificateResultTypeDef",
    "CreateCloudFormationStackRequestRequestTypeDef",
    "CreateCloudFormationStackResultTypeDef",
    "CreateContactMethodRequestRequestTypeDef",
    "CreateContactMethodResultTypeDef",
    "CreateContainerServiceDeploymentRequestRequestTypeDef",
    "CreateContainerServiceDeploymentResultTypeDef",
    "CreateContainerServiceRegistryLoginResultTypeDef",
    "CreateContainerServiceRequestRequestTypeDef",
    "CreateContainerServiceResultTypeDef",
    "CreateDiskFromSnapshotRequestRequestTypeDef",
    "CreateDiskFromSnapshotResultTypeDef",
    "CreateDiskRequestRequestTypeDef",
    "CreateDiskResultTypeDef",
    "CreateDiskSnapshotRequestRequestTypeDef",
    "CreateDiskSnapshotResultTypeDef",
    "CreateDistributionRequestRequestTypeDef",
    "CreateDistributionResultTypeDef",
    "CreateDomainEntryRequestRequestTypeDef",
    "CreateDomainEntryResultTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "CreateDomainResultTypeDef",
    "CreateInstanceSnapshotRequestRequestTypeDef",
    "CreateInstanceSnapshotResultTypeDef",
    "CreateInstancesFromSnapshotRequestRequestTypeDef",
    "CreateInstancesFromSnapshotResultTypeDef",
    "CreateInstancesRequestRequestTypeDef",
    "CreateInstancesResultTypeDef",
    "CreateKeyPairRequestRequestTypeDef",
    "CreateKeyPairResultTypeDef",
    "CreateLoadBalancerRequestRequestTypeDef",
    "CreateLoadBalancerResultTypeDef",
    "CreateLoadBalancerTlsCertificateRequestRequestTypeDef",
    "CreateLoadBalancerTlsCertificateResultTypeDef",
    "CreateRelationalDatabaseFromSnapshotRequestRequestTypeDef",
    "CreateRelationalDatabaseFromSnapshotResultTypeDef",
    "CreateRelationalDatabaseRequestRequestTypeDef",
    "CreateRelationalDatabaseResultTypeDef",
    "CreateRelationalDatabaseSnapshotRequestRequestTypeDef",
    "CreateRelationalDatabaseSnapshotResultTypeDef",
    "DeleteAlarmRequestRequestTypeDef",
    "DeleteAlarmResultTypeDef",
    "DeleteAutoSnapshotRequestRequestTypeDef",
    "DeleteAutoSnapshotResultTypeDef",
    "DeleteBucketAccessKeyRequestRequestTypeDef",
    "DeleteBucketAccessKeyResultTypeDef",
    "DeleteBucketRequestRequestTypeDef",
    "DeleteBucketResultTypeDef",
    "DeleteCertificateRequestRequestTypeDef",
    "DeleteCertificateResultTypeDef",
    "DeleteContactMethodRequestRequestTypeDef",
    "DeleteContactMethodResultTypeDef",
    "DeleteContainerImageRequestRequestTypeDef",
    "DeleteContainerServiceRequestRequestTypeDef",
    "DeleteDiskRequestRequestTypeDef",
    "DeleteDiskResultTypeDef",
    "DeleteDiskSnapshotRequestRequestTypeDef",
    "DeleteDiskSnapshotResultTypeDef",
    "DeleteDistributionRequestRequestTypeDef",
    "DeleteDistributionResultTypeDef",
    "DeleteDomainEntryRequestRequestTypeDef",
    "DeleteDomainEntryResultTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteDomainResultTypeDef",
    "DeleteInstanceRequestRequestTypeDef",
    "DeleteInstanceResultTypeDef",
    "DeleteInstanceSnapshotRequestRequestTypeDef",
    "DeleteInstanceSnapshotResultTypeDef",
    "DeleteKeyPairRequestRequestTypeDef",
    "DeleteKeyPairResultTypeDef",
    "DeleteKnownHostKeysRequestRequestTypeDef",
    "DeleteKnownHostKeysResultTypeDef",
    "DeleteLoadBalancerRequestRequestTypeDef",
    "DeleteLoadBalancerResultTypeDef",
    "DeleteLoadBalancerTlsCertificateRequestRequestTypeDef",
    "DeleteLoadBalancerTlsCertificateResultTypeDef",
    "DeleteRelationalDatabaseRequestRequestTypeDef",
    "DeleteRelationalDatabaseResultTypeDef",
    "DeleteRelationalDatabaseSnapshotRequestRequestTypeDef",
    "DeleteRelationalDatabaseSnapshotResultTypeDef",
    "DestinationInfoTypeDef",
    "DetachCertificateFromDistributionRequestRequestTypeDef",
    "DetachCertificateFromDistributionResultTypeDef",
    "DetachDiskRequestRequestTypeDef",
    "DetachDiskResultTypeDef",
    "DetachInstancesFromLoadBalancerRequestRequestTypeDef",
    "DetachInstancesFromLoadBalancerResultTypeDef",
    "DetachStaticIpRequestRequestTypeDef",
    "DetachStaticIpResultTypeDef",
    "DisableAddOnRequestRequestTypeDef",
    "DisableAddOnResultTypeDef",
    "DiskInfoTypeDef",
    "DiskMapTypeDef",
    "DiskSnapshotInfoTypeDef",
    "DiskSnapshotTypeDef",
    "DiskTypeDef",
    "DistributionBundleTypeDef",
    "DomainEntryTypeDef",
    "DomainTypeDef",
    "DomainValidationRecordTypeDef",
    "DownloadDefaultKeyPairResultTypeDef",
    "EnableAddOnRequestRequestTypeDef",
    "EnableAddOnResultTypeDef",
    "EndpointRequestTypeDef",
    "ExportSnapshotRecordSourceInfoTypeDef",
    "ExportSnapshotRecordTypeDef",
    "ExportSnapshotRequestRequestTypeDef",
    "ExportSnapshotResultTypeDef",
    "GetActiveNamesRequestRequestTypeDef",
    "GetActiveNamesResultTypeDef",
    "GetAlarmsRequestRequestTypeDef",
    "GetAlarmsResultTypeDef",
    "GetAutoSnapshotsRequestRequestTypeDef",
    "GetAutoSnapshotsResultTypeDef",
    "GetBlueprintsRequestRequestTypeDef",
    "GetBlueprintsResultTypeDef",
    "GetBucketAccessKeysRequestRequestTypeDef",
    "GetBucketAccessKeysResultTypeDef",
    "GetBucketBundlesRequestRequestTypeDef",
    "GetBucketBundlesResultTypeDef",
    "GetBucketMetricDataRequestRequestTypeDef",
    "GetBucketMetricDataResultTypeDef",
    "GetBucketsRequestRequestTypeDef",
    "GetBucketsResultTypeDef",
    "GetBundlesRequestRequestTypeDef",
    "GetBundlesResultTypeDef",
    "GetCertificatesRequestRequestTypeDef",
    "GetCertificatesResultTypeDef",
    "GetCloudFormationStackRecordsRequestRequestTypeDef",
    "GetCloudFormationStackRecordsResultTypeDef",
    "GetContactMethodsRequestRequestTypeDef",
    "GetContactMethodsResultTypeDef",
    "GetContainerAPIMetadataResultTypeDef",
    "GetContainerImagesRequestRequestTypeDef",
    "GetContainerImagesResultTypeDef",
    "GetContainerLogRequestRequestTypeDef",
    "GetContainerLogResultTypeDef",
    "GetContainerServiceDeploymentsRequestRequestTypeDef",
    "GetContainerServiceDeploymentsResultTypeDef",
    "GetContainerServiceMetricDataRequestRequestTypeDef",
    "GetContainerServiceMetricDataResultTypeDef",
    "GetContainerServicePowersResultTypeDef",
    "GetContainerServicesRequestRequestTypeDef",
    "GetDiskRequestRequestTypeDef",
    "GetDiskResultTypeDef",
    "GetDiskSnapshotRequestRequestTypeDef",
    "GetDiskSnapshotResultTypeDef",
    "GetDiskSnapshotsRequestRequestTypeDef",
    "GetDiskSnapshotsResultTypeDef",
    "GetDisksRequestRequestTypeDef",
    "GetDisksResultTypeDef",
    "GetDistributionBundlesResultTypeDef",
    "GetDistributionLatestCacheResetRequestRequestTypeDef",
    "GetDistributionLatestCacheResetResultTypeDef",
    "GetDistributionMetricDataRequestRequestTypeDef",
    "GetDistributionMetricDataResultTypeDef",
    "GetDistributionsRequestRequestTypeDef",
    "GetDistributionsResultTypeDef",
    "GetDomainRequestRequestTypeDef",
    "GetDomainResultTypeDef",
    "GetDomainsRequestRequestTypeDef",
    "GetDomainsResultTypeDef",
    "GetExportSnapshotRecordsRequestRequestTypeDef",
    "GetExportSnapshotRecordsResultTypeDef",
    "GetInstanceAccessDetailsRequestRequestTypeDef",
    "GetInstanceAccessDetailsResultTypeDef",
    "GetInstanceMetricDataRequestRequestTypeDef",
    "GetInstanceMetricDataResultTypeDef",
    "GetInstancePortStatesRequestRequestTypeDef",
    "GetInstancePortStatesResultTypeDef",
    "GetInstanceRequestRequestTypeDef",
    "GetInstanceResultTypeDef",
    "GetInstanceSnapshotRequestRequestTypeDef",
    "GetInstanceSnapshotResultTypeDef",
    "GetInstanceSnapshotsRequestRequestTypeDef",
    "GetInstanceSnapshotsResultTypeDef",
    "GetInstanceStateRequestRequestTypeDef",
    "GetInstanceStateResultTypeDef",
    "GetInstancesRequestRequestTypeDef",
    "GetInstancesResultTypeDef",
    "GetKeyPairRequestRequestTypeDef",
    "GetKeyPairResultTypeDef",
    "GetKeyPairsRequestRequestTypeDef",
    "GetKeyPairsResultTypeDef",
    "GetLoadBalancerMetricDataRequestRequestTypeDef",
    "GetLoadBalancerMetricDataResultTypeDef",
    "GetLoadBalancerRequestRequestTypeDef",
    "GetLoadBalancerResultTypeDef",
    "GetLoadBalancerTlsCertificatesRequestRequestTypeDef",
    "GetLoadBalancerTlsCertificatesResultTypeDef",
    "GetLoadBalancersRequestRequestTypeDef",
    "GetLoadBalancersResultTypeDef",
    "GetOperationRequestRequestTypeDef",
    "GetOperationResultTypeDef",
    "GetOperationsForResourceRequestRequestTypeDef",
    "GetOperationsForResourceResultTypeDef",
    "GetOperationsRequestRequestTypeDef",
    "GetOperationsResultTypeDef",
    "GetRegionsRequestRequestTypeDef",
    "GetRegionsResultTypeDef",
    "GetRelationalDatabaseBlueprintsRequestRequestTypeDef",
    "GetRelationalDatabaseBlueprintsResultTypeDef",
    "GetRelationalDatabaseBundlesRequestRequestTypeDef",
    "GetRelationalDatabaseBundlesResultTypeDef",
    "GetRelationalDatabaseEventsRequestRequestTypeDef",
    "GetRelationalDatabaseEventsResultTypeDef",
    "GetRelationalDatabaseLogEventsRequestRequestTypeDef",
    "GetRelationalDatabaseLogEventsResultTypeDef",
    "GetRelationalDatabaseLogStreamsRequestRequestTypeDef",
    "GetRelationalDatabaseLogStreamsResultTypeDef",
    "GetRelationalDatabaseMasterUserPasswordRequestRequestTypeDef",
    "GetRelationalDatabaseMasterUserPasswordResultTypeDef",
    "GetRelationalDatabaseMetricDataRequestRequestTypeDef",
    "GetRelationalDatabaseMetricDataResultTypeDef",
    "GetRelationalDatabaseParametersRequestRequestTypeDef",
    "GetRelationalDatabaseParametersResultTypeDef",
    "GetRelationalDatabaseRequestRequestTypeDef",
    "GetRelationalDatabaseResultTypeDef",
    "GetRelationalDatabaseSnapshotRequestRequestTypeDef",
    "GetRelationalDatabaseSnapshotResultTypeDef",
    "GetRelationalDatabaseSnapshotsRequestRequestTypeDef",
    "GetRelationalDatabaseSnapshotsResultTypeDef",
    "GetRelationalDatabasesRequestRequestTypeDef",
    "GetRelationalDatabasesResultTypeDef",
    "GetStaticIpRequestRequestTypeDef",
    "GetStaticIpResultTypeDef",
    "GetStaticIpsRequestRequestTypeDef",
    "GetStaticIpsResultTypeDef",
    "HeaderObjectTypeDef",
    "HostKeyAttributesTypeDef",
    "ImportKeyPairRequestRequestTypeDef",
    "ImportKeyPairResultTypeDef",
    "InputOriginTypeDef",
    "InstanceAccessDetailsTypeDef",
    "InstanceEntryTypeDef",
    "InstanceHardwareTypeDef",
    "InstanceHealthSummaryTypeDef",
    "InstanceNetworkingTypeDef",
    "InstancePortInfoTypeDef",
    "InstancePortStateTypeDef",
    "InstanceSnapshotInfoTypeDef",
    "InstanceSnapshotTypeDef",
    "InstanceStateTypeDef",
    "InstanceTypeDef",
    "IsVpcPeeredResultTypeDef",
    "KeyPairTypeDef",
    "LightsailDistributionTypeDef",
    "LoadBalancerTlsCertificateDomainValidationOptionTypeDef",
    "LoadBalancerTlsCertificateDomainValidationRecordTypeDef",
    "LoadBalancerTlsCertificateRenewalSummaryTypeDef",
    "LoadBalancerTlsCertificateSummaryTypeDef",
    "LoadBalancerTlsCertificateTypeDef",
    "LoadBalancerTypeDef",
    "LogEventTypeDef",
    "MetricDatapointTypeDef",
    "MonitoredResourceInfoTypeDef",
    "MonthlyTransferTypeDef",
    "OpenInstancePublicPortsRequestRequestTypeDef",
    "OpenInstancePublicPortsResultTypeDef",
    "OperationTypeDef",
    "OriginTypeDef",
    "PaginatorConfigTypeDef",
    "PasswordDataTypeDef",
    "PeerVpcResultTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingModifiedRelationalDatabaseValuesTypeDef",
    "PortInfoTypeDef",
    "PutAlarmRequestRequestTypeDef",
    "PutAlarmResultTypeDef",
    "PutInstancePublicPortsRequestRequestTypeDef",
    "PutInstancePublicPortsResultTypeDef",
    "QueryStringObjectTypeDef",
    "RebootInstanceRequestRequestTypeDef",
    "RebootInstanceResultTypeDef",
    "RebootRelationalDatabaseRequestRequestTypeDef",
    "RebootRelationalDatabaseResultTypeDef",
    "RegionTypeDef",
    "RegisterContainerImageRequestRequestTypeDef",
    "RegisterContainerImageResultTypeDef",
    "RelationalDatabaseBlueprintTypeDef",
    "RelationalDatabaseBundleTypeDef",
    "RelationalDatabaseEndpointTypeDef",
    "RelationalDatabaseEventTypeDef",
    "RelationalDatabaseHardwareTypeDef",
    "RelationalDatabaseParameterTypeDef",
    "RelationalDatabaseSnapshotTypeDef",
    "RelationalDatabaseTypeDef",
    "ReleaseStaticIpRequestRequestTypeDef",
    "ReleaseStaticIpResultTypeDef",
    "RenewalSummaryTypeDef",
    "ResetDistributionCacheRequestRequestTypeDef",
    "ResetDistributionCacheResultTypeDef",
    "ResourceLocationTypeDef",
    "ResourceReceivingAccessTypeDef",
    "ResourceRecordTypeDef",
    "ResponseMetadataTypeDef",
    "SendContactMethodVerificationRequestRequestTypeDef",
    "SendContactMethodVerificationResultTypeDef",
    "SetIpAddressTypeRequestRequestTypeDef",
    "SetIpAddressTypeResultTypeDef",
    "SetResourceAccessForBucketRequestRequestTypeDef",
    "SetResourceAccessForBucketResultTypeDef",
    "StartInstanceRequestRequestTypeDef",
    "StartInstanceResultTypeDef",
    "StartRelationalDatabaseRequestRequestTypeDef",
    "StartRelationalDatabaseResultTypeDef",
    "StaticIpTypeDef",
    "StopInstanceRequestRequestTypeDef",
    "StopInstanceResultTypeDef",
    "StopRelationalDatabaseRequestRequestTypeDef",
    "StopRelationalDatabaseResultTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagResourceResultTypeDef",
    "TagTypeDef",
    "TestAlarmRequestRequestTypeDef",
    "TestAlarmResultTypeDef",
    "UnpeerVpcResultTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UntagResourceResultTypeDef",
    "UpdateBucketBundleRequestRequestTypeDef",
    "UpdateBucketBundleResultTypeDef",
    "UpdateBucketRequestRequestTypeDef",
    "UpdateBucketResultTypeDef",
    "UpdateContainerServiceRequestRequestTypeDef",
    "UpdateContainerServiceResultTypeDef",
    "UpdateDistributionBundleRequestRequestTypeDef",
    "UpdateDistributionBundleResultTypeDef",
    "UpdateDistributionRequestRequestTypeDef",
    "UpdateDistributionResultTypeDef",
    "UpdateDomainEntryRequestRequestTypeDef",
    "UpdateDomainEntryResultTypeDef",
    "UpdateLoadBalancerAttributeRequestRequestTypeDef",
    "UpdateLoadBalancerAttributeResultTypeDef",
    "UpdateRelationalDatabaseParametersRequestRequestTypeDef",
    "UpdateRelationalDatabaseParametersResultTypeDef",
    "UpdateRelationalDatabaseRequestRequestTypeDef",
    "UpdateRelationalDatabaseResultTypeDef",
)

AccessKeyLastUsedTypeDef = TypedDict(
    "AccessKeyLastUsedTypeDef",
    {
        "lastUsedDate": NotRequired[datetime],
        "region": NotRequired[str],
        "serviceName": NotRequired[str],
    },
)

AccessKeyTypeDef = TypedDict(
    "AccessKeyTypeDef",
    {
        "accessKeyId": NotRequired[str],
        "secretAccessKey": NotRequired[str],
        "status": NotRequired[StatusTypeType],
        "createdAt": NotRequired[datetime],
        "lastUsed": NotRequired["AccessKeyLastUsedTypeDef"],
    },
)

AccessRulesTypeDef = TypedDict(
    "AccessRulesTypeDef",
    {
        "getObject": NotRequired[AccessTypeType],
        "allowPublicOverrides": NotRequired[bool],
    },
)

AddOnRequestTypeDef = TypedDict(
    "AddOnRequestTypeDef",
    {
        "addOnType": Literal["AutoSnapshot"],
        "autoSnapshotAddOnRequest": NotRequired["AutoSnapshotAddOnRequestTypeDef"],
    },
)

AddOnTypeDef = TypedDict(
    "AddOnTypeDef",
    {
        "name": NotRequired[str],
        "status": NotRequired[str],
        "snapshotTimeOfDay": NotRequired[str],
        "nextSnapshotTimeOfDay": NotRequired[str],
    },
)

AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired["ResourceLocationTypeDef"],
        "resourceType": NotRequired[ResourceTypeType],
        "supportCode": NotRequired[str],
        "monitoredResourceInfo": NotRequired["MonitoredResourceInfoTypeDef"],
        "comparisonOperator": NotRequired[ComparisonOperatorType],
        "evaluationPeriods": NotRequired[int],
        "period": NotRequired[int],
        "threshold": NotRequired[float],
        "datapointsToAlarm": NotRequired[int],
        "treatMissingData": NotRequired[TreatMissingDataType],
        "statistic": NotRequired[MetricStatisticType],
        "metricName": NotRequired[MetricNameType],
        "state": NotRequired[AlarmStateType],
        "unit": NotRequired[MetricUnitType],
        "contactProtocols": NotRequired[List[ContactProtocolType]],
        "notificationTriggers": NotRequired[List[AlarmStateType]],
        "notificationEnabled": NotRequired[bool],
    },
)

AllocateStaticIpRequestRequestTypeDef = TypedDict(
    "AllocateStaticIpRequestRequestTypeDef",
    {
        "staticIpName": str,
    },
)

AllocateStaticIpResultTypeDef = TypedDict(
    "AllocateStaticIpResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachCertificateToDistributionRequestRequestTypeDef = TypedDict(
    "AttachCertificateToDistributionRequestRequestTypeDef",
    {
        "distributionName": str,
        "certificateName": str,
    },
)

AttachCertificateToDistributionResultTypeDef = TypedDict(
    "AttachCertificateToDistributionResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachDiskRequestRequestTypeDef = TypedDict(
    "AttachDiskRequestRequestTypeDef",
    {
        "diskName": str,
        "instanceName": str,
        "diskPath": str,
    },
)

AttachDiskResultTypeDef = TypedDict(
    "AttachDiskResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachInstancesToLoadBalancerRequestRequestTypeDef = TypedDict(
    "AttachInstancesToLoadBalancerRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "instanceNames": Sequence[str],
    },
)

AttachInstancesToLoadBalancerResultTypeDef = TypedDict(
    "AttachInstancesToLoadBalancerResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachLoadBalancerTlsCertificateRequestRequestTypeDef = TypedDict(
    "AttachLoadBalancerTlsCertificateRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "certificateName": str,
    },
)

AttachLoadBalancerTlsCertificateResultTypeDef = TypedDict(
    "AttachLoadBalancerTlsCertificateResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachStaticIpRequestRequestTypeDef = TypedDict(
    "AttachStaticIpRequestRequestTypeDef",
    {
        "staticIpName": str,
        "instanceName": str,
    },
)

AttachStaticIpResultTypeDef = TypedDict(
    "AttachStaticIpResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachedDiskTypeDef = TypedDict(
    "AttachedDiskTypeDef",
    {
        "path": NotRequired[str],
        "sizeInGb": NotRequired[int],
    },
)

AutoSnapshotAddOnRequestTypeDef = TypedDict(
    "AutoSnapshotAddOnRequestTypeDef",
    {
        "snapshotTimeOfDay": NotRequired[str],
    },
)

AutoSnapshotDetailsTypeDef = TypedDict(
    "AutoSnapshotDetailsTypeDef",
    {
        "date": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "status": NotRequired[AutoSnapshotStatusType],
        "fromAttachedDisks": NotRequired[List["AttachedDiskTypeDef"]],
    },
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "zoneName": NotRequired[str],
        "state": NotRequired[str],
    },
)

BlueprintTypeDef = TypedDict(
    "BlueprintTypeDef",
    {
        "blueprintId": NotRequired[str],
        "name": NotRequired[str],
        "group": NotRequired[str],
        "type": NotRequired[BlueprintTypeType],
        "description": NotRequired[str],
        "isActive": NotRequired[bool],
        "minPower": NotRequired[int],
        "version": NotRequired[str],
        "versionCode": NotRequired[str],
        "productUrl": NotRequired[str],
        "licenseUrl": NotRequired[str],
        "platform": NotRequired[InstancePlatformType],
    },
)

BucketAccessLogConfigTypeDef = TypedDict(
    "BucketAccessLogConfigTypeDef",
    {
        "enabled": bool,
        "destination": NotRequired[str],
        "prefix": NotRequired[str],
    },
)

BucketBundleTypeDef = TypedDict(
    "BucketBundleTypeDef",
    {
        "bundleId": NotRequired[str],
        "name": NotRequired[str],
        "price": NotRequired[float],
        "storagePerMonthInGb": NotRequired[int],
        "transferPerMonthInGb": NotRequired[int],
        "isActive": NotRequired[bool],
    },
)

BucketStateTypeDef = TypedDict(
    "BucketStateTypeDef",
    {
        "code": NotRequired[str],
        "message": NotRequired[str],
    },
)

BucketTypeDef = TypedDict(
    "BucketTypeDef",
    {
        "resourceType": NotRequired[str],
        "accessRules": NotRequired["AccessRulesTypeDef"],
        "arn": NotRequired[str],
        "bundleId": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "url": NotRequired[str],
        "location": NotRequired["ResourceLocationTypeDef"],
        "name": NotRequired[str],
        "supportCode": NotRequired[str],
        "tags": NotRequired[List["TagTypeDef"]],
        "objectVersioning": NotRequired[str],
        "ableToUpdateBundle": NotRequired[bool],
        "readonlyAccessAccounts": NotRequired[List[str]],
        "resourcesReceivingAccess": NotRequired[List["ResourceReceivingAccessTypeDef"]],
        "state": NotRequired["BucketStateTypeDef"],
        "accessLogConfig": NotRequired["BucketAccessLogConfigTypeDef"],
    },
)

BundleTypeDef = TypedDict(
    "BundleTypeDef",
    {
        "price": NotRequired[float],
        "cpuCount": NotRequired[int],
        "diskSizeInGb": NotRequired[int],
        "bundleId": NotRequired[str],
        "instanceType": NotRequired[str],
        "isActive": NotRequired[bool],
        "name": NotRequired[str],
        "power": NotRequired[int],
        "ramSizeInGb": NotRequired[float],
        "transferPerMonthInGb": NotRequired[int],
        "supportedPlatforms": NotRequired[List[InstancePlatformType]],
    },
)

CacheBehaviorPerPathTypeDef = TypedDict(
    "CacheBehaviorPerPathTypeDef",
    {
        "path": NotRequired[str],
        "behavior": NotRequired[BehaviorEnumType],
    },
)

CacheBehaviorTypeDef = TypedDict(
    "CacheBehaviorTypeDef",
    {
        "behavior": NotRequired[BehaviorEnumType],
    },
)

CacheSettingsTypeDef = TypedDict(
    "CacheSettingsTypeDef",
    {
        "defaultTTL": NotRequired[int],
        "minimumTTL": NotRequired[int],
        "maximumTTL": NotRequired[int],
        "allowedHTTPMethods": NotRequired[str],
        "cachedHTTPMethods": NotRequired[str],
        "forwardedCookies": NotRequired["CookieObjectTypeDef"],
        "forwardedHeaders": NotRequired["HeaderObjectTypeDef"],
        "forwardedQueryStrings": NotRequired["QueryStringObjectTypeDef"],
    },
)

CertificateSummaryTypeDef = TypedDict(
    "CertificateSummaryTypeDef",
    {
        "certificateArn": NotRequired[str],
        "certificateName": NotRequired[str],
        "domainName": NotRequired[str],
        "certificateDetail": NotRequired["CertificateTypeDef"],
        "tags": NotRequired[List["TagTypeDef"]],
    },
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "domainName": NotRequired[str],
        "status": NotRequired[CertificateStatusType],
        "serialNumber": NotRequired[str],
        "subjectAlternativeNames": NotRequired[List[str]],
        "domainValidationRecords": NotRequired[List["DomainValidationRecordTypeDef"]],
        "requestFailureReason": NotRequired[str],
        "inUseResourceCount": NotRequired[int],
        "keyAlgorithm": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "issuedAt": NotRequired[datetime],
        "issuerCA": NotRequired[str],
        "notBefore": NotRequired[datetime],
        "notAfter": NotRequired[datetime],
        "eligibleToRenew": NotRequired[str],
        "renewalSummary": NotRequired["RenewalSummaryTypeDef"],
        "revokedAt": NotRequired[datetime],
        "revocationReason": NotRequired[str],
        "tags": NotRequired[List["TagTypeDef"]],
        "supportCode": NotRequired[str],
    },
)

CloseInstancePublicPortsRequestRequestTypeDef = TypedDict(
    "CloseInstancePublicPortsRequestRequestTypeDef",
    {
        "portInfo": "PortInfoTypeDef",
        "instanceName": str,
    },
)

CloseInstancePublicPortsResultTypeDef = TypedDict(
    "CloseInstancePublicPortsResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CloudFormationStackRecordSourceInfoTypeDef = TypedDict(
    "CloudFormationStackRecordSourceInfoTypeDef",
    {
        "resourceType": NotRequired[Literal["ExportSnapshotRecord"]],
        "name": NotRequired[str],
        "arn": NotRequired[str],
    },
)

CloudFormationStackRecordTypeDef = TypedDict(
    "CloudFormationStackRecordTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired["ResourceLocationTypeDef"],
        "resourceType": NotRequired[ResourceTypeType],
        "state": NotRequired[RecordStateType],
        "sourceInfo": NotRequired[List["CloudFormationStackRecordSourceInfoTypeDef"]],
        "destinationInfo": NotRequired["DestinationInfoTypeDef"],
    },
)

ContactMethodTypeDef = TypedDict(
    "ContactMethodTypeDef",
    {
        "contactEndpoint": NotRequired[str],
        "status": NotRequired[ContactMethodStatusType],
        "protocol": NotRequired[ContactProtocolType],
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired["ResourceLocationTypeDef"],
        "resourceType": NotRequired[ResourceTypeType],
        "supportCode": NotRequired[str],
    },
)

ContainerImageTypeDef = TypedDict(
    "ContainerImageTypeDef",
    {
        "image": NotRequired[str],
        "digest": NotRequired[str],
        "createdAt": NotRequired[datetime],
    },
)

ContainerServiceDeploymentRequestTypeDef = TypedDict(
    "ContainerServiceDeploymentRequestTypeDef",
    {
        "containers": NotRequired[Mapping[str, "ContainerTypeDef"]],
        "publicEndpoint": NotRequired["EndpointRequestTypeDef"],
    },
)

ContainerServiceDeploymentTypeDef = TypedDict(
    "ContainerServiceDeploymentTypeDef",
    {
        "version": NotRequired[int],
        "state": NotRequired[ContainerServiceDeploymentStateType],
        "containers": NotRequired[Dict[str, "ContainerTypeDef"]],
        "publicEndpoint": NotRequired["ContainerServiceEndpointTypeDef"],
        "createdAt": NotRequired[datetime],
    },
)

ContainerServiceEndpointTypeDef = TypedDict(
    "ContainerServiceEndpointTypeDef",
    {
        "containerName": NotRequired[str],
        "containerPort": NotRequired[int],
        "healthCheck": NotRequired["ContainerServiceHealthCheckConfigTypeDef"],
    },
)

ContainerServiceHealthCheckConfigTypeDef = TypedDict(
    "ContainerServiceHealthCheckConfigTypeDef",
    {
        "healthyThreshold": NotRequired[int],
        "unhealthyThreshold": NotRequired[int],
        "timeoutSeconds": NotRequired[int],
        "intervalSeconds": NotRequired[int],
        "path": NotRequired[str],
        "successCodes": NotRequired[str],
    },
)

ContainerServiceLogEventTypeDef = TypedDict(
    "ContainerServiceLogEventTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "message": NotRequired[str],
    },
)

ContainerServicePowerTypeDef = TypedDict(
    "ContainerServicePowerTypeDef",
    {
        "powerId": NotRequired[str],
        "price": NotRequired[float],
        "cpuCount": NotRequired[float],
        "ramSizeInGb": NotRequired[float],
        "name": NotRequired[str],
        "isActive": NotRequired[bool],
    },
)

ContainerServiceRegistryLoginTypeDef = TypedDict(
    "ContainerServiceRegistryLoginTypeDef",
    {
        "username": NotRequired[str],
        "password": NotRequired[str],
        "expiresAt": NotRequired[datetime],
        "registry": NotRequired[str],
    },
)

ContainerServiceStateDetailTypeDef = TypedDict(
    "ContainerServiceStateDetailTypeDef",
    {
        "code": NotRequired[ContainerServiceStateDetailCodeType],
        "message": NotRequired[str],
    },
)

ContainerServiceTypeDef = TypedDict(
    "ContainerServiceTypeDef",
    {
        "containerServiceName": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired["ResourceLocationTypeDef"],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List["TagTypeDef"]],
        "power": NotRequired[ContainerServicePowerNameType],
        "powerId": NotRequired[str],
        "state": NotRequired[ContainerServiceStateType],
        "stateDetail": NotRequired["ContainerServiceStateDetailTypeDef"],
        "scale": NotRequired[int],
        "currentDeployment": NotRequired["ContainerServiceDeploymentTypeDef"],
        "nextDeployment": NotRequired["ContainerServiceDeploymentTypeDef"],
        "isDisabled": NotRequired[bool],
        "principalArn": NotRequired[str],
        "privateDomainName": NotRequired[str],
        "publicDomainNames": NotRequired[Dict[str, List[str]]],
        "url": NotRequired[str],
    },
)

ContainerServicesListResultTypeDef = TypedDict(
    "ContainerServicesListResultTypeDef",
    {
        "containerServices": List["ContainerServiceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "image": NotRequired[str],
        "command": NotRequired[Sequence[str]],
        "environment": NotRequired[Mapping[str, str]],
        "ports": NotRequired[Mapping[str, ContainerServiceProtocolType]],
    },
)

CookieObjectTypeDef = TypedDict(
    "CookieObjectTypeDef",
    {
        "option": NotRequired[ForwardValuesType],
        "cookiesAllowList": NotRequired[Sequence[str]],
    },
)

CopySnapshotRequestRequestTypeDef = TypedDict(
    "CopySnapshotRequestRequestTypeDef",
    {
        "targetSnapshotName": str,
        "sourceRegion": RegionNameType,
        "sourceSnapshotName": NotRequired[str],
        "sourceResourceName": NotRequired[str],
        "restoreDate": NotRequired[str],
        "useLatestRestorableAutoSnapshot": NotRequired[bool],
    },
)

CopySnapshotResultTypeDef = TypedDict(
    "CopySnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBucketAccessKeyRequestRequestTypeDef = TypedDict(
    "CreateBucketAccessKeyRequestRequestTypeDef",
    {
        "bucketName": str,
    },
)

CreateBucketAccessKeyResultTypeDef = TypedDict(
    "CreateBucketAccessKeyResultTypeDef",
    {
        "accessKey": "AccessKeyTypeDef",
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBucketRequestRequestTypeDef = TypedDict(
    "CreateBucketRequestRequestTypeDef",
    {
        "bucketName": str,
        "bundleId": str,
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "enableObjectVersioning": NotRequired[bool],
    },
)

CreateBucketResultTypeDef = TypedDict(
    "CreateBucketResultTypeDef",
    {
        "bucket": "BucketTypeDef",
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCertificateRequestRequestTypeDef = TypedDict(
    "CreateCertificateRequestRequestTypeDef",
    {
        "certificateName": str,
        "domainName": str,
        "subjectAlternativeNames": NotRequired[Sequence[str]],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateCertificateResultTypeDef = TypedDict(
    "CreateCertificateResultTypeDef",
    {
        "certificate": "CertificateSummaryTypeDef",
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCloudFormationStackRequestRequestTypeDef = TypedDict(
    "CreateCloudFormationStackRequestRequestTypeDef",
    {
        "instances": Sequence["InstanceEntryTypeDef"],
    },
)

CreateCloudFormationStackResultTypeDef = TypedDict(
    "CreateCloudFormationStackResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateContactMethodRequestRequestTypeDef = TypedDict(
    "CreateContactMethodRequestRequestTypeDef",
    {
        "protocol": ContactProtocolType,
        "contactEndpoint": str,
    },
)

CreateContactMethodResultTypeDef = TypedDict(
    "CreateContactMethodResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateContainerServiceDeploymentRequestRequestTypeDef = TypedDict(
    "CreateContainerServiceDeploymentRequestRequestTypeDef",
    {
        "serviceName": str,
        "containers": NotRequired[Mapping[str, "ContainerTypeDef"]],
        "publicEndpoint": NotRequired["EndpointRequestTypeDef"],
    },
)

CreateContainerServiceDeploymentResultTypeDef = TypedDict(
    "CreateContainerServiceDeploymentResultTypeDef",
    {
        "containerService": "ContainerServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateContainerServiceRegistryLoginResultTypeDef = TypedDict(
    "CreateContainerServiceRegistryLoginResultTypeDef",
    {
        "registryLogin": "ContainerServiceRegistryLoginTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateContainerServiceRequestRequestTypeDef = TypedDict(
    "CreateContainerServiceRequestRequestTypeDef",
    {
        "serviceName": str,
        "power": ContainerServicePowerNameType,
        "scale": int,
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "publicDomainNames": NotRequired[Mapping[str, Sequence[str]]],
        "deployment": NotRequired["ContainerServiceDeploymentRequestTypeDef"],
    },
)

CreateContainerServiceResultTypeDef = TypedDict(
    "CreateContainerServiceResultTypeDef",
    {
        "containerService": "ContainerServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDiskFromSnapshotRequestRequestTypeDef = TypedDict(
    "CreateDiskFromSnapshotRequestRequestTypeDef",
    {
        "diskName": str,
        "availabilityZone": str,
        "sizeInGb": int,
        "diskSnapshotName": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "addOns": NotRequired[Sequence["AddOnRequestTypeDef"]],
        "sourceDiskName": NotRequired[str],
        "restoreDate": NotRequired[str],
        "useLatestRestorableAutoSnapshot": NotRequired[bool],
    },
)

CreateDiskFromSnapshotResultTypeDef = TypedDict(
    "CreateDiskFromSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDiskRequestRequestTypeDef = TypedDict(
    "CreateDiskRequestRequestTypeDef",
    {
        "diskName": str,
        "availabilityZone": str,
        "sizeInGb": int,
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "addOns": NotRequired[Sequence["AddOnRequestTypeDef"]],
    },
)

CreateDiskResultTypeDef = TypedDict(
    "CreateDiskResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDiskSnapshotRequestRequestTypeDef = TypedDict(
    "CreateDiskSnapshotRequestRequestTypeDef",
    {
        "diskSnapshotName": str,
        "diskName": NotRequired[str],
        "instanceName": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDiskSnapshotResultTypeDef = TypedDict(
    "CreateDiskSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDistributionRequestRequestTypeDef = TypedDict(
    "CreateDistributionRequestRequestTypeDef",
    {
        "distributionName": str,
        "origin": "InputOriginTypeDef",
        "defaultCacheBehavior": "CacheBehaviorTypeDef",
        "bundleId": str,
        "cacheBehaviorSettings": NotRequired["CacheSettingsTypeDef"],
        "cacheBehaviors": NotRequired[Sequence["CacheBehaviorPerPathTypeDef"]],
        "ipAddressType": NotRequired[IpAddressTypeType],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDistributionResultTypeDef = TypedDict(
    "CreateDistributionResultTypeDef",
    {
        "distribution": "LightsailDistributionTypeDef",
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDomainEntryRequestRequestTypeDef = TypedDict(
    "CreateDomainEntryRequestRequestTypeDef",
    {
        "domainName": str,
        "domainEntry": "DomainEntryTypeDef",
    },
)

CreateDomainEntryResultTypeDef = TypedDict(
    "CreateDomainEntryResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDomainRequestRequestTypeDef = TypedDict(
    "CreateDomainRequestRequestTypeDef",
    {
        "domainName": str,
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDomainResultTypeDef = TypedDict(
    "CreateDomainResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInstanceSnapshotRequestRequestTypeDef = TypedDict(
    "CreateInstanceSnapshotRequestRequestTypeDef",
    {
        "instanceSnapshotName": str,
        "instanceName": str,
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateInstanceSnapshotResultTypeDef = TypedDict(
    "CreateInstanceSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInstancesFromSnapshotRequestRequestTypeDef = TypedDict(
    "CreateInstancesFromSnapshotRequestRequestTypeDef",
    {
        "instanceNames": Sequence[str],
        "availabilityZone": str,
        "bundleId": str,
        "attachedDiskMapping": NotRequired[Mapping[str, Sequence["DiskMapTypeDef"]]],
        "instanceSnapshotName": NotRequired[str],
        "userData": NotRequired[str],
        "keyPairName": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "addOns": NotRequired[Sequence["AddOnRequestTypeDef"]],
        "ipAddressType": NotRequired[IpAddressTypeType],
        "sourceInstanceName": NotRequired[str],
        "restoreDate": NotRequired[str],
        "useLatestRestorableAutoSnapshot": NotRequired[bool],
    },
)

CreateInstancesFromSnapshotResultTypeDef = TypedDict(
    "CreateInstancesFromSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInstancesRequestRequestTypeDef = TypedDict(
    "CreateInstancesRequestRequestTypeDef",
    {
        "instanceNames": Sequence[str],
        "availabilityZone": str,
        "blueprintId": str,
        "bundleId": str,
        "customImageName": NotRequired[str],
        "userData": NotRequired[str],
        "keyPairName": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "addOns": NotRequired[Sequence["AddOnRequestTypeDef"]],
        "ipAddressType": NotRequired[IpAddressTypeType],
    },
)

CreateInstancesResultTypeDef = TypedDict(
    "CreateInstancesResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateKeyPairRequestRequestTypeDef = TypedDict(
    "CreateKeyPairRequestRequestTypeDef",
    {
        "keyPairName": str,
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateKeyPairResultTypeDef = TypedDict(
    "CreateKeyPairResultTypeDef",
    {
        "keyPair": "KeyPairTypeDef",
        "publicKeyBase64": str,
        "privateKeyBase64": str,
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLoadBalancerRequestRequestTypeDef = TypedDict(
    "CreateLoadBalancerRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "instancePort": int,
        "healthCheckPath": NotRequired[str],
        "certificateName": NotRequired[str],
        "certificateDomainName": NotRequired[str],
        "certificateAlternativeNames": NotRequired[Sequence[str]],
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "ipAddressType": NotRequired[IpAddressTypeType],
    },
)

CreateLoadBalancerResultTypeDef = TypedDict(
    "CreateLoadBalancerResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLoadBalancerTlsCertificateRequestRequestTypeDef = TypedDict(
    "CreateLoadBalancerTlsCertificateRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "certificateName": str,
        "certificateDomainName": str,
        "certificateAlternativeNames": NotRequired[Sequence[str]],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateLoadBalancerTlsCertificateResultTypeDef = TypedDict(
    "CreateLoadBalancerTlsCertificateResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRelationalDatabaseFromSnapshotRequestRequestTypeDef = TypedDict(
    "CreateRelationalDatabaseFromSnapshotRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "availabilityZone": NotRequired[str],
        "publiclyAccessible": NotRequired[bool],
        "relationalDatabaseSnapshotName": NotRequired[str],
        "relationalDatabaseBundleId": NotRequired[str],
        "sourceRelationalDatabaseName": NotRequired[str],
        "restoreTime": NotRequired[Union[datetime, str]],
        "useLatestRestorableTime": NotRequired[bool],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateRelationalDatabaseFromSnapshotResultTypeDef = TypedDict(
    "CreateRelationalDatabaseFromSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "CreateRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "relationalDatabaseBlueprintId": str,
        "relationalDatabaseBundleId": str,
        "masterDatabaseName": str,
        "masterUsername": str,
        "availabilityZone": NotRequired[str],
        "masterUserPassword": NotRequired[str],
        "preferredBackupWindow": NotRequired[str],
        "preferredMaintenanceWindow": NotRequired[str],
        "publiclyAccessible": NotRequired[bool],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateRelationalDatabaseResultTypeDef = TypedDict(
    "CreateRelationalDatabaseResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRelationalDatabaseSnapshotRequestRequestTypeDef = TypedDict(
    "CreateRelationalDatabaseSnapshotRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "relationalDatabaseSnapshotName": str,
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateRelationalDatabaseSnapshotResultTypeDef = TypedDict(
    "CreateRelationalDatabaseSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAlarmRequestRequestTypeDef = TypedDict(
    "DeleteAlarmRequestRequestTypeDef",
    {
        "alarmName": str,
    },
)

DeleteAlarmResultTypeDef = TypedDict(
    "DeleteAlarmResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAutoSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteAutoSnapshotRequestRequestTypeDef",
    {
        "resourceName": str,
        "date": str,
    },
)

DeleteAutoSnapshotResultTypeDef = TypedDict(
    "DeleteAutoSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBucketAccessKeyRequestRequestTypeDef = TypedDict(
    "DeleteBucketAccessKeyRequestRequestTypeDef",
    {
        "bucketName": str,
        "accessKeyId": str,
    },
)

DeleteBucketAccessKeyResultTypeDef = TypedDict(
    "DeleteBucketAccessKeyResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBucketRequestRequestTypeDef = TypedDict(
    "DeleteBucketRequestRequestTypeDef",
    {
        "bucketName": str,
        "forceDelete": NotRequired[bool],
    },
)

DeleteBucketResultTypeDef = TypedDict(
    "DeleteBucketResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCertificateRequestRequestTypeDef = TypedDict(
    "DeleteCertificateRequestRequestTypeDef",
    {
        "certificateName": str,
    },
)

DeleteCertificateResultTypeDef = TypedDict(
    "DeleteCertificateResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteContactMethodRequestRequestTypeDef = TypedDict(
    "DeleteContactMethodRequestRequestTypeDef",
    {
        "protocol": ContactProtocolType,
    },
)

DeleteContactMethodResultTypeDef = TypedDict(
    "DeleteContactMethodResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteContainerImageRequestRequestTypeDef = TypedDict(
    "DeleteContainerImageRequestRequestTypeDef",
    {
        "serviceName": str,
        "image": str,
    },
)

DeleteContainerServiceRequestRequestTypeDef = TypedDict(
    "DeleteContainerServiceRequestRequestTypeDef",
    {
        "serviceName": str,
    },
)

DeleteDiskRequestRequestTypeDef = TypedDict(
    "DeleteDiskRequestRequestTypeDef",
    {
        "diskName": str,
        "forceDeleteAddOns": NotRequired[bool],
    },
)

DeleteDiskResultTypeDef = TypedDict(
    "DeleteDiskResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDiskSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteDiskSnapshotRequestRequestTypeDef",
    {
        "diskSnapshotName": str,
    },
)

DeleteDiskSnapshotResultTypeDef = TypedDict(
    "DeleteDiskSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDistributionRequestRequestTypeDef = TypedDict(
    "DeleteDistributionRequestRequestTypeDef",
    {
        "distributionName": NotRequired[str],
    },
)

DeleteDistributionResultTypeDef = TypedDict(
    "DeleteDistributionResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDomainEntryRequestRequestTypeDef = TypedDict(
    "DeleteDomainEntryRequestRequestTypeDef",
    {
        "domainName": str,
        "domainEntry": "DomainEntryTypeDef",
    },
)

DeleteDomainEntryResultTypeDef = TypedDict(
    "DeleteDomainEntryResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "domainName": str,
    },
)

DeleteDomainResultTypeDef = TypedDict(
    "DeleteDomainResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInstanceRequestRequestTypeDef = TypedDict(
    "DeleteInstanceRequestRequestTypeDef",
    {
        "instanceName": str,
        "forceDeleteAddOns": NotRequired[bool],
    },
)

DeleteInstanceResultTypeDef = TypedDict(
    "DeleteInstanceResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInstanceSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteInstanceSnapshotRequestRequestTypeDef",
    {
        "instanceSnapshotName": str,
    },
)

DeleteInstanceSnapshotResultTypeDef = TypedDict(
    "DeleteInstanceSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteKeyPairRequestRequestTypeDef = TypedDict(
    "DeleteKeyPairRequestRequestTypeDef",
    {
        "keyPairName": str,
        "expectedFingerprint": NotRequired[str],
    },
)

DeleteKeyPairResultTypeDef = TypedDict(
    "DeleteKeyPairResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteKnownHostKeysRequestRequestTypeDef = TypedDict(
    "DeleteKnownHostKeysRequestRequestTypeDef",
    {
        "instanceName": str,
    },
)

DeleteKnownHostKeysResultTypeDef = TypedDict(
    "DeleteKnownHostKeysResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLoadBalancerRequestRequestTypeDef = TypedDict(
    "DeleteLoadBalancerRequestRequestTypeDef",
    {
        "loadBalancerName": str,
    },
)

DeleteLoadBalancerResultTypeDef = TypedDict(
    "DeleteLoadBalancerResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLoadBalancerTlsCertificateRequestRequestTypeDef = TypedDict(
    "DeleteLoadBalancerTlsCertificateRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "certificateName": str,
        "force": NotRequired[bool],
    },
)

DeleteLoadBalancerTlsCertificateResultTypeDef = TypedDict(
    "DeleteLoadBalancerTlsCertificateResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "DeleteRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "skipFinalSnapshot": NotRequired[bool],
        "finalRelationalDatabaseSnapshotName": NotRequired[str],
    },
)

DeleteRelationalDatabaseResultTypeDef = TypedDict(
    "DeleteRelationalDatabaseResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRelationalDatabaseSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteRelationalDatabaseSnapshotRequestRequestTypeDef",
    {
        "relationalDatabaseSnapshotName": str,
    },
)

DeleteRelationalDatabaseSnapshotResultTypeDef = TypedDict(
    "DeleteRelationalDatabaseSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationInfoTypeDef = TypedDict(
    "DestinationInfoTypeDef",
    {
        "id": NotRequired[str],
        "service": NotRequired[str],
    },
)

DetachCertificateFromDistributionRequestRequestTypeDef = TypedDict(
    "DetachCertificateFromDistributionRequestRequestTypeDef",
    {
        "distributionName": str,
    },
)

DetachCertificateFromDistributionResultTypeDef = TypedDict(
    "DetachCertificateFromDistributionResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachDiskRequestRequestTypeDef = TypedDict(
    "DetachDiskRequestRequestTypeDef",
    {
        "diskName": str,
    },
)

DetachDiskResultTypeDef = TypedDict(
    "DetachDiskResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachInstancesFromLoadBalancerRequestRequestTypeDef = TypedDict(
    "DetachInstancesFromLoadBalancerRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "instanceNames": Sequence[str],
    },
)

DetachInstancesFromLoadBalancerResultTypeDef = TypedDict(
    "DetachInstancesFromLoadBalancerResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachStaticIpRequestRequestTypeDef = TypedDict(
    "DetachStaticIpRequestRequestTypeDef",
    {
        "staticIpName": str,
    },
)

DetachStaticIpResultTypeDef = TypedDict(
    "DetachStaticIpResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableAddOnRequestRequestTypeDef = TypedDict(
    "DisableAddOnRequestRequestTypeDef",
    {
        "addOnType": Literal["AutoSnapshot"],
        "resourceName": str,
    },
)

DisableAddOnResultTypeDef = TypedDict(
    "DisableAddOnResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DiskInfoTypeDef = TypedDict(
    "DiskInfoTypeDef",
    {
        "name": NotRequired[str],
        "path": NotRequired[str],
        "sizeInGb": NotRequired[int],
        "isSystemDisk": NotRequired[bool],
    },
)

DiskMapTypeDef = TypedDict(
    "DiskMapTypeDef",
    {
        "originalDiskPath": NotRequired[str],
        "newDiskName": NotRequired[str],
    },
)

DiskSnapshotInfoTypeDef = TypedDict(
    "DiskSnapshotInfoTypeDef",
    {
        "sizeInGb": NotRequired[int],
    },
)

DiskSnapshotTypeDef = TypedDict(
    "DiskSnapshotTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired["ResourceLocationTypeDef"],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List["TagTypeDef"]],
        "sizeInGb": NotRequired[int],
        "state": NotRequired[DiskSnapshotStateType],
        "progress": NotRequired[str],
        "fromDiskName": NotRequired[str],
        "fromDiskArn": NotRequired[str],
        "fromInstanceName": NotRequired[str],
        "fromInstanceArn": NotRequired[str],
        "isFromAutoSnapshot": NotRequired[bool],
    },
)

DiskTypeDef = TypedDict(
    "DiskTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired["ResourceLocationTypeDef"],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List["TagTypeDef"]],
        "addOns": NotRequired[List["AddOnTypeDef"]],
        "sizeInGb": NotRequired[int],
        "isSystemDisk": NotRequired[bool],
        "iops": NotRequired[int],
        "path": NotRequired[str],
        "state": NotRequired[DiskStateType],
        "attachedTo": NotRequired[str],
        "isAttached": NotRequired[bool],
        "attachmentState": NotRequired[str],
        "gbInUse": NotRequired[int],
    },
)

DistributionBundleTypeDef = TypedDict(
    "DistributionBundleTypeDef",
    {
        "bundleId": NotRequired[str],
        "name": NotRequired[str],
        "price": NotRequired[float],
        "transferPerMonthInGb": NotRequired[int],
        "isActive": NotRequired[bool],
    },
)

DomainEntryTypeDef = TypedDict(
    "DomainEntryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "target": NotRequired[str],
        "isAlias": NotRequired[bool],
        "type": NotRequired[str],
        "options": NotRequired[Mapping[str, str]],
    },
)

DomainTypeDef = TypedDict(
    "DomainTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired["ResourceLocationTypeDef"],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List["TagTypeDef"]],
        "domainEntries": NotRequired[List["DomainEntryTypeDef"]],
    },
)

DomainValidationRecordTypeDef = TypedDict(
    "DomainValidationRecordTypeDef",
    {
        "domainName": NotRequired[str],
        "resourceRecord": NotRequired["ResourceRecordTypeDef"],
    },
)

DownloadDefaultKeyPairResultTypeDef = TypedDict(
    "DownloadDefaultKeyPairResultTypeDef",
    {
        "publicKeyBase64": str,
        "privateKeyBase64": str,
        "createdAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableAddOnRequestRequestTypeDef = TypedDict(
    "EnableAddOnRequestRequestTypeDef",
    {
        "resourceName": str,
        "addOnRequest": "AddOnRequestTypeDef",
    },
)

EnableAddOnResultTypeDef = TypedDict(
    "EnableAddOnResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointRequestTypeDef = TypedDict(
    "EndpointRequestTypeDef",
    {
        "containerName": str,
        "containerPort": int,
        "healthCheck": NotRequired["ContainerServiceHealthCheckConfigTypeDef"],
    },
)

ExportSnapshotRecordSourceInfoTypeDef = TypedDict(
    "ExportSnapshotRecordSourceInfoTypeDef",
    {
        "resourceType": NotRequired[ExportSnapshotRecordSourceTypeType],
        "createdAt": NotRequired[datetime],
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "fromResourceName": NotRequired[str],
        "fromResourceArn": NotRequired[str],
        "instanceSnapshotInfo": NotRequired["InstanceSnapshotInfoTypeDef"],
        "diskSnapshotInfo": NotRequired["DiskSnapshotInfoTypeDef"],
    },
)

ExportSnapshotRecordTypeDef = TypedDict(
    "ExportSnapshotRecordTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired["ResourceLocationTypeDef"],
        "resourceType": NotRequired[ResourceTypeType],
        "state": NotRequired[RecordStateType],
        "sourceInfo": NotRequired["ExportSnapshotRecordSourceInfoTypeDef"],
        "destinationInfo": NotRequired["DestinationInfoTypeDef"],
    },
)

ExportSnapshotRequestRequestTypeDef = TypedDict(
    "ExportSnapshotRequestRequestTypeDef",
    {
        "sourceSnapshotName": str,
    },
)

ExportSnapshotResultTypeDef = TypedDict(
    "ExportSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetActiveNamesRequestRequestTypeDef = TypedDict(
    "GetActiveNamesRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)

GetActiveNamesResultTypeDef = TypedDict(
    "GetActiveNamesResultTypeDef",
    {
        "activeNames": List[str],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAlarmsRequestRequestTypeDef = TypedDict(
    "GetAlarmsRequestRequestTypeDef",
    {
        "alarmName": NotRequired[str],
        "pageToken": NotRequired[str],
        "monitoredResourceName": NotRequired[str],
    },
)

GetAlarmsResultTypeDef = TypedDict(
    "GetAlarmsResultTypeDef",
    {
        "alarms": List["AlarmTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAutoSnapshotsRequestRequestTypeDef = TypedDict(
    "GetAutoSnapshotsRequestRequestTypeDef",
    {
        "resourceName": str,
    },
)

GetAutoSnapshotsResultTypeDef = TypedDict(
    "GetAutoSnapshotsResultTypeDef",
    {
        "resourceName": str,
        "resourceType": ResourceTypeType,
        "autoSnapshots": List["AutoSnapshotDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBlueprintsRequestRequestTypeDef = TypedDict(
    "GetBlueprintsRequestRequestTypeDef",
    {
        "includeInactive": NotRequired[bool],
        "pageToken": NotRequired[str],
    },
)

GetBlueprintsResultTypeDef = TypedDict(
    "GetBlueprintsResultTypeDef",
    {
        "blueprints": List["BlueprintTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketAccessKeysRequestRequestTypeDef = TypedDict(
    "GetBucketAccessKeysRequestRequestTypeDef",
    {
        "bucketName": str,
    },
)

GetBucketAccessKeysResultTypeDef = TypedDict(
    "GetBucketAccessKeysResultTypeDef",
    {
        "accessKeys": List["AccessKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketBundlesRequestRequestTypeDef = TypedDict(
    "GetBucketBundlesRequestRequestTypeDef",
    {
        "includeInactive": NotRequired[bool],
    },
)

GetBucketBundlesResultTypeDef = TypedDict(
    "GetBucketBundlesResultTypeDef",
    {
        "bundles": List["BucketBundleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketMetricDataRequestRequestTypeDef = TypedDict(
    "GetBucketMetricDataRequestRequestTypeDef",
    {
        "bucketName": str,
        "metricName": BucketMetricNameType,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "period": int,
        "statistics": Sequence[MetricStatisticType],
        "unit": MetricUnitType,
    },
)

GetBucketMetricDataResultTypeDef = TypedDict(
    "GetBucketMetricDataResultTypeDef",
    {
        "metricName": BucketMetricNameType,
        "metricData": List["MetricDatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketsRequestRequestTypeDef = TypedDict(
    "GetBucketsRequestRequestTypeDef",
    {
        "bucketName": NotRequired[str],
        "pageToken": NotRequired[str],
        "includeConnectedResources": NotRequired[bool],
    },
)

GetBucketsResultTypeDef = TypedDict(
    "GetBucketsResultTypeDef",
    {
        "buckets": List["BucketTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBundlesRequestRequestTypeDef = TypedDict(
    "GetBundlesRequestRequestTypeDef",
    {
        "includeInactive": NotRequired[bool],
        "pageToken": NotRequired[str],
    },
)

GetBundlesResultTypeDef = TypedDict(
    "GetBundlesResultTypeDef",
    {
        "bundles": List["BundleTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCertificatesRequestRequestTypeDef = TypedDict(
    "GetCertificatesRequestRequestTypeDef",
    {
        "certificateStatuses": NotRequired[Sequence[CertificateStatusType]],
        "includeCertificateDetails": NotRequired[bool],
        "certificateName": NotRequired[str],
    },
)

GetCertificatesResultTypeDef = TypedDict(
    "GetCertificatesResultTypeDef",
    {
        "certificates": List["CertificateSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCloudFormationStackRecordsRequestRequestTypeDef = TypedDict(
    "GetCloudFormationStackRecordsRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)

GetCloudFormationStackRecordsResultTypeDef = TypedDict(
    "GetCloudFormationStackRecordsResultTypeDef",
    {
        "cloudFormationStackRecords": List["CloudFormationStackRecordTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContactMethodsRequestRequestTypeDef = TypedDict(
    "GetContactMethodsRequestRequestTypeDef",
    {
        "protocols": NotRequired[Sequence[ContactProtocolType]],
    },
)

GetContactMethodsResultTypeDef = TypedDict(
    "GetContactMethodsResultTypeDef",
    {
        "contactMethods": List["ContactMethodTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerAPIMetadataResultTypeDef = TypedDict(
    "GetContainerAPIMetadataResultTypeDef",
    {
        "metadata": List[Dict[str, str]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerImagesRequestRequestTypeDef = TypedDict(
    "GetContainerImagesRequestRequestTypeDef",
    {
        "serviceName": str,
    },
)

GetContainerImagesResultTypeDef = TypedDict(
    "GetContainerImagesResultTypeDef",
    {
        "containerImages": List["ContainerImageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerLogRequestRequestTypeDef = TypedDict(
    "GetContainerLogRequestRequestTypeDef",
    {
        "serviceName": str,
        "containerName": str,
        "startTime": NotRequired[Union[datetime, str]],
        "endTime": NotRequired[Union[datetime, str]],
        "filterPattern": NotRequired[str],
        "pageToken": NotRequired[str],
    },
)

GetContainerLogResultTypeDef = TypedDict(
    "GetContainerLogResultTypeDef",
    {
        "logEvents": List["ContainerServiceLogEventTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerServiceDeploymentsRequestRequestTypeDef = TypedDict(
    "GetContainerServiceDeploymentsRequestRequestTypeDef",
    {
        "serviceName": str,
    },
)

GetContainerServiceDeploymentsResultTypeDef = TypedDict(
    "GetContainerServiceDeploymentsResultTypeDef",
    {
        "deployments": List["ContainerServiceDeploymentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerServiceMetricDataRequestRequestTypeDef = TypedDict(
    "GetContainerServiceMetricDataRequestRequestTypeDef",
    {
        "serviceName": str,
        "metricName": ContainerServiceMetricNameType,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "period": int,
        "statistics": Sequence[MetricStatisticType],
    },
)

GetContainerServiceMetricDataResultTypeDef = TypedDict(
    "GetContainerServiceMetricDataResultTypeDef",
    {
        "metricName": ContainerServiceMetricNameType,
        "metricData": List["MetricDatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerServicePowersResultTypeDef = TypedDict(
    "GetContainerServicePowersResultTypeDef",
    {
        "powers": List["ContainerServicePowerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerServicesRequestRequestTypeDef = TypedDict(
    "GetContainerServicesRequestRequestTypeDef",
    {
        "serviceName": NotRequired[str],
    },
)

GetDiskRequestRequestTypeDef = TypedDict(
    "GetDiskRequestRequestTypeDef",
    {
        "diskName": str,
    },
)

GetDiskResultTypeDef = TypedDict(
    "GetDiskResultTypeDef",
    {
        "disk": "DiskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDiskSnapshotRequestRequestTypeDef = TypedDict(
    "GetDiskSnapshotRequestRequestTypeDef",
    {
        "diskSnapshotName": str,
    },
)

GetDiskSnapshotResultTypeDef = TypedDict(
    "GetDiskSnapshotResultTypeDef",
    {
        "diskSnapshot": "DiskSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDiskSnapshotsRequestRequestTypeDef = TypedDict(
    "GetDiskSnapshotsRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)

GetDiskSnapshotsResultTypeDef = TypedDict(
    "GetDiskSnapshotsResultTypeDef",
    {
        "diskSnapshots": List["DiskSnapshotTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDisksRequestRequestTypeDef = TypedDict(
    "GetDisksRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)

GetDisksResultTypeDef = TypedDict(
    "GetDisksResultTypeDef",
    {
        "disks": List["DiskTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDistributionBundlesResultTypeDef = TypedDict(
    "GetDistributionBundlesResultTypeDef",
    {
        "bundles": List["DistributionBundleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDistributionLatestCacheResetRequestRequestTypeDef = TypedDict(
    "GetDistributionLatestCacheResetRequestRequestTypeDef",
    {
        "distributionName": NotRequired[str],
    },
)

GetDistributionLatestCacheResetResultTypeDef = TypedDict(
    "GetDistributionLatestCacheResetResultTypeDef",
    {
        "status": str,
        "createTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDistributionMetricDataRequestRequestTypeDef = TypedDict(
    "GetDistributionMetricDataRequestRequestTypeDef",
    {
        "distributionName": str,
        "metricName": DistributionMetricNameType,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "period": int,
        "unit": MetricUnitType,
        "statistics": Sequence[MetricStatisticType],
    },
)

GetDistributionMetricDataResultTypeDef = TypedDict(
    "GetDistributionMetricDataResultTypeDef",
    {
        "metricName": DistributionMetricNameType,
        "metricData": List["MetricDatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDistributionsRequestRequestTypeDef = TypedDict(
    "GetDistributionsRequestRequestTypeDef",
    {
        "distributionName": NotRequired[str],
        "pageToken": NotRequired[str],
    },
)

GetDistributionsResultTypeDef = TypedDict(
    "GetDistributionsResultTypeDef",
    {
        "distributions": List["LightsailDistributionTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainRequestRequestTypeDef = TypedDict(
    "GetDomainRequestRequestTypeDef",
    {
        "domainName": str,
    },
)

GetDomainResultTypeDef = TypedDict(
    "GetDomainResultTypeDef",
    {
        "domain": "DomainTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainsRequestRequestTypeDef = TypedDict(
    "GetDomainsRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)

GetDomainsResultTypeDef = TypedDict(
    "GetDomainsResultTypeDef",
    {
        "domains": List["DomainTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExportSnapshotRecordsRequestRequestTypeDef = TypedDict(
    "GetExportSnapshotRecordsRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)

GetExportSnapshotRecordsResultTypeDef = TypedDict(
    "GetExportSnapshotRecordsResultTypeDef",
    {
        "exportSnapshotRecords": List["ExportSnapshotRecordTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceAccessDetailsRequestRequestTypeDef = TypedDict(
    "GetInstanceAccessDetailsRequestRequestTypeDef",
    {
        "instanceName": str,
        "protocol": NotRequired[InstanceAccessProtocolType],
    },
)

GetInstanceAccessDetailsResultTypeDef = TypedDict(
    "GetInstanceAccessDetailsResultTypeDef",
    {
        "accessDetails": "InstanceAccessDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceMetricDataRequestRequestTypeDef = TypedDict(
    "GetInstanceMetricDataRequestRequestTypeDef",
    {
        "instanceName": str,
        "metricName": InstanceMetricNameType,
        "period": int,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "unit": MetricUnitType,
        "statistics": Sequence[MetricStatisticType],
    },
)

GetInstanceMetricDataResultTypeDef = TypedDict(
    "GetInstanceMetricDataResultTypeDef",
    {
        "metricName": InstanceMetricNameType,
        "metricData": List["MetricDatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstancePortStatesRequestRequestTypeDef = TypedDict(
    "GetInstancePortStatesRequestRequestTypeDef",
    {
        "instanceName": str,
    },
)

GetInstancePortStatesResultTypeDef = TypedDict(
    "GetInstancePortStatesResultTypeDef",
    {
        "portStates": List["InstancePortStateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceRequestRequestTypeDef = TypedDict(
    "GetInstanceRequestRequestTypeDef",
    {
        "instanceName": str,
    },
)

GetInstanceResultTypeDef = TypedDict(
    "GetInstanceResultTypeDef",
    {
        "instance": "InstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceSnapshotRequestRequestTypeDef = TypedDict(
    "GetInstanceSnapshotRequestRequestTypeDef",
    {
        "instanceSnapshotName": str,
    },
)

GetInstanceSnapshotResultTypeDef = TypedDict(
    "GetInstanceSnapshotResultTypeDef",
    {
        "instanceSnapshot": "InstanceSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceSnapshotsRequestRequestTypeDef = TypedDict(
    "GetInstanceSnapshotsRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)

GetInstanceSnapshotsResultTypeDef = TypedDict(
    "GetInstanceSnapshotsResultTypeDef",
    {
        "instanceSnapshots": List["InstanceSnapshotTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceStateRequestRequestTypeDef = TypedDict(
    "GetInstanceStateRequestRequestTypeDef",
    {
        "instanceName": str,
    },
)

GetInstanceStateResultTypeDef = TypedDict(
    "GetInstanceStateResultTypeDef",
    {
        "state": "InstanceStateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstancesRequestRequestTypeDef = TypedDict(
    "GetInstancesRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)

GetInstancesResultTypeDef = TypedDict(
    "GetInstancesResultTypeDef",
    {
        "instances": List["InstanceTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKeyPairRequestRequestTypeDef = TypedDict(
    "GetKeyPairRequestRequestTypeDef",
    {
        "keyPairName": str,
    },
)

GetKeyPairResultTypeDef = TypedDict(
    "GetKeyPairResultTypeDef",
    {
        "keyPair": "KeyPairTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKeyPairsRequestRequestTypeDef = TypedDict(
    "GetKeyPairsRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
        "includeDefaultKeyPair": NotRequired[bool],
    },
)

GetKeyPairsResultTypeDef = TypedDict(
    "GetKeyPairsResultTypeDef",
    {
        "keyPairs": List["KeyPairTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoadBalancerMetricDataRequestRequestTypeDef = TypedDict(
    "GetLoadBalancerMetricDataRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "metricName": LoadBalancerMetricNameType,
        "period": int,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "unit": MetricUnitType,
        "statistics": Sequence[MetricStatisticType],
    },
)

GetLoadBalancerMetricDataResultTypeDef = TypedDict(
    "GetLoadBalancerMetricDataResultTypeDef",
    {
        "metricName": LoadBalancerMetricNameType,
        "metricData": List["MetricDatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoadBalancerRequestRequestTypeDef = TypedDict(
    "GetLoadBalancerRequestRequestTypeDef",
    {
        "loadBalancerName": str,
    },
)

GetLoadBalancerResultTypeDef = TypedDict(
    "GetLoadBalancerResultTypeDef",
    {
        "loadBalancer": "LoadBalancerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoadBalancerTlsCertificatesRequestRequestTypeDef = TypedDict(
    "GetLoadBalancerTlsCertificatesRequestRequestTypeDef",
    {
        "loadBalancerName": str,
    },
)

GetLoadBalancerTlsCertificatesResultTypeDef = TypedDict(
    "GetLoadBalancerTlsCertificatesResultTypeDef",
    {
        "tlsCertificates": List["LoadBalancerTlsCertificateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoadBalancersRequestRequestTypeDef = TypedDict(
    "GetLoadBalancersRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)

GetLoadBalancersResultTypeDef = TypedDict(
    "GetLoadBalancersResultTypeDef",
    {
        "loadBalancers": List["LoadBalancerTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOperationRequestRequestTypeDef = TypedDict(
    "GetOperationRequestRequestTypeDef",
    {
        "operationId": str,
    },
)

GetOperationResultTypeDef = TypedDict(
    "GetOperationResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOperationsForResourceRequestRequestTypeDef = TypedDict(
    "GetOperationsForResourceRequestRequestTypeDef",
    {
        "resourceName": str,
        "pageToken": NotRequired[str],
    },
)

GetOperationsForResourceResultTypeDef = TypedDict(
    "GetOperationsForResourceResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "nextPageCount": str,
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOperationsRequestRequestTypeDef = TypedDict(
    "GetOperationsRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)

GetOperationsResultTypeDef = TypedDict(
    "GetOperationsResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegionsRequestRequestTypeDef = TypedDict(
    "GetRegionsRequestRequestTypeDef",
    {
        "includeAvailabilityZones": NotRequired[bool],
        "includeRelationalDatabaseAvailabilityZones": NotRequired[bool],
    },
)

GetRegionsResultTypeDef = TypedDict(
    "GetRegionsResultTypeDef",
    {
        "regions": List["RegionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseBlueprintsRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseBlueprintsRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)

GetRelationalDatabaseBlueprintsResultTypeDef = TypedDict(
    "GetRelationalDatabaseBlueprintsResultTypeDef",
    {
        "blueprints": List["RelationalDatabaseBlueprintTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseBundlesRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseBundlesRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)

GetRelationalDatabaseBundlesResultTypeDef = TypedDict(
    "GetRelationalDatabaseBundlesResultTypeDef",
    {
        "bundles": List["RelationalDatabaseBundleTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseEventsRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseEventsRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "durationInMinutes": NotRequired[int],
        "pageToken": NotRequired[str],
    },
)

GetRelationalDatabaseEventsResultTypeDef = TypedDict(
    "GetRelationalDatabaseEventsResultTypeDef",
    {
        "relationalDatabaseEvents": List["RelationalDatabaseEventTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseLogEventsRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseLogEventsRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "logStreamName": str,
        "startTime": NotRequired[Union[datetime, str]],
        "endTime": NotRequired[Union[datetime, str]],
        "startFromHead": NotRequired[bool],
        "pageToken": NotRequired[str],
    },
)

GetRelationalDatabaseLogEventsResultTypeDef = TypedDict(
    "GetRelationalDatabaseLogEventsResultTypeDef",
    {
        "resourceLogEvents": List["LogEventTypeDef"],
        "nextBackwardToken": str,
        "nextForwardToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseLogStreamsRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseLogStreamsRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)

GetRelationalDatabaseLogStreamsResultTypeDef = TypedDict(
    "GetRelationalDatabaseLogStreamsResultTypeDef",
    {
        "logStreams": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseMasterUserPasswordRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseMasterUserPasswordRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "passwordVersion": NotRequired[RelationalDatabasePasswordVersionType],
    },
)

GetRelationalDatabaseMasterUserPasswordResultTypeDef = TypedDict(
    "GetRelationalDatabaseMasterUserPasswordResultTypeDef",
    {
        "masterUserPassword": str,
        "createdAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseMetricDataRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseMetricDataRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "metricName": RelationalDatabaseMetricNameType,
        "period": int,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "unit": MetricUnitType,
        "statistics": Sequence[MetricStatisticType],
    },
)

GetRelationalDatabaseMetricDataResultTypeDef = TypedDict(
    "GetRelationalDatabaseMetricDataResultTypeDef",
    {
        "metricName": RelationalDatabaseMetricNameType,
        "metricData": List["MetricDatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseParametersRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseParametersRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "pageToken": NotRequired[str],
    },
)

GetRelationalDatabaseParametersResultTypeDef = TypedDict(
    "GetRelationalDatabaseParametersResultTypeDef",
    {
        "parameters": List["RelationalDatabaseParameterTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)

GetRelationalDatabaseResultTypeDef = TypedDict(
    "GetRelationalDatabaseResultTypeDef",
    {
        "relationalDatabase": "RelationalDatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseSnapshotRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseSnapshotRequestRequestTypeDef",
    {
        "relationalDatabaseSnapshotName": str,
    },
)

GetRelationalDatabaseSnapshotResultTypeDef = TypedDict(
    "GetRelationalDatabaseSnapshotResultTypeDef",
    {
        "relationalDatabaseSnapshot": "RelationalDatabaseSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseSnapshotsRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseSnapshotsRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)

GetRelationalDatabaseSnapshotsResultTypeDef = TypedDict(
    "GetRelationalDatabaseSnapshotsResultTypeDef",
    {
        "relationalDatabaseSnapshots": List["RelationalDatabaseSnapshotTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabasesRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabasesRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)

GetRelationalDatabasesResultTypeDef = TypedDict(
    "GetRelationalDatabasesResultTypeDef",
    {
        "relationalDatabases": List["RelationalDatabaseTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStaticIpRequestRequestTypeDef = TypedDict(
    "GetStaticIpRequestRequestTypeDef",
    {
        "staticIpName": str,
    },
)

GetStaticIpResultTypeDef = TypedDict(
    "GetStaticIpResultTypeDef",
    {
        "staticIp": "StaticIpTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStaticIpsRequestRequestTypeDef = TypedDict(
    "GetStaticIpsRequestRequestTypeDef",
    {
        "pageToken": NotRequired[str],
    },
)

GetStaticIpsResultTypeDef = TypedDict(
    "GetStaticIpsResultTypeDef",
    {
        "staticIps": List["StaticIpTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HeaderObjectTypeDef = TypedDict(
    "HeaderObjectTypeDef",
    {
        "option": NotRequired[ForwardValuesType],
        "headersAllowList": NotRequired[Sequence[HeaderEnumType]],
    },
)

HostKeyAttributesTypeDef = TypedDict(
    "HostKeyAttributesTypeDef",
    {
        "algorithm": NotRequired[str],
        "publicKey": NotRequired[str],
        "witnessedAt": NotRequired[datetime],
        "fingerprintSHA1": NotRequired[str],
        "fingerprintSHA256": NotRequired[str],
        "notValidBefore": NotRequired[datetime],
        "notValidAfter": NotRequired[datetime],
    },
)

ImportKeyPairRequestRequestTypeDef = TypedDict(
    "ImportKeyPairRequestRequestTypeDef",
    {
        "keyPairName": str,
        "publicKeyBase64": str,
    },
)

ImportKeyPairResultTypeDef = TypedDict(
    "ImportKeyPairResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputOriginTypeDef = TypedDict(
    "InputOriginTypeDef",
    {
        "name": NotRequired[str],
        "regionName": NotRequired[RegionNameType],
        "protocolPolicy": NotRequired[OriginProtocolPolicyEnumType],
    },
)

InstanceAccessDetailsTypeDef = TypedDict(
    "InstanceAccessDetailsTypeDef",
    {
        "certKey": NotRequired[str],
        "expiresAt": NotRequired[datetime],
        "ipAddress": NotRequired[str],
        "password": NotRequired[str],
        "passwordData": NotRequired["PasswordDataTypeDef"],
        "privateKey": NotRequired[str],
        "protocol": NotRequired[InstanceAccessProtocolType],
        "instanceName": NotRequired[str],
        "username": NotRequired[str],
        "hostKeys": NotRequired[List["HostKeyAttributesTypeDef"]],
    },
)

InstanceEntryTypeDef = TypedDict(
    "InstanceEntryTypeDef",
    {
        "sourceName": str,
        "instanceType": str,
        "portInfoSource": PortInfoSourceTypeType,
        "availabilityZone": str,
        "userData": NotRequired[str],
    },
)

InstanceHardwareTypeDef = TypedDict(
    "InstanceHardwareTypeDef",
    {
        "cpuCount": NotRequired[int],
        "disks": NotRequired[List["DiskTypeDef"]],
        "ramSizeInGb": NotRequired[float],
    },
)

InstanceHealthSummaryTypeDef = TypedDict(
    "InstanceHealthSummaryTypeDef",
    {
        "instanceName": NotRequired[str],
        "instanceHealth": NotRequired[InstanceHealthStateType],
        "instanceHealthReason": NotRequired[InstanceHealthReasonType],
    },
)

InstanceNetworkingTypeDef = TypedDict(
    "InstanceNetworkingTypeDef",
    {
        "monthlyTransfer": NotRequired["MonthlyTransferTypeDef"],
        "ports": NotRequired[List["InstancePortInfoTypeDef"]],
    },
)

InstancePortInfoTypeDef = TypedDict(
    "InstancePortInfoTypeDef",
    {
        "fromPort": NotRequired[int],
        "toPort": NotRequired[int],
        "protocol": NotRequired[NetworkProtocolType],
        "accessFrom": NotRequired[str],
        "accessType": NotRequired[PortAccessTypeType],
        "commonName": NotRequired[str],
        "accessDirection": NotRequired[AccessDirectionType],
        "cidrs": NotRequired[List[str]],
        "ipv6Cidrs": NotRequired[List[str]],
        "cidrListAliases": NotRequired[List[str]],
    },
)

InstancePortStateTypeDef = TypedDict(
    "InstancePortStateTypeDef",
    {
        "fromPort": NotRequired[int],
        "toPort": NotRequired[int],
        "protocol": NotRequired[NetworkProtocolType],
        "state": NotRequired[PortStateType],
        "cidrs": NotRequired[List[str]],
        "ipv6Cidrs": NotRequired[List[str]],
        "cidrListAliases": NotRequired[List[str]],
    },
)

InstanceSnapshotInfoTypeDef = TypedDict(
    "InstanceSnapshotInfoTypeDef",
    {
        "fromBundleId": NotRequired[str],
        "fromBlueprintId": NotRequired[str],
        "fromDiskInfo": NotRequired[List["DiskInfoTypeDef"]],
    },
)

InstanceSnapshotTypeDef = TypedDict(
    "InstanceSnapshotTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired["ResourceLocationTypeDef"],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List["TagTypeDef"]],
        "state": NotRequired[InstanceSnapshotStateType],
        "progress": NotRequired[str],
        "fromAttachedDisks": NotRequired[List["DiskTypeDef"]],
        "fromInstanceName": NotRequired[str],
        "fromInstanceArn": NotRequired[str],
        "fromBlueprintId": NotRequired[str],
        "fromBundleId": NotRequired[str],
        "isFromAutoSnapshot": NotRequired[bool],
        "sizeInGb": NotRequired[int],
    },
)

InstanceStateTypeDef = TypedDict(
    "InstanceStateTypeDef",
    {
        "code": NotRequired[int],
        "name": NotRequired[str],
    },
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired["ResourceLocationTypeDef"],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List["TagTypeDef"]],
        "blueprintId": NotRequired[str],
        "blueprintName": NotRequired[str],
        "bundleId": NotRequired[str],
        "addOns": NotRequired[List["AddOnTypeDef"]],
        "isStaticIp": NotRequired[bool],
        "privateIpAddress": NotRequired[str],
        "publicIpAddress": NotRequired[str],
        "ipv6Addresses": NotRequired[List[str]],
        "ipAddressType": NotRequired[IpAddressTypeType],
        "hardware": NotRequired["InstanceHardwareTypeDef"],
        "networking": NotRequired["InstanceNetworkingTypeDef"],
        "state": NotRequired["InstanceStateTypeDef"],
        "username": NotRequired[str],
        "sshKeyName": NotRequired[str],
    },
)

IsVpcPeeredResultTypeDef = TypedDict(
    "IsVpcPeeredResultTypeDef",
    {
        "isPeered": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KeyPairTypeDef = TypedDict(
    "KeyPairTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired["ResourceLocationTypeDef"],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List["TagTypeDef"]],
        "fingerprint": NotRequired[str],
    },
)

LightsailDistributionTypeDef = TypedDict(
    "LightsailDistributionTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired["ResourceLocationTypeDef"],
        "resourceType": NotRequired[ResourceTypeType],
        "alternativeDomainNames": NotRequired[List[str]],
        "status": NotRequired[str],
        "isEnabled": NotRequired[bool],
        "domainName": NotRequired[str],
        "bundleId": NotRequired[str],
        "certificateName": NotRequired[str],
        "origin": NotRequired["OriginTypeDef"],
        "originPublicDNS": NotRequired[str],
        "defaultCacheBehavior": NotRequired["CacheBehaviorTypeDef"],
        "cacheBehaviorSettings": NotRequired["CacheSettingsTypeDef"],
        "cacheBehaviors": NotRequired[List["CacheBehaviorPerPathTypeDef"]],
        "ableToUpdateBundle": NotRequired[bool],
        "ipAddressType": NotRequired[IpAddressTypeType],
        "tags": NotRequired[List["TagTypeDef"]],
    },
)

LoadBalancerTlsCertificateDomainValidationOptionTypeDef = TypedDict(
    "LoadBalancerTlsCertificateDomainValidationOptionTypeDef",
    {
        "domainName": NotRequired[str],
        "validationStatus": NotRequired[LoadBalancerTlsCertificateDomainStatusType],
    },
)

LoadBalancerTlsCertificateDomainValidationRecordTypeDef = TypedDict(
    "LoadBalancerTlsCertificateDomainValidationRecordTypeDef",
    {
        "name": NotRequired[str],
        "type": NotRequired[str],
        "value": NotRequired[str],
        "validationStatus": NotRequired[LoadBalancerTlsCertificateDomainStatusType],
        "domainName": NotRequired[str],
    },
)

LoadBalancerTlsCertificateRenewalSummaryTypeDef = TypedDict(
    "LoadBalancerTlsCertificateRenewalSummaryTypeDef",
    {
        "renewalStatus": NotRequired[LoadBalancerTlsCertificateRenewalStatusType],
        "domainValidationOptions": NotRequired[
            List["LoadBalancerTlsCertificateDomainValidationOptionTypeDef"]
        ],
    },
)

LoadBalancerTlsCertificateSummaryTypeDef = TypedDict(
    "LoadBalancerTlsCertificateSummaryTypeDef",
    {
        "name": NotRequired[str],
        "isAttached": NotRequired[bool],
    },
)

LoadBalancerTlsCertificateTypeDef = TypedDict(
    "LoadBalancerTlsCertificateTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired["ResourceLocationTypeDef"],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List["TagTypeDef"]],
        "loadBalancerName": NotRequired[str],
        "isAttached": NotRequired[bool],
        "status": NotRequired[LoadBalancerTlsCertificateStatusType],
        "domainName": NotRequired[str],
        "domainValidationRecords": NotRequired[
            List["LoadBalancerTlsCertificateDomainValidationRecordTypeDef"]
        ],
        "failureReason": NotRequired[LoadBalancerTlsCertificateFailureReasonType],
        "issuedAt": NotRequired[datetime],
        "issuer": NotRequired[str],
        "keyAlgorithm": NotRequired[str],
        "notAfter": NotRequired[datetime],
        "notBefore": NotRequired[datetime],
        "renewalSummary": NotRequired["LoadBalancerTlsCertificateRenewalSummaryTypeDef"],
        "revocationReason": NotRequired[LoadBalancerTlsCertificateRevocationReasonType],
        "revokedAt": NotRequired[datetime],
        "serial": NotRequired[str],
        "signatureAlgorithm": NotRequired[str],
        "subject": NotRequired[str],
        "subjectAlternativeNames": NotRequired[List[str]],
    },
)

LoadBalancerTypeDef = TypedDict(
    "LoadBalancerTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired["ResourceLocationTypeDef"],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List["TagTypeDef"]],
        "dnsName": NotRequired[str],
        "state": NotRequired[LoadBalancerStateType],
        "protocol": NotRequired[LoadBalancerProtocolType],
        "publicPorts": NotRequired[List[int]],
        "healthCheckPath": NotRequired[str],
        "instancePort": NotRequired[int],
        "instanceHealthSummary": NotRequired[List["InstanceHealthSummaryTypeDef"]],
        "tlsCertificateSummaries": NotRequired[List["LoadBalancerTlsCertificateSummaryTypeDef"]],
        "configurationOptions": NotRequired[Dict[LoadBalancerAttributeNameType, str]],
        "ipAddressType": NotRequired[IpAddressTypeType],
    },
)

LogEventTypeDef = TypedDict(
    "LogEventTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "message": NotRequired[str],
    },
)

MetricDatapointTypeDef = TypedDict(
    "MetricDatapointTypeDef",
    {
        "average": NotRequired[float],
        "maximum": NotRequired[float],
        "minimum": NotRequired[float],
        "sampleCount": NotRequired[float],
        "sum": NotRequired[float],
        "timestamp": NotRequired[datetime],
        "unit": NotRequired[MetricUnitType],
    },
)

MonitoredResourceInfoTypeDef = TypedDict(
    "MonitoredResourceInfoTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "resourceType": NotRequired[ResourceTypeType],
    },
)

MonthlyTransferTypeDef = TypedDict(
    "MonthlyTransferTypeDef",
    {
        "gbPerMonthAllocated": NotRequired[int],
    },
)

OpenInstancePublicPortsRequestRequestTypeDef = TypedDict(
    "OpenInstancePublicPortsRequestRequestTypeDef",
    {
        "portInfo": "PortInfoTypeDef",
        "instanceName": str,
    },
)

OpenInstancePublicPortsResultTypeDef = TypedDict(
    "OpenInstancePublicPortsResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OperationTypeDef = TypedDict(
    "OperationTypeDef",
    {
        "id": NotRequired[str],
        "resourceName": NotRequired[str],
        "resourceType": NotRequired[ResourceTypeType],
        "createdAt": NotRequired[datetime],
        "location": NotRequired["ResourceLocationTypeDef"],
        "isTerminal": NotRequired[bool],
        "operationDetails": NotRequired[str],
        "operationType": NotRequired[OperationTypeType],
        "status": NotRequired[OperationStatusType],
        "statusChangedAt": NotRequired[datetime],
        "errorCode": NotRequired[str],
        "errorDetails": NotRequired[str],
    },
)

OriginTypeDef = TypedDict(
    "OriginTypeDef",
    {
        "name": NotRequired[str],
        "resourceType": NotRequired[ResourceTypeType],
        "regionName": NotRequired[RegionNameType],
        "protocolPolicy": NotRequired[OriginProtocolPolicyEnumType],
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

PasswordDataTypeDef = TypedDict(
    "PasswordDataTypeDef",
    {
        "ciphertext": NotRequired[str],
        "keyPairName": NotRequired[str],
    },
)

PeerVpcResultTypeDef = TypedDict(
    "PeerVpcResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PendingMaintenanceActionTypeDef = TypedDict(
    "PendingMaintenanceActionTypeDef",
    {
        "action": NotRequired[str],
        "description": NotRequired[str],
        "currentApplyDate": NotRequired[datetime],
    },
)

PendingModifiedRelationalDatabaseValuesTypeDef = TypedDict(
    "PendingModifiedRelationalDatabaseValuesTypeDef",
    {
        "masterUserPassword": NotRequired[str],
        "engineVersion": NotRequired[str],
        "backupRetentionEnabled": NotRequired[bool],
    },
)

PortInfoTypeDef = TypedDict(
    "PortInfoTypeDef",
    {
        "fromPort": NotRequired[int],
        "toPort": NotRequired[int],
        "protocol": NotRequired[NetworkProtocolType],
        "cidrs": NotRequired[Sequence[str]],
        "ipv6Cidrs": NotRequired[Sequence[str]],
        "cidrListAliases": NotRequired[Sequence[str]],
    },
)

PutAlarmRequestRequestTypeDef = TypedDict(
    "PutAlarmRequestRequestTypeDef",
    {
        "alarmName": str,
        "metricName": MetricNameType,
        "monitoredResourceName": str,
        "comparisonOperator": ComparisonOperatorType,
        "threshold": float,
        "evaluationPeriods": int,
        "datapointsToAlarm": NotRequired[int],
        "treatMissingData": NotRequired[TreatMissingDataType],
        "contactProtocols": NotRequired[Sequence[ContactProtocolType]],
        "notificationTriggers": NotRequired[Sequence[AlarmStateType]],
        "notificationEnabled": NotRequired[bool],
    },
)

PutAlarmResultTypeDef = TypedDict(
    "PutAlarmResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutInstancePublicPortsRequestRequestTypeDef = TypedDict(
    "PutInstancePublicPortsRequestRequestTypeDef",
    {
        "portInfos": Sequence["PortInfoTypeDef"],
        "instanceName": str,
    },
)

PutInstancePublicPortsResultTypeDef = TypedDict(
    "PutInstancePublicPortsResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryStringObjectTypeDef = TypedDict(
    "QueryStringObjectTypeDef",
    {
        "option": NotRequired[bool],
        "queryStringsAllowList": NotRequired[Sequence[str]],
    },
)

RebootInstanceRequestRequestTypeDef = TypedDict(
    "RebootInstanceRequestRequestTypeDef",
    {
        "instanceName": str,
    },
)

RebootInstanceResultTypeDef = TypedDict(
    "RebootInstanceResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RebootRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "RebootRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)

RebootRelationalDatabaseResultTypeDef = TypedDict(
    "RebootRelationalDatabaseResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegionTypeDef = TypedDict(
    "RegionTypeDef",
    {
        "continentCode": NotRequired[str],
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "name": NotRequired[RegionNameType],
        "availabilityZones": NotRequired[List["AvailabilityZoneTypeDef"]],
        "relationalDatabaseAvailabilityZones": NotRequired[List["AvailabilityZoneTypeDef"]],
    },
)

RegisterContainerImageRequestRequestTypeDef = TypedDict(
    "RegisterContainerImageRequestRequestTypeDef",
    {
        "serviceName": str,
        "label": str,
        "digest": str,
    },
)

RegisterContainerImageResultTypeDef = TypedDict(
    "RegisterContainerImageResultTypeDef",
    {
        "containerImage": "ContainerImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RelationalDatabaseBlueprintTypeDef = TypedDict(
    "RelationalDatabaseBlueprintTypeDef",
    {
        "blueprintId": NotRequired[str],
        "engine": NotRequired[Literal["mysql"]],
        "engineVersion": NotRequired[str],
        "engineDescription": NotRequired[str],
        "engineVersionDescription": NotRequired[str],
        "isEngineDefault": NotRequired[bool],
    },
)

RelationalDatabaseBundleTypeDef = TypedDict(
    "RelationalDatabaseBundleTypeDef",
    {
        "bundleId": NotRequired[str],
        "name": NotRequired[str],
        "price": NotRequired[float],
        "ramSizeInGb": NotRequired[float],
        "diskSizeInGb": NotRequired[int],
        "transferPerMonthInGb": NotRequired[int],
        "cpuCount": NotRequired[int],
        "isEncrypted": NotRequired[bool],
        "isActive": NotRequired[bool],
    },
)

RelationalDatabaseEndpointTypeDef = TypedDict(
    "RelationalDatabaseEndpointTypeDef",
    {
        "port": NotRequired[int],
        "address": NotRequired[str],
    },
)

RelationalDatabaseEventTypeDef = TypedDict(
    "RelationalDatabaseEventTypeDef",
    {
        "resource": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "message": NotRequired[str],
        "eventCategories": NotRequired[List[str]],
    },
)

RelationalDatabaseHardwareTypeDef = TypedDict(
    "RelationalDatabaseHardwareTypeDef",
    {
        "cpuCount": NotRequired[int],
        "diskSizeInGb": NotRequired[int],
        "ramSizeInGb": NotRequired[float],
    },
)

RelationalDatabaseParameterTypeDef = TypedDict(
    "RelationalDatabaseParameterTypeDef",
    {
        "allowedValues": NotRequired[str],
        "applyMethod": NotRequired[str],
        "applyType": NotRequired[str],
        "dataType": NotRequired[str],
        "description": NotRequired[str],
        "isModifiable": NotRequired[bool],
        "parameterName": NotRequired[str],
        "parameterValue": NotRequired[str],
    },
)

RelationalDatabaseSnapshotTypeDef = TypedDict(
    "RelationalDatabaseSnapshotTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired["ResourceLocationTypeDef"],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List["TagTypeDef"]],
        "engine": NotRequired[str],
        "engineVersion": NotRequired[str],
        "sizeInGb": NotRequired[int],
        "state": NotRequired[str],
        "fromRelationalDatabaseName": NotRequired[str],
        "fromRelationalDatabaseArn": NotRequired[str],
        "fromRelationalDatabaseBundleId": NotRequired[str],
        "fromRelationalDatabaseBlueprintId": NotRequired[str],
    },
)

RelationalDatabaseTypeDef = TypedDict(
    "RelationalDatabaseTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired["ResourceLocationTypeDef"],
        "resourceType": NotRequired[ResourceTypeType],
        "tags": NotRequired[List["TagTypeDef"]],
        "relationalDatabaseBlueprintId": NotRequired[str],
        "relationalDatabaseBundleId": NotRequired[str],
        "masterDatabaseName": NotRequired[str],
        "hardware": NotRequired["RelationalDatabaseHardwareTypeDef"],
        "state": NotRequired[str],
        "secondaryAvailabilityZone": NotRequired[str],
        "backupRetentionEnabled": NotRequired[bool],
        "pendingModifiedValues": NotRequired["PendingModifiedRelationalDatabaseValuesTypeDef"],
        "engine": NotRequired[str],
        "engineVersion": NotRequired[str],
        "latestRestorableTime": NotRequired[datetime],
        "masterUsername": NotRequired[str],
        "parameterApplyStatus": NotRequired[str],
        "preferredBackupWindow": NotRequired[str],
        "preferredMaintenanceWindow": NotRequired[str],
        "publiclyAccessible": NotRequired[bool],
        "masterEndpoint": NotRequired["RelationalDatabaseEndpointTypeDef"],
        "pendingMaintenanceActions": NotRequired[List["PendingMaintenanceActionTypeDef"]],
        "caCertificateIdentifier": NotRequired[str],
    },
)

ReleaseStaticIpRequestRequestTypeDef = TypedDict(
    "ReleaseStaticIpRequestRequestTypeDef",
    {
        "staticIpName": str,
    },
)

ReleaseStaticIpResultTypeDef = TypedDict(
    "ReleaseStaticIpResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RenewalSummaryTypeDef = TypedDict(
    "RenewalSummaryTypeDef",
    {
        "domainValidationRecords": NotRequired[List["DomainValidationRecordTypeDef"]],
        "renewalStatus": NotRequired[RenewalStatusType],
        "renewalStatusReason": NotRequired[str],
        "updatedAt": NotRequired[datetime],
    },
)

ResetDistributionCacheRequestRequestTypeDef = TypedDict(
    "ResetDistributionCacheRequestRequestTypeDef",
    {
        "distributionName": NotRequired[str],
    },
)

ResetDistributionCacheResultTypeDef = TypedDict(
    "ResetDistributionCacheResultTypeDef",
    {
        "status": str,
        "createTime": datetime,
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceLocationTypeDef = TypedDict(
    "ResourceLocationTypeDef",
    {
        "availabilityZone": NotRequired[str],
        "regionName": NotRequired[RegionNameType],
    },
)

ResourceReceivingAccessTypeDef = TypedDict(
    "ResourceReceivingAccessTypeDef",
    {
        "name": NotRequired[str],
        "resourceType": NotRequired[str],
    },
)

ResourceRecordTypeDef = TypedDict(
    "ResourceRecordTypeDef",
    {
        "name": NotRequired[str],
        "type": NotRequired[str],
        "value": NotRequired[str],
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

SendContactMethodVerificationRequestRequestTypeDef = TypedDict(
    "SendContactMethodVerificationRequestRequestTypeDef",
    {
        "protocol": Literal["Email"],
    },
)

SendContactMethodVerificationResultTypeDef = TypedDict(
    "SendContactMethodVerificationResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetIpAddressTypeRequestRequestTypeDef = TypedDict(
    "SetIpAddressTypeRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceName": str,
        "ipAddressType": IpAddressTypeType,
    },
)

SetIpAddressTypeResultTypeDef = TypedDict(
    "SetIpAddressTypeResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetResourceAccessForBucketRequestRequestTypeDef = TypedDict(
    "SetResourceAccessForBucketRequestRequestTypeDef",
    {
        "resourceName": str,
        "bucketName": str,
        "access": ResourceBucketAccessType,
    },
)

SetResourceAccessForBucketResultTypeDef = TypedDict(
    "SetResourceAccessForBucketResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartInstanceRequestRequestTypeDef = TypedDict(
    "StartInstanceRequestRequestTypeDef",
    {
        "instanceName": str,
    },
)

StartInstanceResultTypeDef = TypedDict(
    "StartInstanceResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "StartRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)

StartRelationalDatabaseResultTypeDef = TypedDict(
    "StartRelationalDatabaseResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StaticIpTypeDef = TypedDict(
    "StaticIpTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "supportCode": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "location": NotRequired["ResourceLocationTypeDef"],
        "resourceType": NotRequired[ResourceTypeType],
        "ipAddress": NotRequired[str],
        "attachedTo": NotRequired[str],
        "isAttached": NotRequired[bool],
    },
)

StopInstanceRequestRequestTypeDef = TypedDict(
    "StopInstanceRequestRequestTypeDef",
    {
        "instanceName": str,
        "force": NotRequired[bool],
    },
)

StopInstanceResultTypeDef = TypedDict(
    "StopInstanceResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "StopRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "relationalDatabaseSnapshotName": NotRequired[str],
    },
)

StopRelationalDatabaseResultTypeDef = TypedDict(
    "StopRelationalDatabaseResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceName": str,
        "tags": Sequence["TagTypeDef"],
        "resourceArn": NotRequired[str],
    },
)

TagResourceResultTypeDef = TypedDict(
    "TagResourceResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
    },
)

TestAlarmRequestRequestTypeDef = TypedDict(
    "TestAlarmRequestRequestTypeDef",
    {
        "alarmName": str,
        "state": AlarmStateType,
    },
)

TestAlarmResultTypeDef = TypedDict(
    "TestAlarmResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UnpeerVpcResultTypeDef = TypedDict(
    "UnpeerVpcResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceName": str,
        "tagKeys": Sequence[str],
        "resourceArn": NotRequired[str],
    },
)

UntagResourceResultTypeDef = TypedDict(
    "UntagResourceResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBucketBundleRequestRequestTypeDef = TypedDict(
    "UpdateBucketBundleRequestRequestTypeDef",
    {
        "bucketName": str,
        "bundleId": str,
    },
)

UpdateBucketBundleResultTypeDef = TypedDict(
    "UpdateBucketBundleResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBucketRequestRequestTypeDef = TypedDict(
    "UpdateBucketRequestRequestTypeDef",
    {
        "bucketName": str,
        "accessRules": NotRequired["AccessRulesTypeDef"],
        "versioning": NotRequired[str],
        "readonlyAccessAccounts": NotRequired[Sequence[str]],
        "accessLogConfig": NotRequired["BucketAccessLogConfigTypeDef"],
    },
)

UpdateBucketResultTypeDef = TypedDict(
    "UpdateBucketResultTypeDef",
    {
        "bucket": "BucketTypeDef",
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateContainerServiceRequestRequestTypeDef = TypedDict(
    "UpdateContainerServiceRequestRequestTypeDef",
    {
        "serviceName": str,
        "power": NotRequired[ContainerServicePowerNameType],
        "scale": NotRequired[int],
        "isDisabled": NotRequired[bool],
        "publicDomainNames": NotRequired[Mapping[str, Sequence[str]]],
    },
)

UpdateContainerServiceResultTypeDef = TypedDict(
    "UpdateContainerServiceResultTypeDef",
    {
        "containerService": "ContainerServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDistributionBundleRequestRequestTypeDef = TypedDict(
    "UpdateDistributionBundleRequestRequestTypeDef",
    {
        "distributionName": NotRequired[str],
        "bundleId": NotRequired[str],
    },
)

UpdateDistributionBundleResultTypeDef = TypedDict(
    "UpdateDistributionBundleResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDistributionRequestRequestTypeDef = TypedDict(
    "UpdateDistributionRequestRequestTypeDef",
    {
        "distributionName": str,
        "origin": NotRequired["InputOriginTypeDef"],
        "defaultCacheBehavior": NotRequired["CacheBehaviorTypeDef"],
        "cacheBehaviorSettings": NotRequired["CacheSettingsTypeDef"],
        "cacheBehaviors": NotRequired[Sequence["CacheBehaviorPerPathTypeDef"]],
        "isEnabled": NotRequired[bool],
    },
)

UpdateDistributionResultTypeDef = TypedDict(
    "UpdateDistributionResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDomainEntryRequestRequestTypeDef = TypedDict(
    "UpdateDomainEntryRequestRequestTypeDef",
    {
        "domainName": str,
        "domainEntry": "DomainEntryTypeDef",
    },
)

UpdateDomainEntryResultTypeDef = TypedDict(
    "UpdateDomainEntryResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateLoadBalancerAttributeRequestRequestTypeDef = TypedDict(
    "UpdateLoadBalancerAttributeRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "attributeName": LoadBalancerAttributeNameType,
        "attributeValue": str,
    },
)

UpdateLoadBalancerAttributeResultTypeDef = TypedDict(
    "UpdateLoadBalancerAttributeResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRelationalDatabaseParametersRequestRequestTypeDef = TypedDict(
    "UpdateRelationalDatabaseParametersRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "parameters": Sequence["RelationalDatabaseParameterTypeDef"],
    },
)

UpdateRelationalDatabaseParametersResultTypeDef = TypedDict(
    "UpdateRelationalDatabaseParametersResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "UpdateRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "masterUserPassword": NotRequired[str],
        "rotateMasterUserPassword": NotRequired[bool],
        "preferredBackupWindow": NotRequired[str],
        "preferredMaintenanceWindow": NotRequired[str],
        "enableBackupRetention": NotRequired[bool],
        "disableBackupRetention": NotRequired[bool],
        "publiclyAccessible": NotRequired[bool],
        "applyImmediately": NotRequired[bool],
        "caCertificateIdentifier": NotRequired[str],
    },
)

UpdateRelationalDatabaseResultTypeDef = TypedDict(
    "UpdateRelationalDatabaseResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
