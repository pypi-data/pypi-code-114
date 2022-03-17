# -*- coding: utf-8 -*-
"""Publish executable using briefcase."""

from typing import TYPE_CHECKING, Optional

from invoke import Collection, task

if TYPE_CHECKING:
    from invoke import Context


@task
def build(
    ctx, update=False, docker=True, verbose=False
):  # type: (Context, bool, bool, bool) -> None
    """Build executable."""
    args = ['--no-input']
    if update:
        args.append('--update')
    if not docker or ctx.container.runtime != 'docker':
        args.append('--no-docker')
    if verbose:
        args.append('--verbosity')
    ctx.run(f"poetry build {' '.join(args)}")


@task
def package(
    ctx,  # type: Context
    kind=None,  # type: Optional[str]
    identity=None,  # type: Optional[str]
    sign=True,  # type: bool
    adhoc_sign=False,  # type: bool
    docker=True,  # type: bool
    verbose=False,  # type: bool
):  # type: (...) -> None
    """Create executable package."""
    args = ['--no-input']
    if kind:
        args.append(f"--packaging-format {kind}")
    if identity:
        args.append(f"--identity {identity}")
    if not sign:
        args.append('--no-sign')
    if adhoc_sign:
        args.append('--adhoc-sign')
    if not docker or ctx.container.runtime != 'docker':
        args.append('--no-docker')
    if verbose:
        args.append('--verbosity')


namespace = Collection(build, package)
