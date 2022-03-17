"""Provide git config management."""

import os
from typing import TYPE_CHECKING, Any, Dict, Optional

from invoke import Collection, task
from pygit2 import Config, Repository

from .. import filesystem, templates

if TYPE_CHECKING:
    from invoke import Context


def to_dict(config: Config) -> Dict[str, Any]:
    """Convert gitconfig to dictionary."""
    sections: Dict[str, Any] = {}
    for entry in config:
        s = sections
        if hasattr(entry, 'name'):
            items = entry.name.split('.')
            for index, part in enumerate(items):
                if index < (len(items) - 1):
                    s = s.setdefault(part, {})
                else:
                    s[part] = entry.value
    return {'sections': sections}


@task
def repo(ctx):  # type: (Context) -> Repository
    """Set git as SCM."""
    # XXX: can set context using set
    return Repository(ctx.repo_dir)


@task
def dump(
    ctx, data, template_name, dest, executable=False, update=False
):  # type: (Context, Dict[str, Any], str, str, bool, bool) -> None
    """Create git hook."""
    if update or not os.path.exists(dest):
        content = templates.render(ctx, data=data, template_name=template_name)
        filesystem.write(
            ctx,
            content=content,
            dest=dest,
            executable=executable,
            update=update,
        )
    else:
        print('Config already exists.')


@task
def load(
    ctx, filepath=None, scope=None
):  # type: (Context, Optional[str], Optional[str]) -> Dict[str, Any]
    """Get git config as dictionary."""
    vcs = repo(ctx)
    if scope == 'system':
        config = vcs.config.get_system_config()
    elif scope == 'global':
        config = vcs.config.get_global_config()
    elif scope == 'xdg':
        config = vcs.config.get_xdg_config()
    else:
        config = Config(filepath or os.path.join(ctx.repo_dir, 'config'))
    return to_dict(config)


@task
def setup(
    ctx, filepath=None, scope=None, update=False
):  # type: (Context, Optional[str], Optional[str], bool) -> None
    """Set VCS configuration."""
    data = load(ctx, filepath=filepath, scope=scope)

    # if 'user.name' not in config:
    #     username = pyip.inputStr(
    #         prompt='GIT: Enter full name: ',
    #         limit=255,
    #     )
    #     config.set_multivar('user.name', regex='^.*$', value=username)
    #     print('user.name', config.get_multivar('user.name'))
    # if 'user.email' not in config:
    #     email = pyip.inputEmail(
    #         prompt='GIT: Enter email: ',
    #         limit=255,
    #     )
    #     config.set_multivar('user.email', regex='^.*$', value=email)
    #     print('user.email', config.get_multivar('user.email'))

    dump(
        ctx,
        data,
        template_name='gitconfig',
        dest=os.path.join(ctx.repo_dir, 'check'),
        update=update,
    )


config_tasks = Collection(dump, load)
