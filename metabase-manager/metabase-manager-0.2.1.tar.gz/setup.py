# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['metabase_manager', 'metabase_manager.cli']

package_data = \
{'': ['*']}

install_requires = \
['alive-progress', 'metabase-python>=0.3.0,<0.4.0', 'pyyaml']

entry_points = \
{'console_scripts': ['metabase-manager = metabase_manager.cli.main:cli']}

setup_kwargs = {
    'name': 'metabase-manager',
    'version': '0.2.1',
    'description': 'Manage your Metabase instance programmatically.',
    'long_description': "# metabase-manager\n\nManage your Metabase instance programmatically by declaring your desired state. `metabase-manager` will create, update,\nand delete objects in Metabase to ensure to it matches your declared configuration.\n\n\n## Installation\n\n```shell\npip install metabase-manager\n```\n\n\n## Usage\n\nHere is an example configuration for Users and Groups:\n```yaml\n# metabase.yml\n\nusers:\n  - email: jdoe@example.com\n    first_name: Jane\n    last_name: Doe\n    groups:\n      - Administrators\n      - Finance\n\n  - name: jsmith@example.com\n    first_name: John\n    last_name: Smith\n    groups:\n      - Marketing\n\ngroups:\n  - name: Finance\n  - name: Marketing\n```\n\nBy running the following command, `metabase-manager` will create these users and groups if they don't already exist,\nupdate them if some attributes differ, and delete users and groups that exist in Metabase but are not declared here.\n```shell\nmetabase-manager sync\n```\n\n```shell\n[CREATE] Group(name='Finance')\n[CREATE] Group(name='Marketing')\n[DELETE] Group(name='Sales')      # Sales is not defined in metabase.yml\n[CREATE] User(first_name='Jane', last_name='Doe', email='jdoe@example.com', groups=[Group(name='Administrators'), Group(name='Finance')])\n# jsmith@example.com already exists in Metabase, but some attributes or group membership differ\n[UPDATE] User(first_name='John', last_name='Smith', email='jsmith@example.com', groups=[Group(name='Marketing')])\n```\n\n### Credentials\n\nIt is possible to provide credentials to your Metabase instance through the command-line as follows:\n\n```shell\nmetabase-manager sync --host=https://<org>.metabaseapp.com --user <email> --password <password>\n```\n\nIt is also possible to provide credentials as environment variables. `metabase-manager` will automatically use\nthese variables if they are set in the environment.\n\n- `METABASE_HOST=<host>`\n- `METABASE_USER=<user>`\n- `METABASE_PASSWORD=<password>`\n\n\n### Configuration\n\nBy default, `metabase-manager` will expect to find a `metabase.yml` file in the current directory. You can override this\ndefault, and optionally provide more than one file, with the `--file/-f` parameter.\n\n```shell\nmetabase-manager sync -f users.yml -f <directory>/groups.yml\n```\n\n### Selection\n\nIt is possible to run your sync only for certain types of objects by using the `--select/-s` or `--exclude/-e` options.\n\n```shell\nmetabase-manager sync --select users  # only users will be synced\n```\n\n```shell\nmetabase-manager sync --exclude users  # everything by users will be synced\n```\n\n\n### Dry Run\n\nIt is possible to execute a dry run to see which objects would be created, updated, or deleted given your configuration.\nThis will only log the changes, but not actually execute any changes on your Metabase instance.\n\n```shell\nmetabase-manager sync --dry-run\n```\n\n\n### Upsert Only\n\nIf you do not want `metabase-manager` to delete anything in your Metabase instance, you can use the `--no-delete` flag.\nThis is useful if your `metabase.yml` configuration file does not exhaustively define object that you wish to exist in\nyour Metabase instance.\n\n```shell\nmetabase-manager sync --no-delete\n```\n\n\n\n### Supported Entities\n\nCurrently, it is possible to manage the following entities:\n\n- Users\n- Groups\n",
    'author': 'Charles Lariviere',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/chasleslr/metabase-manager',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
