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
        cpu: jsii.Number,
        desired_count: jsii.Number,
        docker_dir_asset: builtins.str,
        docker_file_asset: builtins.str,
        max_azs: jsii.Number,
        memory_limit_mib: jsii.Number,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cpu: 
        :param desired_count: 
        :param docker_dir_asset: 
        :param docker_file_asset: 
        :param max_azs: 
        :param memory_limit_mib: 
        '''
        props = MyEcsProps(
            cpu=cpu,
            desired_count=desired_count,
            docker_dir_asset=docker_dir_asset,
            docker_file_asset=docker_file_asset,
            max_azs=max_azs,
            memory_limit_mib=memory_limit_mib,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="ecs-package.MyEcsProps",
    jsii_struct_bases=[],
    name_mapping={
        "cpu": "cpu",
        "desired_count": "desiredCount",
        "docker_dir_asset": "dockerDirAsset",
        "docker_file_asset": "dockerFileAsset",
        "max_azs": "maxAzs",
        "memory_limit_mib": "memoryLimitMiB",
    },
)
class MyEcsProps:
    def __init__(
        self,
        *,
        cpu: jsii.Number,
        desired_count: jsii.Number,
        docker_dir_asset: builtins.str,
        docker_file_asset: builtins.str,
        max_azs: jsii.Number,
        memory_limit_mib: jsii.Number,
    ) -> None:
        '''
        :param cpu: 
        :param desired_count: 
        :param docker_dir_asset: 
        :param docker_file_asset: 
        :param max_azs: 
        :param memory_limit_mib: 
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "cpu": cpu,
            "desired_count": desired_count,
            "docker_dir_asset": docker_dir_asset,
            "docker_file_asset": docker_file_asset,
            "max_azs": max_azs,
            "memory_limit_mib": memory_limit_mib,
        }

    @builtins.property
    def cpu(self) -> jsii.Number:
        result = self._values.get("cpu")
        assert result is not None, "Required property 'cpu' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def desired_count(self) -> jsii.Number:
        result = self._values.get("desired_count")
        assert result is not None, "Required property 'desired_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def docker_dir_asset(self) -> builtins.str:
        result = self._values.get("docker_dir_asset")
        assert result is not None, "Required property 'docker_dir_asset' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def docker_file_asset(self) -> builtins.str:
        result = self._values.get("docker_file_asset")
        assert result is not None, "Required property 'docker_file_asset' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_azs(self) -> jsii.Number:
        result = self._values.get("max_azs")
        assert result is not None, "Required property 'max_azs' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def memory_limit_mib(self) -> jsii.Number:
        result = self._values.get("memory_limit_mib")
        assert result is not None, "Required property 'memory_limit_mib' is missing"
        return typing.cast(jsii.Number, result)

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
