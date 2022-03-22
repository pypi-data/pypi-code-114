from typing import List

from cloudshell.api.cloudshell_api import ReservedResourceInfo, ReservationDescriptionInfo
from cloudshell.workflow.orchestration.sandbox import Sandbox

from cloudshell.orch.pool.helpers.consts import VM_POOL_NAME_ATTR


def get_mgmt_resource(master_sandbox_resources: List[ReservedResourceInfo]) -> ReservedResourceInfo:
    for resource in master_sandbox_resources:
        if resource.ResourceModelName == "VM Pool Mgmt Resource":
            return resource
    raise ValueError("Couldn't find VM Pool Management Resource")


def get_master_sandbox(sandbox: Sandbox) -> List[ReservationDescriptionInfo]:
    master_sandboxes = []
    checked_vm_pool_names = []

    for resource in sandbox.components.resources.values():
        if "/" in resource.Name:
            # This is a sub resource. need to get root resource
            root_resource_name = resource.Name.split("/")[0]
            resource_details = sandbox.automation_api.GetResourceDetails(root_resource_name)
        else:
            resource_details = sandbox.automation_api.GetResourceDetails(resource.Name)

        # need to support 1st gen and 2nd gen attribute name because "new vm request" uses 1st gen
        filtered_attributes = list(
            filter(lambda x:
                   x.Name in [f"{resource_details.ResourceModelName}.{VM_POOL_NAME_ATTR}", VM_POOL_NAME_ATTR],
                   resource_details.ResourceAttributes))
        if not filtered_attributes:
            # VM Pool Name attribute not found
            continue

        vm_pool_name = filtered_attributes[0].Value

        # we want to makes sure to get master sandbox details only for unique pools
        if vm_pool_name in checked_vm_pool_names:
            continue
        else:
            checked_vm_pool_names.append(vm_pool_name)

        # get resource details for VM Pool resource and extract master sandbox details
        vm_pool_resource = sandbox.automation_api.GetResourceDetails(vm_pool_name)
        vm_pool_resource_availability = sandbox.automation_api.GetResourceAvailability([vm_pool_resource.Name])
        master_sandbox_id = vm_pool_resource_availability.Resources[0].Reservations[0].ReservationId
        master_sandbox = sandbox.automation_api.GetReservationDetails(master_sandbox_id).ReservationDescription

        master_sandboxes.append(master_sandbox)

    if not master_sandboxes:
        raise ValueError("Master sandbox not found")

    return master_sandboxes
