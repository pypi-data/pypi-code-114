"""
Type annotations for secretsmanager service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/type_defs.html)

Usage::

    ```python
    from mypy_boto3_secretsmanager.type_defs import CancelRotateSecretRequestRequestTypeDef

    data: CancelRotateSecretRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import FilterNameStringTypeType, SortOrderTypeType, StatusTypeType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CancelRotateSecretRequestRequestTypeDef",
    "CancelRotateSecretResponseTypeDef",
    "CreateSecretRequestRequestTypeDef",
    "CreateSecretResponseTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteResourcePolicyResponseTypeDef",
    "DeleteSecretRequestRequestTypeDef",
    "DeleteSecretResponseTypeDef",
    "DescribeSecretRequestRequestTypeDef",
    "DescribeSecretResponseTypeDef",
    "FilterTypeDef",
    "GetRandomPasswordRequestRequestTypeDef",
    "GetRandomPasswordResponseTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetSecretValueRequestRequestTypeDef",
    "GetSecretValueResponseTypeDef",
    "ListSecretVersionIdsRequestRequestTypeDef",
    "ListSecretVersionIdsResponseTypeDef",
    "ListSecretsRequestRequestTypeDef",
    "ListSecretsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "PutSecretValueRequestRequestTypeDef",
    "PutSecretValueResponseTypeDef",
    "RemoveRegionsFromReplicationRequestRequestTypeDef",
    "RemoveRegionsFromReplicationResponseTypeDef",
    "ReplicaRegionTypeTypeDef",
    "ReplicateSecretToRegionsRequestRequestTypeDef",
    "ReplicateSecretToRegionsResponseTypeDef",
    "ReplicationStatusTypeTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreSecretRequestRequestTypeDef",
    "RestoreSecretResponseTypeDef",
    "RotateSecretRequestRequestTypeDef",
    "RotateSecretResponseTypeDef",
    "RotationRulesTypeTypeDef",
    "SecretListEntryTypeDef",
    "SecretVersionsListEntryTypeDef",
    "StopReplicationToReplicaRequestRequestTypeDef",
    "StopReplicationToReplicaResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateSecretRequestRequestTypeDef",
    "UpdateSecretResponseTypeDef",
    "UpdateSecretVersionStageRequestRequestTypeDef",
    "UpdateSecretVersionStageResponseTypeDef",
    "ValidateResourcePolicyRequestRequestTypeDef",
    "ValidateResourcePolicyResponseTypeDef",
    "ValidationErrorsEntryTypeDef",
)

CancelRotateSecretRequestRequestTypeDef = TypedDict(
    "CancelRotateSecretRequestRequestTypeDef",
    {
        "SecretId": str,
    },
)

CancelRotateSecretResponseTypeDef = TypedDict(
    "CancelRotateSecretResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "VersionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSecretRequestRequestTypeDef = TypedDict(
    "CreateSecretRequestRequestTypeDef",
    {
        "Name": str,
        "ClientRequestToken": NotRequired[str],
        "Description": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "SecretBinary": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "SecretString": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "AddReplicaRegions": NotRequired[Sequence["ReplicaRegionTypeTypeDef"]],
        "ForceOverwriteReplicaSecret": NotRequired[bool],
    },
)

CreateSecretResponseTypeDef = TypedDict(
    "CreateSecretResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "VersionId": str,
        "ReplicationStatus": List["ReplicationStatusTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "SecretId": str,
    },
)

DeleteResourcePolicyResponseTypeDef = TypedDict(
    "DeleteResourcePolicyResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSecretRequestRequestTypeDef = TypedDict(
    "DeleteSecretRequestRequestTypeDef",
    {
        "SecretId": str,
        "RecoveryWindowInDays": NotRequired[int],
        "ForceDeleteWithoutRecovery": NotRequired[bool],
    },
)

DeleteSecretResponseTypeDef = TypedDict(
    "DeleteSecretResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "DeletionDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecretRequestRequestTypeDef = TypedDict(
    "DescribeSecretRequestRequestTypeDef",
    {
        "SecretId": str,
    },
)

DescribeSecretResponseTypeDef = TypedDict(
    "DescribeSecretResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "Description": str,
        "KmsKeyId": str,
        "RotationEnabled": bool,
        "RotationLambdaARN": str,
        "RotationRules": "RotationRulesTypeTypeDef",
        "LastRotatedDate": datetime,
        "LastChangedDate": datetime,
        "LastAccessedDate": datetime,
        "DeletedDate": datetime,
        "Tags": List["TagTypeDef"],
        "VersionIdsToStages": Dict[str, List[str]],
        "OwningService": str,
        "CreatedDate": datetime,
        "PrimaryRegion": str,
        "ReplicationStatus": List["ReplicationStatusTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Key": NotRequired[FilterNameStringTypeType],
        "Values": NotRequired[Sequence[str]],
    },
)

GetRandomPasswordRequestRequestTypeDef = TypedDict(
    "GetRandomPasswordRequestRequestTypeDef",
    {
        "PasswordLength": NotRequired[int],
        "ExcludeCharacters": NotRequired[str],
        "ExcludeNumbers": NotRequired[bool],
        "ExcludePunctuation": NotRequired[bool],
        "ExcludeUppercase": NotRequired[bool],
        "ExcludeLowercase": NotRequired[bool],
        "IncludeSpace": NotRequired[bool],
        "RequireEachIncludedType": NotRequired[bool],
    },
)

GetRandomPasswordResponseTypeDef = TypedDict(
    "GetRandomPasswordResponseTypeDef",
    {
        "RandomPassword": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "SecretId": str,
    },
)

GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "ResourcePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSecretValueRequestRequestTypeDef = TypedDict(
    "GetSecretValueRequestRequestTypeDef",
    {
        "SecretId": str,
        "VersionId": NotRequired[str],
        "VersionStage": NotRequired[str],
    },
)

GetSecretValueResponseTypeDef = TypedDict(
    "GetSecretValueResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "VersionId": str,
        "SecretBinary": bytes,
        "SecretString": str,
        "VersionStages": List[str],
        "CreatedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSecretVersionIdsRequestRequestTypeDef = TypedDict(
    "ListSecretVersionIdsRequestRequestTypeDef",
    {
        "SecretId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "IncludeDeprecated": NotRequired[bool],
    },
)

ListSecretVersionIdsResponseTypeDef = TypedDict(
    "ListSecretVersionIdsResponseTypeDef",
    {
        "Versions": List["SecretVersionsListEntryTypeDef"],
        "NextToken": str,
        "ARN": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSecretsRequestRequestTypeDef = TypedDict(
    "ListSecretsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "SortOrder": NotRequired[SortOrderTypeType],
    },
)

ListSecretsResponseTypeDef = TypedDict(
    "ListSecretsResponseTypeDef",
    {
        "SecretList": List["SecretListEntryTypeDef"],
        "NextToken": str,
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

PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "SecretId": str,
        "ResourcePolicy": str,
        "BlockPublicPolicy": NotRequired[bool],
    },
)

PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutSecretValueRequestRequestTypeDef = TypedDict(
    "PutSecretValueRequestRequestTypeDef",
    {
        "SecretId": str,
        "ClientRequestToken": NotRequired[str],
        "SecretBinary": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "SecretString": NotRequired[str],
        "VersionStages": NotRequired[Sequence[str]],
    },
)

PutSecretValueResponseTypeDef = TypedDict(
    "PutSecretValueResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "VersionId": str,
        "VersionStages": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveRegionsFromReplicationRequestRequestTypeDef = TypedDict(
    "RemoveRegionsFromReplicationRequestRequestTypeDef",
    {
        "SecretId": str,
        "RemoveReplicaRegions": Sequence[str],
    },
)

RemoveRegionsFromReplicationResponseTypeDef = TypedDict(
    "RemoveRegionsFromReplicationResponseTypeDef",
    {
        "ARN": str,
        "ReplicationStatus": List["ReplicationStatusTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplicaRegionTypeTypeDef = TypedDict(
    "ReplicaRegionTypeTypeDef",
    {
        "Region": NotRequired[str],
        "KmsKeyId": NotRequired[str],
    },
)

ReplicateSecretToRegionsRequestRequestTypeDef = TypedDict(
    "ReplicateSecretToRegionsRequestRequestTypeDef",
    {
        "SecretId": str,
        "AddReplicaRegions": Sequence["ReplicaRegionTypeTypeDef"],
        "ForceOverwriteReplicaSecret": NotRequired[bool],
    },
)

ReplicateSecretToRegionsResponseTypeDef = TypedDict(
    "ReplicateSecretToRegionsResponseTypeDef",
    {
        "ARN": str,
        "ReplicationStatus": List["ReplicationStatusTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplicationStatusTypeTypeDef = TypedDict(
    "ReplicationStatusTypeTypeDef",
    {
        "Region": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Status": NotRequired[StatusTypeType],
        "StatusMessage": NotRequired[str],
        "LastAccessedDate": NotRequired[datetime],
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

RestoreSecretRequestRequestTypeDef = TypedDict(
    "RestoreSecretRequestRequestTypeDef",
    {
        "SecretId": str,
    },
)

RestoreSecretResponseTypeDef = TypedDict(
    "RestoreSecretResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RotateSecretRequestRequestTypeDef = TypedDict(
    "RotateSecretRequestRequestTypeDef",
    {
        "SecretId": str,
        "ClientRequestToken": NotRequired[str],
        "RotationLambdaARN": NotRequired[str],
        "RotationRules": NotRequired["RotationRulesTypeTypeDef"],
        "RotateImmediately": NotRequired[bool],
    },
)

RotateSecretResponseTypeDef = TypedDict(
    "RotateSecretResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "VersionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RotationRulesTypeTypeDef = TypedDict(
    "RotationRulesTypeTypeDef",
    {
        "AutomaticallyAfterDays": NotRequired[int],
        "Duration": NotRequired[str],
        "ScheduleExpression": NotRequired[str],
    },
)

SecretListEntryTypeDef = TypedDict(
    "SecretListEntryTypeDef",
    {
        "ARN": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "RotationEnabled": NotRequired[bool],
        "RotationLambdaARN": NotRequired[str],
        "RotationRules": NotRequired["RotationRulesTypeTypeDef"],
        "LastRotatedDate": NotRequired[datetime],
        "LastChangedDate": NotRequired[datetime],
        "LastAccessedDate": NotRequired[datetime],
        "DeletedDate": NotRequired[datetime],
        "Tags": NotRequired[List["TagTypeDef"]],
        "SecretVersionsToStages": NotRequired[Dict[str, List[str]]],
        "OwningService": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "PrimaryRegion": NotRequired[str],
    },
)

SecretVersionsListEntryTypeDef = TypedDict(
    "SecretVersionsListEntryTypeDef",
    {
        "VersionId": NotRequired[str],
        "VersionStages": NotRequired[List[str]],
        "LastAccessedDate": NotRequired[datetime],
        "CreatedDate": NotRequired[datetime],
        "KmsKeyIds": NotRequired[List[str]],
    },
)

StopReplicationToReplicaRequestRequestTypeDef = TypedDict(
    "StopReplicationToReplicaRequestRequestTypeDef",
    {
        "SecretId": str,
    },
)

StopReplicationToReplicaResponseTypeDef = TypedDict(
    "StopReplicationToReplicaResponseTypeDef",
    {
        "ARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "SecretId": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "SecretId": str,
        "TagKeys": Sequence[str],
    },
)

UpdateSecretRequestRequestTypeDef = TypedDict(
    "UpdateSecretRequestRequestTypeDef",
    {
        "SecretId": str,
        "ClientRequestToken": NotRequired[str],
        "Description": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "SecretBinary": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "SecretString": NotRequired[str],
    },
)

UpdateSecretResponseTypeDef = TypedDict(
    "UpdateSecretResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "VersionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSecretVersionStageRequestRequestTypeDef = TypedDict(
    "UpdateSecretVersionStageRequestRequestTypeDef",
    {
        "SecretId": str,
        "VersionStage": str,
        "RemoveFromVersionId": NotRequired[str],
        "MoveToVersionId": NotRequired[str],
    },
)

UpdateSecretVersionStageResponseTypeDef = TypedDict(
    "UpdateSecretVersionStageResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidateResourcePolicyRequestRequestTypeDef = TypedDict(
    "ValidateResourcePolicyRequestRequestTypeDef",
    {
        "ResourcePolicy": str,
        "SecretId": NotRequired[str],
    },
)

ValidateResourcePolicyResponseTypeDef = TypedDict(
    "ValidateResourcePolicyResponseTypeDef",
    {
        "PolicyValidationPassed": bool,
        "ValidationErrors": List["ValidationErrorsEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidationErrorsEntryTypeDef = TypedDict(
    "ValidationErrorsEntryTypeDef",
    {
        "CheckName": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
