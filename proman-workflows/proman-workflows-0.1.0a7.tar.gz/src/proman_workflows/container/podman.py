# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Build Task-Runner."""

from typing import TYPE_CHECKING, Any, Dict, List, Optional

from invoke import Collection, task

if TYPE_CHECKING:
    from invoke import Context

# TODO: switch to podman module


@task(iterable=['files'])
def start(
    ctx,  # type: Context
    files,  # type: List[str]
    env={},  # type: Dict[str, Any]
    build=False,  # type: bool
    recreate=False,  # type: bool
    dev=False,  # type: bool
):  # type: (...) -> None
    """Start all compose containers."""
    args = []
    if build:
        args.append('--build')
    if recreate:
        args.append('--force-recreate')

    if dev:
        files.append('docker-compose.yml')
        files.append('docker-compose.override.yml')

    if files != []:
        files = [f"--file={f}" for f in files]

    with ctx.cd(ctx.container_build_dir):
        ctx.run(
            "podman-compose {f} up -d {a}".format(
                f='' if files == [] else ' '.join(files), a=' '.join(args)
            ),
            env=env,
        )


@task
def stop(
    ctx,  # type: Context
    remove_images=None,  # type: Optional[str]
    remove_volumes=True,  # type: bool
    remove_orphans=True,  # type: bool
):  # type: (...) -> None
    """Stop all compose containers."""
    args = []
    if remove_images:
        args.append(f"--rmi={remove_images}")
    if remove_volumes:
        args.append('--volumes')
    if remove_orphans:
        args.append('--remove-orphans')
    with ctx.cd(ctx.container_build_dir):
        ctx.run(f"podman-compose down {' '.join(args)}")


namespace = Collection(start, stop)
