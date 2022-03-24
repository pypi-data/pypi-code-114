""" CLI Get options"""
import argparse
from typing import Any, Dict, List, Optional, Tuple, cast

from rich.table import Table

from mcli.cli.m_get.display import MCLIGetDisplay, OutputDisplay, create_display_table
from mcli.cli.m_get.runs import get_runs_argparser
from mcli.config import MCLIConfig, MCLIConfigError
from mcli.config_objects import MCLIPlatform
from mcli.platform.platform_info import get_platform_list
from mcli.projects.project_info import get_projects_list
from mcli.utils.utils_rich import console


def get_entrypoint(parser, **kwargs) -> int:
    del kwargs
    parser.print_help()
    return 0


class MCLIPlatformDisplay(MCLIGetDisplay):
    """`mcli get platforms` display class
    """

    def __init__(self, platforms: List[MCLIPlatform]):
        self.platforms = platforms

    def to_table(self) -> Table:
        column_names = ['CONTEXT', 'NAMESPACE']
        unzipped = list(zip(*[(x.name, x.kubernetes_context, x.namespace) for x in self.platforms]))
        names = cast(List[str], list(unzipped[0]))
        data = cast(List[Tuple[str, str]], list(zip(*unzipped[1:])))
        return create_display_table(names=names, columns=data, column_names=column_names)

    def to_name(self) -> List[str]:
        return [pl.name for pl in self.platforms]

    def to_json(self) -> List[Dict[str, Any]]:
        return [pl.to_dict() for pl in self.platforms]


def get_platforms(output: OutputDisplay = OutputDisplay.TABLE, **kwargs) -> int:
    del kwargs

    try:
        platforms = get_platform_list()
    except MCLIConfigError:
        platforms = []

    if not platforms:
        print('None')
        return 0

    display = MCLIPlatformDisplay(platforms)
    display.print(output)
    return 0


def get_environment_variables(**kwargs) -> int:
    del kwargs

    conf: MCLIConfig = MCLIConfig.load_config()
    var_names = [f'Name: {x.name}, Key: {x.env_key}' for x in conf.environment_variables]
    print('ENV Variables:')
    if var_names:
        print('\n'.join(var_names))
    else:
        print('None')
    return 0


def get_secrets(output: OutputDisplay = OutputDisplay.TABLE, **kwargs) -> int:
    del kwargs

    conf: MCLIConfig = MCLIConfig.load_config()
    if not conf.secrets:
        print('None')
        return 0
    if output == OutputDisplay.TABLE:
        column_names = ['TYPE']
        unzipped = list(zip(*[(x.name, x.secret_type.value) for x in conf.secrets]))
        names = cast(List[str], list(unzipped[0]))
        data = cast(List[Tuple[str]], list(zip(*unzipped[1:])))
        output_table = create_display_table(names=names, columns=data, column_names=column_names)
        console.print(output_table)
    return 0


def get_projects(**kwargs) -> int:
    del kwargs
    all_projects = sorted(get_projects_list(), reverse=True)
    print('Projects:')

    for project in all_projects:
        print(f'Project: {project.project}  (last used {project.get_last_accessed_string()})')
    if len(all_projects) == 0:
        print('None')

    return 0


def configure_argparser(parser: argparse.ArgumentParser,
                        parents: List[argparse.ArgumentParser]) -> argparse.ArgumentParser:
    subparsers = parser.add_subparsers(title='gettable objects',
                                       description='Get information on ',
                                       help='Some extra help',
                                       metavar='OBJECT')
    parser.set_defaults(func=get_entrypoint, parser=parser)

    projects_parser = subparsers.add_parser('projects', aliases=['project'], help='Get Project')
    projects_parser.set_defaults(func=get_projects)
    platform_parser = subparsers.add_parser('platforms', aliases=['platform'], help='Get Platforms', parents=parents)
    platform_parser.set_defaults(func=get_platforms)
    environment_parser = subparsers.add_parser('env', aliases=['environment'], help='Get Environment Variables')
    environment_parser.set_defaults(func=get_environment_variables)
    secrets_parser = subparsers.add_parser('secrets', aliases=['secret'], help='Get Secrets')
    secrets_parser.set_defaults(func=get_secrets)
    get_runs_argparser(subparsers)

    return parser


def add_get_argparser(subparser: argparse._SubParsersAction,
                      parents: Optional[List[argparse.ArgumentParser]] = None) -> argparse.ArgumentParser:
    """Adds the get parser to a subparser

    Args:
        subparser: the Subparser to add the Get parser to
    """
    if not parents:
        parents = []

    # Add common `get` arguments to a parent parser
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument('--output',
                        type=OutputDisplay,
                        choices=list(OutputDisplay),
                        default=OutputDisplay.TABLE,
                        metavar='FORMAT',
                        help=f'Output display format. Should be one of {list(OutputDisplay)}')
    parents.append(common)

    get_parser: argparse.ArgumentParser = subparser.add_parser(
        'get',
        aliases=['g'],
        help='Get info about objects created with mcli',
        parents=parents,
    )
    get_parser = configure_argparser(parser=get_parser, parents=parents)
    return get_parser
