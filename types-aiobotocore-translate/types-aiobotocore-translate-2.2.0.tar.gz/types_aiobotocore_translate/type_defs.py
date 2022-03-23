"""
Type annotations for translate service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_translate/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_translate.type_defs import AppliedTerminologyTypeDef

    data: AppliedTerminologyTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    DirectionalityType,
    FormalityType,
    JobStatusType,
    ParallelDataFormatType,
    ParallelDataStatusType,
    TerminologyDataFormatType,
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
    "AppliedTerminologyTypeDef",
    "CreateParallelDataRequestRequestTypeDef",
    "CreateParallelDataResponseTypeDef",
    "DeleteParallelDataRequestRequestTypeDef",
    "DeleteParallelDataResponseTypeDef",
    "DeleteTerminologyRequestRequestTypeDef",
    "DescribeTextTranslationJobRequestRequestTypeDef",
    "DescribeTextTranslationJobResponseTypeDef",
    "EncryptionKeyTypeDef",
    "GetParallelDataRequestRequestTypeDef",
    "GetParallelDataResponseTypeDef",
    "GetTerminologyRequestRequestTypeDef",
    "GetTerminologyResponseTypeDef",
    "ImportTerminologyRequestRequestTypeDef",
    "ImportTerminologyResponseTypeDef",
    "InputDataConfigTypeDef",
    "JobDetailsTypeDef",
    "ListParallelDataRequestRequestTypeDef",
    "ListParallelDataResponseTypeDef",
    "ListTerminologiesRequestRequestTypeDef",
    "ListTerminologiesResponseTypeDef",
    "ListTextTranslationJobsRequestRequestTypeDef",
    "ListTextTranslationJobsResponseTypeDef",
    "OutputDataConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ParallelDataConfigTypeDef",
    "ParallelDataDataLocationTypeDef",
    "ParallelDataPropertiesTypeDef",
    "ResponseMetadataTypeDef",
    "StartTextTranslationJobRequestRequestTypeDef",
    "StartTextTranslationJobResponseTypeDef",
    "StopTextTranslationJobRequestRequestTypeDef",
    "StopTextTranslationJobResponseTypeDef",
    "TermTypeDef",
    "TerminologyDataLocationTypeDef",
    "TerminologyDataTypeDef",
    "TerminologyPropertiesTypeDef",
    "TextTranslationJobFilterTypeDef",
    "TextTranslationJobPropertiesTypeDef",
    "TranslateTextRequestRequestTypeDef",
    "TranslateTextResponseTypeDef",
    "TranslationSettingsTypeDef",
    "UpdateParallelDataRequestRequestTypeDef",
    "UpdateParallelDataResponseTypeDef",
)

AppliedTerminologyTypeDef = TypedDict(
    "AppliedTerminologyTypeDef",
    {
        "Name": NotRequired[str],
        "Terms": NotRequired[List["TermTypeDef"]],
    },
)

CreateParallelDataRequestRequestTypeDef = TypedDict(
    "CreateParallelDataRequestRequestTypeDef",
    {
        "Name": str,
        "ParallelDataConfig": "ParallelDataConfigTypeDef",
        "ClientToken": str,
        "Description": NotRequired[str],
        "EncryptionKey": NotRequired["EncryptionKeyTypeDef"],
    },
)

CreateParallelDataResponseTypeDef = TypedDict(
    "CreateParallelDataResponseTypeDef",
    {
        "Name": str,
        "Status": ParallelDataStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteParallelDataRequestRequestTypeDef = TypedDict(
    "DeleteParallelDataRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteParallelDataResponseTypeDef = TypedDict(
    "DeleteParallelDataResponseTypeDef",
    {
        "Name": str,
        "Status": ParallelDataStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTerminologyRequestRequestTypeDef = TypedDict(
    "DeleteTerminologyRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeTextTranslationJobRequestRequestTypeDef = TypedDict(
    "DescribeTextTranslationJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeTextTranslationJobResponseTypeDef = TypedDict(
    "DescribeTextTranslationJobResponseTypeDef",
    {
        "TextTranslationJobProperties": "TextTranslationJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EncryptionKeyTypeDef = TypedDict(
    "EncryptionKeyTypeDef",
    {
        "Type": Literal["KMS"],
        "Id": str,
    },
)

GetParallelDataRequestRequestTypeDef = TypedDict(
    "GetParallelDataRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetParallelDataResponseTypeDef = TypedDict(
    "GetParallelDataResponseTypeDef",
    {
        "ParallelDataProperties": "ParallelDataPropertiesTypeDef",
        "DataLocation": "ParallelDataDataLocationTypeDef",
        "AuxiliaryDataLocation": "ParallelDataDataLocationTypeDef",
        "LatestUpdateAttemptAuxiliaryDataLocation": "ParallelDataDataLocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTerminologyRequestRequestTypeDef = TypedDict(
    "GetTerminologyRequestRequestTypeDef",
    {
        "Name": str,
        "TerminologyDataFormat": NotRequired[TerminologyDataFormatType],
    },
)

GetTerminologyResponseTypeDef = TypedDict(
    "GetTerminologyResponseTypeDef",
    {
        "TerminologyProperties": "TerminologyPropertiesTypeDef",
        "TerminologyDataLocation": "TerminologyDataLocationTypeDef",
        "AuxiliaryDataLocation": "TerminologyDataLocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportTerminologyRequestRequestTypeDef = TypedDict(
    "ImportTerminologyRequestRequestTypeDef",
    {
        "Name": str,
        "MergeStrategy": Literal["OVERWRITE"],
        "TerminologyData": "TerminologyDataTypeDef",
        "Description": NotRequired[str],
        "EncryptionKey": NotRequired["EncryptionKeyTypeDef"],
    },
)

ImportTerminologyResponseTypeDef = TypedDict(
    "ImportTerminologyResponseTypeDef",
    {
        "TerminologyProperties": "TerminologyPropertiesTypeDef",
        "AuxiliaryDataLocation": "TerminologyDataLocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputDataConfigTypeDef = TypedDict(
    "InputDataConfigTypeDef",
    {
        "S3Uri": str,
        "ContentType": str,
    },
)

JobDetailsTypeDef = TypedDict(
    "JobDetailsTypeDef",
    {
        "TranslatedDocumentsCount": NotRequired[int],
        "DocumentsWithErrorsCount": NotRequired[int],
        "InputDocumentsCount": NotRequired[int],
    },
)

ListParallelDataRequestRequestTypeDef = TypedDict(
    "ListParallelDataRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListParallelDataResponseTypeDef = TypedDict(
    "ListParallelDataResponseTypeDef",
    {
        "ParallelDataPropertiesList": List["ParallelDataPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTerminologiesRequestRequestTypeDef = TypedDict(
    "ListTerminologiesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTerminologiesResponseTypeDef = TypedDict(
    "ListTerminologiesResponseTypeDef",
    {
        "TerminologyPropertiesList": List["TerminologyPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTextTranslationJobsRequestRequestTypeDef = TypedDict(
    "ListTextTranslationJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired["TextTranslationJobFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTextTranslationJobsResponseTypeDef = TypedDict(
    "ListTextTranslationJobsResponseTypeDef",
    {
        "TextTranslationJobPropertiesList": List["TextTranslationJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OutputDataConfigTypeDef = TypedDict(
    "OutputDataConfigTypeDef",
    {
        "S3Uri": str,
        "EncryptionKey": NotRequired["EncryptionKeyTypeDef"],
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

ParallelDataConfigTypeDef = TypedDict(
    "ParallelDataConfigTypeDef",
    {
        "S3Uri": str,
        "Format": ParallelDataFormatType,
    },
)

ParallelDataDataLocationTypeDef = TypedDict(
    "ParallelDataDataLocationTypeDef",
    {
        "RepositoryType": str,
        "Location": str,
    },
)

ParallelDataPropertiesTypeDef = TypedDict(
    "ParallelDataPropertiesTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[ParallelDataStatusType],
        "SourceLanguageCode": NotRequired[str],
        "TargetLanguageCodes": NotRequired[List[str]],
        "ParallelDataConfig": NotRequired["ParallelDataConfigTypeDef"],
        "Message": NotRequired[str],
        "ImportedDataSize": NotRequired[int],
        "ImportedRecordCount": NotRequired[int],
        "FailedRecordCount": NotRequired[int],
        "SkippedRecordCount": NotRequired[int],
        "EncryptionKey": NotRequired["EncryptionKeyTypeDef"],
        "CreatedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "LatestUpdateAttemptStatus": NotRequired[ParallelDataStatusType],
        "LatestUpdateAttemptAt": NotRequired[datetime],
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

StartTextTranslationJobRequestRequestTypeDef = TypedDict(
    "StartTextTranslationJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": Sequence[str],
        "ClientToken": str,
        "JobName": NotRequired[str],
        "TerminologyNames": NotRequired[Sequence[str]],
        "ParallelDataNames": NotRequired[Sequence[str]],
        "Settings": NotRequired["TranslationSettingsTypeDef"],
    },
)

StartTextTranslationJobResponseTypeDef = TypedDict(
    "StartTextTranslationJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopTextTranslationJobRequestRequestTypeDef = TypedDict(
    "StopTextTranslationJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopTextTranslationJobResponseTypeDef = TypedDict(
    "StopTextTranslationJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TermTypeDef = TypedDict(
    "TermTypeDef",
    {
        "SourceText": NotRequired[str],
        "TargetText": NotRequired[str],
    },
)

TerminologyDataLocationTypeDef = TypedDict(
    "TerminologyDataLocationTypeDef",
    {
        "RepositoryType": str,
        "Location": str,
    },
)

TerminologyDataTypeDef = TypedDict(
    "TerminologyDataTypeDef",
    {
        "File": Union[bytes, IO[bytes], StreamingBody],
        "Format": TerminologyDataFormatType,
        "Directionality": NotRequired[DirectionalityType],
    },
)

TerminologyPropertiesTypeDef = TypedDict(
    "TerminologyPropertiesTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Arn": NotRequired[str],
        "SourceLanguageCode": NotRequired[str],
        "TargetLanguageCodes": NotRequired[List[str]],
        "EncryptionKey": NotRequired["EncryptionKeyTypeDef"],
        "SizeBytes": NotRequired[int],
        "TermCount": NotRequired[int],
        "CreatedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "Directionality": NotRequired[DirectionalityType],
        "Message": NotRequired[str],
        "SkippedTermCount": NotRequired[int],
        "Format": NotRequired[TerminologyDataFormatType],
    },
)

TextTranslationJobFilterTypeDef = TypedDict(
    "TextTranslationJobFilterTypeDef",
    {
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmittedBeforeTime": NotRequired[Union[datetime, str]],
        "SubmittedAfterTime": NotRequired[Union[datetime, str]],
    },
)

TextTranslationJobPropertiesTypeDef = TypedDict(
    "TextTranslationJobPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "JobDetails": NotRequired["JobDetailsTypeDef"],
        "SourceLanguageCode": NotRequired[str],
        "TargetLanguageCodes": NotRequired[List[str]],
        "TerminologyNames": NotRequired[List[str]],
        "ParallelDataNames": NotRequired[List[str]],
        "Message": NotRequired[str],
        "SubmittedTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired["InputDataConfigTypeDef"],
        "OutputDataConfig": NotRequired["OutputDataConfigTypeDef"],
        "DataAccessRoleArn": NotRequired[str],
        "Settings": NotRequired["TranslationSettingsTypeDef"],
    },
)

TranslateTextRequestRequestTypeDef = TypedDict(
    "TranslateTextRequestRequestTypeDef",
    {
        "Text": str,
        "SourceLanguageCode": str,
        "TargetLanguageCode": str,
        "TerminologyNames": NotRequired[Sequence[str]],
        "Settings": NotRequired["TranslationSettingsTypeDef"],
    },
)

TranslateTextResponseTypeDef = TypedDict(
    "TranslateTextResponseTypeDef",
    {
        "TranslatedText": str,
        "SourceLanguageCode": str,
        "TargetLanguageCode": str,
        "AppliedTerminologies": List["AppliedTerminologyTypeDef"],
        "AppliedSettings": "TranslationSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TranslationSettingsTypeDef = TypedDict(
    "TranslationSettingsTypeDef",
    {
        "Formality": NotRequired[FormalityType],
        "Profanity": NotRequired[Literal["MASK"]],
    },
)

UpdateParallelDataRequestRequestTypeDef = TypedDict(
    "UpdateParallelDataRequestRequestTypeDef",
    {
        "Name": str,
        "ParallelDataConfig": "ParallelDataConfigTypeDef",
        "ClientToken": str,
        "Description": NotRequired[str],
    },
)

UpdateParallelDataResponseTypeDef = TypedDict(
    "UpdateParallelDataResponseTypeDef",
    {
        "Name": str,
        "Status": ParallelDataStatusType,
        "LatestUpdateAttemptStatus": ParallelDataStatusType,
        "LatestUpdateAttemptAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
