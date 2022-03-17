# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Validation Task-Runner."""

# import platform
from typing import TYPE_CHECKING, Optional

from invoke import Collection, task

from .. import filesystem

# from .package_manager import github

if TYPE_CHECKING:
    from invoke import Context

# mkcert = f"mkcert-{config.mkcert_version}-{config.system_type}-amd64"


@task
def setup(ctx):  # type: (Context) -> None
    """Install GitHub release."""
    # github.install(
    #     ctx,
    #     repo='FiloSottile/mkcert',
    #     version=config.mkcert_version,
    #     filename=mkcert,
    #     new_filename='mkcert',
    #     file_pattern=f"*{platform.system().lower()}-amd64*"
    # )
    ctx.run('mkcert -install')


@task(pre=[setup], iterable=['name'])
def generate(
    ctx,  # type: Context
    name,  # type: str
    key=None,  # type: Optional[str]
    cert=None,  # type: Optional[str]
    p12=None,  # type: Optional[str]
    client=None,  # type: Optional[str]
    csr=None,  # type: Optional[str]
    ecdsa=False,  # type: bool
    pkcs12=False,  # type: bool
    path=None,  # type: Optional[str]
):  # type: (...) -> None
    """Generate certificate."""
    args = []
    if key:
        args.append(f"-key-file={key}")
    if cert:
        args.append(f"-cert-file={cert}")
    if p12:
        args.append(f"-client={client}")
    if ecdsa:
        args.append(f"-ecdsa={ecdsa}")
    if pkcs12:
        args.append(f"-pkcs12={pkcs12}")
    if csr:
        args.append(f"-csr={csr}")
    cmd = f"mkcert {' '.join(args)} {' '.join(name)}"
    if path:
        filesystem.mkdir(ctx, path)
        with ctx.cd(path):
            ctx.run(cmd)
    else:
        ctx.run(cmd)


@task
def clean(ctx, path=None):  # type: (Context, Optional[str]) -> None
    """Cleanup certificates."""
    if path:
        filesystem.rm(ctx, path)
    ctx.run('mkcert -uninstall')


namespace = Collection(clean, generate, setup)
