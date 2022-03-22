from multiprocessing.pool import ThreadPool
from typing import List, Dict

from cloudshell.api.cloudshell_api import InputNameValue, ReservedResourceInfo, ResourceInfo
from cloudshell.workflow.orchestration.sandbox import Sandbox

from cloudshell.orch.pool.helpers.consts import VM_POOL_NAME_ATTR
from cloudshell.orch.pool.helpers.email_helper import get_email_service, get_master_sandbox_emails
from cloudshell.orch.pool.helpers.utils import get_pool_name_to_master_sandbox_id_map


def request_new_vm_if_needed(sandbox, componenets):
    """
    :param Sandbox sandbox:
    """
    try:
        # check if we have resources from model "New VM Request"
        sandbox.logger.info("Checking if we have 'New VM Request' deployed app")
        new_vm_requests = list(filter(lambda x: x.ResourceModelName.lower() == "new vm request",
                                      sandbox.components.resources.values()))  # type: List[ReservedResourceInfo]
        new_vm_requests_details = list(
            map(lambda x: sandbox.automation_api.GetResourceDetails(x.Name), new_vm_requests))
        sandbox.logger.info("Found {} new vm requests".format(len(new_vm_requests_details)))

        if new_vm_requests_details:
            pool_name_to_master_sandbox_map = get_pool_name_to_master_sandbox_id_map(sandbox)

            pool = ThreadPool()
            async_results = [pool.apply_async(_handle_new_vm_req, (sandbox, pool_name_to_master_sandbox_map, vm_req))
                             for vm_req in new_vm_requests_details]
            pool.close()
            pool.join()

            # check results for errors
            for async_result in async_results:
                try:
                    # if thread ended with error get() will raise an exception
                    async_result.get()
                except Exception:
                    sandbox.logger.exception("error in _handle_new_vm_req")

            if any(filter(lambda x: not x.successful(), async_results)):
                raise Exception("Error deploying a new VM. Look at the logs for more details.")
    except:
        email_service = get_email_service(sandbox)
        if email_service:
            emails = get_master_sandbox_emails(sandbox)
            email_service.send_error_email(emails, sandbox.id, get_exc_info=True)
        raise


def _handle_new_vm_req(sandbox: Sandbox, pool_name_to_master_sandbox_map: Dict[str, str],
                       new_vm_requests: ResourceInfo):
    # get pool name
    pool_name = next(x for x in new_vm_requests.ResourceAttributes if x.Name == VM_POOL_NAME_ATTR).Value
    # get sandbox id
    master_sandbox_id = pool_name_to_master_sandbox_map[pool_name]
    # execute deploy_and_replace command on the New VM Request resource
    sandbox.automation_api.ExecuteCommand(sandbox.id,
                                          new_vm_requests.Name,
                                          'Resource',
                                          'deploy_and_replace',
                                          commandInputs=[InputNameValue('master_sandbox_id',
                                                                        master_sandbox_id),
                                                         InputNameValue('mgmt_resource_name',
                                                                        pool_name)])
