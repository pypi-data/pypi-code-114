"""
Type annotations for comprehend service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_comprehend.type_defs import AugmentedManifestsListItemTypeDef

    data: AugmentedManifestsListItemTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AugmentedManifestsDocumentTypeFormatType,
    DocumentClassifierDataFormatType,
    DocumentClassifierModeType,
    DocumentReadActionType,
    DocumentReadFeatureTypesType,
    DocumentReadModeType,
    EndpointStatusType,
    EntityRecognizerDataFormatType,
    EntityTypeType,
    InputFormatType,
    JobStatusType,
    LanguageCodeType,
    ModelStatusType,
    PartOfSpeechTagTypeType,
    PiiEntitiesDetectionMaskModeType,
    PiiEntitiesDetectionModeType,
    PiiEntityTypeType,
    SentimentTypeType,
    SplitType,
    SyntaxLanguageCodeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AugmentedManifestsListItemTypeDef",
    "BatchDetectDominantLanguageItemResultTypeDef",
    "BatchDetectDominantLanguageRequestRequestTypeDef",
    "BatchDetectDominantLanguageResponseTypeDef",
    "BatchDetectEntitiesItemResultTypeDef",
    "BatchDetectEntitiesRequestRequestTypeDef",
    "BatchDetectEntitiesResponseTypeDef",
    "BatchDetectKeyPhrasesItemResultTypeDef",
    "BatchDetectKeyPhrasesRequestRequestTypeDef",
    "BatchDetectKeyPhrasesResponseTypeDef",
    "BatchDetectSentimentItemResultTypeDef",
    "BatchDetectSentimentRequestRequestTypeDef",
    "BatchDetectSentimentResponseTypeDef",
    "BatchDetectSyntaxItemResultTypeDef",
    "BatchDetectSyntaxRequestRequestTypeDef",
    "BatchDetectSyntaxResponseTypeDef",
    "BatchItemErrorTypeDef",
    "ClassifierEvaluationMetricsTypeDef",
    "ClassifierMetadataTypeDef",
    "ClassifyDocumentRequestRequestTypeDef",
    "ClassifyDocumentResponseTypeDef",
    "ContainsPiiEntitiesRequestRequestTypeDef",
    "ContainsPiiEntitiesResponseTypeDef",
    "CreateDocumentClassifierRequestRequestTypeDef",
    "CreateDocumentClassifierResponseTypeDef",
    "CreateEndpointRequestRequestTypeDef",
    "CreateEndpointResponseTypeDef",
    "CreateEntityRecognizerRequestRequestTypeDef",
    "CreateEntityRecognizerResponseTypeDef",
    "DeleteDocumentClassifierRequestRequestTypeDef",
    "DeleteEndpointRequestRequestTypeDef",
    "DeleteEntityRecognizerRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DescribeDocumentClassificationJobRequestRequestTypeDef",
    "DescribeDocumentClassificationJobResponseTypeDef",
    "DescribeDocumentClassifierRequestRequestTypeDef",
    "DescribeDocumentClassifierResponseTypeDef",
    "DescribeDominantLanguageDetectionJobRequestRequestTypeDef",
    "DescribeDominantLanguageDetectionJobResponseTypeDef",
    "DescribeEndpointRequestRequestTypeDef",
    "DescribeEndpointResponseTypeDef",
    "DescribeEntitiesDetectionJobRequestRequestTypeDef",
    "DescribeEntitiesDetectionJobResponseTypeDef",
    "DescribeEntityRecognizerRequestRequestTypeDef",
    "DescribeEntityRecognizerResponseTypeDef",
    "DescribeEventsDetectionJobRequestRequestTypeDef",
    "DescribeEventsDetectionJobResponseTypeDef",
    "DescribeKeyPhrasesDetectionJobRequestRequestTypeDef",
    "DescribeKeyPhrasesDetectionJobResponseTypeDef",
    "DescribePiiEntitiesDetectionJobRequestRequestTypeDef",
    "DescribePiiEntitiesDetectionJobResponseTypeDef",
    "DescribeResourcePolicyRequestRequestTypeDef",
    "DescribeResourcePolicyResponseTypeDef",
    "DescribeSentimentDetectionJobRequestRequestTypeDef",
    "DescribeSentimentDetectionJobResponseTypeDef",
    "DescribeTargetedSentimentDetectionJobRequestRequestTypeDef",
    "DescribeTargetedSentimentDetectionJobResponseTypeDef",
    "DescribeTopicsDetectionJobRequestRequestTypeDef",
    "DescribeTopicsDetectionJobResponseTypeDef",
    "DetectDominantLanguageRequestRequestTypeDef",
    "DetectDominantLanguageResponseTypeDef",
    "DetectEntitiesRequestRequestTypeDef",
    "DetectEntitiesResponseTypeDef",
    "DetectKeyPhrasesRequestRequestTypeDef",
    "DetectKeyPhrasesResponseTypeDef",
    "DetectPiiEntitiesRequestRequestTypeDef",
    "DetectPiiEntitiesResponseTypeDef",
    "DetectSentimentRequestRequestTypeDef",
    "DetectSentimentResponseTypeDef",
    "DetectSyntaxRequestRequestTypeDef",
    "DetectSyntaxResponseTypeDef",
    "DocumentClassTypeDef",
    "DocumentClassificationJobFilterTypeDef",
    "DocumentClassificationJobPropertiesTypeDef",
    "DocumentClassifierFilterTypeDef",
    "DocumentClassifierInputDataConfigTypeDef",
    "DocumentClassifierOutputDataConfigTypeDef",
    "DocumentClassifierPropertiesTypeDef",
    "DocumentClassifierSummaryTypeDef",
    "DocumentLabelTypeDef",
    "DocumentReaderConfigTypeDef",
    "DominantLanguageDetectionJobFilterTypeDef",
    "DominantLanguageDetectionJobPropertiesTypeDef",
    "DominantLanguageTypeDef",
    "EndpointFilterTypeDef",
    "EndpointPropertiesTypeDef",
    "EntitiesDetectionJobFilterTypeDef",
    "EntitiesDetectionJobPropertiesTypeDef",
    "EntityLabelTypeDef",
    "EntityRecognizerAnnotationsTypeDef",
    "EntityRecognizerDocumentsTypeDef",
    "EntityRecognizerEntityListTypeDef",
    "EntityRecognizerEvaluationMetricsTypeDef",
    "EntityRecognizerFilterTypeDef",
    "EntityRecognizerInputDataConfigTypeDef",
    "EntityRecognizerMetadataEntityTypesListItemTypeDef",
    "EntityRecognizerMetadataTypeDef",
    "EntityRecognizerPropertiesTypeDef",
    "EntityRecognizerSummaryTypeDef",
    "EntityTypeDef",
    "EntityTypesEvaluationMetricsTypeDef",
    "EntityTypesListItemTypeDef",
    "EventsDetectionJobFilterTypeDef",
    "EventsDetectionJobPropertiesTypeDef",
    "ImportModelRequestRequestTypeDef",
    "ImportModelResponseTypeDef",
    "InputDataConfigTypeDef",
    "KeyPhraseTypeDef",
    "KeyPhrasesDetectionJobFilterTypeDef",
    "KeyPhrasesDetectionJobPropertiesTypeDef",
    "ListDocumentClassificationJobsRequestRequestTypeDef",
    "ListDocumentClassificationJobsResponseTypeDef",
    "ListDocumentClassifierSummariesRequestRequestTypeDef",
    "ListDocumentClassifierSummariesResponseTypeDef",
    "ListDocumentClassifiersRequestRequestTypeDef",
    "ListDocumentClassifiersResponseTypeDef",
    "ListDominantLanguageDetectionJobsRequestRequestTypeDef",
    "ListDominantLanguageDetectionJobsResponseTypeDef",
    "ListEndpointsRequestRequestTypeDef",
    "ListEndpointsResponseTypeDef",
    "ListEntitiesDetectionJobsRequestRequestTypeDef",
    "ListEntitiesDetectionJobsResponseTypeDef",
    "ListEntityRecognizerSummariesRequestRequestTypeDef",
    "ListEntityRecognizerSummariesResponseTypeDef",
    "ListEntityRecognizersRequestRequestTypeDef",
    "ListEntityRecognizersResponseTypeDef",
    "ListEventsDetectionJobsRequestRequestTypeDef",
    "ListEventsDetectionJobsResponseTypeDef",
    "ListKeyPhrasesDetectionJobsRequestRequestTypeDef",
    "ListKeyPhrasesDetectionJobsResponseTypeDef",
    "ListPiiEntitiesDetectionJobsRequestRequestTypeDef",
    "ListPiiEntitiesDetectionJobsResponseTypeDef",
    "ListSentimentDetectionJobsRequestRequestTypeDef",
    "ListSentimentDetectionJobsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTargetedSentimentDetectionJobsRequestRequestTypeDef",
    "ListTargetedSentimentDetectionJobsResponseTypeDef",
    "ListTopicsDetectionJobsRequestRequestTypeDef",
    "ListTopicsDetectionJobsResponseTypeDef",
    "OutputDataConfigTypeDef",
    "PaginatorConfigTypeDef",
    "PartOfSpeechTagTypeDef",
    "PiiEntitiesDetectionJobFilterTypeDef",
    "PiiEntitiesDetectionJobPropertiesTypeDef",
    "PiiEntityTypeDef",
    "PiiOutputDataConfigTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "RedactionConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SentimentDetectionJobFilterTypeDef",
    "SentimentDetectionJobPropertiesTypeDef",
    "SentimentScoreTypeDef",
    "StartDocumentClassificationJobRequestRequestTypeDef",
    "StartDocumentClassificationJobResponseTypeDef",
    "StartDominantLanguageDetectionJobRequestRequestTypeDef",
    "StartDominantLanguageDetectionJobResponseTypeDef",
    "StartEntitiesDetectionJobRequestRequestTypeDef",
    "StartEntitiesDetectionJobResponseTypeDef",
    "StartEventsDetectionJobRequestRequestTypeDef",
    "StartEventsDetectionJobResponseTypeDef",
    "StartKeyPhrasesDetectionJobRequestRequestTypeDef",
    "StartKeyPhrasesDetectionJobResponseTypeDef",
    "StartPiiEntitiesDetectionJobRequestRequestTypeDef",
    "StartPiiEntitiesDetectionJobResponseTypeDef",
    "StartSentimentDetectionJobRequestRequestTypeDef",
    "StartSentimentDetectionJobResponseTypeDef",
    "StartTargetedSentimentDetectionJobRequestRequestTypeDef",
    "StartTargetedSentimentDetectionJobResponseTypeDef",
    "StartTopicsDetectionJobRequestRequestTypeDef",
    "StartTopicsDetectionJobResponseTypeDef",
    "StopDominantLanguageDetectionJobRequestRequestTypeDef",
    "StopDominantLanguageDetectionJobResponseTypeDef",
    "StopEntitiesDetectionJobRequestRequestTypeDef",
    "StopEntitiesDetectionJobResponseTypeDef",
    "StopEventsDetectionJobRequestRequestTypeDef",
    "StopEventsDetectionJobResponseTypeDef",
    "StopKeyPhrasesDetectionJobRequestRequestTypeDef",
    "StopKeyPhrasesDetectionJobResponseTypeDef",
    "StopPiiEntitiesDetectionJobRequestRequestTypeDef",
    "StopPiiEntitiesDetectionJobResponseTypeDef",
    "StopSentimentDetectionJobRequestRequestTypeDef",
    "StopSentimentDetectionJobResponseTypeDef",
    "StopTargetedSentimentDetectionJobRequestRequestTypeDef",
    "StopTargetedSentimentDetectionJobResponseTypeDef",
    "StopTrainingDocumentClassifierRequestRequestTypeDef",
    "StopTrainingEntityRecognizerRequestRequestTypeDef",
    "SyntaxTokenTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TargetedSentimentDetectionJobFilterTypeDef",
    "TargetedSentimentDetectionJobPropertiesTypeDef",
    "TopicsDetectionJobFilterTypeDef",
    "TopicsDetectionJobPropertiesTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateEndpointRequestRequestTypeDef",
    "VpcConfigTypeDef",
)

AugmentedManifestsListItemTypeDef = TypedDict(
    "AugmentedManifestsListItemTypeDef",
    {
        "S3Uri": str,
        "AttributeNames": Sequence[str],
        "Split": NotRequired[SplitType],
        "AnnotationDataS3Uri": NotRequired[str],
        "SourceDocumentsS3Uri": NotRequired[str],
        "DocumentType": NotRequired[AugmentedManifestsDocumentTypeFormatType],
    },
)

BatchDetectDominantLanguageItemResultTypeDef = TypedDict(
    "BatchDetectDominantLanguageItemResultTypeDef",
    {
        "Index": NotRequired[int],
        "Languages": NotRequired[List["DominantLanguageTypeDef"]],
    },
)

BatchDetectDominantLanguageRequestRequestTypeDef = TypedDict(
    "BatchDetectDominantLanguageRequestRequestTypeDef",
    {
        "TextList": Sequence[str],
    },
)

BatchDetectDominantLanguageResponseTypeDef = TypedDict(
    "BatchDetectDominantLanguageResponseTypeDef",
    {
        "ResultList": List["BatchDetectDominantLanguageItemResultTypeDef"],
        "ErrorList": List["BatchItemErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDetectEntitiesItemResultTypeDef = TypedDict(
    "BatchDetectEntitiesItemResultTypeDef",
    {
        "Index": NotRequired[int],
        "Entities": NotRequired[List["EntityTypeDef"]],
    },
)

BatchDetectEntitiesRequestRequestTypeDef = TypedDict(
    "BatchDetectEntitiesRequestRequestTypeDef",
    {
        "TextList": Sequence[str],
        "LanguageCode": LanguageCodeType,
    },
)

BatchDetectEntitiesResponseTypeDef = TypedDict(
    "BatchDetectEntitiesResponseTypeDef",
    {
        "ResultList": List["BatchDetectEntitiesItemResultTypeDef"],
        "ErrorList": List["BatchItemErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDetectKeyPhrasesItemResultTypeDef = TypedDict(
    "BatchDetectKeyPhrasesItemResultTypeDef",
    {
        "Index": NotRequired[int],
        "KeyPhrases": NotRequired[List["KeyPhraseTypeDef"]],
    },
)

BatchDetectKeyPhrasesRequestRequestTypeDef = TypedDict(
    "BatchDetectKeyPhrasesRequestRequestTypeDef",
    {
        "TextList": Sequence[str],
        "LanguageCode": LanguageCodeType,
    },
)

BatchDetectKeyPhrasesResponseTypeDef = TypedDict(
    "BatchDetectKeyPhrasesResponseTypeDef",
    {
        "ResultList": List["BatchDetectKeyPhrasesItemResultTypeDef"],
        "ErrorList": List["BatchItemErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDetectSentimentItemResultTypeDef = TypedDict(
    "BatchDetectSentimentItemResultTypeDef",
    {
        "Index": NotRequired[int],
        "Sentiment": NotRequired[SentimentTypeType],
        "SentimentScore": NotRequired["SentimentScoreTypeDef"],
    },
)

BatchDetectSentimentRequestRequestTypeDef = TypedDict(
    "BatchDetectSentimentRequestRequestTypeDef",
    {
        "TextList": Sequence[str],
        "LanguageCode": LanguageCodeType,
    },
)

BatchDetectSentimentResponseTypeDef = TypedDict(
    "BatchDetectSentimentResponseTypeDef",
    {
        "ResultList": List["BatchDetectSentimentItemResultTypeDef"],
        "ErrorList": List["BatchItemErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDetectSyntaxItemResultTypeDef = TypedDict(
    "BatchDetectSyntaxItemResultTypeDef",
    {
        "Index": NotRequired[int],
        "SyntaxTokens": NotRequired[List["SyntaxTokenTypeDef"]],
    },
)

BatchDetectSyntaxRequestRequestTypeDef = TypedDict(
    "BatchDetectSyntaxRequestRequestTypeDef",
    {
        "TextList": Sequence[str],
        "LanguageCode": SyntaxLanguageCodeType,
    },
)

BatchDetectSyntaxResponseTypeDef = TypedDict(
    "BatchDetectSyntaxResponseTypeDef",
    {
        "ResultList": List["BatchDetectSyntaxItemResultTypeDef"],
        "ErrorList": List["BatchItemErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchItemErrorTypeDef = TypedDict(
    "BatchItemErrorTypeDef",
    {
        "Index": NotRequired[int],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

ClassifierEvaluationMetricsTypeDef = TypedDict(
    "ClassifierEvaluationMetricsTypeDef",
    {
        "Accuracy": NotRequired[float],
        "Precision": NotRequired[float],
        "Recall": NotRequired[float],
        "F1Score": NotRequired[float],
        "MicroPrecision": NotRequired[float],
        "MicroRecall": NotRequired[float],
        "MicroF1Score": NotRequired[float],
        "HammingLoss": NotRequired[float],
    },
)

ClassifierMetadataTypeDef = TypedDict(
    "ClassifierMetadataTypeDef",
    {
        "NumberOfLabels": NotRequired[int],
        "NumberOfTrainedDocuments": NotRequired[int],
        "NumberOfTestDocuments": NotRequired[int],
        "EvaluationMetrics": NotRequired["ClassifierEvaluationMetricsTypeDef"],
    },
)

ClassifyDocumentRequestRequestTypeDef = TypedDict(
    "ClassifyDocumentRequestRequestTypeDef",
    {
        "Text": str,
        "EndpointArn": str,
    },
)

ClassifyDocumentResponseTypeDef = TypedDict(
    "ClassifyDocumentResponseTypeDef",
    {
        "Classes": List["DocumentClassTypeDef"],
        "Labels": List["DocumentLabelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ContainsPiiEntitiesRequestRequestTypeDef = TypedDict(
    "ContainsPiiEntitiesRequestRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)

ContainsPiiEntitiesResponseTypeDef = TypedDict(
    "ContainsPiiEntitiesResponseTypeDef",
    {
        "Labels": List["EntityLabelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDocumentClassifierRequestRequestTypeDef = TypedDict(
    "CreateDocumentClassifierRequestRequestTypeDef",
    {
        "DocumentClassifierName": str,
        "DataAccessRoleArn": str,
        "InputDataConfig": "DocumentClassifierInputDataConfigTypeDef",
        "LanguageCode": LanguageCodeType,
        "VersionName": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "OutputDataConfig": NotRequired["DocumentClassifierOutputDataConfigTypeDef"],
        "ClientRequestToken": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "Mode": NotRequired[DocumentClassifierModeType],
        "ModelKmsKeyId": NotRequired[str],
        "ModelPolicy": NotRequired[str],
    },
)

CreateDocumentClassifierResponseTypeDef = TypedDict(
    "CreateDocumentClassifierResponseTypeDef",
    {
        "DocumentClassifierArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEndpointRequestRequestTypeDef = TypedDict(
    "CreateEndpointRequestRequestTypeDef",
    {
        "EndpointName": str,
        "ModelArn": str,
        "DesiredInferenceUnits": int,
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "DataAccessRoleArn": NotRequired[str],
    },
)

CreateEndpointResponseTypeDef = TypedDict(
    "CreateEndpointResponseTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEntityRecognizerRequestRequestTypeDef = TypedDict(
    "CreateEntityRecognizerRequestRequestTypeDef",
    {
        "RecognizerName": str,
        "DataAccessRoleArn": str,
        "InputDataConfig": "EntityRecognizerInputDataConfigTypeDef",
        "LanguageCode": LanguageCodeType,
        "VersionName": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ClientRequestToken": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "ModelKmsKeyId": NotRequired[str],
        "ModelPolicy": NotRequired[str],
    },
)

CreateEntityRecognizerResponseTypeDef = TypedDict(
    "CreateEntityRecognizerResponseTypeDef",
    {
        "EntityRecognizerArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDocumentClassifierRequestRequestTypeDef = TypedDict(
    "DeleteDocumentClassifierRequestRequestTypeDef",
    {
        "DocumentClassifierArn": str,
    },
)

DeleteEndpointRequestRequestTypeDef = TypedDict(
    "DeleteEndpointRequestRequestTypeDef",
    {
        "EndpointArn": str,
    },
)

DeleteEntityRecognizerRequestRequestTypeDef = TypedDict(
    "DeleteEntityRecognizerRequestRequestTypeDef",
    {
        "EntityRecognizerArn": str,
    },
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "PolicyRevisionId": NotRequired[str],
    },
)

DescribeDocumentClassificationJobRequestRequestTypeDef = TypedDict(
    "DescribeDocumentClassificationJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeDocumentClassificationJobResponseTypeDef = TypedDict(
    "DescribeDocumentClassificationJobResponseTypeDef",
    {
        "DocumentClassificationJobProperties": "DocumentClassificationJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDocumentClassifierRequestRequestTypeDef = TypedDict(
    "DescribeDocumentClassifierRequestRequestTypeDef",
    {
        "DocumentClassifierArn": str,
    },
)

DescribeDocumentClassifierResponseTypeDef = TypedDict(
    "DescribeDocumentClassifierResponseTypeDef",
    {
        "DocumentClassifierProperties": "DocumentClassifierPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDominantLanguageDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribeDominantLanguageDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeDominantLanguageDetectionJobResponseTypeDef = TypedDict(
    "DescribeDominantLanguageDetectionJobResponseTypeDef",
    {
        "DominantLanguageDetectionJobProperties": "DominantLanguageDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointRequestRequestTypeDef = TypedDict(
    "DescribeEndpointRequestRequestTypeDef",
    {
        "EndpointArn": str,
    },
)

DescribeEndpointResponseTypeDef = TypedDict(
    "DescribeEndpointResponseTypeDef",
    {
        "EndpointProperties": "EndpointPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEntitiesDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribeEntitiesDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeEntitiesDetectionJobResponseTypeDef = TypedDict(
    "DescribeEntitiesDetectionJobResponseTypeDef",
    {
        "EntitiesDetectionJobProperties": "EntitiesDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEntityRecognizerRequestRequestTypeDef = TypedDict(
    "DescribeEntityRecognizerRequestRequestTypeDef",
    {
        "EntityRecognizerArn": str,
    },
)

DescribeEntityRecognizerResponseTypeDef = TypedDict(
    "DescribeEntityRecognizerResponseTypeDef",
    {
        "EntityRecognizerProperties": "EntityRecognizerPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventsDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribeEventsDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeEventsDetectionJobResponseTypeDef = TypedDict(
    "DescribeEventsDetectionJobResponseTypeDef",
    {
        "EventsDetectionJobProperties": "EventsDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeKeyPhrasesDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribeKeyPhrasesDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeKeyPhrasesDetectionJobResponseTypeDef = TypedDict(
    "DescribeKeyPhrasesDetectionJobResponseTypeDef",
    {
        "KeyPhrasesDetectionJobProperties": "KeyPhrasesDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePiiEntitiesDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribePiiEntitiesDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribePiiEntitiesDetectionJobResponseTypeDef = TypedDict(
    "DescribePiiEntitiesDetectionJobResponseTypeDef",
    {
        "PiiEntitiesDetectionJobProperties": "PiiEntitiesDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourcePolicyRequestRequestTypeDef = TypedDict(
    "DescribeResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeResourcePolicyResponseTypeDef = TypedDict(
    "DescribeResourcePolicyResponseTypeDef",
    {
        "ResourcePolicy": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "PolicyRevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSentimentDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribeSentimentDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeSentimentDetectionJobResponseTypeDef = TypedDict(
    "DescribeSentimentDetectionJobResponseTypeDef",
    {
        "SentimentDetectionJobProperties": "SentimentDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTargetedSentimentDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribeTargetedSentimentDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeTargetedSentimentDetectionJobResponseTypeDef = TypedDict(
    "DescribeTargetedSentimentDetectionJobResponseTypeDef",
    {
        "TargetedSentimentDetectionJobProperties": "TargetedSentimentDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTopicsDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribeTopicsDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeTopicsDetectionJobResponseTypeDef = TypedDict(
    "DescribeTopicsDetectionJobResponseTypeDef",
    {
        "TopicsDetectionJobProperties": "TopicsDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectDominantLanguageRequestRequestTypeDef = TypedDict(
    "DetectDominantLanguageRequestRequestTypeDef",
    {
        "Text": str,
    },
)

DetectDominantLanguageResponseTypeDef = TypedDict(
    "DetectDominantLanguageResponseTypeDef",
    {
        "Languages": List["DominantLanguageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectEntitiesRequestRequestTypeDef = TypedDict(
    "DetectEntitiesRequestRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": NotRequired[LanguageCodeType],
        "EndpointArn": NotRequired[str],
    },
)

DetectEntitiesResponseTypeDef = TypedDict(
    "DetectEntitiesResponseTypeDef",
    {
        "Entities": List["EntityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectKeyPhrasesRequestRequestTypeDef = TypedDict(
    "DetectKeyPhrasesRequestRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)

DetectKeyPhrasesResponseTypeDef = TypedDict(
    "DetectKeyPhrasesResponseTypeDef",
    {
        "KeyPhrases": List["KeyPhraseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectPiiEntitiesRequestRequestTypeDef = TypedDict(
    "DetectPiiEntitiesRequestRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)

DetectPiiEntitiesResponseTypeDef = TypedDict(
    "DetectPiiEntitiesResponseTypeDef",
    {
        "Entities": List["PiiEntityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectSentimentRequestRequestTypeDef = TypedDict(
    "DetectSentimentRequestRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)

DetectSentimentResponseTypeDef = TypedDict(
    "DetectSentimentResponseTypeDef",
    {
        "Sentiment": SentimentTypeType,
        "SentimentScore": "SentimentScoreTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectSyntaxRequestRequestTypeDef = TypedDict(
    "DetectSyntaxRequestRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": SyntaxLanguageCodeType,
    },
)

DetectSyntaxResponseTypeDef = TypedDict(
    "DetectSyntaxResponseTypeDef",
    {
        "SyntaxTokens": List["SyntaxTokenTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DocumentClassTypeDef = TypedDict(
    "DocumentClassTypeDef",
    {
        "Name": NotRequired[str],
        "Score": NotRequired[float],
    },
)

DocumentClassificationJobFilterTypeDef = TypedDict(
    "DocumentClassificationJobFilterTypeDef",
    {
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmitTimeBefore": NotRequired[Union[datetime, str]],
        "SubmitTimeAfter": NotRequired[Union[datetime, str]],
    },
)

DocumentClassificationJobPropertiesTypeDef = TypedDict(
    "DocumentClassificationJobPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "DocumentClassifierArn": NotRequired[str],
        "InputDataConfig": NotRequired["InputDataConfigTypeDef"],
        "OutputDataConfig": NotRequired["OutputDataConfigTypeDef"],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
    },
)

DocumentClassifierFilterTypeDef = TypedDict(
    "DocumentClassifierFilterTypeDef",
    {
        "Status": NotRequired[ModelStatusType],
        "DocumentClassifierName": NotRequired[str],
        "SubmitTimeBefore": NotRequired[Union[datetime, str]],
        "SubmitTimeAfter": NotRequired[Union[datetime, str]],
    },
)

DocumentClassifierInputDataConfigTypeDef = TypedDict(
    "DocumentClassifierInputDataConfigTypeDef",
    {
        "DataFormat": NotRequired[DocumentClassifierDataFormatType],
        "S3Uri": NotRequired[str],
        "TestS3Uri": NotRequired[str],
        "LabelDelimiter": NotRequired[str],
        "AugmentedManifests": NotRequired[Sequence["AugmentedManifestsListItemTypeDef"]],
    },
)

DocumentClassifierOutputDataConfigTypeDef = TypedDict(
    "DocumentClassifierOutputDataConfigTypeDef",
    {
        "S3Uri": NotRequired[str],
        "KmsKeyId": NotRequired[str],
    },
)

DocumentClassifierPropertiesTypeDef = TypedDict(
    "DocumentClassifierPropertiesTypeDef",
    {
        "DocumentClassifierArn": NotRequired[str],
        "LanguageCode": NotRequired[LanguageCodeType],
        "Status": NotRequired[ModelStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "TrainingStartTime": NotRequired[datetime],
        "TrainingEndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired["DocumentClassifierInputDataConfigTypeDef"],
        "OutputDataConfig": NotRequired["DocumentClassifierOutputDataConfigTypeDef"],
        "ClassifierMetadata": NotRequired["ClassifierMetadataTypeDef"],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "Mode": NotRequired[DocumentClassifierModeType],
        "ModelKmsKeyId": NotRequired[str],
        "VersionName": NotRequired[str],
        "SourceModelArn": NotRequired[str],
    },
)

DocumentClassifierSummaryTypeDef = TypedDict(
    "DocumentClassifierSummaryTypeDef",
    {
        "DocumentClassifierName": NotRequired[str],
        "NumberOfVersions": NotRequired[int],
        "LatestVersionCreatedAt": NotRequired[datetime],
        "LatestVersionName": NotRequired[str],
        "LatestVersionStatus": NotRequired[ModelStatusType],
    },
)

DocumentLabelTypeDef = TypedDict(
    "DocumentLabelTypeDef",
    {
        "Name": NotRequired[str],
        "Score": NotRequired[float],
    },
)

DocumentReaderConfigTypeDef = TypedDict(
    "DocumentReaderConfigTypeDef",
    {
        "DocumentReadAction": DocumentReadActionType,
        "DocumentReadMode": NotRequired[DocumentReadModeType],
        "FeatureTypes": NotRequired[List[DocumentReadFeatureTypesType]],
    },
)

DominantLanguageDetectionJobFilterTypeDef = TypedDict(
    "DominantLanguageDetectionJobFilterTypeDef",
    {
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmitTimeBefore": NotRequired[Union[datetime, str]],
        "SubmitTimeAfter": NotRequired[Union[datetime, str]],
    },
)

DominantLanguageDetectionJobPropertiesTypeDef = TypedDict(
    "DominantLanguageDetectionJobPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired["InputDataConfigTypeDef"],
        "OutputDataConfig": NotRequired["OutputDataConfigTypeDef"],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
    },
)

DominantLanguageTypeDef = TypedDict(
    "DominantLanguageTypeDef",
    {
        "LanguageCode": NotRequired[str],
        "Score": NotRequired[float],
    },
)

EndpointFilterTypeDef = TypedDict(
    "EndpointFilterTypeDef",
    {
        "ModelArn": NotRequired[str],
        "Status": NotRequired[EndpointStatusType],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
    },
)

EndpointPropertiesTypeDef = TypedDict(
    "EndpointPropertiesTypeDef",
    {
        "EndpointArn": NotRequired[str],
        "Status": NotRequired[EndpointStatusType],
        "Message": NotRequired[str],
        "ModelArn": NotRequired[str],
        "DesiredModelArn": NotRequired[str],
        "DesiredInferenceUnits": NotRequired[int],
        "CurrentInferenceUnits": NotRequired[int],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "DataAccessRoleArn": NotRequired[str],
        "DesiredDataAccessRoleArn": NotRequired[str],
    },
)

EntitiesDetectionJobFilterTypeDef = TypedDict(
    "EntitiesDetectionJobFilterTypeDef",
    {
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmitTimeBefore": NotRequired[Union[datetime, str]],
        "SubmitTimeAfter": NotRequired[Union[datetime, str]],
    },
)

EntitiesDetectionJobPropertiesTypeDef = TypedDict(
    "EntitiesDetectionJobPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "EntityRecognizerArn": NotRequired[str],
        "InputDataConfig": NotRequired["InputDataConfigTypeDef"],
        "OutputDataConfig": NotRequired["OutputDataConfigTypeDef"],
        "LanguageCode": NotRequired[LanguageCodeType],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
    },
)

EntityLabelTypeDef = TypedDict(
    "EntityLabelTypeDef",
    {
        "Name": NotRequired[PiiEntityTypeType],
        "Score": NotRequired[float],
    },
)

EntityRecognizerAnnotationsTypeDef = TypedDict(
    "EntityRecognizerAnnotationsTypeDef",
    {
        "S3Uri": str,
        "TestS3Uri": NotRequired[str],
    },
)

EntityRecognizerDocumentsTypeDef = TypedDict(
    "EntityRecognizerDocumentsTypeDef",
    {
        "S3Uri": str,
        "TestS3Uri": NotRequired[str],
        "InputFormat": NotRequired[InputFormatType],
    },
)

EntityRecognizerEntityListTypeDef = TypedDict(
    "EntityRecognizerEntityListTypeDef",
    {
        "S3Uri": str,
    },
)

EntityRecognizerEvaluationMetricsTypeDef = TypedDict(
    "EntityRecognizerEvaluationMetricsTypeDef",
    {
        "Precision": NotRequired[float],
        "Recall": NotRequired[float],
        "F1Score": NotRequired[float],
    },
)

EntityRecognizerFilterTypeDef = TypedDict(
    "EntityRecognizerFilterTypeDef",
    {
        "Status": NotRequired[ModelStatusType],
        "RecognizerName": NotRequired[str],
        "SubmitTimeBefore": NotRequired[Union[datetime, str]],
        "SubmitTimeAfter": NotRequired[Union[datetime, str]],
    },
)

EntityRecognizerInputDataConfigTypeDef = TypedDict(
    "EntityRecognizerInputDataConfigTypeDef",
    {
        "EntityTypes": Sequence["EntityTypesListItemTypeDef"],
        "DataFormat": NotRequired[EntityRecognizerDataFormatType],
        "Documents": NotRequired["EntityRecognizerDocumentsTypeDef"],
        "Annotations": NotRequired["EntityRecognizerAnnotationsTypeDef"],
        "EntityList": NotRequired["EntityRecognizerEntityListTypeDef"],
        "AugmentedManifests": NotRequired[Sequence["AugmentedManifestsListItemTypeDef"]],
    },
)

EntityRecognizerMetadataEntityTypesListItemTypeDef = TypedDict(
    "EntityRecognizerMetadataEntityTypesListItemTypeDef",
    {
        "Type": NotRequired[str],
        "EvaluationMetrics": NotRequired["EntityTypesEvaluationMetricsTypeDef"],
        "NumberOfTrainMentions": NotRequired[int],
    },
)

EntityRecognizerMetadataTypeDef = TypedDict(
    "EntityRecognizerMetadataTypeDef",
    {
        "NumberOfTrainedDocuments": NotRequired[int],
        "NumberOfTestDocuments": NotRequired[int],
        "EvaluationMetrics": NotRequired["EntityRecognizerEvaluationMetricsTypeDef"],
        "EntityTypes": NotRequired[List["EntityRecognizerMetadataEntityTypesListItemTypeDef"]],
    },
)

EntityRecognizerPropertiesTypeDef = TypedDict(
    "EntityRecognizerPropertiesTypeDef",
    {
        "EntityRecognizerArn": NotRequired[str],
        "LanguageCode": NotRequired[LanguageCodeType],
        "Status": NotRequired[ModelStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "TrainingStartTime": NotRequired[datetime],
        "TrainingEndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired["EntityRecognizerInputDataConfigTypeDef"],
        "RecognizerMetadata": NotRequired["EntityRecognizerMetadataTypeDef"],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "ModelKmsKeyId": NotRequired[str],
        "VersionName": NotRequired[str],
        "SourceModelArn": NotRequired[str],
    },
)

EntityRecognizerSummaryTypeDef = TypedDict(
    "EntityRecognizerSummaryTypeDef",
    {
        "RecognizerName": NotRequired[str],
        "NumberOfVersions": NotRequired[int],
        "LatestVersionCreatedAt": NotRequired[datetime],
        "LatestVersionName": NotRequired[str],
        "LatestVersionStatus": NotRequired[ModelStatusType],
    },
)

EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "Score": NotRequired[float],
        "Type": NotRequired[EntityTypeType],
        "Text": NotRequired[str],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
    },
)

EntityTypesEvaluationMetricsTypeDef = TypedDict(
    "EntityTypesEvaluationMetricsTypeDef",
    {
        "Precision": NotRequired[float],
        "Recall": NotRequired[float],
        "F1Score": NotRequired[float],
    },
)

EntityTypesListItemTypeDef = TypedDict(
    "EntityTypesListItemTypeDef",
    {
        "Type": str,
    },
)

EventsDetectionJobFilterTypeDef = TypedDict(
    "EventsDetectionJobFilterTypeDef",
    {
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmitTimeBefore": NotRequired[Union[datetime, str]],
        "SubmitTimeAfter": NotRequired[Union[datetime, str]],
    },
)

EventsDetectionJobPropertiesTypeDef = TypedDict(
    "EventsDetectionJobPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired["InputDataConfigTypeDef"],
        "OutputDataConfig": NotRequired["OutputDataConfigTypeDef"],
        "LanguageCode": NotRequired[LanguageCodeType],
        "DataAccessRoleArn": NotRequired[str],
        "TargetEventTypes": NotRequired[List[str]],
    },
)

ImportModelRequestRequestTypeDef = TypedDict(
    "ImportModelRequestRequestTypeDef",
    {
        "SourceModelArn": str,
        "ModelName": NotRequired[str],
        "VersionName": NotRequired[str],
        "ModelKmsKeyId": NotRequired[str],
        "DataAccessRoleArn": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

ImportModelResponseTypeDef = TypedDict(
    "ImportModelResponseTypeDef",
    {
        "ModelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputDataConfigTypeDef = TypedDict(
    "InputDataConfigTypeDef",
    {
        "S3Uri": str,
        "InputFormat": NotRequired[InputFormatType],
        "DocumentReaderConfig": NotRequired["DocumentReaderConfigTypeDef"],
    },
)

KeyPhraseTypeDef = TypedDict(
    "KeyPhraseTypeDef",
    {
        "Score": NotRequired[float],
        "Text": NotRequired[str],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
    },
)

KeyPhrasesDetectionJobFilterTypeDef = TypedDict(
    "KeyPhrasesDetectionJobFilterTypeDef",
    {
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmitTimeBefore": NotRequired[Union[datetime, str]],
        "SubmitTimeAfter": NotRequired[Union[datetime, str]],
    },
)

KeyPhrasesDetectionJobPropertiesTypeDef = TypedDict(
    "KeyPhrasesDetectionJobPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired["InputDataConfigTypeDef"],
        "OutputDataConfig": NotRequired["OutputDataConfigTypeDef"],
        "LanguageCode": NotRequired[LanguageCodeType],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
    },
)

ListDocumentClassificationJobsRequestRequestTypeDef = TypedDict(
    "ListDocumentClassificationJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired["DocumentClassificationJobFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDocumentClassificationJobsResponseTypeDef = TypedDict(
    "ListDocumentClassificationJobsResponseTypeDef",
    {
        "DocumentClassificationJobPropertiesList": List[
            "DocumentClassificationJobPropertiesTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDocumentClassifierSummariesRequestRequestTypeDef = TypedDict(
    "ListDocumentClassifierSummariesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDocumentClassifierSummariesResponseTypeDef = TypedDict(
    "ListDocumentClassifierSummariesResponseTypeDef",
    {
        "DocumentClassifierSummariesList": List["DocumentClassifierSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDocumentClassifiersRequestRequestTypeDef = TypedDict(
    "ListDocumentClassifiersRequestRequestTypeDef",
    {
        "Filter": NotRequired["DocumentClassifierFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDocumentClassifiersResponseTypeDef = TypedDict(
    "ListDocumentClassifiersResponseTypeDef",
    {
        "DocumentClassifierPropertiesList": List["DocumentClassifierPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDominantLanguageDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListDominantLanguageDetectionJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired["DominantLanguageDetectionJobFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDominantLanguageDetectionJobsResponseTypeDef = TypedDict(
    "ListDominantLanguageDetectionJobsResponseTypeDef",
    {
        "DominantLanguageDetectionJobPropertiesList": List[
            "DominantLanguageDetectionJobPropertiesTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEndpointsRequestRequestTypeDef = TypedDict(
    "ListEndpointsRequestRequestTypeDef",
    {
        "Filter": NotRequired["EndpointFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListEndpointsResponseTypeDef = TypedDict(
    "ListEndpointsResponseTypeDef",
    {
        "EndpointPropertiesList": List["EndpointPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEntitiesDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListEntitiesDetectionJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired["EntitiesDetectionJobFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListEntitiesDetectionJobsResponseTypeDef = TypedDict(
    "ListEntitiesDetectionJobsResponseTypeDef",
    {
        "EntitiesDetectionJobPropertiesList": List["EntitiesDetectionJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEntityRecognizerSummariesRequestRequestTypeDef = TypedDict(
    "ListEntityRecognizerSummariesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListEntityRecognizerSummariesResponseTypeDef = TypedDict(
    "ListEntityRecognizerSummariesResponseTypeDef",
    {
        "EntityRecognizerSummariesList": List["EntityRecognizerSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEntityRecognizersRequestRequestTypeDef = TypedDict(
    "ListEntityRecognizersRequestRequestTypeDef",
    {
        "Filter": NotRequired["EntityRecognizerFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListEntityRecognizersResponseTypeDef = TypedDict(
    "ListEntityRecognizersResponseTypeDef",
    {
        "EntityRecognizerPropertiesList": List["EntityRecognizerPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventsDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListEventsDetectionJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired["EventsDetectionJobFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListEventsDetectionJobsResponseTypeDef = TypedDict(
    "ListEventsDetectionJobsResponseTypeDef",
    {
        "EventsDetectionJobPropertiesList": List["EventsDetectionJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKeyPhrasesDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListKeyPhrasesDetectionJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired["KeyPhrasesDetectionJobFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListKeyPhrasesDetectionJobsResponseTypeDef = TypedDict(
    "ListKeyPhrasesDetectionJobsResponseTypeDef",
    {
        "KeyPhrasesDetectionJobPropertiesList": List["KeyPhrasesDetectionJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPiiEntitiesDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListPiiEntitiesDetectionJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired["PiiEntitiesDetectionJobFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListPiiEntitiesDetectionJobsResponseTypeDef = TypedDict(
    "ListPiiEntitiesDetectionJobsResponseTypeDef",
    {
        "PiiEntitiesDetectionJobPropertiesList": List["PiiEntitiesDetectionJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSentimentDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListSentimentDetectionJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired["SentimentDetectionJobFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListSentimentDetectionJobsResponseTypeDef = TypedDict(
    "ListSentimentDetectionJobsResponseTypeDef",
    {
        "SentimentDetectionJobPropertiesList": List["SentimentDetectionJobPropertiesTypeDef"],
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
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTargetedSentimentDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListTargetedSentimentDetectionJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired["TargetedSentimentDetectionJobFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTargetedSentimentDetectionJobsResponseTypeDef = TypedDict(
    "ListTargetedSentimentDetectionJobsResponseTypeDef",
    {
        "TargetedSentimentDetectionJobPropertiesList": List[
            "TargetedSentimentDetectionJobPropertiesTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTopicsDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListTopicsDetectionJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired["TopicsDetectionJobFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTopicsDetectionJobsResponseTypeDef = TypedDict(
    "ListTopicsDetectionJobsResponseTypeDef",
    {
        "TopicsDetectionJobPropertiesList": List["TopicsDetectionJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OutputDataConfigTypeDef = TypedDict(
    "OutputDataConfigTypeDef",
    {
        "S3Uri": str,
        "KmsKeyId": NotRequired[str],
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

PartOfSpeechTagTypeDef = TypedDict(
    "PartOfSpeechTagTypeDef",
    {
        "Tag": NotRequired[PartOfSpeechTagTypeType],
        "Score": NotRequired[float],
    },
)

PiiEntitiesDetectionJobFilterTypeDef = TypedDict(
    "PiiEntitiesDetectionJobFilterTypeDef",
    {
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmitTimeBefore": NotRequired[Union[datetime, str]],
        "SubmitTimeAfter": NotRequired[Union[datetime, str]],
    },
)

PiiEntitiesDetectionJobPropertiesTypeDef = TypedDict(
    "PiiEntitiesDetectionJobPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired["InputDataConfigTypeDef"],
        "OutputDataConfig": NotRequired["PiiOutputDataConfigTypeDef"],
        "RedactionConfig": NotRequired["RedactionConfigTypeDef"],
        "LanguageCode": NotRequired[LanguageCodeType],
        "DataAccessRoleArn": NotRequired[str],
        "Mode": NotRequired[PiiEntitiesDetectionModeType],
    },
)

PiiEntityTypeDef = TypedDict(
    "PiiEntityTypeDef",
    {
        "Score": NotRequired[float],
        "Type": NotRequired[PiiEntityTypeType],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
    },
)

PiiOutputDataConfigTypeDef = TypedDict(
    "PiiOutputDataConfigTypeDef",
    {
        "S3Uri": str,
        "KmsKeyId": NotRequired[str],
    },
)

PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "ResourcePolicy": str,
        "PolicyRevisionId": NotRequired[str],
    },
)

PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef",
    {
        "PolicyRevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RedactionConfigTypeDef = TypedDict(
    "RedactionConfigTypeDef",
    {
        "PiiEntityTypes": NotRequired[List[PiiEntityTypeType]],
        "MaskMode": NotRequired[PiiEntitiesDetectionMaskModeType],
        "MaskCharacter": NotRequired[str],
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

SentimentDetectionJobFilterTypeDef = TypedDict(
    "SentimentDetectionJobFilterTypeDef",
    {
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmitTimeBefore": NotRequired[Union[datetime, str]],
        "SubmitTimeAfter": NotRequired[Union[datetime, str]],
    },
)

SentimentDetectionJobPropertiesTypeDef = TypedDict(
    "SentimentDetectionJobPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired["InputDataConfigTypeDef"],
        "OutputDataConfig": NotRequired["OutputDataConfigTypeDef"],
        "LanguageCode": NotRequired[LanguageCodeType],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
    },
)

SentimentScoreTypeDef = TypedDict(
    "SentimentScoreTypeDef",
    {
        "Positive": NotRequired[float],
        "Negative": NotRequired[float],
        "Neutral": NotRequired[float],
        "Mixed": NotRequired[float],
    },
)

StartDocumentClassificationJobRequestRequestTypeDef = TypedDict(
    "StartDocumentClassificationJobRequestRequestTypeDef",
    {
        "DocumentClassifierArn": str,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

StartDocumentClassificationJobResponseTypeDef = TypedDict(
    "StartDocumentClassificationJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartDominantLanguageDetectionJobRequestRequestTypeDef = TypedDict(
    "StartDominantLanguageDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

StartDominantLanguageDetectionJobResponseTypeDef = TypedDict(
    "StartDominantLanguageDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartEntitiesDetectionJobRequestRequestTypeDef = TypedDict(
    "StartEntitiesDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
        "JobName": NotRequired[str],
        "EntityRecognizerArn": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

StartEntitiesDetectionJobResponseTypeDef = TypedDict(
    "StartEntitiesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartEventsDetectionJobRequestRequestTypeDef = TypedDict(
    "StartEventsDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
        "TargetEventTypes": Sequence[str],
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

StartEventsDetectionJobResponseTypeDef = TypedDict(
    "StartEventsDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartKeyPhrasesDetectionJobRequestRequestTypeDef = TypedDict(
    "StartKeyPhrasesDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

StartKeyPhrasesDetectionJobResponseTypeDef = TypedDict(
    "StartKeyPhrasesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartPiiEntitiesDetectionJobRequestRequestTypeDef = TypedDict(
    "StartPiiEntitiesDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "Mode": PiiEntitiesDetectionModeType,
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
        "RedactionConfig": NotRequired["RedactionConfigTypeDef"],
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

StartPiiEntitiesDetectionJobResponseTypeDef = TypedDict(
    "StartPiiEntitiesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartSentimentDetectionJobRequestRequestTypeDef = TypedDict(
    "StartSentimentDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

StartSentimentDetectionJobResponseTypeDef = TypedDict(
    "StartSentimentDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartTargetedSentimentDetectionJobRequestRequestTypeDef = TypedDict(
    "StartTargetedSentimentDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

StartTargetedSentimentDetectionJobResponseTypeDef = TypedDict(
    "StartTargetedSentimentDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartTopicsDetectionJobRequestRequestTypeDef = TypedDict(
    "StartTopicsDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "JobName": NotRequired[str],
        "NumberOfTopics": NotRequired[int],
        "ClientRequestToken": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

StartTopicsDetectionJobResponseTypeDef = TypedDict(
    "StartTopicsDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopDominantLanguageDetectionJobRequestRequestTypeDef = TypedDict(
    "StopDominantLanguageDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopDominantLanguageDetectionJobResponseTypeDef = TypedDict(
    "StopDominantLanguageDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopEntitiesDetectionJobRequestRequestTypeDef = TypedDict(
    "StopEntitiesDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopEntitiesDetectionJobResponseTypeDef = TypedDict(
    "StopEntitiesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopEventsDetectionJobRequestRequestTypeDef = TypedDict(
    "StopEventsDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopEventsDetectionJobResponseTypeDef = TypedDict(
    "StopEventsDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopKeyPhrasesDetectionJobRequestRequestTypeDef = TypedDict(
    "StopKeyPhrasesDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopKeyPhrasesDetectionJobResponseTypeDef = TypedDict(
    "StopKeyPhrasesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopPiiEntitiesDetectionJobRequestRequestTypeDef = TypedDict(
    "StopPiiEntitiesDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopPiiEntitiesDetectionJobResponseTypeDef = TypedDict(
    "StopPiiEntitiesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopSentimentDetectionJobRequestRequestTypeDef = TypedDict(
    "StopSentimentDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopSentimentDetectionJobResponseTypeDef = TypedDict(
    "StopSentimentDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopTargetedSentimentDetectionJobRequestRequestTypeDef = TypedDict(
    "StopTargetedSentimentDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopTargetedSentimentDetectionJobResponseTypeDef = TypedDict(
    "StopTargetedSentimentDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopTrainingDocumentClassifierRequestRequestTypeDef = TypedDict(
    "StopTrainingDocumentClassifierRequestRequestTypeDef",
    {
        "DocumentClassifierArn": str,
    },
)

StopTrainingEntityRecognizerRequestRequestTypeDef = TypedDict(
    "StopTrainingEntityRecognizerRequestRequestTypeDef",
    {
        "EntityRecognizerArn": str,
    },
)

SyntaxTokenTypeDef = TypedDict(
    "SyntaxTokenTypeDef",
    {
        "TokenId": NotRequired[int],
        "Text": NotRequired[str],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "PartOfSpeech": NotRequired["PartOfSpeechTagTypeDef"],
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
        "Value": NotRequired[str],
    },
)

TargetedSentimentDetectionJobFilterTypeDef = TypedDict(
    "TargetedSentimentDetectionJobFilterTypeDef",
    {
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmitTimeBefore": NotRequired[Union[datetime, str]],
        "SubmitTimeAfter": NotRequired[Union[datetime, str]],
    },
)

TargetedSentimentDetectionJobPropertiesTypeDef = TypedDict(
    "TargetedSentimentDetectionJobPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired["InputDataConfigTypeDef"],
        "OutputDataConfig": NotRequired["OutputDataConfigTypeDef"],
        "LanguageCode": NotRequired[LanguageCodeType],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
    },
)

TopicsDetectionJobFilterTypeDef = TypedDict(
    "TopicsDetectionJobFilterTypeDef",
    {
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmitTimeBefore": NotRequired[Union[datetime, str]],
        "SubmitTimeAfter": NotRequired[Union[datetime, str]],
    },
)

TopicsDetectionJobPropertiesTypeDef = TypedDict(
    "TopicsDetectionJobPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired["InputDataConfigTypeDef"],
        "OutputDataConfig": NotRequired["OutputDataConfigTypeDef"],
        "NumberOfTopics": NotRequired[int],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateEndpointRequestRequestTypeDef = TypedDict(
    "UpdateEndpointRequestRequestTypeDef",
    {
        "EndpointArn": str,
        "DesiredModelArn": NotRequired[str],
        "DesiredInferenceUnits": NotRequired[int],
        "DesiredDataAccessRoleArn": NotRequired[str],
    },
)

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "SecurityGroupIds": Sequence[str],
        "Subnets": Sequence[str],
    },
)
