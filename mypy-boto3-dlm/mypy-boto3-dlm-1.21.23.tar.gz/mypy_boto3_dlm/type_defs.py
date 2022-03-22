"""
Type annotations for dlm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dlm/type_defs.html)

Usage::

    ```python
    from mypy_boto3_dlm.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    GettablePolicyStateValuesType,
    LocationValuesType,
    PolicyTypeValuesType,
    ResourceLocationValuesType,
    ResourceTypeValuesType,
    RetentionIntervalUnitValuesType,
    SettablePolicyStateValuesType,
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
    "ActionTypeDef",
    "CreateLifecyclePolicyRequestRequestTypeDef",
    "CreateLifecyclePolicyResponseTypeDef",
    "CreateRuleTypeDef",
    "CrossRegionCopyActionTypeDef",
    "CrossRegionCopyDeprecateRuleTypeDef",
    "CrossRegionCopyRetainRuleTypeDef",
    "CrossRegionCopyRuleTypeDef",
    "DeleteLifecyclePolicyRequestRequestTypeDef",
    "DeprecateRuleTypeDef",
    "EncryptionConfigurationTypeDef",
    "EventParametersTypeDef",
    "EventSourceTypeDef",
    "FastRestoreRuleTypeDef",
    "GetLifecyclePoliciesRequestRequestTypeDef",
    "GetLifecyclePoliciesResponseTypeDef",
    "GetLifecyclePolicyRequestRequestTypeDef",
    "GetLifecyclePolicyResponseTypeDef",
    "LifecyclePolicySummaryTypeDef",
    "LifecyclePolicyTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ParametersTypeDef",
    "PolicyDetailsTypeDef",
    "ResponseMetadataTypeDef",
    "RetainRuleTypeDef",
    "ScheduleTypeDef",
    "ShareRuleTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateLifecyclePolicyRequestRequestTypeDef",
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "Name": str,
        "CrossRegionCopy": Sequence["CrossRegionCopyActionTypeDef"],
    },
)

CreateLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "CreateLifecyclePolicyRequestRequestTypeDef",
    {
        "ExecutionRoleArn": str,
        "Description": str,
        "State": SettablePolicyStateValuesType,
        "PolicyDetails": "PolicyDetailsTypeDef",
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateLifecyclePolicyResponseTypeDef = TypedDict(
    "CreateLifecyclePolicyResponseTypeDef",
    {
        "PolicyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRuleTypeDef = TypedDict(
    "CreateRuleTypeDef",
    {
        "Location": NotRequired[LocationValuesType],
        "Interval": NotRequired[int],
        "IntervalUnit": NotRequired[Literal["HOURS"]],
        "Times": NotRequired[Sequence[str]],
        "CronExpression": NotRequired[str],
    },
)

CrossRegionCopyActionTypeDef = TypedDict(
    "CrossRegionCopyActionTypeDef",
    {
        "Target": str,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "RetainRule": NotRequired["CrossRegionCopyRetainRuleTypeDef"],
    },
)

CrossRegionCopyDeprecateRuleTypeDef = TypedDict(
    "CrossRegionCopyDeprecateRuleTypeDef",
    {
        "Interval": NotRequired[int],
        "IntervalUnit": NotRequired[RetentionIntervalUnitValuesType],
    },
)

CrossRegionCopyRetainRuleTypeDef = TypedDict(
    "CrossRegionCopyRetainRuleTypeDef",
    {
        "Interval": NotRequired[int],
        "IntervalUnit": NotRequired[RetentionIntervalUnitValuesType],
    },
)

CrossRegionCopyRuleTypeDef = TypedDict(
    "CrossRegionCopyRuleTypeDef",
    {
        "Encrypted": bool,
        "TargetRegion": NotRequired[str],
        "Target": NotRequired[str],
        "CmkArn": NotRequired[str],
        "CopyTags": NotRequired[bool],
        "RetainRule": NotRequired["CrossRegionCopyRetainRuleTypeDef"],
        "DeprecateRule": NotRequired["CrossRegionCopyDeprecateRuleTypeDef"],
    },
)

DeleteLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "DeleteLifecyclePolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)

DeprecateRuleTypeDef = TypedDict(
    "DeprecateRuleTypeDef",
    {
        "Count": NotRequired[int],
        "Interval": NotRequired[int],
        "IntervalUnit": NotRequired[RetentionIntervalUnitValuesType],
    },
)

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "Encrypted": bool,
        "CmkArn": NotRequired[str],
    },
)

EventParametersTypeDef = TypedDict(
    "EventParametersTypeDef",
    {
        "EventType": Literal["shareSnapshot"],
        "SnapshotOwner": Sequence[str],
        "DescriptionRegex": str,
    },
)

EventSourceTypeDef = TypedDict(
    "EventSourceTypeDef",
    {
        "Type": Literal["MANAGED_CWE"],
        "Parameters": NotRequired["EventParametersTypeDef"],
    },
)

FastRestoreRuleTypeDef = TypedDict(
    "FastRestoreRuleTypeDef",
    {
        "AvailabilityZones": Sequence[str],
        "Count": NotRequired[int],
        "Interval": NotRequired[int],
        "IntervalUnit": NotRequired[RetentionIntervalUnitValuesType],
    },
)

GetLifecyclePoliciesRequestRequestTypeDef = TypedDict(
    "GetLifecyclePoliciesRequestRequestTypeDef",
    {
        "PolicyIds": NotRequired[Sequence[str]],
        "State": NotRequired[GettablePolicyStateValuesType],
        "ResourceTypes": NotRequired[Sequence[ResourceTypeValuesType]],
        "TargetTags": NotRequired[Sequence[str]],
        "TagsToAdd": NotRequired[Sequence[str]],
    },
)

GetLifecyclePoliciesResponseTypeDef = TypedDict(
    "GetLifecyclePoliciesResponseTypeDef",
    {
        "Policies": List["LifecyclePolicySummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "GetLifecyclePolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)

GetLifecyclePolicyResponseTypeDef = TypedDict(
    "GetLifecyclePolicyResponseTypeDef",
    {
        "Policy": "LifecyclePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LifecyclePolicySummaryTypeDef = TypedDict(
    "LifecyclePolicySummaryTypeDef",
    {
        "PolicyId": NotRequired[str],
        "Description": NotRequired[str],
        "State": NotRequired[GettablePolicyStateValuesType],
        "Tags": NotRequired[Dict[str, str]],
        "PolicyType": NotRequired[PolicyTypeValuesType],
    },
)

LifecyclePolicyTypeDef = TypedDict(
    "LifecyclePolicyTypeDef",
    {
        "PolicyId": NotRequired[str],
        "Description": NotRequired[str],
        "State": NotRequired[GettablePolicyStateValuesType],
        "StatusMessage": NotRequired[str],
        "ExecutionRoleArn": NotRequired[str],
        "DateCreated": NotRequired[datetime],
        "DateModified": NotRequired[datetime],
        "PolicyDetails": NotRequired["PolicyDetailsTypeDef"],
        "Tags": NotRequired[Dict[str, str]],
        "PolicyArn": NotRequired[str],
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

ParametersTypeDef = TypedDict(
    "ParametersTypeDef",
    {
        "ExcludeBootVolume": NotRequired[bool],
        "NoReboot": NotRequired[bool],
    },
)

PolicyDetailsTypeDef = TypedDict(
    "PolicyDetailsTypeDef",
    {
        "PolicyType": NotRequired[PolicyTypeValuesType],
        "ResourceTypes": NotRequired[Sequence[ResourceTypeValuesType]],
        "ResourceLocations": NotRequired[Sequence[ResourceLocationValuesType]],
        "TargetTags": NotRequired[Sequence["TagTypeDef"]],
        "Schedules": NotRequired[Sequence["ScheduleTypeDef"]],
        "Parameters": NotRequired["ParametersTypeDef"],
        "EventSource": NotRequired["EventSourceTypeDef"],
        "Actions": NotRequired[Sequence["ActionTypeDef"]],
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

RetainRuleTypeDef = TypedDict(
    "RetainRuleTypeDef",
    {
        "Count": NotRequired[int],
        "Interval": NotRequired[int],
        "IntervalUnit": NotRequired[RetentionIntervalUnitValuesType],
    },
)

ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "Name": NotRequired[str],
        "CopyTags": NotRequired[bool],
        "TagsToAdd": NotRequired[Sequence["TagTypeDef"]],
        "VariableTags": NotRequired[Sequence["TagTypeDef"]],
        "CreateRule": NotRequired["CreateRuleTypeDef"],
        "RetainRule": NotRequired["RetainRuleTypeDef"],
        "FastRestoreRule": NotRequired["FastRestoreRuleTypeDef"],
        "CrossRegionCopyRules": NotRequired[Sequence["CrossRegionCopyRuleTypeDef"]],
        "ShareRules": NotRequired[Sequence["ShareRuleTypeDef"]],
        "DeprecateRule": NotRequired["DeprecateRuleTypeDef"],
    },
)

ShareRuleTypeDef = TypedDict(
    "ShareRuleTypeDef",
    {
        "TargetAccounts": Sequence[str],
        "UnshareInterval": NotRequired[int],
        "UnshareIntervalUnit": NotRequired[RetentionIntervalUnitValuesType],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "UpdateLifecyclePolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
        "ExecutionRoleArn": NotRequired[str],
        "State": NotRequired[SettablePolicyStateValuesType],
        "Description": NotRequired[str],
        "PolicyDetails": NotRequired["PolicyDetailsTypeDef"],
    },
)
