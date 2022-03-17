# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Build packages using flit."""

from typing import TYPE_CHECKING, Optional

from invoke import Collection, task

if TYPE_CHECKING:
    from invoke import Context


@task
def build(
    ctx, kind=None, no_setup_py=True
):  # type: (Context, Optional[bool], bool) -> None
    """Build wheel package."""
    args = []
    if kind:
        args.append(f"--format={kind}")
    if no_setup_py:
        args.append('--no-setup-py')
    ctx.run(f"flit build {' '.join(args)}")


@task
def install(
    ctx,  # type: Context
    kind='symlink',  # type: str
    user=None,  # type: Optional[bool]
    env=None,  # type: Optional[bool]
    deps=None,  # type: Optional[str]
    extras=None,  # type: Optional[str]
):  # type: (...) -> None
    """Install within environment."""
    args = []
    if kind == 'symlink':
        args.append('--symlink')
    elif kind == 'pth-file':
        args.append('--pth-file')
    if user is not None:
        args.append(f"--user={user}")
    if env is not None:
        args.append(f"--env={env}")
    if deps:
        args.append(f"--deps={deps}")
    if extras:
        args.append(f"--extras={extras}")
    ctx.run(f"flit install {' '.join(args)}")


@task
def publish(
    ctx,
    kind=None,
    no_setup_py=True,
    repository=None,
):  # type: (Context, Optional[str], bool, Optional[str]) -> None
    """Publish project distribution."""
    args = []
    if kind:
        args.append(f"--format={kind}")
    if no_setup_py:
        args.append('--no-setup-py')
    if repository:
        args.append(f"--repository={repository}")
    ctx.run(f"flit publish {' '.join(args)}")


tasks = Collection(build, install, publish)
