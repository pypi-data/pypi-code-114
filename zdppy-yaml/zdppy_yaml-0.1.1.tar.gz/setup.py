# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zdppy_yaml', 'zdppy_yaml.libs', 'zdppy_yaml.libs.yaml']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'zdppy-yaml',
    'version': '0.1.1',
    'description': 'Python读取yaml配置，无任何依赖，符合中国人使用习惯',
    'long_description': '# zdppy_yaml\npython解析yaml文件\n\n## 版本历史\n',
    'author': 'zhangdapeng',
    'author_email': 'pygosuperman@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/zhangdapeng520/zdppy_yaml',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
