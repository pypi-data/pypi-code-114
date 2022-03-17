# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['HistoryArgs', 'History']

@pulumi.input_type
class HistoryArgs:
    def __init__(__self__, *,
                 display_name: Optional[pulumi.Input[str]] = None,
                 history_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 test_platform: Optional[pulumi.Input['HistoryTestPlatform']] = None):
        """
        The set of arguments for constructing a History resource.
        :param pulumi.Input[str] display_name: A short human-readable (plain text) name to display in the UI. Maximum of 100 characters. - In response: present if set during create. - In create request: optional
        :param pulumi.Input[str] history_id: A unique identifier within a project for this History. Returns INVALID_ARGUMENT if this field is set or overwritten by the caller. - In response always set - In create request: never set
        :param pulumi.Input[str] name: A name to uniquely identify a history within a project. Maximum of 200 characters. - In response always set - In create request: always set
        :param pulumi.Input[str] request_id: A unique request ID for server to detect duplicated requests. For example, a UUID. Optional, but strongly recommended.
        :param pulumi.Input['HistoryTestPlatform'] test_platform: The platform of the test history. - In response: always set. Returns the platform of the last execution if unknown.
        """
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if history_id is not None:
            pulumi.set(__self__, "history_id", history_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)
        if test_platform is not None:
            pulumi.set(__self__, "test_platform", test_platform)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        A short human-readable (plain text) name to display in the UI. Maximum of 100 characters. - In response: present if set during create. - In create request: optional
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="historyId")
    def history_id(self) -> Optional[pulumi.Input[str]]:
        """
        A unique identifier within a project for this History. Returns INVALID_ARGUMENT if this field is set or overwritten by the caller. - In response always set - In create request: never set
        """
        return pulumi.get(self, "history_id")

    @history_id.setter
    def history_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "history_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A name to uniquely identify a history within a project. Maximum of 200 characters. - In response always set - In create request: always set
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

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
        A unique request ID for server to detect duplicated requests. For example, a UUID. Optional, but strongly recommended.
        """
        return pulumi.get(self, "request_id")

    @request_id.setter
    def request_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_id", value)

    @property
    @pulumi.getter(name="testPlatform")
    def test_platform(self) -> Optional[pulumi.Input['HistoryTestPlatform']]:
        """
        The platform of the test history. - In response: always set. Returns the platform of the last execution if unknown.
        """
        return pulumi.get(self, "test_platform")

    @test_platform.setter
    def test_platform(self, value: Optional[pulumi.Input['HistoryTestPlatform']]):
        pulumi.set(self, "test_platform", value)


class History(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 history_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 test_platform: Optional[pulumi.Input['HistoryTestPlatform']] = None,
                 __props__=None):
        """
        Creates a History. The returned History will have the id set. May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to write to project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the containing project does not exist
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: A short human-readable (plain text) name to display in the UI. Maximum of 100 characters. - In response: present if set during create. - In create request: optional
        :param pulumi.Input[str] history_id: A unique identifier within a project for this History. Returns INVALID_ARGUMENT if this field is set or overwritten by the caller. - In response always set - In create request: never set
        :param pulumi.Input[str] name: A name to uniquely identify a history within a project. Maximum of 200 characters. - In response always set - In create request: always set
        :param pulumi.Input[str] request_id: A unique request ID for server to detect duplicated requests. For example, a UUID. Optional, but strongly recommended.
        :param pulumi.Input['HistoryTestPlatform'] test_platform: The platform of the test history. - In response: always set. Returns the platform of the last execution if unknown.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[HistoryArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a History. The returned History will have the id set. May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to write to project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the containing project does not exist
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param HistoryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HistoryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 history_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 test_platform: Optional[pulumi.Input['HistoryTestPlatform']] = None,
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
            __props__ = HistoryArgs.__new__(HistoryArgs)

            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["history_id"] = history_id
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["request_id"] = request_id
            __props__.__dict__["test_platform"] = test_platform
        super(History, __self__).__init__(
            'google-native:toolresults/v1beta3:History',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'History':
        """
        Get an existing History resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = HistoryArgs.__new__(HistoryArgs)

        __props__.__dict__["display_name"] = None
        __props__.__dict__["history_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["test_platform"] = None
        return History(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        A short human-readable (plain text) name to display in the UI. Maximum of 100 characters. - In response: present if set during create. - In create request: optional
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="historyId")
    def history_id(self) -> pulumi.Output[str]:
        """
        A unique identifier within a project for this History. Returns INVALID_ARGUMENT if this field is set or overwritten by the caller. - In response always set - In create request: never set
        """
        return pulumi.get(self, "history_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A name to uniquely identify a history within a project. Maximum of 200 characters. - In response always set - In create request: always set
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="testPlatform")
    def test_platform(self) -> pulumi.Output[str]:
        """
        The platform of the test history. - In response: always set. Returns the platform of the last execution if unknown.
        """
        return pulumi.get(self, "test_platform")

