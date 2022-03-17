# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Provide package task-runner."""

# import importlib
from typing import TYPE_CHECKING, Optional

from invoke import task

from ..collection import Collection

if TYPE_CHECKING:
    from invoke import Context


@task
def version(
    ctx,
    part=None,
    tag=False,
    commit=False,
    message=None,
):  # type: (Context, Optional[str], bool, bool, Optional[str]) -> None
    """Update project version and apply tags."""
    version = ctx.specfile['tool']['poetry']['version']
    if (
        'dev' in version
        or ('a' in version or 'alpha' in version)
        or ('b' in version or 'beta' in version)
        or 'rc' in version
    ):
        part = 'build'
    else:
        part = 'patch'

    args = [part]
    if commit:
        args.append('--commit')
    else:
        args.append('--dry-run')
        args.append('--allow-dirty')
        args.append('--verbose')
        print('Add "--commit" to actually bump the version.')
    if tag or message:
        args.append('--tag')
        if message:
            args.append(f"--tag-message '{message}'")
    ctx.run(f"bumpversion {' '.join(args)}")


namespace = Collection(
    configuration={
        'plugins': [
            {
                'name': 'package',
                'driver_name': 'poetry',
                'driver_namespace': 'proman.workflows.package',
            }
        ]
    }
)
namespace.add_task(version)
