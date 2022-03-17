# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Quality Assurance Task-Runner."""

from typing import TYPE_CHECKING, Optional

from invoke import Collection, task

if TYPE_CHECKING:
    from invoke import Context


@task(name='license')
def licensing(
    ctx,  # type: Context
    key=None,  # type: Optional[str]
    db=None,  # type: Optional[str]
    json=None,  # type: Optional[bool]
    bare=None,  # type: Optional[bool]
    cache=None,  # type: Optional[bool]
    file=None,  # type: Optional[str]
    proxy_host=None,  # type: Optional[str]
    proxy_port=None,  # type: Optional[int]
    proxy_protocol=None,  # type: Optional[str]
):  # type: (...) -> None
    """Configure license for safety."""
    args = []
    if key:
        args.append(f"--key={key}")
    if db:
        args.append(f"--db={db}")
    if json is not None:
        args.append('--json' if json else '--no-json')
    if bare is not None:
        args.append('--bare' if bare else '--not-bare')
    if cache is not None:
        args.append('--cache' if cache else '--no-cache')
    if file:
        args.append(f"--file={file}")
    if proxy_host:
        args.append(f"--proxy-host={proxy_host}")
    if proxy_port:
        args.append(f"--proxy-port={proxy_port}")
    if proxy_protocol:
        args.append(f"--proxy-protocol={proxy_protocol}")
    with ctx.cd(ctx.project_dir):
        ctx.run(f"safety license {' '.join(args)}")


@task
def review(
    ctx,  # type: Context
    full_report=None,  # type: Optional[bool]
    bare=None,  # type: Optional[bool]
    file=None,  # type: Optional[str]
):  # type: (...) -> None
    """Perform safety reiew of reports."""
    args = []
    if full_report is not None:
        args.append('--full-report' if full_report else '--short-report')
    if bare is not None:
        args.append('--bare' if bare else '--not-bare')
    if file:
        args.append(f"--file={file}")
    with ctx.cd(ctx.project_dir):
        ctx.run(f"safety review {' '.join(args)}")


@task
def check(
    ctx,  # type: Context
    key=None,  # type: Optional[str]
    db=None,  # type: Optional[str]
    json=None,  # type: Optional[bool]
    full_report=None,  # type: Optional[bool]
    bare=None,  # type: Optional[bool]
    cache=None,  # type: Optional[bool]
    stdin=None,  # type: Optional[bool]
    file=None,  # type: Optional[str]
    ignore=None,  # type: Optional[str]
    output=None,  # type: Optional[str]
    proxy_host=None,  # type: Optional[str]
    proxy_port=None,  # type: Optional[int]
    proxy_protocol=None,  # type: Optional[str]
):  # type: (...) -> None
    """Perform safety check of project dependencies."""
    args = []
    if key:
        args.append(f"--key={key}")
    if db:
        args.append(f"--db={db}")
    if json is not None:
        args.append('--json' if json else '--no-json')
    if full_report is not None:
        args.append('--full-report' if full_report else '--short-report')
    if bare is not None:
        args.append('--bare' if bare else '--not-bare')
    if cache is not None:
        args.append('--cache' if cache else '--no-cache')
    if stdin is not None:
        args.append('--stdin' if stdin else '--no-stdin')
    if file:
        args.append(f"--file={file}")
    if ignore:
        args.append(f"--ignore={ignore}")
    if output:
        args.append(f"--output={output}")
    if proxy_host:
        args.append(f"--proxy-host={proxy_host}")
    if proxy_port:
        args.append(f"--proxy-port={proxy_port}")
    if proxy_protocol:
        args.append(f"--proxy-protocol={proxy_protocol}")
    with ctx.cd(ctx.project_dir):
        ctx.run(f"safety check {' '.join(args)}")


namespace = Collection(check, licensing, review)
