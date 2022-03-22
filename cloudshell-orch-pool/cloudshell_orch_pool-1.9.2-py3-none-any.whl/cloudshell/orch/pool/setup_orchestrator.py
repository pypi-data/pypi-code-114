from cloudshell.workflow.orchestration.sandbox import Sandbox

from cloudshell.orch.pool.logic.new_vm_request import request_new_vm_if_needed
from cloudshell.orch.pool.logic.power import power_on_vms_and_refresh_vm_details
from cloudshell.orch.pool.logic.trigger import trigger_extend_vm_pool_if_needed_async_safely


class VMPoolSetupWorkflow(object):

    def register(self, sandbox: Sandbox, enable_power_on: bool = True) -> None:
        sandbox.logger.info("Adding VM Pool setup orchestration")

        sandbox.workflow.add_to_provisioning(request_new_vm_if_needed)
        sandbox.workflow.on_provisioning_ended(trigger_extend_vm_pool_if_needed_async_safely)

        if enable_power_on:
            sandbox.workflow.add_to_connectivity(power_on_vms_and_refresh_vm_details)
            sandbox.logger.info("Added power_on_vms_and_refresh_vm_details to VM Pool setup orchestration")

        # TODO - handle edge case when we dont have any more apps in the pool and we get a stub
