# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['CertificateArgs', 'Certificate']

@pulumi.input_type
class CertificateArgs:
    def __init__(__self__, *,
                 content: pulumi.Input[str],
                 name: pulumi.Input[str],
                 full_path: Optional[pulumi.Input[str]] = None,
                 partition: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Certificate resource.
        :param pulumi.Input[str] content: Content of certificate on Disk
        :param pulumi.Input[str] name: Name of the SSL Certificate to be Imported on to BIGIP
        :param pulumi.Input[str] full_path: Full Path Name of ssl certificate
        :param pulumi.Input[str] partition: Partition of ssl certificate
        """
        pulumi.set(__self__, "content", content)
        pulumi.set(__self__, "name", name)
        if full_path is not None:
            pulumi.set(__self__, "full_path", full_path)
        if partition is not None:
            pulumi.set(__self__, "partition", partition)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Input[str]:
        """
        Content of certificate on Disk
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: pulumi.Input[str]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the SSL Certificate to be Imported on to BIGIP
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="fullPath")
    def full_path(self) -> Optional[pulumi.Input[str]]:
        """
        Full Path Name of ssl certificate
        """
        return pulumi.get(self, "full_path")

    @full_path.setter
    def full_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "full_path", value)

    @property
    @pulumi.getter
    def partition(self) -> Optional[pulumi.Input[str]]:
        """
        Partition of ssl certificate
        """
        return pulumi.get(self, "partition")

    @partition.setter
    def partition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partition", value)


@pulumi.input_type
class _CertificateState:
    def __init__(__self__, *,
                 content: Optional[pulumi.Input[str]] = None,
                 full_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 partition: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Certificate resources.
        :param pulumi.Input[str] content: Content of certificate on Disk
        :param pulumi.Input[str] full_path: Full Path Name of ssl certificate
        :param pulumi.Input[str] name: Name of the SSL Certificate to be Imported on to BIGIP
        :param pulumi.Input[str] partition: Partition of ssl certificate
        """
        if content is not None:
            pulumi.set(__self__, "content", content)
        if full_path is not None:
            pulumi.set(__self__, "full_path", full_path)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if partition is not None:
            pulumi.set(__self__, "partition", partition)

    @property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[str]]:
        """
        Content of certificate on Disk
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter(name="fullPath")
    def full_path(self) -> Optional[pulumi.Input[str]]:
        """
        Full Path Name of ssl certificate
        """
        return pulumi.get(self, "full_path")

    @full_path.setter
    def full_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "full_path", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the SSL Certificate to be Imported on to BIGIP
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def partition(self) -> Optional[pulumi.Input[str]]:
        """
        Partition of ssl certificate
        """
        return pulumi.get(self, "partition")

    @partition.setter
    def partition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partition", value)


class Certificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 full_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 partition: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        `ssl.Certificate` This resource will import SSL certificates on BIG-IP LTM.
        Certificates can be imported from certificate files on the local disk, in PEM format

        ## Example Usage

        ```python
        import pulumi
        import pulumi_f5bigip as f5bigip

        test_cert = f5bigip.ssl.Certificate("test-cert",
            name="servercert.crt",
            content=(lambda path: open(path).read())("servercert.crt"),
            partition="Common")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] content: Content of certificate on Disk
        :param pulumi.Input[str] full_path: Full Path Name of ssl certificate
        :param pulumi.Input[str] name: Name of the SSL Certificate to be Imported on to BIGIP
        :param pulumi.Input[str] partition: Partition of ssl certificate
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        `ssl.Certificate` This resource will import SSL certificates on BIG-IP LTM.
        Certificates can be imported from certificate files on the local disk, in PEM format

        ## Example Usage

        ```python
        import pulumi
        import pulumi_f5bigip as f5bigip

        test_cert = f5bigip.ssl.Certificate("test-cert",
            name="servercert.crt",
            content=(lambda path: open(path).read())("servercert.crt"),
            partition="Common")
        ```

        :param str resource_name: The name of the resource.
        :param CertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 full_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 partition: Optional[pulumi.Input[str]] = None,
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
            __props__ = CertificateArgs.__new__(CertificateArgs)

            if content is None and not opts.urn:
                raise TypeError("Missing required property 'content'")
            __props__.__dict__["content"] = content
            __props__.__dict__["full_path"] = full_path
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["partition"] = partition
        super(Certificate, __self__).__init__(
            'f5bigip:ssl/certificate:Certificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            content: Optional[pulumi.Input[str]] = None,
            full_path: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            partition: Optional[pulumi.Input[str]] = None) -> 'Certificate':
        """
        Get an existing Certificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] content: Content of certificate on Disk
        :param pulumi.Input[str] full_path: Full Path Name of ssl certificate
        :param pulumi.Input[str] name: Name of the SSL Certificate to be Imported on to BIGIP
        :param pulumi.Input[str] partition: Partition of ssl certificate
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CertificateState.__new__(_CertificateState)

        __props__.__dict__["content"] = content
        __props__.__dict__["full_path"] = full_path
        __props__.__dict__["name"] = name
        __props__.__dict__["partition"] = partition
        return Certificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output[str]:
        """
        Content of certificate on Disk
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="fullPath")
    def full_path(self) -> pulumi.Output[str]:
        """
        Full Path Name of ssl certificate
        """
        return pulumi.get(self, "full_path")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the SSL Certificate to be Imported on to BIGIP
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def partition(self) -> pulumi.Output[Optional[str]]:
        """
        Partition of ssl certificate
        """
        return pulumi.get(self, "partition")

