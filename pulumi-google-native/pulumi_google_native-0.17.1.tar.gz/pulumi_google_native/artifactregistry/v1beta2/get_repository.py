# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetRepositoryResult',
    'AwaitableGetRepositoryResult',
    'get_repository',
    'get_repository_output',
]

@pulumi.output_type
class GetRepositoryResult:
    def __init__(__self__, create_time=None, description=None, format=None, kms_key_name=None, labels=None, maven_config=None, name=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if format and not isinstance(format, str):
            raise TypeError("Expected argument 'format' to be a str")
        pulumi.set(__self__, "format", format)
        if kms_key_name and not isinstance(kms_key_name, str):
            raise TypeError("Expected argument 'kms_key_name' to be a str")
        pulumi.set(__self__, "kms_key_name", kms_key_name)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if maven_config and not isinstance(maven_config, dict):
            raise TypeError("Expected argument 'maven_config' to be a dict")
        pulumi.set(__self__, "maven_config", maven_config)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time when the repository was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The user-provided description of the repository.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def format(self) -> str:
        """
        The format of packages that are stored in the repository.
        """
        return pulumi.get(self, "format")

    @property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> str:
        """
        The Cloud KMS resource name of the customer managed encryption key that's used to encrypt the contents of the Repository. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. This value may not be changed after the Repository has been created.
        """
        return pulumi.get(self, "kms_key_name")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Labels with user-defined metadata. This field may contain up to 64 entries. Label keys and values may be no longer than 63 characters. Label keys must begin with a lowercase letter and may only contain lowercase letters, numeric characters, underscores, and dashes.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="mavenConfig")
    def maven_config(self) -> 'outputs.MavenRepositoryConfigResponse':
        """
        Maven repository config contains repository level configuration for the repositories of maven type.
        """
        return pulumi.get(self, "maven_config")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the repository, for example: "projects/p1/locations/us-central1/repositories/repo1".
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The time when the repository was last updated.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetRepositoryResult(GetRepositoryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRepositoryResult(
            create_time=self.create_time,
            description=self.description,
            format=self.format,
            kms_key_name=self.kms_key_name,
            labels=self.labels,
            maven_config=self.maven_config,
            name=self.name,
            update_time=self.update_time)


def get_repository(location: Optional[str] = None,
                   project: Optional[str] = None,
                   repository_id: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRepositoryResult:
    """
    Gets a repository.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['project'] = project
    __args__['repositoryId'] = repository_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:artifactregistry/v1beta2:getRepository', __args__, opts=opts, typ=GetRepositoryResult).value

    return AwaitableGetRepositoryResult(
        create_time=__ret__.create_time,
        description=__ret__.description,
        format=__ret__.format,
        kms_key_name=__ret__.kms_key_name,
        labels=__ret__.labels,
        maven_config=__ret__.maven_config,
        name=__ret__.name,
        update_time=__ret__.update_time)


@_utilities.lift_output_func(get_repository)
def get_repository_output(location: Optional[pulumi.Input[str]] = None,
                          project: Optional[pulumi.Input[Optional[str]]] = None,
                          repository_id: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRepositoryResult]:
    """
    Gets a repository.
    """
    ...
