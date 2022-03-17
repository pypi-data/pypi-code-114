# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Quality Assurance Task-Runner."""

from typing import TYPE_CHECKING

from invoke import Collection, task

if TYPE_CHECKING:
    from invoke import Context


@task
def run(ctx, path='.'):  # type: (Context, str) -> None
    """Check project source types."""
    with ctx.cd(ctx.project_dir):
        ctx.run(f"mypy {path}")


namespace = Collection(run)
