"""
Type annotations for snowball service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/type_defs.html)

Usage::

    ```python
    from mypy_boto3_snowball.type_defs import AddressTypeDef

    data: AddressTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    ClusterStateType,
    DeviceServiceNameType,
    JobStateType,
    JobTypeType,
    LongTermPricingTypeType,
    RemoteManagementType,
    ShipmentStateType,
    ShippingLabelStatusType,
    ShippingOptionType,
    SnowballCapacityType,
    SnowballTypeType,
    TransferOptionType,
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
    "AddressTypeDef",
    "CancelClusterRequestRequestTypeDef",
    "CancelJobRequestRequestTypeDef",
    "ClusterListEntryTypeDef",
    "ClusterMetadataTypeDef",
    "CompatibleImageTypeDef",
    "CreateAddressRequestRequestTypeDef",
    "CreateAddressResultTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "CreateClusterResultTypeDef",
    "CreateJobRequestRequestTypeDef",
    "CreateJobResultTypeDef",
    "CreateLongTermPricingRequestRequestTypeDef",
    "CreateLongTermPricingResultTypeDef",
    "CreateReturnShippingLabelRequestRequestTypeDef",
    "CreateReturnShippingLabelResultTypeDef",
    "DataTransferTypeDef",
    "DescribeAddressRequestRequestTypeDef",
    "DescribeAddressResultTypeDef",
    "DescribeAddressesRequestRequestTypeDef",
    "DescribeAddressesResultTypeDef",
    "DescribeClusterRequestRequestTypeDef",
    "DescribeClusterResultTypeDef",
    "DescribeJobRequestRequestTypeDef",
    "DescribeJobResultTypeDef",
    "DescribeReturnShippingLabelRequestRequestTypeDef",
    "DescribeReturnShippingLabelResultTypeDef",
    "DeviceConfigurationTypeDef",
    "Ec2AmiResourceTypeDef",
    "EventTriggerDefinitionTypeDef",
    "GetJobManifestRequestRequestTypeDef",
    "GetJobManifestResultTypeDef",
    "GetJobUnlockCodeRequestRequestTypeDef",
    "GetJobUnlockCodeResultTypeDef",
    "GetSnowballUsageResultTypeDef",
    "GetSoftwareUpdatesRequestRequestTypeDef",
    "GetSoftwareUpdatesResultTypeDef",
    "INDTaxDocumentsTypeDef",
    "JobListEntryTypeDef",
    "JobLogsTypeDef",
    "JobMetadataTypeDef",
    "JobResourceTypeDef",
    "KeyRangeTypeDef",
    "LambdaResourceTypeDef",
    "ListClusterJobsRequestRequestTypeDef",
    "ListClusterJobsResultTypeDef",
    "ListClustersRequestRequestTypeDef",
    "ListClustersResultTypeDef",
    "ListCompatibleImagesRequestRequestTypeDef",
    "ListCompatibleImagesResultTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListJobsResultTypeDef",
    "ListLongTermPricingRequestRequestTypeDef",
    "ListLongTermPricingResultTypeDef",
    "LongTermPricingListEntryTypeDef",
    "NFSOnDeviceServiceConfigurationTypeDef",
    "NotificationTypeDef",
    "OnDeviceServiceConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "S3ResourceTypeDef",
    "ShipmentTypeDef",
    "ShippingDetailsTypeDef",
    "SnowconeDeviceConfigurationTypeDef",
    "TGWOnDeviceServiceConfigurationTypeDef",
    "TargetOnDeviceServiceTypeDef",
    "TaxDocumentsTypeDef",
    "UpdateClusterRequestRequestTypeDef",
    "UpdateJobRequestRequestTypeDef",
    "UpdateJobShipmentStateRequestRequestTypeDef",
    "UpdateLongTermPricingRequestRequestTypeDef",
    "WirelessConnectionTypeDef",
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "AddressId": NotRequired[str],
        "Name": NotRequired[str],
        "Company": NotRequired[str],
        "Street1": NotRequired[str],
        "Street2": NotRequired[str],
        "Street3": NotRequired[str],
        "City": NotRequired[str],
        "StateOrProvince": NotRequired[str],
        "PrefectureOrDistrict": NotRequired[str],
        "Landmark": NotRequired[str],
        "Country": NotRequired[str],
        "PostalCode": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "IsRestricted": NotRequired[bool],
    },
)

CancelClusterRequestRequestTypeDef = TypedDict(
    "CancelClusterRequestRequestTypeDef",
    {
        "ClusterId": str,
    },
)

CancelJobRequestRequestTypeDef = TypedDict(
    "CancelJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

ClusterListEntryTypeDef = TypedDict(
    "ClusterListEntryTypeDef",
    {
        "ClusterId": NotRequired[str],
        "ClusterState": NotRequired[ClusterStateType],
        "CreationDate": NotRequired[datetime],
        "Description": NotRequired[str],
    },
)

ClusterMetadataTypeDef = TypedDict(
    "ClusterMetadataTypeDef",
    {
        "ClusterId": NotRequired[str],
        "Description": NotRequired[str],
        "KmsKeyARN": NotRequired[str],
        "RoleARN": NotRequired[str],
        "ClusterState": NotRequired[ClusterStateType],
        "JobType": NotRequired[JobTypeType],
        "SnowballType": NotRequired[SnowballTypeType],
        "CreationDate": NotRequired[datetime],
        "Resources": NotRequired["JobResourceTypeDef"],
        "AddressId": NotRequired[str],
        "ShippingOption": NotRequired[ShippingOptionType],
        "Notification": NotRequired["NotificationTypeDef"],
        "ForwardingAddressId": NotRequired[str],
        "TaxDocuments": NotRequired["TaxDocumentsTypeDef"],
        "OnDeviceServiceConfiguration": NotRequired["OnDeviceServiceConfigurationTypeDef"],
    },
)

CompatibleImageTypeDef = TypedDict(
    "CompatibleImageTypeDef",
    {
        "AmiId": NotRequired[str],
        "Name": NotRequired[str],
    },
)

CreateAddressRequestRequestTypeDef = TypedDict(
    "CreateAddressRequestRequestTypeDef",
    {
        "Address": "AddressTypeDef",
    },
)

CreateAddressResultTypeDef = TypedDict(
    "CreateAddressResultTypeDef",
    {
        "AddressId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateClusterRequestRequestTypeDef = TypedDict(
    "CreateClusterRequestRequestTypeDef",
    {
        "JobType": JobTypeType,
        "Resources": "JobResourceTypeDef",
        "AddressId": str,
        "RoleARN": str,
        "SnowballType": SnowballTypeType,
        "ShippingOption": ShippingOptionType,
        "OnDeviceServiceConfiguration": NotRequired["OnDeviceServiceConfigurationTypeDef"],
        "Description": NotRequired[str],
        "KmsKeyARN": NotRequired[str],
        "Notification": NotRequired["NotificationTypeDef"],
        "ForwardingAddressId": NotRequired[str],
        "TaxDocuments": NotRequired["TaxDocumentsTypeDef"],
        "RemoteManagement": NotRequired[RemoteManagementType],
    },
)

CreateClusterResultTypeDef = TypedDict(
    "CreateClusterResultTypeDef",
    {
        "ClusterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateJobRequestRequestTypeDef = TypedDict(
    "CreateJobRequestRequestTypeDef",
    {
        "JobType": NotRequired[JobTypeType],
        "Resources": NotRequired["JobResourceTypeDef"],
        "OnDeviceServiceConfiguration": NotRequired["OnDeviceServiceConfigurationTypeDef"],
        "Description": NotRequired[str],
        "AddressId": NotRequired[str],
        "KmsKeyARN": NotRequired[str],
        "RoleARN": NotRequired[str],
        "SnowballCapacityPreference": NotRequired[SnowballCapacityType],
        "ShippingOption": NotRequired[ShippingOptionType],
        "Notification": NotRequired["NotificationTypeDef"],
        "ClusterId": NotRequired[str],
        "SnowballType": NotRequired[SnowballTypeType],
        "ForwardingAddressId": NotRequired[str],
        "TaxDocuments": NotRequired["TaxDocumentsTypeDef"],
        "DeviceConfiguration": NotRequired["DeviceConfigurationTypeDef"],
        "RemoteManagement": NotRequired[RemoteManagementType],
        "LongTermPricingId": NotRequired[str],
    },
)

CreateJobResultTypeDef = TypedDict(
    "CreateJobResultTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLongTermPricingRequestRequestTypeDef = TypedDict(
    "CreateLongTermPricingRequestRequestTypeDef",
    {
        "LongTermPricingType": LongTermPricingTypeType,
        "IsLongTermPricingAutoRenew": NotRequired[bool],
        "SnowballType": NotRequired[SnowballTypeType],
    },
)

CreateLongTermPricingResultTypeDef = TypedDict(
    "CreateLongTermPricingResultTypeDef",
    {
        "LongTermPricingId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateReturnShippingLabelRequestRequestTypeDef = TypedDict(
    "CreateReturnShippingLabelRequestRequestTypeDef",
    {
        "JobId": str,
        "ShippingOption": NotRequired[ShippingOptionType],
    },
)

CreateReturnShippingLabelResultTypeDef = TypedDict(
    "CreateReturnShippingLabelResultTypeDef",
    {
        "Status": ShippingLabelStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataTransferTypeDef = TypedDict(
    "DataTransferTypeDef",
    {
        "BytesTransferred": NotRequired[int],
        "ObjectsTransferred": NotRequired[int],
        "TotalBytes": NotRequired[int],
        "TotalObjects": NotRequired[int],
    },
)

DescribeAddressRequestRequestTypeDef = TypedDict(
    "DescribeAddressRequestRequestTypeDef",
    {
        "AddressId": str,
    },
)

DescribeAddressResultTypeDef = TypedDict(
    "DescribeAddressResultTypeDef",
    {
        "Address": "AddressTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAddressesRequestRequestTypeDef = TypedDict(
    "DescribeAddressesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeAddressesResultTypeDef = TypedDict(
    "DescribeAddressesResultTypeDef",
    {
        "Addresses": List["AddressTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClusterRequestRequestTypeDef = TypedDict(
    "DescribeClusterRequestRequestTypeDef",
    {
        "ClusterId": str,
    },
)

DescribeClusterResultTypeDef = TypedDict(
    "DescribeClusterResultTypeDef",
    {
        "ClusterMetadata": "ClusterMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobRequestRequestTypeDef = TypedDict(
    "DescribeJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeJobResultTypeDef = TypedDict(
    "DescribeJobResultTypeDef",
    {
        "JobMetadata": "JobMetadataTypeDef",
        "SubJobMetadata": List["JobMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReturnShippingLabelRequestRequestTypeDef = TypedDict(
    "DescribeReturnShippingLabelRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeReturnShippingLabelResultTypeDef = TypedDict(
    "DescribeReturnShippingLabelResultTypeDef",
    {
        "Status": ShippingLabelStatusType,
        "ExpirationDate": datetime,
        "ReturnShippingLabelURI": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceConfigurationTypeDef = TypedDict(
    "DeviceConfigurationTypeDef",
    {
        "SnowconeDeviceConfiguration": NotRequired["SnowconeDeviceConfigurationTypeDef"],
    },
)

Ec2AmiResourceTypeDef = TypedDict(
    "Ec2AmiResourceTypeDef",
    {
        "AmiId": str,
        "SnowballAmiId": NotRequired[str],
    },
)

EventTriggerDefinitionTypeDef = TypedDict(
    "EventTriggerDefinitionTypeDef",
    {
        "EventResourceARN": NotRequired[str],
    },
)

GetJobManifestRequestRequestTypeDef = TypedDict(
    "GetJobManifestRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

GetJobManifestResultTypeDef = TypedDict(
    "GetJobManifestResultTypeDef",
    {
        "ManifestURI": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobUnlockCodeRequestRequestTypeDef = TypedDict(
    "GetJobUnlockCodeRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

GetJobUnlockCodeResultTypeDef = TypedDict(
    "GetJobUnlockCodeResultTypeDef",
    {
        "UnlockCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSnowballUsageResultTypeDef = TypedDict(
    "GetSnowballUsageResultTypeDef",
    {
        "SnowballLimit": int,
        "SnowballsInUse": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSoftwareUpdatesRequestRequestTypeDef = TypedDict(
    "GetSoftwareUpdatesRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

GetSoftwareUpdatesResultTypeDef = TypedDict(
    "GetSoftwareUpdatesResultTypeDef",
    {
        "UpdatesURI": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

INDTaxDocumentsTypeDef = TypedDict(
    "INDTaxDocumentsTypeDef",
    {
        "GSTIN": NotRequired[str],
    },
)

JobListEntryTypeDef = TypedDict(
    "JobListEntryTypeDef",
    {
        "JobId": NotRequired[str],
        "JobState": NotRequired[JobStateType],
        "IsMaster": NotRequired[bool],
        "JobType": NotRequired[JobTypeType],
        "SnowballType": NotRequired[SnowballTypeType],
        "CreationDate": NotRequired[datetime],
        "Description": NotRequired[str],
    },
)

JobLogsTypeDef = TypedDict(
    "JobLogsTypeDef",
    {
        "JobCompletionReportURI": NotRequired[str],
        "JobSuccessLogURI": NotRequired[str],
        "JobFailureLogURI": NotRequired[str],
    },
)

JobMetadataTypeDef = TypedDict(
    "JobMetadataTypeDef",
    {
        "JobId": NotRequired[str],
        "JobState": NotRequired[JobStateType],
        "JobType": NotRequired[JobTypeType],
        "SnowballType": NotRequired[SnowballTypeType],
        "CreationDate": NotRequired[datetime],
        "Resources": NotRequired["JobResourceTypeDef"],
        "Description": NotRequired[str],
        "KmsKeyARN": NotRequired[str],
        "RoleARN": NotRequired[str],
        "AddressId": NotRequired[str],
        "ShippingDetails": NotRequired["ShippingDetailsTypeDef"],
        "SnowballCapacityPreference": NotRequired[SnowballCapacityType],
        "Notification": NotRequired["NotificationTypeDef"],
        "DataTransferProgress": NotRequired["DataTransferTypeDef"],
        "JobLogInfo": NotRequired["JobLogsTypeDef"],
        "ClusterId": NotRequired[str],
        "ForwardingAddressId": NotRequired[str],
        "TaxDocuments": NotRequired["TaxDocumentsTypeDef"],
        "DeviceConfiguration": NotRequired["DeviceConfigurationTypeDef"],
        "RemoteManagement": NotRequired[RemoteManagementType],
        "LongTermPricingId": NotRequired[str],
        "OnDeviceServiceConfiguration": NotRequired["OnDeviceServiceConfigurationTypeDef"],
    },
)

JobResourceTypeDef = TypedDict(
    "JobResourceTypeDef",
    {
        "S3Resources": NotRequired[Sequence["S3ResourceTypeDef"]],
        "LambdaResources": NotRequired[Sequence["LambdaResourceTypeDef"]],
        "Ec2AmiResources": NotRequired[Sequence["Ec2AmiResourceTypeDef"]],
    },
)

KeyRangeTypeDef = TypedDict(
    "KeyRangeTypeDef",
    {
        "BeginMarker": NotRequired[str],
        "EndMarker": NotRequired[str],
    },
)

LambdaResourceTypeDef = TypedDict(
    "LambdaResourceTypeDef",
    {
        "LambdaArn": NotRequired[str],
        "EventTriggers": NotRequired[Sequence["EventTriggerDefinitionTypeDef"]],
    },
)

ListClusterJobsRequestRequestTypeDef = TypedDict(
    "ListClusterJobsRequestRequestTypeDef",
    {
        "ClusterId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListClusterJobsResultTypeDef = TypedDict(
    "ListClusterJobsResultTypeDef",
    {
        "JobListEntries": List["JobListEntryTypeDef"],
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

ListClustersResultTypeDef = TypedDict(
    "ListClustersResultTypeDef",
    {
        "ClusterListEntries": List["ClusterListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCompatibleImagesRequestRequestTypeDef = TypedDict(
    "ListCompatibleImagesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListCompatibleImagesResultTypeDef = TypedDict(
    "ListCompatibleImagesResultTypeDef",
    {
        "CompatibleImages": List["CompatibleImageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef",
    {
        "JobListEntries": List["JobListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLongTermPricingRequestRequestTypeDef = TypedDict(
    "ListLongTermPricingRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListLongTermPricingResultTypeDef = TypedDict(
    "ListLongTermPricingResultTypeDef",
    {
        "LongTermPricingEntries": List["LongTermPricingListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LongTermPricingListEntryTypeDef = TypedDict(
    "LongTermPricingListEntryTypeDef",
    {
        "LongTermPricingId": NotRequired[str],
        "LongTermPricingEndDate": NotRequired[datetime],
        "LongTermPricingStartDate": NotRequired[datetime],
        "LongTermPricingType": NotRequired[LongTermPricingTypeType],
        "CurrentActiveJob": NotRequired[str],
        "ReplacementJob": NotRequired[str],
        "IsLongTermPricingAutoRenew": NotRequired[bool],
        "LongTermPricingStatus": NotRequired[str],
        "SnowballType": NotRequired[SnowballTypeType],
        "JobIds": NotRequired[List[str]],
    },
)

NFSOnDeviceServiceConfigurationTypeDef = TypedDict(
    "NFSOnDeviceServiceConfigurationTypeDef",
    {
        "StorageLimit": NotRequired[int],
        "StorageUnit": NotRequired[Literal["TB"]],
    },
)

NotificationTypeDef = TypedDict(
    "NotificationTypeDef",
    {
        "SnsTopicARN": NotRequired[str],
        "JobStatesToNotify": NotRequired[Sequence[JobStateType]],
        "NotifyAll": NotRequired[bool],
    },
)

OnDeviceServiceConfigurationTypeDef = TypedDict(
    "OnDeviceServiceConfigurationTypeDef",
    {
        "NFSOnDeviceService": NotRequired["NFSOnDeviceServiceConfigurationTypeDef"],
        "TGWOnDeviceService": NotRequired["TGWOnDeviceServiceConfigurationTypeDef"],
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

S3ResourceTypeDef = TypedDict(
    "S3ResourceTypeDef",
    {
        "BucketArn": NotRequired[str],
        "KeyRange": NotRequired["KeyRangeTypeDef"],
        "TargetOnDeviceServices": NotRequired[Sequence["TargetOnDeviceServiceTypeDef"]],
    },
)

ShipmentTypeDef = TypedDict(
    "ShipmentTypeDef",
    {
        "Status": NotRequired[str],
        "TrackingNumber": NotRequired[str],
    },
)

ShippingDetailsTypeDef = TypedDict(
    "ShippingDetailsTypeDef",
    {
        "ShippingOption": NotRequired[ShippingOptionType],
        "InboundShipment": NotRequired["ShipmentTypeDef"],
        "OutboundShipment": NotRequired["ShipmentTypeDef"],
    },
)

SnowconeDeviceConfigurationTypeDef = TypedDict(
    "SnowconeDeviceConfigurationTypeDef",
    {
        "WirelessConnection": NotRequired["WirelessConnectionTypeDef"],
    },
)

TGWOnDeviceServiceConfigurationTypeDef = TypedDict(
    "TGWOnDeviceServiceConfigurationTypeDef",
    {
        "StorageLimit": NotRequired[int],
        "StorageUnit": NotRequired[Literal["TB"]],
    },
)

TargetOnDeviceServiceTypeDef = TypedDict(
    "TargetOnDeviceServiceTypeDef",
    {
        "ServiceName": NotRequired[DeviceServiceNameType],
        "TransferOption": NotRequired[TransferOptionType],
    },
)

TaxDocumentsTypeDef = TypedDict(
    "TaxDocumentsTypeDef",
    {
        "IND": NotRequired["INDTaxDocumentsTypeDef"],
    },
)

UpdateClusterRequestRequestTypeDef = TypedDict(
    "UpdateClusterRequestRequestTypeDef",
    {
        "ClusterId": str,
        "RoleARN": NotRequired[str],
        "Description": NotRequired[str],
        "Resources": NotRequired["JobResourceTypeDef"],
        "OnDeviceServiceConfiguration": NotRequired["OnDeviceServiceConfigurationTypeDef"],
        "AddressId": NotRequired[str],
        "ShippingOption": NotRequired[ShippingOptionType],
        "Notification": NotRequired["NotificationTypeDef"],
        "ForwardingAddressId": NotRequired[str],
    },
)

UpdateJobRequestRequestTypeDef = TypedDict(
    "UpdateJobRequestRequestTypeDef",
    {
        "JobId": str,
        "RoleARN": NotRequired[str],
        "Notification": NotRequired["NotificationTypeDef"],
        "Resources": NotRequired["JobResourceTypeDef"],
        "OnDeviceServiceConfiguration": NotRequired["OnDeviceServiceConfigurationTypeDef"],
        "AddressId": NotRequired[str],
        "ShippingOption": NotRequired[ShippingOptionType],
        "Description": NotRequired[str],
        "SnowballCapacityPreference": NotRequired[SnowballCapacityType],
        "ForwardingAddressId": NotRequired[str],
    },
)

UpdateJobShipmentStateRequestRequestTypeDef = TypedDict(
    "UpdateJobShipmentStateRequestRequestTypeDef",
    {
        "JobId": str,
        "ShipmentState": ShipmentStateType,
    },
)

UpdateLongTermPricingRequestRequestTypeDef = TypedDict(
    "UpdateLongTermPricingRequestRequestTypeDef",
    {
        "LongTermPricingId": str,
        "ReplacementJob": NotRequired[str],
        "IsLongTermPricingAutoRenew": NotRequired[bool],
    },
)

WirelessConnectionTypeDef = TypedDict(
    "WirelessConnectionTypeDef",
    {
        "IsWifiEnabled": NotRequired[bool],
    },
)
