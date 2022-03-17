"""Provide templating for git hooks."""

import os
import shutil
from typing import TYPE_CHECKING, List

from invoke import Collection, task

# from proman_workflows import git, filesystem, templates
from . import config

if TYPE_CHECKING:
    from invoke import Context


@task(name='list')
def index(ctx):  # type: (Context) -> List[str]
    """List git hooks."""
    hooks = [
        x
        for x in os.listdir(os.path.join(ctx.repo_dir, 'hooks'))
        if not x.endswith('sample')
    ]
    for hook in hooks:
        print(hook)
    return hooks


@task
def setup(
    ctx, name='pre-commit', update=False
):  # type: (Context, str, bool) -> None
    """Create git hook."""
    path = os.path.join(ctx.hooks_dir, name)
    if update or not os.path.exists(path):
        data = {
            'executable': shutil.which('project'),
            'hook': name,
        }
        config.dump(
            ctx,
            data,
            template_name='githooks',
            dest=path,
            executable=True,
            update=update,
        )


@task
def remove(ctx, name='pre-commit'):  # type: (Context, str) -> None
    """Remove git hook."""
    path = os.path.join(ctx.hooks_dir, name)
    if os.path.exists(path):
        os.remove(path)


@task
def execute(ctx, name):  # type: (Context, str) -> None
    """Execute task for githook."""
    # TODO setup tasks config for executor
    print(f"{name} hook executed")


namespace = Collection(execute, index, remove, setup)
