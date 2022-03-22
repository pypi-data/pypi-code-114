import os

import typer

from ingeniictl.clients import pulumi
from .main import app


@app.command()
def destroy(
        pulumi_stack_name: str = typer.Argument(
            ..., help="Name of the Pulumi stack. e.g. 'ingenii/dev' "
        ),
        pulumi_project_dir: str = typer.Option(
            "",
            help="This is the directory that has the 'Pulumi.yaml' file. Defaults to current working directory.",
        ),
        skip_resource_protection_removal: bool = typer.Option(
            False,
            help="Skip Pulumi and Cloud provider resource protection removal.",
        ),
) -> None:
    if not pulumi_project_dir:
        pulumi_project_dir = os.getcwd()

    if not skip_resource_protection_removal:
        pulumi.remove_protect_flags(pulumi_stack_name, pulumi_project_dir)
        pulumi.remove_azure_management_locks(pulumi_stack_name, pulumi_project_dir)

    pulumi.destroy_stack(pulumi_stack_name, pulumi_project_dir)
