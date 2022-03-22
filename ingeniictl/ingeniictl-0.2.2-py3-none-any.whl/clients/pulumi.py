import copy
import json
import os
import subprocess
from typing import Any

import ingeniictl.config as config
from ingeniictl.clients.logger import log_client


def run(args: list, cwd: str = None) -> str:
    if cwd:
        args.append("--cwd")
        args.append(cwd)
    run_command = ["pulumi"] + args

    if config.DEBUG:
        log_client.debug(f"pulumi run command: {run_command}")

    result = str(subprocess.run(run_command, stderr=subprocess.STDOUT, stdout=subprocess.PIPE).stdout.decode("utf-8"))

    if config.DEBUG:
        log_client.debug(f"pulumi run command output: {result}")

    return result


def export_stack(name: str, cwd: str = None) -> str:
    cmd = ["stack", "export", "--stack", name]
    stack = run(cmd, cwd)
    if not stack:
        log_client.err(f"Stack name {name} not found.")
        exit(1)
    return stack


def import_stack(name: str, input_file: str, cwd: str = None) -> None:
    cmd = ["stack", "import", "--stack", name, "--file", input_file]
    run(cmd, cwd)


def get_stack_resources(stack_name: str, cwd: str = None) -> Any:
    stack = export_stack(stack_name, cwd)
    stack_obj = json.loads(stack)

    if not stack_obj["deployment"].get("resources"):
        log_client.info(f"No resources found on stack: {stack_name}")
        return []

    return stack_obj["deployment"]["resources"]


def destroy_stack_resources(name: str, cwd: str = None) -> None:
    cmd = ["destroy", "--stack", name, "--yes", "--skip-preview"]
    run(cmd, cwd)


def delete_stack(name: str, cwd: str = None) -> None:
    cmd = ["stack", "rm", "--stack", name, "--yes", "--force"]
    result = run(cmd, cwd)
    if "[403]" in result:
        log_client.err(f"Unable to delete stack {name}. Insufficient permissions.")
        exit(1)
    elif "has been removed" in result:
        log_client.ok(f"Stack {name} has been deleted.")
    else:
        log_client.info(f"Attempting to delete the stack {name} resulted in {result}.")


def remove_protect_flags(stack_name: str, cwd: str = None) -> None:
    """Removes Pulumi protect flags which allows the resources to be deleted."""

    log_client.info("Removing Pulumi resource protection flags...")
    cmd = ["state", "unprotect", "--all", "--yes", "--stack", stack_name]
    result = run(cmd, cwd)
    if "successfully unprotected" not in result:
        log_client.err(f"Unable to remove Pulumi protection flags for stack {stack_name}. "
                       + "Make sure the stack name is correct.")
        exit(1)
    log_client.ok("Protection flags removed.")


def remove_azure_management_locks(stack_name: str, cwd: str = None) -> None:
    """Removes Azure Management Locks resources which will allow the rest of the resources to be deleted."""

    log_client.info("Looking for Azure Management Locks...")

    stack_resources = get_stack_resources(stack_name, cwd)

    found_locks = []

    for resource in stack_resources:
        urn = resource["urn"]

        if "azure-native:authorization:ManagementLock" in urn:
            found_locks.append("--target")
            found_locks.append(urn)

    # Do not _run the 'remove_command' unless we have management locks to remove.
    if len(found_locks) >= 2:
        log_client.info(f"Removing {int(len(found_locks) / 2)} Azure Management Locks...")
        cmd = [
                  "destroy",
                  "--yes",
                  "--skip-preview",
                  "--stack",
                  stack_name,
              ] + found_locks
        run(cmd, cwd)
        log_client.ok("All Azure Management Locks removed.")
    else:
        log_client.ok("No Azure Management Locks found.")


def destroy_stack(stack_name: str, cwd: str = None) -> Any:
    log_client.info(f"Destroying Pulumi stack {stack_name}...")

    stack_obj = json.loads(export_stack(stack_name, cwd))

    if stack_obj["deployment"].get("resources"):
        filtered_stack_obj = dict(copy.deepcopy(stack_obj))

        # Remove all resources from the stack copy.
        # We'll be adding only the resources Pulumin has to destroy.
        filtered_stack_obj["deployment"]["resources"] = []

        for resource in stack_obj["deployment"]["resources"]:

            # ID based filtering
            if resource.get("id"):
                resource_id = resource["id"].lower()

                # Filter out child resources that are deployed in a resource group
                if "/resourcegroups/" in resource_id and "/providers/" in resource_id:
                    continue

            # Type based filtering
            if resource.get("type"):
                resource_type = resource["type"].lower()

                # Filter out child resources of Azure Databricks workspaces.
                if "databricks:" in resource_type:
                    continue
                if "pulumi:providers:databricks" in resource_type:
                    continue

                # Filter out child resources of Azure storage accounts.
                if "azure:storage" in resource_type:
                    continue

                # Filter out child resources of Azure DevOps Project resource.
                if "azuredevops:" in resource_type and "index/project:" not in resource_type:
                    continue

            # If the resource was not filtered out, it means we should include it in our final stack state
            filtered_stack_obj["deployment"]["resources"].append(resource)

        # Save the new (filtered) stack into a new file
        filtered_stack_file = os.path.join(os.getcwd(), "pulumi-filtered-stack.json")
        with open(filtered_stack_file, "w") as filtered_file:
            filtered_file.write(json.dumps(filtered_stack_obj))

        # Import stack to Pulumi
        import_stack(stack_name, filtered_stack_file, cwd)

        # Run Pulumi destroy
        destroy_stack_resources(stack_name, cwd)

    # Delete Pulumi stack
    delete_stack(stack_name, cwd)
