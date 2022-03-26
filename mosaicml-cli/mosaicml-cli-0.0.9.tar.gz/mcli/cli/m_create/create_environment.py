""" mcli create env Entrypoint """
import argparse
from textwrap import dedent

create_env_helptext = dedent("""
To create an environment variable run:

> mosaic create env <variable_name> <ENV_KEY> <env_value>

Which will create an environment variable with the following:

ENV_KEY=env_value

Note: `variable_name` must be unique and will be the identifier
""")


def configure_environment_argparser(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        'variable_name',
        type=str,
        nargs='?',
        help='What you will refer to the environment variable as. Must be unique',
    )
    parser.add_argument(
        'key',
        type=str,
        nargs='?',
        help='The ENV Variable KEY in KEY=VALUE',
    )
    parser.add_argument(
        'value',
        type=str,
        nargs='?',
        help='The ENV Variable VALUE in KEY=VALUE',
    )
