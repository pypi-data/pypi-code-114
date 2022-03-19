'''
#### Part1 ([CDK Construct Library](https://github.com/AymanZahran/projen-cdk-tutorial-part-1))

[![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)
[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/AymanZahran/projen-cdk-tutorial-part-1)
[![build](https://github.com/AymanZahran/projen-cdk-tutorial-part-1/actions/workflows/build.yml/badge.svg)](https://github.com/AymanZahran/projen-cdk-tutorial-part-1/actions/workflows/build.yml)
[![release](https://github.com/AymanZahran/projen-cdk-tutorial-part-1/actions/workflows/release.yml/badge.svg)](https://github.com/AymanZahran/projen-cdk-tutorial-part-1/actions/workflows/release.yml)
[![docker](https://img.shields.io/badge/docker-jsii%2Fsuperchain-brightgreen?logo=docker)](https://hub.docker.com/r/jsii/superchain)

#### Part2 ([CDK App](https://github.com/AymanZahran/projen-cdk-tutorial-part-2))

[![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)
[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/AymanZahran/projen-cdk-tutorial-part-2)

#### Part3 ([CDK Pipelines App](https://github.com/AymanZahran/projen-cdk-tutorial-part-3))

[![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)
[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/AymanZahran/projen-cdk-tutorial-part-3)

## Part 1
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import constructs


@jsii.interface(jsii_type="ecs-package.IMyEcsProps")
class IMyEcsProps(typing_extensions.Protocol):
    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cpu")
    def cpu(self) -> jsii.Number:
        ...

    @cpu.setter
    def cpu(self, value: jsii.Number) -> None:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="desiredCount")
    def desired_count(self) -> jsii.Number:
        ...

    @desired_count.setter
    def desired_count(self, value: jsii.Number) -> None:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dockerDirAsset")
    def docker_dir_asset(self) -> builtins.str:
        ...

    @docker_dir_asset.setter
    def docker_dir_asset(self, value: builtins.str) -> None:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dockerFileAsset")
    def docker_file_asset(self) -> builtins.str:
        ...

    @docker_file_asset.setter
    def docker_file_asset(self, value: builtins.str) -> None:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxAzs")
    def max_azs(self) -> jsii.Number:
        ...

    @max_azs.setter
    def max_azs(self, value: jsii.Number) -> None:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="memoryLimitMiB")
    def memory_limit_mib(self) -> jsii.Number:
        ...

    @memory_limit_mib.setter
    def memory_limit_mib(self, value: jsii.Number) -> None:
        ...


class _IMyEcsPropsProxy:
    __jsii_type__: typing.ClassVar[str] = "ecs-package.IMyEcsProps"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cpu")
    def cpu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpu"))

    @cpu.setter
    def cpu(self, value: jsii.Number) -> None:
        jsii.set(self, "cpu", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="desiredCount")
    def desired_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "desiredCount"))

    @desired_count.setter
    def desired_count(self, value: jsii.Number) -> None:
        jsii.set(self, "desiredCount", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dockerDirAsset")
    def docker_dir_asset(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dockerDirAsset"))

    @docker_dir_asset.setter
    def docker_dir_asset(self, value: builtins.str) -> None:
        jsii.set(self, "dockerDirAsset", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dockerFileAsset")
    def docker_file_asset(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dockerFileAsset"))

    @docker_file_asset.setter
    def docker_file_asset(self, value: builtins.str) -> None:
        jsii.set(self, "dockerFileAsset", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxAzs")
    def max_azs(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAzs"))

    @max_azs.setter
    def max_azs(self, value: jsii.Number) -> None:
        jsii.set(self, "maxAzs", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="memoryLimitMiB")
    def memory_limit_mib(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryLimitMiB"))

    @memory_limit_mib.setter
    def memory_limit_mib(self, value: jsii.Number) -> None:
        jsii.set(self, "memoryLimitMiB", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMyEcsProps).__jsii_proxy_class__ = lambda : _IMyEcsPropsProxy


class MyEcsConstruct(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="ecs-package.MyEcsConstruct",
):
    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        props: IMyEcsProps,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param props: -
        '''
        jsii.create(self.__class__, self, [scope, id, props])


__all__ = [
    "IMyEcsProps",
    "MyEcsConstruct",
]

publication.publish()
