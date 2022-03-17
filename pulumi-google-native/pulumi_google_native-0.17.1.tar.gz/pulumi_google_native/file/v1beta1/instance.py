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

__all__ = ['InstanceArgs', 'Instance']

@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *,
                 instance_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 file_shares: Optional[pulumi.Input[Sequence[pulumi.Input['FileShareConfigArgs']]]] = None,
                 kms_key_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 networks: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkConfigArgs']]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 tier: Optional[pulumi.Input['InstanceTier']] = None):
        """
        The set of arguments for constructing a Instance resource.
        :param pulumi.Input[str] instance_id: Required. The ID of the instance to create. The ID must be unique within the specified project and location. This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens, and cannot end with a hyphen.
        :param pulumi.Input[str] description: The description of the instance (2048 characters or less).
        :param pulumi.Input[str] etag: Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other.
        :param pulumi.Input[Sequence[pulumi.Input['FileShareConfigArgs']]] file_shares: File system shares on the instance. For this version, only a single file share is supported.
        :param pulumi.Input[str] kms_key_name: KMS key name used for data encryption.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Resource labels to represent user provided metadata.
        :param pulumi.Input[Sequence[pulumi.Input['NetworkConfigArgs']]] networks: VPC networks to which the instance is connected. For this version, only a single network is supported.
        :param pulumi.Input['InstanceTier'] tier: The service tier of the instance.
        """
        pulumi.set(__self__, "instance_id", instance_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if file_shares is not None:
            pulumi.set(__self__, "file_shares", file_shares)
        if kms_key_name is not None:
            pulumi.set(__self__, "kms_key_name", kms_key_name)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if networks is not None:
            pulumi.set(__self__, "networks", networks)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[str]:
        """
        Required. The ID of the instance to create. The ID must be unique within the specified project and location. This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens, and cannot end with a hyphen.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the instance (2048 characters or less).
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter(name="fileShares")
    def file_shares(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FileShareConfigArgs']]]]:
        """
        File system shares on the instance. For this version, only a single file share is supported.
        """
        return pulumi.get(self, "file_shares")

    @file_shares.setter
    def file_shares(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FileShareConfigArgs']]]]):
        pulumi.set(self, "file_shares", value)

    @property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[str]]:
        """
        KMS key name used for data encryption.
        """
        return pulumi.get(self, "kms_key_name")

    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_name", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource labels to represent user provided metadata.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkConfigArgs']]]]:
        """
        VPC networks to which the instance is connected. For this version, only a single network is supported.
        """
        return pulumi.get(self, "networks")

    @networks.setter
    def networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkConfigArgs']]]]):
        pulumi.set(self, "networks", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input['InstanceTier']]:
        """
        The service tier of the instance.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input['InstanceTier']]):
        pulumi.set(self, "tier", value)


class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 file_shares: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FileShareConfigArgs']]]]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 kms_key_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 networks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkConfigArgs']]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 tier: Optional[pulumi.Input['InstanceTier']] = None,
                 __props__=None):
        """
        Creates an instance. When creating from a backup, the capacity of the new instance needs to be equal to or larger than the capacity of the backup (and also equal to or larger than the minimum capacity of the tier).
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the instance (2048 characters or less).
        :param pulumi.Input[str] etag: Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FileShareConfigArgs']]]] file_shares: File system shares on the instance. For this version, only a single file share is supported.
        :param pulumi.Input[str] instance_id: Required. The ID of the instance to create. The ID must be unique within the specified project and location. This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens, and cannot end with a hyphen.
        :param pulumi.Input[str] kms_key_name: KMS key name used for data encryption.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Resource labels to represent user provided metadata.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkConfigArgs']]]] networks: VPC networks to which the instance is connected. For this version, only a single network is supported.
        :param pulumi.Input['InstanceTier'] tier: The service tier of the instance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an instance. When creating from a backup, the capacity of the new instance needs to be equal to or larger than the capacity of the backup (and also equal to or larger than the minimum capacity of the tier).
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param InstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 file_shares: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FileShareConfigArgs']]]]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 kms_key_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 networks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkConfigArgs']]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 tier: Optional[pulumi.Input['InstanceTier']] = None,
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
            __props__ = InstanceArgs.__new__(InstanceArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["etag"] = etag
            __props__.__dict__["file_shares"] = file_shares
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            __props__.__dict__["kms_key_name"] = kms_key_name
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["networks"] = networks
            __props__.__dict__["project"] = project
            __props__.__dict__["tier"] = tier
            __props__.__dict__["create_time"] = None
            __props__.__dict__["max_share_count"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["satisfies_pzs"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["status_message"] = None
            __props__.__dict__["suspension_reasons"] = None
        super(Instance, __self__).__init__(
            'google-native:file/v1beta1:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Instance':
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InstanceArgs.__new__(InstanceArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["file_shares"] = None
        __props__.__dict__["kms_key_name"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["max_share_count"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["networks"] = None
        __props__.__dict__["satisfies_pzs"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["status_message"] = None
        __props__.__dict__["suspension_reasons"] = None
        __props__.__dict__["tier"] = None
        return Instance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time when the instance was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the instance (2048 characters or less).
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="fileShares")
    def file_shares(self) -> pulumi.Output[Sequence['outputs.FileShareConfigResponse']]:
        """
        File system shares on the instance. For this version, only a single file share is supported.
        """
        return pulumi.get(self, "file_shares")

    @property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Output[str]:
        """
        KMS key name used for data encryption.
        """
        return pulumi.get(self, "kms_key_name")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Resource labels to represent user provided metadata.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="maxShareCount")
    def max_share_count(self) -> pulumi.Output[str]:
        """
        The max number of shares allowed.
        """
        return pulumi.get(self, "max_share_count")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the instance, in the format `projects/{project_id}/locations/{location_id}/instances/{instance_id}`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def networks(self) -> pulumi.Output[Sequence['outputs.NetworkConfigResponse']]:
        """
        VPC networks to which the instance is connected. For this version, only a single network is supported.
        """
        return pulumi.get(self, "networks")

    @property
    @pulumi.getter(name="satisfiesPzs")
    def satisfies_pzs(self) -> pulumi.Output[bool]:
        """
        Reserved for future use.
        """
        return pulumi.get(self, "satisfies_pzs")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The instance state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Output[str]:
        """
        Additional information about the instance state, if available.
        """
        return pulumi.get(self, "status_message")

    @property
    @pulumi.getter(name="suspensionReasons")
    def suspension_reasons(self) -> pulumi.Output[Sequence[str]]:
        """
        field indicates all the reasons the instance is in "SUSPENDED" state.
        """
        return pulumi.get(self, "suspension_reasons")

    @property
    @pulumi.getter
    def tier(self) -> pulumi.Output[str]:
        """
        The service tier of the instance.
        """
        return pulumi.get(self, "tier")

