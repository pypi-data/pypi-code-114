"""
Type annotations for lexv2-models service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_lexv2_models.type_defs import AdvancedRecognitionSettingTypeDef

    data: AdvancedRecognitionSettingTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AggregatedUtterancesFilterOperatorType,
    AggregatedUtterancesSortAttributeType,
    AssociatedTranscriptFilterNameType,
    BotAliasStatusType,
    BotFilterOperatorType,
    BotLocaleFilterOperatorType,
    BotLocaleStatusType,
    BotRecommendationStatusType,
    BotStatusType,
    CustomVocabularyStatusType,
    EffectType,
    ExportFilterOperatorType,
    ExportStatusType,
    ImportExportFileFormatType,
    ImportFilterOperatorType,
    ImportResourceTypeType,
    ImportStatusType,
    IntentFilterOperatorType,
    IntentSortAttributeType,
    MergeStrategyType,
    ObfuscationSettingTypeType,
    SearchOrderType,
    SlotConstraintType,
    SlotFilterOperatorType,
    SlotSortAttributeType,
    SlotTypeCategoryType,
    SlotTypeFilterNameType,
    SlotTypeFilterOperatorType,
    SlotTypeSortAttributeType,
    SlotValueResolutionStrategyType,
    SortOrderType,
    TimeDimensionType,
    VoiceEngineType,
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
    "AdvancedRecognitionSettingTypeDef",
    "AggregatedUtterancesFilterTypeDef",
    "AggregatedUtterancesSortByTypeDef",
    "AggregatedUtterancesSummaryTypeDef",
    "AssociatedTranscriptFilterTypeDef",
    "AssociatedTranscriptTypeDef",
    "AudioLogDestinationTypeDef",
    "AudioLogSettingTypeDef",
    "BotAliasHistoryEventTypeDef",
    "BotAliasLocaleSettingsTypeDef",
    "BotAliasSummaryTypeDef",
    "BotExportSpecificationTypeDef",
    "BotFilterTypeDef",
    "BotImportSpecificationTypeDef",
    "BotLocaleExportSpecificationTypeDef",
    "BotLocaleFilterTypeDef",
    "BotLocaleHistoryEventTypeDef",
    "BotLocaleImportSpecificationTypeDef",
    "BotLocaleSortByTypeDef",
    "BotLocaleSummaryTypeDef",
    "BotRecommendationResultStatisticsTypeDef",
    "BotRecommendationResultsTypeDef",
    "BotRecommendationSummaryTypeDef",
    "BotSortByTypeDef",
    "BotSummaryTypeDef",
    "BotVersionLocaleDetailsTypeDef",
    "BotVersionSortByTypeDef",
    "BotVersionSummaryTypeDef",
    "BuildBotLocaleRequestRequestTypeDef",
    "BuildBotLocaleResponseTypeDef",
    "BuiltInIntentSortByTypeDef",
    "BuiltInIntentSummaryTypeDef",
    "BuiltInSlotTypeSortByTypeDef",
    "BuiltInSlotTypeSummaryTypeDef",
    "ButtonTypeDef",
    "CloudWatchLogGroupLogDestinationTypeDef",
    "CodeHookSpecificationTypeDef",
    "ConversationLogSettingsTypeDef",
    "CreateBotAliasRequestRequestTypeDef",
    "CreateBotAliasResponseTypeDef",
    "CreateBotLocaleRequestRequestTypeDef",
    "CreateBotLocaleResponseTypeDef",
    "CreateBotRequestRequestTypeDef",
    "CreateBotResponseTypeDef",
    "CreateBotVersionRequestRequestTypeDef",
    "CreateBotVersionResponseTypeDef",
    "CreateExportRequestRequestTypeDef",
    "CreateExportResponseTypeDef",
    "CreateIntentRequestRequestTypeDef",
    "CreateIntentResponseTypeDef",
    "CreateResourcePolicyRequestRequestTypeDef",
    "CreateResourcePolicyResponseTypeDef",
    "CreateResourcePolicyStatementRequestRequestTypeDef",
    "CreateResourcePolicyStatementResponseTypeDef",
    "CreateSlotRequestRequestTypeDef",
    "CreateSlotResponseTypeDef",
    "CreateSlotTypeRequestRequestTypeDef",
    "CreateSlotTypeResponseTypeDef",
    "CreateUploadUrlResponseTypeDef",
    "CustomPayloadTypeDef",
    "CustomVocabularyExportSpecificationTypeDef",
    "CustomVocabularyImportSpecificationTypeDef",
    "DataPrivacyTypeDef",
    "DateRangeFilterTypeDef",
    "DeleteBotAliasRequestRequestTypeDef",
    "DeleteBotAliasResponseTypeDef",
    "DeleteBotLocaleRequestRequestTypeDef",
    "DeleteBotLocaleResponseTypeDef",
    "DeleteBotRequestRequestTypeDef",
    "DeleteBotResponseTypeDef",
    "DeleteBotVersionRequestRequestTypeDef",
    "DeleteBotVersionResponseTypeDef",
    "DeleteCustomVocabularyRequestRequestTypeDef",
    "DeleteCustomVocabularyResponseTypeDef",
    "DeleteExportRequestRequestTypeDef",
    "DeleteExportResponseTypeDef",
    "DeleteImportRequestRequestTypeDef",
    "DeleteImportResponseTypeDef",
    "DeleteIntentRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteResourcePolicyResponseTypeDef",
    "DeleteResourcePolicyStatementRequestRequestTypeDef",
    "DeleteResourcePolicyStatementResponseTypeDef",
    "DeleteSlotRequestRequestTypeDef",
    "DeleteSlotTypeRequestRequestTypeDef",
    "DeleteUtterancesRequestRequestTypeDef",
    "DescribeBotAliasRequestRequestTypeDef",
    "DescribeBotAliasResponseTypeDef",
    "DescribeBotLocaleRequestRequestTypeDef",
    "DescribeBotLocaleResponseTypeDef",
    "DescribeBotRecommendationRequestRequestTypeDef",
    "DescribeBotRecommendationResponseTypeDef",
    "DescribeBotRequestRequestTypeDef",
    "DescribeBotResponseTypeDef",
    "DescribeBotVersionRequestRequestTypeDef",
    "DescribeBotVersionResponseTypeDef",
    "DescribeCustomVocabularyMetadataRequestRequestTypeDef",
    "DescribeCustomVocabularyMetadataResponseTypeDef",
    "DescribeExportRequestRequestTypeDef",
    "DescribeExportResponseTypeDef",
    "DescribeImportRequestRequestTypeDef",
    "DescribeImportResponseTypeDef",
    "DescribeIntentRequestRequestTypeDef",
    "DescribeIntentResponseTypeDef",
    "DescribeResourcePolicyRequestRequestTypeDef",
    "DescribeResourcePolicyResponseTypeDef",
    "DescribeSlotRequestRequestTypeDef",
    "DescribeSlotResponseTypeDef",
    "DescribeSlotTypeRequestRequestTypeDef",
    "DescribeSlotTypeResponseTypeDef",
    "DialogCodeHookSettingsTypeDef",
    "EncryptionSettingTypeDef",
    "ExportFilterTypeDef",
    "ExportResourceSpecificationTypeDef",
    "ExportSortByTypeDef",
    "ExportSummaryTypeDef",
    "ExternalSourceSettingTypeDef",
    "FulfillmentCodeHookSettingsTypeDef",
    "FulfillmentStartResponseSpecificationTypeDef",
    "FulfillmentUpdateResponseSpecificationTypeDef",
    "FulfillmentUpdatesSpecificationTypeDef",
    "GrammarSlotTypeSettingTypeDef",
    "GrammarSlotTypeSourceTypeDef",
    "ImageResponseCardTypeDef",
    "ImportFilterTypeDef",
    "ImportResourceSpecificationTypeDef",
    "ImportSortByTypeDef",
    "ImportSummaryTypeDef",
    "InputContextTypeDef",
    "IntentClosingSettingTypeDef",
    "IntentConfirmationSettingTypeDef",
    "IntentFilterTypeDef",
    "IntentSortByTypeDef",
    "IntentStatisticsTypeDef",
    "IntentSummaryTypeDef",
    "KendraConfigurationTypeDef",
    "LambdaCodeHookTypeDef",
    "LexTranscriptFilterTypeDef",
    "ListAggregatedUtterancesRequestRequestTypeDef",
    "ListAggregatedUtterancesResponseTypeDef",
    "ListBotAliasesRequestRequestTypeDef",
    "ListBotAliasesResponseTypeDef",
    "ListBotLocalesRequestRequestTypeDef",
    "ListBotLocalesResponseTypeDef",
    "ListBotRecommendationsRequestRequestTypeDef",
    "ListBotRecommendationsResponseTypeDef",
    "ListBotVersionsRequestRequestTypeDef",
    "ListBotVersionsResponseTypeDef",
    "ListBotsRequestRequestTypeDef",
    "ListBotsResponseTypeDef",
    "ListBuiltInIntentsRequestRequestTypeDef",
    "ListBuiltInIntentsResponseTypeDef",
    "ListBuiltInSlotTypesRequestRequestTypeDef",
    "ListBuiltInSlotTypesResponseTypeDef",
    "ListExportsRequestRequestTypeDef",
    "ListExportsResponseTypeDef",
    "ListImportsRequestRequestTypeDef",
    "ListImportsResponseTypeDef",
    "ListIntentsRequestRequestTypeDef",
    "ListIntentsResponseTypeDef",
    "ListRecommendedIntentsRequestRequestTypeDef",
    "ListRecommendedIntentsResponseTypeDef",
    "ListSlotTypesRequestRequestTypeDef",
    "ListSlotTypesResponseTypeDef",
    "ListSlotsRequestRequestTypeDef",
    "ListSlotsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MessageGroupTypeDef",
    "MessageTypeDef",
    "MultipleValuesSettingTypeDef",
    "ObfuscationSettingTypeDef",
    "OutputContextTypeDef",
    "PathFormatTypeDef",
    "PlainTextMessageTypeDef",
    "PostFulfillmentStatusSpecificationTypeDef",
    "PrincipalTypeDef",
    "PromptSpecificationTypeDef",
    "RecommendedIntentSummaryTypeDef",
    "RelativeAggregationDurationTypeDef",
    "ResponseMetadataTypeDef",
    "ResponseSpecificationTypeDef",
    "S3BucketLogDestinationTypeDef",
    "S3BucketTranscriptSourceTypeDef",
    "SSMLMessageTypeDef",
    "SampleUtteranceTypeDef",
    "SampleValueTypeDef",
    "SearchAssociatedTranscriptsRequestRequestTypeDef",
    "SearchAssociatedTranscriptsResponseTypeDef",
    "SentimentAnalysisSettingsTypeDef",
    "SlotDefaultValueSpecificationTypeDef",
    "SlotDefaultValueTypeDef",
    "SlotFilterTypeDef",
    "SlotPriorityTypeDef",
    "SlotSortByTypeDef",
    "SlotSummaryTypeDef",
    "SlotTypeFilterTypeDef",
    "SlotTypeSortByTypeDef",
    "SlotTypeStatisticsTypeDef",
    "SlotTypeSummaryTypeDef",
    "SlotTypeValueTypeDef",
    "SlotValueElicitationSettingTypeDef",
    "SlotValueRegexFilterTypeDef",
    "SlotValueSelectionSettingTypeDef",
    "StartBotRecommendationRequestRequestTypeDef",
    "StartBotRecommendationResponseTypeDef",
    "StartImportRequestRequestTypeDef",
    "StartImportResponseTypeDef",
    "StillWaitingResponseSpecificationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TextLogDestinationTypeDef",
    "TextLogSettingTypeDef",
    "TranscriptFilterTypeDef",
    "TranscriptSourceSettingTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBotAliasRequestRequestTypeDef",
    "UpdateBotAliasResponseTypeDef",
    "UpdateBotLocaleRequestRequestTypeDef",
    "UpdateBotLocaleResponseTypeDef",
    "UpdateBotRecommendationRequestRequestTypeDef",
    "UpdateBotRecommendationResponseTypeDef",
    "UpdateBotRequestRequestTypeDef",
    "UpdateBotResponseTypeDef",
    "UpdateExportRequestRequestTypeDef",
    "UpdateExportResponseTypeDef",
    "UpdateIntentRequestRequestTypeDef",
    "UpdateIntentResponseTypeDef",
    "UpdateResourcePolicyRequestRequestTypeDef",
    "UpdateResourcePolicyResponseTypeDef",
    "UpdateSlotRequestRequestTypeDef",
    "UpdateSlotResponseTypeDef",
    "UpdateSlotTypeRequestRequestTypeDef",
    "UpdateSlotTypeResponseTypeDef",
    "UtteranceAggregationDurationTypeDef",
    "VoiceSettingsTypeDef",
    "WaitAndContinueSpecificationTypeDef",
    "WaiterConfigTypeDef",
)

AdvancedRecognitionSettingTypeDef = TypedDict(
    "AdvancedRecognitionSettingTypeDef",
    {
        "audioRecognitionStrategy": NotRequired[Literal["UseSlotValuesAsCustomVocabulary"]],
    },
)

AggregatedUtterancesFilterTypeDef = TypedDict(
    "AggregatedUtterancesFilterTypeDef",
    {
        "name": Literal["Utterance"],
        "values": Sequence[str],
        "operator": AggregatedUtterancesFilterOperatorType,
    },
)

AggregatedUtterancesSortByTypeDef = TypedDict(
    "AggregatedUtterancesSortByTypeDef",
    {
        "attribute": AggregatedUtterancesSortAttributeType,
        "order": SortOrderType,
    },
)

AggregatedUtterancesSummaryTypeDef = TypedDict(
    "AggregatedUtterancesSummaryTypeDef",
    {
        "utterance": NotRequired[str],
        "hitCount": NotRequired[int],
        "missedCount": NotRequired[int],
        "utteranceFirstRecordedInAggregationDuration": NotRequired[datetime],
        "utteranceLastRecordedInAggregationDuration": NotRequired[datetime],
        "containsDataFromDeletedResources": NotRequired[bool],
    },
)

AssociatedTranscriptFilterTypeDef = TypedDict(
    "AssociatedTranscriptFilterTypeDef",
    {
        "name": AssociatedTranscriptFilterNameType,
        "values": Sequence[str],
    },
)

AssociatedTranscriptTypeDef = TypedDict(
    "AssociatedTranscriptTypeDef",
    {
        "transcript": NotRequired[str],
    },
)

AudioLogDestinationTypeDef = TypedDict(
    "AudioLogDestinationTypeDef",
    {
        "s3Bucket": "S3BucketLogDestinationTypeDef",
    },
)

AudioLogSettingTypeDef = TypedDict(
    "AudioLogSettingTypeDef",
    {
        "enabled": bool,
        "destination": "AudioLogDestinationTypeDef",
    },
)

BotAliasHistoryEventTypeDef = TypedDict(
    "BotAliasHistoryEventTypeDef",
    {
        "botVersion": NotRequired[str],
        "startDate": NotRequired[datetime],
        "endDate": NotRequired[datetime],
    },
)

BotAliasLocaleSettingsTypeDef = TypedDict(
    "BotAliasLocaleSettingsTypeDef",
    {
        "enabled": bool,
        "codeHookSpecification": NotRequired["CodeHookSpecificationTypeDef"],
    },
)

BotAliasSummaryTypeDef = TypedDict(
    "BotAliasSummaryTypeDef",
    {
        "botAliasId": NotRequired[str],
        "botAliasName": NotRequired[str],
        "description": NotRequired[str],
        "botVersion": NotRequired[str],
        "botAliasStatus": NotRequired[BotAliasStatusType],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)

BotExportSpecificationTypeDef = TypedDict(
    "BotExportSpecificationTypeDef",
    {
        "botId": str,
        "botVersion": str,
    },
)

BotFilterTypeDef = TypedDict(
    "BotFilterTypeDef",
    {
        "name": Literal["BotName"],
        "values": Sequence[str],
        "operator": BotFilterOperatorType,
    },
)

BotImportSpecificationTypeDef = TypedDict(
    "BotImportSpecificationTypeDef",
    {
        "botName": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
        "idleSessionTTLInSeconds": NotRequired[int],
        "botTags": NotRequired[Dict[str, str]],
        "testBotAliasTags": NotRequired[Dict[str, str]],
    },
)

BotLocaleExportSpecificationTypeDef = TypedDict(
    "BotLocaleExportSpecificationTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

BotLocaleFilterTypeDef = TypedDict(
    "BotLocaleFilterTypeDef",
    {
        "name": Literal["BotLocaleName"],
        "values": Sequence[str],
        "operator": BotLocaleFilterOperatorType,
    },
)

BotLocaleHistoryEventTypeDef = TypedDict(
    "BotLocaleHistoryEventTypeDef",
    {
        "event": str,
        "eventDate": datetime,
    },
)

BotLocaleImportSpecificationTypeDef = TypedDict(
    "BotLocaleImportSpecificationTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "nluIntentConfidenceThreshold": NotRequired[float],
        "voiceSettings": NotRequired["VoiceSettingsTypeDef"],
    },
)

BotLocaleSortByTypeDef = TypedDict(
    "BotLocaleSortByTypeDef",
    {
        "attribute": Literal["BotLocaleName"],
        "order": SortOrderType,
    },
)

BotLocaleSummaryTypeDef = TypedDict(
    "BotLocaleSummaryTypeDef",
    {
        "localeId": NotRequired[str],
        "localeName": NotRequired[str],
        "description": NotRequired[str],
        "botLocaleStatus": NotRequired[BotLocaleStatusType],
        "lastUpdatedDateTime": NotRequired[datetime],
        "lastBuildSubmittedDateTime": NotRequired[datetime],
    },
)

BotRecommendationResultStatisticsTypeDef = TypedDict(
    "BotRecommendationResultStatisticsTypeDef",
    {
        "intents": NotRequired["IntentStatisticsTypeDef"],
        "slotTypes": NotRequired["SlotTypeStatisticsTypeDef"],
    },
)

BotRecommendationResultsTypeDef = TypedDict(
    "BotRecommendationResultsTypeDef",
    {
        "botLocaleExportUrl": NotRequired[str],
        "associatedTranscriptsUrl": NotRequired[str],
        "statistics": NotRequired["BotRecommendationResultStatisticsTypeDef"],
    },
)

BotRecommendationSummaryTypeDef = TypedDict(
    "BotRecommendationSummaryTypeDef",
    {
        "botRecommendationStatus": BotRecommendationStatusType,
        "botRecommendationId": str,
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)

BotSortByTypeDef = TypedDict(
    "BotSortByTypeDef",
    {
        "attribute": Literal["BotName"],
        "order": SortOrderType,
    },
)

BotSummaryTypeDef = TypedDict(
    "BotSummaryTypeDef",
    {
        "botId": NotRequired[str],
        "botName": NotRequired[str],
        "description": NotRequired[str],
        "botStatus": NotRequired[BotStatusType],
        "latestBotVersion": NotRequired[str],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)

BotVersionLocaleDetailsTypeDef = TypedDict(
    "BotVersionLocaleDetailsTypeDef",
    {
        "sourceBotVersion": str,
    },
)

BotVersionSortByTypeDef = TypedDict(
    "BotVersionSortByTypeDef",
    {
        "attribute": Literal["BotVersion"],
        "order": SortOrderType,
    },
)

BotVersionSummaryTypeDef = TypedDict(
    "BotVersionSummaryTypeDef",
    {
        "botName": NotRequired[str],
        "botVersion": NotRequired[str],
        "description": NotRequired[str],
        "botStatus": NotRequired[BotStatusType],
        "creationDateTime": NotRequired[datetime],
    },
)

BuildBotLocaleRequestRequestTypeDef = TypedDict(
    "BuildBotLocaleRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

BuildBotLocaleResponseTypeDef = TypedDict(
    "BuildBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botLocaleStatus": BotLocaleStatusType,
        "lastBuildSubmittedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BuiltInIntentSortByTypeDef = TypedDict(
    "BuiltInIntentSortByTypeDef",
    {
        "attribute": Literal["IntentSignature"],
        "order": SortOrderType,
    },
)

BuiltInIntentSummaryTypeDef = TypedDict(
    "BuiltInIntentSummaryTypeDef",
    {
        "intentSignature": NotRequired[str],
        "description": NotRequired[str],
    },
)

BuiltInSlotTypeSortByTypeDef = TypedDict(
    "BuiltInSlotTypeSortByTypeDef",
    {
        "attribute": Literal["SlotTypeSignature"],
        "order": SortOrderType,
    },
)

BuiltInSlotTypeSummaryTypeDef = TypedDict(
    "BuiltInSlotTypeSummaryTypeDef",
    {
        "slotTypeSignature": NotRequired[str],
        "description": NotRequired[str],
    },
)

ButtonTypeDef = TypedDict(
    "ButtonTypeDef",
    {
        "text": str,
        "value": str,
    },
)

CloudWatchLogGroupLogDestinationTypeDef = TypedDict(
    "CloudWatchLogGroupLogDestinationTypeDef",
    {
        "cloudWatchLogGroupArn": str,
        "logPrefix": str,
    },
)

CodeHookSpecificationTypeDef = TypedDict(
    "CodeHookSpecificationTypeDef",
    {
        "lambdaCodeHook": "LambdaCodeHookTypeDef",
    },
)

ConversationLogSettingsTypeDef = TypedDict(
    "ConversationLogSettingsTypeDef",
    {
        "textLogSettings": NotRequired[Sequence["TextLogSettingTypeDef"]],
        "audioLogSettings": NotRequired[Sequence["AudioLogSettingTypeDef"]],
    },
)

CreateBotAliasRequestRequestTypeDef = TypedDict(
    "CreateBotAliasRequestRequestTypeDef",
    {
        "botAliasName": str,
        "botId": str,
        "description": NotRequired[str],
        "botVersion": NotRequired[str],
        "botAliasLocaleSettings": NotRequired[Mapping[str, "BotAliasLocaleSettingsTypeDef"]],
        "conversationLogSettings": NotRequired["ConversationLogSettingsTypeDef"],
        "sentimentAnalysisSettings": NotRequired["SentimentAnalysisSettingsTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateBotAliasResponseTypeDef = TypedDict(
    "CreateBotAliasResponseTypeDef",
    {
        "botAliasId": str,
        "botAliasName": str,
        "description": str,
        "botVersion": str,
        "botAliasLocaleSettings": Dict[str, "BotAliasLocaleSettingsTypeDef"],
        "conversationLogSettings": "ConversationLogSettingsTypeDef",
        "sentimentAnalysisSettings": "SentimentAnalysisSettingsTypeDef",
        "botAliasStatus": BotAliasStatusType,
        "botId": str,
        "creationDateTime": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBotLocaleRequestRequestTypeDef = TypedDict(
    "CreateBotLocaleRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "nluIntentConfidenceThreshold": float,
        "description": NotRequired[str],
        "voiceSettings": NotRequired["VoiceSettingsTypeDef"],
    },
)

CreateBotLocaleResponseTypeDef = TypedDict(
    "CreateBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeName": str,
        "localeId": str,
        "description": str,
        "nluIntentConfidenceThreshold": float,
        "voiceSettings": "VoiceSettingsTypeDef",
        "botLocaleStatus": BotLocaleStatusType,
        "creationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBotRequestRequestTypeDef = TypedDict(
    "CreateBotRequestRequestTypeDef",
    {
        "botName": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
        "idleSessionTTLInSeconds": int,
        "description": NotRequired[str],
        "botTags": NotRequired[Mapping[str, str]],
        "testBotAliasTags": NotRequired[Mapping[str, str]],
    },
)

CreateBotResponseTypeDef = TypedDict(
    "CreateBotResponseTypeDef",
    {
        "botId": str,
        "botName": str,
        "description": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
        "idleSessionTTLInSeconds": int,
        "botStatus": BotStatusType,
        "creationDateTime": datetime,
        "botTags": Dict[str, str],
        "testBotAliasTags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBotVersionRequestRequestTypeDef = TypedDict(
    "CreateBotVersionRequestRequestTypeDef",
    {
        "botId": str,
        "botVersionLocaleSpecification": Mapping[str, "BotVersionLocaleDetailsTypeDef"],
        "description": NotRequired[str],
    },
)

CreateBotVersionResponseTypeDef = TypedDict(
    "CreateBotVersionResponseTypeDef",
    {
        "botId": str,
        "description": str,
        "botVersion": str,
        "botVersionLocaleSpecification": Dict[str, "BotVersionLocaleDetailsTypeDef"],
        "botStatus": BotStatusType,
        "creationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateExportRequestRequestTypeDef = TypedDict(
    "CreateExportRequestRequestTypeDef",
    {
        "resourceSpecification": "ExportResourceSpecificationTypeDef",
        "fileFormat": ImportExportFileFormatType,
        "filePassword": NotRequired[str],
    },
)

CreateExportResponseTypeDef = TypedDict(
    "CreateExportResponseTypeDef",
    {
        "exportId": str,
        "resourceSpecification": "ExportResourceSpecificationTypeDef",
        "fileFormat": ImportExportFileFormatType,
        "exportStatus": ExportStatusType,
        "creationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIntentRequestRequestTypeDef = TypedDict(
    "CreateIntentRequestRequestTypeDef",
    {
        "intentName": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "description": NotRequired[str],
        "parentIntentSignature": NotRequired[str],
        "sampleUtterances": NotRequired[Sequence["SampleUtteranceTypeDef"]],
        "dialogCodeHook": NotRequired["DialogCodeHookSettingsTypeDef"],
        "fulfillmentCodeHook": NotRequired["FulfillmentCodeHookSettingsTypeDef"],
        "intentConfirmationSetting": NotRequired["IntentConfirmationSettingTypeDef"],
        "intentClosingSetting": NotRequired["IntentClosingSettingTypeDef"],
        "inputContexts": NotRequired[Sequence["InputContextTypeDef"]],
        "outputContexts": NotRequired[Sequence["OutputContextTypeDef"]],
        "kendraConfiguration": NotRequired["KendraConfigurationTypeDef"],
    },
)

CreateIntentResponseTypeDef = TypedDict(
    "CreateIntentResponseTypeDef",
    {
        "intentId": str,
        "intentName": str,
        "description": str,
        "parentIntentSignature": str,
        "sampleUtterances": List["SampleUtteranceTypeDef"],
        "dialogCodeHook": "DialogCodeHookSettingsTypeDef",
        "fulfillmentCodeHook": "FulfillmentCodeHookSettingsTypeDef",
        "intentConfirmationSetting": "IntentConfirmationSettingTypeDef",
        "intentClosingSetting": "IntentClosingSettingTypeDef",
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
        "kendraConfiguration": "KendraConfigurationTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResourcePolicyRequestRequestTypeDef = TypedDict(
    "CreateResourcePolicyRequestRequestTypeDef",
    {
        "resourceArn": str,
        "policy": str,
    },
)

CreateResourcePolicyResponseTypeDef = TypedDict(
    "CreateResourcePolicyResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResourcePolicyStatementRequestRequestTypeDef = TypedDict(
    "CreateResourcePolicyStatementRequestRequestTypeDef",
    {
        "resourceArn": str,
        "statementId": str,
        "effect": EffectType,
        "principal": Sequence["PrincipalTypeDef"],
        "action": Sequence[str],
        "condition": NotRequired[Mapping[str, Mapping[str, str]]],
        "expectedRevisionId": NotRequired[str],
    },
)

CreateResourcePolicyStatementResponseTypeDef = TypedDict(
    "CreateResourcePolicyStatementResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSlotRequestRequestTypeDef = TypedDict(
    "CreateSlotRequestRequestTypeDef",
    {
        "slotName": str,
        "valueElicitationSetting": "SlotValueElicitationSettingTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
        "description": NotRequired[str],
        "slotTypeId": NotRequired[str],
        "obfuscationSetting": NotRequired["ObfuscationSettingTypeDef"],
        "multipleValuesSetting": NotRequired["MultipleValuesSettingTypeDef"],
    },
)

CreateSlotResponseTypeDef = TypedDict(
    "CreateSlotResponseTypeDef",
    {
        "slotId": str,
        "slotName": str,
        "description": str,
        "slotTypeId": str,
        "valueElicitationSetting": "SlotValueElicitationSettingTypeDef",
        "obfuscationSetting": "ObfuscationSettingTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
        "creationDateTime": datetime,
        "multipleValuesSetting": "MultipleValuesSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSlotTypeRequestRequestTypeDef = TypedDict(
    "CreateSlotTypeRequestRequestTypeDef",
    {
        "slotTypeName": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "description": NotRequired[str],
        "slotTypeValues": NotRequired[Sequence["SlotTypeValueTypeDef"]],
        "valueSelectionSetting": NotRequired["SlotValueSelectionSettingTypeDef"],
        "parentSlotTypeSignature": NotRequired[str],
        "externalSourceSetting": NotRequired["ExternalSourceSettingTypeDef"],
    },
)

CreateSlotTypeResponseTypeDef = TypedDict(
    "CreateSlotTypeResponseTypeDef",
    {
        "slotTypeId": str,
        "slotTypeName": str,
        "description": str,
        "slotTypeValues": List["SlotTypeValueTypeDef"],
        "valueSelectionSetting": "SlotValueSelectionSettingTypeDef",
        "parentSlotTypeSignature": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
        "externalSourceSetting": "ExternalSourceSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUploadUrlResponseTypeDef = TypedDict(
    "CreateUploadUrlResponseTypeDef",
    {
        "importId": str,
        "uploadUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomPayloadTypeDef = TypedDict(
    "CustomPayloadTypeDef",
    {
        "value": str,
    },
)

CustomVocabularyExportSpecificationTypeDef = TypedDict(
    "CustomVocabularyExportSpecificationTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

CustomVocabularyImportSpecificationTypeDef = TypedDict(
    "CustomVocabularyImportSpecificationTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

DataPrivacyTypeDef = TypedDict(
    "DataPrivacyTypeDef",
    {
        "childDirected": bool,
    },
)

DateRangeFilterTypeDef = TypedDict(
    "DateRangeFilterTypeDef",
    {
        "startDateTime": datetime,
        "endDateTime": datetime,
    },
)

DeleteBotAliasRequestRequestTypeDef = TypedDict(
    "DeleteBotAliasRequestRequestTypeDef",
    {
        "botAliasId": str,
        "botId": str,
        "skipResourceInUseCheck": NotRequired[bool],
    },
)

DeleteBotAliasResponseTypeDef = TypedDict(
    "DeleteBotAliasResponseTypeDef",
    {
        "botAliasId": str,
        "botId": str,
        "botAliasStatus": BotAliasStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBotLocaleRequestRequestTypeDef = TypedDict(
    "DeleteBotLocaleRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

DeleteBotLocaleResponseTypeDef = TypedDict(
    "DeleteBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botLocaleStatus": BotLocaleStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBotRequestRequestTypeDef = TypedDict(
    "DeleteBotRequestRequestTypeDef",
    {
        "botId": str,
        "skipResourceInUseCheck": NotRequired[bool],
    },
)

DeleteBotResponseTypeDef = TypedDict(
    "DeleteBotResponseTypeDef",
    {
        "botId": str,
        "botStatus": BotStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBotVersionRequestRequestTypeDef = TypedDict(
    "DeleteBotVersionRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "skipResourceInUseCheck": NotRequired[bool],
    },
)

DeleteBotVersionResponseTypeDef = TypedDict(
    "DeleteBotVersionResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "botStatus": BotStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCustomVocabularyRequestRequestTypeDef = TypedDict(
    "DeleteCustomVocabularyRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

DeleteCustomVocabularyResponseTypeDef = TypedDict(
    "DeleteCustomVocabularyResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "customVocabularyStatus": CustomVocabularyStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteExportRequestRequestTypeDef = TypedDict(
    "DeleteExportRequestRequestTypeDef",
    {
        "exportId": str,
    },
)

DeleteExportResponseTypeDef = TypedDict(
    "DeleteExportResponseTypeDef",
    {
        "exportId": str,
        "exportStatus": ExportStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteImportRequestRequestTypeDef = TypedDict(
    "DeleteImportRequestRequestTypeDef",
    {
        "importId": str,
    },
)

DeleteImportResponseTypeDef = TypedDict(
    "DeleteImportResponseTypeDef",
    {
        "importId": str,
        "importStatus": ImportStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIntentRequestRequestTypeDef = TypedDict(
    "DeleteIntentRequestRequestTypeDef",
    {
        "intentId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "resourceArn": str,
        "expectedRevisionId": NotRequired[str],
    },
)

DeleteResourcePolicyResponseTypeDef = TypedDict(
    "DeleteResourcePolicyResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourcePolicyStatementRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyStatementRequestRequestTypeDef",
    {
        "resourceArn": str,
        "statementId": str,
        "expectedRevisionId": NotRequired[str],
    },
)

DeleteResourcePolicyStatementResponseTypeDef = TypedDict(
    "DeleteResourcePolicyStatementResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSlotRequestRequestTypeDef = TypedDict(
    "DeleteSlotRequestRequestTypeDef",
    {
        "slotId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
    },
)

DeleteSlotTypeRequestRequestTypeDef = TypedDict(
    "DeleteSlotTypeRequestRequestTypeDef",
    {
        "slotTypeId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "skipResourceInUseCheck": NotRequired[bool],
    },
)

DeleteUtterancesRequestRequestTypeDef = TypedDict(
    "DeleteUtterancesRequestRequestTypeDef",
    {
        "botId": str,
        "localeId": NotRequired[str],
        "sessionId": NotRequired[str],
    },
)

DescribeBotAliasRequestRequestTypeDef = TypedDict(
    "DescribeBotAliasRequestRequestTypeDef",
    {
        "botAliasId": str,
        "botId": str,
    },
)

DescribeBotAliasResponseTypeDef = TypedDict(
    "DescribeBotAliasResponseTypeDef",
    {
        "botAliasId": str,
        "botAliasName": str,
        "description": str,
        "botVersion": str,
        "botAliasLocaleSettings": Dict[str, "BotAliasLocaleSettingsTypeDef"],
        "conversationLogSettings": "ConversationLogSettingsTypeDef",
        "sentimentAnalysisSettings": "SentimentAnalysisSettingsTypeDef",
        "botAliasHistoryEvents": List["BotAliasHistoryEventTypeDef"],
        "botAliasStatus": BotAliasStatusType,
        "botId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBotLocaleRequestRequestTypeDef = TypedDict(
    "DescribeBotLocaleRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

DescribeBotLocaleResponseTypeDef = TypedDict(
    "DescribeBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "localeName": str,
        "description": str,
        "nluIntentConfidenceThreshold": float,
        "voiceSettings": "VoiceSettingsTypeDef",
        "intentsCount": int,
        "slotTypesCount": int,
        "botLocaleStatus": BotLocaleStatusType,
        "failureReasons": List[str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "lastBuildSubmittedDateTime": datetime,
        "botLocaleHistoryEvents": List["BotLocaleHistoryEventTypeDef"],
        "recommendedActions": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBotRecommendationRequestRequestTypeDef = TypedDict(
    "DescribeBotRecommendationRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationId": str,
    },
)

DescribeBotRecommendationResponseTypeDef = TypedDict(
    "DescribeBotRecommendationResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationStatus": BotRecommendationStatusType,
        "botRecommendationId": str,
        "failureReasons": List[str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "transcriptSourceSetting": "TranscriptSourceSettingTypeDef",
        "encryptionSetting": "EncryptionSettingTypeDef",
        "botRecommendationResults": "BotRecommendationResultsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBotRequestRequestTypeDef = TypedDict(
    "DescribeBotRequestRequestTypeDef",
    {
        "botId": str,
    },
)

DescribeBotResponseTypeDef = TypedDict(
    "DescribeBotResponseTypeDef",
    {
        "botId": str,
        "botName": str,
        "description": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
        "idleSessionTTLInSeconds": int,
        "botStatus": BotStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBotVersionRequestRequestTypeDef = TypedDict(
    "DescribeBotVersionRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
    },
)

DescribeBotVersionResponseTypeDef = TypedDict(
    "DescribeBotVersionResponseTypeDef",
    {
        "botId": str,
        "botName": str,
        "botVersion": str,
        "description": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
        "idleSessionTTLInSeconds": int,
        "botStatus": BotStatusType,
        "failureReasons": List[str],
        "creationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomVocabularyMetadataRequestRequestTypeDef = TypedDict(
    "DescribeCustomVocabularyMetadataRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

DescribeCustomVocabularyMetadataResponseTypeDef = TypedDict(
    "DescribeCustomVocabularyMetadataResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "customVocabularyStatus": CustomVocabularyStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportRequestRequestTypeDef = TypedDict(
    "DescribeExportRequestRequestTypeDef",
    {
        "exportId": str,
    },
)

DescribeExportResponseTypeDef = TypedDict(
    "DescribeExportResponseTypeDef",
    {
        "exportId": str,
        "resourceSpecification": "ExportResourceSpecificationTypeDef",
        "fileFormat": ImportExportFileFormatType,
        "exportStatus": ExportStatusType,
        "failureReasons": List[str],
        "downloadUrl": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImportRequestRequestTypeDef = TypedDict(
    "DescribeImportRequestRequestTypeDef",
    {
        "importId": str,
    },
)

DescribeImportResponseTypeDef = TypedDict(
    "DescribeImportResponseTypeDef",
    {
        "importId": str,
        "resourceSpecification": "ImportResourceSpecificationTypeDef",
        "importedResourceId": str,
        "importedResourceName": str,
        "mergeStrategy": MergeStrategyType,
        "importStatus": ImportStatusType,
        "failureReasons": List[str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIntentRequestRequestTypeDef = TypedDict(
    "DescribeIntentRequestRequestTypeDef",
    {
        "intentId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

DescribeIntentResponseTypeDef = TypedDict(
    "DescribeIntentResponseTypeDef",
    {
        "intentId": str,
        "intentName": str,
        "description": str,
        "parentIntentSignature": str,
        "sampleUtterances": List["SampleUtteranceTypeDef"],
        "dialogCodeHook": "DialogCodeHookSettingsTypeDef",
        "fulfillmentCodeHook": "FulfillmentCodeHookSettingsTypeDef",
        "slotPriorities": List["SlotPriorityTypeDef"],
        "intentConfirmationSetting": "IntentConfirmationSettingTypeDef",
        "intentClosingSetting": "IntentClosingSettingTypeDef",
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
        "kendraConfiguration": "KendraConfigurationTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourcePolicyRequestRequestTypeDef = TypedDict(
    "DescribeResourcePolicyRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

DescribeResourcePolicyResponseTypeDef = TypedDict(
    "DescribeResourcePolicyResponseTypeDef",
    {
        "resourceArn": str,
        "policy": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSlotRequestRequestTypeDef = TypedDict(
    "DescribeSlotRequestRequestTypeDef",
    {
        "slotId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
    },
)

DescribeSlotResponseTypeDef = TypedDict(
    "DescribeSlotResponseTypeDef",
    {
        "slotId": str,
        "slotName": str,
        "description": str,
        "slotTypeId": str,
        "valueElicitationSetting": "SlotValueElicitationSettingTypeDef",
        "obfuscationSetting": "ObfuscationSettingTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "multipleValuesSetting": "MultipleValuesSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSlotTypeRequestRequestTypeDef = TypedDict(
    "DescribeSlotTypeRequestRequestTypeDef",
    {
        "slotTypeId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

DescribeSlotTypeResponseTypeDef = TypedDict(
    "DescribeSlotTypeResponseTypeDef",
    {
        "slotTypeId": str,
        "slotTypeName": str,
        "description": str,
        "slotTypeValues": List["SlotTypeValueTypeDef"],
        "valueSelectionSetting": "SlotValueSelectionSettingTypeDef",
        "parentSlotTypeSignature": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "externalSourceSetting": "ExternalSourceSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DialogCodeHookSettingsTypeDef = TypedDict(
    "DialogCodeHookSettingsTypeDef",
    {
        "enabled": bool,
    },
)

EncryptionSettingTypeDef = TypedDict(
    "EncryptionSettingTypeDef",
    {
        "kmsKeyArn": NotRequired[str],
        "botLocaleExportPassword": NotRequired[str],
        "associatedTranscriptsPassword": NotRequired[str],
    },
)

ExportFilterTypeDef = TypedDict(
    "ExportFilterTypeDef",
    {
        "name": Literal["ExportResourceType"],
        "values": Sequence[str],
        "operator": ExportFilterOperatorType,
    },
)

ExportResourceSpecificationTypeDef = TypedDict(
    "ExportResourceSpecificationTypeDef",
    {
        "botExportSpecification": NotRequired["BotExportSpecificationTypeDef"],
        "botLocaleExportSpecification": NotRequired["BotLocaleExportSpecificationTypeDef"],
        "customVocabularyExportSpecification": NotRequired[
            "CustomVocabularyExportSpecificationTypeDef"
        ],
    },
)

ExportSortByTypeDef = TypedDict(
    "ExportSortByTypeDef",
    {
        "attribute": Literal["LastUpdatedDateTime"],
        "order": SortOrderType,
    },
)

ExportSummaryTypeDef = TypedDict(
    "ExportSummaryTypeDef",
    {
        "exportId": NotRequired[str],
        "resourceSpecification": NotRequired["ExportResourceSpecificationTypeDef"],
        "fileFormat": NotRequired[ImportExportFileFormatType],
        "exportStatus": NotRequired[ExportStatusType],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)

ExternalSourceSettingTypeDef = TypedDict(
    "ExternalSourceSettingTypeDef",
    {
        "grammarSlotTypeSetting": NotRequired["GrammarSlotTypeSettingTypeDef"],
    },
)

FulfillmentCodeHookSettingsTypeDef = TypedDict(
    "FulfillmentCodeHookSettingsTypeDef",
    {
        "enabled": bool,
        "postFulfillmentStatusSpecification": NotRequired[
            "PostFulfillmentStatusSpecificationTypeDef"
        ],
        "fulfillmentUpdatesSpecification": NotRequired["FulfillmentUpdatesSpecificationTypeDef"],
    },
)

FulfillmentStartResponseSpecificationTypeDef = TypedDict(
    "FulfillmentStartResponseSpecificationTypeDef",
    {
        "delayInSeconds": int,
        "messageGroups": Sequence["MessageGroupTypeDef"],
        "allowInterrupt": NotRequired[bool],
    },
)

FulfillmentUpdateResponseSpecificationTypeDef = TypedDict(
    "FulfillmentUpdateResponseSpecificationTypeDef",
    {
        "frequencyInSeconds": int,
        "messageGroups": Sequence["MessageGroupTypeDef"],
        "allowInterrupt": NotRequired[bool],
    },
)

FulfillmentUpdatesSpecificationTypeDef = TypedDict(
    "FulfillmentUpdatesSpecificationTypeDef",
    {
        "active": bool,
        "startResponse": NotRequired["FulfillmentStartResponseSpecificationTypeDef"],
        "updateResponse": NotRequired["FulfillmentUpdateResponseSpecificationTypeDef"],
        "timeoutInSeconds": NotRequired[int],
    },
)

GrammarSlotTypeSettingTypeDef = TypedDict(
    "GrammarSlotTypeSettingTypeDef",
    {
        "source": NotRequired["GrammarSlotTypeSourceTypeDef"],
    },
)

GrammarSlotTypeSourceTypeDef = TypedDict(
    "GrammarSlotTypeSourceTypeDef",
    {
        "s3BucketName": str,
        "s3ObjectKey": str,
        "kmsKeyArn": NotRequired[str],
    },
)

ImageResponseCardTypeDef = TypedDict(
    "ImageResponseCardTypeDef",
    {
        "title": str,
        "subtitle": NotRequired[str],
        "imageUrl": NotRequired[str],
        "buttons": NotRequired[Sequence["ButtonTypeDef"]],
    },
)

ImportFilterTypeDef = TypedDict(
    "ImportFilterTypeDef",
    {
        "name": Literal["ImportResourceType"],
        "values": Sequence[str],
        "operator": ImportFilterOperatorType,
    },
)

ImportResourceSpecificationTypeDef = TypedDict(
    "ImportResourceSpecificationTypeDef",
    {
        "botImportSpecification": NotRequired["BotImportSpecificationTypeDef"],
        "botLocaleImportSpecification": NotRequired["BotLocaleImportSpecificationTypeDef"],
        "customVocabularyImportSpecification": NotRequired[
            "CustomVocabularyImportSpecificationTypeDef"
        ],
    },
)

ImportSortByTypeDef = TypedDict(
    "ImportSortByTypeDef",
    {
        "attribute": Literal["LastUpdatedDateTime"],
        "order": SortOrderType,
    },
)

ImportSummaryTypeDef = TypedDict(
    "ImportSummaryTypeDef",
    {
        "importId": NotRequired[str],
        "importedResourceId": NotRequired[str],
        "importedResourceName": NotRequired[str],
        "importStatus": NotRequired[ImportStatusType],
        "mergeStrategy": NotRequired[MergeStrategyType],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "importedResourceType": NotRequired[ImportResourceTypeType],
    },
)

InputContextTypeDef = TypedDict(
    "InputContextTypeDef",
    {
        "name": str,
    },
)

IntentClosingSettingTypeDef = TypedDict(
    "IntentClosingSettingTypeDef",
    {
        "closingResponse": "ResponseSpecificationTypeDef",
        "active": NotRequired[bool],
    },
)

IntentConfirmationSettingTypeDef = TypedDict(
    "IntentConfirmationSettingTypeDef",
    {
        "promptSpecification": "PromptSpecificationTypeDef",
        "declinationResponse": "ResponseSpecificationTypeDef",
        "active": NotRequired[bool],
    },
)

IntentFilterTypeDef = TypedDict(
    "IntentFilterTypeDef",
    {
        "name": Literal["IntentName"],
        "values": Sequence[str],
        "operator": IntentFilterOperatorType,
    },
)

IntentSortByTypeDef = TypedDict(
    "IntentSortByTypeDef",
    {
        "attribute": IntentSortAttributeType,
        "order": SortOrderType,
    },
)

IntentStatisticsTypeDef = TypedDict(
    "IntentStatisticsTypeDef",
    {
        "discoveredIntentCount": NotRequired[int],
    },
)

IntentSummaryTypeDef = TypedDict(
    "IntentSummaryTypeDef",
    {
        "intentId": NotRequired[str],
        "intentName": NotRequired[str],
        "description": NotRequired[str],
        "parentIntentSignature": NotRequired[str],
        "inputContexts": NotRequired[List["InputContextTypeDef"]],
        "outputContexts": NotRequired[List["OutputContextTypeDef"]],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)

KendraConfigurationTypeDef = TypedDict(
    "KendraConfigurationTypeDef",
    {
        "kendraIndex": str,
        "queryFilterStringEnabled": NotRequired[bool],
        "queryFilterString": NotRequired[str],
    },
)

LambdaCodeHookTypeDef = TypedDict(
    "LambdaCodeHookTypeDef",
    {
        "lambdaARN": str,
        "codeHookInterfaceVersion": str,
    },
)

LexTranscriptFilterTypeDef = TypedDict(
    "LexTranscriptFilterTypeDef",
    {
        "dateRangeFilter": NotRequired["DateRangeFilterTypeDef"],
    },
)

ListAggregatedUtterancesRequestRequestTypeDef = TypedDict(
    "ListAggregatedUtterancesRequestRequestTypeDef",
    {
        "botId": str,
        "localeId": str,
        "aggregationDuration": "UtteranceAggregationDurationTypeDef",
        "botAliasId": NotRequired[str],
        "botVersion": NotRequired[str],
        "sortBy": NotRequired["AggregatedUtterancesSortByTypeDef"],
        "filters": NotRequired[Sequence["AggregatedUtterancesFilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListAggregatedUtterancesResponseTypeDef = TypedDict(
    "ListAggregatedUtterancesResponseTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "botVersion": str,
        "localeId": str,
        "aggregationDuration": "UtteranceAggregationDurationTypeDef",
        "aggregationWindowStartTime": datetime,
        "aggregationWindowEndTime": datetime,
        "aggregationLastRefreshedDateTime": datetime,
        "aggregatedUtterancesSummaries": List["AggregatedUtterancesSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBotAliasesRequestRequestTypeDef = TypedDict(
    "ListBotAliasesRequestRequestTypeDef",
    {
        "botId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListBotAliasesResponseTypeDef = TypedDict(
    "ListBotAliasesResponseTypeDef",
    {
        "botAliasSummaries": List["BotAliasSummaryTypeDef"],
        "nextToken": str,
        "botId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBotLocalesRequestRequestTypeDef = TypedDict(
    "ListBotLocalesRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "sortBy": NotRequired["BotLocaleSortByTypeDef"],
        "filters": NotRequired[Sequence["BotLocaleFilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListBotLocalesResponseTypeDef = TypedDict(
    "ListBotLocalesResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "nextToken": str,
        "botLocaleSummaries": List["BotLocaleSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBotRecommendationsRequestRequestTypeDef = TypedDict(
    "ListBotRecommendationsRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListBotRecommendationsResponseTypeDef = TypedDict(
    "ListBotRecommendationsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationSummaries": List["BotRecommendationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBotVersionsRequestRequestTypeDef = TypedDict(
    "ListBotVersionsRequestRequestTypeDef",
    {
        "botId": str,
        "sortBy": NotRequired["BotVersionSortByTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListBotVersionsResponseTypeDef = TypedDict(
    "ListBotVersionsResponseTypeDef",
    {
        "botId": str,
        "botVersionSummaries": List["BotVersionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBotsRequestRequestTypeDef = TypedDict(
    "ListBotsRequestRequestTypeDef",
    {
        "sortBy": NotRequired["BotSortByTypeDef"],
        "filters": NotRequired[Sequence["BotFilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListBotsResponseTypeDef = TypedDict(
    "ListBotsResponseTypeDef",
    {
        "botSummaries": List["BotSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBuiltInIntentsRequestRequestTypeDef = TypedDict(
    "ListBuiltInIntentsRequestRequestTypeDef",
    {
        "localeId": str,
        "sortBy": NotRequired["BuiltInIntentSortByTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListBuiltInIntentsResponseTypeDef = TypedDict(
    "ListBuiltInIntentsResponseTypeDef",
    {
        "builtInIntentSummaries": List["BuiltInIntentSummaryTypeDef"],
        "nextToken": str,
        "localeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBuiltInSlotTypesRequestRequestTypeDef = TypedDict(
    "ListBuiltInSlotTypesRequestRequestTypeDef",
    {
        "localeId": str,
        "sortBy": NotRequired["BuiltInSlotTypeSortByTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListBuiltInSlotTypesResponseTypeDef = TypedDict(
    "ListBuiltInSlotTypesResponseTypeDef",
    {
        "builtInSlotTypeSummaries": List["BuiltInSlotTypeSummaryTypeDef"],
        "nextToken": str,
        "localeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExportsRequestRequestTypeDef = TypedDict(
    "ListExportsRequestRequestTypeDef",
    {
        "botId": NotRequired[str],
        "botVersion": NotRequired[str],
        "sortBy": NotRequired["ExportSortByTypeDef"],
        "filters": NotRequired[Sequence["ExportFilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "localeId": NotRequired[str],
    },
)

ListExportsResponseTypeDef = TypedDict(
    "ListExportsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "exportSummaries": List["ExportSummaryTypeDef"],
        "nextToken": str,
        "localeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImportsRequestRequestTypeDef = TypedDict(
    "ListImportsRequestRequestTypeDef",
    {
        "botId": NotRequired[str],
        "botVersion": NotRequired[str],
        "sortBy": NotRequired["ImportSortByTypeDef"],
        "filters": NotRequired[Sequence["ImportFilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "localeId": NotRequired[str],
    },
)

ListImportsResponseTypeDef = TypedDict(
    "ListImportsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "importSummaries": List["ImportSummaryTypeDef"],
        "nextToken": str,
        "localeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIntentsRequestRequestTypeDef = TypedDict(
    "ListIntentsRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "sortBy": NotRequired["IntentSortByTypeDef"],
        "filters": NotRequired[Sequence["IntentFilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListIntentsResponseTypeDef = TypedDict(
    "ListIntentsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentSummaries": List["IntentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecommendedIntentsRequestRequestTypeDef = TypedDict(
    "ListRecommendedIntentsRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListRecommendedIntentsResponseTypeDef = TypedDict(
    "ListRecommendedIntentsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationId": str,
        "summaryList": List["RecommendedIntentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSlotTypesRequestRequestTypeDef = TypedDict(
    "ListSlotTypesRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "sortBy": NotRequired["SlotTypeSortByTypeDef"],
        "filters": NotRequired[Sequence["SlotTypeFilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListSlotTypesResponseTypeDef = TypedDict(
    "ListSlotTypesResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "slotTypeSummaries": List["SlotTypeSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSlotsRequestRequestTypeDef = TypedDict(
    "ListSlotsRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
        "sortBy": NotRequired["SlotSortByTypeDef"],
        "filters": NotRequired[Sequence["SlotFilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListSlotsResponseTypeDef = TypedDict(
    "ListSlotsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
        "slotSummaries": List["SlotSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MessageGroupTypeDef = TypedDict(
    "MessageGroupTypeDef",
    {
        "message": "MessageTypeDef",
        "variations": NotRequired[Sequence["MessageTypeDef"]],
    },
)

MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "plainTextMessage": NotRequired["PlainTextMessageTypeDef"],
        "customPayload": NotRequired["CustomPayloadTypeDef"],
        "ssmlMessage": NotRequired["SSMLMessageTypeDef"],
        "imageResponseCard": NotRequired["ImageResponseCardTypeDef"],
    },
)

MultipleValuesSettingTypeDef = TypedDict(
    "MultipleValuesSettingTypeDef",
    {
        "allowMultipleValues": NotRequired[bool],
    },
)

ObfuscationSettingTypeDef = TypedDict(
    "ObfuscationSettingTypeDef",
    {
        "obfuscationSettingType": ObfuscationSettingTypeType,
    },
)

OutputContextTypeDef = TypedDict(
    "OutputContextTypeDef",
    {
        "name": str,
        "timeToLiveInSeconds": int,
        "turnsToLive": int,
    },
)

PathFormatTypeDef = TypedDict(
    "PathFormatTypeDef",
    {
        "objectPrefixes": NotRequired[List[str]],
    },
)

PlainTextMessageTypeDef = TypedDict(
    "PlainTextMessageTypeDef",
    {
        "value": str,
    },
)

PostFulfillmentStatusSpecificationTypeDef = TypedDict(
    "PostFulfillmentStatusSpecificationTypeDef",
    {
        "successResponse": NotRequired["ResponseSpecificationTypeDef"],
        "failureResponse": NotRequired["ResponseSpecificationTypeDef"],
        "timeoutResponse": NotRequired["ResponseSpecificationTypeDef"],
    },
)

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "service": NotRequired[str],
        "arn": NotRequired[str],
    },
)

PromptSpecificationTypeDef = TypedDict(
    "PromptSpecificationTypeDef",
    {
        "messageGroups": Sequence["MessageGroupTypeDef"],
        "maxRetries": int,
        "allowInterrupt": NotRequired[bool],
    },
)

RecommendedIntentSummaryTypeDef = TypedDict(
    "RecommendedIntentSummaryTypeDef",
    {
        "intentId": NotRequired[str],
        "intentName": NotRequired[str],
        "sampleUtterancesCount": NotRequired[int],
    },
)

RelativeAggregationDurationTypeDef = TypedDict(
    "RelativeAggregationDurationTypeDef",
    {
        "timeDimension": TimeDimensionType,
        "timeValue": int,
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

ResponseSpecificationTypeDef = TypedDict(
    "ResponseSpecificationTypeDef",
    {
        "messageGroups": Sequence["MessageGroupTypeDef"],
        "allowInterrupt": NotRequired[bool],
    },
)

S3BucketLogDestinationTypeDef = TypedDict(
    "S3BucketLogDestinationTypeDef",
    {
        "s3BucketArn": str,
        "logPrefix": str,
        "kmsKeyArn": NotRequired[str],
    },
)

S3BucketTranscriptSourceTypeDef = TypedDict(
    "S3BucketTranscriptSourceTypeDef",
    {
        "s3BucketName": str,
        "transcriptFormat": Literal["Lex"],
        "pathFormat": NotRequired["PathFormatTypeDef"],
        "transcriptFilter": NotRequired["TranscriptFilterTypeDef"],
        "kmsKeyArn": NotRequired[str],
    },
)

SSMLMessageTypeDef = TypedDict(
    "SSMLMessageTypeDef",
    {
        "value": str,
    },
)

SampleUtteranceTypeDef = TypedDict(
    "SampleUtteranceTypeDef",
    {
        "utterance": str,
    },
)

SampleValueTypeDef = TypedDict(
    "SampleValueTypeDef",
    {
        "value": str,
    },
)

SearchAssociatedTranscriptsRequestRequestTypeDef = TypedDict(
    "SearchAssociatedTranscriptsRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationId": str,
        "filters": Sequence["AssociatedTranscriptFilterTypeDef"],
        "searchOrder": NotRequired[SearchOrderType],
        "maxResults": NotRequired[int],
        "nextIndex": NotRequired[int],
    },
)

SearchAssociatedTranscriptsResponseTypeDef = TypedDict(
    "SearchAssociatedTranscriptsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationId": str,
        "nextIndex": int,
        "associatedTranscripts": List["AssociatedTranscriptTypeDef"],
        "totalResults": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SentimentAnalysisSettingsTypeDef = TypedDict(
    "SentimentAnalysisSettingsTypeDef",
    {
        "detectSentiment": bool,
    },
)

SlotDefaultValueSpecificationTypeDef = TypedDict(
    "SlotDefaultValueSpecificationTypeDef",
    {
        "defaultValueList": Sequence["SlotDefaultValueTypeDef"],
    },
)

SlotDefaultValueTypeDef = TypedDict(
    "SlotDefaultValueTypeDef",
    {
        "defaultValue": str,
    },
)

SlotFilterTypeDef = TypedDict(
    "SlotFilterTypeDef",
    {
        "name": Literal["SlotName"],
        "values": Sequence[str],
        "operator": SlotFilterOperatorType,
    },
)

SlotPriorityTypeDef = TypedDict(
    "SlotPriorityTypeDef",
    {
        "priority": int,
        "slotId": str,
    },
)

SlotSortByTypeDef = TypedDict(
    "SlotSortByTypeDef",
    {
        "attribute": SlotSortAttributeType,
        "order": SortOrderType,
    },
)

SlotSummaryTypeDef = TypedDict(
    "SlotSummaryTypeDef",
    {
        "slotId": NotRequired[str],
        "slotName": NotRequired[str],
        "description": NotRequired[str],
        "slotConstraint": NotRequired[SlotConstraintType],
        "slotTypeId": NotRequired[str],
        "valueElicitationPromptSpecification": NotRequired["PromptSpecificationTypeDef"],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)

SlotTypeFilterTypeDef = TypedDict(
    "SlotTypeFilterTypeDef",
    {
        "name": SlotTypeFilterNameType,
        "values": Sequence[str],
        "operator": SlotTypeFilterOperatorType,
    },
)

SlotTypeSortByTypeDef = TypedDict(
    "SlotTypeSortByTypeDef",
    {
        "attribute": SlotTypeSortAttributeType,
        "order": SortOrderType,
    },
)

SlotTypeStatisticsTypeDef = TypedDict(
    "SlotTypeStatisticsTypeDef",
    {
        "discoveredSlotTypeCount": NotRequired[int],
    },
)

SlotTypeSummaryTypeDef = TypedDict(
    "SlotTypeSummaryTypeDef",
    {
        "slotTypeId": NotRequired[str],
        "slotTypeName": NotRequired[str],
        "description": NotRequired[str],
        "parentSlotTypeSignature": NotRequired[str],
        "lastUpdatedDateTime": NotRequired[datetime],
        "slotTypeCategory": NotRequired[SlotTypeCategoryType],
    },
)

SlotTypeValueTypeDef = TypedDict(
    "SlotTypeValueTypeDef",
    {
        "sampleValue": NotRequired["SampleValueTypeDef"],
        "synonyms": NotRequired[Sequence["SampleValueTypeDef"]],
    },
)

SlotValueElicitationSettingTypeDef = TypedDict(
    "SlotValueElicitationSettingTypeDef",
    {
        "slotConstraint": SlotConstraintType,
        "defaultValueSpecification": NotRequired["SlotDefaultValueSpecificationTypeDef"],
        "promptSpecification": NotRequired["PromptSpecificationTypeDef"],
        "sampleUtterances": NotRequired[Sequence["SampleUtteranceTypeDef"]],
        "waitAndContinueSpecification": NotRequired["WaitAndContinueSpecificationTypeDef"],
    },
)

SlotValueRegexFilterTypeDef = TypedDict(
    "SlotValueRegexFilterTypeDef",
    {
        "pattern": str,
    },
)

SlotValueSelectionSettingTypeDef = TypedDict(
    "SlotValueSelectionSettingTypeDef",
    {
        "resolutionStrategy": SlotValueResolutionStrategyType,
        "regexFilter": NotRequired["SlotValueRegexFilterTypeDef"],
        "advancedRecognitionSetting": NotRequired["AdvancedRecognitionSettingTypeDef"],
    },
)

StartBotRecommendationRequestRequestTypeDef = TypedDict(
    "StartBotRecommendationRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "transcriptSourceSetting": "TranscriptSourceSettingTypeDef",
        "encryptionSetting": NotRequired["EncryptionSettingTypeDef"],
    },
)

StartBotRecommendationResponseTypeDef = TypedDict(
    "StartBotRecommendationResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationStatus": BotRecommendationStatusType,
        "botRecommendationId": str,
        "creationDateTime": datetime,
        "transcriptSourceSetting": "TranscriptSourceSettingTypeDef",
        "encryptionSetting": "EncryptionSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartImportRequestRequestTypeDef = TypedDict(
    "StartImportRequestRequestTypeDef",
    {
        "importId": str,
        "resourceSpecification": "ImportResourceSpecificationTypeDef",
        "mergeStrategy": MergeStrategyType,
        "filePassword": NotRequired[str],
    },
)

StartImportResponseTypeDef = TypedDict(
    "StartImportResponseTypeDef",
    {
        "importId": str,
        "resourceSpecification": "ImportResourceSpecificationTypeDef",
        "mergeStrategy": MergeStrategyType,
        "importStatus": ImportStatusType,
        "creationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StillWaitingResponseSpecificationTypeDef = TypedDict(
    "StillWaitingResponseSpecificationTypeDef",
    {
        "messageGroups": Sequence["MessageGroupTypeDef"],
        "frequencyInSeconds": int,
        "timeoutInSeconds": int,
        "allowInterrupt": NotRequired[bool],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tags": Mapping[str, str],
    },
)

TextLogDestinationTypeDef = TypedDict(
    "TextLogDestinationTypeDef",
    {
        "cloudWatch": "CloudWatchLogGroupLogDestinationTypeDef",
    },
)

TextLogSettingTypeDef = TypedDict(
    "TextLogSettingTypeDef",
    {
        "enabled": bool,
        "destination": "TextLogDestinationTypeDef",
    },
)

TranscriptFilterTypeDef = TypedDict(
    "TranscriptFilterTypeDef",
    {
        "lexTranscriptFilter": NotRequired["LexTranscriptFilterTypeDef"],
    },
)

TranscriptSourceSettingTypeDef = TypedDict(
    "TranscriptSourceSettingTypeDef",
    {
        "s3BucketTranscriptSource": NotRequired["S3BucketTranscriptSourceTypeDef"],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tagKeys": Sequence[str],
    },
)

UpdateBotAliasRequestRequestTypeDef = TypedDict(
    "UpdateBotAliasRequestRequestTypeDef",
    {
        "botAliasId": str,
        "botAliasName": str,
        "botId": str,
        "description": NotRequired[str],
        "botVersion": NotRequired[str],
        "botAliasLocaleSettings": NotRequired[Mapping[str, "BotAliasLocaleSettingsTypeDef"]],
        "conversationLogSettings": NotRequired["ConversationLogSettingsTypeDef"],
        "sentimentAnalysisSettings": NotRequired["SentimentAnalysisSettingsTypeDef"],
    },
)

UpdateBotAliasResponseTypeDef = TypedDict(
    "UpdateBotAliasResponseTypeDef",
    {
        "botAliasId": str,
        "botAliasName": str,
        "description": str,
        "botVersion": str,
        "botAliasLocaleSettings": Dict[str, "BotAliasLocaleSettingsTypeDef"],
        "conversationLogSettings": "ConversationLogSettingsTypeDef",
        "sentimentAnalysisSettings": "SentimentAnalysisSettingsTypeDef",
        "botAliasStatus": BotAliasStatusType,
        "botId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBotLocaleRequestRequestTypeDef = TypedDict(
    "UpdateBotLocaleRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "nluIntentConfidenceThreshold": float,
        "description": NotRequired[str],
        "voiceSettings": NotRequired["VoiceSettingsTypeDef"],
    },
)

UpdateBotLocaleResponseTypeDef = TypedDict(
    "UpdateBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "localeName": str,
        "description": str,
        "nluIntentConfidenceThreshold": float,
        "voiceSettings": "VoiceSettingsTypeDef",
        "botLocaleStatus": BotLocaleStatusType,
        "failureReasons": List[str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "recommendedActions": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBotRecommendationRequestRequestTypeDef = TypedDict(
    "UpdateBotRecommendationRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationId": str,
        "encryptionSetting": "EncryptionSettingTypeDef",
    },
)

UpdateBotRecommendationResponseTypeDef = TypedDict(
    "UpdateBotRecommendationResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationStatus": BotRecommendationStatusType,
        "botRecommendationId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "transcriptSourceSetting": "TranscriptSourceSettingTypeDef",
        "encryptionSetting": "EncryptionSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBotRequestRequestTypeDef = TypedDict(
    "UpdateBotRequestRequestTypeDef",
    {
        "botId": str,
        "botName": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
        "idleSessionTTLInSeconds": int,
        "description": NotRequired[str],
    },
)

UpdateBotResponseTypeDef = TypedDict(
    "UpdateBotResponseTypeDef",
    {
        "botId": str,
        "botName": str,
        "description": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
        "idleSessionTTLInSeconds": int,
        "botStatus": BotStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateExportRequestRequestTypeDef = TypedDict(
    "UpdateExportRequestRequestTypeDef",
    {
        "exportId": str,
        "filePassword": NotRequired[str],
    },
)

UpdateExportResponseTypeDef = TypedDict(
    "UpdateExportResponseTypeDef",
    {
        "exportId": str,
        "resourceSpecification": "ExportResourceSpecificationTypeDef",
        "fileFormat": ImportExportFileFormatType,
        "exportStatus": ExportStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateIntentRequestRequestTypeDef = TypedDict(
    "UpdateIntentRequestRequestTypeDef",
    {
        "intentId": str,
        "intentName": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "description": NotRequired[str],
        "parentIntentSignature": NotRequired[str],
        "sampleUtterances": NotRequired[Sequence["SampleUtteranceTypeDef"]],
        "dialogCodeHook": NotRequired["DialogCodeHookSettingsTypeDef"],
        "fulfillmentCodeHook": NotRequired["FulfillmentCodeHookSettingsTypeDef"],
        "slotPriorities": NotRequired[Sequence["SlotPriorityTypeDef"]],
        "intentConfirmationSetting": NotRequired["IntentConfirmationSettingTypeDef"],
        "intentClosingSetting": NotRequired["IntentClosingSettingTypeDef"],
        "inputContexts": NotRequired[Sequence["InputContextTypeDef"]],
        "outputContexts": NotRequired[Sequence["OutputContextTypeDef"]],
        "kendraConfiguration": NotRequired["KendraConfigurationTypeDef"],
    },
)

UpdateIntentResponseTypeDef = TypedDict(
    "UpdateIntentResponseTypeDef",
    {
        "intentId": str,
        "intentName": str,
        "description": str,
        "parentIntentSignature": str,
        "sampleUtterances": List["SampleUtteranceTypeDef"],
        "dialogCodeHook": "DialogCodeHookSettingsTypeDef",
        "fulfillmentCodeHook": "FulfillmentCodeHookSettingsTypeDef",
        "slotPriorities": List["SlotPriorityTypeDef"],
        "intentConfirmationSetting": "IntentConfirmationSettingTypeDef",
        "intentClosingSetting": "IntentClosingSettingTypeDef",
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
        "kendraConfiguration": "KendraConfigurationTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateResourcePolicyRequestRequestTypeDef = TypedDict(
    "UpdateResourcePolicyRequestRequestTypeDef",
    {
        "resourceArn": str,
        "policy": str,
        "expectedRevisionId": NotRequired[str],
    },
)

UpdateResourcePolicyResponseTypeDef = TypedDict(
    "UpdateResourcePolicyResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSlotRequestRequestTypeDef = TypedDict(
    "UpdateSlotRequestRequestTypeDef",
    {
        "slotId": str,
        "slotName": str,
        "valueElicitationSetting": "SlotValueElicitationSettingTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
        "description": NotRequired[str],
        "slotTypeId": NotRequired[str],
        "obfuscationSetting": NotRequired["ObfuscationSettingTypeDef"],
        "multipleValuesSetting": NotRequired["MultipleValuesSettingTypeDef"],
    },
)

UpdateSlotResponseTypeDef = TypedDict(
    "UpdateSlotResponseTypeDef",
    {
        "slotId": str,
        "slotName": str,
        "description": str,
        "slotTypeId": str,
        "valueElicitationSetting": "SlotValueElicitationSettingTypeDef",
        "obfuscationSetting": "ObfuscationSettingTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "multipleValuesSetting": "MultipleValuesSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSlotTypeRequestRequestTypeDef = TypedDict(
    "UpdateSlotTypeRequestRequestTypeDef",
    {
        "slotTypeId": str,
        "slotTypeName": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "description": NotRequired[str],
        "slotTypeValues": NotRequired[Sequence["SlotTypeValueTypeDef"]],
        "valueSelectionSetting": NotRequired["SlotValueSelectionSettingTypeDef"],
        "parentSlotTypeSignature": NotRequired[str],
        "externalSourceSetting": NotRequired["ExternalSourceSettingTypeDef"],
    },
)

UpdateSlotTypeResponseTypeDef = TypedDict(
    "UpdateSlotTypeResponseTypeDef",
    {
        "slotTypeId": str,
        "slotTypeName": str,
        "description": str,
        "slotTypeValues": List["SlotTypeValueTypeDef"],
        "valueSelectionSetting": "SlotValueSelectionSettingTypeDef",
        "parentSlotTypeSignature": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "externalSourceSetting": "ExternalSourceSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UtteranceAggregationDurationTypeDef = TypedDict(
    "UtteranceAggregationDurationTypeDef",
    {
        "relativeAggregationDuration": "RelativeAggregationDurationTypeDef",
    },
)

VoiceSettingsTypeDef = TypedDict(
    "VoiceSettingsTypeDef",
    {
        "voiceId": str,
        "engine": NotRequired[VoiceEngineType],
    },
)

WaitAndContinueSpecificationTypeDef = TypedDict(
    "WaitAndContinueSpecificationTypeDef",
    {
        "waitingResponse": "ResponseSpecificationTypeDef",
        "continueResponse": "ResponseSpecificationTypeDef",
        "stillWaitingResponse": NotRequired["StillWaitingResponseSpecificationTypeDef"],
        "active": NotRequired[bool],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
