"""
Type annotations for glacier service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/type_defs.html)

Usage::

    ```python
    from mypy_boto3_glacier.type_defs import AbortMultipartUploadInputRequestTypeDef

    data: AbortMultipartUploadInputRequestTypeDef = {...}
    ```
"""
import sys
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    ActionCodeType,
    CannedACLType,
    EncryptionTypeType,
    FileHeaderInfoType,
    PermissionType,
    QuoteFieldsType,
    StatusCodeType,
    StorageClassType,
    TypeType,
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
    "AbortMultipartUploadInputRequestTypeDef",
    "AbortVaultLockInputRequestTypeDef",
    "AccountVaultRequestTypeDef",
    "AddTagsToVaultInputRequestTypeDef",
    "ArchiveCreationOutputTypeDef",
    "CSVInputTypeDef",
    "CSVOutputTypeDef",
    "CompleteMultipartUploadInputMultipartUploadCompleteTypeDef",
    "CompleteMultipartUploadInputRequestTypeDef",
    "CompleteVaultLockInputRequestTypeDef",
    "CreateVaultInputAccountCreateVaultTypeDef",
    "CreateVaultInputRequestTypeDef",
    "CreateVaultInputServiceResourceCreateVaultTypeDef",
    "CreateVaultOutputTypeDef",
    "DataRetrievalPolicyTypeDef",
    "DataRetrievalRuleTypeDef",
    "DeleteArchiveInputRequestTypeDef",
    "DeleteVaultAccessPolicyInputRequestTypeDef",
    "DeleteVaultInputRequestTypeDef",
    "DeleteVaultNotificationsInputRequestTypeDef",
    "DescribeJobInputRequestTypeDef",
    "DescribeVaultInputRequestTypeDef",
    "DescribeVaultOutputResponseMetadataTypeDef",
    "DescribeVaultOutputTypeDef",
    "EncryptionTypeDef",
    "GetDataRetrievalPolicyInputRequestTypeDef",
    "GetDataRetrievalPolicyOutputTypeDef",
    "GetJobOutputInputJobGetOutputTypeDef",
    "GetJobOutputInputRequestTypeDef",
    "GetJobOutputOutputTypeDef",
    "GetVaultAccessPolicyInputRequestTypeDef",
    "GetVaultAccessPolicyOutputTypeDef",
    "GetVaultLockInputRequestTypeDef",
    "GetVaultLockOutputTypeDef",
    "GetVaultNotificationsInputRequestTypeDef",
    "GetVaultNotificationsOutputTypeDef",
    "GlacierJobDescriptionResponseMetadataTypeDef",
    "GlacierJobDescriptionTypeDef",
    "GrantTypeDef",
    "GranteeTypeDef",
    "InitiateJobInputRequestTypeDef",
    "InitiateJobOutputTypeDef",
    "InitiateMultipartUploadInputRequestTypeDef",
    "InitiateMultipartUploadInputVaultInitiateMultipartUploadTypeDef",
    "InitiateMultipartUploadOutputTypeDef",
    "InitiateVaultLockInputRequestTypeDef",
    "InitiateVaultLockOutputTypeDef",
    "InputSerializationTypeDef",
    "InventoryRetrievalJobDescriptionResponseMetadataTypeDef",
    "InventoryRetrievalJobDescriptionTypeDef",
    "InventoryRetrievalJobInputTypeDef",
    "JobParametersTypeDef",
    "ListJobsInputRequestTypeDef",
    "ListJobsOutputTypeDef",
    "ListMultipartUploadsInputRequestTypeDef",
    "ListMultipartUploadsOutputTypeDef",
    "ListPartsInputMultipartUploadPartsTypeDef",
    "ListPartsInputRequestTypeDef",
    "ListPartsOutputTypeDef",
    "ListProvisionedCapacityInputRequestTypeDef",
    "ListProvisionedCapacityOutputTypeDef",
    "ListTagsForVaultInputRequestTypeDef",
    "ListTagsForVaultOutputTypeDef",
    "ListVaultsInputRequestTypeDef",
    "ListVaultsOutputTypeDef",
    "OutputLocationResponseMetadataTypeDef",
    "OutputLocationTypeDef",
    "OutputSerializationTypeDef",
    "PaginatorConfigTypeDef",
    "PartListElementTypeDef",
    "ProvisionedCapacityDescriptionTypeDef",
    "PurchaseProvisionedCapacityInputRequestTypeDef",
    "PurchaseProvisionedCapacityOutputTypeDef",
    "RemoveTagsFromVaultInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "SelectParametersResponseMetadataTypeDef",
    "SelectParametersTypeDef",
    "ServiceResourceAccountRequestTypeDef",
    "ServiceResourceArchiveRequestTypeDef",
    "ServiceResourceJobRequestTypeDef",
    "ServiceResourceMultipartUploadRequestTypeDef",
    "ServiceResourceNotificationRequestTypeDef",
    "ServiceResourceVaultRequestTypeDef",
    "SetDataRetrievalPolicyInputRequestTypeDef",
    "SetVaultAccessPolicyInputRequestTypeDef",
    "SetVaultNotificationsInputNotificationSetTypeDef",
    "SetVaultNotificationsInputRequestTypeDef",
    "UploadArchiveInputRequestTypeDef",
    "UploadArchiveInputVaultUploadArchiveTypeDef",
    "UploadListElementTypeDef",
    "UploadMultipartPartInputMultipartUploadUploadPartTypeDef",
    "UploadMultipartPartInputRequestTypeDef",
    "UploadMultipartPartOutputTypeDef",
    "VaultAccessPolicyTypeDef",
    "VaultArchiveRequestTypeDef",
    "VaultJobRequestTypeDef",
    "VaultLockPolicyTypeDef",
    "VaultMultipartUploadRequestTypeDef",
    "VaultNotificationConfigTypeDef",
    "WaiterConfigTypeDef",
)

AbortMultipartUploadInputRequestTypeDef = TypedDict(
    "AbortMultipartUploadInputRequestTypeDef",
    {
        "vaultName": str,
        "uploadId": str,
        "accountId": NotRequired[str],
    },
)

AbortVaultLockInputRequestTypeDef = TypedDict(
    "AbortVaultLockInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)

AccountVaultRequestTypeDef = TypedDict(
    "AccountVaultRequestTypeDef",
    {
        "name": str,
    },
)

AddTagsToVaultInputRequestTypeDef = TypedDict(
    "AddTagsToVaultInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

ArchiveCreationOutputTypeDef = TypedDict(
    "ArchiveCreationOutputTypeDef",
    {
        "location": str,
        "checksum": str,
        "archiveId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CSVInputTypeDef = TypedDict(
    "CSVInputTypeDef",
    {
        "FileHeaderInfo": NotRequired[FileHeaderInfoType],
        "Comments": NotRequired[str],
        "QuoteEscapeCharacter": NotRequired[str],
        "RecordDelimiter": NotRequired[str],
        "FieldDelimiter": NotRequired[str],
        "QuoteCharacter": NotRequired[str],
    },
)

CSVOutputTypeDef = TypedDict(
    "CSVOutputTypeDef",
    {
        "QuoteFields": NotRequired[QuoteFieldsType],
        "QuoteEscapeCharacter": NotRequired[str],
        "RecordDelimiter": NotRequired[str],
        "FieldDelimiter": NotRequired[str],
        "QuoteCharacter": NotRequired[str],
    },
)

CompleteMultipartUploadInputMultipartUploadCompleteTypeDef = TypedDict(
    "CompleteMultipartUploadInputMultipartUploadCompleteTypeDef",
    {
        "archiveSize": NotRequired[str],
        "checksum": NotRequired[str],
    },
)

CompleteMultipartUploadInputRequestTypeDef = TypedDict(
    "CompleteMultipartUploadInputRequestTypeDef",
    {
        "vaultName": str,
        "uploadId": str,
        "accountId": NotRequired[str],
        "archiveSize": NotRequired[str],
        "checksum": NotRequired[str],
    },
)

CompleteVaultLockInputRequestTypeDef = TypedDict(
    "CompleteVaultLockInputRequestTypeDef",
    {
        "vaultName": str,
        "lockId": str,
        "accountId": NotRequired[str],
    },
)

CreateVaultInputAccountCreateVaultTypeDef = TypedDict(
    "CreateVaultInputAccountCreateVaultTypeDef",
    {
        "vaultName": str,
    },
)

CreateVaultInputRequestTypeDef = TypedDict(
    "CreateVaultInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)

CreateVaultInputServiceResourceCreateVaultTypeDef = TypedDict(
    "CreateVaultInputServiceResourceCreateVaultTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)

CreateVaultOutputTypeDef = TypedDict(
    "CreateVaultOutputTypeDef",
    {
        "location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataRetrievalPolicyTypeDef = TypedDict(
    "DataRetrievalPolicyTypeDef",
    {
        "Rules": NotRequired[List["DataRetrievalRuleTypeDef"]],
    },
)

DataRetrievalRuleTypeDef = TypedDict(
    "DataRetrievalRuleTypeDef",
    {
        "Strategy": NotRequired[str],
        "BytesPerHour": NotRequired[int],
    },
)

DeleteArchiveInputRequestTypeDef = TypedDict(
    "DeleteArchiveInputRequestTypeDef",
    {
        "vaultName": str,
        "archiveId": str,
        "accountId": NotRequired[str],
    },
)

DeleteVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "DeleteVaultAccessPolicyInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)

DeleteVaultInputRequestTypeDef = TypedDict(
    "DeleteVaultInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)

DeleteVaultNotificationsInputRequestTypeDef = TypedDict(
    "DeleteVaultNotificationsInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)

DescribeJobInputRequestTypeDef = TypedDict(
    "DescribeJobInputRequestTypeDef",
    {
        "vaultName": str,
        "jobId": str,
        "accountId": NotRequired[str],
    },
)

DescribeVaultInputRequestTypeDef = TypedDict(
    "DescribeVaultInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)

DescribeVaultOutputResponseMetadataTypeDef = TypedDict(
    "DescribeVaultOutputResponseMetadataTypeDef",
    {
        "VaultARN": str,
        "VaultName": str,
        "CreationDate": str,
        "LastInventoryDate": str,
        "NumberOfArchives": int,
        "SizeInBytes": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVaultOutputTypeDef = TypedDict(
    "DescribeVaultOutputTypeDef",
    {
        "VaultARN": NotRequired[str],
        "VaultName": NotRequired[str],
        "CreationDate": NotRequired[str],
        "LastInventoryDate": NotRequired[str],
        "NumberOfArchives": NotRequired[int],
        "SizeInBytes": NotRequired[int],
    },
)

EncryptionTypeDef = TypedDict(
    "EncryptionTypeDef",
    {
        "EncryptionType": NotRequired[EncryptionTypeType],
        "KMSKeyId": NotRequired[str],
        "KMSContext": NotRequired[str],
    },
)

GetDataRetrievalPolicyInputRequestTypeDef = TypedDict(
    "GetDataRetrievalPolicyInputRequestTypeDef",
    {
        "accountId": NotRequired[str],
    },
)

GetDataRetrievalPolicyOutputTypeDef = TypedDict(
    "GetDataRetrievalPolicyOutputTypeDef",
    {
        "Policy": "DataRetrievalPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobOutputInputJobGetOutputTypeDef = TypedDict(
    "GetJobOutputInputJobGetOutputTypeDef",
    {
        "range": NotRequired[str],
    },
)

GetJobOutputInputRequestTypeDef = TypedDict(
    "GetJobOutputInputRequestTypeDef",
    {
        "vaultName": str,
        "jobId": str,
        "accountId": NotRequired[str],
        "range": NotRequired[str],
    },
)

GetJobOutputOutputTypeDef = TypedDict(
    "GetJobOutputOutputTypeDef",
    {
        "body": StreamingBody,
        "checksum": str,
        "status": int,
        "contentRange": str,
        "acceptRanges": str,
        "contentType": str,
        "archiveDescription": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "GetVaultAccessPolicyInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)

GetVaultAccessPolicyOutputTypeDef = TypedDict(
    "GetVaultAccessPolicyOutputTypeDef",
    {
        "policy": "VaultAccessPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVaultLockInputRequestTypeDef = TypedDict(
    "GetVaultLockInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)

GetVaultLockOutputTypeDef = TypedDict(
    "GetVaultLockOutputTypeDef",
    {
        "Policy": str,
        "State": str,
        "ExpirationDate": str,
        "CreationDate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVaultNotificationsInputRequestTypeDef = TypedDict(
    "GetVaultNotificationsInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)

GetVaultNotificationsOutputTypeDef = TypedDict(
    "GetVaultNotificationsOutputTypeDef",
    {
        "vaultNotificationConfig": "VaultNotificationConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GlacierJobDescriptionResponseMetadataTypeDef = TypedDict(
    "GlacierJobDescriptionResponseMetadataTypeDef",
    {
        "JobId": str,
        "JobDescription": str,
        "Action": ActionCodeType,
        "ArchiveId": str,
        "VaultARN": str,
        "CreationDate": str,
        "Completed": bool,
        "StatusCode": StatusCodeType,
        "StatusMessage": str,
        "ArchiveSizeInBytes": int,
        "InventorySizeInBytes": int,
        "SNSTopic": str,
        "CompletionDate": str,
        "SHA256TreeHash": str,
        "ArchiveSHA256TreeHash": str,
        "RetrievalByteRange": str,
        "Tier": str,
        "InventoryRetrievalParameters": "InventoryRetrievalJobDescriptionTypeDef",
        "JobOutputPath": str,
        "SelectParameters": "SelectParametersTypeDef",
        "OutputLocation": "OutputLocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GlacierJobDescriptionTypeDef = TypedDict(
    "GlacierJobDescriptionTypeDef",
    {
        "JobId": NotRequired[str],
        "JobDescription": NotRequired[str],
        "Action": NotRequired[ActionCodeType],
        "ArchiveId": NotRequired[str],
        "VaultARN": NotRequired[str],
        "CreationDate": NotRequired[str],
        "Completed": NotRequired[bool],
        "StatusCode": NotRequired[StatusCodeType],
        "StatusMessage": NotRequired[str],
        "ArchiveSizeInBytes": NotRequired[int],
        "InventorySizeInBytes": NotRequired[int],
        "SNSTopic": NotRequired[str],
        "CompletionDate": NotRequired[str],
        "SHA256TreeHash": NotRequired[str],
        "ArchiveSHA256TreeHash": NotRequired[str],
        "RetrievalByteRange": NotRequired[str],
        "Tier": NotRequired[str],
        "InventoryRetrievalParameters": NotRequired["InventoryRetrievalJobDescriptionTypeDef"],
        "JobOutputPath": NotRequired[str],
        "SelectParameters": NotRequired["SelectParametersTypeDef"],
        "OutputLocation": NotRequired["OutputLocationTypeDef"],
    },
)

GrantTypeDef = TypedDict(
    "GrantTypeDef",
    {
        "Grantee": NotRequired["GranteeTypeDef"],
        "Permission": NotRequired[PermissionType],
    },
)

GranteeTypeDef = TypedDict(
    "GranteeTypeDef",
    {
        "Type": TypeType,
        "DisplayName": NotRequired[str],
        "URI": NotRequired[str],
        "ID": NotRequired[str],
        "EmailAddress": NotRequired[str],
    },
)

InitiateJobInputRequestTypeDef = TypedDict(
    "InitiateJobInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
        "jobParameters": NotRequired["JobParametersTypeDef"],
    },
)

InitiateJobOutputTypeDef = TypedDict(
    "InitiateJobOutputTypeDef",
    {
        "location": str,
        "jobId": str,
        "jobOutputPath": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InitiateMultipartUploadInputRequestTypeDef = TypedDict(
    "InitiateMultipartUploadInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
        "archiveDescription": NotRequired[str],
        "partSize": NotRequired[str],
    },
)

InitiateMultipartUploadInputVaultInitiateMultipartUploadTypeDef = TypedDict(
    "InitiateMultipartUploadInputVaultInitiateMultipartUploadTypeDef",
    {
        "archiveDescription": NotRequired[str],
        "partSize": NotRequired[str],
    },
)

InitiateMultipartUploadOutputTypeDef = TypedDict(
    "InitiateMultipartUploadOutputTypeDef",
    {
        "location": str,
        "uploadId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InitiateVaultLockInputRequestTypeDef = TypedDict(
    "InitiateVaultLockInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
        "policy": NotRequired["VaultLockPolicyTypeDef"],
    },
)

InitiateVaultLockOutputTypeDef = TypedDict(
    "InitiateVaultLockOutputTypeDef",
    {
        "lockId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputSerializationTypeDef = TypedDict(
    "InputSerializationTypeDef",
    {
        "csv": NotRequired["CSVInputTypeDef"],
    },
)

InventoryRetrievalJobDescriptionResponseMetadataTypeDef = TypedDict(
    "InventoryRetrievalJobDescriptionResponseMetadataTypeDef",
    {
        "Format": str,
        "StartDate": str,
        "EndDate": str,
        "Limit": str,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InventoryRetrievalJobDescriptionTypeDef = TypedDict(
    "InventoryRetrievalJobDescriptionTypeDef",
    {
        "Format": NotRequired[str],
        "StartDate": NotRequired[str],
        "EndDate": NotRequired[str],
        "Limit": NotRequired[str],
        "Marker": NotRequired[str],
    },
)

InventoryRetrievalJobInputTypeDef = TypedDict(
    "InventoryRetrievalJobInputTypeDef",
    {
        "StartDate": NotRequired[str],
        "EndDate": NotRequired[str],
        "Limit": NotRequired[str],
        "Marker": NotRequired[str],
    },
)

JobParametersTypeDef = TypedDict(
    "JobParametersTypeDef",
    {
        "Format": NotRequired[str],
        "Type": NotRequired[str],
        "ArchiveId": NotRequired[str],
        "Description": NotRequired[str],
        "SNSTopic": NotRequired[str],
        "RetrievalByteRange": NotRequired[str],
        "Tier": NotRequired[str],
        "InventoryRetrievalParameters": NotRequired["InventoryRetrievalJobInputTypeDef"],
        "SelectParameters": NotRequired["SelectParametersTypeDef"],
        "OutputLocation": NotRequired["OutputLocationTypeDef"],
    },
)

ListJobsInputRequestTypeDef = TypedDict(
    "ListJobsInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
        "limit": NotRequired[str],
        "marker": NotRequired[str],
        "statuscode": NotRequired[str],
        "completed": NotRequired[str],
    },
)

ListJobsOutputTypeDef = TypedDict(
    "ListJobsOutputTypeDef",
    {
        "JobList": List["GlacierJobDescriptionTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMultipartUploadsInputRequestTypeDef = TypedDict(
    "ListMultipartUploadsInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
        "marker": NotRequired[str],
        "limit": NotRequired[str],
    },
)

ListMultipartUploadsOutputTypeDef = TypedDict(
    "ListMultipartUploadsOutputTypeDef",
    {
        "UploadsList": List["UploadListElementTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPartsInputMultipartUploadPartsTypeDef = TypedDict(
    "ListPartsInputMultipartUploadPartsTypeDef",
    {
        "marker": NotRequired[str],
        "limit": NotRequired[str],
    },
)

ListPartsInputRequestTypeDef = TypedDict(
    "ListPartsInputRequestTypeDef",
    {
        "vaultName": str,
        "uploadId": str,
        "accountId": NotRequired[str],
        "marker": NotRequired[str],
        "limit": NotRequired[str],
    },
)

ListPartsOutputTypeDef = TypedDict(
    "ListPartsOutputTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
        "Parts": List["PartListElementTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProvisionedCapacityInputRequestTypeDef = TypedDict(
    "ListProvisionedCapacityInputRequestTypeDef",
    {
        "accountId": NotRequired[str],
    },
)

ListProvisionedCapacityOutputTypeDef = TypedDict(
    "ListProvisionedCapacityOutputTypeDef",
    {
        "ProvisionedCapacityList": List["ProvisionedCapacityDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForVaultInputRequestTypeDef = TypedDict(
    "ListTagsForVaultInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)

ListTagsForVaultOutputTypeDef = TypedDict(
    "ListTagsForVaultOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVaultsInputRequestTypeDef = TypedDict(
    "ListVaultsInputRequestTypeDef",
    {
        "accountId": NotRequired[str],
        "marker": NotRequired[str],
        "limit": NotRequired[str],
    },
)

ListVaultsOutputTypeDef = TypedDict(
    "ListVaultsOutputTypeDef",
    {
        "VaultList": List["DescribeVaultOutputTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OutputLocationResponseMetadataTypeDef = TypedDict(
    "OutputLocationResponseMetadataTypeDef",
    {
        "S3": "S3LocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OutputLocationTypeDef = TypedDict(
    "OutputLocationTypeDef",
    {
        "S3": NotRequired["S3LocationTypeDef"],
    },
)

OutputSerializationTypeDef = TypedDict(
    "OutputSerializationTypeDef",
    {
        "csv": NotRequired["CSVOutputTypeDef"],
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

PartListElementTypeDef = TypedDict(
    "PartListElementTypeDef",
    {
        "RangeInBytes": NotRequired[str],
        "SHA256TreeHash": NotRequired[str],
    },
)

ProvisionedCapacityDescriptionTypeDef = TypedDict(
    "ProvisionedCapacityDescriptionTypeDef",
    {
        "CapacityId": NotRequired[str],
        "StartDate": NotRequired[str],
        "ExpirationDate": NotRequired[str],
    },
)

PurchaseProvisionedCapacityInputRequestTypeDef = TypedDict(
    "PurchaseProvisionedCapacityInputRequestTypeDef",
    {
        "accountId": NotRequired[str],
    },
)

PurchaseProvisionedCapacityOutputTypeDef = TypedDict(
    "PurchaseProvisionedCapacityOutputTypeDef",
    {
        "capacityId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTagsFromVaultInputRequestTypeDef = TypedDict(
    "RemoveTagsFromVaultInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
        "TagKeys": NotRequired[Sequence[str]],
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
        "BucketName": NotRequired[str],
        "Prefix": NotRequired[str],
        "Encryption": NotRequired["EncryptionTypeDef"],
        "CannedACL": NotRequired[CannedACLType],
        "AccessControlList": NotRequired[List["GrantTypeDef"]],
        "Tagging": NotRequired[Dict[str, str]],
        "UserMetadata": NotRequired[Dict[str, str]],
        "StorageClass": NotRequired[StorageClassType],
    },
)

SelectParametersResponseMetadataTypeDef = TypedDict(
    "SelectParametersResponseMetadataTypeDef",
    {
        "InputSerialization": "InputSerializationTypeDef",
        "ExpressionType": Literal["SQL"],
        "Expression": str,
        "OutputSerialization": "OutputSerializationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SelectParametersTypeDef = TypedDict(
    "SelectParametersTypeDef",
    {
        "InputSerialization": NotRequired["InputSerializationTypeDef"],
        "ExpressionType": NotRequired[Literal["SQL"]],
        "Expression": NotRequired[str],
        "OutputSerialization": NotRequired["OutputSerializationTypeDef"],
    },
)

ServiceResourceAccountRequestTypeDef = TypedDict(
    "ServiceResourceAccountRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceArchiveRequestTypeDef = TypedDict(
    "ServiceResourceArchiveRequestTypeDef",
    {
        "account_id": str,
        "vault_name": str,
        "id": str,
    },
)

ServiceResourceJobRequestTypeDef = TypedDict(
    "ServiceResourceJobRequestTypeDef",
    {
        "account_id": str,
        "vault_name": str,
        "id": str,
    },
)

ServiceResourceMultipartUploadRequestTypeDef = TypedDict(
    "ServiceResourceMultipartUploadRequestTypeDef",
    {
        "account_id": str,
        "vault_name": str,
        "id": str,
    },
)

ServiceResourceNotificationRequestTypeDef = TypedDict(
    "ServiceResourceNotificationRequestTypeDef",
    {
        "account_id": str,
        "vault_name": str,
    },
)

ServiceResourceVaultRequestTypeDef = TypedDict(
    "ServiceResourceVaultRequestTypeDef",
    {
        "account_id": str,
        "name": str,
    },
)

SetDataRetrievalPolicyInputRequestTypeDef = TypedDict(
    "SetDataRetrievalPolicyInputRequestTypeDef",
    {
        "accountId": NotRequired[str],
        "Policy": NotRequired["DataRetrievalPolicyTypeDef"],
    },
)

SetVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "SetVaultAccessPolicyInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
        "policy": NotRequired["VaultAccessPolicyTypeDef"],
    },
)

SetVaultNotificationsInputNotificationSetTypeDef = TypedDict(
    "SetVaultNotificationsInputNotificationSetTypeDef",
    {
        "vaultNotificationConfig": NotRequired["VaultNotificationConfigTypeDef"],
    },
)

SetVaultNotificationsInputRequestTypeDef = TypedDict(
    "SetVaultNotificationsInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
        "vaultNotificationConfig": NotRequired["VaultNotificationConfigTypeDef"],
    },
)

UploadArchiveInputRequestTypeDef = TypedDict(
    "UploadArchiveInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
        "archiveDescription": NotRequired[str],
        "checksum": NotRequired[str],
        "body": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
    },
)

UploadArchiveInputVaultUploadArchiveTypeDef = TypedDict(
    "UploadArchiveInputVaultUploadArchiveTypeDef",
    {
        "archiveDescription": NotRequired[str],
        "checksum": NotRequired[str],
        "body": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
    },
)

UploadListElementTypeDef = TypedDict(
    "UploadListElementTypeDef",
    {
        "MultipartUploadId": NotRequired[str],
        "VaultARN": NotRequired[str],
        "ArchiveDescription": NotRequired[str],
        "PartSizeInBytes": NotRequired[int],
        "CreationDate": NotRequired[str],
    },
)

UploadMultipartPartInputMultipartUploadUploadPartTypeDef = TypedDict(
    "UploadMultipartPartInputMultipartUploadUploadPartTypeDef",
    {
        "checksum": NotRequired[str],
        "range": NotRequired[str],
        "body": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
    },
)

UploadMultipartPartInputRequestTypeDef = TypedDict(
    "UploadMultipartPartInputRequestTypeDef",
    {
        "vaultName": str,
        "uploadId": str,
        "accountId": NotRequired[str],
        "checksum": NotRequired[str],
        "range": NotRequired[str],
        "body": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
    },
)

UploadMultipartPartOutputTypeDef = TypedDict(
    "UploadMultipartPartOutputTypeDef",
    {
        "checksum": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VaultAccessPolicyTypeDef = TypedDict(
    "VaultAccessPolicyTypeDef",
    {
        "Policy": NotRequired[str],
    },
)

VaultArchiveRequestTypeDef = TypedDict(
    "VaultArchiveRequestTypeDef",
    {
        "id": str,
    },
)

VaultJobRequestTypeDef = TypedDict(
    "VaultJobRequestTypeDef",
    {
        "id": str,
    },
)

VaultLockPolicyTypeDef = TypedDict(
    "VaultLockPolicyTypeDef",
    {
        "Policy": NotRequired[str],
    },
)

VaultMultipartUploadRequestTypeDef = TypedDict(
    "VaultMultipartUploadRequestTypeDef",
    {
        "id": str,
    },
)

VaultNotificationConfigTypeDef = TypedDict(
    "VaultNotificationConfigTypeDef",
    {
        "SNSTopic": NotRequired[str],
        "Events": NotRequired[List[str]],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
