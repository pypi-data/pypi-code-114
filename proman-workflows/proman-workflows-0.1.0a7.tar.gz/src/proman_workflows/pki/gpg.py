"""Provide signature capability using GnuPG."""

import os
from dataclasses import asdict
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from gnupg import GPG
from invoke import Collection, task

from proman_workflows.config import GPGConfig

if TYPE_CHECKING:
    from gnupg import GenKey, ListKeys
    from invoke import Context

ELYPTICAL_KEY_TYPES = [
    'ECDH',
    'ECDSA',
    'EDDSA',
]
KEY_TYPES = [
    'DSA',
    'ELG',
    'RSA',
] + ELYPTICAL_KEY_TYPES

# TODO: need better way of mapping curves
# ELYPTICAL_CURVES = [
#     'curve25519',  # cv25519, or ed25519
#     'nistp256',  # nothing up my sleeve?
#     'nistp384',  # nothing up my sleeve?
#     'nistp521',  # nothing up my sleeve?
#     'secp256k1',
#     # 'brainpoolP256r1',  # verifiable?
#     # 'brainpoolP384r1',  # verifiable?
#     # 'brainpoolP512r1',  # verifiable?
# ]


@task
def agent(
    ctx,  # type: Context
    daemon=False,  # type: bool
    supervised=False,  # type: bool
    verbose=False,  # type: bool
    quiet=False,  # type: bool
    sh=False,  # type: bool
    csh=False,  # type: bool
    options=None,  # type: Optional[str]
    dettach=True,  # type: bool
    log_file=None,  # type: Optional[str]
    pinentry_program=None,  # type: Optional[str]
    allow_loopback_pinentry=True,  # type: bool
    allow_emacs_pinentry=True,  # type: bool
    scdaemon_program=None,  # type: Optional[str]
    disable_scdaemon=True,  # type: bool
    extra_socket=None,  # type: Optional[int]
    keep_tty=True,  # type: bool
    keep_display=False,  # type: bool
    default_cache_ttl=None,  # type: Optional[int]
    ignore_cache_for_signing=False,  # type: bool
    allow_external_cache=True,  # type: bool
    allow_mark_trusted=True,  # type: bool
    allow_preset_passphrase=False,  # type: bool
    enable_ssh_support=False,  # type: bool
    ssh_fingerprint_digest=None,  # type: Optional[str]
):  # type: (...) -> None
    """Start gpg agent."""
    args = []
    if daemon:
        args.append('--daemon')
    if supervised:
        args.append('--supervised')
    if verbose:
        args.append('--verbose')
    if quiet:
        args.append('--quiet')

    # shell
    if sh:
        args.append('--sh')
    if csh:
        args.append('--csh')

    if keep_tty:
        args.append('--keep-tty')
    if keep_display:
        args.append('--keep-display')

    if not dettach:
        args.append('--no-detach')
    if log_file:
        args.append('--log-file')

    # setup pin entry UI application
    if pinentry_program:
        args.append(f"--pinentry-program {pinentry_program}")
        if not allow_loopback_pinentry:
            args.append('--no-allow-loopback-pinentry')
        if allow_emacs_pinentry:
            args.append('--allow-emacs-pinentry')

    # setup smartcard integration
    if disable_scdaemon:
        args.append('--disable-scdaemon')
    elif scdaemon_program:
        args.append(f"--scdaemon-program {scdaemon_program}")

    if extra_socket:
        args.append(f"--extra-socket {extra_socket}")

    # cache
    if default_cache_ttl:
        args.append(f"--default-cache-ttl {default_cache_ttl}")
    if ignore_cache_for_signing:
        args.append('--ignore-cache-for-signing')
    if not allow_external_cache:
        args.append('--no-allow-external-cache')

    if not allow_mark_trusted:
        args.append('--no-allow-mark-trusted')
    if allow_preset_passphrase:
        args.append('--allow-preset-passphrase')
    if enable_ssh_support:
        args.append('--enable-ssh-support')
        if ssh_fingerprint_digest:
            args.append(f"--ssh-fingerprint-digest {ssh_fingerprint_digest}")

    # gpg options
    if options:
        args.append(f"--options '{','.join(options)}'")
    ctx.run(f"gpgconf --launch gpg-agent {' '.join(args)}")


@task
def gpg(
    ctx,  # type: Context
    gnupghome=os.path.join(os.path.expanduser('~'), '.gnupg'),  # type: str
    keyring=None,  # type: Optional[str]
    secret_keyring=None,  # type: Optional[str]
):  # type: (...) -> None
    """Get gpg instance."""
    if '__gpg' not in ctx:
        ctx.__gpg = GPG(
            gnupghome=gnupghome,
            keyring=keyring,
            secret_keyring=secret_keyring
        )


@task(pre=[gpg])
def list_keys(
    ctx, secret=False, keys=None, sigs=False
):  # type: (Context, bool, Optional[str], bool) -> ListKeys
    """List GPG keys."""
    keys = ctx.__gpg.list_keys(secret=secret, keys=keys, sigs=sigs)
    print([k['keyid'] for k in keys])  # type: ignore
    return keys


@task(pre=[gpg])
def get_key(
    ctx, query, secret=False, sigs=False
):  # type: (Context, str, bool, bool) -> List[GenKey]
    """Get GPG key."""
    keys = []
    for key in list_keys(ctx, secret=secret, sigs=sigs):
        if '=' in query:
            k, v = query.split('=')
            if key[k] == v:
                keys.append(key)
        elif query in key.values():
            keys.append(key)
    return keys


@task(pre=[gpg])
def export_key(
    ctx, key, keypath, secret=False
):  # type: (Context, str, str, bool) -> None
    """Export an armored GPG key."""
    ascii_armored_keys = ctx.__gpg.export_keys(key, secret)
    with open(f"{key}.asc", 'w') as f:
        f.write(ascii_armored_keys)


@task(pre=[gpg])
def delete_key(
    ctx,
    query,
    passphrase,
    # secret=True,
    sigs=False,
    expect_passphrase=True,
):  # type: (Context, str, str, bool, bool) -> None
    """Delete GPG key."""
    for secret in (True, False):
        keys = get_key(ctx, query, secret, sigs)
        for key in keys:
            ctx.__gpg.delete_keys(
                [x['fingerprint'] for x in keys],
                secret=secret,
                passphrase=passphrase,
                expect_passphrase=expect_passphrase,
            )


@task(pre=[gpg], iterable=['key_usage', 'subkey_usage'])
def gen_key(
    ctx,  # type: Context
    name,  # type: str
    email,  # type: str
    password,  # type: str
    comment='generated by proman',  # type: Optional[str]
    key_type='EDDSA',  # type: str
    key_curve='ed25519',  # type: str
    key_length=None,  # type: Optional[int]
    key_usage=None,  # type: Optional[List[str]]
    subkey_type='EDDSA',  # type: str
    subkey_curve='ed25519',  # type: str
    subkey_length=None,  # type: Optional[int]
    subkey_usage=None,  # type: Optional[List[str]]
    expire_date='1y',  # type: str
):  # type: (...) -> GenKey
    """Generate GPG key."""
    # TODO: default to subkey if primary key exists
    usage = ['auth', 'cert', 'encrypt', 'sign']
    settings: Dict[str, Any] = {}

    # separate_keyring
    # save_batchfile
    # testing
    # key_grip
    # creation_date
    # preferences
    # revoker
    # keyserver
    # handle

    settings['key_type'] = key_type
    if key_type not in ELYPTICAL_KEY_TYPES:
        settings['key_length'] = key_length
    elif key_type in ELYPTICAL_KEY_TYPES:
        if key_curve:
            # and key_curve in KEY_CURVES:
            settings['key_curve'] = key_curve
    if key_usage and all(item in key_usage for item in usage):
        settings['key_usage'] = ','.join(key_usage)

    settings['subkey_type'] = subkey_type
    if subkey_type not in ELYPTICAL_KEY_TYPES:
        settings['subkey_length'] = subkey_length
    elif subkey_type in ELYPTICAL_KEY_TYPES:
        if subkey_curve:
            # and subkey_curve in KEY_CURVES:
            settings['subkey_curve'] = subkey_curve
    if subkey_usage and all(item in subkey_usage for item in usage):
        settings['subkey_usage'] = ','.join(subkey_usage)

    settings['expire_date'] = expire_date

    input_data = ctx.__gpg.gen_key_input(
        name_real=name,
        name_email=email,
        name_comment=comment,
        passphrase=password,
        **settings,
    )
    print('input', input_data)
    key = ctx.__gpg.gen_key(input_data)
    # print('key', key)
    return key


namespace = Collection(
    list_keys,
    get_key,
    delete_key,
    export_key,
    gen_key,
)
namespace.configure(
    {
        'settings': asdict(GPGConfig()),
        'signing': {
            'developers': {
                'required': True,
            },
            'packaging': {
                'required': True,
            },
        },
    }
)
