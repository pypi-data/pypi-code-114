# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Provide documentation task-runner for Sphinx."""

from typing import TYPE_CHECKING

from invoke import Collection, task

if TYPE_CHECKING:
    from invoke import Context


@task
def build(
    ctx,  # type: Context
):  # type: (...) -> None
    """Build documentation site."""
    pass


@task
def start(
    ctx,  # type: Context
):  # type: (...) -> None
    """Start docsite."""
    pass


@task
def stop(ctx):  # type: (Context) -> None
    """Stop docsite."""
    pass


namespace = Collection(build, start, stop)
