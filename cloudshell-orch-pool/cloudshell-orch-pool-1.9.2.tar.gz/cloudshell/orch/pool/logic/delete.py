from multiprocessing.pool import ThreadPool
from typing import Dict, List

from cloudshell.api.cloudshell_api import InputNameValue
from cloudshell.workflow.orchestration.sandbox import Sandbox

from cloudshell.orch.pool.helpers.consts import VM_POOL_NAME_ATTR
from cloudshell.orch.pool.helpers.email_helper import get_email_service, get_master_sandbox_emails
from cloudshell.orch.pool.helpers.utils import get_pool_name_to_master_sandbox_id_map


def delete_vms(sandbox, components):
    """
    :param Sandbox sandbox:
    """
    try:
        sandbox.logger.info("Started delete_vms")
        sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id, "Deleting VMs in sandbox...")

        pool_to_master_id_map = get_pool_name_to_master_sandbox_id_map(sandbox)
        delete_reqs: Dict[str, List[str]] = {}

        deployed_apps_names = list(map(lambda x: x.deployed_app.Name, sandbox.components.apps.values()))
        deployed_app_details = list(map(lambda x: sandbox.automation_api.GetResourceDetails(x), deployed_apps_names))

        for deployed_app in deployed_app_details:
            vm_pool_name_attr = next(filter(lambda x: x.Name == VM_POOL_NAME_ATTR, deployed_app.ResourceAttributes),
                                     None)
            if vm_pool_name_attr:
                vm_pool_name = vm_pool_name_attr.Value
                if vm_pool_name in delete_reqs:
                    delete_reqs[vm_pool_name].append(deployed_app.Name)
                else:
                    delete_reqs[vm_pool_name] = [deployed_app.Name]

        pool = ThreadPool()
        async_results = [pool.apply_async(execute_delete_vms, (sandbox, pool_to_master_id_map[pool_name], pool_name,
                                                               vm_names_to_delete))
                         for pool_name, vm_names_to_delete in delete_reqs.items()]
        pool.close()
        pool.join()

        # check results for errors
        for async_result in async_results:
            try:
                # if thread ended with error get() will raise an exception
                async_result.get()
            except Exception:
                sandbox.logger.exception("error in execute_delete_vms")

        if any(filter(lambda x: not x.successful(), async_results)):
            raise Exception("Error deleting VMs. Look at the logs for more details.")

        sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id, "Deleted VMs in successfully")
    except:
        email_service = get_email_service(sandbox)
        if email_service:
            emails = get_master_sandbox_emails(sandbox)
            email_service.send_error_email(emails, sandbox.id, get_exc_info=True)
        raise


def execute_delete_vms(sandbox: Sandbox, sandbox_id: str, pool_name: str, vm_names_to_delete: List[str]):
    sandbox.logger.info(f"Going to deleted VMs {vm_names_to_delete} in master sandbox {sandbox_id} using pool mgmt "
                        f"resource {pool_name}")
    sandbox.automation_api.ExecuteCommand(sandbox_id,
                                          pool_name,
                                          "Resource",
                                          "delete_vms",
                                          [InputNameValue("vm_names", ",".join(vm_names_to_delete))])
    sandbox.logger.info(f"Deleted VMs {vm_names_to_delete}")
