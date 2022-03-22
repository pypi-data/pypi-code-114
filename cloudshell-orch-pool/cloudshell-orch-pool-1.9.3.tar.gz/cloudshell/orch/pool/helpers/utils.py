import time

from cloudshell.api.cloudshell_api import ReservedResourceInfo
from cloudshell.api.common_cloudshell_api import CloudShellAPIError
from cloudshell.workflow.orchestration.sandbox import Sandbox
from typing import List, Dict

from cloudshell.orch.pool.helpers.master_sandbox import get_master_sandbox, get_mgmt_resource


def retry_with_interval(action, logger, retries=6, interval=10):
    retry = 0
    while True:
        try:
            action()
            logger.info("Action completed")
            return
        except CloudShellAPIError:
            logger.info("Retry {} failed".format(retry + 1))
            if retry >= retries - 1:
                logger.info("No more retries left, raising original exception")
                raise
            retry += 1
            logger.info("Going to sleep for {} seconds".format(interval))
            time.sleep(interval)


def get_deployed_apps(sandbox: Sandbox) -> List[ReservedResourceInfo]:
    deployed_apps = list(map(lambda x: x.deployed_app, sandbox.components.apps.values()))
    return deployed_apps


def get_pool_name_to_master_sandbox_id_map(sandbox: Sandbox) -> Dict[str, str]:
    master_sandboxes = get_master_sandbox(sandbox)
    # create map between pool name to it's master sandbox id
    pool_name_to_master_sandbox_map: Dict[str, str] = {}
    for master_sandbox in master_sandboxes:
        mgmt_resource = get_mgmt_resource(master_sandbox.Resources)
        pool_name_to_master_sandbox_map[mgmt_resource.Name] = master_sandbox.Id
    return pool_name_to_master_sandbox_map
