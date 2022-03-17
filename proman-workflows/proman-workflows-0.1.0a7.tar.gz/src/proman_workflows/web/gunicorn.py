# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Provide App Task-Runner."""

import os
import textwrap
from typing import TYPE_CHECKING

from invoke import task

if TYPE_CHECKING:
    from invoke import Context


@task
def start(
    ctx, hostname='localhost', port=8080, workers=4
):  # type: (Context, str, int, int) -> None
    """Start webapp."""
    with ctx.cd(ctx.webapp_dir):
        ctx.run(
            textwrap.dedent(
                f"""\
                gunicorn app:app \
                --pid={os.getcwd()}/.pid \
                --bind={hostname}:{port} \
                --workers={workers} \
                --reload
            """
            ),
            disown=True,
        )


@task
def stop(ctx):  # type: (Context) -> None
    """Stop webapp."""
    ctx.run('pkill gunicorn')
