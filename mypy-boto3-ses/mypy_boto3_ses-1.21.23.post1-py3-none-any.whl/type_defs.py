"""
Type annotations for ses service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ses.type_defs import AddHeaderActionTypeDef

    data: AddHeaderActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    BehaviorOnMXFailureType,
    BounceTypeType,
    BulkEmailStatusType,
    ConfigurationSetAttributeType,
    CustomMailFromStatusType,
    DimensionValueSourceType,
    DsnActionType,
    EventTypeType,
    IdentityTypeType,
    InvocationTypeType,
    NotificationTypeType,
    ReceiptFilterPolicyType,
    SNSActionEncodingType,
    TlsPolicyType,
    VerificationStatusType,
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
    "AddHeaderActionTypeDef",
    "BodyTypeDef",
    "BounceActionTypeDef",
    "BouncedRecipientInfoTypeDef",
    "BulkEmailDestinationStatusTypeDef",
    "BulkEmailDestinationTypeDef",
    "CloneReceiptRuleSetRequestRequestTypeDef",
    "CloudWatchDestinationTypeDef",
    "CloudWatchDimensionConfigurationTypeDef",
    "ConfigurationSetTypeDef",
    "ContentTypeDef",
    "CreateConfigurationSetEventDestinationRequestRequestTypeDef",
    "CreateConfigurationSetRequestRequestTypeDef",
    "CreateConfigurationSetTrackingOptionsRequestRequestTypeDef",
    "CreateCustomVerificationEmailTemplateRequestRequestTypeDef",
    "CreateReceiptFilterRequestRequestTypeDef",
    "CreateReceiptRuleRequestRequestTypeDef",
    "CreateReceiptRuleSetRequestRequestTypeDef",
    "CreateTemplateRequestRequestTypeDef",
    "CustomVerificationEmailTemplateTypeDef",
    "DeleteConfigurationSetEventDestinationRequestRequestTypeDef",
    "DeleteConfigurationSetRequestRequestTypeDef",
    "DeleteConfigurationSetTrackingOptionsRequestRequestTypeDef",
    "DeleteCustomVerificationEmailTemplateRequestRequestTypeDef",
    "DeleteIdentityPolicyRequestRequestTypeDef",
    "DeleteIdentityRequestRequestTypeDef",
    "DeleteReceiptFilterRequestRequestTypeDef",
    "DeleteReceiptRuleRequestRequestTypeDef",
    "DeleteReceiptRuleSetRequestRequestTypeDef",
    "DeleteTemplateRequestRequestTypeDef",
    "DeleteVerifiedEmailAddressRequestRequestTypeDef",
    "DeliveryOptionsTypeDef",
    "DescribeActiveReceiptRuleSetResponseTypeDef",
    "DescribeConfigurationSetRequestRequestTypeDef",
    "DescribeConfigurationSetResponseTypeDef",
    "DescribeReceiptRuleRequestRequestTypeDef",
    "DescribeReceiptRuleResponseTypeDef",
    "DescribeReceiptRuleSetRequestRequestTypeDef",
    "DescribeReceiptRuleSetResponseTypeDef",
    "DestinationTypeDef",
    "EventDestinationTypeDef",
    "ExtensionFieldTypeDef",
    "GetAccountSendingEnabledResponseTypeDef",
    "GetCustomVerificationEmailTemplateRequestRequestTypeDef",
    "GetCustomVerificationEmailTemplateResponseTypeDef",
    "GetIdentityDkimAttributesRequestRequestTypeDef",
    "GetIdentityDkimAttributesResponseTypeDef",
    "GetIdentityMailFromDomainAttributesRequestRequestTypeDef",
    "GetIdentityMailFromDomainAttributesResponseTypeDef",
    "GetIdentityNotificationAttributesRequestRequestTypeDef",
    "GetIdentityNotificationAttributesResponseTypeDef",
    "GetIdentityPoliciesRequestRequestTypeDef",
    "GetIdentityPoliciesResponseTypeDef",
    "GetIdentityVerificationAttributesRequestRequestTypeDef",
    "GetIdentityVerificationAttributesResponseTypeDef",
    "GetSendQuotaResponseTypeDef",
    "GetSendStatisticsResponseTypeDef",
    "GetTemplateRequestRequestTypeDef",
    "GetTemplateResponseTypeDef",
    "IdentityDkimAttributesTypeDef",
    "IdentityMailFromDomainAttributesTypeDef",
    "IdentityNotificationAttributesTypeDef",
    "IdentityVerificationAttributesTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "LambdaActionTypeDef",
    "ListConfigurationSetsRequestRequestTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "ListCustomVerificationEmailTemplatesRequestRequestTypeDef",
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    "ListIdentitiesRequestRequestTypeDef",
    "ListIdentitiesResponseTypeDef",
    "ListIdentityPoliciesRequestRequestTypeDef",
    "ListIdentityPoliciesResponseTypeDef",
    "ListReceiptFiltersResponseTypeDef",
    "ListReceiptRuleSetsRequestRequestTypeDef",
    "ListReceiptRuleSetsResponseTypeDef",
    "ListTemplatesRequestRequestTypeDef",
    "ListTemplatesResponseTypeDef",
    "ListVerifiedEmailAddressesResponseTypeDef",
    "MessageDsnTypeDef",
    "MessageTagTypeDef",
    "MessageTypeDef",
    "PaginatorConfigTypeDef",
    "PutConfigurationSetDeliveryOptionsRequestRequestTypeDef",
    "PutIdentityPolicyRequestRequestTypeDef",
    "RawMessageTypeDef",
    "ReceiptActionTypeDef",
    "ReceiptFilterTypeDef",
    "ReceiptIpFilterTypeDef",
    "ReceiptRuleSetMetadataTypeDef",
    "ReceiptRuleTypeDef",
    "RecipientDsnFieldsTypeDef",
    "ReorderReceiptRuleSetRequestRequestTypeDef",
    "ReputationOptionsTypeDef",
    "ResponseMetadataTypeDef",
    "S3ActionTypeDef",
    "SNSActionTypeDef",
    "SNSDestinationTypeDef",
    "SendBounceRequestRequestTypeDef",
    "SendBounceResponseTypeDef",
    "SendBulkTemplatedEmailRequestRequestTypeDef",
    "SendBulkTemplatedEmailResponseTypeDef",
    "SendCustomVerificationEmailRequestRequestTypeDef",
    "SendCustomVerificationEmailResponseTypeDef",
    "SendDataPointTypeDef",
    "SendEmailRequestRequestTypeDef",
    "SendEmailResponseTypeDef",
    "SendRawEmailRequestRequestTypeDef",
    "SendRawEmailResponseTypeDef",
    "SendTemplatedEmailRequestRequestTypeDef",
    "SendTemplatedEmailResponseTypeDef",
    "SetActiveReceiptRuleSetRequestRequestTypeDef",
    "SetIdentityDkimEnabledRequestRequestTypeDef",
    "SetIdentityFeedbackForwardingEnabledRequestRequestTypeDef",
    "SetIdentityHeadersInNotificationsEnabledRequestRequestTypeDef",
    "SetIdentityMailFromDomainRequestRequestTypeDef",
    "SetIdentityNotificationTopicRequestRequestTypeDef",
    "SetReceiptRulePositionRequestRequestTypeDef",
    "StopActionTypeDef",
    "TemplateMetadataTypeDef",
    "TemplateTypeDef",
    "TestRenderTemplateRequestRequestTypeDef",
    "TestRenderTemplateResponseTypeDef",
    "TrackingOptionsTypeDef",
    "UpdateAccountSendingEnabledRequestRequestTypeDef",
    "UpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    "UpdateConfigurationSetReputationMetricsEnabledRequestRequestTypeDef",
    "UpdateConfigurationSetSendingEnabledRequestRequestTypeDef",
    "UpdateConfigurationSetTrackingOptionsRequestRequestTypeDef",
    "UpdateCustomVerificationEmailTemplateRequestRequestTypeDef",
    "UpdateReceiptRuleRequestRequestTypeDef",
    "UpdateTemplateRequestRequestTypeDef",
    "VerifyDomainDkimRequestRequestTypeDef",
    "VerifyDomainDkimResponseTypeDef",
    "VerifyDomainIdentityRequestRequestTypeDef",
    "VerifyDomainIdentityResponseTypeDef",
    "VerifyEmailAddressRequestRequestTypeDef",
    "VerifyEmailIdentityRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "WorkmailActionTypeDef",
)

AddHeaderActionTypeDef = TypedDict(
    "AddHeaderActionTypeDef",
    {
        "HeaderName": str,
        "HeaderValue": str,
    },
)

BodyTypeDef = TypedDict(
    "BodyTypeDef",
    {
        "Text": NotRequired["ContentTypeDef"],
        "Html": NotRequired["ContentTypeDef"],
    },
)

BounceActionTypeDef = TypedDict(
    "BounceActionTypeDef",
    {
        "SmtpReplyCode": str,
        "Message": str,
        "Sender": str,
        "TopicArn": NotRequired[str],
        "StatusCode": NotRequired[str],
    },
)

BouncedRecipientInfoTypeDef = TypedDict(
    "BouncedRecipientInfoTypeDef",
    {
        "Recipient": str,
        "RecipientArn": NotRequired[str],
        "BounceType": NotRequired[BounceTypeType],
        "RecipientDsnFields": NotRequired["RecipientDsnFieldsTypeDef"],
    },
)

BulkEmailDestinationStatusTypeDef = TypedDict(
    "BulkEmailDestinationStatusTypeDef",
    {
        "Status": NotRequired[BulkEmailStatusType],
        "Error": NotRequired[str],
        "MessageId": NotRequired[str],
    },
)

BulkEmailDestinationTypeDef = TypedDict(
    "BulkEmailDestinationTypeDef",
    {
        "Destination": "DestinationTypeDef",
        "ReplacementTags": NotRequired[Sequence["MessageTagTypeDef"]],
        "ReplacementTemplateData": NotRequired[str],
    },
)

CloneReceiptRuleSetRequestRequestTypeDef = TypedDict(
    "CloneReceiptRuleSetRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "OriginalRuleSetName": str,
    },
)

CloudWatchDestinationTypeDef = TypedDict(
    "CloudWatchDestinationTypeDef",
    {
        "DimensionConfigurations": Sequence["CloudWatchDimensionConfigurationTypeDef"],
    },
)

CloudWatchDimensionConfigurationTypeDef = TypedDict(
    "CloudWatchDimensionConfigurationTypeDef",
    {
        "DimensionName": str,
        "DimensionValueSource": DimensionValueSourceType,
        "DefaultDimensionValue": str,
    },
)

ConfigurationSetTypeDef = TypedDict(
    "ConfigurationSetTypeDef",
    {
        "Name": str,
    },
)

ContentTypeDef = TypedDict(
    "ContentTypeDef",
    {
        "Data": str,
        "Charset": NotRequired[str],
    },
)

CreateConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "CreateConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestination": "EventDestinationTypeDef",
    },
)

CreateConfigurationSetRequestRequestTypeDef = TypedDict(
    "CreateConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSet": "ConfigurationSetTypeDef",
    },
)

CreateConfigurationSetTrackingOptionsRequestRequestTypeDef = TypedDict(
    "CreateConfigurationSetTrackingOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "TrackingOptions": "TrackingOptionsTypeDef",
    },
)

CreateCustomVerificationEmailTemplateRequestRequestTypeDef = TypedDict(
    "CreateCustomVerificationEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "TemplateContent": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
)

CreateReceiptFilterRequestRequestTypeDef = TypedDict(
    "CreateReceiptFilterRequestRequestTypeDef",
    {
        "Filter": "ReceiptFilterTypeDef",
    },
)

CreateReceiptRuleRequestRequestTypeDef = TypedDict(
    "CreateReceiptRuleRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "Rule": "ReceiptRuleTypeDef",
        "After": NotRequired[str],
    },
)

CreateReceiptRuleSetRequestRequestTypeDef = TypedDict(
    "CreateReceiptRuleSetRequestRequestTypeDef",
    {
        "RuleSetName": str,
    },
)

CreateTemplateRequestRequestTypeDef = TypedDict(
    "CreateTemplateRequestRequestTypeDef",
    {
        "Template": "TemplateTypeDef",
    },
)

CustomVerificationEmailTemplateTypeDef = TypedDict(
    "CustomVerificationEmailTemplateTypeDef",
    {
        "TemplateName": NotRequired[str],
        "FromEmailAddress": NotRequired[str],
        "TemplateSubject": NotRequired[str],
        "SuccessRedirectionURL": NotRequired[str],
        "FailureRedirectionURL": NotRequired[str],
    },
)

DeleteConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
    },
)

DeleteConfigurationSetRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

DeleteConfigurationSetTrackingOptionsRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationSetTrackingOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

DeleteCustomVerificationEmailTemplateRequestRequestTypeDef = TypedDict(
    "DeleteCustomVerificationEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)

DeleteIdentityPolicyRequestRequestTypeDef = TypedDict(
    "DeleteIdentityPolicyRequestRequestTypeDef",
    {
        "Identity": str,
        "PolicyName": str,
    },
)

DeleteIdentityRequestRequestTypeDef = TypedDict(
    "DeleteIdentityRequestRequestTypeDef",
    {
        "Identity": str,
    },
)

DeleteReceiptFilterRequestRequestTypeDef = TypedDict(
    "DeleteReceiptFilterRequestRequestTypeDef",
    {
        "FilterName": str,
    },
)

DeleteReceiptRuleRequestRequestTypeDef = TypedDict(
    "DeleteReceiptRuleRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "RuleName": str,
    },
)

DeleteReceiptRuleSetRequestRequestTypeDef = TypedDict(
    "DeleteReceiptRuleSetRequestRequestTypeDef",
    {
        "RuleSetName": str,
    },
)

DeleteTemplateRequestRequestTypeDef = TypedDict(
    "DeleteTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)

DeleteVerifiedEmailAddressRequestRequestTypeDef = TypedDict(
    "DeleteVerifiedEmailAddressRequestRequestTypeDef",
    {
        "EmailAddress": str,
    },
)

DeliveryOptionsTypeDef = TypedDict(
    "DeliveryOptionsTypeDef",
    {
        "TlsPolicy": NotRequired[TlsPolicyType],
    },
)

DescribeActiveReceiptRuleSetResponseTypeDef = TypedDict(
    "DescribeActiveReceiptRuleSetResponseTypeDef",
    {
        "Metadata": "ReceiptRuleSetMetadataTypeDef",
        "Rules": List["ReceiptRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationSetRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "ConfigurationSetAttributeNames": NotRequired[Sequence[ConfigurationSetAttributeType]],
    },
)

DescribeConfigurationSetResponseTypeDef = TypedDict(
    "DescribeConfigurationSetResponseTypeDef",
    {
        "ConfigurationSet": "ConfigurationSetTypeDef",
        "EventDestinations": List["EventDestinationTypeDef"],
        "TrackingOptions": "TrackingOptionsTypeDef",
        "DeliveryOptions": "DeliveryOptionsTypeDef",
        "ReputationOptions": "ReputationOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReceiptRuleRequestRequestTypeDef = TypedDict(
    "DescribeReceiptRuleRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "RuleName": str,
    },
)

DescribeReceiptRuleResponseTypeDef = TypedDict(
    "DescribeReceiptRuleResponseTypeDef",
    {
        "Rule": "ReceiptRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReceiptRuleSetRequestRequestTypeDef = TypedDict(
    "DescribeReceiptRuleSetRequestRequestTypeDef",
    {
        "RuleSetName": str,
    },
)

DescribeReceiptRuleSetResponseTypeDef = TypedDict(
    "DescribeReceiptRuleSetResponseTypeDef",
    {
        "Metadata": "ReceiptRuleSetMetadataTypeDef",
        "Rules": List["ReceiptRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "ToAddresses": NotRequired[Sequence[str]],
        "CcAddresses": NotRequired[Sequence[str]],
        "BccAddresses": NotRequired[Sequence[str]],
    },
)

EventDestinationTypeDef = TypedDict(
    "EventDestinationTypeDef",
    {
        "Name": str,
        "MatchingEventTypes": Sequence[EventTypeType],
        "Enabled": NotRequired[bool],
        "KinesisFirehoseDestination": NotRequired["KinesisFirehoseDestinationTypeDef"],
        "CloudWatchDestination": NotRequired["CloudWatchDestinationTypeDef"],
        "SNSDestination": NotRequired["SNSDestinationTypeDef"],
    },
)

ExtensionFieldTypeDef = TypedDict(
    "ExtensionFieldTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

GetAccountSendingEnabledResponseTypeDef = TypedDict(
    "GetAccountSendingEnabledResponseTypeDef",
    {
        "Enabled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCustomVerificationEmailTemplateRequestRequestTypeDef = TypedDict(
    "GetCustomVerificationEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)

GetCustomVerificationEmailTemplateResponseTypeDef = TypedDict(
    "GetCustomVerificationEmailTemplateResponseTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "TemplateContent": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityDkimAttributesRequestRequestTypeDef = TypedDict(
    "GetIdentityDkimAttributesRequestRequestTypeDef",
    {
        "Identities": Sequence[str],
    },
)

GetIdentityDkimAttributesResponseTypeDef = TypedDict(
    "GetIdentityDkimAttributesResponseTypeDef",
    {
        "DkimAttributes": Dict[str, "IdentityDkimAttributesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityMailFromDomainAttributesRequestRequestTypeDef = TypedDict(
    "GetIdentityMailFromDomainAttributesRequestRequestTypeDef",
    {
        "Identities": Sequence[str],
    },
)

GetIdentityMailFromDomainAttributesResponseTypeDef = TypedDict(
    "GetIdentityMailFromDomainAttributesResponseTypeDef",
    {
        "MailFromDomainAttributes": Dict[str, "IdentityMailFromDomainAttributesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityNotificationAttributesRequestRequestTypeDef = TypedDict(
    "GetIdentityNotificationAttributesRequestRequestTypeDef",
    {
        "Identities": Sequence[str],
    },
)

GetIdentityNotificationAttributesResponseTypeDef = TypedDict(
    "GetIdentityNotificationAttributesResponseTypeDef",
    {
        "NotificationAttributes": Dict[str, "IdentityNotificationAttributesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityPoliciesRequestRequestTypeDef = TypedDict(
    "GetIdentityPoliciesRequestRequestTypeDef",
    {
        "Identity": str,
        "PolicyNames": Sequence[str],
    },
)

GetIdentityPoliciesResponseTypeDef = TypedDict(
    "GetIdentityPoliciesResponseTypeDef",
    {
        "Policies": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityVerificationAttributesRequestRequestTypeDef = TypedDict(
    "GetIdentityVerificationAttributesRequestRequestTypeDef",
    {
        "Identities": Sequence[str],
    },
)

GetIdentityVerificationAttributesResponseTypeDef = TypedDict(
    "GetIdentityVerificationAttributesResponseTypeDef",
    {
        "VerificationAttributes": Dict[str, "IdentityVerificationAttributesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSendQuotaResponseTypeDef = TypedDict(
    "GetSendQuotaResponseTypeDef",
    {
        "Max24HourSend": float,
        "MaxSendRate": float,
        "SentLast24Hours": float,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSendStatisticsResponseTypeDef = TypedDict(
    "GetSendStatisticsResponseTypeDef",
    {
        "SendDataPoints": List["SendDataPointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTemplateRequestRequestTypeDef = TypedDict(
    "GetTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)

GetTemplateResponseTypeDef = TypedDict(
    "GetTemplateResponseTypeDef",
    {
        "Template": "TemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityDkimAttributesTypeDef = TypedDict(
    "IdentityDkimAttributesTypeDef",
    {
        "DkimEnabled": bool,
        "DkimVerificationStatus": VerificationStatusType,
        "DkimTokens": NotRequired[List[str]],
    },
)

IdentityMailFromDomainAttributesTypeDef = TypedDict(
    "IdentityMailFromDomainAttributesTypeDef",
    {
        "MailFromDomain": str,
        "MailFromDomainStatus": CustomMailFromStatusType,
        "BehaviorOnMXFailure": BehaviorOnMXFailureType,
    },
)

IdentityNotificationAttributesTypeDef = TypedDict(
    "IdentityNotificationAttributesTypeDef",
    {
        "BounceTopic": str,
        "ComplaintTopic": str,
        "DeliveryTopic": str,
        "ForwardingEnabled": bool,
        "HeadersInBounceNotificationsEnabled": NotRequired[bool],
        "HeadersInComplaintNotificationsEnabled": NotRequired[bool],
        "HeadersInDeliveryNotificationsEnabled": NotRequired[bool],
    },
)

IdentityVerificationAttributesTypeDef = TypedDict(
    "IdentityVerificationAttributesTypeDef",
    {
        "VerificationStatus": VerificationStatusType,
        "VerificationToken": NotRequired[str],
    },
)

KinesisFirehoseDestinationTypeDef = TypedDict(
    "KinesisFirehoseDestinationTypeDef",
    {
        "IAMRoleARN": str,
        "DeliveryStreamARN": str,
    },
)

LambdaActionTypeDef = TypedDict(
    "LambdaActionTypeDef",
    {
        "FunctionArn": str,
        "TopicArn": NotRequired[str],
        "InvocationType": NotRequired[InvocationTypeType],
    },
)

ListConfigurationSetsRequestRequestTypeDef = TypedDict(
    "ListConfigurationSetsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListConfigurationSetsResponseTypeDef = TypedDict(
    "ListConfigurationSetsResponseTypeDef",
    {
        "ConfigurationSets": List["ConfigurationSetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomVerificationEmailTemplatesRequestRequestTypeDef = TypedDict(
    "ListCustomVerificationEmailTemplatesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListCustomVerificationEmailTemplatesResponseTypeDef = TypedDict(
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    {
        "CustomVerificationEmailTemplates": List["CustomVerificationEmailTemplateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIdentitiesRequestRequestTypeDef = TypedDict(
    "ListIdentitiesRequestRequestTypeDef",
    {
        "IdentityType": NotRequired[IdentityTypeType],
        "NextToken": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListIdentitiesResponseTypeDef = TypedDict(
    "ListIdentitiesResponseTypeDef",
    {
        "Identities": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIdentityPoliciesRequestRequestTypeDef = TypedDict(
    "ListIdentityPoliciesRequestRequestTypeDef",
    {
        "Identity": str,
    },
)

ListIdentityPoliciesResponseTypeDef = TypedDict(
    "ListIdentityPoliciesResponseTypeDef",
    {
        "PolicyNames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReceiptFiltersResponseTypeDef = TypedDict(
    "ListReceiptFiltersResponseTypeDef",
    {
        "Filters": List["ReceiptFilterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReceiptRuleSetsRequestRequestTypeDef = TypedDict(
    "ListReceiptRuleSetsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)

ListReceiptRuleSetsResponseTypeDef = TypedDict(
    "ListReceiptRuleSetsResponseTypeDef",
    {
        "RuleSets": List["ReceiptRuleSetMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTemplatesRequestRequestTypeDef = TypedDict(
    "ListTemplatesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListTemplatesResponseTypeDef = TypedDict(
    "ListTemplatesResponseTypeDef",
    {
        "TemplatesMetadata": List["TemplateMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVerifiedEmailAddressesResponseTypeDef = TypedDict(
    "ListVerifiedEmailAddressesResponseTypeDef",
    {
        "VerifiedEmailAddresses": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MessageDsnTypeDef = TypedDict(
    "MessageDsnTypeDef",
    {
        "ReportingMta": str,
        "ArrivalDate": NotRequired[Union[datetime, str]],
        "ExtensionFields": NotRequired[Sequence["ExtensionFieldTypeDef"]],
    },
)

MessageTagTypeDef = TypedDict(
    "MessageTagTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "Subject": "ContentTypeDef",
        "Body": "BodyTypeDef",
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

PutConfigurationSetDeliveryOptionsRequestRequestTypeDef = TypedDict(
    "PutConfigurationSetDeliveryOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "DeliveryOptions": NotRequired["DeliveryOptionsTypeDef"],
    },
)

PutIdentityPolicyRequestRequestTypeDef = TypedDict(
    "PutIdentityPolicyRequestRequestTypeDef",
    {
        "Identity": str,
        "PolicyName": str,
        "Policy": str,
    },
)

RawMessageTypeDef = TypedDict(
    "RawMessageTypeDef",
    {
        "Data": Union[bytes, IO[bytes], StreamingBody],
    },
)

ReceiptActionTypeDef = TypedDict(
    "ReceiptActionTypeDef",
    {
        "S3Action": NotRequired["S3ActionTypeDef"],
        "BounceAction": NotRequired["BounceActionTypeDef"],
        "WorkmailAction": NotRequired["WorkmailActionTypeDef"],
        "LambdaAction": NotRequired["LambdaActionTypeDef"],
        "StopAction": NotRequired["StopActionTypeDef"],
        "AddHeaderAction": NotRequired["AddHeaderActionTypeDef"],
        "SNSAction": NotRequired["SNSActionTypeDef"],
    },
)

ReceiptFilterTypeDef = TypedDict(
    "ReceiptFilterTypeDef",
    {
        "Name": str,
        "IpFilter": "ReceiptIpFilterTypeDef",
    },
)

ReceiptIpFilterTypeDef = TypedDict(
    "ReceiptIpFilterTypeDef",
    {
        "Policy": ReceiptFilterPolicyType,
        "Cidr": str,
    },
)

ReceiptRuleSetMetadataTypeDef = TypedDict(
    "ReceiptRuleSetMetadataTypeDef",
    {
        "Name": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
    },
)

ReceiptRuleTypeDef = TypedDict(
    "ReceiptRuleTypeDef",
    {
        "Name": str,
        "Enabled": NotRequired[bool],
        "TlsPolicy": NotRequired[TlsPolicyType],
        "Recipients": NotRequired[Sequence[str]],
        "Actions": NotRequired[Sequence["ReceiptActionTypeDef"]],
        "ScanEnabled": NotRequired[bool],
    },
)

RecipientDsnFieldsTypeDef = TypedDict(
    "RecipientDsnFieldsTypeDef",
    {
        "Action": DsnActionType,
        "Status": str,
        "FinalRecipient": NotRequired[str],
        "RemoteMta": NotRequired[str],
        "DiagnosticCode": NotRequired[str],
        "LastAttemptDate": NotRequired[Union[datetime, str]],
        "ExtensionFields": NotRequired[Sequence["ExtensionFieldTypeDef"]],
    },
)

ReorderReceiptRuleSetRequestRequestTypeDef = TypedDict(
    "ReorderReceiptRuleSetRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "RuleNames": Sequence[str],
    },
)

ReputationOptionsTypeDef = TypedDict(
    "ReputationOptionsTypeDef",
    {
        "SendingEnabled": NotRequired[bool],
        "ReputationMetricsEnabled": NotRequired[bool],
        "LastFreshStart": NotRequired[datetime],
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

S3ActionTypeDef = TypedDict(
    "S3ActionTypeDef",
    {
        "BucketName": str,
        "TopicArn": NotRequired[str],
        "ObjectKeyPrefix": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
    },
)

SNSActionTypeDef = TypedDict(
    "SNSActionTypeDef",
    {
        "TopicArn": str,
        "Encoding": NotRequired[SNSActionEncodingType],
    },
)

SNSDestinationTypeDef = TypedDict(
    "SNSDestinationTypeDef",
    {
        "TopicARN": str,
    },
)

SendBounceRequestRequestTypeDef = TypedDict(
    "SendBounceRequestRequestTypeDef",
    {
        "OriginalMessageId": str,
        "BounceSender": str,
        "BouncedRecipientInfoList": Sequence["BouncedRecipientInfoTypeDef"],
        "Explanation": NotRequired[str],
        "MessageDsn": NotRequired["MessageDsnTypeDef"],
        "BounceSenderArn": NotRequired[str],
    },
)

SendBounceResponseTypeDef = TypedDict(
    "SendBounceResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SendBulkTemplatedEmailRequestRequestTypeDef = TypedDict(
    "SendBulkTemplatedEmailRequestRequestTypeDef",
    {
        "Source": str,
        "Template": str,
        "Destinations": Sequence["BulkEmailDestinationTypeDef"],
        "SourceArn": NotRequired[str],
        "ReplyToAddresses": NotRequired[Sequence[str]],
        "ReturnPath": NotRequired[str],
        "ReturnPathArn": NotRequired[str],
        "ConfigurationSetName": NotRequired[str],
        "DefaultTags": NotRequired[Sequence["MessageTagTypeDef"]],
        "TemplateArn": NotRequired[str],
        "DefaultTemplateData": NotRequired[str],
    },
)

SendBulkTemplatedEmailResponseTypeDef = TypedDict(
    "SendBulkTemplatedEmailResponseTypeDef",
    {
        "Status": List["BulkEmailDestinationStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SendCustomVerificationEmailRequestRequestTypeDef = TypedDict(
    "SendCustomVerificationEmailRequestRequestTypeDef",
    {
        "EmailAddress": str,
        "TemplateName": str,
        "ConfigurationSetName": NotRequired[str],
    },
)

SendCustomVerificationEmailResponseTypeDef = TypedDict(
    "SendCustomVerificationEmailResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SendDataPointTypeDef = TypedDict(
    "SendDataPointTypeDef",
    {
        "Timestamp": NotRequired[datetime],
        "DeliveryAttempts": NotRequired[int],
        "Bounces": NotRequired[int],
        "Complaints": NotRequired[int],
        "Rejects": NotRequired[int],
    },
)

SendEmailRequestRequestTypeDef = TypedDict(
    "SendEmailRequestRequestTypeDef",
    {
        "Source": str,
        "Destination": "DestinationTypeDef",
        "Message": "MessageTypeDef",
        "ReplyToAddresses": NotRequired[Sequence[str]],
        "ReturnPath": NotRequired[str],
        "SourceArn": NotRequired[str],
        "ReturnPathArn": NotRequired[str],
        "Tags": NotRequired[Sequence["MessageTagTypeDef"]],
        "ConfigurationSetName": NotRequired[str],
    },
)

SendEmailResponseTypeDef = TypedDict(
    "SendEmailResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SendRawEmailRequestRequestTypeDef = TypedDict(
    "SendRawEmailRequestRequestTypeDef",
    {
        "RawMessage": "RawMessageTypeDef",
        "Source": NotRequired[str],
        "Destinations": NotRequired[Sequence[str]],
        "FromArn": NotRequired[str],
        "SourceArn": NotRequired[str],
        "ReturnPathArn": NotRequired[str],
        "Tags": NotRequired[Sequence["MessageTagTypeDef"]],
        "ConfigurationSetName": NotRequired[str],
    },
)

SendRawEmailResponseTypeDef = TypedDict(
    "SendRawEmailResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SendTemplatedEmailRequestRequestTypeDef = TypedDict(
    "SendTemplatedEmailRequestRequestTypeDef",
    {
        "Source": str,
        "Destination": "DestinationTypeDef",
        "Template": str,
        "TemplateData": str,
        "ReplyToAddresses": NotRequired[Sequence[str]],
        "ReturnPath": NotRequired[str],
        "SourceArn": NotRequired[str],
        "ReturnPathArn": NotRequired[str],
        "Tags": NotRequired[Sequence["MessageTagTypeDef"]],
        "ConfigurationSetName": NotRequired[str],
        "TemplateArn": NotRequired[str],
    },
)

SendTemplatedEmailResponseTypeDef = TypedDict(
    "SendTemplatedEmailResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetActiveReceiptRuleSetRequestRequestTypeDef = TypedDict(
    "SetActiveReceiptRuleSetRequestRequestTypeDef",
    {
        "RuleSetName": NotRequired[str],
    },
)

SetIdentityDkimEnabledRequestRequestTypeDef = TypedDict(
    "SetIdentityDkimEnabledRequestRequestTypeDef",
    {
        "Identity": str,
        "DkimEnabled": bool,
    },
)

SetIdentityFeedbackForwardingEnabledRequestRequestTypeDef = TypedDict(
    "SetIdentityFeedbackForwardingEnabledRequestRequestTypeDef",
    {
        "Identity": str,
        "ForwardingEnabled": bool,
    },
)

SetIdentityHeadersInNotificationsEnabledRequestRequestTypeDef = TypedDict(
    "SetIdentityHeadersInNotificationsEnabledRequestRequestTypeDef",
    {
        "Identity": str,
        "NotificationType": NotificationTypeType,
        "Enabled": bool,
    },
)

SetIdentityMailFromDomainRequestRequestTypeDef = TypedDict(
    "SetIdentityMailFromDomainRequestRequestTypeDef",
    {
        "Identity": str,
        "MailFromDomain": NotRequired[str],
        "BehaviorOnMXFailure": NotRequired[BehaviorOnMXFailureType],
    },
)

SetIdentityNotificationTopicRequestRequestTypeDef = TypedDict(
    "SetIdentityNotificationTopicRequestRequestTypeDef",
    {
        "Identity": str,
        "NotificationType": NotificationTypeType,
        "SnsTopic": NotRequired[str],
    },
)

SetReceiptRulePositionRequestRequestTypeDef = TypedDict(
    "SetReceiptRulePositionRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "RuleName": str,
        "After": NotRequired[str],
    },
)

StopActionTypeDef = TypedDict(
    "StopActionTypeDef",
    {
        "Scope": Literal["RuleSet"],
        "TopicArn": NotRequired[str],
    },
)

TemplateMetadataTypeDef = TypedDict(
    "TemplateMetadataTypeDef",
    {
        "Name": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
    },
)

TemplateTypeDef = TypedDict(
    "TemplateTypeDef",
    {
        "TemplateName": str,
        "SubjectPart": NotRequired[str],
        "TextPart": NotRequired[str],
        "HtmlPart": NotRequired[str],
    },
)

TestRenderTemplateRequestRequestTypeDef = TypedDict(
    "TestRenderTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "TemplateData": str,
    },
)

TestRenderTemplateResponseTypeDef = TypedDict(
    "TestRenderTemplateResponseTypeDef",
    {
        "RenderedTemplate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TrackingOptionsTypeDef = TypedDict(
    "TrackingOptionsTypeDef",
    {
        "CustomRedirectDomain": NotRequired[str],
    },
)

UpdateAccountSendingEnabledRequestRequestTypeDef = TypedDict(
    "UpdateAccountSendingEnabledRequestRequestTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)

UpdateConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestination": "EventDestinationTypeDef",
    },
)

UpdateConfigurationSetReputationMetricsEnabledRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationSetReputationMetricsEnabledRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "Enabled": bool,
    },
)

UpdateConfigurationSetSendingEnabledRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationSetSendingEnabledRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "Enabled": bool,
    },
)

UpdateConfigurationSetTrackingOptionsRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationSetTrackingOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "TrackingOptions": "TrackingOptionsTypeDef",
    },
)

UpdateCustomVerificationEmailTemplateRequestRequestTypeDef = TypedDict(
    "UpdateCustomVerificationEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": NotRequired[str],
        "TemplateSubject": NotRequired[str],
        "TemplateContent": NotRequired[str],
        "SuccessRedirectionURL": NotRequired[str],
        "FailureRedirectionURL": NotRequired[str],
    },
)

UpdateReceiptRuleRequestRequestTypeDef = TypedDict(
    "UpdateReceiptRuleRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "Rule": "ReceiptRuleTypeDef",
    },
)

UpdateTemplateRequestRequestTypeDef = TypedDict(
    "UpdateTemplateRequestRequestTypeDef",
    {
        "Template": "TemplateTypeDef",
    },
)

VerifyDomainDkimRequestRequestTypeDef = TypedDict(
    "VerifyDomainDkimRequestRequestTypeDef",
    {
        "Domain": str,
    },
)

VerifyDomainDkimResponseTypeDef = TypedDict(
    "VerifyDomainDkimResponseTypeDef",
    {
        "DkimTokens": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VerifyDomainIdentityRequestRequestTypeDef = TypedDict(
    "VerifyDomainIdentityRequestRequestTypeDef",
    {
        "Domain": str,
    },
)

VerifyDomainIdentityResponseTypeDef = TypedDict(
    "VerifyDomainIdentityResponseTypeDef",
    {
        "VerificationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VerifyEmailAddressRequestRequestTypeDef = TypedDict(
    "VerifyEmailAddressRequestRequestTypeDef",
    {
        "EmailAddress": str,
    },
)

VerifyEmailIdentityRequestRequestTypeDef = TypedDict(
    "VerifyEmailIdentityRequestRequestTypeDef",
    {
        "EmailAddress": str,
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)

WorkmailActionTypeDef = TypedDict(
    "WorkmailActionTypeDef",
    {
        "OrganizationArn": str,
        "TopicArn": NotRequired[str],
    },
)
