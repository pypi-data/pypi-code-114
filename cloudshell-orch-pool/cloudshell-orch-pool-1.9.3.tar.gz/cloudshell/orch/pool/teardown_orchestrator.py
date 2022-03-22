from cloudshell.workflow.orchestration.sandbox import Sandbox

from cloudshell.orch.pool.logic.delete import delete_vms
from cloudshell.orch.pool.logic.power import power_off_vms
from cloudshell.orch.pool.logic.trigger import trigger_shrink_pool_if_needed_safely, trigger_rebuild_outdated_vms


class VMPoolTeardownWorkflow(object):

    def register(self, sandbox: Sandbox, enable_power_off: bool = True, enable_shrink_trigger: bool = True,
                 enable_rebuild_trigger: bool = True, enable_delete_vms: bool = False) -> None:
        sandbox.logger.info("Adding VM Pool teardown orchestration")

        if enable_power_off:
            sandbox.workflow.add_to_teardown(power_off_vms)
            sandbox.logger.info("Added power_off_vms to teardown workflow")

        if enable_shrink_trigger:
            sandbox.workflow.add_to_teardown(trigger_shrink_pool_if_needed_safely)
            sandbox.logger.info("Added trigger_shrink_pool_if_needed_safely to teardown workflow")

        if enable_rebuild_trigger:
            sandbox.workflow.add_to_teardown(trigger_rebuild_outdated_vms)
            sandbox.logger.info("Added trigger_rebuild_outdated_vms to teardown workflow")

        if enable_delete_vms:
            sandbox.workflow.add_to_teardown(delete_vms)
            sandbox.logger.info("Added delete_vms to teardown workflow")
