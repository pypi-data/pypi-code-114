# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['FeatureArgs', 'Feature']

@pulumi.input_type
class FeatureArgs:
    def __init__(__self__, *,
                 membership_id: pulumi.Input[str],
                 feature_config_ref: Optional[pulumi.Input['FeatureConfigRefArgs']] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 resource_state: Optional[pulumi.Input['ResourceStateArgs']] = None):
        """
        The set of arguments for constructing a Feature resource.
        :param pulumi.Input['FeatureConfigRefArgs'] feature_config_ref: Reference information for a FeatureConfig applied on the MembershipFeature.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: GCP labels for this MembershipFeature.
        :param pulumi.Input[str] request_id: Idempotent request UUID.
        :param pulumi.Input['ResourceStateArgs'] resource_state: Lifecycle information of the resource itself.
        """
        pulumi.set(__self__, "membership_id", membership_id)
        if feature_config_ref is not None:
            pulumi.set(__self__, "feature_config_ref", feature_config_ref)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)
        if resource_state is not None:
            pulumi.set(__self__, "resource_state", resource_state)

    @property
    @pulumi.getter(name="membershipId")
    def membership_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "membership_id")

    @membership_id.setter
    def membership_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "membership_id", value)

    @property
    @pulumi.getter(name="featureConfigRef")
    def feature_config_ref(self) -> Optional[pulumi.Input['FeatureConfigRefArgs']]:
        """
        Reference information for a FeatureConfig applied on the MembershipFeature.
        """
        return pulumi.get(self, "feature_config_ref")

    @feature_config_ref.setter
    def feature_config_ref(self, value: Optional[pulumi.Input['FeatureConfigRefArgs']]):
        pulumi.set(self, "feature_config_ref", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        GCP labels for this MembershipFeature.
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
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> Optional[pulumi.Input[str]]:
        """
        Idempotent request UUID.
        """
        return pulumi.get(self, "request_id")

    @request_id.setter
    def request_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_id", value)

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> Optional[pulumi.Input['ResourceStateArgs']]:
        """
        Lifecycle information of the resource itself.
        """
        return pulumi.get(self, "resource_state")

    @resource_state.setter
    def resource_state(self, value: Optional[pulumi.Input['ResourceStateArgs']]):
        pulumi.set(self, "resource_state", value)


class Feature(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 feature_config_ref: Optional[pulumi.Input[pulumi.InputType['FeatureConfigRefArgs']]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 membership_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 resource_state: Optional[pulumi.Input[pulumi.InputType['ResourceStateArgs']]] = None,
                 __props__=None):
        """
        Creates membershipFeature under a given parent.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['FeatureConfigRefArgs']] feature_config_ref: Reference information for a FeatureConfig applied on the MembershipFeature.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: GCP labels for this MembershipFeature.
        :param pulumi.Input[str] request_id: Idempotent request UUID.
        :param pulumi.Input[pulumi.InputType['ResourceStateArgs']] resource_state: Lifecycle information of the resource itself.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FeatureArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates membershipFeature under a given parent.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param FeatureArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FeatureArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 feature_config_ref: Optional[pulumi.Input[pulumi.InputType['FeatureConfigRefArgs']]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 membership_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 resource_state: Optional[pulumi.Input[pulumi.InputType['ResourceStateArgs']]] = None,
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
            __props__ = FeatureArgs.__new__(FeatureArgs)

            __props__.__dict__["feature_config_ref"] = feature_config_ref
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            if membership_id is None and not opts.urn:
                raise TypeError("Missing required property 'membership_id'")
            __props__.__dict__["membership_id"] = membership_id
            __props__.__dict__["project"] = project
            __props__.__dict__["request_id"] = request_id
            __props__.__dict__["resource_state"] = resource_state
            __props__.__dict__["create_time"] = None
            __props__.__dict__["delete_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["spec"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["update_time"] = None
        super(Feature, __self__).__init__(
            'google-native:gkehub/v2alpha:Feature',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Feature':
        """
        Get an existing Feature resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FeatureArgs.__new__(FeatureArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["delete_time"] = None
        __props__.__dict__["feature_config_ref"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["resource_state"] = None
        __props__.__dict__["spec"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["update_time"] = None
        return Feature(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        When the MembershipFeature resource was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[str]:
        """
        When the MembershipFeature resource was deleted.
        """
        return pulumi.get(self, "delete_time")

    @property
    @pulumi.getter(name="featureConfigRef")
    def feature_config_ref(self) -> pulumi.Output['outputs.FeatureConfigRefResponse']:
        """
        Reference information for a FeatureConfig applied on the MembershipFeature.
        """
        return pulumi.get(self, "feature_config_ref")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        GCP labels for this MembershipFeature.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the membershipFeature, in the format: `projects/{project}/locations/{location}/memberships/{membership}/features/{feature}`. Note that `membershipFeatures` is shortened to `features` in the resource name. (see http://go/aip/122#collection-identifiers)
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output['outputs.ResourceStateResponse']:
        """
        Lifecycle information of the resource itself.
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Output['outputs.FeatureSpecResponse']:
        """
        Spec of this membershipFeature.
        """
        return pulumi.get(self, "spec")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output['outputs.FeatureStateResponse']:
        """
        State of the this membershipFeature.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        When the MembershipFeature resource was last updated.
        """
        return pulumi.get(self, "update_time")

