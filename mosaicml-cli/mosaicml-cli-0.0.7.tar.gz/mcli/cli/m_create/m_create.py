""" mcli create Commands """
import argparse

from mcli.cli.m_create.create_environment import configure_environment_argparser
from mcli.cli.m_create.create_secret import configure_secret_argparser
from mcli.platform.environment import create_new_environment_variable
from mcli.platform.platform_create import create_new_platform
from mcli.platform.secrets import create_new_secret
from mcli.projects.project_create import create_new_project


def create(**kwargs,) -> int:
    del kwargs
    mock_parser = configure_argparser(parser=argparse.ArgumentParser())
    mock_parser.print_help()
    return 0


def configure_argparser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    subparsers = parser.add_subparsers()
    parser.set_defaults(func=create)

    project_parser = subparsers.add_parser('project', aliases=['p'], help='Create a project')
    project_parser.set_defaults(func=create_new_project)

    platform_parser = subparsers.add_parser('platform', aliases=['pl'], help='Create a platform')
    platform_parser.set_defaults(func=create_new_platform)

    environment_parser = subparsers.add_parser(
        'env',
        aliases=['environment_variable'],
        help='Create an Environment Variable',
    )
    configure_environment_argparser(environment_parser)
    environment_parser.set_defaults(func=create_new_environment_variable)

    secrets_parser = subparsers.add_parser(
        'secrets',
        aliases=['secret'],
        help='Create a Secret',
    )
    configure_secret_argparser(secrets_parser, secret_handler=create_new_secret)
    secrets_parser.set_defaults(func=create_new_secret)

    return parser


def add_create_argparser(subparser: argparse._SubParsersAction,) -> argparse.ArgumentParser:
    create_parser: argparse.ArgumentParser = subparser.add_parser(
        'create',
        aliases=['cr'],
        help='Configure your local project',
    )
    create_parser = configure_argparser(parser=create_parser)
    return create_parser
