# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['slap',
 'slap.ext',
 'slap.ext.application',
 'slap.ext.changelog_update_automation',
 'slap.ext.checks',
 'slap.ext.project_handlers',
 'slap.ext.release',
 'slap.ext.repository_handlers',
 'slap.ext.repository_hosts',
 'slap.util',
 'slap.util.external']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=4.0',
 'beautifulsoup4>=4.10.0,<5.0.0',
 'cleo>=1.0.0a4',
 'databind>=2.0.0a2,<3.0.0',
 'flit>=3.6.0,<4.0.0',
 'nr.util>=0.8.4,<1.0.0',
 'poetry-core>=1.1.0a6,<2.0.0',
 'ptyprocess>=0.7.0,<0.8.0',
 'pygments>=2.11.2,<3.0.0',
 'requests>=2.27.1,<3.0.0',
 'tomli>=2.0.0,<3.0.0',
 'twine>=3.7.0,<4.0.0']

entry_points = \
{'console_scripts': ['slap = slap.__main__:main'],
 'slap.plugins.application': ['changelog = '
                              'slap.ext.application.changelog:ChangelogCommandPlugin',
                              'check = '
                              'slap.ext.application.check:CheckCommandPlugin',
                              'info = '
                              'slap.ext.application.info:InfoCommandPlugin',
                              'init = '
                              'slap.ext.application.init:InitCommandPlugin',
                              'install = '
                              'slap.ext.application.install:InstallCommandPlugin',
                              'link = '
                              'slap.ext.application.link:LinkCommandPlugin',
                              'publish = '
                              'slap.ext.application.publish:PublishCommandPlugin',
                              'release = '
                              'slap.ext.application.release:ReleaseCommandPlugin',
                              'run = slap.ext.application.run:RunCommandPlugin',
                              'test = '
                              'slap.ext.application.test:TestCommandPlugin',
                              'venv = slap.ext.application.venv:VenvPlugin'],
 'slap.plugins.changelog_update_automation': ['github-actions = '
                                              'slap.ext.changelog_update_automation.github_actions:GithubActionsChangelogUpdateAutomationPlugin'],
 'slap.plugins.check': ['changelog = '
                        'slap.ext.checks.changelog:ChangelogValidationCheckPlugin',
                        'general = slap.ext.checks.general:GeneralChecksPlugin',
                        'poetry = slap.ext.checks.poetry:PoetryChecksPlugin',
                        'release = '
                        'slap.ext.checks.release:ReleaseChecksPlugin'],
 'slap.plugins.project': ['flit = '
                          'slap.ext.project_handlers.flit:FlitProjectHandler',
                          'poetry = '
                          'slap.ext.project_handlers.poetry:PoetryProjectHandler',
                          'setuptools = '
                          'slap.ext.project_handlers.setuptools:SetuptoolsProjectHandler'],
 'slap.plugins.release': ['changelog_release = '
                          'slap.ext.release.changelog:ChangelogReleasePlugin',
                          'source_code_version = '
                          'slap.ext.release.source_code_version:SourceCodeVersionReferencesPlugin'],
 'slap.plugins.repository': ['default = '
                             'slap.ext.repository_handlers.default:DefaultRepositoryHandler'],
 'slap.plugins.repository_host': ['github = '
                                  'slap.ext.repository_hosts.github:GithubRepositoryHost'],
 'slap.plugins.version_incrementing_rule': ['major = '
                                            'slap.ext.version_incrementing_rule:major',
                                            'minor = '
                                            'slap.ext.version_incrementing_rule:minor',
                                            'patch = '
                                            'slap.ext.version_incrementing_rule:patch',
                                            'premajor = '
                                            'slap.ext.version_incrementing_rule:premajor',
                                            'preminor = '
                                            'slap.ext.version_incrementing_rule:preminor',
                                            'prepatch = '
                                            'slap.ext.version_incrementing_rule:prepatch',
                                            'prerelease = '
                                            'slap.ext.version_incrementing_rule:prerelease']}

setup_kwargs = {
    'name': 'slap-cli',
    'version': '1.3.2',
    'description': 'Slap is a command-line utility for developing Python applications.',
    'long_description': '# slap\n\nSlap is a command-line tool for developing Python projects that provides a common interface for many tasks independent\nof the build system you use (currently supporting Setuptools via Pyproject, Poetry and Flit). It makes it easier to\nmanage monorepositories of multiple projects which may even have inter-dependencies.\n\n> Developer\'s note: I personally use Poetry as the build system for some of its features, in particular because of\n> its support for semantic version selectors which are not supported by Setuptools or Flit; but never actually\n> use the Poetry CLI because I too often run into issues with it\'s dependency resolution and installation mechanism\n> as well as its implicitly created virtual environments.\n\nSlap provides a variety of features, including but not limited to\n\n* Sanity check your project configuration\n* Install your project and it\'s dependencies via Pip (in the right order in case of a monorepository)\n* Symlink your project (using Flit\'s symlinking function internally, independent of your actual build system; Poetry\n  does not support editable installs so this is really convenient)\n* Build and publish your project (and all its individual packages in case of a monorepository) to Pypi using Twine\n* Release new versions (automatically update version numbers in code, create a Git tag and push)\n* Run tests configured in your Pyproject config under `[tool.slap.test]`\n* Manage local (`~/.venvs`) and global (`~/.local/venvs`) virtual environments (backed by Python\'s `venv` module)\n* Manage structured changelogs (TOML) via the CLI; easily inject PR URLs into changelog entries in pull requests via CI\n\n## Installation\n\nIt is recommended to install Slap via Pipx, but you can also install it with Pip directly.\n\n    $ pipx install slap-cli\n\n> __Note__: Currently, Slap relies on an alpha version of `poetry-core` (`^1.1.0a6`). If you install it into\n> the same environment as Poetry itself, you may also need to use an alpha version of Poetry (e.g. `1.2.0a2`).\n\n## Usage examples\n\nBootstrap a (opinionated) Poetry project using Slap.\n\n    $ slap init --name my.pkg\n    write my-pkg/pyproject.toml\n    write my-pkg/LICENSE\n    write my-pkg/readme.md\n    write my-pkg/.gitignore\n    write my-pkg/src/my/pkg/__init__.py\n    write my-pkg/test/test_import.py\n    write my-pkg/src/my/pkg/py.typed\n\nSanity check your project configuration\n\n    $ slap check\n    Checks for project slap-cli\n\n      changelog:validate           OK             — All 74 changelogs are valid.\n      general:packages             OK             — Detected /home/niklas/git/slap/src/slap\n      general:typed                OK             — py.typed exists as expected\n      poetry:classifiers           OK             — All classifiers are valid.\n      poetry:license               OK             — License "MIT" is a valid SPDX identifier.\n      poetry:readme                OK             — Poetry readme is configured correctly (path: readme.md)\n      poetry:urls                  RECOMMENDATION — Please configure the following URLs: "Bug Tracker"\n      release:source-code-version  OK             — Found __version__ in slap\n\nInstall and link your project (by default, the command protects you from accidentally installing the project; you can pass `--no-venv-check` to skip this safeguard).\n\n    $ slap install --link\n\nValidate the version numbers in your project and release a new version.\n\n    $ slap release --validate\n    versions are ok\n      pyproject.toml:          1.2.4 # version = "1.2.4"\n      src/slap/__init__.py:    1.2.4 # __version__ = \'1.2.4\'\n    $ slap release --tag --push minor\n    bumping 3 version references to 1.3.0\n      pyproject.toml:          1.2.4 → 1.3.0 # version = "1.2.4"\n      src/slap/__init__.py:    1.2.4 → 1.3.0 # __version__ = \'1.2.4\'\n\n    releasing changelog\n      .changelog/_unreleased.toml → .changelog/1.3.0.toml\n\n    tagging 1.3.0\n\n    pushing develop, 1.3.0 to origin\n',
    'author': 'Niklas Rosenstein',
    'author_email': 'rosensteinniklas@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
