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

__all__ = ['CapacityCommitmentArgs', 'CapacityCommitment']

@pulumi.input_type
class CapacityCommitmentArgs:
    def __init__(__self__, *,
                 capacity_commitment_id: Optional[pulumi.Input[str]] = None,
                 enforce_single_admin_project_per_org: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 multi_region_auxiliary: Optional[pulumi.Input[bool]] = None,
                 plan: Optional[pulumi.Input['CapacityCommitmentPlan']] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 renewal_plan: Optional[pulumi.Input['CapacityCommitmentRenewalPlan']] = None,
                 slot_count: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CapacityCommitment resource.
        :param pulumi.Input[str] capacity_commitment_id: The optional capacity commitment ID. Capacity commitment name will be generated automatically if this field is empty. This field must only contain lower case alphanumeric characters or dashes. The first and last character cannot be a dash. Max length is 64 characters. NOTE: this ID won't be kept if the capacity commitment is split or merged.
        :param pulumi.Input[str] enforce_single_admin_project_per_org: If true, fail the request if another project in the organization has a capacity commitment.
        :param pulumi.Input[bool] multi_region_auxiliary: Applicable only for commitments located within one of the BigQuery multi-regions (US or EU). If set to true, this commitment is placed in the organization's secondary region which is designated for disaster recovery purposes. If false, this commitment is placed in the organization's default region.
        :param pulumi.Input['CapacityCommitmentPlan'] plan: Capacity commitment commitment plan.
        :param pulumi.Input['CapacityCommitmentRenewalPlan'] renewal_plan: The plan this capacity commitment is converted to after commitment_end_time passes. Once the plan is changed, committed period is extended according to commitment plan. Only applicable for ANNUAL and TRIAL commitments.
        :param pulumi.Input[str] slot_count: Number of slots in this commitment.
        """
        if capacity_commitment_id is not None:
            pulumi.set(__self__, "capacity_commitment_id", capacity_commitment_id)
        if enforce_single_admin_project_per_org is not None:
            pulumi.set(__self__, "enforce_single_admin_project_per_org", enforce_single_admin_project_per_org)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if multi_region_auxiliary is not None:
            pulumi.set(__self__, "multi_region_auxiliary", multi_region_auxiliary)
        if plan is not None:
            pulumi.set(__self__, "plan", plan)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if renewal_plan is not None:
            pulumi.set(__self__, "renewal_plan", renewal_plan)
        if slot_count is not None:
            pulumi.set(__self__, "slot_count", slot_count)

    @property
    @pulumi.getter(name="capacityCommitmentId")
    def capacity_commitment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The optional capacity commitment ID. Capacity commitment name will be generated automatically if this field is empty. This field must only contain lower case alphanumeric characters or dashes. The first and last character cannot be a dash. Max length is 64 characters. NOTE: this ID won't be kept if the capacity commitment is split or merged.
        """
        return pulumi.get(self, "capacity_commitment_id")

    @capacity_commitment_id.setter
    def capacity_commitment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "capacity_commitment_id", value)

    @property
    @pulumi.getter(name="enforceSingleAdminProjectPerOrg")
    def enforce_single_admin_project_per_org(self) -> Optional[pulumi.Input[str]]:
        """
        If true, fail the request if another project in the organization has a capacity commitment.
        """
        return pulumi.get(self, "enforce_single_admin_project_per_org")

    @enforce_single_admin_project_per_org.setter
    def enforce_single_admin_project_per_org(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "enforce_single_admin_project_per_org", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="multiRegionAuxiliary")
    def multi_region_auxiliary(self) -> Optional[pulumi.Input[bool]]:
        """
        Applicable only for commitments located within one of the BigQuery multi-regions (US or EU). If set to true, this commitment is placed in the organization's secondary region which is designated for disaster recovery purposes. If false, this commitment is placed in the organization's default region.
        """
        return pulumi.get(self, "multi_region_auxiliary")

    @multi_region_auxiliary.setter
    def multi_region_auxiliary(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "multi_region_auxiliary", value)

    @property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input['CapacityCommitmentPlan']]:
        """
        Capacity commitment commitment plan.
        """
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: Optional[pulumi.Input['CapacityCommitmentPlan']]):
        pulumi.set(self, "plan", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="renewalPlan")
    def renewal_plan(self) -> Optional[pulumi.Input['CapacityCommitmentRenewalPlan']]:
        """
        The plan this capacity commitment is converted to after commitment_end_time passes. Once the plan is changed, committed period is extended according to commitment plan. Only applicable for ANNUAL and TRIAL commitments.
        """
        return pulumi.get(self, "renewal_plan")

    @renewal_plan.setter
    def renewal_plan(self, value: Optional[pulumi.Input['CapacityCommitmentRenewalPlan']]):
        pulumi.set(self, "renewal_plan", value)

    @property
    @pulumi.getter(name="slotCount")
    def slot_count(self) -> Optional[pulumi.Input[str]]:
        """
        Number of slots in this commitment.
        """
        return pulumi.get(self, "slot_count")

    @slot_count.setter
    def slot_count(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slot_count", value)


class CapacityCommitment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capacity_commitment_id: Optional[pulumi.Input[str]] = None,
                 enforce_single_admin_project_per_org: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 multi_region_auxiliary: Optional[pulumi.Input[bool]] = None,
                 plan: Optional[pulumi.Input['CapacityCommitmentPlan']] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 renewal_plan: Optional[pulumi.Input['CapacityCommitmentRenewalPlan']] = None,
                 slot_count: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new capacity commitment resource.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] capacity_commitment_id: The optional capacity commitment ID. Capacity commitment name will be generated automatically if this field is empty. This field must only contain lower case alphanumeric characters or dashes. The first and last character cannot be a dash. Max length is 64 characters. NOTE: this ID won't be kept if the capacity commitment is split or merged.
        :param pulumi.Input[str] enforce_single_admin_project_per_org: If true, fail the request if another project in the organization has a capacity commitment.
        :param pulumi.Input[bool] multi_region_auxiliary: Applicable only for commitments located within one of the BigQuery multi-regions (US or EU). If set to true, this commitment is placed in the organization's secondary region which is designated for disaster recovery purposes. If false, this commitment is placed in the organization's default region.
        :param pulumi.Input['CapacityCommitmentPlan'] plan: Capacity commitment commitment plan.
        :param pulumi.Input['CapacityCommitmentRenewalPlan'] renewal_plan: The plan this capacity commitment is converted to after commitment_end_time passes. Once the plan is changed, committed period is extended according to commitment plan. Only applicable for ANNUAL and TRIAL commitments.
        :param pulumi.Input[str] slot_count: Number of slots in this commitment.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[CapacityCommitmentArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new capacity commitment resource.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param CapacityCommitmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CapacityCommitmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capacity_commitment_id: Optional[pulumi.Input[str]] = None,
                 enforce_single_admin_project_per_org: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 multi_region_auxiliary: Optional[pulumi.Input[bool]] = None,
                 plan: Optional[pulumi.Input['CapacityCommitmentPlan']] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 renewal_plan: Optional[pulumi.Input['CapacityCommitmentRenewalPlan']] = None,
                 slot_count: Optional[pulumi.Input[str]] = None,
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
            __props__ = CapacityCommitmentArgs.__new__(CapacityCommitmentArgs)

            __props__.__dict__["capacity_commitment_id"] = capacity_commitment_id
            __props__.__dict__["enforce_single_admin_project_per_org"] = enforce_single_admin_project_per_org
            __props__.__dict__["location"] = location
            __props__.__dict__["multi_region_auxiliary"] = multi_region_auxiliary
            __props__.__dict__["plan"] = plan
            __props__.__dict__["project"] = project
            __props__.__dict__["renewal_plan"] = renewal_plan
            __props__.__dict__["slot_count"] = slot_count
            __props__.__dict__["commitment_end_time"] = None
            __props__.__dict__["commitment_start_time"] = None
            __props__.__dict__["failure_status"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["state"] = None
        super(CapacityCommitment, __self__).__init__(
            'google-native:bigqueryreservation/v1:CapacityCommitment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CapacityCommitment':
        """
        Get an existing CapacityCommitment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CapacityCommitmentArgs.__new__(CapacityCommitmentArgs)

        __props__.__dict__["commitment_end_time"] = None
        __props__.__dict__["commitment_start_time"] = None
        __props__.__dict__["failure_status"] = None
        __props__.__dict__["multi_region_auxiliary"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["plan"] = None
        __props__.__dict__["renewal_plan"] = None
        __props__.__dict__["slot_count"] = None
        __props__.__dict__["state"] = None
        return CapacityCommitment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="commitmentEndTime")
    def commitment_end_time(self) -> pulumi.Output[str]:
        """
        The end of the current commitment period. It is applicable only for ACTIVE capacity commitments.
        """
        return pulumi.get(self, "commitment_end_time")

    @property
    @pulumi.getter(name="commitmentStartTime")
    def commitment_start_time(self) -> pulumi.Output[str]:
        """
        The start of the current commitment period. It is applicable only for ACTIVE capacity commitments.
        """
        return pulumi.get(self, "commitment_start_time")

    @property
    @pulumi.getter(name="failureStatus")
    def failure_status(self) -> pulumi.Output['outputs.StatusResponse']:
        """
        For FAILED commitment plan, provides the reason of failure.
        """
        return pulumi.get(self, "failure_status")

    @property
    @pulumi.getter(name="multiRegionAuxiliary")
    def multi_region_auxiliary(self) -> pulumi.Output[bool]:
        """
        Applicable only for commitments located within one of the BigQuery multi-regions (US or EU). If set to true, this commitment is placed in the organization's secondary region which is designated for disaster recovery purposes. If false, this commitment is placed in the organization's default region.
        """
        return pulumi.get(self, "multi_region_auxiliary")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the capacity commitment, e.g., `projects/myproject/locations/US/capacityCommitments/123` For the commitment id, it must only contain lower case alphanumeric characters or dashes.It must start with a letter and must not end with a dash. Its maximum length is 64 characters.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def plan(self) -> pulumi.Output[str]:
        """
        Capacity commitment commitment plan.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="renewalPlan")
    def renewal_plan(self) -> pulumi.Output[str]:
        """
        The plan this capacity commitment is converted to after commitment_end_time passes. Once the plan is changed, committed period is extended according to commitment plan. Only applicable for ANNUAL and TRIAL commitments.
        """
        return pulumi.get(self, "renewal_plan")

    @property
    @pulumi.getter(name="slotCount")
    def slot_count(self) -> pulumi.Output[str]:
        """
        Number of slots in this commitment.
        """
        return pulumi.get(self, "slot_count")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of the commitment.
        """
        return pulumi.get(self, "state")

