# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Static Content Task-Runner."""

from typing import Optional

from invoke import Context, task


@task
def install(
    ctx, path=None, also='dev'
):  # type: (Context, Optional[str], str) -> None
    """Install WebUI dependencies."""
    with ctx.cd(path or ctx.webui_dir):
        ctx.run(f"npm install --also={also}")


@task(pre=[install])
def build(ctx, path=None):  # type: (Context, Optional[str]) -> None
    """Build static content."""
    with ctx.cd(path or ctx.webui_dir):
        ctx.run('npm run build')


@task
def start(
    ctx, host=None, port=8000, browser=False, path=None
):  # type: (Context, Optional[str], int, bool, Optional[str]) -> None
    """Start webui development."""
    args = []
    if browser:
        args.append('--open')
    if host:
        args.append(f"--host={host}")
    if port:
        args.append(f"--port={port}")
    with ctx.cd(path or ctx.webui_dir):
        print(f"npx vue-cli-service serve {' '.join(args)}")
        ctx.run(
            'npx vue-cli-service serve',  # {}".format(' '.join(args)),
            asynchronous=True,
        )


@task
def stop(ctx):  # type: (Context) -> None
    """Stop WebUI development."""
    ctx.run('pkill npm')
