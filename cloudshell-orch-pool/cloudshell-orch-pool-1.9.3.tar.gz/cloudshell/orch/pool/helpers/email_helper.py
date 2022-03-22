import logging

from cloudshell.api.cloudshell_api import CloudShellAPISession
from cloudshell.email import EmailService, EmailConfig
from cloudshell.workflow.orchestration.sandbox import Sandbox
from typing import List

from cloudshell.orch.pool.helpers.master_sandbox import get_master_sandbox, get_mgmt_resource


def get_email_service(sandbox: Sandbox) -> EmailService:
    """
    :returns email service from the first found email provider if there are multiple master sandboxes found
    """
    master_sandboxes = get_master_sandbox(sandbox)
    for master_sandbox in master_sandboxes:
        vm_pool_mgmt_resource = get_mgmt_resource(master_sandbox.Resources)
        email_provider_name = sandbox.automation_api.GetAttributeValue(
            vm_pool_mgmt_resource.Name, f"{vm_pool_mgmt_resource.ResourceModelName}.Email Provider").Value

        if email_provider_name:
            email_config = EmailConfig.create_from_email_config_resource(sandbox.automation_api, email_provider_name)
            return EmailService(email_config, sandbox.logger, sandbox.automation_api)

    return None


def get_master_sandbox_emails(sandbox: Sandbox) -> List[str]:
    """
    gets emails from all master sandboxes and combines into a single list returning an emails list without
    duplicates
    """
    master_sandboxes = get_master_sandbox(sandbox)
    emails = []
    for master_sandbox in master_sandboxes:
        emails.extend(
            get_emails_list_for_sandbox_users(sandbox.logger, sandbox.automation_api, master_sandbox.Id))
    # return emails list without duplicates
    return list(set(emails))


def get_emails_list_for_sandbox_users(logger: logging.Logger, api: CloudShellAPISession, sandbox_id: str) -> List[str]:
    # get owner and permitted users of master sandbox
    admin_users = get_sandbox_users(api, sandbox_id)

    # get emails for active all users of the master sandbox with valid emails
    emails = []
    for user_name in admin_users:
        user_details = api.GetUserDetails(user_name)
        if user_details.IsActive and EmailService.is_valid_email_address(user_details.Email):
            logger.info(f"User {user_details.Email} is active and has a valid notifications address")
            emails.append(user_details.Email)
        else:
            logger.info(f"User {user_details.Email} is not active or has an invalid notifications address")

    return list(set(emails))


def get_sandbox_users(api: CloudShellAPISession, sandbox_id: str) -> List[str]:
    reservation_info = api.GetReservationDetails(sandbox_id).ReservationDescription
    users = [reservation_info.Owner]
    users.extend(reservation_info.PermittedUsers)
    return list(set(users))
