"""
Type annotations for pinpoint service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_pinpoint.type_defs import ADMChannelRequestTypeDef

    data: ADMChannelRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    ActionType,
    AlignmentType,
    AttributeTypeType,
    ButtonActionType,
    CampaignStatusType,
    ChannelTypeType,
    DeliveryStatusType,
    DimensionTypeType,
    DurationType,
    EndpointTypesElementType,
    FilterTypeType,
    FormatType,
    FrequencyType,
    IncludeType,
    JobStatusType,
    LayoutType,
    MessageTypeType,
    ModeType,
    OperatorType,
    RecencyTypeType,
    SegmentTypeType,
    SourceTypeType,
    StateType,
    TemplateTypeType,
    TypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ADMChannelRequestTypeDef",
    "ADMChannelResponseTypeDef",
    "ADMMessageTypeDef",
    "APNSChannelRequestTypeDef",
    "APNSChannelResponseTypeDef",
    "APNSMessageTypeDef",
    "APNSPushNotificationTemplateTypeDef",
    "APNSSandboxChannelRequestTypeDef",
    "APNSSandboxChannelResponseTypeDef",
    "APNSVoipChannelRequestTypeDef",
    "APNSVoipChannelResponseTypeDef",
    "APNSVoipSandboxChannelRequestTypeDef",
    "APNSVoipSandboxChannelResponseTypeDef",
    "ActivitiesResponseTypeDef",
    "ActivityResponseTypeDef",
    "ActivityTypeDef",
    "AddressConfigurationTypeDef",
    "AndroidPushNotificationTemplateTypeDef",
    "ApplicationDateRangeKpiResponseTypeDef",
    "ApplicationResponseTypeDef",
    "ApplicationSettingsResourceTypeDef",
    "ApplicationsResponseTypeDef",
    "AttributeDimensionTypeDef",
    "AttributesResourceTypeDef",
    "BaiduChannelRequestTypeDef",
    "BaiduChannelResponseTypeDef",
    "BaiduMessageTypeDef",
    "BaseKpiResultTypeDef",
    "CampaignCustomMessageTypeDef",
    "CampaignDateRangeKpiResponseTypeDef",
    "CampaignEmailMessageTypeDef",
    "CampaignEventFilterTypeDef",
    "CampaignHookTypeDef",
    "CampaignInAppMessageTypeDef",
    "CampaignLimitsTypeDef",
    "CampaignResponseTypeDef",
    "CampaignSmsMessageTypeDef",
    "CampaignStateTypeDef",
    "CampaignsResponseTypeDef",
    "ChannelResponseTypeDef",
    "ChannelsResponseTypeDef",
    "ConditionTypeDef",
    "ConditionalSplitActivityTypeDef",
    "ContactCenterActivityTypeDef",
    "CreateAppRequestRequestTypeDef",
    "CreateAppResponseTypeDef",
    "CreateApplicationRequestTypeDef",
    "CreateCampaignRequestRequestTypeDef",
    "CreateCampaignResponseTypeDef",
    "CreateEmailTemplateRequestRequestTypeDef",
    "CreateEmailTemplateResponseTypeDef",
    "CreateExportJobRequestRequestTypeDef",
    "CreateExportJobResponseTypeDef",
    "CreateImportJobRequestRequestTypeDef",
    "CreateImportJobResponseTypeDef",
    "CreateInAppTemplateRequestRequestTypeDef",
    "CreateInAppTemplateResponseTypeDef",
    "CreateJourneyRequestRequestTypeDef",
    "CreateJourneyResponseTypeDef",
    "CreatePushTemplateRequestRequestTypeDef",
    "CreatePushTemplateResponseTypeDef",
    "CreateRecommenderConfigurationRequestRequestTypeDef",
    "CreateRecommenderConfigurationResponseTypeDef",
    "CreateRecommenderConfigurationTypeDef",
    "CreateSegmentRequestRequestTypeDef",
    "CreateSegmentResponseTypeDef",
    "CreateSmsTemplateRequestRequestTypeDef",
    "CreateSmsTemplateResponseTypeDef",
    "CreateTemplateMessageBodyTypeDef",
    "CreateVoiceTemplateRequestRequestTypeDef",
    "CreateVoiceTemplateResponseTypeDef",
    "CustomDeliveryConfigurationTypeDef",
    "CustomMessageActivityTypeDef",
    "DefaultButtonConfigurationTypeDef",
    "DefaultMessageTypeDef",
    "DefaultPushNotificationMessageTypeDef",
    "DefaultPushNotificationTemplateTypeDef",
    "DeleteAdmChannelRequestRequestTypeDef",
    "DeleteAdmChannelResponseTypeDef",
    "DeleteApnsChannelRequestRequestTypeDef",
    "DeleteApnsChannelResponseTypeDef",
    "DeleteApnsSandboxChannelRequestRequestTypeDef",
    "DeleteApnsSandboxChannelResponseTypeDef",
    "DeleteApnsVoipChannelRequestRequestTypeDef",
    "DeleteApnsVoipChannelResponseTypeDef",
    "DeleteApnsVoipSandboxChannelRequestRequestTypeDef",
    "DeleteApnsVoipSandboxChannelResponseTypeDef",
    "DeleteAppRequestRequestTypeDef",
    "DeleteAppResponseTypeDef",
    "DeleteBaiduChannelRequestRequestTypeDef",
    "DeleteBaiduChannelResponseTypeDef",
    "DeleteCampaignRequestRequestTypeDef",
    "DeleteCampaignResponseTypeDef",
    "DeleteEmailChannelRequestRequestTypeDef",
    "DeleteEmailChannelResponseTypeDef",
    "DeleteEmailTemplateRequestRequestTypeDef",
    "DeleteEmailTemplateResponseTypeDef",
    "DeleteEndpointRequestRequestTypeDef",
    "DeleteEndpointResponseTypeDef",
    "DeleteEventStreamRequestRequestTypeDef",
    "DeleteEventStreamResponseTypeDef",
    "DeleteGcmChannelRequestRequestTypeDef",
    "DeleteGcmChannelResponseTypeDef",
    "DeleteInAppTemplateRequestRequestTypeDef",
    "DeleteInAppTemplateResponseTypeDef",
    "DeleteJourneyRequestRequestTypeDef",
    "DeleteJourneyResponseTypeDef",
    "DeletePushTemplateRequestRequestTypeDef",
    "DeletePushTemplateResponseTypeDef",
    "DeleteRecommenderConfigurationRequestRequestTypeDef",
    "DeleteRecommenderConfigurationResponseTypeDef",
    "DeleteSegmentRequestRequestTypeDef",
    "DeleteSegmentResponseTypeDef",
    "DeleteSmsChannelRequestRequestTypeDef",
    "DeleteSmsChannelResponseTypeDef",
    "DeleteSmsTemplateRequestRequestTypeDef",
    "DeleteSmsTemplateResponseTypeDef",
    "DeleteUserEndpointsRequestRequestTypeDef",
    "DeleteUserEndpointsResponseTypeDef",
    "DeleteVoiceChannelRequestRequestTypeDef",
    "DeleteVoiceChannelResponseTypeDef",
    "DeleteVoiceTemplateRequestRequestTypeDef",
    "DeleteVoiceTemplateResponseTypeDef",
    "DirectMessageConfigurationTypeDef",
    "EmailChannelRequestTypeDef",
    "EmailChannelResponseTypeDef",
    "EmailMessageActivityTypeDef",
    "EmailMessageTypeDef",
    "EmailTemplateRequestTypeDef",
    "EmailTemplateResponseTypeDef",
    "EndpointBatchItemTypeDef",
    "EndpointBatchRequestTypeDef",
    "EndpointDemographicTypeDef",
    "EndpointItemResponseTypeDef",
    "EndpointLocationTypeDef",
    "EndpointMessageResultTypeDef",
    "EndpointRequestTypeDef",
    "EndpointResponseTypeDef",
    "EndpointSendConfigurationTypeDef",
    "EndpointUserTypeDef",
    "EndpointsResponseTypeDef",
    "EventConditionTypeDef",
    "EventDimensionsTypeDef",
    "EventFilterTypeDef",
    "EventItemResponseTypeDef",
    "EventStartConditionTypeDef",
    "EventStreamTypeDef",
    "EventTypeDef",
    "EventsBatchTypeDef",
    "EventsRequestTypeDef",
    "EventsResponseTypeDef",
    "ExportJobRequestTypeDef",
    "ExportJobResourceTypeDef",
    "ExportJobResponseTypeDef",
    "ExportJobsResponseTypeDef",
    "GCMChannelRequestTypeDef",
    "GCMChannelResponseTypeDef",
    "GCMMessageTypeDef",
    "GPSCoordinatesTypeDef",
    "GPSPointDimensionTypeDef",
    "GetAdmChannelRequestRequestTypeDef",
    "GetAdmChannelResponseTypeDef",
    "GetApnsChannelRequestRequestTypeDef",
    "GetApnsChannelResponseTypeDef",
    "GetApnsSandboxChannelRequestRequestTypeDef",
    "GetApnsSandboxChannelResponseTypeDef",
    "GetApnsVoipChannelRequestRequestTypeDef",
    "GetApnsVoipChannelResponseTypeDef",
    "GetApnsVoipSandboxChannelRequestRequestTypeDef",
    "GetApnsVoipSandboxChannelResponseTypeDef",
    "GetAppRequestRequestTypeDef",
    "GetAppResponseTypeDef",
    "GetApplicationDateRangeKpiRequestRequestTypeDef",
    "GetApplicationDateRangeKpiResponseTypeDef",
    "GetApplicationSettingsRequestRequestTypeDef",
    "GetApplicationSettingsResponseTypeDef",
    "GetAppsRequestRequestTypeDef",
    "GetAppsResponseTypeDef",
    "GetBaiduChannelRequestRequestTypeDef",
    "GetBaiduChannelResponseTypeDef",
    "GetCampaignActivitiesRequestRequestTypeDef",
    "GetCampaignActivitiesResponseTypeDef",
    "GetCampaignDateRangeKpiRequestRequestTypeDef",
    "GetCampaignDateRangeKpiResponseTypeDef",
    "GetCampaignRequestRequestTypeDef",
    "GetCampaignResponseTypeDef",
    "GetCampaignVersionRequestRequestTypeDef",
    "GetCampaignVersionResponseTypeDef",
    "GetCampaignVersionsRequestRequestTypeDef",
    "GetCampaignVersionsResponseTypeDef",
    "GetCampaignsRequestRequestTypeDef",
    "GetCampaignsResponseTypeDef",
    "GetChannelsRequestRequestTypeDef",
    "GetChannelsResponseTypeDef",
    "GetEmailChannelRequestRequestTypeDef",
    "GetEmailChannelResponseTypeDef",
    "GetEmailTemplateRequestRequestTypeDef",
    "GetEmailTemplateResponseTypeDef",
    "GetEndpointRequestRequestTypeDef",
    "GetEndpointResponseTypeDef",
    "GetEventStreamRequestRequestTypeDef",
    "GetEventStreamResponseTypeDef",
    "GetExportJobRequestRequestTypeDef",
    "GetExportJobResponseTypeDef",
    "GetExportJobsRequestRequestTypeDef",
    "GetExportJobsResponseTypeDef",
    "GetGcmChannelRequestRequestTypeDef",
    "GetGcmChannelResponseTypeDef",
    "GetImportJobRequestRequestTypeDef",
    "GetImportJobResponseTypeDef",
    "GetImportJobsRequestRequestTypeDef",
    "GetImportJobsResponseTypeDef",
    "GetInAppMessagesRequestRequestTypeDef",
    "GetInAppMessagesResponseTypeDef",
    "GetInAppTemplateRequestRequestTypeDef",
    "GetInAppTemplateResponseTypeDef",
    "GetJourneyDateRangeKpiRequestRequestTypeDef",
    "GetJourneyDateRangeKpiResponseTypeDef",
    "GetJourneyExecutionActivityMetricsRequestRequestTypeDef",
    "GetJourneyExecutionActivityMetricsResponseTypeDef",
    "GetJourneyExecutionMetricsRequestRequestTypeDef",
    "GetJourneyExecutionMetricsResponseTypeDef",
    "GetJourneyRequestRequestTypeDef",
    "GetJourneyResponseTypeDef",
    "GetPushTemplateRequestRequestTypeDef",
    "GetPushTemplateResponseTypeDef",
    "GetRecommenderConfigurationRequestRequestTypeDef",
    "GetRecommenderConfigurationResponseTypeDef",
    "GetRecommenderConfigurationsRequestRequestTypeDef",
    "GetRecommenderConfigurationsResponseTypeDef",
    "GetSegmentExportJobsRequestRequestTypeDef",
    "GetSegmentExportJobsResponseTypeDef",
    "GetSegmentImportJobsRequestRequestTypeDef",
    "GetSegmentImportJobsResponseTypeDef",
    "GetSegmentRequestRequestTypeDef",
    "GetSegmentResponseTypeDef",
    "GetSegmentVersionRequestRequestTypeDef",
    "GetSegmentVersionResponseTypeDef",
    "GetSegmentVersionsRequestRequestTypeDef",
    "GetSegmentVersionsResponseTypeDef",
    "GetSegmentsRequestRequestTypeDef",
    "GetSegmentsResponseTypeDef",
    "GetSmsChannelRequestRequestTypeDef",
    "GetSmsChannelResponseTypeDef",
    "GetSmsTemplateRequestRequestTypeDef",
    "GetSmsTemplateResponseTypeDef",
    "GetUserEndpointsRequestRequestTypeDef",
    "GetUserEndpointsResponseTypeDef",
    "GetVoiceChannelRequestRequestTypeDef",
    "GetVoiceChannelResponseTypeDef",
    "GetVoiceTemplateRequestRequestTypeDef",
    "GetVoiceTemplateResponseTypeDef",
    "HoldoutActivityTypeDef",
    "ImportJobRequestTypeDef",
    "ImportJobResourceTypeDef",
    "ImportJobResponseTypeDef",
    "ImportJobsResponseTypeDef",
    "InAppCampaignScheduleTypeDef",
    "InAppMessageBodyConfigTypeDef",
    "InAppMessageButtonTypeDef",
    "InAppMessageCampaignTypeDef",
    "InAppMessageContentTypeDef",
    "InAppMessageHeaderConfigTypeDef",
    "InAppMessageTypeDef",
    "InAppMessagesResponseTypeDef",
    "InAppTemplateRequestTypeDef",
    "InAppTemplateResponseTypeDef",
    "ItemResponseTypeDef",
    "JourneyChannelSettingsTypeDef",
    "JourneyCustomMessageTypeDef",
    "JourneyDateRangeKpiResponseTypeDef",
    "JourneyEmailMessageTypeDef",
    "JourneyExecutionActivityMetricsResponseTypeDef",
    "JourneyExecutionMetricsResponseTypeDef",
    "JourneyLimitsTypeDef",
    "JourneyPushMessageTypeDef",
    "JourneyResponseTypeDef",
    "JourneySMSMessageTypeDef",
    "JourneyScheduleTypeDef",
    "JourneyStateRequestTypeDef",
    "JourneysResponseTypeDef",
    "ListJourneysRequestRequestTypeDef",
    "ListJourneysResponseTypeDef",
    "ListRecommenderConfigurationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTemplateVersionsRequestRequestTypeDef",
    "ListTemplateVersionsResponseTypeDef",
    "ListTemplatesRequestRequestTypeDef",
    "ListTemplatesResponseTypeDef",
    "MessageBodyTypeDef",
    "MessageConfigurationTypeDef",
    "MessageRequestTypeDef",
    "MessageResponseTypeDef",
    "MessageResultTypeDef",
    "MessageTypeDef",
    "MetricDimensionTypeDef",
    "MultiConditionalBranchTypeDef",
    "MultiConditionalSplitActivityTypeDef",
    "NumberValidateRequestTypeDef",
    "NumberValidateResponseTypeDef",
    "OverrideButtonConfigurationTypeDef",
    "PhoneNumberValidateRequestRequestTypeDef",
    "PhoneNumberValidateResponseTypeDef",
    "PublicEndpointTypeDef",
    "PushMessageActivityTypeDef",
    "PushNotificationTemplateRequestTypeDef",
    "PushNotificationTemplateResponseTypeDef",
    "PutEventStreamRequestRequestTypeDef",
    "PutEventStreamResponseTypeDef",
    "PutEventsRequestRequestTypeDef",
    "PutEventsResponseTypeDef",
    "QuietTimeTypeDef",
    "RandomSplitActivityTypeDef",
    "RandomSplitEntryTypeDef",
    "RawEmailTypeDef",
    "RecencyDimensionTypeDef",
    "RecommenderConfigurationResponseTypeDef",
    "RemoveAttributesRequestRequestTypeDef",
    "RemoveAttributesResponseTypeDef",
    "ResponseMetadataTypeDef",
    "ResultRowTypeDef",
    "ResultRowValueTypeDef",
    "SMSChannelRequestTypeDef",
    "SMSChannelResponseTypeDef",
    "SMSMessageActivityTypeDef",
    "SMSMessageTypeDef",
    "SMSTemplateRequestTypeDef",
    "SMSTemplateResponseTypeDef",
    "ScheduleTypeDef",
    "SegmentBehaviorsTypeDef",
    "SegmentConditionTypeDef",
    "SegmentDemographicsTypeDef",
    "SegmentDimensionsTypeDef",
    "SegmentGroupListTypeDef",
    "SegmentGroupTypeDef",
    "SegmentImportResourceTypeDef",
    "SegmentLocationTypeDef",
    "SegmentReferenceTypeDef",
    "SegmentResponseTypeDef",
    "SegmentsResponseTypeDef",
    "SendMessagesRequestRequestTypeDef",
    "SendMessagesResponseTypeDef",
    "SendOTPMessageRequestParametersTypeDef",
    "SendOTPMessageRequestRequestTypeDef",
    "SendOTPMessageResponseTypeDef",
    "SendUsersMessageRequestTypeDef",
    "SendUsersMessageResponseTypeDef",
    "SendUsersMessagesRequestRequestTypeDef",
    "SendUsersMessagesResponseTypeDef",
    "SessionTypeDef",
    "SetDimensionTypeDef",
    "SimpleConditionTypeDef",
    "SimpleEmailPartTypeDef",
    "SimpleEmailTypeDef",
    "StartConditionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagsModelTypeDef",
    "TemplateActiveVersionRequestTypeDef",
    "TemplateConfigurationTypeDef",
    "TemplateCreateMessageBodyTypeDef",
    "TemplateResponseTypeDef",
    "TemplateTypeDef",
    "TemplateVersionResponseTypeDef",
    "TemplateVersionsResponseTypeDef",
    "TemplatesResponseTypeDef",
    "TreatmentResourceTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAdmChannelRequestRequestTypeDef",
    "UpdateAdmChannelResponseTypeDef",
    "UpdateApnsChannelRequestRequestTypeDef",
    "UpdateApnsChannelResponseTypeDef",
    "UpdateApnsSandboxChannelRequestRequestTypeDef",
    "UpdateApnsSandboxChannelResponseTypeDef",
    "UpdateApnsVoipChannelRequestRequestTypeDef",
    "UpdateApnsVoipChannelResponseTypeDef",
    "UpdateApnsVoipSandboxChannelRequestRequestTypeDef",
    "UpdateApnsVoipSandboxChannelResponseTypeDef",
    "UpdateApplicationSettingsRequestRequestTypeDef",
    "UpdateApplicationSettingsResponseTypeDef",
    "UpdateAttributesRequestTypeDef",
    "UpdateBaiduChannelRequestRequestTypeDef",
    "UpdateBaiduChannelResponseTypeDef",
    "UpdateCampaignRequestRequestTypeDef",
    "UpdateCampaignResponseTypeDef",
    "UpdateEmailChannelRequestRequestTypeDef",
    "UpdateEmailChannelResponseTypeDef",
    "UpdateEmailTemplateRequestRequestTypeDef",
    "UpdateEmailTemplateResponseTypeDef",
    "UpdateEndpointRequestRequestTypeDef",
    "UpdateEndpointResponseTypeDef",
    "UpdateEndpointsBatchRequestRequestTypeDef",
    "UpdateEndpointsBatchResponseTypeDef",
    "UpdateGcmChannelRequestRequestTypeDef",
    "UpdateGcmChannelResponseTypeDef",
    "UpdateInAppTemplateRequestRequestTypeDef",
    "UpdateInAppTemplateResponseTypeDef",
    "UpdateJourneyRequestRequestTypeDef",
    "UpdateJourneyResponseTypeDef",
    "UpdateJourneyStateRequestRequestTypeDef",
    "UpdateJourneyStateResponseTypeDef",
    "UpdatePushTemplateRequestRequestTypeDef",
    "UpdatePushTemplateResponseTypeDef",
    "UpdateRecommenderConfigurationRequestRequestTypeDef",
    "UpdateRecommenderConfigurationResponseTypeDef",
    "UpdateRecommenderConfigurationTypeDef",
    "UpdateSegmentRequestRequestTypeDef",
    "UpdateSegmentResponseTypeDef",
    "UpdateSmsChannelRequestRequestTypeDef",
    "UpdateSmsChannelResponseTypeDef",
    "UpdateSmsTemplateRequestRequestTypeDef",
    "UpdateSmsTemplateResponseTypeDef",
    "UpdateTemplateActiveVersionRequestRequestTypeDef",
    "UpdateTemplateActiveVersionResponseTypeDef",
    "UpdateVoiceChannelRequestRequestTypeDef",
    "UpdateVoiceChannelResponseTypeDef",
    "UpdateVoiceTemplateRequestRequestTypeDef",
    "UpdateVoiceTemplateResponseTypeDef",
    "VerificationResponseTypeDef",
    "VerifyOTPMessageRequestParametersTypeDef",
    "VerifyOTPMessageRequestRequestTypeDef",
    "VerifyOTPMessageResponseTypeDef",
    "VoiceChannelRequestTypeDef",
    "VoiceChannelResponseTypeDef",
    "VoiceMessageTypeDef",
    "VoiceTemplateRequestTypeDef",
    "VoiceTemplateResponseTypeDef",
    "WaitActivityTypeDef",
    "WaitTimeTypeDef",
    "WriteApplicationSettingsRequestTypeDef",
    "WriteCampaignRequestTypeDef",
    "WriteEventStreamTypeDef",
    "WriteJourneyRequestTypeDef",
    "WriteSegmentRequestTypeDef",
    "WriteTreatmentResourceTypeDef",
)

ADMChannelRequestTypeDef = TypedDict(
    "ADMChannelRequestTypeDef",
    {
        "ClientId": str,
        "ClientSecret": str,
        "Enabled": NotRequired[bool],
    },
)

ADMChannelResponseTypeDef = TypedDict(
    "ADMChannelResponseTypeDef",
    {
        "Platform": str,
        "ApplicationId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "Enabled": NotRequired[bool],
        "HasCredential": NotRequired[bool],
        "Id": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Version": NotRequired[int],
    },
)

ADMMessageTypeDef = TypedDict(
    "ADMMessageTypeDef",
    {
        "Action": NotRequired[ActionType],
        "Body": NotRequired[str],
        "ConsolidationKey": NotRequired[str],
        "Data": NotRequired[Mapping[str, str]],
        "ExpiresAfter": NotRequired[str],
        "IconReference": NotRequired[str],
        "ImageIconUrl": NotRequired[str],
        "ImageUrl": NotRequired[str],
        "MD5": NotRequired[str],
        "RawContent": NotRequired[str],
        "SilentPush": NotRequired[bool],
        "SmallImageIconUrl": NotRequired[str],
        "Sound": NotRequired[str],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
        "Title": NotRequired[str],
        "Url": NotRequired[str],
    },
)

APNSChannelRequestTypeDef = TypedDict(
    "APNSChannelRequestTypeDef",
    {
        "BundleId": NotRequired[str],
        "Certificate": NotRequired[str],
        "DefaultAuthenticationMethod": NotRequired[str],
        "Enabled": NotRequired[bool],
        "PrivateKey": NotRequired[str],
        "TeamId": NotRequired[str],
        "TokenKey": NotRequired[str],
        "TokenKeyId": NotRequired[str],
    },
)

APNSChannelResponseTypeDef = TypedDict(
    "APNSChannelResponseTypeDef",
    {
        "Platform": str,
        "ApplicationId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "DefaultAuthenticationMethod": NotRequired[str],
        "Enabled": NotRequired[bool],
        "HasCredential": NotRequired[bool],
        "HasTokenKey": NotRequired[bool],
        "Id": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Version": NotRequired[int],
    },
)

APNSMessageTypeDef = TypedDict(
    "APNSMessageTypeDef",
    {
        "APNSPushType": NotRequired[str],
        "Action": NotRequired[ActionType],
        "Badge": NotRequired[int],
        "Body": NotRequired[str],
        "Category": NotRequired[str],
        "CollapseId": NotRequired[str],
        "Data": NotRequired[Mapping[str, str]],
        "MediaUrl": NotRequired[str],
        "PreferredAuthenticationMethod": NotRequired[str],
        "Priority": NotRequired[str],
        "RawContent": NotRequired[str],
        "SilentPush": NotRequired[bool],
        "Sound": NotRequired[str],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
        "ThreadId": NotRequired[str],
        "TimeToLive": NotRequired[int],
        "Title": NotRequired[str],
        "Url": NotRequired[str],
    },
)

APNSPushNotificationTemplateTypeDef = TypedDict(
    "APNSPushNotificationTemplateTypeDef",
    {
        "Action": NotRequired[ActionType],
        "Body": NotRequired[str],
        "MediaUrl": NotRequired[str],
        "RawContent": NotRequired[str],
        "Sound": NotRequired[str],
        "Title": NotRequired[str],
        "Url": NotRequired[str],
    },
)

APNSSandboxChannelRequestTypeDef = TypedDict(
    "APNSSandboxChannelRequestTypeDef",
    {
        "BundleId": NotRequired[str],
        "Certificate": NotRequired[str],
        "DefaultAuthenticationMethod": NotRequired[str],
        "Enabled": NotRequired[bool],
        "PrivateKey": NotRequired[str],
        "TeamId": NotRequired[str],
        "TokenKey": NotRequired[str],
        "TokenKeyId": NotRequired[str],
    },
)

APNSSandboxChannelResponseTypeDef = TypedDict(
    "APNSSandboxChannelResponseTypeDef",
    {
        "Platform": str,
        "ApplicationId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "DefaultAuthenticationMethod": NotRequired[str],
        "Enabled": NotRequired[bool],
        "HasCredential": NotRequired[bool],
        "HasTokenKey": NotRequired[bool],
        "Id": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Version": NotRequired[int],
    },
)

APNSVoipChannelRequestTypeDef = TypedDict(
    "APNSVoipChannelRequestTypeDef",
    {
        "BundleId": NotRequired[str],
        "Certificate": NotRequired[str],
        "DefaultAuthenticationMethod": NotRequired[str],
        "Enabled": NotRequired[bool],
        "PrivateKey": NotRequired[str],
        "TeamId": NotRequired[str],
        "TokenKey": NotRequired[str],
        "TokenKeyId": NotRequired[str],
    },
)

APNSVoipChannelResponseTypeDef = TypedDict(
    "APNSVoipChannelResponseTypeDef",
    {
        "Platform": str,
        "ApplicationId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "DefaultAuthenticationMethod": NotRequired[str],
        "Enabled": NotRequired[bool],
        "HasCredential": NotRequired[bool],
        "HasTokenKey": NotRequired[bool],
        "Id": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Version": NotRequired[int],
    },
)

APNSVoipSandboxChannelRequestTypeDef = TypedDict(
    "APNSVoipSandboxChannelRequestTypeDef",
    {
        "BundleId": NotRequired[str],
        "Certificate": NotRequired[str],
        "DefaultAuthenticationMethod": NotRequired[str],
        "Enabled": NotRequired[bool],
        "PrivateKey": NotRequired[str],
        "TeamId": NotRequired[str],
        "TokenKey": NotRequired[str],
        "TokenKeyId": NotRequired[str],
    },
)

APNSVoipSandboxChannelResponseTypeDef = TypedDict(
    "APNSVoipSandboxChannelResponseTypeDef",
    {
        "Platform": str,
        "ApplicationId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "DefaultAuthenticationMethod": NotRequired[str],
        "Enabled": NotRequired[bool],
        "HasCredential": NotRequired[bool],
        "HasTokenKey": NotRequired[bool],
        "Id": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Version": NotRequired[int],
    },
)

ActivitiesResponseTypeDef = TypedDict(
    "ActivitiesResponseTypeDef",
    {
        "Item": List["ActivityResponseTypeDef"],
        "NextToken": NotRequired[str],
    },
)

ActivityResponseTypeDef = TypedDict(
    "ActivityResponseTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "Id": str,
        "End": NotRequired[str],
        "Result": NotRequired[str],
        "ScheduledStart": NotRequired[str],
        "Start": NotRequired[str],
        "State": NotRequired[str],
        "SuccessfulEndpointCount": NotRequired[int],
        "TimezonesCompletedCount": NotRequired[int],
        "TimezonesTotalCount": NotRequired[int],
        "TotalEndpointCount": NotRequired[int],
        "TreatmentId": NotRequired[str],
    },
)

ActivityTypeDef = TypedDict(
    "ActivityTypeDef",
    {
        "CUSTOM": NotRequired["CustomMessageActivityTypeDef"],
        "ConditionalSplit": NotRequired["ConditionalSplitActivityTypeDef"],
        "Description": NotRequired[str],
        "EMAIL": NotRequired["EmailMessageActivityTypeDef"],
        "Holdout": NotRequired["HoldoutActivityTypeDef"],
        "MultiCondition": NotRequired["MultiConditionalSplitActivityTypeDef"],
        "PUSH": NotRequired["PushMessageActivityTypeDef"],
        "RandomSplit": NotRequired["RandomSplitActivityTypeDef"],
        "SMS": NotRequired["SMSMessageActivityTypeDef"],
        "Wait": NotRequired["WaitActivityTypeDef"],
        "ContactCenter": NotRequired["ContactCenterActivityTypeDef"],
    },
)

AddressConfigurationTypeDef = TypedDict(
    "AddressConfigurationTypeDef",
    {
        "BodyOverride": NotRequired[str],
        "ChannelType": NotRequired[ChannelTypeType],
        "Context": NotRequired[Mapping[str, str]],
        "RawContent": NotRequired[str],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
        "TitleOverride": NotRequired[str],
    },
)

AndroidPushNotificationTemplateTypeDef = TypedDict(
    "AndroidPushNotificationTemplateTypeDef",
    {
        "Action": NotRequired[ActionType],
        "Body": NotRequired[str],
        "ImageIconUrl": NotRequired[str],
        "ImageUrl": NotRequired[str],
        "RawContent": NotRequired[str],
        "SmallImageIconUrl": NotRequired[str],
        "Sound": NotRequired[str],
        "Title": NotRequired[str],
        "Url": NotRequired[str],
    },
)

ApplicationDateRangeKpiResponseTypeDef = TypedDict(
    "ApplicationDateRangeKpiResponseTypeDef",
    {
        "ApplicationId": str,
        "EndTime": datetime,
        "KpiName": str,
        "KpiResult": "BaseKpiResultTypeDef",
        "StartTime": datetime,
        "NextToken": NotRequired[str],
    },
)

ApplicationResponseTypeDef = TypedDict(
    "ApplicationResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "tags": NotRequired[Dict[str, str]],
        "CreationDate": NotRequired[str],
    },
)

ApplicationSettingsResourceTypeDef = TypedDict(
    "ApplicationSettingsResourceTypeDef",
    {
        "ApplicationId": str,
        "CampaignHook": NotRequired["CampaignHookTypeDef"],
        "LastModifiedDate": NotRequired[str],
        "Limits": NotRequired["CampaignLimitsTypeDef"],
        "QuietTime": NotRequired["QuietTimeTypeDef"],
    },
)

ApplicationsResponseTypeDef = TypedDict(
    "ApplicationsResponseTypeDef",
    {
        "Item": NotRequired[List["ApplicationResponseTypeDef"]],
        "NextToken": NotRequired[str],
    },
)

AttributeDimensionTypeDef = TypedDict(
    "AttributeDimensionTypeDef",
    {
        "Values": Sequence[str],
        "AttributeType": NotRequired[AttributeTypeType],
    },
)

AttributesResourceTypeDef = TypedDict(
    "AttributesResourceTypeDef",
    {
        "ApplicationId": str,
        "AttributeType": str,
        "Attributes": NotRequired[List[str]],
    },
)

BaiduChannelRequestTypeDef = TypedDict(
    "BaiduChannelRequestTypeDef",
    {
        "ApiKey": str,
        "SecretKey": str,
        "Enabled": NotRequired[bool],
    },
)

BaiduChannelResponseTypeDef = TypedDict(
    "BaiduChannelResponseTypeDef",
    {
        "Credential": str,
        "Platform": str,
        "ApplicationId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "Enabled": NotRequired[bool],
        "HasCredential": NotRequired[bool],
        "Id": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Version": NotRequired[int],
    },
)

BaiduMessageTypeDef = TypedDict(
    "BaiduMessageTypeDef",
    {
        "Action": NotRequired[ActionType],
        "Body": NotRequired[str],
        "Data": NotRequired[Mapping[str, str]],
        "IconReference": NotRequired[str],
        "ImageIconUrl": NotRequired[str],
        "ImageUrl": NotRequired[str],
        "RawContent": NotRequired[str],
        "SilentPush": NotRequired[bool],
        "SmallImageIconUrl": NotRequired[str],
        "Sound": NotRequired[str],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
        "TimeToLive": NotRequired[int],
        "Title": NotRequired[str],
        "Url": NotRequired[str],
    },
)

BaseKpiResultTypeDef = TypedDict(
    "BaseKpiResultTypeDef",
    {
        "Rows": List["ResultRowTypeDef"],
    },
)

CampaignCustomMessageTypeDef = TypedDict(
    "CampaignCustomMessageTypeDef",
    {
        "Data": NotRequired[str],
    },
)

CampaignDateRangeKpiResponseTypeDef = TypedDict(
    "CampaignDateRangeKpiResponseTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "EndTime": datetime,
        "KpiName": str,
        "KpiResult": "BaseKpiResultTypeDef",
        "StartTime": datetime,
        "NextToken": NotRequired[str],
    },
)

CampaignEmailMessageTypeDef = TypedDict(
    "CampaignEmailMessageTypeDef",
    {
        "Body": NotRequired[str],
        "FromAddress": NotRequired[str],
        "HtmlBody": NotRequired[str],
        "Title": NotRequired[str],
    },
)

CampaignEventFilterTypeDef = TypedDict(
    "CampaignEventFilterTypeDef",
    {
        "Dimensions": "EventDimensionsTypeDef",
        "FilterType": FilterTypeType,
    },
)

CampaignHookTypeDef = TypedDict(
    "CampaignHookTypeDef",
    {
        "LambdaFunctionName": NotRequired[str],
        "Mode": NotRequired[ModeType],
        "WebUrl": NotRequired[str],
    },
)

CampaignInAppMessageTypeDef = TypedDict(
    "CampaignInAppMessageTypeDef",
    {
        "Body": NotRequired[str],
        "Content": NotRequired[Sequence["InAppMessageContentTypeDef"]],
        "CustomConfig": NotRequired[Mapping[str, str]],
        "Layout": NotRequired[LayoutType],
    },
)

CampaignLimitsTypeDef = TypedDict(
    "CampaignLimitsTypeDef",
    {
        "Daily": NotRequired[int],
        "MaximumDuration": NotRequired[int],
        "MessagesPerSecond": NotRequired[int],
        "Total": NotRequired[int],
        "Session": NotRequired[int],
    },
)

CampaignResponseTypeDef = TypedDict(
    "CampaignResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "CreationDate": str,
        "Id": str,
        "LastModifiedDate": str,
        "SegmentId": str,
        "SegmentVersion": int,
        "AdditionalTreatments": NotRequired[List["TreatmentResourceTypeDef"]],
        "CustomDeliveryConfiguration": NotRequired["CustomDeliveryConfigurationTypeDef"],
        "DefaultState": NotRequired["CampaignStateTypeDef"],
        "Description": NotRequired[str],
        "HoldoutPercent": NotRequired[int],
        "Hook": NotRequired["CampaignHookTypeDef"],
        "IsPaused": NotRequired[bool],
        "Limits": NotRequired["CampaignLimitsTypeDef"],
        "MessageConfiguration": NotRequired["MessageConfigurationTypeDef"],
        "Name": NotRequired[str],
        "Schedule": NotRequired["ScheduleTypeDef"],
        "State": NotRequired["CampaignStateTypeDef"],
        "tags": NotRequired[Dict[str, str]],
        "TemplateConfiguration": NotRequired["TemplateConfigurationTypeDef"],
        "TreatmentDescription": NotRequired[str],
        "TreatmentName": NotRequired[str],
        "Version": NotRequired[int],
        "Priority": NotRequired[int],
    },
)

CampaignSmsMessageTypeDef = TypedDict(
    "CampaignSmsMessageTypeDef",
    {
        "Body": NotRequired[str],
        "MessageType": NotRequired[MessageTypeType],
        "OriginationNumber": NotRequired[str],
        "SenderId": NotRequired[str],
        "EntityId": NotRequired[str],
        "TemplateId": NotRequired[str],
    },
)

CampaignStateTypeDef = TypedDict(
    "CampaignStateTypeDef",
    {
        "CampaignStatus": NotRequired[CampaignStatusType],
    },
)

CampaignsResponseTypeDef = TypedDict(
    "CampaignsResponseTypeDef",
    {
        "Item": List["CampaignResponseTypeDef"],
        "NextToken": NotRequired[str],
    },
)

ChannelResponseTypeDef = TypedDict(
    "ChannelResponseTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "Enabled": NotRequired[bool],
        "HasCredential": NotRequired[bool],
        "Id": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Version": NotRequired[int],
    },
)

ChannelsResponseTypeDef = TypedDict(
    "ChannelsResponseTypeDef",
    {
        "Channels": Dict[str, "ChannelResponseTypeDef"],
    },
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "Conditions": NotRequired[Sequence["SimpleConditionTypeDef"]],
        "Operator": NotRequired[OperatorType],
    },
)

ConditionalSplitActivityTypeDef = TypedDict(
    "ConditionalSplitActivityTypeDef",
    {
        "Condition": NotRequired["ConditionTypeDef"],
        "EvaluationWaitTime": NotRequired["WaitTimeTypeDef"],
        "FalseActivity": NotRequired[str],
        "TrueActivity": NotRequired[str],
    },
)

ContactCenterActivityTypeDef = TypedDict(
    "ContactCenterActivityTypeDef",
    {
        "NextActivity": NotRequired[str],
    },
)

CreateAppRequestRequestTypeDef = TypedDict(
    "CreateAppRequestRequestTypeDef",
    {
        "CreateApplicationRequest": "CreateApplicationRequestTypeDef",
    },
)

CreateAppResponseTypeDef = TypedDict(
    "CreateAppResponseTypeDef",
    {
        "ApplicationResponse": "ApplicationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateApplicationRequestTypeDef = TypedDict(
    "CreateApplicationRequestTypeDef",
    {
        "Name": str,
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateCampaignRequestRequestTypeDef = TypedDict(
    "CreateCampaignRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "WriteCampaignRequest": "WriteCampaignRequestTypeDef",
    },
)

CreateCampaignResponseTypeDef = TypedDict(
    "CreateCampaignResponseTypeDef",
    {
        "CampaignResponse": "CampaignResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEmailTemplateRequestRequestTypeDef = TypedDict(
    "CreateEmailTemplateRequestRequestTypeDef",
    {
        "EmailTemplateRequest": "EmailTemplateRequestTypeDef",
        "TemplateName": str,
    },
)

CreateEmailTemplateResponseTypeDef = TypedDict(
    "CreateEmailTemplateResponseTypeDef",
    {
        "CreateTemplateMessageBody": "CreateTemplateMessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateExportJobRequestRequestTypeDef = TypedDict(
    "CreateExportJobRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ExportJobRequest": "ExportJobRequestTypeDef",
    },
)

CreateExportJobResponseTypeDef = TypedDict(
    "CreateExportJobResponseTypeDef",
    {
        "ExportJobResponse": "ExportJobResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateImportJobRequestRequestTypeDef = TypedDict(
    "CreateImportJobRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ImportJobRequest": "ImportJobRequestTypeDef",
    },
)

CreateImportJobResponseTypeDef = TypedDict(
    "CreateImportJobResponseTypeDef",
    {
        "ImportJobResponse": "ImportJobResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInAppTemplateRequestRequestTypeDef = TypedDict(
    "CreateInAppTemplateRequestRequestTypeDef",
    {
        "InAppTemplateRequest": "InAppTemplateRequestTypeDef",
        "TemplateName": str,
    },
)

CreateInAppTemplateResponseTypeDef = TypedDict(
    "CreateInAppTemplateResponseTypeDef",
    {
        "TemplateCreateMessageBody": "TemplateCreateMessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateJourneyRequestRequestTypeDef = TypedDict(
    "CreateJourneyRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "WriteJourneyRequest": "WriteJourneyRequestTypeDef",
    },
)

CreateJourneyResponseTypeDef = TypedDict(
    "CreateJourneyResponseTypeDef",
    {
        "JourneyResponse": "JourneyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePushTemplateRequestRequestTypeDef = TypedDict(
    "CreatePushTemplateRequestRequestTypeDef",
    {
        "PushNotificationTemplateRequest": "PushNotificationTemplateRequestTypeDef",
        "TemplateName": str,
    },
)

CreatePushTemplateResponseTypeDef = TypedDict(
    "CreatePushTemplateResponseTypeDef",
    {
        "CreateTemplateMessageBody": "CreateTemplateMessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRecommenderConfigurationRequestRequestTypeDef = TypedDict(
    "CreateRecommenderConfigurationRequestRequestTypeDef",
    {
        "CreateRecommenderConfiguration": "CreateRecommenderConfigurationTypeDef",
    },
)

CreateRecommenderConfigurationResponseTypeDef = TypedDict(
    "CreateRecommenderConfigurationResponseTypeDef",
    {
        "RecommenderConfigurationResponse": "RecommenderConfigurationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRecommenderConfigurationTypeDef = TypedDict(
    "CreateRecommenderConfigurationTypeDef",
    {
        "RecommendationProviderRoleArn": str,
        "RecommendationProviderUri": str,
        "Attributes": NotRequired[Mapping[str, str]],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "RecommendationProviderIdType": NotRequired[str],
        "RecommendationTransformerUri": NotRequired[str],
        "RecommendationsDisplayName": NotRequired[str],
        "RecommendationsPerMessage": NotRequired[int],
    },
)

CreateSegmentRequestRequestTypeDef = TypedDict(
    "CreateSegmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "WriteSegmentRequest": "WriteSegmentRequestTypeDef",
    },
)

CreateSegmentResponseTypeDef = TypedDict(
    "CreateSegmentResponseTypeDef",
    {
        "SegmentResponse": "SegmentResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSmsTemplateRequestRequestTypeDef = TypedDict(
    "CreateSmsTemplateRequestRequestTypeDef",
    {
        "SMSTemplateRequest": "SMSTemplateRequestTypeDef",
        "TemplateName": str,
    },
)

CreateSmsTemplateResponseTypeDef = TypedDict(
    "CreateSmsTemplateResponseTypeDef",
    {
        "CreateTemplateMessageBody": "CreateTemplateMessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTemplateMessageBodyTypeDef = TypedDict(
    "CreateTemplateMessageBodyTypeDef",
    {
        "Arn": NotRequired[str],
        "Message": NotRequired[str],
        "RequestID": NotRequired[str],
    },
)

CreateVoiceTemplateRequestRequestTypeDef = TypedDict(
    "CreateVoiceTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "VoiceTemplateRequest": "VoiceTemplateRequestTypeDef",
    },
)

CreateVoiceTemplateResponseTypeDef = TypedDict(
    "CreateVoiceTemplateResponseTypeDef",
    {
        "CreateTemplateMessageBody": "CreateTemplateMessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomDeliveryConfigurationTypeDef = TypedDict(
    "CustomDeliveryConfigurationTypeDef",
    {
        "DeliveryUri": str,
        "EndpointTypes": NotRequired[Sequence[EndpointTypesElementType]],
    },
)

CustomMessageActivityTypeDef = TypedDict(
    "CustomMessageActivityTypeDef",
    {
        "DeliveryUri": NotRequired[str],
        "EndpointTypes": NotRequired[Sequence[EndpointTypesElementType]],
        "MessageConfig": NotRequired["JourneyCustomMessageTypeDef"],
        "NextActivity": NotRequired[str],
        "TemplateName": NotRequired[str],
        "TemplateVersion": NotRequired[str],
    },
)

DefaultButtonConfigurationTypeDef = TypedDict(
    "DefaultButtonConfigurationTypeDef",
    {
        "ButtonAction": ButtonActionType,
        "Text": str,
        "BackgroundColor": NotRequired[str],
        "BorderRadius": NotRequired[int],
        "Link": NotRequired[str],
        "TextColor": NotRequired[str],
    },
)

DefaultMessageTypeDef = TypedDict(
    "DefaultMessageTypeDef",
    {
        "Body": NotRequired[str],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
    },
)

DefaultPushNotificationMessageTypeDef = TypedDict(
    "DefaultPushNotificationMessageTypeDef",
    {
        "Action": NotRequired[ActionType],
        "Body": NotRequired[str],
        "Data": NotRequired[Mapping[str, str]],
        "SilentPush": NotRequired[bool],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
        "Title": NotRequired[str],
        "Url": NotRequired[str],
    },
)

DefaultPushNotificationTemplateTypeDef = TypedDict(
    "DefaultPushNotificationTemplateTypeDef",
    {
        "Action": NotRequired[ActionType],
        "Body": NotRequired[str],
        "Sound": NotRequired[str],
        "Title": NotRequired[str],
        "Url": NotRequired[str],
    },
)

DeleteAdmChannelRequestRequestTypeDef = TypedDict(
    "DeleteAdmChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteAdmChannelResponseTypeDef = TypedDict(
    "DeleteAdmChannelResponseTypeDef",
    {
        "ADMChannelResponse": "ADMChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApnsChannelRequestRequestTypeDef = TypedDict(
    "DeleteApnsChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteApnsChannelResponseTypeDef = TypedDict(
    "DeleteApnsChannelResponseTypeDef",
    {
        "APNSChannelResponse": "APNSChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApnsSandboxChannelRequestRequestTypeDef = TypedDict(
    "DeleteApnsSandboxChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteApnsSandboxChannelResponseTypeDef = TypedDict(
    "DeleteApnsSandboxChannelResponseTypeDef",
    {
        "APNSSandboxChannelResponse": "APNSSandboxChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApnsVoipChannelRequestRequestTypeDef = TypedDict(
    "DeleteApnsVoipChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteApnsVoipChannelResponseTypeDef = TypedDict(
    "DeleteApnsVoipChannelResponseTypeDef",
    {
        "APNSVoipChannelResponse": "APNSVoipChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApnsVoipSandboxChannelRequestRequestTypeDef = TypedDict(
    "DeleteApnsVoipSandboxChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteApnsVoipSandboxChannelResponseTypeDef = TypedDict(
    "DeleteApnsVoipSandboxChannelResponseTypeDef",
    {
        "APNSVoipSandboxChannelResponse": "APNSVoipSandboxChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAppRequestRequestTypeDef = TypedDict(
    "DeleteAppRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteAppResponseTypeDef = TypedDict(
    "DeleteAppResponseTypeDef",
    {
        "ApplicationResponse": "ApplicationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBaiduChannelRequestRequestTypeDef = TypedDict(
    "DeleteBaiduChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteBaiduChannelResponseTypeDef = TypedDict(
    "DeleteBaiduChannelResponseTypeDef",
    {
        "BaiduChannelResponse": "BaiduChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCampaignRequestRequestTypeDef = TypedDict(
    "DeleteCampaignRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
    },
)

DeleteCampaignResponseTypeDef = TypedDict(
    "DeleteCampaignResponseTypeDef",
    {
        "CampaignResponse": "CampaignResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEmailChannelRequestRequestTypeDef = TypedDict(
    "DeleteEmailChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteEmailChannelResponseTypeDef = TypedDict(
    "DeleteEmailChannelResponseTypeDef",
    {
        "EmailChannelResponse": "EmailChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEmailTemplateRequestRequestTypeDef = TypedDict(
    "DeleteEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "Version": NotRequired[str],
    },
)

DeleteEmailTemplateResponseTypeDef = TypedDict(
    "DeleteEmailTemplateResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEndpointRequestRequestTypeDef = TypedDict(
    "DeleteEndpointRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EndpointId": str,
    },
)

DeleteEndpointResponseTypeDef = TypedDict(
    "DeleteEndpointResponseTypeDef",
    {
        "EndpointResponse": "EndpointResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEventStreamRequestRequestTypeDef = TypedDict(
    "DeleteEventStreamRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteEventStreamResponseTypeDef = TypedDict(
    "DeleteEventStreamResponseTypeDef",
    {
        "EventStream": "EventStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGcmChannelRequestRequestTypeDef = TypedDict(
    "DeleteGcmChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteGcmChannelResponseTypeDef = TypedDict(
    "DeleteGcmChannelResponseTypeDef",
    {
        "GCMChannelResponse": "GCMChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInAppTemplateRequestRequestTypeDef = TypedDict(
    "DeleteInAppTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "Version": NotRequired[str],
    },
)

DeleteInAppTemplateResponseTypeDef = TypedDict(
    "DeleteInAppTemplateResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteJourneyRequestRequestTypeDef = TypedDict(
    "DeleteJourneyRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
    },
)

DeleteJourneyResponseTypeDef = TypedDict(
    "DeleteJourneyResponseTypeDef",
    {
        "JourneyResponse": "JourneyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePushTemplateRequestRequestTypeDef = TypedDict(
    "DeletePushTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "Version": NotRequired[str],
    },
)

DeletePushTemplateResponseTypeDef = TypedDict(
    "DeletePushTemplateResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRecommenderConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteRecommenderConfigurationRequestRequestTypeDef",
    {
        "RecommenderId": str,
    },
)

DeleteRecommenderConfigurationResponseTypeDef = TypedDict(
    "DeleteRecommenderConfigurationResponseTypeDef",
    {
        "RecommenderConfigurationResponse": "RecommenderConfigurationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSegmentRequestRequestTypeDef = TypedDict(
    "DeleteSegmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
    },
)

DeleteSegmentResponseTypeDef = TypedDict(
    "DeleteSegmentResponseTypeDef",
    {
        "SegmentResponse": "SegmentResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSmsChannelRequestRequestTypeDef = TypedDict(
    "DeleteSmsChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteSmsChannelResponseTypeDef = TypedDict(
    "DeleteSmsChannelResponseTypeDef",
    {
        "SMSChannelResponse": "SMSChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSmsTemplateRequestRequestTypeDef = TypedDict(
    "DeleteSmsTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "Version": NotRequired[str],
    },
)

DeleteSmsTemplateResponseTypeDef = TypedDict(
    "DeleteSmsTemplateResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUserEndpointsRequestRequestTypeDef = TypedDict(
    "DeleteUserEndpointsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "UserId": str,
    },
)

DeleteUserEndpointsResponseTypeDef = TypedDict(
    "DeleteUserEndpointsResponseTypeDef",
    {
        "EndpointsResponse": "EndpointsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVoiceChannelRequestRequestTypeDef = TypedDict(
    "DeleteVoiceChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteVoiceChannelResponseTypeDef = TypedDict(
    "DeleteVoiceChannelResponseTypeDef",
    {
        "VoiceChannelResponse": "VoiceChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVoiceTemplateRequestRequestTypeDef = TypedDict(
    "DeleteVoiceTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "Version": NotRequired[str],
    },
)

DeleteVoiceTemplateResponseTypeDef = TypedDict(
    "DeleteVoiceTemplateResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DirectMessageConfigurationTypeDef = TypedDict(
    "DirectMessageConfigurationTypeDef",
    {
        "ADMMessage": NotRequired["ADMMessageTypeDef"],
        "APNSMessage": NotRequired["APNSMessageTypeDef"],
        "BaiduMessage": NotRequired["BaiduMessageTypeDef"],
        "DefaultMessage": NotRequired["DefaultMessageTypeDef"],
        "DefaultPushNotificationMessage": NotRequired["DefaultPushNotificationMessageTypeDef"],
        "EmailMessage": NotRequired["EmailMessageTypeDef"],
        "GCMMessage": NotRequired["GCMMessageTypeDef"],
        "SMSMessage": NotRequired["SMSMessageTypeDef"],
        "VoiceMessage": NotRequired["VoiceMessageTypeDef"],
    },
)

EmailChannelRequestTypeDef = TypedDict(
    "EmailChannelRequestTypeDef",
    {
        "FromAddress": str,
        "Identity": str,
        "ConfigurationSet": NotRequired[str],
        "Enabled": NotRequired[bool],
        "RoleArn": NotRequired[str],
    },
)

EmailChannelResponseTypeDef = TypedDict(
    "EmailChannelResponseTypeDef",
    {
        "Platform": str,
        "ApplicationId": NotRequired[str],
        "ConfigurationSet": NotRequired[str],
        "CreationDate": NotRequired[str],
        "Enabled": NotRequired[bool],
        "FromAddress": NotRequired[str],
        "HasCredential": NotRequired[bool],
        "Id": NotRequired[str],
        "Identity": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "MessagesPerSecond": NotRequired[int],
        "RoleArn": NotRequired[str],
        "Version": NotRequired[int],
    },
)

EmailMessageActivityTypeDef = TypedDict(
    "EmailMessageActivityTypeDef",
    {
        "MessageConfig": NotRequired["JourneyEmailMessageTypeDef"],
        "NextActivity": NotRequired[str],
        "TemplateName": NotRequired[str],
        "TemplateVersion": NotRequired[str],
    },
)

EmailMessageTypeDef = TypedDict(
    "EmailMessageTypeDef",
    {
        "Body": NotRequired[str],
        "FeedbackForwardingAddress": NotRequired[str],
        "FromAddress": NotRequired[str],
        "RawEmail": NotRequired["RawEmailTypeDef"],
        "ReplyToAddresses": NotRequired[Sequence[str]],
        "SimpleEmail": NotRequired["SimpleEmailTypeDef"],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
    },
)

EmailTemplateRequestTypeDef = TypedDict(
    "EmailTemplateRequestTypeDef",
    {
        "DefaultSubstitutions": NotRequired[str],
        "HtmlPart": NotRequired[str],
        "RecommenderId": NotRequired[str],
        "Subject": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "TemplateDescription": NotRequired[str],
        "TextPart": NotRequired[str],
    },
)

EmailTemplateResponseTypeDef = TypedDict(
    "EmailTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
        "Arn": NotRequired[str],
        "DefaultSubstitutions": NotRequired[str],
        "HtmlPart": NotRequired[str],
        "RecommenderId": NotRequired[str],
        "Subject": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "TemplateDescription": NotRequired[str],
        "TextPart": NotRequired[str],
        "Version": NotRequired[str],
    },
)

EndpointBatchItemTypeDef = TypedDict(
    "EndpointBatchItemTypeDef",
    {
        "Address": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, Sequence[str]]],
        "ChannelType": NotRequired[ChannelTypeType],
        "Demographic": NotRequired["EndpointDemographicTypeDef"],
        "EffectiveDate": NotRequired[str],
        "EndpointStatus": NotRequired[str],
        "Id": NotRequired[str],
        "Location": NotRequired["EndpointLocationTypeDef"],
        "Metrics": NotRequired[Mapping[str, float]],
        "OptOut": NotRequired[str],
        "RequestId": NotRequired[str],
        "User": NotRequired["EndpointUserTypeDef"],
    },
)

EndpointBatchRequestTypeDef = TypedDict(
    "EndpointBatchRequestTypeDef",
    {
        "Item": Sequence["EndpointBatchItemTypeDef"],
    },
)

EndpointDemographicTypeDef = TypedDict(
    "EndpointDemographicTypeDef",
    {
        "AppVersion": NotRequired[str],
        "Locale": NotRequired[str],
        "Make": NotRequired[str],
        "Model": NotRequired[str],
        "ModelVersion": NotRequired[str],
        "Platform": NotRequired[str],
        "PlatformVersion": NotRequired[str],
        "Timezone": NotRequired[str],
    },
)

EndpointItemResponseTypeDef = TypedDict(
    "EndpointItemResponseTypeDef",
    {
        "Message": NotRequired[str],
        "StatusCode": NotRequired[int],
    },
)

EndpointLocationTypeDef = TypedDict(
    "EndpointLocationTypeDef",
    {
        "City": NotRequired[str],
        "Country": NotRequired[str],
        "Latitude": NotRequired[float],
        "Longitude": NotRequired[float],
        "PostalCode": NotRequired[str],
        "Region": NotRequired[str],
    },
)

EndpointMessageResultTypeDef = TypedDict(
    "EndpointMessageResultTypeDef",
    {
        "DeliveryStatus": DeliveryStatusType,
        "StatusCode": int,
        "Address": NotRequired[str],
        "MessageId": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "UpdatedToken": NotRequired[str],
    },
)

EndpointRequestTypeDef = TypedDict(
    "EndpointRequestTypeDef",
    {
        "Address": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, Sequence[str]]],
        "ChannelType": NotRequired[ChannelTypeType],
        "Demographic": NotRequired["EndpointDemographicTypeDef"],
        "EffectiveDate": NotRequired[str],
        "EndpointStatus": NotRequired[str],
        "Location": NotRequired["EndpointLocationTypeDef"],
        "Metrics": NotRequired[Mapping[str, float]],
        "OptOut": NotRequired[str],
        "RequestId": NotRequired[str],
        "User": NotRequired["EndpointUserTypeDef"],
    },
)

EndpointResponseTypeDef = TypedDict(
    "EndpointResponseTypeDef",
    {
        "Address": NotRequired[str],
        "ApplicationId": NotRequired[str],
        "Attributes": NotRequired[Dict[str, List[str]]],
        "ChannelType": NotRequired[ChannelTypeType],
        "CohortId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "Demographic": NotRequired["EndpointDemographicTypeDef"],
        "EffectiveDate": NotRequired[str],
        "EndpointStatus": NotRequired[str],
        "Id": NotRequired[str],
        "Location": NotRequired["EndpointLocationTypeDef"],
        "Metrics": NotRequired[Dict[str, float]],
        "OptOut": NotRequired[str],
        "RequestId": NotRequired[str],
        "User": NotRequired["EndpointUserTypeDef"],
    },
)

EndpointSendConfigurationTypeDef = TypedDict(
    "EndpointSendConfigurationTypeDef",
    {
        "BodyOverride": NotRequired[str],
        "Context": NotRequired[Mapping[str, str]],
        "RawContent": NotRequired[str],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
        "TitleOverride": NotRequired[str],
    },
)

EndpointUserTypeDef = TypedDict(
    "EndpointUserTypeDef",
    {
        "UserAttributes": NotRequired[Dict[str, List[str]]],
        "UserId": NotRequired[str],
    },
)

EndpointsResponseTypeDef = TypedDict(
    "EndpointsResponseTypeDef",
    {
        "Item": List["EndpointResponseTypeDef"],
    },
)

EventConditionTypeDef = TypedDict(
    "EventConditionTypeDef",
    {
        "Dimensions": NotRequired["EventDimensionsTypeDef"],
        "MessageActivity": NotRequired[str],
    },
)

EventDimensionsTypeDef = TypedDict(
    "EventDimensionsTypeDef",
    {
        "Attributes": NotRequired[Mapping[str, "AttributeDimensionTypeDef"]],
        "EventType": NotRequired["SetDimensionTypeDef"],
        "Metrics": NotRequired[Mapping[str, "MetricDimensionTypeDef"]],
    },
)

EventFilterTypeDef = TypedDict(
    "EventFilterTypeDef",
    {
        "Dimensions": "EventDimensionsTypeDef",
        "FilterType": FilterTypeType,
    },
)

EventItemResponseTypeDef = TypedDict(
    "EventItemResponseTypeDef",
    {
        "Message": NotRequired[str],
        "StatusCode": NotRequired[int],
    },
)

EventStartConditionTypeDef = TypedDict(
    "EventStartConditionTypeDef",
    {
        "EventFilter": NotRequired["EventFilterTypeDef"],
        "SegmentId": NotRequired[str],
    },
)

EventStreamTypeDef = TypedDict(
    "EventStreamTypeDef",
    {
        "ApplicationId": str,
        "DestinationStreamArn": str,
        "RoleArn": str,
        "ExternalId": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "LastUpdatedBy": NotRequired[str],
    },
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "EventType": str,
        "Timestamp": str,
        "AppPackageName": NotRequired[str],
        "AppTitle": NotRequired[str],
        "AppVersionCode": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
        "ClientSdkVersion": NotRequired[str],
        "Metrics": NotRequired[Mapping[str, float]],
        "SdkName": NotRequired[str],
        "Session": NotRequired["SessionTypeDef"],
    },
)

EventsBatchTypeDef = TypedDict(
    "EventsBatchTypeDef",
    {
        "Endpoint": "PublicEndpointTypeDef",
        "Events": Mapping[str, "EventTypeDef"],
    },
)

EventsRequestTypeDef = TypedDict(
    "EventsRequestTypeDef",
    {
        "BatchItem": Mapping[str, "EventsBatchTypeDef"],
    },
)

EventsResponseTypeDef = TypedDict(
    "EventsResponseTypeDef",
    {
        "Results": NotRequired[Dict[str, "ItemResponseTypeDef"]],
    },
)

ExportJobRequestTypeDef = TypedDict(
    "ExportJobRequestTypeDef",
    {
        "RoleArn": str,
        "S3UrlPrefix": str,
        "SegmentId": NotRequired[str],
        "SegmentVersion": NotRequired[int],
    },
)

ExportJobResourceTypeDef = TypedDict(
    "ExportJobResourceTypeDef",
    {
        "RoleArn": str,
        "S3UrlPrefix": str,
        "SegmentId": NotRequired[str],
        "SegmentVersion": NotRequired[int],
    },
)

ExportJobResponseTypeDef = TypedDict(
    "ExportJobResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Definition": "ExportJobResourceTypeDef",
        "Id": str,
        "JobStatus": JobStatusType,
        "Type": str,
        "CompletedPieces": NotRequired[int],
        "CompletionDate": NotRequired[str],
        "FailedPieces": NotRequired[int],
        "Failures": NotRequired[List[str]],
        "TotalFailures": NotRequired[int],
        "TotalPieces": NotRequired[int],
        "TotalProcessed": NotRequired[int],
    },
)

ExportJobsResponseTypeDef = TypedDict(
    "ExportJobsResponseTypeDef",
    {
        "Item": List["ExportJobResponseTypeDef"],
        "NextToken": NotRequired[str],
    },
)

GCMChannelRequestTypeDef = TypedDict(
    "GCMChannelRequestTypeDef",
    {
        "ApiKey": str,
        "Enabled": NotRequired[bool],
    },
)

GCMChannelResponseTypeDef = TypedDict(
    "GCMChannelResponseTypeDef",
    {
        "Credential": str,
        "Platform": str,
        "ApplicationId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "Enabled": NotRequired[bool],
        "HasCredential": NotRequired[bool],
        "Id": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Version": NotRequired[int],
    },
)

GCMMessageTypeDef = TypedDict(
    "GCMMessageTypeDef",
    {
        "Action": NotRequired[ActionType],
        "Body": NotRequired[str],
        "CollapseKey": NotRequired[str],
        "Data": NotRequired[Mapping[str, str]],
        "IconReference": NotRequired[str],
        "ImageIconUrl": NotRequired[str],
        "ImageUrl": NotRequired[str],
        "Priority": NotRequired[str],
        "RawContent": NotRequired[str],
        "RestrictedPackageName": NotRequired[str],
        "SilentPush": NotRequired[bool],
        "SmallImageIconUrl": NotRequired[str],
        "Sound": NotRequired[str],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
        "TimeToLive": NotRequired[int],
        "Title": NotRequired[str],
        "Url": NotRequired[str],
    },
)

GPSCoordinatesTypeDef = TypedDict(
    "GPSCoordinatesTypeDef",
    {
        "Latitude": float,
        "Longitude": float,
    },
)

GPSPointDimensionTypeDef = TypedDict(
    "GPSPointDimensionTypeDef",
    {
        "Coordinates": "GPSCoordinatesTypeDef",
        "RangeInKilometers": NotRequired[float],
    },
)

GetAdmChannelRequestRequestTypeDef = TypedDict(
    "GetAdmChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetAdmChannelResponseTypeDef = TypedDict(
    "GetAdmChannelResponseTypeDef",
    {
        "ADMChannelResponse": "ADMChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApnsChannelRequestRequestTypeDef = TypedDict(
    "GetApnsChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetApnsChannelResponseTypeDef = TypedDict(
    "GetApnsChannelResponseTypeDef",
    {
        "APNSChannelResponse": "APNSChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApnsSandboxChannelRequestRequestTypeDef = TypedDict(
    "GetApnsSandboxChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetApnsSandboxChannelResponseTypeDef = TypedDict(
    "GetApnsSandboxChannelResponseTypeDef",
    {
        "APNSSandboxChannelResponse": "APNSSandboxChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApnsVoipChannelRequestRequestTypeDef = TypedDict(
    "GetApnsVoipChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetApnsVoipChannelResponseTypeDef = TypedDict(
    "GetApnsVoipChannelResponseTypeDef",
    {
        "APNSVoipChannelResponse": "APNSVoipChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApnsVoipSandboxChannelRequestRequestTypeDef = TypedDict(
    "GetApnsVoipSandboxChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetApnsVoipSandboxChannelResponseTypeDef = TypedDict(
    "GetApnsVoipSandboxChannelResponseTypeDef",
    {
        "APNSVoipSandboxChannelResponse": "APNSVoipSandboxChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppRequestRequestTypeDef = TypedDict(
    "GetAppRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetAppResponseTypeDef = TypedDict(
    "GetAppResponseTypeDef",
    {
        "ApplicationResponse": "ApplicationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApplicationDateRangeKpiRequestRequestTypeDef = TypedDict(
    "GetApplicationDateRangeKpiRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "KpiName": str,
        "EndTime": NotRequired[Union[datetime, str]],
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[str],
        "StartTime": NotRequired[Union[datetime, str]],
    },
)

GetApplicationDateRangeKpiResponseTypeDef = TypedDict(
    "GetApplicationDateRangeKpiResponseTypeDef",
    {
        "ApplicationDateRangeKpiResponse": "ApplicationDateRangeKpiResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApplicationSettingsRequestRequestTypeDef = TypedDict(
    "GetApplicationSettingsRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetApplicationSettingsResponseTypeDef = TypedDict(
    "GetApplicationSettingsResponseTypeDef",
    {
        "ApplicationSettingsResource": "ApplicationSettingsResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppsRequestRequestTypeDef = TypedDict(
    "GetAppsRequestRequestTypeDef",
    {
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)

GetAppsResponseTypeDef = TypedDict(
    "GetAppsResponseTypeDef",
    {
        "ApplicationsResponse": "ApplicationsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBaiduChannelRequestRequestTypeDef = TypedDict(
    "GetBaiduChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetBaiduChannelResponseTypeDef = TypedDict(
    "GetBaiduChannelResponseTypeDef",
    {
        "BaiduChannelResponse": "BaiduChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCampaignActivitiesRequestRequestTypeDef = TypedDict(
    "GetCampaignActivitiesRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)

GetCampaignActivitiesResponseTypeDef = TypedDict(
    "GetCampaignActivitiesResponseTypeDef",
    {
        "ActivitiesResponse": "ActivitiesResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCampaignDateRangeKpiRequestRequestTypeDef = TypedDict(
    "GetCampaignDateRangeKpiRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "KpiName": str,
        "EndTime": NotRequired[Union[datetime, str]],
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[str],
        "StartTime": NotRequired[Union[datetime, str]],
    },
)

GetCampaignDateRangeKpiResponseTypeDef = TypedDict(
    "GetCampaignDateRangeKpiResponseTypeDef",
    {
        "CampaignDateRangeKpiResponse": "CampaignDateRangeKpiResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCampaignRequestRequestTypeDef = TypedDict(
    "GetCampaignRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
    },
)

GetCampaignResponseTypeDef = TypedDict(
    "GetCampaignResponseTypeDef",
    {
        "CampaignResponse": "CampaignResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCampaignVersionRequestRequestTypeDef = TypedDict(
    "GetCampaignVersionRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "Version": str,
    },
)

GetCampaignVersionResponseTypeDef = TypedDict(
    "GetCampaignVersionResponseTypeDef",
    {
        "CampaignResponse": "CampaignResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCampaignVersionsRequestRequestTypeDef = TypedDict(
    "GetCampaignVersionsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)

GetCampaignVersionsResponseTypeDef = TypedDict(
    "GetCampaignVersionsResponseTypeDef",
    {
        "CampaignsResponse": "CampaignsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCampaignsRequestRequestTypeDef = TypedDict(
    "GetCampaignsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)

GetCampaignsResponseTypeDef = TypedDict(
    "GetCampaignsResponseTypeDef",
    {
        "CampaignsResponse": "CampaignsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChannelsRequestRequestTypeDef = TypedDict(
    "GetChannelsRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetChannelsResponseTypeDef = TypedDict(
    "GetChannelsResponseTypeDef",
    {
        "ChannelsResponse": "ChannelsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEmailChannelRequestRequestTypeDef = TypedDict(
    "GetEmailChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetEmailChannelResponseTypeDef = TypedDict(
    "GetEmailChannelResponseTypeDef",
    {
        "EmailChannelResponse": "EmailChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEmailTemplateRequestRequestTypeDef = TypedDict(
    "GetEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "Version": NotRequired[str],
    },
)

GetEmailTemplateResponseTypeDef = TypedDict(
    "GetEmailTemplateResponseTypeDef",
    {
        "EmailTemplateResponse": "EmailTemplateResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEndpointRequestRequestTypeDef = TypedDict(
    "GetEndpointRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EndpointId": str,
    },
)

GetEndpointResponseTypeDef = TypedDict(
    "GetEndpointResponseTypeDef",
    {
        "EndpointResponse": "EndpointResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventStreamRequestRequestTypeDef = TypedDict(
    "GetEventStreamRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetEventStreamResponseTypeDef = TypedDict(
    "GetEventStreamResponseTypeDef",
    {
        "EventStream": "EventStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExportJobRequestRequestTypeDef = TypedDict(
    "GetExportJobRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JobId": str,
    },
)

GetExportJobResponseTypeDef = TypedDict(
    "GetExportJobResponseTypeDef",
    {
        "ExportJobResponse": "ExportJobResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExportJobsRequestRequestTypeDef = TypedDict(
    "GetExportJobsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)

GetExportJobsResponseTypeDef = TypedDict(
    "GetExportJobsResponseTypeDef",
    {
        "ExportJobsResponse": "ExportJobsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGcmChannelRequestRequestTypeDef = TypedDict(
    "GetGcmChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetGcmChannelResponseTypeDef = TypedDict(
    "GetGcmChannelResponseTypeDef",
    {
        "GCMChannelResponse": "GCMChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImportJobRequestRequestTypeDef = TypedDict(
    "GetImportJobRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JobId": str,
    },
)

GetImportJobResponseTypeDef = TypedDict(
    "GetImportJobResponseTypeDef",
    {
        "ImportJobResponse": "ImportJobResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImportJobsRequestRequestTypeDef = TypedDict(
    "GetImportJobsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)

GetImportJobsResponseTypeDef = TypedDict(
    "GetImportJobsResponseTypeDef",
    {
        "ImportJobsResponse": "ImportJobsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInAppMessagesRequestRequestTypeDef = TypedDict(
    "GetInAppMessagesRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EndpointId": str,
    },
)

GetInAppMessagesResponseTypeDef = TypedDict(
    "GetInAppMessagesResponseTypeDef",
    {
        "InAppMessagesResponse": "InAppMessagesResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInAppTemplateRequestRequestTypeDef = TypedDict(
    "GetInAppTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "Version": NotRequired[str],
    },
)

GetInAppTemplateResponseTypeDef = TypedDict(
    "GetInAppTemplateResponseTypeDef",
    {
        "InAppTemplateResponse": "InAppTemplateResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJourneyDateRangeKpiRequestRequestTypeDef = TypedDict(
    "GetJourneyDateRangeKpiRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
        "KpiName": str,
        "EndTime": NotRequired[Union[datetime, str]],
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[str],
        "StartTime": NotRequired[Union[datetime, str]],
    },
)

GetJourneyDateRangeKpiResponseTypeDef = TypedDict(
    "GetJourneyDateRangeKpiResponseTypeDef",
    {
        "JourneyDateRangeKpiResponse": "JourneyDateRangeKpiResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJourneyExecutionActivityMetricsRequestRequestTypeDef = TypedDict(
    "GetJourneyExecutionActivityMetricsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyActivityId": str,
        "JourneyId": str,
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[str],
    },
)

GetJourneyExecutionActivityMetricsResponseTypeDef = TypedDict(
    "GetJourneyExecutionActivityMetricsResponseTypeDef",
    {
        "JourneyExecutionActivityMetricsResponse": "JourneyExecutionActivityMetricsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJourneyExecutionMetricsRequestRequestTypeDef = TypedDict(
    "GetJourneyExecutionMetricsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[str],
    },
)

GetJourneyExecutionMetricsResponseTypeDef = TypedDict(
    "GetJourneyExecutionMetricsResponseTypeDef",
    {
        "JourneyExecutionMetricsResponse": "JourneyExecutionMetricsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJourneyRequestRequestTypeDef = TypedDict(
    "GetJourneyRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
    },
)

GetJourneyResponseTypeDef = TypedDict(
    "GetJourneyResponseTypeDef",
    {
        "JourneyResponse": "JourneyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPushTemplateRequestRequestTypeDef = TypedDict(
    "GetPushTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "Version": NotRequired[str],
    },
)

GetPushTemplateResponseTypeDef = TypedDict(
    "GetPushTemplateResponseTypeDef",
    {
        "PushNotificationTemplateResponse": "PushNotificationTemplateResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecommenderConfigurationRequestRequestTypeDef = TypedDict(
    "GetRecommenderConfigurationRequestRequestTypeDef",
    {
        "RecommenderId": str,
    },
)

GetRecommenderConfigurationResponseTypeDef = TypedDict(
    "GetRecommenderConfigurationResponseTypeDef",
    {
        "RecommenderConfigurationResponse": "RecommenderConfigurationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecommenderConfigurationsRequestRequestTypeDef = TypedDict(
    "GetRecommenderConfigurationsRequestRequestTypeDef",
    {
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)

GetRecommenderConfigurationsResponseTypeDef = TypedDict(
    "GetRecommenderConfigurationsResponseTypeDef",
    {
        "ListRecommenderConfigurationsResponse": "ListRecommenderConfigurationsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSegmentExportJobsRequestRequestTypeDef = TypedDict(
    "GetSegmentExportJobsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)

GetSegmentExportJobsResponseTypeDef = TypedDict(
    "GetSegmentExportJobsResponseTypeDef",
    {
        "ExportJobsResponse": "ExportJobsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSegmentImportJobsRequestRequestTypeDef = TypedDict(
    "GetSegmentImportJobsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)

GetSegmentImportJobsResponseTypeDef = TypedDict(
    "GetSegmentImportJobsResponseTypeDef",
    {
        "ImportJobsResponse": "ImportJobsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSegmentRequestRequestTypeDef = TypedDict(
    "GetSegmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
    },
)

GetSegmentResponseTypeDef = TypedDict(
    "GetSegmentResponseTypeDef",
    {
        "SegmentResponse": "SegmentResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSegmentVersionRequestRequestTypeDef = TypedDict(
    "GetSegmentVersionRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
        "Version": str,
    },
)

GetSegmentVersionResponseTypeDef = TypedDict(
    "GetSegmentVersionResponseTypeDef",
    {
        "SegmentResponse": "SegmentResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSegmentVersionsRequestRequestTypeDef = TypedDict(
    "GetSegmentVersionsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)

GetSegmentVersionsResponseTypeDef = TypedDict(
    "GetSegmentVersionsResponseTypeDef",
    {
        "SegmentsResponse": "SegmentsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSegmentsRequestRequestTypeDef = TypedDict(
    "GetSegmentsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)

GetSegmentsResponseTypeDef = TypedDict(
    "GetSegmentsResponseTypeDef",
    {
        "SegmentsResponse": "SegmentsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSmsChannelRequestRequestTypeDef = TypedDict(
    "GetSmsChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetSmsChannelResponseTypeDef = TypedDict(
    "GetSmsChannelResponseTypeDef",
    {
        "SMSChannelResponse": "SMSChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSmsTemplateRequestRequestTypeDef = TypedDict(
    "GetSmsTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "Version": NotRequired[str],
    },
)

GetSmsTemplateResponseTypeDef = TypedDict(
    "GetSmsTemplateResponseTypeDef",
    {
        "SMSTemplateResponse": "SMSTemplateResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserEndpointsRequestRequestTypeDef = TypedDict(
    "GetUserEndpointsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "UserId": str,
    },
)

GetUserEndpointsResponseTypeDef = TypedDict(
    "GetUserEndpointsResponseTypeDef",
    {
        "EndpointsResponse": "EndpointsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceChannelRequestRequestTypeDef = TypedDict(
    "GetVoiceChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetVoiceChannelResponseTypeDef = TypedDict(
    "GetVoiceChannelResponseTypeDef",
    {
        "VoiceChannelResponse": "VoiceChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceTemplateRequestRequestTypeDef = TypedDict(
    "GetVoiceTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "Version": NotRequired[str],
    },
)

GetVoiceTemplateResponseTypeDef = TypedDict(
    "GetVoiceTemplateResponseTypeDef",
    {
        "VoiceTemplateResponse": "VoiceTemplateResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HoldoutActivityTypeDef = TypedDict(
    "HoldoutActivityTypeDef",
    {
        "Percentage": int,
        "NextActivity": NotRequired[str],
    },
)

ImportJobRequestTypeDef = TypedDict(
    "ImportJobRequestTypeDef",
    {
        "Format": FormatType,
        "RoleArn": str,
        "S3Url": str,
        "DefineSegment": NotRequired[bool],
        "ExternalId": NotRequired[str],
        "RegisterEndpoints": NotRequired[bool],
        "SegmentId": NotRequired[str],
        "SegmentName": NotRequired[str],
    },
)

ImportJobResourceTypeDef = TypedDict(
    "ImportJobResourceTypeDef",
    {
        "Format": FormatType,
        "RoleArn": str,
        "S3Url": str,
        "DefineSegment": NotRequired[bool],
        "ExternalId": NotRequired[str],
        "RegisterEndpoints": NotRequired[bool],
        "SegmentId": NotRequired[str],
        "SegmentName": NotRequired[str],
    },
)

ImportJobResponseTypeDef = TypedDict(
    "ImportJobResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Definition": "ImportJobResourceTypeDef",
        "Id": str,
        "JobStatus": JobStatusType,
        "Type": str,
        "CompletedPieces": NotRequired[int],
        "CompletionDate": NotRequired[str],
        "FailedPieces": NotRequired[int],
        "Failures": NotRequired[List[str]],
        "TotalFailures": NotRequired[int],
        "TotalPieces": NotRequired[int],
        "TotalProcessed": NotRequired[int],
    },
)

ImportJobsResponseTypeDef = TypedDict(
    "ImportJobsResponseTypeDef",
    {
        "Item": List["ImportJobResponseTypeDef"],
        "NextToken": NotRequired[str],
    },
)

InAppCampaignScheduleTypeDef = TypedDict(
    "InAppCampaignScheduleTypeDef",
    {
        "EndDate": NotRequired[str],
        "EventFilter": NotRequired["CampaignEventFilterTypeDef"],
        "QuietTime": NotRequired["QuietTimeTypeDef"],
    },
)

InAppMessageBodyConfigTypeDef = TypedDict(
    "InAppMessageBodyConfigTypeDef",
    {
        "Alignment": AlignmentType,
        "Body": str,
        "TextColor": str,
    },
)

InAppMessageButtonTypeDef = TypedDict(
    "InAppMessageButtonTypeDef",
    {
        "Android": NotRequired["OverrideButtonConfigurationTypeDef"],
        "DefaultConfig": NotRequired["DefaultButtonConfigurationTypeDef"],
        "IOS": NotRequired["OverrideButtonConfigurationTypeDef"],
        "Web": NotRequired["OverrideButtonConfigurationTypeDef"],
    },
)

InAppMessageCampaignTypeDef = TypedDict(
    "InAppMessageCampaignTypeDef",
    {
        "CampaignId": NotRequired[str],
        "DailyCap": NotRequired[int],
        "InAppMessage": NotRequired["InAppMessageTypeDef"],
        "Priority": NotRequired[int],
        "Schedule": NotRequired["InAppCampaignScheduleTypeDef"],
        "SessionCap": NotRequired[int],
        "TotalCap": NotRequired[int],
        "TreatmentId": NotRequired[str],
    },
)

InAppMessageContentTypeDef = TypedDict(
    "InAppMessageContentTypeDef",
    {
        "BackgroundColor": NotRequired[str],
        "BodyConfig": NotRequired["InAppMessageBodyConfigTypeDef"],
        "HeaderConfig": NotRequired["InAppMessageHeaderConfigTypeDef"],
        "ImageUrl": NotRequired[str],
        "PrimaryBtn": NotRequired["InAppMessageButtonTypeDef"],
        "SecondaryBtn": NotRequired["InAppMessageButtonTypeDef"],
    },
)

InAppMessageHeaderConfigTypeDef = TypedDict(
    "InAppMessageHeaderConfigTypeDef",
    {
        "Alignment": AlignmentType,
        "Header": str,
        "TextColor": str,
    },
)

InAppMessageTypeDef = TypedDict(
    "InAppMessageTypeDef",
    {
        "Content": NotRequired[List["InAppMessageContentTypeDef"]],
        "CustomConfig": NotRequired[Dict[str, str]],
        "Layout": NotRequired[LayoutType],
    },
)

InAppMessagesResponseTypeDef = TypedDict(
    "InAppMessagesResponseTypeDef",
    {
        "InAppMessageCampaigns": NotRequired[List["InAppMessageCampaignTypeDef"]],
    },
)

InAppTemplateRequestTypeDef = TypedDict(
    "InAppTemplateRequestTypeDef",
    {
        "Content": NotRequired[Sequence["InAppMessageContentTypeDef"]],
        "CustomConfig": NotRequired[Mapping[str, str]],
        "Layout": NotRequired[LayoutType],
        "tags": NotRequired[Mapping[str, str]],
        "TemplateDescription": NotRequired[str],
    },
)

InAppTemplateResponseTypeDef = TypedDict(
    "InAppTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
        "Arn": NotRequired[str],
        "Content": NotRequired[List["InAppMessageContentTypeDef"]],
        "CustomConfig": NotRequired[Dict[str, str]],
        "Layout": NotRequired[LayoutType],
        "tags": NotRequired[Dict[str, str]],
        "TemplateDescription": NotRequired[str],
        "Version": NotRequired[str],
    },
)

ItemResponseTypeDef = TypedDict(
    "ItemResponseTypeDef",
    {
        "EndpointItemResponse": NotRequired["EndpointItemResponseTypeDef"],
        "EventsItemResponse": NotRequired[Dict[str, "EventItemResponseTypeDef"]],
    },
)

JourneyChannelSettingsTypeDef = TypedDict(
    "JourneyChannelSettingsTypeDef",
    {
        "ConnectCampaignArn": NotRequired[str],
        "ConnectCampaignExecutionRoleArn": NotRequired[str],
    },
)

JourneyCustomMessageTypeDef = TypedDict(
    "JourneyCustomMessageTypeDef",
    {
        "Data": NotRequired[str],
    },
)

JourneyDateRangeKpiResponseTypeDef = TypedDict(
    "JourneyDateRangeKpiResponseTypeDef",
    {
        "ApplicationId": str,
        "EndTime": datetime,
        "JourneyId": str,
        "KpiName": str,
        "KpiResult": "BaseKpiResultTypeDef",
        "StartTime": datetime,
        "NextToken": NotRequired[str],
    },
)

JourneyEmailMessageTypeDef = TypedDict(
    "JourneyEmailMessageTypeDef",
    {
        "FromAddress": NotRequired[str],
    },
)

JourneyExecutionActivityMetricsResponseTypeDef = TypedDict(
    "JourneyExecutionActivityMetricsResponseTypeDef",
    {
        "ActivityType": str,
        "ApplicationId": str,
        "JourneyActivityId": str,
        "JourneyId": str,
        "LastEvaluatedTime": str,
        "Metrics": Dict[str, str],
    },
)

JourneyExecutionMetricsResponseTypeDef = TypedDict(
    "JourneyExecutionMetricsResponseTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
        "LastEvaluatedTime": str,
        "Metrics": Dict[str, str],
    },
)

JourneyLimitsTypeDef = TypedDict(
    "JourneyLimitsTypeDef",
    {
        "DailyCap": NotRequired[int],
        "EndpointReentryCap": NotRequired[int],
        "MessagesPerSecond": NotRequired[int],
        "EndpointReentryInterval": NotRequired[str],
    },
)

JourneyPushMessageTypeDef = TypedDict(
    "JourneyPushMessageTypeDef",
    {
        "TimeToLive": NotRequired[str],
    },
)

JourneyResponseTypeDef = TypedDict(
    "JourneyResponseTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Activities": NotRequired[Dict[str, "ActivityTypeDef"]],
        "CreationDate": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Limits": NotRequired["JourneyLimitsTypeDef"],
        "LocalTime": NotRequired[bool],
        "QuietTime": NotRequired["QuietTimeTypeDef"],
        "RefreshFrequency": NotRequired[str],
        "Schedule": NotRequired["JourneyScheduleTypeDef"],
        "StartActivity": NotRequired[str],
        "StartCondition": NotRequired["StartConditionTypeDef"],
        "State": NotRequired[StateType],
        "tags": NotRequired[Dict[str, str]],
        "WaitForQuietTime": NotRequired[bool],
        "RefreshOnSegmentUpdate": NotRequired[bool],
        "JourneyChannelSettings": NotRequired["JourneyChannelSettingsTypeDef"],
    },
)

JourneySMSMessageTypeDef = TypedDict(
    "JourneySMSMessageTypeDef",
    {
        "MessageType": NotRequired[MessageTypeType],
        "OriginationNumber": NotRequired[str],
        "SenderId": NotRequired[str],
        "EntityId": NotRequired[str],
        "TemplateId": NotRequired[str],
    },
)

JourneyScheduleTypeDef = TypedDict(
    "JourneyScheduleTypeDef",
    {
        "EndTime": NotRequired[Union[datetime, str]],
        "StartTime": NotRequired[Union[datetime, str]],
        "Timezone": NotRequired[str],
    },
)

JourneyStateRequestTypeDef = TypedDict(
    "JourneyStateRequestTypeDef",
    {
        "State": NotRequired[StateType],
    },
)

JourneysResponseTypeDef = TypedDict(
    "JourneysResponseTypeDef",
    {
        "Item": List["JourneyResponseTypeDef"],
        "NextToken": NotRequired[str],
    },
)

ListJourneysRequestRequestTypeDef = TypedDict(
    "ListJourneysRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "PageSize": NotRequired[str],
        "Token": NotRequired[str],
    },
)

ListJourneysResponseTypeDef = TypedDict(
    "ListJourneysResponseTypeDef",
    {
        "JourneysResponse": "JourneysResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecommenderConfigurationsResponseTypeDef = TypedDict(
    "ListRecommenderConfigurationsResponseTypeDef",
    {
        "Item": List["RecommenderConfigurationResponseTypeDef"],
        "NextToken": NotRequired[str],
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
        "TagsModel": "TagsModelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTemplateVersionsRequestRequestTypeDef = TypedDict(
    "ListTemplateVersionsRequestRequestTypeDef",
    {
        "TemplateName": str,
        "TemplateType": str,
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[str],
    },
)

ListTemplateVersionsResponseTypeDef = TypedDict(
    "ListTemplateVersionsResponseTypeDef",
    {
        "TemplateVersionsResponse": "TemplateVersionsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTemplatesRequestRequestTypeDef = TypedDict(
    "ListTemplatesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[str],
        "Prefix": NotRequired[str],
        "TemplateType": NotRequired[str],
    },
)

ListTemplatesResponseTypeDef = TypedDict(
    "ListTemplatesResponseTypeDef",
    {
        "TemplatesResponse": "TemplatesResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MessageBodyTypeDef = TypedDict(
    "MessageBodyTypeDef",
    {
        "Message": NotRequired[str],
        "RequestID": NotRequired[str],
    },
)

MessageConfigurationTypeDef = TypedDict(
    "MessageConfigurationTypeDef",
    {
        "ADMMessage": NotRequired["MessageTypeDef"],
        "APNSMessage": NotRequired["MessageTypeDef"],
        "BaiduMessage": NotRequired["MessageTypeDef"],
        "CustomMessage": NotRequired["CampaignCustomMessageTypeDef"],
        "DefaultMessage": NotRequired["MessageTypeDef"],
        "EmailMessage": NotRequired["CampaignEmailMessageTypeDef"],
        "GCMMessage": NotRequired["MessageTypeDef"],
        "SMSMessage": NotRequired["CampaignSmsMessageTypeDef"],
        "InAppMessage": NotRequired["CampaignInAppMessageTypeDef"],
    },
)

MessageRequestTypeDef = TypedDict(
    "MessageRequestTypeDef",
    {
        "MessageConfiguration": "DirectMessageConfigurationTypeDef",
        "Addresses": NotRequired[Mapping[str, "AddressConfigurationTypeDef"]],
        "Context": NotRequired[Mapping[str, str]],
        "Endpoints": NotRequired[Mapping[str, "EndpointSendConfigurationTypeDef"]],
        "TemplateConfiguration": NotRequired["TemplateConfigurationTypeDef"],
        "TraceId": NotRequired[str],
    },
)

MessageResponseTypeDef = TypedDict(
    "MessageResponseTypeDef",
    {
        "ApplicationId": str,
        "EndpointResult": NotRequired[Dict[str, "EndpointMessageResultTypeDef"]],
        "RequestId": NotRequired[str],
        "Result": NotRequired[Dict[str, "MessageResultTypeDef"]],
    },
)

MessageResultTypeDef = TypedDict(
    "MessageResultTypeDef",
    {
        "DeliveryStatus": DeliveryStatusType,
        "StatusCode": int,
        "MessageId": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "UpdatedToken": NotRequired[str],
    },
)

MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "Action": NotRequired[ActionType],
        "Body": NotRequired[str],
        "ImageIconUrl": NotRequired[str],
        "ImageSmallIconUrl": NotRequired[str],
        "ImageUrl": NotRequired[str],
        "JsonBody": NotRequired[str],
        "MediaUrl": NotRequired[str],
        "RawContent": NotRequired[str],
        "SilentPush": NotRequired[bool],
        "TimeToLive": NotRequired[int],
        "Title": NotRequired[str],
        "Url": NotRequired[str],
    },
)

MetricDimensionTypeDef = TypedDict(
    "MetricDimensionTypeDef",
    {
        "ComparisonOperator": str,
        "Value": float,
    },
)

MultiConditionalBranchTypeDef = TypedDict(
    "MultiConditionalBranchTypeDef",
    {
        "Condition": NotRequired["SimpleConditionTypeDef"],
        "NextActivity": NotRequired[str],
    },
)

MultiConditionalSplitActivityTypeDef = TypedDict(
    "MultiConditionalSplitActivityTypeDef",
    {
        "Branches": NotRequired[Sequence["MultiConditionalBranchTypeDef"]],
        "DefaultActivity": NotRequired[str],
        "EvaluationWaitTime": NotRequired["WaitTimeTypeDef"],
    },
)

NumberValidateRequestTypeDef = TypedDict(
    "NumberValidateRequestTypeDef",
    {
        "IsoCountryCode": NotRequired[str],
        "PhoneNumber": NotRequired[str],
    },
)

NumberValidateResponseTypeDef = TypedDict(
    "NumberValidateResponseTypeDef",
    {
        "Carrier": NotRequired[str],
        "City": NotRequired[str],
        "CleansedPhoneNumberE164": NotRequired[str],
        "CleansedPhoneNumberNational": NotRequired[str],
        "Country": NotRequired[str],
        "CountryCodeIso2": NotRequired[str],
        "CountryCodeNumeric": NotRequired[str],
        "County": NotRequired[str],
        "OriginalCountryCodeIso2": NotRequired[str],
        "OriginalPhoneNumber": NotRequired[str],
        "PhoneType": NotRequired[str],
        "PhoneTypeCode": NotRequired[int],
        "Timezone": NotRequired[str],
        "ZipCode": NotRequired[str],
    },
)

OverrideButtonConfigurationTypeDef = TypedDict(
    "OverrideButtonConfigurationTypeDef",
    {
        "ButtonAction": ButtonActionType,
        "Link": NotRequired[str],
    },
)

PhoneNumberValidateRequestRequestTypeDef = TypedDict(
    "PhoneNumberValidateRequestRequestTypeDef",
    {
        "NumberValidateRequest": "NumberValidateRequestTypeDef",
    },
)

PhoneNumberValidateResponseTypeDef = TypedDict(
    "PhoneNumberValidateResponseTypeDef",
    {
        "NumberValidateResponse": "NumberValidateResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PublicEndpointTypeDef = TypedDict(
    "PublicEndpointTypeDef",
    {
        "Address": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, Sequence[str]]],
        "ChannelType": NotRequired[ChannelTypeType],
        "Demographic": NotRequired["EndpointDemographicTypeDef"],
        "EffectiveDate": NotRequired[str],
        "EndpointStatus": NotRequired[str],
        "Location": NotRequired["EndpointLocationTypeDef"],
        "Metrics": NotRequired[Mapping[str, float]],
        "OptOut": NotRequired[str],
        "RequestId": NotRequired[str],
        "User": NotRequired["EndpointUserTypeDef"],
    },
)

PushMessageActivityTypeDef = TypedDict(
    "PushMessageActivityTypeDef",
    {
        "MessageConfig": NotRequired["JourneyPushMessageTypeDef"],
        "NextActivity": NotRequired[str],
        "TemplateName": NotRequired[str],
        "TemplateVersion": NotRequired[str],
    },
)

PushNotificationTemplateRequestTypeDef = TypedDict(
    "PushNotificationTemplateRequestTypeDef",
    {
        "ADM": NotRequired["AndroidPushNotificationTemplateTypeDef"],
        "APNS": NotRequired["APNSPushNotificationTemplateTypeDef"],
        "Baidu": NotRequired["AndroidPushNotificationTemplateTypeDef"],
        "Default": NotRequired["DefaultPushNotificationTemplateTypeDef"],
        "DefaultSubstitutions": NotRequired[str],
        "GCM": NotRequired["AndroidPushNotificationTemplateTypeDef"],
        "RecommenderId": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "TemplateDescription": NotRequired[str],
    },
)

PushNotificationTemplateResponseTypeDef = TypedDict(
    "PushNotificationTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
        "ADM": NotRequired["AndroidPushNotificationTemplateTypeDef"],
        "APNS": NotRequired["APNSPushNotificationTemplateTypeDef"],
        "Arn": NotRequired[str],
        "Baidu": NotRequired["AndroidPushNotificationTemplateTypeDef"],
        "Default": NotRequired["DefaultPushNotificationTemplateTypeDef"],
        "DefaultSubstitutions": NotRequired[str],
        "GCM": NotRequired["AndroidPushNotificationTemplateTypeDef"],
        "RecommenderId": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "TemplateDescription": NotRequired[str],
        "Version": NotRequired[str],
    },
)

PutEventStreamRequestRequestTypeDef = TypedDict(
    "PutEventStreamRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "WriteEventStream": "WriteEventStreamTypeDef",
    },
)

PutEventStreamResponseTypeDef = TypedDict(
    "PutEventStreamResponseTypeDef",
    {
        "EventStream": "EventStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutEventsRequestRequestTypeDef = TypedDict(
    "PutEventsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EventsRequest": "EventsRequestTypeDef",
    },
)

PutEventsResponseTypeDef = TypedDict(
    "PutEventsResponseTypeDef",
    {
        "EventsResponse": "EventsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QuietTimeTypeDef = TypedDict(
    "QuietTimeTypeDef",
    {
        "End": NotRequired[str],
        "Start": NotRequired[str],
    },
)

RandomSplitActivityTypeDef = TypedDict(
    "RandomSplitActivityTypeDef",
    {
        "Branches": NotRequired[Sequence["RandomSplitEntryTypeDef"]],
    },
)

RandomSplitEntryTypeDef = TypedDict(
    "RandomSplitEntryTypeDef",
    {
        "NextActivity": NotRequired[str],
        "Percentage": NotRequired[int],
    },
)

RawEmailTypeDef = TypedDict(
    "RawEmailTypeDef",
    {
        "Data": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
    },
)

RecencyDimensionTypeDef = TypedDict(
    "RecencyDimensionTypeDef",
    {
        "Duration": DurationType,
        "RecencyType": RecencyTypeType,
    },
)

RecommenderConfigurationResponseTypeDef = TypedDict(
    "RecommenderConfigurationResponseTypeDef",
    {
        "CreationDate": str,
        "Id": str,
        "LastModifiedDate": str,
        "RecommendationProviderRoleArn": str,
        "RecommendationProviderUri": str,
        "Attributes": NotRequired[Dict[str, str]],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "RecommendationProviderIdType": NotRequired[str],
        "RecommendationTransformerUri": NotRequired[str],
        "RecommendationsDisplayName": NotRequired[str],
        "RecommendationsPerMessage": NotRequired[int],
    },
)

RemoveAttributesRequestRequestTypeDef = TypedDict(
    "RemoveAttributesRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "AttributeType": str,
        "UpdateAttributesRequest": "UpdateAttributesRequestTypeDef",
    },
)

RemoveAttributesResponseTypeDef = TypedDict(
    "RemoveAttributesResponseTypeDef",
    {
        "AttributesResource": "AttributesResourceTypeDef",
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

ResultRowTypeDef = TypedDict(
    "ResultRowTypeDef",
    {
        "GroupedBys": List["ResultRowValueTypeDef"],
        "Values": List["ResultRowValueTypeDef"],
    },
)

ResultRowValueTypeDef = TypedDict(
    "ResultRowValueTypeDef",
    {
        "Key": str,
        "Type": str,
        "Value": str,
    },
)

SMSChannelRequestTypeDef = TypedDict(
    "SMSChannelRequestTypeDef",
    {
        "Enabled": NotRequired[bool],
        "SenderId": NotRequired[str],
        "ShortCode": NotRequired[str],
    },
)

SMSChannelResponseTypeDef = TypedDict(
    "SMSChannelResponseTypeDef",
    {
        "Platform": str,
        "ApplicationId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "Enabled": NotRequired[bool],
        "HasCredential": NotRequired[bool],
        "Id": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "PromotionalMessagesPerSecond": NotRequired[int],
        "SenderId": NotRequired[str],
        "ShortCode": NotRequired[str],
        "TransactionalMessagesPerSecond": NotRequired[int],
        "Version": NotRequired[int],
    },
)

SMSMessageActivityTypeDef = TypedDict(
    "SMSMessageActivityTypeDef",
    {
        "MessageConfig": NotRequired["JourneySMSMessageTypeDef"],
        "NextActivity": NotRequired[str],
        "TemplateName": NotRequired[str],
        "TemplateVersion": NotRequired[str],
    },
)

SMSMessageTypeDef = TypedDict(
    "SMSMessageTypeDef",
    {
        "Body": NotRequired[str],
        "Keyword": NotRequired[str],
        "MediaUrl": NotRequired[str],
        "MessageType": NotRequired[MessageTypeType],
        "OriginationNumber": NotRequired[str],
        "SenderId": NotRequired[str],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
        "EntityId": NotRequired[str],
        "TemplateId": NotRequired[str],
    },
)

SMSTemplateRequestTypeDef = TypedDict(
    "SMSTemplateRequestTypeDef",
    {
        "Body": NotRequired[str],
        "DefaultSubstitutions": NotRequired[str],
        "RecommenderId": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "TemplateDescription": NotRequired[str],
    },
)

SMSTemplateResponseTypeDef = TypedDict(
    "SMSTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
        "Arn": NotRequired[str],
        "Body": NotRequired[str],
        "DefaultSubstitutions": NotRequired[str],
        "RecommenderId": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "TemplateDescription": NotRequired[str],
        "Version": NotRequired[str],
    },
)

ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "StartTime": str,
        "EndTime": NotRequired[str],
        "EventFilter": NotRequired["CampaignEventFilterTypeDef"],
        "Frequency": NotRequired[FrequencyType],
        "IsLocalTime": NotRequired[bool],
        "QuietTime": NotRequired["QuietTimeTypeDef"],
        "Timezone": NotRequired[str],
    },
)

SegmentBehaviorsTypeDef = TypedDict(
    "SegmentBehaviorsTypeDef",
    {
        "Recency": NotRequired["RecencyDimensionTypeDef"],
    },
)

SegmentConditionTypeDef = TypedDict(
    "SegmentConditionTypeDef",
    {
        "SegmentId": str,
    },
)

SegmentDemographicsTypeDef = TypedDict(
    "SegmentDemographicsTypeDef",
    {
        "AppVersion": NotRequired["SetDimensionTypeDef"],
        "Channel": NotRequired["SetDimensionTypeDef"],
        "DeviceType": NotRequired["SetDimensionTypeDef"],
        "Make": NotRequired["SetDimensionTypeDef"],
        "Model": NotRequired["SetDimensionTypeDef"],
        "Platform": NotRequired["SetDimensionTypeDef"],
    },
)

SegmentDimensionsTypeDef = TypedDict(
    "SegmentDimensionsTypeDef",
    {
        "Attributes": NotRequired[Mapping[str, "AttributeDimensionTypeDef"]],
        "Behavior": NotRequired["SegmentBehaviorsTypeDef"],
        "Demographic": NotRequired["SegmentDemographicsTypeDef"],
        "Location": NotRequired["SegmentLocationTypeDef"],
        "Metrics": NotRequired[Mapping[str, "MetricDimensionTypeDef"]],
        "UserAttributes": NotRequired[Mapping[str, "AttributeDimensionTypeDef"]],
    },
)

SegmentGroupListTypeDef = TypedDict(
    "SegmentGroupListTypeDef",
    {
        "Groups": NotRequired[Sequence["SegmentGroupTypeDef"]],
        "Include": NotRequired[IncludeType],
    },
)

SegmentGroupTypeDef = TypedDict(
    "SegmentGroupTypeDef",
    {
        "Dimensions": NotRequired[Sequence["SegmentDimensionsTypeDef"]],
        "SourceSegments": NotRequired[Sequence["SegmentReferenceTypeDef"]],
        "SourceType": NotRequired[SourceTypeType],
        "Type": NotRequired[TypeType],
    },
)

SegmentImportResourceTypeDef = TypedDict(
    "SegmentImportResourceTypeDef",
    {
        "ExternalId": str,
        "Format": FormatType,
        "RoleArn": str,
        "S3Url": str,
        "Size": int,
        "ChannelCounts": NotRequired[Dict[str, int]],
    },
)

SegmentLocationTypeDef = TypedDict(
    "SegmentLocationTypeDef",
    {
        "Country": NotRequired["SetDimensionTypeDef"],
        "GPSPoint": NotRequired["GPSPointDimensionTypeDef"],
    },
)

SegmentReferenceTypeDef = TypedDict(
    "SegmentReferenceTypeDef",
    {
        "Id": str,
        "Version": NotRequired[int],
    },
)

SegmentResponseTypeDef = TypedDict(
    "SegmentResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "CreationDate": str,
        "Id": str,
        "SegmentType": SegmentTypeType,
        "Dimensions": NotRequired["SegmentDimensionsTypeDef"],
        "ImportDefinition": NotRequired["SegmentImportResourceTypeDef"],
        "LastModifiedDate": NotRequired[str],
        "Name": NotRequired[str],
        "SegmentGroups": NotRequired["SegmentGroupListTypeDef"],
        "tags": NotRequired[Dict[str, str]],
        "Version": NotRequired[int],
    },
)

SegmentsResponseTypeDef = TypedDict(
    "SegmentsResponseTypeDef",
    {
        "Item": List["SegmentResponseTypeDef"],
        "NextToken": NotRequired[str],
    },
)

SendMessagesRequestRequestTypeDef = TypedDict(
    "SendMessagesRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "MessageRequest": "MessageRequestTypeDef",
    },
)

SendMessagesResponseTypeDef = TypedDict(
    "SendMessagesResponseTypeDef",
    {
        "MessageResponse": "MessageResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SendOTPMessageRequestParametersTypeDef = TypedDict(
    "SendOTPMessageRequestParametersTypeDef",
    {
        "BrandName": str,
        "Channel": str,
        "DestinationIdentity": str,
        "OriginationIdentity": str,
        "ReferenceId": str,
        "AllowedAttempts": NotRequired[int],
        "CodeLength": NotRequired[int],
        "EntityId": NotRequired[str],
        "Language": NotRequired[str],
        "TemplateId": NotRequired[str],
        "ValidityPeriod": NotRequired[int],
    },
)

SendOTPMessageRequestRequestTypeDef = TypedDict(
    "SendOTPMessageRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SendOTPMessageRequestParameters": "SendOTPMessageRequestParametersTypeDef",
    },
)

SendOTPMessageResponseTypeDef = TypedDict(
    "SendOTPMessageResponseTypeDef",
    {
        "MessageResponse": "MessageResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SendUsersMessageRequestTypeDef = TypedDict(
    "SendUsersMessageRequestTypeDef",
    {
        "MessageConfiguration": "DirectMessageConfigurationTypeDef",
        "Users": Mapping[str, "EndpointSendConfigurationTypeDef"],
        "Context": NotRequired[Mapping[str, str]],
        "TemplateConfiguration": NotRequired["TemplateConfigurationTypeDef"],
        "TraceId": NotRequired[str],
    },
)

SendUsersMessageResponseTypeDef = TypedDict(
    "SendUsersMessageResponseTypeDef",
    {
        "ApplicationId": str,
        "RequestId": NotRequired[str],
        "Result": NotRequired[Dict[str, Dict[str, "EndpointMessageResultTypeDef"]]],
    },
)

SendUsersMessagesRequestRequestTypeDef = TypedDict(
    "SendUsersMessagesRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SendUsersMessageRequest": "SendUsersMessageRequestTypeDef",
    },
)

SendUsersMessagesResponseTypeDef = TypedDict(
    "SendUsersMessagesResponseTypeDef",
    {
        "SendUsersMessageResponse": "SendUsersMessageResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SessionTypeDef = TypedDict(
    "SessionTypeDef",
    {
        "Id": str,
        "StartTimestamp": str,
        "Duration": NotRequired[int],
        "StopTimestamp": NotRequired[str],
    },
)

SetDimensionTypeDef = TypedDict(
    "SetDimensionTypeDef",
    {
        "Values": Sequence[str],
        "DimensionType": NotRequired[DimensionTypeType],
    },
)

SimpleConditionTypeDef = TypedDict(
    "SimpleConditionTypeDef",
    {
        "EventCondition": NotRequired["EventConditionTypeDef"],
        "SegmentCondition": NotRequired["SegmentConditionTypeDef"],
        "SegmentDimensions": NotRequired["SegmentDimensionsTypeDef"],
    },
)

SimpleEmailPartTypeDef = TypedDict(
    "SimpleEmailPartTypeDef",
    {
        "Charset": NotRequired[str],
        "Data": NotRequired[str],
    },
)

SimpleEmailTypeDef = TypedDict(
    "SimpleEmailTypeDef",
    {
        "HtmlPart": NotRequired["SimpleEmailPartTypeDef"],
        "Subject": NotRequired["SimpleEmailPartTypeDef"],
        "TextPart": NotRequired["SimpleEmailPartTypeDef"],
    },
)

StartConditionTypeDef = TypedDict(
    "StartConditionTypeDef",
    {
        "Description": NotRequired[str],
        "EventStartCondition": NotRequired["EventStartConditionTypeDef"],
        "SegmentStartCondition": NotRequired["SegmentConditionTypeDef"],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagsModel": "TagsModelTypeDef",
    },
)

TagsModelTypeDef = TypedDict(
    "TagsModelTypeDef",
    {
        "tags": Dict[str, str],
    },
)

TemplateActiveVersionRequestTypeDef = TypedDict(
    "TemplateActiveVersionRequestTypeDef",
    {
        "Version": NotRequired[str],
    },
)

TemplateConfigurationTypeDef = TypedDict(
    "TemplateConfigurationTypeDef",
    {
        "EmailTemplate": NotRequired["TemplateTypeDef"],
        "PushTemplate": NotRequired["TemplateTypeDef"],
        "SMSTemplate": NotRequired["TemplateTypeDef"],
        "VoiceTemplate": NotRequired["TemplateTypeDef"],
    },
)

TemplateCreateMessageBodyTypeDef = TypedDict(
    "TemplateCreateMessageBodyTypeDef",
    {
        "Arn": NotRequired[str],
        "Message": NotRequired[str],
        "RequestID": NotRequired[str],
    },
)

TemplateResponseTypeDef = TypedDict(
    "TemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
        "Arn": NotRequired[str],
        "DefaultSubstitutions": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "TemplateDescription": NotRequired[str],
        "Version": NotRequired[str],
    },
)

TemplateTypeDef = TypedDict(
    "TemplateTypeDef",
    {
        "Name": NotRequired[str],
        "Version": NotRequired[str],
    },
)

TemplateVersionResponseTypeDef = TypedDict(
    "TemplateVersionResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": str,
        "DefaultSubstitutions": NotRequired[str],
        "TemplateDescription": NotRequired[str],
        "Version": NotRequired[str],
    },
)

TemplateVersionsResponseTypeDef = TypedDict(
    "TemplateVersionsResponseTypeDef",
    {
        "Item": List["TemplateVersionResponseTypeDef"],
        "Message": NotRequired[str],
        "NextToken": NotRequired[str],
        "RequestID": NotRequired[str],
    },
)

TemplatesResponseTypeDef = TypedDict(
    "TemplatesResponseTypeDef",
    {
        "Item": List["TemplateResponseTypeDef"],
        "NextToken": NotRequired[str],
    },
)

TreatmentResourceTypeDef = TypedDict(
    "TreatmentResourceTypeDef",
    {
        "Id": str,
        "SizePercent": int,
        "CustomDeliveryConfiguration": NotRequired["CustomDeliveryConfigurationTypeDef"],
        "MessageConfiguration": NotRequired["MessageConfigurationTypeDef"],
        "Schedule": NotRequired["ScheduleTypeDef"],
        "State": NotRequired["CampaignStateTypeDef"],
        "TemplateConfiguration": NotRequired["TemplateConfigurationTypeDef"],
        "TreatmentDescription": NotRequired[str],
        "TreatmentName": NotRequired[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateAdmChannelRequestRequestTypeDef = TypedDict(
    "UpdateAdmChannelRequestRequestTypeDef",
    {
        "ADMChannelRequest": "ADMChannelRequestTypeDef",
        "ApplicationId": str,
    },
)

UpdateAdmChannelResponseTypeDef = TypedDict(
    "UpdateAdmChannelResponseTypeDef",
    {
        "ADMChannelResponse": "ADMChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApnsChannelRequestRequestTypeDef = TypedDict(
    "UpdateApnsChannelRequestRequestTypeDef",
    {
        "APNSChannelRequest": "APNSChannelRequestTypeDef",
        "ApplicationId": str,
    },
)

UpdateApnsChannelResponseTypeDef = TypedDict(
    "UpdateApnsChannelResponseTypeDef",
    {
        "APNSChannelResponse": "APNSChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApnsSandboxChannelRequestRequestTypeDef = TypedDict(
    "UpdateApnsSandboxChannelRequestRequestTypeDef",
    {
        "APNSSandboxChannelRequest": "APNSSandboxChannelRequestTypeDef",
        "ApplicationId": str,
    },
)

UpdateApnsSandboxChannelResponseTypeDef = TypedDict(
    "UpdateApnsSandboxChannelResponseTypeDef",
    {
        "APNSSandboxChannelResponse": "APNSSandboxChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApnsVoipChannelRequestRequestTypeDef = TypedDict(
    "UpdateApnsVoipChannelRequestRequestTypeDef",
    {
        "APNSVoipChannelRequest": "APNSVoipChannelRequestTypeDef",
        "ApplicationId": str,
    },
)

UpdateApnsVoipChannelResponseTypeDef = TypedDict(
    "UpdateApnsVoipChannelResponseTypeDef",
    {
        "APNSVoipChannelResponse": "APNSVoipChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApnsVoipSandboxChannelRequestRequestTypeDef = TypedDict(
    "UpdateApnsVoipSandboxChannelRequestRequestTypeDef",
    {
        "APNSVoipSandboxChannelRequest": "APNSVoipSandboxChannelRequestTypeDef",
        "ApplicationId": str,
    },
)

UpdateApnsVoipSandboxChannelResponseTypeDef = TypedDict(
    "UpdateApnsVoipSandboxChannelResponseTypeDef",
    {
        "APNSVoipSandboxChannelResponse": "APNSVoipSandboxChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApplicationSettingsRequestRequestTypeDef = TypedDict(
    "UpdateApplicationSettingsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "WriteApplicationSettingsRequest": "WriteApplicationSettingsRequestTypeDef",
    },
)

UpdateApplicationSettingsResponseTypeDef = TypedDict(
    "UpdateApplicationSettingsResponseTypeDef",
    {
        "ApplicationSettingsResource": "ApplicationSettingsResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAttributesRequestTypeDef = TypedDict(
    "UpdateAttributesRequestTypeDef",
    {
        "Blacklist": NotRequired[Sequence[str]],
    },
)

UpdateBaiduChannelRequestRequestTypeDef = TypedDict(
    "UpdateBaiduChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "BaiduChannelRequest": "BaiduChannelRequestTypeDef",
    },
)

UpdateBaiduChannelResponseTypeDef = TypedDict(
    "UpdateBaiduChannelResponseTypeDef",
    {
        "BaiduChannelResponse": "BaiduChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCampaignRequestRequestTypeDef = TypedDict(
    "UpdateCampaignRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "WriteCampaignRequest": "WriteCampaignRequestTypeDef",
    },
)

UpdateCampaignResponseTypeDef = TypedDict(
    "UpdateCampaignResponseTypeDef",
    {
        "CampaignResponse": "CampaignResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEmailChannelRequestRequestTypeDef = TypedDict(
    "UpdateEmailChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EmailChannelRequest": "EmailChannelRequestTypeDef",
    },
)

UpdateEmailChannelResponseTypeDef = TypedDict(
    "UpdateEmailChannelResponseTypeDef",
    {
        "EmailChannelResponse": "EmailChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEmailTemplateRequestRequestTypeDef = TypedDict(
    "UpdateEmailTemplateRequestRequestTypeDef",
    {
        "EmailTemplateRequest": "EmailTemplateRequestTypeDef",
        "TemplateName": str,
        "CreateNewVersion": NotRequired[bool],
        "Version": NotRequired[str],
    },
)

UpdateEmailTemplateResponseTypeDef = TypedDict(
    "UpdateEmailTemplateResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEndpointRequestRequestTypeDef = TypedDict(
    "UpdateEndpointRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EndpointId": str,
        "EndpointRequest": "EndpointRequestTypeDef",
    },
)

UpdateEndpointResponseTypeDef = TypedDict(
    "UpdateEndpointResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEndpointsBatchRequestRequestTypeDef = TypedDict(
    "UpdateEndpointsBatchRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EndpointBatchRequest": "EndpointBatchRequestTypeDef",
    },
)

UpdateEndpointsBatchResponseTypeDef = TypedDict(
    "UpdateEndpointsBatchResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGcmChannelRequestRequestTypeDef = TypedDict(
    "UpdateGcmChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "GCMChannelRequest": "GCMChannelRequestTypeDef",
    },
)

UpdateGcmChannelResponseTypeDef = TypedDict(
    "UpdateGcmChannelResponseTypeDef",
    {
        "GCMChannelResponse": "GCMChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateInAppTemplateRequestRequestTypeDef = TypedDict(
    "UpdateInAppTemplateRequestRequestTypeDef",
    {
        "InAppTemplateRequest": "InAppTemplateRequestTypeDef",
        "TemplateName": str,
        "CreateNewVersion": NotRequired[bool],
        "Version": NotRequired[str],
    },
)

UpdateInAppTemplateResponseTypeDef = TypedDict(
    "UpdateInAppTemplateResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateJourneyRequestRequestTypeDef = TypedDict(
    "UpdateJourneyRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
        "WriteJourneyRequest": "WriteJourneyRequestTypeDef",
    },
)

UpdateJourneyResponseTypeDef = TypedDict(
    "UpdateJourneyResponseTypeDef",
    {
        "JourneyResponse": "JourneyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateJourneyStateRequestRequestTypeDef = TypedDict(
    "UpdateJourneyStateRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
        "JourneyStateRequest": "JourneyStateRequestTypeDef",
    },
)

UpdateJourneyStateResponseTypeDef = TypedDict(
    "UpdateJourneyStateResponseTypeDef",
    {
        "JourneyResponse": "JourneyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePushTemplateRequestRequestTypeDef = TypedDict(
    "UpdatePushTemplateRequestRequestTypeDef",
    {
        "PushNotificationTemplateRequest": "PushNotificationTemplateRequestTypeDef",
        "TemplateName": str,
        "CreateNewVersion": NotRequired[bool],
        "Version": NotRequired[str],
    },
)

UpdatePushTemplateResponseTypeDef = TypedDict(
    "UpdatePushTemplateResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRecommenderConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateRecommenderConfigurationRequestRequestTypeDef",
    {
        "RecommenderId": str,
        "UpdateRecommenderConfiguration": "UpdateRecommenderConfigurationTypeDef",
    },
)

UpdateRecommenderConfigurationResponseTypeDef = TypedDict(
    "UpdateRecommenderConfigurationResponseTypeDef",
    {
        "RecommenderConfigurationResponse": "RecommenderConfigurationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRecommenderConfigurationTypeDef = TypedDict(
    "UpdateRecommenderConfigurationTypeDef",
    {
        "RecommendationProviderRoleArn": str,
        "RecommendationProviderUri": str,
        "Attributes": NotRequired[Mapping[str, str]],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "RecommendationProviderIdType": NotRequired[str],
        "RecommendationTransformerUri": NotRequired[str],
        "RecommendationsDisplayName": NotRequired[str],
        "RecommendationsPerMessage": NotRequired[int],
    },
)

UpdateSegmentRequestRequestTypeDef = TypedDict(
    "UpdateSegmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
        "WriteSegmentRequest": "WriteSegmentRequestTypeDef",
    },
)

UpdateSegmentResponseTypeDef = TypedDict(
    "UpdateSegmentResponseTypeDef",
    {
        "SegmentResponse": "SegmentResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSmsChannelRequestRequestTypeDef = TypedDict(
    "UpdateSmsChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SMSChannelRequest": "SMSChannelRequestTypeDef",
    },
)

UpdateSmsChannelResponseTypeDef = TypedDict(
    "UpdateSmsChannelResponseTypeDef",
    {
        "SMSChannelResponse": "SMSChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSmsTemplateRequestRequestTypeDef = TypedDict(
    "UpdateSmsTemplateRequestRequestTypeDef",
    {
        "SMSTemplateRequest": "SMSTemplateRequestTypeDef",
        "TemplateName": str,
        "CreateNewVersion": NotRequired[bool],
        "Version": NotRequired[str],
    },
)

UpdateSmsTemplateResponseTypeDef = TypedDict(
    "UpdateSmsTemplateResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTemplateActiveVersionRequestRequestTypeDef = TypedDict(
    "UpdateTemplateActiveVersionRequestRequestTypeDef",
    {
        "TemplateActiveVersionRequest": "TemplateActiveVersionRequestTypeDef",
        "TemplateName": str,
        "TemplateType": str,
    },
)

UpdateTemplateActiveVersionResponseTypeDef = TypedDict(
    "UpdateTemplateActiveVersionResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVoiceChannelRequestRequestTypeDef = TypedDict(
    "UpdateVoiceChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "VoiceChannelRequest": "VoiceChannelRequestTypeDef",
    },
)

UpdateVoiceChannelResponseTypeDef = TypedDict(
    "UpdateVoiceChannelResponseTypeDef",
    {
        "VoiceChannelResponse": "VoiceChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVoiceTemplateRequestRequestTypeDef = TypedDict(
    "UpdateVoiceTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "VoiceTemplateRequest": "VoiceTemplateRequestTypeDef",
        "CreateNewVersion": NotRequired[bool],
        "Version": NotRequired[str],
    },
)

UpdateVoiceTemplateResponseTypeDef = TypedDict(
    "UpdateVoiceTemplateResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VerificationResponseTypeDef = TypedDict(
    "VerificationResponseTypeDef",
    {
        "Valid": NotRequired[bool],
    },
)

VerifyOTPMessageRequestParametersTypeDef = TypedDict(
    "VerifyOTPMessageRequestParametersTypeDef",
    {
        "DestinationIdentity": str,
        "Otp": str,
        "ReferenceId": str,
    },
)

VerifyOTPMessageRequestRequestTypeDef = TypedDict(
    "VerifyOTPMessageRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "VerifyOTPMessageRequestParameters": "VerifyOTPMessageRequestParametersTypeDef",
    },
)

VerifyOTPMessageResponseTypeDef = TypedDict(
    "VerifyOTPMessageResponseTypeDef",
    {
        "VerificationResponse": "VerificationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VoiceChannelRequestTypeDef = TypedDict(
    "VoiceChannelRequestTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)

VoiceChannelResponseTypeDef = TypedDict(
    "VoiceChannelResponseTypeDef",
    {
        "Platform": str,
        "ApplicationId": NotRequired[str],
        "CreationDate": NotRequired[str],
        "Enabled": NotRequired[bool],
        "HasCredential": NotRequired[bool],
        "Id": NotRequired[str],
        "IsArchived": NotRequired[bool],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Version": NotRequired[int],
    },
)

VoiceMessageTypeDef = TypedDict(
    "VoiceMessageTypeDef",
    {
        "Body": NotRequired[str],
        "LanguageCode": NotRequired[str],
        "OriginationNumber": NotRequired[str],
        "Substitutions": NotRequired[Mapping[str, Sequence[str]]],
        "VoiceId": NotRequired[str],
    },
)

VoiceTemplateRequestTypeDef = TypedDict(
    "VoiceTemplateRequestTypeDef",
    {
        "Body": NotRequired[str],
        "DefaultSubstitutions": NotRequired[str],
        "LanguageCode": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "TemplateDescription": NotRequired[str],
        "VoiceId": NotRequired[str],
    },
)

VoiceTemplateResponseTypeDef = TypedDict(
    "VoiceTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
        "Arn": NotRequired[str],
        "Body": NotRequired[str],
        "DefaultSubstitutions": NotRequired[str],
        "LanguageCode": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "TemplateDescription": NotRequired[str],
        "Version": NotRequired[str],
        "VoiceId": NotRequired[str],
    },
)

WaitActivityTypeDef = TypedDict(
    "WaitActivityTypeDef",
    {
        "NextActivity": NotRequired[str],
        "WaitTime": NotRequired["WaitTimeTypeDef"],
    },
)

WaitTimeTypeDef = TypedDict(
    "WaitTimeTypeDef",
    {
        "WaitFor": NotRequired[str],
        "WaitUntil": NotRequired[str],
    },
)

WriteApplicationSettingsRequestTypeDef = TypedDict(
    "WriteApplicationSettingsRequestTypeDef",
    {
        "CampaignHook": NotRequired["CampaignHookTypeDef"],
        "CloudWatchMetricsEnabled": NotRequired[bool],
        "EventTaggingEnabled": NotRequired[bool],
        "Limits": NotRequired["CampaignLimitsTypeDef"],
        "QuietTime": NotRequired["QuietTimeTypeDef"],
    },
)

WriteCampaignRequestTypeDef = TypedDict(
    "WriteCampaignRequestTypeDef",
    {
        "AdditionalTreatments": NotRequired[Sequence["WriteTreatmentResourceTypeDef"]],
        "CustomDeliveryConfiguration": NotRequired["CustomDeliveryConfigurationTypeDef"],
        "Description": NotRequired[str],
        "HoldoutPercent": NotRequired[int],
        "Hook": NotRequired["CampaignHookTypeDef"],
        "IsPaused": NotRequired[bool],
        "Limits": NotRequired["CampaignLimitsTypeDef"],
        "MessageConfiguration": NotRequired["MessageConfigurationTypeDef"],
        "Name": NotRequired[str],
        "Schedule": NotRequired["ScheduleTypeDef"],
        "SegmentId": NotRequired[str],
        "SegmentVersion": NotRequired[int],
        "tags": NotRequired[Mapping[str, str]],
        "TemplateConfiguration": NotRequired["TemplateConfigurationTypeDef"],
        "TreatmentDescription": NotRequired[str],
        "TreatmentName": NotRequired[str],
        "Priority": NotRequired[int],
    },
)

WriteEventStreamTypeDef = TypedDict(
    "WriteEventStreamTypeDef",
    {
        "DestinationStreamArn": str,
        "RoleArn": str,
    },
)

WriteJourneyRequestTypeDef = TypedDict(
    "WriteJourneyRequestTypeDef",
    {
        "Name": str,
        "Activities": NotRequired[Mapping[str, "ActivityTypeDef"]],
        "CreationDate": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Limits": NotRequired["JourneyLimitsTypeDef"],
        "LocalTime": NotRequired[bool],
        "QuietTime": NotRequired["QuietTimeTypeDef"],
        "RefreshFrequency": NotRequired[str],
        "Schedule": NotRequired["JourneyScheduleTypeDef"],
        "StartActivity": NotRequired[str],
        "StartCondition": NotRequired["StartConditionTypeDef"],
        "State": NotRequired[StateType],
        "WaitForQuietTime": NotRequired[bool],
        "RefreshOnSegmentUpdate": NotRequired[bool],
        "JourneyChannelSettings": NotRequired["JourneyChannelSettingsTypeDef"],
    },
)

WriteSegmentRequestTypeDef = TypedDict(
    "WriteSegmentRequestTypeDef",
    {
        "Dimensions": NotRequired["SegmentDimensionsTypeDef"],
        "Name": NotRequired[str],
        "SegmentGroups": NotRequired["SegmentGroupListTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
    },
)

WriteTreatmentResourceTypeDef = TypedDict(
    "WriteTreatmentResourceTypeDef",
    {
        "SizePercent": int,
        "CustomDeliveryConfiguration": NotRequired["CustomDeliveryConfigurationTypeDef"],
        "MessageConfiguration": NotRequired["MessageConfigurationTypeDef"],
        "Schedule": NotRequired["ScheduleTypeDef"],
        "TemplateConfiguration": NotRequired["TemplateConfigurationTypeDef"],
        "TreatmentDescription": NotRequired[str],
        "TreatmentName": NotRequired[str],
    },
)
