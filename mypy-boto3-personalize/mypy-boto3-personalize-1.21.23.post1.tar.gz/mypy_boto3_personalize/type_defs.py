"""
Type annotations for personalize service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/type_defs.html)

Usage::

    ```python
    from mypy_boto3_personalize.type_defs import AlgorithmImageTypeDef

    data: AlgorithmImageTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import DomainType, IngestionModeType, ObjectiveSensitivityType, TrainingModeType

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AlgorithmImageTypeDef",
    "AlgorithmTypeDef",
    "AutoMLConfigTypeDef",
    "AutoMLResultTypeDef",
    "BatchInferenceJobConfigTypeDef",
    "BatchInferenceJobInputTypeDef",
    "BatchInferenceJobOutputTypeDef",
    "BatchInferenceJobSummaryTypeDef",
    "BatchInferenceJobTypeDef",
    "BatchSegmentJobInputTypeDef",
    "BatchSegmentJobOutputTypeDef",
    "BatchSegmentJobSummaryTypeDef",
    "BatchSegmentJobTypeDef",
    "CampaignConfigTypeDef",
    "CampaignSummaryTypeDef",
    "CampaignTypeDef",
    "CampaignUpdateSummaryTypeDef",
    "CategoricalHyperParameterRangeTypeDef",
    "ContinuousHyperParameterRangeTypeDef",
    "CreateBatchInferenceJobRequestRequestTypeDef",
    "CreateBatchInferenceJobResponseTypeDef",
    "CreateBatchSegmentJobRequestRequestTypeDef",
    "CreateBatchSegmentJobResponseTypeDef",
    "CreateCampaignRequestRequestTypeDef",
    "CreateCampaignResponseTypeDef",
    "CreateDatasetExportJobRequestRequestTypeDef",
    "CreateDatasetExportJobResponseTypeDef",
    "CreateDatasetGroupRequestRequestTypeDef",
    "CreateDatasetGroupResponseTypeDef",
    "CreateDatasetImportJobRequestRequestTypeDef",
    "CreateDatasetImportJobResponseTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateEventTrackerRequestRequestTypeDef",
    "CreateEventTrackerResponseTypeDef",
    "CreateFilterRequestRequestTypeDef",
    "CreateFilterResponseTypeDef",
    "CreateRecommenderRequestRequestTypeDef",
    "CreateRecommenderResponseTypeDef",
    "CreateSchemaRequestRequestTypeDef",
    "CreateSchemaResponseTypeDef",
    "CreateSolutionRequestRequestTypeDef",
    "CreateSolutionResponseTypeDef",
    "CreateSolutionVersionRequestRequestTypeDef",
    "CreateSolutionVersionResponseTypeDef",
    "DataSourceTypeDef",
    "DatasetExportJobOutputTypeDef",
    "DatasetExportJobSummaryTypeDef",
    "DatasetExportJobTypeDef",
    "DatasetGroupSummaryTypeDef",
    "DatasetGroupTypeDef",
    "DatasetImportJobSummaryTypeDef",
    "DatasetImportJobTypeDef",
    "DatasetSchemaSummaryTypeDef",
    "DatasetSchemaTypeDef",
    "DatasetSummaryTypeDef",
    "DatasetTypeDef",
    "DefaultCategoricalHyperParameterRangeTypeDef",
    "DefaultContinuousHyperParameterRangeTypeDef",
    "DefaultHyperParameterRangesTypeDef",
    "DefaultIntegerHyperParameterRangeTypeDef",
    "DeleteCampaignRequestRequestTypeDef",
    "DeleteDatasetGroupRequestRequestTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteEventTrackerRequestRequestTypeDef",
    "DeleteFilterRequestRequestTypeDef",
    "DeleteRecommenderRequestRequestTypeDef",
    "DeleteSchemaRequestRequestTypeDef",
    "DeleteSolutionRequestRequestTypeDef",
    "DescribeAlgorithmRequestRequestTypeDef",
    "DescribeAlgorithmResponseTypeDef",
    "DescribeBatchInferenceJobRequestRequestTypeDef",
    "DescribeBatchInferenceJobResponseTypeDef",
    "DescribeBatchSegmentJobRequestRequestTypeDef",
    "DescribeBatchSegmentJobResponseTypeDef",
    "DescribeCampaignRequestRequestTypeDef",
    "DescribeCampaignResponseTypeDef",
    "DescribeDatasetExportJobRequestRequestTypeDef",
    "DescribeDatasetExportJobResponseTypeDef",
    "DescribeDatasetGroupRequestRequestTypeDef",
    "DescribeDatasetGroupResponseTypeDef",
    "DescribeDatasetImportJobRequestRequestTypeDef",
    "DescribeDatasetImportJobResponseTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeEventTrackerRequestRequestTypeDef",
    "DescribeEventTrackerResponseTypeDef",
    "DescribeFeatureTransformationRequestRequestTypeDef",
    "DescribeFeatureTransformationResponseTypeDef",
    "DescribeFilterRequestRequestTypeDef",
    "DescribeFilterResponseTypeDef",
    "DescribeRecipeRequestRequestTypeDef",
    "DescribeRecipeResponseTypeDef",
    "DescribeRecommenderRequestRequestTypeDef",
    "DescribeRecommenderResponseTypeDef",
    "DescribeSchemaRequestRequestTypeDef",
    "DescribeSchemaResponseTypeDef",
    "DescribeSolutionRequestRequestTypeDef",
    "DescribeSolutionResponseTypeDef",
    "DescribeSolutionVersionRequestRequestTypeDef",
    "DescribeSolutionVersionResponseTypeDef",
    "EventTrackerSummaryTypeDef",
    "EventTrackerTypeDef",
    "FeatureTransformationTypeDef",
    "FilterSummaryTypeDef",
    "FilterTypeDef",
    "GetSolutionMetricsRequestRequestTypeDef",
    "GetSolutionMetricsResponseTypeDef",
    "HPOConfigTypeDef",
    "HPOObjectiveTypeDef",
    "HPOResourceConfigTypeDef",
    "HyperParameterRangesTypeDef",
    "IntegerHyperParameterRangeTypeDef",
    "ListBatchInferenceJobsRequestRequestTypeDef",
    "ListBatchInferenceJobsResponseTypeDef",
    "ListBatchSegmentJobsRequestRequestTypeDef",
    "ListBatchSegmentJobsResponseTypeDef",
    "ListCampaignsRequestRequestTypeDef",
    "ListCampaignsResponseTypeDef",
    "ListDatasetExportJobsRequestRequestTypeDef",
    "ListDatasetExportJobsResponseTypeDef",
    "ListDatasetGroupsRequestRequestTypeDef",
    "ListDatasetGroupsResponseTypeDef",
    "ListDatasetImportJobsRequestRequestTypeDef",
    "ListDatasetImportJobsResponseTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListEventTrackersRequestRequestTypeDef",
    "ListEventTrackersResponseTypeDef",
    "ListFiltersRequestRequestTypeDef",
    "ListFiltersResponseTypeDef",
    "ListRecipesRequestRequestTypeDef",
    "ListRecipesResponseTypeDef",
    "ListRecommendersRequestRequestTypeDef",
    "ListRecommendersResponseTypeDef",
    "ListSchemasRequestRequestTypeDef",
    "ListSchemasResponseTypeDef",
    "ListSolutionVersionsRequestRequestTypeDef",
    "ListSolutionVersionsResponseTypeDef",
    "ListSolutionsRequestRequestTypeDef",
    "ListSolutionsResponseTypeDef",
    "OptimizationObjectiveTypeDef",
    "PaginatorConfigTypeDef",
    "RecipeSummaryTypeDef",
    "RecipeTypeDef",
    "RecommenderConfigTypeDef",
    "RecommenderSummaryTypeDef",
    "RecommenderTypeDef",
    "RecommenderUpdateSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "S3DataConfigTypeDef",
    "SolutionConfigTypeDef",
    "SolutionSummaryTypeDef",
    "SolutionTypeDef",
    "SolutionVersionSummaryTypeDef",
    "SolutionVersionTypeDef",
    "StopSolutionVersionCreationRequestRequestTypeDef",
    "TunedHPOParamsTypeDef",
    "UpdateCampaignRequestRequestTypeDef",
    "UpdateCampaignResponseTypeDef",
    "UpdateRecommenderRequestRequestTypeDef",
    "UpdateRecommenderResponseTypeDef",
)

AlgorithmImageTypeDef = TypedDict(
    "AlgorithmImageTypeDef",
    {
        "dockerURI": str,
        "name": NotRequired[str],
    },
)

AlgorithmTypeDef = TypedDict(
    "AlgorithmTypeDef",
    {
        "name": NotRequired[str],
        "algorithmArn": NotRequired[str],
        "algorithmImage": NotRequired["AlgorithmImageTypeDef"],
        "defaultHyperParameters": NotRequired[Dict[str, str]],
        "defaultHyperParameterRanges": NotRequired["DefaultHyperParameterRangesTypeDef"],
        "defaultResourceConfig": NotRequired[Dict[str, str]],
        "trainingInputMode": NotRequired[str],
        "roleArn": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)

AutoMLConfigTypeDef = TypedDict(
    "AutoMLConfigTypeDef",
    {
        "metricName": NotRequired[str],
        "recipeList": NotRequired[Sequence[str]],
    },
)

AutoMLResultTypeDef = TypedDict(
    "AutoMLResultTypeDef",
    {
        "bestRecipeArn": NotRequired[str],
    },
)

BatchInferenceJobConfigTypeDef = TypedDict(
    "BatchInferenceJobConfigTypeDef",
    {
        "itemExplorationConfig": NotRequired[Mapping[str, str]],
    },
)

BatchInferenceJobInputTypeDef = TypedDict(
    "BatchInferenceJobInputTypeDef",
    {
        "s3DataSource": "S3DataConfigTypeDef",
    },
)

BatchInferenceJobOutputTypeDef = TypedDict(
    "BatchInferenceJobOutputTypeDef",
    {
        "s3DataDestination": "S3DataConfigTypeDef",
    },
)

BatchInferenceJobSummaryTypeDef = TypedDict(
    "BatchInferenceJobSummaryTypeDef",
    {
        "batchInferenceJobArn": NotRequired[str],
        "jobName": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
        "solutionVersionArn": NotRequired[str],
    },
)

BatchInferenceJobTypeDef = TypedDict(
    "BatchInferenceJobTypeDef",
    {
        "jobName": NotRequired[str],
        "batchInferenceJobArn": NotRequired[str],
        "filterArn": NotRequired[str],
        "failureReason": NotRequired[str],
        "solutionVersionArn": NotRequired[str],
        "numResults": NotRequired[int],
        "jobInput": NotRequired["BatchInferenceJobInputTypeDef"],
        "jobOutput": NotRequired["BatchInferenceJobOutputTypeDef"],
        "batchInferenceJobConfig": NotRequired["BatchInferenceJobConfigTypeDef"],
        "roleArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)

BatchSegmentJobInputTypeDef = TypedDict(
    "BatchSegmentJobInputTypeDef",
    {
        "s3DataSource": "S3DataConfigTypeDef",
    },
)

BatchSegmentJobOutputTypeDef = TypedDict(
    "BatchSegmentJobOutputTypeDef",
    {
        "s3DataDestination": "S3DataConfigTypeDef",
    },
)

BatchSegmentJobSummaryTypeDef = TypedDict(
    "BatchSegmentJobSummaryTypeDef",
    {
        "batchSegmentJobArn": NotRequired[str],
        "jobName": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
        "solutionVersionArn": NotRequired[str],
    },
)

BatchSegmentJobTypeDef = TypedDict(
    "BatchSegmentJobTypeDef",
    {
        "jobName": NotRequired[str],
        "batchSegmentJobArn": NotRequired[str],
        "filterArn": NotRequired[str],
        "failureReason": NotRequired[str],
        "solutionVersionArn": NotRequired[str],
        "numResults": NotRequired[int],
        "jobInput": NotRequired["BatchSegmentJobInputTypeDef"],
        "jobOutput": NotRequired["BatchSegmentJobOutputTypeDef"],
        "roleArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)

CampaignConfigTypeDef = TypedDict(
    "CampaignConfigTypeDef",
    {
        "itemExplorationConfig": NotRequired[Mapping[str, str]],
    },
)

CampaignSummaryTypeDef = TypedDict(
    "CampaignSummaryTypeDef",
    {
        "name": NotRequired[str],
        "campaignArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
    },
)

CampaignTypeDef = TypedDict(
    "CampaignTypeDef",
    {
        "name": NotRequired[str],
        "campaignArn": NotRequired[str],
        "solutionVersionArn": NotRequired[str],
        "minProvisionedTPS": NotRequired[int],
        "campaignConfig": NotRequired["CampaignConfigTypeDef"],
        "status": NotRequired[str],
        "failureReason": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "latestCampaignUpdate": NotRequired["CampaignUpdateSummaryTypeDef"],
    },
)

CampaignUpdateSummaryTypeDef = TypedDict(
    "CampaignUpdateSummaryTypeDef",
    {
        "solutionVersionArn": NotRequired[str],
        "minProvisionedTPS": NotRequired[int],
        "campaignConfig": NotRequired["CampaignConfigTypeDef"],
        "status": NotRequired[str],
        "failureReason": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)

CategoricalHyperParameterRangeTypeDef = TypedDict(
    "CategoricalHyperParameterRangeTypeDef",
    {
        "name": NotRequired[str],
        "values": NotRequired[Sequence[str]],
    },
)

ContinuousHyperParameterRangeTypeDef = TypedDict(
    "ContinuousHyperParameterRangeTypeDef",
    {
        "name": NotRequired[str],
        "minValue": NotRequired[float],
        "maxValue": NotRequired[float],
    },
)

CreateBatchInferenceJobRequestRequestTypeDef = TypedDict(
    "CreateBatchInferenceJobRequestRequestTypeDef",
    {
        "jobName": str,
        "solutionVersionArn": str,
        "jobInput": "BatchInferenceJobInputTypeDef",
        "jobOutput": "BatchInferenceJobOutputTypeDef",
        "roleArn": str,
        "filterArn": NotRequired[str],
        "numResults": NotRequired[int],
        "batchInferenceJobConfig": NotRequired["BatchInferenceJobConfigTypeDef"],
    },
)

CreateBatchInferenceJobResponseTypeDef = TypedDict(
    "CreateBatchInferenceJobResponseTypeDef",
    {
        "batchInferenceJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBatchSegmentJobRequestRequestTypeDef = TypedDict(
    "CreateBatchSegmentJobRequestRequestTypeDef",
    {
        "jobName": str,
        "solutionVersionArn": str,
        "jobInput": "BatchSegmentJobInputTypeDef",
        "jobOutput": "BatchSegmentJobOutputTypeDef",
        "roleArn": str,
        "filterArn": NotRequired[str],
        "numResults": NotRequired[int],
    },
)

CreateBatchSegmentJobResponseTypeDef = TypedDict(
    "CreateBatchSegmentJobResponseTypeDef",
    {
        "batchSegmentJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCampaignRequestRequestTypeDef = TypedDict(
    "CreateCampaignRequestRequestTypeDef",
    {
        "name": str,
        "solutionVersionArn": str,
        "minProvisionedTPS": NotRequired[int],
        "campaignConfig": NotRequired["CampaignConfigTypeDef"],
    },
)

CreateCampaignResponseTypeDef = TypedDict(
    "CreateCampaignResponseTypeDef",
    {
        "campaignArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDatasetExportJobRequestRequestTypeDef = TypedDict(
    "CreateDatasetExportJobRequestRequestTypeDef",
    {
        "jobName": str,
        "datasetArn": str,
        "roleArn": str,
        "jobOutput": "DatasetExportJobOutputTypeDef",
        "ingestionMode": NotRequired[IngestionModeType],
    },
)

CreateDatasetExportJobResponseTypeDef = TypedDict(
    "CreateDatasetExportJobResponseTypeDef",
    {
        "datasetExportJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDatasetGroupRequestRequestTypeDef = TypedDict(
    "CreateDatasetGroupRequestRequestTypeDef",
    {
        "name": str,
        "roleArn": NotRequired[str],
        "kmsKeyArn": NotRequired[str],
        "domain": NotRequired[DomainType],
    },
)

CreateDatasetGroupResponseTypeDef = TypedDict(
    "CreateDatasetGroupResponseTypeDef",
    {
        "datasetGroupArn": str,
        "domain": DomainType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDatasetImportJobRequestRequestTypeDef = TypedDict(
    "CreateDatasetImportJobRequestRequestTypeDef",
    {
        "jobName": str,
        "datasetArn": str,
        "dataSource": "DataSourceTypeDef",
        "roleArn": str,
    },
)

CreateDatasetImportJobResponseTypeDef = TypedDict(
    "CreateDatasetImportJobResponseTypeDef",
    {
        "datasetImportJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDatasetRequestRequestTypeDef = TypedDict(
    "CreateDatasetRequestRequestTypeDef",
    {
        "name": str,
        "schemaArn": str,
        "datasetGroupArn": str,
        "datasetType": str,
    },
)

CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "datasetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEventTrackerRequestRequestTypeDef = TypedDict(
    "CreateEventTrackerRequestRequestTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
    },
)

CreateEventTrackerResponseTypeDef = TypedDict(
    "CreateEventTrackerResponseTypeDef",
    {
        "eventTrackerArn": str,
        "trackingId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFilterRequestRequestTypeDef = TypedDict(
    "CreateFilterRequestRequestTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "filterExpression": str,
    },
)

CreateFilterResponseTypeDef = TypedDict(
    "CreateFilterResponseTypeDef",
    {
        "filterArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRecommenderRequestRequestTypeDef = TypedDict(
    "CreateRecommenderRequestRequestTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "recipeArn": str,
        "recommenderConfig": NotRequired["RecommenderConfigTypeDef"],
    },
)

CreateRecommenderResponseTypeDef = TypedDict(
    "CreateRecommenderResponseTypeDef",
    {
        "recommenderArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSchemaRequestRequestTypeDef = TypedDict(
    "CreateSchemaRequestRequestTypeDef",
    {
        "name": str,
        "schema": str,
        "domain": NotRequired[DomainType],
    },
)

CreateSchemaResponseTypeDef = TypedDict(
    "CreateSchemaResponseTypeDef",
    {
        "schemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSolutionRequestRequestTypeDef = TypedDict(
    "CreateSolutionRequestRequestTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "performHPO": NotRequired[bool],
        "performAutoML": NotRequired[bool],
        "recipeArn": NotRequired[str],
        "eventType": NotRequired[str],
        "solutionConfig": NotRequired["SolutionConfigTypeDef"],
    },
)

CreateSolutionResponseTypeDef = TypedDict(
    "CreateSolutionResponseTypeDef",
    {
        "solutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSolutionVersionRequestRequestTypeDef = TypedDict(
    "CreateSolutionVersionRequestRequestTypeDef",
    {
        "solutionArn": str,
        "trainingMode": NotRequired[TrainingModeType],
    },
)

CreateSolutionVersionResponseTypeDef = TypedDict(
    "CreateSolutionVersionResponseTypeDef",
    {
        "solutionVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "dataLocation": NotRequired[str],
    },
)

DatasetExportJobOutputTypeDef = TypedDict(
    "DatasetExportJobOutputTypeDef",
    {
        "s3DataDestination": "S3DataConfigTypeDef",
    },
)

DatasetExportJobSummaryTypeDef = TypedDict(
    "DatasetExportJobSummaryTypeDef",
    {
        "datasetExportJobArn": NotRequired[str],
        "jobName": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
    },
)

DatasetExportJobTypeDef = TypedDict(
    "DatasetExportJobTypeDef",
    {
        "jobName": NotRequired[str],
        "datasetExportJobArn": NotRequired[str],
        "datasetArn": NotRequired[str],
        "ingestionMode": NotRequired[IngestionModeType],
        "roleArn": NotRequired[str],
        "status": NotRequired[str],
        "jobOutput": NotRequired["DatasetExportJobOutputTypeDef"],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
    },
)

DatasetGroupSummaryTypeDef = TypedDict(
    "DatasetGroupSummaryTypeDef",
    {
        "name": NotRequired[str],
        "datasetGroupArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
        "domain": NotRequired[DomainType],
    },
)

DatasetGroupTypeDef = TypedDict(
    "DatasetGroupTypeDef",
    {
        "name": NotRequired[str],
        "datasetGroupArn": NotRequired[str],
        "status": NotRequired[str],
        "roleArn": NotRequired[str],
        "kmsKeyArn": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
        "domain": NotRequired[DomainType],
    },
)

DatasetImportJobSummaryTypeDef = TypedDict(
    "DatasetImportJobSummaryTypeDef",
    {
        "datasetImportJobArn": NotRequired[str],
        "jobName": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
    },
)

DatasetImportJobTypeDef = TypedDict(
    "DatasetImportJobTypeDef",
    {
        "jobName": NotRequired[str],
        "datasetImportJobArn": NotRequired[str],
        "datasetArn": NotRequired[str],
        "dataSource": NotRequired["DataSourceTypeDef"],
        "roleArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
    },
)

DatasetSchemaSummaryTypeDef = TypedDict(
    "DatasetSchemaSummaryTypeDef",
    {
        "name": NotRequired[str],
        "schemaArn": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "domain": NotRequired[DomainType],
    },
)

DatasetSchemaTypeDef = TypedDict(
    "DatasetSchemaTypeDef",
    {
        "name": NotRequired[str],
        "schemaArn": NotRequired[str],
        "schema": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "domain": NotRequired[DomainType],
    },
)

DatasetSummaryTypeDef = TypedDict(
    "DatasetSummaryTypeDef",
    {
        "name": NotRequired[str],
        "datasetArn": NotRequired[str],
        "datasetType": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)

DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "name": NotRequired[str],
        "datasetArn": NotRequired[str],
        "datasetGroupArn": NotRequired[str],
        "datasetType": NotRequired[str],
        "schemaArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)

DefaultCategoricalHyperParameterRangeTypeDef = TypedDict(
    "DefaultCategoricalHyperParameterRangeTypeDef",
    {
        "name": NotRequired[str],
        "values": NotRequired[List[str]],
        "isTunable": NotRequired[bool],
    },
)

DefaultContinuousHyperParameterRangeTypeDef = TypedDict(
    "DefaultContinuousHyperParameterRangeTypeDef",
    {
        "name": NotRequired[str],
        "minValue": NotRequired[float],
        "maxValue": NotRequired[float],
        "isTunable": NotRequired[bool],
    },
)

DefaultHyperParameterRangesTypeDef = TypedDict(
    "DefaultHyperParameterRangesTypeDef",
    {
        "integerHyperParameterRanges": NotRequired[
            List["DefaultIntegerHyperParameterRangeTypeDef"]
        ],
        "continuousHyperParameterRanges": NotRequired[
            List["DefaultContinuousHyperParameterRangeTypeDef"]
        ],
        "categoricalHyperParameterRanges": NotRequired[
            List["DefaultCategoricalHyperParameterRangeTypeDef"]
        ],
    },
)

DefaultIntegerHyperParameterRangeTypeDef = TypedDict(
    "DefaultIntegerHyperParameterRangeTypeDef",
    {
        "name": NotRequired[str],
        "minValue": NotRequired[int],
        "maxValue": NotRequired[int],
        "isTunable": NotRequired[bool],
    },
)

DeleteCampaignRequestRequestTypeDef = TypedDict(
    "DeleteCampaignRequestRequestTypeDef",
    {
        "campaignArn": str,
    },
)

DeleteDatasetGroupRequestRequestTypeDef = TypedDict(
    "DeleteDatasetGroupRequestRequestTypeDef",
    {
        "datasetGroupArn": str,
    },
)

DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "datasetArn": str,
    },
)

DeleteEventTrackerRequestRequestTypeDef = TypedDict(
    "DeleteEventTrackerRequestRequestTypeDef",
    {
        "eventTrackerArn": str,
    },
)

DeleteFilterRequestRequestTypeDef = TypedDict(
    "DeleteFilterRequestRequestTypeDef",
    {
        "filterArn": str,
    },
)

DeleteRecommenderRequestRequestTypeDef = TypedDict(
    "DeleteRecommenderRequestRequestTypeDef",
    {
        "recommenderArn": str,
    },
)

DeleteSchemaRequestRequestTypeDef = TypedDict(
    "DeleteSchemaRequestRequestTypeDef",
    {
        "schemaArn": str,
    },
)

DeleteSolutionRequestRequestTypeDef = TypedDict(
    "DeleteSolutionRequestRequestTypeDef",
    {
        "solutionArn": str,
    },
)

DescribeAlgorithmRequestRequestTypeDef = TypedDict(
    "DescribeAlgorithmRequestRequestTypeDef",
    {
        "algorithmArn": str,
    },
)

DescribeAlgorithmResponseTypeDef = TypedDict(
    "DescribeAlgorithmResponseTypeDef",
    {
        "algorithm": "AlgorithmTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBatchInferenceJobRequestRequestTypeDef = TypedDict(
    "DescribeBatchInferenceJobRequestRequestTypeDef",
    {
        "batchInferenceJobArn": str,
    },
)

DescribeBatchInferenceJobResponseTypeDef = TypedDict(
    "DescribeBatchInferenceJobResponseTypeDef",
    {
        "batchInferenceJob": "BatchInferenceJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBatchSegmentJobRequestRequestTypeDef = TypedDict(
    "DescribeBatchSegmentJobRequestRequestTypeDef",
    {
        "batchSegmentJobArn": str,
    },
)

DescribeBatchSegmentJobResponseTypeDef = TypedDict(
    "DescribeBatchSegmentJobResponseTypeDef",
    {
        "batchSegmentJob": "BatchSegmentJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCampaignRequestRequestTypeDef = TypedDict(
    "DescribeCampaignRequestRequestTypeDef",
    {
        "campaignArn": str,
    },
)

DescribeCampaignResponseTypeDef = TypedDict(
    "DescribeCampaignResponseTypeDef",
    {
        "campaign": "CampaignTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetExportJobRequestRequestTypeDef = TypedDict(
    "DescribeDatasetExportJobRequestRequestTypeDef",
    {
        "datasetExportJobArn": str,
    },
)

DescribeDatasetExportJobResponseTypeDef = TypedDict(
    "DescribeDatasetExportJobResponseTypeDef",
    {
        "datasetExportJob": "DatasetExportJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetGroupRequestRequestTypeDef = TypedDict(
    "DescribeDatasetGroupRequestRequestTypeDef",
    {
        "datasetGroupArn": str,
    },
)

DescribeDatasetGroupResponseTypeDef = TypedDict(
    "DescribeDatasetGroupResponseTypeDef",
    {
        "datasetGroup": "DatasetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetImportJobRequestRequestTypeDef = TypedDict(
    "DescribeDatasetImportJobRequestRequestTypeDef",
    {
        "datasetImportJobArn": str,
    },
)

DescribeDatasetImportJobResponseTypeDef = TypedDict(
    "DescribeDatasetImportJobResponseTypeDef",
    {
        "datasetImportJob": "DatasetImportJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "datasetArn": str,
    },
)

DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "dataset": "DatasetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventTrackerRequestRequestTypeDef = TypedDict(
    "DescribeEventTrackerRequestRequestTypeDef",
    {
        "eventTrackerArn": str,
    },
)

DescribeEventTrackerResponseTypeDef = TypedDict(
    "DescribeEventTrackerResponseTypeDef",
    {
        "eventTracker": "EventTrackerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFeatureTransformationRequestRequestTypeDef = TypedDict(
    "DescribeFeatureTransformationRequestRequestTypeDef",
    {
        "featureTransformationArn": str,
    },
)

DescribeFeatureTransformationResponseTypeDef = TypedDict(
    "DescribeFeatureTransformationResponseTypeDef",
    {
        "featureTransformation": "FeatureTransformationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFilterRequestRequestTypeDef = TypedDict(
    "DescribeFilterRequestRequestTypeDef",
    {
        "filterArn": str,
    },
)

DescribeFilterResponseTypeDef = TypedDict(
    "DescribeFilterResponseTypeDef",
    {
        "filter": "FilterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRecipeRequestRequestTypeDef = TypedDict(
    "DescribeRecipeRequestRequestTypeDef",
    {
        "recipeArn": str,
    },
)

DescribeRecipeResponseTypeDef = TypedDict(
    "DescribeRecipeResponseTypeDef",
    {
        "recipe": "RecipeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRecommenderRequestRequestTypeDef = TypedDict(
    "DescribeRecommenderRequestRequestTypeDef",
    {
        "recommenderArn": str,
    },
)

DescribeRecommenderResponseTypeDef = TypedDict(
    "DescribeRecommenderResponseTypeDef",
    {
        "recommender": "RecommenderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSchemaRequestRequestTypeDef = TypedDict(
    "DescribeSchemaRequestRequestTypeDef",
    {
        "schemaArn": str,
    },
)

DescribeSchemaResponseTypeDef = TypedDict(
    "DescribeSchemaResponseTypeDef",
    {
        "schema": "DatasetSchemaTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSolutionRequestRequestTypeDef = TypedDict(
    "DescribeSolutionRequestRequestTypeDef",
    {
        "solutionArn": str,
    },
)

DescribeSolutionResponseTypeDef = TypedDict(
    "DescribeSolutionResponseTypeDef",
    {
        "solution": "SolutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSolutionVersionRequestRequestTypeDef = TypedDict(
    "DescribeSolutionVersionRequestRequestTypeDef",
    {
        "solutionVersionArn": str,
    },
)

DescribeSolutionVersionResponseTypeDef = TypedDict(
    "DescribeSolutionVersionResponseTypeDef",
    {
        "solutionVersion": "SolutionVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventTrackerSummaryTypeDef = TypedDict(
    "EventTrackerSummaryTypeDef",
    {
        "name": NotRequired[str],
        "eventTrackerArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)

EventTrackerTypeDef = TypedDict(
    "EventTrackerTypeDef",
    {
        "name": NotRequired[str],
        "eventTrackerArn": NotRequired[str],
        "accountId": NotRequired[str],
        "trackingId": NotRequired[str],
        "datasetGroupArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)

FeatureTransformationTypeDef = TypedDict(
    "FeatureTransformationTypeDef",
    {
        "name": NotRequired[str],
        "featureTransformationArn": NotRequired[str],
        "defaultParameters": NotRequired[Dict[str, str]],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "status": NotRequired[str],
    },
)

FilterSummaryTypeDef = TypedDict(
    "FilterSummaryTypeDef",
    {
        "name": NotRequired[str],
        "filterArn": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "datasetGroupArn": NotRequired[str],
        "failureReason": NotRequired[str],
        "status": NotRequired[str],
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": NotRequired[str],
        "filterArn": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "datasetGroupArn": NotRequired[str],
        "failureReason": NotRequired[str],
        "filterExpression": NotRequired[str],
        "status": NotRequired[str],
    },
)

GetSolutionMetricsRequestRequestTypeDef = TypedDict(
    "GetSolutionMetricsRequestRequestTypeDef",
    {
        "solutionVersionArn": str,
    },
)

GetSolutionMetricsResponseTypeDef = TypedDict(
    "GetSolutionMetricsResponseTypeDef",
    {
        "solutionVersionArn": str,
        "metrics": Dict[str, float],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HPOConfigTypeDef = TypedDict(
    "HPOConfigTypeDef",
    {
        "hpoObjective": NotRequired["HPOObjectiveTypeDef"],
        "hpoResourceConfig": NotRequired["HPOResourceConfigTypeDef"],
        "algorithmHyperParameterRanges": NotRequired["HyperParameterRangesTypeDef"],
    },
)

HPOObjectiveTypeDef = TypedDict(
    "HPOObjectiveTypeDef",
    {
        "type": NotRequired[str],
        "metricName": NotRequired[str],
        "metricRegex": NotRequired[str],
    },
)

HPOResourceConfigTypeDef = TypedDict(
    "HPOResourceConfigTypeDef",
    {
        "maxNumberOfTrainingJobs": NotRequired[str],
        "maxParallelTrainingJobs": NotRequired[str],
    },
)

HyperParameterRangesTypeDef = TypedDict(
    "HyperParameterRangesTypeDef",
    {
        "integerHyperParameterRanges": NotRequired[Sequence["IntegerHyperParameterRangeTypeDef"]],
        "continuousHyperParameterRanges": NotRequired[
            Sequence["ContinuousHyperParameterRangeTypeDef"]
        ],
        "categoricalHyperParameterRanges": NotRequired[
            Sequence["CategoricalHyperParameterRangeTypeDef"]
        ],
    },
)

IntegerHyperParameterRangeTypeDef = TypedDict(
    "IntegerHyperParameterRangeTypeDef",
    {
        "name": NotRequired[str],
        "minValue": NotRequired[int],
        "maxValue": NotRequired[int],
    },
)

ListBatchInferenceJobsRequestRequestTypeDef = TypedDict(
    "ListBatchInferenceJobsRequestRequestTypeDef",
    {
        "solutionVersionArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListBatchInferenceJobsResponseTypeDef = TypedDict(
    "ListBatchInferenceJobsResponseTypeDef",
    {
        "batchInferenceJobs": List["BatchInferenceJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBatchSegmentJobsRequestRequestTypeDef = TypedDict(
    "ListBatchSegmentJobsRequestRequestTypeDef",
    {
        "solutionVersionArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListBatchSegmentJobsResponseTypeDef = TypedDict(
    "ListBatchSegmentJobsResponseTypeDef",
    {
        "batchSegmentJobs": List["BatchSegmentJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCampaignsRequestRequestTypeDef = TypedDict(
    "ListCampaignsRequestRequestTypeDef",
    {
        "solutionArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListCampaignsResponseTypeDef = TypedDict(
    "ListCampaignsResponseTypeDef",
    {
        "campaigns": List["CampaignSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetExportJobsRequestRequestTypeDef = TypedDict(
    "ListDatasetExportJobsRequestRequestTypeDef",
    {
        "datasetArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListDatasetExportJobsResponseTypeDef = TypedDict(
    "ListDatasetExportJobsResponseTypeDef",
    {
        "datasetExportJobs": List["DatasetExportJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetGroupsRequestRequestTypeDef = TypedDict(
    "ListDatasetGroupsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListDatasetGroupsResponseTypeDef = TypedDict(
    "ListDatasetGroupsResponseTypeDef",
    {
        "datasetGroups": List["DatasetGroupSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetImportJobsRequestRequestTypeDef = TypedDict(
    "ListDatasetImportJobsRequestRequestTypeDef",
    {
        "datasetArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListDatasetImportJobsResponseTypeDef = TypedDict(
    "ListDatasetImportJobsResponseTypeDef",
    {
        "datasetImportJobs": List["DatasetImportJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "datasetGroupArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "datasets": List["DatasetSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventTrackersRequestRequestTypeDef = TypedDict(
    "ListEventTrackersRequestRequestTypeDef",
    {
        "datasetGroupArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListEventTrackersResponseTypeDef = TypedDict(
    "ListEventTrackersResponseTypeDef",
    {
        "eventTrackers": List["EventTrackerSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFiltersRequestRequestTypeDef = TypedDict(
    "ListFiltersRequestRequestTypeDef",
    {
        "datasetGroupArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListFiltersResponseTypeDef = TypedDict(
    "ListFiltersResponseTypeDef",
    {
        "Filters": List["FilterSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecipesRequestRequestTypeDef = TypedDict(
    "ListRecipesRequestRequestTypeDef",
    {
        "recipeProvider": NotRequired[Literal["SERVICE"]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "domain": NotRequired[DomainType],
    },
)

ListRecipesResponseTypeDef = TypedDict(
    "ListRecipesResponseTypeDef",
    {
        "recipes": List["RecipeSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecommendersRequestRequestTypeDef = TypedDict(
    "ListRecommendersRequestRequestTypeDef",
    {
        "datasetGroupArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListRecommendersResponseTypeDef = TypedDict(
    "ListRecommendersResponseTypeDef",
    {
        "recommenders": List["RecommenderSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSchemasRequestRequestTypeDef = TypedDict(
    "ListSchemasRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListSchemasResponseTypeDef = TypedDict(
    "ListSchemasResponseTypeDef",
    {
        "schemas": List["DatasetSchemaSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSolutionVersionsRequestRequestTypeDef = TypedDict(
    "ListSolutionVersionsRequestRequestTypeDef",
    {
        "solutionArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListSolutionVersionsResponseTypeDef = TypedDict(
    "ListSolutionVersionsResponseTypeDef",
    {
        "solutionVersions": List["SolutionVersionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSolutionsRequestRequestTypeDef = TypedDict(
    "ListSolutionsRequestRequestTypeDef",
    {
        "datasetGroupArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListSolutionsResponseTypeDef = TypedDict(
    "ListSolutionsResponseTypeDef",
    {
        "solutions": List["SolutionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OptimizationObjectiveTypeDef = TypedDict(
    "OptimizationObjectiveTypeDef",
    {
        "itemAttribute": NotRequired[str],
        "objectiveSensitivity": NotRequired[ObjectiveSensitivityType],
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

RecipeSummaryTypeDef = TypedDict(
    "RecipeSummaryTypeDef",
    {
        "name": NotRequired[str],
        "recipeArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "domain": NotRequired[DomainType],
    },
)

RecipeTypeDef = TypedDict(
    "RecipeTypeDef",
    {
        "name": NotRequired[str],
        "recipeArn": NotRequired[str],
        "algorithmArn": NotRequired[str],
        "featureTransformationArn": NotRequired[str],
        "status": NotRequired[str],
        "description": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "recipeType": NotRequired[str],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)

RecommenderConfigTypeDef = TypedDict(
    "RecommenderConfigTypeDef",
    {
        "itemExplorationConfig": NotRequired[Mapping[str, str]],
        "minRecommendationRequestsPerSecond": NotRequired[int],
    },
)

RecommenderSummaryTypeDef = TypedDict(
    "RecommenderSummaryTypeDef",
    {
        "name": NotRequired[str],
        "recommenderArn": NotRequired[str],
        "datasetGroupArn": NotRequired[str],
        "recipeArn": NotRequired[str],
        "recommenderConfig": NotRequired["RecommenderConfigTypeDef"],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)

RecommenderTypeDef = TypedDict(
    "RecommenderTypeDef",
    {
        "recommenderArn": NotRequired[str],
        "datasetGroupArn": NotRequired[str],
        "name": NotRequired[str],
        "recipeArn": NotRequired[str],
        "recommenderConfig": NotRequired["RecommenderConfigTypeDef"],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "status": NotRequired[str],
        "failureReason": NotRequired[str],
        "latestRecommenderUpdate": NotRequired["RecommenderUpdateSummaryTypeDef"],
    },
)

RecommenderUpdateSummaryTypeDef = TypedDict(
    "RecommenderUpdateSummaryTypeDef",
    {
        "recommenderConfig": NotRequired["RecommenderConfigTypeDef"],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "status": NotRequired[str],
        "failureReason": NotRequired[str],
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

S3DataConfigTypeDef = TypedDict(
    "S3DataConfigTypeDef",
    {
        "path": str,
        "kmsKeyArn": NotRequired[str],
    },
)

SolutionConfigTypeDef = TypedDict(
    "SolutionConfigTypeDef",
    {
        "eventValueThreshold": NotRequired[str],
        "hpoConfig": NotRequired["HPOConfigTypeDef"],
        "algorithmHyperParameters": NotRequired[Mapping[str, str]],
        "featureTransformationParameters": NotRequired[Mapping[str, str]],
        "autoMLConfig": NotRequired["AutoMLConfigTypeDef"],
        "optimizationObjective": NotRequired["OptimizationObjectiveTypeDef"],
    },
)

SolutionSummaryTypeDef = TypedDict(
    "SolutionSummaryTypeDef",
    {
        "name": NotRequired[str],
        "solutionArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)

SolutionTypeDef = TypedDict(
    "SolutionTypeDef",
    {
        "name": NotRequired[str],
        "solutionArn": NotRequired[str],
        "performHPO": NotRequired[bool],
        "performAutoML": NotRequired[bool],
        "recipeArn": NotRequired[str],
        "datasetGroupArn": NotRequired[str],
        "eventType": NotRequired[str],
        "solutionConfig": NotRequired["SolutionConfigTypeDef"],
        "autoMLResult": NotRequired["AutoMLResultTypeDef"],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "latestSolutionVersion": NotRequired["SolutionVersionSummaryTypeDef"],
    },
)

SolutionVersionSummaryTypeDef = TypedDict(
    "SolutionVersionSummaryTypeDef",
    {
        "solutionVersionArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
    },
)

SolutionVersionTypeDef = TypedDict(
    "SolutionVersionTypeDef",
    {
        "solutionVersionArn": NotRequired[str],
        "solutionArn": NotRequired[str],
        "performHPO": NotRequired[bool],
        "performAutoML": NotRequired[bool],
        "recipeArn": NotRequired[str],
        "eventType": NotRequired[str],
        "datasetGroupArn": NotRequired[str],
        "solutionConfig": NotRequired["SolutionConfigTypeDef"],
        "trainingHours": NotRequired[float],
        "trainingMode": NotRequired[TrainingModeType],
        "tunedHPOParams": NotRequired["TunedHPOParamsTypeDef"],
        "status": NotRequired[str],
        "failureReason": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)

StopSolutionVersionCreationRequestRequestTypeDef = TypedDict(
    "StopSolutionVersionCreationRequestRequestTypeDef",
    {
        "solutionVersionArn": str,
    },
)

TunedHPOParamsTypeDef = TypedDict(
    "TunedHPOParamsTypeDef",
    {
        "algorithmHyperParameters": NotRequired[Dict[str, str]],
    },
)

UpdateCampaignRequestRequestTypeDef = TypedDict(
    "UpdateCampaignRequestRequestTypeDef",
    {
        "campaignArn": str,
        "solutionVersionArn": NotRequired[str],
        "minProvisionedTPS": NotRequired[int],
        "campaignConfig": NotRequired["CampaignConfigTypeDef"],
    },
)

UpdateCampaignResponseTypeDef = TypedDict(
    "UpdateCampaignResponseTypeDef",
    {
        "campaignArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRecommenderRequestRequestTypeDef = TypedDict(
    "UpdateRecommenderRequestRequestTypeDef",
    {
        "recommenderArn": str,
        "recommenderConfig": "RecommenderConfigTypeDef",
    },
)

UpdateRecommenderResponseTypeDef = TypedDict(
    "UpdateRecommenderResponseTypeDef",
    {
        "recommenderArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
