"""
Type annotations for cognito-idp service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_cognito_idp/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_cognito_idp.type_defs import AccountRecoverySettingTypeTypeDef

    data: AccountRecoverySettingTypeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    AccountTakeoverEventActionTypeType,
    AdvancedSecurityModeTypeType,
    AliasAttributeTypeType,
    AttributeDataTypeType,
    AuthFlowTypeType,
    ChallengeNameType,
    ChallengeNameTypeType,
    ChallengeResponseType,
    CompromisedCredentialsEventActionTypeType,
    DefaultEmailOptionTypeType,
    DeliveryMediumTypeType,
    DeviceRememberedStatusTypeType,
    DomainStatusTypeType,
    EmailSendingAccountTypeType,
    EventFilterTypeType,
    EventResponseTypeType,
    EventTypeType,
    ExplicitAuthFlowsTypeType,
    FeedbackValueTypeType,
    IdentityProviderTypeTypeType,
    MessageActionTypeType,
    OAuthFlowTypeType,
    PreventUserExistenceErrorTypesType,
    RecoveryOptionNameTypeType,
    RiskDecisionTypeType,
    RiskLevelTypeType,
    StatusTypeType,
    TimeUnitsTypeType,
    UserImportJobStatusTypeType,
    UsernameAttributeTypeType,
    UserPoolMfaTypeType,
    UserStatusTypeType,
    VerifiedAttributeTypeType,
    VerifySoftwareTokenResponseTypeType,
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
    "AccountRecoverySettingTypeTypeDef",
    "AccountTakeoverActionTypeTypeDef",
    "AccountTakeoverActionsTypeTypeDef",
    "AccountTakeoverRiskConfigurationTypeTypeDef",
    "AddCustomAttributesRequestRequestTypeDef",
    "AdminAddUserToGroupRequestRequestTypeDef",
    "AdminConfirmSignUpRequestRequestTypeDef",
    "AdminCreateUserConfigTypeTypeDef",
    "AdminCreateUserRequestRequestTypeDef",
    "AdminCreateUserResponseTypeDef",
    "AdminDeleteUserAttributesRequestRequestTypeDef",
    "AdminDeleteUserRequestRequestTypeDef",
    "AdminDisableProviderForUserRequestRequestTypeDef",
    "AdminDisableUserRequestRequestTypeDef",
    "AdminEnableUserRequestRequestTypeDef",
    "AdminForgetDeviceRequestRequestTypeDef",
    "AdminGetDeviceRequestRequestTypeDef",
    "AdminGetDeviceResponseTypeDef",
    "AdminGetUserRequestRequestTypeDef",
    "AdminGetUserResponseTypeDef",
    "AdminInitiateAuthRequestRequestTypeDef",
    "AdminInitiateAuthResponseTypeDef",
    "AdminLinkProviderForUserRequestRequestTypeDef",
    "AdminListDevicesRequestRequestTypeDef",
    "AdminListDevicesResponseTypeDef",
    "AdminListGroupsForUserRequestRequestTypeDef",
    "AdminListGroupsForUserResponseTypeDef",
    "AdminListUserAuthEventsRequestRequestTypeDef",
    "AdminListUserAuthEventsResponseTypeDef",
    "AdminRemoveUserFromGroupRequestRequestTypeDef",
    "AdminResetUserPasswordRequestRequestTypeDef",
    "AdminRespondToAuthChallengeRequestRequestTypeDef",
    "AdminRespondToAuthChallengeResponseTypeDef",
    "AdminSetUserMFAPreferenceRequestRequestTypeDef",
    "AdminSetUserPasswordRequestRequestTypeDef",
    "AdminSetUserSettingsRequestRequestTypeDef",
    "AdminUpdateAuthEventFeedbackRequestRequestTypeDef",
    "AdminUpdateDeviceStatusRequestRequestTypeDef",
    "AdminUpdateUserAttributesRequestRequestTypeDef",
    "AdminUserGlobalSignOutRequestRequestTypeDef",
    "AnalyticsConfigurationTypeTypeDef",
    "AnalyticsMetadataTypeTypeDef",
    "AssociateSoftwareTokenRequestRequestTypeDef",
    "AssociateSoftwareTokenResponseTypeDef",
    "AttributeTypeTypeDef",
    "AuthEventTypeTypeDef",
    "AuthenticationResultTypeTypeDef",
    "ChallengeResponseTypeTypeDef",
    "ChangePasswordRequestRequestTypeDef",
    "CodeDeliveryDetailsTypeTypeDef",
    "CompromisedCredentialsActionsTypeTypeDef",
    "CompromisedCredentialsRiskConfigurationTypeTypeDef",
    "ConfirmDeviceRequestRequestTypeDef",
    "ConfirmDeviceResponseTypeDef",
    "ConfirmForgotPasswordRequestRequestTypeDef",
    "ConfirmSignUpRequestRequestTypeDef",
    "ContextDataTypeTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateIdentityProviderRequestRequestTypeDef",
    "CreateIdentityProviderResponseTypeDef",
    "CreateResourceServerRequestRequestTypeDef",
    "CreateResourceServerResponseTypeDef",
    "CreateUserImportJobRequestRequestTypeDef",
    "CreateUserImportJobResponseTypeDef",
    "CreateUserPoolClientRequestRequestTypeDef",
    "CreateUserPoolClientResponseTypeDef",
    "CreateUserPoolDomainRequestRequestTypeDef",
    "CreateUserPoolDomainResponseTypeDef",
    "CreateUserPoolRequestRequestTypeDef",
    "CreateUserPoolResponseTypeDef",
    "CustomDomainConfigTypeTypeDef",
    "CustomEmailLambdaVersionConfigTypeTypeDef",
    "CustomSMSLambdaVersionConfigTypeTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteIdentityProviderRequestRequestTypeDef",
    "DeleteResourceServerRequestRequestTypeDef",
    "DeleteUserAttributesRequestRequestTypeDef",
    "DeleteUserPoolClientRequestRequestTypeDef",
    "DeleteUserPoolDomainRequestRequestTypeDef",
    "DeleteUserPoolRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DescribeIdentityProviderRequestRequestTypeDef",
    "DescribeIdentityProviderResponseTypeDef",
    "DescribeResourceServerRequestRequestTypeDef",
    "DescribeResourceServerResponseTypeDef",
    "DescribeRiskConfigurationRequestRequestTypeDef",
    "DescribeRiskConfigurationResponseTypeDef",
    "DescribeUserImportJobRequestRequestTypeDef",
    "DescribeUserImportJobResponseTypeDef",
    "DescribeUserPoolClientRequestRequestTypeDef",
    "DescribeUserPoolClientResponseTypeDef",
    "DescribeUserPoolDomainRequestRequestTypeDef",
    "DescribeUserPoolDomainResponseTypeDef",
    "DescribeUserPoolRequestRequestTypeDef",
    "DescribeUserPoolResponseTypeDef",
    "DeviceConfigurationTypeTypeDef",
    "DeviceSecretVerifierConfigTypeTypeDef",
    "DeviceTypeTypeDef",
    "DomainDescriptionTypeTypeDef",
    "EmailConfigurationTypeTypeDef",
    "EventContextDataTypeTypeDef",
    "EventFeedbackTypeTypeDef",
    "EventRiskTypeTypeDef",
    "ForgetDeviceRequestRequestTypeDef",
    "ForgotPasswordRequestRequestTypeDef",
    "ForgotPasswordResponseTypeDef",
    "GetCSVHeaderRequestRequestTypeDef",
    "GetCSVHeaderResponseTypeDef",
    "GetDeviceRequestRequestTypeDef",
    "GetDeviceResponseTypeDef",
    "GetGroupRequestRequestTypeDef",
    "GetGroupResponseTypeDef",
    "GetIdentityProviderByIdentifierRequestRequestTypeDef",
    "GetIdentityProviderByIdentifierResponseTypeDef",
    "GetSigningCertificateRequestRequestTypeDef",
    "GetSigningCertificateResponseTypeDef",
    "GetUICustomizationRequestRequestTypeDef",
    "GetUICustomizationResponseTypeDef",
    "GetUserAttributeVerificationCodeRequestRequestTypeDef",
    "GetUserAttributeVerificationCodeResponseTypeDef",
    "GetUserPoolMfaConfigRequestRequestTypeDef",
    "GetUserPoolMfaConfigResponseTypeDef",
    "GetUserRequestRequestTypeDef",
    "GetUserResponseTypeDef",
    "GlobalSignOutRequestRequestTypeDef",
    "GroupTypeTypeDef",
    "HttpHeaderTypeDef",
    "IdentityProviderTypeTypeDef",
    "InitiateAuthRequestRequestTypeDef",
    "InitiateAuthResponseTypeDef",
    "LambdaConfigTypeTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "ListDevicesResponseTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListGroupsResponseTypeDef",
    "ListIdentityProvidersRequestRequestTypeDef",
    "ListIdentityProvidersResponseTypeDef",
    "ListResourceServersRequestRequestTypeDef",
    "ListResourceServersResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUserImportJobsRequestRequestTypeDef",
    "ListUserImportJobsResponseTypeDef",
    "ListUserPoolClientsRequestRequestTypeDef",
    "ListUserPoolClientsResponseTypeDef",
    "ListUserPoolsRequestRequestTypeDef",
    "ListUserPoolsResponseTypeDef",
    "ListUsersInGroupRequestRequestTypeDef",
    "ListUsersInGroupResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "MFAOptionTypeTypeDef",
    "MessageTemplateTypeTypeDef",
    "NewDeviceMetadataTypeTypeDef",
    "NotifyConfigurationTypeTypeDef",
    "NotifyEmailTypeTypeDef",
    "NumberAttributeConstraintsTypeTypeDef",
    "PaginatorConfigTypeDef",
    "PasswordPolicyTypeTypeDef",
    "ProviderDescriptionTypeDef",
    "ProviderUserIdentifierTypeTypeDef",
    "RecoveryOptionTypeTypeDef",
    "ResendConfirmationCodeRequestRequestTypeDef",
    "ResendConfirmationCodeResponseTypeDef",
    "ResourceServerScopeTypeTypeDef",
    "ResourceServerTypeTypeDef",
    "RespondToAuthChallengeRequestRequestTypeDef",
    "RespondToAuthChallengeResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeTokenRequestRequestTypeDef",
    "RiskConfigurationTypeTypeDef",
    "RiskExceptionConfigurationTypeTypeDef",
    "SMSMfaSettingsTypeTypeDef",
    "SchemaAttributeTypeTypeDef",
    "SetRiskConfigurationRequestRequestTypeDef",
    "SetRiskConfigurationResponseTypeDef",
    "SetUICustomizationRequestRequestTypeDef",
    "SetUICustomizationResponseTypeDef",
    "SetUserMFAPreferenceRequestRequestTypeDef",
    "SetUserPoolMfaConfigRequestRequestTypeDef",
    "SetUserPoolMfaConfigResponseTypeDef",
    "SetUserSettingsRequestRequestTypeDef",
    "SignUpRequestRequestTypeDef",
    "SignUpResponseTypeDef",
    "SmsConfigurationTypeTypeDef",
    "SmsMfaConfigTypeTypeDef",
    "SoftwareTokenMfaConfigTypeTypeDef",
    "SoftwareTokenMfaSettingsTypeTypeDef",
    "StartUserImportJobRequestRequestTypeDef",
    "StartUserImportJobResponseTypeDef",
    "StopUserImportJobRequestRequestTypeDef",
    "StopUserImportJobResponseTypeDef",
    "StringAttributeConstraintsTypeTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TokenValidityUnitsTypeTypeDef",
    "UICustomizationTypeTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAuthEventFeedbackRequestRequestTypeDef",
    "UpdateDeviceStatusRequestRequestTypeDef",
    "UpdateGroupRequestRequestTypeDef",
    "UpdateGroupResponseTypeDef",
    "UpdateIdentityProviderRequestRequestTypeDef",
    "UpdateIdentityProviderResponseTypeDef",
    "UpdateResourceServerRequestRequestTypeDef",
    "UpdateResourceServerResponseTypeDef",
    "UpdateUserAttributesRequestRequestTypeDef",
    "UpdateUserAttributesResponseTypeDef",
    "UpdateUserPoolClientRequestRequestTypeDef",
    "UpdateUserPoolClientResponseTypeDef",
    "UpdateUserPoolDomainRequestRequestTypeDef",
    "UpdateUserPoolDomainResponseTypeDef",
    "UpdateUserPoolRequestRequestTypeDef",
    "UserContextDataTypeTypeDef",
    "UserImportJobTypeTypeDef",
    "UserPoolAddOnsTypeTypeDef",
    "UserPoolClientDescriptionTypeDef",
    "UserPoolClientTypeTypeDef",
    "UserPoolDescriptionTypeTypeDef",
    "UserPoolPolicyTypeTypeDef",
    "UserPoolTypeTypeDef",
    "UserTypeTypeDef",
    "UsernameConfigurationTypeTypeDef",
    "VerificationMessageTemplateTypeTypeDef",
    "VerifySoftwareTokenRequestRequestTypeDef",
    "VerifySoftwareTokenResponseTypeDef",
    "VerifyUserAttributeRequestRequestTypeDef",
)

AccountRecoverySettingTypeTypeDef = TypedDict(
    "AccountRecoverySettingTypeTypeDef",
    {
        "RecoveryMechanisms": NotRequired[Sequence["RecoveryOptionTypeTypeDef"]],
    },
)

AccountTakeoverActionTypeTypeDef = TypedDict(
    "AccountTakeoverActionTypeTypeDef",
    {
        "Notify": bool,
        "EventAction": AccountTakeoverEventActionTypeType,
    },
)

AccountTakeoverActionsTypeTypeDef = TypedDict(
    "AccountTakeoverActionsTypeTypeDef",
    {
        "LowAction": NotRequired["AccountTakeoverActionTypeTypeDef"],
        "MediumAction": NotRequired["AccountTakeoverActionTypeTypeDef"],
        "HighAction": NotRequired["AccountTakeoverActionTypeTypeDef"],
    },
)

AccountTakeoverRiskConfigurationTypeTypeDef = TypedDict(
    "AccountTakeoverRiskConfigurationTypeTypeDef",
    {
        "Actions": "AccountTakeoverActionsTypeTypeDef",
        "NotifyConfiguration": NotRequired["NotifyConfigurationTypeTypeDef"],
    },
)

AddCustomAttributesRequestRequestTypeDef = TypedDict(
    "AddCustomAttributesRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "CustomAttributes": Sequence["SchemaAttributeTypeTypeDef"],
    },
)

AdminAddUserToGroupRequestRequestTypeDef = TypedDict(
    "AdminAddUserToGroupRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "GroupName": str,
    },
)

AdminConfirmSignUpRequestRequestTypeDef = TypedDict(
    "AdminConfirmSignUpRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)

AdminCreateUserConfigTypeTypeDef = TypedDict(
    "AdminCreateUserConfigTypeTypeDef",
    {
        "AllowAdminCreateUserOnly": NotRequired[bool],
        "UnusedAccountValidityDays": NotRequired[int],
        "InviteMessageTemplate": NotRequired["MessageTemplateTypeTypeDef"],
    },
)

AdminCreateUserRequestRequestTypeDef = TypedDict(
    "AdminCreateUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "UserAttributes": NotRequired[Sequence["AttributeTypeTypeDef"]],
        "ValidationData": NotRequired[Sequence["AttributeTypeTypeDef"]],
        "TemporaryPassword": NotRequired[str],
        "ForceAliasCreation": NotRequired[bool],
        "MessageAction": NotRequired[MessageActionTypeType],
        "DesiredDeliveryMediums": NotRequired[Sequence[DeliveryMediumTypeType]],
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)

AdminCreateUserResponseTypeDef = TypedDict(
    "AdminCreateUserResponseTypeDef",
    {
        "User": "UserTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdminDeleteUserAttributesRequestRequestTypeDef = TypedDict(
    "AdminDeleteUserAttributesRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "UserAttributeNames": Sequence[str],
    },
)

AdminDeleteUserRequestRequestTypeDef = TypedDict(
    "AdminDeleteUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)

AdminDisableProviderForUserRequestRequestTypeDef = TypedDict(
    "AdminDisableProviderForUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "User": "ProviderUserIdentifierTypeTypeDef",
    },
)

AdminDisableUserRequestRequestTypeDef = TypedDict(
    "AdminDisableUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)

AdminEnableUserRequestRequestTypeDef = TypedDict(
    "AdminEnableUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)

AdminForgetDeviceRequestRequestTypeDef = TypedDict(
    "AdminForgetDeviceRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "DeviceKey": str,
    },
)

AdminGetDeviceRequestRequestTypeDef = TypedDict(
    "AdminGetDeviceRequestRequestTypeDef",
    {
        "DeviceKey": str,
        "UserPoolId": str,
        "Username": str,
    },
)

AdminGetDeviceResponseTypeDef = TypedDict(
    "AdminGetDeviceResponseTypeDef",
    {
        "Device": "DeviceTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdminGetUserRequestRequestTypeDef = TypedDict(
    "AdminGetUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)

AdminGetUserResponseTypeDef = TypedDict(
    "AdminGetUserResponseTypeDef",
    {
        "Username": str,
        "UserAttributes": List["AttributeTypeTypeDef"],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": UserStatusTypeType,
        "MFAOptions": List["MFAOptionTypeTypeDef"],
        "PreferredMfaSetting": str,
        "UserMFASettingList": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdminInitiateAuthRequestRequestTypeDef = TypedDict(
    "AdminInitiateAuthRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "AuthFlow": AuthFlowTypeType,
        "AuthParameters": NotRequired[Mapping[str, str]],
        "ClientMetadata": NotRequired[Mapping[str, str]],
        "AnalyticsMetadata": NotRequired["AnalyticsMetadataTypeTypeDef"],
        "ContextData": NotRequired["ContextDataTypeTypeDef"],
    },
)

AdminInitiateAuthResponseTypeDef = TypedDict(
    "AdminInitiateAuthResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": "AuthenticationResultTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdminLinkProviderForUserRequestRequestTypeDef = TypedDict(
    "AdminLinkProviderForUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "DestinationUser": "ProviderUserIdentifierTypeTypeDef",
        "SourceUser": "ProviderUserIdentifierTypeTypeDef",
    },
)

AdminListDevicesRequestRequestTypeDef = TypedDict(
    "AdminListDevicesRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "Limit": NotRequired[int],
        "PaginationToken": NotRequired[str],
    },
)

AdminListDevicesResponseTypeDef = TypedDict(
    "AdminListDevicesResponseTypeDef",
    {
        "Devices": List["DeviceTypeTypeDef"],
        "PaginationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdminListGroupsForUserRequestRequestTypeDef = TypedDict(
    "AdminListGroupsForUserRequestRequestTypeDef",
    {
        "Username": str,
        "UserPoolId": str,
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

AdminListGroupsForUserResponseTypeDef = TypedDict(
    "AdminListGroupsForUserResponseTypeDef",
    {
        "Groups": List["GroupTypeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdminListUserAuthEventsRequestRequestTypeDef = TypedDict(
    "AdminListUserAuthEventsRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

AdminListUserAuthEventsResponseTypeDef = TypedDict(
    "AdminListUserAuthEventsResponseTypeDef",
    {
        "AuthEvents": List["AuthEventTypeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdminRemoveUserFromGroupRequestRequestTypeDef = TypedDict(
    "AdminRemoveUserFromGroupRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "GroupName": str,
    },
)

AdminResetUserPasswordRequestRequestTypeDef = TypedDict(
    "AdminResetUserPasswordRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)

AdminRespondToAuthChallengeRequestRequestTypeDef = TypedDict(
    "AdminRespondToAuthChallengeRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "ChallengeName": ChallengeNameTypeType,
        "ChallengeResponses": NotRequired[Mapping[str, str]],
        "Session": NotRequired[str],
        "AnalyticsMetadata": NotRequired["AnalyticsMetadataTypeTypeDef"],
        "ContextData": NotRequired["ContextDataTypeTypeDef"],
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)

AdminRespondToAuthChallengeResponseTypeDef = TypedDict(
    "AdminRespondToAuthChallengeResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": "AuthenticationResultTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdminSetUserMFAPreferenceRequestRequestTypeDef = TypedDict(
    "AdminSetUserMFAPreferenceRequestRequestTypeDef",
    {
        "Username": str,
        "UserPoolId": str,
        "SMSMfaSettings": NotRequired["SMSMfaSettingsTypeTypeDef"],
        "SoftwareTokenMfaSettings": NotRequired["SoftwareTokenMfaSettingsTypeTypeDef"],
    },
)

AdminSetUserPasswordRequestRequestTypeDef = TypedDict(
    "AdminSetUserPasswordRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "Password": str,
        "Permanent": NotRequired[bool],
    },
)

AdminSetUserSettingsRequestRequestTypeDef = TypedDict(
    "AdminSetUserSettingsRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "MFAOptions": Sequence["MFAOptionTypeTypeDef"],
    },
)

AdminUpdateAuthEventFeedbackRequestRequestTypeDef = TypedDict(
    "AdminUpdateAuthEventFeedbackRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "EventId": str,
        "FeedbackValue": FeedbackValueTypeType,
    },
)

AdminUpdateDeviceStatusRequestRequestTypeDef = TypedDict(
    "AdminUpdateDeviceStatusRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "DeviceKey": str,
        "DeviceRememberedStatus": NotRequired[DeviceRememberedStatusTypeType],
    },
)

AdminUpdateUserAttributesRequestRequestTypeDef = TypedDict(
    "AdminUpdateUserAttributesRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "UserAttributes": Sequence["AttributeTypeTypeDef"],
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)

AdminUserGlobalSignOutRequestRequestTypeDef = TypedDict(
    "AdminUserGlobalSignOutRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)

AnalyticsConfigurationTypeTypeDef = TypedDict(
    "AnalyticsConfigurationTypeTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "ApplicationArn": NotRequired[str],
        "RoleArn": NotRequired[str],
        "ExternalId": NotRequired[str],
        "UserDataShared": NotRequired[bool],
    },
)

AnalyticsMetadataTypeTypeDef = TypedDict(
    "AnalyticsMetadataTypeTypeDef",
    {
        "AnalyticsEndpointId": NotRequired[str],
    },
)

AssociateSoftwareTokenRequestRequestTypeDef = TypedDict(
    "AssociateSoftwareTokenRequestRequestTypeDef",
    {
        "AccessToken": NotRequired[str],
        "Session": NotRequired[str],
    },
)

AssociateSoftwareTokenResponseTypeDef = TypedDict(
    "AssociateSoftwareTokenResponseTypeDef",
    {
        "SecretCode": str,
        "Session": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttributeTypeTypeDef = TypedDict(
    "AttributeTypeTypeDef",
    {
        "Name": str,
        "Value": NotRequired[str],
    },
)

AuthEventTypeTypeDef = TypedDict(
    "AuthEventTypeTypeDef",
    {
        "EventId": NotRequired[str],
        "EventType": NotRequired[EventTypeType],
        "CreationDate": NotRequired[datetime],
        "EventResponse": NotRequired[EventResponseTypeType],
        "EventRisk": NotRequired["EventRiskTypeTypeDef"],
        "ChallengeResponses": NotRequired[List["ChallengeResponseTypeTypeDef"]],
        "EventContextData": NotRequired["EventContextDataTypeTypeDef"],
        "EventFeedback": NotRequired["EventFeedbackTypeTypeDef"],
    },
)

AuthenticationResultTypeTypeDef = TypedDict(
    "AuthenticationResultTypeTypeDef",
    {
        "AccessToken": NotRequired[str],
        "ExpiresIn": NotRequired[int],
        "TokenType": NotRequired[str],
        "RefreshToken": NotRequired[str],
        "IdToken": NotRequired[str],
        "NewDeviceMetadata": NotRequired["NewDeviceMetadataTypeTypeDef"],
    },
)

ChallengeResponseTypeTypeDef = TypedDict(
    "ChallengeResponseTypeTypeDef",
    {
        "ChallengeName": NotRequired[ChallengeNameType],
        "ChallengeResponse": NotRequired[ChallengeResponseType],
    },
)

ChangePasswordRequestRequestTypeDef = TypedDict(
    "ChangePasswordRequestRequestTypeDef",
    {
        "PreviousPassword": str,
        "ProposedPassword": str,
        "AccessToken": str,
    },
)

CodeDeliveryDetailsTypeTypeDef = TypedDict(
    "CodeDeliveryDetailsTypeTypeDef",
    {
        "Destination": NotRequired[str],
        "DeliveryMedium": NotRequired[DeliveryMediumTypeType],
        "AttributeName": NotRequired[str],
    },
)

CompromisedCredentialsActionsTypeTypeDef = TypedDict(
    "CompromisedCredentialsActionsTypeTypeDef",
    {
        "EventAction": CompromisedCredentialsEventActionTypeType,
    },
)

CompromisedCredentialsRiskConfigurationTypeTypeDef = TypedDict(
    "CompromisedCredentialsRiskConfigurationTypeTypeDef",
    {
        "Actions": "CompromisedCredentialsActionsTypeTypeDef",
        "EventFilter": NotRequired[List[EventFilterTypeType]],
    },
)

ConfirmDeviceRequestRequestTypeDef = TypedDict(
    "ConfirmDeviceRequestRequestTypeDef",
    {
        "AccessToken": str,
        "DeviceKey": str,
        "DeviceSecretVerifierConfig": NotRequired["DeviceSecretVerifierConfigTypeTypeDef"],
        "DeviceName": NotRequired[str],
    },
)

ConfirmDeviceResponseTypeDef = TypedDict(
    "ConfirmDeviceResponseTypeDef",
    {
        "UserConfirmationNecessary": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfirmForgotPasswordRequestRequestTypeDef = TypedDict(
    "ConfirmForgotPasswordRequestRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
        "ConfirmationCode": str,
        "Password": str,
        "SecretHash": NotRequired[str],
        "AnalyticsMetadata": NotRequired["AnalyticsMetadataTypeTypeDef"],
        "UserContextData": NotRequired["UserContextDataTypeTypeDef"],
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)

ConfirmSignUpRequestRequestTypeDef = TypedDict(
    "ConfirmSignUpRequestRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
        "ConfirmationCode": str,
        "SecretHash": NotRequired[str],
        "ForceAliasCreation": NotRequired[bool],
        "AnalyticsMetadata": NotRequired["AnalyticsMetadataTypeTypeDef"],
        "UserContextData": NotRequired["UserContextDataTypeTypeDef"],
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)

ContextDataTypeTypeDef = TypedDict(
    "ContextDataTypeTypeDef",
    {
        "IpAddress": str,
        "ServerName": str,
        "ServerPath": str,
        "HttpHeaders": Sequence["HttpHeaderTypeDef"],
        "EncodedData": NotRequired[str],
    },
)

CreateGroupRequestRequestTypeDef = TypedDict(
    "CreateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Precedence": NotRequired[int],
    },
)

CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {
        "Group": "GroupTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIdentityProviderRequestRequestTypeDef = TypedDict(
    "CreateIdentityProviderRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderType": IdentityProviderTypeTypeType,
        "ProviderDetails": Mapping[str, str],
        "AttributeMapping": NotRequired[Mapping[str, str]],
        "IdpIdentifiers": NotRequired[Sequence[str]],
    },
)

CreateIdentityProviderResponseTypeDef = TypedDict(
    "CreateIdentityProviderResponseTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResourceServerRequestRequestTypeDef = TypedDict(
    "CreateResourceServerRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": NotRequired[Sequence["ResourceServerScopeTypeTypeDef"]],
    },
)

CreateResourceServerResponseTypeDef = TypedDict(
    "CreateResourceServerResponseTypeDef",
    {
        "ResourceServer": "ResourceServerTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserImportJobRequestRequestTypeDef = TypedDict(
    "CreateUserImportJobRequestRequestTypeDef",
    {
        "JobName": str,
        "UserPoolId": str,
        "CloudWatchLogsRoleArn": str,
    },
)

CreateUserImportJobResponseTypeDef = TypedDict(
    "CreateUserImportJobResponseTypeDef",
    {
        "UserImportJob": "UserImportJobTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserPoolClientRequestRequestTypeDef = TypedDict(
    "CreateUserPoolClientRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientName": str,
        "GenerateSecret": NotRequired[bool],
        "RefreshTokenValidity": NotRequired[int],
        "AccessTokenValidity": NotRequired[int],
        "IdTokenValidity": NotRequired[int],
        "TokenValidityUnits": NotRequired["TokenValidityUnitsTypeTypeDef"],
        "ReadAttributes": NotRequired[Sequence[str]],
        "WriteAttributes": NotRequired[Sequence[str]],
        "ExplicitAuthFlows": NotRequired[Sequence[ExplicitAuthFlowsTypeType]],
        "SupportedIdentityProviders": NotRequired[Sequence[str]],
        "CallbackURLs": NotRequired[Sequence[str]],
        "LogoutURLs": NotRequired[Sequence[str]],
        "DefaultRedirectURI": NotRequired[str],
        "AllowedOAuthFlows": NotRequired[Sequence[OAuthFlowTypeType]],
        "AllowedOAuthScopes": NotRequired[Sequence[str]],
        "AllowedOAuthFlowsUserPoolClient": NotRequired[bool],
        "AnalyticsConfiguration": NotRequired["AnalyticsConfigurationTypeTypeDef"],
        "PreventUserExistenceErrors": NotRequired[PreventUserExistenceErrorTypesType],
        "EnableTokenRevocation": NotRequired[bool],
    },
)

CreateUserPoolClientResponseTypeDef = TypedDict(
    "CreateUserPoolClientResponseTypeDef",
    {
        "UserPoolClient": "UserPoolClientTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserPoolDomainRequestRequestTypeDef = TypedDict(
    "CreateUserPoolDomainRequestRequestTypeDef",
    {
        "Domain": str,
        "UserPoolId": str,
        "CustomDomainConfig": NotRequired["CustomDomainConfigTypeTypeDef"],
    },
)

CreateUserPoolDomainResponseTypeDef = TypedDict(
    "CreateUserPoolDomainResponseTypeDef",
    {
        "CloudFrontDomain": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserPoolRequestRequestTypeDef = TypedDict(
    "CreateUserPoolRequestRequestTypeDef",
    {
        "PoolName": str,
        "Policies": NotRequired["UserPoolPolicyTypeTypeDef"],
        "LambdaConfig": NotRequired["LambdaConfigTypeTypeDef"],
        "AutoVerifiedAttributes": NotRequired[Sequence[VerifiedAttributeTypeType]],
        "AliasAttributes": NotRequired[Sequence[AliasAttributeTypeType]],
        "UsernameAttributes": NotRequired[Sequence[UsernameAttributeTypeType]],
        "SmsVerificationMessage": NotRequired[str],
        "EmailVerificationMessage": NotRequired[str],
        "EmailVerificationSubject": NotRequired[str],
        "VerificationMessageTemplate": NotRequired["VerificationMessageTemplateTypeTypeDef"],
        "SmsAuthenticationMessage": NotRequired[str],
        "MfaConfiguration": NotRequired[UserPoolMfaTypeType],
        "DeviceConfiguration": NotRequired["DeviceConfigurationTypeTypeDef"],
        "EmailConfiguration": NotRequired["EmailConfigurationTypeTypeDef"],
        "SmsConfiguration": NotRequired["SmsConfigurationTypeTypeDef"],
        "UserPoolTags": NotRequired[Mapping[str, str]],
        "AdminCreateUserConfig": NotRequired["AdminCreateUserConfigTypeTypeDef"],
        "Schema": NotRequired[Sequence["SchemaAttributeTypeTypeDef"]],
        "UserPoolAddOns": NotRequired["UserPoolAddOnsTypeTypeDef"],
        "UsernameConfiguration": NotRequired["UsernameConfigurationTypeTypeDef"],
        "AccountRecoverySetting": NotRequired["AccountRecoverySettingTypeTypeDef"],
    },
)

CreateUserPoolResponseTypeDef = TypedDict(
    "CreateUserPoolResponseTypeDef",
    {
        "UserPool": "UserPoolTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomDomainConfigTypeTypeDef = TypedDict(
    "CustomDomainConfigTypeTypeDef",
    {
        "CertificateArn": str,
    },
)

CustomEmailLambdaVersionConfigTypeTypeDef = TypedDict(
    "CustomEmailLambdaVersionConfigTypeTypeDef",
    {
        "LambdaVersion": Literal["V1_0"],
        "LambdaArn": str,
    },
)

CustomSMSLambdaVersionConfigTypeTypeDef = TypedDict(
    "CustomSMSLambdaVersionConfigTypeTypeDef",
    {
        "LambdaVersion": Literal["V1_0"],
        "LambdaArn": str,
    },
)

DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
    },
)

DeleteIdentityProviderRequestRequestTypeDef = TypedDict(
    "DeleteIdentityProviderRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
    },
)

DeleteResourceServerRequestRequestTypeDef = TypedDict(
    "DeleteResourceServerRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
    },
)

DeleteUserAttributesRequestRequestTypeDef = TypedDict(
    "DeleteUserAttributesRequestRequestTypeDef",
    {
        "UserAttributeNames": Sequence[str],
        "AccessToken": str,
    },
)

DeleteUserPoolClientRequestRequestTypeDef = TypedDict(
    "DeleteUserPoolClientRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
    },
)

DeleteUserPoolDomainRequestRequestTypeDef = TypedDict(
    "DeleteUserPoolDomainRequestRequestTypeDef",
    {
        "Domain": str,
        "UserPoolId": str,
    },
)

DeleteUserPoolRequestRequestTypeDef = TypedDict(
    "DeleteUserPoolRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "AccessToken": str,
    },
)

DescribeIdentityProviderRequestRequestTypeDef = TypedDict(
    "DescribeIdentityProviderRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
    },
)

DescribeIdentityProviderResponseTypeDef = TypedDict(
    "DescribeIdentityProviderResponseTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourceServerRequestRequestTypeDef = TypedDict(
    "DescribeResourceServerRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
    },
)

DescribeResourceServerResponseTypeDef = TypedDict(
    "DescribeResourceServerResponseTypeDef",
    {
        "ResourceServer": "ResourceServerTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRiskConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeRiskConfigurationRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": NotRequired[str],
    },
)

DescribeRiskConfigurationResponseTypeDef = TypedDict(
    "DescribeRiskConfigurationResponseTypeDef",
    {
        "RiskConfiguration": "RiskConfigurationTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserImportJobRequestRequestTypeDef = TypedDict(
    "DescribeUserImportJobRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "JobId": str,
    },
)

DescribeUserImportJobResponseTypeDef = TypedDict(
    "DescribeUserImportJobResponseTypeDef",
    {
        "UserImportJob": "UserImportJobTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserPoolClientRequestRequestTypeDef = TypedDict(
    "DescribeUserPoolClientRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
    },
)

DescribeUserPoolClientResponseTypeDef = TypedDict(
    "DescribeUserPoolClientResponseTypeDef",
    {
        "UserPoolClient": "UserPoolClientTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserPoolDomainRequestRequestTypeDef = TypedDict(
    "DescribeUserPoolDomainRequestRequestTypeDef",
    {
        "Domain": str,
    },
)

DescribeUserPoolDomainResponseTypeDef = TypedDict(
    "DescribeUserPoolDomainResponseTypeDef",
    {
        "DomainDescription": "DomainDescriptionTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserPoolRequestRequestTypeDef = TypedDict(
    "DescribeUserPoolRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)

DescribeUserPoolResponseTypeDef = TypedDict(
    "DescribeUserPoolResponseTypeDef",
    {
        "UserPool": "UserPoolTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceConfigurationTypeTypeDef = TypedDict(
    "DeviceConfigurationTypeTypeDef",
    {
        "ChallengeRequiredOnNewDevice": NotRequired[bool],
        "DeviceOnlyRememberedOnUserPrompt": NotRequired[bool],
    },
)

DeviceSecretVerifierConfigTypeTypeDef = TypedDict(
    "DeviceSecretVerifierConfigTypeTypeDef",
    {
        "PasswordVerifier": NotRequired[str],
        "Salt": NotRequired[str],
    },
)

DeviceTypeTypeDef = TypedDict(
    "DeviceTypeTypeDef",
    {
        "DeviceKey": NotRequired[str],
        "DeviceAttributes": NotRequired[List["AttributeTypeTypeDef"]],
        "DeviceCreateDate": NotRequired[datetime],
        "DeviceLastModifiedDate": NotRequired[datetime],
        "DeviceLastAuthenticatedDate": NotRequired[datetime],
    },
)

DomainDescriptionTypeTypeDef = TypedDict(
    "DomainDescriptionTypeTypeDef",
    {
        "UserPoolId": NotRequired[str],
        "AWSAccountId": NotRequired[str],
        "Domain": NotRequired[str],
        "S3Bucket": NotRequired[str],
        "CloudFrontDistribution": NotRequired[str],
        "Version": NotRequired[str],
        "Status": NotRequired[DomainStatusTypeType],
        "CustomDomainConfig": NotRequired["CustomDomainConfigTypeTypeDef"],
    },
)

EmailConfigurationTypeTypeDef = TypedDict(
    "EmailConfigurationTypeTypeDef",
    {
        "SourceArn": NotRequired[str],
        "ReplyToEmailAddress": NotRequired[str],
        "EmailSendingAccount": NotRequired[EmailSendingAccountTypeType],
        "From": NotRequired[str],
        "ConfigurationSet": NotRequired[str],
    },
)

EventContextDataTypeTypeDef = TypedDict(
    "EventContextDataTypeTypeDef",
    {
        "IpAddress": NotRequired[str],
        "DeviceName": NotRequired[str],
        "Timezone": NotRequired[str],
        "City": NotRequired[str],
        "Country": NotRequired[str],
    },
)

EventFeedbackTypeTypeDef = TypedDict(
    "EventFeedbackTypeTypeDef",
    {
        "FeedbackValue": FeedbackValueTypeType,
        "Provider": str,
        "FeedbackDate": NotRequired[datetime],
    },
)

EventRiskTypeTypeDef = TypedDict(
    "EventRiskTypeTypeDef",
    {
        "RiskDecision": NotRequired[RiskDecisionTypeType],
        "RiskLevel": NotRequired[RiskLevelTypeType],
        "CompromisedCredentialsDetected": NotRequired[bool],
    },
)

ForgetDeviceRequestRequestTypeDef = TypedDict(
    "ForgetDeviceRequestRequestTypeDef",
    {
        "DeviceKey": str,
        "AccessToken": NotRequired[str],
    },
)

ForgotPasswordRequestRequestTypeDef = TypedDict(
    "ForgotPasswordRequestRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
        "SecretHash": NotRequired[str],
        "UserContextData": NotRequired["UserContextDataTypeTypeDef"],
        "AnalyticsMetadata": NotRequired["AnalyticsMetadataTypeTypeDef"],
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)

ForgotPasswordResponseTypeDef = TypedDict(
    "ForgotPasswordResponseTypeDef",
    {
        "CodeDeliveryDetails": "CodeDeliveryDetailsTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCSVHeaderRequestRequestTypeDef = TypedDict(
    "GetCSVHeaderRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)

GetCSVHeaderResponseTypeDef = TypedDict(
    "GetCSVHeaderResponseTypeDef",
    {
        "UserPoolId": str,
        "CSVHeader": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeviceRequestRequestTypeDef = TypedDict(
    "GetDeviceRequestRequestTypeDef",
    {
        "DeviceKey": str,
        "AccessToken": NotRequired[str],
    },
)

GetDeviceResponseTypeDef = TypedDict(
    "GetDeviceResponseTypeDef",
    {
        "Device": "DeviceTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupRequestRequestTypeDef = TypedDict(
    "GetGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
    },
)

GetGroupResponseTypeDef = TypedDict(
    "GetGroupResponseTypeDef",
    {
        "Group": "GroupTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityProviderByIdentifierRequestRequestTypeDef = TypedDict(
    "GetIdentityProviderByIdentifierRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "IdpIdentifier": str,
    },
)

GetIdentityProviderByIdentifierResponseTypeDef = TypedDict(
    "GetIdentityProviderByIdentifierResponseTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSigningCertificateRequestRequestTypeDef = TypedDict(
    "GetSigningCertificateRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)

GetSigningCertificateResponseTypeDef = TypedDict(
    "GetSigningCertificateResponseTypeDef",
    {
        "Certificate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUICustomizationRequestRequestTypeDef = TypedDict(
    "GetUICustomizationRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": NotRequired[str],
    },
)

GetUICustomizationResponseTypeDef = TypedDict(
    "GetUICustomizationResponseTypeDef",
    {
        "UICustomization": "UICustomizationTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserAttributeVerificationCodeRequestRequestTypeDef = TypedDict(
    "GetUserAttributeVerificationCodeRequestRequestTypeDef",
    {
        "AccessToken": str,
        "AttributeName": str,
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)

GetUserAttributeVerificationCodeResponseTypeDef = TypedDict(
    "GetUserAttributeVerificationCodeResponseTypeDef",
    {
        "CodeDeliveryDetails": "CodeDeliveryDetailsTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserPoolMfaConfigRequestRequestTypeDef = TypedDict(
    "GetUserPoolMfaConfigRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)

GetUserPoolMfaConfigResponseTypeDef = TypedDict(
    "GetUserPoolMfaConfigResponseTypeDef",
    {
        "SmsMfaConfiguration": "SmsMfaConfigTypeTypeDef",
        "SoftwareTokenMfaConfiguration": "SoftwareTokenMfaConfigTypeTypeDef",
        "MfaConfiguration": UserPoolMfaTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserRequestRequestTypeDef = TypedDict(
    "GetUserRequestRequestTypeDef",
    {
        "AccessToken": str,
    },
)

GetUserResponseTypeDef = TypedDict(
    "GetUserResponseTypeDef",
    {
        "Username": str,
        "UserAttributes": List["AttributeTypeTypeDef"],
        "MFAOptions": List["MFAOptionTypeTypeDef"],
        "PreferredMfaSetting": str,
        "UserMFASettingList": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GlobalSignOutRequestRequestTypeDef = TypedDict(
    "GlobalSignOutRequestRequestTypeDef",
    {
        "AccessToken": str,
    },
)

GroupTypeTypeDef = TypedDict(
    "GroupTypeTypeDef",
    {
        "GroupName": NotRequired[str],
        "UserPoolId": NotRequired[str],
        "Description": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Precedence": NotRequired[int],
        "LastModifiedDate": NotRequired[datetime],
        "CreationDate": NotRequired[datetime],
    },
)

HttpHeaderTypeDef = TypedDict(
    "HttpHeaderTypeDef",
    {
        "headerName": NotRequired[str],
        "headerValue": NotRequired[str],
    },
)

IdentityProviderTypeTypeDef = TypedDict(
    "IdentityProviderTypeTypeDef",
    {
        "UserPoolId": NotRequired[str],
        "ProviderName": NotRequired[str],
        "ProviderType": NotRequired[IdentityProviderTypeTypeType],
        "ProviderDetails": NotRequired[Dict[str, str]],
        "AttributeMapping": NotRequired[Dict[str, str]],
        "IdpIdentifiers": NotRequired[List[str]],
        "LastModifiedDate": NotRequired[datetime],
        "CreationDate": NotRequired[datetime],
    },
)

InitiateAuthRequestRequestTypeDef = TypedDict(
    "InitiateAuthRequestRequestTypeDef",
    {
        "AuthFlow": AuthFlowTypeType,
        "ClientId": str,
        "AuthParameters": NotRequired[Mapping[str, str]],
        "ClientMetadata": NotRequired[Mapping[str, str]],
        "AnalyticsMetadata": NotRequired["AnalyticsMetadataTypeTypeDef"],
        "UserContextData": NotRequired["UserContextDataTypeTypeDef"],
    },
)

InitiateAuthResponseTypeDef = TypedDict(
    "InitiateAuthResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": "AuthenticationResultTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LambdaConfigTypeTypeDef = TypedDict(
    "LambdaConfigTypeTypeDef",
    {
        "PreSignUp": NotRequired[str],
        "CustomMessage": NotRequired[str],
        "PostConfirmation": NotRequired[str],
        "PreAuthentication": NotRequired[str],
        "PostAuthentication": NotRequired[str],
        "DefineAuthChallenge": NotRequired[str],
        "CreateAuthChallenge": NotRequired[str],
        "VerifyAuthChallengeResponse": NotRequired[str],
        "PreTokenGeneration": NotRequired[str],
        "UserMigration": NotRequired[str],
        "CustomSMSSender": NotRequired["CustomSMSLambdaVersionConfigTypeTypeDef"],
        "CustomEmailSender": NotRequired["CustomEmailLambdaVersionConfigTypeTypeDef"],
        "KMSKeyID": NotRequired[str],
    },
)

ListDevicesRequestRequestTypeDef = TypedDict(
    "ListDevicesRequestRequestTypeDef",
    {
        "AccessToken": str,
        "Limit": NotRequired[int],
        "PaginationToken": NotRequired[str],
    },
)

ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {
        "Devices": List["DeviceTypeTypeDef"],
        "PaginationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroupsRequestRequestTypeDef = TypedDict(
    "ListGroupsRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "Groups": List["GroupTypeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIdentityProvidersRequestRequestTypeDef = TypedDict(
    "ListIdentityProvidersRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListIdentityProvidersResponseTypeDef = TypedDict(
    "ListIdentityProvidersResponseTypeDef",
    {
        "Providers": List["ProviderDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceServersRequestRequestTypeDef = TypedDict(
    "ListResourceServersRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListResourceServersResponseTypeDef = TypedDict(
    "ListResourceServersResponseTypeDef",
    {
        "ResourceServers": List["ResourceServerTypeTypeDef"],
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
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUserImportJobsRequestRequestTypeDef = TypedDict(
    "ListUserImportJobsRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "MaxResults": int,
        "PaginationToken": NotRequired[str],
    },
)

ListUserImportJobsResponseTypeDef = TypedDict(
    "ListUserImportJobsResponseTypeDef",
    {
        "UserImportJobs": List["UserImportJobTypeTypeDef"],
        "PaginationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUserPoolClientsRequestRequestTypeDef = TypedDict(
    "ListUserPoolClientsRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListUserPoolClientsResponseTypeDef = TypedDict(
    "ListUserPoolClientsResponseTypeDef",
    {
        "UserPoolClients": List["UserPoolClientDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUserPoolsRequestRequestTypeDef = TypedDict(
    "ListUserPoolsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": NotRequired[str],
    },
)

ListUserPoolsResponseTypeDef = TypedDict(
    "ListUserPoolsResponseTypeDef",
    {
        "UserPools": List["UserPoolDescriptionTypeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUsersInGroupRequestRequestTypeDef = TypedDict(
    "ListUsersInGroupRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "GroupName": str,
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListUsersInGroupResponseTypeDef = TypedDict(
    "ListUsersInGroupResponseTypeDef",
    {
        "Users": List["UserTypeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUsersRequestRequestTypeDef = TypedDict(
    "ListUsersRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "AttributesToGet": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "PaginationToken": NotRequired[str],
        "Filter": NotRequired[str],
    },
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "Users": List["UserTypeTypeDef"],
        "PaginationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MFAOptionTypeTypeDef = TypedDict(
    "MFAOptionTypeTypeDef",
    {
        "DeliveryMedium": NotRequired[DeliveryMediumTypeType],
        "AttributeName": NotRequired[str],
    },
)

MessageTemplateTypeTypeDef = TypedDict(
    "MessageTemplateTypeTypeDef",
    {
        "SMSMessage": NotRequired[str],
        "EmailMessage": NotRequired[str],
        "EmailSubject": NotRequired[str],
    },
)

NewDeviceMetadataTypeTypeDef = TypedDict(
    "NewDeviceMetadataTypeTypeDef",
    {
        "DeviceKey": NotRequired[str],
        "DeviceGroupKey": NotRequired[str],
    },
)

NotifyConfigurationTypeTypeDef = TypedDict(
    "NotifyConfigurationTypeTypeDef",
    {
        "SourceArn": str,
        "From": NotRequired[str],
        "ReplyTo": NotRequired[str],
        "BlockEmail": NotRequired["NotifyEmailTypeTypeDef"],
        "NoActionEmail": NotRequired["NotifyEmailTypeTypeDef"],
        "MfaEmail": NotRequired["NotifyEmailTypeTypeDef"],
    },
)

NotifyEmailTypeTypeDef = TypedDict(
    "NotifyEmailTypeTypeDef",
    {
        "Subject": str,
        "HtmlBody": NotRequired[str],
        "TextBody": NotRequired[str],
    },
)

NumberAttributeConstraintsTypeTypeDef = TypedDict(
    "NumberAttributeConstraintsTypeTypeDef",
    {
        "MinValue": NotRequired[str],
        "MaxValue": NotRequired[str],
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

PasswordPolicyTypeTypeDef = TypedDict(
    "PasswordPolicyTypeTypeDef",
    {
        "MinimumLength": NotRequired[int],
        "RequireUppercase": NotRequired[bool],
        "RequireLowercase": NotRequired[bool],
        "RequireNumbers": NotRequired[bool],
        "RequireSymbols": NotRequired[bool],
        "TemporaryPasswordValidityDays": NotRequired[int],
    },
)

ProviderDescriptionTypeDef = TypedDict(
    "ProviderDescriptionTypeDef",
    {
        "ProviderName": NotRequired[str],
        "ProviderType": NotRequired[IdentityProviderTypeTypeType],
        "LastModifiedDate": NotRequired[datetime],
        "CreationDate": NotRequired[datetime],
    },
)

ProviderUserIdentifierTypeTypeDef = TypedDict(
    "ProviderUserIdentifierTypeTypeDef",
    {
        "ProviderName": NotRequired[str],
        "ProviderAttributeName": NotRequired[str],
        "ProviderAttributeValue": NotRequired[str],
    },
)

RecoveryOptionTypeTypeDef = TypedDict(
    "RecoveryOptionTypeTypeDef",
    {
        "Priority": int,
        "Name": RecoveryOptionNameTypeType,
    },
)

ResendConfirmationCodeRequestRequestTypeDef = TypedDict(
    "ResendConfirmationCodeRequestRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
        "SecretHash": NotRequired[str],
        "UserContextData": NotRequired["UserContextDataTypeTypeDef"],
        "AnalyticsMetadata": NotRequired["AnalyticsMetadataTypeTypeDef"],
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)

ResendConfirmationCodeResponseTypeDef = TypedDict(
    "ResendConfirmationCodeResponseTypeDef",
    {
        "CodeDeliveryDetails": "CodeDeliveryDetailsTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceServerScopeTypeTypeDef = TypedDict(
    "ResourceServerScopeTypeTypeDef",
    {
        "ScopeName": str,
        "ScopeDescription": str,
    },
)

ResourceServerTypeTypeDef = TypedDict(
    "ResourceServerTypeTypeDef",
    {
        "UserPoolId": NotRequired[str],
        "Identifier": NotRequired[str],
        "Name": NotRequired[str],
        "Scopes": NotRequired[List["ResourceServerScopeTypeTypeDef"]],
    },
)

RespondToAuthChallengeRequestRequestTypeDef = TypedDict(
    "RespondToAuthChallengeRequestRequestTypeDef",
    {
        "ClientId": str,
        "ChallengeName": ChallengeNameTypeType,
        "Session": NotRequired[str],
        "ChallengeResponses": NotRequired[Mapping[str, str]],
        "AnalyticsMetadata": NotRequired["AnalyticsMetadataTypeTypeDef"],
        "UserContextData": NotRequired["UserContextDataTypeTypeDef"],
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)

RespondToAuthChallengeResponseTypeDef = TypedDict(
    "RespondToAuthChallengeResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": "AuthenticationResultTypeTypeDef",
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

RevokeTokenRequestRequestTypeDef = TypedDict(
    "RevokeTokenRequestRequestTypeDef",
    {
        "Token": str,
        "ClientId": str,
        "ClientSecret": NotRequired[str],
    },
)

RiskConfigurationTypeTypeDef = TypedDict(
    "RiskConfigurationTypeTypeDef",
    {
        "UserPoolId": NotRequired[str],
        "ClientId": NotRequired[str],
        "CompromisedCredentialsRiskConfiguration": NotRequired[
            "CompromisedCredentialsRiskConfigurationTypeTypeDef"
        ],
        "AccountTakeoverRiskConfiguration": NotRequired[
            "AccountTakeoverRiskConfigurationTypeTypeDef"
        ],
        "RiskExceptionConfiguration": NotRequired["RiskExceptionConfigurationTypeTypeDef"],
        "LastModifiedDate": NotRequired[datetime],
    },
)

RiskExceptionConfigurationTypeTypeDef = TypedDict(
    "RiskExceptionConfigurationTypeTypeDef",
    {
        "BlockedIPRangeList": NotRequired[List[str]],
        "SkippedIPRangeList": NotRequired[List[str]],
    },
)

SMSMfaSettingsTypeTypeDef = TypedDict(
    "SMSMfaSettingsTypeTypeDef",
    {
        "Enabled": NotRequired[bool],
        "PreferredMfa": NotRequired[bool],
    },
)

SchemaAttributeTypeTypeDef = TypedDict(
    "SchemaAttributeTypeTypeDef",
    {
        "Name": NotRequired[str],
        "AttributeDataType": NotRequired[AttributeDataTypeType],
        "DeveloperOnlyAttribute": NotRequired[bool],
        "Mutable": NotRequired[bool],
        "Required": NotRequired[bool],
        "NumberAttributeConstraints": NotRequired["NumberAttributeConstraintsTypeTypeDef"],
        "StringAttributeConstraints": NotRequired["StringAttributeConstraintsTypeTypeDef"],
    },
)

SetRiskConfigurationRequestRequestTypeDef = TypedDict(
    "SetRiskConfigurationRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": NotRequired[str],
        "CompromisedCredentialsRiskConfiguration": NotRequired[
            "CompromisedCredentialsRiskConfigurationTypeTypeDef"
        ],
        "AccountTakeoverRiskConfiguration": NotRequired[
            "AccountTakeoverRiskConfigurationTypeTypeDef"
        ],
        "RiskExceptionConfiguration": NotRequired["RiskExceptionConfigurationTypeTypeDef"],
    },
)

SetRiskConfigurationResponseTypeDef = TypedDict(
    "SetRiskConfigurationResponseTypeDef",
    {
        "RiskConfiguration": "RiskConfigurationTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetUICustomizationRequestRequestTypeDef = TypedDict(
    "SetUICustomizationRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": NotRequired[str],
        "CSS": NotRequired[str],
        "ImageFile": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
    },
)

SetUICustomizationResponseTypeDef = TypedDict(
    "SetUICustomizationResponseTypeDef",
    {
        "UICustomization": "UICustomizationTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetUserMFAPreferenceRequestRequestTypeDef = TypedDict(
    "SetUserMFAPreferenceRequestRequestTypeDef",
    {
        "AccessToken": str,
        "SMSMfaSettings": NotRequired["SMSMfaSettingsTypeTypeDef"],
        "SoftwareTokenMfaSettings": NotRequired["SoftwareTokenMfaSettingsTypeTypeDef"],
    },
)

SetUserPoolMfaConfigRequestRequestTypeDef = TypedDict(
    "SetUserPoolMfaConfigRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "SmsMfaConfiguration": NotRequired["SmsMfaConfigTypeTypeDef"],
        "SoftwareTokenMfaConfiguration": NotRequired["SoftwareTokenMfaConfigTypeTypeDef"],
        "MfaConfiguration": NotRequired[UserPoolMfaTypeType],
    },
)

SetUserPoolMfaConfigResponseTypeDef = TypedDict(
    "SetUserPoolMfaConfigResponseTypeDef",
    {
        "SmsMfaConfiguration": "SmsMfaConfigTypeTypeDef",
        "SoftwareTokenMfaConfiguration": "SoftwareTokenMfaConfigTypeTypeDef",
        "MfaConfiguration": UserPoolMfaTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetUserSettingsRequestRequestTypeDef = TypedDict(
    "SetUserSettingsRequestRequestTypeDef",
    {
        "AccessToken": str,
        "MFAOptions": Sequence["MFAOptionTypeTypeDef"],
    },
)

SignUpRequestRequestTypeDef = TypedDict(
    "SignUpRequestRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
        "Password": str,
        "SecretHash": NotRequired[str],
        "UserAttributes": NotRequired[Sequence["AttributeTypeTypeDef"]],
        "ValidationData": NotRequired[Sequence["AttributeTypeTypeDef"]],
        "AnalyticsMetadata": NotRequired["AnalyticsMetadataTypeTypeDef"],
        "UserContextData": NotRequired["UserContextDataTypeTypeDef"],
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)

SignUpResponseTypeDef = TypedDict(
    "SignUpResponseTypeDef",
    {
        "UserConfirmed": bool,
        "CodeDeliveryDetails": "CodeDeliveryDetailsTypeTypeDef",
        "UserSub": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SmsConfigurationTypeTypeDef = TypedDict(
    "SmsConfigurationTypeTypeDef",
    {
        "SnsCallerArn": str,
        "ExternalId": NotRequired[str],
        "SnsRegion": NotRequired[str],
    },
)

SmsMfaConfigTypeTypeDef = TypedDict(
    "SmsMfaConfigTypeTypeDef",
    {
        "SmsAuthenticationMessage": NotRequired[str],
        "SmsConfiguration": NotRequired["SmsConfigurationTypeTypeDef"],
    },
)

SoftwareTokenMfaConfigTypeTypeDef = TypedDict(
    "SoftwareTokenMfaConfigTypeTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)

SoftwareTokenMfaSettingsTypeTypeDef = TypedDict(
    "SoftwareTokenMfaSettingsTypeTypeDef",
    {
        "Enabled": NotRequired[bool],
        "PreferredMfa": NotRequired[bool],
    },
)

StartUserImportJobRequestRequestTypeDef = TypedDict(
    "StartUserImportJobRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "JobId": str,
    },
)

StartUserImportJobResponseTypeDef = TypedDict(
    "StartUserImportJobResponseTypeDef",
    {
        "UserImportJob": "UserImportJobTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopUserImportJobRequestRequestTypeDef = TypedDict(
    "StopUserImportJobRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "JobId": str,
    },
)

StopUserImportJobResponseTypeDef = TypedDict(
    "StopUserImportJobResponseTypeDef",
    {
        "UserImportJob": "UserImportJobTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StringAttributeConstraintsTypeTypeDef = TypedDict(
    "StringAttributeConstraintsTypeTypeDef",
    {
        "MinLength": NotRequired[str],
        "MaxLength": NotRequired[str],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

TokenValidityUnitsTypeTypeDef = TypedDict(
    "TokenValidityUnitsTypeTypeDef",
    {
        "AccessToken": NotRequired[TimeUnitsTypeType],
        "IdToken": NotRequired[TimeUnitsTypeType],
        "RefreshToken": NotRequired[TimeUnitsTypeType],
    },
)

UICustomizationTypeTypeDef = TypedDict(
    "UICustomizationTypeTypeDef",
    {
        "UserPoolId": NotRequired[str],
        "ClientId": NotRequired[str],
        "ImageUrl": NotRequired[str],
        "CSS": NotRequired[str],
        "CSSVersion": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "CreationDate": NotRequired[datetime],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateAuthEventFeedbackRequestRequestTypeDef = TypedDict(
    "UpdateAuthEventFeedbackRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "EventId": str,
        "FeedbackToken": str,
        "FeedbackValue": FeedbackValueTypeType,
    },
)

UpdateDeviceStatusRequestRequestTypeDef = TypedDict(
    "UpdateDeviceStatusRequestRequestTypeDef",
    {
        "AccessToken": str,
        "DeviceKey": str,
        "DeviceRememberedStatus": NotRequired[DeviceRememberedStatusTypeType],
    },
)

UpdateGroupRequestRequestTypeDef = TypedDict(
    "UpdateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Precedence": NotRequired[int],
    },
)

UpdateGroupResponseTypeDef = TypedDict(
    "UpdateGroupResponseTypeDef",
    {
        "Group": "GroupTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateIdentityProviderRequestRequestTypeDef = TypedDict(
    "UpdateIdentityProviderRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderDetails": NotRequired[Mapping[str, str]],
        "AttributeMapping": NotRequired[Mapping[str, str]],
        "IdpIdentifiers": NotRequired[Sequence[str]],
    },
)

UpdateIdentityProviderResponseTypeDef = TypedDict(
    "UpdateIdentityProviderResponseTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateResourceServerRequestRequestTypeDef = TypedDict(
    "UpdateResourceServerRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": NotRequired[Sequence["ResourceServerScopeTypeTypeDef"]],
    },
)

UpdateResourceServerResponseTypeDef = TypedDict(
    "UpdateResourceServerResponseTypeDef",
    {
        "ResourceServer": "ResourceServerTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserAttributesRequestRequestTypeDef = TypedDict(
    "UpdateUserAttributesRequestRequestTypeDef",
    {
        "UserAttributes": Sequence["AttributeTypeTypeDef"],
        "AccessToken": str,
        "ClientMetadata": NotRequired[Mapping[str, str]],
    },
)

UpdateUserAttributesResponseTypeDef = TypedDict(
    "UpdateUserAttributesResponseTypeDef",
    {
        "CodeDeliveryDetailsList": List["CodeDeliveryDetailsTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserPoolClientRequestRequestTypeDef = TypedDict(
    "UpdateUserPoolClientRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "ClientName": NotRequired[str],
        "RefreshTokenValidity": NotRequired[int],
        "AccessTokenValidity": NotRequired[int],
        "IdTokenValidity": NotRequired[int],
        "TokenValidityUnits": NotRequired["TokenValidityUnitsTypeTypeDef"],
        "ReadAttributes": NotRequired[Sequence[str]],
        "WriteAttributes": NotRequired[Sequence[str]],
        "ExplicitAuthFlows": NotRequired[Sequence[ExplicitAuthFlowsTypeType]],
        "SupportedIdentityProviders": NotRequired[Sequence[str]],
        "CallbackURLs": NotRequired[Sequence[str]],
        "LogoutURLs": NotRequired[Sequence[str]],
        "DefaultRedirectURI": NotRequired[str],
        "AllowedOAuthFlows": NotRequired[Sequence[OAuthFlowTypeType]],
        "AllowedOAuthScopes": NotRequired[Sequence[str]],
        "AllowedOAuthFlowsUserPoolClient": NotRequired[bool],
        "AnalyticsConfiguration": NotRequired["AnalyticsConfigurationTypeTypeDef"],
        "PreventUserExistenceErrors": NotRequired[PreventUserExistenceErrorTypesType],
        "EnableTokenRevocation": NotRequired[bool],
    },
)

UpdateUserPoolClientResponseTypeDef = TypedDict(
    "UpdateUserPoolClientResponseTypeDef",
    {
        "UserPoolClient": "UserPoolClientTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserPoolDomainRequestRequestTypeDef = TypedDict(
    "UpdateUserPoolDomainRequestRequestTypeDef",
    {
        "Domain": str,
        "UserPoolId": str,
        "CustomDomainConfig": "CustomDomainConfigTypeTypeDef",
    },
)

UpdateUserPoolDomainResponseTypeDef = TypedDict(
    "UpdateUserPoolDomainResponseTypeDef",
    {
        "CloudFrontDomain": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserPoolRequestRequestTypeDef = TypedDict(
    "UpdateUserPoolRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Policies": NotRequired["UserPoolPolicyTypeTypeDef"],
        "LambdaConfig": NotRequired["LambdaConfigTypeTypeDef"],
        "AutoVerifiedAttributes": NotRequired[Sequence[VerifiedAttributeTypeType]],
        "SmsVerificationMessage": NotRequired[str],
        "EmailVerificationMessage": NotRequired[str],
        "EmailVerificationSubject": NotRequired[str],
        "VerificationMessageTemplate": NotRequired["VerificationMessageTemplateTypeTypeDef"],
        "SmsAuthenticationMessage": NotRequired[str],
        "MfaConfiguration": NotRequired[UserPoolMfaTypeType],
        "DeviceConfiguration": NotRequired["DeviceConfigurationTypeTypeDef"],
        "EmailConfiguration": NotRequired["EmailConfigurationTypeTypeDef"],
        "SmsConfiguration": NotRequired["SmsConfigurationTypeTypeDef"],
        "UserPoolTags": NotRequired[Mapping[str, str]],
        "AdminCreateUserConfig": NotRequired["AdminCreateUserConfigTypeTypeDef"],
        "UserPoolAddOns": NotRequired["UserPoolAddOnsTypeTypeDef"],
        "AccountRecoverySetting": NotRequired["AccountRecoverySettingTypeTypeDef"],
    },
)

UserContextDataTypeTypeDef = TypedDict(
    "UserContextDataTypeTypeDef",
    {
        "EncodedData": NotRequired[str],
    },
)

UserImportJobTypeTypeDef = TypedDict(
    "UserImportJobTypeTypeDef",
    {
        "JobName": NotRequired[str],
        "JobId": NotRequired[str],
        "UserPoolId": NotRequired[str],
        "PreSignedUrl": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "StartDate": NotRequired[datetime],
        "CompletionDate": NotRequired[datetime],
        "Status": NotRequired[UserImportJobStatusTypeType],
        "CloudWatchLogsRoleArn": NotRequired[str],
        "ImportedUsers": NotRequired[int],
        "SkippedUsers": NotRequired[int],
        "FailedUsers": NotRequired[int],
        "CompletionMessage": NotRequired[str],
    },
)

UserPoolAddOnsTypeTypeDef = TypedDict(
    "UserPoolAddOnsTypeTypeDef",
    {
        "AdvancedSecurityMode": AdvancedSecurityModeTypeType,
    },
)

UserPoolClientDescriptionTypeDef = TypedDict(
    "UserPoolClientDescriptionTypeDef",
    {
        "ClientId": NotRequired[str],
        "UserPoolId": NotRequired[str],
        "ClientName": NotRequired[str],
    },
)

UserPoolClientTypeTypeDef = TypedDict(
    "UserPoolClientTypeTypeDef",
    {
        "UserPoolId": NotRequired[str],
        "ClientName": NotRequired[str],
        "ClientId": NotRequired[str],
        "ClientSecret": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "CreationDate": NotRequired[datetime],
        "RefreshTokenValidity": NotRequired[int],
        "AccessTokenValidity": NotRequired[int],
        "IdTokenValidity": NotRequired[int],
        "TokenValidityUnits": NotRequired["TokenValidityUnitsTypeTypeDef"],
        "ReadAttributes": NotRequired[List[str]],
        "WriteAttributes": NotRequired[List[str]],
        "ExplicitAuthFlows": NotRequired[List[ExplicitAuthFlowsTypeType]],
        "SupportedIdentityProviders": NotRequired[List[str]],
        "CallbackURLs": NotRequired[List[str]],
        "LogoutURLs": NotRequired[List[str]],
        "DefaultRedirectURI": NotRequired[str],
        "AllowedOAuthFlows": NotRequired[List[OAuthFlowTypeType]],
        "AllowedOAuthScopes": NotRequired[List[str]],
        "AllowedOAuthFlowsUserPoolClient": NotRequired[bool],
        "AnalyticsConfiguration": NotRequired["AnalyticsConfigurationTypeTypeDef"],
        "PreventUserExistenceErrors": NotRequired[PreventUserExistenceErrorTypesType],
        "EnableTokenRevocation": NotRequired[bool],
    },
)

UserPoolDescriptionTypeTypeDef = TypedDict(
    "UserPoolDescriptionTypeTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "LambdaConfig": NotRequired["LambdaConfigTypeTypeDef"],
        "Status": NotRequired[StatusTypeType],
        "LastModifiedDate": NotRequired[datetime],
        "CreationDate": NotRequired[datetime],
    },
)

UserPoolPolicyTypeTypeDef = TypedDict(
    "UserPoolPolicyTypeTypeDef",
    {
        "PasswordPolicy": NotRequired["PasswordPolicyTypeTypeDef"],
    },
)

UserPoolTypeTypeDef = TypedDict(
    "UserPoolTypeTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Policies": NotRequired["UserPoolPolicyTypeTypeDef"],
        "LambdaConfig": NotRequired["LambdaConfigTypeTypeDef"],
        "Status": NotRequired[StatusTypeType],
        "LastModifiedDate": NotRequired[datetime],
        "CreationDate": NotRequired[datetime],
        "SchemaAttributes": NotRequired[List["SchemaAttributeTypeTypeDef"]],
        "AutoVerifiedAttributes": NotRequired[List[VerifiedAttributeTypeType]],
        "AliasAttributes": NotRequired[List[AliasAttributeTypeType]],
        "UsernameAttributes": NotRequired[List[UsernameAttributeTypeType]],
        "SmsVerificationMessage": NotRequired[str],
        "EmailVerificationMessage": NotRequired[str],
        "EmailVerificationSubject": NotRequired[str],
        "VerificationMessageTemplate": NotRequired["VerificationMessageTemplateTypeTypeDef"],
        "SmsAuthenticationMessage": NotRequired[str],
        "MfaConfiguration": NotRequired[UserPoolMfaTypeType],
        "DeviceConfiguration": NotRequired["DeviceConfigurationTypeTypeDef"],
        "EstimatedNumberOfUsers": NotRequired[int],
        "EmailConfiguration": NotRequired["EmailConfigurationTypeTypeDef"],
        "SmsConfiguration": NotRequired["SmsConfigurationTypeTypeDef"],
        "UserPoolTags": NotRequired[Dict[str, str]],
        "SmsConfigurationFailure": NotRequired[str],
        "EmailConfigurationFailure": NotRequired[str],
        "Domain": NotRequired[str],
        "CustomDomain": NotRequired[str],
        "AdminCreateUserConfig": NotRequired["AdminCreateUserConfigTypeTypeDef"],
        "UserPoolAddOns": NotRequired["UserPoolAddOnsTypeTypeDef"],
        "UsernameConfiguration": NotRequired["UsernameConfigurationTypeTypeDef"],
        "Arn": NotRequired[str],
        "AccountRecoverySetting": NotRequired["AccountRecoverySettingTypeTypeDef"],
    },
)

UserTypeTypeDef = TypedDict(
    "UserTypeTypeDef",
    {
        "Username": NotRequired[str],
        "Attributes": NotRequired[List["AttributeTypeTypeDef"]],
        "UserCreateDate": NotRequired[datetime],
        "UserLastModifiedDate": NotRequired[datetime],
        "Enabled": NotRequired[bool],
        "UserStatus": NotRequired[UserStatusTypeType],
        "MFAOptions": NotRequired[List["MFAOptionTypeTypeDef"]],
    },
)

UsernameConfigurationTypeTypeDef = TypedDict(
    "UsernameConfigurationTypeTypeDef",
    {
        "CaseSensitive": bool,
    },
)

VerificationMessageTemplateTypeTypeDef = TypedDict(
    "VerificationMessageTemplateTypeTypeDef",
    {
        "SmsMessage": NotRequired[str],
        "EmailMessage": NotRequired[str],
        "EmailSubject": NotRequired[str],
        "EmailMessageByLink": NotRequired[str],
        "EmailSubjectByLink": NotRequired[str],
        "DefaultEmailOption": NotRequired[DefaultEmailOptionTypeType],
    },
)

VerifySoftwareTokenRequestRequestTypeDef = TypedDict(
    "VerifySoftwareTokenRequestRequestTypeDef",
    {
        "UserCode": str,
        "AccessToken": NotRequired[str],
        "Session": NotRequired[str],
        "FriendlyDeviceName": NotRequired[str],
    },
)

VerifySoftwareTokenResponseTypeDef = TypedDict(
    "VerifySoftwareTokenResponseTypeDef",
    {
        "Status": VerifySoftwareTokenResponseTypeType,
        "Session": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VerifyUserAttributeRequestRequestTypeDef = TypedDict(
    "VerifyUserAttributeRequestRequestTypeDef",
    {
        "AccessToken": str,
        "AttributeName": str,
        "Code": str,
    },
)
