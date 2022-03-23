"""
Type annotations for lambda service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_lambda/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_lambda.type_defs import AccountLimitTypeDef

    data: AccountLimitTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    ArchitectureType,
    CodeSigningPolicyType,
    EventSourcePositionType,
    InvocationTypeType,
    LastUpdateStatusReasonCodeType,
    LastUpdateStatusType,
    LogTypeType,
    PackageTypeType,
    ProvisionedConcurrencyStatusEnumType,
    RuntimeType,
    SourceAccessTypeType,
    StateReasonCodeType,
    StateType,
    TracingModeType,
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
    "AccountLimitTypeDef",
    "AccountUsageTypeDef",
    "AddLayerVersionPermissionRequestRequestTypeDef",
    "AddLayerVersionPermissionResponseTypeDef",
    "AddPermissionRequestRequestTypeDef",
    "AddPermissionResponseTypeDef",
    "AliasConfigurationResponseMetadataTypeDef",
    "AliasConfigurationTypeDef",
    "AliasRoutingConfigurationTypeDef",
    "AllowedPublishersTypeDef",
    "CodeSigningConfigTypeDef",
    "CodeSigningPoliciesTypeDef",
    "ConcurrencyResponseMetadataTypeDef",
    "ConcurrencyTypeDef",
    "CreateAliasRequestRequestTypeDef",
    "CreateCodeSigningConfigRequestRequestTypeDef",
    "CreateCodeSigningConfigResponseTypeDef",
    "CreateEventSourceMappingRequestRequestTypeDef",
    "CreateFunctionRequestRequestTypeDef",
    "DeadLetterConfigTypeDef",
    "DeleteAliasRequestRequestTypeDef",
    "DeleteCodeSigningConfigRequestRequestTypeDef",
    "DeleteEventSourceMappingRequestRequestTypeDef",
    "DeleteFunctionCodeSigningConfigRequestRequestTypeDef",
    "DeleteFunctionConcurrencyRequestRequestTypeDef",
    "DeleteFunctionEventInvokeConfigRequestRequestTypeDef",
    "DeleteFunctionRequestRequestTypeDef",
    "DeleteLayerVersionRequestRequestTypeDef",
    "DeleteProvisionedConcurrencyConfigRequestRequestTypeDef",
    "DestinationConfigTypeDef",
    "EnvironmentErrorTypeDef",
    "EnvironmentResponseTypeDef",
    "EnvironmentTypeDef",
    "EventSourceMappingConfigurationResponseMetadataTypeDef",
    "EventSourceMappingConfigurationTypeDef",
    "FileSystemConfigTypeDef",
    "FilterCriteriaTypeDef",
    "FilterTypeDef",
    "FunctionCodeLocationTypeDef",
    "FunctionCodeTypeDef",
    "FunctionConfigurationResponseMetadataTypeDef",
    "FunctionConfigurationTypeDef",
    "FunctionEventInvokeConfigResponseMetadataTypeDef",
    "FunctionEventInvokeConfigTypeDef",
    "GetAccountSettingsResponseTypeDef",
    "GetAliasRequestRequestTypeDef",
    "GetCodeSigningConfigRequestRequestTypeDef",
    "GetCodeSigningConfigResponseTypeDef",
    "GetEventSourceMappingRequestRequestTypeDef",
    "GetFunctionCodeSigningConfigRequestRequestTypeDef",
    "GetFunctionCodeSigningConfigResponseTypeDef",
    "GetFunctionConcurrencyRequestRequestTypeDef",
    "GetFunctionConcurrencyResponseTypeDef",
    "GetFunctionConfigurationRequestRequestTypeDef",
    "GetFunctionEventInvokeConfigRequestRequestTypeDef",
    "GetFunctionRequestRequestTypeDef",
    "GetFunctionResponseTypeDef",
    "GetLayerVersionByArnRequestRequestTypeDef",
    "GetLayerVersionPolicyRequestRequestTypeDef",
    "GetLayerVersionPolicyResponseTypeDef",
    "GetLayerVersionRequestRequestTypeDef",
    "GetLayerVersionResponseTypeDef",
    "GetPolicyRequestRequestTypeDef",
    "GetPolicyResponseTypeDef",
    "GetProvisionedConcurrencyConfigRequestRequestTypeDef",
    "GetProvisionedConcurrencyConfigResponseTypeDef",
    "ImageConfigErrorTypeDef",
    "ImageConfigResponseTypeDef",
    "ImageConfigTypeDef",
    "InvocationRequestRequestTypeDef",
    "InvocationResponseTypeDef",
    "InvokeAsyncRequestRequestTypeDef",
    "InvokeAsyncResponseTypeDef",
    "LayerTypeDef",
    "LayerVersionContentInputTypeDef",
    "LayerVersionContentOutputTypeDef",
    "LayerVersionsListItemTypeDef",
    "LayersListItemTypeDef",
    "ListAliasesRequestRequestTypeDef",
    "ListAliasesResponseTypeDef",
    "ListCodeSigningConfigsRequestRequestTypeDef",
    "ListCodeSigningConfigsResponseTypeDef",
    "ListEventSourceMappingsRequestRequestTypeDef",
    "ListEventSourceMappingsResponseTypeDef",
    "ListFunctionEventInvokeConfigsRequestRequestTypeDef",
    "ListFunctionEventInvokeConfigsResponseTypeDef",
    "ListFunctionsByCodeSigningConfigRequestRequestTypeDef",
    "ListFunctionsByCodeSigningConfigResponseTypeDef",
    "ListFunctionsRequestRequestTypeDef",
    "ListFunctionsResponseTypeDef",
    "ListLayerVersionsRequestRequestTypeDef",
    "ListLayerVersionsResponseTypeDef",
    "ListLayersRequestRequestTypeDef",
    "ListLayersResponseTypeDef",
    "ListProvisionedConcurrencyConfigsRequestRequestTypeDef",
    "ListProvisionedConcurrencyConfigsResponseTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "ListVersionsByFunctionRequestRequestTypeDef",
    "ListVersionsByFunctionResponseTypeDef",
    "OnFailureTypeDef",
    "OnSuccessTypeDef",
    "PaginatorConfigTypeDef",
    "ProvisionedConcurrencyConfigListItemTypeDef",
    "PublishLayerVersionRequestRequestTypeDef",
    "PublishLayerVersionResponseTypeDef",
    "PublishVersionRequestRequestTypeDef",
    "PutFunctionCodeSigningConfigRequestRequestTypeDef",
    "PutFunctionCodeSigningConfigResponseTypeDef",
    "PutFunctionConcurrencyRequestRequestTypeDef",
    "PutFunctionEventInvokeConfigRequestRequestTypeDef",
    "PutProvisionedConcurrencyConfigRequestRequestTypeDef",
    "PutProvisionedConcurrencyConfigResponseTypeDef",
    "RemoveLayerVersionPermissionRequestRequestTypeDef",
    "RemovePermissionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SelfManagedEventSourceTypeDef",
    "SourceAccessConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TracingConfigResponseTypeDef",
    "TracingConfigTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAliasRequestRequestTypeDef",
    "UpdateCodeSigningConfigRequestRequestTypeDef",
    "UpdateCodeSigningConfigResponseTypeDef",
    "UpdateEventSourceMappingRequestRequestTypeDef",
    "UpdateFunctionCodeRequestRequestTypeDef",
    "UpdateFunctionConfigurationRequestRequestTypeDef",
    "UpdateFunctionEventInvokeConfigRequestRequestTypeDef",
    "VpcConfigResponseTypeDef",
    "VpcConfigTypeDef",
    "WaiterConfigTypeDef",
)

AccountLimitTypeDef = TypedDict(
    "AccountLimitTypeDef",
    {
        "TotalCodeSize": NotRequired[int],
        "CodeSizeUnzipped": NotRequired[int],
        "CodeSizeZipped": NotRequired[int],
        "ConcurrentExecutions": NotRequired[int],
        "UnreservedConcurrentExecutions": NotRequired[int],
    },
)

AccountUsageTypeDef = TypedDict(
    "AccountUsageTypeDef",
    {
        "TotalCodeSize": NotRequired[int],
        "FunctionCount": NotRequired[int],
    },
)

AddLayerVersionPermissionRequestRequestTypeDef = TypedDict(
    "AddLayerVersionPermissionRequestRequestTypeDef",
    {
        "LayerName": str,
        "VersionNumber": int,
        "StatementId": str,
        "Action": str,
        "Principal": str,
        "OrganizationId": NotRequired[str],
        "RevisionId": NotRequired[str],
    },
)

AddLayerVersionPermissionResponseTypeDef = TypedDict(
    "AddLayerVersionPermissionResponseTypeDef",
    {
        "Statement": str,
        "RevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddPermissionRequestRequestTypeDef = TypedDict(
    "AddPermissionRequestRequestTypeDef",
    {
        "FunctionName": str,
        "StatementId": str,
        "Action": str,
        "Principal": str,
        "SourceArn": NotRequired[str],
        "SourceAccount": NotRequired[str],
        "EventSourceToken": NotRequired[str],
        "Qualifier": NotRequired[str],
        "RevisionId": NotRequired[str],
        "PrincipalOrgID": NotRequired[str],
    },
)

AddPermissionResponseTypeDef = TypedDict(
    "AddPermissionResponseTypeDef",
    {
        "Statement": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AliasConfigurationResponseMetadataTypeDef = TypedDict(
    "AliasConfigurationResponseMetadataTypeDef",
    {
        "AliasArn": str,
        "Name": str,
        "FunctionVersion": str,
        "Description": str,
        "RoutingConfig": "AliasRoutingConfigurationTypeDef",
        "RevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AliasConfigurationTypeDef = TypedDict(
    "AliasConfigurationTypeDef",
    {
        "AliasArn": NotRequired[str],
        "Name": NotRequired[str],
        "FunctionVersion": NotRequired[str],
        "Description": NotRequired[str],
        "RoutingConfig": NotRequired["AliasRoutingConfigurationTypeDef"],
        "RevisionId": NotRequired[str],
    },
)

AliasRoutingConfigurationTypeDef = TypedDict(
    "AliasRoutingConfigurationTypeDef",
    {
        "AdditionalVersionWeights": NotRequired[Mapping[str, float]],
    },
)

AllowedPublishersTypeDef = TypedDict(
    "AllowedPublishersTypeDef",
    {
        "SigningProfileVersionArns": Sequence[str],
    },
)

CodeSigningConfigTypeDef = TypedDict(
    "CodeSigningConfigTypeDef",
    {
        "CodeSigningConfigId": str,
        "CodeSigningConfigArn": str,
        "AllowedPublishers": "AllowedPublishersTypeDef",
        "CodeSigningPolicies": "CodeSigningPoliciesTypeDef",
        "LastModified": str,
        "Description": NotRequired[str],
    },
)

CodeSigningPoliciesTypeDef = TypedDict(
    "CodeSigningPoliciesTypeDef",
    {
        "UntrustedArtifactOnDeployment": NotRequired[CodeSigningPolicyType],
    },
)

ConcurrencyResponseMetadataTypeDef = TypedDict(
    "ConcurrencyResponseMetadataTypeDef",
    {
        "ReservedConcurrentExecutions": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConcurrencyTypeDef = TypedDict(
    "ConcurrencyTypeDef",
    {
        "ReservedConcurrentExecutions": NotRequired[int],
    },
)

CreateAliasRequestRequestTypeDef = TypedDict(
    "CreateAliasRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Name": str,
        "FunctionVersion": str,
        "Description": NotRequired[str],
        "RoutingConfig": NotRequired["AliasRoutingConfigurationTypeDef"],
    },
)

CreateCodeSigningConfigRequestRequestTypeDef = TypedDict(
    "CreateCodeSigningConfigRequestRequestTypeDef",
    {
        "AllowedPublishers": "AllowedPublishersTypeDef",
        "Description": NotRequired[str],
        "CodeSigningPolicies": NotRequired["CodeSigningPoliciesTypeDef"],
    },
)

CreateCodeSigningConfigResponseTypeDef = TypedDict(
    "CreateCodeSigningConfigResponseTypeDef",
    {
        "CodeSigningConfig": "CodeSigningConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEventSourceMappingRequestRequestTypeDef = TypedDict(
    "CreateEventSourceMappingRequestRequestTypeDef",
    {
        "FunctionName": str,
        "EventSourceArn": NotRequired[str],
        "Enabled": NotRequired[bool],
        "BatchSize": NotRequired[int],
        "FilterCriteria": NotRequired["FilterCriteriaTypeDef"],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
        "ParallelizationFactor": NotRequired[int],
        "StartingPosition": NotRequired[EventSourcePositionType],
        "StartingPositionTimestamp": NotRequired[Union[datetime, str]],
        "DestinationConfig": NotRequired["DestinationConfigTypeDef"],
        "MaximumRecordAgeInSeconds": NotRequired[int],
        "BisectBatchOnFunctionError": NotRequired[bool],
        "MaximumRetryAttempts": NotRequired[int],
        "TumblingWindowInSeconds": NotRequired[int],
        "Topics": NotRequired[Sequence[str]],
        "Queues": NotRequired[Sequence[str]],
        "SourceAccessConfigurations": NotRequired[Sequence["SourceAccessConfigurationTypeDef"]],
        "SelfManagedEventSource": NotRequired["SelfManagedEventSourceTypeDef"],
        "FunctionResponseTypes": NotRequired[Sequence[Literal["ReportBatchItemFailures"]]],
    },
)

CreateFunctionRequestRequestTypeDef = TypedDict(
    "CreateFunctionRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Role": str,
        "Code": "FunctionCodeTypeDef",
        "Runtime": NotRequired[RuntimeType],
        "Handler": NotRequired[str],
        "Description": NotRequired[str],
        "Timeout": NotRequired[int],
        "MemorySize": NotRequired[int],
        "Publish": NotRequired[bool],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "PackageType": NotRequired[PackageTypeType],
        "DeadLetterConfig": NotRequired["DeadLetterConfigTypeDef"],
        "Environment": NotRequired["EnvironmentTypeDef"],
        "KMSKeyArn": NotRequired[str],
        "TracingConfig": NotRequired["TracingConfigTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
        "Layers": NotRequired[Sequence[str]],
        "FileSystemConfigs": NotRequired[Sequence["FileSystemConfigTypeDef"]],
        "ImageConfig": NotRequired["ImageConfigTypeDef"],
        "CodeSigningConfigArn": NotRequired[str],
        "Architectures": NotRequired[Sequence[ArchitectureType]],
    },
)

DeadLetterConfigTypeDef = TypedDict(
    "DeadLetterConfigTypeDef",
    {
        "TargetArn": NotRequired[str],
    },
)

DeleteAliasRequestRequestTypeDef = TypedDict(
    "DeleteAliasRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Name": str,
    },
)

DeleteCodeSigningConfigRequestRequestTypeDef = TypedDict(
    "DeleteCodeSigningConfigRequestRequestTypeDef",
    {
        "CodeSigningConfigArn": str,
    },
)

DeleteEventSourceMappingRequestRequestTypeDef = TypedDict(
    "DeleteEventSourceMappingRequestRequestTypeDef",
    {
        "UUID": str,
    },
)

DeleteFunctionCodeSigningConfigRequestRequestTypeDef = TypedDict(
    "DeleteFunctionCodeSigningConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)

DeleteFunctionConcurrencyRequestRequestTypeDef = TypedDict(
    "DeleteFunctionConcurrencyRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)

DeleteFunctionEventInvokeConfigRequestRequestTypeDef = TypedDict(
    "DeleteFunctionEventInvokeConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Qualifier": NotRequired[str],
    },
)

DeleteFunctionRequestRequestTypeDef = TypedDict(
    "DeleteFunctionRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Qualifier": NotRequired[str],
    },
)

DeleteLayerVersionRequestRequestTypeDef = TypedDict(
    "DeleteLayerVersionRequestRequestTypeDef",
    {
        "LayerName": str,
        "VersionNumber": int,
    },
)

DeleteProvisionedConcurrencyConfigRequestRequestTypeDef = TypedDict(
    "DeleteProvisionedConcurrencyConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Qualifier": str,
    },
)

DestinationConfigTypeDef = TypedDict(
    "DestinationConfigTypeDef",
    {
        "OnSuccess": NotRequired["OnSuccessTypeDef"],
        "OnFailure": NotRequired["OnFailureTypeDef"],
    },
)

EnvironmentErrorTypeDef = TypedDict(
    "EnvironmentErrorTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "Message": NotRequired[str],
    },
)

EnvironmentResponseTypeDef = TypedDict(
    "EnvironmentResponseTypeDef",
    {
        "Variables": NotRequired[Dict[str, str]],
        "Error": NotRequired["EnvironmentErrorTypeDef"],
    },
)

EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "Variables": NotRequired[Mapping[str, str]],
    },
)

EventSourceMappingConfigurationResponseMetadataTypeDef = TypedDict(
    "EventSourceMappingConfigurationResponseMetadataTypeDef",
    {
        "UUID": str,
        "StartingPosition": EventSourcePositionType,
        "StartingPositionTimestamp": datetime,
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "ParallelizationFactor": int,
        "EventSourceArn": str,
        "FilterCriteria": "FilterCriteriaTypeDef",
        "FunctionArn": str,
        "LastModified": datetime,
        "LastProcessingResult": str,
        "State": str,
        "StateTransitionReason": str,
        "DestinationConfig": "DestinationConfigTypeDef",
        "Topics": List[str],
        "Queues": List[str],
        "SourceAccessConfigurations": List["SourceAccessConfigurationTypeDef"],
        "SelfManagedEventSource": "SelfManagedEventSourceTypeDef",
        "MaximumRecordAgeInSeconds": int,
        "BisectBatchOnFunctionError": bool,
        "MaximumRetryAttempts": int,
        "TumblingWindowInSeconds": int,
        "FunctionResponseTypes": List[Literal["ReportBatchItemFailures"]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventSourceMappingConfigurationTypeDef = TypedDict(
    "EventSourceMappingConfigurationTypeDef",
    {
        "UUID": NotRequired[str],
        "StartingPosition": NotRequired[EventSourcePositionType],
        "StartingPositionTimestamp": NotRequired[datetime],
        "BatchSize": NotRequired[int],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
        "ParallelizationFactor": NotRequired[int],
        "EventSourceArn": NotRequired[str],
        "FilterCriteria": NotRequired["FilterCriteriaTypeDef"],
        "FunctionArn": NotRequired[str],
        "LastModified": NotRequired[datetime],
        "LastProcessingResult": NotRequired[str],
        "State": NotRequired[str],
        "StateTransitionReason": NotRequired[str],
        "DestinationConfig": NotRequired["DestinationConfigTypeDef"],
        "Topics": NotRequired[List[str]],
        "Queues": NotRequired[List[str]],
        "SourceAccessConfigurations": NotRequired[List["SourceAccessConfigurationTypeDef"]],
        "SelfManagedEventSource": NotRequired["SelfManagedEventSourceTypeDef"],
        "MaximumRecordAgeInSeconds": NotRequired[int],
        "BisectBatchOnFunctionError": NotRequired[bool],
        "MaximumRetryAttempts": NotRequired[int],
        "TumblingWindowInSeconds": NotRequired[int],
        "FunctionResponseTypes": NotRequired[List[Literal["ReportBatchItemFailures"]]],
    },
)

FileSystemConfigTypeDef = TypedDict(
    "FileSystemConfigTypeDef",
    {
        "Arn": str,
        "LocalMountPath": str,
    },
)

FilterCriteriaTypeDef = TypedDict(
    "FilterCriteriaTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Pattern": NotRequired[str],
    },
)

FunctionCodeLocationTypeDef = TypedDict(
    "FunctionCodeLocationTypeDef",
    {
        "RepositoryType": NotRequired[str],
        "Location": NotRequired[str],
        "ImageUri": NotRequired[str],
        "ResolvedImageUri": NotRequired[str],
    },
)

FunctionCodeTypeDef = TypedDict(
    "FunctionCodeTypeDef",
    {
        "ZipFile": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "S3Bucket": NotRequired[str],
        "S3Key": NotRequired[str],
        "S3ObjectVersion": NotRequired[str],
        "ImageUri": NotRequired[str],
    },
)

FunctionConfigurationResponseMetadataTypeDef = TypedDict(
    "FunctionConfigurationResponseMetadataTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": RuntimeType,
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": "VpcConfigResponseTypeDef",
        "DeadLetterConfig": "DeadLetterConfigTypeDef",
        "Environment": "EnvironmentResponseTypeDef",
        "KMSKeyArn": str,
        "TracingConfig": "TracingConfigResponseTypeDef",
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List["LayerTypeDef"],
        "State": StateType,
        "StateReason": str,
        "StateReasonCode": StateReasonCodeType,
        "LastUpdateStatus": LastUpdateStatusType,
        "LastUpdateStatusReason": str,
        "LastUpdateStatusReasonCode": LastUpdateStatusReasonCodeType,
        "FileSystemConfigs": List["FileSystemConfigTypeDef"],
        "PackageType": PackageTypeType,
        "ImageConfigResponse": "ImageConfigResponseTypeDef",
        "SigningProfileVersionArn": str,
        "SigningJobArn": str,
        "Architectures": List[ArchitectureType],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FunctionConfigurationTypeDef = TypedDict(
    "FunctionConfigurationTypeDef",
    {
        "FunctionName": NotRequired[str],
        "FunctionArn": NotRequired[str],
        "Runtime": NotRequired[RuntimeType],
        "Role": NotRequired[str],
        "Handler": NotRequired[str],
        "CodeSize": NotRequired[int],
        "Description": NotRequired[str],
        "Timeout": NotRequired[int],
        "MemorySize": NotRequired[int],
        "LastModified": NotRequired[str],
        "CodeSha256": NotRequired[str],
        "Version": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigResponseTypeDef"],
        "DeadLetterConfig": NotRequired["DeadLetterConfigTypeDef"],
        "Environment": NotRequired["EnvironmentResponseTypeDef"],
        "KMSKeyArn": NotRequired[str],
        "TracingConfig": NotRequired["TracingConfigResponseTypeDef"],
        "MasterArn": NotRequired[str],
        "RevisionId": NotRequired[str],
        "Layers": NotRequired[List["LayerTypeDef"]],
        "State": NotRequired[StateType],
        "StateReason": NotRequired[str],
        "StateReasonCode": NotRequired[StateReasonCodeType],
        "LastUpdateStatus": NotRequired[LastUpdateStatusType],
        "LastUpdateStatusReason": NotRequired[str],
        "LastUpdateStatusReasonCode": NotRequired[LastUpdateStatusReasonCodeType],
        "FileSystemConfigs": NotRequired[List["FileSystemConfigTypeDef"]],
        "PackageType": NotRequired[PackageTypeType],
        "ImageConfigResponse": NotRequired["ImageConfigResponseTypeDef"],
        "SigningProfileVersionArn": NotRequired[str],
        "SigningJobArn": NotRequired[str],
        "Architectures": NotRequired[List[ArchitectureType]],
    },
)

FunctionEventInvokeConfigResponseMetadataTypeDef = TypedDict(
    "FunctionEventInvokeConfigResponseMetadataTypeDef",
    {
        "LastModified": datetime,
        "FunctionArn": str,
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
        "DestinationConfig": "DestinationConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FunctionEventInvokeConfigTypeDef = TypedDict(
    "FunctionEventInvokeConfigTypeDef",
    {
        "LastModified": NotRequired[datetime],
        "FunctionArn": NotRequired[str],
        "MaximumRetryAttempts": NotRequired[int],
        "MaximumEventAgeInSeconds": NotRequired[int],
        "DestinationConfig": NotRequired["DestinationConfigTypeDef"],
    },
)

GetAccountSettingsResponseTypeDef = TypedDict(
    "GetAccountSettingsResponseTypeDef",
    {
        "AccountLimit": "AccountLimitTypeDef",
        "AccountUsage": "AccountUsageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAliasRequestRequestTypeDef = TypedDict(
    "GetAliasRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Name": str,
    },
)

GetCodeSigningConfigRequestRequestTypeDef = TypedDict(
    "GetCodeSigningConfigRequestRequestTypeDef",
    {
        "CodeSigningConfigArn": str,
    },
)

GetCodeSigningConfigResponseTypeDef = TypedDict(
    "GetCodeSigningConfigResponseTypeDef",
    {
        "CodeSigningConfig": "CodeSigningConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventSourceMappingRequestRequestTypeDef = TypedDict(
    "GetEventSourceMappingRequestRequestTypeDef",
    {
        "UUID": str,
    },
)

GetFunctionCodeSigningConfigRequestRequestTypeDef = TypedDict(
    "GetFunctionCodeSigningConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)

GetFunctionCodeSigningConfigResponseTypeDef = TypedDict(
    "GetFunctionCodeSigningConfigResponseTypeDef",
    {
        "CodeSigningConfigArn": str,
        "FunctionName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFunctionConcurrencyRequestRequestTypeDef = TypedDict(
    "GetFunctionConcurrencyRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)

GetFunctionConcurrencyResponseTypeDef = TypedDict(
    "GetFunctionConcurrencyResponseTypeDef",
    {
        "ReservedConcurrentExecutions": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFunctionConfigurationRequestRequestTypeDef = TypedDict(
    "GetFunctionConfigurationRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Qualifier": NotRequired[str],
    },
)

GetFunctionEventInvokeConfigRequestRequestTypeDef = TypedDict(
    "GetFunctionEventInvokeConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Qualifier": NotRequired[str],
    },
)

GetFunctionRequestRequestTypeDef = TypedDict(
    "GetFunctionRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Qualifier": NotRequired[str],
    },
)

GetFunctionResponseTypeDef = TypedDict(
    "GetFunctionResponseTypeDef",
    {
        "Configuration": "FunctionConfigurationTypeDef",
        "Code": "FunctionCodeLocationTypeDef",
        "Tags": Dict[str, str],
        "Concurrency": "ConcurrencyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLayerVersionByArnRequestRequestTypeDef = TypedDict(
    "GetLayerVersionByArnRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

GetLayerVersionPolicyRequestRequestTypeDef = TypedDict(
    "GetLayerVersionPolicyRequestRequestTypeDef",
    {
        "LayerName": str,
        "VersionNumber": int,
    },
)

GetLayerVersionPolicyResponseTypeDef = TypedDict(
    "GetLayerVersionPolicyResponseTypeDef",
    {
        "Policy": str,
        "RevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLayerVersionRequestRequestTypeDef = TypedDict(
    "GetLayerVersionRequestRequestTypeDef",
    {
        "LayerName": str,
        "VersionNumber": int,
    },
)

GetLayerVersionResponseTypeDef = TypedDict(
    "GetLayerVersionResponseTypeDef",
    {
        "Content": "LayerVersionContentOutputTypeDef",
        "LayerArn": str,
        "LayerVersionArn": str,
        "Description": str,
        "CreatedDate": str,
        "Version": int,
        "CompatibleRuntimes": List[RuntimeType],
        "LicenseInfo": str,
        "CompatibleArchitectures": List[ArchitectureType],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyRequestRequestTypeDef = TypedDict(
    "GetPolicyRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Qualifier": NotRequired[str],
    },
)

GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef",
    {
        "Policy": str,
        "RevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProvisionedConcurrencyConfigRequestRequestTypeDef = TypedDict(
    "GetProvisionedConcurrencyConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Qualifier": str,
    },
)

GetProvisionedConcurrencyConfigResponseTypeDef = TypedDict(
    "GetProvisionedConcurrencyConfigResponseTypeDef",
    {
        "RequestedProvisionedConcurrentExecutions": int,
        "AvailableProvisionedConcurrentExecutions": int,
        "AllocatedProvisionedConcurrentExecutions": int,
        "Status": ProvisionedConcurrencyStatusEnumType,
        "StatusReason": str,
        "LastModified": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImageConfigErrorTypeDef = TypedDict(
    "ImageConfigErrorTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "Message": NotRequired[str],
    },
)

ImageConfigResponseTypeDef = TypedDict(
    "ImageConfigResponseTypeDef",
    {
        "ImageConfig": NotRequired["ImageConfigTypeDef"],
        "Error": NotRequired["ImageConfigErrorTypeDef"],
    },
)

ImageConfigTypeDef = TypedDict(
    "ImageConfigTypeDef",
    {
        "EntryPoint": NotRequired[Sequence[str]],
        "Command": NotRequired[Sequence[str]],
        "WorkingDirectory": NotRequired[str],
    },
)

InvocationRequestRequestTypeDef = TypedDict(
    "InvocationRequestRequestTypeDef",
    {
        "FunctionName": str,
        "InvocationType": NotRequired[InvocationTypeType],
        "LogType": NotRequired[LogTypeType],
        "ClientContext": NotRequired[str],
        "Payload": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "Qualifier": NotRequired[str],
    },
)

InvocationResponseTypeDef = TypedDict(
    "InvocationResponseTypeDef",
    {
        "StatusCode": NotRequired[int],
        "FunctionError": NotRequired[str],
        "LogResult": NotRequired[str],
        "Payload": NotRequired[IO[bytes]],
        "ExecutedVersion": NotRequired[str],
    },
)

InvokeAsyncRequestRequestTypeDef = TypedDict(
    "InvokeAsyncRequestRequestTypeDef",
    {
        "FunctionName": str,
        "InvokeArgs": Union[bytes, IO[bytes], StreamingBody],
    },
)

InvokeAsyncResponseTypeDef = TypedDict(
    "InvokeAsyncResponseTypeDef",
    {
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LayerTypeDef = TypedDict(
    "LayerTypeDef",
    {
        "Arn": NotRequired[str],
        "CodeSize": NotRequired[int],
        "SigningProfileVersionArn": NotRequired[str],
        "SigningJobArn": NotRequired[str],
    },
)

LayerVersionContentInputTypeDef = TypedDict(
    "LayerVersionContentInputTypeDef",
    {
        "S3Bucket": NotRequired[str],
        "S3Key": NotRequired[str],
        "S3ObjectVersion": NotRequired[str],
        "ZipFile": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
    },
)

LayerVersionContentOutputTypeDef = TypedDict(
    "LayerVersionContentOutputTypeDef",
    {
        "Location": NotRequired[str],
        "CodeSha256": NotRequired[str],
        "CodeSize": NotRequired[int],
        "SigningProfileVersionArn": NotRequired[str],
        "SigningJobArn": NotRequired[str],
    },
)

LayerVersionsListItemTypeDef = TypedDict(
    "LayerVersionsListItemTypeDef",
    {
        "LayerVersionArn": NotRequired[str],
        "Version": NotRequired[int],
        "Description": NotRequired[str],
        "CreatedDate": NotRequired[str],
        "CompatibleRuntimes": NotRequired[List[RuntimeType]],
        "LicenseInfo": NotRequired[str],
        "CompatibleArchitectures": NotRequired[List[ArchitectureType]],
    },
)

LayersListItemTypeDef = TypedDict(
    "LayersListItemTypeDef",
    {
        "LayerName": NotRequired[str],
        "LayerArn": NotRequired[str],
        "LatestMatchingVersion": NotRequired["LayerVersionsListItemTypeDef"],
    },
)

ListAliasesRequestRequestTypeDef = TypedDict(
    "ListAliasesRequestRequestTypeDef",
    {
        "FunctionName": str,
        "FunctionVersion": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListAliasesResponseTypeDef = TypedDict(
    "ListAliasesResponseTypeDef",
    {
        "NextMarker": str,
        "Aliases": List["AliasConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCodeSigningConfigsRequestRequestTypeDef = TypedDict(
    "ListCodeSigningConfigsRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListCodeSigningConfigsResponseTypeDef = TypedDict(
    "ListCodeSigningConfigsResponseTypeDef",
    {
        "NextMarker": str,
        "CodeSigningConfigs": List["CodeSigningConfigTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventSourceMappingsRequestRequestTypeDef = TypedDict(
    "ListEventSourceMappingsRequestRequestTypeDef",
    {
        "EventSourceArn": NotRequired[str],
        "FunctionName": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListEventSourceMappingsResponseTypeDef = TypedDict(
    "ListEventSourceMappingsResponseTypeDef",
    {
        "NextMarker": str,
        "EventSourceMappings": List["EventSourceMappingConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFunctionEventInvokeConfigsRequestRequestTypeDef = TypedDict(
    "ListFunctionEventInvokeConfigsRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListFunctionEventInvokeConfigsResponseTypeDef = TypedDict(
    "ListFunctionEventInvokeConfigsResponseTypeDef",
    {
        "FunctionEventInvokeConfigs": List["FunctionEventInvokeConfigTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFunctionsByCodeSigningConfigRequestRequestTypeDef = TypedDict(
    "ListFunctionsByCodeSigningConfigRequestRequestTypeDef",
    {
        "CodeSigningConfigArn": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListFunctionsByCodeSigningConfigResponseTypeDef = TypedDict(
    "ListFunctionsByCodeSigningConfigResponseTypeDef",
    {
        "NextMarker": str,
        "FunctionArns": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFunctionsRequestRequestTypeDef = TypedDict(
    "ListFunctionsRequestRequestTypeDef",
    {
        "MasterRegion": NotRequired[str],
        "FunctionVersion": NotRequired[Literal["ALL"]],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListFunctionsResponseTypeDef = TypedDict(
    "ListFunctionsResponseTypeDef",
    {
        "NextMarker": str,
        "Functions": List["FunctionConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLayerVersionsRequestRequestTypeDef = TypedDict(
    "ListLayerVersionsRequestRequestTypeDef",
    {
        "LayerName": str,
        "CompatibleRuntime": NotRequired[RuntimeType],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
        "CompatibleArchitecture": NotRequired[ArchitectureType],
    },
)

ListLayerVersionsResponseTypeDef = TypedDict(
    "ListLayerVersionsResponseTypeDef",
    {
        "NextMarker": str,
        "LayerVersions": List["LayerVersionsListItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLayersRequestRequestTypeDef = TypedDict(
    "ListLayersRequestRequestTypeDef",
    {
        "CompatibleRuntime": NotRequired[RuntimeType],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
        "CompatibleArchitecture": NotRequired[ArchitectureType],
    },
)

ListLayersResponseTypeDef = TypedDict(
    "ListLayersResponseTypeDef",
    {
        "NextMarker": str,
        "Layers": List["LayersListItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProvisionedConcurrencyConfigsRequestRequestTypeDef = TypedDict(
    "ListProvisionedConcurrencyConfigsRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListProvisionedConcurrencyConfigsResponseTypeDef = TypedDict(
    "ListProvisionedConcurrencyConfigsResponseTypeDef",
    {
        "ProvisionedConcurrencyConfigs": List["ProvisionedConcurrencyConfigListItemTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "Resource": str,
    },
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVersionsByFunctionRequestRequestTypeDef = TypedDict(
    "ListVersionsByFunctionRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListVersionsByFunctionResponseTypeDef = TypedDict(
    "ListVersionsByFunctionResponseTypeDef",
    {
        "NextMarker": str,
        "Versions": List["FunctionConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OnFailureTypeDef = TypedDict(
    "OnFailureTypeDef",
    {
        "Destination": NotRequired[str],
    },
)

OnSuccessTypeDef = TypedDict(
    "OnSuccessTypeDef",
    {
        "Destination": NotRequired[str],
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

ProvisionedConcurrencyConfigListItemTypeDef = TypedDict(
    "ProvisionedConcurrencyConfigListItemTypeDef",
    {
        "FunctionArn": NotRequired[str],
        "RequestedProvisionedConcurrentExecutions": NotRequired[int],
        "AvailableProvisionedConcurrentExecutions": NotRequired[int],
        "AllocatedProvisionedConcurrentExecutions": NotRequired[int],
        "Status": NotRequired[ProvisionedConcurrencyStatusEnumType],
        "StatusReason": NotRequired[str],
        "LastModified": NotRequired[str],
    },
)

PublishLayerVersionRequestRequestTypeDef = TypedDict(
    "PublishLayerVersionRequestRequestTypeDef",
    {
        "LayerName": str,
        "Content": "LayerVersionContentInputTypeDef",
        "Description": NotRequired[str],
        "CompatibleRuntimes": NotRequired[Sequence[RuntimeType]],
        "LicenseInfo": NotRequired[str],
        "CompatibleArchitectures": NotRequired[Sequence[ArchitectureType]],
    },
)

PublishLayerVersionResponseTypeDef = TypedDict(
    "PublishLayerVersionResponseTypeDef",
    {
        "Content": "LayerVersionContentOutputTypeDef",
        "LayerArn": str,
        "LayerVersionArn": str,
        "Description": str,
        "CreatedDate": str,
        "Version": int,
        "CompatibleRuntimes": List[RuntimeType],
        "LicenseInfo": str,
        "CompatibleArchitectures": List[ArchitectureType],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PublishVersionRequestRequestTypeDef = TypedDict(
    "PublishVersionRequestRequestTypeDef",
    {
        "FunctionName": str,
        "CodeSha256": NotRequired[str],
        "Description": NotRequired[str],
        "RevisionId": NotRequired[str],
    },
)

PutFunctionCodeSigningConfigRequestRequestTypeDef = TypedDict(
    "PutFunctionCodeSigningConfigRequestRequestTypeDef",
    {
        "CodeSigningConfigArn": str,
        "FunctionName": str,
    },
)

PutFunctionCodeSigningConfigResponseTypeDef = TypedDict(
    "PutFunctionCodeSigningConfigResponseTypeDef",
    {
        "CodeSigningConfigArn": str,
        "FunctionName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutFunctionConcurrencyRequestRequestTypeDef = TypedDict(
    "PutFunctionConcurrencyRequestRequestTypeDef",
    {
        "FunctionName": str,
        "ReservedConcurrentExecutions": int,
    },
)

PutFunctionEventInvokeConfigRequestRequestTypeDef = TypedDict(
    "PutFunctionEventInvokeConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Qualifier": NotRequired[str],
        "MaximumRetryAttempts": NotRequired[int],
        "MaximumEventAgeInSeconds": NotRequired[int],
        "DestinationConfig": NotRequired["DestinationConfigTypeDef"],
    },
)

PutProvisionedConcurrencyConfigRequestRequestTypeDef = TypedDict(
    "PutProvisionedConcurrencyConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Qualifier": str,
        "ProvisionedConcurrentExecutions": int,
    },
)

PutProvisionedConcurrencyConfigResponseTypeDef = TypedDict(
    "PutProvisionedConcurrencyConfigResponseTypeDef",
    {
        "RequestedProvisionedConcurrentExecutions": int,
        "AvailableProvisionedConcurrentExecutions": int,
        "AllocatedProvisionedConcurrentExecutions": int,
        "Status": ProvisionedConcurrencyStatusEnumType,
        "StatusReason": str,
        "LastModified": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveLayerVersionPermissionRequestRequestTypeDef = TypedDict(
    "RemoveLayerVersionPermissionRequestRequestTypeDef",
    {
        "LayerName": str,
        "VersionNumber": int,
        "StatementId": str,
        "RevisionId": NotRequired[str],
    },
)

RemovePermissionRequestRequestTypeDef = TypedDict(
    "RemovePermissionRequestRequestTypeDef",
    {
        "FunctionName": str,
        "StatementId": str,
        "Qualifier": NotRequired[str],
        "RevisionId": NotRequired[str],
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

SelfManagedEventSourceTypeDef = TypedDict(
    "SelfManagedEventSourceTypeDef",
    {
        "Endpoints": NotRequired[Mapping[Literal["KAFKA_BOOTSTRAP_SERVERS"], Sequence[str]]],
    },
)

SourceAccessConfigurationTypeDef = TypedDict(
    "SourceAccessConfigurationTypeDef",
    {
        "Type": NotRequired[SourceAccessTypeType],
        "URI": NotRequired[str],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "Resource": str,
        "Tags": Mapping[str, str],
    },
)

TracingConfigResponseTypeDef = TypedDict(
    "TracingConfigResponseTypeDef",
    {
        "Mode": NotRequired[TracingModeType],
    },
)

TracingConfigTypeDef = TypedDict(
    "TracingConfigTypeDef",
    {
        "Mode": NotRequired[TracingModeType],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "Resource": str,
        "TagKeys": Sequence[str],
    },
)

UpdateAliasRequestRequestTypeDef = TypedDict(
    "UpdateAliasRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Name": str,
        "FunctionVersion": NotRequired[str],
        "Description": NotRequired[str],
        "RoutingConfig": NotRequired["AliasRoutingConfigurationTypeDef"],
        "RevisionId": NotRequired[str],
    },
)

UpdateCodeSigningConfigRequestRequestTypeDef = TypedDict(
    "UpdateCodeSigningConfigRequestRequestTypeDef",
    {
        "CodeSigningConfigArn": str,
        "Description": NotRequired[str],
        "AllowedPublishers": NotRequired["AllowedPublishersTypeDef"],
        "CodeSigningPolicies": NotRequired["CodeSigningPoliciesTypeDef"],
    },
)

UpdateCodeSigningConfigResponseTypeDef = TypedDict(
    "UpdateCodeSigningConfigResponseTypeDef",
    {
        "CodeSigningConfig": "CodeSigningConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEventSourceMappingRequestRequestTypeDef = TypedDict(
    "UpdateEventSourceMappingRequestRequestTypeDef",
    {
        "UUID": str,
        "FunctionName": NotRequired[str],
        "Enabled": NotRequired[bool],
        "BatchSize": NotRequired[int],
        "FilterCriteria": NotRequired["FilterCriteriaTypeDef"],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
        "DestinationConfig": NotRequired["DestinationConfigTypeDef"],
        "MaximumRecordAgeInSeconds": NotRequired[int],
        "BisectBatchOnFunctionError": NotRequired[bool],
        "MaximumRetryAttempts": NotRequired[int],
        "ParallelizationFactor": NotRequired[int],
        "SourceAccessConfigurations": NotRequired[Sequence["SourceAccessConfigurationTypeDef"]],
        "TumblingWindowInSeconds": NotRequired[int],
        "FunctionResponseTypes": NotRequired[Sequence[Literal["ReportBatchItemFailures"]]],
    },
)

UpdateFunctionCodeRequestRequestTypeDef = TypedDict(
    "UpdateFunctionCodeRequestRequestTypeDef",
    {
        "FunctionName": str,
        "ZipFile": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "S3Bucket": NotRequired[str],
        "S3Key": NotRequired[str],
        "S3ObjectVersion": NotRequired[str],
        "ImageUri": NotRequired[str],
        "Publish": NotRequired[bool],
        "DryRun": NotRequired[bool],
        "RevisionId": NotRequired[str],
        "Architectures": NotRequired[Sequence[ArchitectureType]],
    },
)

UpdateFunctionConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateFunctionConfigurationRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Role": NotRequired[str],
        "Handler": NotRequired[str],
        "Description": NotRequired[str],
        "Timeout": NotRequired[int],
        "MemorySize": NotRequired[int],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "Environment": NotRequired["EnvironmentTypeDef"],
        "Runtime": NotRequired[RuntimeType],
        "DeadLetterConfig": NotRequired["DeadLetterConfigTypeDef"],
        "KMSKeyArn": NotRequired[str],
        "TracingConfig": NotRequired["TracingConfigTypeDef"],
        "RevisionId": NotRequired[str],
        "Layers": NotRequired[Sequence[str]],
        "FileSystemConfigs": NotRequired[Sequence["FileSystemConfigTypeDef"]],
        "ImageConfig": NotRequired["ImageConfigTypeDef"],
    },
)

UpdateFunctionEventInvokeConfigRequestRequestTypeDef = TypedDict(
    "UpdateFunctionEventInvokeConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Qualifier": NotRequired[str],
        "MaximumRetryAttempts": NotRequired[int],
        "MaximumEventAgeInSeconds": NotRequired[int],
        "DestinationConfig": NotRequired["DestinationConfigTypeDef"],
    },
)

VpcConfigResponseTypeDef = TypedDict(
    "VpcConfigResponseTypeDef",
    {
        "SubnetIds": NotRequired[List[str]],
        "SecurityGroupIds": NotRequired[List[str]],
        "VpcId": NotRequired[str],
    },
)

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "SubnetIds": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
