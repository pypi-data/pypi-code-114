"""Provide git management capabilities."""

from typing import TYPE_CHECKING

from invoke import Collection, task
from pygit2 import Repository

from .config import config_tasks

# from .submodule import submodule_tasks
# import pyinputplus as pyip


if TYPE_CHECKING:
    from invoke import Context


@task
def repo(ctx):  # type: (Context) -> Repository
    """Set git as SCM."""
    return Repository(ctx.repo_dir)


namespace = Collection()
namespace.add_collection(config_tasks, 'config')
# namespace.add_collection(submodule_tasks, 'submodule')
