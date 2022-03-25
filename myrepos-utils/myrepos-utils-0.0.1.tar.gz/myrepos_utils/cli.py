#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (c) Michel Alexandre Salim
#
# Fedora-License-Identifier: GPLv2+
# SPDX-2.0-License-Identifier: GPL-2.0+
# SPDX-3.0-License-Identifier: GPL-2.0-or-later
#
# This program is free software.
# For more information on the license, see COPYING.md.
# For more information on free software, see
# <https://www.gnu.org/philosophy/free-sw.en.html>.

import click
import json
import sys
from . import utils


@click.group()
def cli():
    pass


@cli.command(help="find repo directories tracked by myrepos")
@click.argument("query", nargs=-1)
def find(query: list[str]):
    import os

    matches = utils.find_repo(query)
    for repo in matches:
        click.echo(repo)
