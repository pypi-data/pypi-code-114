"""
Type annotations for sesv2 service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sesv2/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_sesv2.type_defs import AccountDetailsTypeDef

    data: AccountDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    BehaviorOnMxFailureType,
    BulkEmailStatusType,
    ContactLanguageType,
    ContactListImportActionType,
    DataFormatType,
    DeliverabilityDashboardAccountStatusType,
    DeliverabilityTestStatusType,
    DimensionValueSourceType,
    DkimSigningAttributesOriginType,
    DkimSigningKeyLengthType,
    DkimStatusType,
    EventTypeType,
    IdentityTypeType,
    ImportDestinationTypeType,
    JobStatusType,
    MailFromDomainStatusType,
    MailTypeType,
    ReviewStatusType,
    SubscriptionStatusType,
    SuppressionListImportActionType,
    SuppressionListReasonType,
    TlsPolicyType,
    WarmupStatusType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountDetailsTypeDef",
    "BlacklistEntryTypeDef",
    "BodyTypeDef",
    "BulkEmailContentTypeDef",
    "BulkEmailEntryResultTypeDef",
    "BulkEmailEntryTypeDef",
    "CloudWatchDestinationTypeDef",
    "CloudWatchDimensionConfigurationTypeDef",
    "ContactListDestinationTypeDef",
    "ContactListTypeDef",
    "ContactTypeDef",
    "ContentTypeDef",
    "CreateConfigurationSetEventDestinationRequestRequestTypeDef",
    "CreateConfigurationSetRequestRequestTypeDef",
    "CreateContactListRequestRequestTypeDef",
    "CreateContactRequestRequestTypeDef",
    "CreateCustomVerificationEmailTemplateRequestRequestTypeDef",
    "CreateDedicatedIpPoolRequestRequestTypeDef",
    "CreateDeliverabilityTestReportRequestRequestTypeDef",
    "CreateDeliverabilityTestReportResponseTypeDef",
    "CreateEmailIdentityPolicyRequestRequestTypeDef",
    "CreateEmailIdentityRequestRequestTypeDef",
    "CreateEmailIdentityResponseTypeDef",
    "CreateEmailTemplateRequestRequestTypeDef",
    "CreateImportJobRequestRequestTypeDef",
    "CreateImportJobResponseTypeDef",
    "CustomVerificationEmailTemplateMetadataTypeDef",
    "DailyVolumeTypeDef",
    "DedicatedIpTypeDef",
    "DeleteConfigurationSetEventDestinationRequestRequestTypeDef",
    "DeleteConfigurationSetRequestRequestTypeDef",
    "DeleteContactListRequestRequestTypeDef",
    "DeleteContactRequestRequestTypeDef",
    "DeleteCustomVerificationEmailTemplateRequestRequestTypeDef",
    "DeleteDedicatedIpPoolRequestRequestTypeDef",
    "DeleteEmailIdentityPolicyRequestRequestTypeDef",
    "DeleteEmailIdentityRequestRequestTypeDef",
    "DeleteEmailTemplateRequestRequestTypeDef",
    "DeleteSuppressedDestinationRequestRequestTypeDef",
    "DeliverabilityTestReportTypeDef",
    "DeliveryOptionsTypeDef",
    "DestinationTypeDef",
    "DkimAttributesTypeDef",
    "DkimSigningAttributesTypeDef",
    "DomainDeliverabilityCampaignTypeDef",
    "DomainDeliverabilityTrackingOptionTypeDef",
    "DomainIspPlacementTypeDef",
    "EmailContentTypeDef",
    "EmailTemplateContentTypeDef",
    "EmailTemplateMetadataTypeDef",
    "EventDestinationDefinitionTypeDef",
    "EventDestinationTypeDef",
    "FailureInfoTypeDef",
    "GetAccountResponseTypeDef",
    "GetBlacklistReportsRequestRequestTypeDef",
    "GetBlacklistReportsResponseTypeDef",
    "GetConfigurationSetEventDestinationsRequestRequestTypeDef",
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    "GetConfigurationSetRequestRequestTypeDef",
    "GetConfigurationSetResponseTypeDef",
    "GetContactListRequestRequestTypeDef",
    "GetContactListResponseTypeDef",
    "GetContactRequestRequestTypeDef",
    "GetContactResponseTypeDef",
    "GetCustomVerificationEmailTemplateRequestRequestTypeDef",
    "GetCustomVerificationEmailTemplateResponseTypeDef",
    "GetDedicatedIpRequestRequestTypeDef",
    "GetDedicatedIpResponseTypeDef",
    "GetDedicatedIpsRequestRequestTypeDef",
    "GetDedicatedIpsResponseTypeDef",
    "GetDeliverabilityDashboardOptionsResponseTypeDef",
    "GetDeliverabilityTestReportRequestRequestTypeDef",
    "GetDeliverabilityTestReportResponseTypeDef",
    "GetDomainDeliverabilityCampaignRequestRequestTypeDef",
    "GetDomainDeliverabilityCampaignResponseTypeDef",
    "GetDomainStatisticsReportRequestRequestTypeDef",
    "GetDomainStatisticsReportResponseTypeDef",
    "GetEmailIdentityPoliciesRequestRequestTypeDef",
    "GetEmailIdentityPoliciesResponseTypeDef",
    "GetEmailIdentityRequestRequestTypeDef",
    "GetEmailIdentityResponseTypeDef",
    "GetEmailTemplateRequestRequestTypeDef",
    "GetEmailTemplateResponseTypeDef",
    "GetImportJobRequestRequestTypeDef",
    "GetImportJobResponseTypeDef",
    "GetSuppressedDestinationRequestRequestTypeDef",
    "GetSuppressedDestinationResponseTypeDef",
    "IdentityInfoTypeDef",
    "ImportDataSourceTypeDef",
    "ImportDestinationTypeDef",
    "ImportJobSummaryTypeDef",
    "InboxPlacementTrackingOptionTypeDef",
    "IspPlacementTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "ListConfigurationSetsRequestRequestTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "ListContactListsRequestRequestTypeDef",
    "ListContactListsResponseTypeDef",
    "ListContactsFilterTypeDef",
    "ListContactsRequestRequestTypeDef",
    "ListContactsResponseTypeDef",
    "ListCustomVerificationEmailTemplatesRequestRequestTypeDef",
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    "ListDedicatedIpPoolsRequestRequestTypeDef",
    "ListDedicatedIpPoolsResponseTypeDef",
    "ListDeliverabilityTestReportsRequestRequestTypeDef",
    "ListDeliverabilityTestReportsResponseTypeDef",
    "ListDomainDeliverabilityCampaignsRequestRequestTypeDef",
    "ListDomainDeliverabilityCampaignsResponseTypeDef",
    "ListEmailIdentitiesRequestRequestTypeDef",
    "ListEmailIdentitiesResponseTypeDef",
    "ListEmailTemplatesRequestRequestTypeDef",
    "ListEmailTemplatesResponseTypeDef",
    "ListImportJobsRequestRequestTypeDef",
    "ListImportJobsResponseTypeDef",
    "ListManagementOptionsTypeDef",
    "ListSuppressedDestinationsRequestRequestTypeDef",
    "ListSuppressedDestinationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MailFromAttributesTypeDef",
    "MessageTagTypeDef",
    "MessageTypeDef",
    "OverallVolumeTypeDef",
    "PinpointDestinationTypeDef",
    "PlacementStatisticsTypeDef",
    "PutAccountDedicatedIpWarmupAttributesRequestRequestTypeDef",
    "PutAccountDetailsRequestRequestTypeDef",
    "PutAccountSendingAttributesRequestRequestTypeDef",
    "PutAccountSuppressionAttributesRequestRequestTypeDef",
    "PutConfigurationSetDeliveryOptionsRequestRequestTypeDef",
    "PutConfigurationSetReputationOptionsRequestRequestTypeDef",
    "PutConfigurationSetSendingOptionsRequestRequestTypeDef",
    "PutConfigurationSetSuppressionOptionsRequestRequestTypeDef",
    "PutConfigurationSetTrackingOptionsRequestRequestTypeDef",
    "PutDedicatedIpInPoolRequestRequestTypeDef",
    "PutDedicatedIpWarmupAttributesRequestRequestTypeDef",
    "PutDeliverabilityDashboardOptionRequestRequestTypeDef",
    "PutEmailIdentityConfigurationSetAttributesRequestRequestTypeDef",
    "PutEmailIdentityDkimAttributesRequestRequestTypeDef",
    "PutEmailIdentityDkimSigningAttributesRequestRequestTypeDef",
    "PutEmailIdentityDkimSigningAttributesResponseTypeDef",
    "PutEmailIdentityFeedbackAttributesRequestRequestTypeDef",
    "PutEmailIdentityMailFromAttributesRequestRequestTypeDef",
    "PutSuppressedDestinationRequestRequestTypeDef",
    "RawMessageTypeDef",
    "ReplacementEmailContentTypeDef",
    "ReplacementTemplateTypeDef",
    "ReputationOptionsTypeDef",
    "ResponseMetadataTypeDef",
    "ReviewDetailsTypeDef",
    "SendBulkEmailRequestRequestTypeDef",
    "SendBulkEmailResponseTypeDef",
    "SendCustomVerificationEmailRequestRequestTypeDef",
    "SendCustomVerificationEmailResponseTypeDef",
    "SendEmailRequestRequestTypeDef",
    "SendEmailResponseTypeDef",
    "SendQuotaTypeDef",
    "SendingOptionsTypeDef",
    "SnsDestinationTypeDef",
    "SuppressedDestinationAttributesTypeDef",
    "SuppressedDestinationSummaryTypeDef",
    "SuppressedDestinationTypeDef",
    "SuppressionAttributesTypeDef",
    "SuppressionListDestinationTypeDef",
    "SuppressionOptionsTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TemplateTypeDef",
    "TestRenderEmailTemplateRequestRequestTypeDef",
    "TestRenderEmailTemplateResponseTypeDef",
    "TopicFilterTypeDef",
    "TopicPreferenceTypeDef",
    "TopicTypeDef",
    "TrackingOptionsTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    "UpdateContactListRequestRequestTypeDef",
    "UpdateContactRequestRequestTypeDef",
    "UpdateCustomVerificationEmailTemplateRequestRequestTypeDef",
    "UpdateEmailIdentityPolicyRequestRequestTypeDef",
    "UpdateEmailTemplateRequestRequestTypeDef",
    "VolumeStatisticsTypeDef",
)

AccountDetailsTypeDef = TypedDict(
    "AccountDetailsTypeDef",
    {
        "MailType": NotRequired[MailTypeType],
        "WebsiteURL": NotRequired[str],
        "ContactLanguage": NotRequired[ContactLanguageType],
        "UseCaseDescription": NotRequired[str],
        "AdditionalContactEmailAddresses": NotRequired[List[str]],
        "ReviewDetails": NotRequired["ReviewDetailsTypeDef"],
    },
)

BlacklistEntryTypeDef = TypedDict(
    "BlacklistEntryTypeDef",
    {
        "RblName": NotRequired[str],
        "ListingTime": NotRequired[datetime],
        "Description": NotRequired[str],
    },
)

BodyTypeDef = TypedDict(
    "BodyTypeDef",
    {
        "Text": NotRequired["ContentTypeDef"],
        "Html": NotRequired["ContentTypeDef"],
    },
)

BulkEmailContentTypeDef = TypedDict(
    "BulkEmailContentTypeDef",
    {
        "Template": NotRequired["TemplateTypeDef"],
    },
)

BulkEmailEntryResultTypeDef = TypedDict(
    "BulkEmailEntryResultTypeDef",
    {
        "Status": NotRequired[BulkEmailStatusType],
        "Error": NotRequired[str],
        "MessageId": NotRequired[str],
    },
)

BulkEmailEntryTypeDef = TypedDict(
    "BulkEmailEntryTypeDef",
    {
        "Destination": "DestinationTypeDef",
        "ReplacementTags": NotRequired[Sequence["MessageTagTypeDef"]],
        "ReplacementEmailContent": NotRequired["ReplacementEmailContentTypeDef"],
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

ContactListDestinationTypeDef = TypedDict(
    "ContactListDestinationTypeDef",
    {
        "ContactListName": str,
        "ContactListImportAction": ContactListImportActionType,
    },
)

ContactListTypeDef = TypedDict(
    "ContactListTypeDef",
    {
        "ContactListName": NotRequired[str],
        "LastUpdatedTimestamp": NotRequired[datetime],
    },
)

ContactTypeDef = TypedDict(
    "ContactTypeDef",
    {
        "EmailAddress": NotRequired[str],
        "TopicPreferences": NotRequired[List["TopicPreferenceTypeDef"]],
        "TopicDefaultPreferences": NotRequired[List["TopicPreferenceTypeDef"]],
        "UnsubscribeAll": NotRequired[bool],
        "LastUpdatedTimestamp": NotRequired[datetime],
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
        "EventDestinationName": str,
        "EventDestination": "EventDestinationDefinitionTypeDef",
    },
)

CreateConfigurationSetRequestRequestTypeDef = TypedDict(
    "CreateConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "TrackingOptions": NotRequired["TrackingOptionsTypeDef"],
        "DeliveryOptions": NotRequired["DeliveryOptionsTypeDef"],
        "ReputationOptions": NotRequired["ReputationOptionsTypeDef"],
        "SendingOptions": NotRequired["SendingOptionsTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "SuppressionOptions": NotRequired["SuppressionOptionsTypeDef"],
    },
)

CreateContactListRequestRequestTypeDef = TypedDict(
    "CreateContactListRequestRequestTypeDef",
    {
        "ContactListName": str,
        "Topics": NotRequired[Sequence["TopicTypeDef"]],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateContactRequestRequestTypeDef = TypedDict(
    "CreateContactRequestRequestTypeDef",
    {
        "ContactListName": str,
        "EmailAddress": str,
        "TopicPreferences": NotRequired[Sequence["TopicPreferenceTypeDef"]],
        "UnsubscribeAll": NotRequired[bool],
        "AttributesData": NotRequired[str],
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

CreateDedicatedIpPoolRequestRequestTypeDef = TypedDict(
    "CreateDedicatedIpPoolRequestRequestTypeDef",
    {
        "PoolName": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDeliverabilityTestReportRequestRequestTypeDef = TypedDict(
    "CreateDeliverabilityTestReportRequestRequestTypeDef",
    {
        "FromEmailAddress": str,
        "Content": "EmailContentTypeDef",
        "ReportName": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDeliverabilityTestReportResponseTypeDef = TypedDict(
    "CreateDeliverabilityTestReportResponseTypeDef",
    {
        "ReportId": str,
        "DeliverabilityTestStatus": DeliverabilityTestStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEmailIdentityPolicyRequestRequestTypeDef = TypedDict(
    "CreateEmailIdentityPolicyRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "PolicyName": str,
        "Policy": str,
    },
)

CreateEmailIdentityRequestRequestTypeDef = TypedDict(
    "CreateEmailIdentityRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "DkimSigningAttributes": NotRequired["DkimSigningAttributesTypeDef"],
        "ConfigurationSetName": NotRequired[str],
    },
)

CreateEmailIdentityResponseTypeDef = TypedDict(
    "CreateEmailIdentityResponseTypeDef",
    {
        "IdentityType": IdentityTypeType,
        "VerifiedForSendingStatus": bool,
        "DkimAttributes": "DkimAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEmailTemplateRequestRequestTypeDef = TypedDict(
    "CreateEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "TemplateContent": "EmailTemplateContentTypeDef",
    },
)

CreateImportJobRequestRequestTypeDef = TypedDict(
    "CreateImportJobRequestRequestTypeDef",
    {
        "ImportDestination": "ImportDestinationTypeDef",
        "ImportDataSource": "ImportDataSourceTypeDef",
    },
)

CreateImportJobResponseTypeDef = TypedDict(
    "CreateImportJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomVerificationEmailTemplateMetadataTypeDef = TypedDict(
    "CustomVerificationEmailTemplateMetadataTypeDef",
    {
        "TemplateName": NotRequired[str],
        "FromEmailAddress": NotRequired[str],
        "TemplateSubject": NotRequired[str],
        "SuccessRedirectionURL": NotRequired[str],
        "FailureRedirectionURL": NotRequired[str],
    },
)

DailyVolumeTypeDef = TypedDict(
    "DailyVolumeTypeDef",
    {
        "StartDate": NotRequired[datetime],
        "VolumeStatistics": NotRequired["VolumeStatisticsTypeDef"],
        "DomainIspPlacements": NotRequired[List["DomainIspPlacementTypeDef"]],
    },
)

DedicatedIpTypeDef = TypedDict(
    "DedicatedIpTypeDef",
    {
        "Ip": str,
        "WarmupStatus": WarmupStatusType,
        "WarmupPercentage": int,
        "PoolName": NotRequired[str],
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

DeleteContactListRequestRequestTypeDef = TypedDict(
    "DeleteContactListRequestRequestTypeDef",
    {
        "ContactListName": str,
    },
)

DeleteContactRequestRequestTypeDef = TypedDict(
    "DeleteContactRequestRequestTypeDef",
    {
        "ContactListName": str,
        "EmailAddress": str,
    },
)

DeleteCustomVerificationEmailTemplateRequestRequestTypeDef = TypedDict(
    "DeleteCustomVerificationEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)

DeleteDedicatedIpPoolRequestRequestTypeDef = TypedDict(
    "DeleteDedicatedIpPoolRequestRequestTypeDef",
    {
        "PoolName": str,
    },
)

DeleteEmailIdentityPolicyRequestRequestTypeDef = TypedDict(
    "DeleteEmailIdentityPolicyRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "PolicyName": str,
    },
)

DeleteEmailIdentityRequestRequestTypeDef = TypedDict(
    "DeleteEmailIdentityRequestRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)

DeleteEmailTemplateRequestRequestTypeDef = TypedDict(
    "DeleteEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)

DeleteSuppressedDestinationRequestRequestTypeDef = TypedDict(
    "DeleteSuppressedDestinationRequestRequestTypeDef",
    {
        "EmailAddress": str,
    },
)

DeliverabilityTestReportTypeDef = TypedDict(
    "DeliverabilityTestReportTypeDef",
    {
        "ReportId": NotRequired[str],
        "ReportName": NotRequired[str],
        "Subject": NotRequired[str],
        "FromEmailAddress": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "DeliverabilityTestStatus": NotRequired[DeliverabilityTestStatusType],
    },
)

DeliveryOptionsTypeDef = TypedDict(
    "DeliveryOptionsTypeDef",
    {
        "TlsPolicy": NotRequired[TlsPolicyType],
        "SendingPoolName": NotRequired[str],
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

DkimAttributesTypeDef = TypedDict(
    "DkimAttributesTypeDef",
    {
        "SigningEnabled": NotRequired[bool],
        "Status": NotRequired[DkimStatusType],
        "Tokens": NotRequired[List[str]],
        "SigningAttributesOrigin": NotRequired[DkimSigningAttributesOriginType],
        "NextSigningKeyLength": NotRequired[DkimSigningKeyLengthType],
        "CurrentSigningKeyLength": NotRequired[DkimSigningKeyLengthType],
        "LastKeyGenerationTimestamp": NotRequired[datetime],
    },
)

DkimSigningAttributesTypeDef = TypedDict(
    "DkimSigningAttributesTypeDef",
    {
        "DomainSigningSelector": NotRequired[str],
        "DomainSigningPrivateKey": NotRequired[str],
        "NextSigningKeyLength": NotRequired[DkimSigningKeyLengthType],
    },
)

DomainDeliverabilityCampaignTypeDef = TypedDict(
    "DomainDeliverabilityCampaignTypeDef",
    {
        "CampaignId": NotRequired[str],
        "ImageUrl": NotRequired[str],
        "Subject": NotRequired[str],
        "FromAddress": NotRequired[str],
        "SendingIps": NotRequired[List[str]],
        "FirstSeenDateTime": NotRequired[datetime],
        "LastSeenDateTime": NotRequired[datetime],
        "InboxCount": NotRequired[int],
        "SpamCount": NotRequired[int],
        "ReadRate": NotRequired[float],
        "DeleteRate": NotRequired[float],
        "ReadDeleteRate": NotRequired[float],
        "ProjectedVolume": NotRequired[int],
        "Esps": NotRequired[List[str]],
    },
)

DomainDeliverabilityTrackingOptionTypeDef = TypedDict(
    "DomainDeliverabilityTrackingOptionTypeDef",
    {
        "Domain": NotRequired[str],
        "SubscriptionStartDate": NotRequired[datetime],
        "InboxPlacementTrackingOption": NotRequired["InboxPlacementTrackingOptionTypeDef"],
    },
)

DomainIspPlacementTypeDef = TypedDict(
    "DomainIspPlacementTypeDef",
    {
        "IspName": NotRequired[str],
        "InboxRawCount": NotRequired[int],
        "SpamRawCount": NotRequired[int],
        "InboxPercentage": NotRequired[float],
        "SpamPercentage": NotRequired[float],
    },
)

EmailContentTypeDef = TypedDict(
    "EmailContentTypeDef",
    {
        "Simple": NotRequired["MessageTypeDef"],
        "Raw": NotRequired["RawMessageTypeDef"],
        "Template": NotRequired["TemplateTypeDef"],
    },
)

EmailTemplateContentTypeDef = TypedDict(
    "EmailTemplateContentTypeDef",
    {
        "Subject": NotRequired[str],
        "Text": NotRequired[str],
        "Html": NotRequired[str],
    },
)

EmailTemplateMetadataTypeDef = TypedDict(
    "EmailTemplateMetadataTypeDef",
    {
        "TemplateName": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
    },
)

EventDestinationDefinitionTypeDef = TypedDict(
    "EventDestinationDefinitionTypeDef",
    {
        "Enabled": NotRequired[bool],
        "MatchingEventTypes": NotRequired[Sequence[EventTypeType]],
        "KinesisFirehoseDestination": NotRequired["KinesisFirehoseDestinationTypeDef"],
        "CloudWatchDestination": NotRequired["CloudWatchDestinationTypeDef"],
        "SnsDestination": NotRequired["SnsDestinationTypeDef"],
        "PinpointDestination": NotRequired["PinpointDestinationTypeDef"],
    },
)

EventDestinationTypeDef = TypedDict(
    "EventDestinationTypeDef",
    {
        "Name": str,
        "MatchingEventTypes": List[EventTypeType],
        "Enabled": NotRequired[bool],
        "KinesisFirehoseDestination": NotRequired["KinesisFirehoseDestinationTypeDef"],
        "CloudWatchDestination": NotRequired["CloudWatchDestinationTypeDef"],
        "SnsDestination": NotRequired["SnsDestinationTypeDef"],
        "PinpointDestination": NotRequired["PinpointDestinationTypeDef"],
    },
)

FailureInfoTypeDef = TypedDict(
    "FailureInfoTypeDef",
    {
        "FailedRecordsS3Url": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

GetAccountResponseTypeDef = TypedDict(
    "GetAccountResponseTypeDef",
    {
        "DedicatedIpAutoWarmupEnabled": bool,
        "EnforcementStatus": str,
        "ProductionAccessEnabled": bool,
        "SendQuota": "SendQuotaTypeDef",
        "SendingEnabled": bool,
        "SuppressionAttributes": "SuppressionAttributesTypeDef",
        "Details": "AccountDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBlacklistReportsRequestRequestTypeDef = TypedDict(
    "GetBlacklistReportsRequestRequestTypeDef",
    {
        "BlacklistItemNames": Sequence[str],
    },
)

GetBlacklistReportsResponseTypeDef = TypedDict(
    "GetBlacklistReportsResponseTypeDef",
    {
        "BlacklistReport": Dict[str, List["BlacklistEntryTypeDef"]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConfigurationSetEventDestinationsRequestRequestTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

GetConfigurationSetEventDestinationsResponseTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    {
        "EventDestinations": List["EventDestinationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConfigurationSetRequestRequestTypeDef = TypedDict(
    "GetConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

GetConfigurationSetResponseTypeDef = TypedDict(
    "GetConfigurationSetResponseTypeDef",
    {
        "ConfigurationSetName": str,
        "TrackingOptions": "TrackingOptionsTypeDef",
        "DeliveryOptions": "DeliveryOptionsTypeDef",
        "ReputationOptions": "ReputationOptionsTypeDef",
        "SendingOptions": "SendingOptionsTypeDef",
        "Tags": List["TagTypeDef"],
        "SuppressionOptions": "SuppressionOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContactListRequestRequestTypeDef = TypedDict(
    "GetContactListRequestRequestTypeDef",
    {
        "ContactListName": str,
    },
)

GetContactListResponseTypeDef = TypedDict(
    "GetContactListResponseTypeDef",
    {
        "ContactListName": str,
        "Topics": List["TopicTypeDef"],
        "Description": str,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContactRequestRequestTypeDef = TypedDict(
    "GetContactRequestRequestTypeDef",
    {
        "ContactListName": str,
        "EmailAddress": str,
    },
)

GetContactResponseTypeDef = TypedDict(
    "GetContactResponseTypeDef",
    {
        "ContactListName": str,
        "EmailAddress": str,
        "TopicPreferences": List["TopicPreferenceTypeDef"],
        "TopicDefaultPreferences": List["TopicPreferenceTypeDef"],
        "UnsubscribeAll": bool,
        "AttributesData": str,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
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

GetDedicatedIpRequestRequestTypeDef = TypedDict(
    "GetDedicatedIpRequestRequestTypeDef",
    {
        "Ip": str,
    },
)

GetDedicatedIpResponseTypeDef = TypedDict(
    "GetDedicatedIpResponseTypeDef",
    {
        "DedicatedIp": "DedicatedIpTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDedicatedIpsRequestRequestTypeDef = TypedDict(
    "GetDedicatedIpsRequestRequestTypeDef",
    {
        "PoolName": NotRequired[str],
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

GetDedicatedIpsResponseTypeDef = TypedDict(
    "GetDedicatedIpsResponseTypeDef",
    {
        "DedicatedIps": List["DedicatedIpTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeliverabilityDashboardOptionsResponseTypeDef = TypedDict(
    "GetDeliverabilityDashboardOptionsResponseTypeDef",
    {
        "DashboardEnabled": bool,
        "SubscriptionExpiryDate": datetime,
        "AccountStatus": DeliverabilityDashboardAccountStatusType,
        "ActiveSubscribedDomains": List["DomainDeliverabilityTrackingOptionTypeDef"],
        "PendingExpirationSubscribedDomains": List["DomainDeliverabilityTrackingOptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeliverabilityTestReportRequestRequestTypeDef = TypedDict(
    "GetDeliverabilityTestReportRequestRequestTypeDef",
    {
        "ReportId": str,
    },
)

GetDeliverabilityTestReportResponseTypeDef = TypedDict(
    "GetDeliverabilityTestReportResponseTypeDef",
    {
        "DeliverabilityTestReport": "DeliverabilityTestReportTypeDef",
        "OverallPlacement": "PlacementStatisticsTypeDef",
        "IspPlacements": List["IspPlacementTypeDef"],
        "Message": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainDeliverabilityCampaignRequestRequestTypeDef = TypedDict(
    "GetDomainDeliverabilityCampaignRequestRequestTypeDef",
    {
        "CampaignId": str,
    },
)

GetDomainDeliverabilityCampaignResponseTypeDef = TypedDict(
    "GetDomainDeliverabilityCampaignResponseTypeDef",
    {
        "DomainDeliverabilityCampaign": "DomainDeliverabilityCampaignTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainStatisticsReportRequestRequestTypeDef = TypedDict(
    "GetDomainStatisticsReportRequestRequestTypeDef",
    {
        "Domain": str,
        "StartDate": Union[datetime, str],
        "EndDate": Union[datetime, str],
    },
)

GetDomainStatisticsReportResponseTypeDef = TypedDict(
    "GetDomainStatisticsReportResponseTypeDef",
    {
        "OverallVolume": "OverallVolumeTypeDef",
        "DailyVolumes": List["DailyVolumeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEmailIdentityPoliciesRequestRequestTypeDef = TypedDict(
    "GetEmailIdentityPoliciesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)

GetEmailIdentityPoliciesResponseTypeDef = TypedDict(
    "GetEmailIdentityPoliciesResponseTypeDef",
    {
        "Policies": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEmailIdentityRequestRequestTypeDef = TypedDict(
    "GetEmailIdentityRequestRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)

GetEmailIdentityResponseTypeDef = TypedDict(
    "GetEmailIdentityResponseTypeDef",
    {
        "IdentityType": IdentityTypeType,
        "FeedbackForwardingStatus": bool,
        "VerifiedForSendingStatus": bool,
        "DkimAttributes": "DkimAttributesTypeDef",
        "MailFromAttributes": "MailFromAttributesTypeDef",
        "Policies": Dict[str, str],
        "Tags": List["TagTypeDef"],
        "ConfigurationSetName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEmailTemplateRequestRequestTypeDef = TypedDict(
    "GetEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)

GetEmailTemplateResponseTypeDef = TypedDict(
    "GetEmailTemplateResponseTypeDef",
    {
        "TemplateName": str,
        "TemplateContent": "EmailTemplateContentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImportJobRequestRequestTypeDef = TypedDict(
    "GetImportJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

GetImportJobResponseTypeDef = TypedDict(
    "GetImportJobResponseTypeDef",
    {
        "JobId": str,
        "ImportDestination": "ImportDestinationTypeDef",
        "ImportDataSource": "ImportDataSourceTypeDef",
        "FailureInfo": "FailureInfoTypeDef",
        "JobStatus": JobStatusType,
        "CreatedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "ProcessedRecordsCount": int,
        "FailedRecordsCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSuppressedDestinationRequestRequestTypeDef = TypedDict(
    "GetSuppressedDestinationRequestRequestTypeDef",
    {
        "EmailAddress": str,
    },
)

GetSuppressedDestinationResponseTypeDef = TypedDict(
    "GetSuppressedDestinationResponseTypeDef",
    {
        "SuppressedDestination": "SuppressedDestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityInfoTypeDef = TypedDict(
    "IdentityInfoTypeDef",
    {
        "IdentityType": NotRequired[IdentityTypeType],
        "IdentityName": NotRequired[str],
        "SendingEnabled": NotRequired[bool],
    },
)

ImportDataSourceTypeDef = TypedDict(
    "ImportDataSourceTypeDef",
    {
        "S3Url": str,
        "DataFormat": DataFormatType,
    },
)

ImportDestinationTypeDef = TypedDict(
    "ImportDestinationTypeDef",
    {
        "SuppressionListDestination": NotRequired["SuppressionListDestinationTypeDef"],
        "ContactListDestination": NotRequired["ContactListDestinationTypeDef"],
    },
)

ImportJobSummaryTypeDef = TypedDict(
    "ImportJobSummaryTypeDef",
    {
        "JobId": NotRequired[str],
        "ImportDestination": NotRequired["ImportDestinationTypeDef"],
        "JobStatus": NotRequired[JobStatusType],
        "CreatedTimestamp": NotRequired[datetime],
    },
)

InboxPlacementTrackingOptionTypeDef = TypedDict(
    "InboxPlacementTrackingOptionTypeDef",
    {
        "Global": NotRequired[bool],
        "TrackedIsps": NotRequired[List[str]],
    },
)

IspPlacementTypeDef = TypedDict(
    "IspPlacementTypeDef",
    {
        "IspName": NotRequired[str],
        "PlacementStatistics": NotRequired["PlacementStatisticsTypeDef"],
    },
)

KinesisFirehoseDestinationTypeDef = TypedDict(
    "KinesisFirehoseDestinationTypeDef",
    {
        "IamRoleArn": str,
        "DeliveryStreamArn": str,
    },
)

ListConfigurationSetsRequestRequestTypeDef = TypedDict(
    "ListConfigurationSetsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

ListConfigurationSetsResponseTypeDef = TypedDict(
    "ListConfigurationSetsResponseTypeDef",
    {
        "ConfigurationSets": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContactListsRequestRequestTypeDef = TypedDict(
    "ListContactListsRequestRequestTypeDef",
    {
        "PageSize": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListContactListsResponseTypeDef = TypedDict(
    "ListContactListsResponseTypeDef",
    {
        "ContactLists": List["ContactListTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContactsFilterTypeDef = TypedDict(
    "ListContactsFilterTypeDef",
    {
        "FilteredStatus": NotRequired[SubscriptionStatusType],
        "TopicFilter": NotRequired["TopicFilterTypeDef"],
    },
)

ListContactsRequestRequestTypeDef = TypedDict(
    "ListContactsRequestRequestTypeDef",
    {
        "ContactListName": str,
        "Filter": NotRequired["ListContactsFilterTypeDef"],
        "PageSize": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListContactsResponseTypeDef = TypedDict(
    "ListContactsResponseTypeDef",
    {
        "Contacts": List["ContactTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomVerificationEmailTemplatesRequestRequestTypeDef = TypedDict(
    "ListCustomVerificationEmailTemplatesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

ListCustomVerificationEmailTemplatesResponseTypeDef = TypedDict(
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    {
        "CustomVerificationEmailTemplates": List["CustomVerificationEmailTemplateMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDedicatedIpPoolsRequestRequestTypeDef = TypedDict(
    "ListDedicatedIpPoolsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

ListDedicatedIpPoolsResponseTypeDef = TypedDict(
    "ListDedicatedIpPoolsResponseTypeDef",
    {
        "DedicatedIpPools": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeliverabilityTestReportsRequestRequestTypeDef = TypedDict(
    "ListDeliverabilityTestReportsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

ListDeliverabilityTestReportsResponseTypeDef = TypedDict(
    "ListDeliverabilityTestReportsResponseTypeDef",
    {
        "DeliverabilityTestReports": List["DeliverabilityTestReportTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDomainDeliverabilityCampaignsRequestRequestTypeDef = TypedDict(
    "ListDomainDeliverabilityCampaignsRequestRequestTypeDef",
    {
        "StartDate": Union[datetime, str],
        "EndDate": Union[datetime, str],
        "SubscribedDomain": str,
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

ListDomainDeliverabilityCampaignsResponseTypeDef = TypedDict(
    "ListDomainDeliverabilityCampaignsResponseTypeDef",
    {
        "DomainDeliverabilityCampaigns": List["DomainDeliverabilityCampaignTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEmailIdentitiesRequestRequestTypeDef = TypedDict(
    "ListEmailIdentitiesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

ListEmailIdentitiesResponseTypeDef = TypedDict(
    "ListEmailIdentitiesResponseTypeDef",
    {
        "EmailIdentities": List["IdentityInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEmailTemplatesRequestRequestTypeDef = TypedDict(
    "ListEmailTemplatesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

ListEmailTemplatesResponseTypeDef = TypedDict(
    "ListEmailTemplatesResponseTypeDef",
    {
        "TemplatesMetadata": List["EmailTemplateMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImportJobsRequestRequestTypeDef = TypedDict(
    "ListImportJobsRequestRequestTypeDef",
    {
        "ImportDestinationType": NotRequired[ImportDestinationTypeType],
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

ListImportJobsResponseTypeDef = TypedDict(
    "ListImportJobsResponseTypeDef",
    {
        "ImportJobs": List["ImportJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListManagementOptionsTypeDef = TypedDict(
    "ListManagementOptionsTypeDef",
    {
        "ContactListName": str,
        "TopicName": NotRequired[str],
    },
)

ListSuppressedDestinationsRequestRequestTypeDef = TypedDict(
    "ListSuppressedDestinationsRequestRequestTypeDef",
    {
        "Reasons": NotRequired[Sequence[SuppressionListReasonType]],
        "StartDate": NotRequired[Union[datetime, str]],
        "EndDate": NotRequired[Union[datetime, str]],
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

ListSuppressedDestinationsResponseTypeDef = TypedDict(
    "ListSuppressedDestinationsResponseTypeDef",
    {
        "SuppressedDestinationSummaries": List["SuppressedDestinationSummaryTypeDef"],
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
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MailFromAttributesTypeDef = TypedDict(
    "MailFromAttributesTypeDef",
    {
        "MailFromDomain": str,
        "MailFromDomainStatus": MailFromDomainStatusType,
        "BehaviorOnMxFailure": BehaviorOnMxFailureType,
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

OverallVolumeTypeDef = TypedDict(
    "OverallVolumeTypeDef",
    {
        "VolumeStatistics": NotRequired["VolumeStatisticsTypeDef"],
        "ReadRatePercent": NotRequired[float],
        "DomainIspPlacements": NotRequired[List["DomainIspPlacementTypeDef"]],
    },
)

PinpointDestinationTypeDef = TypedDict(
    "PinpointDestinationTypeDef",
    {
        "ApplicationArn": NotRequired[str],
    },
)

PlacementStatisticsTypeDef = TypedDict(
    "PlacementStatisticsTypeDef",
    {
        "InboxPercentage": NotRequired[float],
        "SpamPercentage": NotRequired[float],
        "MissingPercentage": NotRequired[float],
        "SpfPercentage": NotRequired[float],
        "DkimPercentage": NotRequired[float],
    },
)

PutAccountDedicatedIpWarmupAttributesRequestRequestTypeDef = TypedDict(
    "PutAccountDedicatedIpWarmupAttributesRequestRequestTypeDef",
    {
        "AutoWarmupEnabled": NotRequired[bool],
    },
)

PutAccountDetailsRequestRequestTypeDef = TypedDict(
    "PutAccountDetailsRequestRequestTypeDef",
    {
        "MailType": MailTypeType,
        "WebsiteURL": str,
        "UseCaseDescription": str,
        "ContactLanguage": NotRequired[ContactLanguageType],
        "AdditionalContactEmailAddresses": NotRequired[Sequence[str]],
        "ProductionAccessEnabled": NotRequired[bool],
    },
)

PutAccountSendingAttributesRequestRequestTypeDef = TypedDict(
    "PutAccountSendingAttributesRequestRequestTypeDef",
    {
        "SendingEnabled": NotRequired[bool],
    },
)

PutAccountSuppressionAttributesRequestRequestTypeDef = TypedDict(
    "PutAccountSuppressionAttributesRequestRequestTypeDef",
    {
        "SuppressedReasons": NotRequired[Sequence[SuppressionListReasonType]],
    },
)

PutConfigurationSetDeliveryOptionsRequestRequestTypeDef = TypedDict(
    "PutConfigurationSetDeliveryOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "TlsPolicy": NotRequired[TlsPolicyType],
        "SendingPoolName": NotRequired[str],
    },
)

PutConfigurationSetReputationOptionsRequestRequestTypeDef = TypedDict(
    "PutConfigurationSetReputationOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "ReputationMetricsEnabled": NotRequired[bool],
    },
)

PutConfigurationSetSendingOptionsRequestRequestTypeDef = TypedDict(
    "PutConfigurationSetSendingOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "SendingEnabled": NotRequired[bool],
    },
)

PutConfigurationSetSuppressionOptionsRequestRequestTypeDef = TypedDict(
    "PutConfigurationSetSuppressionOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "SuppressedReasons": NotRequired[Sequence[SuppressionListReasonType]],
    },
)

PutConfigurationSetTrackingOptionsRequestRequestTypeDef = TypedDict(
    "PutConfigurationSetTrackingOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "CustomRedirectDomain": NotRequired[str],
    },
)

PutDedicatedIpInPoolRequestRequestTypeDef = TypedDict(
    "PutDedicatedIpInPoolRequestRequestTypeDef",
    {
        "Ip": str,
        "DestinationPoolName": str,
    },
)

PutDedicatedIpWarmupAttributesRequestRequestTypeDef = TypedDict(
    "PutDedicatedIpWarmupAttributesRequestRequestTypeDef",
    {
        "Ip": str,
        "WarmupPercentage": int,
    },
)

PutDeliverabilityDashboardOptionRequestRequestTypeDef = TypedDict(
    "PutDeliverabilityDashboardOptionRequestRequestTypeDef",
    {
        "DashboardEnabled": bool,
        "SubscribedDomains": NotRequired[Sequence["DomainDeliverabilityTrackingOptionTypeDef"]],
    },
)

PutEmailIdentityConfigurationSetAttributesRequestRequestTypeDef = TypedDict(
    "PutEmailIdentityConfigurationSetAttributesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "ConfigurationSetName": NotRequired[str],
    },
)

PutEmailIdentityDkimAttributesRequestRequestTypeDef = TypedDict(
    "PutEmailIdentityDkimAttributesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "SigningEnabled": NotRequired[bool],
    },
)

PutEmailIdentityDkimSigningAttributesRequestRequestTypeDef = TypedDict(
    "PutEmailIdentityDkimSigningAttributesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "SigningAttributesOrigin": DkimSigningAttributesOriginType,
        "SigningAttributes": NotRequired["DkimSigningAttributesTypeDef"],
    },
)

PutEmailIdentityDkimSigningAttributesResponseTypeDef = TypedDict(
    "PutEmailIdentityDkimSigningAttributesResponseTypeDef",
    {
        "DkimStatus": DkimStatusType,
        "DkimTokens": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutEmailIdentityFeedbackAttributesRequestRequestTypeDef = TypedDict(
    "PutEmailIdentityFeedbackAttributesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "EmailForwardingEnabled": NotRequired[bool],
    },
)

PutEmailIdentityMailFromAttributesRequestRequestTypeDef = TypedDict(
    "PutEmailIdentityMailFromAttributesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "MailFromDomain": NotRequired[str],
        "BehaviorOnMxFailure": NotRequired[BehaviorOnMxFailureType],
    },
)

PutSuppressedDestinationRequestRequestTypeDef = TypedDict(
    "PutSuppressedDestinationRequestRequestTypeDef",
    {
        "EmailAddress": str,
        "Reason": SuppressionListReasonType,
    },
)

RawMessageTypeDef = TypedDict(
    "RawMessageTypeDef",
    {
        "Data": Union[bytes, IO[bytes], StreamingBody],
    },
)

ReplacementEmailContentTypeDef = TypedDict(
    "ReplacementEmailContentTypeDef",
    {
        "ReplacementTemplate": NotRequired["ReplacementTemplateTypeDef"],
    },
)

ReplacementTemplateTypeDef = TypedDict(
    "ReplacementTemplateTypeDef",
    {
        "ReplacementTemplateData": NotRequired[str],
    },
)

ReputationOptionsTypeDef = TypedDict(
    "ReputationOptionsTypeDef",
    {
        "ReputationMetricsEnabled": NotRequired[bool],
        "LastFreshStart": NotRequired[Union[datetime, str]],
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

ReviewDetailsTypeDef = TypedDict(
    "ReviewDetailsTypeDef",
    {
        "Status": NotRequired[ReviewStatusType],
        "CaseId": NotRequired[str],
    },
)

SendBulkEmailRequestRequestTypeDef = TypedDict(
    "SendBulkEmailRequestRequestTypeDef",
    {
        "DefaultContent": "BulkEmailContentTypeDef",
        "BulkEmailEntries": Sequence["BulkEmailEntryTypeDef"],
        "FromEmailAddress": NotRequired[str],
        "FromEmailAddressIdentityArn": NotRequired[str],
        "ReplyToAddresses": NotRequired[Sequence[str]],
        "FeedbackForwardingEmailAddress": NotRequired[str],
        "FeedbackForwardingEmailAddressIdentityArn": NotRequired[str],
        "DefaultEmailTags": NotRequired[Sequence["MessageTagTypeDef"]],
        "ConfigurationSetName": NotRequired[str],
    },
)

SendBulkEmailResponseTypeDef = TypedDict(
    "SendBulkEmailResponseTypeDef",
    {
        "BulkEmailEntryResults": List["BulkEmailEntryResultTypeDef"],
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

SendEmailRequestRequestTypeDef = TypedDict(
    "SendEmailRequestRequestTypeDef",
    {
        "Content": "EmailContentTypeDef",
        "FromEmailAddress": NotRequired[str],
        "FromEmailAddressIdentityArn": NotRequired[str],
        "Destination": NotRequired["DestinationTypeDef"],
        "ReplyToAddresses": NotRequired[Sequence[str]],
        "FeedbackForwardingEmailAddress": NotRequired[str],
        "FeedbackForwardingEmailAddressIdentityArn": NotRequired[str],
        "EmailTags": NotRequired[Sequence["MessageTagTypeDef"]],
        "ConfigurationSetName": NotRequired[str],
        "ListManagementOptions": NotRequired["ListManagementOptionsTypeDef"],
    },
)

SendEmailResponseTypeDef = TypedDict(
    "SendEmailResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SendQuotaTypeDef = TypedDict(
    "SendQuotaTypeDef",
    {
        "Max24HourSend": NotRequired[float],
        "MaxSendRate": NotRequired[float],
        "SentLast24Hours": NotRequired[float],
    },
)

SendingOptionsTypeDef = TypedDict(
    "SendingOptionsTypeDef",
    {
        "SendingEnabled": NotRequired[bool],
    },
)

SnsDestinationTypeDef = TypedDict(
    "SnsDestinationTypeDef",
    {
        "TopicArn": str,
    },
)

SuppressedDestinationAttributesTypeDef = TypedDict(
    "SuppressedDestinationAttributesTypeDef",
    {
        "MessageId": NotRequired[str],
        "FeedbackId": NotRequired[str],
    },
)

SuppressedDestinationSummaryTypeDef = TypedDict(
    "SuppressedDestinationSummaryTypeDef",
    {
        "EmailAddress": str,
        "Reason": SuppressionListReasonType,
        "LastUpdateTime": datetime,
    },
)

SuppressedDestinationTypeDef = TypedDict(
    "SuppressedDestinationTypeDef",
    {
        "EmailAddress": str,
        "Reason": SuppressionListReasonType,
        "LastUpdateTime": datetime,
        "Attributes": NotRequired["SuppressedDestinationAttributesTypeDef"],
    },
)

SuppressionAttributesTypeDef = TypedDict(
    "SuppressionAttributesTypeDef",
    {
        "SuppressedReasons": NotRequired[List[SuppressionListReasonType]],
    },
)

SuppressionListDestinationTypeDef = TypedDict(
    "SuppressionListDestinationTypeDef",
    {
        "SuppressionListImportAction": SuppressionListImportActionType,
    },
)

SuppressionOptionsTypeDef = TypedDict(
    "SuppressionOptionsTypeDef",
    {
        "SuppressedReasons": NotRequired[Sequence[SuppressionListReasonType]],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TemplateTypeDef = TypedDict(
    "TemplateTypeDef",
    {
        "TemplateName": NotRequired[str],
        "TemplateArn": NotRequired[str],
        "TemplateData": NotRequired[str],
    },
)

TestRenderEmailTemplateRequestRequestTypeDef = TypedDict(
    "TestRenderEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "TemplateData": str,
    },
)

TestRenderEmailTemplateResponseTypeDef = TypedDict(
    "TestRenderEmailTemplateResponseTypeDef",
    {
        "RenderedTemplate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TopicFilterTypeDef = TypedDict(
    "TopicFilterTypeDef",
    {
        "TopicName": NotRequired[str],
        "UseDefaultIfPreferenceUnavailable": NotRequired[bool],
    },
)

TopicPreferenceTypeDef = TypedDict(
    "TopicPreferenceTypeDef",
    {
        "TopicName": str,
        "SubscriptionStatus": SubscriptionStatusType,
    },
)

TopicTypeDef = TypedDict(
    "TopicTypeDef",
    {
        "TopicName": str,
        "DisplayName": str,
        "DefaultSubscriptionStatus": SubscriptionStatusType,
        "Description": NotRequired[str],
    },
)

TrackingOptionsTypeDef = TypedDict(
    "TrackingOptionsTypeDef",
    {
        "CustomRedirectDomain": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
        "EventDestination": "EventDestinationDefinitionTypeDef",
    },
)

UpdateContactListRequestRequestTypeDef = TypedDict(
    "UpdateContactListRequestRequestTypeDef",
    {
        "ContactListName": str,
        "Topics": NotRequired[Sequence["TopicTypeDef"]],
        "Description": NotRequired[str],
    },
)

UpdateContactRequestRequestTypeDef = TypedDict(
    "UpdateContactRequestRequestTypeDef",
    {
        "ContactListName": str,
        "EmailAddress": str,
        "TopicPreferences": NotRequired[Sequence["TopicPreferenceTypeDef"]],
        "UnsubscribeAll": NotRequired[bool],
        "AttributesData": NotRequired[str],
    },
)

UpdateCustomVerificationEmailTemplateRequestRequestTypeDef = TypedDict(
    "UpdateCustomVerificationEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "TemplateContent": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
)

UpdateEmailIdentityPolicyRequestRequestTypeDef = TypedDict(
    "UpdateEmailIdentityPolicyRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "PolicyName": str,
        "Policy": str,
    },
)

UpdateEmailTemplateRequestRequestTypeDef = TypedDict(
    "UpdateEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "TemplateContent": "EmailTemplateContentTypeDef",
    },
)

VolumeStatisticsTypeDef = TypedDict(
    "VolumeStatisticsTypeDef",
    {
        "InboxRawCount": NotRequired[int],
        "SpamRawCount": NotRequired[int],
        "ProjectedInbox": NotRequired[int],
        "ProjectedSpam": NotRequired[int],
    },
)
