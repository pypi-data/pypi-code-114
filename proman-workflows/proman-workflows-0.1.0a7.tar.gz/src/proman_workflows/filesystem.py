# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Validation Task-Runner."""

import os
import shutil
import stat
from typing import TYPE_CHECKING, Optional

from invoke import task

if TYPE_CHECKING:
    from invoke import Context


# async def rwalk(
#     path: str, stop: Optional[str] = None
# ) -> AsyncGenerator[str, str]:
#     """Walk the reverse path of a directory."""
#     current_path = os.path.abspath(path)
#     for _ in path.split(os.sep):
#         yield current_path
#         current_path = os.path.abspath(os.path.join(current_path, '..'))


@task
def write(ctx, content, dest, executable=False, update=False):
    # type: (Context, str, str, bool, bool) -> None
    """Create git hook."""
    if update or not os.path.exists(dest):
        with open(dest, 'w+') as f:
            f.write(content)

        if executable:
            st = os.stat(dest)
            os.chmod(dest, st.st_mode | stat.S_IEXEC)


@task
def mkdir(ctx, path):  # type: (Context, str) -> None
    """Make directory path."""
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as err:
        print(f"unable to download github release due to: {err}")


@task
def rm(ctx, path):  # type: (Context, str) -> None
    """Remove directory path."""
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
        if os.path.isdir(path):
            try:
                shutil.rmtree(path)
            except OSError as err:
                print(f"unable to delete direcotry path due to: {err}")
    else:
        print(f"path does not exists: {path}")


@task(iterable=['path'])
def clean(
    ctx,  # type: Context
    path=None,  # type: Optional[str]
    mindepth=None,  # type: Optional[int]
    maxdepth=None,  # type: Optional[int]
):  # type: (...) -> None
    """Clean project dependencies and build."""
    args = []
    if not path:
        paths = [
            '__pycache__',
            '.mypy_cache',
            'dist',
            '*.pyc',
        ]
    if mindepth:
        args.append(f"-mindepth {mindepth}")
    if maxdepth:
        args.append(f"-maxdepth {maxdepth}")
    for path in paths:
        ctx.run(
            "find . %s -exec rm -rf {} +"
            % (' '.join([f"-name {path}"] + args))
        )
