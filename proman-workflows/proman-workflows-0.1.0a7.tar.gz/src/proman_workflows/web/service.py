# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Build Task-Runner."""

from invoke import Context, task
from passlib.pwd import genword

from .. import filesystem
from ..container import docker
from ..pki import tls


@task
def start(ctx, certs_path='./nginx/certs'):  # type: (Context, str) -> None
    """Start all services."""
    tls.setup(ctx)
    filesystem.mkdir(ctx, certs_path)
    tls.generate(
        ctx,
        name=['spades.local', 'localhost'],
        key=f"{certs_path}/spades.key",
        cert=f"{certs_path}/spades.crt",
    )
    env = {
        'POSTGRESQL_PASSWORD': genword(entropy=56, length=128),
        'REDIS_PASSWORD': genword(entropy=56, length=128),
    }
    docker.start(ctx, files=[], env=env)


@task
def stop(ctx, certs_path='./nginx/certs'):  # type: (Context, str) -> None
    """Stop all services."""
    docker.stop(ctx)
    tls.clean(ctx)
    filesystem.rm(ctx, certs_path)
