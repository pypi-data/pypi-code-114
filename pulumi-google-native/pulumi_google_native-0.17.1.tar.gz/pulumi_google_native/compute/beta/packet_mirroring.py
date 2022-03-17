# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['PacketMirroringArgs', 'PacketMirroring']

@pulumi.input_type
class PacketMirroringArgs:
    def __init__(__self__, *,
                 region: pulumi.Input[str],
                 collector_ilb: Optional[pulumi.Input['PacketMirroringForwardingRuleInfoArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable: Optional[pulumi.Input['PacketMirroringEnable']] = None,
                 filter: Optional[pulumi.Input['PacketMirroringFilterArgs']] = None,
                 mirrored_resources: Optional[pulumi.Input['PacketMirroringMirroredResourceInfoArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input['PacketMirroringNetworkInfoArgs']] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PacketMirroring resource.
        :param pulumi.Input['PacketMirroringForwardingRuleInfoArgs'] collector_ilb: The Forwarding Rule resource of type loadBalancingScheme=INTERNAL that will be used as collector for mirrored traffic. The specified forwarding rule must have isMirroringCollector set to true.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input['PacketMirroringEnable'] enable: Indicates whether or not this packet mirroring takes effect. If set to FALSE, this packet mirroring policy will not be enforced on the network. The default is TRUE.
        :param pulumi.Input['PacketMirroringFilterArgs'] filter: Filter for mirrored traffic. If unspecified, all traffic is mirrored.
        :param pulumi.Input['PacketMirroringMirroredResourceInfoArgs'] mirrored_resources: PacketMirroring mirroredResourceInfos. MirroredResourceInfo specifies a set of mirrored VM instances, subnetworks and/or tags for which traffic from/to all VM instances will be mirrored.
        :param pulumi.Input[str] name: Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input['PacketMirroringNetworkInfoArgs'] network: Specifies the mirrored VPC network. Only packets in this network will be mirrored. All mirrored VMs should have a NIC in the given network. All mirrored subnetworks should belong to the given network.
        :param pulumi.Input[int] priority: The priority of applying this configuration. Priority is used to break ties in cases where there is more than one matching rule. In the case of two rules that apply for a given Instance, the one with the lowest-numbered priority value wins. Default value is 1000. Valid range is 0 through 65535.
        :param pulumi.Input[str] request_id: An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported ( 00000000-0000-0000-0000-000000000000).
        """
        pulumi.set(__self__, "region", region)
        if collector_ilb is not None:
            pulumi.set(__self__, "collector_ilb", collector_ilb)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if mirrored_resources is not None:
            pulumi.set(__self__, "mirrored_resources", mirrored_resources)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network is not None:
            pulumi.set(__self__, "network", network)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="collectorIlb")
    def collector_ilb(self) -> Optional[pulumi.Input['PacketMirroringForwardingRuleInfoArgs']]:
        """
        The Forwarding Rule resource of type loadBalancingScheme=INTERNAL that will be used as collector for mirrored traffic. The specified forwarding rule must have isMirroringCollector set to true.
        """
        return pulumi.get(self, "collector_ilb")

    @collector_ilb.setter
    def collector_ilb(self, value: Optional[pulumi.Input['PacketMirroringForwardingRuleInfoArgs']]):
        pulumi.set(self, "collector_ilb", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional description of this resource. Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input['PacketMirroringEnable']]:
        """
        Indicates whether or not this packet mirroring takes effect. If set to FALSE, this packet mirroring policy will not be enforced on the network. The default is TRUE.
        """
        return pulumi.get(self, "enable")

    @enable.setter
    def enable(self, value: Optional[pulumi.Input['PacketMirroringEnable']]):
        pulumi.set(self, "enable", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input['PacketMirroringFilterArgs']]:
        """
        Filter for mirrored traffic. If unspecified, all traffic is mirrored.
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input['PacketMirroringFilterArgs']]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter(name="mirroredResources")
    def mirrored_resources(self) -> Optional[pulumi.Input['PacketMirroringMirroredResourceInfoArgs']]:
        """
        PacketMirroring mirroredResourceInfos. MirroredResourceInfo specifies a set of mirrored VM instances, subnetworks and/or tags for which traffic from/to all VM instances will be mirrored.
        """
        return pulumi.get(self, "mirrored_resources")

    @mirrored_resources.setter
    def mirrored_resources(self, value: Optional[pulumi.Input['PacketMirroringMirroredResourceInfoArgs']]):
        pulumi.set(self, "mirrored_resources", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input['PacketMirroringNetworkInfoArgs']]:
        """
        Specifies the mirrored VPC network. Only packets in this network will be mirrored. All mirrored VMs should have a NIC in the given network. All mirrored subnetworks should belong to the given network.
        """
        return pulumi.get(self, "network")

    @network.setter
    def network(self, value: Optional[pulumi.Input['PacketMirroringNetworkInfoArgs']]):
        pulumi.set(self, "network", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        The priority of applying this configuration. Priority is used to break ties in cases where there is more than one matching rule. In the case of two rules that apply for a given Instance, the one with the lowest-numbered priority value wins. Default value is 1000. Valid range is 0 through 65535.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> Optional[pulumi.Input[str]]:
        """
        An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported ( 00000000-0000-0000-0000-000000000000).
        """
        return pulumi.get(self, "request_id")

    @request_id.setter
    def request_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_id", value)


class PacketMirroring(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 collector_ilb: Optional[pulumi.Input[pulumi.InputType['PacketMirroringForwardingRuleInfoArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable: Optional[pulumi.Input['PacketMirroringEnable']] = None,
                 filter: Optional[pulumi.Input[pulumi.InputType['PacketMirroringFilterArgs']]] = None,
                 mirrored_resources: Optional[pulumi.Input[pulumi.InputType['PacketMirroringMirroredResourceInfoArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[pulumi.InputType['PacketMirroringNetworkInfoArgs']]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a PacketMirroring resource in the specified project and region using the data included in the request.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['PacketMirroringForwardingRuleInfoArgs']] collector_ilb: The Forwarding Rule resource of type loadBalancingScheme=INTERNAL that will be used as collector for mirrored traffic. The specified forwarding rule must have isMirroringCollector set to true.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input['PacketMirroringEnable'] enable: Indicates whether or not this packet mirroring takes effect. If set to FALSE, this packet mirroring policy will not be enforced on the network. The default is TRUE.
        :param pulumi.Input[pulumi.InputType['PacketMirroringFilterArgs']] filter: Filter for mirrored traffic. If unspecified, all traffic is mirrored.
        :param pulumi.Input[pulumi.InputType['PacketMirroringMirroredResourceInfoArgs']] mirrored_resources: PacketMirroring mirroredResourceInfos. MirroredResourceInfo specifies a set of mirrored VM instances, subnetworks and/or tags for which traffic from/to all VM instances will be mirrored.
        :param pulumi.Input[str] name: Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[pulumi.InputType['PacketMirroringNetworkInfoArgs']] network: Specifies the mirrored VPC network. Only packets in this network will be mirrored. All mirrored VMs should have a NIC in the given network. All mirrored subnetworks should belong to the given network.
        :param pulumi.Input[int] priority: The priority of applying this configuration. Priority is used to break ties in cases where there is more than one matching rule. In the case of two rules that apply for a given Instance, the one with the lowest-numbered priority value wins. Default value is 1000. Valid range is 0 through 65535.
        :param pulumi.Input[str] request_id: An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported ( 00000000-0000-0000-0000-000000000000).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PacketMirroringArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a PacketMirroring resource in the specified project and region using the data included in the request.

        :param str resource_name: The name of the resource.
        :param PacketMirroringArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PacketMirroringArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 collector_ilb: Optional[pulumi.Input[pulumi.InputType['PacketMirroringForwardingRuleInfoArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable: Optional[pulumi.Input['PacketMirroringEnable']] = None,
                 filter: Optional[pulumi.Input[pulumi.InputType['PacketMirroringFilterArgs']]] = None,
                 mirrored_resources: Optional[pulumi.Input[pulumi.InputType['PacketMirroringMirroredResourceInfoArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[pulumi.InputType['PacketMirroringNetworkInfoArgs']]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PacketMirroringArgs.__new__(PacketMirroringArgs)

            __props__.__dict__["collector_ilb"] = collector_ilb
            __props__.__dict__["description"] = description
            __props__.__dict__["enable"] = enable
            __props__.__dict__["filter"] = filter
            __props__.__dict__["mirrored_resources"] = mirrored_resources
            __props__.__dict__["name"] = name
            __props__.__dict__["network"] = network
            __props__.__dict__["priority"] = priority
            __props__.__dict__["project"] = project
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            __props__.__dict__["request_id"] = request_id
            __props__.__dict__["creation_timestamp"] = None
            __props__.__dict__["kind"] = None
            __props__.__dict__["self_link"] = None
        super(PacketMirroring, __self__).__init__(
            'google-native:compute/beta:PacketMirroring',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PacketMirroring':
        """
        Get an existing PacketMirroring resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PacketMirroringArgs.__new__(PacketMirroringArgs)

        __props__.__dict__["collector_ilb"] = None
        __props__.__dict__["creation_timestamp"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["enable"] = None
        __props__.__dict__["filter"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["mirrored_resources"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network"] = None
        __props__.__dict__["priority"] = None
        __props__.__dict__["region"] = None
        __props__.__dict__["self_link"] = None
        return PacketMirroring(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="collectorIlb")
    def collector_ilb(self) -> pulumi.Output['outputs.PacketMirroringForwardingRuleInfoResponse']:
        """
        The Forwarding Rule resource of type loadBalancingScheme=INTERNAL that will be used as collector for mirrored traffic. The specified forwarding rule must have isMirroringCollector set to true.
        """
        return pulumi.get(self, "collector_ilb")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        An optional description of this resource. Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enable(self) -> pulumi.Output[str]:
        """
        Indicates whether or not this packet mirroring takes effect. If set to FALSE, this packet mirroring policy will not be enforced on the network. The default is TRUE.
        """
        return pulumi.get(self, "enable")

    @property
    @pulumi.getter
    def filter(self) -> pulumi.Output['outputs.PacketMirroringFilterResponse']:
        """
        Filter for mirrored traffic. If unspecified, all traffic is mirrored.
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Type of the resource. Always compute#packetMirroring for packet mirrorings.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="mirroredResources")
    def mirrored_resources(self) -> pulumi.Output['outputs.PacketMirroringMirroredResourceInfoResponse']:
        """
        PacketMirroring mirroredResourceInfos. MirroredResourceInfo specifies a set of mirrored VM instances, subnetworks and/or tags for which traffic from/to all VM instances will be mirrored.
        """
        return pulumi.get(self, "mirrored_resources")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> pulumi.Output['outputs.PacketMirroringNetworkInfoResponse']:
        """
        Specifies the mirrored VPC network. Only packets in this network will be mirrored. All mirrored VMs should have a NIC in the given network. All mirrored subnetworks should belong to the given network.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        """
        The priority of applying this configuration. Priority is used to break ties in cases where there is more than one matching rule. In the case of two rules that apply for a given Instance, the one with the lowest-numbered priority value wins. Default value is 1000. Valid range is 0 through 65535.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        URI of the region where the packetMirroring resides.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

