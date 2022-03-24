# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dbt_coves',
 'dbt_coves.config',
 'dbt_coves.core',
 'dbt_coves.tasks',
 'dbt_coves.tasks.extract',
 'dbt_coves.tasks.generate',
 'dbt_coves.tasks.load',
 'dbt_coves.ui',
 'dbt_coves.utils']

package_data = \
{'': ['*'], 'dbt_coves': ['templates/*']}

install_requires = \
['Jinja2>=2.11.2,<2.12.0',
 'PyYAML>=5.4.1',
 'click>=8.0.3,<9.0.0',
 'cookiecutter>=1.7.3,<2.0.0',
 'dbt-bigquery>=1.0.0,<2.0.0',
 'dbt-core>=0.18.0,<2.0.0',
 'dbt-redshift>=1.0.0,<2.0.0',
 'dbt-snowflake>=1.0.0,<2.0.0',
 'luddite>=1.0.1,<2.0.0',
 'packaging>=20.8,<21.0',
 'pre-commit>=2.15.0,<3.0.0',
 'pretty-errors>=1.2.19,<2.0.0',
 'pydantic>=1.8,<2.0',
 'pyfiglet>=0.8.post1,<0.9',
 'python-slugify>=5.0.2,<6.0.0',
 'questionary>=1.9.0,<2.0.0',
 'rich>=10.4.0,<11.0.0',
 'sqlfluff-templater-dbt>=0.9.1,<0.10.0',
 'sqlfluff>=0.9.1,<0.10.0',
 'yamlloader>=1.0.0,<2.0.0']

entry_points = \
{'console_scripts': ['dbt-coves = dbt_coves.core.main:main']}

setup_kwargs = {
    'name': 'dbt-coves',
    'version': '1.0.4a1',
    'description': 'CLI tool for dbt users adopting analytics engineering best practices.',
    'long_description': "\ndbt-coves\n*********\n\n|Maintenance| |PyPI version fury.io| |Code Style| |Checked with mypy| |Imports: isort| |Imports: python| |Build| |pre-commit.ci status| |codecov| |Maintainability| |Downloads|\n\n.. |Maintenance| image:: https://img.shields.io/badge/Maintained%3F-yes-green.svg\n   :target: https://github.com/datacoves/dbt-coves/graphs/commit-activity\n\n.. |PyPI version fury.io| image:: https://badge.fury.io/py/dbt-coves.svg\n   :target: https://pypi.python.org/pypi/dbt-coves/\n\n.. |Code Style| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n   :target: https://github.com/ambv/black\n\n.. |Checked with mypy| image:: http://www.mypy-lang.org/static/mypy_badge.svg\n   :target: http://mypy-lang.org\n\n.. |Imports: isort| image:: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336\n   :target: https://pycqa.github.io/isort/\n\n.. |Imports: python| image:: https://img.shields.io/badge/python-3.8%20%7C%203.9-blue\n   :target: https://img.shields.io/badge/python-3.8%20%7C%203.9-blue\n\n.. |Build| image:: https://github.com/datacoves/dbt-coves/actions/workflows/main_ci.yml/badge.svg\n   :target: https://github.com/datacoves/dbt-coves/actions/workflows/main_ci.yml/badge.svg\n\n.. |pre-commit.ci status| image:: https://results.pre-commit.ci/badge/github/bitpicky/dbt-coves/main.svg\n   :target: https://results.pre-commit.ci/latest/github/datacoves/dbt-coves/main\n\n.. |codecov| image:: https://codecov.io/gh/datacoves/dbt-coves/branch/main/graph/badge.svg?token=JB0E0LZDW1\n   :target: https://codecov.io/gh/datacoves/dbt-coves\n\n.. |Maintainability| image:: https://api.codeclimate.com/v1/badges/1e6a887de605ef8e0eca/maintainability\n   :target: https://codeclimate.com/github/datacoves/dbt-coves/maintainability\n\n.. |Downloads| image:: https://pepy.tech/badge/dbt-coves\n   :target: https://pepy.tech/project/dbt-coves\n\nWhat is dbt-coves?\n==================\n\ndbt-coves is a complimentary CLI tool for `dbt <https://www.getdbt.com>`_ that allows users to quickly apply `Analytics Engineering <https://www.getdbt.com/what-is-analytics-engineering/>`_ best practices.\n\ndbt-coves helps with the generation of scaffold for dbt by analyzing your data warehouse schema in Redshift, Snowflake, or Big Query and creating the necessary configuration files (sql and yml).\n\n⚠️ **dbt-coves is in alpha version. Don’t use on your prod models unless you have tested it before.**\n\nHere's the tool in action\n-------------------------\n\n.. image:: https://cdn.loom.com/sessions/thumbnails/74062cf71cbe4898805ca508ea2d9455-1624905546029-with-play.gif\n   :target: https://www.loom.com/share/74062cf71cbe4898805ca508ea2d9455\n\nSupported dbt versions\n======================\n\n.. list-table::\n   :header-rows: 1\n\n   * - Version\n     - Status\n   * - <= 0.17.0\n     - ❌ Not supported\n   * - 0.18.x - 0.21x\n     - ✅ Tested\n   * - 1.x\n     - ✅ Tested\n\nSupported adapters\n==================\n\n.. list-table::\n   :header-rows: 1\n\n   * - Feature\n     - Snowflake\n     - Redshift\n     - BigQuery\n     - Postgres\n   * - profile.yml generation\n     - ✅ Tested\n     - 🕥 In progress\n     - ❌ Not tested\n     - ❌ Not tested\n   * - sources generation\n     - ✅ Tested\n     - 🕥 In progress\n     - ❌ Not tested\n     - ❌ Not tested\n",
    'author': 'Datacoves',
    'author_email': 'hello@datacoves.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://datacoves.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
