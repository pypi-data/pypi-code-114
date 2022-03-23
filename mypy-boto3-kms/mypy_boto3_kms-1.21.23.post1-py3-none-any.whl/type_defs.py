"""
Type annotations for kms service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kms.type_defs import AliasListEntryTypeDef

    data: AliasListEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    AlgorithmSpecType,
    ConnectionErrorCodeTypeType,
    ConnectionStateTypeType,
    CustomerMasterKeySpecType,
    DataKeyPairSpecType,
    DataKeySpecType,
    EncryptionAlgorithmSpecType,
    ExpirationModelTypeType,
    GrantOperationType,
    KeyManagerTypeType,
    KeySpecType,
    KeyStateType,
    KeyUsageTypeType,
    MessageTypeType,
    MultiRegionKeyTypeType,
    OriginTypeType,
    SigningAlgorithmSpecType,
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
    "AliasListEntryTypeDef",
    "CancelKeyDeletionRequestRequestTypeDef",
    "CancelKeyDeletionResponseTypeDef",
    "ConnectCustomKeyStoreRequestRequestTypeDef",
    "CreateAliasRequestRequestTypeDef",
    "CreateCustomKeyStoreRequestRequestTypeDef",
    "CreateCustomKeyStoreResponseTypeDef",
    "CreateGrantRequestRequestTypeDef",
    "CreateGrantResponseTypeDef",
    "CreateKeyRequestRequestTypeDef",
    "CreateKeyResponseTypeDef",
    "CustomKeyStoresListEntryTypeDef",
    "DecryptRequestRequestTypeDef",
    "DecryptResponseTypeDef",
    "DeleteAliasRequestRequestTypeDef",
    "DeleteCustomKeyStoreRequestRequestTypeDef",
    "DeleteImportedKeyMaterialRequestRequestTypeDef",
    "DescribeCustomKeyStoresRequestRequestTypeDef",
    "DescribeCustomKeyStoresResponseTypeDef",
    "DescribeKeyRequestRequestTypeDef",
    "DescribeKeyResponseTypeDef",
    "DisableKeyRequestRequestTypeDef",
    "DisableKeyRotationRequestRequestTypeDef",
    "DisconnectCustomKeyStoreRequestRequestTypeDef",
    "EnableKeyRequestRequestTypeDef",
    "EnableKeyRotationRequestRequestTypeDef",
    "EncryptRequestRequestTypeDef",
    "EncryptResponseTypeDef",
    "GenerateDataKeyPairRequestRequestTypeDef",
    "GenerateDataKeyPairResponseTypeDef",
    "GenerateDataKeyPairWithoutPlaintextRequestRequestTypeDef",
    "GenerateDataKeyPairWithoutPlaintextResponseTypeDef",
    "GenerateDataKeyRequestRequestTypeDef",
    "GenerateDataKeyResponseTypeDef",
    "GenerateDataKeyWithoutPlaintextRequestRequestTypeDef",
    "GenerateDataKeyWithoutPlaintextResponseTypeDef",
    "GenerateRandomRequestRequestTypeDef",
    "GenerateRandomResponseTypeDef",
    "GetKeyPolicyRequestRequestTypeDef",
    "GetKeyPolicyResponseTypeDef",
    "GetKeyRotationStatusRequestRequestTypeDef",
    "GetKeyRotationStatusResponseTypeDef",
    "GetParametersForImportRequestRequestTypeDef",
    "GetParametersForImportResponseTypeDef",
    "GetPublicKeyRequestRequestTypeDef",
    "GetPublicKeyResponseTypeDef",
    "GrantConstraintsTypeDef",
    "GrantListEntryTypeDef",
    "ImportKeyMaterialRequestRequestTypeDef",
    "KeyListEntryTypeDef",
    "KeyMetadataTypeDef",
    "ListAliasesRequestRequestTypeDef",
    "ListAliasesResponseTypeDef",
    "ListGrantsRequestRequestTypeDef",
    "ListGrantsResponseTypeDef",
    "ListKeyPoliciesRequestRequestTypeDef",
    "ListKeyPoliciesResponseTypeDef",
    "ListKeysRequestRequestTypeDef",
    "ListKeysResponseTypeDef",
    "ListResourceTagsRequestRequestTypeDef",
    "ListResourceTagsResponseTypeDef",
    "ListRetirableGrantsRequestRequestTypeDef",
    "MultiRegionConfigurationTypeDef",
    "MultiRegionKeyTypeDef",
    "PaginatorConfigTypeDef",
    "PutKeyPolicyRequestRequestTypeDef",
    "ReEncryptRequestRequestTypeDef",
    "ReEncryptResponseTypeDef",
    "ReplicateKeyRequestRequestTypeDef",
    "ReplicateKeyResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RetireGrantRequestRequestTypeDef",
    "RevokeGrantRequestRequestTypeDef",
    "ScheduleKeyDeletionRequestRequestTypeDef",
    "ScheduleKeyDeletionResponseTypeDef",
    "SignRequestRequestTypeDef",
    "SignResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAliasRequestRequestTypeDef",
    "UpdateCustomKeyStoreRequestRequestTypeDef",
    "UpdateKeyDescriptionRequestRequestTypeDef",
    "UpdatePrimaryRegionRequestRequestTypeDef",
    "VerifyRequestRequestTypeDef",
    "VerifyResponseTypeDef",
)

AliasListEntryTypeDef = TypedDict(
    "AliasListEntryTypeDef",
    {
        "AliasName": NotRequired[str],
        "AliasArn": NotRequired[str],
        "TargetKeyId": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "LastUpdatedDate": NotRequired[datetime],
    },
)

CancelKeyDeletionRequestRequestTypeDef = TypedDict(
    "CancelKeyDeletionRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)

CancelKeyDeletionResponseTypeDef = TypedDict(
    "CancelKeyDeletionResponseTypeDef",
    {
        "KeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConnectCustomKeyStoreRequestRequestTypeDef = TypedDict(
    "ConnectCustomKeyStoreRequestRequestTypeDef",
    {
        "CustomKeyStoreId": str,
    },
)

CreateAliasRequestRequestTypeDef = TypedDict(
    "CreateAliasRequestRequestTypeDef",
    {
        "AliasName": str,
        "TargetKeyId": str,
    },
)

CreateCustomKeyStoreRequestRequestTypeDef = TypedDict(
    "CreateCustomKeyStoreRequestRequestTypeDef",
    {
        "CustomKeyStoreName": str,
        "CloudHsmClusterId": str,
        "TrustAnchorCertificate": str,
        "KeyStorePassword": str,
    },
)

CreateCustomKeyStoreResponseTypeDef = TypedDict(
    "CreateCustomKeyStoreResponseTypeDef",
    {
        "CustomKeyStoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGrantRequestRequestTypeDef = TypedDict(
    "CreateGrantRequestRequestTypeDef",
    {
        "KeyId": str,
        "GranteePrincipal": str,
        "Operations": Sequence[GrantOperationType],
        "RetiringPrincipal": NotRequired[str],
        "Constraints": NotRequired["GrantConstraintsTypeDef"],
        "GrantTokens": NotRequired[Sequence[str]],
        "Name": NotRequired[str],
    },
)

CreateGrantResponseTypeDef = TypedDict(
    "CreateGrantResponseTypeDef",
    {
        "GrantToken": str,
        "GrantId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateKeyRequestRequestTypeDef = TypedDict(
    "CreateKeyRequestRequestTypeDef",
    {
        "Policy": NotRequired[str],
        "Description": NotRequired[str],
        "KeyUsage": NotRequired[KeyUsageTypeType],
        "CustomerMasterKeySpec": NotRequired[CustomerMasterKeySpecType],
        "KeySpec": NotRequired[KeySpecType],
        "Origin": NotRequired[OriginTypeType],
        "CustomKeyStoreId": NotRequired[str],
        "BypassPolicyLockoutSafetyCheck": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "MultiRegion": NotRequired[bool],
    },
)

CreateKeyResponseTypeDef = TypedDict(
    "CreateKeyResponseTypeDef",
    {
        "KeyMetadata": "KeyMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomKeyStoresListEntryTypeDef = TypedDict(
    "CustomKeyStoresListEntryTypeDef",
    {
        "CustomKeyStoreId": NotRequired[str],
        "CustomKeyStoreName": NotRequired[str],
        "CloudHsmClusterId": NotRequired[str],
        "TrustAnchorCertificate": NotRequired[str],
        "ConnectionState": NotRequired[ConnectionStateTypeType],
        "ConnectionErrorCode": NotRequired[ConnectionErrorCodeTypeType],
        "CreationDate": NotRequired[datetime],
    },
)

DecryptRequestRequestTypeDef = TypedDict(
    "DecryptRequestRequestTypeDef",
    {
        "CiphertextBlob": Union[bytes, IO[bytes], StreamingBody],
        "EncryptionContext": NotRequired[Mapping[str, str]],
        "GrantTokens": NotRequired[Sequence[str]],
        "KeyId": NotRequired[str],
        "EncryptionAlgorithm": NotRequired[EncryptionAlgorithmSpecType],
    },
)

DecryptResponseTypeDef = TypedDict(
    "DecryptResponseTypeDef",
    {
        "KeyId": str,
        "Plaintext": bytes,
        "EncryptionAlgorithm": EncryptionAlgorithmSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAliasRequestRequestTypeDef = TypedDict(
    "DeleteAliasRequestRequestTypeDef",
    {
        "AliasName": str,
    },
)

DeleteCustomKeyStoreRequestRequestTypeDef = TypedDict(
    "DeleteCustomKeyStoreRequestRequestTypeDef",
    {
        "CustomKeyStoreId": str,
    },
)

DeleteImportedKeyMaterialRequestRequestTypeDef = TypedDict(
    "DeleteImportedKeyMaterialRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)

DescribeCustomKeyStoresRequestRequestTypeDef = TypedDict(
    "DescribeCustomKeyStoresRequestRequestTypeDef",
    {
        "CustomKeyStoreId": NotRequired[str],
        "CustomKeyStoreName": NotRequired[str],
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeCustomKeyStoresResponseTypeDef = TypedDict(
    "DescribeCustomKeyStoresResponseTypeDef",
    {
        "CustomKeyStores": List["CustomKeyStoresListEntryTypeDef"],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeKeyRequestRequestTypeDef = TypedDict(
    "DescribeKeyRequestRequestTypeDef",
    {
        "KeyId": str,
        "GrantTokens": NotRequired[Sequence[str]],
    },
)

DescribeKeyResponseTypeDef = TypedDict(
    "DescribeKeyResponseTypeDef",
    {
        "KeyMetadata": "KeyMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableKeyRequestRequestTypeDef = TypedDict(
    "DisableKeyRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)

DisableKeyRotationRequestRequestTypeDef = TypedDict(
    "DisableKeyRotationRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)

DisconnectCustomKeyStoreRequestRequestTypeDef = TypedDict(
    "DisconnectCustomKeyStoreRequestRequestTypeDef",
    {
        "CustomKeyStoreId": str,
    },
)

EnableKeyRequestRequestTypeDef = TypedDict(
    "EnableKeyRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)

EnableKeyRotationRequestRequestTypeDef = TypedDict(
    "EnableKeyRotationRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)

EncryptRequestRequestTypeDef = TypedDict(
    "EncryptRequestRequestTypeDef",
    {
        "KeyId": str,
        "Plaintext": Union[bytes, IO[bytes], StreamingBody],
        "EncryptionContext": NotRequired[Mapping[str, str]],
        "GrantTokens": NotRequired[Sequence[str]],
        "EncryptionAlgorithm": NotRequired[EncryptionAlgorithmSpecType],
    },
)

EncryptResponseTypeDef = TypedDict(
    "EncryptResponseTypeDef",
    {
        "CiphertextBlob": bytes,
        "KeyId": str,
        "EncryptionAlgorithm": EncryptionAlgorithmSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GenerateDataKeyPairRequestRequestTypeDef = TypedDict(
    "GenerateDataKeyPairRequestRequestTypeDef",
    {
        "KeyId": str,
        "KeyPairSpec": DataKeyPairSpecType,
        "EncryptionContext": NotRequired[Mapping[str, str]],
        "GrantTokens": NotRequired[Sequence[str]],
    },
)

GenerateDataKeyPairResponseTypeDef = TypedDict(
    "GenerateDataKeyPairResponseTypeDef",
    {
        "PrivateKeyCiphertextBlob": bytes,
        "PrivateKeyPlaintext": bytes,
        "PublicKey": bytes,
        "KeyId": str,
        "KeyPairSpec": DataKeyPairSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GenerateDataKeyPairWithoutPlaintextRequestRequestTypeDef = TypedDict(
    "GenerateDataKeyPairWithoutPlaintextRequestRequestTypeDef",
    {
        "KeyId": str,
        "KeyPairSpec": DataKeyPairSpecType,
        "EncryptionContext": NotRequired[Mapping[str, str]],
        "GrantTokens": NotRequired[Sequence[str]],
    },
)

GenerateDataKeyPairWithoutPlaintextResponseTypeDef = TypedDict(
    "GenerateDataKeyPairWithoutPlaintextResponseTypeDef",
    {
        "PrivateKeyCiphertextBlob": bytes,
        "PublicKey": bytes,
        "KeyId": str,
        "KeyPairSpec": DataKeyPairSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GenerateDataKeyRequestRequestTypeDef = TypedDict(
    "GenerateDataKeyRequestRequestTypeDef",
    {
        "KeyId": str,
        "EncryptionContext": NotRequired[Mapping[str, str]],
        "NumberOfBytes": NotRequired[int],
        "KeySpec": NotRequired[DataKeySpecType],
        "GrantTokens": NotRequired[Sequence[str]],
    },
)

GenerateDataKeyResponseTypeDef = TypedDict(
    "GenerateDataKeyResponseTypeDef",
    {
        "CiphertextBlob": bytes,
        "Plaintext": bytes,
        "KeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GenerateDataKeyWithoutPlaintextRequestRequestTypeDef = TypedDict(
    "GenerateDataKeyWithoutPlaintextRequestRequestTypeDef",
    {
        "KeyId": str,
        "EncryptionContext": NotRequired[Mapping[str, str]],
        "KeySpec": NotRequired[DataKeySpecType],
        "NumberOfBytes": NotRequired[int],
        "GrantTokens": NotRequired[Sequence[str]],
    },
)

GenerateDataKeyWithoutPlaintextResponseTypeDef = TypedDict(
    "GenerateDataKeyWithoutPlaintextResponseTypeDef",
    {
        "CiphertextBlob": bytes,
        "KeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GenerateRandomRequestRequestTypeDef = TypedDict(
    "GenerateRandomRequestRequestTypeDef",
    {
        "NumberOfBytes": NotRequired[int],
        "CustomKeyStoreId": NotRequired[str],
    },
)

GenerateRandomResponseTypeDef = TypedDict(
    "GenerateRandomResponseTypeDef",
    {
        "Plaintext": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKeyPolicyRequestRequestTypeDef = TypedDict(
    "GetKeyPolicyRequestRequestTypeDef",
    {
        "KeyId": str,
        "PolicyName": str,
    },
)

GetKeyPolicyResponseTypeDef = TypedDict(
    "GetKeyPolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKeyRotationStatusRequestRequestTypeDef = TypedDict(
    "GetKeyRotationStatusRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)

GetKeyRotationStatusResponseTypeDef = TypedDict(
    "GetKeyRotationStatusResponseTypeDef",
    {
        "KeyRotationEnabled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetParametersForImportRequestRequestTypeDef = TypedDict(
    "GetParametersForImportRequestRequestTypeDef",
    {
        "KeyId": str,
        "WrappingAlgorithm": AlgorithmSpecType,
        "WrappingKeySpec": Literal["RSA_2048"],
    },
)

GetParametersForImportResponseTypeDef = TypedDict(
    "GetParametersForImportResponseTypeDef",
    {
        "KeyId": str,
        "ImportToken": bytes,
        "PublicKey": bytes,
        "ParametersValidTo": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPublicKeyRequestRequestTypeDef = TypedDict(
    "GetPublicKeyRequestRequestTypeDef",
    {
        "KeyId": str,
        "GrantTokens": NotRequired[Sequence[str]],
    },
)

GetPublicKeyResponseTypeDef = TypedDict(
    "GetPublicKeyResponseTypeDef",
    {
        "KeyId": str,
        "PublicKey": bytes,
        "CustomerMasterKeySpec": CustomerMasterKeySpecType,
        "KeySpec": KeySpecType,
        "KeyUsage": KeyUsageTypeType,
        "EncryptionAlgorithms": List[EncryptionAlgorithmSpecType],
        "SigningAlgorithms": List[SigningAlgorithmSpecType],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GrantConstraintsTypeDef = TypedDict(
    "GrantConstraintsTypeDef",
    {
        "EncryptionContextSubset": NotRequired[Mapping[str, str]],
        "EncryptionContextEquals": NotRequired[Mapping[str, str]],
    },
)

GrantListEntryTypeDef = TypedDict(
    "GrantListEntryTypeDef",
    {
        "KeyId": NotRequired[str],
        "GrantId": NotRequired[str],
        "Name": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "GranteePrincipal": NotRequired[str],
        "RetiringPrincipal": NotRequired[str],
        "IssuingAccount": NotRequired[str],
        "Operations": NotRequired[List[GrantOperationType]],
        "Constraints": NotRequired["GrantConstraintsTypeDef"],
    },
)

ImportKeyMaterialRequestRequestTypeDef = TypedDict(
    "ImportKeyMaterialRequestRequestTypeDef",
    {
        "KeyId": str,
        "ImportToken": Union[bytes, IO[bytes], StreamingBody],
        "EncryptedKeyMaterial": Union[bytes, IO[bytes], StreamingBody],
        "ValidTo": NotRequired[Union[datetime, str]],
        "ExpirationModel": NotRequired[ExpirationModelTypeType],
    },
)

KeyListEntryTypeDef = TypedDict(
    "KeyListEntryTypeDef",
    {
        "KeyId": NotRequired[str],
        "KeyArn": NotRequired[str],
    },
)

KeyMetadataTypeDef = TypedDict(
    "KeyMetadataTypeDef",
    {
        "KeyId": str,
        "AWSAccountId": NotRequired[str],
        "Arn": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "Enabled": NotRequired[bool],
        "Description": NotRequired[str],
        "KeyUsage": NotRequired[KeyUsageTypeType],
        "KeyState": NotRequired[KeyStateType],
        "DeletionDate": NotRequired[datetime],
        "ValidTo": NotRequired[datetime],
        "Origin": NotRequired[OriginTypeType],
        "CustomKeyStoreId": NotRequired[str],
        "CloudHsmClusterId": NotRequired[str],
        "ExpirationModel": NotRequired[ExpirationModelTypeType],
        "KeyManager": NotRequired[KeyManagerTypeType],
        "CustomerMasterKeySpec": NotRequired[CustomerMasterKeySpecType],
        "KeySpec": NotRequired[KeySpecType],
        "EncryptionAlgorithms": NotRequired[List[EncryptionAlgorithmSpecType]],
        "SigningAlgorithms": NotRequired[List[SigningAlgorithmSpecType]],
        "MultiRegion": NotRequired[bool],
        "MultiRegionConfiguration": NotRequired["MultiRegionConfigurationTypeDef"],
        "PendingDeletionWindowInDays": NotRequired[int],
    },
)

ListAliasesRequestRequestTypeDef = TypedDict(
    "ListAliasesRequestRequestTypeDef",
    {
        "KeyId": NotRequired[str],
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

ListAliasesResponseTypeDef = TypedDict(
    "ListAliasesResponseTypeDef",
    {
        "Aliases": List["AliasListEntryTypeDef"],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGrantsRequestRequestTypeDef = TypedDict(
    "ListGrantsRequestRequestTypeDef",
    {
        "KeyId": str,
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
        "GrantId": NotRequired[str],
        "GranteePrincipal": NotRequired[str],
    },
)

ListGrantsResponseTypeDef = TypedDict(
    "ListGrantsResponseTypeDef",
    {
        "Grants": List["GrantListEntryTypeDef"],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKeyPoliciesRequestRequestTypeDef = TypedDict(
    "ListKeyPoliciesRequestRequestTypeDef",
    {
        "KeyId": str,
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

ListKeyPoliciesResponseTypeDef = TypedDict(
    "ListKeyPoliciesResponseTypeDef",
    {
        "PolicyNames": List[str],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKeysRequestRequestTypeDef = TypedDict(
    "ListKeysRequestRequestTypeDef",
    {
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

ListKeysResponseTypeDef = TypedDict(
    "ListKeysResponseTypeDef",
    {
        "Keys": List["KeyListEntryTypeDef"],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceTagsRequestRequestTypeDef = TypedDict(
    "ListResourceTagsRequestRequestTypeDef",
    {
        "KeyId": str,
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

ListResourceTagsResponseTypeDef = TypedDict(
    "ListResourceTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRetirableGrantsRequestRequestTypeDef = TypedDict(
    "ListRetirableGrantsRequestRequestTypeDef",
    {
        "RetiringPrincipal": str,
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

MultiRegionConfigurationTypeDef = TypedDict(
    "MultiRegionConfigurationTypeDef",
    {
        "MultiRegionKeyType": NotRequired[MultiRegionKeyTypeType],
        "PrimaryKey": NotRequired["MultiRegionKeyTypeDef"],
        "ReplicaKeys": NotRequired[List["MultiRegionKeyTypeDef"]],
    },
)

MultiRegionKeyTypeDef = TypedDict(
    "MultiRegionKeyTypeDef",
    {
        "Arn": NotRequired[str],
        "Region": NotRequired[str],
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

PutKeyPolicyRequestRequestTypeDef = TypedDict(
    "PutKeyPolicyRequestRequestTypeDef",
    {
        "KeyId": str,
        "PolicyName": str,
        "Policy": str,
        "BypassPolicyLockoutSafetyCheck": NotRequired[bool],
    },
)

ReEncryptRequestRequestTypeDef = TypedDict(
    "ReEncryptRequestRequestTypeDef",
    {
        "CiphertextBlob": Union[bytes, IO[bytes], StreamingBody],
        "DestinationKeyId": str,
        "SourceEncryptionContext": NotRequired[Mapping[str, str]],
        "SourceKeyId": NotRequired[str],
        "DestinationEncryptionContext": NotRequired[Mapping[str, str]],
        "SourceEncryptionAlgorithm": NotRequired[EncryptionAlgorithmSpecType],
        "DestinationEncryptionAlgorithm": NotRequired[EncryptionAlgorithmSpecType],
        "GrantTokens": NotRequired[Sequence[str]],
    },
)

ReEncryptResponseTypeDef = TypedDict(
    "ReEncryptResponseTypeDef",
    {
        "CiphertextBlob": bytes,
        "SourceKeyId": str,
        "KeyId": str,
        "SourceEncryptionAlgorithm": EncryptionAlgorithmSpecType,
        "DestinationEncryptionAlgorithm": EncryptionAlgorithmSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplicateKeyRequestRequestTypeDef = TypedDict(
    "ReplicateKeyRequestRequestTypeDef",
    {
        "KeyId": str,
        "ReplicaRegion": str,
        "Policy": NotRequired[str],
        "BypassPolicyLockoutSafetyCheck": NotRequired[bool],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

ReplicateKeyResponseTypeDef = TypedDict(
    "ReplicateKeyResponseTypeDef",
    {
        "ReplicaKeyMetadata": "KeyMetadataTypeDef",
        "ReplicaPolicy": str,
        "ReplicaTags": List["TagTypeDef"],
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

RetireGrantRequestRequestTypeDef = TypedDict(
    "RetireGrantRequestRequestTypeDef",
    {
        "GrantToken": NotRequired[str],
        "KeyId": NotRequired[str],
        "GrantId": NotRequired[str],
    },
)

RevokeGrantRequestRequestTypeDef = TypedDict(
    "RevokeGrantRequestRequestTypeDef",
    {
        "KeyId": str,
        "GrantId": str,
    },
)

ScheduleKeyDeletionRequestRequestTypeDef = TypedDict(
    "ScheduleKeyDeletionRequestRequestTypeDef",
    {
        "KeyId": str,
        "PendingWindowInDays": NotRequired[int],
    },
)

ScheduleKeyDeletionResponseTypeDef = TypedDict(
    "ScheduleKeyDeletionResponseTypeDef",
    {
        "KeyId": str,
        "DeletionDate": datetime,
        "KeyState": KeyStateType,
        "PendingWindowInDays": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SignRequestRequestTypeDef = TypedDict(
    "SignRequestRequestTypeDef",
    {
        "KeyId": str,
        "Message": Union[bytes, IO[bytes], StreamingBody],
        "SigningAlgorithm": SigningAlgorithmSpecType,
        "MessageType": NotRequired[MessageTypeType],
        "GrantTokens": NotRequired[Sequence[str]],
    },
)

SignResponseTypeDef = TypedDict(
    "SignResponseTypeDef",
    {
        "KeyId": str,
        "Signature": bytes,
        "SigningAlgorithm": SigningAlgorithmSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "KeyId": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "TagKey": str,
        "TagValue": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "KeyId": str,
        "TagKeys": Sequence[str],
    },
)

UpdateAliasRequestRequestTypeDef = TypedDict(
    "UpdateAliasRequestRequestTypeDef",
    {
        "AliasName": str,
        "TargetKeyId": str,
    },
)

UpdateCustomKeyStoreRequestRequestTypeDef = TypedDict(
    "UpdateCustomKeyStoreRequestRequestTypeDef",
    {
        "CustomKeyStoreId": str,
        "NewCustomKeyStoreName": NotRequired[str],
        "KeyStorePassword": NotRequired[str],
        "CloudHsmClusterId": NotRequired[str],
    },
)

UpdateKeyDescriptionRequestRequestTypeDef = TypedDict(
    "UpdateKeyDescriptionRequestRequestTypeDef",
    {
        "KeyId": str,
        "Description": str,
    },
)

UpdatePrimaryRegionRequestRequestTypeDef = TypedDict(
    "UpdatePrimaryRegionRequestRequestTypeDef",
    {
        "KeyId": str,
        "PrimaryRegion": str,
    },
)

VerifyRequestRequestTypeDef = TypedDict(
    "VerifyRequestRequestTypeDef",
    {
        "KeyId": str,
        "Message": Union[bytes, IO[bytes], StreamingBody],
        "Signature": Union[bytes, IO[bytes], StreamingBody],
        "SigningAlgorithm": SigningAlgorithmSpecType,
        "MessageType": NotRequired[MessageTypeType],
        "GrantTokens": NotRequired[Sequence[str]],
    },
)

VerifyResponseTypeDef = TypedDict(
    "VerifyResponseTypeDef",
    {
        "KeyId": str,
        "SignatureValid": bool,
        "SigningAlgorithm": SigningAlgorithmSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
