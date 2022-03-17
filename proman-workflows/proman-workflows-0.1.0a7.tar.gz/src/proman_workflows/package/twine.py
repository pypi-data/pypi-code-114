# -*- coding: utf-8 -*-
"""Publish packages using Twine."""

from typing import TYPE_CHECKING, Optional

from invoke import Collection, task

if TYPE_CHECKING:
    from invoke import Context


@task
def check(ctx, path, strict=True):  # type: (Context, str, bool) -> None
    """Check package."""
    args = [path]
    if strict:
        args.append('--strict')
    ctx.run(f"twine check {' '.join(args)}")


@task
def register(
    ctx,  # type: Context
    repository=None,  # type: Optional[str]
    repository_url=None,  # type: Optional[str]
    sign=False,  # type: bool
    sign_with=None,  # type: Optional[str]
    identity=None,  # type: Optional[str]
    username=None,  # type: Optional[str]
    password=None,  # type: Optional[str]
    comment=None,  # type: Optional[str]
    skip_existing=False,  # type: bool
    cert_path=None,  # type: Optional[str]
    client_cert_path=None,  # type: Optional[str]
    verbose=False,  # type: bool
    disable_progress_bar=False,  # type: bool
):  # type: (...) -> None
    """Register package to a PyPI repository."""
    args = ['--non-interactive']
    if repository:
        args.append(f"--repository={repository}")
    if repository_url:
        args.append(f"--repository-url={repository_url}")
    if sign:
        args.append('--sign')
        if sign_with:
            args.append(f"--sign-with='{sign_with}'")
        else:
            raise Exception('need to provide signature for package signing')
    if identity:
        args.append(f"--identity='{identity}'")
    if username:
        args.append(f"--username={username}")
        if password:
            args.append(f"--password='{password}'")
        else:
            raise Exception('username requires a password')
    if comment:
        args.append(f"--comment='{comment}'")
    if skip_existing:
        args.append('--skip-existing')
    if cert_path:
        args.append(f"--cert={cert_path}")
    if client_cert_path:
        args.append(f"--client-cert={client_cert_path}")
    if verbose:
        args.append('--verbose')
    if disable_progress_bar:
        args.append('--disable-progress-bar')
    ctx.run(f"twine register {' '.join(args)}")


@task
def publish(
    ctx,  # type: Context
    repository=None,  # type: Optional[str]
    repository_url=None,  # type: Optional[str]
    sign=False,  # type: bool
    sign_with=None,  # type: Optional[str]
    identity=None,  # type: Optional[str]
    username=None,  # type: Optional[str]
    password=None,  # type: Optional[str]
    comment=None,  # type: Optional[str]
    skip_existing=False,  # type: bool
    cert_path=None,  # type: Optional[str]
    client_cert_path=None,  # type: Optional[str]
    verbose=False,  # type: bool
    disable_progress_bar=False,  # type: bool
):  # type: (...) -> None
    """Upload package to a PyPI repository."""
    args = ['--non-interactive']
    if repository:
        args.append(f"--repository={repository}")
    if repository_url:
        args.append(f"--repository-url={repository_url}")
    if sign:
        args.append('--sign')
        if sign_with:
            args.append(f"--sign-with='{sign_with}'")
        else:
            raise Exception('need to provide signature for package signing')
    if identity:
        args.append(f"--identity='{identity}'")
    if username:
        args.append(f"--username={username}")
        if password:
            args.append(f"--password='{password}'")
        else:
            raise Exception('username requires a password')
    if comment:
        args.append(f"--comment='{comment}'")
    if skip_existing:
        args.append('--skip-existing')
    if cert_path:
        args.append(f"--cert {cert_path}")
    if client_cert_path:
        args.append(f"--client-cert {client_cert_path}")
    if verbose:
        args.append('--verbose')
    if disable_progress_bar:
        args.append('--disable-progress-bar')
    ctx.run(f"twine upload {' '.join(args)}")


namespace = Collection(check, register, publish)
