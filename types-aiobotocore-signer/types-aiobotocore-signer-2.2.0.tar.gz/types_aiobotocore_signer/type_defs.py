"""
Type annotations for signer service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_signer/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_signer.type_defs import AddProfilePermissionRequestRequestTypeDef

    data: AddProfilePermissionRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    EncryptionAlgorithmType,
    HashAlgorithmType,
    ImageFormatType,
    SigningProfileStatusType,
    SigningStatusType,
    ValidityTypeType,
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
    "AddProfilePermissionRequestRequestTypeDef",
    "AddProfilePermissionResponseTypeDef",
    "CancelSigningProfileRequestRequestTypeDef",
    "DescribeSigningJobRequestRequestTypeDef",
    "DescribeSigningJobResponseTypeDef",
    "DestinationTypeDef",
    "EncryptionAlgorithmOptionsTypeDef",
    "GetSigningPlatformRequestRequestTypeDef",
    "GetSigningPlatformResponseTypeDef",
    "GetSigningProfileRequestRequestTypeDef",
    "GetSigningProfileResponseTypeDef",
    "HashAlgorithmOptionsTypeDef",
    "ListProfilePermissionsRequestRequestTypeDef",
    "ListProfilePermissionsResponseTypeDef",
    "ListSigningJobsRequestRequestTypeDef",
    "ListSigningJobsResponseTypeDef",
    "ListSigningPlatformsRequestRequestTypeDef",
    "ListSigningPlatformsResponseTypeDef",
    "ListSigningProfilesRequestRequestTypeDef",
    "ListSigningProfilesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "PutSigningProfileRequestRequestTypeDef",
    "PutSigningProfileResponseTypeDef",
    "RemoveProfilePermissionRequestRequestTypeDef",
    "RemoveProfilePermissionResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeSignatureRequestRequestTypeDef",
    "RevokeSigningProfileRequestRequestTypeDef",
    "S3DestinationTypeDef",
    "S3SignedObjectTypeDef",
    "S3SourceTypeDef",
    "SignatureValidityPeriodTypeDef",
    "SignedObjectTypeDef",
    "SigningConfigurationOverridesTypeDef",
    "SigningConfigurationTypeDef",
    "SigningImageFormatTypeDef",
    "SigningJobRevocationRecordTypeDef",
    "SigningJobTypeDef",
    "SigningMaterialTypeDef",
    "SigningPlatformOverridesTypeDef",
    "SigningPlatformTypeDef",
    "SigningProfileRevocationRecordTypeDef",
    "SigningProfileTypeDef",
    "SourceTypeDef",
    "StartSigningJobRequestRequestTypeDef",
    "StartSigningJobResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "WaiterConfigTypeDef",
)

AddProfilePermissionRequestRequestTypeDef = TypedDict(
    "AddProfilePermissionRequestRequestTypeDef",
    {
        "profileName": str,
        "action": str,
        "principal": str,
        "statementId": str,
        "profileVersion": NotRequired[str],
        "revisionId": NotRequired[str],
    },
)

AddProfilePermissionResponseTypeDef = TypedDict(
    "AddProfilePermissionResponseTypeDef",
    {
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelSigningProfileRequestRequestTypeDef = TypedDict(
    "CancelSigningProfileRequestRequestTypeDef",
    {
        "profileName": str,
    },
)

DescribeSigningJobRequestRequestTypeDef = TypedDict(
    "DescribeSigningJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

DescribeSigningJobResponseTypeDef = TypedDict(
    "DescribeSigningJobResponseTypeDef",
    {
        "jobId": str,
        "source": "SourceTypeDef",
        "signingMaterial": "SigningMaterialTypeDef",
        "platformId": str,
        "platformDisplayName": str,
        "profileName": str,
        "profileVersion": str,
        "overrides": "SigningPlatformOverridesTypeDef",
        "signingParameters": Dict[str, str],
        "createdAt": datetime,
        "completedAt": datetime,
        "signatureExpiresAt": datetime,
        "requestedBy": str,
        "status": SigningStatusType,
        "statusReason": str,
        "revocationRecord": "SigningJobRevocationRecordTypeDef",
        "signedObject": "SignedObjectTypeDef",
        "jobOwner": str,
        "jobInvoker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "s3": NotRequired["S3DestinationTypeDef"],
    },
)

EncryptionAlgorithmOptionsTypeDef = TypedDict(
    "EncryptionAlgorithmOptionsTypeDef",
    {
        "allowedValues": List[EncryptionAlgorithmType],
        "defaultValue": EncryptionAlgorithmType,
    },
)

GetSigningPlatformRequestRequestTypeDef = TypedDict(
    "GetSigningPlatformRequestRequestTypeDef",
    {
        "platformId": str,
    },
)

GetSigningPlatformResponseTypeDef = TypedDict(
    "GetSigningPlatformResponseTypeDef",
    {
        "platformId": str,
        "displayName": str,
        "partner": str,
        "target": str,
        "category": Literal["AWSIoT"],
        "signingConfiguration": "SigningConfigurationTypeDef",
        "signingImageFormat": "SigningImageFormatTypeDef",
        "maxSizeInMB": int,
        "revocationSupported": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSigningProfileRequestRequestTypeDef = TypedDict(
    "GetSigningProfileRequestRequestTypeDef",
    {
        "profileName": str,
        "profileOwner": NotRequired[str],
    },
)

GetSigningProfileResponseTypeDef = TypedDict(
    "GetSigningProfileResponseTypeDef",
    {
        "profileName": str,
        "profileVersion": str,
        "profileVersionArn": str,
        "revocationRecord": "SigningProfileRevocationRecordTypeDef",
        "signingMaterial": "SigningMaterialTypeDef",
        "platformId": str,
        "platformDisplayName": str,
        "signatureValidityPeriod": "SignatureValidityPeriodTypeDef",
        "overrides": "SigningPlatformOverridesTypeDef",
        "signingParameters": Dict[str, str],
        "status": SigningProfileStatusType,
        "statusReason": str,
        "arn": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HashAlgorithmOptionsTypeDef = TypedDict(
    "HashAlgorithmOptionsTypeDef",
    {
        "allowedValues": List[HashAlgorithmType],
        "defaultValue": HashAlgorithmType,
    },
)

ListProfilePermissionsRequestRequestTypeDef = TypedDict(
    "ListProfilePermissionsRequestRequestTypeDef",
    {
        "profileName": str,
        "nextToken": NotRequired[str],
    },
)

ListProfilePermissionsResponseTypeDef = TypedDict(
    "ListProfilePermissionsResponseTypeDef",
    {
        "revisionId": str,
        "policySizeBytes": int,
        "permissions": List["PermissionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSigningJobsRequestRequestTypeDef = TypedDict(
    "ListSigningJobsRequestRequestTypeDef",
    {
        "status": NotRequired[SigningStatusType],
        "platformId": NotRequired[str],
        "requestedBy": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "isRevoked": NotRequired[bool],
        "signatureExpiresBefore": NotRequired[Union[datetime, str]],
        "signatureExpiresAfter": NotRequired[Union[datetime, str]],
        "jobInvoker": NotRequired[str],
    },
)

ListSigningJobsResponseTypeDef = TypedDict(
    "ListSigningJobsResponseTypeDef",
    {
        "jobs": List["SigningJobTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSigningPlatformsRequestRequestTypeDef = TypedDict(
    "ListSigningPlatformsRequestRequestTypeDef",
    {
        "category": NotRequired[str],
        "partner": NotRequired[str],
        "target": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListSigningPlatformsResponseTypeDef = TypedDict(
    "ListSigningPlatformsResponseTypeDef",
    {
        "platforms": List["SigningPlatformTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSigningProfilesRequestRequestTypeDef = TypedDict(
    "ListSigningProfilesRequestRequestTypeDef",
    {
        "includeCanceled": NotRequired[bool],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "platformId": NotRequired[str],
        "statuses": NotRequired[Sequence[SigningProfileStatusType]],
    },
)

ListSigningProfilesResponseTypeDef = TypedDict(
    "ListSigningProfilesResponseTypeDef",
    {
        "profiles": List["SigningProfileTypeDef"],
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)

PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {
        "action": NotRequired[str],
        "principal": NotRequired[str],
        "statementId": NotRequired[str],
        "profileVersion": NotRequired[str],
    },
)

PutSigningProfileRequestRequestTypeDef = TypedDict(
    "PutSigningProfileRequestRequestTypeDef",
    {
        "profileName": str,
        "platformId": str,
        "signingMaterial": NotRequired["SigningMaterialTypeDef"],
        "signatureValidityPeriod": NotRequired["SignatureValidityPeriodTypeDef"],
        "overrides": NotRequired["SigningPlatformOverridesTypeDef"],
        "signingParameters": NotRequired[Mapping[str, str]],
        "tags": NotRequired[Mapping[str, str]],
    },
)

PutSigningProfileResponseTypeDef = TypedDict(
    "PutSigningProfileResponseTypeDef",
    {
        "arn": str,
        "profileVersion": str,
        "profileVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveProfilePermissionRequestRequestTypeDef = TypedDict(
    "RemoveProfilePermissionRequestRequestTypeDef",
    {
        "profileName": str,
        "revisionId": str,
        "statementId": str,
    },
)

RemoveProfilePermissionResponseTypeDef = TypedDict(
    "RemoveProfilePermissionResponseTypeDef",
    {
        "revisionId": str,
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

RevokeSignatureRequestRequestTypeDef = TypedDict(
    "RevokeSignatureRequestRequestTypeDef",
    {
        "jobId": str,
        "reason": str,
        "jobOwner": NotRequired[str],
    },
)

RevokeSigningProfileRequestRequestTypeDef = TypedDict(
    "RevokeSigningProfileRequestRequestTypeDef",
    {
        "profileName": str,
        "profileVersion": str,
        "reason": str,
        "effectiveTime": Union[datetime, str],
    },
)

S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "bucketName": NotRequired[str],
        "prefix": NotRequired[str],
    },
)

S3SignedObjectTypeDef = TypedDict(
    "S3SignedObjectTypeDef",
    {
        "bucketName": NotRequired[str],
        "key": NotRequired[str],
    },
)

S3SourceTypeDef = TypedDict(
    "S3SourceTypeDef",
    {
        "bucketName": str,
        "key": str,
        "version": str,
    },
)

SignatureValidityPeriodTypeDef = TypedDict(
    "SignatureValidityPeriodTypeDef",
    {
        "value": NotRequired[int],
        "type": NotRequired[ValidityTypeType],
    },
)

SignedObjectTypeDef = TypedDict(
    "SignedObjectTypeDef",
    {
        "s3": NotRequired["S3SignedObjectTypeDef"],
    },
)

SigningConfigurationOverridesTypeDef = TypedDict(
    "SigningConfigurationOverridesTypeDef",
    {
        "encryptionAlgorithm": NotRequired[EncryptionAlgorithmType],
        "hashAlgorithm": NotRequired[HashAlgorithmType],
    },
)

SigningConfigurationTypeDef = TypedDict(
    "SigningConfigurationTypeDef",
    {
        "encryptionAlgorithmOptions": "EncryptionAlgorithmOptionsTypeDef",
        "hashAlgorithmOptions": "HashAlgorithmOptionsTypeDef",
    },
)

SigningImageFormatTypeDef = TypedDict(
    "SigningImageFormatTypeDef",
    {
        "supportedFormats": List[ImageFormatType],
        "defaultFormat": ImageFormatType,
    },
)

SigningJobRevocationRecordTypeDef = TypedDict(
    "SigningJobRevocationRecordTypeDef",
    {
        "reason": NotRequired[str],
        "revokedAt": NotRequired[datetime],
        "revokedBy": NotRequired[str],
    },
)

SigningJobTypeDef = TypedDict(
    "SigningJobTypeDef",
    {
        "jobId": NotRequired[str],
        "source": NotRequired["SourceTypeDef"],
        "signedObject": NotRequired["SignedObjectTypeDef"],
        "signingMaterial": NotRequired["SigningMaterialTypeDef"],
        "createdAt": NotRequired[datetime],
        "status": NotRequired[SigningStatusType],
        "isRevoked": NotRequired[bool],
        "profileName": NotRequired[str],
        "profileVersion": NotRequired[str],
        "platformId": NotRequired[str],
        "platformDisplayName": NotRequired[str],
        "signatureExpiresAt": NotRequired[datetime],
        "jobOwner": NotRequired[str],
        "jobInvoker": NotRequired[str],
    },
)

SigningMaterialTypeDef = TypedDict(
    "SigningMaterialTypeDef",
    {
        "certificateArn": str,
    },
)

SigningPlatformOverridesTypeDef = TypedDict(
    "SigningPlatformOverridesTypeDef",
    {
        "signingConfiguration": NotRequired["SigningConfigurationOverridesTypeDef"],
        "signingImageFormat": NotRequired[ImageFormatType],
    },
)

SigningPlatformTypeDef = TypedDict(
    "SigningPlatformTypeDef",
    {
        "platformId": NotRequired[str],
        "displayName": NotRequired[str],
        "partner": NotRequired[str],
        "target": NotRequired[str],
        "category": NotRequired[Literal["AWSIoT"]],
        "signingConfiguration": NotRequired["SigningConfigurationTypeDef"],
        "signingImageFormat": NotRequired["SigningImageFormatTypeDef"],
        "maxSizeInMB": NotRequired[int],
        "revocationSupported": NotRequired[bool],
    },
)

SigningProfileRevocationRecordTypeDef = TypedDict(
    "SigningProfileRevocationRecordTypeDef",
    {
        "revocationEffectiveFrom": NotRequired[datetime],
        "revokedAt": NotRequired[datetime],
        "revokedBy": NotRequired[str],
    },
)

SigningProfileTypeDef = TypedDict(
    "SigningProfileTypeDef",
    {
        "profileName": NotRequired[str],
        "profileVersion": NotRequired[str],
        "profileVersionArn": NotRequired[str],
        "signingMaterial": NotRequired["SigningMaterialTypeDef"],
        "signatureValidityPeriod": NotRequired["SignatureValidityPeriodTypeDef"],
        "platformId": NotRequired[str],
        "platformDisplayName": NotRequired[str],
        "signingParameters": NotRequired[Dict[str, str]],
        "status": NotRequired[SigningProfileStatusType],
        "arn": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "s3": NotRequired["S3SourceTypeDef"],
    },
)

StartSigningJobRequestRequestTypeDef = TypedDict(
    "StartSigningJobRequestRequestTypeDef",
    {
        "source": "SourceTypeDef",
        "destination": "DestinationTypeDef",
        "profileName": str,
        "clientRequestToken": str,
        "profileOwner": NotRequired[str],
    },
)

StartSigningJobResponseTypeDef = TypedDict(
    "StartSigningJobResponseTypeDef",
    {
        "jobId": str,
        "jobOwner": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
