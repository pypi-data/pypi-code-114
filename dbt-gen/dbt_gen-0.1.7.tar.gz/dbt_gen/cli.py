from argparse import ArgumentParser

from . import generate_source_yaml
from . import generate_base_model
from . import generate_dbt
from . import generate_base_test
from . import get_template


def add_parser(sub_parsers, name, config_func):
    subparser = sub_parsers.add_parser(name)
    config_func(subparser)
    return subparser


def cli():
    parser = ArgumentParser()
    sub_parsers = parser.add_subparsers(help="Action")

    add_parser(sub_parsers, "generate_source", generate_source_yaml.config_parser)
    add_parser(sub_parsers, "generate_base_model", generate_base_model.config_parser)
    add_parser(sub_parsers, "generate_dbt", generate_dbt.config_parser)
    add_parser(sub_parsers, "generate_base_test", generate_base_test.config_parser)
    add_parser(sub_parsers, "get_template", get_template.config_parser)

    args = parser.parse_args()

    if "func" in args:
        args.func(args)
    else:
        print("Please choose action\n")
        parser.print_help()


def main():
    cli()
