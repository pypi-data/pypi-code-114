# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['MetadataImportArgs', 'MetadataImport']

@pulumi.input_type
class MetadataImportArgs:
    def __init__(__self__, *,
                 metadata_import_id: pulumi.Input[str],
                 service_id: pulumi.Input[str],
                 database_dump: Optional[pulumi.Input['DatabaseDumpArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MetadataImport resource.
        :param pulumi.Input[str] metadata_import_id: Required. The ID of the metadata import, which is used as the final component of the metadata import's name.This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.
        :param pulumi.Input['DatabaseDumpArgs'] database_dump: Immutable. A database dump from a pre-existing metastore's database.
        :param pulumi.Input[str] description: The description of the metadata import.
        :param pulumi.Input[str] name: Immutable. The relative resource name of the metadata import, of the form:projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{metadata_import_id}.
        :param pulumi.Input[str] request_id: Optional. A request ID. Specify a unique request ID to allow the server to ignore the request if it has completed. The server will ignore subsequent requests that provide a duplicate request ID for at least 60 minutes after the first request.For example, if an initial request times out, followed by another request with the same request ID, the server ignores the second request to prevent the creation of duplicate commitments.The request ID must be a valid UUID (https://en.wikipedia.org/wiki/Universally_unique_identifier#Format) A zero UUID (00000000-0000-0000-0000-000000000000) is not supported.
        """
        pulumi.set(__self__, "metadata_import_id", metadata_import_id)
        pulumi.set(__self__, "service_id", service_id)
        if database_dump is not None:
            pulumi.set(__self__, "database_dump", database_dump)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)

    @property
    @pulumi.getter(name="metadataImportId")
    def metadata_import_id(self) -> pulumi.Input[str]:
        """
        Required. The ID of the metadata import, which is used as the final component of the metadata import's name.This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.
        """
        return pulumi.get(self, "metadata_import_id")

    @metadata_import_id.setter
    def metadata_import_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "metadata_import_id", value)

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "service_id")

    @service_id.setter
    def service_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_id", value)

    @property
    @pulumi.getter(name="databaseDump")
    def database_dump(self) -> Optional[pulumi.Input['DatabaseDumpArgs']]:
        """
        Immutable. A database dump from a pre-existing metastore's database.
        """
        return pulumi.get(self, "database_dump")

    @database_dump.setter
    def database_dump(self, value: Optional[pulumi.Input['DatabaseDumpArgs']]):
        pulumi.set(self, "database_dump", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the metadata import.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Immutable. The relative resource name of the metadata import, of the form:projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{metadata_import_id}.
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
        Optional. A request ID. Specify a unique request ID to allow the server to ignore the request if it has completed. The server will ignore subsequent requests that provide a duplicate request ID for at least 60 minutes after the first request.For example, if an initial request times out, followed by another request with the same request ID, the server ignores the second request to prevent the creation of duplicate commitments.The request ID must be a valid UUID (https://en.wikipedia.org/wiki/Universally_unique_identifier#Format) A zero UUID (00000000-0000-0000-0000-000000000000) is not supported.
        """
        return pulumi.get(self, "request_id")

    @request_id.setter
    def request_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_id", value)


class MetadataImport(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_dump: Optional[pulumi.Input[pulumi.InputType['DatabaseDumpArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata_import_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 service_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new MetadataImport in a given project and location.
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['DatabaseDumpArgs']] database_dump: Immutable. A database dump from a pre-existing metastore's database.
        :param pulumi.Input[str] description: The description of the metadata import.
        :param pulumi.Input[str] metadata_import_id: Required. The ID of the metadata import, which is used as the final component of the metadata import's name.This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.
        :param pulumi.Input[str] name: Immutable. The relative resource name of the metadata import, of the form:projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{metadata_import_id}.
        :param pulumi.Input[str] request_id: Optional. A request ID. Specify a unique request ID to allow the server to ignore the request if it has completed. The server will ignore subsequent requests that provide a duplicate request ID for at least 60 minutes after the first request.For example, if an initial request times out, followed by another request with the same request ID, the server ignores the second request to prevent the creation of duplicate commitments.The request ID must be a valid UUID (https://en.wikipedia.org/wiki/Universally_unique_identifier#Format) A zero UUID (00000000-0000-0000-0000-000000000000) is not supported.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MetadataImportArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new MetadataImport in a given project and location.
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param MetadataImportArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MetadataImportArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_dump: Optional[pulumi.Input[pulumi.InputType['DatabaseDumpArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata_import_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 service_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = MetadataImportArgs.__new__(MetadataImportArgs)

            __props__.__dict__["database_dump"] = database_dump
            __props__.__dict__["description"] = description
            __props__.__dict__["location"] = location
            if metadata_import_id is None and not opts.urn:
                raise TypeError("Missing required property 'metadata_import_id'")
            __props__.__dict__["metadata_import_id"] = metadata_import_id
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["request_id"] = request_id
            if service_id is None and not opts.urn:
                raise TypeError("Missing required property 'service_id'")
            __props__.__dict__["service_id"] = service_id
            __props__.__dict__["create_time"] = None
            __props__.__dict__["end_time"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["update_time"] = None
        super(MetadataImport, __self__).__init__(
            'google-native:metastore/v1beta:MetadataImport',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'MetadataImport':
        """
        Get an existing MetadataImport resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MetadataImportArgs.__new__(MetadataImportArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["database_dump"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["end_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["update_time"] = None
        return MetadataImport(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time when the metadata import was started.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="databaseDump")
    def database_dump(self) -> pulumi.Output['outputs.DatabaseDumpResponse']:
        """
        Immutable. A database dump from a pre-existing metastore's database.
        """
        return pulumi.get(self, "database_dump")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the metadata import.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Output[str]:
        """
        The time when the metadata import finished.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Immutable. The relative resource name of the metadata import, of the form:projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{metadata_import_id}.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the metadata import.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The time when the metadata import was last updated.
        """
        return pulumi.get(self, "update_time")

