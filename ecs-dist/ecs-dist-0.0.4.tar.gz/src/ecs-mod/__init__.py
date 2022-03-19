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


class MyEcsConstruct(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="ecs-package.MyEcsConstruct",
):
    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        docker_dir_asset: builtins.str,
        cpu: typing.Optional[jsii.Number] = None,
        desired_count: typing.Optional[jsii.Number] = None,
        docker_file_asset: typing.Optional[builtins.str] = None,
        max_azs: typing.Optional[jsii.Number] = None,
        memory_limit_mib: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param docker_dir_asset: 
        :param cpu: 
        :param desired_count: 
        :param docker_file_asset: 
        :param max_azs: 
        :param memory_limit_mib: 
        '''
        props = MyEcsProps(
            docker_dir_asset=docker_dir_asset,
            cpu=cpu,
            desired_count=desired_count,
            docker_file_asset=docker_file_asset,
            max_azs=max_azs,
            memory_limit_mib=memory_limit_mib,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="ecs-package.MyEcsProps",
    jsii_struct_bases=[],
    name_mapping={
        "docker_dir_asset": "dockerDirAsset",
        "cpu": "cpu",
        "desired_count": "desiredCount",
        "docker_file_asset": "dockerFileAsset",
        "max_azs": "maxAzs",
        "memory_limit_mib": "memoryLimitMiB",
    },
)
class MyEcsProps:
    def __init__(
        self,
        *,
        docker_dir_asset: builtins.str,
        cpu: typing.Optional[jsii.Number] = None,
        desired_count: typing.Optional[jsii.Number] = None,
        docker_file_asset: typing.Optional[builtins.str] = None,
        max_azs: typing.Optional[jsii.Number] = None,
        memory_limit_mib: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param docker_dir_asset: 
        :param cpu: 
        :param desired_count: 
        :param docker_file_asset: 
        :param max_azs: 
        :param memory_limit_mib: 
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "docker_dir_asset": docker_dir_asset,
        }
        if cpu is not None:
            self._values["cpu"] = cpu
        if desired_count is not None:
            self._values["desired_count"] = desired_count
        if docker_file_asset is not None:
            self._values["docker_file_asset"] = docker_file_asset
        if max_azs is not None:
            self._values["max_azs"] = max_azs
        if memory_limit_mib is not None:
            self._values["memory_limit_mib"] = memory_limit_mib

    @builtins.property
    def docker_dir_asset(self) -> builtins.str:
        result = self._values.get("docker_dir_asset")
        assert result is not None, "Required property 'docker_dir_asset' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cpu(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def desired_count(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("desired_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def docker_file_asset(self) -> typing.Optional[builtins.str]:
        result = self._values.get("docker_file_asset")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_azs(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("max_azs")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_limit_mib(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("memory_limit_mib")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MyEcsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "MyEcsConstruct",
    "MyEcsProps",
]

publication.publish()
