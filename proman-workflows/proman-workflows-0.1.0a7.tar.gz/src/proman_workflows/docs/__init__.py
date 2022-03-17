# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Provide documentation task-runner."""

from typing import TYPE_CHECKING, Optional

from invoke import task

from ..collection import Collection

if TYPE_CHECKING:
    from invoke import Context


@task(iterable='ignore_decorators')
def style(
    ctx,  # type: Context
    explain=False,  # type: bool
    source=False,  # type: bool
    count=False,  # type: bool
    configpath=None,  # type: Optional[str]
    match=None,  # type: Optional[str]
    match_dir=None,  # type: Optional[str]
    ignore_decorators=None,  # type: Optional[str]
    debug=False,  # type: bool
    verbose=False,  # type: bool
    version=False,  # type: bool
):  # type: (...) -> None
    """Check code for documentation errors."""
    args = []
    if configpath:
        args.append(f"--config={configpath}")
    if explain:
        args.append('--explain')
    if source:
        args.append('--source')
    if count:
        args.append('--count')
    if match:
        args.append(f"--match={match}")
    if match_dir:
        args.append(f"--match-dir={match_dir}")
    if ignore_decorators:
        args.append(f"--ignore-decorators={ignore_decorators}")
    if debug:
        args.append('--debug')
    if verbose:
        args.append('--verbose')
    if version:
        args.append('--version')
    ctx.run(f"pydocstyle {' '.join(args)}")


@task(incrementable=['verbose'])
def coverage(
    ctx,  # type: Context
    exclude=None,  # type: Optional[str]
    skipmagic=False,  # type: bool
    skipfiledoc=False,  # type: bool
    skipinit=False,  # type: bool
    skipclassdef=False,  # type: bool
    skip_private=False,  # type: bool
    followlinks=False,  # type: bool
    docstr_ignore_file=None,  # type: Optional[str]
    failunder=90,  # type: int
    badge=None,  # type: Optional[str]
    percentage_only=False,  # type: bool
    verbose=None,  # type: Optional[int]
    path='.',  # type: str
):  # type: (...) -> None
    """Ensure all code is documented."""
    args = [ctx.project_dir]
    if exclude:
        args.append(f"--exclude '{exclude}'")
    if skipmagic:
        args.append('--skipmagic')
    if skipfiledoc:
        args.append('--skipfiledoc')
    if skipinit:
        args.append('--skipinit')
    if skipclassdef:
        args.append('--skipclassdef')
    if skip_private:
        args.append('--skip-private')
    if followlinks:
        args.append('--followlinks')
    if docstr_ignore_file:
        args.append(f"--docstr-ignore-file {docstr_ignore_file}")
    if failunder:
        args.append(f"--failunder {failunder}")
    if badge:
        args.append(f"--badge {badge}")
    if percentage_only:
        args.append('--percentage-only')
    if verbose:
        args.append(f"--verbose {verbose}")
    ctx.run(f"docstr-coverage {' '.join(args)}")


namespace = Collection(style, coverage)
# namespace.configure({})
namespace.load_collections(
    plugins=[
        {
            'name': 'site',
            'driver_name': 'mkdocs',
            'driver_namespace': 'proman.workflows.docs',
        }
    ]
)

__all__ = ['style', 'coverage', 'namespace']
