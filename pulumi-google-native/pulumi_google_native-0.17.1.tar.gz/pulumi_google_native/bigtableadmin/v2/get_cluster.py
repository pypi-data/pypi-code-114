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
    'GetClusterResult',
    'AwaitableGetClusterResult',
    'get_cluster',
    'get_cluster_output',
]

@pulumi.output_type
class GetClusterResult:
    def __init__(__self__, cluster_config=None, default_storage_type=None, encryption_config=None, location=None, name=None, serve_nodes=None, state=None):
        if cluster_config and not isinstance(cluster_config, dict):
            raise TypeError("Expected argument 'cluster_config' to be a dict")
        pulumi.set(__self__, "cluster_config", cluster_config)
        if default_storage_type and not isinstance(default_storage_type, str):
            raise TypeError("Expected argument 'default_storage_type' to be a str")
        pulumi.set(__self__, "default_storage_type", default_storage_type)
        if encryption_config and not isinstance(encryption_config, dict):
            raise TypeError("Expected argument 'encryption_config' to be a dict")
        pulumi.set(__self__, "encryption_config", encryption_config)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if serve_nodes and not isinstance(serve_nodes, int):
            raise TypeError("Expected argument 'serve_nodes' to be a int")
        pulumi.set(__self__, "serve_nodes", serve_nodes)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="clusterConfig")
    def cluster_config(self) -> 'outputs.ClusterConfigResponse':
        """
        Configuration for this cluster.
        """
        return pulumi.get(self, "cluster_config")

    @property
    @pulumi.getter(name="defaultStorageType")
    def default_storage_type(self) -> str:
        """
        Immutable. The type of storage used by this cluster to serve its parent instance's tables, unless explicitly overridden.
        """
        return pulumi.get(self, "default_storage_type")

    @property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> 'outputs.EncryptionConfigResponse':
        """
        Immutable. The encryption configuration for CMEK-protected clusters.
        """
        return pulumi.get(self, "encryption_config")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Immutable. The location where this cluster's nodes and storage reside. For best performance, clients should be located as close as possible to this cluster. Currently only zones are supported, so values should be of the form `projects/{project}/locations/{zone}`.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The unique name of the cluster. Values are of the form `projects/{project}/instances/{instance}/clusters/a-z*`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="serveNodes")
    def serve_nodes(self) -> int:
        """
        The number of nodes allocated to this cluster. More nodes enable higher throughput and more consistent performance.
        """
        return pulumi.get(self, "serve_nodes")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the cluster.
        """
        return pulumi.get(self, "state")


class AwaitableGetClusterResult(GetClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterResult(
            cluster_config=self.cluster_config,
            default_storage_type=self.default_storage_type,
            encryption_config=self.encryption_config,
            location=self.location,
            name=self.name,
            serve_nodes=self.serve_nodes,
            state=self.state)


def get_cluster(cluster_id: Optional[str] = None,
                instance_id: Optional[str] = None,
                project: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterResult:
    """
    Gets information about a cluster.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    __args__['instanceId'] = instance_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:bigtableadmin/v2:getCluster', __args__, opts=opts, typ=GetClusterResult).value

    return AwaitableGetClusterResult(
        cluster_config=__ret__.cluster_config,
        default_storage_type=__ret__.default_storage_type,
        encryption_config=__ret__.encryption_config,
        location=__ret__.location,
        name=__ret__.name,
        serve_nodes=__ret__.serve_nodes,
        state=__ret__.state)


@_utilities.lift_output_func(get_cluster)
def get_cluster_output(cluster_id: Optional[pulumi.Input[str]] = None,
                       instance_id: Optional[pulumi.Input[str]] = None,
                       project: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterResult]:
    """
    Gets information about a cluster.
    """
    ...
