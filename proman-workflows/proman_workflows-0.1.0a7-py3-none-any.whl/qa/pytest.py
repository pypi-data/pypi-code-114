# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Quality Assurance Task-Runner."""

from typing import TYPE_CHECKING, Optional

from invoke import Collection, task

if TYPE_CHECKING:
    from invoke import Context


@task
def run(
    ctx,  # type: Context
    marker=None,  # type: str
    capture=None,  # type: Optional[str]
    debugger=None,  # type: Optional[str]
    durations=None,  # type: Optional[int]
    durations_min=None,  # type: Optional[int]
    maxfail=None,  # type: Optional[int]
):  # type: (...) -> None
    """Perform unit tests."""
    from pprint import pprint
    pprint(ctx.config.__dict__)
    args = []
    if marker:
        args.append(f"-m {marker}")
    if capture:
        args.append(f"--capture={capture}")
    if debugger:
        args.append('--pdb')
    if durations:
        args.append(f"--durations={durations}")
    if durations_min:
        args.append(f"--durations-min={durations_min}")
    if maxfail:
        args.append(f"--maxfail={maxfail}")
    with ctx.cd(ctx.project_dir):
        ctx.run(f"pytest {' '.join(args)}")


@task
def coverage(
    ctx,  # type: Context
    # project_dir,  # type: str
    coverage=True,  # type: bool
    coverage_on_fail=True,  # type: bool
    minimum=80,  # type: int
    append=False,  # type: bool
    branch=None,  # type: Optional[str]
    context=None,  # type: Optional[str]
    configpath=None,  # type: Optional[str]
    report=None,  # type: Optional[str]
):  # type: (...) -> None
    """Perform coverage checks for tests."""
    args = []
    if coverage:
        args.append('--no-cov')
    if not coverage_on_fail:
        args.append('--no-cov-on-fail')
    else:
        # args.append(f"--cov={project_dir}")
        if configpath:
            args.append(f"--cov-config={configpath}")
        if minimum:
            args.append(f"--cov-fail-under={minimum}")
        if append:
            args.append('--cov-append')
        if branch:
            args.append('--cov-branch')
        if context:
            args.append(f"--cov-context={context}")
        if report:
            args.append(f"--cov-report={report}")
    with ctx.cd(ctx.project_dir):
        ctx.run(f"pytest {' '.join(args)}")


namespace = Collection(coverage, run)
