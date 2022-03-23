"""
Type annotations for sagemaker service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_sagemaker.type_defs import ActionSourceTypeDef

    data: ActionSourceTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    ActionStatusType,
    AlgorithmSortByType,
    AlgorithmStatusType,
    AppImageConfigSortKeyType,
    AppInstanceTypeType,
    AppNetworkAccessTypeType,
    AppSecurityGroupManagementType,
    AppStatusType,
    AppTypeType,
    ArtifactSourceIdTypeType,
    AssemblyTypeType,
    AssociationEdgeTypeType,
    AthenaResultCompressionTypeType,
    AthenaResultFormatType,
    AuthModeType,
    AutoMLJobObjectiveTypeType,
    AutoMLJobSecondaryStatusType,
    AutoMLJobStatusType,
    AutoMLMetricEnumType,
    AutoMLS3DataTypeType,
    AutoMLSortByType,
    AutoMLSortOrderType,
    AwsManagedHumanLoopRequestSourceType,
    BatchStrategyType,
    BooleanOperatorType,
    CandidateSortByType,
    CandidateStatusType,
    CandidateStepTypeType,
    CapacitySizeTypeType,
    CaptureModeType,
    CaptureStatusType,
    CodeRepositorySortByType,
    CodeRepositorySortOrderType,
    CompilationJobStatusType,
    CompressionTypeType,
    ConditionOutcomeType,
    ContainerModeType,
    ContentClassifierType,
    DataDistributionTypeType,
    DetailedAlgorithmStatusType,
    DetailedModelPackageStatusType,
    DirectInternetAccessType,
    DirectionType,
    DomainStatusType,
    EdgePackagingJobStatusType,
    EdgePresetDeploymentStatusType,
    EndpointConfigSortKeyType,
    EndpointSortKeyType,
    EndpointStatusType,
    ExecutionStatusType,
    FeatureGroupSortByType,
    FeatureGroupSortOrderType,
    FeatureGroupStatusType,
    FeatureTypeType,
    FileSystemAccessModeType,
    FileSystemTypeType,
    FlowDefinitionStatusType,
    FrameworkType,
    HumanTaskUiStatusType,
    HyperParameterScalingTypeType,
    HyperParameterTuningJobObjectiveTypeType,
    HyperParameterTuningJobSortByOptionsType,
    HyperParameterTuningJobStatusType,
    HyperParameterTuningJobStrategyTypeType,
    HyperParameterTuningJobWarmStartTypeType,
    ImageSortByType,
    ImageSortOrderType,
    ImageStatusType,
    ImageVersionSortByType,
    ImageVersionSortOrderType,
    ImageVersionStatusType,
    InferenceExecutionModeType,
    InputModeType,
    InstanceTypeType,
    JoinSourceType,
    LabelingJobStatusType,
    LineageTypeType,
    ListCompilationJobsSortByType,
    ListDeviceFleetsSortByType,
    ListEdgePackagingJobsSortByType,
    ListInferenceRecommendationsJobsSortByType,
    ListWorkforcesSortByOptionsType,
    ListWorkteamsSortByOptionsType,
    MetricSetSourceType,
    ModelApprovalStatusType,
    ModelCacheSettingType,
    ModelMetadataFilterTypeType,
    ModelPackageGroupSortByType,
    ModelPackageGroupStatusType,
    ModelPackageSortByType,
    ModelPackageStatusType,
    ModelPackageTypeType,
    ModelSortKeyType,
    MonitoringExecutionSortKeyType,
    MonitoringJobDefinitionSortKeyType,
    MonitoringProblemTypeType,
    MonitoringScheduleSortKeyType,
    MonitoringTypeType,
    NotebookInstanceAcceleratorTypeType,
    NotebookInstanceLifecycleConfigSortKeyType,
    NotebookInstanceLifecycleConfigSortOrderType,
    NotebookInstanceSortKeyType,
    NotebookInstanceSortOrderType,
    NotebookInstanceStatusType,
    NotebookOutputOptionType,
    ObjectiveStatusType,
    OfflineStoreStatusValueType,
    OperatorType,
    OrderKeyType,
    ParameterTypeType,
    PipelineExecutionStatusType,
    ProblemTypeType,
    ProcessingInstanceTypeType,
    ProcessingJobStatusType,
    ProcessingS3CompressionTypeType,
    ProcessingS3DataDistributionTypeType,
    ProcessingS3DataTypeType,
    ProcessingS3InputModeType,
    ProcessingS3UploadModeType,
    ProductionVariantAcceleratorTypeType,
    ProductionVariantInstanceTypeType,
    ProfilingStatusType,
    ProjectSortByType,
    ProjectSortOrderType,
    ProjectStatusType,
    RecommendationJobStatusType,
    RecommendationJobTypeType,
    RecordWrapperType,
    RedshiftResultCompressionTypeType,
    RedshiftResultFormatType,
    RepositoryAccessModeType,
    ResourceTypeType,
    RetentionTypeType,
    RootAccessType,
    RStudioServerProAccessStatusType,
    RStudioServerProUserGroupType,
    RuleEvaluationStatusType,
    S3DataDistributionType,
    S3DataTypeType,
    SagemakerServicecatalogStatusType,
    ScheduleStatusType,
    SearchSortOrderType,
    SecondaryStatusType,
    SortActionsByType,
    SortAssociationsByType,
    SortByType,
    SortContextsByType,
    SortExperimentsByType,
    SortLineageGroupsByType,
    SortOrderType,
    SortPipelineExecutionsByType,
    SortPipelinesByType,
    SortTrialComponentsByType,
    SortTrialsByType,
    SplitTypeType,
    StepStatusType,
    StudioLifecycleConfigAppTypeType,
    StudioLifecycleConfigSortKeyType,
    TargetDeviceType,
    TargetPlatformAcceleratorType,
    TargetPlatformArchType,
    TargetPlatformOsType,
    TrafficRoutingConfigTypeType,
    TrainingInputModeType,
    TrainingInstanceTypeType,
    TrainingJobEarlyStoppingTypeType,
    TrainingJobSortByOptionsType,
    TrainingJobStatusType,
    TransformInstanceTypeType,
    TransformJobStatusType,
    TrialComponentPrimaryStatusType,
    UserProfileSortKeyType,
    UserProfileStatusType,
    VariantPropertyTypeType,
    VariantStatusType,
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
    "ActionSourceTypeDef",
    "ActionSummaryTypeDef",
    "AddAssociationRequestRequestTypeDef",
    "AddAssociationResponseTypeDef",
    "AddTagsInputRequestTypeDef",
    "AddTagsOutputTypeDef",
    "AdditionalInferenceSpecificationDefinitionTypeDef",
    "AgentVersionTypeDef",
    "AlarmTypeDef",
    "AlgorithmSpecificationTypeDef",
    "AlgorithmStatusDetailsTypeDef",
    "AlgorithmStatusItemTypeDef",
    "AlgorithmSummaryTypeDef",
    "AlgorithmValidationProfileTypeDef",
    "AlgorithmValidationSpecificationTypeDef",
    "AnnotationConsolidationConfigTypeDef",
    "AppDetailsTypeDef",
    "AppImageConfigDetailsTypeDef",
    "AppSpecificationTypeDef",
    "ArtifactSourceTypeDef",
    "ArtifactSourceTypeTypeDef",
    "ArtifactSummaryTypeDef",
    "AssociateTrialComponentRequestRequestTypeDef",
    "AssociateTrialComponentResponseTypeDef",
    "AssociationSummaryTypeDef",
    "AsyncInferenceClientConfigTypeDef",
    "AsyncInferenceConfigTypeDef",
    "AsyncInferenceNotificationConfigTypeDef",
    "AsyncInferenceOutputConfigTypeDef",
    "AthenaDatasetDefinitionTypeDef",
    "AutoMLCandidateStepTypeDef",
    "AutoMLCandidateTypeDef",
    "AutoMLChannelTypeDef",
    "AutoMLContainerDefinitionTypeDef",
    "AutoMLDataSourceTypeDef",
    "AutoMLJobArtifactsTypeDef",
    "AutoMLJobCompletionCriteriaTypeDef",
    "AutoMLJobConfigTypeDef",
    "AutoMLJobObjectiveTypeDef",
    "AutoMLJobSummaryTypeDef",
    "AutoMLOutputDataConfigTypeDef",
    "AutoMLPartialFailureReasonTypeDef",
    "AutoMLS3DataSourceTypeDef",
    "AutoMLSecurityConfigTypeDef",
    "AutoRollbackConfigTypeDef",
    "BatchDescribeModelPackageErrorTypeDef",
    "BatchDescribeModelPackageInputRequestTypeDef",
    "BatchDescribeModelPackageOutputTypeDef",
    "BatchDescribeModelPackageSummaryTypeDef",
    "BiasTypeDef",
    "BlueGreenUpdatePolicyTypeDef",
    "CacheHitResultTypeDef",
    "CallbackStepMetadataTypeDef",
    "CandidateArtifactLocationsTypeDef",
    "CandidatePropertiesTypeDef",
    "CapacitySizeTypeDef",
    "CaptureContentTypeHeaderTypeDef",
    "CaptureOptionTypeDef",
    "CategoricalParameterRangeSpecificationTypeDef",
    "CategoricalParameterRangeTypeDef",
    "CategoricalParameterTypeDef",
    "ChannelSpecificationTypeDef",
    "ChannelTypeDef",
    "CheckpointConfigTypeDef",
    "ClarifyCheckStepMetadataTypeDef",
    "CodeRepositorySummaryTypeDef",
    "CognitoConfigTypeDef",
    "CognitoMemberDefinitionTypeDef",
    "CollectionConfigurationTypeDef",
    "CompilationJobSummaryTypeDef",
    "ConditionStepMetadataTypeDef",
    "ContainerDefinitionTypeDef",
    "ContextSourceTypeDef",
    "ContextSummaryTypeDef",
    "ContinuousParameterRangeSpecificationTypeDef",
    "ContinuousParameterRangeTypeDef",
    "CreateActionRequestRequestTypeDef",
    "CreateActionResponseTypeDef",
    "CreateAlgorithmInputRequestTypeDef",
    "CreateAlgorithmOutputTypeDef",
    "CreateAppImageConfigRequestRequestTypeDef",
    "CreateAppImageConfigResponseTypeDef",
    "CreateAppRequestRequestTypeDef",
    "CreateAppResponseTypeDef",
    "CreateArtifactRequestRequestTypeDef",
    "CreateArtifactResponseTypeDef",
    "CreateAutoMLJobRequestRequestTypeDef",
    "CreateAutoMLJobResponseTypeDef",
    "CreateCodeRepositoryInputRequestTypeDef",
    "CreateCodeRepositoryOutputTypeDef",
    "CreateCompilationJobRequestRequestTypeDef",
    "CreateCompilationJobResponseTypeDef",
    "CreateContextRequestRequestTypeDef",
    "CreateContextResponseTypeDef",
    "CreateDataQualityJobDefinitionRequestRequestTypeDef",
    "CreateDataQualityJobDefinitionResponseTypeDef",
    "CreateDeviceFleetRequestRequestTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "CreateDomainResponseTypeDef",
    "CreateEdgePackagingJobRequestRequestTypeDef",
    "CreateEndpointConfigInputRequestTypeDef",
    "CreateEndpointConfigOutputTypeDef",
    "CreateEndpointInputRequestTypeDef",
    "CreateEndpointOutputTypeDef",
    "CreateExperimentRequestRequestTypeDef",
    "CreateExperimentResponseTypeDef",
    "CreateFeatureGroupRequestRequestTypeDef",
    "CreateFeatureGroupResponseTypeDef",
    "CreateFlowDefinitionRequestRequestTypeDef",
    "CreateFlowDefinitionResponseTypeDef",
    "CreateHumanTaskUiRequestRequestTypeDef",
    "CreateHumanTaskUiResponseTypeDef",
    "CreateHyperParameterTuningJobRequestRequestTypeDef",
    "CreateHyperParameterTuningJobResponseTypeDef",
    "CreateImageRequestRequestTypeDef",
    "CreateImageResponseTypeDef",
    "CreateImageVersionRequestRequestTypeDef",
    "CreateImageVersionResponseTypeDef",
    "CreateInferenceRecommendationsJobRequestRequestTypeDef",
    "CreateInferenceRecommendationsJobResponseTypeDef",
    "CreateLabelingJobRequestRequestTypeDef",
    "CreateLabelingJobResponseTypeDef",
    "CreateModelBiasJobDefinitionRequestRequestTypeDef",
    "CreateModelBiasJobDefinitionResponseTypeDef",
    "CreateModelExplainabilityJobDefinitionRequestRequestTypeDef",
    "CreateModelExplainabilityJobDefinitionResponseTypeDef",
    "CreateModelInputRequestTypeDef",
    "CreateModelOutputTypeDef",
    "CreateModelPackageGroupInputRequestTypeDef",
    "CreateModelPackageGroupOutputTypeDef",
    "CreateModelPackageInputRequestTypeDef",
    "CreateModelPackageOutputTypeDef",
    "CreateModelQualityJobDefinitionRequestRequestTypeDef",
    "CreateModelQualityJobDefinitionResponseTypeDef",
    "CreateMonitoringScheduleRequestRequestTypeDef",
    "CreateMonitoringScheduleResponseTypeDef",
    "CreateNotebookInstanceInputRequestTypeDef",
    "CreateNotebookInstanceLifecycleConfigInputRequestTypeDef",
    "CreateNotebookInstanceLifecycleConfigOutputTypeDef",
    "CreateNotebookInstanceOutputTypeDef",
    "CreatePipelineRequestRequestTypeDef",
    "CreatePipelineResponseTypeDef",
    "CreatePresignedDomainUrlRequestRequestTypeDef",
    "CreatePresignedDomainUrlResponseTypeDef",
    "CreatePresignedNotebookInstanceUrlInputRequestTypeDef",
    "CreatePresignedNotebookInstanceUrlOutputTypeDef",
    "CreateProcessingJobRequestRequestTypeDef",
    "CreateProcessingJobResponseTypeDef",
    "CreateProjectInputRequestTypeDef",
    "CreateProjectOutputTypeDef",
    "CreateStudioLifecycleConfigRequestRequestTypeDef",
    "CreateStudioLifecycleConfigResponseTypeDef",
    "CreateTrainingJobRequestRequestTypeDef",
    "CreateTrainingJobResponseTypeDef",
    "CreateTransformJobRequestRequestTypeDef",
    "CreateTransformJobResponseTypeDef",
    "CreateTrialComponentRequestRequestTypeDef",
    "CreateTrialComponentResponseTypeDef",
    "CreateTrialRequestRequestTypeDef",
    "CreateTrialResponseTypeDef",
    "CreateUserProfileRequestRequestTypeDef",
    "CreateUserProfileResponseTypeDef",
    "CreateWorkforceRequestRequestTypeDef",
    "CreateWorkforceResponseTypeDef",
    "CreateWorkteamRequestRequestTypeDef",
    "CreateWorkteamResponseTypeDef",
    "CustomImageTypeDef",
    "DataCaptureConfigSummaryTypeDef",
    "DataCaptureConfigTypeDef",
    "DataCatalogConfigTypeDef",
    "DataProcessingTypeDef",
    "DataQualityAppSpecificationTypeDef",
    "DataQualityBaselineConfigTypeDef",
    "DataQualityJobInputTypeDef",
    "DataSourceTypeDef",
    "DatasetDefinitionTypeDef",
    "DebugHookConfigTypeDef",
    "DebugRuleConfigurationTypeDef",
    "DebugRuleEvaluationStatusTypeDef",
    "DeleteActionRequestRequestTypeDef",
    "DeleteActionResponseTypeDef",
    "DeleteAlgorithmInputRequestTypeDef",
    "DeleteAppImageConfigRequestRequestTypeDef",
    "DeleteAppRequestRequestTypeDef",
    "DeleteArtifactRequestRequestTypeDef",
    "DeleteArtifactResponseTypeDef",
    "DeleteAssociationRequestRequestTypeDef",
    "DeleteAssociationResponseTypeDef",
    "DeleteCodeRepositoryInputRequestTypeDef",
    "DeleteContextRequestRequestTypeDef",
    "DeleteContextResponseTypeDef",
    "DeleteDataQualityJobDefinitionRequestRequestTypeDef",
    "DeleteDeviceFleetRequestRequestTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteEndpointConfigInputRequestTypeDef",
    "DeleteEndpointInputRequestTypeDef",
    "DeleteExperimentRequestRequestTypeDef",
    "DeleteExperimentResponseTypeDef",
    "DeleteFeatureGroupRequestRequestTypeDef",
    "DeleteFlowDefinitionRequestRequestTypeDef",
    "DeleteHumanTaskUiRequestRequestTypeDef",
    "DeleteImageRequestRequestTypeDef",
    "DeleteImageVersionRequestRequestTypeDef",
    "DeleteModelBiasJobDefinitionRequestRequestTypeDef",
    "DeleteModelExplainabilityJobDefinitionRequestRequestTypeDef",
    "DeleteModelInputRequestTypeDef",
    "DeleteModelPackageGroupInputRequestTypeDef",
    "DeleteModelPackageGroupPolicyInputRequestTypeDef",
    "DeleteModelPackageInputRequestTypeDef",
    "DeleteModelQualityJobDefinitionRequestRequestTypeDef",
    "DeleteMonitoringScheduleRequestRequestTypeDef",
    "DeleteNotebookInstanceInputRequestTypeDef",
    "DeleteNotebookInstanceLifecycleConfigInputRequestTypeDef",
    "DeletePipelineRequestRequestTypeDef",
    "DeletePipelineResponseTypeDef",
    "DeleteProjectInputRequestTypeDef",
    "DeleteStudioLifecycleConfigRequestRequestTypeDef",
    "DeleteTagsInputRequestTypeDef",
    "DeleteTrialComponentRequestRequestTypeDef",
    "DeleteTrialComponentResponseTypeDef",
    "DeleteTrialRequestRequestTypeDef",
    "DeleteTrialResponseTypeDef",
    "DeleteUserProfileRequestRequestTypeDef",
    "DeleteWorkforceRequestRequestTypeDef",
    "DeleteWorkteamRequestRequestTypeDef",
    "DeleteWorkteamResponseTypeDef",
    "DeployedImageTypeDef",
    "DeploymentConfigTypeDef",
    "DeregisterDevicesRequestRequestTypeDef",
    "DescribeActionRequestRequestTypeDef",
    "DescribeActionResponseTypeDef",
    "DescribeAlgorithmInputRequestTypeDef",
    "DescribeAlgorithmOutputTypeDef",
    "DescribeAppImageConfigRequestRequestTypeDef",
    "DescribeAppImageConfigResponseTypeDef",
    "DescribeAppRequestRequestTypeDef",
    "DescribeAppResponseTypeDef",
    "DescribeArtifactRequestRequestTypeDef",
    "DescribeArtifactResponseTypeDef",
    "DescribeAutoMLJobRequestRequestTypeDef",
    "DescribeAutoMLJobResponseTypeDef",
    "DescribeCodeRepositoryInputRequestTypeDef",
    "DescribeCodeRepositoryOutputTypeDef",
    "DescribeCompilationJobRequestRequestTypeDef",
    "DescribeCompilationJobResponseTypeDef",
    "DescribeContextRequestRequestTypeDef",
    "DescribeContextResponseTypeDef",
    "DescribeDataQualityJobDefinitionRequestRequestTypeDef",
    "DescribeDataQualityJobDefinitionResponseTypeDef",
    "DescribeDeviceFleetRequestRequestTypeDef",
    "DescribeDeviceFleetResponseTypeDef",
    "DescribeDeviceRequestRequestTypeDef",
    "DescribeDeviceResponseTypeDef",
    "DescribeDomainRequestRequestTypeDef",
    "DescribeDomainResponseTypeDef",
    "DescribeEdgePackagingJobRequestRequestTypeDef",
    "DescribeEdgePackagingJobResponseTypeDef",
    "DescribeEndpointConfigInputRequestTypeDef",
    "DescribeEndpointConfigOutputTypeDef",
    "DescribeEndpointInputRequestTypeDef",
    "DescribeEndpointOutputTypeDef",
    "DescribeExperimentRequestRequestTypeDef",
    "DescribeExperimentResponseTypeDef",
    "DescribeFeatureGroupRequestRequestTypeDef",
    "DescribeFeatureGroupResponseTypeDef",
    "DescribeFlowDefinitionRequestRequestTypeDef",
    "DescribeFlowDefinitionResponseTypeDef",
    "DescribeHumanTaskUiRequestRequestTypeDef",
    "DescribeHumanTaskUiResponseTypeDef",
    "DescribeHyperParameterTuningJobRequestRequestTypeDef",
    "DescribeHyperParameterTuningJobResponseTypeDef",
    "DescribeImageRequestRequestTypeDef",
    "DescribeImageResponseTypeDef",
    "DescribeImageVersionRequestRequestTypeDef",
    "DescribeImageVersionResponseTypeDef",
    "DescribeInferenceRecommendationsJobRequestRequestTypeDef",
    "DescribeInferenceRecommendationsJobResponseTypeDef",
    "DescribeLabelingJobRequestRequestTypeDef",
    "DescribeLabelingJobResponseTypeDef",
    "DescribeLineageGroupRequestRequestTypeDef",
    "DescribeLineageGroupResponseTypeDef",
    "DescribeModelBiasJobDefinitionRequestRequestTypeDef",
    "DescribeModelBiasJobDefinitionResponseTypeDef",
    "DescribeModelExplainabilityJobDefinitionRequestRequestTypeDef",
    "DescribeModelExplainabilityJobDefinitionResponseTypeDef",
    "DescribeModelInputRequestTypeDef",
    "DescribeModelOutputTypeDef",
    "DescribeModelPackageGroupInputRequestTypeDef",
    "DescribeModelPackageGroupOutputTypeDef",
    "DescribeModelPackageInputRequestTypeDef",
    "DescribeModelPackageOutputTypeDef",
    "DescribeModelQualityJobDefinitionRequestRequestTypeDef",
    "DescribeModelQualityJobDefinitionResponseTypeDef",
    "DescribeMonitoringScheduleRequestRequestTypeDef",
    "DescribeMonitoringScheduleResponseTypeDef",
    "DescribeNotebookInstanceInputRequestTypeDef",
    "DescribeNotebookInstanceLifecycleConfigInputRequestTypeDef",
    "DescribeNotebookInstanceLifecycleConfigOutputTypeDef",
    "DescribeNotebookInstanceOutputTypeDef",
    "DescribePipelineDefinitionForExecutionRequestRequestTypeDef",
    "DescribePipelineDefinitionForExecutionResponseTypeDef",
    "DescribePipelineExecutionRequestRequestTypeDef",
    "DescribePipelineExecutionResponseTypeDef",
    "DescribePipelineRequestRequestTypeDef",
    "DescribePipelineResponseTypeDef",
    "DescribeProcessingJobRequestRequestTypeDef",
    "DescribeProcessingJobResponseTypeDef",
    "DescribeProjectInputRequestTypeDef",
    "DescribeProjectOutputTypeDef",
    "DescribeStudioLifecycleConfigRequestRequestTypeDef",
    "DescribeStudioLifecycleConfigResponseTypeDef",
    "DescribeSubscribedWorkteamRequestRequestTypeDef",
    "DescribeSubscribedWorkteamResponseTypeDef",
    "DescribeTrainingJobRequestRequestTypeDef",
    "DescribeTrainingJobResponseTypeDef",
    "DescribeTransformJobRequestRequestTypeDef",
    "DescribeTransformJobResponseTypeDef",
    "DescribeTrialComponentRequestRequestTypeDef",
    "DescribeTrialComponentResponseTypeDef",
    "DescribeTrialRequestRequestTypeDef",
    "DescribeTrialResponseTypeDef",
    "DescribeUserProfileRequestRequestTypeDef",
    "DescribeUserProfileResponseTypeDef",
    "DescribeWorkforceRequestRequestTypeDef",
    "DescribeWorkforceResponseTypeDef",
    "DescribeWorkteamRequestRequestTypeDef",
    "DescribeWorkteamResponseTypeDef",
    "DesiredWeightAndCapacityTypeDef",
    "DeviceFleetSummaryTypeDef",
    "DeviceStatsTypeDef",
    "DeviceSummaryTypeDef",
    "DeviceTypeDef",
    "DisassociateTrialComponentRequestRequestTypeDef",
    "DisassociateTrialComponentResponseTypeDef",
    "DomainDetailsTypeDef",
    "DomainSettingsForUpdateTypeDef",
    "DomainSettingsTypeDef",
    "DriftCheckBaselinesTypeDef",
    "DriftCheckBiasTypeDef",
    "DriftCheckExplainabilityTypeDef",
    "DriftCheckModelDataQualityTypeDef",
    "DriftCheckModelQualityTypeDef",
    "EMRStepMetadataTypeDef",
    "EdgeModelStatTypeDef",
    "EdgeModelSummaryTypeDef",
    "EdgeModelTypeDef",
    "EdgeOutputConfigTypeDef",
    "EdgePackagingJobSummaryTypeDef",
    "EdgePresetDeploymentOutputTypeDef",
    "EdgeTypeDef",
    "EndpointConfigSummaryTypeDef",
    "EndpointInputConfigurationTypeDef",
    "EndpointInputTypeDef",
    "EndpointOutputConfigurationTypeDef",
    "EndpointSummaryTypeDef",
    "EndpointTypeDef",
    "EnvironmentParameterRangesTypeDef",
    "EnvironmentParameterTypeDef",
    "ExperimentConfigTypeDef",
    "ExperimentSourceTypeDef",
    "ExperimentSummaryTypeDef",
    "ExperimentTypeDef",
    "ExplainabilityTypeDef",
    "FailStepMetadataTypeDef",
    "FeatureDefinitionTypeDef",
    "FeatureGroupSummaryTypeDef",
    "FeatureGroupTypeDef",
    "FileSourceTypeDef",
    "FileSystemConfigTypeDef",
    "FileSystemDataSourceTypeDef",
    "FilterTypeDef",
    "FinalAutoMLJobObjectiveMetricTypeDef",
    "FinalHyperParameterTuningJobObjectiveMetricTypeDef",
    "FlowDefinitionOutputConfigTypeDef",
    "FlowDefinitionSummaryTypeDef",
    "GetDeviceFleetReportRequestRequestTypeDef",
    "GetDeviceFleetReportResponseTypeDef",
    "GetLineageGroupPolicyRequestRequestTypeDef",
    "GetLineageGroupPolicyResponseTypeDef",
    "GetModelPackageGroupPolicyInputRequestTypeDef",
    "GetModelPackageGroupPolicyOutputTypeDef",
    "GetSagemakerServicecatalogPortfolioStatusOutputTypeDef",
    "GetSearchSuggestionsRequestRequestTypeDef",
    "GetSearchSuggestionsResponseTypeDef",
    "GitConfigForUpdateTypeDef",
    "GitConfigTypeDef",
    "HumanLoopActivationConditionsConfigTypeDef",
    "HumanLoopActivationConfigTypeDef",
    "HumanLoopConfigTypeDef",
    "HumanLoopRequestSourceTypeDef",
    "HumanTaskConfigTypeDef",
    "HumanTaskUiSummaryTypeDef",
    "HyperParameterAlgorithmSpecificationTypeDef",
    "HyperParameterSpecificationTypeDef",
    "HyperParameterTrainingJobDefinitionTypeDef",
    "HyperParameterTrainingJobSummaryTypeDef",
    "HyperParameterTuningJobConfigTypeDef",
    "HyperParameterTuningJobObjectiveTypeDef",
    "HyperParameterTuningJobSummaryTypeDef",
    "HyperParameterTuningJobWarmStartConfigTypeDef",
    "ImageConfigTypeDef",
    "ImageTypeDef",
    "ImageVersionTypeDef",
    "InferenceExecutionConfigTypeDef",
    "InferenceRecommendationTypeDef",
    "InferenceRecommendationsJobTypeDef",
    "InferenceSpecificationTypeDef",
    "InputConfigTypeDef",
    "IntegerParameterRangeSpecificationTypeDef",
    "IntegerParameterRangeTypeDef",
    "JupyterServerAppSettingsTypeDef",
    "KernelGatewayAppSettingsTypeDef",
    "KernelGatewayImageConfigTypeDef",
    "KernelSpecTypeDef",
    "LabelCountersForWorkteamTypeDef",
    "LabelCountersTypeDef",
    "LabelingJobAlgorithmsConfigTypeDef",
    "LabelingJobDataAttributesTypeDef",
    "LabelingJobDataSourceTypeDef",
    "LabelingJobForWorkteamSummaryTypeDef",
    "LabelingJobInputConfigTypeDef",
    "LabelingJobOutputConfigTypeDef",
    "LabelingJobOutputTypeDef",
    "LabelingJobResourceConfigTypeDef",
    "LabelingJobS3DataSourceTypeDef",
    "LabelingJobSnsDataSourceTypeDef",
    "LabelingJobStoppingConditionsTypeDef",
    "LabelingJobSummaryTypeDef",
    "LambdaStepMetadataTypeDef",
    "LineageGroupSummaryTypeDef",
    "ListActionsRequestRequestTypeDef",
    "ListActionsResponseTypeDef",
    "ListAlgorithmsInputRequestTypeDef",
    "ListAlgorithmsOutputTypeDef",
    "ListAppImageConfigsRequestRequestTypeDef",
    "ListAppImageConfigsResponseTypeDef",
    "ListAppsRequestRequestTypeDef",
    "ListAppsResponseTypeDef",
    "ListArtifactsRequestRequestTypeDef",
    "ListArtifactsResponseTypeDef",
    "ListAssociationsRequestRequestTypeDef",
    "ListAssociationsResponseTypeDef",
    "ListAutoMLJobsRequestRequestTypeDef",
    "ListAutoMLJobsResponseTypeDef",
    "ListCandidatesForAutoMLJobRequestRequestTypeDef",
    "ListCandidatesForAutoMLJobResponseTypeDef",
    "ListCodeRepositoriesInputRequestTypeDef",
    "ListCodeRepositoriesOutputTypeDef",
    "ListCompilationJobsRequestRequestTypeDef",
    "ListCompilationJobsResponseTypeDef",
    "ListContextsRequestRequestTypeDef",
    "ListContextsResponseTypeDef",
    "ListDataQualityJobDefinitionsRequestRequestTypeDef",
    "ListDataQualityJobDefinitionsResponseTypeDef",
    "ListDeviceFleetsRequestRequestTypeDef",
    "ListDeviceFleetsResponseTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "ListDevicesResponseTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListDomainsResponseTypeDef",
    "ListEdgePackagingJobsRequestRequestTypeDef",
    "ListEdgePackagingJobsResponseTypeDef",
    "ListEndpointConfigsInputRequestTypeDef",
    "ListEndpointConfigsOutputTypeDef",
    "ListEndpointsInputRequestTypeDef",
    "ListEndpointsOutputTypeDef",
    "ListExperimentsRequestRequestTypeDef",
    "ListExperimentsResponseTypeDef",
    "ListFeatureGroupsRequestRequestTypeDef",
    "ListFeatureGroupsResponseTypeDef",
    "ListFlowDefinitionsRequestRequestTypeDef",
    "ListFlowDefinitionsResponseTypeDef",
    "ListHumanTaskUisRequestRequestTypeDef",
    "ListHumanTaskUisResponseTypeDef",
    "ListHyperParameterTuningJobsRequestRequestTypeDef",
    "ListHyperParameterTuningJobsResponseTypeDef",
    "ListImageVersionsRequestRequestTypeDef",
    "ListImageVersionsResponseTypeDef",
    "ListImagesRequestRequestTypeDef",
    "ListImagesResponseTypeDef",
    "ListInferenceRecommendationsJobsRequestRequestTypeDef",
    "ListInferenceRecommendationsJobsResponseTypeDef",
    "ListLabelingJobsForWorkteamRequestRequestTypeDef",
    "ListLabelingJobsForWorkteamResponseTypeDef",
    "ListLabelingJobsRequestRequestTypeDef",
    "ListLabelingJobsResponseTypeDef",
    "ListLineageGroupsRequestRequestTypeDef",
    "ListLineageGroupsResponseTypeDef",
    "ListModelBiasJobDefinitionsRequestRequestTypeDef",
    "ListModelBiasJobDefinitionsResponseTypeDef",
    "ListModelExplainabilityJobDefinitionsRequestRequestTypeDef",
    "ListModelExplainabilityJobDefinitionsResponseTypeDef",
    "ListModelMetadataRequestRequestTypeDef",
    "ListModelMetadataResponseTypeDef",
    "ListModelPackageGroupsInputRequestTypeDef",
    "ListModelPackageGroupsOutputTypeDef",
    "ListModelPackagesInputRequestTypeDef",
    "ListModelPackagesOutputTypeDef",
    "ListModelQualityJobDefinitionsRequestRequestTypeDef",
    "ListModelQualityJobDefinitionsResponseTypeDef",
    "ListModelsInputRequestTypeDef",
    "ListModelsOutputTypeDef",
    "ListMonitoringExecutionsRequestRequestTypeDef",
    "ListMonitoringExecutionsResponseTypeDef",
    "ListMonitoringSchedulesRequestRequestTypeDef",
    "ListMonitoringSchedulesResponseTypeDef",
    "ListNotebookInstanceLifecycleConfigsInputRequestTypeDef",
    "ListNotebookInstanceLifecycleConfigsOutputTypeDef",
    "ListNotebookInstancesInputRequestTypeDef",
    "ListNotebookInstancesOutputTypeDef",
    "ListPipelineExecutionStepsRequestRequestTypeDef",
    "ListPipelineExecutionStepsResponseTypeDef",
    "ListPipelineExecutionsRequestRequestTypeDef",
    "ListPipelineExecutionsResponseTypeDef",
    "ListPipelineParametersForExecutionRequestRequestTypeDef",
    "ListPipelineParametersForExecutionResponseTypeDef",
    "ListPipelinesRequestRequestTypeDef",
    "ListPipelinesResponseTypeDef",
    "ListProcessingJobsRequestRequestTypeDef",
    "ListProcessingJobsResponseTypeDef",
    "ListProjectsInputRequestTypeDef",
    "ListProjectsOutputTypeDef",
    "ListStudioLifecycleConfigsRequestRequestTypeDef",
    "ListStudioLifecycleConfigsResponseTypeDef",
    "ListSubscribedWorkteamsRequestRequestTypeDef",
    "ListSubscribedWorkteamsResponseTypeDef",
    "ListTagsInputRequestTypeDef",
    "ListTagsOutputTypeDef",
    "ListTrainingJobsForHyperParameterTuningJobRequestRequestTypeDef",
    "ListTrainingJobsForHyperParameterTuningJobResponseTypeDef",
    "ListTrainingJobsRequestRequestTypeDef",
    "ListTrainingJobsResponseTypeDef",
    "ListTransformJobsRequestRequestTypeDef",
    "ListTransformJobsResponseTypeDef",
    "ListTrialComponentsRequestRequestTypeDef",
    "ListTrialComponentsResponseTypeDef",
    "ListTrialsRequestRequestTypeDef",
    "ListTrialsResponseTypeDef",
    "ListUserProfilesRequestRequestTypeDef",
    "ListUserProfilesResponseTypeDef",
    "ListWorkforcesRequestRequestTypeDef",
    "ListWorkforcesResponseTypeDef",
    "ListWorkteamsRequestRequestTypeDef",
    "ListWorkteamsResponseTypeDef",
    "MemberDefinitionTypeDef",
    "MetadataPropertiesTypeDef",
    "MetricDataTypeDef",
    "MetricDatumTypeDef",
    "MetricDefinitionTypeDef",
    "MetricsSourceTypeDef",
    "ModelArtifactsTypeDef",
    "ModelBiasAppSpecificationTypeDef",
    "ModelBiasBaselineConfigTypeDef",
    "ModelBiasJobInputTypeDef",
    "ModelClientConfigTypeDef",
    "ModelConfigurationTypeDef",
    "ModelDataQualityTypeDef",
    "ModelDeployConfigTypeDef",
    "ModelDeployResultTypeDef",
    "ModelDigestsTypeDef",
    "ModelExplainabilityAppSpecificationTypeDef",
    "ModelExplainabilityBaselineConfigTypeDef",
    "ModelExplainabilityJobInputTypeDef",
    "ModelInputTypeDef",
    "ModelLatencyThresholdTypeDef",
    "ModelMetadataFilterTypeDef",
    "ModelMetadataSearchExpressionTypeDef",
    "ModelMetadataSummaryTypeDef",
    "ModelMetricsTypeDef",
    "ModelPackageContainerDefinitionTypeDef",
    "ModelPackageGroupSummaryTypeDef",
    "ModelPackageGroupTypeDef",
    "ModelPackageStatusDetailsTypeDef",
    "ModelPackageStatusItemTypeDef",
    "ModelPackageSummaryTypeDef",
    "ModelPackageTypeDef",
    "ModelPackageValidationProfileTypeDef",
    "ModelPackageValidationSpecificationTypeDef",
    "ModelQualityAppSpecificationTypeDef",
    "ModelQualityBaselineConfigTypeDef",
    "ModelQualityJobInputTypeDef",
    "ModelQualityTypeDef",
    "ModelStepMetadataTypeDef",
    "ModelSummaryTypeDef",
    "MonitoringAppSpecificationTypeDef",
    "MonitoringBaselineConfigTypeDef",
    "MonitoringClusterConfigTypeDef",
    "MonitoringConstraintsResourceTypeDef",
    "MonitoringExecutionSummaryTypeDef",
    "MonitoringGroundTruthS3InputTypeDef",
    "MonitoringInputTypeDef",
    "MonitoringJobDefinitionSummaryTypeDef",
    "MonitoringJobDefinitionTypeDef",
    "MonitoringNetworkConfigTypeDef",
    "MonitoringOutputConfigTypeDef",
    "MonitoringOutputTypeDef",
    "MonitoringResourcesTypeDef",
    "MonitoringS3OutputTypeDef",
    "MonitoringScheduleConfigTypeDef",
    "MonitoringScheduleSummaryTypeDef",
    "MonitoringScheduleTypeDef",
    "MonitoringStatisticsResourceTypeDef",
    "MonitoringStoppingConditionTypeDef",
    "MultiModelConfigTypeDef",
    "NeoVpcConfigTypeDef",
    "NestedFiltersTypeDef",
    "NetworkConfigTypeDef",
    "NotebookInstanceLifecycleConfigSummaryTypeDef",
    "NotebookInstanceLifecycleHookTypeDef",
    "NotebookInstanceSummaryTypeDef",
    "NotificationConfigurationTypeDef",
    "ObjectiveStatusCountersTypeDef",
    "OfflineStoreConfigTypeDef",
    "OfflineStoreStatusTypeDef",
    "OidcConfigForResponseTypeDef",
    "OidcConfigTypeDef",
    "OidcMemberDefinitionTypeDef",
    "OnlineStoreConfigTypeDef",
    "OnlineStoreSecurityConfigTypeDef",
    "OutputConfigTypeDef",
    "OutputDataConfigTypeDef",
    "OutputParameterTypeDef",
    "PaginatorConfigTypeDef",
    "ParallelismConfigurationTypeDef",
    "ParameterRangeTypeDef",
    "ParameterRangesTypeDef",
    "ParameterTypeDef",
    "ParentHyperParameterTuningJobTypeDef",
    "ParentTypeDef",
    "PendingDeploymentSummaryTypeDef",
    "PendingProductionVariantSummaryTypeDef",
    "PhaseTypeDef",
    "PipelineDefinitionS3LocationTypeDef",
    "PipelineExecutionStepMetadataTypeDef",
    "PipelineExecutionStepTypeDef",
    "PipelineExecutionSummaryTypeDef",
    "PipelineExecutionTypeDef",
    "PipelineExperimentConfigTypeDef",
    "PipelineSummaryTypeDef",
    "PipelineTypeDef",
    "ProcessingClusterConfigTypeDef",
    "ProcessingFeatureStoreOutputTypeDef",
    "ProcessingInputTypeDef",
    "ProcessingJobStepMetadataTypeDef",
    "ProcessingJobSummaryTypeDef",
    "ProcessingJobTypeDef",
    "ProcessingOutputConfigTypeDef",
    "ProcessingOutputTypeDef",
    "ProcessingResourcesTypeDef",
    "ProcessingS3InputTypeDef",
    "ProcessingS3OutputTypeDef",
    "ProcessingStoppingConditionTypeDef",
    "ProductionVariantCoreDumpConfigTypeDef",
    "ProductionVariantServerlessConfigTypeDef",
    "ProductionVariantStatusTypeDef",
    "ProductionVariantSummaryTypeDef",
    "ProductionVariantTypeDef",
    "ProfilerConfigForUpdateTypeDef",
    "ProfilerConfigTypeDef",
    "ProfilerRuleConfigurationTypeDef",
    "ProfilerRuleEvaluationStatusTypeDef",
    "ProjectSummaryTypeDef",
    "ProjectTypeDef",
    "PropertyNameQueryTypeDef",
    "PropertyNameSuggestionTypeDef",
    "ProvisioningParameterTypeDef",
    "PublicWorkforceTaskPriceTypeDef",
    "PutModelPackageGroupPolicyInputRequestTypeDef",
    "PutModelPackageGroupPolicyOutputTypeDef",
    "QualityCheckStepMetadataTypeDef",
    "QueryFiltersTypeDef",
    "QueryLineageRequestRequestTypeDef",
    "QueryLineageResponseTypeDef",
    "RStudioServerProAppSettingsTypeDef",
    "RStudioServerProDomainSettingsForUpdateTypeDef",
    "RStudioServerProDomainSettingsTypeDef",
    "RecommendationJobInputConfigTypeDef",
    "RecommendationJobResourceLimitTypeDef",
    "RecommendationJobStoppingConditionsTypeDef",
    "RecommendationMetricsTypeDef",
    "RedshiftDatasetDefinitionTypeDef",
    "RegisterDevicesRequestRequestTypeDef",
    "RegisterModelStepMetadataTypeDef",
    "RenderUiTemplateRequestRequestTypeDef",
    "RenderUiTemplateResponseTypeDef",
    "RenderableTaskTypeDef",
    "RenderingErrorTypeDef",
    "RepositoryAuthConfigTypeDef",
    "ResolvedAttributesTypeDef",
    "ResourceConfigTypeDef",
    "ResourceLimitsTypeDef",
    "ResourceSpecTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionPolicyTypeDef",
    "RetryPipelineExecutionRequestRequestTypeDef",
    "RetryPipelineExecutionResponseTypeDef",
    "RetryStrategyTypeDef",
    "S3DataSourceTypeDef",
    "S3StorageConfigTypeDef",
    "ScheduleConfigTypeDef",
    "SearchExpressionTypeDef",
    "SearchRecordTypeDef",
    "SearchRequestRequestTypeDef",
    "SearchResponseTypeDef",
    "SecondaryStatusTransitionTypeDef",
    "SendPipelineExecutionStepFailureRequestRequestTypeDef",
    "SendPipelineExecutionStepFailureResponseTypeDef",
    "SendPipelineExecutionStepSuccessRequestRequestTypeDef",
    "SendPipelineExecutionStepSuccessResponseTypeDef",
    "ServiceCatalogProvisionedProductDetailsTypeDef",
    "ServiceCatalogProvisioningDetailsTypeDef",
    "ServiceCatalogProvisioningUpdateDetailsTypeDef",
    "SharingSettingsTypeDef",
    "ShuffleConfigTypeDef",
    "SourceAlgorithmSpecificationTypeDef",
    "SourceAlgorithmTypeDef",
    "SourceIpConfigTypeDef",
    "StartMonitoringScheduleRequestRequestTypeDef",
    "StartNotebookInstanceInputRequestTypeDef",
    "StartPipelineExecutionRequestRequestTypeDef",
    "StartPipelineExecutionResponseTypeDef",
    "StopAutoMLJobRequestRequestTypeDef",
    "StopCompilationJobRequestRequestTypeDef",
    "StopEdgePackagingJobRequestRequestTypeDef",
    "StopHyperParameterTuningJobRequestRequestTypeDef",
    "StopInferenceRecommendationsJobRequestRequestTypeDef",
    "StopLabelingJobRequestRequestTypeDef",
    "StopMonitoringScheduleRequestRequestTypeDef",
    "StopNotebookInstanceInputRequestTypeDef",
    "StopPipelineExecutionRequestRequestTypeDef",
    "StopPipelineExecutionResponseTypeDef",
    "StopProcessingJobRequestRequestTypeDef",
    "StopTrainingJobRequestRequestTypeDef",
    "StopTransformJobRequestRequestTypeDef",
    "StoppingConditionTypeDef",
    "StudioLifecycleConfigDetailsTypeDef",
    "SubscribedWorkteamTypeDef",
    "SuggestionQueryTypeDef",
    "TagTypeDef",
    "TargetPlatformTypeDef",
    "TensorBoardAppSettingsTypeDef",
    "TensorBoardOutputConfigTypeDef",
    "TrafficPatternTypeDef",
    "TrafficRoutingConfigTypeDef",
    "TrainingJobDefinitionTypeDef",
    "TrainingJobStatusCountersTypeDef",
    "TrainingJobStepMetadataTypeDef",
    "TrainingJobSummaryTypeDef",
    "TrainingJobTypeDef",
    "TrainingSpecificationTypeDef",
    "TransformDataSourceTypeDef",
    "TransformInputTypeDef",
    "TransformJobDefinitionTypeDef",
    "TransformJobStepMetadataTypeDef",
    "TransformJobSummaryTypeDef",
    "TransformJobTypeDef",
    "TransformOutputTypeDef",
    "TransformResourcesTypeDef",
    "TransformS3DataSourceTypeDef",
    "TrialComponentArtifactTypeDef",
    "TrialComponentMetricSummaryTypeDef",
    "TrialComponentParameterValueTypeDef",
    "TrialComponentSimpleSummaryTypeDef",
    "TrialComponentSourceDetailTypeDef",
    "TrialComponentSourceTypeDef",
    "TrialComponentStatusTypeDef",
    "TrialComponentSummaryTypeDef",
    "TrialComponentTypeDef",
    "TrialSourceTypeDef",
    "TrialSummaryTypeDef",
    "TrialTypeDef",
    "TuningJobCompletionCriteriaTypeDef",
    "TuningJobStepMetaDataTypeDef",
    "USDTypeDef",
    "UiConfigTypeDef",
    "UiTemplateInfoTypeDef",
    "UiTemplateTypeDef",
    "UpdateActionRequestRequestTypeDef",
    "UpdateActionResponseTypeDef",
    "UpdateAppImageConfigRequestRequestTypeDef",
    "UpdateAppImageConfigResponseTypeDef",
    "UpdateArtifactRequestRequestTypeDef",
    "UpdateArtifactResponseTypeDef",
    "UpdateCodeRepositoryInputRequestTypeDef",
    "UpdateCodeRepositoryOutputTypeDef",
    "UpdateContextRequestRequestTypeDef",
    "UpdateContextResponseTypeDef",
    "UpdateDeviceFleetRequestRequestTypeDef",
    "UpdateDevicesRequestRequestTypeDef",
    "UpdateDomainRequestRequestTypeDef",
    "UpdateDomainResponseTypeDef",
    "UpdateEndpointInputRequestTypeDef",
    "UpdateEndpointOutputTypeDef",
    "UpdateEndpointWeightsAndCapacitiesInputRequestTypeDef",
    "UpdateEndpointWeightsAndCapacitiesOutputTypeDef",
    "UpdateExperimentRequestRequestTypeDef",
    "UpdateExperimentResponseTypeDef",
    "UpdateImageRequestRequestTypeDef",
    "UpdateImageResponseTypeDef",
    "UpdateModelPackageInputRequestTypeDef",
    "UpdateModelPackageOutputTypeDef",
    "UpdateMonitoringScheduleRequestRequestTypeDef",
    "UpdateMonitoringScheduleResponseTypeDef",
    "UpdateNotebookInstanceInputRequestTypeDef",
    "UpdateNotebookInstanceLifecycleConfigInputRequestTypeDef",
    "UpdatePipelineExecutionRequestRequestTypeDef",
    "UpdatePipelineExecutionResponseTypeDef",
    "UpdatePipelineRequestRequestTypeDef",
    "UpdatePipelineResponseTypeDef",
    "UpdateProjectInputRequestTypeDef",
    "UpdateProjectOutputTypeDef",
    "UpdateTrainingJobRequestRequestTypeDef",
    "UpdateTrainingJobResponseTypeDef",
    "UpdateTrialComponentRequestRequestTypeDef",
    "UpdateTrialComponentResponseTypeDef",
    "UpdateTrialRequestRequestTypeDef",
    "UpdateTrialResponseTypeDef",
    "UpdateUserProfileRequestRequestTypeDef",
    "UpdateUserProfileResponseTypeDef",
    "UpdateWorkforceRequestRequestTypeDef",
    "UpdateWorkforceResponseTypeDef",
    "UpdateWorkteamRequestRequestTypeDef",
    "UpdateWorkteamResponseTypeDef",
    "UserContextTypeDef",
    "UserProfileDetailsTypeDef",
    "UserSettingsTypeDef",
    "VariantPropertyTypeDef",
    "VertexTypeDef",
    "VpcConfigTypeDef",
    "WaiterConfigTypeDef",
    "WorkforceTypeDef",
    "WorkteamTypeDef",
)

ActionSourceTypeDef = TypedDict(
    "ActionSourceTypeDef",
    {
        "SourceUri": str,
        "SourceType": NotRequired[str],
        "SourceId": NotRequired[str],
    },
)

ActionSummaryTypeDef = TypedDict(
    "ActionSummaryTypeDef",
    {
        "ActionArn": NotRequired[str],
        "ActionName": NotRequired[str],
        "Source": NotRequired["ActionSourceTypeDef"],
        "ActionType": NotRequired[str],
        "Status": NotRequired[ActionStatusType],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)

AddAssociationRequestRequestTypeDef = TypedDict(
    "AddAssociationRequestRequestTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
        "AssociationType": NotRequired[AssociationEdgeTypeType],
    },
)

AddAssociationResponseTypeDef = TypedDict(
    "AddAssociationResponseTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsInputRequestTypeDef = TypedDict(
    "AddTagsInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

AddTagsOutputTypeDef = TypedDict(
    "AddTagsOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdditionalInferenceSpecificationDefinitionTypeDef = TypedDict(
    "AdditionalInferenceSpecificationDefinitionTypeDef",
    {
        "Name": str,
        "Containers": Sequence["ModelPackageContainerDefinitionTypeDef"],
        "Description": NotRequired[str],
        "SupportedTransformInstanceTypes": NotRequired[Sequence[TransformInstanceTypeType]],
        "SupportedRealtimeInferenceInstanceTypes": NotRequired[
            Sequence[ProductionVariantInstanceTypeType]
        ],
        "SupportedContentTypes": NotRequired[Sequence[str]],
        "SupportedResponseMIMETypes": NotRequired[Sequence[str]],
    },
)

AgentVersionTypeDef = TypedDict(
    "AgentVersionTypeDef",
    {
        "Version": str,
        "AgentCount": int,
    },
)

AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "AlarmName": NotRequired[str],
    },
)

AlgorithmSpecificationTypeDef = TypedDict(
    "AlgorithmSpecificationTypeDef",
    {
        "TrainingInputMode": TrainingInputModeType,
        "TrainingImage": NotRequired[str],
        "AlgorithmName": NotRequired[str],
        "MetricDefinitions": NotRequired[Sequence["MetricDefinitionTypeDef"]],
        "EnableSageMakerMetricsTimeSeries": NotRequired[bool],
    },
)

AlgorithmStatusDetailsTypeDef = TypedDict(
    "AlgorithmStatusDetailsTypeDef",
    {
        "ValidationStatuses": NotRequired[List["AlgorithmStatusItemTypeDef"]],
        "ImageScanStatuses": NotRequired[List["AlgorithmStatusItemTypeDef"]],
    },
)

AlgorithmStatusItemTypeDef = TypedDict(
    "AlgorithmStatusItemTypeDef",
    {
        "Name": str,
        "Status": DetailedAlgorithmStatusType,
        "FailureReason": NotRequired[str],
    },
)

AlgorithmSummaryTypeDef = TypedDict(
    "AlgorithmSummaryTypeDef",
    {
        "AlgorithmName": str,
        "AlgorithmArn": str,
        "CreationTime": datetime,
        "AlgorithmStatus": AlgorithmStatusType,
        "AlgorithmDescription": NotRequired[str],
    },
)

AlgorithmValidationProfileTypeDef = TypedDict(
    "AlgorithmValidationProfileTypeDef",
    {
        "ProfileName": str,
        "TrainingJobDefinition": "TrainingJobDefinitionTypeDef",
        "TransformJobDefinition": NotRequired["TransformJobDefinitionTypeDef"],
    },
)

AlgorithmValidationSpecificationTypeDef = TypedDict(
    "AlgorithmValidationSpecificationTypeDef",
    {
        "ValidationRole": str,
        "ValidationProfiles": Sequence["AlgorithmValidationProfileTypeDef"],
    },
)

AnnotationConsolidationConfigTypeDef = TypedDict(
    "AnnotationConsolidationConfigTypeDef",
    {
        "AnnotationConsolidationLambdaArn": str,
    },
)

AppDetailsTypeDef = TypedDict(
    "AppDetailsTypeDef",
    {
        "DomainId": NotRequired[str],
        "UserProfileName": NotRequired[str],
        "AppType": NotRequired[AppTypeType],
        "AppName": NotRequired[str],
        "Status": NotRequired[AppStatusType],
        "CreationTime": NotRequired[datetime],
    },
)

AppImageConfigDetailsTypeDef = TypedDict(
    "AppImageConfigDetailsTypeDef",
    {
        "AppImageConfigArn": NotRequired[str],
        "AppImageConfigName": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "KernelGatewayImageConfig": NotRequired["KernelGatewayImageConfigTypeDef"],
    },
)

AppSpecificationTypeDef = TypedDict(
    "AppSpecificationTypeDef",
    {
        "ImageUri": str,
        "ContainerEntrypoint": NotRequired[Sequence[str]],
        "ContainerArguments": NotRequired[Sequence[str]],
    },
)

ArtifactSourceTypeDef = TypedDict(
    "ArtifactSourceTypeDef",
    {
        "SourceUri": str,
        "SourceTypes": NotRequired[Sequence["ArtifactSourceTypeTypeDef"]],
    },
)

ArtifactSourceTypeTypeDef = TypedDict(
    "ArtifactSourceTypeTypeDef",
    {
        "SourceIdType": ArtifactSourceIdTypeType,
        "Value": str,
    },
)

ArtifactSummaryTypeDef = TypedDict(
    "ArtifactSummaryTypeDef",
    {
        "ArtifactArn": NotRequired[str],
        "ArtifactName": NotRequired[str],
        "Source": NotRequired["ArtifactSourceTypeDef"],
        "ArtifactType": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)

AssociateTrialComponentRequestRequestTypeDef = TypedDict(
    "AssociateTrialComponentRequestRequestTypeDef",
    {
        "TrialComponentName": str,
        "TrialName": str,
    },
)

AssociateTrialComponentResponseTypeDef = TypedDict(
    "AssociateTrialComponentResponseTypeDef",
    {
        "TrialComponentArn": str,
        "TrialArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociationSummaryTypeDef = TypedDict(
    "AssociationSummaryTypeDef",
    {
        "SourceArn": NotRequired[str],
        "DestinationArn": NotRequired[str],
        "SourceType": NotRequired[str],
        "DestinationType": NotRequired[str],
        "AssociationType": NotRequired[AssociationEdgeTypeType],
        "SourceName": NotRequired[str],
        "DestinationName": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "CreatedBy": NotRequired["UserContextTypeDef"],
    },
)

AsyncInferenceClientConfigTypeDef = TypedDict(
    "AsyncInferenceClientConfigTypeDef",
    {
        "MaxConcurrentInvocationsPerInstance": NotRequired[int],
    },
)

AsyncInferenceConfigTypeDef = TypedDict(
    "AsyncInferenceConfigTypeDef",
    {
        "OutputConfig": "AsyncInferenceOutputConfigTypeDef",
        "ClientConfig": NotRequired["AsyncInferenceClientConfigTypeDef"],
    },
)

AsyncInferenceNotificationConfigTypeDef = TypedDict(
    "AsyncInferenceNotificationConfigTypeDef",
    {
        "SuccessTopic": NotRequired[str],
        "ErrorTopic": NotRequired[str],
    },
)

AsyncInferenceOutputConfigTypeDef = TypedDict(
    "AsyncInferenceOutputConfigTypeDef",
    {
        "S3OutputPath": str,
        "KmsKeyId": NotRequired[str],
        "NotificationConfig": NotRequired["AsyncInferenceNotificationConfigTypeDef"],
    },
)

AthenaDatasetDefinitionTypeDef = TypedDict(
    "AthenaDatasetDefinitionTypeDef",
    {
        "Catalog": str,
        "Database": str,
        "QueryString": str,
        "OutputS3Uri": str,
        "OutputFormat": AthenaResultFormatType,
        "WorkGroup": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "OutputCompression": NotRequired[AthenaResultCompressionTypeType],
    },
)

AutoMLCandidateStepTypeDef = TypedDict(
    "AutoMLCandidateStepTypeDef",
    {
        "CandidateStepType": CandidateStepTypeType,
        "CandidateStepArn": str,
        "CandidateStepName": str,
    },
)

AutoMLCandidateTypeDef = TypedDict(
    "AutoMLCandidateTypeDef",
    {
        "CandidateName": str,
        "ObjectiveStatus": ObjectiveStatusType,
        "CandidateSteps": List["AutoMLCandidateStepTypeDef"],
        "CandidateStatus": CandidateStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "FinalAutoMLJobObjectiveMetric": NotRequired["FinalAutoMLJobObjectiveMetricTypeDef"],
        "InferenceContainers": NotRequired[List["AutoMLContainerDefinitionTypeDef"]],
        "EndTime": NotRequired[datetime],
        "FailureReason": NotRequired[str],
        "CandidateProperties": NotRequired["CandidatePropertiesTypeDef"],
    },
)

AutoMLChannelTypeDef = TypedDict(
    "AutoMLChannelTypeDef",
    {
        "DataSource": "AutoMLDataSourceTypeDef",
        "TargetAttributeName": str,
        "CompressionType": NotRequired[CompressionTypeType],
        "ContentType": NotRequired[str],
    },
)

AutoMLContainerDefinitionTypeDef = TypedDict(
    "AutoMLContainerDefinitionTypeDef",
    {
        "Image": str,
        "ModelDataUrl": str,
        "Environment": NotRequired[Dict[str, str]],
    },
)

AutoMLDataSourceTypeDef = TypedDict(
    "AutoMLDataSourceTypeDef",
    {
        "S3DataSource": "AutoMLS3DataSourceTypeDef",
    },
)

AutoMLJobArtifactsTypeDef = TypedDict(
    "AutoMLJobArtifactsTypeDef",
    {
        "CandidateDefinitionNotebookLocation": NotRequired[str],
        "DataExplorationNotebookLocation": NotRequired[str],
    },
)

AutoMLJobCompletionCriteriaTypeDef = TypedDict(
    "AutoMLJobCompletionCriteriaTypeDef",
    {
        "MaxCandidates": NotRequired[int],
        "MaxRuntimePerTrainingJobInSeconds": NotRequired[int],
        "MaxAutoMLJobRuntimeInSeconds": NotRequired[int],
    },
)

AutoMLJobConfigTypeDef = TypedDict(
    "AutoMLJobConfigTypeDef",
    {
        "CompletionCriteria": NotRequired["AutoMLJobCompletionCriteriaTypeDef"],
        "SecurityConfig": NotRequired["AutoMLSecurityConfigTypeDef"],
    },
)

AutoMLJobObjectiveTypeDef = TypedDict(
    "AutoMLJobObjectiveTypeDef",
    {
        "MetricName": AutoMLMetricEnumType,
    },
)

AutoMLJobSummaryTypeDef = TypedDict(
    "AutoMLJobSummaryTypeDef",
    {
        "AutoMLJobName": str,
        "AutoMLJobArn": str,
        "AutoMLJobStatus": AutoMLJobStatusType,
        "AutoMLJobSecondaryStatus": AutoMLJobSecondaryStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "EndTime": NotRequired[datetime],
        "FailureReason": NotRequired[str],
        "PartialFailureReasons": NotRequired[List["AutoMLPartialFailureReasonTypeDef"]],
    },
)

AutoMLOutputDataConfigTypeDef = TypedDict(
    "AutoMLOutputDataConfigTypeDef",
    {
        "S3OutputPath": str,
        "KmsKeyId": NotRequired[str],
    },
)

AutoMLPartialFailureReasonTypeDef = TypedDict(
    "AutoMLPartialFailureReasonTypeDef",
    {
        "PartialFailureMessage": NotRequired[str],
    },
)

AutoMLS3DataSourceTypeDef = TypedDict(
    "AutoMLS3DataSourceTypeDef",
    {
        "S3DataType": AutoMLS3DataTypeType,
        "S3Uri": str,
    },
)

AutoMLSecurityConfigTypeDef = TypedDict(
    "AutoMLSecurityConfigTypeDef",
    {
        "VolumeKmsKeyId": NotRequired[str],
        "EnableInterContainerTrafficEncryption": NotRequired[bool],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
    },
)

AutoRollbackConfigTypeDef = TypedDict(
    "AutoRollbackConfigTypeDef",
    {
        "Alarms": NotRequired[Sequence["AlarmTypeDef"]],
    },
)

BatchDescribeModelPackageErrorTypeDef = TypedDict(
    "BatchDescribeModelPackageErrorTypeDef",
    {
        "ErrorCode": str,
        "ErrorResponse": str,
    },
)

BatchDescribeModelPackageInputRequestTypeDef = TypedDict(
    "BatchDescribeModelPackageInputRequestTypeDef",
    {
        "ModelPackageArnList": Sequence[str],
    },
)

BatchDescribeModelPackageOutputTypeDef = TypedDict(
    "BatchDescribeModelPackageOutputTypeDef",
    {
        "ModelPackageSummaries": Dict[str, "BatchDescribeModelPackageSummaryTypeDef"],
        "BatchDescribeModelPackageErrorMap": Dict[str, "BatchDescribeModelPackageErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDescribeModelPackageSummaryTypeDef = TypedDict(
    "BatchDescribeModelPackageSummaryTypeDef",
    {
        "ModelPackageGroupName": str,
        "ModelPackageArn": str,
        "CreationTime": datetime,
        "InferenceSpecification": "InferenceSpecificationTypeDef",
        "ModelPackageStatus": ModelPackageStatusType,
        "ModelPackageVersion": NotRequired[int],
        "ModelPackageDescription": NotRequired[str],
        "ModelApprovalStatus": NotRequired[ModelApprovalStatusType],
    },
)

BiasTypeDef = TypedDict(
    "BiasTypeDef",
    {
        "Report": NotRequired["MetricsSourceTypeDef"],
        "PreTrainingReport": NotRequired["MetricsSourceTypeDef"],
        "PostTrainingReport": NotRequired["MetricsSourceTypeDef"],
    },
)

BlueGreenUpdatePolicyTypeDef = TypedDict(
    "BlueGreenUpdatePolicyTypeDef",
    {
        "TrafficRoutingConfiguration": "TrafficRoutingConfigTypeDef",
        "TerminationWaitInSeconds": NotRequired[int],
        "MaximumExecutionTimeoutInSeconds": NotRequired[int],
    },
)

CacheHitResultTypeDef = TypedDict(
    "CacheHitResultTypeDef",
    {
        "SourcePipelineExecutionArn": NotRequired[str],
    },
)

CallbackStepMetadataTypeDef = TypedDict(
    "CallbackStepMetadataTypeDef",
    {
        "CallbackToken": NotRequired[str],
        "SqsQueueUrl": NotRequired[str],
        "OutputParameters": NotRequired[List["OutputParameterTypeDef"]],
    },
)

CandidateArtifactLocationsTypeDef = TypedDict(
    "CandidateArtifactLocationsTypeDef",
    {
        "Explainability": str,
        "ModelInsights": NotRequired[str],
    },
)

CandidatePropertiesTypeDef = TypedDict(
    "CandidatePropertiesTypeDef",
    {
        "CandidateArtifactLocations": NotRequired["CandidateArtifactLocationsTypeDef"],
        "CandidateMetrics": NotRequired[List["MetricDatumTypeDef"]],
    },
)

CapacitySizeTypeDef = TypedDict(
    "CapacitySizeTypeDef",
    {
        "Type": CapacitySizeTypeType,
        "Value": int,
    },
)

CaptureContentTypeHeaderTypeDef = TypedDict(
    "CaptureContentTypeHeaderTypeDef",
    {
        "CsvContentTypes": NotRequired[Sequence[str]],
        "JsonContentTypes": NotRequired[Sequence[str]],
    },
)

CaptureOptionTypeDef = TypedDict(
    "CaptureOptionTypeDef",
    {
        "CaptureMode": CaptureModeType,
    },
)

CategoricalParameterRangeSpecificationTypeDef = TypedDict(
    "CategoricalParameterRangeSpecificationTypeDef",
    {
        "Values": Sequence[str],
    },
)

CategoricalParameterRangeTypeDef = TypedDict(
    "CategoricalParameterRangeTypeDef",
    {
        "Name": str,
        "Values": Sequence[str],
    },
)

CategoricalParameterTypeDef = TypedDict(
    "CategoricalParameterTypeDef",
    {
        "Name": str,
        "Value": Sequence[str],
    },
)

ChannelSpecificationTypeDef = TypedDict(
    "ChannelSpecificationTypeDef",
    {
        "Name": str,
        "SupportedContentTypes": Sequence[str],
        "SupportedInputModes": Sequence[TrainingInputModeType],
        "Description": NotRequired[str],
        "IsRequired": NotRequired[bool],
        "SupportedCompressionTypes": NotRequired[Sequence[CompressionTypeType]],
    },
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "ChannelName": str,
        "DataSource": "DataSourceTypeDef",
        "ContentType": NotRequired[str],
        "CompressionType": NotRequired[CompressionTypeType],
        "RecordWrapperType": NotRequired[RecordWrapperType],
        "InputMode": NotRequired[TrainingInputModeType],
        "ShuffleConfig": NotRequired["ShuffleConfigTypeDef"],
    },
)

CheckpointConfigTypeDef = TypedDict(
    "CheckpointConfigTypeDef",
    {
        "S3Uri": str,
        "LocalPath": NotRequired[str],
    },
)

ClarifyCheckStepMetadataTypeDef = TypedDict(
    "ClarifyCheckStepMetadataTypeDef",
    {
        "CheckType": NotRequired[str],
        "BaselineUsedForDriftCheckConstraints": NotRequired[str],
        "CalculatedBaselineConstraints": NotRequired[str],
        "ModelPackageGroupName": NotRequired[str],
        "ViolationReport": NotRequired[str],
        "CheckJobArn": NotRequired[str],
        "SkipCheck": NotRequired[bool],
        "RegisterNewBaseline": NotRequired[bool],
    },
)

CodeRepositorySummaryTypeDef = TypedDict(
    "CodeRepositorySummaryTypeDef",
    {
        "CodeRepositoryName": str,
        "CodeRepositoryArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "GitConfig": NotRequired["GitConfigTypeDef"],
    },
)

CognitoConfigTypeDef = TypedDict(
    "CognitoConfigTypeDef",
    {
        "UserPool": str,
        "ClientId": str,
    },
)

CognitoMemberDefinitionTypeDef = TypedDict(
    "CognitoMemberDefinitionTypeDef",
    {
        "UserPool": str,
        "UserGroup": str,
        "ClientId": str,
    },
)

CollectionConfigurationTypeDef = TypedDict(
    "CollectionConfigurationTypeDef",
    {
        "CollectionName": NotRequired[str],
        "CollectionParameters": NotRequired[Mapping[str, str]],
    },
)

CompilationJobSummaryTypeDef = TypedDict(
    "CompilationJobSummaryTypeDef",
    {
        "CompilationJobName": str,
        "CompilationJobArn": str,
        "CreationTime": datetime,
        "CompilationJobStatus": CompilationJobStatusType,
        "CompilationStartTime": NotRequired[datetime],
        "CompilationEndTime": NotRequired[datetime],
        "CompilationTargetDevice": NotRequired[TargetDeviceType],
        "CompilationTargetPlatformOs": NotRequired[TargetPlatformOsType],
        "CompilationTargetPlatformArch": NotRequired[TargetPlatformArchType],
        "CompilationTargetPlatformAccelerator": NotRequired[TargetPlatformAcceleratorType],
        "LastModifiedTime": NotRequired[datetime],
    },
)

ConditionStepMetadataTypeDef = TypedDict(
    "ConditionStepMetadataTypeDef",
    {
        "Outcome": NotRequired[ConditionOutcomeType],
    },
)

ContainerDefinitionTypeDef = TypedDict(
    "ContainerDefinitionTypeDef",
    {
        "ContainerHostname": NotRequired[str],
        "Image": NotRequired[str],
        "ImageConfig": NotRequired["ImageConfigTypeDef"],
        "Mode": NotRequired[ContainerModeType],
        "ModelDataUrl": NotRequired[str],
        "Environment": NotRequired[Mapping[str, str]],
        "ModelPackageName": NotRequired[str],
        "InferenceSpecificationName": NotRequired[str],
        "MultiModelConfig": NotRequired["MultiModelConfigTypeDef"],
    },
)

ContextSourceTypeDef = TypedDict(
    "ContextSourceTypeDef",
    {
        "SourceUri": str,
        "SourceType": NotRequired[str],
        "SourceId": NotRequired[str],
    },
)

ContextSummaryTypeDef = TypedDict(
    "ContextSummaryTypeDef",
    {
        "ContextArn": NotRequired[str],
        "ContextName": NotRequired[str],
        "Source": NotRequired["ContextSourceTypeDef"],
        "ContextType": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)

ContinuousParameterRangeSpecificationTypeDef = TypedDict(
    "ContinuousParameterRangeSpecificationTypeDef",
    {
        "MinValue": str,
        "MaxValue": str,
    },
)

ContinuousParameterRangeTypeDef = TypedDict(
    "ContinuousParameterRangeTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
        "ScalingType": NotRequired[HyperParameterScalingTypeType],
    },
)

CreateActionRequestRequestTypeDef = TypedDict(
    "CreateActionRequestRequestTypeDef",
    {
        "ActionName": str,
        "Source": "ActionSourceTypeDef",
        "ActionType": str,
        "Description": NotRequired[str],
        "Status": NotRequired[ActionStatusType],
        "Properties": NotRequired[Mapping[str, str]],
        "MetadataProperties": NotRequired["MetadataPropertiesTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateActionResponseTypeDef = TypedDict(
    "CreateActionResponseTypeDef",
    {
        "ActionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAlgorithmInputRequestTypeDef = TypedDict(
    "CreateAlgorithmInputRequestTypeDef",
    {
        "AlgorithmName": str,
        "TrainingSpecification": "TrainingSpecificationTypeDef",
        "AlgorithmDescription": NotRequired[str],
        "InferenceSpecification": NotRequired["InferenceSpecificationTypeDef"],
        "ValidationSpecification": NotRequired["AlgorithmValidationSpecificationTypeDef"],
        "CertifyForMarketplace": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateAlgorithmOutputTypeDef = TypedDict(
    "CreateAlgorithmOutputTypeDef",
    {
        "AlgorithmArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAppImageConfigRequestRequestTypeDef = TypedDict(
    "CreateAppImageConfigRequestRequestTypeDef",
    {
        "AppImageConfigName": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "KernelGatewayImageConfig": NotRequired["KernelGatewayImageConfigTypeDef"],
    },
)

CreateAppImageConfigResponseTypeDef = TypedDict(
    "CreateAppImageConfigResponseTypeDef",
    {
        "AppImageConfigArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAppRequestRequestTypeDef = TypedDict(
    "CreateAppRequestRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
        "AppType": AppTypeType,
        "AppName": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ResourceSpec": NotRequired["ResourceSpecTypeDef"],
    },
)

CreateAppResponseTypeDef = TypedDict(
    "CreateAppResponseTypeDef",
    {
        "AppArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateArtifactRequestRequestTypeDef = TypedDict(
    "CreateArtifactRequestRequestTypeDef",
    {
        "Source": "ArtifactSourceTypeDef",
        "ArtifactType": str,
        "ArtifactName": NotRequired[str],
        "Properties": NotRequired[Mapping[str, str]],
        "MetadataProperties": NotRequired["MetadataPropertiesTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateArtifactResponseTypeDef = TypedDict(
    "CreateArtifactResponseTypeDef",
    {
        "ArtifactArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAutoMLJobRequestRequestTypeDef = TypedDict(
    "CreateAutoMLJobRequestRequestTypeDef",
    {
        "AutoMLJobName": str,
        "InputDataConfig": Sequence["AutoMLChannelTypeDef"],
        "OutputDataConfig": "AutoMLOutputDataConfigTypeDef",
        "RoleArn": str,
        "ProblemType": NotRequired[ProblemTypeType],
        "AutoMLJobObjective": NotRequired["AutoMLJobObjectiveTypeDef"],
        "AutoMLJobConfig": NotRequired["AutoMLJobConfigTypeDef"],
        "GenerateCandidateDefinitionsOnly": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ModelDeployConfig": NotRequired["ModelDeployConfigTypeDef"],
    },
)

CreateAutoMLJobResponseTypeDef = TypedDict(
    "CreateAutoMLJobResponseTypeDef",
    {
        "AutoMLJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCodeRepositoryInputRequestTypeDef = TypedDict(
    "CreateCodeRepositoryInputRequestTypeDef",
    {
        "CodeRepositoryName": str,
        "GitConfig": "GitConfigTypeDef",
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateCodeRepositoryOutputTypeDef = TypedDict(
    "CreateCodeRepositoryOutputTypeDef",
    {
        "CodeRepositoryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCompilationJobRequestRequestTypeDef = TypedDict(
    "CreateCompilationJobRequestRequestTypeDef",
    {
        "CompilationJobName": str,
        "RoleArn": str,
        "OutputConfig": "OutputConfigTypeDef",
        "StoppingCondition": "StoppingConditionTypeDef",
        "ModelPackageVersionArn": NotRequired[str],
        "InputConfig": NotRequired["InputConfigTypeDef"],
        "VpcConfig": NotRequired["NeoVpcConfigTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateCompilationJobResponseTypeDef = TypedDict(
    "CreateCompilationJobResponseTypeDef",
    {
        "CompilationJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateContextRequestRequestTypeDef = TypedDict(
    "CreateContextRequestRequestTypeDef",
    {
        "ContextName": str,
        "Source": "ContextSourceTypeDef",
        "ContextType": str,
        "Description": NotRequired[str],
        "Properties": NotRequired[Mapping[str, str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateContextResponseTypeDef = TypedDict(
    "CreateContextResponseTypeDef",
    {
        "ContextArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDataQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "CreateDataQualityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
        "DataQualityAppSpecification": "DataQualityAppSpecificationTypeDef",
        "DataQualityJobInput": "DataQualityJobInputTypeDef",
        "DataQualityJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "RoleArn": str,
        "DataQualityBaselineConfig": NotRequired["DataQualityBaselineConfigTypeDef"],
        "NetworkConfig": NotRequired["MonitoringNetworkConfigTypeDef"],
        "StoppingCondition": NotRequired["MonitoringStoppingConditionTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDataQualityJobDefinitionResponseTypeDef = TypedDict(
    "CreateDataQualityJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDeviceFleetRequestRequestTypeDef = TypedDict(
    "CreateDeviceFleetRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
        "OutputConfig": "EdgeOutputConfigTypeDef",
        "RoleArn": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "EnableIotRoleAlias": NotRequired[bool],
    },
)

CreateDomainRequestRequestTypeDef = TypedDict(
    "CreateDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "AuthMode": AuthModeType,
        "DefaultUserSettings": "UserSettingsTypeDef",
        "SubnetIds": Sequence[str],
        "VpcId": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "AppNetworkAccessType": NotRequired[AppNetworkAccessTypeType],
        "HomeEfsFileSystemKmsKeyId": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "AppSecurityGroupManagement": NotRequired[AppSecurityGroupManagementType],
        "DomainSettings": NotRequired["DomainSettingsTypeDef"],
    },
)

CreateDomainResponseTypeDef = TypedDict(
    "CreateDomainResponseTypeDef",
    {
        "DomainArn": str,
        "Url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEdgePackagingJobRequestRequestTypeDef = TypedDict(
    "CreateEdgePackagingJobRequestRequestTypeDef",
    {
        "EdgePackagingJobName": str,
        "CompilationJobName": str,
        "ModelName": str,
        "ModelVersion": str,
        "RoleArn": str,
        "OutputConfig": "EdgeOutputConfigTypeDef",
        "ResourceKey": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateEndpointConfigInputRequestTypeDef = TypedDict(
    "CreateEndpointConfigInputRequestTypeDef",
    {
        "EndpointConfigName": str,
        "ProductionVariants": Sequence["ProductionVariantTypeDef"],
        "DataCaptureConfig": NotRequired["DataCaptureConfigTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "KmsKeyId": NotRequired[str],
        "AsyncInferenceConfig": NotRequired["AsyncInferenceConfigTypeDef"],
    },
)

CreateEndpointConfigOutputTypeDef = TypedDict(
    "CreateEndpointConfigOutputTypeDef",
    {
        "EndpointConfigArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEndpointInputRequestTypeDef = TypedDict(
    "CreateEndpointInputRequestTypeDef",
    {
        "EndpointName": str,
        "EndpointConfigName": str,
        "DeploymentConfig": NotRequired["DeploymentConfigTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateEndpointOutputTypeDef = TypedDict(
    "CreateEndpointOutputTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateExperimentRequestRequestTypeDef = TypedDict(
    "CreateExperimentRequestRequestTypeDef",
    {
        "ExperimentName": str,
        "DisplayName": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateExperimentResponseTypeDef = TypedDict(
    "CreateExperimentResponseTypeDef",
    {
        "ExperimentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFeatureGroupRequestRequestTypeDef = TypedDict(
    "CreateFeatureGroupRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierFeatureName": str,
        "EventTimeFeatureName": str,
        "FeatureDefinitions": Sequence["FeatureDefinitionTypeDef"],
        "OnlineStoreConfig": NotRequired["OnlineStoreConfigTypeDef"],
        "OfflineStoreConfig": NotRequired["OfflineStoreConfigTypeDef"],
        "RoleArn": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateFeatureGroupResponseTypeDef = TypedDict(
    "CreateFeatureGroupResponseTypeDef",
    {
        "FeatureGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFlowDefinitionRequestRequestTypeDef = TypedDict(
    "CreateFlowDefinitionRequestRequestTypeDef",
    {
        "FlowDefinitionName": str,
        "HumanLoopConfig": "HumanLoopConfigTypeDef",
        "OutputConfig": "FlowDefinitionOutputConfigTypeDef",
        "RoleArn": str,
        "HumanLoopRequestSource": NotRequired["HumanLoopRequestSourceTypeDef"],
        "HumanLoopActivationConfig": NotRequired["HumanLoopActivationConfigTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateFlowDefinitionResponseTypeDef = TypedDict(
    "CreateFlowDefinitionResponseTypeDef",
    {
        "FlowDefinitionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateHumanTaskUiRequestRequestTypeDef = TypedDict(
    "CreateHumanTaskUiRequestRequestTypeDef",
    {
        "HumanTaskUiName": str,
        "UiTemplate": "UiTemplateTypeDef",
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateHumanTaskUiResponseTypeDef = TypedDict(
    "CreateHumanTaskUiResponseTypeDef",
    {
        "HumanTaskUiArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateHyperParameterTuningJobRequestRequestTypeDef = TypedDict(
    "CreateHyperParameterTuningJobRequestRequestTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobConfig": "HyperParameterTuningJobConfigTypeDef",
        "TrainingJobDefinition": NotRequired["HyperParameterTrainingJobDefinitionTypeDef"],
        "TrainingJobDefinitions": NotRequired[
            Sequence["HyperParameterTrainingJobDefinitionTypeDef"]
        ],
        "WarmStartConfig": NotRequired["HyperParameterTuningJobWarmStartConfigTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateHyperParameterTuningJobResponseTypeDef = TypedDict(
    "CreateHyperParameterTuningJobResponseTypeDef",
    {
        "HyperParameterTuningJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateImageRequestRequestTypeDef = TypedDict(
    "CreateImageRequestRequestTypeDef",
    {
        "ImageName": str,
        "RoleArn": str,
        "Description": NotRequired[str],
        "DisplayName": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateImageResponseTypeDef = TypedDict(
    "CreateImageResponseTypeDef",
    {
        "ImageArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateImageVersionRequestRequestTypeDef = TypedDict(
    "CreateImageVersionRequestRequestTypeDef",
    {
        "BaseImage": str,
        "ClientToken": str,
        "ImageName": str,
    },
)

CreateImageVersionResponseTypeDef = TypedDict(
    "CreateImageVersionResponseTypeDef",
    {
        "ImageVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInferenceRecommendationsJobRequestRequestTypeDef = TypedDict(
    "CreateInferenceRecommendationsJobRequestRequestTypeDef",
    {
        "JobName": str,
        "JobType": RecommendationJobTypeType,
        "RoleArn": str,
        "InputConfig": "RecommendationJobInputConfigTypeDef",
        "JobDescription": NotRequired[str],
        "StoppingConditions": NotRequired["RecommendationJobStoppingConditionsTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateInferenceRecommendationsJobResponseTypeDef = TypedDict(
    "CreateInferenceRecommendationsJobResponseTypeDef",
    {
        "JobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLabelingJobRequestRequestTypeDef = TypedDict(
    "CreateLabelingJobRequestRequestTypeDef",
    {
        "LabelingJobName": str,
        "LabelAttributeName": str,
        "InputConfig": "LabelingJobInputConfigTypeDef",
        "OutputConfig": "LabelingJobOutputConfigTypeDef",
        "RoleArn": str,
        "HumanTaskConfig": "HumanTaskConfigTypeDef",
        "LabelCategoryConfigS3Uri": NotRequired[str],
        "StoppingConditions": NotRequired["LabelingJobStoppingConditionsTypeDef"],
        "LabelingJobAlgorithmsConfig": NotRequired["LabelingJobAlgorithmsConfigTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateLabelingJobResponseTypeDef = TypedDict(
    "CreateLabelingJobResponseTypeDef",
    {
        "LabelingJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateModelBiasJobDefinitionRequestRequestTypeDef = TypedDict(
    "CreateModelBiasJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
        "ModelBiasAppSpecification": "ModelBiasAppSpecificationTypeDef",
        "ModelBiasJobInput": "ModelBiasJobInputTypeDef",
        "ModelBiasJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "RoleArn": str,
        "ModelBiasBaselineConfig": NotRequired["ModelBiasBaselineConfigTypeDef"],
        "NetworkConfig": NotRequired["MonitoringNetworkConfigTypeDef"],
        "StoppingCondition": NotRequired["MonitoringStoppingConditionTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateModelBiasJobDefinitionResponseTypeDef = TypedDict(
    "CreateModelBiasJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateModelExplainabilityJobDefinitionRequestRequestTypeDef = TypedDict(
    "CreateModelExplainabilityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
        "ModelExplainabilityAppSpecification": "ModelExplainabilityAppSpecificationTypeDef",
        "ModelExplainabilityJobInput": "ModelExplainabilityJobInputTypeDef",
        "ModelExplainabilityJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "RoleArn": str,
        "ModelExplainabilityBaselineConfig": NotRequired[
            "ModelExplainabilityBaselineConfigTypeDef"
        ],
        "NetworkConfig": NotRequired["MonitoringNetworkConfigTypeDef"],
        "StoppingCondition": NotRequired["MonitoringStoppingConditionTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateModelExplainabilityJobDefinitionResponseTypeDef = TypedDict(
    "CreateModelExplainabilityJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateModelInputRequestTypeDef = TypedDict(
    "CreateModelInputRequestTypeDef",
    {
        "ModelName": str,
        "ExecutionRoleArn": str,
        "PrimaryContainer": NotRequired["ContainerDefinitionTypeDef"],
        "Containers": NotRequired[Sequence["ContainerDefinitionTypeDef"]],
        "InferenceExecutionConfig": NotRequired["InferenceExecutionConfigTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "EnableNetworkIsolation": NotRequired[bool],
    },
)

CreateModelOutputTypeDef = TypedDict(
    "CreateModelOutputTypeDef",
    {
        "ModelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateModelPackageGroupInputRequestTypeDef = TypedDict(
    "CreateModelPackageGroupInputRequestTypeDef",
    {
        "ModelPackageGroupName": str,
        "ModelPackageGroupDescription": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateModelPackageGroupOutputTypeDef = TypedDict(
    "CreateModelPackageGroupOutputTypeDef",
    {
        "ModelPackageGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateModelPackageInputRequestTypeDef = TypedDict(
    "CreateModelPackageInputRequestTypeDef",
    {
        "ModelPackageName": NotRequired[str],
        "ModelPackageGroupName": NotRequired[str],
        "ModelPackageDescription": NotRequired[str],
        "InferenceSpecification": NotRequired["InferenceSpecificationTypeDef"],
        "ValidationSpecification": NotRequired["ModelPackageValidationSpecificationTypeDef"],
        "SourceAlgorithmSpecification": NotRequired["SourceAlgorithmSpecificationTypeDef"],
        "CertifyForMarketplace": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ModelApprovalStatus": NotRequired[ModelApprovalStatusType],
        "MetadataProperties": NotRequired["MetadataPropertiesTypeDef"],
        "ModelMetrics": NotRequired["ModelMetricsTypeDef"],
        "ClientToken": NotRequired[str],
        "CustomerMetadataProperties": NotRequired[Mapping[str, str]],
        "DriftCheckBaselines": NotRequired["DriftCheckBaselinesTypeDef"],
        "Domain": NotRequired[str],
        "Task": NotRequired[str],
        "SamplePayloadUrl": NotRequired[str],
        "AdditionalInferenceSpecifications": NotRequired[
            Sequence["AdditionalInferenceSpecificationDefinitionTypeDef"]
        ],
    },
)

CreateModelPackageOutputTypeDef = TypedDict(
    "CreateModelPackageOutputTypeDef",
    {
        "ModelPackageArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateModelQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "CreateModelQualityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
        "ModelQualityAppSpecification": "ModelQualityAppSpecificationTypeDef",
        "ModelQualityJobInput": "ModelQualityJobInputTypeDef",
        "ModelQualityJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "RoleArn": str,
        "ModelQualityBaselineConfig": NotRequired["ModelQualityBaselineConfigTypeDef"],
        "NetworkConfig": NotRequired["MonitoringNetworkConfigTypeDef"],
        "StoppingCondition": NotRequired["MonitoringStoppingConditionTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateModelQualityJobDefinitionResponseTypeDef = TypedDict(
    "CreateModelQualityJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMonitoringScheduleRequestRequestTypeDef = TypedDict(
    "CreateMonitoringScheduleRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringScheduleConfig": "MonitoringScheduleConfigTypeDef",
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateMonitoringScheduleResponseTypeDef = TypedDict(
    "CreateMonitoringScheduleResponseTypeDef",
    {
        "MonitoringScheduleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateNotebookInstanceInputRequestTypeDef = TypedDict(
    "CreateNotebookInstanceInputRequestTypeDef",
    {
        "NotebookInstanceName": str,
        "InstanceType": InstanceTypeType,
        "RoleArn": str,
        "SubnetId": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "KmsKeyId": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "LifecycleConfigName": NotRequired[str],
        "DirectInternetAccess": NotRequired[DirectInternetAccessType],
        "VolumeSizeInGB": NotRequired[int],
        "AcceleratorTypes": NotRequired[Sequence[NotebookInstanceAcceleratorTypeType]],
        "DefaultCodeRepository": NotRequired[str],
        "AdditionalCodeRepositories": NotRequired[Sequence[str]],
        "RootAccess": NotRequired[RootAccessType],
        "PlatformIdentifier": NotRequired[str],
    },
)

CreateNotebookInstanceLifecycleConfigInputRequestTypeDef = TypedDict(
    "CreateNotebookInstanceLifecycleConfigInputRequestTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
        "OnCreate": NotRequired[Sequence["NotebookInstanceLifecycleHookTypeDef"]],
        "OnStart": NotRequired[Sequence["NotebookInstanceLifecycleHookTypeDef"]],
    },
)

CreateNotebookInstanceLifecycleConfigOutputTypeDef = TypedDict(
    "CreateNotebookInstanceLifecycleConfigOutputTypeDef",
    {
        "NotebookInstanceLifecycleConfigArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateNotebookInstanceOutputTypeDef = TypedDict(
    "CreateNotebookInstanceOutputTypeDef",
    {
        "NotebookInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePipelineRequestRequestTypeDef = TypedDict(
    "CreatePipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
        "ClientRequestToken": str,
        "RoleArn": str,
        "PipelineDisplayName": NotRequired[str],
        "PipelineDefinition": NotRequired[str],
        "PipelineDefinitionS3Location": NotRequired["PipelineDefinitionS3LocationTypeDef"],
        "PipelineDescription": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ParallelismConfiguration": NotRequired["ParallelismConfigurationTypeDef"],
    },
)

CreatePipelineResponseTypeDef = TypedDict(
    "CreatePipelineResponseTypeDef",
    {
        "PipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePresignedDomainUrlRequestRequestTypeDef = TypedDict(
    "CreatePresignedDomainUrlRequestRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
        "SessionExpirationDurationInSeconds": NotRequired[int],
        "ExpiresInSeconds": NotRequired[int],
    },
)

CreatePresignedDomainUrlResponseTypeDef = TypedDict(
    "CreatePresignedDomainUrlResponseTypeDef",
    {
        "AuthorizedUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePresignedNotebookInstanceUrlInputRequestTypeDef = TypedDict(
    "CreatePresignedNotebookInstanceUrlInputRequestTypeDef",
    {
        "NotebookInstanceName": str,
        "SessionExpirationDurationInSeconds": NotRequired[int],
    },
)

CreatePresignedNotebookInstanceUrlOutputTypeDef = TypedDict(
    "CreatePresignedNotebookInstanceUrlOutputTypeDef",
    {
        "AuthorizedUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProcessingJobRequestRequestTypeDef = TypedDict(
    "CreateProcessingJobRequestRequestTypeDef",
    {
        "ProcessingJobName": str,
        "ProcessingResources": "ProcessingResourcesTypeDef",
        "AppSpecification": "AppSpecificationTypeDef",
        "RoleArn": str,
        "ProcessingInputs": NotRequired[Sequence["ProcessingInputTypeDef"]],
        "ProcessingOutputConfig": NotRequired["ProcessingOutputConfigTypeDef"],
        "StoppingCondition": NotRequired["ProcessingStoppingConditionTypeDef"],
        "Environment": NotRequired[Mapping[str, str]],
        "NetworkConfig": NotRequired["NetworkConfigTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ExperimentConfig": NotRequired["ExperimentConfigTypeDef"],
    },
)

CreateProcessingJobResponseTypeDef = TypedDict(
    "CreateProcessingJobResponseTypeDef",
    {
        "ProcessingJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProjectInputRequestTypeDef = TypedDict(
    "CreateProjectInputRequestTypeDef",
    {
        "ProjectName": str,
        "ServiceCatalogProvisioningDetails": "ServiceCatalogProvisioningDetailsTypeDef",
        "ProjectDescription": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateProjectOutputTypeDef = TypedDict(
    "CreateProjectOutputTypeDef",
    {
        "ProjectArn": str,
        "ProjectId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStudioLifecycleConfigRequestRequestTypeDef = TypedDict(
    "CreateStudioLifecycleConfigRequestRequestTypeDef",
    {
        "StudioLifecycleConfigName": str,
        "StudioLifecycleConfigContent": str,
        "StudioLifecycleConfigAppType": StudioLifecycleConfigAppTypeType,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateStudioLifecycleConfigResponseTypeDef = TypedDict(
    "CreateStudioLifecycleConfigResponseTypeDef",
    {
        "StudioLifecycleConfigArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTrainingJobRequestRequestTypeDef = TypedDict(
    "CreateTrainingJobRequestRequestTypeDef",
    {
        "TrainingJobName": str,
        "AlgorithmSpecification": "AlgorithmSpecificationTypeDef",
        "RoleArn": str,
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "ResourceConfig": "ResourceConfigTypeDef",
        "StoppingCondition": "StoppingConditionTypeDef",
        "HyperParameters": NotRequired[Mapping[str, str]],
        "InputDataConfig": NotRequired[Sequence["ChannelTypeDef"]],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "EnableNetworkIsolation": NotRequired[bool],
        "EnableInterContainerTrafficEncryption": NotRequired[bool],
        "EnableManagedSpotTraining": NotRequired[bool],
        "CheckpointConfig": NotRequired["CheckpointConfigTypeDef"],
        "DebugHookConfig": NotRequired["DebugHookConfigTypeDef"],
        "DebugRuleConfigurations": NotRequired[Sequence["DebugRuleConfigurationTypeDef"]],
        "TensorBoardOutputConfig": NotRequired["TensorBoardOutputConfigTypeDef"],
        "ExperimentConfig": NotRequired["ExperimentConfigTypeDef"],
        "ProfilerConfig": NotRequired["ProfilerConfigTypeDef"],
        "ProfilerRuleConfigurations": NotRequired[Sequence["ProfilerRuleConfigurationTypeDef"]],
        "Environment": NotRequired[Mapping[str, str]],
        "RetryStrategy": NotRequired["RetryStrategyTypeDef"],
    },
)

CreateTrainingJobResponseTypeDef = TypedDict(
    "CreateTrainingJobResponseTypeDef",
    {
        "TrainingJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTransformJobRequestRequestTypeDef = TypedDict(
    "CreateTransformJobRequestRequestTypeDef",
    {
        "TransformJobName": str,
        "ModelName": str,
        "TransformInput": "TransformInputTypeDef",
        "TransformOutput": "TransformOutputTypeDef",
        "TransformResources": "TransformResourcesTypeDef",
        "MaxConcurrentTransforms": NotRequired[int],
        "ModelClientConfig": NotRequired["ModelClientConfigTypeDef"],
        "MaxPayloadInMB": NotRequired[int],
        "BatchStrategy": NotRequired[BatchStrategyType],
        "Environment": NotRequired[Mapping[str, str]],
        "DataProcessing": NotRequired["DataProcessingTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ExperimentConfig": NotRequired["ExperimentConfigTypeDef"],
    },
)

CreateTransformJobResponseTypeDef = TypedDict(
    "CreateTransformJobResponseTypeDef",
    {
        "TransformJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTrialComponentRequestRequestTypeDef = TypedDict(
    "CreateTrialComponentRequestRequestTypeDef",
    {
        "TrialComponentName": str,
        "DisplayName": NotRequired[str],
        "Status": NotRequired["TrialComponentStatusTypeDef"],
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "Parameters": NotRequired[Mapping[str, "TrialComponentParameterValueTypeDef"]],
        "InputArtifacts": NotRequired[Mapping[str, "TrialComponentArtifactTypeDef"]],
        "OutputArtifacts": NotRequired[Mapping[str, "TrialComponentArtifactTypeDef"]],
        "MetadataProperties": NotRequired["MetadataPropertiesTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateTrialComponentResponseTypeDef = TypedDict(
    "CreateTrialComponentResponseTypeDef",
    {
        "TrialComponentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTrialRequestRequestTypeDef = TypedDict(
    "CreateTrialRequestRequestTypeDef",
    {
        "TrialName": str,
        "ExperimentName": str,
        "DisplayName": NotRequired[str],
        "MetadataProperties": NotRequired["MetadataPropertiesTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateTrialResponseTypeDef = TypedDict(
    "CreateTrialResponseTypeDef",
    {
        "TrialArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserProfileRequestRequestTypeDef = TypedDict(
    "CreateUserProfileRequestRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
        "SingleSignOnUserIdentifier": NotRequired[str],
        "SingleSignOnUserValue": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "UserSettings": NotRequired["UserSettingsTypeDef"],
    },
)

CreateUserProfileResponseTypeDef = TypedDict(
    "CreateUserProfileResponseTypeDef",
    {
        "UserProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorkforceRequestRequestTypeDef = TypedDict(
    "CreateWorkforceRequestRequestTypeDef",
    {
        "WorkforceName": str,
        "CognitoConfig": NotRequired["CognitoConfigTypeDef"],
        "OidcConfig": NotRequired["OidcConfigTypeDef"],
        "SourceIpConfig": NotRequired["SourceIpConfigTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateWorkforceResponseTypeDef = TypedDict(
    "CreateWorkforceResponseTypeDef",
    {
        "WorkforceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorkteamRequestRequestTypeDef = TypedDict(
    "CreateWorkteamRequestRequestTypeDef",
    {
        "WorkteamName": str,
        "MemberDefinitions": Sequence["MemberDefinitionTypeDef"],
        "Description": str,
        "WorkforceName": NotRequired[str],
        "NotificationConfiguration": NotRequired["NotificationConfigurationTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateWorkteamResponseTypeDef = TypedDict(
    "CreateWorkteamResponseTypeDef",
    {
        "WorkteamArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomImageTypeDef = TypedDict(
    "CustomImageTypeDef",
    {
        "ImageName": str,
        "AppImageConfigName": str,
        "ImageVersionNumber": NotRequired[int],
    },
)

DataCaptureConfigSummaryTypeDef = TypedDict(
    "DataCaptureConfigSummaryTypeDef",
    {
        "EnableCapture": bool,
        "CaptureStatus": CaptureStatusType,
        "CurrentSamplingPercentage": int,
        "DestinationS3Uri": str,
        "KmsKeyId": str,
    },
)

DataCaptureConfigTypeDef = TypedDict(
    "DataCaptureConfigTypeDef",
    {
        "InitialSamplingPercentage": int,
        "DestinationS3Uri": str,
        "CaptureOptions": Sequence["CaptureOptionTypeDef"],
        "EnableCapture": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "CaptureContentTypeHeader": NotRequired["CaptureContentTypeHeaderTypeDef"],
    },
)

DataCatalogConfigTypeDef = TypedDict(
    "DataCatalogConfigTypeDef",
    {
        "TableName": str,
        "Catalog": str,
        "Database": str,
    },
)

DataProcessingTypeDef = TypedDict(
    "DataProcessingTypeDef",
    {
        "InputFilter": NotRequired[str],
        "OutputFilter": NotRequired[str],
        "JoinSource": NotRequired[JoinSourceType],
    },
)

DataQualityAppSpecificationTypeDef = TypedDict(
    "DataQualityAppSpecificationTypeDef",
    {
        "ImageUri": str,
        "ContainerEntrypoint": NotRequired[Sequence[str]],
        "ContainerArguments": NotRequired[Sequence[str]],
        "RecordPreprocessorSourceUri": NotRequired[str],
        "PostAnalyticsProcessorSourceUri": NotRequired[str],
        "Environment": NotRequired[Mapping[str, str]],
    },
)

DataQualityBaselineConfigTypeDef = TypedDict(
    "DataQualityBaselineConfigTypeDef",
    {
        "BaseliningJobName": NotRequired[str],
        "ConstraintsResource": NotRequired["MonitoringConstraintsResourceTypeDef"],
        "StatisticsResource": NotRequired["MonitoringStatisticsResourceTypeDef"],
    },
)

DataQualityJobInputTypeDef = TypedDict(
    "DataQualityJobInputTypeDef",
    {
        "EndpointInput": "EndpointInputTypeDef",
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "S3DataSource": NotRequired["S3DataSourceTypeDef"],
        "FileSystemDataSource": NotRequired["FileSystemDataSourceTypeDef"],
    },
)

DatasetDefinitionTypeDef = TypedDict(
    "DatasetDefinitionTypeDef",
    {
        "AthenaDatasetDefinition": NotRequired["AthenaDatasetDefinitionTypeDef"],
        "RedshiftDatasetDefinition": NotRequired["RedshiftDatasetDefinitionTypeDef"],
        "LocalPath": NotRequired[str],
        "DataDistributionType": NotRequired[DataDistributionTypeType],
        "InputMode": NotRequired[InputModeType],
    },
)

DebugHookConfigTypeDef = TypedDict(
    "DebugHookConfigTypeDef",
    {
        "S3OutputPath": str,
        "LocalPath": NotRequired[str],
        "HookParameters": NotRequired[Mapping[str, str]],
        "CollectionConfigurations": NotRequired[Sequence["CollectionConfigurationTypeDef"]],
    },
)

DebugRuleConfigurationTypeDef = TypedDict(
    "DebugRuleConfigurationTypeDef",
    {
        "RuleConfigurationName": str,
        "RuleEvaluatorImage": str,
        "LocalPath": NotRequired[str],
        "S3OutputPath": NotRequired[str],
        "InstanceType": NotRequired[ProcessingInstanceTypeType],
        "VolumeSizeInGB": NotRequired[int],
        "RuleParameters": NotRequired[Mapping[str, str]],
    },
)

DebugRuleEvaluationStatusTypeDef = TypedDict(
    "DebugRuleEvaluationStatusTypeDef",
    {
        "RuleConfigurationName": NotRequired[str],
        "RuleEvaluationJobArn": NotRequired[str],
        "RuleEvaluationStatus": NotRequired[RuleEvaluationStatusType],
        "StatusDetails": NotRequired[str],
        "LastModifiedTime": NotRequired[datetime],
    },
)

DeleteActionRequestRequestTypeDef = TypedDict(
    "DeleteActionRequestRequestTypeDef",
    {
        "ActionName": str,
    },
)

DeleteActionResponseTypeDef = TypedDict(
    "DeleteActionResponseTypeDef",
    {
        "ActionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAlgorithmInputRequestTypeDef = TypedDict(
    "DeleteAlgorithmInputRequestTypeDef",
    {
        "AlgorithmName": str,
    },
)

DeleteAppImageConfigRequestRequestTypeDef = TypedDict(
    "DeleteAppImageConfigRequestRequestTypeDef",
    {
        "AppImageConfigName": str,
    },
)

DeleteAppRequestRequestTypeDef = TypedDict(
    "DeleteAppRequestRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
        "AppType": AppTypeType,
        "AppName": str,
    },
)

DeleteArtifactRequestRequestTypeDef = TypedDict(
    "DeleteArtifactRequestRequestTypeDef",
    {
        "ArtifactArn": NotRequired[str],
        "Source": NotRequired["ArtifactSourceTypeDef"],
    },
)

DeleteArtifactResponseTypeDef = TypedDict(
    "DeleteArtifactResponseTypeDef",
    {
        "ArtifactArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAssociationRequestRequestTypeDef = TypedDict(
    "DeleteAssociationRequestRequestTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
    },
)

DeleteAssociationResponseTypeDef = TypedDict(
    "DeleteAssociationResponseTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCodeRepositoryInputRequestTypeDef = TypedDict(
    "DeleteCodeRepositoryInputRequestTypeDef",
    {
        "CodeRepositoryName": str,
    },
)

DeleteContextRequestRequestTypeDef = TypedDict(
    "DeleteContextRequestRequestTypeDef",
    {
        "ContextName": str,
    },
)

DeleteContextResponseTypeDef = TypedDict(
    "DeleteContextResponseTypeDef",
    {
        "ContextArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDataQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteDataQualityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DeleteDeviceFleetRequestRequestTypeDef = TypedDict(
    "DeleteDeviceFleetRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
    },
)

DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "DomainId": str,
        "RetentionPolicy": NotRequired["RetentionPolicyTypeDef"],
    },
)

DeleteEndpointConfigInputRequestTypeDef = TypedDict(
    "DeleteEndpointConfigInputRequestTypeDef",
    {
        "EndpointConfigName": str,
    },
)

DeleteEndpointInputRequestTypeDef = TypedDict(
    "DeleteEndpointInputRequestTypeDef",
    {
        "EndpointName": str,
    },
)

DeleteExperimentRequestRequestTypeDef = TypedDict(
    "DeleteExperimentRequestRequestTypeDef",
    {
        "ExperimentName": str,
    },
)

DeleteExperimentResponseTypeDef = TypedDict(
    "DeleteExperimentResponseTypeDef",
    {
        "ExperimentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFeatureGroupRequestRequestTypeDef = TypedDict(
    "DeleteFeatureGroupRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
    },
)

DeleteFlowDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteFlowDefinitionRequestRequestTypeDef",
    {
        "FlowDefinitionName": str,
    },
)

DeleteHumanTaskUiRequestRequestTypeDef = TypedDict(
    "DeleteHumanTaskUiRequestRequestTypeDef",
    {
        "HumanTaskUiName": str,
    },
)

DeleteImageRequestRequestTypeDef = TypedDict(
    "DeleteImageRequestRequestTypeDef",
    {
        "ImageName": str,
    },
)

DeleteImageVersionRequestRequestTypeDef = TypedDict(
    "DeleteImageVersionRequestRequestTypeDef",
    {
        "ImageName": str,
        "Version": int,
    },
)

DeleteModelBiasJobDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteModelBiasJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DeleteModelExplainabilityJobDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteModelExplainabilityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DeleteModelInputRequestTypeDef = TypedDict(
    "DeleteModelInputRequestTypeDef",
    {
        "ModelName": str,
    },
)

DeleteModelPackageGroupInputRequestTypeDef = TypedDict(
    "DeleteModelPackageGroupInputRequestTypeDef",
    {
        "ModelPackageGroupName": str,
    },
)

DeleteModelPackageGroupPolicyInputRequestTypeDef = TypedDict(
    "DeleteModelPackageGroupPolicyInputRequestTypeDef",
    {
        "ModelPackageGroupName": str,
    },
)

DeleteModelPackageInputRequestTypeDef = TypedDict(
    "DeleteModelPackageInputRequestTypeDef",
    {
        "ModelPackageName": str,
    },
)

DeleteModelQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteModelQualityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DeleteMonitoringScheduleRequestRequestTypeDef = TypedDict(
    "DeleteMonitoringScheduleRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
    },
)

DeleteNotebookInstanceInputRequestTypeDef = TypedDict(
    "DeleteNotebookInstanceInputRequestTypeDef",
    {
        "NotebookInstanceName": str,
    },
)

DeleteNotebookInstanceLifecycleConfigInputRequestTypeDef = TypedDict(
    "DeleteNotebookInstanceLifecycleConfigInputRequestTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
    },
)

DeletePipelineRequestRequestTypeDef = TypedDict(
    "DeletePipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
        "ClientRequestToken": str,
    },
)

DeletePipelineResponseTypeDef = TypedDict(
    "DeletePipelineResponseTypeDef",
    {
        "PipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProjectInputRequestTypeDef = TypedDict(
    "DeleteProjectInputRequestTypeDef",
    {
        "ProjectName": str,
    },
)

DeleteStudioLifecycleConfigRequestRequestTypeDef = TypedDict(
    "DeleteStudioLifecycleConfigRequestRequestTypeDef",
    {
        "StudioLifecycleConfigName": str,
    },
)

DeleteTagsInputRequestTypeDef = TypedDict(
    "DeleteTagsInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

DeleteTrialComponentRequestRequestTypeDef = TypedDict(
    "DeleteTrialComponentRequestRequestTypeDef",
    {
        "TrialComponentName": str,
    },
)

DeleteTrialComponentResponseTypeDef = TypedDict(
    "DeleteTrialComponentResponseTypeDef",
    {
        "TrialComponentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTrialRequestRequestTypeDef = TypedDict(
    "DeleteTrialRequestRequestTypeDef",
    {
        "TrialName": str,
    },
)

DeleteTrialResponseTypeDef = TypedDict(
    "DeleteTrialResponseTypeDef",
    {
        "TrialArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUserProfileRequestRequestTypeDef = TypedDict(
    "DeleteUserProfileRequestRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
    },
)

DeleteWorkforceRequestRequestTypeDef = TypedDict(
    "DeleteWorkforceRequestRequestTypeDef",
    {
        "WorkforceName": str,
    },
)

DeleteWorkteamRequestRequestTypeDef = TypedDict(
    "DeleteWorkteamRequestRequestTypeDef",
    {
        "WorkteamName": str,
    },
)

DeleteWorkteamResponseTypeDef = TypedDict(
    "DeleteWorkteamResponseTypeDef",
    {
        "Success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeployedImageTypeDef = TypedDict(
    "DeployedImageTypeDef",
    {
        "SpecifiedImage": NotRequired[str],
        "ResolvedImage": NotRequired[str],
        "ResolutionTime": NotRequired[datetime],
    },
)

DeploymentConfigTypeDef = TypedDict(
    "DeploymentConfigTypeDef",
    {
        "BlueGreenUpdatePolicy": "BlueGreenUpdatePolicyTypeDef",
        "AutoRollbackConfiguration": NotRequired["AutoRollbackConfigTypeDef"],
    },
)

DeregisterDevicesRequestRequestTypeDef = TypedDict(
    "DeregisterDevicesRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
        "DeviceNames": Sequence[str],
    },
)

DescribeActionRequestRequestTypeDef = TypedDict(
    "DescribeActionRequestRequestTypeDef",
    {
        "ActionName": str,
    },
)

DescribeActionResponseTypeDef = TypedDict(
    "DescribeActionResponseTypeDef",
    {
        "ActionName": str,
        "ActionArn": str,
        "Source": "ActionSourceTypeDef",
        "ActionType": str,
        "Description": str,
        "Status": ActionStatusType,
        "Properties": Dict[str, str],
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "LineageGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAlgorithmInputRequestTypeDef = TypedDict(
    "DescribeAlgorithmInputRequestTypeDef",
    {
        "AlgorithmName": str,
    },
)

DescribeAlgorithmOutputTypeDef = TypedDict(
    "DescribeAlgorithmOutputTypeDef",
    {
        "AlgorithmName": str,
        "AlgorithmArn": str,
        "AlgorithmDescription": str,
        "CreationTime": datetime,
        "TrainingSpecification": "TrainingSpecificationTypeDef",
        "InferenceSpecification": "InferenceSpecificationTypeDef",
        "ValidationSpecification": "AlgorithmValidationSpecificationTypeDef",
        "AlgorithmStatus": AlgorithmStatusType,
        "AlgorithmStatusDetails": "AlgorithmStatusDetailsTypeDef",
        "ProductId": str,
        "CertifyForMarketplace": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppImageConfigRequestRequestTypeDef = TypedDict(
    "DescribeAppImageConfigRequestRequestTypeDef",
    {
        "AppImageConfigName": str,
    },
)

DescribeAppImageConfigResponseTypeDef = TypedDict(
    "DescribeAppImageConfigResponseTypeDef",
    {
        "AppImageConfigArn": str,
        "AppImageConfigName": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "KernelGatewayImageConfig": "KernelGatewayImageConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppRequestRequestTypeDef = TypedDict(
    "DescribeAppRequestRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
        "AppType": AppTypeType,
        "AppName": str,
    },
)

DescribeAppResponseTypeDef = TypedDict(
    "DescribeAppResponseTypeDef",
    {
        "AppArn": str,
        "AppType": AppTypeType,
        "AppName": str,
        "DomainId": str,
        "UserProfileName": str,
        "Status": AppStatusType,
        "LastHealthCheckTimestamp": datetime,
        "LastUserActivityTimestamp": datetime,
        "CreationTime": datetime,
        "FailureReason": str,
        "ResourceSpec": "ResourceSpecTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeArtifactRequestRequestTypeDef = TypedDict(
    "DescribeArtifactRequestRequestTypeDef",
    {
        "ArtifactArn": str,
    },
)

DescribeArtifactResponseTypeDef = TypedDict(
    "DescribeArtifactResponseTypeDef",
    {
        "ArtifactName": str,
        "ArtifactArn": str,
        "Source": "ArtifactSourceTypeDef",
        "ArtifactType": str,
        "Properties": Dict[str, str],
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "LineageGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAutoMLJobRequestRequestTypeDef = TypedDict(
    "DescribeAutoMLJobRequestRequestTypeDef",
    {
        "AutoMLJobName": str,
    },
)

DescribeAutoMLJobResponseTypeDef = TypedDict(
    "DescribeAutoMLJobResponseTypeDef",
    {
        "AutoMLJobName": str,
        "AutoMLJobArn": str,
        "InputDataConfig": List["AutoMLChannelTypeDef"],
        "OutputDataConfig": "AutoMLOutputDataConfigTypeDef",
        "RoleArn": str,
        "AutoMLJobObjective": "AutoMLJobObjectiveTypeDef",
        "ProblemType": ProblemTypeType,
        "AutoMLJobConfig": "AutoMLJobConfigTypeDef",
        "CreationTime": datetime,
        "EndTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "PartialFailureReasons": List["AutoMLPartialFailureReasonTypeDef"],
        "BestCandidate": "AutoMLCandidateTypeDef",
        "AutoMLJobStatus": AutoMLJobStatusType,
        "AutoMLJobSecondaryStatus": AutoMLJobSecondaryStatusType,
        "GenerateCandidateDefinitionsOnly": bool,
        "AutoMLJobArtifacts": "AutoMLJobArtifactsTypeDef",
        "ResolvedAttributes": "ResolvedAttributesTypeDef",
        "ModelDeployConfig": "ModelDeployConfigTypeDef",
        "ModelDeployResult": "ModelDeployResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCodeRepositoryInputRequestTypeDef = TypedDict(
    "DescribeCodeRepositoryInputRequestTypeDef",
    {
        "CodeRepositoryName": str,
    },
)

DescribeCodeRepositoryOutputTypeDef = TypedDict(
    "DescribeCodeRepositoryOutputTypeDef",
    {
        "CodeRepositoryName": str,
        "CodeRepositoryArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "GitConfig": "GitConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCompilationJobRequestRequestTypeDef = TypedDict(
    "DescribeCompilationJobRequestRequestTypeDef",
    {
        "CompilationJobName": str,
    },
)

DescribeCompilationJobResponseTypeDef = TypedDict(
    "DescribeCompilationJobResponseTypeDef",
    {
        "CompilationJobName": str,
        "CompilationJobArn": str,
        "CompilationJobStatus": CompilationJobStatusType,
        "CompilationStartTime": datetime,
        "CompilationEndTime": datetime,
        "StoppingCondition": "StoppingConditionTypeDef",
        "InferenceImage": str,
        "ModelPackageVersionArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "ModelArtifacts": "ModelArtifactsTypeDef",
        "ModelDigests": "ModelDigestsTypeDef",
        "RoleArn": str,
        "InputConfig": "InputConfigTypeDef",
        "OutputConfig": "OutputConfigTypeDef",
        "VpcConfig": "NeoVpcConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContextRequestRequestTypeDef = TypedDict(
    "DescribeContextRequestRequestTypeDef",
    {
        "ContextName": str,
    },
)

DescribeContextResponseTypeDef = TypedDict(
    "DescribeContextResponseTypeDef",
    {
        "ContextName": str,
        "ContextArn": str,
        "Source": "ContextSourceTypeDef",
        "ContextType": str,
        "Description": str,
        "Properties": Dict[str, str],
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "LineageGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeDataQualityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DescribeDataQualityJobDefinitionResponseTypeDef = TypedDict(
    "DescribeDataQualityJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "JobDefinitionName": str,
        "CreationTime": datetime,
        "DataQualityBaselineConfig": "DataQualityBaselineConfigTypeDef",
        "DataQualityAppSpecification": "DataQualityAppSpecificationTypeDef",
        "DataQualityJobInput": "DataQualityJobInputTypeDef",
        "DataQualityJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "NetworkConfig": "MonitoringNetworkConfigTypeDef",
        "RoleArn": str,
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeviceFleetRequestRequestTypeDef = TypedDict(
    "DescribeDeviceFleetRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
    },
)

DescribeDeviceFleetResponseTypeDef = TypedDict(
    "DescribeDeviceFleetResponseTypeDef",
    {
        "DeviceFleetName": str,
        "DeviceFleetArn": str,
        "OutputConfig": "EdgeOutputConfigTypeDef",
        "Description": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "RoleArn": str,
        "IotRoleAlias": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeviceRequestRequestTypeDef = TypedDict(
    "DescribeDeviceRequestRequestTypeDef",
    {
        "DeviceName": str,
        "DeviceFleetName": str,
        "NextToken": NotRequired[str],
    },
)

DescribeDeviceResponseTypeDef = TypedDict(
    "DescribeDeviceResponseTypeDef",
    {
        "DeviceArn": str,
        "DeviceName": str,
        "Description": str,
        "DeviceFleetName": str,
        "IotThingName": str,
        "RegistrationTime": datetime,
        "LatestHeartbeat": datetime,
        "Models": List["EdgeModelTypeDef"],
        "MaxModels": int,
        "NextToken": str,
        "AgentVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainRequestRequestTypeDef = TypedDict(
    "DescribeDomainRequestRequestTypeDef",
    {
        "DomainId": str,
    },
)

DescribeDomainResponseTypeDef = TypedDict(
    "DescribeDomainResponseTypeDef",
    {
        "DomainArn": str,
        "DomainId": str,
        "DomainName": str,
        "HomeEfsFileSystemId": str,
        "SingleSignOnManagedApplicationInstanceId": str,
        "Status": DomainStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "AuthMode": AuthModeType,
        "DefaultUserSettings": "UserSettingsTypeDef",
        "AppNetworkAccessType": AppNetworkAccessTypeType,
        "HomeEfsFileSystemKmsKeyId": str,
        "SubnetIds": List[str],
        "Url": str,
        "VpcId": str,
        "KmsKeyId": str,
        "DomainSettings": "DomainSettingsTypeDef",
        "AppSecurityGroupManagement": AppSecurityGroupManagementType,
        "SecurityGroupIdForDomainBoundary": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEdgePackagingJobRequestRequestTypeDef = TypedDict(
    "DescribeEdgePackagingJobRequestRequestTypeDef",
    {
        "EdgePackagingJobName": str,
    },
)

DescribeEdgePackagingJobResponseTypeDef = TypedDict(
    "DescribeEdgePackagingJobResponseTypeDef",
    {
        "EdgePackagingJobArn": str,
        "EdgePackagingJobName": str,
        "CompilationJobName": str,
        "ModelName": str,
        "ModelVersion": str,
        "RoleArn": str,
        "OutputConfig": "EdgeOutputConfigTypeDef",
        "ResourceKey": str,
        "EdgePackagingJobStatus": EdgePackagingJobStatusType,
        "EdgePackagingJobStatusMessage": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ModelArtifact": str,
        "ModelSignature": str,
        "PresetDeploymentOutput": "EdgePresetDeploymentOutputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointConfigInputRequestTypeDef = TypedDict(
    "DescribeEndpointConfigInputRequestTypeDef",
    {
        "EndpointConfigName": str,
    },
)

DescribeEndpointConfigOutputTypeDef = TypedDict(
    "DescribeEndpointConfigOutputTypeDef",
    {
        "EndpointConfigName": str,
        "EndpointConfigArn": str,
        "ProductionVariants": List["ProductionVariantTypeDef"],
        "DataCaptureConfig": "DataCaptureConfigTypeDef",
        "KmsKeyId": str,
        "CreationTime": datetime,
        "AsyncInferenceConfig": "AsyncInferenceConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointInputRequestTypeDef = TypedDict(
    "DescribeEndpointInputRequestTypeDef",
    {
        "EndpointName": str,
    },
)

DescribeEndpointOutputTypeDef = TypedDict(
    "DescribeEndpointOutputTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "EndpointConfigName": str,
        "ProductionVariants": List["ProductionVariantSummaryTypeDef"],
        "DataCaptureConfig": "DataCaptureConfigSummaryTypeDef",
        "EndpointStatus": EndpointStatusType,
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastDeploymentConfig": "DeploymentConfigTypeDef",
        "AsyncInferenceConfig": "AsyncInferenceConfigTypeDef",
        "PendingDeploymentSummary": "PendingDeploymentSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExperimentRequestRequestTypeDef = TypedDict(
    "DescribeExperimentRequestRequestTypeDef",
    {
        "ExperimentName": str,
    },
)

DescribeExperimentResponseTypeDef = TypedDict(
    "DescribeExperimentResponseTypeDef",
    {
        "ExperimentName": str,
        "ExperimentArn": str,
        "DisplayName": str,
        "Source": "ExperimentSourceTypeDef",
        "Description": str,
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFeatureGroupRequestRequestTypeDef = TypedDict(
    "DescribeFeatureGroupRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
        "NextToken": NotRequired[str],
    },
)

DescribeFeatureGroupResponseTypeDef = TypedDict(
    "DescribeFeatureGroupResponseTypeDef",
    {
        "FeatureGroupArn": str,
        "FeatureGroupName": str,
        "RecordIdentifierFeatureName": str,
        "EventTimeFeatureName": str,
        "FeatureDefinitions": List["FeatureDefinitionTypeDef"],
        "CreationTime": datetime,
        "OnlineStoreConfig": "OnlineStoreConfigTypeDef",
        "OfflineStoreConfig": "OfflineStoreConfigTypeDef",
        "RoleArn": str,
        "FeatureGroupStatus": FeatureGroupStatusType,
        "OfflineStoreStatus": "OfflineStoreStatusTypeDef",
        "FailureReason": str,
        "Description": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFlowDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeFlowDefinitionRequestRequestTypeDef",
    {
        "FlowDefinitionName": str,
    },
)

DescribeFlowDefinitionResponseTypeDef = TypedDict(
    "DescribeFlowDefinitionResponseTypeDef",
    {
        "FlowDefinitionArn": str,
        "FlowDefinitionName": str,
        "FlowDefinitionStatus": FlowDefinitionStatusType,
        "CreationTime": datetime,
        "HumanLoopRequestSource": "HumanLoopRequestSourceTypeDef",
        "HumanLoopActivationConfig": "HumanLoopActivationConfigTypeDef",
        "HumanLoopConfig": "HumanLoopConfigTypeDef",
        "OutputConfig": "FlowDefinitionOutputConfigTypeDef",
        "RoleArn": str,
        "FailureReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHumanTaskUiRequestRequestTypeDef = TypedDict(
    "DescribeHumanTaskUiRequestRequestTypeDef",
    {
        "HumanTaskUiName": str,
    },
)

DescribeHumanTaskUiResponseTypeDef = TypedDict(
    "DescribeHumanTaskUiResponseTypeDef",
    {
        "HumanTaskUiArn": str,
        "HumanTaskUiName": str,
        "HumanTaskUiStatus": HumanTaskUiStatusType,
        "CreationTime": datetime,
        "UiTemplate": "UiTemplateInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHyperParameterTuningJobRequestRequestTypeDef = TypedDict(
    "DescribeHyperParameterTuningJobRequestRequestTypeDef",
    {
        "HyperParameterTuningJobName": str,
    },
)

DescribeHyperParameterTuningJobResponseTypeDef = TypedDict(
    "DescribeHyperParameterTuningJobResponseTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobArn": str,
        "HyperParameterTuningJobConfig": "HyperParameterTuningJobConfigTypeDef",
        "TrainingJobDefinition": "HyperParameterTrainingJobDefinitionTypeDef",
        "TrainingJobDefinitions": List["HyperParameterTrainingJobDefinitionTypeDef"],
        "HyperParameterTuningJobStatus": HyperParameterTuningJobStatusType,
        "CreationTime": datetime,
        "HyperParameterTuningEndTime": datetime,
        "LastModifiedTime": datetime,
        "TrainingJobStatusCounters": "TrainingJobStatusCountersTypeDef",
        "ObjectiveStatusCounters": "ObjectiveStatusCountersTypeDef",
        "BestTrainingJob": "HyperParameterTrainingJobSummaryTypeDef",
        "OverallBestTrainingJob": "HyperParameterTrainingJobSummaryTypeDef",
        "WarmStartConfig": "HyperParameterTuningJobWarmStartConfigTypeDef",
        "FailureReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImageRequestRequestTypeDef = TypedDict(
    "DescribeImageRequestRequestTypeDef",
    {
        "ImageName": str,
    },
)

DescribeImageResponseTypeDef = TypedDict(
    "DescribeImageResponseTypeDef",
    {
        "CreationTime": datetime,
        "Description": str,
        "DisplayName": str,
        "FailureReason": str,
        "ImageArn": str,
        "ImageName": str,
        "ImageStatus": ImageStatusType,
        "LastModifiedTime": datetime,
        "RoleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImageVersionRequestRequestTypeDef = TypedDict(
    "DescribeImageVersionRequestRequestTypeDef",
    {
        "ImageName": str,
        "Version": NotRequired[int],
    },
)

DescribeImageVersionResponseTypeDef = TypedDict(
    "DescribeImageVersionResponseTypeDef",
    {
        "BaseImage": str,
        "ContainerImage": str,
        "CreationTime": datetime,
        "FailureReason": str,
        "ImageArn": str,
        "ImageVersionArn": str,
        "ImageVersionStatus": ImageVersionStatusType,
        "LastModifiedTime": datetime,
        "Version": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInferenceRecommendationsJobRequestRequestTypeDef = TypedDict(
    "DescribeInferenceRecommendationsJobRequestRequestTypeDef",
    {
        "JobName": str,
    },
)

DescribeInferenceRecommendationsJobResponseTypeDef = TypedDict(
    "DescribeInferenceRecommendationsJobResponseTypeDef",
    {
        "JobName": str,
        "JobDescription": str,
        "JobType": RecommendationJobTypeType,
        "JobArn": str,
        "RoleArn": str,
        "Status": RecommendationJobStatusType,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "InputConfig": "RecommendationJobInputConfigTypeDef",
        "StoppingConditions": "RecommendationJobStoppingConditionsTypeDef",
        "InferenceRecommendations": List["InferenceRecommendationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLabelingJobRequestRequestTypeDef = TypedDict(
    "DescribeLabelingJobRequestRequestTypeDef",
    {
        "LabelingJobName": str,
    },
)

DescribeLabelingJobResponseTypeDef = TypedDict(
    "DescribeLabelingJobResponseTypeDef",
    {
        "LabelingJobStatus": LabelingJobStatusType,
        "LabelCounters": "LabelCountersTypeDef",
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "JobReferenceCode": str,
        "LabelingJobName": str,
        "LabelingJobArn": str,
        "LabelAttributeName": str,
        "InputConfig": "LabelingJobInputConfigTypeDef",
        "OutputConfig": "LabelingJobOutputConfigTypeDef",
        "RoleArn": str,
        "LabelCategoryConfigS3Uri": str,
        "StoppingConditions": "LabelingJobStoppingConditionsTypeDef",
        "LabelingJobAlgorithmsConfig": "LabelingJobAlgorithmsConfigTypeDef",
        "HumanTaskConfig": "HumanTaskConfigTypeDef",
        "Tags": List["TagTypeDef"],
        "LabelingJobOutput": "LabelingJobOutputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLineageGroupRequestRequestTypeDef = TypedDict(
    "DescribeLineageGroupRequestRequestTypeDef",
    {
        "LineageGroupName": str,
    },
)

DescribeLineageGroupResponseTypeDef = TypedDict(
    "DescribeLineageGroupResponseTypeDef",
    {
        "LineageGroupName": str,
        "LineageGroupArn": str,
        "DisplayName": str,
        "Description": str,
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelBiasJobDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeModelBiasJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DescribeModelBiasJobDefinitionResponseTypeDef = TypedDict(
    "DescribeModelBiasJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "JobDefinitionName": str,
        "CreationTime": datetime,
        "ModelBiasBaselineConfig": "ModelBiasBaselineConfigTypeDef",
        "ModelBiasAppSpecification": "ModelBiasAppSpecificationTypeDef",
        "ModelBiasJobInput": "ModelBiasJobInputTypeDef",
        "ModelBiasJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "NetworkConfig": "MonitoringNetworkConfigTypeDef",
        "RoleArn": str,
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelExplainabilityJobDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeModelExplainabilityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DescribeModelExplainabilityJobDefinitionResponseTypeDef = TypedDict(
    "DescribeModelExplainabilityJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "JobDefinitionName": str,
        "CreationTime": datetime,
        "ModelExplainabilityBaselineConfig": "ModelExplainabilityBaselineConfigTypeDef",
        "ModelExplainabilityAppSpecification": "ModelExplainabilityAppSpecificationTypeDef",
        "ModelExplainabilityJobInput": "ModelExplainabilityJobInputTypeDef",
        "ModelExplainabilityJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "NetworkConfig": "MonitoringNetworkConfigTypeDef",
        "RoleArn": str,
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelInputRequestTypeDef = TypedDict(
    "DescribeModelInputRequestTypeDef",
    {
        "ModelName": str,
    },
)

DescribeModelOutputTypeDef = TypedDict(
    "DescribeModelOutputTypeDef",
    {
        "ModelName": str,
        "PrimaryContainer": "ContainerDefinitionTypeDef",
        "Containers": List["ContainerDefinitionTypeDef"],
        "InferenceExecutionConfig": "InferenceExecutionConfigTypeDef",
        "ExecutionRoleArn": str,
        "VpcConfig": "VpcConfigTypeDef",
        "CreationTime": datetime,
        "ModelArn": str,
        "EnableNetworkIsolation": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelPackageGroupInputRequestTypeDef = TypedDict(
    "DescribeModelPackageGroupInputRequestTypeDef",
    {
        "ModelPackageGroupName": str,
    },
)

DescribeModelPackageGroupOutputTypeDef = TypedDict(
    "DescribeModelPackageGroupOutputTypeDef",
    {
        "ModelPackageGroupName": str,
        "ModelPackageGroupArn": str,
        "ModelPackageGroupDescription": str,
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "ModelPackageGroupStatus": ModelPackageGroupStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelPackageInputRequestTypeDef = TypedDict(
    "DescribeModelPackageInputRequestTypeDef",
    {
        "ModelPackageName": str,
    },
)

DescribeModelPackageOutputTypeDef = TypedDict(
    "DescribeModelPackageOutputTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageGroupName": str,
        "ModelPackageVersion": int,
        "ModelPackageArn": str,
        "ModelPackageDescription": str,
        "CreationTime": datetime,
        "InferenceSpecification": "InferenceSpecificationTypeDef",
        "SourceAlgorithmSpecification": "SourceAlgorithmSpecificationTypeDef",
        "ValidationSpecification": "ModelPackageValidationSpecificationTypeDef",
        "ModelPackageStatus": ModelPackageStatusType,
        "ModelPackageStatusDetails": "ModelPackageStatusDetailsTypeDef",
        "CertifyForMarketplace": bool,
        "ModelApprovalStatus": ModelApprovalStatusType,
        "CreatedBy": "UserContextTypeDef",
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "ModelMetrics": "ModelMetricsTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "ApprovalDescription": str,
        "CustomerMetadataProperties": Dict[str, str],
        "DriftCheckBaselines": "DriftCheckBaselinesTypeDef",
        "Domain": str,
        "Task": str,
        "SamplePayloadUrl": str,
        "AdditionalInferenceSpecifications": List[
            "AdditionalInferenceSpecificationDefinitionTypeDef"
        ],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeModelQualityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DescribeModelQualityJobDefinitionResponseTypeDef = TypedDict(
    "DescribeModelQualityJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "JobDefinitionName": str,
        "CreationTime": datetime,
        "ModelQualityBaselineConfig": "ModelQualityBaselineConfigTypeDef",
        "ModelQualityAppSpecification": "ModelQualityAppSpecificationTypeDef",
        "ModelQualityJobInput": "ModelQualityJobInputTypeDef",
        "ModelQualityJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "NetworkConfig": "MonitoringNetworkConfigTypeDef",
        "RoleArn": str,
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMonitoringScheduleRequestRequestTypeDef = TypedDict(
    "DescribeMonitoringScheduleRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
    },
)

DescribeMonitoringScheduleResponseTypeDef = TypedDict(
    "DescribeMonitoringScheduleResponseTypeDef",
    {
        "MonitoringScheduleArn": str,
        "MonitoringScheduleName": str,
        "MonitoringScheduleStatus": ScheduleStatusType,
        "MonitoringType": MonitoringTypeType,
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringScheduleConfig": "MonitoringScheduleConfigTypeDef",
        "EndpointName": str,
        "LastMonitoringExecutionSummary": "MonitoringExecutionSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNotebookInstanceInputRequestTypeDef = TypedDict(
    "DescribeNotebookInstanceInputRequestTypeDef",
    {
        "NotebookInstanceName": str,
    },
)

DescribeNotebookInstanceLifecycleConfigInputRequestTypeDef = TypedDict(
    "DescribeNotebookInstanceLifecycleConfigInputRequestTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
    },
)

DescribeNotebookInstanceLifecycleConfigOutputTypeDef = TypedDict(
    "DescribeNotebookInstanceLifecycleConfigOutputTypeDef",
    {
        "NotebookInstanceLifecycleConfigArn": str,
        "NotebookInstanceLifecycleConfigName": str,
        "OnCreate": List["NotebookInstanceLifecycleHookTypeDef"],
        "OnStart": List["NotebookInstanceLifecycleHookTypeDef"],
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNotebookInstanceOutputTypeDef = TypedDict(
    "DescribeNotebookInstanceOutputTypeDef",
    {
        "NotebookInstanceArn": str,
        "NotebookInstanceName": str,
        "NotebookInstanceStatus": NotebookInstanceStatusType,
        "FailureReason": str,
        "Url": str,
        "InstanceType": InstanceTypeType,
        "SubnetId": str,
        "SecurityGroups": List[str],
        "RoleArn": str,
        "KmsKeyId": str,
        "NetworkInterfaceId": str,
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "NotebookInstanceLifecycleConfigName": str,
        "DirectInternetAccess": DirectInternetAccessType,
        "VolumeSizeInGB": int,
        "AcceleratorTypes": List[NotebookInstanceAcceleratorTypeType],
        "DefaultCodeRepository": str,
        "AdditionalCodeRepositories": List[str],
        "RootAccess": RootAccessType,
        "PlatformIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePipelineDefinitionForExecutionRequestRequestTypeDef = TypedDict(
    "DescribePipelineDefinitionForExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionArn": str,
    },
)

DescribePipelineDefinitionForExecutionResponseTypeDef = TypedDict(
    "DescribePipelineDefinitionForExecutionResponseTypeDef",
    {
        "PipelineDefinition": str,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePipelineExecutionRequestRequestTypeDef = TypedDict(
    "DescribePipelineExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionArn": str,
    },
)

DescribePipelineExecutionResponseTypeDef = TypedDict(
    "DescribePipelineExecutionResponseTypeDef",
    {
        "PipelineArn": str,
        "PipelineExecutionArn": str,
        "PipelineExecutionDisplayName": str,
        "PipelineExecutionStatus": PipelineExecutionStatusType,
        "PipelineExecutionDescription": str,
        "PipelineExperimentConfig": "PipelineExperimentConfigTypeDef",
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedBy": "UserContextTypeDef",
        "ParallelismConfiguration": "ParallelismConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePipelineRequestRequestTypeDef = TypedDict(
    "DescribePipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
    },
)

DescribePipelineResponseTypeDef = TypedDict(
    "DescribePipelineResponseTypeDef",
    {
        "PipelineArn": str,
        "PipelineName": str,
        "PipelineDisplayName": str,
        "PipelineDefinition": str,
        "PipelineDescription": str,
        "RoleArn": str,
        "PipelineStatus": Literal["Active"],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastRunTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedBy": "UserContextTypeDef",
        "ParallelismConfiguration": "ParallelismConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProcessingJobRequestRequestTypeDef = TypedDict(
    "DescribeProcessingJobRequestRequestTypeDef",
    {
        "ProcessingJobName": str,
    },
)

DescribeProcessingJobResponseTypeDef = TypedDict(
    "DescribeProcessingJobResponseTypeDef",
    {
        "ProcessingInputs": List["ProcessingInputTypeDef"],
        "ProcessingOutputConfig": "ProcessingOutputConfigTypeDef",
        "ProcessingJobName": str,
        "ProcessingResources": "ProcessingResourcesTypeDef",
        "StoppingCondition": "ProcessingStoppingConditionTypeDef",
        "AppSpecification": "AppSpecificationTypeDef",
        "Environment": Dict[str, str],
        "NetworkConfig": "NetworkConfigTypeDef",
        "RoleArn": str,
        "ExperimentConfig": "ExperimentConfigTypeDef",
        "ProcessingJobArn": str,
        "ProcessingJobStatus": ProcessingJobStatusType,
        "ExitMessage": str,
        "FailureReason": str,
        "ProcessingEndTime": datetime,
        "ProcessingStartTime": datetime,
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "MonitoringScheduleArn": str,
        "AutoMLJobArn": str,
        "TrainingJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectInputRequestTypeDef = TypedDict(
    "DescribeProjectInputRequestTypeDef",
    {
        "ProjectName": str,
    },
)

DescribeProjectOutputTypeDef = TypedDict(
    "DescribeProjectOutputTypeDef",
    {
        "ProjectArn": str,
        "ProjectName": str,
        "ProjectId": str,
        "ProjectDescription": str,
        "ServiceCatalogProvisioningDetails": "ServiceCatalogProvisioningDetailsTypeDef",
        "ServiceCatalogProvisionedProductDetails": "ServiceCatalogProvisionedProductDetailsTypeDef",
        "ProjectStatus": ProjectStatusType,
        "CreatedBy": "UserContextTypeDef",
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStudioLifecycleConfigRequestRequestTypeDef = TypedDict(
    "DescribeStudioLifecycleConfigRequestRequestTypeDef",
    {
        "StudioLifecycleConfigName": str,
    },
)

DescribeStudioLifecycleConfigResponseTypeDef = TypedDict(
    "DescribeStudioLifecycleConfigResponseTypeDef",
    {
        "StudioLifecycleConfigArn": str,
        "StudioLifecycleConfigName": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "StudioLifecycleConfigContent": str,
        "StudioLifecycleConfigAppType": StudioLifecycleConfigAppTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSubscribedWorkteamRequestRequestTypeDef = TypedDict(
    "DescribeSubscribedWorkteamRequestRequestTypeDef",
    {
        "WorkteamArn": str,
    },
)

DescribeSubscribedWorkteamResponseTypeDef = TypedDict(
    "DescribeSubscribedWorkteamResponseTypeDef",
    {
        "SubscribedWorkteam": "SubscribedWorkteamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrainingJobRequestRequestTypeDef = TypedDict(
    "DescribeTrainingJobRequestRequestTypeDef",
    {
        "TrainingJobName": str,
    },
)

DescribeTrainingJobResponseTypeDef = TypedDict(
    "DescribeTrainingJobResponseTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "TuningJobArn": str,
        "LabelingJobArn": str,
        "AutoMLJobArn": str,
        "ModelArtifacts": "ModelArtifactsTypeDef",
        "TrainingJobStatus": TrainingJobStatusType,
        "SecondaryStatus": SecondaryStatusType,
        "FailureReason": str,
        "HyperParameters": Dict[str, str],
        "AlgorithmSpecification": "AlgorithmSpecificationTypeDef",
        "RoleArn": str,
        "InputDataConfig": List["ChannelTypeDef"],
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "ResourceConfig": "ResourceConfigTypeDef",
        "VpcConfig": "VpcConfigTypeDef",
        "StoppingCondition": "StoppingConditionTypeDef",
        "CreationTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "LastModifiedTime": datetime,
        "SecondaryStatusTransitions": List["SecondaryStatusTransitionTypeDef"],
        "FinalMetricDataList": List["MetricDataTypeDef"],
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": "CheckpointConfigTypeDef",
        "TrainingTimeInSeconds": int,
        "BillableTimeInSeconds": int,
        "DebugHookConfig": "DebugHookConfigTypeDef",
        "ExperimentConfig": "ExperimentConfigTypeDef",
        "DebugRuleConfigurations": List["DebugRuleConfigurationTypeDef"],
        "TensorBoardOutputConfig": "TensorBoardOutputConfigTypeDef",
        "DebugRuleEvaluationStatuses": List["DebugRuleEvaluationStatusTypeDef"],
        "ProfilerConfig": "ProfilerConfigTypeDef",
        "ProfilerRuleConfigurations": List["ProfilerRuleConfigurationTypeDef"],
        "ProfilerRuleEvaluationStatuses": List["ProfilerRuleEvaluationStatusTypeDef"],
        "ProfilingStatus": ProfilingStatusType,
        "RetryStrategy": "RetryStrategyTypeDef",
        "Environment": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransformJobRequestRequestTypeDef = TypedDict(
    "DescribeTransformJobRequestRequestTypeDef",
    {
        "TransformJobName": str,
    },
)

DescribeTransformJobResponseTypeDef = TypedDict(
    "DescribeTransformJobResponseTypeDef",
    {
        "TransformJobName": str,
        "TransformJobArn": str,
        "TransformJobStatus": TransformJobStatusType,
        "FailureReason": str,
        "ModelName": str,
        "MaxConcurrentTransforms": int,
        "ModelClientConfig": "ModelClientConfigTypeDef",
        "MaxPayloadInMB": int,
        "BatchStrategy": BatchStrategyType,
        "Environment": Dict[str, str],
        "TransformInput": "TransformInputTypeDef",
        "TransformOutput": "TransformOutputTypeDef",
        "TransformResources": "TransformResourcesTypeDef",
        "CreationTime": datetime,
        "TransformStartTime": datetime,
        "TransformEndTime": datetime,
        "LabelingJobArn": str,
        "AutoMLJobArn": str,
        "DataProcessing": "DataProcessingTypeDef",
        "ExperimentConfig": "ExperimentConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrialComponentRequestRequestTypeDef = TypedDict(
    "DescribeTrialComponentRequestRequestTypeDef",
    {
        "TrialComponentName": str,
    },
)

DescribeTrialComponentResponseTypeDef = TypedDict(
    "DescribeTrialComponentResponseTypeDef",
    {
        "TrialComponentName": str,
        "TrialComponentArn": str,
        "DisplayName": str,
        "Source": "TrialComponentSourceTypeDef",
        "Status": "TrialComponentStatusTypeDef",
        "StartTime": datetime,
        "EndTime": datetime,
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "Parameters": Dict[str, "TrialComponentParameterValueTypeDef"],
        "InputArtifacts": Dict[str, "TrialComponentArtifactTypeDef"],
        "OutputArtifacts": Dict[str, "TrialComponentArtifactTypeDef"],
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "Metrics": List["TrialComponentMetricSummaryTypeDef"],
        "LineageGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrialRequestRequestTypeDef = TypedDict(
    "DescribeTrialRequestRequestTypeDef",
    {
        "TrialName": str,
    },
)

DescribeTrialResponseTypeDef = TypedDict(
    "DescribeTrialResponseTypeDef",
    {
        "TrialName": str,
        "TrialArn": str,
        "DisplayName": str,
        "ExperimentName": str,
        "Source": "TrialSourceTypeDef",
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserProfileRequestRequestTypeDef = TypedDict(
    "DescribeUserProfileRequestRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
    },
)

DescribeUserProfileResponseTypeDef = TypedDict(
    "DescribeUserProfileResponseTypeDef",
    {
        "DomainId": str,
        "UserProfileArn": str,
        "UserProfileName": str,
        "HomeEfsFileSystemUid": str,
        "Status": UserProfileStatusType,
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "FailureReason": str,
        "SingleSignOnUserIdentifier": str,
        "SingleSignOnUserValue": str,
        "UserSettings": "UserSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkforceRequestRequestTypeDef = TypedDict(
    "DescribeWorkforceRequestRequestTypeDef",
    {
        "WorkforceName": str,
    },
)

DescribeWorkforceResponseTypeDef = TypedDict(
    "DescribeWorkforceResponseTypeDef",
    {
        "Workforce": "WorkforceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkteamRequestRequestTypeDef = TypedDict(
    "DescribeWorkteamRequestRequestTypeDef",
    {
        "WorkteamName": str,
    },
)

DescribeWorkteamResponseTypeDef = TypedDict(
    "DescribeWorkteamResponseTypeDef",
    {
        "Workteam": "WorkteamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DesiredWeightAndCapacityTypeDef = TypedDict(
    "DesiredWeightAndCapacityTypeDef",
    {
        "VariantName": str,
        "DesiredWeight": NotRequired[float],
        "DesiredInstanceCount": NotRequired[int],
    },
)

DeviceFleetSummaryTypeDef = TypedDict(
    "DeviceFleetSummaryTypeDef",
    {
        "DeviceFleetArn": str,
        "DeviceFleetName": str,
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)

DeviceStatsTypeDef = TypedDict(
    "DeviceStatsTypeDef",
    {
        "ConnectedDeviceCount": int,
        "RegisteredDeviceCount": int,
    },
)

DeviceSummaryTypeDef = TypedDict(
    "DeviceSummaryTypeDef",
    {
        "DeviceName": str,
        "DeviceArn": str,
        "Description": NotRequired[str],
        "DeviceFleetName": NotRequired[str],
        "IotThingName": NotRequired[str],
        "RegistrationTime": NotRequired[datetime],
        "LatestHeartbeat": NotRequired[datetime],
        "Models": NotRequired[List["EdgeModelSummaryTypeDef"]],
        "AgentVersion": NotRequired[str],
    },
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "DeviceName": str,
        "Description": NotRequired[str],
        "IotThingName": NotRequired[str],
    },
)

DisassociateTrialComponentRequestRequestTypeDef = TypedDict(
    "DisassociateTrialComponentRequestRequestTypeDef",
    {
        "TrialComponentName": str,
        "TrialName": str,
    },
)

DisassociateTrialComponentResponseTypeDef = TypedDict(
    "DisassociateTrialComponentResponseTypeDef",
    {
        "TrialComponentArn": str,
        "TrialArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainDetailsTypeDef = TypedDict(
    "DomainDetailsTypeDef",
    {
        "DomainArn": NotRequired[str],
        "DomainId": NotRequired[str],
        "DomainName": NotRequired[str],
        "Status": NotRequired[DomainStatusType],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "Url": NotRequired[str],
    },
)

DomainSettingsForUpdateTypeDef = TypedDict(
    "DomainSettingsForUpdateTypeDef",
    {
        "RStudioServerProDomainSettingsForUpdate": NotRequired[
            "RStudioServerProDomainSettingsForUpdateTypeDef"
        ],
    },
)

DomainSettingsTypeDef = TypedDict(
    "DomainSettingsTypeDef",
    {
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "RStudioServerProDomainSettings": NotRequired["RStudioServerProDomainSettingsTypeDef"],
    },
)

DriftCheckBaselinesTypeDef = TypedDict(
    "DriftCheckBaselinesTypeDef",
    {
        "Bias": NotRequired["DriftCheckBiasTypeDef"],
        "Explainability": NotRequired["DriftCheckExplainabilityTypeDef"],
        "ModelQuality": NotRequired["DriftCheckModelQualityTypeDef"],
        "ModelDataQuality": NotRequired["DriftCheckModelDataQualityTypeDef"],
    },
)

DriftCheckBiasTypeDef = TypedDict(
    "DriftCheckBiasTypeDef",
    {
        "ConfigFile": NotRequired["FileSourceTypeDef"],
        "PreTrainingConstraints": NotRequired["MetricsSourceTypeDef"],
        "PostTrainingConstraints": NotRequired["MetricsSourceTypeDef"],
    },
)

DriftCheckExplainabilityTypeDef = TypedDict(
    "DriftCheckExplainabilityTypeDef",
    {
        "Constraints": NotRequired["MetricsSourceTypeDef"],
        "ConfigFile": NotRequired["FileSourceTypeDef"],
    },
)

DriftCheckModelDataQualityTypeDef = TypedDict(
    "DriftCheckModelDataQualityTypeDef",
    {
        "Statistics": NotRequired["MetricsSourceTypeDef"],
        "Constraints": NotRequired["MetricsSourceTypeDef"],
    },
)

DriftCheckModelQualityTypeDef = TypedDict(
    "DriftCheckModelQualityTypeDef",
    {
        "Statistics": NotRequired["MetricsSourceTypeDef"],
        "Constraints": NotRequired["MetricsSourceTypeDef"],
    },
)

EMRStepMetadataTypeDef = TypedDict(
    "EMRStepMetadataTypeDef",
    {
        "ClusterId": NotRequired[str],
        "StepId": NotRequired[str],
        "StepName": NotRequired[str],
        "LogFilePath": NotRequired[str],
    },
)

EdgeModelStatTypeDef = TypedDict(
    "EdgeModelStatTypeDef",
    {
        "ModelName": str,
        "ModelVersion": str,
        "OfflineDeviceCount": int,
        "ConnectedDeviceCount": int,
        "ActiveDeviceCount": int,
        "SamplingDeviceCount": int,
    },
)

EdgeModelSummaryTypeDef = TypedDict(
    "EdgeModelSummaryTypeDef",
    {
        "ModelName": str,
        "ModelVersion": str,
    },
)

EdgeModelTypeDef = TypedDict(
    "EdgeModelTypeDef",
    {
        "ModelName": str,
        "ModelVersion": str,
        "LatestSampleTime": NotRequired[datetime],
        "LatestInference": NotRequired[datetime],
    },
)

EdgeOutputConfigTypeDef = TypedDict(
    "EdgeOutputConfigTypeDef",
    {
        "S3OutputLocation": str,
        "KmsKeyId": NotRequired[str],
        "PresetDeploymentType": NotRequired[Literal["GreengrassV2Component"]],
        "PresetDeploymentConfig": NotRequired[str],
    },
)

EdgePackagingJobSummaryTypeDef = TypedDict(
    "EdgePackagingJobSummaryTypeDef",
    {
        "EdgePackagingJobArn": str,
        "EdgePackagingJobName": str,
        "EdgePackagingJobStatus": EdgePackagingJobStatusType,
        "CompilationJobName": NotRequired[str],
        "ModelName": NotRequired[str],
        "ModelVersion": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)

EdgePresetDeploymentOutputTypeDef = TypedDict(
    "EdgePresetDeploymentOutputTypeDef",
    {
        "Type": Literal["GreengrassV2Component"],
        "Artifact": NotRequired[str],
        "Status": NotRequired[EdgePresetDeploymentStatusType],
        "StatusMessage": NotRequired[str],
    },
)

EdgeTypeDef = TypedDict(
    "EdgeTypeDef",
    {
        "SourceArn": NotRequired[str],
        "DestinationArn": NotRequired[str],
        "AssociationType": NotRequired[AssociationEdgeTypeType],
    },
)

EndpointConfigSummaryTypeDef = TypedDict(
    "EndpointConfigSummaryTypeDef",
    {
        "EndpointConfigName": str,
        "EndpointConfigArn": str,
        "CreationTime": datetime,
    },
)

EndpointInputConfigurationTypeDef = TypedDict(
    "EndpointInputConfigurationTypeDef",
    {
        "InstanceType": ProductionVariantInstanceTypeType,
        "InferenceSpecificationName": NotRequired[str],
        "EnvironmentParameterRanges": NotRequired["EnvironmentParameterRangesTypeDef"],
    },
)

EndpointInputTypeDef = TypedDict(
    "EndpointInputTypeDef",
    {
        "EndpointName": str,
        "LocalPath": str,
        "S3InputMode": NotRequired[ProcessingS3InputModeType],
        "S3DataDistributionType": NotRequired[ProcessingS3DataDistributionTypeType],
        "FeaturesAttribute": NotRequired[str],
        "InferenceAttribute": NotRequired[str],
        "ProbabilityAttribute": NotRequired[str],
        "ProbabilityThresholdAttribute": NotRequired[float],
        "StartTimeOffset": NotRequired[str],
        "EndTimeOffset": NotRequired[str],
    },
)

EndpointOutputConfigurationTypeDef = TypedDict(
    "EndpointOutputConfigurationTypeDef",
    {
        "EndpointName": str,
        "VariantName": str,
        "InstanceType": ProductionVariantInstanceTypeType,
        "InitialInstanceCount": int,
    },
)

EndpointSummaryTypeDef = TypedDict(
    "EndpointSummaryTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "EndpointStatus": EndpointStatusType,
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "EndpointConfigName": str,
        "EndpointStatus": EndpointStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ProductionVariants": NotRequired[List["ProductionVariantSummaryTypeDef"]],
        "DataCaptureConfig": NotRequired["DataCaptureConfigSummaryTypeDef"],
        "FailureReason": NotRequired[str],
        "MonitoringSchedules": NotRequired[List["MonitoringScheduleTypeDef"]],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

EnvironmentParameterRangesTypeDef = TypedDict(
    "EnvironmentParameterRangesTypeDef",
    {
        "CategoricalParameterRanges": NotRequired[Sequence["CategoricalParameterTypeDef"]],
    },
)

EnvironmentParameterTypeDef = TypedDict(
    "EnvironmentParameterTypeDef",
    {
        "Key": str,
        "ValueType": str,
        "Value": str,
    },
)

ExperimentConfigTypeDef = TypedDict(
    "ExperimentConfigTypeDef",
    {
        "ExperimentName": NotRequired[str],
        "TrialName": NotRequired[str],
        "TrialComponentDisplayName": NotRequired[str],
    },
)

ExperimentSourceTypeDef = TypedDict(
    "ExperimentSourceTypeDef",
    {
        "SourceArn": str,
        "SourceType": NotRequired[str],
    },
)

ExperimentSummaryTypeDef = TypedDict(
    "ExperimentSummaryTypeDef",
    {
        "ExperimentArn": NotRequired[str],
        "ExperimentName": NotRequired[str],
        "DisplayName": NotRequired[str],
        "ExperimentSource": NotRequired["ExperimentSourceTypeDef"],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)

ExperimentTypeDef = TypedDict(
    "ExperimentTypeDef",
    {
        "ExperimentName": NotRequired[str],
        "ExperimentArn": NotRequired[str],
        "DisplayName": NotRequired[str],
        "Source": NotRequired["ExperimentSourceTypeDef"],
        "Description": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "CreatedBy": NotRequired["UserContextTypeDef"],
        "LastModifiedTime": NotRequired[datetime],
        "LastModifiedBy": NotRequired["UserContextTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ExplainabilityTypeDef = TypedDict(
    "ExplainabilityTypeDef",
    {
        "Report": NotRequired["MetricsSourceTypeDef"],
    },
)

FailStepMetadataTypeDef = TypedDict(
    "FailStepMetadataTypeDef",
    {
        "ErrorMessage": NotRequired[str],
    },
)

FeatureDefinitionTypeDef = TypedDict(
    "FeatureDefinitionTypeDef",
    {
        "FeatureName": NotRequired[str],
        "FeatureType": NotRequired[FeatureTypeType],
    },
)

FeatureGroupSummaryTypeDef = TypedDict(
    "FeatureGroupSummaryTypeDef",
    {
        "FeatureGroupName": str,
        "FeatureGroupArn": str,
        "CreationTime": datetime,
        "FeatureGroupStatus": NotRequired[FeatureGroupStatusType],
        "OfflineStoreStatus": NotRequired["OfflineStoreStatusTypeDef"],
    },
)

FeatureGroupTypeDef = TypedDict(
    "FeatureGroupTypeDef",
    {
        "FeatureGroupArn": NotRequired[str],
        "FeatureGroupName": NotRequired[str],
        "RecordIdentifierFeatureName": NotRequired[str],
        "EventTimeFeatureName": NotRequired[str],
        "FeatureDefinitions": NotRequired[List["FeatureDefinitionTypeDef"]],
        "CreationTime": NotRequired[datetime],
        "OnlineStoreConfig": NotRequired["OnlineStoreConfigTypeDef"],
        "OfflineStoreConfig": NotRequired["OfflineStoreConfigTypeDef"],
        "RoleArn": NotRequired[str],
        "FeatureGroupStatus": NotRequired[FeatureGroupStatusType],
        "OfflineStoreStatus": NotRequired["OfflineStoreStatusTypeDef"],
        "FailureReason": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

FileSourceTypeDef = TypedDict(
    "FileSourceTypeDef",
    {
        "S3Uri": str,
        "ContentType": NotRequired[str],
        "ContentDigest": NotRequired[str],
    },
)

FileSystemConfigTypeDef = TypedDict(
    "FileSystemConfigTypeDef",
    {
        "MountPath": NotRequired[str],
        "DefaultUid": NotRequired[int],
        "DefaultGid": NotRequired[int],
    },
)

FileSystemDataSourceTypeDef = TypedDict(
    "FileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": FileSystemAccessModeType,
        "FileSystemType": FileSystemTypeType,
        "DirectoryPath": str,
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Operator": NotRequired[OperatorType],
        "Value": NotRequired[str],
    },
)

FinalAutoMLJobObjectiveMetricTypeDef = TypedDict(
    "FinalAutoMLJobObjectiveMetricTypeDef",
    {
        "MetricName": AutoMLMetricEnumType,
        "Value": float,
        "Type": NotRequired[AutoMLJobObjectiveTypeType],
    },
)

FinalHyperParameterTuningJobObjectiveMetricTypeDef = TypedDict(
    "FinalHyperParameterTuningJobObjectiveMetricTypeDef",
    {
        "MetricName": str,
        "Value": float,
        "Type": NotRequired[HyperParameterTuningJobObjectiveTypeType],
    },
)

FlowDefinitionOutputConfigTypeDef = TypedDict(
    "FlowDefinitionOutputConfigTypeDef",
    {
        "S3OutputPath": str,
        "KmsKeyId": NotRequired[str],
    },
)

FlowDefinitionSummaryTypeDef = TypedDict(
    "FlowDefinitionSummaryTypeDef",
    {
        "FlowDefinitionName": str,
        "FlowDefinitionArn": str,
        "FlowDefinitionStatus": FlowDefinitionStatusType,
        "CreationTime": datetime,
        "FailureReason": NotRequired[str],
    },
)

GetDeviceFleetReportRequestRequestTypeDef = TypedDict(
    "GetDeviceFleetReportRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
    },
)

GetDeviceFleetReportResponseTypeDef = TypedDict(
    "GetDeviceFleetReportResponseTypeDef",
    {
        "DeviceFleetArn": str,
        "DeviceFleetName": str,
        "OutputConfig": "EdgeOutputConfigTypeDef",
        "Description": str,
        "ReportGenerated": datetime,
        "DeviceStats": "DeviceStatsTypeDef",
        "AgentVersions": List["AgentVersionTypeDef"],
        "ModelStats": List["EdgeModelStatTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLineageGroupPolicyRequestRequestTypeDef = TypedDict(
    "GetLineageGroupPolicyRequestRequestTypeDef",
    {
        "LineageGroupName": str,
    },
)

GetLineageGroupPolicyResponseTypeDef = TypedDict(
    "GetLineageGroupPolicyResponseTypeDef",
    {
        "LineageGroupArn": str,
        "ResourcePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetModelPackageGroupPolicyInputRequestTypeDef = TypedDict(
    "GetModelPackageGroupPolicyInputRequestTypeDef",
    {
        "ModelPackageGroupName": str,
    },
)

GetModelPackageGroupPolicyOutputTypeDef = TypedDict(
    "GetModelPackageGroupPolicyOutputTypeDef",
    {
        "ResourcePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSagemakerServicecatalogPortfolioStatusOutputTypeDef = TypedDict(
    "GetSagemakerServicecatalogPortfolioStatusOutputTypeDef",
    {
        "Status": SagemakerServicecatalogStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSearchSuggestionsRequestRequestTypeDef = TypedDict(
    "GetSearchSuggestionsRequestRequestTypeDef",
    {
        "Resource": ResourceTypeType,
        "SuggestionQuery": NotRequired["SuggestionQueryTypeDef"],
    },
)

GetSearchSuggestionsResponseTypeDef = TypedDict(
    "GetSearchSuggestionsResponseTypeDef",
    {
        "PropertyNameSuggestions": List["PropertyNameSuggestionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GitConfigForUpdateTypeDef = TypedDict(
    "GitConfigForUpdateTypeDef",
    {
        "SecretArn": NotRequired[str],
    },
)

GitConfigTypeDef = TypedDict(
    "GitConfigTypeDef",
    {
        "RepositoryUrl": str,
        "Branch": NotRequired[str],
        "SecretArn": NotRequired[str],
    },
)

HumanLoopActivationConditionsConfigTypeDef = TypedDict(
    "HumanLoopActivationConditionsConfigTypeDef",
    {
        "HumanLoopActivationConditions": str,
    },
)

HumanLoopActivationConfigTypeDef = TypedDict(
    "HumanLoopActivationConfigTypeDef",
    {
        "HumanLoopActivationConditionsConfig": "HumanLoopActivationConditionsConfigTypeDef",
    },
)

HumanLoopConfigTypeDef = TypedDict(
    "HumanLoopConfigTypeDef",
    {
        "WorkteamArn": str,
        "HumanTaskUiArn": str,
        "TaskTitle": str,
        "TaskDescription": str,
        "TaskCount": int,
        "TaskAvailabilityLifetimeInSeconds": NotRequired[int],
        "TaskTimeLimitInSeconds": NotRequired[int],
        "TaskKeywords": NotRequired[Sequence[str]],
        "PublicWorkforceTaskPrice": NotRequired["PublicWorkforceTaskPriceTypeDef"],
    },
)

HumanLoopRequestSourceTypeDef = TypedDict(
    "HumanLoopRequestSourceTypeDef",
    {
        "AwsManagedHumanLoopRequestSource": AwsManagedHumanLoopRequestSourceType,
    },
)

HumanTaskConfigTypeDef = TypedDict(
    "HumanTaskConfigTypeDef",
    {
        "WorkteamArn": str,
        "UiConfig": "UiConfigTypeDef",
        "PreHumanTaskLambdaArn": str,
        "TaskTitle": str,
        "TaskDescription": str,
        "NumberOfHumanWorkersPerDataObject": int,
        "TaskTimeLimitInSeconds": int,
        "AnnotationConsolidationConfig": "AnnotationConsolidationConfigTypeDef",
        "TaskKeywords": NotRequired[Sequence[str]],
        "TaskAvailabilityLifetimeInSeconds": NotRequired[int],
        "MaxConcurrentTaskCount": NotRequired[int],
        "PublicWorkforceTaskPrice": NotRequired["PublicWorkforceTaskPriceTypeDef"],
    },
)

HumanTaskUiSummaryTypeDef = TypedDict(
    "HumanTaskUiSummaryTypeDef",
    {
        "HumanTaskUiName": str,
        "HumanTaskUiArn": str,
        "CreationTime": datetime,
    },
)

HyperParameterAlgorithmSpecificationTypeDef = TypedDict(
    "HyperParameterAlgorithmSpecificationTypeDef",
    {
        "TrainingInputMode": TrainingInputModeType,
        "TrainingImage": NotRequired[str],
        "AlgorithmName": NotRequired[str],
        "MetricDefinitions": NotRequired[Sequence["MetricDefinitionTypeDef"]],
    },
)

HyperParameterSpecificationTypeDef = TypedDict(
    "HyperParameterSpecificationTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
        "Description": NotRequired[str],
        "Range": NotRequired["ParameterRangeTypeDef"],
        "IsTunable": NotRequired[bool],
        "IsRequired": NotRequired[bool],
        "DefaultValue": NotRequired[str],
    },
)

HyperParameterTrainingJobDefinitionTypeDef = TypedDict(
    "HyperParameterTrainingJobDefinitionTypeDef",
    {
        "AlgorithmSpecification": "HyperParameterAlgorithmSpecificationTypeDef",
        "RoleArn": str,
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "ResourceConfig": "ResourceConfigTypeDef",
        "StoppingCondition": "StoppingConditionTypeDef",
        "DefinitionName": NotRequired[str],
        "TuningObjective": NotRequired["HyperParameterTuningJobObjectiveTypeDef"],
        "HyperParameterRanges": NotRequired["ParameterRangesTypeDef"],
        "StaticHyperParameters": NotRequired[Mapping[str, str]],
        "InputDataConfig": NotRequired[Sequence["ChannelTypeDef"]],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "EnableNetworkIsolation": NotRequired[bool],
        "EnableInterContainerTrafficEncryption": NotRequired[bool],
        "EnableManagedSpotTraining": NotRequired[bool],
        "CheckpointConfig": NotRequired["CheckpointConfigTypeDef"],
        "RetryStrategy": NotRequired["RetryStrategyTypeDef"],
    },
)

HyperParameterTrainingJobSummaryTypeDef = TypedDict(
    "HyperParameterTrainingJobSummaryTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "CreationTime": datetime,
        "TrainingJobStatus": TrainingJobStatusType,
        "TunedHyperParameters": Dict[str, str],
        "TrainingJobDefinitionName": NotRequired[str],
        "TuningJobName": NotRequired[str],
        "TrainingStartTime": NotRequired[datetime],
        "TrainingEndTime": NotRequired[datetime],
        "FailureReason": NotRequired[str],
        "FinalHyperParameterTuningJobObjectiveMetric": NotRequired[
            "FinalHyperParameterTuningJobObjectiveMetricTypeDef"
        ],
        "ObjectiveStatus": NotRequired[ObjectiveStatusType],
    },
)

HyperParameterTuningJobConfigTypeDef = TypedDict(
    "HyperParameterTuningJobConfigTypeDef",
    {
        "Strategy": HyperParameterTuningJobStrategyTypeType,
        "ResourceLimits": "ResourceLimitsTypeDef",
        "HyperParameterTuningJobObjective": NotRequired["HyperParameterTuningJobObjectiveTypeDef"],
        "ParameterRanges": NotRequired["ParameterRangesTypeDef"],
        "TrainingJobEarlyStoppingType": NotRequired[TrainingJobEarlyStoppingTypeType],
        "TuningJobCompletionCriteria": NotRequired["TuningJobCompletionCriteriaTypeDef"],
    },
)

HyperParameterTuningJobObjectiveTypeDef = TypedDict(
    "HyperParameterTuningJobObjectiveTypeDef",
    {
        "Type": HyperParameterTuningJobObjectiveTypeType,
        "MetricName": str,
    },
)

HyperParameterTuningJobSummaryTypeDef = TypedDict(
    "HyperParameterTuningJobSummaryTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobArn": str,
        "HyperParameterTuningJobStatus": HyperParameterTuningJobStatusType,
        "Strategy": HyperParameterTuningJobStrategyTypeType,
        "CreationTime": datetime,
        "TrainingJobStatusCounters": "TrainingJobStatusCountersTypeDef",
        "ObjectiveStatusCounters": "ObjectiveStatusCountersTypeDef",
        "HyperParameterTuningEndTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "ResourceLimits": NotRequired["ResourceLimitsTypeDef"],
    },
)

HyperParameterTuningJobWarmStartConfigTypeDef = TypedDict(
    "HyperParameterTuningJobWarmStartConfigTypeDef",
    {
        "ParentHyperParameterTuningJobs": Sequence["ParentHyperParameterTuningJobTypeDef"],
        "WarmStartType": HyperParameterTuningJobWarmStartTypeType,
    },
)

ImageConfigTypeDef = TypedDict(
    "ImageConfigTypeDef",
    {
        "RepositoryAccessMode": RepositoryAccessModeType,
        "RepositoryAuthConfig": NotRequired["RepositoryAuthConfigTypeDef"],
    },
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "CreationTime": datetime,
        "ImageArn": str,
        "ImageName": str,
        "ImageStatus": ImageStatusType,
        "LastModifiedTime": datetime,
        "Description": NotRequired[str],
        "DisplayName": NotRequired[str],
        "FailureReason": NotRequired[str],
    },
)

ImageVersionTypeDef = TypedDict(
    "ImageVersionTypeDef",
    {
        "CreationTime": datetime,
        "ImageArn": str,
        "ImageVersionArn": str,
        "ImageVersionStatus": ImageVersionStatusType,
        "LastModifiedTime": datetime,
        "Version": int,
        "FailureReason": NotRequired[str],
    },
)

InferenceExecutionConfigTypeDef = TypedDict(
    "InferenceExecutionConfigTypeDef",
    {
        "Mode": InferenceExecutionModeType,
    },
)

InferenceRecommendationTypeDef = TypedDict(
    "InferenceRecommendationTypeDef",
    {
        "Metrics": "RecommendationMetricsTypeDef",
        "EndpointConfiguration": "EndpointOutputConfigurationTypeDef",
        "ModelConfiguration": "ModelConfigurationTypeDef",
    },
)

InferenceRecommendationsJobTypeDef = TypedDict(
    "InferenceRecommendationsJobTypeDef",
    {
        "JobName": str,
        "JobDescription": str,
        "JobType": RecommendationJobTypeType,
        "JobArn": str,
        "Status": RecommendationJobStatusType,
        "CreationTime": datetime,
        "RoleArn": str,
        "LastModifiedTime": datetime,
        "CompletionTime": NotRequired[datetime],
        "FailureReason": NotRequired[str],
    },
)

InferenceSpecificationTypeDef = TypedDict(
    "InferenceSpecificationTypeDef",
    {
        "Containers": List["ModelPackageContainerDefinitionTypeDef"],
        "SupportedContentTypes": List[str],
        "SupportedResponseMIMETypes": List[str],
        "SupportedTransformInstanceTypes": NotRequired[List[TransformInstanceTypeType]],
        "SupportedRealtimeInferenceInstanceTypes": NotRequired[
            List[ProductionVariantInstanceTypeType]
        ],
    },
)

InputConfigTypeDef = TypedDict(
    "InputConfigTypeDef",
    {
        "S3Uri": str,
        "DataInputConfig": str,
        "Framework": FrameworkType,
        "FrameworkVersion": NotRequired[str],
    },
)

IntegerParameterRangeSpecificationTypeDef = TypedDict(
    "IntegerParameterRangeSpecificationTypeDef",
    {
        "MinValue": str,
        "MaxValue": str,
    },
)

IntegerParameterRangeTypeDef = TypedDict(
    "IntegerParameterRangeTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
        "ScalingType": NotRequired[HyperParameterScalingTypeType],
    },
)

JupyterServerAppSettingsTypeDef = TypedDict(
    "JupyterServerAppSettingsTypeDef",
    {
        "DefaultResourceSpec": NotRequired["ResourceSpecTypeDef"],
        "LifecycleConfigArns": NotRequired[Sequence[str]],
    },
)

KernelGatewayAppSettingsTypeDef = TypedDict(
    "KernelGatewayAppSettingsTypeDef",
    {
        "DefaultResourceSpec": NotRequired["ResourceSpecTypeDef"],
        "CustomImages": NotRequired[Sequence["CustomImageTypeDef"]],
        "LifecycleConfigArns": NotRequired[Sequence[str]],
    },
)

KernelGatewayImageConfigTypeDef = TypedDict(
    "KernelGatewayImageConfigTypeDef",
    {
        "KernelSpecs": Sequence["KernelSpecTypeDef"],
        "FileSystemConfig": NotRequired["FileSystemConfigTypeDef"],
    },
)

KernelSpecTypeDef = TypedDict(
    "KernelSpecTypeDef",
    {
        "Name": str,
        "DisplayName": NotRequired[str],
    },
)

LabelCountersForWorkteamTypeDef = TypedDict(
    "LabelCountersForWorkteamTypeDef",
    {
        "HumanLabeled": NotRequired[int],
        "PendingHuman": NotRequired[int],
        "Total": NotRequired[int],
    },
)

LabelCountersTypeDef = TypedDict(
    "LabelCountersTypeDef",
    {
        "TotalLabeled": NotRequired[int],
        "HumanLabeled": NotRequired[int],
        "MachineLabeled": NotRequired[int],
        "FailedNonRetryableError": NotRequired[int],
        "Unlabeled": NotRequired[int],
    },
)

LabelingJobAlgorithmsConfigTypeDef = TypedDict(
    "LabelingJobAlgorithmsConfigTypeDef",
    {
        "LabelingJobAlgorithmSpecificationArn": str,
        "InitialActiveLearningModelArn": NotRequired[str],
        "LabelingJobResourceConfig": NotRequired["LabelingJobResourceConfigTypeDef"],
    },
)

LabelingJobDataAttributesTypeDef = TypedDict(
    "LabelingJobDataAttributesTypeDef",
    {
        "ContentClassifiers": NotRequired[Sequence[ContentClassifierType]],
    },
)

LabelingJobDataSourceTypeDef = TypedDict(
    "LabelingJobDataSourceTypeDef",
    {
        "S3DataSource": NotRequired["LabelingJobS3DataSourceTypeDef"],
        "SnsDataSource": NotRequired["LabelingJobSnsDataSourceTypeDef"],
    },
)

LabelingJobForWorkteamSummaryTypeDef = TypedDict(
    "LabelingJobForWorkteamSummaryTypeDef",
    {
        "JobReferenceCode": str,
        "WorkRequesterAccountId": str,
        "CreationTime": datetime,
        "LabelingJobName": NotRequired[str],
        "LabelCounters": NotRequired["LabelCountersForWorkteamTypeDef"],
        "NumberOfHumanWorkersPerDataObject": NotRequired[int],
    },
)

LabelingJobInputConfigTypeDef = TypedDict(
    "LabelingJobInputConfigTypeDef",
    {
        "DataSource": "LabelingJobDataSourceTypeDef",
        "DataAttributes": NotRequired["LabelingJobDataAttributesTypeDef"],
    },
)

LabelingJobOutputConfigTypeDef = TypedDict(
    "LabelingJobOutputConfigTypeDef",
    {
        "S3OutputPath": str,
        "KmsKeyId": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
    },
)

LabelingJobOutputTypeDef = TypedDict(
    "LabelingJobOutputTypeDef",
    {
        "OutputDatasetS3Uri": str,
        "FinalActiveLearningModelArn": NotRequired[str],
    },
)

LabelingJobResourceConfigTypeDef = TypedDict(
    "LabelingJobResourceConfigTypeDef",
    {
        "VolumeKmsKeyId": NotRequired[str],
    },
)

LabelingJobS3DataSourceTypeDef = TypedDict(
    "LabelingJobS3DataSourceTypeDef",
    {
        "ManifestS3Uri": str,
    },
)

LabelingJobSnsDataSourceTypeDef = TypedDict(
    "LabelingJobSnsDataSourceTypeDef",
    {
        "SnsTopicArn": str,
    },
)

LabelingJobStoppingConditionsTypeDef = TypedDict(
    "LabelingJobStoppingConditionsTypeDef",
    {
        "MaxHumanLabeledObjectCount": NotRequired[int],
        "MaxPercentageOfInputDatasetLabeled": NotRequired[int],
    },
)

LabelingJobSummaryTypeDef = TypedDict(
    "LabelingJobSummaryTypeDef",
    {
        "LabelingJobName": str,
        "LabelingJobArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LabelingJobStatus": LabelingJobStatusType,
        "LabelCounters": "LabelCountersTypeDef",
        "WorkteamArn": str,
        "PreHumanTaskLambdaArn": str,
        "AnnotationConsolidationLambdaArn": NotRequired[str],
        "FailureReason": NotRequired[str],
        "LabelingJobOutput": NotRequired["LabelingJobOutputTypeDef"],
        "InputConfig": NotRequired["LabelingJobInputConfigTypeDef"],
    },
)

LambdaStepMetadataTypeDef = TypedDict(
    "LambdaStepMetadataTypeDef",
    {
        "Arn": NotRequired[str],
        "OutputParameters": NotRequired[List["OutputParameterTypeDef"]],
    },
)

LineageGroupSummaryTypeDef = TypedDict(
    "LineageGroupSummaryTypeDef",
    {
        "LineageGroupArn": NotRequired[str],
        "LineageGroupName": NotRequired[str],
        "DisplayName": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)

ListActionsRequestRequestTypeDef = TypedDict(
    "ListActionsRequestRequestTypeDef",
    {
        "SourceUri": NotRequired[str],
        "ActionType": NotRequired[str],
        "CreatedAfter": NotRequired[Union[datetime, str]],
        "CreatedBefore": NotRequired[Union[datetime, str]],
        "SortBy": NotRequired[SortActionsByType],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListActionsResponseTypeDef = TypedDict(
    "ListActionsResponseTypeDef",
    {
        "ActionSummaries": List["ActionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAlgorithmsInputRequestTypeDef = TypedDict(
    "ListAlgorithmsInputRequestTypeDef",
    {
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "MaxResults": NotRequired[int],
        "NameContains": NotRequired[str],
        "NextToken": NotRequired[str],
        "SortBy": NotRequired[AlgorithmSortByType],
        "SortOrder": NotRequired[SortOrderType],
    },
)

ListAlgorithmsOutputTypeDef = TypedDict(
    "ListAlgorithmsOutputTypeDef",
    {
        "AlgorithmSummaryList": List["AlgorithmSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppImageConfigsRequestRequestTypeDef = TypedDict(
    "ListAppImageConfigsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "NameContains": NotRequired[str],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "ModifiedTimeBefore": NotRequired[Union[datetime, str]],
        "ModifiedTimeAfter": NotRequired[Union[datetime, str]],
        "SortBy": NotRequired[AppImageConfigSortKeyType],
        "SortOrder": NotRequired[SortOrderType],
    },
)

ListAppImageConfigsResponseTypeDef = TypedDict(
    "ListAppImageConfigsResponseTypeDef",
    {
        "NextToken": str,
        "AppImageConfigs": List["AppImageConfigDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppsRequestRequestTypeDef = TypedDict(
    "ListAppsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "SortOrder": NotRequired[SortOrderType],
        "SortBy": NotRequired[Literal["CreationTime"]],
        "DomainIdEquals": NotRequired[str],
        "UserProfileNameEquals": NotRequired[str],
    },
)

ListAppsResponseTypeDef = TypedDict(
    "ListAppsResponseTypeDef",
    {
        "Apps": List["AppDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListArtifactsRequestRequestTypeDef = TypedDict(
    "ListArtifactsRequestRequestTypeDef",
    {
        "SourceUri": NotRequired[str],
        "ArtifactType": NotRequired[str],
        "CreatedAfter": NotRequired[Union[datetime, str]],
        "CreatedBefore": NotRequired[Union[datetime, str]],
        "SortBy": NotRequired[Literal["CreationTime"]],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListArtifactsResponseTypeDef = TypedDict(
    "ListArtifactsResponseTypeDef",
    {
        "ArtifactSummaries": List["ArtifactSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssociationsRequestRequestTypeDef = TypedDict(
    "ListAssociationsRequestRequestTypeDef",
    {
        "SourceArn": NotRequired[str],
        "DestinationArn": NotRequired[str],
        "SourceType": NotRequired[str],
        "DestinationType": NotRequired[str],
        "AssociationType": NotRequired[AssociationEdgeTypeType],
        "CreatedAfter": NotRequired[Union[datetime, str]],
        "CreatedBefore": NotRequired[Union[datetime, str]],
        "SortBy": NotRequired[SortAssociationsByType],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListAssociationsResponseTypeDef = TypedDict(
    "ListAssociationsResponseTypeDef",
    {
        "AssociationSummaries": List["AssociationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAutoMLJobsRequestRequestTypeDef = TypedDict(
    "ListAutoMLJobsRequestRequestTypeDef",
    {
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "LastModifiedTimeAfter": NotRequired[Union[datetime, str]],
        "LastModifiedTimeBefore": NotRequired[Union[datetime, str]],
        "NameContains": NotRequired[str],
        "StatusEquals": NotRequired[AutoMLJobStatusType],
        "SortOrder": NotRequired[AutoMLSortOrderType],
        "SortBy": NotRequired[AutoMLSortByType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAutoMLJobsResponseTypeDef = TypedDict(
    "ListAutoMLJobsResponseTypeDef",
    {
        "AutoMLJobSummaries": List["AutoMLJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCandidatesForAutoMLJobRequestRequestTypeDef = TypedDict(
    "ListCandidatesForAutoMLJobRequestRequestTypeDef",
    {
        "AutoMLJobName": str,
        "StatusEquals": NotRequired[CandidateStatusType],
        "CandidateNameEquals": NotRequired[str],
        "SortOrder": NotRequired[AutoMLSortOrderType],
        "SortBy": NotRequired[CandidateSortByType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListCandidatesForAutoMLJobResponseTypeDef = TypedDict(
    "ListCandidatesForAutoMLJobResponseTypeDef",
    {
        "Candidates": List["AutoMLCandidateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCodeRepositoriesInputRequestTypeDef = TypedDict(
    "ListCodeRepositoriesInputRequestTypeDef",
    {
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "LastModifiedTimeAfter": NotRequired[Union[datetime, str]],
        "LastModifiedTimeBefore": NotRequired[Union[datetime, str]],
        "MaxResults": NotRequired[int],
        "NameContains": NotRequired[str],
        "NextToken": NotRequired[str],
        "SortBy": NotRequired[CodeRepositorySortByType],
        "SortOrder": NotRequired[CodeRepositorySortOrderType],
    },
)

ListCodeRepositoriesOutputTypeDef = TypedDict(
    "ListCodeRepositoriesOutputTypeDef",
    {
        "CodeRepositorySummaryList": List["CodeRepositorySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCompilationJobsRequestRequestTypeDef = TypedDict(
    "ListCompilationJobsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "LastModifiedTimeAfter": NotRequired[Union[datetime, str]],
        "LastModifiedTimeBefore": NotRequired[Union[datetime, str]],
        "NameContains": NotRequired[str],
        "StatusEquals": NotRequired[CompilationJobStatusType],
        "SortBy": NotRequired[ListCompilationJobsSortByType],
        "SortOrder": NotRequired[SortOrderType],
    },
)

ListCompilationJobsResponseTypeDef = TypedDict(
    "ListCompilationJobsResponseTypeDef",
    {
        "CompilationJobSummaries": List["CompilationJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContextsRequestRequestTypeDef = TypedDict(
    "ListContextsRequestRequestTypeDef",
    {
        "SourceUri": NotRequired[str],
        "ContextType": NotRequired[str],
        "CreatedAfter": NotRequired[Union[datetime, str]],
        "CreatedBefore": NotRequired[Union[datetime, str]],
        "SortBy": NotRequired[SortContextsByType],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListContextsResponseTypeDef = TypedDict(
    "ListContextsResponseTypeDef",
    {
        "ContextSummaries": List["ContextSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataQualityJobDefinitionsRequestRequestTypeDef = TypedDict(
    "ListDataQualityJobDefinitionsRequestRequestTypeDef",
    {
        "EndpointName": NotRequired[str],
        "SortBy": NotRequired[MonitoringJobDefinitionSortKeyType],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NameContains": NotRequired[str],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
    },
)

ListDataQualityJobDefinitionsResponseTypeDef = TypedDict(
    "ListDataQualityJobDefinitionsResponseTypeDef",
    {
        "JobDefinitionSummaries": List["MonitoringJobDefinitionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeviceFleetsRequestRequestTypeDef = TypedDict(
    "ListDeviceFleetsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "LastModifiedTimeAfter": NotRequired[Union[datetime, str]],
        "LastModifiedTimeBefore": NotRequired[Union[datetime, str]],
        "NameContains": NotRequired[str],
        "SortBy": NotRequired[ListDeviceFleetsSortByType],
        "SortOrder": NotRequired[SortOrderType],
    },
)

ListDeviceFleetsResponseTypeDef = TypedDict(
    "ListDeviceFleetsResponseTypeDef",
    {
        "DeviceFleetSummaries": List["DeviceFleetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevicesRequestRequestTypeDef = TypedDict(
    "ListDevicesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "LatestHeartbeatAfter": NotRequired[Union[datetime, str]],
        "ModelName": NotRequired[str],
        "DeviceFleetName": NotRequired[str],
    },
)

ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {
        "DeviceSummaries": List["DeviceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {
        "Domains": List["DomainDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEdgePackagingJobsRequestRequestTypeDef = TypedDict(
    "ListEdgePackagingJobsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "LastModifiedTimeAfter": NotRequired[Union[datetime, str]],
        "LastModifiedTimeBefore": NotRequired[Union[datetime, str]],
        "NameContains": NotRequired[str],
        "ModelNameContains": NotRequired[str],
        "StatusEquals": NotRequired[EdgePackagingJobStatusType],
        "SortBy": NotRequired[ListEdgePackagingJobsSortByType],
        "SortOrder": NotRequired[SortOrderType],
    },
)

ListEdgePackagingJobsResponseTypeDef = TypedDict(
    "ListEdgePackagingJobsResponseTypeDef",
    {
        "EdgePackagingJobSummaries": List["EdgePackagingJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEndpointConfigsInputRequestTypeDef = TypedDict(
    "ListEndpointConfigsInputRequestTypeDef",
    {
        "SortBy": NotRequired[EndpointConfigSortKeyType],
        "SortOrder": NotRequired[OrderKeyType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NameContains": NotRequired[str],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
    },
)

ListEndpointConfigsOutputTypeDef = TypedDict(
    "ListEndpointConfigsOutputTypeDef",
    {
        "EndpointConfigs": List["EndpointConfigSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEndpointsInputRequestTypeDef = TypedDict(
    "ListEndpointsInputRequestTypeDef",
    {
        "SortBy": NotRequired[EndpointSortKeyType],
        "SortOrder": NotRequired[OrderKeyType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NameContains": NotRequired[str],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "LastModifiedTimeBefore": NotRequired[Union[datetime, str]],
        "LastModifiedTimeAfter": NotRequired[Union[datetime, str]],
        "StatusEquals": NotRequired[EndpointStatusType],
    },
)

ListEndpointsOutputTypeDef = TypedDict(
    "ListEndpointsOutputTypeDef",
    {
        "Endpoints": List["EndpointSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExperimentsRequestRequestTypeDef = TypedDict(
    "ListExperimentsRequestRequestTypeDef",
    {
        "CreatedAfter": NotRequired[Union[datetime, str]],
        "CreatedBefore": NotRequired[Union[datetime, str]],
        "SortBy": NotRequired[SortExperimentsByType],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListExperimentsResponseTypeDef = TypedDict(
    "ListExperimentsResponseTypeDef",
    {
        "ExperimentSummaries": List["ExperimentSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFeatureGroupsRequestRequestTypeDef = TypedDict(
    "ListFeatureGroupsRequestRequestTypeDef",
    {
        "NameContains": NotRequired[str],
        "FeatureGroupStatusEquals": NotRequired[FeatureGroupStatusType],
        "OfflineStoreStatusEquals": NotRequired[OfflineStoreStatusValueType],
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "SortOrder": NotRequired[FeatureGroupSortOrderType],
        "SortBy": NotRequired[FeatureGroupSortByType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListFeatureGroupsResponseTypeDef = TypedDict(
    "ListFeatureGroupsResponseTypeDef",
    {
        "FeatureGroupSummaries": List["FeatureGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFlowDefinitionsRequestRequestTypeDef = TypedDict(
    "ListFlowDefinitionsRequestRequestTypeDef",
    {
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListFlowDefinitionsResponseTypeDef = TypedDict(
    "ListFlowDefinitionsResponseTypeDef",
    {
        "FlowDefinitionSummaries": List["FlowDefinitionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHumanTaskUisRequestRequestTypeDef = TypedDict(
    "ListHumanTaskUisRequestRequestTypeDef",
    {
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListHumanTaskUisResponseTypeDef = TypedDict(
    "ListHumanTaskUisResponseTypeDef",
    {
        "HumanTaskUiSummaries": List["HumanTaskUiSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHyperParameterTuningJobsRequestRequestTypeDef = TypedDict(
    "ListHyperParameterTuningJobsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "SortBy": NotRequired[HyperParameterTuningJobSortByOptionsType],
        "SortOrder": NotRequired[SortOrderType],
        "NameContains": NotRequired[str],
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "LastModifiedTimeAfter": NotRequired[Union[datetime, str]],
        "LastModifiedTimeBefore": NotRequired[Union[datetime, str]],
        "StatusEquals": NotRequired[HyperParameterTuningJobStatusType],
    },
)

ListHyperParameterTuningJobsResponseTypeDef = TypedDict(
    "ListHyperParameterTuningJobsResponseTypeDef",
    {
        "HyperParameterTuningJobSummaries": List["HyperParameterTuningJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImageVersionsRequestRequestTypeDef = TypedDict(
    "ListImageVersionsRequestRequestTypeDef",
    {
        "ImageName": str,
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "LastModifiedTimeAfter": NotRequired[Union[datetime, str]],
        "LastModifiedTimeBefore": NotRequired[Union[datetime, str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SortBy": NotRequired[ImageVersionSortByType],
        "SortOrder": NotRequired[ImageVersionSortOrderType],
    },
)

ListImageVersionsResponseTypeDef = TypedDict(
    "ListImageVersionsResponseTypeDef",
    {
        "ImageVersions": List["ImageVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImagesRequestRequestTypeDef = TypedDict(
    "ListImagesRequestRequestTypeDef",
    {
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "LastModifiedTimeAfter": NotRequired[Union[datetime, str]],
        "LastModifiedTimeBefore": NotRequired[Union[datetime, str]],
        "MaxResults": NotRequired[int],
        "NameContains": NotRequired[str],
        "NextToken": NotRequired[str],
        "SortBy": NotRequired[ImageSortByType],
        "SortOrder": NotRequired[ImageSortOrderType],
    },
)

ListImagesResponseTypeDef = TypedDict(
    "ListImagesResponseTypeDef",
    {
        "Images": List["ImageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInferenceRecommendationsJobsRequestRequestTypeDef = TypedDict(
    "ListInferenceRecommendationsJobsRequestRequestTypeDef",
    {
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "LastModifiedTimeAfter": NotRequired[Union[datetime, str]],
        "LastModifiedTimeBefore": NotRequired[Union[datetime, str]],
        "NameContains": NotRequired[str],
        "StatusEquals": NotRequired[RecommendationJobStatusType],
        "SortBy": NotRequired[ListInferenceRecommendationsJobsSortByType],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListInferenceRecommendationsJobsResponseTypeDef = TypedDict(
    "ListInferenceRecommendationsJobsResponseTypeDef",
    {
        "InferenceRecommendationsJobs": List["InferenceRecommendationsJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLabelingJobsForWorkteamRequestRequestTypeDef = TypedDict(
    "ListLabelingJobsForWorkteamRequestRequestTypeDef",
    {
        "WorkteamArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "JobReferenceCodeContains": NotRequired[str],
        "SortBy": NotRequired[Literal["CreationTime"]],
        "SortOrder": NotRequired[SortOrderType],
    },
)

ListLabelingJobsForWorkteamResponseTypeDef = TypedDict(
    "ListLabelingJobsForWorkteamResponseTypeDef",
    {
        "LabelingJobSummaryList": List["LabelingJobForWorkteamSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLabelingJobsRequestRequestTypeDef = TypedDict(
    "ListLabelingJobsRequestRequestTypeDef",
    {
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "LastModifiedTimeAfter": NotRequired[Union[datetime, str]],
        "LastModifiedTimeBefore": NotRequired[Union[datetime, str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "NameContains": NotRequired[str],
        "SortBy": NotRequired[SortByType],
        "SortOrder": NotRequired[SortOrderType],
        "StatusEquals": NotRequired[LabelingJobStatusType],
    },
)

ListLabelingJobsResponseTypeDef = TypedDict(
    "ListLabelingJobsResponseTypeDef",
    {
        "LabelingJobSummaryList": List["LabelingJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLineageGroupsRequestRequestTypeDef = TypedDict(
    "ListLineageGroupsRequestRequestTypeDef",
    {
        "CreatedAfter": NotRequired[Union[datetime, str]],
        "CreatedBefore": NotRequired[Union[datetime, str]],
        "SortBy": NotRequired[SortLineageGroupsByType],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListLineageGroupsResponseTypeDef = TypedDict(
    "ListLineageGroupsResponseTypeDef",
    {
        "LineageGroupSummaries": List["LineageGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelBiasJobDefinitionsRequestRequestTypeDef = TypedDict(
    "ListModelBiasJobDefinitionsRequestRequestTypeDef",
    {
        "EndpointName": NotRequired[str],
        "SortBy": NotRequired[MonitoringJobDefinitionSortKeyType],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NameContains": NotRequired[str],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
    },
)

ListModelBiasJobDefinitionsResponseTypeDef = TypedDict(
    "ListModelBiasJobDefinitionsResponseTypeDef",
    {
        "JobDefinitionSummaries": List["MonitoringJobDefinitionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelExplainabilityJobDefinitionsRequestRequestTypeDef = TypedDict(
    "ListModelExplainabilityJobDefinitionsRequestRequestTypeDef",
    {
        "EndpointName": NotRequired[str],
        "SortBy": NotRequired[MonitoringJobDefinitionSortKeyType],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NameContains": NotRequired[str],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
    },
)

ListModelExplainabilityJobDefinitionsResponseTypeDef = TypedDict(
    "ListModelExplainabilityJobDefinitionsResponseTypeDef",
    {
        "JobDefinitionSummaries": List["MonitoringJobDefinitionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelMetadataRequestRequestTypeDef = TypedDict(
    "ListModelMetadataRequestRequestTypeDef",
    {
        "SearchExpression": NotRequired["ModelMetadataSearchExpressionTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListModelMetadataResponseTypeDef = TypedDict(
    "ListModelMetadataResponseTypeDef",
    {
        "ModelMetadataSummaries": List["ModelMetadataSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelPackageGroupsInputRequestTypeDef = TypedDict(
    "ListModelPackageGroupsInputRequestTypeDef",
    {
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "MaxResults": NotRequired[int],
        "NameContains": NotRequired[str],
        "NextToken": NotRequired[str],
        "SortBy": NotRequired[ModelPackageGroupSortByType],
        "SortOrder": NotRequired[SortOrderType],
    },
)

ListModelPackageGroupsOutputTypeDef = TypedDict(
    "ListModelPackageGroupsOutputTypeDef",
    {
        "ModelPackageGroupSummaryList": List["ModelPackageGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelPackagesInputRequestTypeDef = TypedDict(
    "ListModelPackagesInputRequestTypeDef",
    {
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "MaxResults": NotRequired[int],
        "NameContains": NotRequired[str],
        "ModelApprovalStatus": NotRequired[ModelApprovalStatusType],
        "ModelPackageGroupName": NotRequired[str],
        "ModelPackageType": NotRequired[ModelPackageTypeType],
        "NextToken": NotRequired[str],
        "SortBy": NotRequired[ModelPackageSortByType],
        "SortOrder": NotRequired[SortOrderType],
    },
)

ListModelPackagesOutputTypeDef = TypedDict(
    "ListModelPackagesOutputTypeDef",
    {
        "ModelPackageSummaryList": List["ModelPackageSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelQualityJobDefinitionsRequestRequestTypeDef = TypedDict(
    "ListModelQualityJobDefinitionsRequestRequestTypeDef",
    {
        "EndpointName": NotRequired[str],
        "SortBy": NotRequired[MonitoringJobDefinitionSortKeyType],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NameContains": NotRequired[str],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
    },
)

ListModelQualityJobDefinitionsResponseTypeDef = TypedDict(
    "ListModelQualityJobDefinitionsResponseTypeDef",
    {
        "JobDefinitionSummaries": List["MonitoringJobDefinitionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelsInputRequestTypeDef = TypedDict(
    "ListModelsInputRequestTypeDef",
    {
        "SortBy": NotRequired[ModelSortKeyType],
        "SortOrder": NotRequired[OrderKeyType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NameContains": NotRequired[str],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
    },
)

ListModelsOutputTypeDef = TypedDict(
    "ListModelsOutputTypeDef",
    {
        "Models": List["ModelSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMonitoringExecutionsRequestRequestTypeDef = TypedDict(
    "ListMonitoringExecutionsRequestRequestTypeDef",
    {
        "MonitoringScheduleName": NotRequired[str],
        "EndpointName": NotRequired[str],
        "SortBy": NotRequired[MonitoringExecutionSortKeyType],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ScheduledTimeBefore": NotRequired[Union[datetime, str]],
        "ScheduledTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "LastModifiedTimeBefore": NotRequired[Union[datetime, str]],
        "LastModifiedTimeAfter": NotRequired[Union[datetime, str]],
        "StatusEquals": NotRequired[ExecutionStatusType],
        "MonitoringJobDefinitionName": NotRequired[str],
        "MonitoringTypeEquals": NotRequired[MonitoringTypeType],
    },
)

ListMonitoringExecutionsResponseTypeDef = TypedDict(
    "ListMonitoringExecutionsResponseTypeDef",
    {
        "MonitoringExecutionSummaries": List["MonitoringExecutionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMonitoringSchedulesRequestRequestTypeDef = TypedDict(
    "ListMonitoringSchedulesRequestRequestTypeDef",
    {
        "EndpointName": NotRequired[str],
        "SortBy": NotRequired[MonitoringScheduleSortKeyType],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NameContains": NotRequired[str],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "LastModifiedTimeBefore": NotRequired[Union[datetime, str]],
        "LastModifiedTimeAfter": NotRequired[Union[datetime, str]],
        "StatusEquals": NotRequired[ScheduleStatusType],
        "MonitoringJobDefinitionName": NotRequired[str],
        "MonitoringTypeEquals": NotRequired[MonitoringTypeType],
    },
)

ListMonitoringSchedulesResponseTypeDef = TypedDict(
    "ListMonitoringSchedulesResponseTypeDef",
    {
        "MonitoringScheduleSummaries": List["MonitoringScheduleSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNotebookInstanceLifecycleConfigsInputRequestTypeDef = TypedDict(
    "ListNotebookInstanceLifecycleConfigsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "SortBy": NotRequired[NotebookInstanceLifecycleConfigSortKeyType],
        "SortOrder": NotRequired[NotebookInstanceLifecycleConfigSortOrderType],
        "NameContains": NotRequired[str],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "LastModifiedTimeBefore": NotRequired[Union[datetime, str]],
        "LastModifiedTimeAfter": NotRequired[Union[datetime, str]],
    },
)

ListNotebookInstanceLifecycleConfigsOutputTypeDef = TypedDict(
    "ListNotebookInstanceLifecycleConfigsOutputTypeDef",
    {
        "NextToken": str,
        "NotebookInstanceLifecycleConfigs": List["NotebookInstanceLifecycleConfigSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNotebookInstancesInputRequestTypeDef = TypedDict(
    "ListNotebookInstancesInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "SortBy": NotRequired[NotebookInstanceSortKeyType],
        "SortOrder": NotRequired[NotebookInstanceSortOrderType],
        "NameContains": NotRequired[str],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "LastModifiedTimeBefore": NotRequired[Union[datetime, str]],
        "LastModifiedTimeAfter": NotRequired[Union[datetime, str]],
        "StatusEquals": NotRequired[NotebookInstanceStatusType],
        "NotebookInstanceLifecycleConfigNameContains": NotRequired[str],
        "DefaultCodeRepositoryContains": NotRequired[str],
        "AdditionalCodeRepositoryEquals": NotRequired[str],
    },
)

ListNotebookInstancesOutputTypeDef = TypedDict(
    "ListNotebookInstancesOutputTypeDef",
    {
        "NextToken": str,
        "NotebookInstances": List["NotebookInstanceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPipelineExecutionStepsRequestRequestTypeDef = TypedDict(
    "ListPipelineExecutionStepsRequestRequestTypeDef",
    {
        "PipelineExecutionArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "SortOrder": NotRequired[SortOrderType],
    },
)

ListPipelineExecutionStepsResponseTypeDef = TypedDict(
    "ListPipelineExecutionStepsResponseTypeDef",
    {
        "PipelineExecutionSteps": List["PipelineExecutionStepTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPipelineExecutionsRequestRequestTypeDef = TypedDict(
    "ListPipelineExecutionsRequestRequestTypeDef",
    {
        "PipelineName": str,
        "CreatedAfter": NotRequired[Union[datetime, str]],
        "CreatedBefore": NotRequired[Union[datetime, str]],
        "SortBy": NotRequired[SortPipelineExecutionsByType],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListPipelineExecutionsResponseTypeDef = TypedDict(
    "ListPipelineExecutionsResponseTypeDef",
    {
        "PipelineExecutionSummaries": List["PipelineExecutionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPipelineParametersForExecutionRequestRequestTypeDef = TypedDict(
    "ListPipelineParametersForExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListPipelineParametersForExecutionResponseTypeDef = TypedDict(
    "ListPipelineParametersForExecutionResponseTypeDef",
    {
        "PipelineParameters": List["ParameterTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPipelinesRequestRequestTypeDef = TypedDict(
    "ListPipelinesRequestRequestTypeDef",
    {
        "PipelineNamePrefix": NotRequired[str],
        "CreatedAfter": NotRequired[Union[datetime, str]],
        "CreatedBefore": NotRequired[Union[datetime, str]],
        "SortBy": NotRequired[SortPipelinesByType],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListPipelinesResponseTypeDef = TypedDict(
    "ListPipelinesResponseTypeDef",
    {
        "PipelineSummaries": List["PipelineSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProcessingJobsRequestRequestTypeDef = TypedDict(
    "ListProcessingJobsRequestRequestTypeDef",
    {
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "LastModifiedTimeAfter": NotRequired[Union[datetime, str]],
        "LastModifiedTimeBefore": NotRequired[Union[datetime, str]],
        "NameContains": NotRequired[str],
        "StatusEquals": NotRequired[ProcessingJobStatusType],
        "SortBy": NotRequired[SortByType],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListProcessingJobsResponseTypeDef = TypedDict(
    "ListProcessingJobsResponseTypeDef",
    {
        "ProcessingJobSummaries": List["ProcessingJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsInputRequestTypeDef = TypedDict(
    "ListProjectsInputRequestTypeDef",
    {
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "MaxResults": NotRequired[int],
        "NameContains": NotRequired[str],
        "NextToken": NotRequired[str],
        "SortBy": NotRequired[ProjectSortByType],
        "SortOrder": NotRequired[ProjectSortOrderType],
    },
)

ListProjectsOutputTypeDef = TypedDict(
    "ListProjectsOutputTypeDef",
    {
        "ProjectSummaryList": List["ProjectSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStudioLifecycleConfigsRequestRequestTypeDef = TypedDict(
    "ListStudioLifecycleConfigsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "NameContains": NotRequired[str],
        "AppTypeEquals": NotRequired[StudioLifecycleConfigAppTypeType],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "ModifiedTimeBefore": NotRequired[Union[datetime, str]],
        "ModifiedTimeAfter": NotRequired[Union[datetime, str]],
        "SortBy": NotRequired[StudioLifecycleConfigSortKeyType],
        "SortOrder": NotRequired[SortOrderType],
    },
)

ListStudioLifecycleConfigsResponseTypeDef = TypedDict(
    "ListStudioLifecycleConfigsResponseTypeDef",
    {
        "NextToken": str,
        "StudioLifecycleConfigs": List["StudioLifecycleConfigDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSubscribedWorkteamsRequestRequestTypeDef = TypedDict(
    "ListSubscribedWorkteamsRequestRequestTypeDef",
    {
        "NameContains": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListSubscribedWorkteamsResponseTypeDef = TypedDict(
    "ListSubscribedWorkteamsResponseTypeDef",
    {
        "SubscribedWorkteams": List["SubscribedWorkteamTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsInputRequestTypeDef = TypedDict(
    "ListTagsInputRequestTypeDef",
    {
        "ResourceArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTagsOutputTypeDef = TypedDict(
    "ListTagsOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrainingJobsForHyperParameterTuningJobRequestRequestTypeDef = TypedDict(
    "ListTrainingJobsForHyperParameterTuningJobRequestRequestTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "StatusEquals": NotRequired[TrainingJobStatusType],
        "SortBy": NotRequired[TrainingJobSortByOptionsType],
        "SortOrder": NotRequired[SortOrderType],
    },
)

ListTrainingJobsForHyperParameterTuningJobResponseTypeDef = TypedDict(
    "ListTrainingJobsForHyperParameterTuningJobResponseTypeDef",
    {
        "TrainingJobSummaries": List["HyperParameterTrainingJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrainingJobsRequestRequestTypeDef = TypedDict(
    "ListTrainingJobsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "LastModifiedTimeAfter": NotRequired[Union[datetime, str]],
        "LastModifiedTimeBefore": NotRequired[Union[datetime, str]],
        "NameContains": NotRequired[str],
        "StatusEquals": NotRequired[TrainingJobStatusType],
        "SortBy": NotRequired[SortByType],
        "SortOrder": NotRequired[SortOrderType],
    },
)

ListTrainingJobsResponseTypeDef = TypedDict(
    "ListTrainingJobsResponseTypeDef",
    {
        "TrainingJobSummaries": List["TrainingJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTransformJobsRequestRequestTypeDef = TypedDict(
    "ListTransformJobsRequestRequestTypeDef",
    {
        "CreationTimeAfter": NotRequired[Union[datetime, str]],
        "CreationTimeBefore": NotRequired[Union[datetime, str]],
        "LastModifiedTimeAfter": NotRequired[Union[datetime, str]],
        "LastModifiedTimeBefore": NotRequired[Union[datetime, str]],
        "NameContains": NotRequired[str],
        "StatusEquals": NotRequired[TransformJobStatusType],
        "SortBy": NotRequired[SortByType],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTransformJobsResponseTypeDef = TypedDict(
    "ListTransformJobsResponseTypeDef",
    {
        "TransformJobSummaries": List["TransformJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrialComponentsRequestRequestTypeDef = TypedDict(
    "ListTrialComponentsRequestRequestTypeDef",
    {
        "ExperimentName": NotRequired[str],
        "TrialName": NotRequired[str],
        "SourceArn": NotRequired[str],
        "CreatedAfter": NotRequired[Union[datetime, str]],
        "CreatedBefore": NotRequired[Union[datetime, str]],
        "SortBy": NotRequired[SortTrialComponentsByType],
        "SortOrder": NotRequired[SortOrderType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListTrialComponentsResponseTypeDef = TypedDict(
    "ListTrialComponentsResponseTypeDef",
    {
        "TrialComponentSummaries": List["TrialComponentSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrialsRequestRequestTypeDef = TypedDict(
    "ListTrialsRequestRequestTypeDef",
    {
        "ExperimentName": NotRequired[str],
        "TrialComponentName": NotRequired[str],
        "CreatedAfter": NotRequired[Union[datetime, str]],
        "CreatedBefore": NotRequired[Union[datetime, str]],
        "SortBy": NotRequired[SortTrialsByType],
        "SortOrder": NotRequired[SortOrderType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListTrialsResponseTypeDef = TypedDict(
    "ListTrialsResponseTypeDef",
    {
        "TrialSummaries": List["TrialSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUserProfilesRequestRequestTypeDef = TypedDict(
    "ListUserProfilesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "SortOrder": NotRequired[SortOrderType],
        "SortBy": NotRequired[UserProfileSortKeyType],
        "DomainIdEquals": NotRequired[str],
        "UserProfileNameContains": NotRequired[str],
    },
)

ListUserProfilesResponseTypeDef = TypedDict(
    "ListUserProfilesResponseTypeDef",
    {
        "UserProfiles": List["UserProfileDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkforcesRequestRequestTypeDef = TypedDict(
    "ListWorkforcesRequestRequestTypeDef",
    {
        "SortBy": NotRequired[ListWorkforcesSortByOptionsType],
        "SortOrder": NotRequired[SortOrderType],
        "NameContains": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListWorkforcesResponseTypeDef = TypedDict(
    "ListWorkforcesResponseTypeDef",
    {
        "Workforces": List["WorkforceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkteamsRequestRequestTypeDef = TypedDict(
    "ListWorkteamsRequestRequestTypeDef",
    {
        "SortBy": NotRequired[ListWorkteamsSortByOptionsType],
        "SortOrder": NotRequired[SortOrderType],
        "NameContains": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListWorkteamsResponseTypeDef = TypedDict(
    "ListWorkteamsResponseTypeDef",
    {
        "Workteams": List["WorkteamTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MemberDefinitionTypeDef = TypedDict(
    "MemberDefinitionTypeDef",
    {
        "CognitoMemberDefinition": NotRequired["CognitoMemberDefinitionTypeDef"],
        "OidcMemberDefinition": NotRequired["OidcMemberDefinitionTypeDef"],
    },
)

MetadataPropertiesTypeDef = TypedDict(
    "MetadataPropertiesTypeDef",
    {
        "CommitId": NotRequired[str],
        "Repository": NotRequired[str],
        "GeneratedBy": NotRequired[str],
        "ProjectId": NotRequired[str],
    },
)

MetricDataTypeDef = TypedDict(
    "MetricDataTypeDef",
    {
        "MetricName": NotRequired[str],
        "Value": NotRequired[float],
        "Timestamp": NotRequired[datetime],
    },
)

MetricDatumTypeDef = TypedDict(
    "MetricDatumTypeDef",
    {
        "MetricName": NotRequired[AutoMLMetricEnumType],
        "Value": NotRequired[float],
        "Set": NotRequired[MetricSetSourceType],
    },
)

MetricDefinitionTypeDef = TypedDict(
    "MetricDefinitionTypeDef",
    {
        "Name": str,
        "Regex": str,
    },
)

MetricsSourceTypeDef = TypedDict(
    "MetricsSourceTypeDef",
    {
        "ContentType": str,
        "S3Uri": str,
        "ContentDigest": NotRequired[str],
    },
)

ModelArtifactsTypeDef = TypedDict(
    "ModelArtifactsTypeDef",
    {
        "S3ModelArtifacts": str,
    },
)

ModelBiasAppSpecificationTypeDef = TypedDict(
    "ModelBiasAppSpecificationTypeDef",
    {
        "ImageUri": str,
        "ConfigUri": str,
        "Environment": NotRequired[Mapping[str, str]],
    },
)

ModelBiasBaselineConfigTypeDef = TypedDict(
    "ModelBiasBaselineConfigTypeDef",
    {
        "BaseliningJobName": NotRequired[str],
        "ConstraintsResource": NotRequired["MonitoringConstraintsResourceTypeDef"],
    },
)

ModelBiasJobInputTypeDef = TypedDict(
    "ModelBiasJobInputTypeDef",
    {
        "EndpointInput": "EndpointInputTypeDef",
        "GroundTruthS3Input": "MonitoringGroundTruthS3InputTypeDef",
    },
)

ModelClientConfigTypeDef = TypedDict(
    "ModelClientConfigTypeDef",
    {
        "InvocationsTimeoutInSeconds": NotRequired[int],
        "InvocationsMaxRetries": NotRequired[int],
    },
)

ModelConfigurationTypeDef = TypedDict(
    "ModelConfigurationTypeDef",
    {
        "InferenceSpecificationName": NotRequired[str],
        "EnvironmentParameters": NotRequired[List["EnvironmentParameterTypeDef"]],
    },
)

ModelDataQualityTypeDef = TypedDict(
    "ModelDataQualityTypeDef",
    {
        "Statistics": NotRequired["MetricsSourceTypeDef"],
        "Constraints": NotRequired["MetricsSourceTypeDef"],
    },
)

ModelDeployConfigTypeDef = TypedDict(
    "ModelDeployConfigTypeDef",
    {
        "AutoGenerateEndpointName": NotRequired[bool],
        "EndpointName": NotRequired[str],
    },
)

ModelDeployResultTypeDef = TypedDict(
    "ModelDeployResultTypeDef",
    {
        "EndpointName": NotRequired[str],
    },
)

ModelDigestsTypeDef = TypedDict(
    "ModelDigestsTypeDef",
    {
        "ArtifactDigest": NotRequired[str],
    },
)

ModelExplainabilityAppSpecificationTypeDef = TypedDict(
    "ModelExplainabilityAppSpecificationTypeDef",
    {
        "ImageUri": str,
        "ConfigUri": str,
        "Environment": NotRequired[Mapping[str, str]],
    },
)

ModelExplainabilityBaselineConfigTypeDef = TypedDict(
    "ModelExplainabilityBaselineConfigTypeDef",
    {
        "BaseliningJobName": NotRequired[str],
        "ConstraintsResource": NotRequired["MonitoringConstraintsResourceTypeDef"],
    },
)

ModelExplainabilityJobInputTypeDef = TypedDict(
    "ModelExplainabilityJobInputTypeDef",
    {
        "EndpointInput": "EndpointInputTypeDef",
    },
)

ModelInputTypeDef = TypedDict(
    "ModelInputTypeDef",
    {
        "DataInputConfig": str,
    },
)

ModelLatencyThresholdTypeDef = TypedDict(
    "ModelLatencyThresholdTypeDef",
    {
        "Percentile": NotRequired[str],
        "ValueInMilliseconds": NotRequired[int],
    },
)

ModelMetadataFilterTypeDef = TypedDict(
    "ModelMetadataFilterTypeDef",
    {
        "Name": ModelMetadataFilterTypeType,
        "Value": str,
    },
)

ModelMetadataSearchExpressionTypeDef = TypedDict(
    "ModelMetadataSearchExpressionTypeDef",
    {
        "Filters": NotRequired[Sequence["ModelMetadataFilterTypeDef"]],
    },
)

ModelMetadataSummaryTypeDef = TypedDict(
    "ModelMetadataSummaryTypeDef",
    {
        "Domain": str,
        "Framework": str,
        "Task": str,
        "Model": str,
        "FrameworkVersion": str,
    },
)

ModelMetricsTypeDef = TypedDict(
    "ModelMetricsTypeDef",
    {
        "ModelQuality": NotRequired["ModelQualityTypeDef"],
        "ModelDataQuality": NotRequired["ModelDataQualityTypeDef"],
        "Bias": NotRequired["BiasTypeDef"],
        "Explainability": NotRequired["ExplainabilityTypeDef"],
    },
)

ModelPackageContainerDefinitionTypeDef = TypedDict(
    "ModelPackageContainerDefinitionTypeDef",
    {
        "Image": str,
        "ContainerHostname": NotRequired[str],
        "ImageDigest": NotRequired[str],
        "ModelDataUrl": NotRequired[str],
        "ProductId": NotRequired[str],
        "Environment": NotRequired[Dict[str, str]],
        "ModelInput": NotRequired["ModelInputTypeDef"],
        "Framework": NotRequired[str],
        "FrameworkVersion": NotRequired[str],
        "NearestModelName": NotRequired[str],
    },
)

ModelPackageGroupSummaryTypeDef = TypedDict(
    "ModelPackageGroupSummaryTypeDef",
    {
        "ModelPackageGroupName": str,
        "ModelPackageGroupArn": str,
        "CreationTime": datetime,
        "ModelPackageGroupStatus": ModelPackageGroupStatusType,
        "ModelPackageGroupDescription": NotRequired[str],
    },
)

ModelPackageGroupTypeDef = TypedDict(
    "ModelPackageGroupTypeDef",
    {
        "ModelPackageGroupName": NotRequired[str],
        "ModelPackageGroupArn": NotRequired[str],
        "ModelPackageGroupDescription": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "CreatedBy": NotRequired["UserContextTypeDef"],
        "ModelPackageGroupStatus": NotRequired[ModelPackageGroupStatusType],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ModelPackageStatusDetailsTypeDef = TypedDict(
    "ModelPackageStatusDetailsTypeDef",
    {
        "ValidationStatuses": List["ModelPackageStatusItemTypeDef"],
        "ImageScanStatuses": NotRequired[List["ModelPackageStatusItemTypeDef"]],
    },
)

ModelPackageStatusItemTypeDef = TypedDict(
    "ModelPackageStatusItemTypeDef",
    {
        "Name": str,
        "Status": DetailedModelPackageStatusType,
        "FailureReason": NotRequired[str],
    },
)

ModelPackageSummaryTypeDef = TypedDict(
    "ModelPackageSummaryTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageArn": str,
        "CreationTime": datetime,
        "ModelPackageStatus": ModelPackageStatusType,
        "ModelPackageGroupName": NotRequired[str],
        "ModelPackageVersion": NotRequired[int],
        "ModelPackageDescription": NotRequired[str],
        "ModelApprovalStatus": NotRequired[ModelApprovalStatusType],
    },
)

ModelPackageTypeDef = TypedDict(
    "ModelPackageTypeDef",
    {
        "ModelPackageName": NotRequired[str],
        "ModelPackageGroupName": NotRequired[str],
        "ModelPackageVersion": NotRequired[int],
        "ModelPackageArn": NotRequired[str],
        "ModelPackageDescription": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "InferenceSpecification": NotRequired["InferenceSpecificationTypeDef"],
        "SourceAlgorithmSpecification": NotRequired["SourceAlgorithmSpecificationTypeDef"],
        "ValidationSpecification": NotRequired["ModelPackageValidationSpecificationTypeDef"],
        "ModelPackageStatus": NotRequired[ModelPackageStatusType],
        "ModelPackageStatusDetails": NotRequired["ModelPackageStatusDetailsTypeDef"],
        "CertifyForMarketplace": NotRequired[bool],
        "ModelApprovalStatus": NotRequired[ModelApprovalStatusType],
        "CreatedBy": NotRequired["UserContextTypeDef"],
        "MetadataProperties": NotRequired["MetadataPropertiesTypeDef"],
        "ModelMetrics": NotRequired["ModelMetricsTypeDef"],
        "LastModifiedTime": NotRequired[datetime],
        "LastModifiedBy": NotRequired["UserContextTypeDef"],
        "ApprovalDescription": NotRequired[str],
        "Domain": NotRequired[str],
        "Task": NotRequired[str],
        "SamplePayloadUrl": NotRequired[str],
        "AdditionalInferenceSpecifications": NotRequired[
            List["AdditionalInferenceSpecificationDefinitionTypeDef"]
        ],
        "Tags": NotRequired[List["TagTypeDef"]],
        "CustomerMetadataProperties": NotRequired[Dict[str, str]],
        "DriftCheckBaselines": NotRequired["DriftCheckBaselinesTypeDef"],
    },
)

ModelPackageValidationProfileTypeDef = TypedDict(
    "ModelPackageValidationProfileTypeDef",
    {
        "ProfileName": str,
        "TransformJobDefinition": "TransformJobDefinitionTypeDef",
    },
)

ModelPackageValidationSpecificationTypeDef = TypedDict(
    "ModelPackageValidationSpecificationTypeDef",
    {
        "ValidationRole": str,
        "ValidationProfiles": Sequence["ModelPackageValidationProfileTypeDef"],
    },
)

ModelQualityAppSpecificationTypeDef = TypedDict(
    "ModelQualityAppSpecificationTypeDef",
    {
        "ImageUri": str,
        "ContainerEntrypoint": NotRequired[Sequence[str]],
        "ContainerArguments": NotRequired[Sequence[str]],
        "RecordPreprocessorSourceUri": NotRequired[str],
        "PostAnalyticsProcessorSourceUri": NotRequired[str],
        "ProblemType": NotRequired[MonitoringProblemTypeType],
        "Environment": NotRequired[Mapping[str, str]],
    },
)

ModelQualityBaselineConfigTypeDef = TypedDict(
    "ModelQualityBaselineConfigTypeDef",
    {
        "BaseliningJobName": NotRequired[str],
        "ConstraintsResource": NotRequired["MonitoringConstraintsResourceTypeDef"],
    },
)

ModelQualityJobInputTypeDef = TypedDict(
    "ModelQualityJobInputTypeDef",
    {
        "EndpointInput": "EndpointInputTypeDef",
        "GroundTruthS3Input": "MonitoringGroundTruthS3InputTypeDef",
    },
)

ModelQualityTypeDef = TypedDict(
    "ModelQualityTypeDef",
    {
        "Statistics": NotRequired["MetricsSourceTypeDef"],
        "Constraints": NotRequired["MetricsSourceTypeDef"],
    },
)

ModelStepMetadataTypeDef = TypedDict(
    "ModelStepMetadataTypeDef",
    {
        "Arn": NotRequired[str],
    },
)

ModelSummaryTypeDef = TypedDict(
    "ModelSummaryTypeDef",
    {
        "ModelName": str,
        "ModelArn": str,
        "CreationTime": datetime,
    },
)

MonitoringAppSpecificationTypeDef = TypedDict(
    "MonitoringAppSpecificationTypeDef",
    {
        "ImageUri": str,
        "ContainerEntrypoint": NotRequired[Sequence[str]],
        "ContainerArguments": NotRequired[Sequence[str]],
        "RecordPreprocessorSourceUri": NotRequired[str],
        "PostAnalyticsProcessorSourceUri": NotRequired[str],
    },
)

MonitoringBaselineConfigTypeDef = TypedDict(
    "MonitoringBaselineConfigTypeDef",
    {
        "BaseliningJobName": NotRequired[str],
        "ConstraintsResource": NotRequired["MonitoringConstraintsResourceTypeDef"],
        "StatisticsResource": NotRequired["MonitoringStatisticsResourceTypeDef"],
    },
)

MonitoringClusterConfigTypeDef = TypedDict(
    "MonitoringClusterConfigTypeDef",
    {
        "InstanceCount": int,
        "InstanceType": ProcessingInstanceTypeType,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": NotRequired[str],
    },
)

MonitoringConstraintsResourceTypeDef = TypedDict(
    "MonitoringConstraintsResourceTypeDef",
    {
        "S3Uri": NotRequired[str],
    },
)

MonitoringExecutionSummaryTypeDef = TypedDict(
    "MonitoringExecutionSummaryTypeDef",
    {
        "MonitoringScheduleName": str,
        "ScheduledTime": datetime,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringExecutionStatus": ExecutionStatusType,
        "ProcessingJobArn": NotRequired[str],
        "EndpointName": NotRequired[str],
        "FailureReason": NotRequired[str],
        "MonitoringJobDefinitionName": NotRequired[str],
        "MonitoringType": NotRequired[MonitoringTypeType],
    },
)

MonitoringGroundTruthS3InputTypeDef = TypedDict(
    "MonitoringGroundTruthS3InputTypeDef",
    {
        "S3Uri": NotRequired[str],
    },
)

MonitoringInputTypeDef = TypedDict(
    "MonitoringInputTypeDef",
    {
        "EndpointInput": "EndpointInputTypeDef",
    },
)

MonitoringJobDefinitionSummaryTypeDef = TypedDict(
    "MonitoringJobDefinitionSummaryTypeDef",
    {
        "MonitoringJobDefinitionName": str,
        "MonitoringJobDefinitionArn": str,
        "CreationTime": datetime,
        "EndpointName": str,
    },
)

MonitoringJobDefinitionTypeDef = TypedDict(
    "MonitoringJobDefinitionTypeDef",
    {
        "MonitoringInputs": Sequence["MonitoringInputTypeDef"],
        "MonitoringOutputConfig": "MonitoringOutputConfigTypeDef",
        "MonitoringResources": "MonitoringResourcesTypeDef",
        "MonitoringAppSpecification": "MonitoringAppSpecificationTypeDef",
        "RoleArn": str,
        "BaselineConfig": NotRequired["MonitoringBaselineConfigTypeDef"],
        "StoppingCondition": NotRequired["MonitoringStoppingConditionTypeDef"],
        "Environment": NotRequired[Mapping[str, str]],
        "NetworkConfig": NotRequired["NetworkConfigTypeDef"],
    },
)

MonitoringNetworkConfigTypeDef = TypedDict(
    "MonitoringNetworkConfigTypeDef",
    {
        "EnableInterContainerTrafficEncryption": NotRequired[bool],
        "EnableNetworkIsolation": NotRequired[bool],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
    },
)

MonitoringOutputConfigTypeDef = TypedDict(
    "MonitoringOutputConfigTypeDef",
    {
        "MonitoringOutputs": Sequence["MonitoringOutputTypeDef"],
        "KmsKeyId": NotRequired[str],
    },
)

MonitoringOutputTypeDef = TypedDict(
    "MonitoringOutputTypeDef",
    {
        "S3Output": "MonitoringS3OutputTypeDef",
    },
)

MonitoringResourcesTypeDef = TypedDict(
    "MonitoringResourcesTypeDef",
    {
        "ClusterConfig": "MonitoringClusterConfigTypeDef",
    },
)

MonitoringS3OutputTypeDef = TypedDict(
    "MonitoringS3OutputTypeDef",
    {
        "S3Uri": str,
        "LocalPath": str,
        "S3UploadMode": NotRequired[ProcessingS3UploadModeType],
    },
)

MonitoringScheduleConfigTypeDef = TypedDict(
    "MonitoringScheduleConfigTypeDef",
    {
        "ScheduleConfig": NotRequired["ScheduleConfigTypeDef"],
        "MonitoringJobDefinition": NotRequired["MonitoringJobDefinitionTypeDef"],
        "MonitoringJobDefinitionName": NotRequired[str],
        "MonitoringType": NotRequired[MonitoringTypeType],
    },
)

MonitoringScheduleSummaryTypeDef = TypedDict(
    "MonitoringScheduleSummaryTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringScheduleArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringScheduleStatus": ScheduleStatusType,
        "EndpointName": NotRequired[str],
        "MonitoringJobDefinitionName": NotRequired[str],
        "MonitoringType": NotRequired[MonitoringTypeType],
    },
)

MonitoringScheduleTypeDef = TypedDict(
    "MonitoringScheduleTypeDef",
    {
        "MonitoringScheduleArn": NotRequired[str],
        "MonitoringScheduleName": NotRequired[str],
        "MonitoringScheduleStatus": NotRequired[ScheduleStatusType],
        "MonitoringType": NotRequired[MonitoringTypeType],
        "FailureReason": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "MonitoringScheduleConfig": NotRequired["MonitoringScheduleConfigTypeDef"],
        "EndpointName": NotRequired[str],
        "LastMonitoringExecutionSummary": NotRequired["MonitoringExecutionSummaryTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

MonitoringStatisticsResourceTypeDef = TypedDict(
    "MonitoringStatisticsResourceTypeDef",
    {
        "S3Uri": NotRequired[str],
    },
)

MonitoringStoppingConditionTypeDef = TypedDict(
    "MonitoringStoppingConditionTypeDef",
    {
        "MaxRuntimeInSeconds": int,
    },
)

MultiModelConfigTypeDef = TypedDict(
    "MultiModelConfigTypeDef",
    {
        "ModelCacheSetting": NotRequired[ModelCacheSettingType],
    },
)

NeoVpcConfigTypeDef = TypedDict(
    "NeoVpcConfigTypeDef",
    {
        "SecurityGroupIds": Sequence[str],
        "Subnets": Sequence[str],
    },
)

NestedFiltersTypeDef = TypedDict(
    "NestedFiltersTypeDef",
    {
        "NestedPropertyName": str,
        "Filters": Sequence["FilterTypeDef"],
    },
)

NetworkConfigTypeDef = TypedDict(
    "NetworkConfigTypeDef",
    {
        "EnableInterContainerTrafficEncryption": NotRequired[bool],
        "EnableNetworkIsolation": NotRequired[bool],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
    },
)

NotebookInstanceLifecycleConfigSummaryTypeDef = TypedDict(
    "NotebookInstanceLifecycleConfigSummaryTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
        "NotebookInstanceLifecycleConfigArn": str,
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)

NotebookInstanceLifecycleHookTypeDef = TypedDict(
    "NotebookInstanceLifecycleHookTypeDef",
    {
        "Content": NotRequired[str],
    },
)

NotebookInstanceSummaryTypeDef = TypedDict(
    "NotebookInstanceSummaryTypeDef",
    {
        "NotebookInstanceName": str,
        "NotebookInstanceArn": str,
        "NotebookInstanceStatus": NotRequired[NotebookInstanceStatusType],
        "Url": NotRequired[str],
        "InstanceType": NotRequired[InstanceTypeType],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "NotebookInstanceLifecycleConfigName": NotRequired[str],
        "DefaultCodeRepository": NotRequired[str],
        "AdditionalCodeRepositories": NotRequired[List[str]],
    },
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "NotificationTopicArn": NotRequired[str],
    },
)

ObjectiveStatusCountersTypeDef = TypedDict(
    "ObjectiveStatusCountersTypeDef",
    {
        "Succeeded": NotRequired[int],
        "Pending": NotRequired[int],
        "Failed": NotRequired[int],
    },
)

OfflineStoreConfigTypeDef = TypedDict(
    "OfflineStoreConfigTypeDef",
    {
        "S3StorageConfig": "S3StorageConfigTypeDef",
        "DisableGlueTableCreation": NotRequired[bool],
        "DataCatalogConfig": NotRequired["DataCatalogConfigTypeDef"],
    },
)

OfflineStoreStatusTypeDef = TypedDict(
    "OfflineStoreStatusTypeDef",
    {
        "Status": OfflineStoreStatusValueType,
        "BlockedReason": NotRequired[str],
    },
)

OidcConfigForResponseTypeDef = TypedDict(
    "OidcConfigForResponseTypeDef",
    {
        "ClientId": NotRequired[str],
        "Issuer": NotRequired[str],
        "AuthorizationEndpoint": NotRequired[str],
        "TokenEndpoint": NotRequired[str],
        "UserInfoEndpoint": NotRequired[str],
        "LogoutEndpoint": NotRequired[str],
        "JwksUri": NotRequired[str],
    },
)

OidcConfigTypeDef = TypedDict(
    "OidcConfigTypeDef",
    {
        "ClientId": str,
        "ClientSecret": str,
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "LogoutEndpoint": str,
        "JwksUri": str,
    },
)

OidcMemberDefinitionTypeDef = TypedDict(
    "OidcMemberDefinitionTypeDef",
    {
        "Groups": Sequence[str],
    },
)

OnlineStoreConfigTypeDef = TypedDict(
    "OnlineStoreConfigTypeDef",
    {
        "SecurityConfig": NotRequired["OnlineStoreSecurityConfigTypeDef"],
        "EnableOnlineStore": NotRequired[bool],
    },
)

OnlineStoreSecurityConfigTypeDef = TypedDict(
    "OnlineStoreSecurityConfigTypeDef",
    {
        "KmsKeyId": NotRequired[str],
    },
)

OutputConfigTypeDef = TypedDict(
    "OutputConfigTypeDef",
    {
        "S3OutputLocation": str,
        "TargetDevice": NotRequired[TargetDeviceType],
        "TargetPlatform": NotRequired["TargetPlatformTypeDef"],
        "CompilerOptions": NotRequired[str],
        "KmsKeyId": NotRequired[str],
    },
)

OutputDataConfigTypeDef = TypedDict(
    "OutputDataConfigTypeDef",
    {
        "S3OutputPath": str,
        "KmsKeyId": NotRequired[str],
    },
)

OutputParameterTypeDef = TypedDict(
    "OutputParameterTypeDef",
    {
        "Name": str,
        "Value": str,
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

ParallelismConfigurationTypeDef = TypedDict(
    "ParallelismConfigurationTypeDef",
    {
        "MaxParallelExecutionSteps": int,
    },
)

ParameterRangeTypeDef = TypedDict(
    "ParameterRangeTypeDef",
    {
        "IntegerParameterRangeSpecification": NotRequired[
            "IntegerParameterRangeSpecificationTypeDef"
        ],
        "ContinuousParameterRangeSpecification": NotRequired[
            "ContinuousParameterRangeSpecificationTypeDef"
        ],
        "CategoricalParameterRangeSpecification": NotRequired[
            "CategoricalParameterRangeSpecificationTypeDef"
        ],
    },
)

ParameterRangesTypeDef = TypedDict(
    "ParameterRangesTypeDef",
    {
        "IntegerParameterRanges": NotRequired[Sequence["IntegerParameterRangeTypeDef"]],
        "ContinuousParameterRanges": NotRequired[Sequence["ContinuousParameterRangeTypeDef"]],
        "CategoricalParameterRanges": NotRequired[Sequence["CategoricalParameterRangeTypeDef"]],
    },
)

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

ParentHyperParameterTuningJobTypeDef = TypedDict(
    "ParentHyperParameterTuningJobTypeDef",
    {
        "HyperParameterTuningJobName": NotRequired[str],
    },
)

ParentTypeDef = TypedDict(
    "ParentTypeDef",
    {
        "TrialName": NotRequired[str],
        "ExperimentName": NotRequired[str],
    },
)

PendingDeploymentSummaryTypeDef = TypedDict(
    "PendingDeploymentSummaryTypeDef",
    {
        "EndpointConfigName": str,
        "ProductionVariants": NotRequired[List["PendingProductionVariantSummaryTypeDef"]],
        "StartTime": NotRequired[datetime],
    },
)

PendingProductionVariantSummaryTypeDef = TypedDict(
    "PendingProductionVariantSummaryTypeDef",
    {
        "VariantName": str,
        "DeployedImages": NotRequired[List["DeployedImageTypeDef"]],
        "CurrentWeight": NotRequired[float],
        "DesiredWeight": NotRequired[float],
        "CurrentInstanceCount": NotRequired[int],
        "DesiredInstanceCount": NotRequired[int],
        "InstanceType": NotRequired[ProductionVariantInstanceTypeType],
        "AcceleratorType": NotRequired[ProductionVariantAcceleratorTypeType],
        "VariantStatus": NotRequired[List["ProductionVariantStatusTypeDef"]],
        "CurrentServerlessConfig": NotRequired["ProductionVariantServerlessConfigTypeDef"],
        "DesiredServerlessConfig": NotRequired["ProductionVariantServerlessConfigTypeDef"],
    },
)

PhaseTypeDef = TypedDict(
    "PhaseTypeDef",
    {
        "InitialNumberOfUsers": NotRequired[int],
        "SpawnRate": NotRequired[int],
        "DurationInSeconds": NotRequired[int],
    },
)

PipelineDefinitionS3LocationTypeDef = TypedDict(
    "PipelineDefinitionS3LocationTypeDef",
    {
        "Bucket": str,
        "ObjectKey": str,
        "VersionId": NotRequired[str],
    },
)

PipelineExecutionStepMetadataTypeDef = TypedDict(
    "PipelineExecutionStepMetadataTypeDef",
    {
        "TrainingJob": NotRequired["TrainingJobStepMetadataTypeDef"],
        "ProcessingJob": NotRequired["ProcessingJobStepMetadataTypeDef"],
        "TransformJob": NotRequired["TransformJobStepMetadataTypeDef"],
        "TuningJob": NotRequired["TuningJobStepMetaDataTypeDef"],
        "Model": NotRequired["ModelStepMetadataTypeDef"],
        "RegisterModel": NotRequired["RegisterModelStepMetadataTypeDef"],
        "Condition": NotRequired["ConditionStepMetadataTypeDef"],
        "Callback": NotRequired["CallbackStepMetadataTypeDef"],
        "Lambda": NotRequired["LambdaStepMetadataTypeDef"],
        "QualityCheck": NotRequired["QualityCheckStepMetadataTypeDef"],
        "ClarifyCheck": NotRequired["ClarifyCheckStepMetadataTypeDef"],
        "EMR": NotRequired["EMRStepMetadataTypeDef"],
        "Fail": NotRequired["FailStepMetadataTypeDef"],
    },
)

PipelineExecutionStepTypeDef = TypedDict(
    "PipelineExecutionStepTypeDef",
    {
        "StepName": NotRequired[str],
        "StepDisplayName": NotRequired[str],
        "StepDescription": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "StepStatus": NotRequired[StepStatusType],
        "CacheHitResult": NotRequired["CacheHitResultTypeDef"],
        "AttemptCount": NotRequired[int],
        "FailureReason": NotRequired[str],
        "Metadata": NotRequired["PipelineExecutionStepMetadataTypeDef"],
    },
)

PipelineExecutionSummaryTypeDef = TypedDict(
    "PipelineExecutionSummaryTypeDef",
    {
        "PipelineExecutionArn": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "PipelineExecutionStatus": NotRequired[PipelineExecutionStatusType],
        "PipelineExecutionDescription": NotRequired[str],
        "PipelineExecutionDisplayName": NotRequired[str],
        "PipelineExecutionFailureReason": NotRequired[str],
    },
)

PipelineExecutionTypeDef = TypedDict(
    "PipelineExecutionTypeDef",
    {
        "PipelineArn": NotRequired[str],
        "PipelineExecutionArn": NotRequired[str],
        "PipelineExecutionDisplayName": NotRequired[str],
        "PipelineExecutionStatus": NotRequired[PipelineExecutionStatusType],
        "PipelineExecutionDescription": NotRequired[str],
        "PipelineExperimentConfig": NotRequired["PipelineExperimentConfigTypeDef"],
        "FailureReason": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "CreatedBy": NotRequired["UserContextTypeDef"],
        "LastModifiedBy": NotRequired["UserContextTypeDef"],
        "ParallelismConfiguration": NotRequired["ParallelismConfigurationTypeDef"],
        "PipelineParameters": NotRequired[List["ParameterTypeDef"]],
    },
)

PipelineExperimentConfigTypeDef = TypedDict(
    "PipelineExperimentConfigTypeDef",
    {
        "ExperimentName": NotRequired[str],
        "TrialName": NotRequired[str],
    },
)

PipelineSummaryTypeDef = TypedDict(
    "PipelineSummaryTypeDef",
    {
        "PipelineArn": NotRequired[str],
        "PipelineName": NotRequired[str],
        "PipelineDisplayName": NotRequired[str],
        "PipelineDescription": NotRequired[str],
        "RoleArn": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "LastExecutionTime": NotRequired[datetime],
    },
)

PipelineTypeDef = TypedDict(
    "PipelineTypeDef",
    {
        "PipelineArn": NotRequired[str],
        "PipelineName": NotRequired[str],
        "PipelineDisplayName": NotRequired[str],
        "PipelineDescription": NotRequired[str],
        "RoleArn": NotRequired[str],
        "PipelineStatus": NotRequired[Literal["Active"]],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "LastRunTime": NotRequired[datetime],
        "CreatedBy": NotRequired["UserContextTypeDef"],
        "LastModifiedBy": NotRequired["UserContextTypeDef"],
        "ParallelismConfiguration": NotRequired["ParallelismConfigurationTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ProcessingClusterConfigTypeDef = TypedDict(
    "ProcessingClusterConfigTypeDef",
    {
        "InstanceCount": int,
        "InstanceType": ProcessingInstanceTypeType,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": NotRequired[str],
    },
)

ProcessingFeatureStoreOutputTypeDef = TypedDict(
    "ProcessingFeatureStoreOutputTypeDef",
    {
        "FeatureGroupName": str,
    },
)

ProcessingInputTypeDef = TypedDict(
    "ProcessingInputTypeDef",
    {
        "InputName": str,
        "AppManaged": NotRequired[bool],
        "S3Input": NotRequired["ProcessingS3InputTypeDef"],
        "DatasetDefinition": NotRequired["DatasetDefinitionTypeDef"],
    },
)

ProcessingJobStepMetadataTypeDef = TypedDict(
    "ProcessingJobStepMetadataTypeDef",
    {
        "Arn": NotRequired[str],
    },
)

ProcessingJobSummaryTypeDef = TypedDict(
    "ProcessingJobSummaryTypeDef",
    {
        "ProcessingJobName": str,
        "ProcessingJobArn": str,
        "CreationTime": datetime,
        "ProcessingJobStatus": ProcessingJobStatusType,
        "ProcessingEndTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "FailureReason": NotRequired[str],
        "ExitMessage": NotRequired[str],
    },
)

ProcessingJobTypeDef = TypedDict(
    "ProcessingJobTypeDef",
    {
        "ProcessingInputs": NotRequired[List["ProcessingInputTypeDef"]],
        "ProcessingOutputConfig": NotRequired["ProcessingOutputConfigTypeDef"],
        "ProcessingJobName": NotRequired[str],
        "ProcessingResources": NotRequired["ProcessingResourcesTypeDef"],
        "StoppingCondition": NotRequired["ProcessingStoppingConditionTypeDef"],
        "AppSpecification": NotRequired["AppSpecificationTypeDef"],
        "Environment": NotRequired[Dict[str, str]],
        "NetworkConfig": NotRequired["NetworkConfigTypeDef"],
        "RoleArn": NotRequired[str],
        "ExperimentConfig": NotRequired["ExperimentConfigTypeDef"],
        "ProcessingJobArn": NotRequired[str],
        "ProcessingJobStatus": NotRequired[ProcessingJobStatusType],
        "ExitMessage": NotRequired[str],
        "FailureReason": NotRequired[str],
        "ProcessingEndTime": NotRequired[datetime],
        "ProcessingStartTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
        "MonitoringScheduleArn": NotRequired[str],
        "AutoMLJobArn": NotRequired[str],
        "TrainingJobArn": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ProcessingOutputConfigTypeDef = TypedDict(
    "ProcessingOutputConfigTypeDef",
    {
        "Outputs": Sequence["ProcessingOutputTypeDef"],
        "KmsKeyId": NotRequired[str],
    },
)

ProcessingOutputTypeDef = TypedDict(
    "ProcessingOutputTypeDef",
    {
        "OutputName": str,
        "S3Output": NotRequired["ProcessingS3OutputTypeDef"],
        "FeatureStoreOutput": NotRequired["ProcessingFeatureStoreOutputTypeDef"],
        "AppManaged": NotRequired[bool],
    },
)

ProcessingResourcesTypeDef = TypedDict(
    "ProcessingResourcesTypeDef",
    {
        "ClusterConfig": "ProcessingClusterConfigTypeDef",
    },
)

ProcessingS3InputTypeDef = TypedDict(
    "ProcessingS3InputTypeDef",
    {
        "S3Uri": str,
        "S3DataType": ProcessingS3DataTypeType,
        "LocalPath": NotRequired[str],
        "S3InputMode": NotRequired[ProcessingS3InputModeType],
        "S3DataDistributionType": NotRequired[ProcessingS3DataDistributionTypeType],
        "S3CompressionType": NotRequired[ProcessingS3CompressionTypeType],
    },
)

ProcessingS3OutputTypeDef = TypedDict(
    "ProcessingS3OutputTypeDef",
    {
        "S3Uri": str,
        "LocalPath": str,
        "S3UploadMode": ProcessingS3UploadModeType,
    },
)

ProcessingStoppingConditionTypeDef = TypedDict(
    "ProcessingStoppingConditionTypeDef",
    {
        "MaxRuntimeInSeconds": int,
    },
)

ProductionVariantCoreDumpConfigTypeDef = TypedDict(
    "ProductionVariantCoreDumpConfigTypeDef",
    {
        "DestinationS3Uri": str,
        "KmsKeyId": NotRequired[str],
    },
)

ProductionVariantServerlessConfigTypeDef = TypedDict(
    "ProductionVariantServerlessConfigTypeDef",
    {
        "MemorySizeInMB": int,
        "MaxConcurrency": int,
    },
)

ProductionVariantStatusTypeDef = TypedDict(
    "ProductionVariantStatusTypeDef",
    {
        "Status": VariantStatusType,
        "StatusMessage": NotRequired[str],
        "StartTime": NotRequired[datetime],
    },
)

ProductionVariantSummaryTypeDef = TypedDict(
    "ProductionVariantSummaryTypeDef",
    {
        "VariantName": str,
        "DeployedImages": NotRequired[List["DeployedImageTypeDef"]],
        "CurrentWeight": NotRequired[float],
        "DesiredWeight": NotRequired[float],
        "CurrentInstanceCount": NotRequired[int],
        "DesiredInstanceCount": NotRequired[int],
        "VariantStatus": NotRequired[List["ProductionVariantStatusTypeDef"]],
        "CurrentServerlessConfig": NotRequired["ProductionVariantServerlessConfigTypeDef"],
        "DesiredServerlessConfig": NotRequired["ProductionVariantServerlessConfigTypeDef"],
    },
)

ProductionVariantTypeDef = TypedDict(
    "ProductionVariantTypeDef",
    {
        "VariantName": str,
        "ModelName": str,
        "InitialInstanceCount": NotRequired[int],
        "InstanceType": NotRequired[ProductionVariantInstanceTypeType],
        "InitialVariantWeight": NotRequired[float],
        "AcceleratorType": NotRequired[ProductionVariantAcceleratorTypeType],
        "CoreDumpConfig": NotRequired["ProductionVariantCoreDumpConfigTypeDef"],
        "ServerlessConfig": NotRequired["ProductionVariantServerlessConfigTypeDef"],
    },
)

ProfilerConfigForUpdateTypeDef = TypedDict(
    "ProfilerConfigForUpdateTypeDef",
    {
        "S3OutputPath": NotRequired[str],
        "ProfilingIntervalInMilliseconds": NotRequired[int],
        "ProfilingParameters": NotRequired[Mapping[str, str]],
        "DisableProfiler": NotRequired[bool],
    },
)

ProfilerConfigTypeDef = TypedDict(
    "ProfilerConfigTypeDef",
    {
        "S3OutputPath": str,
        "ProfilingIntervalInMilliseconds": NotRequired[int],
        "ProfilingParameters": NotRequired[Mapping[str, str]],
    },
)

ProfilerRuleConfigurationTypeDef = TypedDict(
    "ProfilerRuleConfigurationTypeDef",
    {
        "RuleConfigurationName": str,
        "RuleEvaluatorImage": str,
        "LocalPath": NotRequired[str],
        "S3OutputPath": NotRequired[str],
        "InstanceType": NotRequired[ProcessingInstanceTypeType],
        "VolumeSizeInGB": NotRequired[int],
        "RuleParameters": NotRequired[Mapping[str, str]],
    },
)

ProfilerRuleEvaluationStatusTypeDef = TypedDict(
    "ProfilerRuleEvaluationStatusTypeDef",
    {
        "RuleConfigurationName": NotRequired[str],
        "RuleEvaluationJobArn": NotRequired[str],
        "RuleEvaluationStatus": NotRequired[RuleEvaluationStatusType],
        "StatusDetails": NotRequired[str],
        "LastModifiedTime": NotRequired[datetime],
    },
)

ProjectSummaryTypeDef = TypedDict(
    "ProjectSummaryTypeDef",
    {
        "ProjectName": str,
        "ProjectArn": str,
        "ProjectId": str,
        "CreationTime": datetime,
        "ProjectStatus": ProjectStatusType,
        "ProjectDescription": NotRequired[str],
    },
)

ProjectTypeDef = TypedDict(
    "ProjectTypeDef",
    {
        "ProjectArn": NotRequired[str],
        "ProjectName": NotRequired[str],
        "ProjectId": NotRequired[str],
        "ProjectDescription": NotRequired[str],
        "ServiceCatalogProvisioningDetails": NotRequired[
            "ServiceCatalogProvisioningDetailsTypeDef"
        ],
        "ServiceCatalogProvisionedProductDetails": NotRequired[
            "ServiceCatalogProvisionedProductDetailsTypeDef"
        ],
        "ProjectStatus": NotRequired[ProjectStatusType],
        "CreatedBy": NotRequired["UserContextTypeDef"],
        "CreationTime": NotRequired[datetime],
        "Tags": NotRequired[List["TagTypeDef"]],
        "LastModifiedTime": NotRequired[datetime],
        "LastModifiedBy": NotRequired["UserContextTypeDef"],
    },
)

PropertyNameQueryTypeDef = TypedDict(
    "PropertyNameQueryTypeDef",
    {
        "PropertyNameHint": str,
    },
)

PropertyNameSuggestionTypeDef = TypedDict(
    "PropertyNameSuggestionTypeDef",
    {
        "PropertyName": NotRequired[str],
    },
)

ProvisioningParameterTypeDef = TypedDict(
    "ProvisioningParameterTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

PublicWorkforceTaskPriceTypeDef = TypedDict(
    "PublicWorkforceTaskPriceTypeDef",
    {
        "AmountInUsd": NotRequired["USDTypeDef"],
    },
)

PutModelPackageGroupPolicyInputRequestTypeDef = TypedDict(
    "PutModelPackageGroupPolicyInputRequestTypeDef",
    {
        "ModelPackageGroupName": str,
        "ResourcePolicy": str,
    },
)

PutModelPackageGroupPolicyOutputTypeDef = TypedDict(
    "PutModelPackageGroupPolicyOutputTypeDef",
    {
        "ModelPackageGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QualityCheckStepMetadataTypeDef = TypedDict(
    "QualityCheckStepMetadataTypeDef",
    {
        "CheckType": NotRequired[str],
        "BaselineUsedForDriftCheckStatistics": NotRequired[str],
        "BaselineUsedForDriftCheckConstraints": NotRequired[str],
        "CalculatedBaselineStatistics": NotRequired[str],
        "CalculatedBaselineConstraints": NotRequired[str],
        "ModelPackageGroupName": NotRequired[str],
        "ViolationReport": NotRequired[str],
        "CheckJobArn": NotRequired[str],
        "SkipCheck": NotRequired[bool],
        "RegisterNewBaseline": NotRequired[bool],
    },
)

QueryFiltersTypeDef = TypedDict(
    "QueryFiltersTypeDef",
    {
        "Types": NotRequired[Sequence[str]],
        "LineageTypes": NotRequired[Sequence[LineageTypeType]],
        "CreatedBefore": NotRequired[Union[datetime, str]],
        "CreatedAfter": NotRequired[Union[datetime, str]],
        "ModifiedBefore": NotRequired[Union[datetime, str]],
        "ModifiedAfter": NotRequired[Union[datetime, str]],
        "Properties": NotRequired[Mapping[str, str]],
    },
)

QueryLineageRequestRequestTypeDef = TypedDict(
    "QueryLineageRequestRequestTypeDef",
    {
        "StartArns": Sequence[str],
        "Direction": NotRequired[DirectionType],
        "IncludeEdges": NotRequired[bool],
        "Filters": NotRequired["QueryFiltersTypeDef"],
        "MaxDepth": NotRequired[int],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

QueryLineageResponseTypeDef = TypedDict(
    "QueryLineageResponseTypeDef",
    {
        "Vertices": List["VertexTypeDef"],
        "Edges": List["EdgeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RStudioServerProAppSettingsTypeDef = TypedDict(
    "RStudioServerProAppSettingsTypeDef",
    {
        "AccessStatus": NotRequired[RStudioServerProAccessStatusType],
        "UserGroup": NotRequired[RStudioServerProUserGroupType],
    },
)

RStudioServerProDomainSettingsForUpdateTypeDef = TypedDict(
    "RStudioServerProDomainSettingsForUpdateTypeDef",
    {
        "DomainExecutionRoleArn": str,
        "DefaultResourceSpec": NotRequired["ResourceSpecTypeDef"],
    },
)

RStudioServerProDomainSettingsTypeDef = TypedDict(
    "RStudioServerProDomainSettingsTypeDef",
    {
        "DomainExecutionRoleArn": str,
        "RStudioConnectUrl": NotRequired[str],
        "RStudioPackageManagerUrl": NotRequired[str],
        "DefaultResourceSpec": NotRequired["ResourceSpecTypeDef"],
    },
)

RecommendationJobInputConfigTypeDef = TypedDict(
    "RecommendationJobInputConfigTypeDef",
    {
        "ModelPackageVersionArn": str,
        "JobDurationInSeconds": NotRequired[int],
        "TrafficPattern": NotRequired["TrafficPatternTypeDef"],
        "ResourceLimit": NotRequired["RecommendationJobResourceLimitTypeDef"],
        "EndpointConfigurations": NotRequired[Sequence["EndpointInputConfigurationTypeDef"]],
    },
)

RecommendationJobResourceLimitTypeDef = TypedDict(
    "RecommendationJobResourceLimitTypeDef",
    {
        "MaxNumberOfTests": NotRequired[int],
        "MaxParallelOfTests": NotRequired[int],
    },
)

RecommendationJobStoppingConditionsTypeDef = TypedDict(
    "RecommendationJobStoppingConditionsTypeDef",
    {
        "MaxInvocations": NotRequired[int],
        "ModelLatencyThresholds": NotRequired[Sequence["ModelLatencyThresholdTypeDef"]],
    },
)

RecommendationMetricsTypeDef = TypedDict(
    "RecommendationMetricsTypeDef",
    {
        "CostPerHour": float,
        "CostPerInference": float,
        "MaxInvocations": int,
        "ModelLatency": int,
    },
)

RedshiftDatasetDefinitionTypeDef = TypedDict(
    "RedshiftDatasetDefinitionTypeDef",
    {
        "ClusterId": str,
        "Database": str,
        "DbUser": str,
        "QueryString": str,
        "ClusterRoleArn": str,
        "OutputS3Uri": str,
        "OutputFormat": RedshiftResultFormatType,
        "KmsKeyId": NotRequired[str],
        "OutputCompression": NotRequired[RedshiftResultCompressionTypeType],
    },
)

RegisterDevicesRequestRequestTypeDef = TypedDict(
    "RegisterDevicesRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
        "Devices": Sequence["DeviceTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

RegisterModelStepMetadataTypeDef = TypedDict(
    "RegisterModelStepMetadataTypeDef",
    {
        "Arn": NotRequired[str],
    },
)

RenderUiTemplateRequestRequestTypeDef = TypedDict(
    "RenderUiTemplateRequestRequestTypeDef",
    {
        "Task": "RenderableTaskTypeDef",
        "RoleArn": str,
        "UiTemplate": NotRequired["UiTemplateTypeDef"],
        "HumanTaskUiArn": NotRequired[str],
    },
)

RenderUiTemplateResponseTypeDef = TypedDict(
    "RenderUiTemplateResponseTypeDef",
    {
        "RenderedContent": str,
        "Errors": List["RenderingErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RenderableTaskTypeDef = TypedDict(
    "RenderableTaskTypeDef",
    {
        "Input": str,
    },
)

RenderingErrorTypeDef = TypedDict(
    "RenderingErrorTypeDef",
    {
        "Code": str,
        "Message": str,
    },
)

RepositoryAuthConfigTypeDef = TypedDict(
    "RepositoryAuthConfigTypeDef",
    {
        "RepositoryCredentialsProviderArn": str,
    },
)

ResolvedAttributesTypeDef = TypedDict(
    "ResolvedAttributesTypeDef",
    {
        "AutoMLJobObjective": NotRequired["AutoMLJobObjectiveTypeDef"],
        "ProblemType": NotRequired[ProblemTypeType],
        "CompletionCriteria": NotRequired["AutoMLJobCompletionCriteriaTypeDef"],
    },
)

ResourceConfigTypeDef = TypedDict(
    "ResourceConfigTypeDef",
    {
        "InstanceType": TrainingInstanceTypeType,
        "InstanceCount": int,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": NotRequired[str],
    },
)

ResourceLimitsTypeDef = TypedDict(
    "ResourceLimitsTypeDef",
    {
        "MaxNumberOfTrainingJobs": int,
        "MaxParallelTrainingJobs": int,
    },
)

ResourceSpecTypeDef = TypedDict(
    "ResourceSpecTypeDef",
    {
        "SageMakerImageArn": NotRequired[str],
        "SageMakerImageVersionArn": NotRequired[str],
        "InstanceType": NotRequired[AppInstanceTypeType],
        "LifecycleConfigArn": NotRequired[str],
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

RetentionPolicyTypeDef = TypedDict(
    "RetentionPolicyTypeDef",
    {
        "HomeEfsFileSystem": NotRequired[RetentionTypeType],
    },
)

RetryPipelineExecutionRequestRequestTypeDef = TypedDict(
    "RetryPipelineExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionArn": str,
        "ClientRequestToken": str,
        "ParallelismConfiguration": NotRequired["ParallelismConfigurationTypeDef"],
    },
)

RetryPipelineExecutionResponseTypeDef = TypedDict(
    "RetryPipelineExecutionResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RetryStrategyTypeDef = TypedDict(
    "RetryStrategyTypeDef",
    {
        "MaximumRetryAttempts": int,
    },
)

S3DataSourceTypeDef = TypedDict(
    "S3DataSourceTypeDef",
    {
        "S3DataType": S3DataTypeType,
        "S3Uri": str,
        "S3DataDistributionType": NotRequired[S3DataDistributionType],
        "AttributeNames": NotRequired[Sequence[str]],
    },
)

S3StorageConfigTypeDef = TypedDict(
    "S3StorageConfigTypeDef",
    {
        "S3Uri": str,
        "KmsKeyId": NotRequired[str],
        "ResolvedOutputS3Uri": NotRequired[str],
    },
)

ScheduleConfigTypeDef = TypedDict(
    "ScheduleConfigTypeDef",
    {
        "ScheduleExpression": str,
    },
)

SearchExpressionTypeDef = TypedDict(
    "SearchExpressionTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "NestedFilters": NotRequired[Sequence["NestedFiltersTypeDef"]],
        "SubExpressions": NotRequired[Sequence[Dict[str, Any]]],
        "Operator": NotRequired[BooleanOperatorType],
    },
)

SearchRecordTypeDef = TypedDict(
    "SearchRecordTypeDef",
    {
        "TrainingJob": NotRequired["TrainingJobTypeDef"],
        "Experiment": NotRequired["ExperimentTypeDef"],
        "Trial": NotRequired["TrialTypeDef"],
        "TrialComponent": NotRequired["TrialComponentTypeDef"],
        "Endpoint": NotRequired["EndpointTypeDef"],
        "ModelPackage": NotRequired["ModelPackageTypeDef"],
        "ModelPackageGroup": NotRequired["ModelPackageGroupTypeDef"],
        "Pipeline": NotRequired["PipelineTypeDef"],
        "PipelineExecution": NotRequired["PipelineExecutionTypeDef"],
        "FeatureGroup": NotRequired["FeatureGroupTypeDef"],
        "Project": NotRequired["ProjectTypeDef"],
    },
)

SearchRequestRequestTypeDef = TypedDict(
    "SearchRequestRequestTypeDef",
    {
        "Resource": ResourceTypeType,
        "SearchExpression": NotRequired["SearchExpressionTypeDef"],
        "SortBy": NotRequired[str],
        "SortOrder": NotRequired[SearchSortOrderType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

SearchResponseTypeDef = TypedDict(
    "SearchResponseTypeDef",
    {
        "Results": List["SearchRecordTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SecondaryStatusTransitionTypeDef = TypedDict(
    "SecondaryStatusTransitionTypeDef",
    {
        "Status": SecondaryStatusType,
        "StartTime": datetime,
        "EndTime": NotRequired[datetime],
        "StatusMessage": NotRequired[str],
    },
)

SendPipelineExecutionStepFailureRequestRequestTypeDef = TypedDict(
    "SendPipelineExecutionStepFailureRequestRequestTypeDef",
    {
        "CallbackToken": str,
        "FailureReason": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
    },
)

SendPipelineExecutionStepFailureResponseTypeDef = TypedDict(
    "SendPipelineExecutionStepFailureResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SendPipelineExecutionStepSuccessRequestRequestTypeDef = TypedDict(
    "SendPipelineExecutionStepSuccessRequestRequestTypeDef",
    {
        "CallbackToken": str,
        "OutputParameters": NotRequired[Sequence["OutputParameterTypeDef"]],
        "ClientRequestToken": NotRequired[str],
    },
)

SendPipelineExecutionStepSuccessResponseTypeDef = TypedDict(
    "SendPipelineExecutionStepSuccessResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceCatalogProvisionedProductDetailsTypeDef = TypedDict(
    "ServiceCatalogProvisionedProductDetailsTypeDef",
    {
        "ProvisionedProductId": NotRequired[str],
        "ProvisionedProductStatusMessage": NotRequired[str],
    },
)

ServiceCatalogProvisioningDetailsTypeDef = TypedDict(
    "ServiceCatalogProvisioningDetailsTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": NotRequired[str],
        "PathId": NotRequired[str],
        "ProvisioningParameters": NotRequired[Sequence["ProvisioningParameterTypeDef"]],
    },
)

ServiceCatalogProvisioningUpdateDetailsTypeDef = TypedDict(
    "ServiceCatalogProvisioningUpdateDetailsTypeDef",
    {
        "ProvisioningArtifactId": NotRequired[str],
        "ProvisioningParameters": NotRequired[Sequence["ProvisioningParameterTypeDef"]],
    },
)

SharingSettingsTypeDef = TypedDict(
    "SharingSettingsTypeDef",
    {
        "NotebookOutputOption": NotRequired[NotebookOutputOptionType],
        "S3OutputPath": NotRequired[str],
        "S3KmsKeyId": NotRequired[str],
    },
)

ShuffleConfigTypeDef = TypedDict(
    "ShuffleConfigTypeDef",
    {
        "Seed": int,
    },
)

SourceAlgorithmSpecificationTypeDef = TypedDict(
    "SourceAlgorithmSpecificationTypeDef",
    {
        "SourceAlgorithms": Sequence["SourceAlgorithmTypeDef"],
    },
)

SourceAlgorithmTypeDef = TypedDict(
    "SourceAlgorithmTypeDef",
    {
        "AlgorithmName": str,
        "ModelDataUrl": NotRequired[str],
    },
)

SourceIpConfigTypeDef = TypedDict(
    "SourceIpConfigTypeDef",
    {
        "Cidrs": Sequence[str],
    },
)

StartMonitoringScheduleRequestRequestTypeDef = TypedDict(
    "StartMonitoringScheduleRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
    },
)

StartNotebookInstanceInputRequestTypeDef = TypedDict(
    "StartNotebookInstanceInputRequestTypeDef",
    {
        "NotebookInstanceName": str,
    },
)

StartPipelineExecutionRequestRequestTypeDef = TypedDict(
    "StartPipelineExecutionRequestRequestTypeDef",
    {
        "PipelineName": str,
        "ClientRequestToken": str,
        "PipelineExecutionDisplayName": NotRequired[str],
        "PipelineParameters": NotRequired[Sequence["ParameterTypeDef"]],
        "PipelineExecutionDescription": NotRequired[str],
        "ParallelismConfiguration": NotRequired["ParallelismConfigurationTypeDef"],
    },
)

StartPipelineExecutionResponseTypeDef = TypedDict(
    "StartPipelineExecutionResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopAutoMLJobRequestRequestTypeDef = TypedDict(
    "StopAutoMLJobRequestRequestTypeDef",
    {
        "AutoMLJobName": str,
    },
)

StopCompilationJobRequestRequestTypeDef = TypedDict(
    "StopCompilationJobRequestRequestTypeDef",
    {
        "CompilationJobName": str,
    },
)

StopEdgePackagingJobRequestRequestTypeDef = TypedDict(
    "StopEdgePackagingJobRequestRequestTypeDef",
    {
        "EdgePackagingJobName": str,
    },
)

StopHyperParameterTuningJobRequestRequestTypeDef = TypedDict(
    "StopHyperParameterTuningJobRequestRequestTypeDef",
    {
        "HyperParameterTuningJobName": str,
    },
)

StopInferenceRecommendationsJobRequestRequestTypeDef = TypedDict(
    "StopInferenceRecommendationsJobRequestRequestTypeDef",
    {
        "JobName": str,
    },
)

StopLabelingJobRequestRequestTypeDef = TypedDict(
    "StopLabelingJobRequestRequestTypeDef",
    {
        "LabelingJobName": str,
    },
)

StopMonitoringScheduleRequestRequestTypeDef = TypedDict(
    "StopMonitoringScheduleRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
    },
)

StopNotebookInstanceInputRequestTypeDef = TypedDict(
    "StopNotebookInstanceInputRequestTypeDef",
    {
        "NotebookInstanceName": str,
    },
)

StopPipelineExecutionRequestRequestTypeDef = TypedDict(
    "StopPipelineExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionArn": str,
        "ClientRequestToken": str,
    },
)

StopPipelineExecutionResponseTypeDef = TypedDict(
    "StopPipelineExecutionResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopProcessingJobRequestRequestTypeDef = TypedDict(
    "StopProcessingJobRequestRequestTypeDef",
    {
        "ProcessingJobName": str,
    },
)

StopTrainingJobRequestRequestTypeDef = TypedDict(
    "StopTrainingJobRequestRequestTypeDef",
    {
        "TrainingJobName": str,
    },
)

StopTransformJobRequestRequestTypeDef = TypedDict(
    "StopTransformJobRequestRequestTypeDef",
    {
        "TransformJobName": str,
    },
)

StoppingConditionTypeDef = TypedDict(
    "StoppingConditionTypeDef",
    {
        "MaxRuntimeInSeconds": NotRequired[int],
        "MaxWaitTimeInSeconds": NotRequired[int],
    },
)

StudioLifecycleConfigDetailsTypeDef = TypedDict(
    "StudioLifecycleConfigDetailsTypeDef",
    {
        "StudioLifecycleConfigArn": NotRequired[str],
        "StudioLifecycleConfigName": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "StudioLifecycleConfigAppType": NotRequired[StudioLifecycleConfigAppTypeType],
    },
)

SubscribedWorkteamTypeDef = TypedDict(
    "SubscribedWorkteamTypeDef",
    {
        "WorkteamArn": str,
        "MarketplaceTitle": NotRequired[str],
        "SellerName": NotRequired[str],
        "MarketplaceDescription": NotRequired[str],
        "ListingId": NotRequired[str],
    },
)

SuggestionQueryTypeDef = TypedDict(
    "SuggestionQueryTypeDef",
    {
        "PropertyNameQuery": NotRequired["PropertyNameQueryTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TargetPlatformTypeDef = TypedDict(
    "TargetPlatformTypeDef",
    {
        "Os": TargetPlatformOsType,
        "Arch": TargetPlatformArchType,
        "Accelerator": NotRequired[TargetPlatformAcceleratorType],
    },
)

TensorBoardAppSettingsTypeDef = TypedDict(
    "TensorBoardAppSettingsTypeDef",
    {
        "DefaultResourceSpec": NotRequired["ResourceSpecTypeDef"],
    },
)

TensorBoardOutputConfigTypeDef = TypedDict(
    "TensorBoardOutputConfigTypeDef",
    {
        "S3OutputPath": str,
        "LocalPath": NotRequired[str],
    },
)

TrafficPatternTypeDef = TypedDict(
    "TrafficPatternTypeDef",
    {
        "TrafficType": NotRequired[Literal["PHASES"]],
        "Phases": NotRequired[Sequence["PhaseTypeDef"]],
    },
)

TrafficRoutingConfigTypeDef = TypedDict(
    "TrafficRoutingConfigTypeDef",
    {
        "Type": TrafficRoutingConfigTypeType,
        "WaitIntervalInSeconds": int,
        "CanarySize": NotRequired["CapacitySizeTypeDef"],
        "LinearStepSize": NotRequired["CapacitySizeTypeDef"],
    },
)

TrainingJobDefinitionTypeDef = TypedDict(
    "TrainingJobDefinitionTypeDef",
    {
        "TrainingInputMode": TrainingInputModeType,
        "InputDataConfig": Sequence["ChannelTypeDef"],
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "ResourceConfig": "ResourceConfigTypeDef",
        "StoppingCondition": "StoppingConditionTypeDef",
        "HyperParameters": NotRequired[Mapping[str, str]],
    },
)

TrainingJobStatusCountersTypeDef = TypedDict(
    "TrainingJobStatusCountersTypeDef",
    {
        "Completed": NotRequired[int],
        "InProgress": NotRequired[int],
        "RetryableError": NotRequired[int],
        "NonRetryableError": NotRequired[int],
        "Stopped": NotRequired[int],
    },
)

TrainingJobStepMetadataTypeDef = TypedDict(
    "TrainingJobStepMetadataTypeDef",
    {
        "Arn": NotRequired[str],
    },
)

TrainingJobSummaryTypeDef = TypedDict(
    "TrainingJobSummaryTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "CreationTime": datetime,
        "TrainingJobStatus": TrainingJobStatusType,
        "TrainingEndTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)

TrainingJobTypeDef = TypedDict(
    "TrainingJobTypeDef",
    {
        "TrainingJobName": NotRequired[str],
        "TrainingJobArn": NotRequired[str],
        "TuningJobArn": NotRequired[str],
        "LabelingJobArn": NotRequired[str],
        "AutoMLJobArn": NotRequired[str],
        "ModelArtifacts": NotRequired["ModelArtifactsTypeDef"],
        "TrainingJobStatus": NotRequired[TrainingJobStatusType],
        "SecondaryStatus": NotRequired[SecondaryStatusType],
        "FailureReason": NotRequired[str],
        "HyperParameters": NotRequired[Dict[str, str]],
        "AlgorithmSpecification": NotRequired["AlgorithmSpecificationTypeDef"],
        "RoleArn": NotRequired[str],
        "InputDataConfig": NotRequired[List["ChannelTypeDef"]],
        "OutputDataConfig": NotRequired["OutputDataConfigTypeDef"],
        "ResourceConfig": NotRequired["ResourceConfigTypeDef"],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "StoppingCondition": NotRequired["StoppingConditionTypeDef"],
        "CreationTime": NotRequired[datetime],
        "TrainingStartTime": NotRequired[datetime],
        "TrainingEndTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "SecondaryStatusTransitions": NotRequired[List["SecondaryStatusTransitionTypeDef"]],
        "FinalMetricDataList": NotRequired[List["MetricDataTypeDef"]],
        "EnableNetworkIsolation": NotRequired[bool],
        "EnableInterContainerTrafficEncryption": NotRequired[bool],
        "EnableManagedSpotTraining": NotRequired[bool],
        "CheckpointConfig": NotRequired["CheckpointConfigTypeDef"],
        "TrainingTimeInSeconds": NotRequired[int],
        "BillableTimeInSeconds": NotRequired[int],
        "DebugHookConfig": NotRequired["DebugHookConfigTypeDef"],
        "ExperimentConfig": NotRequired["ExperimentConfigTypeDef"],
        "DebugRuleConfigurations": NotRequired[List["DebugRuleConfigurationTypeDef"]],
        "TensorBoardOutputConfig": NotRequired["TensorBoardOutputConfigTypeDef"],
        "DebugRuleEvaluationStatuses": NotRequired[List["DebugRuleEvaluationStatusTypeDef"]],
        "Environment": NotRequired[Dict[str, str]],
        "RetryStrategy": NotRequired["RetryStrategyTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

TrainingSpecificationTypeDef = TypedDict(
    "TrainingSpecificationTypeDef",
    {
        "TrainingImage": str,
        "SupportedTrainingInstanceTypes": Sequence[TrainingInstanceTypeType],
        "TrainingChannels": Sequence["ChannelSpecificationTypeDef"],
        "TrainingImageDigest": NotRequired[str],
        "SupportedHyperParameters": NotRequired[Sequence["HyperParameterSpecificationTypeDef"]],
        "SupportsDistributedTraining": NotRequired[bool],
        "MetricDefinitions": NotRequired[Sequence["MetricDefinitionTypeDef"]],
        "SupportedTuningJobObjectiveMetrics": NotRequired[
            Sequence["HyperParameterTuningJobObjectiveTypeDef"]
        ],
    },
)

TransformDataSourceTypeDef = TypedDict(
    "TransformDataSourceTypeDef",
    {
        "S3DataSource": "TransformS3DataSourceTypeDef",
    },
)

TransformInputTypeDef = TypedDict(
    "TransformInputTypeDef",
    {
        "DataSource": "TransformDataSourceTypeDef",
        "ContentType": NotRequired[str],
        "CompressionType": NotRequired[CompressionTypeType],
        "SplitType": NotRequired[SplitTypeType],
    },
)

TransformJobDefinitionTypeDef = TypedDict(
    "TransformJobDefinitionTypeDef",
    {
        "TransformInput": "TransformInputTypeDef",
        "TransformOutput": "TransformOutputTypeDef",
        "TransformResources": "TransformResourcesTypeDef",
        "MaxConcurrentTransforms": NotRequired[int],
        "MaxPayloadInMB": NotRequired[int],
        "BatchStrategy": NotRequired[BatchStrategyType],
        "Environment": NotRequired[Mapping[str, str]],
    },
)

TransformJobStepMetadataTypeDef = TypedDict(
    "TransformJobStepMetadataTypeDef",
    {
        "Arn": NotRequired[str],
    },
)

TransformJobSummaryTypeDef = TypedDict(
    "TransformJobSummaryTypeDef",
    {
        "TransformJobName": str,
        "TransformJobArn": str,
        "CreationTime": datetime,
        "TransformJobStatus": TransformJobStatusType,
        "TransformEndTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "FailureReason": NotRequired[str],
    },
)

TransformJobTypeDef = TypedDict(
    "TransformJobTypeDef",
    {
        "TransformJobName": NotRequired[str],
        "TransformJobArn": NotRequired[str],
        "TransformJobStatus": NotRequired[TransformJobStatusType],
        "FailureReason": NotRequired[str],
        "ModelName": NotRequired[str],
        "MaxConcurrentTransforms": NotRequired[int],
        "ModelClientConfig": NotRequired["ModelClientConfigTypeDef"],
        "MaxPayloadInMB": NotRequired[int],
        "BatchStrategy": NotRequired[BatchStrategyType],
        "Environment": NotRequired[Dict[str, str]],
        "TransformInput": NotRequired["TransformInputTypeDef"],
        "TransformOutput": NotRequired["TransformOutputTypeDef"],
        "TransformResources": NotRequired["TransformResourcesTypeDef"],
        "CreationTime": NotRequired[datetime],
        "TransformStartTime": NotRequired[datetime],
        "TransformEndTime": NotRequired[datetime],
        "LabelingJobArn": NotRequired[str],
        "AutoMLJobArn": NotRequired[str],
        "DataProcessing": NotRequired["DataProcessingTypeDef"],
        "ExperimentConfig": NotRequired["ExperimentConfigTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

TransformOutputTypeDef = TypedDict(
    "TransformOutputTypeDef",
    {
        "S3OutputPath": str,
        "Accept": NotRequired[str],
        "AssembleWith": NotRequired[AssemblyTypeType],
        "KmsKeyId": NotRequired[str],
    },
)

TransformResourcesTypeDef = TypedDict(
    "TransformResourcesTypeDef",
    {
        "InstanceType": TransformInstanceTypeType,
        "InstanceCount": int,
        "VolumeKmsKeyId": NotRequired[str],
    },
)

TransformS3DataSourceTypeDef = TypedDict(
    "TransformS3DataSourceTypeDef",
    {
        "S3DataType": S3DataTypeType,
        "S3Uri": str,
    },
)

TrialComponentArtifactTypeDef = TypedDict(
    "TrialComponentArtifactTypeDef",
    {
        "Value": str,
        "MediaType": NotRequired[str],
    },
)

TrialComponentMetricSummaryTypeDef = TypedDict(
    "TrialComponentMetricSummaryTypeDef",
    {
        "MetricName": NotRequired[str],
        "SourceArn": NotRequired[str],
        "TimeStamp": NotRequired[datetime],
        "Max": NotRequired[float],
        "Min": NotRequired[float],
        "Last": NotRequired[float],
        "Count": NotRequired[int],
        "Avg": NotRequired[float],
        "StdDev": NotRequired[float],
    },
)

TrialComponentParameterValueTypeDef = TypedDict(
    "TrialComponentParameterValueTypeDef",
    {
        "StringValue": NotRequired[str],
        "NumberValue": NotRequired[float],
    },
)

TrialComponentSimpleSummaryTypeDef = TypedDict(
    "TrialComponentSimpleSummaryTypeDef",
    {
        "TrialComponentName": NotRequired[str],
        "TrialComponentArn": NotRequired[str],
        "TrialComponentSource": NotRequired["TrialComponentSourceTypeDef"],
        "CreationTime": NotRequired[datetime],
        "CreatedBy": NotRequired["UserContextTypeDef"],
    },
)

TrialComponentSourceDetailTypeDef = TypedDict(
    "TrialComponentSourceDetailTypeDef",
    {
        "SourceArn": NotRequired[str],
        "TrainingJob": NotRequired["TrainingJobTypeDef"],
        "ProcessingJob": NotRequired["ProcessingJobTypeDef"],
        "TransformJob": NotRequired["TransformJobTypeDef"],
    },
)

TrialComponentSourceTypeDef = TypedDict(
    "TrialComponentSourceTypeDef",
    {
        "SourceArn": str,
        "SourceType": NotRequired[str],
    },
)

TrialComponentStatusTypeDef = TypedDict(
    "TrialComponentStatusTypeDef",
    {
        "PrimaryStatus": NotRequired[TrialComponentPrimaryStatusType],
        "Message": NotRequired[str],
    },
)

TrialComponentSummaryTypeDef = TypedDict(
    "TrialComponentSummaryTypeDef",
    {
        "TrialComponentName": NotRequired[str],
        "TrialComponentArn": NotRequired[str],
        "DisplayName": NotRequired[str],
        "TrialComponentSource": NotRequired["TrialComponentSourceTypeDef"],
        "Status": NotRequired["TrialComponentStatusTypeDef"],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
        "CreatedBy": NotRequired["UserContextTypeDef"],
        "LastModifiedTime": NotRequired[datetime],
        "LastModifiedBy": NotRequired["UserContextTypeDef"],
    },
)

TrialComponentTypeDef = TypedDict(
    "TrialComponentTypeDef",
    {
        "TrialComponentName": NotRequired[str],
        "DisplayName": NotRequired[str],
        "TrialComponentArn": NotRequired[str],
        "Source": NotRequired["TrialComponentSourceTypeDef"],
        "Status": NotRequired["TrialComponentStatusTypeDef"],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
        "CreatedBy": NotRequired["UserContextTypeDef"],
        "LastModifiedTime": NotRequired[datetime],
        "LastModifiedBy": NotRequired["UserContextTypeDef"],
        "Parameters": NotRequired[Dict[str, "TrialComponentParameterValueTypeDef"]],
        "InputArtifacts": NotRequired[Dict[str, "TrialComponentArtifactTypeDef"]],
        "OutputArtifacts": NotRequired[Dict[str, "TrialComponentArtifactTypeDef"]],
        "Metrics": NotRequired[List["TrialComponentMetricSummaryTypeDef"]],
        "MetadataProperties": NotRequired["MetadataPropertiesTypeDef"],
        "SourceDetail": NotRequired["TrialComponentSourceDetailTypeDef"],
        "LineageGroupArn": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "Parents": NotRequired[List["ParentTypeDef"]],
    },
)

TrialSourceTypeDef = TypedDict(
    "TrialSourceTypeDef",
    {
        "SourceArn": str,
        "SourceType": NotRequired[str],
    },
)

TrialSummaryTypeDef = TypedDict(
    "TrialSummaryTypeDef",
    {
        "TrialArn": NotRequired[str],
        "TrialName": NotRequired[str],
        "DisplayName": NotRequired[str],
        "TrialSource": NotRequired["TrialSourceTypeDef"],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)

TrialTypeDef = TypedDict(
    "TrialTypeDef",
    {
        "TrialName": NotRequired[str],
        "TrialArn": NotRequired[str],
        "DisplayName": NotRequired[str],
        "ExperimentName": NotRequired[str],
        "Source": NotRequired["TrialSourceTypeDef"],
        "CreationTime": NotRequired[datetime],
        "CreatedBy": NotRequired["UserContextTypeDef"],
        "LastModifiedTime": NotRequired[datetime],
        "LastModifiedBy": NotRequired["UserContextTypeDef"],
        "MetadataProperties": NotRequired["MetadataPropertiesTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
        "TrialComponentSummaries": NotRequired[List["TrialComponentSimpleSummaryTypeDef"]],
    },
)

TuningJobCompletionCriteriaTypeDef = TypedDict(
    "TuningJobCompletionCriteriaTypeDef",
    {
        "TargetObjectiveMetricValue": float,
    },
)

TuningJobStepMetaDataTypeDef = TypedDict(
    "TuningJobStepMetaDataTypeDef",
    {
        "Arn": NotRequired[str],
    },
)

USDTypeDef = TypedDict(
    "USDTypeDef",
    {
        "Dollars": NotRequired[int],
        "Cents": NotRequired[int],
        "TenthFractionsOfACent": NotRequired[int],
    },
)

UiConfigTypeDef = TypedDict(
    "UiConfigTypeDef",
    {
        "UiTemplateS3Uri": NotRequired[str],
        "HumanTaskUiArn": NotRequired[str],
    },
)

UiTemplateInfoTypeDef = TypedDict(
    "UiTemplateInfoTypeDef",
    {
        "Url": NotRequired[str],
        "ContentSha256": NotRequired[str],
    },
)

UiTemplateTypeDef = TypedDict(
    "UiTemplateTypeDef",
    {
        "Content": str,
    },
)

UpdateActionRequestRequestTypeDef = TypedDict(
    "UpdateActionRequestRequestTypeDef",
    {
        "ActionName": str,
        "Description": NotRequired[str],
        "Status": NotRequired[ActionStatusType],
        "Properties": NotRequired[Mapping[str, str]],
        "PropertiesToRemove": NotRequired[Sequence[str]],
    },
)

UpdateActionResponseTypeDef = TypedDict(
    "UpdateActionResponseTypeDef",
    {
        "ActionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAppImageConfigRequestRequestTypeDef = TypedDict(
    "UpdateAppImageConfigRequestRequestTypeDef",
    {
        "AppImageConfigName": str,
        "KernelGatewayImageConfig": NotRequired["KernelGatewayImageConfigTypeDef"],
    },
)

UpdateAppImageConfigResponseTypeDef = TypedDict(
    "UpdateAppImageConfigResponseTypeDef",
    {
        "AppImageConfigArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateArtifactRequestRequestTypeDef = TypedDict(
    "UpdateArtifactRequestRequestTypeDef",
    {
        "ArtifactArn": str,
        "ArtifactName": NotRequired[str],
        "Properties": NotRequired[Mapping[str, str]],
        "PropertiesToRemove": NotRequired[Sequence[str]],
    },
)

UpdateArtifactResponseTypeDef = TypedDict(
    "UpdateArtifactResponseTypeDef",
    {
        "ArtifactArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCodeRepositoryInputRequestTypeDef = TypedDict(
    "UpdateCodeRepositoryInputRequestTypeDef",
    {
        "CodeRepositoryName": str,
        "GitConfig": NotRequired["GitConfigForUpdateTypeDef"],
    },
)

UpdateCodeRepositoryOutputTypeDef = TypedDict(
    "UpdateCodeRepositoryOutputTypeDef",
    {
        "CodeRepositoryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateContextRequestRequestTypeDef = TypedDict(
    "UpdateContextRequestRequestTypeDef",
    {
        "ContextName": str,
        "Description": NotRequired[str],
        "Properties": NotRequired[Mapping[str, str]],
        "PropertiesToRemove": NotRequired[Sequence[str]],
    },
)

UpdateContextResponseTypeDef = TypedDict(
    "UpdateContextResponseTypeDef",
    {
        "ContextArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDeviceFleetRequestRequestTypeDef = TypedDict(
    "UpdateDeviceFleetRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
        "OutputConfig": "EdgeOutputConfigTypeDef",
        "RoleArn": NotRequired[str],
        "Description": NotRequired[str],
        "EnableIotRoleAlias": NotRequired[bool],
    },
)

UpdateDevicesRequestRequestTypeDef = TypedDict(
    "UpdateDevicesRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
        "Devices": Sequence["DeviceTypeDef"],
    },
)

UpdateDomainRequestRequestTypeDef = TypedDict(
    "UpdateDomainRequestRequestTypeDef",
    {
        "DomainId": str,
        "DefaultUserSettings": NotRequired["UserSettingsTypeDef"],
        "DomainSettingsForUpdate": NotRequired["DomainSettingsForUpdateTypeDef"],
    },
)

UpdateDomainResponseTypeDef = TypedDict(
    "UpdateDomainResponseTypeDef",
    {
        "DomainArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEndpointInputRequestTypeDef = TypedDict(
    "UpdateEndpointInputRequestTypeDef",
    {
        "EndpointName": str,
        "EndpointConfigName": str,
        "RetainAllVariantProperties": NotRequired[bool],
        "ExcludeRetainedVariantProperties": NotRequired[Sequence["VariantPropertyTypeDef"]],
        "DeploymentConfig": NotRequired["DeploymentConfigTypeDef"],
        "RetainDeploymentConfig": NotRequired[bool],
    },
)

UpdateEndpointOutputTypeDef = TypedDict(
    "UpdateEndpointOutputTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEndpointWeightsAndCapacitiesInputRequestTypeDef = TypedDict(
    "UpdateEndpointWeightsAndCapacitiesInputRequestTypeDef",
    {
        "EndpointName": str,
        "DesiredWeightsAndCapacities": Sequence["DesiredWeightAndCapacityTypeDef"],
    },
)

UpdateEndpointWeightsAndCapacitiesOutputTypeDef = TypedDict(
    "UpdateEndpointWeightsAndCapacitiesOutputTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateExperimentRequestRequestTypeDef = TypedDict(
    "UpdateExperimentRequestRequestTypeDef",
    {
        "ExperimentName": str,
        "DisplayName": NotRequired[str],
        "Description": NotRequired[str],
    },
)

UpdateExperimentResponseTypeDef = TypedDict(
    "UpdateExperimentResponseTypeDef",
    {
        "ExperimentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateImageRequestRequestTypeDef = TypedDict(
    "UpdateImageRequestRequestTypeDef",
    {
        "ImageName": str,
        "DeleteProperties": NotRequired[Sequence[str]],
        "Description": NotRequired[str],
        "DisplayName": NotRequired[str],
        "RoleArn": NotRequired[str],
    },
)

UpdateImageResponseTypeDef = TypedDict(
    "UpdateImageResponseTypeDef",
    {
        "ImageArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateModelPackageInputRequestTypeDef = TypedDict(
    "UpdateModelPackageInputRequestTypeDef",
    {
        "ModelPackageArn": str,
        "ModelApprovalStatus": NotRequired[ModelApprovalStatusType],
        "ApprovalDescription": NotRequired[str],
        "CustomerMetadataProperties": NotRequired[Mapping[str, str]],
        "CustomerMetadataPropertiesToRemove": NotRequired[Sequence[str]],
        "AdditionalInferenceSpecificationsToAdd": NotRequired[
            Sequence["AdditionalInferenceSpecificationDefinitionTypeDef"]
        ],
    },
)

UpdateModelPackageOutputTypeDef = TypedDict(
    "UpdateModelPackageOutputTypeDef",
    {
        "ModelPackageArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMonitoringScheduleRequestRequestTypeDef = TypedDict(
    "UpdateMonitoringScheduleRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringScheduleConfig": "MonitoringScheduleConfigTypeDef",
    },
)

UpdateMonitoringScheduleResponseTypeDef = TypedDict(
    "UpdateMonitoringScheduleResponseTypeDef",
    {
        "MonitoringScheduleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateNotebookInstanceInputRequestTypeDef = TypedDict(
    "UpdateNotebookInstanceInputRequestTypeDef",
    {
        "NotebookInstanceName": str,
        "InstanceType": NotRequired[InstanceTypeType],
        "RoleArn": NotRequired[str],
        "LifecycleConfigName": NotRequired[str],
        "DisassociateLifecycleConfig": NotRequired[bool],
        "VolumeSizeInGB": NotRequired[int],
        "DefaultCodeRepository": NotRequired[str],
        "AdditionalCodeRepositories": NotRequired[Sequence[str]],
        "AcceleratorTypes": NotRequired[Sequence[NotebookInstanceAcceleratorTypeType]],
        "DisassociateAcceleratorTypes": NotRequired[bool],
        "DisassociateDefaultCodeRepository": NotRequired[bool],
        "DisassociateAdditionalCodeRepositories": NotRequired[bool],
        "RootAccess": NotRequired[RootAccessType],
    },
)

UpdateNotebookInstanceLifecycleConfigInputRequestTypeDef = TypedDict(
    "UpdateNotebookInstanceLifecycleConfigInputRequestTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
        "OnCreate": NotRequired[Sequence["NotebookInstanceLifecycleHookTypeDef"]],
        "OnStart": NotRequired[Sequence["NotebookInstanceLifecycleHookTypeDef"]],
    },
)

UpdatePipelineExecutionRequestRequestTypeDef = TypedDict(
    "UpdatePipelineExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionArn": str,
        "PipelineExecutionDescription": NotRequired[str],
        "PipelineExecutionDisplayName": NotRequired[str],
        "ParallelismConfiguration": NotRequired["ParallelismConfigurationTypeDef"],
    },
)

UpdatePipelineExecutionResponseTypeDef = TypedDict(
    "UpdatePipelineExecutionResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePipelineRequestRequestTypeDef = TypedDict(
    "UpdatePipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
        "PipelineDisplayName": NotRequired[str],
        "PipelineDefinition": NotRequired[str],
        "PipelineDefinitionS3Location": NotRequired["PipelineDefinitionS3LocationTypeDef"],
        "PipelineDescription": NotRequired[str],
        "RoleArn": NotRequired[str],
        "ParallelismConfiguration": NotRequired["ParallelismConfigurationTypeDef"],
    },
)

UpdatePipelineResponseTypeDef = TypedDict(
    "UpdatePipelineResponseTypeDef",
    {
        "PipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProjectInputRequestTypeDef = TypedDict(
    "UpdateProjectInputRequestTypeDef",
    {
        "ProjectName": str,
        "ProjectDescription": NotRequired[str],
        "ServiceCatalogProvisioningUpdateDetails": NotRequired[
            "ServiceCatalogProvisioningUpdateDetailsTypeDef"
        ],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

UpdateProjectOutputTypeDef = TypedDict(
    "UpdateProjectOutputTypeDef",
    {
        "ProjectArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTrainingJobRequestRequestTypeDef = TypedDict(
    "UpdateTrainingJobRequestRequestTypeDef",
    {
        "TrainingJobName": str,
        "ProfilerConfig": NotRequired["ProfilerConfigForUpdateTypeDef"],
        "ProfilerRuleConfigurations": NotRequired[Sequence["ProfilerRuleConfigurationTypeDef"]],
    },
)

UpdateTrainingJobResponseTypeDef = TypedDict(
    "UpdateTrainingJobResponseTypeDef",
    {
        "TrainingJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTrialComponentRequestRequestTypeDef = TypedDict(
    "UpdateTrialComponentRequestRequestTypeDef",
    {
        "TrialComponentName": str,
        "DisplayName": NotRequired[str],
        "Status": NotRequired["TrialComponentStatusTypeDef"],
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "Parameters": NotRequired[Mapping[str, "TrialComponentParameterValueTypeDef"]],
        "ParametersToRemove": NotRequired[Sequence[str]],
        "InputArtifacts": NotRequired[Mapping[str, "TrialComponentArtifactTypeDef"]],
        "InputArtifactsToRemove": NotRequired[Sequence[str]],
        "OutputArtifacts": NotRequired[Mapping[str, "TrialComponentArtifactTypeDef"]],
        "OutputArtifactsToRemove": NotRequired[Sequence[str]],
    },
)

UpdateTrialComponentResponseTypeDef = TypedDict(
    "UpdateTrialComponentResponseTypeDef",
    {
        "TrialComponentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTrialRequestRequestTypeDef = TypedDict(
    "UpdateTrialRequestRequestTypeDef",
    {
        "TrialName": str,
        "DisplayName": NotRequired[str],
    },
)

UpdateTrialResponseTypeDef = TypedDict(
    "UpdateTrialResponseTypeDef",
    {
        "TrialArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserProfileRequestRequestTypeDef = TypedDict(
    "UpdateUserProfileRequestRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
        "UserSettings": NotRequired["UserSettingsTypeDef"],
    },
)

UpdateUserProfileResponseTypeDef = TypedDict(
    "UpdateUserProfileResponseTypeDef",
    {
        "UserProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateWorkforceRequestRequestTypeDef = TypedDict(
    "UpdateWorkforceRequestRequestTypeDef",
    {
        "WorkforceName": str,
        "SourceIpConfig": NotRequired["SourceIpConfigTypeDef"],
        "OidcConfig": NotRequired["OidcConfigTypeDef"],
    },
)

UpdateWorkforceResponseTypeDef = TypedDict(
    "UpdateWorkforceResponseTypeDef",
    {
        "Workforce": "WorkforceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateWorkteamRequestRequestTypeDef = TypedDict(
    "UpdateWorkteamRequestRequestTypeDef",
    {
        "WorkteamName": str,
        "MemberDefinitions": NotRequired[Sequence["MemberDefinitionTypeDef"]],
        "Description": NotRequired[str],
        "NotificationConfiguration": NotRequired["NotificationConfigurationTypeDef"],
    },
)

UpdateWorkteamResponseTypeDef = TypedDict(
    "UpdateWorkteamResponseTypeDef",
    {
        "Workteam": "WorkteamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserContextTypeDef = TypedDict(
    "UserContextTypeDef",
    {
        "UserProfileArn": NotRequired[str],
        "UserProfileName": NotRequired[str],
        "DomainId": NotRequired[str],
    },
)

UserProfileDetailsTypeDef = TypedDict(
    "UserProfileDetailsTypeDef",
    {
        "DomainId": NotRequired[str],
        "UserProfileName": NotRequired[str],
        "Status": NotRequired[UserProfileStatusType],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)

UserSettingsTypeDef = TypedDict(
    "UserSettingsTypeDef",
    {
        "ExecutionRole": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "SharingSettings": NotRequired["SharingSettingsTypeDef"],
        "JupyterServerAppSettings": NotRequired["JupyterServerAppSettingsTypeDef"],
        "KernelGatewayAppSettings": NotRequired["KernelGatewayAppSettingsTypeDef"],
        "TensorBoardAppSettings": NotRequired["TensorBoardAppSettingsTypeDef"],
        "RStudioServerProAppSettings": NotRequired["RStudioServerProAppSettingsTypeDef"],
        "RSessionAppSettings": NotRequired[Mapping[str, Any]],
    },
)

VariantPropertyTypeDef = TypedDict(
    "VariantPropertyTypeDef",
    {
        "VariantPropertyType": VariantPropertyTypeType,
    },
)

VertexTypeDef = TypedDict(
    "VertexTypeDef",
    {
        "Arn": NotRequired[str],
        "Type": NotRequired[str],
        "LineageType": NotRequired[LineageTypeType],
    },
)

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "SecurityGroupIds": Sequence[str],
        "Subnets": Sequence[str],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)

WorkforceTypeDef = TypedDict(
    "WorkforceTypeDef",
    {
        "WorkforceName": str,
        "WorkforceArn": str,
        "LastUpdatedDate": NotRequired[datetime],
        "SourceIpConfig": NotRequired["SourceIpConfigTypeDef"],
        "SubDomain": NotRequired[str],
        "CognitoConfig": NotRequired["CognitoConfigTypeDef"],
        "OidcConfig": NotRequired["OidcConfigForResponseTypeDef"],
        "CreateDate": NotRequired[datetime],
    },
)

WorkteamTypeDef = TypedDict(
    "WorkteamTypeDef",
    {
        "WorkteamName": str,
        "MemberDefinitions": List["MemberDefinitionTypeDef"],
        "WorkteamArn": str,
        "Description": str,
        "WorkforceArn": NotRequired[str],
        "ProductListingIds": NotRequired[List[str]],
        "SubDomain": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "LastUpdatedDate": NotRequired[datetime],
        "NotificationConfiguration": NotRequired["NotificationConfigurationTypeDef"],
    },
)
