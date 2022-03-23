"""
Type annotations for panorama service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_panorama/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_panorama.type_defs import AlternateSoftwareMetadataTypeDef

    data: AlternateSoftwareMetadataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    ApplicationInstanceHealthStatusType,
    ApplicationInstanceStatusType,
    ConnectionTypeType,
    DeviceConnectionStatusType,
    DeviceStatusType,
    DeviceTypeType,
    NetworkConnectionStatusType,
    NodeCategoryType,
    NodeFromTemplateJobStatusType,
    NodeInstanceStatusType,
    PackageImportJobStatusType,
    PackageImportJobTypeType,
    PackageVersionStatusType,
    PortTypeType,
    StatusFilterType,
    UpdateProgressType,
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
    "AlternateSoftwareMetadataTypeDef",
    "ApplicationInstanceTypeDef",
    "CreateApplicationInstanceRequestRequestTypeDef",
    "CreateApplicationInstanceResponseTypeDef",
    "CreateJobForDevicesRequestRequestTypeDef",
    "CreateJobForDevicesResponseTypeDef",
    "CreateNodeFromTemplateJobRequestRequestTypeDef",
    "CreateNodeFromTemplateJobResponseTypeDef",
    "CreatePackageImportJobRequestRequestTypeDef",
    "CreatePackageImportJobResponseTypeDef",
    "CreatePackageRequestRequestTypeDef",
    "CreatePackageResponseTypeDef",
    "DeleteDeviceRequestRequestTypeDef",
    "DeleteDeviceResponseTypeDef",
    "DeletePackageRequestRequestTypeDef",
    "DeregisterPackageVersionRequestRequestTypeDef",
    "DescribeApplicationInstanceDetailsRequestRequestTypeDef",
    "DescribeApplicationInstanceDetailsResponseTypeDef",
    "DescribeApplicationInstanceRequestRequestTypeDef",
    "DescribeApplicationInstanceResponseTypeDef",
    "DescribeDeviceJobRequestRequestTypeDef",
    "DescribeDeviceJobResponseTypeDef",
    "DescribeDeviceRequestRequestTypeDef",
    "DescribeDeviceResponseTypeDef",
    "DescribeNodeFromTemplateJobRequestRequestTypeDef",
    "DescribeNodeFromTemplateJobResponseTypeDef",
    "DescribeNodeRequestRequestTypeDef",
    "DescribeNodeResponseTypeDef",
    "DescribePackageImportJobRequestRequestTypeDef",
    "DescribePackageImportJobResponseTypeDef",
    "DescribePackageRequestRequestTypeDef",
    "DescribePackageResponseTypeDef",
    "DescribePackageVersionRequestRequestTypeDef",
    "DescribePackageVersionResponseTypeDef",
    "DeviceJobConfigTypeDef",
    "DeviceJobTypeDef",
    "DeviceTypeDef",
    "EthernetPayloadTypeDef",
    "EthernetStatusTypeDef",
    "JobResourceTagsTypeDef",
    "JobTypeDef",
    "ListApplicationInstanceDependenciesRequestRequestTypeDef",
    "ListApplicationInstanceDependenciesResponseTypeDef",
    "ListApplicationInstanceNodeInstancesRequestRequestTypeDef",
    "ListApplicationInstanceNodeInstancesResponseTypeDef",
    "ListApplicationInstancesRequestRequestTypeDef",
    "ListApplicationInstancesResponseTypeDef",
    "ListDevicesJobsRequestRequestTypeDef",
    "ListDevicesJobsResponseTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "ListDevicesResponseTypeDef",
    "ListNodeFromTemplateJobsRequestRequestTypeDef",
    "ListNodeFromTemplateJobsResponseTypeDef",
    "ListNodesRequestRequestTypeDef",
    "ListNodesResponseTypeDef",
    "ListPackageImportJobsRequestRequestTypeDef",
    "ListPackageImportJobsResponseTypeDef",
    "ListPackagesRequestRequestTypeDef",
    "ListPackagesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ManifestOverridesPayloadTypeDef",
    "ManifestPayloadTypeDef",
    "NetworkPayloadTypeDef",
    "NetworkStatusTypeDef",
    "NodeFromTemplateJobTypeDef",
    "NodeInputPortTypeDef",
    "NodeInstanceTypeDef",
    "NodeInterfaceTypeDef",
    "NodeOutputPortTypeDef",
    "NodeTypeDef",
    "NtpPayloadTypeDef",
    "NtpStatusTypeDef",
    "OTAJobConfigTypeDef",
    "OutPutS3LocationTypeDef",
    "PackageImportJobInputConfigTypeDef",
    "PackageImportJobOutputConfigTypeDef",
    "PackageImportJobOutputTypeDef",
    "PackageImportJobTypeDef",
    "PackageListItemTypeDef",
    "PackageObjectTypeDef",
    "PackageVersionInputConfigTypeDef",
    "PackageVersionOutputConfigTypeDef",
    "ProvisionDeviceRequestRequestTypeDef",
    "ProvisionDeviceResponseTypeDef",
    "RegisterPackageVersionRequestRequestTypeDef",
    "RemoveApplicationInstanceRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "StaticIpConnectionInfoTypeDef",
    "StorageLocationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDeviceMetadataRequestRequestTypeDef",
    "UpdateDeviceMetadataResponseTypeDef",
)

AlternateSoftwareMetadataTypeDef = TypedDict(
    "AlternateSoftwareMetadataTypeDef",
    {
        "Version": NotRequired[str],
    },
)

ApplicationInstanceTypeDef = TypedDict(
    "ApplicationInstanceTypeDef",
    {
        "ApplicationInstanceId": NotRequired[str],
        "Arn": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "DefaultRuntimeContextDevice": NotRequired[str],
        "DefaultRuntimeContextDeviceName": NotRequired[str],
        "Description": NotRequired[str],
        "HealthStatus": NotRequired[ApplicationInstanceHealthStatusType],
        "Name": NotRequired[str],
        "Status": NotRequired[ApplicationInstanceStatusType],
        "StatusDescription": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)

CreateApplicationInstanceRequestRequestTypeDef = TypedDict(
    "CreateApplicationInstanceRequestRequestTypeDef",
    {
        "DefaultRuntimeContextDevice": str,
        "ManifestPayload": "ManifestPayloadTypeDef",
        "ApplicationInstanceIdToReplace": NotRequired[str],
        "Description": NotRequired[str],
        "ManifestOverridesPayload": NotRequired["ManifestOverridesPayloadTypeDef"],
        "Name": NotRequired[str],
        "RuntimeRoleArn": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateApplicationInstanceResponseTypeDef = TypedDict(
    "CreateApplicationInstanceResponseTypeDef",
    {
        "ApplicationInstanceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateJobForDevicesRequestRequestTypeDef = TypedDict(
    "CreateJobForDevicesRequestRequestTypeDef",
    {
        "DeviceIds": Sequence[str],
        "DeviceJobConfig": "DeviceJobConfigTypeDef",
        "JobType": Literal["OTA"],
    },
)

CreateJobForDevicesResponseTypeDef = TypedDict(
    "CreateJobForDevicesResponseTypeDef",
    {
        "Jobs": List["JobTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateNodeFromTemplateJobRequestRequestTypeDef = TypedDict(
    "CreateNodeFromTemplateJobRequestRequestTypeDef",
    {
        "NodeName": str,
        "OutputPackageName": str,
        "OutputPackageVersion": str,
        "TemplateParameters": Mapping[str, str],
        "TemplateType": Literal["RTSP_CAMERA_STREAM"],
        "JobTags": NotRequired[Sequence["JobResourceTagsTypeDef"]],
        "NodeDescription": NotRequired[str],
    },
)

CreateNodeFromTemplateJobResponseTypeDef = TypedDict(
    "CreateNodeFromTemplateJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePackageImportJobRequestRequestTypeDef = TypedDict(
    "CreatePackageImportJobRequestRequestTypeDef",
    {
        "ClientToken": str,
        "InputConfig": "PackageImportJobInputConfigTypeDef",
        "JobType": PackageImportJobTypeType,
        "OutputConfig": "PackageImportJobOutputConfigTypeDef",
        "JobTags": NotRequired[Sequence["JobResourceTagsTypeDef"]],
    },
)

CreatePackageImportJobResponseTypeDef = TypedDict(
    "CreatePackageImportJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePackageRequestRequestTypeDef = TypedDict(
    "CreatePackageRequestRequestTypeDef",
    {
        "PackageName": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreatePackageResponseTypeDef = TypedDict(
    "CreatePackageResponseTypeDef",
    {
        "Arn": str,
        "PackageId": str,
        "StorageLocation": "StorageLocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDeviceRequestRequestTypeDef = TypedDict(
    "DeleteDeviceRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)

DeleteDeviceResponseTypeDef = TypedDict(
    "DeleteDeviceResponseTypeDef",
    {
        "DeviceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePackageRequestRequestTypeDef = TypedDict(
    "DeletePackageRequestRequestTypeDef",
    {
        "PackageId": str,
        "ForceDelete": NotRequired[bool],
    },
)

DeregisterPackageVersionRequestRequestTypeDef = TypedDict(
    "DeregisterPackageVersionRequestRequestTypeDef",
    {
        "PackageId": str,
        "PackageVersion": str,
        "PatchVersion": str,
        "OwnerAccount": NotRequired[str],
        "UpdatedLatestPatchVersion": NotRequired[str],
    },
)

DescribeApplicationInstanceDetailsRequestRequestTypeDef = TypedDict(
    "DescribeApplicationInstanceDetailsRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
    },
)

DescribeApplicationInstanceDetailsResponseTypeDef = TypedDict(
    "DescribeApplicationInstanceDetailsResponseTypeDef",
    {
        "ApplicationInstanceId": str,
        "ApplicationInstanceIdToReplace": str,
        "CreatedTime": datetime,
        "DefaultRuntimeContextDevice": str,
        "Description": str,
        "ManifestOverridesPayload": "ManifestOverridesPayloadTypeDef",
        "ManifestPayload": "ManifestPayloadTypeDef",
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeApplicationInstanceRequestRequestTypeDef = TypedDict(
    "DescribeApplicationInstanceRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
    },
)

DescribeApplicationInstanceResponseTypeDef = TypedDict(
    "DescribeApplicationInstanceResponseTypeDef",
    {
        "ApplicationInstanceId": str,
        "ApplicationInstanceIdToReplace": str,
        "Arn": str,
        "CreatedTime": datetime,
        "DefaultRuntimeContextDevice": str,
        "DefaultRuntimeContextDeviceName": str,
        "Description": str,
        "HealthStatus": ApplicationInstanceHealthStatusType,
        "LastUpdatedTime": datetime,
        "Name": str,
        "RuntimeRoleArn": str,
        "Status": ApplicationInstanceStatusType,
        "StatusDescription": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeviceJobRequestRequestTypeDef = TypedDict(
    "DescribeDeviceJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeDeviceJobResponseTypeDef = TypedDict(
    "DescribeDeviceJobResponseTypeDef",
    {
        "CreatedTime": datetime,
        "DeviceArn": str,
        "DeviceId": str,
        "DeviceName": str,
        "DeviceType": DeviceTypeType,
        "ImageVersion": str,
        "JobId": str,
        "Status": UpdateProgressType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeviceRequestRequestTypeDef = TypedDict(
    "DescribeDeviceRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)

DescribeDeviceResponseTypeDef = TypedDict(
    "DescribeDeviceResponseTypeDef",
    {
        "AlternateSoftwares": List["AlternateSoftwareMetadataTypeDef"],
        "Arn": str,
        "CreatedTime": datetime,
        "CurrentNetworkingStatus": "NetworkStatusTypeDef",
        "CurrentSoftware": str,
        "Description": str,
        "DeviceConnectionStatus": DeviceConnectionStatusType,
        "DeviceId": str,
        "LatestAlternateSoftware": str,
        "LatestSoftware": str,
        "LeaseExpirationTime": datetime,
        "Name": str,
        "NetworkingConfiguration": "NetworkPayloadTypeDef",
        "ProvisioningStatus": DeviceStatusType,
        "SerialNumber": str,
        "Tags": Dict[str, str],
        "Type": DeviceTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNodeFromTemplateJobRequestRequestTypeDef = TypedDict(
    "DescribeNodeFromTemplateJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeNodeFromTemplateJobResponseTypeDef = TypedDict(
    "DescribeNodeFromTemplateJobResponseTypeDef",
    {
        "CreatedTime": datetime,
        "JobId": str,
        "JobTags": List["JobResourceTagsTypeDef"],
        "LastUpdatedTime": datetime,
        "NodeDescription": str,
        "NodeName": str,
        "OutputPackageName": str,
        "OutputPackageVersion": str,
        "Status": NodeFromTemplateJobStatusType,
        "StatusMessage": str,
        "TemplateParameters": Dict[str, str],
        "TemplateType": Literal["RTSP_CAMERA_STREAM"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNodeRequestRequestTypeDef = TypedDict(
    "DescribeNodeRequestRequestTypeDef",
    {
        "NodeId": str,
        "OwnerAccount": NotRequired[str],
    },
)

DescribeNodeResponseTypeDef = TypedDict(
    "DescribeNodeResponseTypeDef",
    {
        "AssetName": str,
        "Category": NodeCategoryType,
        "CreatedTime": datetime,
        "Description": str,
        "LastUpdatedTime": datetime,
        "Name": str,
        "NodeId": str,
        "NodeInterface": "NodeInterfaceTypeDef",
        "OwnerAccount": str,
        "PackageArn": str,
        "PackageId": str,
        "PackageName": str,
        "PackageVersion": str,
        "PatchVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePackageImportJobRequestRequestTypeDef = TypedDict(
    "DescribePackageImportJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribePackageImportJobResponseTypeDef = TypedDict(
    "DescribePackageImportJobResponseTypeDef",
    {
        "ClientToken": str,
        "CreatedTime": datetime,
        "InputConfig": "PackageImportJobInputConfigTypeDef",
        "JobId": str,
        "JobTags": List["JobResourceTagsTypeDef"],
        "JobType": PackageImportJobTypeType,
        "LastUpdatedTime": datetime,
        "Output": "PackageImportJobOutputTypeDef",
        "OutputConfig": "PackageImportJobOutputConfigTypeDef",
        "Status": PackageImportJobStatusType,
        "StatusMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePackageRequestRequestTypeDef = TypedDict(
    "DescribePackageRequestRequestTypeDef",
    {
        "PackageId": str,
    },
)

DescribePackageResponseTypeDef = TypedDict(
    "DescribePackageResponseTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
        "PackageId": str,
        "PackageName": str,
        "ReadAccessPrincipalArns": List[str],
        "StorageLocation": "StorageLocationTypeDef",
        "Tags": Dict[str, str],
        "WriteAccessPrincipalArns": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePackageVersionRequestRequestTypeDef = TypedDict(
    "DescribePackageVersionRequestRequestTypeDef",
    {
        "PackageId": str,
        "PackageVersion": str,
        "OwnerAccount": NotRequired[str],
        "PatchVersion": NotRequired[str],
    },
)

DescribePackageVersionResponseTypeDef = TypedDict(
    "DescribePackageVersionResponseTypeDef",
    {
        "IsLatestPatch": bool,
        "OwnerAccount": str,
        "PackageArn": str,
        "PackageId": str,
        "PackageName": str,
        "PackageVersion": str,
        "PatchVersion": str,
        "RegisteredTime": datetime,
        "Status": PackageVersionStatusType,
        "StatusDescription": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceJobConfigTypeDef = TypedDict(
    "DeviceJobConfigTypeDef",
    {
        "OTAJobConfig": NotRequired["OTAJobConfigTypeDef"],
    },
)

DeviceJobTypeDef = TypedDict(
    "DeviceJobTypeDef",
    {
        "CreatedTime": NotRequired[datetime],
        "DeviceId": NotRequired[str],
        "DeviceName": NotRequired[str],
        "JobId": NotRequired[str],
    },
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "CreatedTime": NotRequired[datetime],
        "DeviceId": NotRequired[str],
        "LastUpdatedTime": NotRequired[datetime],
        "LeaseExpirationTime": NotRequired[datetime],
        "Name": NotRequired[str],
        "ProvisioningStatus": NotRequired[DeviceStatusType],
    },
)

EthernetPayloadTypeDef = TypedDict(
    "EthernetPayloadTypeDef",
    {
        "ConnectionType": ConnectionTypeType,
        "StaticIpConnectionInfo": NotRequired["StaticIpConnectionInfoTypeDef"],
    },
)

EthernetStatusTypeDef = TypedDict(
    "EthernetStatusTypeDef",
    {
        "ConnectionStatus": NotRequired[NetworkConnectionStatusType],
        "HwAddress": NotRequired[str],
        "IpAddress": NotRequired[str],
    },
)

JobResourceTagsTypeDef = TypedDict(
    "JobResourceTagsTypeDef",
    {
        "ResourceType": Literal["PACKAGE"],
        "Tags": Mapping[str, str],
    },
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "DeviceId": NotRequired[str],
        "JobId": NotRequired[str],
    },
)

ListApplicationInstanceDependenciesRequestRequestTypeDef = TypedDict(
    "ListApplicationInstanceDependenciesRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListApplicationInstanceDependenciesResponseTypeDef = TypedDict(
    "ListApplicationInstanceDependenciesResponseTypeDef",
    {
        "NextToken": str,
        "PackageObjects": List["PackageObjectTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationInstanceNodeInstancesRequestRequestTypeDef = TypedDict(
    "ListApplicationInstanceNodeInstancesRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListApplicationInstanceNodeInstancesResponseTypeDef = TypedDict(
    "ListApplicationInstanceNodeInstancesResponseTypeDef",
    {
        "NextToken": str,
        "NodeInstances": List["NodeInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationInstancesRequestRequestTypeDef = TypedDict(
    "ListApplicationInstancesRequestRequestTypeDef",
    {
        "DeviceId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "StatusFilter": NotRequired[StatusFilterType],
    },
)

ListApplicationInstancesResponseTypeDef = TypedDict(
    "ListApplicationInstancesResponseTypeDef",
    {
        "ApplicationInstances": List["ApplicationInstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevicesJobsRequestRequestTypeDef = TypedDict(
    "ListDevicesJobsRequestRequestTypeDef",
    {
        "DeviceId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListDevicesJobsResponseTypeDef = TypedDict(
    "ListDevicesJobsResponseTypeDef",
    {
        "DeviceJobs": List["DeviceJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevicesRequestRequestTypeDef = TypedDict(
    "ListDevicesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {
        "Devices": List["DeviceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNodeFromTemplateJobsRequestRequestTypeDef = TypedDict(
    "ListNodeFromTemplateJobsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListNodeFromTemplateJobsResponseTypeDef = TypedDict(
    "ListNodeFromTemplateJobsResponseTypeDef",
    {
        "NextToken": str,
        "NodeFromTemplateJobs": List["NodeFromTemplateJobTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNodesRequestRequestTypeDef = TypedDict(
    "ListNodesRequestRequestTypeDef",
    {
        "Category": NotRequired[NodeCategoryType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "OwnerAccount": NotRequired[str],
        "PackageName": NotRequired[str],
        "PackageVersion": NotRequired[str],
        "PatchVersion": NotRequired[str],
    },
)

ListNodesResponseTypeDef = TypedDict(
    "ListNodesResponseTypeDef",
    {
        "NextToken": str,
        "Nodes": List["NodeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPackageImportJobsRequestRequestTypeDef = TypedDict(
    "ListPackageImportJobsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListPackageImportJobsResponseTypeDef = TypedDict(
    "ListPackageImportJobsResponseTypeDef",
    {
        "NextToken": str,
        "PackageImportJobs": List["PackageImportJobTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPackagesRequestRequestTypeDef = TypedDict(
    "ListPackagesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListPackagesResponseTypeDef = TypedDict(
    "ListPackagesResponseTypeDef",
    {
        "NextToken": str,
        "Packages": List["PackageListItemTypeDef"],
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

ManifestOverridesPayloadTypeDef = TypedDict(
    "ManifestOverridesPayloadTypeDef",
    {
        "PayloadData": NotRequired[str],
    },
)

ManifestPayloadTypeDef = TypedDict(
    "ManifestPayloadTypeDef",
    {
        "PayloadData": NotRequired[str],
    },
)

NetworkPayloadTypeDef = TypedDict(
    "NetworkPayloadTypeDef",
    {
        "Ethernet0": NotRequired["EthernetPayloadTypeDef"],
        "Ethernet1": NotRequired["EthernetPayloadTypeDef"],
        "Ntp": NotRequired["NtpPayloadTypeDef"],
    },
)

NetworkStatusTypeDef = TypedDict(
    "NetworkStatusTypeDef",
    {
        "Ethernet0Status": NotRequired["EthernetStatusTypeDef"],
        "Ethernet1Status": NotRequired["EthernetStatusTypeDef"],
        "LastUpdatedTime": NotRequired[datetime],
        "NtpStatus": NotRequired["NtpStatusTypeDef"],
    },
)

NodeFromTemplateJobTypeDef = TypedDict(
    "NodeFromTemplateJobTypeDef",
    {
        "CreatedTime": NotRequired[datetime],
        "JobId": NotRequired[str],
        "NodeName": NotRequired[str],
        "Status": NotRequired[NodeFromTemplateJobStatusType],
        "StatusMessage": NotRequired[str],
        "TemplateType": NotRequired[Literal["RTSP_CAMERA_STREAM"]],
    },
)

NodeInputPortTypeDef = TypedDict(
    "NodeInputPortTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "Description": NotRequired[str],
        "MaxConnections": NotRequired[int],
        "Name": NotRequired[str],
        "Type": NotRequired[PortTypeType],
    },
)

NodeInstanceTypeDef = TypedDict(
    "NodeInstanceTypeDef",
    {
        "CurrentStatus": NodeInstanceStatusType,
        "NodeInstanceId": str,
        "NodeId": NotRequired[str],
        "NodeName": NotRequired[str],
        "PackageName": NotRequired[str],
        "PackagePatchVersion": NotRequired[str],
        "PackageVersion": NotRequired[str],
    },
)

NodeInterfaceTypeDef = TypedDict(
    "NodeInterfaceTypeDef",
    {
        "Inputs": List["NodeInputPortTypeDef"],
        "Outputs": List["NodeOutputPortTypeDef"],
    },
)

NodeOutputPortTypeDef = TypedDict(
    "NodeOutputPortTypeDef",
    {
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[PortTypeType],
    },
)

NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "Category": NodeCategoryType,
        "CreatedTime": datetime,
        "Name": str,
        "NodeId": str,
        "PackageId": str,
        "PackageName": str,
        "PackageVersion": str,
        "PatchVersion": str,
        "Description": NotRequired[str],
        "OwnerAccount": NotRequired[str],
        "PackageArn": NotRequired[str],
    },
)

NtpPayloadTypeDef = TypedDict(
    "NtpPayloadTypeDef",
    {
        "NtpServers": List[str],
    },
)

NtpStatusTypeDef = TypedDict(
    "NtpStatusTypeDef",
    {
        "ConnectionStatus": NotRequired[NetworkConnectionStatusType],
        "IpAddress": NotRequired[str],
        "NtpServerName": NotRequired[str],
    },
)

OTAJobConfigTypeDef = TypedDict(
    "OTAJobConfigTypeDef",
    {
        "ImageVersion": str,
    },
)

OutPutS3LocationTypeDef = TypedDict(
    "OutPutS3LocationTypeDef",
    {
        "BucketName": str,
        "ObjectKey": str,
    },
)

PackageImportJobInputConfigTypeDef = TypedDict(
    "PackageImportJobInputConfigTypeDef",
    {
        "PackageVersionInputConfig": NotRequired["PackageVersionInputConfigTypeDef"],
    },
)

PackageImportJobOutputConfigTypeDef = TypedDict(
    "PackageImportJobOutputConfigTypeDef",
    {
        "PackageVersionOutputConfig": NotRequired["PackageVersionOutputConfigTypeDef"],
    },
)

PackageImportJobOutputTypeDef = TypedDict(
    "PackageImportJobOutputTypeDef",
    {
        "OutputS3Location": "OutPutS3LocationTypeDef",
        "PackageId": str,
        "PackageVersion": str,
        "PatchVersion": str,
    },
)

PackageImportJobTypeDef = TypedDict(
    "PackageImportJobTypeDef",
    {
        "CreatedTime": NotRequired[datetime],
        "JobId": NotRequired[str],
        "JobType": NotRequired[PackageImportJobTypeType],
        "LastUpdatedTime": NotRequired[datetime],
        "Status": NotRequired[PackageImportJobStatusType],
        "StatusMessage": NotRequired[str],
    },
)

PackageListItemTypeDef = TypedDict(
    "PackageListItemTypeDef",
    {
        "Arn": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "PackageId": NotRequired[str],
        "PackageName": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)

PackageObjectTypeDef = TypedDict(
    "PackageObjectTypeDef",
    {
        "Name": str,
        "PackageVersion": str,
        "PatchVersion": str,
    },
)

PackageVersionInputConfigTypeDef = TypedDict(
    "PackageVersionInputConfigTypeDef",
    {
        "S3Location": "S3LocationTypeDef",
    },
)

PackageVersionOutputConfigTypeDef = TypedDict(
    "PackageVersionOutputConfigTypeDef",
    {
        "PackageName": str,
        "PackageVersion": str,
        "MarkLatest": NotRequired[bool],
    },
)

ProvisionDeviceRequestRequestTypeDef = TypedDict(
    "ProvisionDeviceRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "NetworkingConfiguration": NotRequired["NetworkPayloadTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

ProvisionDeviceResponseTypeDef = TypedDict(
    "ProvisionDeviceResponseTypeDef",
    {
        "Arn": str,
        "Certificates": bytes,
        "DeviceId": str,
        "IotThingName": str,
        "Status": DeviceStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterPackageVersionRequestRequestTypeDef = TypedDict(
    "RegisterPackageVersionRequestRequestTypeDef",
    {
        "PackageId": str,
        "PackageVersion": str,
        "PatchVersion": str,
        "MarkLatest": NotRequired[bool],
        "OwnerAccount": NotRequired[str],
    },
)

RemoveApplicationInstanceRequestRequestTypeDef = TypedDict(
    "RemoveApplicationInstanceRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
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

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "BucketName": str,
        "ObjectKey": str,
        "Region": NotRequired[str],
    },
)

StaticIpConnectionInfoTypeDef = TypedDict(
    "StaticIpConnectionInfoTypeDef",
    {
        "DefaultGateway": str,
        "Dns": List[str],
        "IpAddress": str,
        "Mask": str,
    },
)

StorageLocationTypeDef = TypedDict(
    "StorageLocationTypeDef",
    {
        "BinaryPrefixLocation": str,
        "Bucket": str,
        "GeneratedPrefixLocation": str,
        "ManifestPrefixLocation": str,
        "RepoPrefixLocation": str,
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

UpdateDeviceMetadataRequestRequestTypeDef = TypedDict(
    "UpdateDeviceMetadataRequestRequestTypeDef",
    {
        "DeviceId": str,
        "Description": NotRequired[str],
    },
)

UpdateDeviceMetadataResponseTypeDef = TypedDict(
    "UpdateDeviceMetadataResponseTypeDef",
    {
        "DeviceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
