import logging
from distutils.command.build import build

import click
from rich import print_json

from ..build.service_foundry_client import ServiceFoundryServiceClient
from .util import handle_exception

logger = logging.getLogger(__name__)


def get_deployment_command():
    @click.group(name="deployment", help="servicefoundry deployment list|show|delete ")
    def deployment():
        pass

    @deployment.command(name="list", help="list deployment")
    def list():
        try:
            tfs_client = ServiceFoundryServiceClient.get_client()
            spaces = tfs_client.list_workspace()
            print_json(data=spaces)
        except Exception as e:
            handle_exception(e)

    @deployment.command(name="show", help="show deployment metadata")
    @click.argument("deployment_id")
    def get(deployment_id):
        try:
            tfs_client = ServiceFoundryServiceClient.get_client()
            deployment = tfs_client.get_deployment(deployment_id)
            print_json(data=deployment)
        except Exception as e:
            handle_exception(e)

    @deployment.command(name="remove", help="remove deployment")
    @click.argument("workspace_name")
    def remove(workspace_name):
        try:
            tfs_client = ServiceFoundryServiceClient.get_client()
            space = tfs_client.remove_workspace(workspace_name)
            print_json(data=space)
        except Exception as e:
            handle_exception(e)

    @deployment.command(name="update", help="update workspace")
    def update():
        click.echo("Hello world")

    return deployment
