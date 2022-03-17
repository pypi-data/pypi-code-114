# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Provide utilities task-runner."""

# import importlib
from typing import TYPE_CHECKING, List, Optional

from invoke import Collection, task

if TYPE_CHECKING:
    from invoke import Context, Result


@task
def find(
    ctx,  # type: Context
    name,  # type: str
    path='.',  # type: str
    mindepth=None,  # type: Optional[int]
    maxdepth=None,  # type: Optional[int]
):  # type: (...) -> List[Result]
    """Clean project dependencies and build."""
    args = []
    if mindepth:
        args.append(f"-mindepth {mindepth}")
    if maxdepth:
        args.append(f"-maxdepth {maxdepth}")
    result = ctx.run(f"find {path} {' '.join(args)}")
    return result


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


@task(iterable=['runstates'])
def pkill(
    ctx,  # type: Context
    pattern,  # type: str
    signal=None,  # type: int
    echo=False,  # type: bool
    count=False,  # type: bool
    full=False,  # type: bool
    pgroup=None,  # type: Optional[str]
    group=None,  # type: Optional[str]
    ignore_case=False,  # type: bool
    newest=False,  # type: bool
    oldest=False,  # type: bool
    parent=None,  # type: Optional[str]
    session=None,  # type: Optional[str]
    terminal=None,  # type: Optional[str]
    euid=None,  # type: Optional[str]
    uid=None,  # type: Optional[str]
    exact=False,  # type: bool
    pidfile=None,  # type: Optional[str]
    logpidfile=False,  # type: bool
    runstates=[],  # type: List[str]
    namespace=None,  # type: Optional[str]
    nslist=None,  # type: Optional[str]
):  # type: (...) -> None
    """Stop docsite."""
    args = []
    if signal:
        args.append(f"--signal {signal}")
    if echo:
        args.append('--echo')
    if count:
        args.append('--count')
    if full:
        args.append('--full')
    if pgroup:
        args.append(f"--pgroup {pgroup}")
    if group:
        args.append(f"--group {group}")
    if ignore_case:
        args.append('--ignore-case')
    if newest:
        args.append('--newest')
    if oldest:
        args.append('--oldest')
    if parent:
        args.append(f"--parent {parent}")
    if session:
        args.append(f"--session {session}")
    if terminal:
        args.append(f"--terminal {terminal}")
    if euid:
        args.append(f"--euid {euid}")
    if uid:
        args.append(f"--uid {uid}")
    if exact:
        args.append('--exact')
    if pidfile:
        args.append(f"--pidfile {pidfile}")
    if logpidfile:
        args.append('--logpidfile')
    if runstates != []:
        args.append(f"--runstates {','.join(runstates)}")
    if namespace:
        args.append(f"--ns {namespace}")
    if nslist:
        # Available namespaces: ipc, mnt, net, pid, user, uts
        args.append(f"--nslist {nslist}")
    args.append(pattern)
    ctx.run(f"pkill {' '.join(args)}")


namespace = Collection(clean)
