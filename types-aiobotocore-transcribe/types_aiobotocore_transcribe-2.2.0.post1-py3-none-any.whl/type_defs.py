"""
Type annotations for transcribe service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_transcribe.type_defs import AbsoluteTimeRangeTypeDef

    data: AbsoluteTimeRangeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    BaseModelNameType,
    CallAnalyticsJobStatusType,
    CLMLanguageCodeType,
    LanguageCodeType,
    MediaFormatType,
    ModelStatusType,
    OutputLocationTypeType,
    ParticipantRoleType,
    PiiEntityTypeType,
    RedactionOutputType,
    SentimentValueType,
    SubtitleFormatType,
    TranscriptionJobStatusType,
    TypeType,
    VocabularyFilterMethodType,
    VocabularyStateType,
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
    "AbsoluteTimeRangeTypeDef",
    "CallAnalyticsJobSettingsTypeDef",
    "CallAnalyticsJobSummaryTypeDef",
    "CallAnalyticsJobTypeDef",
    "CategoryPropertiesTypeDef",
    "ChannelDefinitionTypeDef",
    "ContentRedactionTypeDef",
    "CreateCallAnalyticsCategoryRequestRequestTypeDef",
    "CreateCallAnalyticsCategoryResponseTypeDef",
    "CreateLanguageModelRequestRequestTypeDef",
    "CreateLanguageModelResponseTypeDef",
    "CreateMedicalVocabularyRequestRequestTypeDef",
    "CreateMedicalVocabularyResponseTypeDef",
    "CreateVocabularyFilterRequestRequestTypeDef",
    "CreateVocabularyFilterResponseTypeDef",
    "CreateVocabularyRequestRequestTypeDef",
    "CreateVocabularyResponseTypeDef",
    "DeleteCallAnalyticsCategoryRequestRequestTypeDef",
    "DeleteCallAnalyticsJobRequestRequestTypeDef",
    "DeleteLanguageModelRequestRequestTypeDef",
    "DeleteMedicalTranscriptionJobRequestRequestTypeDef",
    "DeleteMedicalVocabularyRequestRequestTypeDef",
    "DeleteTranscriptionJobRequestRequestTypeDef",
    "DeleteVocabularyFilterRequestRequestTypeDef",
    "DeleteVocabularyRequestRequestTypeDef",
    "DescribeLanguageModelRequestRequestTypeDef",
    "DescribeLanguageModelResponseTypeDef",
    "GetCallAnalyticsCategoryRequestRequestTypeDef",
    "GetCallAnalyticsCategoryResponseTypeDef",
    "GetCallAnalyticsJobRequestRequestTypeDef",
    "GetCallAnalyticsJobResponseTypeDef",
    "GetMedicalTranscriptionJobRequestRequestTypeDef",
    "GetMedicalTranscriptionJobResponseTypeDef",
    "GetMedicalVocabularyRequestRequestTypeDef",
    "GetMedicalVocabularyResponseTypeDef",
    "GetTranscriptionJobRequestRequestTypeDef",
    "GetTranscriptionJobResponseTypeDef",
    "GetVocabularyFilterRequestRequestTypeDef",
    "GetVocabularyFilterResponseTypeDef",
    "GetVocabularyRequestRequestTypeDef",
    "GetVocabularyResponseTypeDef",
    "InputDataConfigTypeDef",
    "InterruptionFilterTypeDef",
    "JobExecutionSettingsTypeDef",
    "LanguageIdSettingsTypeDef",
    "LanguageModelTypeDef",
    "ListCallAnalyticsCategoriesRequestRequestTypeDef",
    "ListCallAnalyticsCategoriesResponseTypeDef",
    "ListCallAnalyticsJobsRequestRequestTypeDef",
    "ListCallAnalyticsJobsResponseTypeDef",
    "ListLanguageModelsRequestRequestTypeDef",
    "ListLanguageModelsResponseTypeDef",
    "ListMedicalTranscriptionJobsRequestRequestTypeDef",
    "ListMedicalTranscriptionJobsResponseTypeDef",
    "ListMedicalVocabulariesRequestRequestTypeDef",
    "ListMedicalVocabulariesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTranscriptionJobsRequestRequestTypeDef",
    "ListTranscriptionJobsResponseTypeDef",
    "ListVocabulariesRequestRequestTypeDef",
    "ListVocabulariesResponseTypeDef",
    "ListVocabularyFiltersRequestRequestTypeDef",
    "ListVocabularyFiltersResponseTypeDef",
    "MediaTypeDef",
    "MedicalTranscriptTypeDef",
    "MedicalTranscriptionJobSummaryTypeDef",
    "MedicalTranscriptionJobTypeDef",
    "MedicalTranscriptionSettingTypeDef",
    "ModelSettingsTypeDef",
    "NonTalkTimeFilterTypeDef",
    "RelativeTimeRangeTypeDef",
    "ResponseMetadataTypeDef",
    "RuleTypeDef",
    "SentimentFilterTypeDef",
    "SettingsTypeDef",
    "StartCallAnalyticsJobRequestRequestTypeDef",
    "StartCallAnalyticsJobResponseTypeDef",
    "StartMedicalTranscriptionJobRequestRequestTypeDef",
    "StartMedicalTranscriptionJobResponseTypeDef",
    "StartTranscriptionJobRequestRequestTypeDef",
    "StartTranscriptionJobResponseTypeDef",
    "SubtitlesOutputTypeDef",
    "SubtitlesTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TranscriptFilterTypeDef",
    "TranscriptTypeDef",
    "TranscriptionJobSummaryTypeDef",
    "TranscriptionJobTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCallAnalyticsCategoryRequestRequestTypeDef",
    "UpdateCallAnalyticsCategoryResponseTypeDef",
    "UpdateMedicalVocabularyRequestRequestTypeDef",
    "UpdateMedicalVocabularyResponseTypeDef",
    "UpdateVocabularyFilterRequestRequestTypeDef",
    "UpdateVocabularyFilterResponseTypeDef",
    "UpdateVocabularyRequestRequestTypeDef",
    "UpdateVocabularyResponseTypeDef",
    "VocabularyFilterInfoTypeDef",
    "VocabularyInfoTypeDef",
)

AbsoluteTimeRangeTypeDef = TypedDict(
    "AbsoluteTimeRangeTypeDef",
    {
        "StartTime": NotRequired[int],
        "EndTime": NotRequired[int],
        "First": NotRequired[int],
        "Last": NotRequired[int],
    },
)

CallAnalyticsJobSettingsTypeDef = TypedDict(
    "CallAnalyticsJobSettingsTypeDef",
    {
        "VocabularyName": NotRequired[str],
        "VocabularyFilterName": NotRequired[str],
        "VocabularyFilterMethod": NotRequired[VocabularyFilterMethodType],
        "LanguageModelName": NotRequired[str],
        "ContentRedaction": NotRequired["ContentRedactionTypeDef"],
        "LanguageOptions": NotRequired[List[LanguageCodeType]],
        "LanguageIdSettings": NotRequired[Dict[LanguageCodeType, "LanguageIdSettingsTypeDef"]],
    },
)

CallAnalyticsJobSummaryTypeDef = TypedDict(
    "CallAnalyticsJobSummaryTypeDef",
    {
        "CallAnalyticsJobName": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "StartTime": NotRequired[datetime],
        "CompletionTime": NotRequired[datetime],
        "LanguageCode": NotRequired[LanguageCodeType],
        "CallAnalyticsJobStatus": NotRequired[CallAnalyticsJobStatusType],
        "FailureReason": NotRequired[str],
    },
)

CallAnalyticsJobTypeDef = TypedDict(
    "CallAnalyticsJobTypeDef",
    {
        "CallAnalyticsJobName": NotRequired[str],
        "CallAnalyticsJobStatus": NotRequired[CallAnalyticsJobStatusType],
        "LanguageCode": NotRequired[LanguageCodeType],
        "MediaSampleRateHertz": NotRequired[int],
        "MediaFormat": NotRequired[MediaFormatType],
        "Media": NotRequired["MediaTypeDef"],
        "Transcript": NotRequired["TranscriptTypeDef"],
        "StartTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
        "CompletionTime": NotRequired[datetime],
        "FailureReason": NotRequired[str],
        "DataAccessRoleArn": NotRequired[str],
        "IdentifiedLanguageScore": NotRequired[float],
        "Settings": NotRequired["CallAnalyticsJobSettingsTypeDef"],
        "ChannelDefinitions": NotRequired[List["ChannelDefinitionTypeDef"]],
    },
)

CategoryPropertiesTypeDef = TypedDict(
    "CategoryPropertiesTypeDef",
    {
        "CategoryName": NotRequired[str],
        "Rules": NotRequired[List["RuleTypeDef"]],
        "CreateTime": NotRequired[datetime],
        "LastUpdateTime": NotRequired[datetime],
    },
)

ChannelDefinitionTypeDef = TypedDict(
    "ChannelDefinitionTypeDef",
    {
        "ChannelId": NotRequired[int],
        "ParticipantRole": NotRequired[ParticipantRoleType],
    },
)

ContentRedactionTypeDef = TypedDict(
    "ContentRedactionTypeDef",
    {
        "RedactionType": Literal["PII"],
        "RedactionOutput": RedactionOutputType,
        "PiiEntityTypes": NotRequired[List[PiiEntityTypeType]],
    },
)

CreateCallAnalyticsCategoryRequestRequestTypeDef = TypedDict(
    "CreateCallAnalyticsCategoryRequestRequestTypeDef",
    {
        "CategoryName": str,
        "Rules": Sequence["RuleTypeDef"],
    },
)

CreateCallAnalyticsCategoryResponseTypeDef = TypedDict(
    "CreateCallAnalyticsCategoryResponseTypeDef",
    {
        "CategoryProperties": "CategoryPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLanguageModelRequestRequestTypeDef = TypedDict(
    "CreateLanguageModelRequestRequestTypeDef",
    {
        "LanguageCode": CLMLanguageCodeType,
        "BaseModelName": BaseModelNameType,
        "ModelName": str,
        "InputDataConfig": "InputDataConfigTypeDef",
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateLanguageModelResponseTypeDef = TypedDict(
    "CreateLanguageModelResponseTypeDef",
    {
        "LanguageCode": CLMLanguageCodeType,
        "BaseModelName": BaseModelNameType,
        "ModelName": str,
        "InputDataConfig": "InputDataConfigTypeDef",
        "ModelStatus": ModelStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMedicalVocabularyRequestRequestTypeDef = TypedDict(
    "CreateMedicalVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyFileUri": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateMedicalVocabularyResponseTypeDef = TypedDict(
    "CreateMedicalVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyState": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVocabularyFilterRequestRequestTypeDef = TypedDict(
    "CreateVocabularyFilterRequestRequestTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCodeType,
        "Words": NotRequired[Sequence[str]],
        "VocabularyFilterFileUri": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateVocabularyFilterResponseTypeDef = TypedDict(
    "CreateVocabularyFilterResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVocabularyRequestRequestTypeDef = TypedDict(
    "CreateVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "Phrases": NotRequired[Sequence[str]],
        "VocabularyFileUri": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateVocabularyResponseTypeDef = TypedDict(
    "CreateVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyState": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCallAnalyticsCategoryRequestRequestTypeDef = TypedDict(
    "DeleteCallAnalyticsCategoryRequestRequestTypeDef",
    {
        "CategoryName": str,
    },
)

DeleteCallAnalyticsJobRequestRequestTypeDef = TypedDict(
    "DeleteCallAnalyticsJobRequestRequestTypeDef",
    {
        "CallAnalyticsJobName": str,
    },
)

DeleteLanguageModelRequestRequestTypeDef = TypedDict(
    "DeleteLanguageModelRequestRequestTypeDef",
    {
        "ModelName": str,
    },
)

DeleteMedicalTranscriptionJobRequestRequestTypeDef = TypedDict(
    "DeleteMedicalTranscriptionJobRequestRequestTypeDef",
    {
        "MedicalTranscriptionJobName": str,
    },
)

DeleteMedicalVocabularyRequestRequestTypeDef = TypedDict(
    "DeleteMedicalVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
    },
)

DeleteTranscriptionJobRequestRequestTypeDef = TypedDict(
    "DeleteTranscriptionJobRequestRequestTypeDef",
    {
        "TranscriptionJobName": str,
    },
)

DeleteVocabularyFilterRequestRequestTypeDef = TypedDict(
    "DeleteVocabularyFilterRequestRequestTypeDef",
    {
        "VocabularyFilterName": str,
    },
)

DeleteVocabularyRequestRequestTypeDef = TypedDict(
    "DeleteVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
    },
)

DescribeLanguageModelRequestRequestTypeDef = TypedDict(
    "DescribeLanguageModelRequestRequestTypeDef",
    {
        "ModelName": str,
    },
)

DescribeLanguageModelResponseTypeDef = TypedDict(
    "DescribeLanguageModelResponseTypeDef",
    {
        "LanguageModel": "LanguageModelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCallAnalyticsCategoryRequestRequestTypeDef = TypedDict(
    "GetCallAnalyticsCategoryRequestRequestTypeDef",
    {
        "CategoryName": str,
    },
)

GetCallAnalyticsCategoryResponseTypeDef = TypedDict(
    "GetCallAnalyticsCategoryResponseTypeDef",
    {
        "CategoryProperties": "CategoryPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCallAnalyticsJobRequestRequestTypeDef = TypedDict(
    "GetCallAnalyticsJobRequestRequestTypeDef",
    {
        "CallAnalyticsJobName": str,
    },
)

GetCallAnalyticsJobResponseTypeDef = TypedDict(
    "GetCallAnalyticsJobResponseTypeDef",
    {
        "CallAnalyticsJob": "CallAnalyticsJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMedicalTranscriptionJobRequestRequestTypeDef = TypedDict(
    "GetMedicalTranscriptionJobRequestRequestTypeDef",
    {
        "MedicalTranscriptionJobName": str,
    },
)

GetMedicalTranscriptionJobResponseTypeDef = TypedDict(
    "GetMedicalTranscriptionJobResponseTypeDef",
    {
        "MedicalTranscriptionJob": "MedicalTranscriptionJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMedicalVocabularyRequestRequestTypeDef = TypedDict(
    "GetMedicalVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
    },
)

GetMedicalVocabularyResponseTypeDef = TypedDict(
    "GetMedicalVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyState": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "DownloadUri": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTranscriptionJobRequestRequestTypeDef = TypedDict(
    "GetTranscriptionJobRequestRequestTypeDef",
    {
        "TranscriptionJobName": str,
    },
)

GetTranscriptionJobResponseTypeDef = TypedDict(
    "GetTranscriptionJobResponseTypeDef",
    {
        "TranscriptionJob": "TranscriptionJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVocabularyFilterRequestRequestTypeDef = TypedDict(
    "GetVocabularyFilterRequestRequestTypeDef",
    {
        "VocabularyFilterName": str,
    },
)

GetVocabularyFilterResponseTypeDef = TypedDict(
    "GetVocabularyFilterResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "DownloadUri": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVocabularyRequestRequestTypeDef = TypedDict(
    "GetVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
    },
)

GetVocabularyResponseTypeDef = TypedDict(
    "GetVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyState": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "DownloadUri": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputDataConfigTypeDef = TypedDict(
    "InputDataConfigTypeDef",
    {
        "S3Uri": str,
        "DataAccessRoleArn": str,
        "TuningDataS3Uri": NotRequired[str],
    },
)

InterruptionFilterTypeDef = TypedDict(
    "InterruptionFilterTypeDef",
    {
        "Threshold": NotRequired[int],
        "ParticipantRole": NotRequired[ParticipantRoleType],
        "AbsoluteTimeRange": NotRequired["AbsoluteTimeRangeTypeDef"],
        "RelativeTimeRange": NotRequired["RelativeTimeRangeTypeDef"],
        "Negate": NotRequired[bool],
    },
)

JobExecutionSettingsTypeDef = TypedDict(
    "JobExecutionSettingsTypeDef",
    {
        "AllowDeferredExecution": NotRequired[bool],
        "DataAccessRoleArn": NotRequired[str],
    },
)

LanguageIdSettingsTypeDef = TypedDict(
    "LanguageIdSettingsTypeDef",
    {
        "VocabularyName": NotRequired[str],
        "VocabularyFilterName": NotRequired[str],
        "LanguageModelName": NotRequired[str],
    },
)

LanguageModelTypeDef = TypedDict(
    "LanguageModelTypeDef",
    {
        "ModelName": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "LanguageCode": NotRequired[CLMLanguageCodeType],
        "BaseModelName": NotRequired[BaseModelNameType],
        "ModelStatus": NotRequired[ModelStatusType],
        "UpgradeAvailability": NotRequired[bool],
        "FailureReason": NotRequired[str],
        "InputDataConfig": NotRequired["InputDataConfigTypeDef"],
    },
)

ListCallAnalyticsCategoriesRequestRequestTypeDef = TypedDict(
    "ListCallAnalyticsCategoriesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListCallAnalyticsCategoriesResponseTypeDef = TypedDict(
    "ListCallAnalyticsCategoriesResponseTypeDef",
    {
        "NextToken": str,
        "Categories": List["CategoryPropertiesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCallAnalyticsJobsRequestRequestTypeDef = TypedDict(
    "ListCallAnalyticsJobsRequestRequestTypeDef",
    {
        "Status": NotRequired[CallAnalyticsJobStatusType],
        "JobNameContains": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListCallAnalyticsJobsResponseTypeDef = TypedDict(
    "ListCallAnalyticsJobsResponseTypeDef",
    {
        "Status": CallAnalyticsJobStatusType,
        "NextToken": str,
        "CallAnalyticsJobSummaries": List["CallAnalyticsJobSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLanguageModelsRequestRequestTypeDef = TypedDict(
    "ListLanguageModelsRequestRequestTypeDef",
    {
        "StatusEquals": NotRequired[ModelStatusType],
        "NameContains": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListLanguageModelsResponseTypeDef = TypedDict(
    "ListLanguageModelsResponseTypeDef",
    {
        "NextToken": str,
        "Models": List["LanguageModelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMedicalTranscriptionJobsRequestRequestTypeDef = TypedDict(
    "ListMedicalTranscriptionJobsRequestRequestTypeDef",
    {
        "Status": NotRequired[TranscriptionJobStatusType],
        "JobNameContains": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListMedicalTranscriptionJobsResponseTypeDef = TypedDict(
    "ListMedicalTranscriptionJobsResponseTypeDef",
    {
        "Status": TranscriptionJobStatusType,
        "NextToken": str,
        "MedicalTranscriptionJobSummaries": List["MedicalTranscriptionJobSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMedicalVocabulariesRequestRequestTypeDef = TypedDict(
    "ListMedicalVocabulariesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "StateEquals": NotRequired[VocabularyStateType],
        "NameContains": NotRequired[str],
    },
)

ListMedicalVocabulariesResponseTypeDef = TypedDict(
    "ListMedicalVocabulariesResponseTypeDef",
    {
        "Status": VocabularyStateType,
        "NextToken": str,
        "Vocabularies": List["VocabularyInfoTypeDef"],
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
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTranscriptionJobsRequestRequestTypeDef = TypedDict(
    "ListTranscriptionJobsRequestRequestTypeDef",
    {
        "Status": NotRequired[TranscriptionJobStatusType],
        "JobNameContains": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTranscriptionJobsResponseTypeDef = TypedDict(
    "ListTranscriptionJobsResponseTypeDef",
    {
        "Status": TranscriptionJobStatusType,
        "NextToken": str,
        "TranscriptionJobSummaries": List["TranscriptionJobSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVocabulariesRequestRequestTypeDef = TypedDict(
    "ListVocabulariesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "StateEquals": NotRequired[VocabularyStateType],
        "NameContains": NotRequired[str],
    },
)

ListVocabulariesResponseTypeDef = TypedDict(
    "ListVocabulariesResponseTypeDef",
    {
        "Status": VocabularyStateType,
        "NextToken": str,
        "Vocabularies": List["VocabularyInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVocabularyFiltersRequestRequestTypeDef = TypedDict(
    "ListVocabularyFiltersRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NameContains": NotRequired[str],
    },
)

ListVocabularyFiltersResponseTypeDef = TypedDict(
    "ListVocabularyFiltersResponseTypeDef",
    {
        "NextToken": str,
        "VocabularyFilters": List["VocabularyFilterInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MediaTypeDef = TypedDict(
    "MediaTypeDef",
    {
        "MediaFileUri": NotRequired[str],
        "RedactedMediaFileUri": NotRequired[str],
    },
)

MedicalTranscriptTypeDef = TypedDict(
    "MedicalTranscriptTypeDef",
    {
        "TranscriptFileUri": NotRequired[str],
    },
)

MedicalTranscriptionJobSummaryTypeDef = TypedDict(
    "MedicalTranscriptionJobSummaryTypeDef",
    {
        "MedicalTranscriptionJobName": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "StartTime": NotRequired[datetime],
        "CompletionTime": NotRequired[datetime],
        "LanguageCode": NotRequired[LanguageCodeType],
        "TranscriptionJobStatus": NotRequired[TranscriptionJobStatusType],
        "FailureReason": NotRequired[str],
        "OutputLocationType": NotRequired[OutputLocationTypeType],
        "Specialty": NotRequired[Literal["PRIMARYCARE"]],
        "ContentIdentificationType": NotRequired[Literal["PHI"]],
        "Type": NotRequired[TypeType],
    },
)

MedicalTranscriptionJobTypeDef = TypedDict(
    "MedicalTranscriptionJobTypeDef",
    {
        "MedicalTranscriptionJobName": NotRequired[str],
        "TranscriptionJobStatus": NotRequired[TranscriptionJobStatusType],
        "LanguageCode": NotRequired[LanguageCodeType],
        "MediaSampleRateHertz": NotRequired[int],
        "MediaFormat": NotRequired[MediaFormatType],
        "Media": NotRequired["MediaTypeDef"],
        "Transcript": NotRequired["MedicalTranscriptTypeDef"],
        "StartTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
        "CompletionTime": NotRequired[datetime],
        "FailureReason": NotRequired[str],
        "Settings": NotRequired["MedicalTranscriptionSettingTypeDef"],
        "ContentIdentificationType": NotRequired[Literal["PHI"]],
        "Specialty": NotRequired[Literal["PRIMARYCARE"]],
        "Type": NotRequired[TypeType],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

MedicalTranscriptionSettingTypeDef = TypedDict(
    "MedicalTranscriptionSettingTypeDef",
    {
        "ShowSpeakerLabels": NotRequired[bool],
        "MaxSpeakerLabels": NotRequired[int],
        "ChannelIdentification": NotRequired[bool],
        "ShowAlternatives": NotRequired[bool],
        "MaxAlternatives": NotRequired[int],
        "VocabularyName": NotRequired[str],
    },
)

ModelSettingsTypeDef = TypedDict(
    "ModelSettingsTypeDef",
    {
        "LanguageModelName": NotRequired[str],
    },
)

NonTalkTimeFilterTypeDef = TypedDict(
    "NonTalkTimeFilterTypeDef",
    {
        "Threshold": NotRequired[int],
        "AbsoluteTimeRange": NotRequired["AbsoluteTimeRangeTypeDef"],
        "RelativeTimeRange": NotRequired["RelativeTimeRangeTypeDef"],
        "Negate": NotRequired[bool],
    },
)

RelativeTimeRangeTypeDef = TypedDict(
    "RelativeTimeRangeTypeDef",
    {
        "StartPercentage": NotRequired[int],
        "EndPercentage": NotRequired[int],
        "First": NotRequired[int],
        "Last": NotRequired[int],
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

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "NonTalkTimeFilter": NotRequired["NonTalkTimeFilterTypeDef"],
        "InterruptionFilter": NotRequired["InterruptionFilterTypeDef"],
        "TranscriptFilter": NotRequired["TranscriptFilterTypeDef"],
        "SentimentFilter": NotRequired["SentimentFilterTypeDef"],
    },
)

SentimentFilterTypeDef = TypedDict(
    "SentimentFilterTypeDef",
    {
        "Sentiments": Sequence[SentimentValueType],
        "AbsoluteTimeRange": NotRequired["AbsoluteTimeRangeTypeDef"],
        "RelativeTimeRange": NotRequired["RelativeTimeRangeTypeDef"],
        "ParticipantRole": NotRequired[ParticipantRoleType],
        "Negate": NotRequired[bool],
    },
)

SettingsTypeDef = TypedDict(
    "SettingsTypeDef",
    {
        "VocabularyName": NotRequired[str],
        "ShowSpeakerLabels": NotRequired[bool],
        "MaxSpeakerLabels": NotRequired[int],
        "ChannelIdentification": NotRequired[bool],
        "ShowAlternatives": NotRequired[bool],
        "MaxAlternatives": NotRequired[int],
        "VocabularyFilterName": NotRequired[str],
        "VocabularyFilterMethod": NotRequired[VocabularyFilterMethodType],
    },
)

StartCallAnalyticsJobRequestRequestTypeDef = TypedDict(
    "StartCallAnalyticsJobRequestRequestTypeDef",
    {
        "CallAnalyticsJobName": str,
        "Media": "MediaTypeDef",
        "DataAccessRoleArn": str,
        "OutputLocation": NotRequired[str],
        "OutputEncryptionKMSKeyId": NotRequired[str],
        "Settings": NotRequired["CallAnalyticsJobSettingsTypeDef"],
        "ChannelDefinitions": NotRequired[Sequence["ChannelDefinitionTypeDef"]],
    },
)

StartCallAnalyticsJobResponseTypeDef = TypedDict(
    "StartCallAnalyticsJobResponseTypeDef",
    {
        "CallAnalyticsJob": "CallAnalyticsJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartMedicalTranscriptionJobRequestRequestTypeDef = TypedDict(
    "StartMedicalTranscriptionJobRequestRequestTypeDef",
    {
        "MedicalTranscriptionJobName": str,
        "LanguageCode": LanguageCodeType,
        "Media": "MediaTypeDef",
        "OutputBucketName": str,
        "Specialty": Literal["PRIMARYCARE"],
        "Type": TypeType,
        "MediaSampleRateHertz": NotRequired[int],
        "MediaFormat": NotRequired[MediaFormatType],
        "OutputKey": NotRequired[str],
        "OutputEncryptionKMSKeyId": NotRequired[str],
        "KMSEncryptionContext": NotRequired[Mapping[str, str]],
        "Settings": NotRequired["MedicalTranscriptionSettingTypeDef"],
        "ContentIdentificationType": NotRequired[Literal["PHI"]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

StartMedicalTranscriptionJobResponseTypeDef = TypedDict(
    "StartMedicalTranscriptionJobResponseTypeDef",
    {
        "MedicalTranscriptionJob": "MedicalTranscriptionJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartTranscriptionJobRequestRequestTypeDef = TypedDict(
    "StartTranscriptionJobRequestRequestTypeDef",
    {
        "TranscriptionJobName": str,
        "Media": "MediaTypeDef",
        "LanguageCode": NotRequired[LanguageCodeType],
        "MediaSampleRateHertz": NotRequired[int],
        "MediaFormat": NotRequired[MediaFormatType],
        "OutputBucketName": NotRequired[str],
        "OutputKey": NotRequired[str],
        "OutputEncryptionKMSKeyId": NotRequired[str],
        "KMSEncryptionContext": NotRequired[Mapping[str, str]],
        "Settings": NotRequired["SettingsTypeDef"],
        "ModelSettings": NotRequired["ModelSettingsTypeDef"],
        "JobExecutionSettings": NotRequired["JobExecutionSettingsTypeDef"],
        "ContentRedaction": NotRequired["ContentRedactionTypeDef"],
        "IdentifyLanguage": NotRequired[bool],
        "LanguageOptions": NotRequired[Sequence[LanguageCodeType]],
        "Subtitles": NotRequired["SubtitlesTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "LanguageIdSettings": NotRequired[Mapping[LanguageCodeType, "LanguageIdSettingsTypeDef"]],
    },
)

StartTranscriptionJobResponseTypeDef = TypedDict(
    "StartTranscriptionJobResponseTypeDef",
    {
        "TranscriptionJob": "TranscriptionJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubtitlesOutputTypeDef = TypedDict(
    "SubtitlesOutputTypeDef",
    {
        "Formats": NotRequired[List[SubtitleFormatType]],
        "SubtitleFileUris": NotRequired[List[str]],
    },
)

SubtitlesTypeDef = TypedDict(
    "SubtitlesTypeDef",
    {
        "Formats": NotRequired[Sequence[SubtitleFormatType]],
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

TranscriptFilterTypeDef = TypedDict(
    "TranscriptFilterTypeDef",
    {
        "TranscriptFilterType": Literal["EXACT"],
        "Targets": Sequence[str],
        "AbsoluteTimeRange": NotRequired["AbsoluteTimeRangeTypeDef"],
        "RelativeTimeRange": NotRequired["RelativeTimeRangeTypeDef"],
        "ParticipantRole": NotRequired[ParticipantRoleType],
        "Negate": NotRequired[bool],
    },
)

TranscriptTypeDef = TypedDict(
    "TranscriptTypeDef",
    {
        "TranscriptFileUri": NotRequired[str],
        "RedactedTranscriptFileUri": NotRequired[str],
    },
)

TranscriptionJobSummaryTypeDef = TypedDict(
    "TranscriptionJobSummaryTypeDef",
    {
        "TranscriptionJobName": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "StartTime": NotRequired[datetime],
        "CompletionTime": NotRequired[datetime],
        "LanguageCode": NotRequired[LanguageCodeType],
        "TranscriptionJobStatus": NotRequired[TranscriptionJobStatusType],
        "FailureReason": NotRequired[str],
        "OutputLocationType": NotRequired[OutputLocationTypeType],
        "ContentRedaction": NotRequired["ContentRedactionTypeDef"],
        "ModelSettings": NotRequired["ModelSettingsTypeDef"],
        "IdentifyLanguage": NotRequired[bool],
        "IdentifiedLanguageScore": NotRequired[float],
    },
)

TranscriptionJobTypeDef = TypedDict(
    "TranscriptionJobTypeDef",
    {
        "TranscriptionJobName": NotRequired[str],
        "TranscriptionJobStatus": NotRequired[TranscriptionJobStatusType],
        "LanguageCode": NotRequired[LanguageCodeType],
        "MediaSampleRateHertz": NotRequired[int],
        "MediaFormat": NotRequired[MediaFormatType],
        "Media": NotRequired["MediaTypeDef"],
        "Transcript": NotRequired["TranscriptTypeDef"],
        "StartTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
        "CompletionTime": NotRequired[datetime],
        "FailureReason": NotRequired[str],
        "Settings": NotRequired["SettingsTypeDef"],
        "ModelSettings": NotRequired["ModelSettingsTypeDef"],
        "JobExecutionSettings": NotRequired["JobExecutionSettingsTypeDef"],
        "ContentRedaction": NotRequired["ContentRedactionTypeDef"],
        "IdentifyLanguage": NotRequired[bool],
        "LanguageOptions": NotRequired[List[LanguageCodeType]],
        "IdentifiedLanguageScore": NotRequired[float],
        "Tags": NotRequired[List["TagTypeDef"]],
        "Subtitles": NotRequired["SubtitlesOutputTypeDef"],
        "LanguageIdSettings": NotRequired[Dict[LanguageCodeType, "LanguageIdSettingsTypeDef"]],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateCallAnalyticsCategoryRequestRequestTypeDef = TypedDict(
    "UpdateCallAnalyticsCategoryRequestRequestTypeDef",
    {
        "CategoryName": str,
        "Rules": Sequence["RuleTypeDef"],
    },
)

UpdateCallAnalyticsCategoryResponseTypeDef = TypedDict(
    "UpdateCallAnalyticsCategoryResponseTypeDef",
    {
        "CategoryProperties": "CategoryPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMedicalVocabularyRequestRequestTypeDef = TypedDict(
    "UpdateMedicalVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyFileUri": NotRequired[str],
    },
)

UpdateMedicalVocabularyResponseTypeDef = TypedDict(
    "UpdateMedicalVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "VocabularyState": VocabularyStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVocabularyFilterRequestRequestTypeDef = TypedDict(
    "UpdateVocabularyFilterRequestRequestTypeDef",
    {
        "VocabularyFilterName": str,
        "Words": NotRequired[Sequence[str]],
        "VocabularyFilterFileUri": NotRequired[str],
    },
)

UpdateVocabularyFilterResponseTypeDef = TypedDict(
    "UpdateVocabularyFilterResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVocabularyRequestRequestTypeDef = TypedDict(
    "UpdateVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "Phrases": NotRequired[Sequence[str]],
        "VocabularyFileUri": NotRequired[str],
    },
)

UpdateVocabularyResponseTypeDef = TypedDict(
    "UpdateVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "VocabularyState": VocabularyStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VocabularyFilterInfoTypeDef = TypedDict(
    "VocabularyFilterInfoTypeDef",
    {
        "VocabularyFilterName": NotRequired[str],
        "LanguageCode": NotRequired[LanguageCodeType],
        "LastModifiedTime": NotRequired[datetime],
    },
)

VocabularyInfoTypeDef = TypedDict(
    "VocabularyInfoTypeDef",
    {
        "VocabularyName": NotRequired[str],
        "LanguageCode": NotRequired[LanguageCodeType],
        "LastModifiedTime": NotRequired[datetime],
        "VocabularyState": NotRequired[VocabularyStateType],
    },
)
