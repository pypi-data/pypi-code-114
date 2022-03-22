"""
Type annotations for lex-models service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lex_models.type_defs import BotAliasMetadataTypeDef

    data: BotAliasMetadataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    ChannelStatusType,
    ChannelTypeType,
    ContentTypeType,
    DestinationType,
    ExportStatusType,
    ExportTypeType,
    FulfillmentActivityTypeType,
    ImportStatusType,
    LocaleType,
    LogTypeType,
    MergeStrategyType,
    MigrationAlertTypeType,
    MigrationSortAttributeType,
    MigrationStatusType,
    MigrationStrategyType,
    ObfuscationSettingType,
    ProcessBehaviorType,
    ResourceTypeType,
    SlotConstraintType,
    SlotValueSelectionStrategyType,
    SortOrderType,
    StatusType,
    StatusTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BotAliasMetadataTypeDef",
    "BotChannelAssociationTypeDef",
    "BotMetadataTypeDef",
    "BuiltinIntentMetadataTypeDef",
    "BuiltinIntentSlotTypeDef",
    "BuiltinSlotTypeMetadataTypeDef",
    "CodeHookTypeDef",
    "ConversationLogsRequestTypeDef",
    "ConversationLogsResponseTypeDef",
    "CreateBotVersionRequestRequestTypeDef",
    "CreateBotVersionResponseTypeDef",
    "CreateIntentVersionRequestRequestTypeDef",
    "CreateIntentVersionResponseTypeDef",
    "CreateSlotTypeVersionRequestRequestTypeDef",
    "CreateSlotTypeVersionResponseTypeDef",
    "DeleteBotAliasRequestRequestTypeDef",
    "DeleteBotChannelAssociationRequestRequestTypeDef",
    "DeleteBotRequestRequestTypeDef",
    "DeleteBotVersionRequestRequestTypeDef",
    "DeleteIntentRequestRequestTypeDef",
    "DeleteIntentVersionRequestRequestTypeDef",
    "DeleteSlotTypeRequestRequestTypeDef",
    "DeleteSlotTypeVersionRequestRequestTypeDef",
    "DeleteUtterancesRequestRequestTypeDef",
    "EnumerationValueTypeDef",
    "FollowUpPromptTypeDef",
    "FulfillmentActivityTypeDef",
    "GetBotAliasRequestRequestTypeDef",
    "GetBotAliasResponseTypeDef",
    "GetBotAliasesRequestRequestTypeDef",
    "GetBotAliasesResponseTypeDef",
    "GetBotChannelAssociationRequestRequestTypeDef",
    "GetBotChannelAssociationResponseTypeDef",
    "GetBotChannelAssociationsRequestRequestTypeDef",
    "GetBotChannelAssociationsResponseTypeDef",
    "GetBotRequestRequestTypeDef",
    "GetBotResponseTypeDef",
    "GetBotVersionsRequestRequestTypeDef",
    "GetBotVersionsResponseTypeDef",
    "GetBotsRequestRequestTypeDef",
    "GetBotsResponseTypeDef",
    "GetBuiltinIntentRequestRequestTypeDef",
    "GetBuiltinIntentResponseTypeDef",
    "GetBuiltinIntentsRequestRequestTypeDef",
    "GetBuiltinIntentsResponseTypeDef",
    "GetBuiltinSlotTypesRequestRequestTypeDef",
    "GetBuiltinSlotTypesResponseTypeDef",
    "GetExportRequestRequestTypeDef",
    "GetExportResponseTypeDef",
    "GetImportRequestRequestTypeDef",
    "GetImportResponseTypeDef",
    "GetIntentRequestRequestTypeDef",
    "GetIntentResponseTypeDef",
    "GetIntentVersionsRequestRequestTypeDef",
    "GetIntentVersionsResponseTypeDef",
    "GetIntentsRequestRequestTypeDef",
    "GetIntentsResponseTypeDef",
    "GetMigrationRequestRequestTypeDef",
    "GetMigrationResponseTypeDef",
    "GetMigrationsRequestRequestTypeDef",
    "GetMigrationsResponseTypeDef",
    "GetSlotTypeRequestRequestTypeDef",
    "GetSlotTypeResponseTypeDef",
    "GetSlotTypeVersionsRequestRequestTypeDef",
    "GetSlotTypeVersionsResponseTypeDef",
    "GetSlotTypesRequestRequestTypeDef",
    "GetSlotTypesResponseTypeDef",
    "GetUtterancesViewRequestRequestTypeDef",
    "GetUtterancesViewResponseTypeDef",
    "InputContextTypeDef",
    "IntentMetadataTypeDef",
    "IntentTypeDef",
    "KendraConfigurationTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogSettingsRequestTypeDef",
    "LogSettingsResponseTypeDef",
    "MessageTypeDef",
    "MigrationAlertTypeDef",
    "MigrationSummaryTypeDef",
    "OutputContextTypeDef",
    "PaginatorConfigTypeDef",
    "PromptTypeDef",
    "PutBotAliasRequestRequestTypeDef",
    "PutBotAliasResponseTypeDef",
    "PutBotRequestRequestTypeDef",
    "PutBotResponseTypeDef",
    "PutIntentRequestRequestTypeDef",
    "PutIntentResponseTypeDef",
    "PutSlotTypeRequestRequestTypeDef",
    "PutSlotTypeResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SlotDefaultValueSpecTypeDef",
    "SlotDefaultValueTypeDef",
    "SlotTypeConfigurationTypeDef",
    "SlotTypeDef",
    "SlotTypeMetadataTypeDef",
    "SlotTypeRegexConfigurationTypeDef",
    "StartImportRequestRequestTypeDef",
    "StartImportResponseTypeDef",
    "StartMigrationRequestRequestTypeDef",
    "StartMigrationResponseTypeDef",
    "StatementTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UtteranceDataTypeDef",
    "UtteranceListTypeDef",
)

BotAliasMetadataTypeDef = TypedDict(
    "BotAliasMetadataTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "botVersion": NotRequired[str],
        "botName": NotRequired[str],
        "lastUpdatedDate": NotRequired[datetime],
        "createdDate": NotRequired[datetime],
        "checksum": NotRequired[str],
        "conversationLogs": NotRequired["ConversationLogsResponseTypeDef"],
    },
)

BotChannelAssociationTypeDef = TypedDict(
    "BotChannelAssociationTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "botAlias": NotRequired[str],
        "botName": NotRequired[str],
        "createdDate": NotRequired[datetime],
        "type": NotRequired[ChannelTypeType],
        "botConfiguration": NotRequired[Dict[str, str]],
        "status": NotRequired[ChannelStatusType],
        "failureReason": NotRequired[str],
    },
)

BotMetadataTypeDef = TypedDict(
    "BotMetadataTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "status": NotRequired[StatusType],
        "lastUpdatedDate": NotRequired[datetime],
        "createdDate": NotRequired[datetime],
        "version": NotRequired[str],
    },
)

BuiltinIntentMetadataTypeDef = TypedDict(
    "BuiltinIntentMetadataTypeDef",
    {
        "signature": NotRequired[str],
        "supportedLocales": NotRequired[List[LocaleType]],
    },
)

BuiltinIntentSlotTypeDef = TypedDict(
    "BuiltinIntentSlotTypeDef",
    {
        "name": NotRequired[str],
    },
)

BuiltinSlotTypeMetadataTypeDef = TypedDict(
    "BuiltinSlotTypeMetadataTypeDef",
    {
        "signature": NotRequired[str],
        "supportedLocales": NotRequired[List[LocaleType]],
    },
)

CodeHookTypeDef = TypedDict(
    "CodeHookTypeDef",
    {
        "uri": str,
        "messageVersion": str,
    },
)

ConversationLogsRequestTypeDef = TypedDict(
    "ConversationLogsRequestTypeDef",
    {
        "logSettings": Sequence["LogSettingsRequestTypeDef"],
        "iamRoleArn": str,
    },
)

ConversationLogsResponseTypeDef = TypedDict(
    "ConversationLogsResponseTypeDef",
    {
        "logSettings": NotRequired[List["LogSettingsResponseTypeDef"]],
        "iamRoleArn": NotRequired[str],
    },
)

CreateBotVersionRequestRequestTypeDef = TypedDict(
    "CreateBotVersionRequestRequestTypeDef",
    {
        "name": str,
        "checksum": NotRequired[str],
    },
)

CreateBotVersionResponseTypeDef = TypedDict(
    "CreateBotVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List["IntentTypeDef"],
        "clarificationPrompt": "PromptTypeDef",
        "abortStatement": "StatementTypeDef",
        "status": StatusType,
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": LocaleType,
        "childDirected": bool,
        "enableModelImprovements": bool,
        "detectSentiment": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIntentVersionRequestRequestTypeDef = TypedDict(
    "CreateIntentVersionRequestRequestTypeDef",
    {
        "name": str,
        "checksum": NotRequired[str],
    },
)

CreateIntentVersionResponseTypeDef = TypedDict(
    "CreateIntentVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List["SlotTypeDef"],
        "sampleUtterances": List[str],
        "confirmationPrompt": "PromptTypeDef",
        "rejectionStatement": "StatementTypeDef",
        "followUpPrompt": "FollowUpPromptTypeDef",
        "conclusionStatement": "StatementTypeDef",
        "dialogCodeHook": "CodeHookTypeDef",
        "fulfillmentActivity": "FulfillmentActivityTypeDef",
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "kendraConfiguration": "KendraConfigurationTypeDef",
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSlotTypeVersionRequestRequestTypeDef = TypedDict(
    "CreateSlotTypeVersionRequestRequestTypeDef",
    {
        "name": str,
        "checksum": NotRequired[str],
    },
)

CreateSlotTypeVersionResponseTypeDef = TypedDict(
    "CreateSlotTypeVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List["EnumerationValueTypeDef"],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": SlotValueSelectionStrategyType,
        "parentSlotTypeSignature": str,
        "slotTypeConfigurations": List["SlotTypeConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBotAliasRequestRequestTypeDef = TypedDict(
    "DeleteBotAliasRequestRequestTypeDef",
    {
        "name": str,
        "botName": str,
    },
)

DeleteBotChannelAssociationRequestRequestTypeDef = TypedDict(
    "DeleteBotChannelAssociationRequestRequestTypeDef",
    {
        "name": str,
        "botName": str,
        "botAlias": str,
    },
)

DeleteBotRequestRequestTypeDef = TypedDict(
    "DeleteBotRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteBotVersionRequestRequestTypeDef = TypedDict(
    "DeleteBotVersionRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)

DeleteIntentRequestRequestTypeDef = TypedDict(
    "DeleteIntentRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteIntentVersionRequestRequestTypeDef = TypedDict(
    "DeleteIntentVersionRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)

DeleteSlotTypeRequestRequestTypeDef = TypedDict(
    "DeleteSlotTypeRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteSlotTypeVersionRequestRequestTypeDef = TypedDict(
    "DeleteSlotTypeVersionRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)

DeleteUtterancesRequestRequestTypeDef = TypedDict(
    "DeleteUtterancesRequestRequestTypeDef",
    {
        "botName": str,
        "userId": str,
    },
)

EnumerationValueTypeDef = TypedDict(
    "EnumerationValueTypeDef",
    {
        "value": str,
        "synonyms": NotRequired[List[str]],
    },
)

FollowUpPromptTypeDef = TypedDict(
    "FollowUpPromptTypeDef",
    {
        "prompt": "PromptTypeDef",
        "rejectionStatement": "StatementTypeDef",
    },
)

FulfillmentActivityTypeDef = TypedDict(
    "FulfillmentActivityTypeDef",
    {
        "type": FulfillmentActivityTypeType,
        "codeHook": NotRequired["CodeHookTypeDef"],
    },
)

GetBotAliasRequestRequestTypeDef = TypedDict(
    "GetBotAliasRequestRequestTypeDef",
    {
        "name": str,
        "botName": str,
    },
)

GetBotAliasResponseTypeDef = TypedDict(
    "GetBotAliasResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
        "conversationLogs": "ConversationLogsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBotAliasesRequestRequestTypeDef = TypedDict(
    "GetBotAliasesRequestRequestTypeDef",
    {
        "botName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "nameContains": NotRequired[str],
    },
)

GetBotAliasesResponseTypeDef = TypedDict(
    "GetBotAliasesResponseTypeDef",
    {
        "BotAliases": List["BotAliasMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBotChannelAssociationRequestRequestTypeDef = TypedDict(
    "GetBotChannelAssociationRequestRequestTypeDef",
    {
        "name": str,
        "botName": str,
        "botAlias": str,
    },
)

GetBotChannelAssociationResponseTypeDef = TypedDict(
    "GetBotChannelAssociationResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botAlias": str,
        "botName": str,
        "createdDate": datetime,
        "type": ChannelTypeType,
        "botConfiguration": Dict[str, str],
        "status": ChannelStatusType,
        "failureReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBotChannelAssociationsRequestRequestTypeDef = TypedDict(
    "GetBotChannelAssociationsRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "nameContains": NotRequired[str],
    },
)

GetBotChannelAssociationsResponseTypeDef = TypedDict(
    "GetBotChannelAssociationsResponseTypeDef",
    {
        "botChannelAssociations": List["BotChannelAssociationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBotRequestRequestTypeDef = TypedDict(
    "GetBotRequestRequestTypeDef",
    {
        "name": str,
        "versionOrAlias": str,
    },
)

GetBotResponseTypeDef = TypedDict(
    "GetBotResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List["IntentTypeDef"],
        "enableModelImprovements": bool,
        "nluIntentConfidenceThreshold": float,
        "clarificationPrompt": "PromptTypeDef",
        "abortStatement": "StatementTypeDef",
        "status": StatusType,
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": LocaleType,
        "childDirected": bool,
        "detectSentiment": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBotVersionsRequestRequestTypeDef = TypedDict(
    "GetBotVersionsRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetBotVersionsResponseTypeDef = TypedDict(
    "GetBotVersionsResponseTypeDef",
    {
        "bots": List["BotMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBotsRequestRequestTypeDef = TypedDict(
    "GetBotsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "nameContains": NotRequired[str],
    },
)

GetBotsResponseTypeDef = TypedDict(
    "GetBotsResponseTypeDef",
    {
        "bots": List["BotMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBuiltinIntentRequestRequestTypeDef = TypedDict(
    "GetBuiltinIntentRequestRequestTypeDef",
    {
        "signature": str,
    },
)

GetBuiltinIntentResponseTypeDef = TypedDict(
    "GetBuiltinIntentResponseTypeDef",
    {
        "signature": str,
        "supportedLocales": List[LocaleType],
        "slots": List["BuiltinIntentSlotTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBuiltinIntentsRequestRequestTypeDef = TypedDict(
    "GetBuiltinIntentsRequestRequestTypeDef",
    {
        "locale": NotRequired[LocaleType],
        "signatureContains": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetBuiltinIntentsResponseTypeDef = TypedDict(
    "GetBuiltinIntentsResponseTypeDef",
    {
        "intents": List["BuiltinIntentMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBuiltinSlotTypesRequestRequestTypeDef = TypedDict(
    "GetBuiltinSlotTypesRequestRequestTypeDef",
    {
        "locale": NotRequired[LocaleType],
        "signatureContains": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetBuiltinSlotTypesResponseTypeDef = TypedDict(
    "GetBuiltinSlotTypesResponseTypeDef",
    {
        "slotTypes": List["BuiltinSlotTypeMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExportRequestRequestTypeDef = TypedDict(
    "GetExportRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
        "resourceType": ResourceTypeType,
        "exportType": ExportTypeType,
    },
)

GetExportResponseTypeDef = TypedDict(
    "GetExportResponseTypeDef",
    {
        "name": str,
        "version": str,
        "resourceType": ResourceTypeType,
        "exportType": ExportTypeType,
        "exportStatus": ExportStatusType,
        "failureReason": str,
        "url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImportRequestRequestTypeDef = TypedDict(
    "GetImportRequestRequestTypeDef",
    {
        "importId": str,
    },
)

GetImportResponseTypeDef = TypedDict(
    "GetImportResponseTypeDef",
    {
        "name": str,
        "resourceType": ResourceTypeType,
        "mergeStrategy": MergeStrategyType,
        "importId": str,
        "importStatus": ImportStatusType,
        "failureReason": List[str],
        "createdDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIntentRequestRequestTypeDef = TypedDict(
    "GetIntentRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)

GetIntentResponseTypeDef = TypedDict(
    "GetIntentResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List["SlotTypeDef"],
        "sampleUtterances": List[str],
        "confirmationPrompt": "PromptTypeDef",
        "rejectionStatement": "StatementTypeDef",
        "followUpPrompt": "FollowUpPromptTypeDef",
        "conclusionStatement": "StatementTypeDef",
        "dialogCodeHook": "CodeHookTypeDef",
        "fulfillmentActivity": "FulfillmentActivityTypeDef",
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "kendraConfiguration": "KendraConfigurationTypeDef",
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIntentVersionsRequestRequestTypeDef = TypedDict(
    "GetIntentVersionsRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetIntentVersionsResponseTypeDef = TypedDict(
    "GetIntentVersionsResponseTypeDef",
    {
        "intents": List["IntentMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIntentsRequestRequestTypeDef = TypedDict(
    "GetIntentsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "nameContains": NotRequired[str],
    },
)

GetIntentsResponseTypeDef = TypedDict(
    "GetIntentsResponseTypeDef",
    {
        "intents": List["IntentMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMigrationRequestRequestTypeDef = TypedDict(
    "GetMigrationRequestRequestTypeDef",
    {
        "migrationId": str,
    },
)

GetMigrationResponseTypeDef = TypedDict(
    "GetMigrationResponseTypeDef",
    {
        "migrationId": str,
        "v1BotName": str,
        "v1BotVersion": str,
        "v1BotLocale": LocaleType,
        "v2BotId": str,
        "v2BotRole": str,
        "migrationStatus": MigrationStatusType,
        "migrationStrategy": MigrationStrategyType,
        "migrationTimestamp": datetime,
        "alerts": List["MigrationAlertTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMigrationsRequestRequestTypeDef = TypedDict(
    "GetMigrationsRequestRequestTypeDef",
    {
        "sortByAttribute": NotRequired[MigrationSortAttributeType],
        "sortByOrder": NotRequired[SortOrderType],
        "v1BotNameContains": NotRequired[str],
        "migrationStatusEquals": NotRequired[MigrationStatusType],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

GetMigrationsResponseTypeDef = TypedDict(
    "GetMigrationsResponseTypeDef",
    {
        "migrationSummaries": List["MigrationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSlotTypeRequestRequestTypeDef = TypedDict(
    "GetSlotTypeRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)

GetSlotTypeResponseTypeDef = TypedDict(
    "GetSlotTypeResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List["EnumerationValueTypeDef"],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": SlotValueSelectionStrategyType,
        "parentSlotTypeSignature": str,
        "slotTypeConfigurations": List["SlotTypeConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSlotTypeVersionsRequestRequestTypeDef = TypedDict(
    "GetSlotTypeVersionsRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetSlotTypeVersionsResponseTypeDef = TypedDict(
    "GetSlotTypeVersionsResponseTypeDef",
    {
        "slotTypes": List["SlotTypeMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSlotTypesRequestRequestTypeDef = TypedDict(
    "GetSlotTypesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "nameContains": NotRequired[str],
    },
)

GetSlotTypesResponseTypeDef = TypedDict(
    "GetSlotTypesResponseTypeDef",
    {
        "slotTypes": List["SlotTypeMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUtterancesViewRequestRequestTypeDef = TypedDict(
    "GetUtterancesViewRequestRequestTypeDef",
    {
        "botName": str,
        "botVersions": Sequence[str],
        "statusType": StatusTypeType,
    },
)

GetUtterancesViewResponseTypeDef = TypedDict(
    "GetUtterancesViewResponseTypeDef",
    {
        "botName": str,
        "utterances": List["UtteranceListTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputContextTypeDef = TypedDict(
    "InputContextTypeDef",
    {
        "name": str,
    },
)

IntentMetadataTypeDef = TypedDict(
    "IntentMetadataTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "lastUpdatedDate": NotRequired[datetime],
        "createdDate": NotRequired[datetime],
        "version": NotRequired[str],
    },
)

IntentTypeDef = TypedDict(
    "IntentTypeDef",
    {
        "intentName": str,
        "intentVersion": str,
    },
)

KendraConfigurationTypeDef = TypedDict(
    "KendraConfigurationTypeDef",
    {
        "kendraIndex": str,
        "role": str,
        "queryFilterString": NotRequired[str],
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
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogSettingsRequestTypeDef = TypedDict(
    "LogSettingsRequestTypeDef",
    {
        "logType": LogTypeType,
        "destination": DestinationType,
        "resourceArn": str,
        "kmsKeyArn": NotRequired[str],
    },
)

LogSettingsResponseTypeDef = TypedDict(
    "LogSettingsResponseTypeDef",
    {
        "logType": NotRequired[LogTypeType],
        "destination": NotRequired[DestinationType],
        "kmsKeyArn": NotRequired[str],
        "resourceArn": NotRequired[str],
        "resourcePrefix": NotRequired[str],
    },
)

MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "contentType": ContentTypeType,
        "content": str,
        "groupNumber": NotRequired[int],
    },
)

MigrationAlertTypeDef = TypedDict(
    "MigrationAlertTypeDef",
    {
        "type": NotRequired[MigrationAlertTypeType],
        "message": NotRequired[str],
        "details": NotRequired[List[str]],
        "referenceURLs": NotRequired[List[str]],
    },
)

MigrationSummaryTypeDef = TypedDict(
    "MigrationSummaryTypeDef",
    {
        "migrationId": NotRequired[str],
        "v1BotName": NotRequired[str],
        "v1BotVersion": NotRequired[str],
        "v1BotLocale": NotRequired[LocaleType],
        "v2BotId": NotRequired[str],
        "v2BotRole": NotRequired[str],
        "migrationStatus": NotRequired[MigrationStatusType],
        "migrationStrategy": NotRequired[MigrationStrategyType],
        "migrationTimestamp": NotRequired[datetime],
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)

PromptTypeDef = TypedDict(
    "PromptTypeDef",
    {
        "messages": List["MessageTypeDef"],
        "maxAttempts": int,
        "responseCard": NotRequired[str],
    },
)

PutBotAliasRequestRequestTypeDef = TypedDict(
    "PutBotAliasRequestRequestTypeDef",
    {
        "name": str,
        "botVersion": str,
        "botName": str,
        "description": NotRequired[str],
        "checksum": NotRequired[str],
        "conversationLogs": NotRequired["ConversationLogsRequestTypeDef"],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

PutBotAliasResponseTypeDef = TypedDict(
    "PutBotAliasResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
        "conversationLogs": "ConversationLogsResponseTypeDef",
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutBotRequestRequestTypeDef = TypedDict(
    "PutBotRequestRequestTypeDef",
    {
        "name": str,
        "locale": LocaleType,
        "childDirected": bool,
        "description": NotRequired[str],
        "intents": NotRequired[Sequence["IntentTypeDef"]],
        "enableModelImprovements": NotRequired[bool],
        "nluIntentConfidenceThreshold": NotRequired[float],
        "clarificationPrompt": NotRequired["PromptTypeDef"],
        "abortStatement": NotRequired["StatementTypeDef"],
        "idleSessionTTLInSeconds": NotRequired[int],
        "voiceId": NotRequired[str],
        "checksum": NotRequired[str],
        "processBehavior": NotRequired[ProcessBehaviorType],
        "detectSentiment": NotRequired[bool],
        "createVersion": NotRequired[bool],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

PutBotResponseTypeDef = TypedDict(
    "PutBotResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List["IntentTypeDef"],
        "enableModelImprovements": bool,
        "nluIntentConfidenceThreshold": float,
        "clarificationPrompt": "PromptTypeDef",
        "abortStatement": "StatementTypeDef",
        "status": StatusType,
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": LocaleType,
        "childDirected": bool,
        "createVersion": bool,
        "detectSentiment": bool,
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutIntentRequestRequestTypeDef = TypedDict(
    "PutIntentRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "slots": NotRequired[Sequence["SlotTypeDef"]],
        "sampleUtterances": NotRequired[Sequence[str]],
        "confirmationPrompt": NotRequired["PromptTypeDef"],
        "rejectionStatement": NotRequired["StatementTypeDef"],
        "followUpPrompt": NotRequired["FollowUpPromptTypeDef"],
        "conclusionStatement": NotRequired["StatementTypeDef"],
        "dialogCodeHook": NotRequired["CodeHookTypeDef"],
        "fulfillmentActivity": NotRequired["FulfillmentActivityTypeDef"],
        "parentIntentSignature": NotRequired[str],
        "checksum": NotRequired[str],
        "createVersion": NotRequired[bool],
        "kendraConfiguration": NotRequired["KendraConfigurationTypeDef"],
        "inputContexts": NotRequired[Sequence["InputContextTypeDef"]],
        "outputContexts": NotRequired[Sequence["OutputContextTypeDef"]],
    },
)

PutIntentResponseTypeDef = TypedDict(
    "PutIntentResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List["SlotTypeDef"],
        "sampleUtterances": List[str],
        "confirmationPrompt": "PromptTypeDef",
        "rejectionStatement": "StatementTypeDef",
        "followUpPrompt": "FollowUpPromptTypeDef",
        "conclusionStatement": "StatementTypeDef",
        "dialogCodeHook": "CodeHookTypeDef",
        "fulfillmentActivity": "FulfillmentActivityTypeDef",
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "createVersion": bool,
        "kendraConfiguration": "KendraConfigurationTypeDef",
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutSlotTypeRequestRequestTypeDef = TypedDict(
    "PutSlotTypeRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "enumerationValues": NotRequired[Sequence["EnumerationValueTypeDef"]],
        "checksum": NotRequired[str],
        "valueSelectionStrategy": NotRequired[SlotValueSelectionStrategyType],
        "createVersion": NotRequired[bool],
        "parentSlotTypeSignature": NotRequired[str],
        "slotTypeConfigurations": NotRequired[Sequence["SlotTypeConfigurationTypeDef"]],
    },
)

PutSlotTypeResponseTypeDef = TypedDict(
    "PutSlotTypeResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List["EnumerationValueTypeDef"],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": SlotValueSelectionStrategyType,
        "createVersion": bool,
        "parentSlotTypeSignature": str,
        "slotTypeConfigurations": List["SlotTypeConfigurationTypeDef"],
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

SlotDefaultValueSpecTypeDef = TypedDict(
    "SlotDefaultValueSpecTypeDef",
    {
        "defaultValueList": List["SlotDefaultValueTypeDef"],
    },
)

SlotDefaultValueTypeDef = TypedDict(
    "SlotDefaultValueTypeDef",
    {
        "defaultValue": str,
    },
)

SlotTypeConfigurationTypeDef = TypedDict(
    "SlotTypeConfigurationTypeDef",
    {
        "regexConfiguration": NotRequired["SlotTypeRegexConfigurationTypeDef"],
    },
)

SlotTypeDef = TypedDict(
    "SlotTypeDef",
    {
        "name": str,
        "slotConstraint": SlotConstraintType,
        "description": NotRequired[str],
        "slotType": NotRequired[str],
        "slotTypeVersion": NotRequired[str],
        "valueElicitationPrompt": NotRequired["PromptTypeDef"],
        "priority": NotRequired[int],
        "sampleUtterances": NotRequired[List[str]],
        "responseCard": NotRequired[str],
        "obfuscationSetting": NotRequired[ObfuscationSettingType],
        "defaultValueSpec": NotRequired["SlotDefaultValueSpecTypeDef"],
    },
)

SlotTypeMetadataTypeDef = TypedDict(
    "SlotTypeMetadataTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "lastUpdatedDate": NotRequired[datetime],
        "createdDate": NotRequired[datetime],
        "version": NotRequired[str],
    },
)

SlotTypeRegexConfigurationTypeDef = TypedDict(
    "SlotTypeRegexConfigurationTypeDef",
    {
        "pattern": str,
    },
)

StartImportRequestRequestTypeDef = TypedDict(
    "StartImportRequestRequestTypeDef",
    {
        "payload": Union[bytes, IO[bytes], StreamingBody],
        "resourceType": ResourceTypeType,
        "mergeStrategy": MergeStrategyType,
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

StartImportResponseTypeDef = TypedDict(
    "StartImportResponseTypeDef",
    {
        "name": str,
        "resourceType": ResourceTypeType,
        "mergeStrategy": MergeStrategyType,
        "importId": str,
        "importStatus": ImportStatusType,
        "tags": List["TagTypeDef"],
        "createdDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartMigrationRequestRequestTypeDef = TypedDict(
    "StartMigrationRequestRequestTypeDef",
    {
        "v1BotName": str,
        "v1BotVersion": str,
        "v2BotName": str,
        "v2BotRole": str,
        "migrationStrategy": MigrationStrategyType,
    },
)

StartMigrationResponseTypeDef = TypedDict(
    "StartMigrationResponseTypeDef",
    {
        "v1BotName": str,
        "v1BotVersion": str,
        "v1BotLocale": LocaleType,
        "v2BotId": str,
        "v2BotRole": str,
        "migrationId": str,
        "migrationStrategy": MigrationStrategyType,
        "migrationTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StatementTypeDef = TypedDict(
    "StatementTypeDef",
    {
        "messages": List["MessageTypeDef"],
        "responseCard": NotRequired[str],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UtteranceDataTypeDef = TypedDict(
    "UtteranceDataTypeDef",
    {
        "utteranceString": NotRequired[str],
        "count": NotRequired[int],
        "distinctUsers": NotRequired[int],
        "firstUtteredDate": NotRequired[datetime],
        "lastUtteredDate": NotRequired[datetime],
    },
)

UtteranceListTypeDef = TypedDict(
    "UtteranceListTypeDef",
    {
        "botVersion": NotRequired[str],
        "utterances": NotRequired[List["UtteranceDataTypeDef"]],
    },
)
