'''
[![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)
[![Build Status](https://github.com/aws/jsii/workflows/Main/badge.svg)](https://github.com/aws/jsii/actions?query=workflow%3AMain+branch%3Amain)
[![Release Status](https://github.com/aws/jsii/workflows/Main/badge.svg)](https://github.com/aws/jsii/actions?query=workflow%3AMain+branch%3Amain)
[![docker](https://img.shields.io/badge/docker-jsii%2Fsuperchain-brightgreen?logo=docker)](https://hub.docker.com/r/jsii/superchain)

#### Part1 ([CDK Construct Library](https://gitpod.io/#https://github.com/AymanZahran/ProjenCdkTutorialPart1))

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/AymanZahran/ProjenCdkTutorialPart1)

#### Part2 ([CDK App](https://gitpod.io/#https://github.com/AymanZahran/ProjenCdkTutorialPart2))

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/AymanZahran/ProjenCdkTutorialPart2)

#### Part3 ([CDK Pipelines App])

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/AymanZahran/ProjenCdkTutorialPart3)
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
    jsii_type="aymanzahranpackage.MyEcsConstruct",
):
    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        dockerfile_asset: builtins.str,
        number_of_azs: jsii.Number,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param dockerfile_asset: 
        :param number_of_azs: 
        '''
        props = MyEcsProps(
            dockerfile_asset=dockerfile_asset, number_of_azs=number_of_azs
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aymanzahranpackage.MyEcsProps",
    jsii_struct_bases=[],
    name_mapping={
        "dockerfile_asset": "dockerfileAsset",
        "number_of_azs": "numberOfAzs",
    },
)
class MyEcsProps:
    def __init__(
        self,
        *,
        dockerfile_asset: builtins.str,
        number_of_azs: jsii.Number,
    ) -> None:
        '''
        :param dockerfile_asset: 
        :param number_of_azs: 
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "dockerfile_asset": dockerfile_asset,
            "number_of_azs": number_of_azs,
        }

    @builtins.property
    def dockerfile_asset(self) -> builtins.str:
        result = self._values.get("dockerfile_asset")
        assert result is not None, "Required property 'dockerfile_asset' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def number_of_azs(self) -> jsii.Number:
        result = self._values.get("number_of_azs")
        assert result is not None, "Required property 'number_of_azs' is missing"
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
