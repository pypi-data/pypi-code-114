import logging

import click
from rich.console import Console
from rich import print_json

from .util import handle_exception
from ..build.service_foundry_client import (
    ServiceFoundryServiceClient,
)

console = Console()
logger = logging.getLogger(__name__)


def get_service_command():

    @click.group(name='service', help="servicefoundry service list|show|remove ")
    def workspace():
        pass

    @workspace.command(name='list', help='list service')
    def list():
        try:
            tfs_client = ServiceFoundryServiceClient.get_client()
            services = tfs_client.list_service()
            print_json(data=services)
        except Exception as e:
            handle_exception(e)

    @workspace.command(name='show', help='show service metadata')
    @click.argument('service_id')
    def get(service_id):
        try:
            tfs_client = ServiceFoundryServiceClient.get_client()
            service = tfs_client.get_service(service_id)
            print_json(data=service)
        except Exception as e:
            handle_exception(e)

    @workspace.command(name='remove', help='remove service')
    @click.argument('service_id')
    def remove(service_id):
        try:
            tfs_client = ServiceFoundryServiceClient.get_client()
            tfs_client.remove_service(service_id)
        except Exception as e:
            handle_exception(e)

    return workspace
