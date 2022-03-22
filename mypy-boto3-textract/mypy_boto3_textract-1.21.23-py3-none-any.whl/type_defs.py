"""
Type annotations for textract service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/type_defs.html)

Usage::

    ```python
    from mypy_boto3_textract.type_defs import AnalyzeDocumentRequestRequestTypeDef

    data: AnalyzeDocumentRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import IO, Dict, List, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    BlockTypeType,
    ContentClassifierType,
    EntityTypeType,
    FeatureTypeType,
    JobStatusType,
    RelationshipTypeType,
    SelectionStatusType,
    TextTypeType,
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
    "AnalyzeDocumentRequestRequestTypeDef",
    "AnalyzeDocumentResponseTypeDef",
    "AnalyzeExpenseRequestRequestTypeDef",
    "AnalyzeExpenseResponseTypeDef",
    "AnalyzeIDDetectionsTypeDef",
    "AnalyzeIDRequestRequestTypeDef",
    "AnalyzeIDResponseTypeDef",
    "BlockTypeDef",
    "BoundingBoxTypeDef",
    "DetectDocumentTextRequestRequestTypeDef",
    "DetectDocumentTextResponseTypeDef",
    "DocumentLocationTypeDef",
    "DocumentMetadataTypeDef",
    "DocumentTypeDef",
    "ExpenseDetectionTypeDef",
    "ExpenseDocumentTypeDef",
    "ExpenseFieldTypeDef",
    "ExpenseTypeTypeDef",
    "GeometryTypeDef",
    "GetDocumentAnalysisRequestRequestTypeDef",
    "GetDocumentAnalysisResponseTypeDef",
    "GetDocumentTextDetectionRequestRequestTypeDef",
    "GetDocumentTextDetectionResponseTypeDef",
    "GetExpenseAnalysisRequestRequestTypeDef",
    "GetExpenseAnalysisResponseTypeDef",
    "HumanLoopActivationOutputTypeDef",
    "HumanLoopConfigTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "IdentityDocumentFieldTypeDef",
    "IdentityDocumentTypeDef",
    "LineItemFieldsTypeDef",
    "LineItemGroupTypeDef",
    "NormalizedValueTypeDef",
    "NotificationChannelTypeDef",
    "OutputConfigTypeDef",
    "PointTypeDef",
    "RelationshipTypeDef",
    "ResponseMetadataTypeDef",
    "S3ObjectTypeDef",
    "StartDocumentAnalysisRequestRequestTypeDef",
    "StartDocumentAnalysisResponseTypeDef",
    "StartDocumentTextDetectionRequestRequestTypeDef",
    "StartDocumentTextDetectionResponseTypeDef",
    "StartExpenseAnalysisRequestRequestTypeDef",
    "StartExpenseAnalysisResponseTypeDef",
    "WarningTypeDef",
)

AnalyzeDocumentRequestRequestTypeDef = TypedDict(
    "AnalyzeDocumentRequestRequestTypeDef",
    {
        "Document": "DocumentTypeDef",
        "FeatureTypes": Sequence[FeatureTypeType],
        "HumanLoopConfig": NotRequired["HumanLoopConfigTypeDef"],
    },
)

AnalyzeDocumentResponseTypeDef = TypedDict(
    "AnalyzeDocumentResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "Blocks": List["BlockTypeDef"],
        "HumanLoopActivationOutput": "HumanLoopActivationOutputTypeDef",
        "AnalyzeDocumentModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AnalyzeExpenseRequestRequestTypeDef = TypedDict(
    "AnalyzeExpenseRequestRequestTypeDef",
    {
        "Document": "DocumentTypeDef",
    },
)

AnalyzeExpenseResponseTypeDef = TypedDict(
    "AnalyzeExpenseResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "ExpenseDocuments": List["ExpenseDocumentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AnalyzeIDDetectionsTypeDef = TypedDict(
    "AnalyzeIDDetectionsTypeDef",
    {
        "Text": str,
        "NormalizedValue": NotRequired["NormalizedValueTypeDef"],
        "Confidence": NotRequired[float],
    },
)

AnalyzeIDRequestRequestTypeDef = TypedDict(
    "AnalyzeIDRequestRequestTypeDef",
    {
        "DocumentPages": Sequence["DocumentTypeDef"],
    },
)

AnalyzeIDResponseTypeDef = TypedDict(
    "AnalyzeIDResponseTypeDef",
    {
        "IdentityDocuments": List["IdentityDocumentTypeDef"],
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "AnalyzeIDModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BlockTypeDef = TypedDict(
    "BlockTypeDef",
    {
        "BlockType": NotRequired[BlockTypeType],
        "Confidence": NotRequired[float],
        "Text": NotRequired[str],
        "TextType": NotRequired[TextTypeType],
        "RowIndex": NotRequired[int],
        "ColumnIndex": NotRequired[int],
        "RowSpan": NotRequired[int],
        "ColumnSpan": NotRequired[int],
        "Geometry": NotRequired["GeometryTypeDef"],
        "Id": NotRequired[str],
        "Relationships": NotRequired[List["RelationshipTypeDef"]],
        "EntityTypes": NotRequired[List[EntityTypeType]],
        "SelectionStatus": NotRequired[SelectionStatusType],
        "Page": NotRequired[int],
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

DetectDocumentTextRequestRequestTypeDef = TypedDict(
    "DetectDocumentTextRequestRequestTypeDef",
    {
        "Document": "DocumentTypeDef",
    },
)

DetectDocumentTextResponseTypeDef = TypedDict(
    "DetectDocumentTextResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "Blocks": List["BlockTypeDef"],
        "DetectDocumentTextModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DocumentLocationTypeDef = TypedDict(
    "DocumentLocationTypeDef",
    {
        "S3Object": NotRequired["S3ObjectTypeDef"],
    },
)

DocumentMetadataTypeDef = TypedDict(
    "DocumentMetadataTypeDef",
    {
        "Pages": NotRequired[int],
    },
)

DocumentTypeDef = TypedDict(
    "DocumentTypeDef",
    {
        "Bytes": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "S3Object": NotRequired["S3ObjectTypeDef"],
    },
)

ExpenseDetectionTypeDef = TypedDict(
    "ExpenseDetectionTypeDef",
    {
        "Text": NotRequired[str],
        "Geometry": NotRequired["GeometryTypeDef"],
        "Confidence": NotRequired[float],
    },
)

ExpenseDocumentTypeDef = TypedDict(
    "ExpenseDocumentTypeDef",
    {
        "ExpenseIndex": NotRequired[int],
        "SummaryFields": NotRequired[List["ExpenseFieldTypeDef"]],
        "LineItemGroups": NotRequired[List["LineItemGroupTypeDef"]],
    },
)

ExpenseFieldTypeDef = TypedDict(
    "ExpenseFieldTypeDef",
    {
        "Type": NotRequired["ExpenseTypeTypeDef"],
        "LabelDetection": NotRequired["ExpenseDetectionTypeDef"],
        "ValueDetection": NotRequired["ExpenseDetectionTypeDef"],
        "PageNumber": NotRequired[int],
    },
)

ExpenseTypeTypeDef = TypedDict(
    "ExpenseTypeTypeDef",
    {
        "Text": NotRequired[str],
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

GetDocumentAnalysisRequestRequestTypeDef = TypedDict(
    "GetDocumentAnalysisRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetDocumentAnalysisResponseTypeDef = TypedDict(
    "GetDocumentAnalysisResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "JobStatus": JobStatusType,
        "NextToken": str,
        "Blocks": List["BlockTypeDef"],
        "Warnings": List["WarningTypeDef"],
        "StatusMessage": str,
        "AnalyzeDocumentModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDocumentTextDetectionRequestRequestTypeDef = TypedDict(
    "GetDocumentTextDetectionRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetDocumentTextDetectionResponseTypeDef = TypedDict(
    "GetDocumentTextDetectionResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "JobStatus": JobStatusType,
        "NextToken": str,
        "Blocks": List["BlockTypeDef"],
        "Warnings": List["WarningTypeDef"],
        "StatusMessage": str,
        "DetectDocumentTextModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExpenseAnalysisRequestRequestTypeDef = TypedDict(
    "GetExpenseAnalysisRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetExpenseAnalysisResponseTypeDef = TypedDict(
    "GetExpenseAnalysisResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "JobStatus": JobStatusType,
        "NextToken": str,
        "ExpenseDocuments": List["ExpenseDocumentTypeDef"],
        "Warnings": List["WarningTypeDef"],
        "StatusMessage": str,
        "AnalyzeExpenseModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

IdentityDocumentFieldTypeDef = TypedDict(
    "IdentityDocumentFieldTypeDef",
    {
        "Type": NotRequired["AnalyzeIDDetectionsTypeDef"],
        "ValueDetection": NotRequired["AnalyzeIDDetectionsTypeDef"],
    },
)

IdentityDocumentTypeDef = TypedDict(
    "IdentityDocumentTypeDef",
    {
        "DocumentIndex": NotRequired[int],
        "IdentityDocumentFields": NotRequired[List["IdentityDocumentFieldTypeDef"]],
    },
)

LineItemFieldsTypeDef = TypedDict(
    "LineItemFieldsTypeDef",
    {
        "LineItemExpenseFields": NotRequired[List["ExpenseFieldTypeDef"]],
    },
)

LineItemGroupTypeDef = TypedDict(
    "LineItemGroupTypeDef",
    {
        "LineItemGroupIndex": NotRequired[int],
        "LineItems": NotRequired[List["LineItemFieldsTypeDef"]],
    },
)

NormalizedValueTypeDef = TypedDict(
    "NormalizedValueTypeDef",
    {
        "Value": NotRequired[str],
        "ValueType": NotRequired[Literal["DATE"]],
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
        "S3Bucket": str,
        "S3Prefix": NotRequired[str],
    },
)

PointTypeDef = TypedDict(
    "PointTypeDef",
    {
        "X": NotRequired[float],
        "Y": NotRequired[float],
    },
)

RelationshipTypeDef = TypedDict(
    "RelationshipTypeDef",
    {
        "Type": NotRequired[RelationshipTypeType],
        "Ids": NotRequired[List[str]],
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

StartDocumentAnalysisRequestRequestTypeDef = TypedDict(
    "StartDocumentAnalysisRequestRequestTypeDef",
    {
        "DocumentLocation": "DocumentLocationTypeDef",
        "FeatureTypes": Sequence[FeatureTypeType],
        "ClientRequestToken": NotRequired[str],
        "JobTag": NotRequired[str],
        "NotificationChannel": NotRequired["NotificationChannelTypeDef"],
        "OutputConfig": NotRequired["OutputConfigTypeDef"],
        "KMSKeyId": NotRequired[str],
    },
)

StartDocumentAnalysisResponseTypeDef = TypedDict(
    "StartDocumentAnalysisResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartDocumentTextDetectionRequestRequestTypeDef = TypedDict(
    "StartDocumentTextDetectionRequestRequestTypeDef",
    {
        "DocumentLocation": "DocumentLocationTypeDef",
        "ClientRequestToken": NotRequired[str],
        "JobTag": NotRequired[str],
        "NotificationChannel": NotRequired["NotificationChannelTypeDef"],
        "OutputConfig": NotRequired["OutputConfigTypeDef"],
        "KMSKeyId": NotRequired[str],
    },
)

StartDocumentTextDetectionResponseTypeDef = TypedDict(
    "StartDocumentTextDetectionResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartExpenseAnalysisRequestRequestTypeDef = TypedDict(
    "StartExpenseAnalysisRequestRequestTypeDef",
    {
        "DocumentLocation": "DocumentLocationTypeDef",
        "ClientRequestToken": NotRequired[str],
        "JobTag": NotRequired[str],
        "NotificationChannel": NotRequired["NotificationChannelTypeDef"],
        "OutputConfig": NotRequired["OutputConfigTypeDef"],
        "KMSKeyId": NotRequired[str],
    },
)

StartExpenseAnalysisResponseTypeDef = TypedDict(
    "StartExpenseAnalysisResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WarningTypeDef = TypedDict(
    "WarningTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "Pages": NotRequired[List[int]],
    },
)
