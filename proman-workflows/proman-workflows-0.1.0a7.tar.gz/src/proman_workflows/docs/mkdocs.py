# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Provide documentation task-runner."""

from typing import TYPE_CHECKING, Optional

from invoke import Collection, task

if TYPE_CHECKING:
    from invoke import Context


@task
def build(
    ctx,  # type: Context
    clean=False,  # type: bool
    configfile=None,  # type: Optional[str]
    strict=False,  # type: bool
    theme=None,  # type: Optional[str]
    use_directory_urls=None,  # type: Optional[str]
    path=None,  # type: Optional[str]
    quiet=False,  # type: bool
    verbose=False,  # type: bool
):  # type: (...) -> None
    """Build documentation site."""
    args = []
    if clean is not None:
        args.append('--clean' if clean else '--dirty')
    if configfile:
        args.append(f"--config-file {configfile}")
    if strict:
        args.append('--strict')
    if theme:
        if theme in ['readthedocs', 'material', 'mkdocs']:
            args.append(f"--theme {theme}")
        else:
            raise Exception(f"{theme} is not a supported mkdocs theme")
    if use_directory_urls is not None:
        args.append(
            '--use-directory-urls'
            if use_directory_urls
            else '--no-directory-urls'
        )
        args.append(f"--site-dir {path}")
    if quiet:
        args.append('--quiet')
    if verbose:
        args.append('--verbose')

    with ctx.cd(ctx.project_dir):
        ctx.run(f"mkdocs build {' '.join(args)}")


@task
def start(
    ctx,  # type: Context
    address='localhost:8001',  # type: str
    livereload=None,  # type: Optional[bool]
    dirtyreload=None,  # type: Optional[bool]
    watch_theme=False,  # type: bool
    configfile=None,  # type: Optional[str]
    strict=False,  # type: bool
    theme='readthedocs',  # type: str
    use_directory_urls=None,  # type: Optional[bool]
    quiet=False,  # type: bool
    verbose=False,  # type: bool
):  # type: (...) -> None
    """Start docsite."""
    args = [f"--dev-addr {address}"]
    if livereload is not None:
        args.append('--livereload' if livereload else '--no-livereload')
    if dirtyreload:
        args.append('--dirtyreload')
    if watch_theme:
        args.append('--watch-theme')
    if configfile:
        args.append(f"--config-file {configfile}")
    if strict:
        args.append('--strict')
    if theme:
        if theme in ['readthedocs', 'mkdocs', 'material']:
            args.append(f"--theme {theme}")
        else:
            raise Exception('unsupported theme')
    if use_directory_urls is not None:
        args.append(
            '--use-directory-urls'
            if use_directory_urls
            else '--no-directory-urls'
        )
    if quiet:
        args.append('--quiet')
    elif verbose:
        args.append('--verbose')

    with ctx.cd(ctx.docs_dir):
        ctx.run(f"mkdocs serve {' '.join(args)}", disown=True)


@task
def stop(ctx):  # type: (Context) -> None
    """Stop docsite."""
    ctx.run('pkill mkdocs')


namespace = Collection(build, start, stop)
