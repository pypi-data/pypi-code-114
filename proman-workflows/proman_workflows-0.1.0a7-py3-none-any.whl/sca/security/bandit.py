# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Quality Assurance Task-Runner."""

from typing import TYPE_CHECKING, Optional

from invoke import Collection, task

if TYPE_CHECKING:
    from invoke import Context


@task(iterable=['kind'])
def check(
    ctx,  # type: Context
    target='**/*.py',  # type: str
    recursive=True,  # type: bool
    aggregate=None,  # type: Optional[str]
    number=None,  # type: Optional[str]
    configfile=None,  # type: Optional[str]
    profile=None,  # type: Optional[str]
    tests=None,  # type: Optional[str]
    skip=None,  # type: Optional[str]
    level=False,  # type: bool
    confidence=False,  # type: bool
    kind=None,  # type: Optional[str]
    msg_template=None,  # type: Optional[str]
    output=None,  # type: Optional[str]
    verbose=False,  # type: bool
    debug=False,  # type: bool
    silent=False,  # type: bool
    ignore_nosec=False,  # type: bool
    exclude=None,  # type: Optional[str]
    baseline=None,  # type: Optional[str]
    ini_path=None,  # type: Optional[str]
    exit_zero=False,  # type: bool
):  # type: (...) -> None
    """Perform static code analysis on imports."""
    args = []
    if recursive:
        args.append('--recursive')
    if aggregate:
        args.append(f"--aggregate {aggregate}")
    if number:
        args.append(f"--number {number}")
    if configfile:
        args.append(f"--configfile {configfile}")
    if profile:
        args.append(f"--profile {profile}")
    if tests:
        args.append(f"--tests {tests}")
    if skip:
        args.append(f"--skip {skip}")
    if level:
        args.append('--level')
    if confidence:
        args.append('--confidence')
    if kind:
        args.append(f"--format {','.join(kind)}")
    if msg_template:
        args.append(f"--msg-template {msg_template}")
    if output:
        args.append(f"--output {output}")
    if verbose:
        args.append('--verbose')
    if debug:
        args.append('--debug')
    if silent:
        args.append('--silent')
    if ignore_nosec:
        args.append('--ignore-nosec')
    if exclude:
        args.append(f"--exclude '{','.join(exclude)}'")
    if baseline:
        args.append(f"--baseline {baseline}")
    if ini_path:
        args.append(f"--ini {ini_path}")
    if exit_zero:
        args.append('--exit-zero')
    args.append(target)
    with ctx.cd(ctx.project_dir):
        ctx.run(f"bandit {' '.join(args)}")


namespace = Collection(check)
