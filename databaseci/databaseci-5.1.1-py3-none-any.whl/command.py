# Copyright DatabaseCI Pty Ltd 2022

import json
from pathlib import Path

import click

# from .do import do_check, do_copy, do_inspect
from databaseciservices.command import init_commands


@click.group()
def cli():
    pass


init_commands(cli)
