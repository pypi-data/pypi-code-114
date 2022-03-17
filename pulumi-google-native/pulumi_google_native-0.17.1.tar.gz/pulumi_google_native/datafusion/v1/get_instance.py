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
    'GetInstanceResult',
    'AwaitableGetInstanceResult',
    'get_instance',
    'get_instance_output',
]

@pulumi.output_type
class GetInstanceResult:
    def __init__(__self__, accelerators=None, api_endpoint=None, available_version=None, create_time=None, crypto_key_config=None, dataproc_service_account=None, description=None, disabled_reason=None, display_name=None, enable_rbac=None, enable_stackdriver_logging=None, enable_stackdriver_monitoring=None, gcs_bucket=None, labels=None, name=None, network_config=None, options=None, p4_service_account=None, private_instance=None, service_account=None, service_endpoint=None, state=None, state_message=None, tenant_project_id=None, type=None, update_time=None, version=None, zone=None):
        if accelerators and not isinstance(accelerators, list):
            raise TypeError("Expected argument 'accelerators' to be a list")
        pulumi.set(__self__, "accelerators", accelerators)
        if api_endpoint and not isinstance(api_endpoint, str):
            raise TypeError("Expected argument 'api_endpoint' to be a str")
        pulumi.set(__self__, "api_endpoint", api_endpoint)
        if available_version and not isinstance(available_version, list):
            raise TypeError("Expected argument 'available_version' to be a list")
        pulumi.set(__self__, "available_version", available_version)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if crypto_key_config and not isinstance(crypto_key_config, dict):
            raise TypeError("Expected argument 'crypto_key_config' to be a dict")
        pulumi.set(__self__, "crypto_key_config", crypto_key_config)
        if dataproc_service_account and not isinstance(dataproc_service_account, str):
            raise TypeError("Expected argument 'dataproc_service_account' to be a str")
        pulumi.set(__self__, "dataproc_service_account", dataproc_service_account)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disabled_reason and not isinstance(disabled_reason, list):
            raise TypeError("Expected argument 'disabled_reason' to be a list")
        pulumi.set(__self__, "disabled_reason", disabled_reason)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if enable_rbac and not isinstance(enable_rbac, bool):
            raise TypeError("Expected argument 'enable_rbac' to be a bool")
        pulumi.set(__self__, "enable_rbac", enable_rbac)
        if enable_stackdriver_logging and not isinstance(enable_stackdriver_logging, bool):
            raise TypeError("Expected argument 'enable_stackdriver_logging' to be a bool")
        pulumi.set(__self__, "enable_stackdriver_logging", enable_stackdriver_logging)
        if enable_stackdriver_monitoring and not isinstance(enable_stackdriver_monitoring, bool):
            raise TypeError("Expected argument 'enable_stackdriver_monitoring' to be a bool")
        pulumi.set(__self__, "enable_stackdriver_monitoring", enable_stackdriver_monitoring)
        if gcs_bucket and not isinstance(gcs_bucket, str):
            raise TypeError("Expected argument 'gcs_bucket' to be a str")
        pulumi.set(__self__, "gcs_bucket", gcs_bucket)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_config and not isinstance(network_config, dict):
            raise TypeError("Expected argument 'network_config' to be a dict")
        pulumi.set(__self__, "network_config", network_config)
        if options and not isinstance(options, dict):
            raise TypeError("Expected argument 'options' to be a dict")
        pulumi.set(__self__, "options", options)
        if p4_service_account and not isinstance(p4_service_account, str):
            raise TypeError("Expected argument 'p4_service_account' to be a str")
        pulumi.set(__self__, "p4_service_account", p4_service_account)
        if private_instance and not isinstance(private_instance, bool):
            raise TypeError("Expected argument 'private_instance' to be a bool")
        pulumi.set(__self__, "private_instance", private_instance)
        if service_account and not isinstance(service_account, str):
            raise TypeError("Expected argument 'service_account' to be a str")
        if service_account is not None:
            warnings.warn("""Output only. Deprecated. Use tenant_project_id instead to extract the tenant project ID.""", DeprecationWarning)
            pulumi.log.warn("""service_account is deprecated: Output only. Deprecated. Use tenant_project_id instead to extract the tenant project ID.""")

        pulumi.set(__self__, "service_account", service_account)
        if service_endpoint and not isinstance(service_endpoint, str):
            raise TypeError("Expected argument 'service_endpoint' to be a str")
        pulumi.set(__self__, "service_endpoint", service_endpoint)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if state_message and not isinstance(state_message, str):
            raise TypeError("Expected argument 'state_message' to be a str")
        pulumi.set(__self__, "state_message", state_message)
        if tenant_project_id and not isinstance(tenant_project_id, str):
            raise TypeError("Expected argument 'tenant_project_id' to be a str")
        pulumi.set(__self__, "tenant_project_id", tenant_project_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def accelerators(self) -> Sequence['outputs.AcceleratorResponse']:
        """
        List of accelerators enabled for this CDF instance.
        """
        return pulumi.get(self, "accelerators")

    @property
    @pulumi.getter(name="apiEndpoint")
    def api_endpoint(self) -> str:
        """
        Endpoint on which the REST APIs is accessible.
        """
        return pulumi.get(self, "api_endpoint")

    @property
    @pulumi.getter(name="availableVersion")
    def available_version(self) -> Sequence['outputs.VersionResponse']:
        """
        Available versions that the instance can be upgraded to using UpdateInstanceRequest.
        """
        return pulumi.get(self, "available_version")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time the instance was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="cryptoKeyConfig")
    def crypto_key_config(self) -> 'outputs.CryptoKeyConfigResponse':
        """
        The crypto key configuration. This field is used by the Customer-Managed Encryption Keys (CMEK) feature.
        """
        return pulumi.get(self, "crypto_key_config")

    @property
    @pulumi.getter(name="dataprocServiceAccount")
    def dataproc_service_account(self) -> str:
        """
        User-managed service account to set on Dataproc when Cloud Data Fusion creates Dataproc to run data processing pipelines. This allows users to have fine-grained access control on Dataproc's accesses to cloud resources.
        """
        return pulumi.get(self, "dataproc_service_account")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A description of this instance.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="disabledReason")
    def disabled_reason(self) -> Sequence[str]:
        """
        If the instance state is DISABLED, the reason for disabling the instance.
        """
        return pulumi.get(self, "disabled_reason")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Display name for an instance.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="enableRbac")
    def enable_rbac(self) -> bool:
        """
        Option to enable granular role-based access control.
        """
        return pulumi.get(self, "enable_rbac")

    @property
    @pulumi.getter(name="enableStackdriverLogging")
    def enable_stackdriver_logging(self) -> bool:
        """
        Option to enable Stackdriver Logging.
        """
        return pulumi.get(self, "enable_stackdriver_logging")

    @property
    @pulumi.getter(name="enableStackdriverMonitoring")
    def enable_stackdriver_monitoring(self) -> bool:
        """
        Option to enable Stackdriver Monitoring.
        """
        return pulumi.get(self, "enable_stackdriver_monitoring")

    @property
    @pulumi.getter(name="gcsBucket")
    def gcs_bucket(self) -> str:
        """
        Cloud Storage bucket generated by Data Fusion in the customer project.
        """
        return pulumi.get(self, "gcs_bucket")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        The resource labels for instance to use to annotate any related underlying resources such as Compute Engine VMs. The character '=' is not allowed to be used within the labels.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of this instance is in the form of projects/{project}/locations/{location}/instances/{instance}.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> 'outputs.NetworkConfigResponse':
        """
        Network configuration options. These are required when a private Data Fusion instance is to be created.
        """
        return pulumi.get(self, "network_config")

    @property
    @pulumi.getter
    def options(self) -> Mapping[str, str]:
        """
        Map of additional options used to configure the behavior of Data Fusion instance.
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter(name="p4ServiceAccount")
    def p4_service_account(self) -> str:
        """
        P4 service account for the customer project.
        """
        return pulumi.get(self, "p4_service_account")

    @property
    @pulumi.getter(name="privateInstance")
    def private_instance(self) -> bool:
        """
        Specifies whether the Data Fusion instance should be private. If set to true, all Data Fusion nodes will have private IP addresses and will not be able to access the public internet.
        """
        return pulumi.get(self, "private_instance")

    @property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> str:
        """
        Deprecated. Use tenant_project_id instead to extract the tenant project ID.
        """
        return pulumi.get(self, "service_account")

    @property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> str:
        """
        Endpoint on which the Data Fusion UI is accessible.
        """
        return pulumi.get(self, "service_endpoint")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of this Data Fusion instance.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> str:
        """
        Additional information about the current state of this Data Fusion instance if available.
        """
        return pulumi.get(self, "state_message")

    @property
    @pulumi.getter(name="tenantProjectId")
    def tenant_project_id(self) -> str:
        """
        The name of the tenant project.
        """
        return pulumi.get(self, "tenant_project_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Instance type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The time the instance was last updated.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Current version of the Data Fusion. Only specifiable in Update.
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter
    def zone(self) -> str:
        """
        Name of the zone in which the Data Fusion instance will be created. Only DEVELOPER instances use this field.
        """
        return pulumi.get(self, "zone")


class AwaitableGetInstanceResult(GetInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceResult(
            accelerators=self.accelerators,
            api_endpoint=self.api_endpoint,
            available_version=self.available_version,
            create_time=self.create_time,
            crypto_key_config=self.crypto_key_config,
            dataproc_service_account=self.dataproc_service_account,
            description=self.description,
            disabled_reason=self.disabled_reason,
            display_name=self.display_name,
            enable_rbac=self.enable_rbac,
            enable_stackdriver_logging=self.enable_stackdriver_logging,
            enable_stackdriver_monitoring=self.enable_stackdriver_monitoring,
            gcs_bucket=self.gcs_bucket,
            labels=self.labels,
            name=self.name,
            network_config=self.network_config,
            options=self.options,
            p4_service_account=self.p4_service_account,
            private_instance=self.private_instance,
            service_account=self.service_account,
            service_endpoint=self.service_endpoint,
            state=self.state,
            state_message=self.state_message,
            tenant_project_id=self.tenant_project_id,
            type=self.type,
            update_time=self.update_time,
            version=self.version,
            zone=self.zone)


def get_instance(instance_id: Optional[str] = None,
                 location: Optional[str] = None,
                 project: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceResult:
    """
    Gets details of a single Data Fusion instance.
    """
    __args__ = dict()
    __args__['instanceId'] = instance_id
    __args__['location'] = location
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:datafusion/v1:getInstance', __args__, opts=opts, typ=GetInstanceResult).value

    return AwaitableGetInstanceResult(
        accelerators=__ret__.accelerators,
        api_endpoint=__ret__.api_endpoint,
        available_version=__ret__.available_version,
        create_time=__ret__.create_time,
        crypto_key_config=__ret__.crypto_key_config,
        dataproc_service_account=__ret__.dataproc_service_account,
        description=__ret__.description,
        disabled_reason=__ret__.disabled_reason,
        display_name=__ret__.display_name,
        enable_rbac=__ret__.enable_rbac,
        enable_stackdriver_logging=__ret__.enable_stackdriver_logging,
        enable_stackdriver_monitoring=__ret__.enable_stackdriver_monitoring,
        gcs_bucket=__ret__.gcs_bucket,
        labels=__ret__.labels,
        name=__ret__.name,
        network_config=__ret__.network_config,
        options=__ret__.options,
        p4_service_account=__ret__.p4_service_account,
        private_instance=__ret__.private_instance,
        service_account=__ret__.service_account,
        service_endpoint=__ret__.service_endpoint,
        state=__ret__.state,
        state_message=__ret__.state_message,
        tenant_project_id=__ret__.tenant_project_id,
        type=__ret__.type,
        update_time=__ret__.update_time,
        version=__ret__.version,
        zone=__ret__.zone)


@_utilities.lift_output_func(get_instance)
def get_instance_output(instance_id: Optional[pulumi.Input[str]] = None,
                        location: Optional[pulumi.Input[str]] = None,
                        project: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceResult]:
    """
    Gets details of a single Data Fusion instance.
    """
    ...
