"""
Type annotations for pinpoint-email service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_email/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_pinpoint_email.type_defs import BlacklistEntryTypeDef

    data: BlacklistEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    BehaviorOnMxFailureType,
    DeliverabilityDashboardAccountStatusType,
    DeliverabilityTestStatusType,
    DimensionValueSourceType,
    DkimStatusType,
    EventTypeType,
    IdentityTypeType,
    MailFromDomainStatusType,
    TlsPolicyType,
    WarmupStatusType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BlacklistEntryTypeDef",
    "BodyTypeDef",
    "CloudWatchDestinationTypeDef",
    "CloudWatchDimensionConfigurationTypeDef",
    "ContentTypeDef",
    "CreateConfigurationSetEventDestinationRequestRequestTypeDef",
    "CreateConfigurationSetRequestRequestTypeDef",
    "CreateDedicatedIpPoolRequestRequestTypeDef",
    "CreateDeliverabilityTestReportRequestRequestTypeDef",
    "CreateDeliverabilityTestReportResponseTypeDef",
    "CreateEmailIdentityRequestRequestTypeDef",
    "CreateEmailIdentityResponseTypeDef",
    "DailyVolumeTypeDef",
    "DedicatedIpTypeDef",
    "DeleteConfigurationSetEventDestinationRequestRequestTypeDef",
    "DeleteConfigurationSetRequestRequestTypeDef",
    "DeleteDedicatedIpPoolRequestRequestTypeDef",
    "DeleteEmailIdentityRequestRequestTypeDef",
    "DeliverabilityTestReportTypeDef",
    "DeliveryOptionsTypeDef",
    "DestinationTypeDef",
    "DkimAttributesTypeDef",
    "DomainDeliverabilityCampaignTypeDef",
    "DomainDeliverabilityTrackingOptionTypeDef",
    "DomainIspPlacementTypeDef",
    "EmailContentTypeDef",
    "EventDestinationDefinitionTypeDef",
    "EventDestinationTypeDef",
    "GetAccountResponseTypeDef",
    "GetBlacklistReportsRequestRequestTypeDef",
    "GetBlacklistReportsResponseTypeDef",
    "GetConfigurationSetEventDestinationsRequestRequestTypeDef",
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    "GetConfigurationSetRequestRequestTypeDef",
    "GetConfigurationSetResponseTypeDef",
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
    "GetEmailIdentityRequestRequestTypeDef",
    "GetEmailIdentityResponseTypeDef",
    "IdentityInfoTypeDef",
    "InboxPlacementTrackingOptionTypeDef",
    "IspPlacementTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "ListConfigurationSetsRequestRequestTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "ListDedicatedIpPoolsRequestRequestTypeDef",
    "ListDedicatedIpPoolsResponseTypeDef",
    "ListDeliverabilityTestReportsRequestRequestTypeDef",
    "ListDeliverabilityTestReportsResponseTypeDef",
    "ListDomainDeliverabilityCampaignsRequestRequestTypeDef",
    "ListDomainDeliverabilityCampaignsResponseTypeDef",
    "ListEmailIdentitiesRequestRequestTypeDef",
    "ListEmailIdentitiesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MailFromAttributesTypeDef",
    "MessageTagTypeDef",
    "MessageTypeDef",
    "OverallVolumeTypeDef",
    "PaginatorConfigTypeDef",
    "PinpointDestinationTypeDef",
    "PlacementStatisticsTypeDef",
    "PutAccountDedicatedIpWarmupAttributesRequestRequestTypeDef",
    "PutAccountSendingAttributesRequestRequestTypeDef",
    "PutConfigurationSetDeliveryOptionsRequestRequestTypeDef",
    "PutConfigurationSetReputationOptionsRequestRequestTypeDef",
    "PutConfigurationSetSendingOptionsRequestRequestTypeDef",
    "PutConfigurationSetTrackingOptionsRequestRequestTypeDef",
    "PutDedicatedIpInPoolRequestRequestTypeDef",
    "PutDedicatedIpWarmupAttributesRequestRequestTypeDef",
    "PutDeliverabilityDashboardOptionRequestRequestTypeDef",
    "PutEmailIdentityDkimAttributesRequestRequestTypeDef",
    "PutEmailIdentityFeedbackAttributesRequestRequestTypeDef",
    "PutEmailIdentityMailFromAttributesRequestRequestTypeDef",
    "RawMessageTypeDef",
    "ReputationOptionsTypeDef",
    "ResponseMetadataTypeDef",
    "SendEmailRequestRequestTypeDef",
    "SendEmailResponseTypeDef",
    "SendQuotaTypeDef",
    "SendingOptionsTypeDef",
    "SnsDestinationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TemplateTypeDef",
    "TrackingOptionsTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    "VolumeStatisticsTypeDef",
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

CreateEmailIdentityRequestRequestTypeDef = TypedDict(
    "CreateEmailIdentityRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
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

DeleteDedicatedIpPoolRequestRequestTypeDef = TypedDict(
    "DeleteDedicatedIpPoolRequestRequestTypeDef",
    {
        "PoolName": str,
    },
)

DeleteEmailIdentityRequestRequestTypeDef = TypedDict(
    "DeleteEmailIdentityRequestRequestTypeDef",
    {
        "EmailIdentity": str,
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

GetAccountResponseTypeDef = TypedDict(
    "GetAccountResponseTypeDef",
    {
        "SendQuota": "SendQuotaTypeDef",
        "SendingEnabled": bool,
        "DedicatedIpAutoWarmupEnabled": bool,
        "EnforcementStatus": str,
        "ProductionAccessEnabled": bool,
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
        "Tags": List["TagTypeDef"],
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
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

PutAccountSendingAttributesRequestRequestTypeDef = TypedDict(
    "PutAccountSendingAttributesRequestRequestTypeDef",
    {
        "SendingEnabled": NotRequired[bool],
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

PutEmailIdentityDkimAttributesRequestRequestTypeDef = TypedDict(
    "PutEmailIdentityDkimAttributesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "SigningEnabled": NotRequired[bool],
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

RawMessageTypeDef = TypedDict(
    "RawMessageTypeDef",
    {
        "Data": Union[bytes, IO[bytes], StreamingBody],
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

SendEmailRequestRequestTypeDef = TypedDict(
    "SendEmailRequestRequestTypeDef",
    {
        "Destination": "DestinationTypeDef",
        "Content": "EmailContentTypeDef",
        "FromEmailAddress": NotRequired[str],
        "ReplyToAddresses": NotRequired[Sequence[str]],
        "FeedbackForwardingEmailAddress": NotRequired[str],
        "EmailTags": NotRequired[Sequence["MessageTagTypeDef"]],
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
        "TemplateArn": NotRequired[str],
        "TemplateData": NotRequired[str],
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

VolumeStatisticsTypeDef = TypedDict(
    "VolumeStatisticsTypeDef",
    {
        "InboxRawCount": NotRequired[int],
        "SpamRawCount": NotRequired[int],
        "ProjectedInbox": NotRequired[int],
        "ProjectedSpam": NotRequired[int],
    },
)
