"""
Type annotations for polly service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_polly/type_defs.html)

Usage::

    ```python
    from mypy_boto3_polly.type_defs import DeleteLexiconInputRequestTypeDef

    data: DeleteLexiconInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    EngineType,
    GenderType,
    LanguageCodeType,
    OutputFormatType,
    SpeechMarkTypeType,
    TaskStatusType,
    TextTypeType,
    VoiceIdType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DeleteLexiconInputRequestTypeDef",
    "DescribeVoicesInputRequestTypeDef",
    "DescribeVoicesOutputTypeDef",
    "GetLexiconInputRequestTypeDef",
    "GetLexiconOutputTypeDef",
    "GetSpeechSynthesisTaskInputRequestTypeDef",
    "GetSpeechSynthesisTaskOutputTypeDef",
    "LexiconAttributesTypeDef",
    "LexiconDescriptionTypeDef",
    "LexiconTypeDef",
    "ListLexiconsInputRequestTypeDef",
    "ListLexiconsOutputTypeDef",
    "ListSpeechSynthesisTasksInputRequestTypeDef",
    "ListSpeechSynthesisTasksOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PutLexiconInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "StartSpeechSynthesisTaskInputRequestTypeDef",
    "StartSpeechSynthesisTaskOutputTypeDef",
    "SynthesisTaskTypeDef",
    "SynthesizeSpeechInputRequestTypeDef",
    "SynthesizeSpeechOutputTypeDef",
    "VoiceTypeDef",
)

DeleteLexiconInputRequestTypeDef = TypedDict(
    "DeleteLexiconInputRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeVoicesInputRequestTypeDef = TypedDict(
    "DescribeVoicesInputRequestTypeDef",
    {
        "Engine": NotRequired[EngineType],
        "LanguageCode": NotRequired[LanguageCodeType],
        "IncludeAdditionalLanguageCodes": NotRequired[bool],
        "NextToken": NotRequired[str],
    },
)

DescribeVoicesOutputTypeDef = TypedDict(
    "DescribeVoicesOutputTypeDef",
    {
        "Voices": List["VoiceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLexiconInputRequestTypeDef = TypedDict(
    "GetLexiconInputRequestTypeDef",
    {
        "Name": str,
    },
)

GetLexiconOutputTypeDef = TypedDict(
    "GetLexiconOutputTypeDef",
    {
        "Lexicon": "LexiconTypeDef",
        "LexiconAttributes": "LexiconAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSpeechSynthesisTaskInputRequestTypeDef = TypedDict(
    "GetSpeechSynthesisTaskInputRequestTypeDef",
    {
        "TaskId": str,
    },
)

GetSpeechSynthesisTaskOutputTypeDef = TypedDict(
    "GetSpeechSynthesisTaskOutputTypeDef",
    {
        "SynthesisTask": "SynthesisTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LexiconAttributesTypeDef = TypedDict(
    "LexiconAttributesTypeDef",
    {
        "Alphabet": NotRequired[str],
        "LanguageCode": NotRequired[LanguageCodeType],
        "LastModified": NotRequired[datetime],
        "LexiconArn": NotRequired[str],
        "LexemesCount": NotRequired[int],
        "Size": NotRequired[int],
    },
)

LexiconDescriptionTypeDef = TypedDict(
    "LexiconDescriptionTypeDef",
    {
        "Name": NotRequired[str],
        "Attributes": NotRequired["LexiconAttributesTypeDef"],
    },
)

LexiconTypeDef = TypedDict(
    "LexiconTypeDef",
    {
        "Content": NotRequired[str],
        "Name": NotRequired[str],
    },
)

ListLexiconsInputRequestTypeDef = TypedDict(
    "ListLexiconsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)

ListLexiconsOutputTypeDef = TypedDict(
    "ListLexiconsOutputTypeDef",
    {
        "Lexicons": List["LexiconDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSpeechSynthesisTasksInputRequestTypeDef = TypedDict(
    "ListSpeechSynthesisTasksInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Status": NotRequired[TaskStatusType],
    },
)

ListSpeechSynthesisTasksOutputTypeDef = TypedDict(
    "ListSpeechSynthesisTasksOutputTypeDef",
    {
        "NextToken": str,
        "SynthesisTasks": List["SynthesisTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

PutLexiconInputRequestTypeDef = TypedDict(
    "PutLexiconInputRequestTypeDef",
    {
        "Name": str,
        "Content": str,
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

StartSpeechSynthesisTaskInputRequestTypeDef = TypedDict(
    "StartSpeechSynthesisTaskInputRequestTypeDef",
    {
        "OutputFormat": OutputFormatType,
        "OutputS3BucketName": str,
        "Text": str,
        "VoiceId": VoiceIdType,
        "Engine": NotRequired[EngineType],
        "LanguageCode": NotRequired[LanguageCodeType],
        "LexiconNames": NotRequired[Sequence[str]],
        "OutputS3KeyPrefix": NotRequired[str],
        "SampleRate": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "SpeechMarkTypes": NotRequired[Sequence[SpeechMarkTypeType]],
        "TextType": NotRequired[TextTypeType],
    },
)

StartSpeechSynthesisTaskOutputTypeDef = TypedDict(
    "StartSpeechSynthesisTaskOutputTypeDef",
    {
        "SynthesisTask": "SynthesisTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SynthesisTaskTypeDef = TypedDict(
    "SynthesisTaskTypeDef",
    {
        "Engine": NotRequired[EngineType],
        "TaskId": NotRequired[str],
        "TaskStatus": NotRequired[TaskStatusType],
        "TaskStatusReason": NotRequired[str],
        "OutputUri": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "RequestCharacters": NotRequired[int],
        "SnsTopicArn": NotRequired[str],
        "LexiconNames": NotRequired[List[str]],
        "OutputFormat": NotRequired[OutputFormatType],
        "SampleRate": NotRequired[str],
        "SpeechMarkTypes": NotRequired[List[SpeechMarkTypeType]],
        "TextType": NotRequired[TextTypeType],
        "VoiceId": NotRequired[VoiceIdType],
        "LanguageCode": NotRequired[LanguageCodeType],
    },
)

SynthesizeSpeechInputRequestTypeDef = TypedDict(
    "SynthesizeSpeechInputRequestTypeDef",
    {
        "OutputFormat": OutputFormatType,
        "Text": str,
        "VoiceId": VoiceIdType,
        "Engine": NotRequired[EngineType],
        "LanguageCode": NotRequired[LanguageCodeType],
        "LexiconNames": NotRequired[Sequence[str]],
        "SampleRate": NotRequired[str],
        "SpeechMarkTypes": NotRequired[Sequence[SpeechMarkTypeType]],
        "TextType": NotRequired[TextTypeType],
    },
)

SynthesizeSpeechOutputTypeDef = TypedDict(
    "SynthesizeSpeechOutputTypeDef",
    {
        "AudioStream": StreamingBody,
        "ContentType": str,
        "RequestCharacters": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VoiceTypeDef = TypedDict(
    "VoiceTypeDef",
    {
        "Gender": NotRequired[GenderType],
        "Id": NotRequired[VoiceIdType],
        "LanguageCode": NotRequired[LanguageCodeType],
        "LanguageName": NotRequired[str],
        "Name": NotRequired[str],
        "AdditionalLanguageCodes": NotRequired[List[LanguageCodeType]],
        "SupportedEngines": NotRequired[List[EngineType]],
    },
)
