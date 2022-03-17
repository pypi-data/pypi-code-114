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

__all__ = ['ServiceArgs', 'Service']

@pulumi.input_type
class ServiceArgs:
    def __init__(__self__, *,
                 service_id: pulumi.Input[str],
                 template: pulumi.Input['GoogleCloudRunOpV2RevisionTemplateArgs'],
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 binary_authorization: Optional[pulumi.Input['GoogleCloudRunOpV2BinaryAuthorizationArgs']] = None,
                 client: Optional[pulumi.Input[str]] = None,
                 client_version: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ingress: Optional[pulumi.Input['ServiceIngress']] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 launch_stage: Optional[pulumi.Input['ServiceLaunchStage']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 traffic: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudRunOpV2TrafficTargetArgs']]]] = None,
                 validate_only: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Service resource.
        :param pulumi.Input[str] service_id: Required. The unique identifier for the Service. The name of the service becomes {parent}/services/{service_id}.
        :param pulumi.Input['GoogleCloudRunOpV2RevisionTemplateArgs'] template: The template used to create revisions for this Service.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotations: Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects. Cloud Run will populate some annotations using 'run.googleapis.com' or 'serving.knative.dev' namespaces. This field follows Kubernetes annotations' namespacing, limits, and rules. More info: https://kubernetes.io/docs/user-guide/annotations
        :param pulumi.Input['GoogleCloudRunOpV2BinaryAuthorizationArgs'] binary_authorization: Settings for the Binary Authorization feature.
        :param pulumi.Input[str] client: Arbitrary identifier for the API client.
        :param pulumi.Input[str] client_version: Arbitrary version identifier for the API client.
        :param pulumi.Input[str] description: User-provided description of the Service. This field currently has a 512-character limit.
        :param pulumi.Input['ServiceIngress'] ingress: Provides the ingress settings for this Service. On output, returns the currently observed ingress settings, or INGRESS_TRAFFIC_UNSPECIFIED if no revision is active.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Map of string keys and values that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels Cloud Run will populate some labels with 'run.googleapis.com' or 'serving.knative.dev' namespaces. Those labels are read-only, and user changes will not be preserved.
        :param pulumi.Input['ServiceLaunchStage'] launch_stage: The launch stage as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). Cloud Run supports `ALPHA`, `BETA`, and `GA`. If no value is specified, GA is assumed.
        :param pulumi.Input[str] name: The fully qualified name of this Service. In CreateServiceRequest, this field is ignored, and instead composed from CreateServiceRequest.parent and CreateServiceRequest.service_id. Format: projects/{project}/locations/{location}/services/{service_id}
        :param pulumi.Input[Sequence[pulumi.Input['GoogleCloudRunOpV2TrafficTargetArgs']]] traffic: Specifies how to distribute traffic over a collection of Revisions belonging to the Service. If traffic is empty or not provided, defaults to 100% traffic to the latest `Ready` Revision.
        :param pulumi.Input[str] validate_only: Indicates that the request should be validated and default values populated, without persisting the request or creating any resources.
        """
        pulumi.set(__self__, "service_id", service_id)
        pulumi.set(__self__, "template", template)
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if binary_authorization is not None:
            pulumi.set(__self__, "binary_authorization", binary_authorization)
        if client is not None:
            pulumi.set(__self__, "client", client)
        if client_version is not None:
            pulumi.set(__self__, "client_version", client_version)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if ingress is not None:
            pulumi.set(__self__, "ingress", ingress)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if launch_stage is not None:
            pulumi.set(__self__, "launch_stage", launch_stage)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if traffic is not None:
            pulumi.set(__self__, "traffic", traffic)
        if validate_only is not None:
            pulumi.set(__self__, "validate_only", validate_only)

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Input[str]:
        """
        Required. The unique identifier for the Service. The name of the service becomes {parent}/services/{service_id}.
        """
        return pulumi.get(self, "service_id")

    @service_id.setter
    def service_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_id", value)

    @property
    @pulumi.getter
    def template(self) -> pulumi.Input['GoogleCloudRunOpV2RevisionTemplateArgs']:
        """
        The template used to create revisions for this Service.
        """
        return pulumi.get(self, "template")

    @template.setter
    def template(self, value: pulumi.Input['GoogleCloudRunOpV2RevisionTemplateArgs']):
        pulumi.set(self, "template", value)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects. Cloud Run will populate some annotations using 'run.googleapis.com' or 'serving.knative.dev' namespaces. This field follows Kubernetes annotations' namespacing, limits, and rules. More info: https://kubernetes.io/docs/user-guide/annotations
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(self) -> Optional[pulumi.Input['GoogleCloudRunOpV2BinaryAuthorizationArgs']]:
        """
        Settings for the Binary Authorization feature.
        """
        return pulumi.get(self, "binary_authorization")

    @binary_authorization.setter
    def binary_authorization(self, value: Optional[pulumi.Input['GoogleCloudRunOpV2BinaryAuthorizationArgs']]):
        pulumi.set(self, "binary_authorization", value)

    @property
    @pulumi.getter
    def client(self) -> Optional[pulumi.Input[str]]:
        """
        Arbitrary identifier for the API client.
        """
        return pulumi.get(self, "client")

    @client.setter
    def client(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client", value)

    @property
    @pulumi.getter(name="clientVersion")
    def client_version(self) -> Optional[pulumi.Input[str]]:
        """
        Arbitrary version identifier for the API client.
        """
        return pulumi.get(self, "client_version")

    @client_version.setter
    def client_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_version", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        User-provided description of the Service. This field currently has a 512-character limit.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def ingress(self) -> Optional[pulumi.Input['ServiceIngress']]:
        """
        Provides the ingress settings for this Service. On output, returns the currently observed ingress settings, or INGRESS_TRAFFIC_UNSPECIFIED if no revision is active.
        """
        return pulumi.get(self, "ingress")

    @ingress.setter
    def ingress(self, value: Optional[pulumi.Input['ServiceIngress']]):
        pulumi.set(self, "ingress", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of string keys and values that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels Cloud Run will populate some labels with 'run.googleapis.com' or 'serving.knative.dev' namespaces. Those labels are read-only, and user changes will not be preserved.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="launchStage")
    def launch_stage(self) -> Optional[pulumi.Input['ServiceLaunchStage']]:
        """
        The launch stage as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). Cloud Run supports `ALPHA`, `BETA`, and `GA`. If no value is specified, GA is assumed.
        """
        return pulumi.get(self, "launch_stage")

    @launch_stage.setter
    def launch_stage(self, value: Optional[pulumi.Input['ServiceLaunchStage']]):
        pulumi.set(self, "launch_stage", value)

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
        The fully qualified name of this Service. In CreateServiceRequest, this field is ignored, and instead composed from CreateServiceRequest.parent and CreateServiceRequest.service_id. Format: projects/{project}/locations/{location}/services/{service_id}
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
    @pulumi.getter
    def traffic(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudRunOpV2TrafficTargetArgs']]]]:
        """
        Specifies how to distribute traffic over a collection of Revisions belonging to the Service. If traffic is empty or not provided, defaults to 100% traffic to the latest `Ready` Revision.
        """
        return pulumi.get(self, "traffic")

    @traffic.setter
    def traffic(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudRunOpV2TrafficTargetArgs']]]]):
        pulumi.set(self, "traffic", value)

    @property
    @pulumi.getter(name="validateOnly")
    def validate_only(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates that the request should be validated and default values populated, without persisting the request or creating any resources.
        """
        return pulumi.get(self, "validate_only")

    @validate_only.setter
    def validate_only(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "validate_only", value)


class Service(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 binary_authorization: Optional[pulumi.Input[pulumi.InputType['GoogleCloudRunOpV2BinaryAuthorizationArgs']]] = None,
                 client: Optional[pulumi.Input[str]] = None,
                 client_version: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ingress: Optional[pulumi.Input['ServiceIngress']] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 launch_stage: Optional[pulumi.Input['ServiceLaunchStage']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service_id: Optional[pulumi.Input[str]] = None,
                 template: Optional[pulumi.Input[pulumi.InputType['GoogleCloudRunOpV2RevisionTemplateArgs']]] = None,
                 traffic: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudRunOpV2TrafficTargetArgs']]]]] = None,
                 validate_only: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new Service in a given project and location.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotations: Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects. Cloud Run will populate some annotations using 'run.googleapis.com' or 'serving.knative.dev' namespaces. This field follows Kubernetes annotations' namespacing, limits, and rules. More info: https://kubernetes.io/docs/user-guide/annotations
        :param pulumi.Input[pulumi.InputType['GoogleCloudRunOpV2BinaryAuthorizationArgs']] binary_authorization: Settings for the Binary Authorization feature.
        :param pulumi.Input[str] client: Arbitrary identifier for the API client.
        :param pulumi.Input[str] client_version: Arbitrary version identifier for the API client.
        :param pulumi.Input[str] description: User-provided description of the Service. This field currently has a 512-character limit.
        :param pulumi.Input['ServiceIngress'] ingress: Provides the ingress settings for this Service. On output, returns the currently observed ingress settings, or INGRESS_TRAFFIC_UNSPECIFIED if no revision is active.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Map of string keys and values that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels Cloud Run will populate some labels with 'run.googleapis.com' or 'serving.knative.dev' namespaces. Those labels are read-only, and user changes will not be preserved.
        :param pulumi.Input['ServiceLaunchStage'] launch_stage: The launch stage as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). Cloud Run supports `ALPHA`, `BETA`, and `GA`. If no value is specified, GA is assumed.
        :param pulumi.Input[str] name: The fully qualified name of this Service. In CreateServiceRequest, this field is ignored, and instead composed from CreateServiceRequest.parent and CreateServiceRequest.service_id. Format: projects/{project}/locations/{location}/services/{service_id}
        :param pulumi.Input[str] service_id: Required. The unique identifier for the Service. The name of the service becomes {parent}/services/{service_id}.
        :param pulumi.Input[pulumi.InputType['GoogleCloudRunOpV2RevisionTemplateArgs']] template: The template used to create revisions for this Service.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudRunOpV2TrafficTargetArgs']]]] traffic: Specifies how to distribute traffic over a collection of Revisions belonging to the Service. If traffic is empty or not provided, defaults to 100% traffic to the latest `Ready` Revision.
        :param pulumi.Input[str] validate_only: Indicates that the request should be validated and default values populated, without persisting the request or creating any resources.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new Service in a given project and location.

        :param str resource_name: The name of the resource.
        :param ServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 binary_authorization: Optional[pulumi.Input[pulumi.InputType['GoogleCloudRunOpV2BinaryAuthorizationArgs']]] = None,
                 client: Optional[pulumi.Input[str]] = None,
                 client_version: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ingress: Optional[pulumi.Input['ServiceIngress']] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 launch_stage: Optional[pulumi.Input['ServiceLaunchStage']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service_id: Optional[pulumi.Input[str]] = None,
                 template: Optional[pulumi.Input[pulumi.InputType['GoogleCloudRunOpV2RevisionTemplateArgs']]] = None,
                 traffic: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudRunOpV2TrafficTargetArgs']]]]] = None,
                 validate_only: Optional[pulumi.Input[str]] = None,
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
            __props__ = ServiceArgs.__new__(ServiceArgs)

            __props__.__dict__["annotations"] = annotations
            __props__.__dict__["binary_authorization"] = binary_authorization
            __props__.__dict__["client"] = client
            __props__.__dict__["client_version"] = client_version
            __props__.__dict__["description"] = description
            __props__.__dict__["ingress"] = ingress
            __props__.__dict__["labels"] = labels
            __props__.__dict__["launch_stage"] = launch_stage
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            if service_id is None and not opts.urn:
                raise TypeError("Missing required property 'service_id'")
            __props__.__dict__["service_id"] = service_id
            if template is None and not opts.urn:
                raise TypeError("Missing required property 'template'")
            __props__.__dict__["template"] = template
            __props__.__dict__["traffic"] = traffic
            __props__.__dict__["validate_only"] = validate_only
            __props__.__dict__["conditions"] = None
            __props__.__dict__["create_time"] = None
            __props__.__dict__["creator"] = None
            __props__.__dict__["delete_time"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["expire_time"] = None
            __props__.__dict__["generation"] = None
            __props__.__dict__["last_modifier"] = None
            __props__.__dict__["latest_created_revision"] = None
            __props__.__dict__["latest_ready_revision"] = None
            __props__.__dict__["observed_generation"] = None
            __props__.__dict__["reconciling"] = None
            __props__.__dict__["terminal_condition"] = None
            __props__.__dict__["traffic_statuses"] = None
            __props__.__dict__["uid"] = None
            __props__.__dict__["update_time"] = None
            __props__.__dict__["uri"] = None
        super(Service, __self__).__init__(
            'google-native:run/v2:Service',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Service':
        """
        Get an existing Service resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServiceArgs.__new__(ServiceArgs)

        __props__.__dict__["annotations"] = None
        __props__.__dict__["binary_authorization"] = None
        __props__.__dict__["client"] = None
        __props__.__dict__["client_version"] = None
        __props__.__dict__["conditions"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["creator"] = None
        __props__.__dict__["delete_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["expire_time"] = None
        __props__.__dict__["generation"] = None
        __props__.__dict__["ingress"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["last_modifier"] = None
        __props__.__dict__["latest_created_revision"] = None
        __props__.__dict__["latest_ready_revision"] = None
        __props__.__dict__["launch_stage"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["observed_generation"] = None
        __props__.__dict__["reconciling"] = None
        __props__.__dict__["template"] = None
        __props__.__dict__["terminal_condition"] = None
        __props__.__dict__["traffic"] = None
        __props__.__dict__["traffic_statuses"] = None
        __props__.__dict__["uid"] = None
        __props__.__dict__["update_time"] = None
        __props__.__dict__["uri"] = None
        return Service(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects. Cloud Run will populate some annotations using 'run.googleapis.com' or 'serving.knative.dev' namespaces. This field follows Kubernetes annotations' namespacing, limits, and rules. More info: https://kubernetes.io/docs/user-guide/annotations
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(self) -> pulumi.Output['outputs.GoogleCloudRunOpV2BinaryAuthorizationResponse']:
        """
        Settings for the Binary Authorization feature.
        """
        return pulumi.get(self, "binary_authorization")

    @property
    @pulumi.getter
    def client(self) -> pulumi.Output[str]:
        """
        Arbitrary identifier for the API client.
        """
        return pulumi.get(self, "client")

    @property
    @pulumi.getter(name="clientVersion")
    def client_version(self) -> pulumi.Output[str]:
        """
        Arbitrary version identifier for the API client.
        """
        return pulumi.get(self, "client_version")

    @property
    @pulumi.getter
    def conditions(self) -> pulumi.Output[Sequence['outputs.GoogleCloudRunOpV2ConditionResponse']]:
        """
        The Conditions of all other associated sub-resources. They contain additional diagnostics information in case the Service does not reach its Serving state. See comments in `reconciling` for additional information on reconciliation process in Cloud Run.
        """
        return pulumi.get(self, "conditions")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The creation time.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def creator(self) -> pulumi.Output[str]:
        """
        Email address of the authenticated creator.
        """
        return pulumi.get(self, "creator")

    @property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[str]:
        """
        The deletion time.
        """
        return pulumi.get(self, "delete_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        User-provided description of the Service. This field currently has a 512-character limit.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> pulumi.Output[str]:
        """
        For a deleted resource, the time after which it will be permamently deleted.
        """
        return pulumi.get(self, "expire_time")

    @property
    @pulumi.getter
    def generation(self) -> pulumi.Output[str]:
        """
        A number that monotonically increases every time the user modifies the desired state.
        """
        return pulumi.get(self, "generation")

    @property
    @pulumi.getter
    def ingress(self) -> pulumi.Output[str]:
        """
        Provides the ingress settings for this Service. On output, returns the currently observed ingress settings, or INGRESS_TRAFFIC_UNSPECIFIED if no revision is active.
        """
        return pulumi.get(self, "ingress")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Map of string keys and values that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels Cloud Run will populate some labels with 'run.googleapis.com' or 'serving.knative.dev' namespaces. Those labels are read-only, and user changes will not be preserved.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="lastModifier")
    def last_modifier(self) -> pulumi.Output[str]:
        """
        Email address of the last authenticated modifier.
        """
        return pulumi.get(self, "last_modifier")

    @property
    @pulumi.getter(name="latestCreatedRevision")
    def latest_created_revision(self) -> pulumi.Output[str]:
        """
        Name of the last created revision. See comments in `reconciling` for additional information on reconciliation process in Cloud Run.
        """
        return pulumi.get(self, "latest_created_revision")

    @property
    @pulumi.getter(name="latestReadyRevision")
    def latest_ready_revision(self) -> pulumi.Output[str]:
        """
        Name of the latest revision that is serving traffic. See comments in `reconciling` for additional information on reconciliation process in Cloud Run.
        """
        return pulumi.get(self, "latest_ready_revision")

    @property
    @pulumi.getter(name="launchStage")
    def launch_stage(self) -> pulumi.Output[str]:
        """
        The launch stage as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). Cloud Run supports `ALPHA`, `BETA`, and `GA`. If no value is specified, GA is assumed.
        """
        return pulumi.get(self, "launch_stage")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The fully qualified name of this Service. In CreateServiceRequest, this field is ignored, and instead composed from CreateServiceRequest.parent and CreateServiceRequest.service_id. Format: projects/{project}/locations/{location}/services/{service_id}
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="observedGeneration")
    def observed_generation(self) -> pulumi.Output[str]:
        """
        The generation of this Service currently serving traffic. See comments in `reconciling` for additional information on reconciliation process in Cloud Run.
        """
        return pulumi.get(self, "observed_generation")

    @property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[bool]:
        """
        Returns true if the Service is currently being acted upon by the system to bring it into the desired state. When a new Service is created, or an existing one is updated, Cloud Run will asynchronously perform all necessary steps to bring the Service to the desired serving state. This process is called reconciliation. While reconciliation is in process, `observed_generation`, `latest_ready_revison`, `traffic_statuses`, and `uri` will have transient values that might mismatch the intended state: Once reconciliation is over (and this field is false), there are two possible outcomes: reconciliation succeeded and the serving state matches the Service, or there was an error, and reconciliation failed. This state can be found in `terminal_condition.state`. If reconciliation succeeded, the following fields will match: `traffic` and `traffic_statuses`, `observed_generation` and `generation`, `latest_ready_revision` and `latest_created_revision`. If reconciliation failed, `traffic_statuses`, `observed_generation`, and `latest_ready_revision` will have the state of the last serving revision, or empty for newly created Services. Additional information on the failure can be found in `terminal_condition` and `conditions`.
        """
        return pulumi.get(self, "reconciling")

    @property
    @pulumi.getter
    def template(self) -> pulumi.Output['outputs.GoogleCloudRunOpV2RevisionTemplateResponse']:
        """
        The template used to create revisions for this Service.
        """
        return pulumi.get(self, "template")

    @property
    @pulumi.getter(name="terminalCondition")
    def terminal_condition(self) -> pulumi.Output['outputs.GoogleCloudRunOpV2ConditionResponse']:
        """
        The Condition of this Service, containing its readiness status, and detailed error information in case it did not reach a serving state. See comments in `reconciling` for additional information on reconciliation process in Cloud Run.
        """
        return pulumi.get(self, "terminal_condition")

    @property
    @pulumi.getter
    def traffic(self) -> pulumi.Output[Sequence['outputs.GoogleCloudRunOpV2TrafficTargetResponse']]:
        """
        Specifies how to distribute traffic over a collection of Revisions belonging to the Service. If traffic is empty or not provided, defaults to 100% traffic to the latest `Ready` Revision.
        """
        return pulumi.get(self, "traffic")

    @property
    @pulumi.getter(name="trafficStatuses")
    def traffic_statuses(self) -> pulumi.Output[Sequence['outputs.GoogleCloudRunOpV2TrafficTargetStatusResponse']]:
        """
        Detailed status information for corresponding traffic targets. See comments in `reconciling` for additional information on reconciliation process in Cloud Run.
        """
        return pulumi.get(self, "traffic_statuses")

    @property
    @pulumi.getter
    def uid(self) -> pulumi.Output[str]:
        """
        Server assigned unique identifier for the trigger. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The last-modified time.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Output[str]:
        """
        The main URI in which this Service is serving traffic.
        """
        return pulumi.get(self, "uri")

