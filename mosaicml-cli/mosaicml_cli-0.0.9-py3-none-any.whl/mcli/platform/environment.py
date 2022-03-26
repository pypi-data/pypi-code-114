""" Platform Environment Variables """
import argparse
from typing import Optional

from mcli.cli.m_create.create_environment import configure_environment_argparser, create_env_helptext
from mcli.config import MCLIConfig
from mcli.config_objects import MCLIEnvVar


def create_new_environment_variable(
    variable_name: Optional[str] = None,
    key: Optional[str] = None,
    value: Optional[str] = None,
    **kwargs,
) -> int:
    del kwargs

    def print_env_parser_usage() -> None:
        parser = argparse.ArgumentParser()
        configure_environment_argparser(parser)
        parser.print_usage()

    if variable_name is None or key is None or value is None:
        print('Missing required positional arguments')
        print_env_parser_usage()
        print(create_env_helptext)
        return 1

    conf = MCLIConfig.load_config()
    existing_variables = conf.environment_variables

    if variable_name in {x.name for x in existing_variables}:
        print(
            f'Environment Variable Name: {variable_name} already taken.'
            ' Please choose a unique Variable Name. ',
            ' To see all env variables `mcli get env`',
        )
        print_env_parser_usage()
        return 1
    if key in {x.env_key for x in existing_variables}:
        print(f'Environment Variable Key: {key} already taken.'
              ' Please choose a unique Variable Key.'
              ' To see all env variables `mcli get env`')
        print_env_parser_usage()
        return 1

    new_env_item = MCLIEnvVar(
        name=variable_name,
        env_key=key,
        env_value=value,
    )

    conf.environment_variables.append(new_env_item)
    conf.save_config()

    return 0
