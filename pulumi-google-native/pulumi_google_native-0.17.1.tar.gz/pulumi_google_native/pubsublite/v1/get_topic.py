# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetTopicResult',
    'AwaitableGetTopicResult',
    'get_topic',
    'get_topic_output',
]

@pulumi.output_type
class GetTopicResult:
    def __init__(__self__, name=None, partition_config=None, reservation_config=None, retention_config=None):
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partition_config and not isinstance(partition_config, dict):
            raise TypeError("Expected argument 'partition_config' to be a dict")
        pulumi.set(__self__, "partition_config", partition_config)
        if reservation_config and not isinstance(reservation_config, dict):
            raise TypeError("Expected argument 'reservation_config' to be a dict")
        pulumi.set(__self__, "reservation_config", reservation_config)
        if retention_config and not isinstance(retention_config, dict):
            raise TypeError("Expected argument 'retention_config' to be a dict")
        pulumi.set(__self__, "retention_config", retention_config)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the topic. Structured like: projects/{project_number}/locations/{location}/topics/{topic_id}
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partitionConfig")
    def partition_config(self) -> 'outputs.PartitionConfigResponse':
        """
        The settings for this topic's partitions.
        """
        return pulumi.get(self, "partition_config")

    @property
    @pulumi.getter(name="reservationConfig")
    def reservation_config(self) -> 'outputs.ReservationConfigResponse':
        """
        The settings for this topic's Reservation usage.
        """
        return pulumi.get(self, "reservation_config")

    @property
    @pulumi.getter(name="retentionConfig")
    def retention_config(self) -> 'outputs.RetentionConfigResponse':
        """
        The settings for this topic's message retention.
        """
        return pulumi.get(self, "retention_config")


class AwaitableGetTopicResult(GetTopicResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTopicResult(
            name=self.name,
            partition_config=self.partition_config,
            reservation_config=self.reservation_config,
            retention_config=self.retention_config)


def get_topic(location: Optional[str] = None,
              project: Optional[str] = None,
              topic_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTopicResult:
    """
    Returns the topic configuration.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['project'] = project
    __args__['topicId'] = topic_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:pubsublite/v1:getTopic', __args__, opts=opts, typ=GetTopicResult).value

    return AwaitableGetTopicResult(
        name=__ret__.name,
        partition_config=__ret__.partition_config,
        reservation_config=__ret__.reservation_config,
        retention_config=__ret__.retention_config)


@_utilities.lift_output_func(get_topic)
def get_topic_output(location: Optional[pulumi.Input[str]] = None,
                     project: Optional[pulumi.Input[Optional[str]]] = None,
                     topic_id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTopicResult]:
    """
    Returns the topic configuration.
    """
    ...
