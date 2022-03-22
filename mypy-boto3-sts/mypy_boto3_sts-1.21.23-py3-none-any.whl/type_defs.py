"""
Type annotations for sts service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sts/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sts.type_defs import AssumeRoleRequestRequestTypeDef

    data: AssumeRoleRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, Sequence

from typing_extensions import NotRequired

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssumeRoleRequestRequestTypeDef",
    "AssumeRoleResponseTypeDef",
    "AssumeRoleWithSAMLRequestRequestTypeDef",
    "AssumeRoleWithSAMLResponseTypeDef",
    "AssumeRoleWithWebIdentityRequestRequestTypeDef",
    "AssumeRoleWithWebIdentityResponseTypeDef",
    "AssumedRoleUserTypeDef",
    "CredentialsTypeDef",
    "DecodeAuthorizationMessageRequestRequestTypeDef",
    "DecodeAuthorizationMessageResponseTypeDef",
    "FederatedUserTypeDef",
    "GetAccessKeyInfoRequestRequestTypeDef",
    "GetAccessKeyInfoResponseTypeDef",
    "GetCallerIdentityResponseTypeDef",
    "GetFederationTokenRequestRequestTypeDef",
    "GetFederationTokenResponseTypeDef",
    "GetSessionTokenRequestRequestTypeDef",
    "GetSessionTokenResponseTypeDef",
    "PolicyDescriptorTypeTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
)

AssumeRoleRequestRequestTypeDef = TypedDict(
    "AssumeRoleRequestRequestTypeDef",
    {
        "RoleArn": str,
        "RoleSessionName": str,
        "PolicyArns": NotRequired[Sequence["PolicyDescriptorTypeTypeDef"]],
        "Policy": NotRequired[str],
        "DurationSeconds": NotRequired[int],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "TransitiveTagKeys": NotRequired[Sequence[str]],
        "ExternalId": NotRequired[str],
        "SerialNumber": NotRequired[str],
        "TokenCode": NotRequired[str],
        "SourceIdentity": NotRequired[str],
    },
)

AssumeRoleResponseTypeDef = TypedDict(
    "AssumeRoleResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "AssumedRoleUser": "AssumedRoleUserTypeDef",
        "PackedPolicySize": int,
        "SourceIdentity": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssumeRoleWithSAMLRequestRequestTypeDef = TypedDict(
    "AssumeRoleWithSAMLRequestRequestTypeDef",
    {
        "RoleArn": str,
        "PrincipalArn": str,
        "SAMLAssertion": str,
        "PolicyArns": NotRequired[Sequence["PolicyDescriptorTypeTypeDef"]],
        "Policy": NotRequired[str],
        "DurationSeconds": NotRequired[int],
    },
)

AssumeRoleWithSAMLResponseTypeDef = TypedDict(
    "AssumeRoleWithSAMLResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "AssumedRoleUser": "AssumedRoleUserTypeDef",
        "PackedPolicySize": int,
        "Subject": str,
        "SubjectType": str,
        "Issuer": str,
        "Audience": str,
        "NameQualifier": str,
        "SourceIdentity": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssumeRoleWithWebIdentityRequestRequestTypeDef = TypedDict(
    "AssumeRoleWithWebIdentityRequestRequestTypeDef",
    {
        "RoleArn": str,
        "RoleSessionName": str,
        "WebIdentityToken": str,
        "ProviderId": NotRequired[str],
        "PolicyArns": NotRequired[Sequence["PolicyDescriptorTypeTypeDef"]],
        "Policy": NotRequired[str],
        "DurationSeconds": NotRequired[int],
    },
)

AssumeRoleWithWebIdentityResponseTypeDef = TypedDict(
    "AssumeRoleWithWebIdentityResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "SubjectFromWebIdentityToken": str,
        "AssumedRoleUser": "AssumedRoleUserTypeDef",
        "PackedPolicySize": int,
        "Provider": str,
        "Audience": str,
        "SourceIdentity": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssumedRoleUserTypeDef = TypedDict(
    "AssumedRoleUserTypeDef",
    {
        "AssumedRoleId": str,
        "Arn": str,
    },
)

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "AccessKeyId": str,
        "SecretAccessKey": str,
        "SessionToken": str,
        "Expiration": datetime,
    },
)

DecodeAuthorizationMessageRequestRequestTypeDef = TypedDict(
    "DecodeAuthorizationMessageRequestRequestTypeDef",
    {
        "EncodedMessage": str,
    },
)

DecodeAuthorizationMessageResponseTypeDef = TypedDict(
    "DecodeAuthorizationMessageResponseTypeDef",
    {
        "DecodedMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FederatedUserTypeDef = TypedDict(
    "FederatedUserTypeDef",
    {
        "FederatedUserId": str,
        "Arn": str,
    },
)

GetAccessKeyInfoRequestRequestTypeDef = TypedDict(
    "GetAccessKeyInfoRequestRequestTypeDef",
    {
        "AccessKeyId": str,
    },
)

GetAccessKeyInfoResponseTypeDef = TypedDict(
    "GetAccessKeyInfoResponseTypeDef",
    {
        "Account": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCallerIdentityResponseTypeDef = TypedDict(
    "GetCallerIdentityResponseTypeDef",
    {
        "UserId": str,
        "Account": str,
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFederationTokenRequestRequestTypeDef = TypedDict(
    "GetFederationTokenRequestRequestTypeDef",
    {
        "Name": str,
        "Policy": NotRequired[str],
        "PolicyArns": NotRequired[Sequence["PolicyDescriptorTypeTypeDef"]],
        "DurationSeconds": NotRequired[int],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

GetFederationTokenResponseTypeDef = TypedDict(
    "GetFederationTokenResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "FederatedUser": "FederatedUserTypeDef",
        "PackedPolicySize": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSessionTokenRequestRequestTypeDef = TypedDict(
    "GetSessionTokenRequestRequestTypeDef",
    {
        "DurationSeconds": NotRequired[int],
        "SerialNumber": NotRequired[str],
        "TokenCode": NotRequired[str],
    },
)

GetSessionTokenResponseTypeDef = TypedDict(
    "GetSessionTokenResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PolicyDescriptorTypeTypeDef = TypedDict(
    "PolicyDescriptorTypeTypeDef",
    {
        "arn": NotRequired[str],
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
