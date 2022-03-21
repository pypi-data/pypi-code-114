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
    'version': '0.2.0',
    'description': 'Manage your Metabase instance programmatically.',
    'long_description': "# metabase-manager\n\nManage your Metabase instance programmatically by declaring your desired state. Metabase-manager will create, update,\nand delete objects in Metabase to ensure to it matches your declared configuration.\n\n\n## Installation\n\n```shell\npip install metabase-manager\n```\n\n\n## Usage\n\nHere is an example configuration for Users and Groups:\n```yaml\n# metabase.yaml\n\nusers:\n  - email: jdoe@example.com\n    first_name: Jane\n    last_name: Doe\n    groups:\n      - Admin\n      - Finance\n\n  - name: jsmith@example.com\n    first_name: John\n    last_name: Smith\n    groups:\n      - Marketing\n\ngroups:\n  - name: Finance\n  - name: Marketing\n```\n\nBy running the following command, `metabase-manager` will create these users and groups if they don't already exist,\nupdate them if some attributes differ, and delete users and groups that exist in Metabase but are not declared here.\n```shell\nmetabase-manager sync --host=https://<org>.metabaseapp.com --user <email> --password <password>\n```\n\n\n### Supported Entities\n- Users\n- Groups\n",
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
