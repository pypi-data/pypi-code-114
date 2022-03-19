import logging

import click
from rich import print_json

from ..build.service_foundry_client import ServiceFoundryServiceClient
from .util import handle_exception

logger = logging.getLogger(__name__)


def get_workspace_command():
    @click.group(
        name="workspace", help="servicefoundry workspace list|show|create|update "
    )
    def workspace():
        pass

    @workspace.command(name="list", help="list workspaces")
    def list():
        try:
            tfs_client = ServiceFoundryServiceClient.get_client()
            spaces = tfs_client.list_workspace()
            print_json(data=spaces)
        except Exception as e:
            handle_exception(e)

    @workspace.command(name="show", help="show workspace metadata")
    @click.argument("workspace_name")
    def get(workspace_name):
        try:
            tfs_client = ServiceFoundryServiceClient.get_client()
            space = tfs_client.get_workspace(workspace_name)
            print_json(data=space)
        except Exception as e:
            handle_exception(e)

    @workspace.command(name="remove", help="remove workspace")
    @click.argument("workspace_name")
    def remove(workspace_name):
        try:
            tfs_client = ServiceFoundryServiceClient.get_client()
            space = tfs_client.remove_workspace(workspace_name)
            print_json(data=space)
        except Exception as e:
            handle_exception(e)

    @workspace.command(name="create", help="create new workspace")
    @click.argument("cluster_name")
    @click.argument("space_name")
    def create(cluster_name, space_name):
        try:
            tfs_client = ServiceFoundryServiceClient.get_client()
            space = tfs_client.create_workspace(cluster_name, space_name)
            print_json(data=space)
        except Exception as e:
            handle_exception(e)

    @workspace.command(name="update", help="update workspace")
    def update():
        click.echo("Hello world")

    return workspace
