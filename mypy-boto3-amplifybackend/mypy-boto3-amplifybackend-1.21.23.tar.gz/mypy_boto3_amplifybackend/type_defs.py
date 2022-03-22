"""
Type annotations for amplifybackend service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/type_defs.html)

Usage::

    ```python
    from mypy_boto3_amplifybackend.type_defs import BackendAPIAppSyncAuthSettingsTypeDef

    data: BackendAPIAppSyncAuthSettingsTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AdditionalConstraintsElementType,
    AuthenticatedElementType,
    AuthResourcesType,
    DeliveryMethodType,
    MFAModeType,
    MfaTypesElementType,
    ModeType,
    OAuthGrantTypeType,
    OAuthScopesElementType,
    RequiredSignUpAttributesElementType,
    ResolutionStrategyType,
    SignInMethodType,
    StatusType,
    UnAuthenticatedElementType,
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
    "BackendAPIAppSyncAuthSettingsTypeDef",
    "BackendAPIAuthTypeTypeDef",
    "BackendAPIConflictResolutionTypeDef",
    "BackendAPIResourceConfigTypeDef",
    "BackendAuthAppleProviderConfigTypeDef",
    "BackendAuthSocialProviderConfigTypeDef",
    "BackendJobRespObjTypeDef",
    "BackendStoragePermissionsTypeDef",
    "CloneBackendRequestRequestTypeDef",
    "CloneBackendResponseTypeDef",
    "CreateBackendAPIRequestRequestTypeDef",
    "CreateBackendAPIResponseTypeDef",
    "CreateBackendAuthForgotPasswordConfigTypeDef",
    "CreateBackendAuthIdentityPoolConfigTypeDef",
    "CreateBackendAuthMFAConfigTypeDef",
    "CreateBackendAuthOAuthConfigTypeDef",
    "CreateBackendAuthPasswordPolicyConfigTypeDef",
    "CreateBackendAuthRequestRequestTypeDef",
    "CreateBackendAuthResourceConfigTypeDef",
    "CreateBackendAuthResponseTypeDef",
    "CreateBackendAuthUserPoolConfigTypeDef",
    "CreateBackendAuthVerificationMessageConfigTypeDef",
    "CreateBackendConfigRequestRequestTypeDef",
    "CreateBackendConfigResponseTypeDef",
    "CreateBackendRequestRequestTypeDef",
    "CreateBackendResponseTypeDef",
    "CreateBackendStorageRequestRequestTypeDef",
    "CreateBackendStorageResourceConfigTypeDef",
    "CreateBackendStorageResponseTypeDef",
    "CreateTokenRequestRequestTypeDef",
    "CreateTokenResponseTypeDef",
    "DeleteBackendAPIRequestRequestTypeDef",
    "DeleteBackendAPIResponseTypeDef",
    "DeleteBackendAuthRequestRequestTypeDef",
    "DeleteBackendAuthResponseTypeDef",
    "DeleteBackendRequestRequestTypeDef",
    "DeleteBackendResponseTypeDef",
    "DeleteBackendStorageRequestRequestTypeDef",
    "DeleteBackendStorageResponseTypeDef",
    "DeleteTokenRequestRequestTypeDef",
    "DeleteTokenResponseTypeDef",
    "EmailSettingsTypeDef",
    "GenerateBackendAPIModelsRequestRequestTypeDef",
    "GenerateBackendAPIModelsResponseTypeDef",
    "GetBackendAPIModelsRequestRequestTypeDef",
    "GetBackendAPIModelsResponseTypeDef",
    "GetBackendAPIRequestRequestTypeDef",
    "GetBackendAPIResponseTypeDef",
    "GetBackendAuthRequestRequestTypeDef",
    "GetBackendAuthResponseTypeDef",
    "GetBackendJobRequestRequestTypeDef",
    "GetBackendJobResponseTypeDef",
    "GetBackendRequestRequestTypeDef",
    "GetBackendResponseTypeDef",
    "GetBackendStorageRequestRequestTypeDef",
    "GetBackendStorageResourceConfigTypeDef",
    "GetBackendStorageResponseTypeDef",
    "GetTokenRequestRequestTypeDef",
    "GetTokenResponseTypeDef",
    "ImportBackendAuthRequestRequestTypeDef",
    "ImportBackendAuthResponseTypeDef",
    "ImportBackendStorageRequestRequestTypeDef",
    "ImportBackendStorageResponseTypeDef",
    "ListBackendJobsRequestRequestTypeDef",
    "ListBackendJobsResponseTypeDef",
    "ListS3BucketsRequestRequestTypeDef",
    "ListS3BucketsResponseTypeDef",
    "LoginAuthConfigReqObjTypeDef",
    "PaginatorConfigTypeDef",
    "RemoveAllBackendsRequestRequestTypeDef",
    "RemoveAllBackendsResponseTypeDef",
    "RemoveBackendConfigRequestRequestTypeDef",
    "RemoveBackendConfigResponseTypeDef",
    "ResponseMetadataTypeDef",
    "S3BucketInfoTypeDef",
    "SettingsTypeDef",
    "SmsSettingsTypeDef",
    "SocialProviderSettingsTypeDef",
    "UpdateBackendAPIRequestRequestTypeDef",
    "UpdateBackendAPIResponseTypeDef",
    "UpdateBackendAuthForgotPasswordConfigTypeDef",
    "UpdateBackendAuthIdentityPoolConfigTypeDef",
    "UpdateBackendAuthMFAConfigTypeDef",
    "UpdateBackendAuthOAuthConfigTypeDef",
    "UpdateBackendAuthPasswordPolicyConfigTypeDef",
    "UpdateBackendAuthRequestRequestTypeDef",
    "UpdateBackendAuthResourceConfigTypeDef",
    "UpdateBackendAuthResponseTypeDef",
    "UpdateBackendAuthUserPoolConfigTypeDef",
    "UpdateBackendAuthVerificationMessageConfigTypeDef",
    "UpdateBackendConfigRequestRequestTypeDef",
    "UpdateBackendConfigResponseTypeDef",
    "UpdateBackendJobRequestRequestTypeDef",
    "UpdateBackendJobResponseTypeDef",
    "UpdateBackendStorageRequestRequestTypeDef",
    "UpdateBackendStorageResourceConfigTypeDef",
    "UpdateBackendStorageResponseTypeDef",
)

BackendAPIAppSyncAuthSettingsTypeDef = TypedDict(
    "BackendAPIAppSyncAuthSettingsTypeDef",
    {
        "CognitoUserPoolId": NotRequired[str],
        "Description": NotRequired[str],
        "ExpirationTime": NotRequired[float],
        "OpenIDAuthTTL": NotRequired[str],
        "OpenIDClientId": NotRequired[str],
        "OpenIDIatTTL": NotRequired[str],
        "OpenIDIssueURL": NotRequired[str],
        "OpenIDProviderName": NotRequired[str],
    },
)

BackendAPIAuthTypeTypeDef = TypedDict(
    "BackendAPIAuthTypeTypeDef",
    {
        "Mode": NotRequired[ModeType],
        "Settings": NotRequired["BackendAPIAppSyncAuthSettingsTypeDef"],
    },
)

BackendAPIConflictResolutionTypeDef = TypedDict(
    "BackendAPIConflictResolutionTypeDef",
    {
        "ResolutionStrategy": NotRequired[ResolutionStrategyType],
    },
)

BackendAPIResourceConfigTypeDef = TypedDict(
    "BackendAPIResourceConfigTypeDef",
    {
        "AdditionalAuthTypes": NotRequired[Sequence["BackendAPIAuthTypeTypeDef"]],
        "ApiName": NotRequired[str],
        "ConflictResolution": NotRequired["BackendAPIConflictResolutionTypeDef"],
        "DefaultAuthType": NotRequired["BackendAPIAuthTypeTypeDef"],
        "Service": NotRequired[str],
        "TransformSchema": NotRequired[str],
    },
)

BackendAuthAppleProviderConfigTypeDef = TypedDict(
    "BackendAuthAppleProviderConfigTypeDef",
    {
        "ClientId": NotRequired[str],
        "KeyId": NotRequired[str],
        "PrivateKey": NotRequired[str],
        "TeamId": NotRequired[str],
    },
)

BackendAuthSocialProviderConfigTypeDef = TypedDict(
    "BackendAuthSocialProviderConfigTypeDef",
    {
        "ClientId": NotRequired[str],
        "ClientSecret": NotRequired[str],
    },
)

BackendJobRespObjTypeDef = TypedDict(
    "BackendJobRespObjTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "CreateTime": NotRequired[str],
        "Error": NotRequired[str],
        "JobId": NotRequired[str],
        "Operation": NotRequired[str],
        "Status": NotRequired[str],
        "UpdateTime": NotRequired[str],
    },
)

BackendStoragePermissionsTypeDef = TypedDict(
    "BackendStoragePermissionsTypeDef",
    {
        "Authenticated": Sequence[AuthenticatedElementType],
        "UnAuthenticated": NotRequired[Sequence[UnAuthenticatedElementType]],
    },
)

CloneBackendRequestRequestTypeDef = TypedDict(
    "CloneBackendRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "TargetEnvironmentName": str,
    },
)

CloneBackendResponseTypeDef = TypedDict(
    "CloneBackendResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBackendAPIRequestRequestTypeDef = TypedDict(
    "CreateBackendAPIRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceConfig": "BackendAPIResourceConfigTypeDef",
        "ResourceName": str,
    },
)

CreateBackendAPIResponseTypeDef = TypedDict(
    "CreateBackendAPIResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBackendAuthForgotPasswordConfigTypeDef = TypedDict(
    "CreateBackendAuthForgotPasswordConfigTypeDef",
    {
        "DeliveryMethod": DeliveryMethodType,
        "EmailSettings": NotRequired["EmailSettingsTypeDef"],
        "SmsSettings": NotRequired["SmsSettingsTypeDef"],
    },
)

CreateBackendAuthIdentityPoolConfigTypeDef = TypedDict(
    "CreateBackendAuthIdentityPoolConfigTypeDef",
    {
        "IdentityPoolName": str,
        "UnauthenticatedLogin": bool,
    },
)

CreateBackendAuthMFAConfigTypeDef = TypedDict(
    "CreateBackendAuthMFAConfigTypeDef",
    {
        "MFAMode": MFAModeType,
        "Settings": NotRequired["SettingsTypeDef"],
    },
)

CreateBackendAuthOAuthConfigTypeDef = TypedDict(
    "CreateBackendAuthOAuthConfigTypeDef",
    {
        "OAuthGrantType": OAuthGrantTypeType,
        "OAuthScopes": Sequence[OAuthScopesElementType],
        "RedirectSignInURIs": Sequence[str],
        "RedirectSignOutURIs": Sequence[str],
        "DomainPrefix": NotRequired[str],
        "SocialProviderSettings": NotRequired["SocialProviderSettingsTypeDef"],
    },
)

CreateBackendAuthPasswordPolicyConfigTypeDef = TypedDict(
    "CreateBackendAuthPasswordPolicyConfigTypeDef",
    {
        "MinimumLength": float,
        "AdditionalConstraints": NotRequired[Sequence[AdditionalConstraintsElementType]],
    },
)

CreateBackendAuthRequestRequestTypeDef = TypedDict(
    "CreateBackendAuthRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceConfig": "CreateBackendAuthResourceConfigTypeDef",
        "ResourceName": str,
    },
)

CreateBackendAuthResourceConfigTypeDef = TypedDict(
    "CreateBackendAuthResourceConfigTypeDef",
    {
        "AuthResources": AuthResourcesType,
        "Service": Literal["COGNITO"],
        "UserPoolConfigs": "CreateBackendAuthUserPoolConfigTypeDef",
        "IdentityPoolConfigs": NotRequired["CreateBackendAuthIdentityPoolConfigTypeDef"],
    },
)

CreateBackendAuthResponseTypeDef = TypedDict(
    "CreateBackendAuthResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBackendAuthUserPoolConfigTypeDef = TypedDict(
    "CreateBackendAuthUserPoolConfigTypeDef",
    {
        "RequiredSignUpAttributes": Sequence[RequiredSignUpAttributesElementType],
        "SignInMethod": SignInMethodType,
        "UserPoolName": str,
        "ForgotPassword": NotRequired["CreateBackendAuthForgotPasswordConfigTypeDef"],
        "Mfa": NotRequired["CreateBackendAuthMFAConfigTypeDef"],
        "OAuth": NotRequired["CreateBackendAuthOAuthConfigTypeDef"],
        "PasswordPolicy": NotRequired["CreateBackendAuthPasswordPolicyConfigTypeDef"],
        "VerificationMessage": NotRequired["CreateBackendAuthVerificationMessageConfigTypeDef"],
    },
)

CreateBackendAuthVerificationMessageConfigTypeDef = TypedDict(
    "CreateBackendAuthVerificationMessageConfigTypeDef",
    {
        "DeliveryMethod": DeliveryMethodType,
        "EmailSettings": NotRequired["EmailSettingsTypeDef"],
        "SmsSettings": NotRequired["SmsSettingsTypeDef"],
    },
)

CreateBackendConfigRequestRequestTypeDef = TypedDict(
    "CreateBackendConfigRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendManagerAppId": NotRequired[str],
    },
)

CreateBackendConfigResponseTypeDef = TypedDict(
    "CreateBackendConfigResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBackendRequestRequestTypeDef = TypedDict(
    "CreateBackendRequestRequestTypeDef",
    {
        "AppId": str,
        "AppName": str,
        "BackendEnvironmentName": str,
        "ResourceConfig": NotRequired[Mapping[str, Any]],
        "ResourceName": NotRequired[str],
    },
)

CreateBackendResponseTypeDef = TypedDict(
    "CreateBackendResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBackendStorageRequestRequestTypeDef = TypedDict(
    "CreateBackendStorageRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceConfig": "CreateBackendStorageResourceConfigTypeDef",
        "ResourceName": str,
    },
)

CreateBackendStorageResourceConfigTypeDef = TypedDict(
    "CreateBackendStorageResourceConfigTypeDef",
    {
        "Permissions": "BackendStoragePermissionsTypeDef",
        "ServiceName": Literal["S3"],
        "BucketName": NotRequired[str],
    },
)

CreateBackendStorageResponseTypeDef = TypedDict(
    "CreateBackendStorageResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTokenRequestRequestTypeDef = TypedDict(
    "CreateTokenRequestRequestTypeDef",
    {
        "AppId": str,
    },
)

CreateTokenResponseTypeDef = TypedDict(
    "CreateTokenResponseTypeDef",
    {
        "AppId": str,
        "ChallengeCode": str,
        "SessionId": str,
        "Ttl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackendAPIRequestRequestTypeDef = TypedDict(
    "DeleteBackendAPIRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
        "ResourceConfig": NotRequired["BackendAPIResourceConfigTypeDef"],
    },
)

DeleteBackendAPIResponseTypeDef = TypedDict(
    "DeleteBackendAPIResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackendAuthRequestRequestTypeDef = TypedDict(
    "DeleteBackendAuthRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)

DeleteBackendAuthResponseTypeDef = TypedDict(
    "DeleteBackendAuthResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackendRequestRequestTypeDef = TypedDict(
    "DeleteBackendRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
    },
)

DeleteBackendResponseTypeDef = TypedDict(
    "DeleteBackendResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackendStorageRequestRequestTypeDef = TypedDict(
    "DeleteBackendStorageRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
        "ServiceName": Literal["S3"],
    },
)

DeleteBackendStorageResponseTypeDef = TypedDict(
    "DeleteBackendStorageResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTokenRequestRequestTypeDef = TypedDict(
    "DeleteTokenRequestRequestTypeDef",
    {
        "AppId": str,
        "SessionId": str,
    },
)

DeleteTokenResponseTypeDef = TypedDict(
    "DeleteTokenResponseTypeDef",
    {
        "IsSuccess": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EmailSettingsTypeDef = TypedDict(
    "EmailSettingsTypeDef",
    {
        "EmailMessage": NotRequired[str],
        "EmailSubject": NotRequired[str],
    },
)

GenerateBackendAPIModelsRequestRequestTypeDef = TypedDict(
    "GenerateBackendAPIModelsRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)

GenerateBackendAPIModelsResponseTypeDef = TypedDict(
    "GenerateBackendAPIModelsResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackendAPIModelsRequestRequestTypeDef = TypedDict(
    "GetBackendAPIModelsRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)

GetBackendAPIModelsResponseTypeDef = TypedDict(
    "GetBackendAPIModelsResponseTypeDef",
    {
        "Models": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackendAPIRequestRequestTypeDef = TypedDict(
    "GetBackendAPIRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
        "ResourceConfig": NotRequired["BackendAPIResourceConfigTypeDef"],
    },
)

GetBackendAPIResponseTypeDef = TypedDict(
    "GetBackendAPIResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "ResourceConfig": "BackendAPIResourceConfigTypeDef",
        "ResourceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackendAuthRequestRequestTypeDef = TypedDict(
    "GetBackendAuthRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)

GetBackendAuthResponseTypeDef = TypedDict(
    "GetBackendAuthResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "ResourceConfig": "CreateBackendAuthResourceConfigTypeDef",
        "ResourceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackendJobRequestRequestTypeDef = TypedDict(
    "GetBackendJobRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": str,
    },
)

GetBackendJobResponseTypeDef = TypedDict(
    "GetBackendJobResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "CreateTime": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "UpdateTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackendRequestRequestTypeDef = TypedDict(
    "GetBackendRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": NotRequired[str],
    },
)

GetBackendResponseTypeDef = TypedDict(
    "GetBackendResponseTypeDef",
    {
        "AmplifyFeatureFlags": str,
        "AmplifyMetaConfig": str,
        "AppId": str,
        "AppName": str,
        "BackendEnvironmentList": List[str],
        "BackendEnvironmentName": str,
        "Error": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackendStorageRequestRequestTypeDef = TypedDict(
    "GetBackendStorageRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)

GetBackendStorageResourceConfigTypeDef = TypedDict(
    "GetBackendStorageResourceConfigTypeDef",
    {
        "Imported": bool,
        "ServiceName": Literal["S3"],
        "BucketName": NotRequired[str],
        "Permissions": NotRequired["BackendStoragePermissionsTypeDef"],
    },
)

GetBackendStorageResponseTypeDef = TypedDict(
    "GetBackendStorageResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceConfig": "GetBackendStorageResourceConfigTypeDef",
        "ResourceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTokenRequestRequestTypeDef = TypedDict(
    "GetTokenRequestRequestTypeDef",
    {
        "AppId": str,
        "SessionId": str,
    },
)

GetTokenResponseTypeDef = TypedDict(
    "GetTokenResponseTypeDef",
    {
        "AppId": str,
        "ChallengeCode": str,
        "SessionId": str,
        "Ttl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportBackendAuthRequestRequestTypeDef = TypedDict(
    "ImportBackendAuthRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "NativeClientId": str,
        "UserPoolId": str,
        "WebClientId": str,
        "IdentityPoolId": NotRequired[str],
    },
)

ImportBackendAuthResponseTypeDef = TypedDict(
    "ImportBackendAuthResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportBackendStorageRequestRequestTypeDef = TypedDict(
    "ImportBackendStorageRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ServiceName": Literal["S3"],
        "BucketName": NotRequired[str],
    },
)

ImportBackendStorageResponseTypeDef = TypedDict(
    "ImportBackendStorageResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBackendJobsRequestRequestTypeDef = TypedDict(
    "ListBackendJobsRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Operation": NotRequired[str],
        "Status": NotRequired[str],
    },
)

ListBackendJobsResponseTypeDef = TypedDict(
    "ListBackendJobsResponseTypeDef",
    {
        "Jobs": List["BackendJobRespObjTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListS3BucketsRequestRequestTypeDef = TypedDict(
    "ListS3BucketsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)

ListS3BucketsResponseTypeDef = TypedDict(
    "ListS3BucketsResponseTypeDef",
    {
        "Buckets": List["S3BucketInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoginAuthConfigReqObjTypeDef = TypedDict(
    "LoginAuthConfigReqObjTypeDef",
    {
        "AwsCognitoIdentityPoolId": NotRequired[str],
        "AwsCognitoRegion": NotRequired[str],
        "AwsUserPoolsId": NotRequired[str],
        "AwsUserPoolsWebClientId": NotRequired[str],
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

RemoveAllBackendsRequestRequestTypeDef = TypedDict(
    "RemoveAllBackendsRequestRequestTypeDef",
    {
        "AppId": str,
        "CleanAmplifyApp": NotRequired[bool],
    },
)

RemoveAllBackendsResponseTypeDef = TypedDict(
    "RemoveAllBackendsResponseTypeDef",
    {
        "AppId": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveBackendConfigRequestRequestTypeDef = TypedDict(
    "RemoveBackendConfigRequestRequestTypeDef",
    {
        "AppId": str,
    },
)

RemoveBackendConfigResponseTypeDef = TypedDict(
    "RemoveBackendConfigResponseTypeDef",
    {
        "Error": str,
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

S3BucketInfoTypeDef = TypedDict(
    "S3BucketInfoTypeDef",
    {
        "CreationDate": NotRequired[str],
        "Name": NotRequired[str],
    },
)

SettingsTypeDef = TypedDict(
    "SettingsTypeDef",
    {
        "MfaTypes": NotRequired[Sequence[MfaTypesElementType]],
        "SmsMessage": NotRequired[str],
    },
)

SmsSettingsTypeDef = TypedDict(
    "SmsSettingsTypeDef",
    {
        "SmsMessage": NotRequired[str],
    },
)

SocialProviderSettingsTypeDef = TypedDict(
    "SocialProviderSettingsTypeDef",
    {
        "Facebook": NotRequired["BackendAuthSocialProviderConfigTypeDef"],
        "Google": NotRequired["BackendAuthSocialProviderConfigTypeDef"],
        "LoginWithAmazon": NotRequired["BackendAuthSocialProviderConfigTypeDef"],
        "SignInWithApple": NotRequired["BackendAuthAppleProviderConfigTypeDef"],
    },
)

UpdateBackendAPIRequestRequestTypeDef = TypedDict(
    "UpdateBackendAPIRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
        "ResourceConfig": NotRequired["BackendAPIResourceConfigTypeDef"],
    },
)

UpdateBackendAPIResponseTypeDef = TypedDict(
    "UpdateBackendAPIResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBackendAuthForgotPasswordConfigTypeDef = TypedDict(
    "UpdateBackendAuthForgotPasswordConfigTypeDef",
    {
        "DeliveryMethod": NotRequired[DeliveryMethodType],
        "EmailSettings": NotRequired["EmailSettingsTypeDef"],
        "SmsSettings": NotRequired["SmsSettingsTypeDef"],
    },
)

UpdateBackendAuthIdentityPoolConfigTypeDef = TypedDict(
    "UpdateBackendAuthIdentityPoolConfigTypeDef",
    {
        "UnauthenticatedLogin": NotRequired[bool],
    },
)

UpdateBackendAuthMFAConfigTypeDef = TypedDict(
    "UpdateBackendAuthMFAConfigTypeDef",
    {
        "MFAMode": NotRequired[MFAModeType],
        "Settings": NotRequired["SettingsTypeDef"],
    },
)

UpdateBackendAuthOAuthConfigTypeDef = TypedDict(
    "UpdateBackendAuthOAuthConfigTypeDef",
    {
        "DomainPrefix": NotRequired[str],
        "OAuthGrantType": NotRequired[OAuthGrantTypeType],
        "OAuthScopes": NotRequired[Sequence[OAuthScopesElementType]],
        "RedirectSignInURIs": NotRequired[Sequence[str]],
        "RedirectSignOutURIs": NotRequired[Sequence[str]],
        "SocialProviderSettings": NotRequired["SocialProviderSettingsTypeDef"],
    },
)

UpdateBackendAuthPasswordPolicyConfigTypeDef = TypedDict(
    "UpdateBackendAuthPasswordPolicyConfigTypeDef",
    {
        "AdditionalConstraints": NotRequired[Sequence[AdditionalConstraintsElementType]],
        "MinimumLength": NotRequired[float],
    },
)

UpdateBackendAuthRequestRequestTypeDef = TypedDict(
    "UpdateBackendAuthRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceConfig": "UpdateBackendAuthResourceConfigTypeDef",
        "ResourceName": str,
    },
)

UpdateBackendAuthResourceConfigTypeDef = TypedDict(
    "UpdateBackendAuthResourceConfigTypeDef",
    {
        "AuthResources": AuthResourcesType,
        "Service": Literal["COGNITO"],
        "UserPoolConfigs": "UpdateBackendAuthUserPoolConfigTypeDef",
        "IdentityPoolConfigs": NotRequired["UpdateBackendAuthIdentityPoolConfigTypeDef"],
    },
)

UpdateBackendAuthResponseTypeDef = TypedDict(
    "UpdateBackendAuthResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBackendAuthUserPoolConfigTypeDef = TypedDict(
    "UpdateBackendAuthUserPoolConfigTypeDef",
    {
        "ForgotPassword": NotRequired["UpdateBackendAuthForgotPasswordConfigTypeDef"],
        "Mfa": NotRequired["UpdateBackendAuthMFAConfigTypeDef"],
        "OAuth": NotRequired["UpdateBackendAuthOAuthConfigTypeDef"],
        "PasswordPolicy": NotRequired["UpdateBackendAuthPasswordPolicyConfigTypeDef"],
        "VerificationMessage": NotRequired["UpdateBackendAuthVerificationMessageConfigTypeDef"],
    },
)

UpdateBackendAuthVerificationMessageConfigTypeDef = TypedDict(
    "UpdateBackendAuthVerificationMessageConfigTypeDef",
    {
        "DeliveryMethod": DeliveryMethodType,
        "EmailSettings": NotRequired["EmailSettingsTypeDef"],
        "SmsSettings": NotRequired["SmsSettingsTypeDef"],
    },
)

UpdateBackendConfigRequestRequestTypeDef = TypedDict(
    "UpdateBackendConfigRequestRequestTypeDef",
    {
        "AppId": str,
        "LoginAuthConfig": NotRequired["LoginAuthConfigReqObjTypeDef"],
    },
)

UpdateBackendConfigResponseTypeDef = TypedDict(
    "UpdateBackendConfigResponseTypeDef",
    {
        "AppId": str,
        "BackendManagerAppId": str,
        "Error": str,
        "LoginAuthConfig": "LoginAuthConfigReqObjTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBackendJobRequestRequestTypeDef = TypedDict(
    "UpdateBackendJobRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": str,
        "Operation": NotRequired[str],
        "Status": NotRequired[str],
    },
)

UpdateBackendJobResponseTypeDef = TypedDict(
    "UpdateBackendJobResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "CreateTime": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "UpdateTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBackendStorageRequestRequestTypeDef = TypedDict(
    "UpdateBackendStorageRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceConfig": "UpdateBackendStorageResourceConfigTypeDef",
        "ResourceName": str,
    },
)

UpdateBackendStorageResourceConfigTypeDef = TypedDict(
    "UpdateBackendStorageResourceConfigTypeDef",
    {
        "Permissions": "BackendStoragePermissionsTypeDef",
        "ServiceName": Literal["S3"],
    },
)

UpdateBackendStorageResponseTypeDef = TypedDict(
    "UpdateBackendStorageResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
