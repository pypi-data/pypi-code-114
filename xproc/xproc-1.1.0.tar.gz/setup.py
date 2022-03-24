# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xproc']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['xproc = xproc.console:main']}

setup_kwargs = {
    'name': 'xproc',
    'version': '1.1.0',
    'description': 'Linux Proc File System Snooper',
    'long_description': '# [xproc](https://github.com/hungrybirder/xproc)\n\n## Install\n\n```bash\npip install -U xproc\n```\n\n## Support commands\n\n*   `xproc mem` or `xproc meiw`\n\n```bash\nxproc mem\n        TIME       KERNEL         USER      MemFree     MemTotal\n    21:19:37    1345876kB   13143712kB   10079620kB   24624680kB\n    21:19:38    1345964kB   13143796kB   10079612kB   24624680kB\n    21:19:39    1345964kB   13143804kB   10079612kB   24624680kB\n    21:19:40    1345964kB   13143808kB   10079644kB   24624680kB\n    21:19:41    1345964kB   13143808kB   10079580kB   24624680kB\n```\n\n```bash\nxproc mem -e "Active,Inactive,Active(anon),Inactive(anon),Active(file),Inactive(file)"\n        TIME       Active     Inactive Active(anon) Inactive(anon) Active(file) Inactive(file)\n    21:21:19    4397264kB    8727816kB     173164kB          128kB    4224100kB      8727688kB\n    21:21:21    4397404kB    8727816kB     173300kB          128kB    4224104kB      8727688kB\n    21:21:23    4397404kB    8727816kB     173300kB          128kB    4224104kB      8727688kB\n    21:21:25    4397404kB    8727816kB     173300kB          128kB    4224104kB      8727688kB\n    21:21:27    4397404kB    8727816kB     173300kB          128kB    4224104kB      8727688kB\n```\n',
    'author': 'liyong',
    'author_email': 'hungrybirder@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hungrybirder/xproc',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
