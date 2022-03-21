'''
#### Part1 ([CDK Construct Library](https://github.com/AymanZahran/projen-cdk-tutorial-part-1))

[![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)
[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/AymanZahran/projen-cdk-tutorial-part-1)
[![build](https://github.com/AymanZahran/projen-cdk-tutorial-part-1/actions/workflows/build.yml/badge.svg)](https://github.com/AymanZahran/projen-cdk-tutorial-part-1/actions/workflows/build.yml)
[![release](https://github.com/AymanZahran/projen-cdk-tutorial-part-1/actions/workflows/release.yml/badge.svg)](https://github.com/AymanZahran/projen-cdk-tutorial-part-1/actions/workflows/release.yml)
[![docker](https://img.shields.io/badge/docker-jsii%2Fsuperchain-brightgreen?logo=docker)](https://hub.docker.com/r/jsii/superchain)
[![npm version](https://badge.fury.io/js/fastfargate.svg)](https://badge.fury.io/js/fastfargate)
[![PyPI version](https://badge.fury.io/py/fastfargate.svg)](https://badge.fury.io/py/fastfargate)
[![NuGet version](https://badge.fury.io/nu/fastfargate.svg)](https://badge.fury.io/nu/fastfargate)

#### Part2 ([CDK App](https://github.com/AymanZahran/projen-cdk-tutorial-part-2))

[![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)
[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/AymanZahran/projen-cdk-tutorial-part-2)
[![build](https://github.com/AymanZahran/projen-cdk-tutorial-part-2/actions/workflows/build.yml/badge.svg)](https://github.com/AymanZahran/projen-cdk-tutorial-part-2/actions/workflows/build.yml)

#### Part3 ([CDK Pipelines App](https://github.com/AymanZahran/projen-cdk-tutorial-part-3))

[![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)
[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/AymanZahran/projen-cdk-tutorial-part-3)
[![build](https://github.com/AymanZahran/projen-cdk-tutorial-part-3/actions/workflows/build.yml/badge.svg)](https://github.com/AymanZahran/projen-cdk-tutorial-part-3/actions/workflows/build.yml)

## Part 1

![projen-cdk-tutorial-part-1](https://projen-cdk-tutorial.s3.amazonaws.com/projen-cdk-tutorial-part-1.png)

### Steps

1- Add Github Secrets

```sh
TWINE_USERNAME
TWINE_PASSWORD
NPM_TOKEN
NUGET_API_KEY
MAVEN_USERNAME
MAVEN_PASSWORD
MAVEN_STAGING_PROFILE_ID
MAVEN_GPG_PRIVATE_KEY
MAVEN_GPG_PRIVATE_KEY_PASSPHRASE
```

2- Create Project locally or launch using [Gitpod](https://gitpod.io/#https://github.com/AymanZahran/projen-cdk-tutorial-part-1)

```sh
mkdir projen-cdk-tutorial-part-1
cd projen-cdk-tutorial-part-1
code .
alias pj="npx projen"
pj new awscdk-construct
```

3- Configure Project

```sh
Add your code to .projenrc, This is the only file that will be modified. During projen it will scaffold your whole project including what you are reading right now ! :)
```

4- execute projen

```sh
pj
```

5- Commit & Push

```sh
git add .
git commit -m "Commit"
git push
```

![projen-cdk-tutorial-part-1-build](https://projen-cdk-tutorial.s3.amazonaws.com/projen-cdk-tutorial-part-1-build.PNG)

![projen-cdk-tutorial-part-1-release](https://projen-cdk-tutorial.s3.amazonaws.com/projen-cdk-tutorial-part-1-release.PNG)

## License

The [Apache-2.0](https://github.com/AymanZahran/projen-cdk-tutorial-part-1/blob/master/LICENSE) license

## References

* [CDK Getting Started](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)
* [CDK API Reference](https://docs.aws.amazon.com/cdk/api/v2/)
* [CDK Workshop](https://cdkworkshop.com/)
* [CDK Patterns](https://cdkpatterns.com/)
* [CDK Construct Hub](https://constructs.dev/)
* [AWS Solutions Constructs](https://docs.aws.amazon.com/solutions/latest/constructs/welcome.html)
* [Projen](https://github.com/projen/projen)
* [Projen API Reference](https://projen.io/api/API.html)
* [Projen AWS CDK Construct Library](https://projen.io/awscdk-construct.html)
* [Projen AWS CDK Applications](https://projen.io/awscdk-apps.html)
* [Publish CDK Constructs](https://github.com/seeebiii/projen-test)
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
    jsii_type="fastfargate.MyEcsConstruct",
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
    jsii_type="fastfargate.MyEcsProps",
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
