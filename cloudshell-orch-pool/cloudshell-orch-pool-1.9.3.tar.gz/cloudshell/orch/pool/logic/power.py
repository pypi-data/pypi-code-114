from multiprocessing.pool import ThreadPool

from cloudshell.api.common_cloudshell_api import CloudShellAPIError

from cloudshell.orch.pool.helpers.email_helper import get_email_service, get_master_sandbox_emails
from cloudshell.orch.pool.helpers.utils import retry_with_interval, get_deployed_apps


def power_off_vms(sandbox, components):
    """
    :param Sandbox sandbox:
    :return:
    """
    sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id, 'VMs are being powered off...')

    deployed_apps = list(map(lambda x: x.deployed_app, sandbox.components.apps.values()))

    pool = ThreadPool()
    async_results = []

    for resource in deployed_apps:
        async_results.append(
            pool.apply_async(power_off_vm, (sandbox, resource)))

    pool.close()
    pool.join()

    for async_result in async_results:
        try:
            res = async_result.get()
            if not res:
                raise Exception("Sandbox is Completed with Errors during Power Off VMs - " + res)
        except:
            email_service = get_email_service(sandbox)
            if email_service:
                emails = get_master_sandbox_emails(sandbox)
                email_service.send_error_email(emails, sandbox.id, get_exc_info=True)
            raise


def power_off_vm(sandbox, deployed_app):
    """
    :param Sandbox sandbox:
    :param ReservedResourceInfo deployed_app:
    :return:
    """
    # 1. unshare resource so that the power off command will be atomic on this resource
    try:
        retry_with_interval(lambda: sandbox.automation_api.SetResourceSharedState(sandbox.id, [deployed_app.Name], False),
                            sandbox.logger)
    except CloudShellAPIError as exc:
        if "used in another sandbox" in str(exc).lower():
            sandbox.logger.info("We couldn't get the entire resource. It means that other sub-resource are currently "
                                "reserved. So no need to power off.")
            sandbox.automation_api.\
                WriteMessageToReservationOutput(sandbox.id,
                                                "VM {} is currently in use in another sandbox so it will not be "
                                                "powered off".format(deployed_app.Name))
            return True
        raise

    # 2. execute power off after we have unshared the resource
    sandbox.logger.info("Executing power off command")
    sandbox.automation_api.ExecuteResourceConnectedCommand(sandbox.id, deployed_app.Name, "PowerOff", "power")
    sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id, "VM {} was powered off successfully"
                                                           .format(deployed_app.Name))

    # 3. share the resource before sandbox ends so it will get back to the pool shared
    sandbox.logger.info("Setting resource share level to 'shared' before we release the VM to the pool")
    sandbox.automation_api.SetResourceSharedState(sandbox.id, [deployed_app.Name], True)

    return True


def power_on_vms_and_refresh_vm_details(sandbox, components):
    """
    :param Sandbox sandbox:
    """
    try:
        sandbox.automation_api.WriteMessageToReservationOutput(sandbox.id, "Powering on VMs...")
        deployed_apps = get_deployed_apps(sandbox)
        run_async_power_on_refresh_ip(sandbox, deployed_apps)
        refresh_vm_details(sandbox, deployed_apps)
    except:
        email_service = get_email_service(sandbox)
        if email_service:
            emails = get_master_sandbox_emails(sandbox)
            email_service.send_error_email(emails, sandbox.id, get_exc_info=True)
        raise


def run_async_power_on_refresh_ip(sandbox, deployed_apps):
    """
    :param Sandbox sandbox:
    :param List[ReservedResourceInfo] deployed_apps:
    """
    if len(deployed_apps) == 0:
        sandbox.logger.info('No resources to power on')
        return

    pool = ThreadPool(len(deployed_apps))

    async_results = [pool.apply_async(power_on_refresh_ip, (sandbox, resource)) for resource in deployed_apps]

    pool.close()
    pool.join()

    for async_result in async_results:
        res = async_result.get()
        if not res[0]:
            raise Exception("Sandbox is Active with Errors - " + res[1])


def power_on_refresh_ip(sandbox, deployed_app):
    """
    :param Sandbox sandbox:
    :param ReservedResourceInfo deployed_app:
    :return:
    """
    try:
        sandbox.logger.info(f"Executing 'Power On' on deployed app {deployed_app.Name} in sandbox {sandbox.id}")

        livestatus = sandbox.automation_api.GetResourceLiveStatus(deployed_app.Name)
        if livestatus.liveStatusName == 'Online':
            sandbox.logger.info(f'Deployed app {deployed_app.Name} already powered on. Nothing to do.')
            return True, ""

        sandbox.automation_api.ExecuteResourceConnectedCommand(sandbox.id, deployed_app.Name,
                                                               "PowerOnHidden",
                                                               "remote_hidden_power_on")
    except Exception as e:
        sandbox.logger.exception(f"Error powering on deployed app {deployed_app.Name} in sandbox {sandbox.id}. Error: ")
        sandbox.automation_api.SetResourceLiveStatus(deployed_app.Name, "Error", "Powering on has failed")
        return False, f"Error powering on deployed app {deployed_app.Name}"

    try:
        sandbox.logger.info(f"Executing 'Refresh IP' on deployed app {deployed_app.Name} in sandbox {sandbox.id}")

        sandbox.automation_api.ExecuteResourceConnectedCommand(
            sandbox.id, deployed_app.Name, "remote_refresh_ip", "remote_connectivity")
    except Exception as exc:
        sandbox.logger.error(f"Error refreshing IP on deployed app {deployed_app.Name} in sandbox {sandbox.id}. "
                             f"Error: {str(exc)}")
        sandbox.automation_api.SetResourceLiveStatus(deployed_app.Name, "Error", "Obtaining IP has failed")
        return False, f"Error refreshing IP deployed app {deployed_app.Name}. Error: {str(exc)}"

    return True, ""


def refresh_vm_details(sandbox, deployed_apps):
    """
    :param Sandbox sandbox:
    :param List[ReservedResourceInfo] deployed_apps:
    """
    try:
        if len(deployed_apps) > 0:
            deployed_app_names = list(map(lambda x: x.Name, deployed_apps))
            sandbox.logger.info('Refreshing VM Details for {0}'.format(', '.join(deployed_app_names)))
            sandbox.automation_api.RefreshVMDetails(sandbox.id, deployed_apps)
    except Exception:
        sandbox.logger.exception("Failed to refresh VM details: ")
        raise Exception("Failed to refresh VM Details")
