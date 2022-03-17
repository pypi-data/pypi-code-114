# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Provide flake8 Task-Runner."""

from typing import TYPE_CHECKING, Optional

from invoke import Collection, task

if TYPE_CHECKING:
    from invoke import Context


@task
def run(
    ctx,  # type: Context
    output_file=None,  # type: Optional[str]
    append_config=None,  # type: Optional[str]
    config=None,  # type: Optional[str]
    isolated=False,  # type: bool
    quiet=False,  # type: bool
    count=False,  # type: bool
    diff=False,  # type: bool
    exclude=None,  # type: Optional[str]
    extend_exclude=None,  # type: Optional[str]
    filename=None,  # type: Optional[str]
    stdin_display_name=None,  # type: Optional[str]
    kind=None,  # type: Optional[bool]
    hang_closing=None,  # type: Optional[bool]
    ignore=None,  # type: Optional[bool]
    extend_ignore=None,  # type: Optional[str]
    per_file_ignores=None,  # type: Optional[str]
    max_line_length=None,  # type: Optional[int]
    max_doc_length=None,  # type: Optional[int]
    indent_size=None,  # type: Optional[int]
    select=None,  # type: Optional[str]
    disable_noqa=False,  # type: bool
    show_source=None,  # type: Optional[bool]
    # no_show_source=None,  # type: Optional[bool]
    statistics=False,  # type: bool
    enable_extensions=None,  # type: Optional[str]
    exit_zero=False,  # type: bool
    jobs=None,  # type: Optional[str]
    tee=False,  # type: bool
    benchmark=False,  # type: bool
    bug_report=False,  # type: bool
    max_complexity=None,  # type: Optional[int]
    builtins=None,  # type: Optional[str]
    doctests=False,  # type: bool
    include_in_doctest=None,  # type: Optional[str]
    exclude_from_doctest=None,  # type: Optional[str]
):  # type: (...) -> None
    """Format project source code to PEP-8 standard."""
    args = []
    if output_file:
        args.append(f"--output-file {output_file}")
    if append_config:
        args.append(f"--append-config {append_config}")
    if config:
        args.append(f"--config {config}")
    if isolated:
        args.append('--isolated')
    if quiet:
        args.append('--quiet')
    if count:
        args.append('--count')
    if diff:
        args.append('--diff')
    if exclude:
        args.append(f"--exclude {exclude}")
    if extend_exclude:
        args.append(f"--extend-exclude {extend_exclude}")
    if filename:
        args.append(f"--filename {filename}")
    if stdin_display_name:
        args.append(f"--stdin-display-name {stdin_display_name}")
    if kind:
        args.append(f"--format {kind}")
    if hang_closing:
        args.append('--hang-closing')
    if ignore:
        args.append(f"--ignore {ignore}")
    if extend_ignore:
        args.append(f"--extend-ignore {extend_ignore}")
    if per_file_ignores:
        args.append(f"--per-file-ignores {per_file_ignores}")
    if max_line_length:
        args.append(f"--max-line-length {max_line_length}")
    if max_doc_length:
        args.append(f"--max-doc-length {max_doc_length}")
    if indent_size:
        args.append(f"--indent-size {indent_size}")
    if select:
        args.append(f"--select {select}")
    if disable_noqa:
        args.append('--disable-noqa')
    if show_source is not None:
        args.append('--show-source' if show_source else '--no-show-source')
    if statistics:
        args.append('--statistics')
    if enable_extensions:
        args.append(f"--enable-extensions {enable_extensions}")
    if exit_zero:
        args.append('--exit-zero')
    if jobs:
        args.append(f"--jobs {jobs}")
    if tee:
        args.append('--tee')
    if benchmark:
        args.append('--benchmark')
    if bug_report:
        args.append('--bug-report')
    if max_complexity:
        args.append(f"--max-complexity {max_complexity}")
    if builtins:
        args.append(f"--builtins {builtins}")
    if doctests:
        args.append('--doctests')
    if include_in_doctest:
        args.append(f"--include-in-doctest {include_in_doctest}")
    if exclude_from_doctest:
        args.append(f"--exclude-from-doctest {exclude_from_doctest}")
    with ctx.cd(ctx.project_dir):
        ctx.run(f"flake8 {' '.join(args)}")


namespace = Collection(run)
