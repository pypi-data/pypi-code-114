"""
Type annotations for rekognition service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_rekognition.type_defs import AgeRangeTypeDef

    data: AgeRangeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    AttributeType,
    BodyPartType,
    CelebrityRecognitionSortByType,
    ContentClassifierType,
    ContentModerationSortByType,
    DatasetStatusMessageCodeType,
    DatasetStatusType,
    DatasetTypeType,
    EmotionNameType,
    FaceAttributesType,
    FaceSearchSortByType,
    GenderTypeType,
    KnownGenderTypeType,
    LabelDetectionSortByType,
    LandmarkTypeType,
    OrientationCorrectionType,
    PersonTrackingSortByType,
    ProjectStatusType,
    ProjectVersionStatusType,
    ProtectiveEquipmentTypeType,
    QualityFilterType,
    ReasonType,
    SegmentTypeType,
    StreamProcessorStatusType,
    TechnicalCueTypeType,
    TextTypesType,
    VideoColorRangeType,
    VideoJobStatusType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AgeRangeTypeDef",
    "AssetTypeDef",
    "AudioMetadataTypeDef",
    "BeardTypeDef",
    "BlackFrameTypeDef",
    "BoundingBoxTypeDef",
    "CelebrityDetailTypeDef",
    "CelebrityRecognitionTypeDef",
    "CelebrityTypeDef",
    "CompareFacesMatchTypeDef",
    "CompareFacesRequestRequestTypeDef",
    "CompareFacesResponseTypeDef",
    "ComparedFaceTypeDef",
    "ComparedSourceImageFaceTypeDef",
    "ContentModerationDetectionTypeDef",
    "CoversBodyPartTypeDef",
    "CreateCollectionRequestRequestTypeDef",
    "CreateCollectionResponseTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "CreateProjectResponseTypeDef",
    "CreateProjectVersionRequestRequestTypeDef",
    "CreateProjectVersionResponseTypeDef",
    "CreateStreamProcessorRequestRequestTypeDef",
    "CreateStreamProcessorResponseTypeDef",
    "CustomLabelTypeDef",
    "DatasetChangesTypeDef",
    "DatasetDescriptionTypeDef",
    "DatasetLabelDescriptionTypeDef",
    "DatasetLabelStatsTypeDef",
    "DatasetMetadataTypeDef",
    "DatasetSourceTypeDef",
    "DatasetStatsTypeDef",
    "DeleteCollectionRequestRequestTypeDef",
    "DeleteCollectionResponseTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteFacesRequestRequestTypeDef",
    "DeleteFacesResponseTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteProjectResponseTypeDef",
    "DeleteProjectVersionRequestRequestTypeDef",
    "DeleteProjectVersionResponseTypeDef",
    "DeleteStreamProcessorRequestRequestTypeDef",
    "DescribeCollectionRequestRequestTypeDef",
    "DescribeCollectionResponseTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeProjectVersionsRequestRequestTypeDef",
    "DescribeProjectVersionsResponseTypeDef",
    "DescribeProjectsRequestRequestTypeDef",
    "DescribeProjectsResponseTypeDef",
    "DescribeStreamProcessorRequestRequestTypeDef",
    "DescribeStreamProcessorResponseTypeDef",
    "DetectCustomLabelsRequestRequestTypeDef",
    "DetectCustomLabelsResponseTypeDef",
    "DetectFacesRequestRequestTypeDef",
    "DetectFacesResponseTypeDef",
    "DetectLabelsRequestRequestTypeDef",
    "DetectLabelsResponseTypeDef",
    "DetectModerationLabelsRequestRequestTypeDef",
    "DetectModerationLabelsResponseTypeDef",
    "DetectProtectiveEquipmentRequestRequestTypeDef",
    "DetectProtectiveEquipmentResponseTypeDef",
    "DetectTextFiltersTypeDef",
    "DetectTextRequestRequestTypeDef",
    "DetectTextResponseTypeDef",
    "DetectionFilterTypeDef",
    "DistributeDatasetEntriesRequestRequestTypeDef",
    "DistributeDatasetTypeDef",
    "EmotionTypeDef",
    "EquipmentDetectionTypeDef",
    "EvaluationResultTypeDef",
    "EyeOpenTypeDef",
    "EyeglassesTypeDef",
    "FaceDetailTypeDef",
    "FaceDetectionTypeDef",
    "FaceMatchTypeDef",
    "FaceRecordTypeDef",
    "FaceSearchSettingsTypeDef",
    "FaceTypeDef",
    "GenderTypeDef",
    "GeometryTypeDef",
    "GetCelebrityInfoRequestRequestTypeDef",
    "GetCelebrityInfoResponseTypeDef",
    "GetCelebrityRecognitionRequestRequestTypeDef",
    "GetCelebrityRecognitionResponseTypeDef",
    "GetContentModerationRequestRequestTypeDef",
    "GetContentModerationResponseTypeDef",
    "GetFaceDetectionRequestRequestTypeDef",
    "GetFaceDetectionResponseTypeDef",
    "GetFaceSearchRequestRequestTypeDef",
    "GetFaceSearchResponseTypeDef",
    "GetLabelDetectionRequestRequestTypeDef",
    "GetLabelDetectionResponseTypeDef",
    "GetPersonTrackingRequestRequestTypeDef",
    "GetPersonTrackingResponseTypeDef",
    "GetSegmentDetectionRequestRequestTypeDef",
    "GetSegmentDetectionResponseTypeDef",
    "GetTextDetectionRequestRequestTypeDef",
    "GetTextDetectionResponseTypeDef",
    "GroundTruthManifestTypeDef",
    "HumanLoopActivationOutputTypeDef",
    "HumanLoopConfigTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "ImageQualityTypeDef",
    "ImageTypeDef",
    "IndexFacesRequestRequestTypeDef",
    "IndexFacesResponseTypeDef",
    "InstanceTypeDef",
    "KinesisDataStreamTypeDef",
    "KinesisVideoStreamTypeDef",
    "KnownGenderTypeDef",
    "LabelDetectionTypeDef",
    "LabelTypeDef",
    "LandmarkTypeDef",
    "ListCollectionsRequestRequestTypeDef",
    "ListCollectionsResponseTypeDef",
    "ListDatasetEntriesRequestRequestTypeDef",
    "ListDatasetEntriesResponseTypeDef",
    "ListDatasetLabelsRequestRequestTypeDef",
    "ListDatasetLabelsResponseTypeDef",
    "ListFacesRequestRequestTypeDef",
    "ListFacesResponseTypeDef",
    "ListStreamProcessorsRequestRequestTypeDef",
    "ListStreamProcessorsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ModerationLabelTypeDef",
    "MouthOpenTypeDef",
    "MustacheTypeDef",
    "NotificationChannelTypeDef",
    "OutputConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ParentTypeDef",
    "PersonDetailTypeDef",
    "PersonDetectionTypeDef",
    "PersonMatchTypeDef",
    "PointTypeDef",
    "PoseTypeDef",
    "ProjectDescriptionTypeDef",
    "ProjectVersionDescriptionTypeDef",
    "ProtectiveEquipmentBodyPartTypeDef",
    "ProtectiveEquipmentPersonTypeDef",
    "ProtectiveEquipmentSummarizationAttributesTypeDef",
    "ProtectiveEquipmentSummaryTypeDef",
    "RecognizeCelebritiesRequestRequestTypeDef",
    "RecognizeCelebritiesResponseTypeDef",
    "RegionOfInterestTypeDef",
    "ResponseMetadataTypeDef",
    "S3ObjectTypeDef",
    "SearchFacesByImageRequestRequestTypeDef",
    "SearchFacesByImageResponseTypeDef",
    "SearchFacesRequestRequestTypeDef",
    "SearchFacesResponseTypeDef",
    "SegmentDetectionTypeDef",
    "SegmentTypeInfoTypeDef",
    "ShotSegmentTypeDef",
    "SmileTypeDef",
    "StartCelebrityRecognitionRequestRequestTypeDef",
    "StartCelebrityRecognitionResponseTypeDef",
    "StartContentModerationRequestRequestTypeDef",
    "StartContentModerationResponseTypeDef",
    "StartFaceDetectionRequestRequestTypeDef",
    "StartFaceDetectionResponseTypeDef",
    "StartFaceSearchRequestRequestTypeDef",
    "StartFaceSearchResponseTypeDef",
    "StartLabelDetectionRequestRequestTypeDef",
    "StartLabelDetectionResponseTypeDef",
    "StartPersonTrackingRequestRequestTypeDef",
    "StartPersonTrackingResponseTypeDef",
    "StartProjectVersionRequestRequestTypeDef",
    "StartProjectVersionResponseTypeDef",
    "StartSegmentDetectionFiltersTypeDef",
    "StartSegmentDetectionRequestRequestTypeDef",
    "StartSegmentDetectionResponseTypeDef",
    "StartShotDetectionFilterTypeDef",
    "StartStreamProcessorRequestRequestTypeDef",
    "StartTechnicalCueDetectionFilterTypeDef",
    "StartTextDetectionFiltersTypeDef",
    "StartTextDetectionRequestRequestTypeDef",
    "StartTextDetectionResponseTypeDef",
    "StopProjectVersionRequestRequestTypeDef",
    "StopProjectVersionResponseTypeDef",
    "StopStreamProcessorRequestRequestTypeDef",
    "StreamProcessorInputTypeDef",
    "StreamProcessorOutputTypeDef",
    "StreamProcessorSettingsTypeDef",
    "StreamProcessorTypeDef",
    "SummaryTypeDef",
    "SunglassesTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TechnicalCueSegmentTypeDef",
    "TestingDataResultTypeDef",
    "TestingDataTypeDef",
    "TextDetectionResultTypeDef",
    "TextDetectionTypeDef",
    "TrainingDataResultTypeDef",
    "TrainingDataTypeDef",
    "UnindexedFaceTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDatasetEntriesRequestRequestTypeDef",
    "ValidationDataTypeDef",
    "VideoMetadataTypeDef",
    "VideoTypeDef",
    "WaiterConfigTypeDef",
)

AgeRangeTypeDef = TypedDict(
    "AgeRangeTypeDef",
    {
        "Low": NotRequired[int],
        "High": NotRequired[int],
    },
)

AssetTypeDef = TypedDict(
    "AssetTypeDef",
    {
        "GroundTruthManifest": NotRequired["GroundTruthManifestTypeDef"],
    },
)

AudioMetadataTypeDef = TypedDict(
    "AudioMetadataTypeDef",
    {
        "Codec": NotRequired[str],
        "DurationMillis": NotRequired[int],
        "SampleRate": NotRequired[int],
        "NumberOfChannels": NotRequired[int],
    },
)

BeardTypeDef = TypedDict(
    "BeardTypeDef",
    {
        "Value": NotRequired[bool],
        "Confidence": NotRequired[float],
    },
)

BlackFrameTypeDef = TypedDict(
    "BlackFrameTypeDef",
    {
        "MaxPixelThreshold": NotRequired[float],
        "MinCoveragePercentage": NotRequired[float],
    },
)

BoundingBoxTypeDef = TypedDict(
    "BoundingBoxTypeDef",
    {
        "Width": NotRequired[float],
        "Height": NotRequired[float],
        "Left": NotRequired[float],
        "Top": NotRequired[float],
    },
)

CelebrityDetailTypeDef = TypedDict(
    "CelebrityDetailTypeDef",
    {
        "Urls": NotRequired[List[str]],
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "Confidence": NotRequired[float],
        "BoundingBox": NotRequired["BoundingBoxTypeDef"],
        "Face": NotRequired["FaceDetailTypeDef"],
        "KnownGender": NotRequired["KnownGenderTypeDef"],
    },
)

CelebrityRecognitionTypeDef = TypedDict(
    "CelebrityRecognitionTypeDef",
    {
        "Timestamp": NotRequired[int],
        "Celebrity": NotRequired["CelebrityDetailTypeDef"],
    },
)

CelebrityTypeDef = TypedDict(
    "CelebrityTypeDef",
    {
        "Urls": NotRequired[List[str]],
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "Face": NotRequired["ComparedFaceTypeDef"],
        "MatchConfidence": NotRequired[float],
        "KnownGender": NotRequired["KnownGenderTypeDef"],
    },
)

CompareFacesMatchTypeDef = TypedDict(
    "CompareFacesMatchTypeDef",
    {
        "Similarity": NotRequired[float],
        "Face": NotRequired["ComparedFaceTypeDef"],
    },
)

CompareFacesRequestRequestTypeDef = TypedDict(
    "CompareFacesRequestRequestTypeDef",
    {
        "SourceImage": "ImageTypeDef",
        "TargetImage": "ImageTypeDef",
        "SimilarityThreshold": NotRequired[float],
        "QualityFilter": NotRequired[QualityFilterType],
    },
)

CompareFacesResponseTypeDef = TypedDict(
    "CompareFacesResponseTypeDef",
    {
        "SourceImageFace": "ComparedSourceImageFaceTypeDef",
        "FaceMatches": List["CompareFacesMatchTypeDef"],
        "UnmatchedFaces": List["ComparedFaceTypeDef"],
        "SourceImageOrientationCorrection": OrientationCorrectionType,
        "TargetImageOrientationCorrection": OrientationCorrectionType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ComparedFaceTypeDef = TypedDict(
    "ComparedFaceTypeDef",
    {
        "BoundingBox": NotRequired["BoundingBoxTypeDef"],
        "Confidence": NotRequired[float],
        "Landmarks": NotRequired[List["LandmarkTypeDef"]],
        "Pose": NotRequired["PoseTypeDef"],
        "Quality": NotRequired["ImageQualityTypeDef"],
        "Emotions": NotRequired[List["EmotionTypeDef"]],
        "Smile": NotRequired["SmileTypeDef"],
    },
)

ComparedSourceImageFaceTypeDef = TypedDict(
    "ComparedSourceImageFaceTypeDef",
    {
        "BoundingBox": NotRequired["BoundingBoxTypeDef"],
        "Confidence": NotRequired[float],
    },
)

ContentModerationDetectionTypeDef = TypedDict(
    "ContentModerationDetectionTypeDef",
    {
        "Timestamp": NotRequired[int],
        "ModerationLabel": NotRequired["ModerationLabelTypeDef"],
    },
)

CoversBodyPartTypeDef = TypedDict(
    "CoversBodyPartTypeDef",
    {
        "Confidence": NotRequired[float],
        "Value": NotRequired[bool],
    },
)

CreateCollectionRequestRequestTypeDef = TypedDict(
    "CreateCollectionRequestRequestTypeDef",
    {
        "CollectionId": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateCollectionResponseTypeDef = TypedDict(
    "CreateCollectionResponseTypeDef",
    {
        "StatusCode": int,
        "CollectionArn": str,
        "FaceModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDatasetRequestRequestTypeDef = TypedDict(
    "CreateDatasetRequestRequestTypeDef",
    {
        "DatasetType": DatasetTypeType,
        "ProjectArn": str,
        "DatasetSource": NotRequired["DatasetSourceTypeDef"],
    },
)

CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "DatasetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProjectRequestRequestTypeDef = TypedDict(
    "CreateProjectRequestRequestTypeDef",
    {
        "ProjectName": str,
    },
)

CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef",
    {
        "ProjectArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProjectVersionRequestRequestTypeDef = TypedDict(
    "CreateProjectVersionRequestRequestTypeDef",
    {
        "ProjectArn": str,
        "VersionName": str,
        "OutputConfig": "OutputConfigTypeDef",
        "TrainingData": NotRequired["TrainingDataTypeDef"],
        "TestingData": NotRequired["TestingDataTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
        "KmsKeyId": NotRequired[str],
    },
)

CreateProjectVersionResponseTypeDef = TypedDict(
    "CreateProjectVersionResponseTypeDef",
    {
        "ProjectVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStreamProcessorRequestRequestTypeDef = TypedDict(
    "CreateStreamProcessorRequestRequestTypeDef",
    {
        "Input": "StreamProcessorInputTypeDef",
        "Output": "StreamProcessorOutputTypeDef",
        "Name": str,
        "Settings": "StreamProcessorSettingsTypeDef",
        "RoleArn": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateStreamProcessorResponseTypeDef = TypedDict(
    "CreateStreamProcessorResponseTypeDef",
    {
        "StreamProcessorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomLabelTypeDef = TypedDict(
    "CustomLabelTypeDef",
    {
        "Name": NotRequired[str],
        "Confidence": NotRequired[float],
        "Geometry": NotRequired["GeometryTypeDef"],
    },
)

DatasetChangesTypeDef = TypedDict(
    "DatasetChangesTypeDef",
    {
        "GroundTruth": Union[bytes, IO[bytes], StreamingBody],
    },
)

DatasetDescriptionTypeDef = TypedDict(
    "DatasetDescriptionTypeDef",
    {
        "CreationTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "Status": NotRequired[DatasetStatusType],
        "StatusMessage": NotRequired[str],
        "StatusMessageCode": NotRequired[DatasetStatusMessageCodeType],
        "DatasetStats": NotRequired["DatasetStatsTypeDef"],
    },
)

DatasetLabelDescriptionTypeDef = TypedDict(
    "DatasetLabelDescriptionTypeDef",
    {
        "LabelName": NotRequired[str],
        "LabelStats": NotRequired["DatasetLabelStatsTypeDef"],
    },
)

DatasetLabelStatsTypeDef = TypedDict(
    "DatasetLabelStatsTypeDef",
    {
        "EntryCount": NotRequired[int],
        "BoundingBoxCount": NotRequired[int],
    },
)

DatasetMetadataTypeDef = TypedDict(
    "DatasetMetadataTypeDef",
    {
        "CreationTimestamp": NotRequired[datetime],
        "DatasetType": NotRequired[DatasetTypeType],
        "DatasetArn": NotRequired[str],
        "Status": NotRequired[DatasetStatusType],
        "StatusMessage": NotRequired[str],
        "StatusMessageCode": NotRequired[DatasetStatusMessageCodeType],
    },
)

DatasetSourceTypeDef = TypedDict(
    "DatasetSourceTypeDef",
    {
        "GroundTruthManifest": NotRequired["GroundTruthManifestTypeDef"],
        "DatasetArn": NotRequired[str],
    },
)

DatasetStatsTypeDef = TypedDict(
    "DatasetStatsTypeDef",
    {
        "LabeledEntries": NotRequired[int],
        "TotalEntries": NotRequired[int],
        "TotalLabels": NotRequired[int],
        "ErrorEntries": NotRequired[int],
    },
)

DeleteCollectionRequestRequestTypeDef = TypedDict(
    "DeleteCollectionRequestRequestTypeDef",
    {
        "CollectionId": str,
    },
)

DeleteCollectionResponseTypeDef = TypedDict(
    "DeleteCollectionResponseTypeDef",
    {
        "StatusCode": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "DatasetArn": str,
    },
)

DeleteFacesRequestRequestTypeDef = TypedDict(
    "DeleteFacesRequestRequestTypeDef",
    {
        "CollectionId": str,
        "FaceIds": Sequence[str],
    },
)

DeleteFacesResponseTypeDef = TypedDict(
    "DeleteFacesResponseTypeDef",
    {
        "DeletedFaces": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "ProjectArn": str,
    },
)

DeleteProjectResponseTypeDef = TypedDict(
    "DeleteProjectResponseTypeDef",
    {
        "Status": ProjectStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProjectVersionRequestRequestTypeDef = TypedDict(
    "DeleteProjectVersionRequestRequestTypeDef",
    {
        "ProjectVersionArn": str,
    },
)

DeleteProjectVersionResponseTypeDef = TypedDict(
    "DeleteProjectVersionResponseTypeDef",
    {
        "Status": ProjectVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteStreamProcessorRequestRequestTypeDef = TypedDict(
    "DeleteStreamProcessorRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeCollectionRequestRequestTypeDef = TypedDict(
    "DescribeCollectionRequestRequestTypeDef",
    {
        "CollectionId": str,
    },
)

DescribeCollectionResponseTypeDef = TypedDict(
    "DescribeCollectionResponseTypeDef",
    {
        "FaceCount": int,
        "FaceModelVersion": str,
        "CollectionARN": str,
        "CreationTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "DatasetArn": str,
    },
)

DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "DatasetDescription": "DatasetDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectVersionsRequestRequestTypeDef = TypedDict(
    "DescribeProjectVersionsRequestRequestTypeDef",
    {
        "ProjectArn": str,
        "VersionNames": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeProjectVersionsResponseTypeDef = TypedDict(
    "DescribeProjectVersionsResponseTypeDef",
    {
        "ProjectVersionDescriptions": List["ProjectVersionDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectsRequestRequestTypeDef = TypedDict(
    "DescribeProjectsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ProjectNames": NotRequired[Sequence[str]],
    },
)

DescribeProjectsResponseTypeDef = TypedDict(
    "DescribeProjectsResponseTypeDef",
    {
        "ProjectDescriptions": List["ProjectDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStreamProcessorRequestRequestTypeDef = TypedDict(
    "DescribeStreamProcessorRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeStreamProcessorResponseTypeDef = TypedDict(
    "DescribeStreamProcessorResponseTypeDef",
    {
        "Name": str,
        "StreamProcessorArn": str,
        "Status": StreamProcessorStatusType,
        "StatusMessage": str,
        "CreationTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "Input": "StreamProcessorInputTypeDef",
        "Output": "StreamProcessorOutputTypeDef",
        "RoleArn": str,
        "Settings": "StreamProcessorSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectCustomLabelsRequestRequestTypeDef = TypedDict(
    "DetectCustomLabelsRequestRequestTypeDef",
    {
        "ProjectVersionArn": str,
        "Image": "ImageTypeDef",
        "MaxResults": NotRequired[int],
        "MinConfidence": NotRequired[float],
    },
)

DetectCustomLabelsResponseTypeDef = TypedDict(
    "DetectCustomLabelsResponseTypeDef",
    {
        "CustomLabels": List["CustomLabelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectFacesRequestRequestTypeDef = TypedDict(
    "DetectFacesRequestRequestTypeDef",
    {
        "Image": "ImageTypeDef",
        "Attributes": NotRequired[Sequence[AttributeType]],
    },
)

DetectFacesResponseTypeDef = TypedDict(
    "DetectFacesResponseTypeDef",
    {
        "FaceDetails": List["FaceDetailTypeDef"],
        "OrientationCorrection": OrientationCorrectionType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectLabelsRequestRequestTypeDef = TypedDict(
    "DetectLabelsRequestRequestTypeDef",
    {
        "Image": "ImageTypeDef",
        "MaxLabels": NotRequired[int],
        "MinConfidence": NotRequired[float],
    },
)

DetectLabelsResponseTypeDef = TypedDict(
    "DetectLabelsResponseTypeDef",
    {
        "Labels": List["LabelTypeDef"],
        "OrientationCorrection": OrientationCorrectionType,
        "LabelModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectModerationLabelsRequestRequestTypeDef = TypedDict(
    "DetectModerationLabelsRequestRequestTypeDef",
    {
        "Image": "ImageTypeDef",
        "MinConfidence": NotRequired[float],
        "HumanLoopConfig": NotRequired["HumanLoopConfigTypeDef"],
    },
)

DetectModerationLabelsResponseTypeDef = TypedDict(
    "DetectModerationLabelsResponseTypeDef",
    {
        "ModerationLabels": List["ModerationLabelTypeDef"],
        "ModerationModelVersion": str,
        "HumanLoopActivationOutput": "HumanLoopActivationOutputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectProtectiveEquipmentRequestRequestTypeDef = TypedDict(
    "DetectProtectiveEquipmentRequestRequestTypeDef",
    {
        "Image": "ImageTypeDef",
        "SummarizationAttributes": NotRequired["ProtectiveEquipmentSummarizationAttributesTypeDef"],
    },
)

DetectProtectiveEquipmentResponseTypeDef = TypedDict(
    "DetectProtectiveEquipmentResponseTypeDef",
    {
        "ProtectiveEquipmentModelVersion": str,
        "Persons": List["ProtectiveEquipmentPersonTypeDef"],
        "Summary": "ProtectiveEquipmentSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectTextFiltersTypeDef = TypedDict(
    "DetectTextFiltersTypeDef",
    {
        "WordFilter": NotRequired["DetectionFilterTypeDef"],
        "RegionsOfInterest": NotRequired[Sequence["RegionOfInterestTypeDef"]],
    },
)

DetectTextRequestRequestTypeDef = TypedDict(
    "DetectTextRequestRequestTypeDef",
    {
        "Image": "ImageTypeDef",
        "Filters": NotRequired["DetectTextFiltersTypeDef"],
    },
)

DetectTextResponseTypeDef = TypedDict(
    "DetectTextResponseTypeDef",
    {
        "TextDetections": List["TextDetectionTypeDef"],
        "TextModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectionFilterTypeDef = TypedDict(
    "DetectionFilterTypeDef",
    {
        "MinConfidence": NotRequired[float],
        "MinBoundingBoxHeight": NotRequired[float],
        "MinBoundingBoxWidth": NotRequired[float],
    },
)

DistributeDatasetEntriesRequestRequestTypeDef = TypedDict(
    "DistributeDatasetEntriesRequestRequestTypeDef",
    {
        "Datasets": Sequence["DistributeDatasetTypeDef"],
    },
)

DistributeDatasetTypeDef = TypedDict(
    "DistributeDatasetTypeDef",
    {
        "Arn": str,
    },
)

EmotionTypeDef = TypedDict(
    "EmotionTypeDef",
    {
        "Type": NotRequired[EmotionNameType],
        "Confidence": NotRequired[float],
    },
)

EquipmentDetectionTypeDef = TypedDict(
    "EquipmentDetectionTypeDef",
    {
        "BoundingBox": NotRequired["BoundingBoxTypeDef"],
        "Confidence": NotRequired[float],
        "Type": NotRequired[ProtectiveEquipmentTypeType],
        "CoversBodyPart": NotRequired["CoversBodyPartTypeDef"],
    },
)

EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "F1Score": NotRequired[float],
        "Summary": NotRequired["SummaryTypeDef"],
    },
)

EyeOpenTypeDef = TypedDict(
    "EyeOpenTypeDef",
    {
        "Value": NotRequired[bool],
        "Confidence": NotRequired[float],
    },
)

EyeglassesTypeDef = TypedDict(
    "EyeglassesTypeDef",
    {
        "Value": NotRequired[bool],
        "Confidence": NotRequired[float],
    },
)

FaceDetailTypeDef = TypedDict(
    "FaceDetailTypeDef",
    {
        "BoundingBox": NotRequired["BoundingBoxTypeDef"],
        "AgeRange": NotRequired["AgeRangeTypeDef"],
        "Smile": NotRequired["SmileTypeDef"],
        "Eyeglasses": NotRequired["EyeglassesTypeDef"],
        "Sunglasses": NotRequired["SunglassesTypeDef"],
        "Gender": NotRequired["GenderTypeDef"],
        "Beard": NotRequired["BeardTypeDef"],
        "Mustache": NotRequired["MustacheTypeDef"],
        "EyesOpen": NotRequired["EyeOpenTypeDef"],
        "MouthOpen": NotRequired["MouthOpenTypeDef"],
        "Emotions": NotRequired[List["EmotionTypeDef"]],
        "Landmarks": NotRequired[List["LandmarkTypeDef"]],
        "Pose": NotRequired["PoseTypeDef"],
        "Quality": NotRequired["ImageQualityTypeDef"],
        "Confidence": NotRequired[float],
    },
)

FaceDetectionTypeDef = TypedDict(
    "FaceDetectionTypeDef",
    {
        "Timestamp": NotRequired[int],
        "Face": NotRequired["FaceDetailTypeDef"],
    },
)

FaceMatchTypeDef = TypedDict(
    "FaceMatchTypeDef",
    {
        "Similarity": NotRequired[float],
        "Face": NotRequired["FaceTypeDef"],
    },
)

FaceRecordTypeDef = TypedDict(
    "FaceRecordTypeDef",
    {
        "Face": NotRequired["FaceTypeDef"],
        "FaceDetail": NotRequired["FaceDetailTypeDef"],
    },
)

FaceSearchSettingsTypeDef = TypedDict(
    "FaceSearchSettingsTypeDef",
    {
        "CollectionId": NotRequired[str],
        "FaceMatchThreshold": NotRequired[float],
    },
)

FaceTypeDef = TypedDict(
    "FaceTypeDef",
    {
        "FaceId": NotRequired[str],
        "BoundingBox": NotRequired["BoundingBoxTypeDef"],
        "ImageId": NotRequired[str],
        "ExternalImageId": NotRequired[str],
        "Confidence": NotRequired[float],
        "IndexFacesModelVersion": NotRequired[str],
    },
)

GenderTypeDef = TypedDict(
    "GenderTypeDef",
    {
        "Value": NotRequired[GenderTypeType],
        "Confidence": NotRequired[float],
    },
)

GeometryTypeDef = TypedDict(
    "GeometryTypeDef",
    {
        "BoundingBox": NotRequired["BoundingBoxTypeDef"],
        "Polygon": NotRequired[List["PointTypeDef"]],
    },
)

GetCelebrityInfoRequestRequestTypeDef = TypedDict(
    "GetCelebrityInfoRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetCelebrityInfoResponseTypeDef = TypedDict(
    "GetCelebrityInfoResponseTypeDef",
    {
        "Urls": List[str],
        "Name": str,
        "KnownGender": "KnownGenderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCelebrityRecognitionRequestRequestTypeDef = TypedDict(
    "GetCelebrityRecognitionRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SortBy": NotRequired[CelebrityRecognitionSortByType],
    },
)

GetCelebrityRecognitionResponseTypeDef = TypedDict(
    "GetCelebrityRecognitionResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "NextToken": str,
        "Celebrities": List["CelebrityRecognitionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContentModerationRequestRequestTypeDef = TypedDict(
    "GetContentModerationRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SortBy": NotRequired[ContentModerationSortByType],
    },
)

GetContentModerationResponseTypeDef = TypedDict(
    "GetContentModerationResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "ModerationLabels": List["ContentModerationDetectionTypeDef"],
        "NextToken": str,
        "ModerationModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFaceDetectionRequestRequestTypeDef = TypedDict(
    "GetFaceDetectionRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetFaceDetectionResponseTypeDef = TypedDict(
    "GetFaceDetectionResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "NextToken": str,
        "Faces": List["FaceDetectionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFaceSearchRequestRequestTypeDef = TypedDict(
    "GetFaceSearchRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SortBy": NotRequired[FaceSearchSortByType],
    },
)

GetFaceSearchResponseTypeDef = TypedDict(
    "GetFaceSearchResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "NextToken": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "Persons": List["PersonMatchTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLabelDetectionRequestRequestTypeDef = TypedDict(
    "GetLabelDetectionRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SortBy": NotRequired[LabelDetectionSortByType],
    },
)

GetLabelDetectionResponseTypeDef = TypedDict(
    "GetLabelDetectionResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "NextToken": str,
        "Labels": List["LabelDetectionTypeDef"],
        "LabelModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPersonTrackingRequestRequestTypeDef = TypedDict(
    "GetPersonTrackingRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SortBy": NotRequired[PersonTrackingSortByType],
    },
)

GetPersonTrackingResponseTypeDef = TypedDict(
    "GetPersonTrackingResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "NextToken": str,
        "Persons": List["PersonDetectionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSegmentDetectionRequestRequestTypeDef = TypedDict(
    "GetSegmentDetectionRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetSegmentDetectionResponseTypeDef = TypedDict(
    "GetSegmentDetectionResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": List["VideoMetadataTypeDef"],
        "AudioMetadata": List["AudioMetadataTypeDef"],
        "NextToken": str,
        "Segments": List["SegmentDetectionTypeDef"],
        "SelectedSegmentTypes": List["SegmentTypeInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTextDetectionRequestRequestTypeDef = TypedDict(
    "GetTextDetectionRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetTextDetectionResponseTypeDef = TypedDict(
    "GetTextDetectionResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "TextDetections": List["TextDetectionResultTypeDef"],
        "NextToken": str,
        "TextModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroundTruthManifestTypeDef = TypedDict(
    "GroundTruthManifestTypeDef",
    {
        "S3Object": NotRequired["S3ObjectTypeDef"],
    },
)

HumanLoopActivationOutputTypeDef = TypedDict(
    "HumanLoopActivationOutputTypeDef",
    {
        "HumanLoopArn": NotRequired[str],
        "HumanLoopActivationReasons": NotRequired[List[str]],
        "HumanLoopActivationConditionsEvaluationResults": NotRequired[str],
    },
)

HumanLoopConfigTypeDef = TypedDict(
    "HumanLoopConfigTypeDef",
    {
        "HumanLoopName": str,
        "FlowDefinitionArn": str,
        "DataAttributes": NotRequired["HumanLoopDataAttributesTypeDef"],
    },
)

HumanLoopDataAttributesTypeDef = TypedDict(
    "HumanLoopDataAttributesTypeDef",
    {
        "ContentClassifiers": NotRequired[Sequence[ContentClassifierType]],
    },
)

ImageQualityTypeDef = TypedDict(
    "ImageQualityTypeDef",
    {
        "Brightness": NotRequired[float],
        "Sharpness": NotRequired[float],
    },
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "Bytes": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "S3Object": NotRequired["S3ObjectTypeDef"],
    },
)

IndexFacesRequestRequestTypeDef = TypedDict(
    "IndexFacesRequestRequestTypeDef",
    {
        "CollectionId": str,
        "Image": "ImageTypeDef",
        "ExternalImageId": NotRequired[str],
        "DetectionAttributes": NotRequired[Sequence[AttributeType]],
        "MaxFaces": NotRequired[int],
        "QualityFilter": NotRequired[QualityFilterType],
    },
)

IndexFacesResponseTypeDef = TypedDict(
    "IndexFacesResponseTypeDef",
    {
        "FaceRecords": List["FaceRecordTypeDef"],
        "OrientationCorrection": OrientationCorrectionType,
        "FaceModelVersion": str,
        "UnindexedFaces": List["UnindexedFaceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "BoundingBox": NotRequired["BoundingBoxTypeDef"],
        "Confidence": NotRequired[float],
    },
)

KinesisDataStreamTypeDef = TypedDict(
    "KinesisDataStreamTypeDef",
    {
        "Arn": NotRequired[str],
    },
)

KinesisVideoStreamTypeDef = TypedDict(
    "KinesisVideoStreamTypeDef",
    {
        "Arn": NotRequired[str],
    },
)

KnownGenderTypeDef = TypedDict(
    "KnownGenderTypeDef",
    {
        "Type": NotRequired[KnownGenderTypeType],
    },
)

LabelDetectionTypeDef = TypedDict(
    "LabelDetectionTypeDef",
    {
        "Timestamp": NotRequired[int],
        "Label": NotRequired["LabelTypeDef"],
    },
)

LabelTypeDef = TypedDict(
    "LabelTypeDef",
    {
        "Name": NotRequired[str],
        "Confidence": NotRequired[float],
        "Instances": NotRequired[List["InstanceTypeDef"]],
        "Parents": NotRequired[List["ParentTypeDef"]],
    },
)

LandmarkTypeDef = TypedDict(
    "LandmarkTypeDef",
    {
        "Type": NotRequired[LandmarkTypeType],
        "X": NotRequired[float],
        "Y": NotRequired[float],
    },
)

ListCollectionsRequestRequestTypeDef = TypedDict(
    "ListCollectionsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListCollectionsResponseTypeDef = TypedDict(
    "ListCollectionsResponseTypeDef",
    {
        "CollectionIds": List[str],
        "NextToken": str,
        "FaceModelVersions": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetEntriesRequestRequestTypeDef = TypedDict(
    "ListDatasetEntriesRequestRequestTypeDef",
    {
        "DatasetArn": str,
        "ContainsLabels": NotRequired[Sequence[str]],
        "Labeled": NotRequired[bool],
        "SourceRefContains": NotRequired[str],
        "HasErrors": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDatasetEntriesResponseTypeDef = TypedDict(
    "ListDatasetEntriesResponseTypeDef",
    {
        "DatasetEntries": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetLabelsRequestRequestTypeDef = TypedDict(
    "ListDatasetLabelsRequestRequestTypeDef",
    {
        "DatasetArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDatasetLabelsResponseTypeDef = TypedDict(
    "ListDatasetLabelsResponseTypeDef",
    {
        "DatasetLabelDescriptions": List["DatasetLabelDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFacesRequestRequestTypeDef = TypedDict(
    "ListFacesRequestRequestTypeDef",
    {
        "CollectionId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListFacesResponseTypeDef = TypedDict(
    "ListFacesResponseTypeDef",
    {
        "Faces": List["FaceTypeDef"],
        "NextToken": str,
        "FaceModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamProcessorsRequestRequestTypeDef = TypedDict(
    "ListStreamProcessorsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListStreamProcessorsResponseTypeDef = TypedDict(
    "ListStreamProcessorsResponseTypeDef",
    {
        "NextToken": str,
        "StreamProcessors": List["StreamProcessorTypeDef"],
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
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModerationLabelTypeDef = TypedDict(
    "ModerationLabelTypeDef",
    {
        "Confidence": NotRequired[float],
        "Name": NotRequired[str],
        "ParentName": NotRequired[str],
    },
)

MouthOpenTypeDef = TypedDict(
    "MouthOpenTypeDef",
    {
        "Value": NotRequired[bool],
        "Confidence": NotRequired[float],
    },
)

MustacheTypeDef = TypedDict(
    "MustacheTypeDef",
    {
        "Value": NotRequired[bool],
        "Confidence": NotRequired[float],
    },
)

NotificationChannelTypeDef = TypedDict(
    "NotificationChannelTypeDef",
    {
        "SNSTopicArn": str,
        "RoleArn": str,
    },
)

OutputConfigTypeDef = TypedDict(
    "OutputConfigTypeDef",
    {
        "S3Bucket": NotRequired[str],
        "S3KeyPrefix": NotRequired[str],
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

ParentTypeDef = TypedDict(
    "ParentTypeDef",
    {
        "Name": NotRequired[str],
    },
)

PersonDetailTypeDef = TypedDict(
    "PersonDetailTypeDef",
    {
        "Index": NotRequired[int],
        "BoundingBox": NotRequired["BoundingBoxTypeDef"],
        "Face": NotRequired["FaceDetailTypeDef"],
    },
)

PersonDetectionTypeDef = TypedDict(
    "PersonDetectionTypeDef",
    {
        "Timestamp": NotRequired[int],
        "Person": NotRequired["PersonDetailTypeDef"],
    },
)

PersonMatchTypeDef = TypedDict(
    "PersonMatchTypeDef",
    {
        "Timestamp": NotRequired[int],
        "Person": NotRequired["PersonDetailTypeDef"],
        "FaceMatches": NotRequired[List["FaceMatchTypeDef"]],
    },
)

PointTypeDef = TypedDict(
    "PointTypeDef",
    {
        "X": NotRequired[float],
        "Y": NotRequired[float],
    },
)

PoseTypeDef = TypedDict(
    "PoseTypeDef",
    {
        "Roll": NotRequired[float],
        "Yaw": NotRequired[float],
        "Pitch": NotRequired[float],
    },
)

ProjectDescriptionTypeDef = TypedDict(
    "ProjectDescriptionTypeDef",
    {
        "ProjectArn": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
        "Status": NotRequired[ProjectStatusType],
        "Datasets": NotRequired[List["DatasetMetadataTypeDef"]],
    },
)

ProjectVersionDescriptionTypeDef = TypedDict(
    "ProjectVersionDescriptionTypeDef",
    {
        "ProjectVersionArn": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
        "MinInferenceUnits": NotRequired[int],
        "Status": NotRequired[ProjectVersionStatusType],
        "StatusMessage": NotRequired[str],
        "BillableTrainingTimeInSeconds": NotRequired[int],
        "TrainingEndTimestamp": NotRequired[datetime],
        "OutputConfig": NotRequired["OutputConfigTypeDef"],
        "TrainingDataResult": NotRequired["TrainingDataResultTypeDef"],
        "TestingDataResult": NotRequired["TestingDataResultTypeDef"],
        "EvaluationResult": NotRequired["EvaluationResultTypeDef"],
        "ManifestSummary": NotRequired["GroundTruthManifestTypeDef"],
        "KmsKeyId": NotRequired[str],
    },
)

ProtectiveEquipmentBodyPartTypeDef = TypedDict(
    "ProtectiveEquipmentBodyPartTypeDef",
    {
        "Name": NotRequired[BodyPartType],
        "Confidence": NotRequired[float],
        "EquipmentDetections": NotRequired[List["EquipmentDetectionTypeDef"]],
    },
)

ProtectiveEquipmentPersonTypeDef = TypedDict(
    "ProtectiveEquipmentPersonTypeDef",
    {
        "BodyParts": NotRequired[List["ProtectiveEquipmentBodyPartTypeDef"]],
        "BoundingBox": NotRequired["BoundingBoxTypeDef"],
        "Confidence": NotRequired[float],
        "Id": NotRequired[int],
    },
)

ProtectiveEquipmentSummarizationAttributesTypeDef = TypedDict(
    "ProtectiveEquipmentSummarizationAttributesTypeDef",
    {
        "MinConfidence": float,
        "RequiredEquipmentTypes": Sequence[ProtectiveEquipmentTypeType],
    },
)

ProtectiveEquipmentSummaryTypeDef = TypedDict(
    "ProtectiveEquipmentSummaryTypeDef",
    {
        "PersonsWithRequiredEquipment": NotRequired[List[int]],
        "PersonsWithoutRequiredEquipment": NotRequired[List[int]],
        "PersonsIndeterminate": NotRequired[List[int]],
    },
)

RecognizeCelebritiesRequestRequestTypeDef = TypedDict(
    "RecognizeCelebritiesRequestRequestTypeDef",
    {
        "Image": "ImageTypeDef",
    },
)

RecognizeCelebritiesResponseTypeDef = TypedDict(
    "RecognizeCelebritiesResponseTypeDef",
    {
        "CelebrityFaces": List["CelebrityTypeDef"],
        "UnrecognizedFaces": List["ComparedFaceTypeDef"],
        "OrientationCorrection": OrientationCorrectionType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegionOfInterestTypeDef = TypedDict(
    "RegionOfInterestTypeDef",
    {
        "BoundingBox": NotRequired["BoundingBoxTypeDef"],
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

S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "Bucket": NotRequired[str],
        "Name": NotRequired[str],
        "Version": NotRequired[str],
    },
)

SearchFacesByImageRequestRequestTypeDef = TypedDict(
    "SearchFacesByImageRequestRequestTypeDef",
    {
        "CollectionId": str,
        "Image": "ImageTypeDef",
        "MaxFaces": NotRequired[int],
        "FaceMatchThreshold": NotRequired[float],
        "QualityFilter": NotRequired[QualityFilterType],
    },
)

SearchFacesByImageResponseTypeDef = TypedDict(
    "SearchFacesByImageResponseTypeDef",
    {
        "SearchedFaceBoundingBox": "BoundingBoxTypeDef",
        "SearchedFaceConfidence": float,
        "FaceMatches": List["FaceMatchTypeDef"],
        "FaceModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchFacesRequestRequestTypeDef = TypedDict(
    "SearchFacesRequestRequestTypeDef",
    {
        "CollectionId": str,
        "FaceId": str,
        "MaxFaces": NotRequired[int],
        "FaceMatchThreshold": NotRequired[float],
    },
)

SearchFacesResponseTypeDef = TypedDict(
    "SearchFacesResponseTypeDef",
    {
        "SearchedFaceId": str,
        "FaceMatches": List["FaceMatchTypeDef"],
        "FaceModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SegmentDetectionTypeDef = TypedDict(
    "SegmentDetectionTypeDef",
    {
        "Type": NotRequired[SegmentTypeType],
        "StartTimestampMillis": NotRequired[int],
        "EndTimestampMillis": NotRequired[int],
        "DurationMillis": NotRequired[int],
        "StartTimecodeSMPTE": NotRequired[str],
        "EndTimecodeSMPTE": NotRequired[str],
        "DurationSMPTE": NotRequired[str],
        "TechnicalCueSegment": NotRequired["TechnicalCueSegmentTypeDef"],
        "ShotSegment": NotRequired["ShotSegmentTypeDef"],
        "StartFrameNumber": NotRequired[int],
        "EndFrameNumber": NotRequired[int],
        "DurationFrames": NotRequired[int],
    },
)

SegmentTypeInfoTypeDef = TypedDict(
    "SegmentTypeInfoTypeDef",
    {
        "Type": NotRequired[SegmentTypeType],
        "ModelVersion": NotRequired[str],
    },
)

ShotSegmentTypeDef = TypedDict(
    "ShotSegmentTypeDef",
    {
        "Index": NotRequired[int],
        "Confidence": NotRequired[float],
    },
)

SmileTypeDef = TypedDict(
    "SmileTypeDef",
    {
        "Value": NotRequired[bool],
        "Confidence": NotRequired[float],
    },
)

StartCelebrityRecognitionRequestRequestTypeDef = TypedDict(
    "StartCelebrityRecognitionRequestRequestTypeDef",
    {
        "Video": "VideoTypeDef",
        "ClientRequestToken": NotRequired[str],
        "NotificationChannel": NotRequired["NotificationChannelTypeDef"],
        "JobTag": NotRequired[str],
    },
)

StartCelebrityRecognitionResponseTypeDef = TypedDict(
    "StartCelebrityRecognitionResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartContentModerationRequestRequestTypeDef = TypedDict(
    "StartContentModerationRequestRequestTypeDef",
    {
        "Video": "VideoTypeDef",
        "MinConfidence": NotRequired[float],
        "ClientRequestToken": NotRequired[str],
        "NotificationChannel": NotRequired["NotificationChannelTypeDef"],
        "JobTag": NotRequired[str],
    },
)

StartContentModerationResponseTypeDef = TypedDict(
    "StartContentModerationResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartFaceDetectionRequestRequestTypeDef = TypedDict(
    "StartFaceDetectionRequestRequestTypeDef",
    {
        "Video": "VideoTypeDef",
        "ClientRequestToken": NotRequired[str],
        "NotificationChannel": NotRequired["NotificationChannelTypeDef"],
        "FaceAttributes": NotRequired[FaceAttributesType],
        "JobTag": NotRequired[str],
    },
)

StartFaceDetectionResponseTypeDef = TypedDict(
    "StartFaceDetectionResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartFaceSearchRequestRequestTypeDef = TypedDict(
    "StartFaceSearchRequestRequestTypeDef",
    {
        "Video": "VideoTypeDef",
        "CollectionId": str,
        "ClientRequestToken": NotRequired[str],
        "FaceMatchThreshold": NotRequired[float],
        "NotificationChannel": NotRequired["NotificationChannelTypeDef"],
        "JobTag": NotRequired[str],
    },
)

StartFaceSearchResponseTypeDef = TypedDict(
    "StartFaceSearchResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartLabelDetectionRequestRequestTypeDef = TypedDict(
    "StartLabelDetectionRequestRequestTypeDef",
    {
        "Video": "VideoTypeDef",
        "ClientRequestToken": NotRequired[str],
        "MinConfidence": NotRequired[float],
        "NotificationChannel": NotRequired["NotificationChannelTypeDef"],
        "JobTag": NotRequired[str],
    },
)

StartLabelDetectionResponseTypeDef = TypedDict(
    "StartLabelDetectionResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartPersonTrackingRequestRequestTypeDef = TypedDict(
    "StartPersonTrackingRequestRequestTypeDef",
    {
        "Video": "VideoTypeDef",
        "ClientRequestToken": NotRequired[str],
        "NotificationChannel": NotRequired["NotificationChannelTypeDef"],
        "JobTag": NotRequired[str],
    },
)

StartPersonTrackingResponseTypeDef = TypedDict(
    "StartPersonTrackingResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartProjectVersionRequestRequestTypeDef = TypedDict(
    "StartProjectVersionRequestRequestTypeDef",
    {
        "ProjectVersionArn": str,
        "MinInferenceUnits": int,
    },
)

StartProjectVersionResponseTypeDef = TypedDict(
    "StartProjectVersionResponseTypeDef",
    {
        "Status": ProjectVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartSegmentDetectionFiltersTypeDef = TypedDict(
    "StartSegmentDetectionFiltersTypeDef",
    {
        "TechnicalCueFilter": NotRequired["StartTechnicalCueDetectionFilterTypeDef"],
        "ShotFilter": NotRequired["StartShotDetectionFilterTypeDef"],
    },
)

StartSegmentDetectionRequestRequestTypeDef = TypedDict(
    "StartSegmentDetectionRequestRequestTypeDef",
    {
        "Video": "VideoTypeDef",
        "SegmentTypes": Sequence[SegmentTypeType],
        "ClientRequestToken": NotRequired[str],
        "NotificationChannel": NotRequired["NotificationChannelTypeDef"],
        "JobTag": NotRequired[str],
        "Filters": NotRequired["StartSegmentDetectionFiltersTypeDef"],
    },
)

StartSegmentDetectionResponseTypeDef = TypedDict(
    "StartSegmentDetectionResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartShotDetectionFilterTypeDef = TypedDict(
    "StartShotDetectionFilterTypeDef",
    {
        "MinSegmentConfidence": NotRequired[float],
    },
)

StartStreamProcessorRequestRequestTypeDef = TypedDict(
    "StartStreamProcessorRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StartTechnicalCueDetectionFilterTypeDef = TypedDict(
    "StartTechnicalCueDetectionFilterTypeDef",
    {
        "MinSegmentConfidence": NotRequired[float],
        "BlackFrame": NotRequired["BlackFrameTypeDef"],
    },
)

StartTextDetectionFiltersTypeDef = TypedDict(
    "StartTextDetectionFiltersTypeDef",
    {
        "WordFilter": NotRequired["DetectionFilterTypeDef"],
        "RegionsOfInterest": NotRequired[Sequence["RegionOfInterestTypeDef"]],
    },
)

StartTextDetectionRequestRequestTypeDef = TypedDict(
    "StartTextDetectionRequestRequestTypeDef",
    {
        "Video": "VideoTypeDef",
        "ClientRequestToken": NotRequired[str],
        "NotificationChannel": NotRequired["NotificationChannelTypeDef"],
        "JobTag": NotRequired[str],
        "Filters": NotRequired["StartTextDetectionFiltersTypeDef"],
    },
)

StartTextDetectionResponseTypeDef = TypedDict(
    "StartTextDetectionResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopProjectVersionRequestRequestTypeDef = TypedDict(
    "StopProjectVersionRequestRequestTypeDef",
    {
        "ProjectVersionArn": str,
    },
)

StopProjectVersionResponseTypeDef = TypedDict(
    "StopProjectVersionResponseTypeDef",
    {
        "Status": ProjectVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopStreamProcessorRequestRequestTypeDef = TypedDict(
    "StopStreamProcessorRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StreamProcessorInputTypeDef = TypedDict(
    "StreamProcessorInputTypeDef",
    {
        "KinesisVideoStream": NotRequired["KinesisVideoStreamTypeDef"],
    },
)

StreamProcessorOutputTypeDef = TypedDict(
    "StreamProcessorOutputTypeDef",
    {
        "KinesisDataStream": NotRequired["KinesisDataStreamTypeDef"],
    },
)

StreamProcessorSettingsTypeDef = TypedDict(
    "StreamProcessorSettingsTypeDef",
    {
        "FaceSearch": NotRequired["FaceSearchSettingsTypeDef"],
    },
)

StreamProcessorTypeDef = TypedDict(
    "StreamProcessorTypeDef",
    {
        "Name": NotRequired[str],
        "Status": NotRequired[StreamProcessorStatusType],
    },
)

SummaryTypeDef = TypedDict(
    "SummaryTypeDef",
    {
        "S3Object": NotRequired["S3ObjectTypeDef"],
    },
)

SunglassesTypeDef = TypedDict(
    "SunglassesTypeDef",
    {
        "Value": NotRequired[bool],
        "Confidence": NotRequired[float],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

TechnicalCueSegmentTypeDef = TypedDict(
    "TechnicalCueSegmentTypeDef",
    {
        "Type": NotRequired[TechnicalCueTypeType],
        "Confidence": NotRequired[float],
    },
)

TestingDataResultTypeDef = TypedDict(
    "TestingDataResultTypeDef",
    {
        "Input": NotRequired["TestingDataTypeDef"],
        "Output": NotRequired["TestingDataTypeDef"],
        "Validation": NotRequired["ValidationDataTypeDef"],
    },
)

TestingDataTypeDef = TypedDict(
    "TestingDataTypeDef",
    {
        "Assets": NotRequired[Sequence["AssetTypeDef"]],
        "AutoCreate": NotRequired[bool],
    },
)

TextDetectionResultTypeDef = TypedDict(
    "TextDetectionResultTypeDef",
    {
        "Timestamp": NotRequired[int],
        "TextDetection": NotRequired["TextDetectionTypeDef"],
    },
)

TextDetectionTypeDef = TypedDict(
    "TextDetectionTypeDef",
    {
        "DetectedText": NotRequired[str],
        "Type": NotRequired[TextTypesType],
        "Id": NotRequired[int],
        "ParentId": NotRequired[int],
        "Confidence": NotRequired[float],
        "Geometry": NotRequired["GeometryTypeDef"],
    },
)

TrainingDataResultTypeDef = TypedDict(
    "TrainingDataResultTypeDef",
    {
        "Input": NotRequired["TrainingDataTypeDef"],
        "Output": NotRequired["TrainingDataTypeDef"],
        "Validation": NotRequired["ValidationDataTypeDef"],
    },
)

TrainingDataTypeDef = TypedDict(
    "TrainingDataTypeDef",
    {
        "Assets": NotRequired[Sequence["AssetTypeDef"]],
    },
)

UnindexedFaceTypeDef = TypedDict(
    "UnindexedFaceTypeDef",
    {
        "Reasons": NotRequired[List[ReasonType]],
        "FaceDetail": NotRequired["FaceDetailTypeDef"],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateDatasetEntriesRequestRequestTypeDef = TypedDict(
    "UpdateDatasetEntriesRequestRequestTypeDef",
    {
        "DatasetArn": str,
        "Changes": "DatasetChangesTypeDef",
    },
)

ValidationDataTypeDef = TypedDict(
    "ValidationDataTypeDef",
    {
        "Assets": NotRequired[List["AssetTypeDef"]],
    },
)

VideoMetadataTypeDef = TypedDict(
    "VideoMetadataTypeDef",
    {
        "Codec": NotRequired[str],
        "DurationMillis": NotRequired[int],
        "Format": NotRequired[str],
        "FrameRate": NotRequired[float],
        "FrameHeight": NotRequired[int],
        "FrameWidth": NotRequired[int],
        "ColorRange": NotRequired[VideoColorRangeType],
    },
)

VideoTypeDef = TypedDict(
    "VideoTypeDef",
    {
        "S3Object": NotRequired["S3ObjectTypeDef"],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
