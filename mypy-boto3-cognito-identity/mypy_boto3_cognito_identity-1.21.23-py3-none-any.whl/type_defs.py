"""
Type annotations for cognito-identity service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cognito_identity.type_defs import CognitoIdentityProviderTypeDef

    data: CognitoIdentityProviderTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AmbiguousRoleResolutionTypeType,
    ErrorCodeType,
    MappingRuleMatchTypeType,
    RoleMappingTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CognitoIdentityProviderTypeDef",
    "CreateIdentityPoolInputRequestTypeDef",
    "CredentialsTypeDef",
    "DeleteIdentitiesInputRequestTypeDef",
    "DeleteIdentitiesResponseTypeDef",
    "DeleteIdentityPoolInputRequestTypeDef",
    "DescribeIdentityInputRequestTypeDef",
    "DescribeIdentityPoolInputRequestTypeDef",
    "GetCredentialsForIdentityInputRequestTypeDef",
    "GetCredentialsForIdentityResponseTypeDef",
    "GetIdInputRequestTypeDef",
    "GetIdResponseTypeDef",
    "GetIdentityPoolRolesInputRequestTypeDef",
    "GetIdentityPoolRolesResponseTypeDef",
    "GetOpenIdTokenForDeveloperIdentityInputRequestTypeDef",
    "GetOpenIdTokenForDeveloperIdentityResponseTypeDef",
    "GetOpenIdTokenInputRequestTypeDef",
    "GetOpenIdTokenResponseTypeDef",
    "GetPrincipalTagAttributeMapInputRequestTypeDef",
    "GetPrincipalTagAttributeMapResponseTypeDef",
    "IdentityDescriptionResponseMetadataTypeDef",
    "IdentityDescriptionTypeDef",
    "IdentityPoolRequestTypeDef",
    "IdentityPoolShortDescriptionTypeDef",
    "IdentityPoolTypeDef",
    "ListIdentitiesInputRequestTypeDef",
    "ListIdentitiesResponseTypeDef",
    "ListIdentityPoolsInputRequestTypeDef",
    "ListIdentityPoolsResponseTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LookupDeveloperIdentityInputRequestTypeDef",
    "LookupDeveloperIdentityResponseTypeDef",
    "MappingRuleTypeDef",
    "MergeDeveloperIdentitiesInputRequestTypeDef",
    "MergeDeveloperIdentitiesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RoleMappingTypeDef",
    "RulesConfigurationTypeTypeDef",
    "SetIdentityPoolRolesInputRequestTypeDef",
    "SetPrincipalTagAttributeMapInputRequestTypeDef",
    "SetPrincipalTagAttributeMapResponseTypeDef",
    "TagResourceInputRequestTypeDef",
    "UnlinkDeveloperIdentityInputRequestTypeDef",
    "UnlinkIdentityInputRequestTypeDef",
    "UnprocessedIdentityIdTypeDef",
    "UntagResourceInputRequestTypeDef",
)

CognitoIdentityProviderTypeDef = TypedDict(
    "CognitoIdentityProviderTypeDef",
    {
        "ProviderName": NotRequired[str],
        "ClientId": NotRequired[str],
        "ServerSideTokenCheck": NotRequired[bool],
    },
)

CreateIdentityPoolInputRequestTypeDef = TypedDict(
    "CreateIdentityPoolInputRequestTypeDef",
    {
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
        "AllowClassicFlow": NotRequired[bool],
        "SupportedLoginProviders": NotRequired[Mapping[str, str]],
        "DeveloperProviderName": NotRequired[str],
        "OpenIdConnectProviderARNs": NotRequired[Sequence[str]],
        "CognitoIdentityProviders": NotRequired[Sequence["CognitoIdentityProviderTypeDef"]],
        "SamlProviderARNs": NotRequired[Sequence[str]],
        "IdentityPoolTags": NotRequired[Mapping[str, str]],
    },
)

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "AccessKeyId": NotRequired[str],
        "SecretKey": NotRequired[str],
        "SessionToken": NotRequired[str],
        "Expiration": NotRequired[datetime],
    },
)

DeleteIdentitiesInputRequestTypeDef = TypedDict(
    "DeleteIdentitiesInputRequestTypeDef",
    {
        "IdentityIdsToDelete": Sequence[str],
    },
)

DeleteIdentitiesResponseTypeDef = TypedDict(
    "DeleteIdentitiesResponseTypeDef",
    {
        "UnprocessedIdentityIds": List["UnprocessedIdentityIdTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIdentityPoolInputRequestTypeDef = TypedDict(
    "DeleteIdentityPoolInputRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

DescribeIdentityInputRequestTypeDef = TypedDict(
    "DescribeIdentityInputRequestTypeDef",
    {
        "IdentityId": str,
    },
)

DescribeIdentityPoolInputRequestTypeDef = TypedDict(
    "DescribeIdentityPoolInputRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

GetCredentialsForIdentityInputRequestTypeDef = TypedDict(
    "GetCredentialsForIdentityInputRequestTypeDef",
    {
        "IdentityId": str,
        "Logins": NotRequired[Mapping[str, str]],
        "CustomRoleArn": NotRequired[str],
    },
)

GetCredentialsForIdentityResponseTypeDef = TypedDict(
    "GetCredentialsForIdentityResponseTypeDef",
    {
        "IdentityId": str,
        "Credentials": "CredentialsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdInputRequestTypeDef = TypedDict(
    "GetIdInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "AccountId": NotRequired[str],
        "Logins": NotRequired[Mapping[str, str]],
    },
)

GetIdResponseTypeDef = TypedDict(
    "GetIdResponseTypeDef",
    {
        "IdentityId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityPoolRolesInputRequestTypeDef = TypedDict(
    "GetIdentityPoolRolesInputRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

GetIdentityPoolRolesResponseTypeDef = TypedDict(
    "GetIdentityPoolRolesResponseTypeDef",
    {
        "IdentityPoolId": str,
        "Roles": Dict[str, str],
        "RoleMappings": Dict[str, "RoleMappingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOpenIdTokenForDeveloperIdentityInputRequestTypeDef = TypedDict(
    "GetOpenIdTokenForDeveloperIdentityInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "Logins": Mapping[str, str],
        "IdentityId": NotRequired[str],
        "PrincipalTags": NotRequired[Mapping[str, str]],
        "TokenDuration": NotRequired[int],
    },
)

GetOpenIdTokenForDeveloperIdentityResponseTypeDef = TypedDict(
    "GetOpenIdTokenForDeveloperIdentityResponseTypeDef",
    {
        "IdentityId": str,
        "Token": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOpenIdTokenInputRequestTypeDef = TypedDict(
    "GetOpenIdTokenInputRequestTypeDef",
    {
        "IdentityId": str,
        "Logins": NotRequired[Mapping[str, str]],
    },
)

GetOpenIdTokenResponseTypeDef = TypedDict(
    "GetOpenIdTokenResponseTypeDef",
    {
        "IdentityId": str,
        "Token": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPrincipalTagAttributeMapInputRequestTypeDef = TypedDict(
    "GetPrincipalTagAttributeMapInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
    },
)

GetPrincipalTagAttributeMapResponseTypeDef = TypedDict(
    "GetPrincipalTagAttributeMapResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
        "UseDefaults": bool,
        "PrincipalTags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityDescriptionResponseMetadataTypeDef = TypedDict(
    "IdentityDescriptionResponseMetadataTypeDef",
    {
        "IdentityId": str,
        "Logins": List[str],
        "CreationDate": datetime,
        "LastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityDescriptionTypeDef = TypedDict(
    "IdentityDescriptionTypeDef",
    {
        "IdentityId": NotRequired[str],
        "Logins": NotRequired[List[str]],
        "CreationDate": NotRequired[datetime],
        "LastModifiedDate": NotRequired[datetime],
    },
)

IdentityPoolRequestTypeDef = TypedDict(
    "IdentityPoolRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
        "AllowClassicFlow": NotRequired[bool],
        "SupportedLoginProviders": NotRequired[Mapping[str, str]],
        "DeveloperProviderName": NotRequired[str],
        "OpenIdConnectProviderARNs": NotRequired[Sequence[str]],
        "CognitoIdentityProviders": NotRequired[Sequence["CognitoIdentityProviderTypeDef"]],
        "SamlProviderARNs": NotRequired[Sequence[str]],
        "IdentityPoolTags": NotRequired[Mapping[str, str]],
    },
)

IdentityPoolShortDescriptionTypeDef = TypedDict(
    "IdentityPoolShortDescriptionTypeDef",
    {
        "IdentityPoolId": NotRequired[str],
        "IdentityPoolName": NotRequired[str],
    },
)

IdentityPoolTypeDef = TypedDict(
    "IdentityPoolTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
        "AllowClassicFlow": bool,
        "SupportedLoginProviders": Dict[str, str],
        "DeveloperProviderName": str,
        "OpenIdConnectProviderARNs": List[str],
        "CognitoIdentityProviders": List["CognitoIdentityProviderTypeDef"],
        "SamlProviderARNs": List[str],
        "IdentityPoolTags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIdentitiesInputRequestTypeDef = TypedDict(
    "ListIdentitiesInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "MaxResults": int,
        "NextToken": NotRequired[str],
        "HideDisabled": NotRequired[bool],
    },
)

ListIdentitiesResponseTypeDef = TypedDict(
    "ListIdentitiesResponseTypeDef",
    {
        "IdentityPoolId": str,
        "Identities": List["IdentityDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIdentityPoolsInputRequestTypeDef = TypedDict(
    "ListIdentityPoolsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": NotRequired[str],
    },
)

ListIdentityPoolsResponseTypeDef = TypedDict(
    "ListIdentityPoolsResponseTypeDef",
    {
        "IdentityPools": List["IdentityPoolShortDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
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

LookupDeveloperIdentityInputRequestTypeDef = TypedDict(
    "LookupDeveloperIdentityInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": NotRequired[str],
        "DeveloperUserIdentifier": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

LookupDeveloperIdentityResponseTypeDef = TypedDict(
    "LookupDeveloperIdentityResponseTypeDef",
    {
        "IdentityId": str,
        "DeveloperUserIdentifierList": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MappingRuleTypeDef = TypedDict(
    "MappingRuleTypeDef",
    {
        "Claim": str,
        "MatchType": MappingRuleMatchTypeType,
        "Value": str,
        "RoleARN": str,
    },
)

MergeDeveloperIdentitiesInputRequestTypeDef = TypedDict(
    "MergeDeveloperIdentitiesInputRequestTypeDef",
    {
        "SourceUserIdentifier": str,
        "DestinationUserIdentifier": str,
        "DeveloperProviderName": str,
        "IdentityPoolId": str,
    },
)

MergeDeveloperIdentitiesResponseTypeDef = TypedDict(
    "MergeDeveloperIdentitiesResponseTypeDef",
    {
        "IdentityId": str,
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

RoleMappingTypeDef = TypedDict(
    "RoleMappingTypeDef",
    {
        "Type": RoleMappingTypeType,
        "AmbiguousRoleResolution": NotRequired[AmbiguousRoleResolutionTypeType],
        "RulesConfiguration": NotRequired["RulesConfigurationTypeTypeDef"],
    },
)

RulesConfigurationTypeTypeDef = TypedDict(
    "RulesConfigurationTypeTypeDef",
    {
        "Rules": List["MappingRuleTypeDef"],
    },
)

SetIdentityPoolRolesInputRequestTypeDef = TypedDict(
    "SetIdentityPoolRolesInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "Roles": Mapping[str, str],
        "RoleMappings": NotRequired[Mapping[str, "RoleMappingTypeDef"]],
    },
)

SetPrincipalTagAttributeMapInputRequestTypeDef = TypedDict(
    "SetPrincipalTagAttributeMapInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
        "UseDefaults": NotRequired[bool],
        "PrincipalTags": NotRequired[Mapping[str, str]],
    },
)

SetPrincipalTagAttributeMapResponseTypeDef = TypedDict(
    "SetPrincipalTagAttributeMapResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
        "UseDefaults": bool,
        "PrincipalTags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

UnlinkDeveloperIdentityInputRequestTypeDef = TypedDict(
    "UnlinkDeveloperIdentityInputRequestTypeDef",
    {
        "IdentityId": str,
        "IdentityPoolId": str,
        "DeveloperProviderName": str,
        "DeveloperUserIdentifier": str,
    },
)

UnlinkIdentityInputRequestTypeDef = TypedDict(
    "UnlinkIdentityInputRequestTypeDef",
    {
        "IdentityId": str,
        "Logins": Mapping[str, str],
        "LoginsToRemove": Sequence[str],
    },
)

UnprocessedIdentityIdTypeDef = TypedDict(
    "UnprocessedIdentityIdTypeDef",
    {
        "IdentityId": NotRequired[str],
        "ErrorCode": NotRequired[ErrorCodeType],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
