"""
Type annotations for cloudhsm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudhsm.type_defs import AddTagsToResourceRequestRequestTypeDef

    data: AddTagsToResourceRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import ClientVersionType, CloudHsmObjectStateType, HsmStatusType

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddTagsToResourceRequestRequestTypeDef",
    "AddTagsToResourceResponseTypeDef",
    "CreateHapgRequestRequestTypeDef",
    "CreateHapgResponseTypeDef",
    "CreateHsmRequestRequestTypeDef",
    "CreateHsmResponseTypeDef",
    "CreateLunaClientRequestRequestTypeDef",
    "CreateLunaClientResponseTypeDef",
    "DeleteHapgRequestRequestTypeDef",
    "DeleteHapgResponseTypeDef",
    "DeleteHsmRequestRequestTypeDef",
    "DeleteHsmResponseTypeDef",
    "DeleteLunaClientRequestRequestTypeDef",
    "DeleteLunaClientResponseTypeDef",
    "DescribeHapgRequestRequestTypeDef",
    "DescribeHapgResponseTypeDef",
    "DescribeHsmRequestRequestTypeDef",
    "DescribeHsmResponseTypeDef",
    "DescribeLunaClientRequestRequestTypeDef",
    "DescribeLunaClientResponseTypeDef",
    "GetConfigRequestRequestTypeDef",
    "GetConfigResponseTypeDef",
    "ListAvailableZonesResponseTypeDef",
    "ListHapgsRequestRequestTypeDef",
    "ListHapgsResponseTypeDef",
    "ListHsmsRequestRequestTypeDef",
    "ListHsmsResponseTypeDef",
    "ListLunaClientsRequestRequestTypeDef",
    "ListLunaClientsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ModifyHapgRequestRequestTypeDef",
    "ModifyHapgResponseTypeDef",
    "ModifyHsmRequestRequestTypeDef",
    "ModifyHsmResponseTypeDef",
    "ModifyLunaClientRequestRequestTypeDef",
    "ModifyLunaClientResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RemoveTagsFromResourceRequestRequestTypeDef",
    "RemoveTagsFromResourceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
)

AddTagsToResourceRequestRequestTypeDef = TypedDict(
    "AddTagsToResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagList": Sequence["TagTypeDef"],
    },
)

AddTagsToResourceResponseTypeDef = TypedDict(
    "AddTagsToResourceResponseTypeDef",
    {
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateHapgRequestRequestTypeDef = TypedDict(
    "CreateHapgRequestRequestTypeDef",
    {
        "Label": str,
    },
)

CreateHapgResponseTypeDef = TypedDict(
    "CreateHapgResponseTypeDef",
    {
        "HapgArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateHsmRequestRequestTypeDef = TypedDict(
    "CreateHsmRequestRequestTypeDef",
    {
        "SubnetId": str,
        "SshKey": str,
        "IamRoleArn": str,
        "SubscriptionType": Literal["PRODUCTION"],
        "EniIp": NotRequired[str],
        "ExternalId": NotRequired[str],
        "ClientToken": NotRequired[str],
        "SyslogIp": NotRequired[str],
    },
)

CreateHsmResponseTypeDef = TypedDict(
    "CreateHsmResponseTypeDef",
    {
        "HsmArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLunaClientRequestRequestTypeDef = TypedDict(
    "CreateLunaClientRequestRequestTypeDef",
    {
        "Certificate": str,
        "Label": NotRequired[str],
    },
)

CreateLunaClientResponseTypeDef = TypedDict(
    "CreateLunaClientResponseTypeDef",
    {
        "ClientArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteHapgRequestRequestTypeDef = TypedDict(
    "DeleteHapgRequestRequestTypeDef",
    {
        "HapgArn": str,
    },
)

DeleteHapgResponseTypeDef = TypedDict(
    "DeleteHapgResponseTypeDef",
    {
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteHsmRequestRequestTypeDef = TypedDict(
    "DeleteHsmRequestRequestTypeDef",
    {
        "HsmArn": str,
    },
)

DeleteHsmResponseTypeDef = TypedDict(
    "DeleteHsmResponseTypeDef",
    {
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLunaClientRequestRequestTypeDef = TypedDict(
    "DeleteLunaClientRequestRequestTypeDef",
    {
        "ClientArn": str,
    },
)

DeleteLunaClientResponseTypeDef = TypedDict(
    "DeleteLunaClientResponseTypeDef",
    {
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHapgRequestRequestTypeDef = TypedDict(
    "DescribeHapgRequestRequestTypeDef",
    {
        "HapgArn": str,
    },
)

DescribeHapgResponseTypeDef = TypedDict(
    "DescribeHapgResponseTypeDef",
    {
        "HapgArn": str,
        "HapgSerial": str,
        "HsmsLastActionFailed": List[str],
        "HsmsPendingDeletion": List[str],
        "HsmsPendingRegistration": List[str],
        "Label": str,
        "LastModifiedTimestamp": str,
        "PartitionSerialList": List[str],
        "State": CloudHsmObjectStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHsmRequestRequestTypeDef = TypedDict(
    "DescribeHsmRequestRequestTypeDef",
    {
        "HsmArn": NotRequired[str],
        "HsmSerialNumber": NotRequired[str],
    },
)

DescribeHsmResponseTypeDef = TypedDict(
    "DescribeHsmResponseTypeDef",
    {
        "HsmArn": str,
        "Status": HsmStatusType,
        "StatusDetails": str,
        "AvailabilityZone": str,
        "EniId": str,
        "EniIp": str,
        "SubscriptionType": Literal["PRODUCTION"],
        "SubscriptionStartDate": str,
        "SubscriptionEndDate": str,
        "VpcId": str,
        "SubnetId": str,
        "IamRoleArn": str,
        "SerialNumber": str,
        "VendorName": str,
        "HsmType": str,
        "SoftwareVersion": str,
        "SshPublicKey": str,
        "SshKeyLastUpdated": str,
        "ServerCertUri": str,
        "ServerCertLastUpdated": str,
        "Partitions": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLunaClientRequestRequestTypeDef = TypedDict(
    "DescribeLunaClientRequestRequestTypeDef",
    {
        "ClientArn": NotRequired[str],
        "CertificateFingerprint": NotRequired[str],
    },
)

DescribeLunaClientResponseTypeDef = TypedDict(
    "DescribeLunaClientResponseTypeDef",
    {
        "ClientArn": str,
        "Certificate": str,
        "CertificateFingerprint": str,
        "LastModifiedTimestamp": str,
        "Label": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConfigRequestRequestTypeDef = TypedDict(
    "GetConfigRequestRequestTypeDef",
    {
        "ClientArn": str,
        "ClientVersion": ClientVersionType,
        "HapgList": Sequence[str],
    },
)

GetConfigResponseTypeDef = TypedDict(
    "GetConfigResponseTypeDef",
    {
        "ConfigType": str,
        "ConfigFile": str,
        "ConfigCred": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAvailableZonesResponseTypeDef = TypedDict(
    "ListAvailableZonesResponseTypeDef",
    {
        "AZList": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHapgsRequestRequestTypeDef = TypedDict(
    "ListHapgsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)

ListHapgsResponseTypeDef = TypedDict(
    "ListHapgsResponseTypeDef",
    {
        "HapgList": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHsmsRequestRequestTypeDef = TypedDict(
    "ListHsmsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)

ListHsmsResponseTypeDef = TypedDict(
    "ListHsmsResponseTypeDef",
    {
        "HsmList": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLunaClientsRequestRequestTypeDef = TypedDict(
    "ListLunaClientsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)

ListLunaClientsResponseTypeDef = TypedDict(
    "ListLunaClientsResponseTypeDef",
    {
        "ClientList": List[str],
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

ModifyHapgRequestRequestTypeDef = TypedDict(
    "ModifyHapgRequestRequestTypeDef",
    {
        "HapgArn": str,
        "Label": NotRequired[str],
        "PartitionSerialList": NotRequired[Sequence[str]],
    },
)

ModifyHapgResponseTypeDef = TypedDict(
    "ModifyHapgResponseTypeDef",
    {
        "HapgArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyHsmRequestRequestTypeDef = TypedDict(
    "ModifyHsmRequestRequestTypeDef",
    {
        "HsmArn": str,
        "SubnetId": NotRequired[str],
        "EniIp": NotRequired[str],
        "IamRoleArn": NotRequired[str],
        "ExternalId": NotRequired[str],
        "SyslogIp": NotRequired[str],
    },
)

ModifyHsmResponseTypeDef = TypedDict(
    "ModifyHsmResponseTypeDef",
    {
        "HsmArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyLunaClientRequestRequestTypeDef = TypedDict(
    "ModifyLunaClientRequestRequestTypeDef",
    {
        "ClientArn": str,
        "Certificate": str,
    },
)

ModifyLunaClientResponseTypeDef = TypedDict(
    "ModifyLunaClientResponseTypeDef",
    {
        "ClientArn": str,
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

RemoveTagsFromResourceRequestRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeyList": Sequence[str],
    },
)

RemoveTagsFromResourceResponseTypeDef = TypedDict(
    "RemoveTagsFromResourceResponseTypeDef",
    {
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
