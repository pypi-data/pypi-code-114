# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['RandomIdArgs', 'RandomId']

@pulumi.input_type
class RandomIdArgs:
    def __init__(__self__, *,
                 byte_length: pulumi.Input[int],
                 keepers: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 prefix: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RandomId resource.
        :param pulumi.Input[int] byte_length: The number of random bytes to produce. The minimum value is 1, which produces eight bits of randomness.
        :param pulumi.Input[Mapping[str, Any]] keepers: Arbitrary map of values that, when changed, will trigger recreation of resource. See [the main provider
               documentation](../index.html) for more information.
        :param pulumi.Input[str] prefix: Arbitrary string to prefix the output value with. This string is supplied as-is, meaning it is not guaranteed to be
               URL-safe or base64 encoded.
        """
        pulumi.set(__self__, "byte_length", byte_length)
        if keepers is not None:
            pulumi.set(__self__, "keepers", keepers)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)

    @property
    @pulumi.getter(name="byteLength")
    def byte_length(self) -> pulumi.Input[int]:
        """
        The number of random bytes to produce. The minimum value is 1, which produces eight bits of randomness.
        """
        return pulumi.get(self, "byte_length")

    @byte_length.setter
    def byte_length(self, value: pulumi.Input[int]):
        pulumi.set(self, "byte_length", value)

    @property
    @pulumi.getter
    def keepers(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Arbitrary map of values that, when changed, will trigger recreation of resource. See [the main provider
        documentation](../index.html) for more information.
        """
        return pulumi.get(self, "keepers")

    @keepers.setter
    def keepers(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "keepers", value)

    @property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Arbitrary string to prefix the output value with. This string is supplied as-is, meaning it is not guaranteed to be
        URL-safe or base64 encoded.
        """
        return pulumi.get(self, "prefix")

    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prefix", value)


@pulumi.input_type
class _RandomIdState:
    def __init__(__self__, *,
                 b64_std: Optional[pulumi.Input[str]] = None,
                 b64_url: Optional[pulumi.Input[str]] = None,
                 byte_length: Optional[pulumi.Input[int]] = None,
                 dec: Optional[pulumi.Input[str]] = None,
                 hex: Optional[pulumi.Input[str]] = None,
                 keepers: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 prefix: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering RandomId resources.
        :param pulumi.Input[str] b64_std: The generated id presented in base64 without additional transformations.
        :param pulumi.Input[str] b64_url: The generated id presented in base64, using the URL-friendly character set: case-sensitive letters, digits and the
               characters `_` and `-`.
        :param pulumi.Input[int] byte_length: The number of random bytes to produce. The minimum value is 1, which produces eight bits of randomness.
        :param pulumi.Input[str] dec: The generated id presented in non-padded decimal digits.
        :param pulumi.Input[str] hex: The generated id presented in padded hexadecimal digits. This result will always be twice as long as the requested byte
               length.
        :param pulumi.Input[Mapping[str, Any]] keepers: Arbitrary map of values that, when changed, will trigger recreation of resource. See [the main provider
               documentation](../index.html) for more information.
        :param pulumi.Input[str] prefix: Arbitrary string to prefix the output value with. This string is supplied as-is, meaning it is not guaranteed to be
               URL-safe or base64 encoded.
        """
        if b64_std is not None:
            pulumi.set(__self__, "b64_std", b64_std)
        if b64_url is not None:
            pulumi.set(__self__, "b64_url", b64_url)
        if byte_length is not None:
            pulumi.set(__self__, "byte_length", byte_length)
        if dec is not None:
            pulumi.set(__self__, "dec", dec)
        if hex is not None:
            pulumi.set(__self__, "hex", hex)
        if keepers is not None:
            pulumi.set(__self__, "keepers", keepers)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)

    @property
    @pulumi.getter(name="b64Std")
    def b64_std(self) -> Optional[pulumi.Input[str]]:
        """
        The generated id presented in base64 without additional transformations.
        """
        return pulumi.get(self, "b64_std")

    @b64_std.setter
    def b64_std(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "b64_std", value)

    @property
    @pulumi.getter(name="b64Url")
    def b64_url(self) -> Optional[pulumi.Input[str]]:
        """
        The generated id presented in base64, using the URL-friendly character set: case-sensitive letters, digits and the
        characters `_` and `-`.
        """
        return pulumi.get(self, "b64_url")

    @b64_url.setter
    def b64_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "b64_url", value)

    @property
    @pulumi.getter(name="byteLength")
    def byte_length(self) -> Optional[pulumi.Input[int]]:
        """
        The number of random bytes to produce. The minimum value is 1, which produces eight bits of randomness.
        """
        return pulumi.get(self, "byte_length")

    @byte_length.setter
    def byte_length(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "byte_length", value)

    @property
    @pulumi.getter
    def dec(self) -> Optional[pulumi.Input[str]]:
        """
        The generated id presented in non-padded decimal digits.
        """
        return pulumi.get(self, "dec")

    @dec.setter
    def dec(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dec", value)

    @property
    @pulumi.getter
    def hex(self) -> Optional[pulumi.Input[str]]:
        """
        The generated id presented in padded hexadecimal digits. This result will always be twice as long as the requested byte
        length.
        """
        return pulumi.get(self, "hex")

    @hex.setter
    def hex(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hex", value)

    @property
    @pulumi.getter
    def keepers(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Arbitrary map of values that, when changed, will trigger recreation of resource. See [the main provider
        documentation](../index.html) for more information.
        """
        return pulumi.get(self, "keepers")

    @keepers.setter
    def keepers(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "keepers", value)

    @property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Arbitrary string to prefix the output value with. This string is supplied as-is, meaning it is not guaranteed to be
        URL-safe or base64 encoded.
        """
        return pulumi.get(self, "prefix")

    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prefix", value)


class RandomId(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 byte_length: Optional[pulumi.Input[int]] = None,
                 keepers: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 prefix: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The resource `RandomId` generates random numbers that are intended to be
        used as unique identifiers for other resources.

        This resource *does* use a cryptographic random number generator in order
        to minimize the chance of collisions, making the results of this resource
        when a 16-byte identifier is requested of equivalent uniqueness to a
        type-4 UUID.

        This resource can be used in conjunction with resources that have
        the `create_before_destroy` lifecycle flag set to avoid conflicts with
        unique names during the brief period where both the old and new resources
        exist concurrently.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_random as random

        # The following example shows how to generate a unique name for an AWS EC2
        # instance that changes each time a new AMI id is selected.
        server_random_id = random.RandomId("serverRandomId",
            keepers={
                "ami_id": var["ami_id"],
            },
            byte_length=8)
        server_instance = aws.ec2.Instance("serverInstance",
            tags={
                "Name": server_random_id.hex.apply(lambda hex: f"web-server {hex}"),
            },
            ami=server_random_id.keepers["amiId"])
        # ... (other aws_instance arguments) ...
        ```

        ## Import

        # Random IDs can be imported using the b64_url with an optional prefix. This # can be used to replace a config value with a value interpolated from the # random provider without experiencing diffs. # Example with no prefix

        ```sh
         $ pulumi import random:index/randomId:RandomId server p-9hUg
        ```

        # Example with prefix (prefix is separated by a ,)

        ```sh
         $ pulumi import random:index/randomId:RandomId server my-prefix-,p-9hUg
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] byte_length: The number of random bytes to produce. The minimum value is 1, which produces eight bits of randomness.
        :param pulumi.Input[Mapping[str, Any]] keepers: Arbitrary map of values that, when changed, will trigger recreation of resource. See [the main provider
               documentation](../index.html) for more information.
        :param pulumi.Input[str] prefix: Arbitrary string to prefix the output value with. This string is supplied as-is, meaning it is not guaranteed to be
               URL-safe or base64 encoded.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RandomIdArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The resource `RandomId` generates random numbers that are intended to be
        used as unique identifiers for other resources.

        This resource *does* use a cryptographic random number generator in order
        to minimize the chance of collisions, making the results of this resource
        when a 16-byte identifier is requested of equivalent uniqueness to a
        type-4 UUID.

        This resource can be used in conjunction with resources that have
        the `create_before_destroy` lifecycle flag set to avoid conflicts with
        unique names during the brief period where both the old and new resources
        exist concurrently.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_random as random

        # The following example shows how to generate a unique name for an AWS EC2
        # instance that changes each time a new AMI id is selected.
        server_random_id = random.RandomId("serverRandomId",
            keepers={
                "ami_id": var["ami_id"],
            },
            byte_length=8)
        server_instance = aws.ec2.Instance("serverInstance",
            tags={
                "Name": server_random_id.hex.apply(lambda hex: f"web-server {hex}"),
            },
            ami=server_random_id.keepers["amiId"])
        # ... (other aws_instance arguments) ...
        ```

        ## Import

        # Random IDs can be imported using the b64_url with an optional prefix. This # can be used to replace a config value with a value interpolated from the # random provider without experiencing diffs. # Example with no prefix

        ```sh
         $ pulumi import random:index/randomId:RandomId server p-9hUg
        ```

        # Example with prefix (prefix is separated by a ,)

        ```sh
         $ pulumi import random:index/randomId:RandomId server my-prefix-,p-9hUg
        ```

        :param str resource_name: The name of the resource.
        :param RandomIdArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RandomIdArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 byte_length: Optional[pulumi.Input[int]] = None,
                 keepers: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 prefix: Optional[pulumi.Input[str]] = None,
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
            __props__ = RandomIdArgs.__new__(RandomIdArgs)

            if byte_length is None and not opts.urn:
                raise TypeError("Missing required property 'byte_length'")
            __props__.__dict__["byte_length"] = byte_length
            __props__.__dict__["keepers"] = keepers
            __props__.__dict__["prefix"] = prefix
            __props__.__dict__["b64_std"] = None
            __props__.__dict__["b64_url"] = None
            __props__.__dict__["dec"] = None
            __props__.__dict__["hex"] = None
        super(RandomId, __self__).__init__(
            'random:index/randomId:RandomId',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            b64_std: Optional[pulumi.Input[str]] = None,
            b64_url: Optional[pulumi.Input[str]] = None,
            byte_length: Optional[pulumi.Input[int]] = None,
            dec: Optional[pulumi.Input[str]] = None,
            hex: Optional[pulumi.Input[str]] = None,
            keepers: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            prefix: Optional[pulumi.Input[str]] = None) -> 'RandomId':
        """
        Get an existing RandomId resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] b64_std: The generated id presented in base64 without additional transformations.
        :param pulumi.Input[str] b64_url: The generated id presented in base64, using the URL-friendly character set: case-sensitive letters, digits and the
               characters `_` and `-`.
        :param pulumi.Input[int] byte_length: The number of random bytes to produce. The minimum value is 1, which produces eight bits of randomness.
        :param pulumi.Input[str] dec: The generated id presented in non-padded decimal digits.
        :param pulumi.Input[str] hex: The generated id presented in padded hexadecimal digits. This result will always be twice as long as the requested byte
               length.
        :param pulumi.Input[Mapping[str, Any]] keepers: Arbitrary map of values that, when changed, will trigger recreation of resource. See [the main provider
               documentation](../index.html) for more information.
        :param pulumi.Input[str] prefix: Arbitrary string to prefix the output value with. This string is supplied as-is, meaning it is not guaranteed to be
               URL-safe or base64 encoded.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RandomIdState.__new__(_RandomIdState)

        __props__.__dict__["b64_std"] = b64_std
        __props__.__dict__["b64_url"] = b64_url
        __props__.__dict__["byte_length"] = byte_length
        __props__.__dict__["dec"] = dec
        __props__.__dict__["hex"] = hex
        __props__.__dict__["keepers"] = keepers
        __props__.__dict__["prefix"] = prefix
        return RandomId(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="b64Std")
    def b64_std(self) -> pulumi.Output[str]:
        """
        The generated id presented in base64 without additional transformations.
        """
        return pulumi.get(self, "b64_std")

    @property
    @pulumi.getter(name="b64Url")
    def b64_url(self) -> pulumi.Output[str]:
        """
        The generated id presented in base64, using the URL-friendly character set: case-sensitive letters, digits and the
        characters `_` and `-`.
        """
        return pulumi.get(self, "b64_url")

    @property
    @pulumi.getter(name="byteLength")
    def byte_length(self) -> pulumi.Output[int]:
        """
        The number of random bytes to produce. The minimum value is 1, which produces eight bits of randomness.
        """
        return pulumi.get(self, "byte_length")

    @property
    @pulumi.getter
    def dec(self) -> pulumi.Output[str]:
        """
        The generated id presented in non-padded decimal digits.
        """
        return pulumi.get(self, "dec")

    @property
    @pulumi.getter
    def hex(self) -> pulumi.Output[str]:
        """
        The generated id presented in padded hexadecimal digits. This result will always be twice as long as the requested byte
        length.
        """
        return pulumi.get(self, "hex")

    @property
    @pulumi.getter
    def keepers(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Arbitrary map of values that, when changed, will trigger recreation of resource. See [the main provider
        documentation](../index.html) for more information.
        """
        return pulumi.get(self, "keepers")

    @property
    @pulumi.getter
    def prefix(self) -> pulumi.Output[Optional[str]]:
        """
        Arbitrary string to prefix the output value with. This string is supplied as-is, meaning it is not guaranteed to be
        URL-safe or base64 encoded.
        """
        return pulumi.get(self, "prefix")

