# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['openapydantic']

package_data = \
{'': ['*']}

install_requires = \
['email-validator>=1.1.3,<2.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'pyyaml>=5.3.1',
 'types-PyYAML>=6.0.5,<7.0.0']

setup_kwargs = {
    'name': 'openapydantic',
    'version': '0.1.1',
    'description': 'openapi specification parser based on pydantic',
    'long_description': '# Openapydantic\n\n[openapi](https://github.com/OAI/OpenAPI-Specification) specification validator based on [pydantic](https://pydantic-docs.helpmanual.io/).\n\n## Openapi versions supported\n\n- ❌ 2.0\n- ❌ 3.0.0\n- ❌ 3.0.1\n- ✅ 3.0.2\n- ❌ 3.0.3\n- ❌ 3.1.0\n\nIn my understanding, openapi versions are retrocompatibles (except for major version).\n\nSo 3.0.2 specification should be able to handle 3.0.0 and 3.0.1 data.\n\nUnittests handle this case (3.0.2 object automatically try to load previous version fixtures).\n\n## Installation\n\nDepending on your preference...\n\n```\n    pip install openapydantic\n```\n\n...or...\n\n```\n    poetry add openapydantic\n```\n\n## Usage\n\nOpenapydantic provide an openapi specification (a.k.a "swagger file" in version 2.X) parser based on pydantic.\n\nThis object represent an openapi structure for a specific openapi version.\n\nThe object\'s version is based on the openapi specification version.\n\nUsing parser:\n\n```python\nimport asyncio\n\nimport openapydantic\n\napi = asyncio.run(openapydantic.parse_api(file_path="openapi-spec.yaml"))\nprint(api.info)\n# if my openapi version is "3.0.2", api is an instance of OpenApi302\n```\n\nYou can use an explicit openapi version but you have to pass a dict object.\n\nIt may be useful for backward compatibility (for eg: create an OpenApi302 object using data from an 3.0.1 openapi specfication ).\n\n```python\nimport yaml\n\nimport openapydantic\n\nraw_api=None\nwith open("openapi-spec.yaml", "r") as file:\n    raw_api = yaml.safe_load(file)\n\napi = openapydantic.OpenApi302(**raw_api) # 3.0.2 openapi pydantic object\nprint(api.info)\n```\n\nFor more usage example, please refers to the *tests/* folder\n',
    'author': 'Richard Devers',
    'author_email': 'ritchiedev25@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/richarddevers/openapydantic',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
