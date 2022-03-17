# -*- coding: utf-8 -*-
# copyright: (c) 2021 by Jesse Johnson.
# license: MPL 2.0, see LICENSE for more details.
"""Acceptance Tests task-runner using behave."""

from typing import TYPE_CHECKING

from invoke import Collection, task

if TYPE_CHECKING:
    from invoke import Context


@task
def run(
    ctx,  # type: Context
):  # type: (...) -> None
    """Perform unit tests."""
    print('behave stub')


namespace = Collection(run)
