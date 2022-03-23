"""
Type annotations for imagebuilder service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/type_defs.html)

Usage::

    ```python
    from mypy_boto3_imagebuilder.type_defs import AdditionalInstanceConfigurationTypeDef

    data: AdditionalInstanceConfigurationTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    BuildTypeType,
    ComponentTypeType,
    DiskImageFormatType,
    EbsVolumeTypeType,
    ImageStatusType,
    ImageTypeType,
    OwnershipType,
    PipelineExecutionStartConditionType,
    PipelineStatusType,
    PlatformType,
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
    "AdditionalInstanceConfigurationTypeDef",
    "AmiDistributionConfigurationTypeDef",
    "AmiTypeDef",
    "CancelImageCreationRequestRequestTypeDef",
    "CancelImageCreationResponseTypeDef",
    "ComponentConfigurationTypeDef",
    "ComponentParameterDetailTypeDef",
    "ComponentParameterTypeDef",
    "ComponentStateTypeDef",
    "ComponentSummaryTypeDef",
    "ComponentTypeDef",
    "ComponentVersionTypeDef",
    "ContainerDistributionConfigurationTypeDef",
    "ContainerRecipeSummaryTypeDef",
    "ContainerRecipeTypeDef",
    "ContainerTypeDef",
    "CreateComponentRequestRequestTypeDef",
    "CreateComponentResponseTypeDef",
    "CreateContainerRecipeRequestRequestTypeDef",
    "CreateContainerRecipeResponseTypeDef",
    "CreateDistributionConfigurationRequestRequestTypeDef",
    "CreateDistributionConfigurationResponseTypeDef",
    "CreateImagePipelineRequestRequestTypeDef",
    "CreateImagePipelineResponseTypeDef",
    "CreateImageRecipeRequestRequestTypeDef",
    "CreateImageRecipeResponseTypeDef",
    "CreateImageRequestRequestTypeDef",
    "CreateImageResponseTypeDef",
    "CreateInfrastructureConfigurationRequestRequestTypeDef",
    "CreateInfrastructureConfigurationResponseTypeDef",
    "DeleteComponentRequestRequestTypeDef",
    "DeleteComponentResponseTypeDef",
    "DeleteContainerRecipeRequestRequestTypeDef",
    "DeleteContainerRecipeResponseTypeDef",
    "DeleteDistributionConfigurationRequestRequestTypeDef",
    "DeleteDistributionConfigurationResponseTypeDef",
    "DeleteImagePipelineRequestRequestTypeDef",
    "DeleteImagePipelineResponseTypeDef",
    "DeleteImageRecipeRequestRequestTypeDef",
    "DeleteImageRecipeResponseTypeDef",
    "DeleteImageRequestRequestTypeDef",
    "DeleteImageResponseTypeDef",
    "DeleteInfrastructureConfigurationRequestRequestTypeDef",
    "DeleteInfrastructureConfigurationResponseTypeDef",
    "DistributionConfigurationSummaryTypeDef",
    "DistributionConfigurationTypeDef",
    "DistributionTypeDef",
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    "FastLaunchConfigurationTypeDef",
    "FastLaunchLaunchTemplateSpecificationTypeDef",
    "FastLaunchSnapshotConfigurationTypeDef",
    "FilterTypeDef",
    "GetComponentPolicyRequestRequestTypeDef",
    "GetComponentPolicyResponseTypeDef",
    "GetComponentRequestRequestTypeDef",
    "GetComponentResponseTypeDef",
    "GetContainerRecipePolicyRequestRequestTypeDef",
    "GetContainerRecipePolicyResponseTypeDef",
    "GetContainerRecipeRequestRequestTypeDef",
    "GetContainerRecipeResponseTypeDef",
    "GetDistributionConfigurationRequestRequestTypeDef",
    "GetDistributionConfigurationResponseTypeDef",
    "GetImagePipelineRequestRequestTypeDef",
    "GetImagePipelineResponseTypeDef",
    "GetImagePolicyRequestRequestTypeDef",
    "GetImagePolicyResponseTypeDef",
    "GetImageRecipePolicyRequestRequestTypeDef",
    "GetImageRecipePolicyResponseTypeDef",
    "GetImageRecipeRequestRequestTypeDef",
    "GetImageRecipeResponseTypeDef",
    "GetImageRequestRequestTypeDef",
    "GetImageResponseTypeDef",
    "GetInfrastructureConfigurationRequestRequestTypeDef",
    "GetInfrastructureConfigurationResponseTypeDef",
    "ImagePackageTypeDef",
    "ImagePipelineTypeDef",
    "ImageRecipeSummaryTypeDef",
    "ImageRecipeTypeDef",
    "ImageStateTypeDef",
    "ImageSummaryTypeDef",
    "ImageTestsConfigurationTypeDef",
    "ImageTypeDef",
    "ImageVersionTypeDef",
    "ImportComponentRequestRequestTypeDef",
    "ImportComponentResponseTypeDef",
    "ImportVmImageRequestRequestTypeDef",
    "ImportVmImageResponseTypeDef",
    "InfrastructureConfigurationSummaryTypeDef",
    "InfrastructureConfigurationTypeDef",
    "InstanceBlockDeviceMappingTypeDef",
    "InstanceConfigurationTypeDef",
    "InstanceMetadataOptionsTypeDef",
    "LaunchPermissionConfigurationTypeDef",
    "LaunchTemplateConfigurationTypeDef",
    "ListComponentBuildVersionsRequestRequestTypeDef",
    "ListComponentBuildVersionsResponseTypeDef",
    "ListComponentsRequestRequestTypeDef",
    "ListComponentsResponseTypeDef",
    "ListContainerRecipesRequestRequestTypeDef",
    "ListContainerRecipesResponseTypeDef",
    "ListDistributionConfigurationsRequestRequestTypeDef",
    "ListDistributionConfigurationsResponseTypeDef",
    "ListImageBuildVersionsRequestRequestTypeDef",
    "ListImageBuildVersionsResponseTypeDef",
    "ListImagePackagesRequestRequestTypeDef",
    "ListImagePackagesResponseTypeDef",
    "ListImagePipelineImagesRequestRequestTypeDef",
    "ListImagePipelineImagesResponseTypeDef",
    "ListImagePipelinesRequestRequestTypeDef",
    "ListImagePipelinesResponseTypeDef",
    "ListImageRecipesRequestRequestTypeDef",
    "ListImageRecipesResponseTypeDef",
    "ListImagesRequestRequestTypeDef",
    "ListImagesResponseTypeDef",
    "ListInfrastructureConfigurationsRequestRequestTypeDef",
    "ListInfrastructureConfigurationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LoggingTypeDef",
    "OutputResourcesTypeDef",
    "PutComponentPolicyRequestRequestTypeDef",
    "PutComponentPolicyResponseTypeDef",
    "PutContainerRecipePolicyRequestRequestTypeDef",
    "PutContainerRecipePolicyResponseTypeDef",
    "PutImagePolicyRequestRequestTypeDef",
    "PutImagePolicyResponseTypeDef",
    "PutImageRecipePolicyRequestRequestTypeDef",
    "PutImageRecipePolicyResponseTypeDef",
    "ResponseMetadataTypeDef",
    "S3ExportConfigurationTypeDef",
    "S3LogsTypeDef",
    "ScheduleTypeDef",
    "StartImagePipelineExecutionRequestRequestTypeDef",
    "StartImagePipelineExecutionResponseTypeDef",
    "SystemsManagerAgentTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TargetContainerRepositoryTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDistributionConfigurationRequestRequestTypeDef",
    "UpdateDistributionConfigurationResponseTypeDef",
    "UpdateImagePipelineRequestRequestTypeDef",
    "UpdateImagePipelineResponseTypeDef",
    "UpdateInfrastructureConfigurationRequestRequestTypeDef",
    "UpdateInfrastructureConfigurationResponseTypeDef",
)

AdditionalInstanceConfigurationTypeDef = TypedDict(
    "AdditionalInstanceConfigurationTypeDef",
    {
        "systemsManagerAgent": NotRequired["SystemsManagerAgentTypeDef"],
        "userDataOverride": NotRequired[str],
    },
)

AmiDistributionConfigurationTypeDef = TypedDict(
    "AmiDistributionConfigurationTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "targetAccountIds": NotRequired[Sequence[str]],
        "amiTags": NotRequired[Mapping[str, str]],
        "kmsKeyId": NotRequired[str],
        "launchPermission": NotRequired["LaunchPermissionConfigurationTypeDef"],
    },
)

AmiTypeDef = TypedDict(
    "AmiTypeDef",
    {
        "region": NotRequired[str],
        "image": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "state": NotRequired["ImageStateTypeDef"],
        "accountId": NotRequired[str],
    },
)

CancelImageCreationRequestRequestTypeDef = TypedDict(
    "CancelImageCreationRequestRequestTypeDef",
    {
        "imageBuildVersionArn": str,
        "clientToken": str,
    },
)

CancelImageCreationResponseTypeDef = TypedDict(
    "CancelImageCreationResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imageBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ComponentConfigurationTypeDef = TypedDict(
    "ComponentConfigurationTypeDef",
    {
        "componentArn": str,
        "parameters": NotRequired[Sequence["ComponentParameterTypeDef"]],
    },
)

ComponentParameterDetailTypeDef = TypedDict(
    "ComponentParameterDetailTypeDef",
    {
        "name": str,
        "type": str,
        "defaultValue": NotRequired[List[str]],
        "description": NotRequired[str],
    },
)

ComponentParameterTypeDef = TypedDict(
    "ComponentParameterTypeDef",
    {
        "name": str,
        "value": Sequence[str],
    },
)

ComponentStateTypeDef = TypedDict(
    "ComponentStateTypeDef",
    {
        "status": NotRequired[Literal["DEPRECATED"]],
        "reason": NotRequired[str],
    },
)

ComponentSummaryTypeDef = TypedDict(
    "ComponentSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "version": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "supportedOsVersions": NotRequired[List[str]],
        "state": NotRequired["ComponentStateTypeDef"],
        "type": NotRequired[ComponentTypeType],
        "owner": NotRequired[str],
        "description": NotRequired[str],
        "changeDescription": NotRequired[str],
        "dateCreated": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

ComponentTypeDef = TypedDict(
    "ComponentTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "version": NotRequired[str],
        "description": NotRequired[str],
        "changeDescription": NotRequired[str],
        "type": NotRequired[ComponentTypeType],
        "platform": NotRequired[PlatformType],
        "supportedOsVersions": NotRequired[List[str]],
        "state": NotRequired["ComponentStateTypeDef"],
        "parameters": NotRequired[List["ComponentParameterDetailTypeDef"]],
        "owner": NotRequired[str],
        "data": NotRequired[str],
        "kmsKeyId": NotRequired[str],
        "encrypted": NotRequired[bool],
        "dateCreated": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

ComponentVersionTypeDef = TypedDict(
    "ComponentVersionTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "version": NotRequired[str],
        "description": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "supportedOsVersions": NotRequired[List[str]],
        "type": NotRequired[ComponentTypeType],
        "owner": NotRequired[str],
        "dateCreated": NotRequired[str],
    },
)

ContainerDistributionConfigurationTypeDef = TypedDict(
    "ContainerDistributionConfigurationTypeDef",
    {
        "targetRepository": "TargetContainerRepositoryTypeDef",
        "description": NotRequired[str],
        "containerTags": NotRequired[Sequence[str]],
    },
)

ContainerRecipeSummaryTypeDef = TypedDict(
    "ContainerRecipeSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "containerType": NotRequired[Literal["DOCKER"]],
        "name": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "owner": NotRequired[str],
        "parentImage": NotRequired[str],
        "dateCreated": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

ContainerRecipeTypeDef = TypedDict(
    "ContainerRecipeTypeDef",
    {
        "arn": NotRequired[str],
        "containerType": NotRequired[Literal["DOCKER"]],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "owner": NotRequired[str],
        "version": NotRequired[str],
        "components": NotRequired[List["ComponentConfigurationTypeDef"]],
        "instanceConfiguration": NotRequired["InstanceConfigurationTypeDef"],
        "dockerfileTemplateData": NotRequired[str],
        "kmsKeyId": NotRequired[str],
        "encrypted": NotRequired[bool],
        "parentImage": NotRequired[str],
        "dateCreated": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "workingDirectory": NotRequired[str],
        "targetRepository": NotRequired["TargetContainerRepositoryTypeDef"],
    },
)

ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "region": NotRequired[str],
        "imageUris": NotRequired[List[str]],
    },
)

CreateComponentRequestRequestTypeDef = TypedDict(
    "CreateComponentRequestRequestTypeDef",
    {
        "name": str,
        "semanticVersion": str,
        "platform": PlatformType,
        "clientToken": str,
        "description": NotRequired[str],
        "changeDescription": NotRequired[str],
        "supportedOsVersions": NotRequired[Sequence[str]],
        "data": NotRequired[str],
        "uri": NotRequired[str],
        "kmsKeyId": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateComponentResponseTypeDef = TypedDict(
    "CreateComponentResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "componentBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateContainerRecipeRequestRequestTypeDef = TypedDict(
    "CreateContainerRecipeRequestRequestTypeDef",
    {
        "containerType": Literal["DOCKER"],
        "name": str,
        "semanticVersion": str,
        "components": Sequence["ComponentConfigurationTypeDef"],
        "parentImage": str,
        "targetRepository": "TargetContainerRepositoryTypeDef",
        "clientToken": str,
        "description": NotRequired[str],
        "instanceConfiguration": NotRequired["InstanceConfigurationTypeDef"],
        "dockerfileTemplateData": NotRequired[str],
        "dockerfileTemplateUri": NotRequired[str],
        "platformOverride": NotRequired[PlatformType],
        "imageOsVersionOverride": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "workingDirectory": NotRequired[str],
        "kmsKeyId": NotRequired[str],
    },
)

CreateContainerRecipeResponseTypeDef = TypedDict(
    "CreateContainerRecipeResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "containerRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDistributionConfigurationRequestRequestTypeDef = TypedDict(
    "CreateDistributionConfigurationRequestRequestTypeDef",
    {
        "name": str,
        "distributions": Sequence["DistributionTypeDef"],
        "clientToken": str,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateDistributionConfigurationResponseTypeDef = TypedDict(
    "CreateDistributionConfigurationResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "distributionConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateImagePipelineRequestRequestTypeDef = TypedDict(
    "CreateImagePipelineRequestRequestTypeDef",
    {
        "name": str,
        "infrastructureConfigurationArn": str,
        "clientToken": str,
        "description": NotRequired[str],
        "imageRecipeArn": NotRequired[str],
        "containerRecipeArn": NotRequired[str],
        "distributionConfigurationArn": NotRequired[str],
        "imageTestsConfiguration": NotRequired["ImageTestsConfigurationTypeDef"],
        "enhancedImageMetadataEnabled": NotRequired[bool],
        "schedule": NotRequired["ScheduleTypeDef"],
        "status": NotRequired[PipelineStatusType],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateImagePipelineResponseTypeDef = TypedDict(
    "CreateImagePipelineResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imagePipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateImageRecipeRequestRequestTypeDef = TypedDict(
    "CreateImageRecipeRequestRequestTypeDef",
    {
        "name": str,
        "semanticVersion": str,
        "components": Sequence["ComponentConfigurationTypeDef"],
        "parentImage": str,
        "clientToken": str,
        "description": NotRequired[str],
        "blockDeviceMappings": NotRequired[Sequence["InstanceBlockDeviceMappingTypeDef"]],
        "tags": NotRequired[Mapping[str, str]],
        "workingDirectory": NotRequired[str],
        "additionalInstanceConfiguration": NotRequired["AdditionalInstanceConfigurationTypeDef"],
    },
)

CreateImageRecipeResponseTypeDef = TypedDict(
    "CreateImageRecipeResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imageRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateImageRequestRequestTypeDef = TypedDict(
    "CreateImageRequestRequestTypeDef",
    {
        "infrastructureConfigurationArn": str,
        "clientToken": str,
        "imageRecipeArn": NotRequired[str],
        "containerRecipeArn": NotRequired[str],
        "distributionConfigurationArn": NotRequired[str],
        "imageTestsConfiguration": NotRequired["ImageTestsConfigurationTypeDef"],
        "enhancedImageMetadataEnabled": NotRequired[bool],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateImageResponseTypeDef = TypedDict(
    "CreateImageResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imageBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInfrastructureConfigurationRequestRequestTypeDef = TypedDict(
    "CreateInfrastructureConfigurationRequestRequestTypeDef",
    {
        "name": str,
        "instanceProfileName": str,
        "clientToken": str,
        "description": NotRequired[str],
        "instanceTypes": NotRequired[Sequence[str]],
        "securityGroupIds": NotRequired[Sequence[str]],
        "subnetId": NotRequired[str],
        "logging": NotRequired["LoggingTypeDef"],
        "keyPair": NotRequired[str],
        "terminateInstanceOnFailure": NotRequired[bool],
        "snsTopicArn": NotRequired[str],
        "resourceTags": NotRequired[Mapping[str, str]],
        "instanceMetadataOptions": NotRequired["InstanceMetadataOptionsTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateInfrastructureConfigurationResponseTypeDef = TypedDict(
    "CreateInfrastructureConfigurationResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "infrastructureConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteComponentRequestRequestTypeDef = TypedDict(
    "DeleteComponentRequestRequestTypeDef",
    {
        "componentBuildVersionArn": str,
    },
)

DeleteComponentResponseTypeDef = TypedDict(
    "DeleteComponentResponseTypeDef",
    {
        "requestId": str,
        "componentBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteContainerRecipeRequestRequestTypeDef = TypedDict(
    "DeleteContainerRecipeRequestRequestTypeDef",
    {
        "containerRecipeArn": str,
    },
)

DeleteContainerRecipeResponseTypeDef = TypedDict(
    "DeleteContainerRecipeResponseTypeDef",
    {
        "requestId": str,
        "containerRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDistributionConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteDistributionConfigurationRequestRequestTypeDef",
    {
        "distributionConfigurationArn": str,
    },
)

DeleteDistributionConfigurationResponseTypeDef = TypedDict(
    "DeleteDistributionConfigurationResponseTypeDef",
    {
        "requestId": str,
        "distributionConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteImagePipelineRequestRequestTypeDef = TypedDict(
    "DeleteImagePipelineRequestRequestTypeDef",
    {
        "imagePipelineArn": str,
    },
)

DeleteImagePipelineResponseTypeDef = TypedDict(
    "DeleteImagePipelineResponseTypeDef",
    {
        "requestId": str,
        "imagePipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteImageRecipeRequestRequestTypeDef = TypedDict(
    "DeleteImageRecipeRequestRequestTypeDef",
    {
        "imageRecipeArn": str,
    },
)

DeleteImageRecipeResponseTypeDef = TypedDict(
    "DeleteImageRecipeResponseTypeDef",
    {
        "requestId": str,
        "imageRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteImageRequestRequestTypeDef = TypedDict(
    "DeleteImageRequestRequestTypeDef",
    {
        "imageBuildVersionArn": str,
    },
)

DeleteImageResponseTypeDef = TypedDict(
    "DeleteImageResponseTypeDef",
    {
        "requestId": str,
        "imageBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInfrastructureConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteInfrastructureConfigurationRequestRequestTypeDef",
    {
        "infrastructureConfigurationArn": str,
    },
)

DeleteInfrastructureConfigurationResponseTypeDef = TypedDict(
    "DeleteInfrastructureConfigurationResponseTypeDef",
    {
        "requestId": str,
        "infrastructureConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DistributionConfigurationSummaryTypeDef = TypedDict(
    "DistributionConfigurationSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "dateCreated": NotRequired[str],
        "dateUpdated": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "regions": NotRequired[List[str]],
    },
)

DistributionConfigurationTypeDef = TypedDict(
    "DistributionConfigurationTypeDef",
    {
        "timeoutMinutes": int,
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "distributions": NotRequired[List["DistributionTypeDef"]],
        "dateCreated": NotRequired[str],
        "dateUpdated": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

DistributionTypeDef = TypedDict(
    "DistributionTypeDef",
    {
        "region": str,
        "amiDistributionConfiguration": NotRequired["AmiDistributionConfigurationTypeDef"],
        "containerDistributionConfiguration": NotRequired[
            "ContainerDistributionConfigurationTypeDef"
        ],
        "licenseConfigurationArns": NotRequired[Sequence[str]],
        "launchTemplateConfigurations": NotRequired[Sequence["LaunchTemplateConfigurationTypeDef"]],
        "s3ExportConfiguration": NotRequired["S3ExportConfigurationTypeDef"],
        "fastLaunchConfigurations": NotRequired[Sequence["FastLaunchConfigurationTypeDef"]],
    },
)

EbsInstanceBlockDeviceSpecificationTypeDef = TypedDict(
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    {
        "encrypted": NotRequired[bool],
        "deleteOnTermination": NotRequired[bool],
        "iops": NotRequired[int],
        "kmsKeyId": NotRequired[str],
        "snapshotId": NotRequired[str],
        "volumeSize": NotRequired[int],
        "volumeType": NotRequired[EbsVolumeTypeType],
        "throughput": NotRequired[int],
    },
)

FastLaunchConfigurationTypeDef = TypedDict(
    "FastLaunchConfigurationTypeDef",
    {
        "enabled": bool,
        "snapshotConfiguration": NotRequired["FastLaunchSnapshotConfigurationTypeDef"],
        "maxParallelLaunches": NotRequired[int],
        "launchTemplate": NotRequired["FastLaunchLaunchTemplateSpecificationTypeDef"],
        "accountId": NotRequired[str],
    },
)

FastLaunchLaunchTemplateSpecificationTypeDef = TypedDict(
    "FastLaunchLaunchTemplateSpecificationTypeDef",
    {
        "launchTemplateId": NotRequired[str],
        "launchTemplateName": NotRequired[str],
        "launchTemplateVersion": NotRequired[str],
    },
)

FastLaunchSnapshotConfigurationTypeDef = TypedDict(
    "FastLaunchSnapshotConfigurationTypeDef",
    {
        "targetResourceCount": NotRequired[int],
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": NotRequired[str],
        "values": NotRequired[Sequence[str]],
    },
)

GetComponentPolicyRequestRequestTypeDef = TypedDict(
    "GetComponentPolicyRequestRequestTypeDef",
    {
        "componentArn": str,
    },
)

GetComponentPolicyResponseTypeDef = TypedDict(
    "GetComponentPolicyResponseTypeDef",
    {
        "requestId": str,
        "policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComponentRequestRequestTypeDef = TypedDict(
    "GetComponentRequestRequestTypeDef",
    {
        "componentBuildVersionArn": str,
    },
)

GetComponentResponseTypeDef = TypedDict(
    "GetComponentResponseTypeDef",
    {
        "requestId": str,
        "component": "ComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerRecipePolicyRequestRequestTypeDef = TypedDict(
    "GetContainerRecipePolicyRequestRequestTypeDef",
    {
        "containerRecipeArn": str,
    },
)

GetContainerRecipePolicyResponseTypeDef = TypedDict(
    "GetContainerRecipePolicyResponseTypeDef",
    {
        "requestId": str,
        "policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerRecipeRequestRequestTypeDef = TypedDict(
    "GetContainerRecipeRequestRequestTypeDef",
    {
        "containerRecipeArn": str,
    },
)

GetContainerRecipeResponseTypeDef = TypedDict(
    "GetContainerRecipeResponseTypeDef",
    {
        "requestId": str,
        "containerRecipe": "ContainerRecipeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDistributionConfigurationRequestRequestTypeDef = TypedDict(
    "GetDistributionConfigurationRequestRequestTypeDef",
    {
        "distributionConfigurationArn": str,
    },
)

GetDistributionConfigurationResponseTypeDef = TypedDict(
    "GetDistributionConfigurationResponseTypeDef",
    {
        "requestId": str,
        "distributionConfiguration": "DistributionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImagePipelineRequestRequestTypeDef = TypedDict(
    "GetImagePipelineRequestRequestTypeDef",
    {
        "imagePipelineArn": str,
    },
)

GetImagePipelineResponseTypeDef = TypedDict(
    "GetImagePipelineResponseTypeDef",
    {
        "requestId": str,
        "imagePipeline": "ImagePipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImagePolicyRequestRequestTypeDef = TypedDict(
    "GetImagePolicyRequestRequestTypeDef",
    {
        "imageArn": str,
    },
)

GetImagePolicyResponseTypeDef = TypedDict(
    "GetImagePolicyResponseTypeDef",
    {
        "requestId": str,
        "policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImageRecipePolicyRequestRequestTypeDef = TypedDict(
    "GetImageRecipePolicyRequestRequestTypeDef",
    {
        "imageRecipeArn": str,
    },
)

GetImageRecipePolicyResponseTypeDef = TypedDict(
    "GetImageRecipePolicyResponseTypeDef",
    {
        "requestId": str,
        "policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImageRecipeRequestRequestTypeDef = TypedDict(
    "GetImageRecipeRequestRequestTypeDef",
    {
        "imageRecipeArn": str,
    },
)

GetImageRecipeResponseTypeDef = TypedDict(
    "GetImageRecipeResponseTypeDef",
    {
        "requestId": str,
        "imageRecipe": "ImageRecipeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImageRequestRequestTypeDef = TypedDict(
    "GetImageRequestRequestTypeDef",
    {
        "imageBuildVersionArn": str,
    },
)

GetImageResponseTypeDef = TypedDict(
    "GetImageResponseTypeDef",
    {
        "requestId": str,
        "image": "ImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInfrastructureConfigurationRequestRequestTypeDef = TypedDict(
    "GetInfrastructureConfigurationRequestRequestTypeDef",
    {
        "infrastructureConfigurationArn": str,
    },
)

GetInfrastructureConfigurationResponseTypeDef = TypedDict(
    "GetInfrastructureConfigurationResponseTypeDef",
    {
        "requestId": str,
        "infrastructureConfiguration": "InfrastructureConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImagePackageTypeDef = TypedDict(
    "ImagePackageTypeDef",
    {
        "packageName": NotRequired[str],
        "packageVersion": NotRequired[str],
    },
)

ImagePipelineTypeDef = TypedDict(
    "ImagePipelineTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "enhancedImageMetadataEnabled": NotRequired[bool],
        "imageRecipeArn": NotRequired[str],
        "containerRecipeArn": NotRequired[str],
        "infrastructureConfigurationArn": NotRequired[str],
        "distributionConfigurationArn": NotRequired[str],
        "imageTestsConfiguration": NotRequired["ImageTestsConfigurationTypeDef"],
        "schedule": NotRequired["ScheduleTypeDef"],
        "status": NotRequired[PipelineStatusType],
        "dateCreated": NotRequired[str],
        "dateUpdated": NotRequired[str],
        "dateLastRun": NotRequired[str],
        "dateNextRun": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

ImageRecipeSummaryTypeDef = TypedDict(
    "ImageRecipeSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "owner": NotRequired[str],
        "parentImage": NotRequired[str],
        "dateCreated": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

ImageRecipeTypeDef = TypedDict(
    "ImageRecipeTypeDef",
    {
        "arn": NotRequired[str],
        "type": NotRequired[ImageTypeType],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "owner": NotRequired[str],
        "version": NotRequired[str],
        "components": NotRequired[List["ComponentConfigurationTypeDef"]],
        "parentImage": NotRequired[str],
        "blockDeviceMappings": NotRequired[List["InstanceBlockDeviceMappingTypeDef"]],
        "dateCreated": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "workingDirectory": NotRequired[str],
        "additionalInstanceConfiguration": NotRequired["AdditionalInstanceConfigurationTypeDef"],
    },
)

ImageStateTypeDef = TypedDict(
    "ImageStateTypeDef",
    {
        "status": NotRequired[ImageStatusType],
        "reason": NotRequired[str],
    },
)

ImageSummaryTypeDef = TypedDict(
    "ImageSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[ImageTypeType],
        "version": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "osVersion": NotRequired[str],
        "state": NotRequired["ImageStateTypeDef"],
        "owner": NotRequired[str],
        "dateCreated": NotRequired[str],
        "outputResources": NotRequired["OutputResourcesTypeDef"],
        "tags": NotRequired[Dict[str, str]],
        "buildType": NotRequired[BuildTypeType],
    },
)

ImageTestsConfigurationTypeDef = TypedDict(
    "ImageTestsConfigurationTypeDef",
    {
        "imageTestsEnabled": NotRequired[bool],
        "timeoutMinutes": NotRequired[int],
    },
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "arn": NotRequired[str],
        "type": NotRequired[ImageTypeType],
        "name": NotRequired[str],
        "version": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "enhancedImageMetadataEnabled": NotRequired[bool],
        "osVersion": NotRequired[str],
        "state": NotRequired["ImageStateTypeDef"],
        "imageRecipe": NotRequired["ImageRecipeTypeDef"],
        "containerRecipe": NotRequired["ContainerRecipeTypeDef"],
        "sourcePipelineName": NotRequired[str],
        "sourcePipelineArn": NotRequired[str],
        "infrastructureConfiguration": NotRequired["InfrastructureConfigurationTypeDef"],
        "distributionConfiguration": NotRequired["DistributionConfigurationTypeDef"],
        "imageTestsConfiguration": NotRequired["ImageTestsConfigurationTypeDef"],
        "dateCreated": NotRequired[str],
        "outputResources": NotRequired["OutputResourcesTypeDef"],
        "tags": NotRequired[Dict[str, str]],
        "buildType": NotRequired[BuildTypeType],
    },
)

ImageVersionTypeDef = TypedDict(
    "ImageVersionTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[ImageTypeType],
        "version": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "osVersion": NotRequired[str],
        "owner": NotRequired[str],
        "dateCreated": NotRequired[str],
        "buildType": NotRequired[BuildTypeType],
    },
)

ImportComponentRequestRequestTypeDef = TypedDict(
    "ImportComponentRequestRequestTypeDef",
    {
        "name": str,
        "semanticVersion": str,
        "type": ComponentTypeType,
        "format": Literal["SHELL"],
        "platform": PlatformType,
        "clientToken": str,
        "description": NotRequired[str],
        "changeDescription": NotRequired[str],
        "data": NotRequired[str],
        "uri": NotRequired[str],
        "kmsKeyId": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

ImportComponentResponseTypeDef = TypedDict(
    "ImportComponentResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "componentBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportVmImageRequestRequestTypeDef = TypedDict(
    "ImportVmImageRequestRequestTypeDef",
    {
        "name": str,
        "semanticVersion": str,
        "platform": PlatformType,
        "vmImportTaskId": str,
        "clientToken": str,
        "description": NotRequired[str],
        "osVersion": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

ImportVmImageResponseTypeDef = TypedDict(
    "ImportVmImageResponseTypeDef",
    {
        "requestId": str,
        "imageArn": str,
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InfrastructureConfigurationSummaryTypeDef = TypedDict(
    "InfrastructureConfigurationSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "dateCreated": NotRequired[str],
        "dateUpdated": NotRequired[str],
        "resourceTags": NotRequired[Dict[str, str]],
        "tags": NotRequired[Dict[str, str]],
        "instanceTypes": NotRequired[List[str]],
        "instanceProfileName": NotRequired[str],
    },
)

InfrastructureConfigurationTypeDef = TypedDict(
    "InfrastructureConfigurationTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "instanceTypes": NotRequired[List[str]],
        "instanceProfileName": NotRequired[str],
        "securityGroupIds": NotRequired[List[str]],
        "subnetId": NotRequired[str],
        "logging": NotRequired["LoggingTypeDef"],
        "keyPair": NotRequired[str],
        "terminateInstanceOnFailure": NotRequired[bool],
        "snsTopicArn": NotRequired[str],
        "dateCreated": NotRequired[str],
        "dateUpdated": NotRequired[str],
        "resourceTags": NotRequired[Dict[str, str]],
        "instanceMetadataOptions": NotRequired["InstanceMetadataOptionsTypeDef"],
        "tags": NotRequired[Dict[str, str]],
    },
)

InstanceBlockDeviceMappingTypeDef = TypedDict(
    "InstanceBlockDeviceMappingTypeDef",
    {
        "deviceName": NotRequired[str],
        "ebs": NotRequired["EbsInstanceBlockDeviceSpecificationTypeDef"],
        "virtualName": NotRequired[str],
        "noDevice": NotRequired[str],
    },
)

InstanceConfigurationTypeDef = TypedDict(
    "InstanceConfigurationTypeDef",
    {
        "image": NotRequired[str],
        "blockDeviceMappings": NotRequired[Sequence["InstanceBlockDeviceMappingTypeDef"]],
    },
)

InstanceMetadataOptionsTypeDef = TypedDict(
    "InstanceMetadataOptionsTypeDef",
    {
        "httpTokens": NotRequired[str],
        "httpPutResponseHopLimit": NotRequired[int],
    },
)

LaunchPermissionConfigurationTypeDef = TypedDict(
    "LaunchPermissionConfigurationTypeDef",
    {
        "userIds": NotRequired[Sequence[str]],
        "userGroups": NotRequired[Sequence[str]],
        "organizationArns": NotRequired[Sequence[str]],
        "organizationalUnitArns": NotRequired[Sequence[str]],
    },
)

LaunchTemplateConfigurationTypeDef = TypedDict(
    "LaunchTemplateConfigurationTypeDef",
    {
        "launchTemplateId": str,
        "accountId": NotRequired[str],
        "setDefaultVersion": NotRequired[bool],
    },
)

ListComponentBuildVersionsRequestRequestTypeDef = TypedDict(
    "ListComponentBuildVersionsRequestRequestTypeDef",
    {
        "componentVersionArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListComponentBuildVersionsResponseTypeDef = TypedDict(
    "ListComponentBuildVersionsResponseTypeDef",
    {
        "requestId": str,
        "componentSummaryList": List["ComponentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListComponentsRequestRequestTypeDef = TypedDict(
    "ListComponentsRequestRequestTypeDef",
    {
        "owner": NotRequired[OwnershipType],
        "filters": NotRequired[Sequence["FilterTypeDef"]],
        "byName": NotRequired[bool],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListComponentsResponseTypeDef = TypedDict(
    "ListComponentsResponseTypeDef",
    {
        "requestId": str,
        "componentVersionList": List["ComponentVersionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContainerRecipesRequestRequestTypeDef = TypedDict(
    "ListContainerRecipesRequestRequestTypeDef",
    {
        "owner": NotRequired[OwnershipType],
        "filters": NotRequired[Sequence["FilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListContainerRecipesResponseTypeDef = TypedDict(
    "ListContainerRecipesResponseTypeDef",
    {
        "requestId": str,
        "containerRecipeSummaryList": List["ContainerRecipeSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributionConfigurationsRequestRequestTypeDef = TypedDict(
    "ListDistributionConfigurationsRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence["FilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListDistributionConfigurationsResponseTypeDef = TypedDict(
    "ListDistributionConfigurationsResponseTypeDef",
    {
        "requestId": str,
        "distributionConfigurationSummaryList": List["DistributionConfigurationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImageBuildVersionsRequestRequestTypeDef = TypedDict(
    "ListImageBuildVersionsRequestRequestTypeDef",
    {
        "imageVersionArn": str,
        "filters": NotRequired[Sequence["FilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListImageBuildVersionsResponseTypeDef = TypedDict(
    "ListImageBuildVersionsResponseTypeDef",
    {
        "requestId": str,
        "imageSummaryList": List["ImageSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImagePackagesRequestRequestTypeDef = TypedDict(
    "ListImagePackagesRequestRequestTypeDef",
    {
        "imageBuildVersionArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListImagePackagesResponseTypeDef = TypedDict(
    "ListImagePackagesResponseTypeDef",
    {
        "requestId": str,
        "imagePackageList": List["ImagePackageTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImagePipelineImagesRequestRequestTypeDef = TypedDict(
    "ListImagePipelineImagesRequestRequestTypeDef",
    {
        "imagePipelineArn": str,
        "filters": NotRequired[Sequence["FilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListImagePipelineImagesResponseTypeDef = TypedDict(
    "ListImagePipelineImagesResponseTypeDef",
    {
        "requestId": str,
        "imageSummaryList": List["ImageSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImagePipelinesRequestRequestTypeDef = TypedDict(
    "ListImagePipelinesRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence["FilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListImagePipelinesResponseTypeDef = TypedDict(
    "ListImagePipelinesResponseTypeDef",
    {
        "requestId": str,
        "imagePipelineList": List["ImagePipelineTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImageRecipesRequestRequestTypeDef = TypedDict(
    "ListImageRecipesRequestRequestTypeDef",
    {
        "owner": NotRequired[OwnershipType],
        "filters": NotRequired[Sequence["FilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListImageRecipesResponseTypeDef = TypedDict(
    "ListImageRecipesResponseTypeDef",
    {
        "requestId": str,
        "imageRecipeSummaryList": List["ImageRecipeSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImagesRequestRequestTypeDef = TypedDict(
    "ListImagesRequestRequestTypeDef",
    {
        "owner": NotRequired[OwnershipType],
        "filters": NotRequired[Sequence["FilterTypeDef"]],
        "byName": NotRequired[bool],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "includeDeprecated": NotRequired[bool],
    },
)

ListImagesResponseTypeDef = TypedDict(
    "ListImagesResponseTypeDef",
    {
        "requestId": str,
        "imageVersionList": List["ImageVersionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInfrastructureConfigurationsRequestRequestTypeDef = TypedDict(
    "ListInfrastructureConfigurationsRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence["FilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListInfrastructureConfigurationsResponseTypeDef = TypedDict(
    "ListInfrastructureConfigurationsResponseTypeDef",
    {
        "requestId": str,
        "infrastructureConfigurationSummaryList": List["InfrastructureConfigurationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingTypeDef = TypedDict(
    "LoggingTypeDef",
    {
        "s3Logs": NotRequired["S3LogsTypeDef"],
    },
)

OutputResourcesTypeDef = TypedDict(
    "OutputResourcesTypeDef",
    {
        "amis": NotRequired[List["AmiTypeDef"]],
        "containers": NotRequired[List["ContainerTypeDef"]],
    },
)

PutComponentPolicyRequestRequestTypeDef = TypedDict(
    "PutComponentPolicyRequestRequestTypeDef",
    {
        "componentArn": str,
        "policy": str,
    },
)

PutComponentPolicyResponseTypeDef = TypedDict(
    "PutComponentPolicyResponseTypeDef",
    {
        "requestId": str,
        "componentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutContainerRecipePolicyRequestRequestTypeDef = TypedDict(
    "PutContainerRecipePolicyRequestRequestTypeDef",
    {
        "containerRecipeArn": str,
        "policy": str,
    },
)

PutContainerRecipePolicyResponseTypeDef = TypedDict(
    "PutContainerRecipePolicyResponseTypeDef",
    {
        "requestId": str,
        "containerRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutImagePolicyRequestRequestTypeDef = TypedDict(
    "PutImagePolicyRequestRequestTypeDef",
    {
        "imageArn": str,
        "policy": str,
    },
)

PutImagePolicyResponseTypeDef = TypedDict(
    "PutImagePolicyResponseTypeDef",
    {
        "requestId": str,
        "imageArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutImageRecipePolicyRequestRequestTypeDef = TypedDict(
    "PutImageRecipePolicyRequestRequestTypeDef",
    {
        "imageRecipeArn": str,
        "policy": str,
    },
)

PutImageRecipePolicyResponseTypeDef = TypedDict(
    "PutImageRecipePolicyResponseTypeDef",
    {
        "requestId": str,
        "imageRecipeArn": str,
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

S3ExportConfigurationTypeDef = TypedDict(
    "S3ExportConfigurationTypeDef",
    {
        "roleName": str,
        "diskImageFormat": DiskImageFormatType,
        "s3Bucket": str,
        "s3Prefix": NotRequired[str],
    },
)

S3LogsTypeDef = TypedDict(
    "S3LogsTypeDef",
    {
        "s3BucketName": NotRequired[str],
        "s3KeyPrefix": NotRequired[str],
    },
)

ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "scheduleExpression": NotRequired[str],
        "timezone": NotRequired[str],
        "pipelineExecutionStartCondition": NotRequired[PipelineExecutionStartConditionType],
    },
)

StartImagePipelineExecutionRequestRequestTypeDef = TypedDict(
    "StartImagePipelineExecutionRequestRequestTypeDef",
    {
        "imagePipelineArn": str,
        "clientToken": str,
    },
)

StartImagePipelineExecutionResponseTypeDef = TypedDict(
    "StartImagePipelineExecutionResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imageBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SystemsManagerAgentTypeDef = TypedDict(
    "SystemsManagerAgentTypeDef",
    {
        "uninstallAfterBuild": NotRequired[bool],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

TargetContainerRepositoryTypeDef = TypedDict(
    "TargetContainerRepositoryTypeDef",
    {
        "service": Literal["ECR"],
        "repositoryName": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateDistributionConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateDistributionConfigurationRequestRequestTypeDef",
    {
        "distributionConfigurationArn": str,
        "distributions": Sequence["DistributionTypeDef"],
        "clientToken": str,
        "description": NotRequired[str],
    },
)

UpdateDistributionConfigurationResponseTypeDef = TypedDict(
    "UpdateDistributionConfigurationResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "distributionConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateImagePipelineRequestRequestTypeDef = TypedDict(
    "UpdateImagePipelineRequestRequestTypeDef",
    {
        "imagePipelineArn": str,
        "infrastructureConfigurationArn": str,
        "clientToken": str,
        "description": NotRequired[str],
        "imageRecipeArn": NotRequired[str],
        "containerRecipeArn": NotRequired[str],
        "distributionConfigurationArn": NotRequired[str],
        "imageTestsConfiguration": NotRequired["ImageTestsConfigurationTypeDef"],
        "enhancedImageMetadataEnabled": NotRequired[bool],
        "schedule": NotRequired["ScheduleTypeDef"],
        "status": NotRequired[PipelineStatusType],
    },
)

UpdateImagePipelineResponseTypeDef = TypedDict(
    "UpdateImagePipelineResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imagePipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateInfrastructureConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateInfrastructureConfigurationRequestRequestTypeDef",
    {
        "infrastructureConfigurationArn": str,
        "instanceProfileName": str,
        "clientToken": str,
        "description": NotRequired[str],
        "instanceTypes": NotRequired[Sequence[str]],
        "securityGroupIds": NotRequired[Sequence[str]],
        "subnetId": NotRequired[str],
        "logging": NotRequired["LoggingTypeDef"],
        "keyPair": NotRequired[str],
        "terminateInstanceOnFailure": NotRequired[bool],
        "snsTopicArn": NotRequired[str],
        "resourceTags": NotRequired[Mapping[str, str]],
        "instanceMetadataOptions": NotRequired["InstanceMetadataOptionsTypeDef"],
    },
)

UpdateInfrastructureConfigurationResponseTypeDef = TypedDict(
    "UpdateInfrastructureConfigurationResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "infrastructureConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
