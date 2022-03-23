"""
Type annotations for connect service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/type_defs.html)

Usage::

    ```python
    from mypy_boto3_connect.type_defs import AgentInfoTypeDef

    data: AgentInfoTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AgentStatusStateType,
    AgentStatusTypeType,
    ChannelType,
    ContactFlowModuleStateType,
    ContactFlowModuleStatusType,
    ContactFlowStateType,
    ContactFlowTypeType,
    ContactInitiationMethodType,
    CurrentMetricNameType,
    DirectoryTypeType,
    GroupingType,
    HistoricalMetricNameType,
    HoursOfOperationDaysType,
    InstanceAttributeTypeType,
    InstanceStatusType,
    InstanceStorageResourceTypeType,
    IntegrationTypeType,
    LexVersionType,
    PhoneNumberCountryCodeType,
    PhoneNumberTypeType,
    PhoneTypeType,
    QueueStatusType,
    QueueTypeType,
    QuickConnectTypeType,
    ReferenceStatusType,
    ReferenceTypeType,
    SourceTypeType,
    StatisticType,
    StorageTypeType,
    TrafficTypeType,
    UnitType,
    UseCaseTypeType,
    VocabularyLanguageCodeType,
    VocabularyStateType,
    VoiceRecordingTrackType,
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
    "AgentInfoTypeDef",
    "AgentStatusSummaryTypeDef",
    "AgentStatusTypeDef",
    "AnswerMachineDetectionConfigTypeDef",
    "AssociateApprovedOriginRequestRequestTypeDef",
    "AssociateBotRequestRequestTypeDef",
    "AssociateDefaultVocabularyRequestRequestTypeDef",
    "AssociateInstanceStorageConfigRequestRequestTypeDef",
    "AssociateInstanceStorageConfigResponseTypeDef",
    "AssociateLambdaFunctionRequestRequestTypeDef",
    "AssociateLexBotRequestRequestTypeDef",
    "AssociateQueueQuickConnectsRequestRequestTypeDef",
    "AssociateRoutingProfileQueuesRequestRequestTypeDef",
    "AssociateSecurityKeyRequestRequestTypeDef",
    "AssociateSecurityKeyResponseTypeDef",
    "AttachmentReferenceTypeDef",
    "AttributeTypeDef",
    "ChatMessageTypeDef",
    "ChatStreamingConfigurationTypeDef",
    "ContactFlowModuleSummaryTypeDef",
    "ContactFlowModuleTypeDef",
    "ContactFlowSummaryTypeDef",
    "ContactFlowTypeDef",
    "ContactTypeDef",
    "CreateAgentStatusRequestRequestTypeDef",
    "CreateAgentStatusResponseTypeDef",
    "CreateContactFlowModuleRequestRequestTypeDef",
    "CreateContactFlowModuleResponseTypeDef",
    "CreateContactFlowRequestRequestTypeDef",
    "CreateContactFlowResponseTypeDef",
    "CreateHoursOfOperationRequestRequestTypeDef",
    "CreateHoursOfOperationResponseTypeDef",
    "CreateInstanceRequestRequestTypeDef",
    "CreateInstanceResponseTypeDef",
    "CreateIntegrationAssociationRequestRequestTypeDef",
    "CreateIntegrationAssociationResponseTypeDef",
    "CreateQueueRequestRequestTypeDef",
    "CreateQueueResponseTypeDef",
    "CreateQuickConnectRequestRequestTypeDef",
    "CreateQuickConnectResponseTypeDef",
    "CreateRoutingProfileRequestRequestTypeDef",
    "CreateRoutingProfileResponseTypeDef",
    "CreateSecurityProfileRequestRequestTypeDef",
    "CreateSecurityProfileResponseTypeDef",
    "CreateUseCaseRequestRequestTypeDef",
    "CreateUseCaseResponseTypeDef",
    "CreateUserHierarchyGroupRequestRequestTypeDef",
    "CreateUserHierarchyGroupResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CreateUserResponseTypeDef",
    "CreateVocabularyRequestRequestTypeDef",
    "CreateVocabularyResponseTypeDef",
    "CredentialsTypeDef",
    "CurrentMetricDataTypeDef",
    "CurrentMetricResultTypeDef",
    "CurrentMetricTypeDef",
    "DefaultVocabularyTypeDef",
    "DeleteContactFlowModuleRequestRequestTypeDef",
    "DeleteContactFlowRequestRequestTypeDef",
    "DeleteHoursOfOperationRequestRequestTypeDef",
    "DeleteInstanceRequestRequestTypeDef",
    "DeleteIntegrationAssociationRequestRequestTypeDef",
    "DeleteQuickConnectRequestRequestTypeDef",
    "DeleteSecurityProfileRequestRequestTypeDef",
    "DeleteUseCaseRequestRequestTypeDef",
    "DeleteUserHierarchyGroupRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DeleteVocabularyRequestRequestTypeDef",
    "DeleteVocabularyResponseTypeDef",
    "DescribeAgentStatusRequestRequestTypeDef",
    "DescribeAgentStatusResponseTypeDef",
    "DescribeContactFlowModuleRequestRequestTypeDef",
    "DescribeContactFlowModuleResponseTypeDef",
    "DescribeContactFlowRequestRequestTypeDef",
    "DescribeContactFlowResponseTypeDef",
    "DescribeContactRequestRequestTypeDef",
    "DescribeContactResponseTypeDef",
    "DescribeHoursOfOperationRequestRequestTypeDef",
    "DescribeHoursOfOperationResponseTypeDef",
    "DescribeInstanceAttributeRequestRequestTypeDef",
    "DescribeInstanceAttributeResponseTypeDef",
    "DescribeInstanceRequestRequestTypeDef",
    "DescribeInstanceResponseTypeDef",
    "DescribeInstanceStorageConfigRequestRequestTypeDef",
    "DescribeInstanceStorageConfigResponseTypeDef",
    "DescribeQueueRequestRequestTypeDef",
    "DescribeQueueResponseTypeDef",
    "DescribeQuickConnectRequestRequestTypeDef",
    "DescribeQuickConnectResponseTypeDef",
    "DescribeRoutingProfileRequestRequestTypeDef",
    "DescribeRoutingProfileResponseTypeDef",
    "DescribeSecurityProfileRequestRequestTypeDef",
    "DescribeSecurityProfileResponseTypeDef",
    "DescribeUserHierarchyGroupRequestRequestTypeDef",
    "DescribeUserHierarchyGroupResponseTypeDef",
    "DescribeUserHierarchyStructureRequestRequestTypeDef",
    "DescribeUserHierarchyStructureResponseTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "DescribeUserResponseTypeDef",
    "DescribeVocabularyRequestRequestTypeDef",
    "DescribeVocabularyResponseTypeDef",
    "DimensionsTypeDef",
    "DisassociateApprovedOriginRequestRequestTypeDef",
    "DisassociateBotRequestRequestTypeDef",
    "DisassociateInstanceStorageConfigRequestRequestTypeDef",
    "DisassociateLambdaFunctionRequestRequestTypeDef",
    "DisassociateLexBotRequestRequestTypeDef",
    "DisassociateQueueQuickConnectsRequestRequestTypeDef",
    "DisassociateRoutingProfileQueuesRequestRequestTypeDef",
    "DisassociateSecurityKeyRequestRequestTypeDef",
    "EncryptionConfigTypeDef",
    "FiltersTypeDef",
    "GetContactAttributesRequestRequestTypeDef",
    "GetContactAttributesResponseTypeDef",
    "GetCurrentMetricDataRequestRequestTypeDef",
    "GetCurrentMetricDataResponseTypeDef",
    "GetFederationTokenRequestRequestTypeDef",
    "GetFederationTokenResponseTypeDef",
    "GetMetricDataRequestRequestTypeDef",
    "GetMetricDataResponseTypeDef",
    "HierarchyGroupSummaryTypeDef",
    "HierarchyGroupTypeDef",
    "HierarchyLevelTypeDef",
    "HierarchyLevelUpdateTypeDef",
    "HierarchyPathTypeDef",
    "HierarchyStructureTypeDef",
    "HierarchyStructureUpdateTypeDef",
    "HistoricalMetricDataTypeDef",
    "HistoricalMetricResultTypeDef",
    "HistoricalMetricTypeDef",
    "HoursOfOperationConfigTypeDef",
    "HoursOfOperationSummaryTypeDef",
    "HoursOfOperationTimeSliceTypeDef",
    "HoursOfOperationTypeDef",
    "InstanceStatusReasonTypeDef",
    "InstanceStorageConfigTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTypeDef",
    "IntegrationAssociationSummaryTypeDef",
    "KinesisFirehoseConfigTypeDef",
    "KinesisStreamConfigTypeDef",
    "KinesisVideoStreamConfigTypeDef",
    "LexBotConfigTypeDef",
    "LexBotTypeDef",
    "LexV2BotTypeDef",
    "ListAgentStatusRequestRequestTypeDef",
    "ListAgentStatusResponseTypeDef",
    "ListApprovedOriginsRequestRequestTypeDef",
    "ListApprovedOriginsResponseTypeDef",
    "ListBotsRequestRequestTypeDef",
    "ListBotsResponseTypeDef",
    "ListContactFlowModulesRequestRequestTypeDef",
    "ListContactFlowModulesResponseTypeDef",
    "ListContactFlowsRequestRequestTypeDef",
    "ListContactFlowsResponseTypeDef",
    "ListContactReferencesRequestRequestTypeDef",
    "ListContactReferencesResponseTypeDef",
    "ListDefaultVocabulariesRequestRequestTypeDef",
    "ListDefaultVocabulariesResponseTypeDef",
    "ListHoursOfOperationsRequestRequestTypeDef",
    "ListHoursOfOperationsResponseTypeDef",
    "ListInstanceAttributesRequestRequestTypeDef",
    "ListInstanceAttributesResponseTypeDef",
    "ListInstanceStorageConfigsRequestRequestTypeDef",
    "ListInstanceStorageConfigsResponseTypeDef",
    "ListInstancesRequestRequestTypeDef",
    "ListInstancesResponseTypeDef",
    "ListIntegrationAssociationsRequestRequestTypeDef",
    "ListIntegrationAssociationsResponseTypeDef",
    "ListLambdaFunctionsRequestRequestTypeDef",
    "ListLambdaFunctionsResponseTypeDef",
    "ListLexBotsRequestRequestTypeDef",
    "ListLexBotsResponseTypeDef",
    "ListPhoneNumbersRequestRequestTypeDef",
    "ListPhoneNumbersResponseTypeDef",
    "ListPromptsRequestRequestTypeDef",
    "ListPromptsResponseTypeDef",
    "ListQueueQuickConnectsRequestRequestTypeDef",
    "ListQueueQuickConnectsResponseTypeDef",
    "ListQueuesRequestRequestTypeDef",
    "ListQueuesResponseTypeDef",
    "ListQuickConnectsRequestRequestTypeDef",
    "ListQuickConnectsResponseTypeDef",
    "ListRoutingProfileQueuesRequestRequestTypeDef",
    "ListRoutingProfileQueuesResponseTypeDef",
    "ListRoutingProfilesRequestRequestTypeDef",
    "ListRoutingProfilesResponseTypeDef",
    "ListSecurityKeysRequestRequestTypeDef",
    "ListSecurityKeysResponseTypeDef",
    "ListSecurityProfilePermissionsRequestRequestTypeDef",
    "ListSecurityProfilePermissionsResponseTypeDef",
    "ListSecurityProfilesRequestRequestTypeDef",
    "ListSecurityProfilesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUseCasesRequestRequestTypeDef",
    "ListUseCasesResponseTypeDef",
    "ListUserHierarchyGroupsRequestRequestTypeDef",
    "ListUserHierarchyGroupsResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "MediaConcurrencyTypeDef",
    "OutboundCallerConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipantDetailsTypeDef",
    "PhoneNumberQuickConnectConfigTypeDef",
    "PhoneNumberSummaryTypeDef",
    "PromptSummaryTypeDef",
    "QueueInfoTypeDef",
    "QueueQuickConnectConfigTypeDef",
    "QueueReferenceTypeDef",
    "QueueSummaryTypeDef",
    "QueueTypeDef",
    "QuickConnectConfigTypeDef",
    "QuickConnectSummaryTypeDef",
    "QuickConnectTypeDef",
    "ReferenceSummaryTypeDef",
    "ReferenceTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeContactRecordingRequestRequestTypeDef",
    "RoutingProfileQueueConfigSummaryTypeDef",
    "RoutingProfileQueueConfigTypeDef",
    "RoutingProfileQueueReferenceTypeDef",
    "RoutingProfileSummaryTypeDef",
    "RoutingProfileTypeDef",
    "S3ConfigTypeDef",
    "SearchVocabulariesRequestRequestTypeDef",
    "SearchVocabulariesResponseTypeDef",
    "SecurityKeyTypeDef",
    "SecurityProfileSummaryTypeDef",
    "SecurityProfileTypeDef",
    "StartChatContactRequestRequestTypeDef",
    "StartChatContactResponseTypeDef",
    "StartContactRecordingRequestRequestTypeDef",
    "StartContactStreamingRequestRequestTypeDef",
    "StartContactStreamingResponseTypeDef",
    "StartOutboundVoiceContactRequestRequestTypeDef",
    "StartOutboundVoiceContactResponseTypeDef",
    "StartTaskContactRequestRequestTypeDef",
    "StartTaskContactResponseTypeDef",
    "StopContactRecordingRequestRequestTypeDef",
    "StopContactRequestRequestTypeDef",
    "StopContactStreamingRequestRequestTypeDef",
    "SuspendContactRecordingRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ThresholdTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAgentStatusRequestRequestTypeDef",
    "UpdateContactAttributesRequestRequestTypeDef",
    "UpdateContactFlowContentRequestRequestTypeDef",
    "UpdateContactFlowMetadataRequestRequestTypeDef",
    "UpdateContactFlowModuleContentRequestRequestTypeDef",
    "UpdateContactFlowModuleMetadataRequestRequestTypeDef",
    "UpdateContactFlowNameRequestRequestTypeDef",
    "UpdateContactRequestRequestTypeDef",
    "UpdateContactScheduleRequestRequestTypeDef",
    "UpdateHoursOfOperationRequestRequestTypeDef",
    "UpdateInstanceAttributeRequestRequestTypeDef",
    "UpdateInstanceStorageConfigRequestRequestTypeDef",
    "UpdateQueueHoursOfOperationRequestRequestTypeDef",
    "UpdateQueueMaxContactsRequestRequestTypeDef",
    "UpdateQueueNameRequestRequestTypeDef",
    "UpdateQueueOutboundCallerConfigRequestRequestTypeDef",
    "UpdateQueueStatusRequestRequestTypeDef",
    "UpdateQuickConnectConfigRequestRequestTypeDef",
    "UpdateQuickConnectNameRequestRequestTypeDef",
    "UpdateRoutingProfileConcurrencyRequestRequestTypeDef",
    "UpdateRoutingProfileDefaultOutboundQueueRequestRequestTypeDef",
    "UpdateRoutingProfileNameRequestRequestTypeDef",
    "UpdateRoutingProfileQueuesRequestRequestTypeDef",
    "UpdateSecurityProfileRequestRequestTypeDef",
    "UpdateUserHierarchyGroupNameRequestRequestTypeDef",
    "UpdateUserHierarchyRequestRequestTypeDef",
    "UpdateUserHierarchyStructureRequestRequestTypeDef",
    "UpdateUserIdentityInfoRequestRequestTypeDef",
    "UpdateUserPhoneConfigRequestRequestTypeDef",
    "UpdateUserRoutingProfileRequestRequestTypeDef",
    "UpdateUserSecurityProfilesRequestRequestTypeDef",
    "UrlReferenceTypeDef",
    "UseCaseTypeDef",
    "UserIdentityInfoTypeDef",
    "UserPhoneConfigTypeDef",
    "UserQuickConnectConfigTypeDef",
    "UserSummaryTypeDef",
    "UserTypeDef",
    "VocabularySummaryTypeDef",
    "VocabularyTypeDef",
    "VoiceRecordingConfigurationTypeDef",
)

AgentInfoTypeDef = TypedDict(
    "AgentInfoTypeDef",
    {
        "Id": NotRequired[str],
        "ConnectedToAgentTimestamp": NotRequired[datetime],
    },
)

AgentStatusSummaryTypeDef = TypedDict(
    "AgentStatusSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[AgentStatusTypeType],
    },
)

AgentStatusTypeDef = TypedDict(
    "AgentStatusTypeDef",
    {
        "AgentStatusARN": NotRequired[str],
        "AgentStatusId": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Type": NotRequired[AgentStatusTypeType],
        "DisplayOrder": NotRequired[int],
        "State": NotRequired[AgentStatusStateType],
        "Tags": NotRequired[Dict[str, str]],
    },
)

AnswerMachineDetectionConfigTypeDef = TypedDict(
    "AnswerMachineDetectionConfigTypeDef",
    {
        "EnableAnswerMachineDetection": NotRequired[bool],
        "AwaitAnswerMachinePrompt": NotRequired[bool],
    },
)

AssociateApprovedOriginRequestRequestTypeDef = TypedDict(
    "AssociateApprovedOriginRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Origin": str,
    },
)

AssociateBotRequestRequestTypeDef = TypedDict(
    "AssociateBotRequestRequestTypeDef",
    {
        "InstanceId": str,
        "LexBot": NotRequired["LexBotTypeDef"],
        "LexV2Bot": NotRequired["LexV2BotTypeDef"],
    },
)

AssociateDefaultVocabularyRequestRequestTypeDef = TypedDict(
    "AssociateDefaultVocabularyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "LanguageCode": VocabularyLanguageCodeType,
        "VocabularyId": NotRequired[str],
    },
)

AssociateInstanceStorageConfigRequestRequestTypeDef = TypedDict(
    "AssociateInstanceStorageConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ResourceType": InstanceStorageResourceTypeType,
        "StorageConfig": "InstanceStorageConfigTypeDef",
    },
)

AssociateInstanceStorageConfigResponseTypeDef = TypedDict(
    "AssociateInstanceStorageConfigResponseTypeDef",
    {
        "AssociationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateLambdaFunctionRequestRequestTypeDef = TypedDict(
    "AssociateLambdaFunctionRequestRequestTypeDef",
    {
        "InstanceId": str,
        "FunctionArn": str,
    },
)

AssociateLexBotRequestRequestTypeDef = TypedDict(
    "AssociateLexBotRequestRequestTypeDef",
    {
        "InstanceId": str,
        "LexBot": "LexBotTypeDef",
    },
)

AssociateQueueQuickConnectsRequestRequestTypeDef = TypedDict(
    "AssociateQueueQuickConnectsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "QuickConnectIds": Sequence[str],
    },
)

AssociateRoutingProfileQueuesRequestRequestTypeDef = TypedDict(
    "AssociateRoutingProfileQueuesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "QueueConfigs": Sequence["RoutingProfileQueueConfigTypeDef"],
    },
)

AssociateSecurityKeyRequestRequestTypeDef = TypedDict(
    "AssociateSecurityKeyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Key": str,
    },
)

AssociateSecurityKeyResponseTypeDef = TypedDict(
    "AssociateSecurityKeyResponseTypeDef",
    {
        "AssociationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachmentReferenceTypeDef = TypedDict(
    "AttachmentReferenceTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
        "Status": NotRequired[ReferenceStatusType],
    },
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "AttributeType": NotRequired[InstanceAttributeTypeType],
        "Value": NotRequired[str],
    },
)

ChatMessageTypeDef = TypedDict(
    "ChatMessageTypeDef",
    {
        "ContentType": str,
        "Content": str,
    },
)

ChatStreamingConfigurationTypeDef = TypedDict(
    "ChatStreamingConfigurationTypeDef",
    {
        "StreamingEndpointArn": str,
    },
)

ContactFlowModuleSummaryTypeDef = TypedDict(
    "ContactFlowModuleSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "State": NotRequired[ContactFlowModuleStateType],
    },
)

ContactFlowModuleTypeDef = TypedDict(
    "ContactFlowModuleTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Content": NotRequired[str],
        "Description": NotRequired[str],
        "State": NotRequired[ContactFlowModuleStateType],
        "Status": NotRequired[ContactFlowModuleStatusType],
        "Tags": NotRequired[Dict[str, str]],
    },
)

ContactFlowSummaryTypeDef = TypedDict(
    "ContactFlowSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "ContactFlowType": NotRequired[ContactFlowTypeType],
        "ContactFlowState": NotRequired[ContactFlowStateType],
    },
)

ContactFlowTypeDef = TypedDict(
    "ContactFlowTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[ContactFlowTypeType],
        "State": NotRequired[ContactFlowStateType],
        "Description": NotRequired[str],
        "Content": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)

ContactTypeDef = TypedDict(
    "ContactTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
        "InitialContactId": NotRequired[str],
        "PreviousContactId": NotRequired[str],
        "InitiationMethod": NotRequired[ContactInitiationMethodType],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Channel": NotRequired[ChannelType],
        "QueueInfo": NotRequired["QueueInfoTypeDef"],
        "AgentInfo": NotRequired["AgentInfoTypeDef"],
        "InitiationTimestamp": NotRequired[datetime],
        "DisconnectTimestamp": NotRequired[datetime],
        "LastUpdateTimestamp": NotRequired[datetime],
        "ScheduledTimestamp": NotRequired[datetime],
    },
)

CreateAgentStatusRequestRequestTypeDef = TypedDict(
    "CreateAgentStatusRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "State": AgentStatusStateType,
        "Description": NotRequired[str],
        "DisplayOrder": NotRequired[int],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateAgentStatusResponseTypeDef = TypedDict(
    "CreateAgentStatusResponseTypeDef",
    {
        "AgentStatusARN": str,
        "AgentStatusId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateContactFlowModuleRequestRequestTypeDef = TypedDict(
    "CreateContactFlowModuleRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "Content": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "ClientToken": NotRequired[str],
    },
)

CreateContactFlowModuleResponseTypeDef = TypedDict(
    "CreateContactFlowModuleResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateContactFlowRequestRequestTypeDef = TypedDict(
    "CreateContactFlowRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "Type": ContactFlowTypeType,
        "Content": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateContactFlowResponseTypeDef = TypedDict(
    "CreateContactFlowResponseTypeDef",
    {
        "ContactFlowId": str,
        "ContactFlowArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateHoursOfOperationRequestRequestTypeDef = TypedDict(
    "CreateHoursOfOperationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "TimeZone": str,
        "Config": Sequence["HoursOfOperationConfigTypeDef"],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateHoursOfOperationResponseTypeDef = TypedDict(
    "CreateHoursOfOperationResponseTypeDef",
    {
        "HoursOfOperationId": str,
        "HoursOfOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInstanceRequestRequestTypeDef = TypedDict(
    "CreateInstanceRequestRequestTypeDef",
    {
        "IdentityManagementType": DirectoryTypeType,
        "InboundCallsEnabled": bool,
        "OutboundCallsEnabled": bool,
        "ClientToken": NotRequired[str],
        "InstanceAlias": NotRequired[str],
        "DirectoryId": NotRequired[str],
    },
)

CreateInstanceResponseTypeDef = TypedDict(
    "CreateInstanceResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIntegrationAssociationRequestRequestTypeDef = TypedDict(
    "CreateIntegrationAssociationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationType": IntegrationTypeType,
        "IntegrationArn": str,
        "SourceApplicationUrl": NotRequired[str],
        "SourceApplicationName": NotRequired[str],
        "SourceType": NotRequired[SourceTypeType],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateIntegrationAssociationResponseTypeDef = TypedDict(
    "CreateIntegrationAssociationResponseTypeDef",
    {
        "IntegrationAssociationId": str,
        "IntegrationAssociationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateQueueRequestRequestTypeDef = TypedDict(
    "CreateQueueRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "HoursOfOperationId": str,
        "Description": NotRequired[str],
        "OutboundCallerConfig": NotRequired["OutboundCallerConfigTypeDef"],
        "MaxContacts": NotRequired[int],
        "QuickConnectIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateQueueResponseTypeDef = TypedDict(
    "CreateQueueResponseTypeDef",
    {
        "QueueArn": str,
        "QueueId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateQuickConnectRequestRequestTypeDef = TypedDict(
    "CreateQuickConnectRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "QuickConnectConfig": "QuickConnectConfigTypeDef",
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateQuickConnectResponseTypeDef = TypedDict(
    "CreateQuickConnectResponseTypeDef",
    {
        "QuickConnectARN": str,
        "QuickConnectId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRoutingProfileRequestRequestTypeDef = TypedDict(
    "CreateRoutingProfileRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "Description": str,
        "DefaultOutboundQueueId": str,
        "MediaConcurrencies": Sequence["MediaConcurrencyTypeDef"],
        "QueueConfigs": NotRequired[Sequence["RoutingProfileQueueConfigTypeDef"]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateRoutingProfileResponseTypeDef = TypedDict(
    "CreateRoutingProfileResponseTypeDef",
    {
        "RoutingProfileArn": str,
        "RoutingProfileId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSecurityProfileRequestRequestTypeDef = TypedDict(
    "CreateSecurityProfileRequestRequestTypeDef",
    {
        "SecurityProfileName": str,
        "InstanceId": str,
        "Description": NotRequired[str],
        "Permissions": NotRequired[Sequence[str]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateSecurityProfileResponseTypeDef = TypedDict(
    "CreateSecurityProfileResponseTypeDef",
    {
        "SecurityProfileId": str,
        "SecurityProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUseCaseRequestRequestTypeDef = TypedDict(
    "CreateUseCaseRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationAssociationId": str,
        "UseCaseType": UseCaseTypeType,
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateUseCaseResponseTypeDef = TypedDict(
    "CreateUseCaseResponseTypeDef",
    {
        "UseCaseId": str,
        "UseCaseArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserHierarchyGroupRequestRequestTypeDef = TypedDict(
    "CreateUserHierarchyGroupRequestRequestTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "ParentGroupId": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateUserHierarchyGroupResponseTypeDef = TypedDict(
    "CreateUserHierarchyGroupResponseTypeDef",
    {
        "HierarchyGroupId": str,
        "HierarchyGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "Username": str,
        "PhoneConfig": "UserPhoneConfigTypeDef",
        "SecurityProfileIds": Sequence[str],
        "RoutingProfileId": str,
        "InstanceId": str,
        "Password": NotRequired[str],
        "IdentityInfo": NotRequired["UserIdentityInfoTypeDef"],
        "DirectoryUserId": NotRequired[str],
        "HierarchyGroupId": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "UserId": str,
        "UserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVocabularyRequestRequestTypeDef = TypedDict(
    "CreateVocabularyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "VocabularyName": str,
        "LanguageCode": VocabularyLanguageCodeType,
        "Content": str,
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateVocabularyResponseTypeDef = TypedDict(
    "CreateVocabularyResponseTypeDef",
    {
        "VocabularyArn": str,
        "VocabularyId": str,
        "State": VocabularyStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "AccessToken": NotRequired[str],
        "AccessTokenExpiration": NotRequired[datetime],
        "RefreshToken": NotRequired[str],
        "RefreshTokenExpiration": NotRequired[datetime],
    },
)

CurrentMetricDataTypeDef = TypedDict(
    "CurrentMetricDataTypeDef",
    {
        "Metric": NotRequired["CurrentMetricTypeDef"],
        "Value": NotRequired[float],
    },
)

CurrentMetricResultTypeDef = TypedDict(
    "CurrentMetricResultTypeDef",
    {
        "Dimensions": NotRequired["DimensionsTypeDef"],
        "Collections": NotRequired[List["CurrentMetricDataTypeDef"]],
    },
)

CurrentMetricTypeDef = TypedDict(
    "CurrentMetricTypeDef",
    {
        "Name": NotRequired[CurrentMetricNameType],
        "Unit": NotRequired[UnitType],
    },
)

DefaultVocabularyTypeDef = TypedDict(
    "DefaultVocabularyTypeDef",
    {
        "InstanceId": str,
        "LanguageCode": VocabularyLanguageCodeType,
        "VocabularyId": str,
        "VocabularyName": str,
    },
)

DeleteContactFlowModuleRequestRequestTypeDef = TypedDict(
    "DeleteContactFlowModuleRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowModuleId": str,
    },
)

DeleteContactFlowRequestRequestTypeDef = TypedDict(
    "DeleteContactFlowRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
    },
)

DeleteHoursOfOperationRequestRequestTypeDef = TypedDict(
    "DeleteHoursOfOperationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "HoursOfOperationId": str,
    },
)

DeleteInstanceRequestRequestTypeDef = TypedDict(
    "DeleteInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

DeleteIntegrationAssociationRequestRequestTypeDef = TypedDict(
    "DeleteIntegrationAssociationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationAssociationId": str,
    },
)

DeleteQuickConnectRequestRequestTypeDef = TypedDict(
    "DeleteQuickConnectRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QuickConnectId": str,
    },
)

DeleteSecurityProfileRequestRequestTypeDef = TypedDict(
    "DeleteSecurityProfileRequestRequestTypeDef",
    {
        "InstanceId": str,
        "SecurityProfileId": str,
    },
)

DeleteUseCaseRequestRequestTypeDef = TypedDict(
    "DeleteUseCaseRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationAssociationId": str,
        "UseCaseId": str,
    },
)

DeleteUserHierarchyGroupRequestRequestTypeDef = TypedDict(
    "DeleteUserHierarchyGroupRequestRequestTypeDef",
    {
        "HierarchyGroupId": str,
        "InstanceId": str,
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "InstanceId": str,
        "UserId": str,
    },
)

DeleteVocabularyRequestRequestTypeDef = TypedDict(
    "DeleteVocabularyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "VocabularyId": str,
    },
)

DeleteVocabularyResponseTypeDef = TypedDict(
    "DeleteVocabularyResponseTypeDef",
    {
        "VocabularyArn": str,
        "VocabularyId": str,
        "State": VocabularyStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAgentStatusRequestRequestTypeDef = TypedDict(
    "DescribeAgentStatusRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AgentStatusId": str,
    },
)

DescribeAgentStatusResponseTypeDef = TypedDict(
    "DescribeAgentStatusResponseTypeDef",
    {
        "AgentStatus": "AgentStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContactFlowModuleRequestRequestTypeDef = TypedDict(
    "DescribeContactFlowModuleRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowModuleId": str,
    },
)

DescribeContactFlowModuleResponseTypeDef = TypedDict(
    "DescribeContactFlowModuleResponseTypeDef",
    {
        "ContactFlowModule": "ContactFlowModuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContactFlowRequestRequestTypeDef = TypedDict(
    "DescribeContactFlowRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
    },
)

DescribeContactFlowResponseTypeDef = TypedDict(
    "DescribeContactFlowResponseTypeDef",
    {
        "ContactFlow": "ContactFlowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContactRequestRequestTypeDef = TypedDict(
    "DescribeContactRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
    },
)

DescribeContactResponseTypeDef = TypedDict(
    "DescribeContactResponseTypeDef",
    {
        "Contact": "ContactTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHoursOfOperationRequestRequestTypeDef = TypedDict(
    "DescribeHoursOfOperationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "HoursOfOperationId": str,
    },
)

DescribeHoursOfOperationResponseTypeDef = TypedDict(
    "DescribeHoursOfOperationResponseTypeDef",
    {
        "HoursOfOperation": "HoursOfOperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceAttributeRequestRequestTypeDef = TypedDict(
    "DescribeInstanceAttributeRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AttributeType": InstanceAttributeTypeType,
    },
)

DescribeInstanceAttributeResponseTypeDef = TypedDict(
    "DescribeInstanceAttributeResponseTypeDef",
    {
        "Attribute": "AttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceRequestRequestTypeDef = TypedDict(
    "DescribeInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

DescribeInstanceResponseTypeDef = TypedDict(
    "DescribeInstanceResponseTypeDef",
    {
        "Instance": "InstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceStorageConfigRequestRequestTypeDef = TypedDict(
    "DescribeInstanceStorageConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AssociationId": str,
        "ResourceType": InstanceStorageResourceTypeType,
    },
)

DescribeInstanceStorageConfigResponseTypeDef = TypedDict(
    "DescribeInstanceStorageConfigResponseTypeDef",
    {
        "StorageConfig": "InstanceStorageConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQueueRequestRequestTypeDef = TypedDict(
    "DescribeQueueRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
    },
)

DescribeQueueResponseTypeDef = TypedDict(
    "DescribeQueueResponseTypeDef",
    {
        "Queue": "QueueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQuickConnectRequestRequestTypeDef = TypedDict(
    "DescribeQuickConnectRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QuickConnectId": str,
    },
)

DescribeQuickConnectResponseTypeDef = TypedDict(
    "DescribeQuickConnectResponseTypeDef",
    {
        "QuickConnect": "QuickConnectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRoutingProfileRequestRequestTypeDef = TypedDict(
    "DescribeRoutingProfileRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
    },
)

DescribeRoutingProfileResponseTypeDef = TypedDict(
    "DescribeRoutingProfileResponseTypeDef",
    {
        "RoutingProfile": "RoutingProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecurityProfileRequestRequestTypeDef = TypedDict(
    "DescribeSecurityProfileRequestRequestTypeDef",
    {
        "SecurityProfileId": str,
        "InstanceId": str,
    },
)

DescribeSecurityProfileResponseTypeDef = TypedDict(
    "DescribeSecurityProfileResponseTypeDef",
    {
        "SecurityProfile": "SecurityProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserHierarchyGroupRequestRequestTypeDef = TypedDict(
    "DescribeUserHierarchyGroupRequestRequestTypeDef",
    {
        "HierarchyGroupId": str,
        "InstanceId": str,
    },
)

DescribeUserHierarchyGroupResponseTypeDef = TypedDict(
    "DescribeUserHierarchyGroupResponseTypeDef",
    {
        "HierarchyGroup": "HierarchyGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserHierarchyStructureRequestRequestTypeDef = TypedDict(
    "DescribeUserHierarchyStructureRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

DescribeUserHierarchyStructureResponseTypeDef = TypedDict(
    "DescribeUserHierarchyStructureResponseTypeDef",
    {
        "HierarchyStructure": "HierarchyStructureTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserRequestRequestTypeDef = TypedDict(
    "DescribeUserRequestRequestTypeDef",
    {
        "UserId": str,
        "InstanceId": str,
    },
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVocabularyRequestRequestTypeDef = TypedDict(
    "DescribeVocabularyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "VocabularyId": str,
    },
)

DescribeVocabularyResponseTypeDef = TypedDict(
    "DescribeVocabularyResponseTypeDef",
    {
        "Vocabulary": "VocabularyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DimensionsTypeDef = TypedDict(
    "DimensionsTypeDef",
    {
        "Queue": NotRequired["QueueReferenceTypeDef"],
        "Channel": NotRequired[ChannelType],
    },
)

DisassociateApprovedOriginRequestRequestTypeDef = TypedDict(
    "DisassociateApprovedOriginRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Origin": str,
    },
)

DisassociateBotRequestRequestTypeDef = TypedDict(
    "DisassociateBotRequestRequestTypeDef",
    {
        "InstanceId": str,
        "LexBot": NotRequired["LexBotTypeDef"],
        "LexV2Bot": NotRequired["LexV2BotTypeDef"],
    },
)

DisassociateInstanceStorageConfigRequestRequestTypeDef = TypedDict(
    "DisassociateInstanceStorageConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AssociationId": str,
        "ResourceType": InstanceStorageResourceTypeType,
    },
)

DisassociateLambdaFunctionRequestRequestTypeDef = TypedDict(
    "DisassociateLambdaFunctionRequestRequestTypeDef",
    {
        "InstanceId": str,
        "FunctionArn": str,
    },
)

DisassociateLexBotRequestRequestTypeDef = TypedDict(
    "DisassociateLexBotRequestRequestTypeDef",
    {
        "InstanceId": str,
        "BotName": str,
        "LexRegion": str,
    },
)

DisassociateQueueQuickConnectsRequestRequestTypeDef = TypedDict(
    "DisassociateQueueQuickConnectsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "QuickConnectIds": Sequence[str],
    },
)

DisassociateRoutingProfileQueuesRequestRequestTypeDef = TypedDict(
    "DisassociateRoutingProfileQueuesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "QueueReferences": Sequence["RoutingProfileQueueReferenceTypeDef"],
    },
)

DisassociateSecurityKeyRequestRequestTypeDef = TypedDict(
    "DisassociateSecurityKeyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AssociationId": str,
    },
)

EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef",
    {
        "EncryptionType": Literal["KMS"],
        "KeyId": str,
    },
)

FiltersTypeDef = TypedDict(
    "FiltersTypeDef",
    {
        "Queues": NotRequired[Sequence[str]],
        "Channels": NotRequired[Sequence[ChannelType]],
    },
)

GetContactAttributesRequestRequestTypeDef = TypedDict(
    "GetContactAttributesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "InitialContactId": str,
    },
)

GetContactAttributesResponseTypeDef = TypedDict(
    "GetContactAttributesResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCurrentMetricDataRequestRequestTypeDef = TypedDict(
    "GetCurrentMetricDataRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Filters": "FiltersTypeDef",
        "CurrentMetrics": Sequence["CurrentMetricTypeDef"],
        "Groupings": NotRequired[Sequence[GroupingType]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetCurrentMetricDataResponseTypeDef = TypedDict(
    "GetCurrentMetricDataResponseTypeDef",
    {
        "NextToken": str,
        "MetricResults": List["CurrentMetricResultTypeDef"],
        "DataSnapshotTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFederationTokenRequestRequestTypeDef = TypedDict(
    "GetFederationTokenRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

GetFederationTokenResponseTypeDef = TypedDict(
    "GetFederationTokenResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMetricDataRequestRequestTypeDef = TypedDict(
    "GetMetricDataRequestRequestTypeDef",
    {
        "InstanceId": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Filters": "FiltersTypeDef",
        "HistoricalMetrics": Sequence["HistoricalMetricTypeDef"],
        "Groupings": NotRequired[Sequence[GroupingType]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetMetricDataResponseTypeDef = TypedDict(
    "GetMetricDataResponseTypeDef",
    {
        "NextToken": str,
        "MetricResults": List["HistoricalMetricResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HierarchyGroupSummaryTypeDef = TypedDict(
    "HierarchyGroupSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)

HierarchyGroupTypeDef = TypedDict(
    "HierarchyGroupTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "LevelId": NotRequired[str],
        "HierarchyPath": NotRequired["HierarchyPathTypeDef"],
        "Tags": NotRequired[Dict[str, str]],
    },
)

HierarchyLevelTypeDef = TypedDict(
    "HierarchyLevelTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)

HierarchyLevelUpdateTypeDef = TypedDict(
    "HierarchyLevelUpdateTypeDef",
    {
        "Name": str,
    },
)

HierarchyPathTypeDef = TypedDict(
    "HierarchyPathTypeDef",
    {
        "LevelOne": NotRequired["HierarchyGroupSummaryTypeDef"],
        "LevelTwo": NotRequired["HierarchyGroupSummaryTypeDef"],
        "LevelThree": NotRequired["HierarchyGroupSummaryTypeDef"],
        "LevelFour": NotRequired["HierarchyGroupSummaryTypeDef"],
        "LevelFive": NotRequired["HierarchyGroupSummaryTypeDef"],
    },
)

HierarchyStructureTypeDef = TypedDict(
    "HierarchyStructureTypeDef",
    {
        "LevelOne": NotRequired["HierarchyLevelTypeDef"],
        "LevelTwo": NotRequired["HierarchyLevelTypeDef"],
        "LevelThree": NotRequired["HierarchyLevelTypeDef"],
        "LevelFour": NotRequired["HierarchyLevelTypeDef"],
        "LevelFive": NotRequired["HierarchyLevelTypeDef"],
    },
)

HierarchyStructureUpdateTypeDef = TypedDict(
    "HierarchyStructureUpdateTypeDef",
    {
        "LevelOne": NotRequired["HierarchyLevelUpdateTypeDef"],
        "LevelTwo": NotRequired["HierarchyLevelUpdateTypeDef"],
        "LevelThree": NotRequired["HierarchyLevelUpdateTypeDef"],
        "LevelFour": NotRequired["HierarchyLevelUpdateTypeDef"],
        "LevelFive": NotRequired["HierarchyLevelUpdateTypeDef"],
    },
)

HistoricalMetricDataTypeDef = TypedDict(
    "HistoricalMetricDataTypeDef",
    {
        "Metric": NotRequired["HistoricalMetricTypeDef"],
        "Value": NotRequired[float],
    },
)

HistoricalMetricResultTypeDef = TypedDict(
    "HistoricalMetricResultTypeDef",
    {
        "Dimensions": NotRequired["DimensionsTypeDef"],
        "Collections": NotRequired[List["HistoricalMetricDataTypeDef"]],
    },
)

HistoricalMetricTypeDef = TypedDict(
    "HistoricalMetricTypeDef",
    {
        "Name": NotRequired[HistoricalMetricNameType],
        "Threshold": NotRequired["ThresholdTypeDef"],
        "Statistic": NotRequired[StatisticType],
        "Unit": NotRequired[UnitType],
    },
)

HoursOfOperationConfigTypeDef = TypedDict(
    "HoursOfOperationConfigTypeDef",
    {
        "Day": HoursOfOperationDaysType,
        "StartTime": "HoursOfOperationTimeSliceTypeDef",
        "EndTime": "HoursOfOperationTimeSliceTypeDef",
    },
)

HoursOfOperationSummaryTypeDef = TypedDict(
    "HoursOfOperationSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)

HoursOfOperationTimeSliceTypeDef = TypedDict(
    "HoursOfOperationTimeSliceTypeDef",
    {
        "Hours": int,
        "Minutes": int,
    },
)

HoursOfOperationTypeDef = TypedDict(
    "HoursOfOperationTypeDef",
    {
        "HoursOfOperationId": NotRequired[str],
        "HoursOfOperationArn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "TimeZone": NotRequired[str],
        "Config": NotRequired[List["HoursOfOperationConfigTypeDef"]],
        "Tags": NotRequired[Dict[str, str]],
    },
)

InstanceStatusReasonTypeDef = TypedDict(
    "InstanceStatusReasonTypeDef",
    {
        "Message": NotRequired[str],
    },
)

InstanceStorageConfigTypeDef = TypedDict(
    "InstanceStorageConfigTypeDef",
    {
        "StorageType": StorageTypeType,
        "AssociationId": NotRequired[str],
        "S3Config": NotRequired["S3ConfigTypeDef"],
        "KinesisVideoStreamConfig": NotRequired["KinesisVideoStreamConfigTypeDef"],
        "KinesisStreamConfig": NotRequired["KinesisStreamConfigTypeDef"],
        "KinesisFirehoseConfig": NotRequired["KinesisFirehoseConfigTypeDef"],
    },
)

InstanceSummaryTypeDef = TypedDict(
    "InstanceSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "IdentityManagementType": NotRequired[DirectoryTypeType],
        "InstanceAlias": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "ServiceRole": NotRequired[str],
        "InstanceStatus": NotRequired[InstanceStatusType],
        "InboundCallsEnabled": NotRequired[bool],
        "OutboundCallsEnabled": NotRequired[bool],
    },
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "IdentityManagementType": NotRequired[DirectoryTypeType],
        "InstanceAlias": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "ServiceRole": NotRequired[str],
        "InstanceStatus": NotRequired[InstanceStatusType],
        "StatusReason": NotRequired["InstanceStatusReasonTypeDef"],
        "InboundCallsEnabled": NotRequired[bool],
        "OutboundCallsEnabled": NotRequired[bool],
    },
)

IntegrationAssociationSummaryTypeDef = TypedDict(
    "IntegrationAssociationSummaryTypeDef",
    {
        "IntegrationAssociationId": NotRequired[str],
        "IntegrationAssociationArn": NotRequired[str],
        "InstanceId": NotRequired[str],
        "IntegrationType": NotRequired[IntegrationTypeType],
        "IntegrationArn": NotRequired[str],
        "SourceApplicationUrl": NotRequired[str],
        "SourceApplicationName": NotRequired[str],
        "SourceType": NotRequired[SourceTypeType],
    },
)

KinesisFirehoseConfigTypeDef = TypedDict(
    "KinesisFirehoseConfigTypeDef",
    {
        "FirehoseArn": str,
    },
)

KinesisStreamConfigTypeDef = TypedDict(
    "KinesisStreamConfigTypeDef",
    {
        "StreamArn": str,
    },
)

KinesisVideoStreamConfigTypeDef = TypedDict(
    "KinesisVideoStreamConfigTypeDef",
    {
        "Prefix": str,
        "RetentionPeriodHours": int,
        "EncryptionConfig": "EncryptionConfigTypeDef",
    },
)

LexBotConfigTypeDef = TypedDict(
    "LexBotConfigTypeDef",
    {
        "LexBot": NotRequired["LexBotTypeDef"],
        "LexV2Bot": NotRequired["LexV2BotTypeDef"],
    },
)

LexBotTypeDef = TypedDict(
    "LexBotTypeDef",
    {
        "Name": NotRequired[str],
        "LexRegion": NotRequired[str],
    },
)

LexV2BotTypeDef = TypedDict(
    "LexV2BotTypeDef",
    {
        "AliasArn": NotRequired[str],
    },
)

ListAgentStatusRequestRequestTypeDef = TypedDict(
    "ListAgentStatusRequestRequestTypeDef",
    {
        "InstanceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "AgentStatusTypes": NotRequired[Sequence[AgentStatusTypeType]],
    },
)

ListAgentStatusResponseTypeDef = TypedDict(
    "ListAgentStatusResponseTypeDef",
    {
        "NextToken": str,
        "AgentStatusSummaryList": List["AgentStatusSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApprovedOriginsRequestRequestTypeDef = TypedDict(
    "ListApprovedOriginsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListApprovedOriginsResponseTypeDef = TypedDict(
    "ListApprovedOriginsResponseTypeDef",
    {
        "Origins": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBotsRequestRequestTypeDef = TypedDict(
    "ListBotsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "LexVersion": LexVersionType,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListBotsResponseTypeDef = TypedDict(
    "ListBotsResponseTypeDef",
    {
        "LexBots": List["LexBotConfigTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContactFlowModulesRequestRequestTypeDef = TypedDict(
    "ListContactFlowModulesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ContactFlowModuleState": NotRequired[ContactFlowModuleStateType],
    },
)

ListContactFlowModulesResponseTypeDef = TypedDict(
    "ListContactFlowModulesResponseTypeDef",
    {
        "ContactFlowModulesSummaryList": List["ContactFlowModuleSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContactFlowsRequestRequestTypeDef = TypedDict(
    "ListContactFlowsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowTypes": NotRequired[Sequence[ContactFlowTypeType]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListContactFlowsResponseTypeDef = TypedDict(
    "ListContactFlowsResponseTypeDef",
    {
        "ContactFlowSummaryList": List["ContactFlowSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContactReferencesRequestRequestTypeDef = TypedDict(
    "ListContactReferencesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "ReferenceTypes": Sequence[ReferenceTypeType],
        "NextToken": NotRequired[str],
    },
)

ListContactReferencesResponseTypeDef = TypedDict(
    "ListContactReferencesResponseTypeDef",
    {
        "ReferenceSummaryList": List["ReferenceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDefaultVocabulariesRequestRequestTypeDef = TypedDict(
    "ListDefaultVocabulariesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "LanguageCode": NotRequired[VocabularyLanguageCodeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListDefaultVocabulariesResponseTypeDef = TypedDict(
    "ListDefaultVocabulariesResponseTypeDef",
    {
        "DefaultVocabularyList": List["DefaultVocabularyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHoursOfOperationsRequestRequestTypeDef = TypedDict(
    "ListHoursOfOperationsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListHoursOfOperationsResponseTypeDef = TypedDict(
    "ListHoursOfOperationsResponseTypeDef",
    {
        "HoursOfOperationSummaryList": List["HoursOfOperationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstanceAttributesRequestRequestTypeDef = TypedDict(
    "ListInstanceAttributesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListInstanceAttributesResponseTypeDef = TypedDict(
    "ListInstanceAttributesResponseTypeDef",
    {
        "Attributes": List["AttributeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstanceStorageConfigsRequestRequestTypeDef = TypedDict(
    "ListInstanceStorageConfigsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ResourceType": InstanceStorageResourceTypeType,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListInstanceStorageConfigsResponseTypeDef = TypedDict(
    "ListInstanceStorageConfigsResponseTypeDef",
    {
        "StorageConfigs": List["InstanceStorageConfigTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstancesRequestRequestTypeDef = TypedDict(
    "ListInstancesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListInstancesResponseTypeDef = TypedDict(
    "ListInstancesResponseTypeDef",
    {
        "InstanceSummaryList": List["InstanceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "ListIntegrationAssociationsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationType": NotRequired[IntegrationTypeType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListIntegrationAssociationsResponseTypeDef = TypedDict(
    "ListIntegrationAssociationsResponseTypeDef",
    {
        "IntegrationAssociationSummaryList": List["IntegrationAssociationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLambdaFunctionsRequestRequestTypeDef = TypedDict(
    "ListLambdaFunctionsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListLambdaFunctionsResponseTypeDef = TypedDict(
    "ListLambdaFunctionsResponseTypeDef",
    {
        "LambdaFunctions": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLexBotsRequestRequestTypeDef = TypedDict(
    "ListLexBotsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListLexBotsResponseTypeDef = TypedDict(
    "ListLexBotsResponseTypeDef",
    {
        "LexBots": List["LexBotTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPhoneNumbersRequestRequestTypeDef = TypedDict(
    "ListPhoneNumbersRequestRequestTypeDef",
    {
        "InstanceId": str,
        "PhoneNumberTypes": NotRequired[Sequence[PhoneNumberTypeType]],
        "PhoneNumberCountryCodes": NotRequired[Sequence[PhoneNumberCountryCodeType]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListPhoneNumbersResponseTypeDef = TypedDict(
    "ListPhoneNumbersResponseTypeDef",
    {
        "PhoneNumberSummaryList": List["PhoneNumberSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPromptsRequestRequestTypeDef = TypedDict(
    "ListPromptsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListPromptsResponseTypeDef = TypedDict(
    "ListPromptsResponseTypeDef",
    {
        "PromptSummaryList": List["PromptSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQueueQuickConnectsRequestRequestTypeDef = TypedDict(
    "ListQueueQuickConnectsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListQueueQuickConnectsResponseTypeDef = TypedDict(
    "ListQueueQuickConnectsResponseTypeDef",
    {
        "NextToken": str,
        "QuickConnectSummaryList": List["QuickConnectSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQueuesRequestRequestTypeDef = TypedDict(
    "ListQueuesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueTypes": NotRequired[Sequence[QueueTypeType]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListQueuesResponseTypeDef = TypedDict(
    "ListQueuesResponseTypeDef",
    {
        "QueueSummaryList": List["QueueSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQuickConnectsRequestRequestTypeDef = TypedDict(
    "ListQuickConnectsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "QuickConnectTypes": NotRequired[Sequence[QuickConnectTypeType]],
    },
)

ListQuickConnectsResponseTypeDef = TypedDict(
    "ListQuickConnectsResponseTypeDef",
    {
        "QuickConnectSummaryList": List["QuickConnectSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRoutingProfileQueuesRequestRequestTypeDef = TypedDict(
    "ListRoutingProfileQueuesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListRoutingProfileQueuesResponseTypeDef = TypedDict(
    "ListRoutingProfileQueuesResponseTypeDef",
    {
        "NextToken": str,
        "RoutingProfileQueueConfigSummaryList": List["RoutingProfileQueueConfigSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRoutingProfilesRequestRequestTypeDef = TypedDict(
    "ListRoutingProfilesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListRoutingProfilesResponseTypeDef = TypedDict(
    "ListRoutingProfilesResponseTypeDef",
    {
        "RoutingProfileSummaryList": List["RoutingProfileSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSecurityKeysRequestRequestTypeDef = TypedDict(
    "ListSecurityKeysRequestRequestTypeDef",
    {
        "InstanceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListSecurityKeysResponseTypeDef = TypedDict(
    "ListSecurityKeysResponseTypeDef",
    {
        "SecurityKeys": List["SecurityKeyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSecurityProfilePermissionsRequestRequestTypeDef = TypedDict(
    "ListSecurityProfilePermissionsRequestRequestTypeDef",
    {
        "SecurityProfileId": str,
        "InstanceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListSecurityProfilePermissionsResponseTypeDef = TypedDict(
    "ListSecurityProfilePermissionsResponseTypeDef",
    {
        "Permissions": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSecurityProfilesRequestRequestTypeDef = TypedDict(
    "ListSecurityProfilesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListSecurityProfilesResponseTypeDef = TypedDict(
    "ListSecurityProfilesResponseTypeDef",
    {
        "SecurityProfileSummaryList": List["SecurityProfileSummaryTypeDef"],
        "NextToken": str,
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

ListUseCasesRequestRequestTypeDef = TypedDict(
    "ListUseCasesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationAssociationId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListUseCasesResponseTypeDef = TypedDict(
    "ListUseCasesResponseTypeDef",
    {
        "UseCaseSummaryList": List["UseCaseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUserHierarchyGroupsRequestRequestTypeDef = TypedDict(
    "ListUserHierarchyGroupsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListUserHierarchyGroupsResponseTypeDef = TypedDict(
    "ListUserHierarchyGroupsResponseTypeDef",
    {
        "UserHierarchyGroupSummaryList": List["HierarchyGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUsersRequestRequestTypeDef = TypedDict(
    "ListUsersRequestRequestTypeDef",
    {
        "InstanceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "UserSummaryList": List["UserSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MediaConcurrencyTypeDef = TypedDict(
    "MediaConcurrencyTypeDef",
    {
        "Channel": ChannelType,
        "Concurrency": int,
    },
)

OutboundCallerConfigTypeDef = TypedDict(
    "OutboundCallerConfigTypeDef",
    {
        "OutboundCallerIdName": NotRequired[str],
        "OutboundCallerIdNumberId": NotRequired[str],
        "OutboundFlowId": NotRequired[str],
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

ParticipantDetailsTypeDef = TypedDict(
    "ParticipantDetailsTypeDef",
    {
        "DisplayName": str,
    },
)

PhoneNumberQuickConnectConfigTypeDef = TypedDict(
    "PhoneNumberQuickConnectConfigTypeDef",
    {
        "PhoneNumber": str,
    },
)

PhoneNumberSummaryTypeDef = TypedDict(
    "PhoneNumberSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "PhoneNumberType": NotRequired[PhoneNumberTypeType],
        "PhoneNumberCountryCode": NotRequired[PhoneNumberCountryCodeType],
    },
)

PromptSummaryTypeDef = TypedDict(
    "PromptSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)

QueueInfoTypeDef = TypedDict(
    "QueueInfoTypeDef",
    {
        "Id": NotRequired[str],
        "EnqueueTimestamp": NotRequired[datetime],
    },
)

QueueQuickConnectConfigTypeDef = TypedDict(
    "QueueQuickConnectConfigTypeDef",
    {
        "QueueId": str,
        "ContactFlowId": str,
    },
)

QueueReferenceTypeDef = TypedDict(
    "QueueReferenceTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
    },
)

QueueSummaryTypeDef = TypedDict(
    "QueueSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "QueueType": NotRequired[QueueTypeType],
    },
)

QueueTypeDef = TypedDict(
    "QueueTypeDef",
    {
        "Name": NotRequired[str],
        "QueueArn": NotRequired[str],
        "QueueId": NotRequired[str],
        "Description": NotRequired[str],
        "OutboundCallerConfig": NotRequired["OutboundCallerConfigTypeDef"],
        "HoursOfOperationId": NotRequired[str],
        "MaxContacts": NotRequired[int],
        "Status": NotRequired[QueueStatusType],
        "Tags": NotRequired[Dict[str, str]],
    },
)

QuickConnectConfigTypeDef = TypedDict(
    "QuickConnectConfigTypeDef",
    {
        "QuickConnectType": QuickConnectTypeType,
        "UserConfig": NotRequired["UserQuickConnectConfigTypeDef"],
        "QueueConfig": NotRequired["QueueQuickConnectConfigTypeDef"],
        "PhoneConfig": NotRequired["PhoneNumberQuickConnectConfigTypeDef"],
    },
)

QuickConnectSummaryTypeDef = TypedDict(
    "QuickConnectSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "QuickConnectType": NotRequired[QuickConnectTypeType],
    },
)

QuickConnectTypeDef = TypedDict(
    "QuickConnectTypeDef",
    {
        "QuickConnectARN": NotRequired[str],
        "QuickConnectId": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "QuickConnectConfig": NotRequired["QuickConnectConfigTypeDef"],
        "Tags": NotRequired[Dict[str, str]],
    },
)

ReferenceSummaryTypeDef = TypedDict(
    "ReferenceSummaryTypeDef",
    {
        "Url": NotRequired["UrlReferenceTypeDef"],
        "Attachment": NotRequired["AttachmentReferenceTypeDef"],
    },
)

ReferenceTypeDef = TypedDict(
    "ReferenceTypeDef",
    {
        "Value": str,
        "Type": ReferenceTypeType,
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

ResumeContactRecordingRequestRequestTypeDef = TypedDict(
    "ResumeContactRecordingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "InitialContactId": str,
    },
)

RoutingProfileQueueConfigSummaryTypeDef = TypedDict(
    "RoutingProfileQueueConfigSummaryTypeDef",
    {
        "QueueId": str,
        "QueueArn": str,
        "QueueName": str,
        "Priority": int,
        "Delay": int,
        "Channel": ChannelType,
    },
)

RoutingProfileQueueConfigTypeDef = TypedDict(
    "RoutingProfileQueueConfigTypeDef",
    {
        "QueueReference": "RoutingProfileQueueReferenceTypeDef",
        "Priority": int,
        "Delay": int,
    },
)

RoutingProfileQueueReferenceTypeDef = TypedDict(
    "RoutingProfileQueueReferenceTypeDef",
    {
        "QueueId": str,
        "Channel": ChannelType,
    },
)

RoutingProfileSummaryTypeDef = TypedDict(
    "RoutingProfileSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)

RoutingProfileTypeDef = TypedDict(
    "RoutingProfileTypeDef",
    {
        "InstanceId": NotRequired[str],
        "Name": NotRequired[str],
        "RoutingProfileArn": NotRequired[str],
        "RoutingProfileId": NotRequired[str],
        "Description": NotRequired[str],
        "MediaConcurrencies": NotRequired[List["MediaConcurrencyTypeDef"]],
        "DefaultOutboundQueueId": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)

S3ConfigTypeDef = TypedDict(
    "S3ConfigTypeDef",
    {
        "BucketName": str,
        "BucketPrefix": str,
        "EncryptionConfig": NotRequired["EncryptionConfigTypeDef"],
    },
)

SearchVocabulariesRequestRequestTypeDef = TypedDict(
    "SearchVocabulariesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "State": NotRequired[VocabularyStateType],
        "NameStartsWith": NotRequired[str],
        "LanguageCode": NotRequired[VocabularyLanguageCodeType],
    },
)

SearchVocabulariesResponseTypeDef = TypedDict(
    "SearchVocabulariesResponseTypeDef",
    {
        "VocabularySummaryList": List["VocabularySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SecurityKeyTypeDef = TypedDict(
    "SecurityKeyTypeDef",
    {
        "AssociationId": NotRequired[str],
        "Key": NotRequired[str],
        "CreationTime": NotRequired[datetime],
    },
)

SecurityProfileSummaryTypeDef = TypedDict(
    "SecurityProfileSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)

SecurityProfileTypeDef = TypedDict(
    "SecurityProfileTypeDef",
    {
        "Id": NotRequired[str],
        "OrganizationResourceId": NotRequired[str],
        "Arn": NotRequired[str],
        "SecurityProfileName": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)

StartChatContactRequestRequestTypeDef = TypedDict(
    "StartChatContactRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
        "ParticipantDetails": "ParticipantDetailsTypeDef",
        "Attributes": NotRequired[Mapping[str, str]],
        "InitialMessage": NotRequired["ChatMessageTypeDef"],
        "ClientToken": NotRequired[str],
        "ChatDurationInMinutes": NotRequired[int],
        "SupportedMessagingContentTypes": NotRequired[Sequence[str]],
    },
)

StartChatContactResponseTypeDef = TypedDict(
    "StartChatContactResponseTypeDef",
    {
        "ContactId": str,
        "ParticipantId": str,
        "ParticipantToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartContactRecordingRequestRequestTypeDef = TypedDict(
    "StartContactRecordingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "InitialContactId": str,
        "VoiceRecordingConfiguration": "VoiceRecordingConfigurationTypeDef",
    },
)

StartContactStreamingRequestRequestTypeDef = TypedDict(
    "StartContactStreamingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "ChatStreamingConfiguration": "ChatStreamingConfigurationTypeDef",
        "ClientToken": str,
    },
)

StartContactStreamingResponseTypeDef = TypedDict(
    "StartContactStreamingResponseTypeDef",
    {
        "StreamingId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartOutboundVoiceContactRequestRequestTypeDef = TypedDict(
    "StartOutboundVoiceContactRequestRequestTypeDef",
    {
        "DestinationPhoneNumber": str,
        "ContactFlowId": str,
        "InstanceId": str,
        "ClientToken": NotRequired[str],
        "SourcePhoneNumber": NotRequired[str],
        "QueueId": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
        "AnswerMachineDetectionConfig": NotRequired["AnswerMachineDetectionConfigTypeDef"],
        "CampaignId": NotRequired[str],
        "TrafficType": NotRequired[TrafficTypeType],
    },
)

StartOutboundVoiceContactResponseTypeDef = TypedDict(
    "StartOutboundVoiceContactResponseTypeDef",
    {
        "ContactId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartTaskContactRequestRequestTypeDef = TypedDict(
    "StartTaskContactRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
        "Name": str,
        "PreviousContactId": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
        "References": NotRequired[Mapping[str, "ReferenceTypeDef"]],
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
        "ScheduledTime": NotRequired[Union[datetime, str]],
    },
)

StartTaskContactResponseTypeDef = TypedDict(
    "StartTaskContactResponseTypeDef",
    {
        "ContactId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopContactRecordingRequestRequestTypeDef = TypedDict(
    "StopContactRecordingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "InitialContactId": str,
    },
)

StopContactRequestRequestTypeDef = TypedDict(
    "StopContactRequestRequestTypeDef",
    {
        "ContactId": str,
        "InstanceId": str,
    },
)

StopContactStreamingRequestRequestTypeDef = TypedDict(
    "StopContactStreamingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "StreamingId": str,
    },
)

SuspendContactRecordingRequestRequestTypeDef = TypedDict(
    "SuspendContactRecordingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "InitialContactId": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

ThresholdTypeDef = TypedDict(
    "ThresholdTypeDef",
    {
        "Comparison": NotRequired[Literal["LT"]],
        "ThresholdValue": NotRequired[float],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateAgentStatusRequestRequestTypeDef = TypedDict(
    "UpdateAgentStatusRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AgentStatusId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "State": NotRequired[AgentStatusStateType],
        "DisplayOrder": NotRequired[int],
        "ResetOrderNumber": NotRequired[bool],
    },
)

UpdateContactAttributesRequestRequestTypeDef = TypedDict(
    "UpdateContactAttributesRequestRequestTypeDef",
    {
        "InitialContactId": str,
        "InstanceId": str,
        "Attributes": Mapping[str, str],
    },
)

UpdateContactFlowContentRequestRequestTypeDef = TypedDict(
    "UpdateContactFlowContentRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
        "Content": str,
    },
)

UpdateContactFlowMetadataRequestRequestTypeDef = TypedDict(
    "UpdateContactFlowMetadataRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ContactFlowState": NotRequired[ContactFlowStateType],
    },
)

UpdateContactFlowModuleContentRequestRequestTypeDef = TypedDict(
    "UpdateContactFlowModuleContentRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowModuleId": str,
        "Content": str,
    },
)

UpdateContactFlowModuleMetadataRequestRequestTypeDef = TypedDict(
    "UpdateContactFlowModuleMetadataRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowModuleId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "State": NotRequired[ContactFlowModuleStateType],
    },
)

UpdateContactFlowNameRequestRequestTypeDef = TypedDict(
    "UpdateContactFlowNameRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)

UpdateContactRequestRequestTypeDef = TypedDict(
    "UpdateContactRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "References": NotRequired[Mapping[str, "ReferenceTypeDef"]],
    },
)

UpdateContactScheduleRequestRequestTypeDef = TypedDict(
    "UpdateContactScheduleRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "ScheduledTime": Union[datetime, str],
    },
)

UpdateHoursOfOperationRequestRequestTypeDef = TypedDict(
    "UpdateHoursOfOperationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "HoursOfOperationId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "TimeZone": NotRequired[str],
        "Config": NotRequired[Sequence["HoursOfOperationConfigTypeDef"]],
    },
)

UpdateInstanceAttributeRequestRequestTypeDef = TypedDict(
    "UpdateInstanceAttributeRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AttributeType": InstanceAttributeTypeType,
        "Value": str,
    },
)

UpdateInstanceStorageConfigRequestRequestTypeDef = TypedDict(
    "UpdateInstanceStorageConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AssociationId": str,
        "ResourceType": InstanceStorageResourceTypeType,
        "StorageConfig": "InstanceStorageConfigTypeDef",
    },
)

UpdateQueueHoursOfOperationRequestRequestTypeDef = TypedDict(
    "UpdateQueueHoursOfOperationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "HoursOfOperationId": str,
    },
)

UpdateQueueMaxContactsRequestRequestTypeDef = TypedDict(
    "UpdateQueueMaxContactsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "MaxContacts": NotRequired[int],
    },
)

UpdateQueueNameRequestRequestTypeDef = TypedDict(
    "UpdateQueueNameRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)

UpdateQueueOutboundCallerConfigRequestRequestTypeDef = TypedDict(
    "UpdateQueueOutboundCallerConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "OutboundCallerConfig": "OutboundCallerConfigTypeDef",
    },
)

UpdateQueueStatusRequestRequestTypeDef = TypedDict(
    "UpdateQueueStatusRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "Status": QueueStatusType,
    },
)

UpdateQuickConnectConfigRequestRequestTypeDef = TypedDict(
    "UpdateQuickConnectConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QuickConnectId": str,
        "QuickConnectConfig": "QuickConnectConfigTypeDef",
    },
)

UpdateQuickConnectNameRequestRequestTypeDef = TypedDict(
    "UpdateQuickConnectNameRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QuickConnectId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)

UpdateRoutingProfileConcurrencyRequestRequestTypeDef = TypedDict(
    "UpdateRoutingProfileConcurrencyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "MediaConcurrencies": Sequence["MediaConcurrencyTypeDef"],
    },
)

UpdateRoutingProfileDefaultOutboundQueueRequestRequestTypeDef = TypedDict(
    "UpdateRoutingProfileDefaultOutboundQueueRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "DefaultOutboundQueueId": str,
    },
)

UpdateRoutingProfileNameRequestRequestTypeDef = TypedDict(
    "UpdateRoutingProfileNameRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)

UpdateRoutingProfileQueuesRequestRequestTypeDef = TypedDict(
    "UpdateRoutingProfileQueuesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "QueueConfigs": Sequence["RoutingProfileQueueConfigTypeDef"],
    },
)

UpdateSecurityProfileRequestRequestTypeDef = TypedDict(
    "UpdateSecurityProfileRequestRequestTypeDef",
    {
        "SecurityProfileId": str,
        "InstanceId": str,
        "Description": NotRequired[str],
        "Permissions": NotRequired[Sequence[str]],
    },
)

UpdateUserHierarchyGroupNameRequestRequestTypeDef = TypedDict(
    "UpdateUserHierarchyGroupNameRequestRequestTypeDef",
    {
        "Name": str,
        "HierarchyGroupId": str,
        "InstanceId": str,
    },
)

UpdateUserHierarchyRequestRequestTypeDef = TypedDict(
    "UpdateUserHierarchyRequestRequestTypeDef",
    {
        "UserId": str,
        "InstanceId": str,
        "HierarchyGroupId": NotRequired[str],
    },
)

UpdateUserHierarchyStructureRequestRequestTypeDef = TypedDict(
    "UpdateUserHierarchyStructureRequestRequestTypeDef",
    {
        "HierarchyStructure": "HierarchyStructureUpdateTypeDef",
        "InstanceId": str,
    },
)

UpdateUserIdentityInfoRequestRequestTypeDef = TypedDict(
    "UpdateUserIdentityInfoRequestRequestTypeDef",
    {
        "IdentityInfo": "UserIdentityInfoTypeDef",
        "UserId": str,
        "InstanceId": str,
    },
)

UpdateUserPhoneConfigRequestRequestTypeDef = TypedDict(
    "UpdateUserPhoneConfigRequestRequestTypeDef",
    {
        "PhoneConfig": "UserPhoneConfigTypeDef",
        "UserId": str,
        "InstanceId": str,
    },
)

UpdateUserRoutingProfileRequestRequestTypeDef = TypedDict(
    "UpdateUserRoutingProfileRequestRequestTypeDef",
    {
        "RoutingProfileId": str,
        "UserId": str,
        "InstanceId": str,
    },
)

UpdateUserSecurityProfilesRequestRequestTypeDef = TypedDict(
    "UpdateUserSecurityProfilesRequestRequestTypeDef",
    {
        "SecurityProfileIds": Sequence[str],
        "UserId": str,
        "InstanceId": str,
    },
)

UrlReferenceTypeDef = TypedDict(
    "UrlReferenceTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)

UseCaseTypeDef = TypedDict(
    "UseCaseTypeDef",
    {
        "UseCaseId": NotRequired[str],
        "UseCaseArn": NotRequired[str],
        "UseCaseType": NotRequired[UseCaseTypeType],
    },
)

UserIdentityInfoTypeDef = TypedDict(
    "UserIdentityInfoTypeDef",
    {
        "FirstName": NotRequired[str],
        "LastName": NotRequired[str],
        "Email": NotRequired[str],
    },
)

UserPhoneConfigTypeDef = TypedDict(
    "UserPhoneConfigTypeDef",
    {
        "PhoneType": PhoneTypeType,
        "AutoAccept": NotRequired[bool],
        "AfterContactWorkTimeLimit": NotRequired[int],
        "DeskPhoneNumber": NotRequired[str],
    },
)

UserQuickConnectConfigTypeDef = TypedDict(
    "UserQuickConnectConfigTypeDef",
    {
        "UserId": str,
        "ContactFlowId": str,
    },
)

UserSummaryTypeDef = TypedDict(
    "UserSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Username": NotRequired[str],
    },
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Username": NotRequired[str],
        "IdentityInfo": NotRequired["UserIdentityInfoTypeDef"],
        "PhoneConfig": NotRequired["UserPhoneConfigTypeDef"],
        "DirectoryUserId": NotRequired[str],
        "SecurityProfileIds": NotRequired[List[str]],
        "RoutingProfileId": NotRequired[str],
        "HierarchyGroupId": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)

VocabularySummaryTypeDef = TypedDict(
    "VocabularySummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Arn": str,
        "LanguageCode": VocabularyLanguageCodeType,
        "State": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": NotRequired[str],
    },
)

VocabularyTypeDef = TypedDict(
    "VocabularyTypeDef",
    {
        "Name": str,
        "Id": str,
        "Arn": str,
        "LanguageCode": VocabularyLanguageCodeType,
        "State": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": NotRequired[str],
        "Content": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)

VoiceRecordingConfigurationTypeDef = TypedDict(
    "VoiceRecordingConfigurationTypeDef",
    {
        "VoiceRecordingTrack": NotRequired[VoiceRecordingTrackType],
    },
)
