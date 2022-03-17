# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Quality Assurance Task-Runner."""

from typing import TYPE_CHECKING, Optional

from invoke import Collection, task

if TYPE_CHECKING:
    from invoke import Context


@task
def version(ctx):  # type: (Context) -> None
    """Get isort version number."""
    ctx.runt('isort --version-number')


@task
def run(
    ctx,  # type: Context
    atomic=True,  # type: bool
    check=False,  # type: bool
    diff=False,  # type: bool
    dedup_heading=False,  # type: bool
    jobs=None,  # type: Optional[int]
    ignore_whitespace=False,  # type: bool
    interactive=False,  # type: bool
    only_modified=False,  # type: bool
    overwrite_in_place=False,  # type: bool
    path=None,  # type: Optional[str]
    quiet=False,  # type: bool
    stdout=False,  # type: bool
    settings_path=None,  # type: Optional[str]
    profile=None,  # type: Optional[str]
    verbose=False,  # type: bool
):  # type: (...) -> None
    """Format project headers to PEP8 standards."""
    args = []
    if jobs:
        args.append(f"--jobs {jobs}")
    if check:
        args.append('--check-only')
    else:
        if atomic:
            args.append('--atomic')
        if dedup_heading:
            args.append('--dedup-headings')
        if overwrite_in_place:
            args.append('--overwrite-in-place')
    if diff:
        args.append('--diff')
    if ignore_whitespace:
        args.append('--ignore-whitespace')
    if settings_path:
        args.append(f"--settings-path {settings_path}")
    if profile:
        args.append(f"--profile {profile}")
    if quiet:
        args.append('--quiet')
    if stdout:
        args.append('--stdout')
    if verbose:
        args.append('--verbose')
    if only_modified:
        args.append('--only-modified')
    if interactive:
        args.append('--interactive')
    args.append(path if path else ctx.project_dir)
    ctx.run(f"isort {' '.join(args)}")


namespace = Collection(run)
