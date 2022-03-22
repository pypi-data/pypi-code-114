from cloudshell.api.cloudshell_api import AttributeNameValue, ResourceAttributesUpdateRequest
from cloudshell.workflow.orchestration.components import Components

from cloudshell.orch.pool.helpers.consts import DEPLOYED_APP_MODEL, MASTER_SANDBOX_ID_ATTR
from cloudshell.orch.pool.helpers.master_sandbox import get_mgmt_resource, get_master_sandbox


def remove_vms_from_pool_and_trigger_pool_extend(sandbox, components):
    """
    Will remove all deployed apps (VMs) from their respective pools by setting an empty string on the
    "Master Sandbox ID" attribute. And after this the method will trigger "extend_vm_pool_if_needed" on all pool
    resources.

    :param Sandbox sandbox:
    """
    sandbox.logger.info("starting remove_vms_from_pool_and_trigger_pool_extend")

    master_sandboxes = get_master_sandbox(sandbox)

    # hard refresh components
    reservation_description = sandbox.automation_api.GetReservationDetails(sandbox.id,
                                                                           disableCache=True).ReservationDescription
    sandbox.components = Components(reservation_description.Resources,
                                    reservation_description.Services,
                                    reservation_description.Apps)

    app_names_to_update = [app.deployed_app.Name for app in sandbox.components.apps.values()
                           if app.deployed_app.ResourceModelName == DEPLOYED_APP_MODEL]
    sandbox.logger.info(f"Found app names to update: {app_names_to_update}")

    # set VM Pool Name attribute to empty for apps in sandbox
    # this will remove the VM from the pool
    update_req = []
    for app_name in app_names_to_update:
        update_req.append(
            ResourceAttributesUpdateRequest(app_name,
                                            [AttributeNameValue(f"{DEPLOYED_APP_MODEL}.{MASTER_SANDBOX_ID_ATTR}", "")]))
    if update_req:
        sandbox.automation_api.SetAttributesValues(update_req)
        sandbox.logger.info(f"Updated Master Sandbox ID attribute to empty string on {len(app_names_to_update)} "
                            f"deployed apps")

    sandbox.logger.info("Triggering extend_vm_pool_if_needed on all master sandboxes")
    for master_sandbox in master_sandboxes:
        # find management service in the master sandbox
        mgmt_resource = get_mgmt_resource(master_sandbox.Resources)
        # execute async extend pool if needed and dont wait for results
        sandbox.automation_api.EnqueueCommand(master_sandbox.Id,
                                              mgmt_resource.Name,
                                              "Resource",
                                              "extend_vm_pool_if_needed")
