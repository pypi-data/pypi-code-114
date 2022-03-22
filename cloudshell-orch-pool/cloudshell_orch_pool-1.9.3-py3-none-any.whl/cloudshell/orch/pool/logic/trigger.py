from cloudshell.api.cloudshell_api import InputNameValue
from typing import Dict, List

from cloudshell.orch.pool.helpers.master_sandbox import get_master_sandbox, get_mgmt_resource
from cloudshell.orch.pool.helpers.consts import OUTDATED_APP_ATTR, DEPLOYED_APP_MODEL, VM_POOL_NAME_ATTR
from cloudshell.orch.pool.helpers.utils import get_pool_name_to_master_sandbox_id_map


def trigger_shrink_pool_if_needed_safely(sandbox, components):
    """
    :param Sandbox sandbox:
    :param components:
    :return:
    """
    try:
        master_sandboxes = get_master_sandbox(sandbox)
        for master_sandbox in master_sandboxes:
            # find management service in the master sandbox
            mgmt_resource = get_mgmt_resource(master_sandbox.Resources)
            # execute async extend pool if needed and dont wait for results
            sandbox.automation_api.EnqueueCommand(master_sandbox.Id,
                                                  mgmt_resource.Name,
                                                  'Resource',
                                                  'shrink_vm_pool_if_needed')
    except Exception:
        sandbox.logger.exception("Error requesting to shrink pool if needed")


def trigger_rebuild_outdated_vms(sandbox, components):
    try:
        pool_name_to_master_sandbox_map = get_pool_name_to_master_sandbox_id_map(sandbox)

        # Collecting a list of vm pool deployed apps in the current sandbox
        deployed_apps = list(map(lambda x: x.deployed_app, sandbox.components.apps.values()))
        vm_pool_deployed_apps = list(filter(lambda x: x.ResourceModelName == DEPLOYED_APP_MODEL, deployed_apps))
        # Collecting resource details for these VMs
        deployed_apps_details = list(
            map(lambda x: sandbox.automation_api.GetResourceDetails(x.Name), vm_pool_deployed_apps))

        # Checking if vms are outdated, building list of the outdated VMs.
        apps_for_rebuild = [app for app in deployed_apps_details if any(
            attr for attr in app.ResourceAttributes if
            attr.Name.endswith(f".{OUTDATED_APP_ATTR}") and "True" == attr.Value)]

        # grouping apps by pool name
        pool_name_to_apps_for_rebuild_map: Dict[str, List[str]] = {}
        for app in apps_for_rebuild:
            # get pool name
            pool_name = next(x for x in app.ResourceAttributes
                             if x.Name in [f"{app.ResourceModelName}.{VM_POOL_NAME_ATTR}", VM_POOL_NAME_ATTR]).Value
            # add app name to mapping to pool name
            if pool_name in pool_name_to_apps_for_rebuild_map:
                pool_name_to_apps_for_rebuild_map[pool_name].append(app.Name)
            else:
                pool_name_to_apps_for_rebuild_map[pool_name] = [app.Name]

        # Triggering rebuild for outdated VMs.
        for pool_name, apps_for_rebuild in pool_name_to_apps_for_rebuild_map.items():
            sandbox.automation_api.EnqueueCommand(pool_name_to_master_sandbox_map[pool_name],
                                                  pool_name,
                                                  'Resource',
                                                  'rebuild_outdated_vms',
                                                  commandInputs=[InputNameValue(Name="apps_for_rebuild",
                                                                                Value=",".join(apps_for_rebuild))])
    except Exception:
        sandbox.logger.exception("Error requesting to shrink pool if needed")


def trigger_extend_vm_pool_if_needed_async_safely(sandbox, components):
    """
    :param Sandbox sandbox:
    """
    try:
        master_sandboxes = get_master_sandbox(sandbox)
        for master_sandbox in master_sandboxes:
            # find management service in the master sandbox
            mgmt_resource = get_mgmt_resource(master_sandbox.Resources)
            # execute async extend pool if needed and dont wait for results
            sandbox.automation_api.EnqueueCommand(master_sandbox.Id,
                                                  mgmt_resource.Name,
                                                  'Resource',
                                                  'extend_vm_pool_if_needed')
    except Exception:
        sandbox.logger.exception("Error requesting to extend pool if needed")
