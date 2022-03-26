""" mcli create secret Entrypoint """
import argparse
from textwrap import dedent
from typing import Callable

create_secret_helptext = dedent("""
There are a couple of different secret types supported:

To create a docker-registry secret run:

> mcli create secret docker_registry <secret_name> <docker_user>

""")


def configure_secret_argparser(
    parser: argparse.ArgumentParser,
    secret_handler: Callable,
) -> None:
    # TODO(HEK-165, averylamp): Add helptext for all argparse options (for now it'll be minimal)

    def add_secret_name_arg(parser: argparse.ArgumentParser):
        parser.add_argument(
            'secret_name',
            type=str,
            nargs='?',
            help='What you will refer to the secret variable as. Must be unique',
        )

    subparser = parser.add_subparsers()
    docker_registry_parser = subparser.add_parser('docker_registry', help='Create a Docker Registry Secret')
    add_secret_name_arg(docker_registry_parser)
    docker_registry_parser.add_argument('--docker-username', required=False)
    docker_registry_parser.add_argument('--docker-password', required=False)
    docker_registry_parser.add_argument('--docker-email', required=False)
    docker_registry_parser.add_argument('--docker-server', required=False)
    docker_registry_parser.set_defaults(func=secret_handler, secret_type='docker_registry')

    ssh_parser = subparser.add_parser('ssh', help='Create a SSH Secret')
    add_secret_name_arg(ssh_parser)
    ssh_parser.add_argument('--ssh-private-key', required=False)
    ssh_parser.add_argument('--mount-path', required=False)
    ssh_parser.set_defaults(func=secret_handler, secret_type='ssh')

    generic_mounted_parser = subparser.add_parser('generic_mounted', help='Create a Generic Mounted Secret')
    add_secret_name_arg(generic_mounted_parser)
    generic_mounted_parser.add_argument('--mount-path', required=False)
    generic_mounted_parser.add_argument('--value', required=False)
    generic_mounted_parser.set_defaults(func=secret_handler, secret_type='generic_mounted')

    generic_env_parser = subparser.add_parser(
        'generic_environment',
        help='Create a Generic Environment Variable Secret',
    )
    add_secret_name_arg(generic_env_parser)
    generic_env_parser.add_argument('--env-key', required=False)
    generic_env_parser.add_argument('--value', required=False)
    generic_env_parser.set_defaults(func=secret_handler, secret_type='generic_environment')

    s3_cred_parser = subparser.add_parser('s3', help='Create an S3 Credentials Secret')
    add_secret_name_arg(s3_cred_parser)
    s3_cred_parser.add_argument('--config-file', required=False)
    s3_cred_parser.add_argument('--credentials-file', required=False)
    s3_cred_parser.set_defaults(func=secret_handler, secret_type='s3_credentials')
