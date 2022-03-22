import os
import traceback

import typer

from ingeniictl.clients import pulumi as pulumi_client
from ingeniictl.clients.logger import log_client
from .main import app


@app.command()
def disable_resource_protection(
        pulumi_stack_name: str = typer.Argument(
            ..., help="Name of the Pulumi stack. e.g. 'ingenii/dev' "
        ),
        pulumi_project_dir: str = typer.Option(
            "",
            help="This is the directory that has the 'Pulumi.yaml' file. Defaults to current working directory.",
        ),
        pulumi_locks_only: bool = typer.Option(
            False,
            help="Remove Pulumi resource protection",
        ),
        cloud_locks_only: bool = typer.Option(
            False,
            help="Remove cloud resource protection. e.g. Azure Management locks",
        ),
) -> None:
    if not pulumi_project_dir:
        pulumi_project_dir = os.getcwd()

    try:
        if pulumi_locks_only:
            pulumi_client.remove_protect_flags(pulumi_stack_name, pulumi_project_dir)
        elif cloud_locks_only:
            pulumi_client.remove_azure_management_locks(
                pulumi_stack_name, pulumi_project_dir
            )
        else:
            pulumi_client.remove_protect_flags(pulumi_stack_name, pulumi_project_dir)
            pulumi_client.remove_azure_management_locks(
                pulumi_stack_name, pulumi_project_dir
            )
        log_client.ok("Resource protection disabled successfully.")
    except:
        log_client.err("Unable to disable the resource protection.")
        log_client.err(traceback.format_exc())
