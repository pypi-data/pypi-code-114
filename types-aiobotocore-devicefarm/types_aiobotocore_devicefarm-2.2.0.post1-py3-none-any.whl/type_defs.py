"""
Type annotations for devicefarm service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_devicefarm/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_devicefarm.type_defs import AccountSettingsTypeDef

    data: AccountSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    ArtifactCategoryType,
    ArtifactTypeType,
    BillingMethodType,
    DeviceAttributeType,
    DeviceAvailabilityType,
    DeviceFilterAttributeType,
    DeviceFormFactorType,
    DevicePlatformType,
    DevicePoolTypeType,
    ExecutionResultCodeType,
    ExecutionResultType,
    ExecutionStatusType,
    InstanceStatusType,
    InteractionModeType,
    NetworkProfileTypeType,
    OfferingTransactionTypeType,
    RuleOperatorType,
    SampleTypeType,
    TestGridSessionArtifactCategoryType,
    TestGridSessionArtifactTypeType,
    TestGridSessionStatusType,
    TestTypeType,
    UploadCategoryType,
    UploadStatusType,
    UploadTypeType,
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
    "AccountSettingsTypeDef",
    "ArtifactTypeDef",
    "CPUTypeDef",
    "CountersTypeDef",
    "CreateDevicePoolRequestRequestTypeDef",
    "CreateDevicePoolResultTypeDef",
    "CreateInstanceProfileRequestRequestTypeDef",
    "CreateInstanceProfileResultTypeDef",
    "CreateNetworkProfileRequestRequestTypeDef",
    "CreateNetworkProfileResultTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "CreateProjectResultTypeDef",
    "CreateRemoteAccessSessionConfigurationTypeDef",
    "CreateRemoteAccessSessionRequestRequestTypeDef",
    "CreateRemoteAccessSessionResultTypeDef",
    "CreateTestGridProjectRequestRequestTypeDef",
    "CreateTestGridProjectResultTypeDef",
    "CreateTestGridUrlRequestRequestTypeDef",
    "CreateTestGridUrlResultTypeDef",
    "CreateUploadRequestRequestTypeDef",
    "CreateUploadResultTypeDef",
    "CreateVPCEConfigurationRequestRequestTypeDef",
    "CreateVPCEConfigurationResultTypeDef",
    "CustomerArtifactPathsTypeDef",
    "DeleteDevicePoolRequestRequestTypeDef",
    "DeleteInstanceProfileRequestRequestTypeDef",
    "DeleteNetworkProfileRequestRequestTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteRemoteAccessSessionRequestRequestTypeDef",
    "DeleteRunRequestRequestTypeDef",
    "DeleteTestGridProjectRequestRequestTypeDef",
    "DeleteUploadRequestRequestTypeDef",
    "DeleteVPCEConfigurationRequestRequestTypeDef",
    "DeviceFilterTypeDef",
    "DeviceInstanceTypeDef",
    "DeviceMinutesTypeDef",
    "DevicePoolCompatibilityResultTypeDef",
    "DevicePoolTypeDef",
    "DeviceSelectionConfigurationTypeDef",
    "DeviceSelectionResultTypeDef",
    "DeviceTypeDef",
    "ExecutionConfigurationTypeDef",
    "GetAccountSettingsResultTypeDef",
    "GetDeviceInstanceRequestRequestTypeDef",
    "GetDeviceInstanceResultTypeDef",
    "GetDevicePoolCompatibilityRequestRequestTypeDef",
    "GetDevicePoolCompatibilityResultTypeDef",
    "GetDevicePoolRequestRequestTypeDef",
    "GetDevicePoolResultTypeDef",
    "GetDeviceRequestRequestTypeDef",
    "GetDeviceResultTypeDef",
    "GetInstanceProfileRequestRequestTypeDef",
    "GetInstanceProfileResultTypeDef",
    "GetJobRequestRequestTypeDef",
    "GetJobResultTypeDef",
    "GetNetworkProfileRequestRequestTypeDef",
    "GetNetworkProfileResultTypeDef",
    "GetOfferingStatusRequestRequestTypeDef",
    "GetOfferingStatusResultTypeDef",
    "GetProjectRequestRequestTypeDef",
    "GetProjectResultTypeDef",
    "GetRemoteAccessSessionRequestRequestTypeDef",
    "GetRemoteAccessSessionResultTypeDef",
    "GetRunRequestRequestTypeDef",
    "GetRunResultTypeDef",
    "GetSuiteRequestRequestTypeDef",
    "GetSuiteResultTypeDef",
    "GetTestGridProjectRequestRequestTypeDef",
    "GetTestGridProjectResultTypeDef",
    "GetTestGridSessionRequestRequestTypeDef",
    "GetTestGridSessionResultTypeDef",
    "GetTestRequestRequestTypeDef",
    "GetTestResultTypeDef",
    "GetUploadRequestRequestTypeDef",
    "GetUploadResultTypeDef",
    "GetVPCEConfigurationRequestRequestTypeDef",
    "GetVPCEConfigurationResultTypeDef",
    "IncompatibilityMessageTypeDef",
    "InstallToRemoteAccessSessionRequestRequestTypeDef",
    "InstallToRemoteAccessSessionResultTypeDef",
    "InstanceProfileTypeDef",
    "JobTypeDef",
    "ListArtifactsRequestRequestTypeDef",
    "ListArtifactsResultTypeDef",
    "ListDeviceInstancesRequestRequestTypeDef",
    "ListDeviceInstancesResultTypeDef",
    "ListDevicePoolsRequestRequestTypeDef",
    "ListDevicePoolsResultTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "ListDevicesResultTypeDef",
    "ListInstanceProfilesRequestRequestTypeDef",
    "ListInstanceProfilesResultTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListJobsResultTypeDef",
    "ListNetworkProfilesRequestRequestTypeDef",
    "ListNetworkProfilesResultTypeDef",
    "ListOfferingPromotionsRequestRequestTypeDef",
    "ListOfferingPromotionsResultTypeDef",
    "ListOfferingTransactionsRequestRequestTypeDef",
    "ListOfferingTransactionsResultTypeDef",
    "ListOfferingsRequestRequestTypeDef",
    "ListOfferingsResultTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListProjectsResultTypeDef",
    "ListRemoteAccessSessionsRequestRequestTypeDef",
    "ListRemoteAccessSessionsResultTypeDef",
    "ListRunsRequestRequestTypeDef",
    "ListRunsResultTypeDef",
    "ListSamplesRequestRequestTypeDef",
    "ListSamplesResultTypeDef",
    "ListSuitesRequestRequestTypeDef",
    "ListSuitesResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTestGridProjectsRequestRequestTypeDef",
    "ListTestGridProjectsResultTypeDef",
    "ListTestGridSessionActionsRequestRequestTypeDef",
    "ListTestGridSessionActionsResultTypeDef",
    "ListTestGridSessionArtifactsRequestRequestTypeDef",
    "ListTestGridSessionArtifactsResultTypeDef",
    "ListTestGridSessionsRequestRequestTypeDef",
    "ListTestGridSessionsResultTypeDef",
    "ListTestsRequestRequestTypeDef",
    "ListTestsResultTypeDef",
    "ListUniqueProblemsRequestRequestTypeDef",
    "ListUniqueProblemsResultTypeDef",
    "ListUploadsRequestRequestTypeDef",
    "ListUploadsResultTypeDef",
    "ListVPCEConfigurationsRequestRequestTypeDef",
    "ListVPCEConfigurationsResultTypeDef",
    "LocationTypeDef",
    "MonetaryAmountTypeDef",
    "NetworkProfileTypeDef",
    "OfferingPromotionTypeDef",
    "OfferingStatusTypeDef",
    "OfferingTransactionTypeDef",
    "OfferingTypeDef",
    "PaginatorConfigTypeDef",
    "ProblemDetailTypeDef",
    "ProblemTypeDef",
    "ProjectTypeDef",
    "PurchaseOfferingRequestRequestTypeDef",
    "PurchaseOfferingResultTypeDef",
    "RadiosTypeDef",
    "RecurringChargeTypeDef",
    "RemoteAccessSessionTypeDef",
    "RenewOfferingRequestRequestTypeDef",
    "RenewOfferingResultTypeDef",
    "ResolutionTypeDef",
    "ResponseMetadataTypeDef",
    "RuleTypeDef",
    "RunTypeDef",
    "SampleTypeDef",
    "ScheduleRunConfigurationTypeDef",
    "ScheduleRunRequestRequestTypeDef",
    "ScheduleRunResultTypeDef",
    "ScheduleRunTestTypeDef",
    "StopJobRequestRequestTypeDef",
    "StopJobResultTypeDef",
    "StopRemoteAccessSessionRequestRequestTypeDef",
    "StopRemoteAccessSessionResultTypeDef",
    "StopRunRequestRequestTypeDef",
    "StopRunResultTypeDef",
    "SuiteTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TestGridProjectTypeDef",
    "TestGridSessionActionTypeDef",
    "TestGridSessionArtifactTypeDef",
    "TestGridSessionTypeDef",
    "TestGridVpcConfigTypeDef",
    "TestTypeDef",
    "TrialMinutesTypeDef",
    "UniqueProblemTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDeviceInstanceRequestRequestTypeDef",
    "UpdateDeviceInstanceResultTypeDef",
    "UpdateDevicePoolRequestRequestTypeDef",
    "UpdateDevicePoolResultTypeDef",
    "UpdateInstanceProfileRequestRequestTypeDef",
    "UpdateInstanceProfileResultTypeDef",
    "UpdateNetworkProfileRequestRequestTypeDef",
    "UpdateNetworkProfileResultTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "UpdateProjectResultTypeDef",
    "UpdateTestGridProjectRequestRequestTypeDef",
    "UpdateTestGridProjectResultTypeDef",
    "UpdateUploadRequestRequestTypeDef",
    "UpdateUploadResultTypeDef",
    "UpdateVPCEConfigurationRequestRequestTypeDef",
    "UpdateVPCEConfigurationResultTypeDef",
    "UploadTypeDef",
    "VPCEConfigurationTypeDef",
)

AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "awsAccountNumber": NotRequired[str],
        "unmeteredDevices": NotRequired[Dict[DevicePlatformType, int]],
        "unmeteredRemoteAccessDevices": NotRequired[Dict[DevicePlatformType, int]],
        "maxJobTimeoutMinutes": NotRequired[int],
        "trialMinutes": NotRequired["TrialMinutesTypeDef"],
        "maxSlots": NotRequired[Dict[str, int]],
        "defaultJobTimeoutMinutes": NotRequired[int],
        "skipAppResign": NotRequired[bool],
    },
)

ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[ArtifactTypeType],
        "extension": NotRequired[str],
        "url": NotRequired[str],
    },
)

CPUTypeDef = TypedDict(
    "CPUTypeDef",
    {
        "frequency": NotRequired[str],
        "architecture": NotRequired[str],
        "clock": NotRequired[float],
    },
)

CountersTypeDef = TypedDict(
    "CountersTypeDef",
    {
        "total": NotRequired[int],
        "passed": NotRequired[int],
        "failed": NotRequired[int],
        "warned": NotRequired[int],
        "errored": NotRequired[int],
        "stopped": NotRequired[int],
        "skipped": NotRequired[int],
    },
)

CreateDevicePoolRequestRequestTypeDef = TypedDict(
    "CreateDevicePoolRequestRequestTypeDef",
    {
        "projectArn": str,
        "name": str,
        "rules": Sequence["RuleTypeDef"],
        "description": NotRequired[str],
        "maxDevices": NotRequired[int],
    },
)

CreateDevicePoolResultTypeDef = TypedDict(
    "CreateDevicePoolResultTypeDef",
    {
        "devicePool": "DevicePoolTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInstanceProfileRequestRequestTypeDef = TypedDict(
    "CreateInstanceProfileRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "packageCleanup": NotRequired[bool],
        "excludeAppPackagesFromCleanup": NotRequired[Sequence[str]],
        "rebootAfterUse": NotRequired[bool],
    },
)

CreateInstanceProfileResultTypeDef = TypedDict(
    "CreateInstanceProfileResultTypeDef",
    {
        "instanceProfile": "InstanceProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateNetworkProfileRequestRequestTypeDef = TypedDict(
    "CreateNetworkProfileRequestRequestTypeDef",
    {
        "projectArn": str,
        "name": str,
        "description": NotRequired[str],
        "type": NotRequired[NetworkProfileTypeType],
        "uplinkBandwidthBits": NotRequired[int],
        "downlinkBandwidthBits": NotRequired[int],
        "uplinkDelayMs": NotRequired[int],
        "downlinkDelayMs": NotRequired[int],
        "uplinkJitterMs": NotRequired[int],
        "downlinkJitterMs": NotRequired[int],
        "uplinkLossPercent": NotRequired[int],
        "downlinkLossPercent": NotRequired[int],
    },
)

CreateNetworkProfileResultTypeDef = TypedDict(
    "CreateNetworkProfileResultTypeDef",
    {
        "networkProfile": "NetworkProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProjectRequestRequestTypeDef = TypedDict(
    "CreateProjectRequestRequestTypeDef",
    {
        "name": str,
        "defaultJobTimeoutMinutes": NotRequired[int],
    },
)

CreateProjectResultTypeDef = TypedDict(
    "CreateProjectResultTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRemoteAccessSessionConfigurationTypeDef = TypedDict(
    "CreateRemoteAccessSessionConfigurationTypeDef",
    {
        "billingMethod": NotRequired[BillingMethodType],
        "vpceConfigurationArns": NotRequired[Sequence[str]],
    },
)

CreateRemoteAccessSessionRequestRequestTypeDef = TypedDict(
    "CreateRemoteAccessSessionRequestRequestTypeDef",
    {
        "projectArn": str,
        "deviceArn": str,
        "instanceArn": NotRequired[str],
        "sshPublicKey": NotRequired[str],
        "remoteDebugEnabled": NotRequired[bool],
        "remoteRecordEnabled": NotRequired[bool],
        "remoteRecordAppArn": NotRequired[str],
        "name": NotRequired[str],
        "clientId": NotRequired[str],
        "configuration": NotRequired["CreateRemoteAccessSessionConfigurationTypeDef"],
        "interactionMode": NotRequired[InteractionModeType],
        "skipAppResign": NotRequired[bool],
    },
)

CreateRemoteAccessSessionResultTypeDef = TypedDict(
    "CreateRemoteAccessSessionResultTypeDef",
    {
        "remoteAccessSession": "RemoteAccessSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTestGridProjectRequestRequestTypeDef = TypedDict(
    "CreateTestGridProjectRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "vpcConfig": NotRequired["TestGridVpcConfigTypeDef"],
    },
)

CreateTestGridProjectResultTypeDef = TypedDict(
    "CreateTestGridProjectResultTypeDef",
    {
        "testGridProject": "TestGridProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTestGridUrlRequestRequestTypeDef = TypedDict(
    "CreateTestGridUrlRequestRequestTypeDef",
    {
        "projectArn": str,
        "expiresInSeconds": int,
    },
)

CreateTestGridUrlResultTypeDef = TypedDict(
    "CreateTestGridUrlResultTypeDef",
    {
        "url": str,
        "expires": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUploadRequestRequestTypeDef = TypedDict(
    "CreateUploadRequestRequestTypeDef",
    {
        "projectArn": str,
        "name": str,
        "type": UploadTypeType,
        "contentType": NotRequired[str],
    },
)

CreateUploadResultTypeDef = TypedDict(
    "CreateUploadResultTypeDef",
    {
        "upload": "UploadTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVPCEConfigurationRequestRequestTypeDef = TypedDict(
    "CreateVPCEConfigurationRequestRequestTypeDef",
    {
        "vpceConfigurationName": str,
        "vpceServiceName": str,
        "serviceDnsName": str,
        "vpceConfigurationDescription": NotRequired[str],
    },
)

CreateVPCEConfigurationResultTypeDef = TypedDict(
    "CreateVPCEConfigurationResultTypeDef",
    {
        "vpceConfiguration": "VPCEConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomerArtifactPathsTypeDef = TypedDict(
    "CustomerArtifactPathsTypeDef",
    {
        "iosPaths": NotRequired[Sequence[str]],
        "androidPaths": NotRequired[Sequence[str]],
        "deviceHostPaths": NotRequired[Sequence[str]],
    },
)

DeleteDevicePoolRequestRequestTypeDef = TypedDict(
    "DeleteDevicePoolRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteInstanceProfileRequestRequestTypeDef = TypedDict(
    "DeleteInstanceProfileRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteNetworkProfileRequestRequestTypeDef = TypedDict(
    "DeleteNetworkProfileRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteRemoteAccessSessionRequestRequestTypeDef = TypedDict(
    "DeleteRemoteAccessSessionRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteRunRequestRequestTypeDef = TypedDict(
    "DeleteRunRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteTestGridProjectRequestRequestTypeDef = TypedDict(
    "DeleteTestGridProjectRequestRequestTypeDef",
    {
        "projectArn": str,
    },
)

DeleteUploadRequestRequestTypeDef = TypedDict(
    "DeleteUploadRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteVPCEConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteVPCEConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeviceFilterTypeDef = TypedDict(
    "DeviceFilterTypeDef",
    {
        "attribute": DeviceFilterAttributeType,
        "operator": RuleOperatorType,
        "values": List[str],
    },
)

DeviceInstanceTypeDef = TypedDict(
    "DeviceInstanceTypeDef",
    {
        "arn": NotRequired[str],
        "deviceArn": NotRequired[str],
        "labels": NotRequired[List[str]],
        "status": NotRequired[InstanceStatusType],
        "udid": NotRequired[str],
        "instanceProfile": NotRequired["InstanceProfileTypeDef"],
    },
)

DeviceMinutesTypeDef = TypedDict(
    "DeviceMinutesTypeDef",
    {
        "total": NotRequired[float],
        "metered": NotRequired[float],
        "unmetered": NotRequired[float],
    },
)

DevicePoolCompatibilityResultTypeDef = TypedDict(
    "DevicePoolCompatibilityResultTypeDef",
    {
        "device": NotRequired["DeviceTypeDef"],
        "compatible": NotRequired[bool],
        "incompatibilityMessages": NotRequired[List["IncompatibilityMessageTypeDef"]],
    },
)

DevicePoolTypeDef = TypedDict(
    "DevicePoolTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "type": NotRequired[DevicePoolTypeType],
        "rules": NotRequired[List["RuleTypeDef"]],
        "maxDevices": NotRequired[int],
    },
)

DeviceSelectionConfigurationTypeDef = TypedDict(
    "DeviceSelectionConfigurationTypeDef",
    {
        "filters": Sequence["DeviceFilterTypeDef"],
        "maxDevices": int,
    },
)

DeviceSelectionResultTypeDef = TypedDict(
    "DeviceSelectionResultTypeDef",
    {
        "filters": NotRequired[List["DeviceFilterTypeDef"]],
        "matchedDevicesCount": NotRequired[int],
        "maxDevices": NotRequired[int],
    },
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "manufacturer": NotRequired[str],
        "model": NotRequired[str],
        "modelId": NotRequired[str],
        "formFactor": NotRequired[DeviceFormFactorType],
        "platform": NotRequired[DevicePlatformType],
        "os": NotRequired[str],
        "cpu": NotRequired["CPUTypeDef"],
        "resolution": NotRequired["ResolutionTypeDef"],
        "heapSize": NotRequired[int],
        "memory": NotRequired[int],
        "image": NotRequired[str],
        "carrier": NotRequired[str],
        "radio": NotRequired[str],
        "remoteAccessEnabled": NotRequired[bool],
        "remoteDebugEnabled": NotRequired[bool],
        "fleetType": NotRequired[str],
        "fleetName": NotRequired[str],
        "instances": NotRequired[List["DeviceInstanceTypeDef"]],
        "availability": NotRequired[DeviceAvailabilityType],
    },
)

ExecutionConfigurationTypeDef = TypedDict(
    "ExecutionConfigurationTypeDef",
    {
        "jobTimeoutMinutes": NotRequired[int],
        "accountsCleanup": NotRequired[bool],
        "appPackagesCleanup": NotRequired[bool],
        "videoCapture": NotRequired[bool],
        "skipAppResign": NotRequired[bool],
    },
)

GetAccountSettingsResultTypeDef = TypedDict(
    "GetAccountSettingsResultTypeDef",
    {
        "accountSettings": "AccountSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeviceInstanceRequestRequestTypeDef = TypedDict(
    "GetDeviceInstanceRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetDeviceInstanceResultTypeDef = TypedDict(
    "GetDeviceInstanceResultTypeDef",
    {
        "deviceInstance": "DeviceInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDevicePoolCompatibilityRequestRequestTypeDef = TypedDict(
    "GetDevicePoolCompatibilityRequestRequestTypeDef",
    {
        "devicePoolArn": str,
        "appArn": NotRequired[str],
        "testType": NotRequired[TestTypeType],
        "test": NotRequired["ScheduleRunTestTypeDef"],
        "configuration": NotRequired["ScheduleRunConfigurationTypeDef"],
    },
)

GetDevicePoolCompatibilityResultTypeDef = TypedDict(
    "GetDevicePoolCompatibilityResultTypeDef",
    {
        "compatibleDevices": List["DevicePoolCompatibilityResultTypeDef"],
        "incompatibleDevices": List["DevicePoolCompatibilityResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDevicePoolRequestRequestTypeDef = TypedDict(
    "GetDevicePoolRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetDevicePoolResultTypeDef = TypedDict(
    "GetDevicePoolResultTypeDef",
    {
        "devicePool": "DevicePoolTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeviceRequestRequestTypeDef = TypedDict(
    "GetDeviceRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetDeviceResultTypeDef = TypedDict(
    "GetDeviceResultTypeDef",
    {
        "device": "DeviceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceProfileRequestRequestTypeDef = TypedDict(
    "GetInstanceProfileRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetInstanceProfileResultTypeDef = TypedDict(
    "GetInstanceProfileResultTypeDef",
    {
        "instanceProfile": "InstanceProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobRequestRequestTypeDef = TypedDict(
    "GetJobRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetJobResultTypeDef = TypedDict(
    "GetJobResultTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkProfileRequestRequestTypeDef = TypedDict(
    "GetNetworkProfileRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetNetworkProfileResultTypeDef = TypedDict(
    "GetNetworkProfileResultTypeDef",
    {
        "networkProfile": "NetworkProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOfferingStatusRequestRequestTypeDef = TypedDict(
    "GetOfferingStatusRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)

GetOfferingStatusResultTypeDef = TypedDict(
    "GetOfferingStatusResultTypeDef",
    {
        "current": Dict[str, "OfferingStatusTypeDef"],
        "nextPeriod": Dict[str, "OfferingStatusTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProjectRequestRequestTypeDef = TypedDict(
    "GetProjectRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetProjectResultTypeDef = TypedDict(
    "GetProjectResultTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRemoteAccessSessionRequestRequestTypeDef = TypedDict(
    "GetRemoteAccessSessionRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetRemoteAccessSessionResultTypeDef = TypedDict(
    "GetRemoteAccessSessionResultTypeDef",
    {
        "remoteAccessSession": "RemoteAccessSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRunRequestRequestTypeDef = TypedDict(
    "GetRunRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetRunResultTypeDef = TypedDict(
    "GetRunResultTypeDef",
    {
        "run": "RunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSuiteRequestRequestTypeDef = TypedDict(
    "GetSuiteRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetSuiteResultTypeDef = TypedDict(
    "GetSuiteResultTypeDef",
    {
        "suite": "SuiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTestGridProjectRequestRequestTypeDef = TypedDict(
    "GetTestGridProjectRequestRequestTypeDef",
    {
        "projectArn": str,
    },
)

GetTestGridProjectResultTypeDef = TypedDict(
    "GetTestGridProjectResultTypeDef",
    {
        "testGridProject": "TestGridProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTestGridSessionRequestRequestTypeDef = TypedDict(
    "GetTestGridSessionRequestRequestTypeDef",
    {
        "projectArn": NotRequired[str],
        "sessionId": NotRequired[str],
        "sessionArn": NotRequired[str],
    },
)

GetTestGridSessionResultTypeDef = TypedDict(
    "GetTestGridSessionResultTypeDef",
    {
        "testGridSession": "TestGridSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTestRequestRequestTypeDef = TypedDict(
    "GetTestRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetTestResultTypeDef = TypedDict(
    "GetTestResultTypeDef",
    {
        "test": "TestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUploadRequestRequestTypeDef = TypedDict(
    "GetUploadRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetUploadResultTypeDef = TypedDict(
    "GetUploadResultTypeDef",
    {
        "upload": "UploadTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVPCEConfigurationRequestRequestTypeDef = TypedDict(
    "GetVPCEConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetVPCEConfigurationResultTypeDef = TypedDict(
    "GetVPCEConfigurationResultTypeDef",
    {
        "vpceConfiguration": "VPCEConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IncompatibilityMessageTypeDef = TypedDict(
    "IncompatibilityMessageTypeDef",
    {
        "message": NotRequired[str],
        "type": NotRequired[DeviceAttributeType],
    },
)

InstallToRemoteAccessSessionRequestRequestTypeDef = TypedDict(
    "InstallToRemoteAccessSessionRequestRequestTypeDef",
    {
        "remoteAccessSessionArn": str,
        "appArn": str,
    },
)

InstallToRemoteAccessSessionResultTypeDef = TypedDict(
    "InstallToRemoteAccessSessionResultTypeDef",
    {
        "appUpload": "UploadTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceProfileTypeDef = TypedDict(
    "InstanceProfileTypeDef",
    {
        "arn": NotRequired[str],
        "packageCleanup": NotRequired[bool],
        "excludeAppPackagesFromCleanup": NotRequired[List[str]],
        "rebootAfterUse": NotRequired[bool],
        "name": NotRequired[str],
        "description": NotRequired[str],
    },
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[TestTypeType],
        "created": NotRequired[datetime],
        "status": NotRequired[ExecutionStatusType],
        "result": NotRequired[ExecutionResultType],
        "started": NotRequired[datetime],
        "stopped": NotRequired[datetime],
        "counters": NotRequired["CountersTypeDef"],
        "message": NotRequired[str],
        "device": NotRequired["DeviceTypeDef"],
        "instanceArn": NotRequired[str],
        "deviceMinutes": NotRequired["DeviceMinutesTypeDef"],
        "videoEndpoint": NotRequired[str],
        "videoCapture": NotRequired[bool],
    },
)

ListArtifactsRequestRequestTypeDef = TypedDict(
    "ListArtifactsRequestRequestTypeDef",
    {
        "arn": str,
        "type": ArtifactCategoryType,
        "nextToken": NotRequired[str],
    },
)

ListArtifactsResultTypeDef = TypedDict(
    "ListArtifactsResultTypeDef",
    {
        "artifacts": List["ArtifactTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeviceInstancesRequestRequestTypeDef = TypedDict(
    "ListDeviceInstancesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListDeviceInstancesResultTypeDef = TypedDict(
    "ListDeviceInstancesResultTypeDef",
    {
        "deviceInstances": List["DeviceInstanceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevicePoolsRequestRequestTypeDef = TypedDict(
    "ListDevicePoolsRequestRequestTypeDef",
    {
        "arn": str,
        "type": NotRequired[DevicePoolTypeType],
        "nextToken": NotRequired[str],
    },
)

ListDevicePoolsResultTypeDef = TypedDict(
    "ListDevicePoolsResultTypeDef",
    {
        "devicePools": List["DevicePoolTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevicesRequestRequestTypeDef = TypedDict(
    "ListDevicesRequestRequestTypeDef",
    {
        "arn": NotRequired[str],
        "nextToken": NotRequired[str],
        "filters": NotRequired[Sequence["DeviceFilterTypeDef"]],
    },
)

ListDevicesResultTypeDef = TypedDict(
    "ListDevicesResultTypeDef",
    {
        "devices": List["DeviceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstanceProfilesRequestRequestTypeDef = TypedDict(
    "ListInstanceProfilesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListInstanceProfilesResultTypeDef = TypedDict(
    "ListInstanceProfilesResultTypeDef",
    {
        "instanceProfiles": List["InstanceProfileTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": NotRequired[str],
    },
)

ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef",
    {
        "jobs": List["JobTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNetworkProfilesRequestRequestTypeDef = TypedDict(
    "ListNetworkProfilesRequestRequestTypeDef",
    {
        "arn": str,
        "type": NotRequired[NetworkProfileTypeType],
        "nextToken": NotRequired[str],
    },
)

ListNetworkProfilesResultTypeDef = TypedDict(
    "ListNetworkProfilesResultTypeDef",
    {
        "networkProfiles": List["NetworkProfileTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOfferingPromotionsRequestRequestTypeDef = TypedDict(
    "ListOfferingPromotionsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)

ListOfferingPromotionsResultTypeDef = TypedDict(
    "ListOfferingPromotionsResultTypeDef",
    {
        "offeringPromotions": List["OfferingPromotionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOfferingTransactionsRequestRequestTypeDef = TypedDict(
    "ListOfferingTransactionsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)

ListOfferingTransactionsResultTypeDef = TypedDict(
    "ListOfferingTransactionsResultTypeDef",
    {
        "offeringTransactions": List["OfferingTransactionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOfferingsRequestRequestTypeDef = TypedDict(
    "ListOfferingsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)

ListOfferingsResultTypeDef = TypedDict(
    "ListOfferingsResultTypeDef",
    {
        "offerings": List["OfferingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "arn": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)

ListProjectsResultTypeDef = TypedDict(
    "ListProjectsResultTypeDef",
    {
        "projects": List["ProjectTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRemoteAccessSessionsRequestRequestTypeDef = TypedDict(
    "ListRemoteAccessSessionsRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": NotRequired[str],
    },
)

ListRemoteAccessSessionsResultTypeDef = TypedDict(
    "ListRemoteAccessSessionsResultTypeDef",
    {
        "remoteAccessSessions": List["RemoteAccessSessionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRunsRequestRequestTypeDef = TypedDict(
    "ListRunsRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": NotRequired[str],
    },
)

ListRunsResultTypeDef = TypedDict(
    "ListRunsResultTypeDef",
    {
        "runs": List["RunTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSamplesRequestRequestTypeDef = TypedDict(
    "ListSamplesRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": NotRequired[str],
    },
)

ListSamplesResultTypeDef = TypedDict(
    "ListSamplesResultTypeDef",
    {
        "samples": List["SampleTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSuitesRequestRequestTypeDef = TypedDict(
    "ListSuitesRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": NotRequired[str],
    },
)

ListSuitesResultTypeDef = TypedDict(
    "ListSuitesResultTypeDef",
    {
        "suites": List["SuiteTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTestGridProjectsRequestRequestTypeDef = TypedDict(
    "ListTestGridProjectsRequestRequestTypeDef",
    {
        "maxResult": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListTestGridProjectsResultTypeDef = TypedDict(
    "ListTestGridProjectsResultTypeDef",
    {
        "testGridProjects": List["TestGridProjectTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTestGridSessionActionsRequestRequestTypeDef = TypedDict(
    "ListTestGridSessionActionsRequestRequestTypeDef",
    {
        "sessionArn": str,
        "maxResult": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListTestGridSessionActionsResultTypeDef = TypedDict(
    "ListTestGridSessionActionsResultTypeDef",
    {
        "actions": List["TestGridSessionActionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTestGridSessionArtifactsRequestRequestTypeDef = TypedDict(
    "ListTestGridSessionArtifactsRequestRequestTypeDef",
    {
        "sessionArn": str,
        "type": NotRequired[TestGridSessionArtifactCategoryType],
        "maxResult": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListTestGridSessionArtifactsResultTypeDef = TypedDict(
    "ListTestGridSessionArtifactsResultTypeDef",
    {
        "artifacts": List["TestGridSessionArtifactTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTestGridSessionsRequestRequestTypeDef = TypedDict(
    "ListTestGridSessionsRequestRequestTypeDef",
    {
        "projectArn": str,
        "status": NotRequired[TestGridSessionStatusType],
        "creationTimeAfter": NotRequired[Union[datetime, str]],
        "creationTimeBefore": NotRequired[Union[datetime, str]],
        "endTimeAfter": NotRequired[Union[datetime, str]],
        "endTimeBefore": NotRequired[Union[datetime, str]],
        "maxResult": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListTestGridSessionsResultTypeDef = TypedDict(
    "ListTestGridSessionsResultTypeDef",
    {
        "testGridSessions": List["TestGridSessionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTestsRequestRequestTypeDef = TypedDict(
    "ListTestsRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": NotRequired[str],
    },
)

ListTestsResultTypeDef = TypedDict(
    "ListTestsResultTypeDef",
    {
        "tests": List["TestTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUniqueProblemsRequestRequestTypeDef = TypedDict(
    "ListUniqueProblemsRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": NotRequired[str],
    },
)

ListUniqueProblemsResultTypeDef = TypedDict(
    "ListUniqueProblemsResultTypeDef",
    {
        "uniqueProblems": Dict[ExecutionResultType, List["UniqueProblemTypeDef"]],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUploadsRequestRequestTypeDef = TypedDict(
    "ListUploadsRequestRequestTypeDef",
    {
        "arn": str,
        "type": NotRequired[UploadTypeType],
        "nextToken": NotRequired[str],
    },
)

ListUploadsResultTypeDef = TypedDict(
    "ListUploadsResultTypeDef",
    {
        "uploads": List["UploadTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVPCEConfigurationsRequestRequestTypeDef = TypedDict(
    "ListVPCEConfigurationsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListVPCEConfigurationsResultTypeDef = TypedDict(
    "ListVPCEConfigurationsResultTypeDef",
    {
        "vpceConfigurations": List["VPCEConfigurationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "latitude": float,
        "longitude": float,
    },
)

MonetaryAmountTypeDef = TypedDict(
    "MonetaryAmountTypeDef",
    {
        "amount": NotRequired[float],
        "currencyCode": NotRequired[Literal["USD"]],
    },
)

NetworkProfileTypeDef = TypedDict(
    "NetworkProfileTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "type": NotRequired[NetworkProfileTypeType],
        "uplinkBandwidthBits": NotRequired[int],
        "downlinkBandwidthBits": NotRequired[int],
        "uplinkDelayMs": NotRequired[int],
        "downlinkDelayMs": NotRequired[int],
        "uplinkJitterMs": NotRequired[int],
        "downlinkJitterMs": NotRequired[int],
        "uplinkLossPercent": NotRequired[int],
        "downlinkLossPercent": NotRequired[int],
    },
)

OfferingPromotionTypeDef = TypedDict(
    "OfferingPromotionTypeDef",
    {
        "id": NotRequired[str],
        "description": NotRequired[str],
    },
)

OfferingStatusTypeDef = TypedDict(
    "OfferingStatusTypeDef",
    {
        "type": NotRequired[OfferingTransactionTypeType],
        "offering": NotRequired["OfferingTypeDef"],
        "quantity": NotRequired[int],
        "effectiveOn": NotRequired[datetime],
    },
)

OfferingTransactionTypeDef = TypedDict(
    "OfferingTransactionTypeDef",
    {
        "offeringStatus": NotRequired["OfferingStatusTypeDef"],
        "transactionId": NotRequired[str],
        "offeringPromotionId": NotRequired[str],
        "createdOn": NotRequired[datetime],
        "cost": NotRequired["MonetaryAmountTypeDef"],
    },
)

OfferingTypeDef = TypedDict(
    "OfferingTypeDef",
    {
        "id": NotRequired[str],
        "description": NotRequired[str],
        "type": NotRequired[Literal["RECURRING"]],
        "platform": NotRequired[DevicePlatformType],
        "recurringCharges": NotRequired[List["RecurringChargeTypeDef"]],
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

ProblemDetailTypeDef = TypedDict(
    "ProblemDetailTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
    },
)

ProblemTypeDef = TypedDict(
    "ProblemTypeDef",
    {
        "run": NotRequired["ProblemDetailTypeDef"],
        "job": NotRequired["ProblemDetailTypeDef"],
        "suite": NotRequired["ProblemDetailTypeDef"],
        "test": NotRequired["ProblemDetailTypeDef"],
        "device": NotRequired["DeviceTypeDef"],
        "result": NotRequired[ExecutionResultType],
        "message": NotRequired[str],
    },
)

ProjectTypeDef = TypedDict(
    "ProjectTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "defaultJobTimeoutMinutes": NotRequired[int],
        "created": NotRequired[datetime],
    },
)

PurchaseOfferingRequestRequestTypeDef = TypedDict(
    "PurchaseOfferingRequestRequestTypeDef",
    {
        "offeringId": str,
        "quantity": int,
        "offeringPromotionId": NotRequired[str],
    },
)

PurchaseOfferingResultTypeDef = TypedDict(
    "PurchaseOfferingResultTypeDef",
    {
        "offeringTransaction": "OfferingTransactionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RadiosTypeDef = TypedDict(
    "RadiosTypeDef",
    {
        "wifi": NotRequired[bool],
        "bluetooth": NotRequired[bool],
        "nfc": NotRequired[bool],
        "gps": NotRequired[bool],
    },
)

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {
        "cost": NotRequired["MonetaryAmountTypeDef"],
        "frequency": NotRequired[Literal["MONTHLY"]],
    },
)

RemoteAccessSessionTypeDef = TypedDict(
    "RemoteAccessSessionTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "created": NotRequired[datetime],
        "status": NotRequired[ExecutionStatusType],
        "result": NotRequired[ExecutionResultType],
        "message": NotRequired[str],
        "started": NotRequired[datetime],
        "stopped": NotRequired[datetime],
        "device": NotRequired["DeviceTypeDef"],
        "instanceArn": NotRequired[str],
        "remoteDebugEnabled": NotRequired[bool],
        "remoteRecordEnabled": NotRequired[bool],
        "remoteRecordAppArn": NotRequired[str],
        "hostAddress": NotRequired[str],
        "clientId": NotRequired[str],
        "billingMethod": NotRequired[BillingMethodType],
        "deviceMinutes": NotRequired["DeviceMinutesTypeDef"],
        "endpoint": NotRequired[str],
        "deviceUdid": NotRequired[str],
        "interactionMode": NotRequired[InteractionModeType],
        "skipAppResign": NotRequired[bool],
    },
)

RenewOfferingRequestRequestTypeDef = TypedDict(
    "RenewOfferingRequestRequestTypeDef",
    {
        "offeringId": str,
        "quantity": int,
    },
)

RenewOfferingResultTypeDef = TypedDict(
    "RenewOfferingResultTypeDef",
    {
        "offeringTransaction": "OfferingTransactionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResolutionTypeDef = TypedDict(
    "ResolutionTypeDef",
    {
        "width": NotRequired[int],
        "height": NotRequired[int],
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
        "attribute": NotRequired[DeviceAttributeType],
        "operator": NotRequired[RuleOperatorType],
        "value": NotRequired[str],
    },
)

RunTypeDef = TypedDict(
    "RunTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[TestTypeType],
        "platform": NotRequired[DevicePlatformType],
        "created": NotRequired[datetime],
        "status": NotRequired[ExecutionStatusType],
        "result": NotRequired[ExecutionResultType],
        "started": NotRequired[datetime],
        "stopped": NotRequired[datetime],
        "counters": NotRequired["CountersTypeDef"],
        "message": NotRequired[str],
        "totalJobs": NotRequired[int],
        "completedJobs": NotRequired[int],
        "billingMethod": NotRequired[BillingMethodType],
        "deviceMinutes": NotRequired["DeviceMinutesTypeDef"],
        "networkProfile": NotRequired["NetworkProfileTypeDef"],
        "parsingResultUrl": NotRequired[str],
        "resultCode": NotRequired[ExecutionResultCodeType],
        "seed": NotRequired[int],
        "appUpload": NotRequired[str],
        "eventCount": NotRequired[int],
        "jobTimeoutMinutes": NotRequired[int],
        "devicePoolArn": NotRequired[str],
        "locale": NotRequired[str],
        "radios": NotRequired["RadiosTypeDef"],
        "location": NotRequired["LocationTypeDef"],
        "customerArtifactPaths": NotRequired["CustomerArtifactPathsTypeDef"],
        "webUrl": NotRequired[str],
        "skipAppResign": NotRequired[bool],
        "testSpecArn": NotRequired[str],
        "deviceSelectionResult": NotRequired["DeviceSelectionResultTypeDef"],
    },
)

SampleTypeDef = TypedDict(
    "SampleTypeDef",
    {
        "arn": NotRequired[str],
        "type": NotRequired[SampleTypeType],
        "url": NotRequired[str],
    },
)

ScheduleRunConfigurationTypeDef = TypedDict(
    "ScheduleRunConfigurationTypeDef",
    {
        "extraDataPackageArn": NotRequired[str],
        "networkProfileArn": NotRequired[str],
        "locale": NotRequired[str],
        "location": NotRequired["LocationTypeDef"],
        "vpceConfigurationArns": NotRequired[Sequence[str]],
        "customerArtifactPaths": NotRequired["CustomerArtifactPathsTypeDef"],
        "radios": NotRequired["RadiosTypeDef"],
        "auxiliaryApps": NotRequired[Sequence[str]],
        "billingMethod": NotRequired[BillingMethodType],
    },
)

ScheduleRunRequestRequestTypeDef = TypedDict(
    "ScheduleRunRequestRequestTypeDef",
    {
        "projectArn": str,
        "test": "ScheduleRunTestTypeDef",
        "appArn": NotRequired[str],
        "devicePoolArn": NotRequired[str],
        "deviceSelectionConfiguration": NotRequired["DeviceSelectionConfigurationTypeDef"],
        "name": NotRequired[str],
        "configuration": NotRequired["ScheduleRunConfigurationTypeDef"],
        "executionConfiguration": NotRequired["ExecutionConfigurationTypeDef"],
    },
)

ScheduleRunResultTypeDef = TypedDict(
    "ScheduleRunResultTypeDef",
    {
        "run": "RunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ScheduleRunTestTypeDef = TypedDict(
    "ScheduleRunTestTypeDef",
    {
        "type": TestTypeType,
        "testPackageArn": NotRequired[str],
        "testSpecArn": NotRequired[str],
        "filter": NotRequired[str],
        "parameters": NotRequired[Mapping[str, str]],
    },
)

StopJobRequestRequestTypeDef = TypedDict(
    "StopJobRequestRequestTypeDef",
    {
        "arn": str,
    },
)

StopJobResultTypeDef = TypedDict(
    "StopJobResultTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopRemoteAccessSessionRequestRequestTypeDef = TypedDict(
    "StopRemoteAccessSessionRequestRequestTypeDef",
    {
        "arn": str,
    },
)

StopRemoteAccessSessionResultTypeDef = TypedDict(
    "StopRemoteAccessSessionResultTypeDef",
    {
        "remoteAccessSession": "RemoteAccessSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopRunRequestRequestTypeDef = TypedDict(
    "StopRunRequestRequestTypeDef",
    {
        "arn": str,
    },
)

StopRunResultTypeDef = TypedDict(
    "StopRunResultTypeDef",
    {
        "run": "RunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SuiteTypeDef = TypedDict(
    "SuiteTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[TestTypeType],
        "created": NotRequired[datetime],
        "status": NotRequired[ExecutionStatusType],
        "result": NotRequired[ExecutionResultType],
        "started": NotRequired[datetime],
        "stopped": NotRequired[datetime],
        "counters": NotRequired["CountersTypeDef"],
        "message": NotRequired[str],
        "deviceMinutes": NotRequired["DeviceMinutesTypeDef"],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
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

TestGridProjectTypeDef = TypedDict(
    "TestGridProjectTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "vpcConfig": NotRequired["TestGridVpcConfigTypeDef"],
        "created": NotRequired[datetime],
    },
)

TestGridSessionActionTypeDef = TypedDict(
    "TestGridSessionActionTypeDef",
    {
        "action": NotRequired[str],
        "started": NotRequired[datetime],
        "duration": NotRequired[int],
        "statusCode": NotRequired[str],
        "requestMethod": NotRequired[str],
    },
)

TestGridSessionArtifactTypeDef = TypedDict(
    "TestGridSessionArtifactTypeDef",
    {
        "filename": NotRequired[str],
        "type": NotRequired[TestGridSessionArtifactTypeType],
        "url": NotRequired[str],
    },
)

TestGridSessionTypeDef = TypedDict(
    "TestGridSessionTypeDef",
    {
        "arn": NotRequired[str],
        "status": NotRequired[TestGridSessionStatusType],
        "created": NotRequired[datetime],
        "ended": NotRequired[datetime],
        "billingMinutes": NotRequired[float],
        "seleniumProperties": NotRequired[str],
    },
)

TestGridVpcConfigTypeDef = TypedDict(
    "TestGridVpcConfigTypeDef",
    {
        "securityGroupIds": Sequence[str],
        "subnetIds": Sequence[str],
        "vpcId": str,
    },
)

TestTypeDef = TypedDict(
    "TestTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[TestTypeType],
        "created": NotRequired[datetime],
        "status": NotRequired[ExecutionStatusType],
        "result": NotRequired[ExecutionResultType],
        "started": NotRequired[datetime],
        "stopped": NotRequired[datetime],
        "counters": NotRequired["CountersTypeDef"],
        "message": NotRequired[str],
        "deviceMinutes": NotRequired["DeviceMinutesTypeDef"],
    },
)

TrialMinutesTypeDef = TypedDict(
    "TrialMinutesTypeDef",
    {
        "total": NotRequired[float],
        "remaining": NotRequired[float],
    },
)

UniqueProblemTypeDef = TypedDict(
    "UniqueProblemTypeDef",
    {
        "message": NotRequired[str],
        "problems": NotRequired[List["ProblemTypeDef"]],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateDeviceInstanceRequestRequestTypeDef = TypedDict(
    "UpdateDeviceInstanceRequestRequestTypeDef",
    {
        "arn": str,
        "profileArn": NotRequired[str],
        "labels": NotRequired[Sequence[str]],
    },
)

UpdateDeviceInstanceResultTypeDef = TypedDict(
    "UpdateDeviceInstanceResultTypeDef",
    {
        "deviceInstance": "DeviceInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDevicePoolRequestRequestTypeDef = TypedDict(
    "UpdateDevicePoolRequestRequestTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "rules": NotRequired[Sequence["RuleTypeDef"]],
        "maxDevices": NotRequired[int],
        "clearMaxDevices": NotRequired[bool],
    },
)

UpdateDevicePoolResultTypeDef = TypedDict(
    "UpdateDevicePoolResultTypeDef",
    {
        "devicePool": "DevicePoolTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateInstanceProfileRequestRequestTypeDef = TypedDict(
    "UpdateInstanceProfileRequestRequestTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "packageCleanup": NotRequired[bool],
        "excludeAppPackagesFromCleanup": NotRequired[Sequence[str]],
        "rebootAfterUse": NotRequired[bool],
    },
)

UpdateInstanceProfileResultTypeDef = TypedDict(
    "UpdateInstanceProfileResultTypeDef",
    {
        "instanceProfile": "InstanceProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateNetworkProfileRequestRequestTypeDef = TypedDict(
    "UpdateNetworkProfileRequestRequestTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "type": NotRequired[NetworkProfileTypeType],
        "uplinkBandwidthBits": NotRequired[int],
        "downlinkBandwidthBits": NotRequired[int],
        "uplinkDelayMs": NotRequired[int],
        "downlinkDelayMs": NotRequired[int],
        "uplinkJitterMs": NotRequired[int],
        "downlinkJitterMs": NotRequired[int],
        "uplinkLossPercent": NotRequired[int],
        "downlinkLossPercent": NotRequired[int],
    },
)

UpdateNetworkProfileResultTypeDef = TypedDict(
    "UpdateNetworkProfileResultTypeDef",
    {
        "networkProfile": "NetworkProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProjectRequestRequestTypeDef = TypedDict(
    "UpdateProjectRequestRequestTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "defaultJobTimeoutMinutes": NotRequired[int],
    },
)

UpdateProjectResultTypeDef = TypedDict(
    "UpdateProjectResultTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTestGridProjectRequestRequestTypeDef = TypedDict(
    "UpdateTestGridProjectRequestRequestTypeDef",
    {
        "projectArn": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "vpcConfig": NotRequired["TestGridVpcConfigTypeDef"],
    },
)

UpdateTestGridProjectResultTypeDef = TypedDict(
    "UpdateTestGridProjectResultTypeDef",
    {
        "testGridProject": "TestGridProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUploadRequestRequestTypeDef = TypedDict(
    "UpdateUploadRequestRequestTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "contentType": NotRequired[str],
        "editContent": NotRequired[bool],
    },
)

UpdateUploadResultTypeDef = TypedDict(
    "UpdateUploadResultTypeDef",
    {
        "upload": "UploadTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVPCEConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateVPCEConfigurationRequestRequestTypeDef",
    {
        "arn": str,
        "vpceConfigurationName": NotRequired[str],
        "vpceServiceName": NotRequired[str],
        "serviceDnsName": NotRequired[str],
        "vpceConfigurationDescription": NotRequired[str],
    },
)

UpdateVPCEConfigurationResultTypeDef = TypedDict(
    "UpdateVPCEConfigurationResultTypeDef",
    {
        "vpceConfiguration": "VPCEConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UploadTypeDef = TypedDict(
    "UploadTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "created": NotRequired[datetime],
        "type": NotRequired[UploadTypeType],
        "status": NotRequired[UploadStatusType],
        "url": NotRequired[str],
        "metadata": NotRequired[str],
        "contentType": NotRequired[str],
        "message": NotRequired[str],
        "category": NotRequired[UploadCategoryType],
    },
)

VPCEConfigurationTypeDef = TypedDict(
    "VPCEConfigurationTypeDef",
    {
        "arn": NotRequired[str],
        "vpceConfigurationName": NotRequired[str],
        "vpceServiceName": NotRequired[str],
        "serviceDnsName": NotRequired[str],
        "vpceConfigurationDescription": NotRequired[str],
    },
)
