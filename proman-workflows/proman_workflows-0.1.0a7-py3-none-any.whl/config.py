# copyright: (c) 2020 by Jesse Johnson.
# license: MPL-2.0, see LICENSE for more details.
"""Provide CLI for git-tools."""

import os
import shutil
import sys
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from compendium.loader import ConfigFile
from invoke.config import Config as InvokeConfig

# from invoke.config import merge_dicts
from pygit2 import discover_repository

# from typing import Optional, Tuple
# from urllib.parse import urljoin, urlparse


VENV_PATH = os.getenv('VIRTUAL_ENV', None)
PATHS = [VENV_PATH] if VENV_PATH else []


class WorkflowConfig(InvokeConfig):
    """Provide project configuration."""

    prefix = 'workflow'

    # @staticmethod
    # def global_defaults() -> Dict[str, Any]:
    #     """Set global defaults."""
    #     defaults = InvokeConfig.global_defaults()
    #     default_plugins = {
    #         'plugins': [
    #             {
    #                 'name': 'package',
    #                 'driver_name': 'poetry',
    #                 'driver_namespace': 'proman.workflows.package',
    #             },
    #             # [tool.poetry.plugins."proman.workflows.vcs"]
    #             # git = "proman_workflows.git:namespace"
    #             {
    #                 'name': 'vcs',
    #                 'driver_name': 'git',
    #                 'driver_namespace': 'proman.workflows.vcs',
    #             },
    #             {
    #                 'name': 'sort-headers',
    #                 'driver_name': 'isort',
    #                 'driver_namespace': 'proman.workflows.formatter',
    #             },
    #             {
    #                 'name': 'format',
    #                 'driver_name': 'black',
    #                 'driver_namespace': 'proman.workflows.formatter',
    #             },
    #             {
    #                 'name': 'unit-tests',
    #                 'driver_name': 'pytest',
    #                 'driver_namespace': 'proman.workflows.unit_tests',
    #             },
    #             {
    #                 'name': 'gpg',
    #                 'driver_name': 'gpg',
    #                 'driver_namespace': 'proman.workflows.pki',
    #             },
    #             {
    #                 'name': 'tls',
    #                 'driver_name': 'tls',
    #                 'driver_namespace': 'proman.workflows.pki',
    #             },
    #         ]
    #     }
    #     return merge_dicts(defaults, default_plugins)


@dataclass
class ProjectDirs:
    """Project package."""

    working_dir: str = os.getcwd()
    python_path: str = sys.executable
    repo_dir: str = discover_repository(os.getcwd())
    base_dir: str = os.path.abspath(os.path.join(repo_dir, os.pardir))
    project_dir: str = field(init=False)
    hooks_dir: str = field(init=False)
    templates_dir: str = field(init=False)
    container_build_dir: str = field(init=False)
    specfiles: List[str] = field(default_factory=list, repr=False)

    def __post_init__(self) -> None:
        """Initialize project settings."""
        if self.specfiles == []:
            self.specfiles = ['pyproject.toml', 'setup.cfg']
        if not hasattr(self, 'project_dir'):
            self.project_dir = os.path.abspath(
                os.path.join(self.repo_dir, os.pardir)
            )
        if not hasattr(self, 'hooks_dir'):
            self.hooks_dir = os.path.join(self.repo_dir, 'hooks')
        if not hasattr(self, 'templates_dir'):
            self.templates_dir = os.path.join(self.base_dir, 'templates')
        if not hasattr(self, 'container_build_dir'):
            self.container_build_dir = self.base_dir


@dataclass
class GlobalConfig(ConfigFile):
    """Configuration for project management."""

    name: str
    writable: bool = True
    directory: str = field(init=False)
    filepath: str = field(init=False)

    def __post_init__(self) -> None:
        """Initialize settings from configuration."""
        self.directory = os.path.join(
            os.path.expanduser('~'), '.config', self.name
        )
        self.filepath = os.path.join(self.directory, 'proman.toml')
        super().__init__(
            self.filepath,
            writable=self.writable,
            separator='.',
        )
        if os.path.exists(self.filepath) and os.path.isfile(self.filepath):
            self.load()
        elif not os.path.exists(self.directory):
            os.makedirs(self.directory)
            self.dump()


# @dataclass
# class Credentials:
#     """Manage credentials."""
#
#     username: Optional[str] = None
#     password: Optional[str] = field(default=None, repr=False)
#     interactive: bool = True
#
#     def __post_init__(self) -> None:
#         """Initialize GPG settings."""
#         if self.interactive:
#             if not self.username:
#                 self.username = pyip.inputStr(
#                     prompt='Enter username: ',
#                     limit=255,
#                 )
#             if not self.password:
#                 self.password = pyip.inputPassword(
#                     prompt='Enter password: ',
#                     limit=255,
#                 )


@dataclass
class GPGConfig:
    """Manage GPG keys."""

    # commit_signing_key: str
    # package_signing_key: str
    home_dir: str = os.path.join(os.path.expanduser('~'), '.gnupg')


@dataclass
class DocsConfig:
    """Manage documentation configuration."""

    def __post_init__(self) -> None:
        """Initialize docs path."""
        if hasattr(self, 'base_dir'):
            print(self.base_dir)  # type: ignore


@dataclass
class WebConfig(ProjectDirs):
    """Manage web configuration."""

    environment = os.getenv('FLASK_ENV', 'development')
    webapp_dir: str = field(init=False)
    static_dir: str = field(init=False)

    def __post_init__(self) -> None:
        """Initialize settings."""
        if not hasattr(self, 'webapp_dir'):
            self.webapp_dir: str = os.path.join(self.base_dir, 'ui')
        if not hasattr(self, 'static_dir'):
            self.static_dir: str = os.path.join(self.webapp_dir, 'static')


@dataclass
class Container:
    """Manage container configuration."""

    runtime: Optional[str] = None

    def __post_init__(self) -> None:
        """Initialize container config."""
        if not hasattr(self, 'runtime'):
            if shutil.which('podman'):
                self.runtime = 'podman'
            elif shutil.which('docker'):
                self.runtime = 'docker'


@dataclass
class Plugin:
    """Provide proman_workflows plugin."""

    name: str
    driver_name: str
    driver_namespace: str


@dataclass
class Job:
    """Provide proman_workflows plugin."""

    command: str
    args: Dict[str, Any] = field(default_factory=dict, repr=False)


@dataclass
class Phase:
    """Provide proman_workflows plugin."""

    name: str
    plugins: Optional[List[str]] = field(default=None)
    jobs: List[Job] = field(default_factory=list, repr=False)


@dataclass
class ProjectConfig(ProjectDirs):
    """Configure project settings."""

    docs: Dict[str, Any] = field(default_factory=dict)
    specfile: Dict[str, Any] = field(default_factory=dict)
    plugins: List[Plugin] = field(default_factory=list)
    phases: List[Phase] = field(default_factory=list)
