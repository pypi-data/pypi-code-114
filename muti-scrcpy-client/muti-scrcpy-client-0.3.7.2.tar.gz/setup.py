# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scrcpy', 'scrcpy_ui', 'scrcpy_ui.scrcpy']

package_data = \
{'': ['*']}

install_requires = \
['adbutils>=0.11.0,<0.12.0', 'av>=8.0.3,<9.0.0', 'opencv-python>=4.5.3,<5.0.0']

extras_require = \
{'ui': ['click>=7.0.0,<8.0.0', 'PySide6>=6.0.0,<7.0.0']}

entry_points = \
{'console_scripts': ['py-muti-scrcpy = scrcpy_ui:main']}

setup_kwargs = {
    'name': 'muti-scrcpy-client',
    'version': '0.3.7.2',
    'description': 'A muticlient of scrcpy',
    'long_description': '# Python Scrcpy Client\n<p>\n    <a href="https://pypi.org/project/muti-scrcpy-client/" target="_blank">\n        <img src="https://img.shields.io/pypi/v/muti-scrcpy-client" />\n    </a>\n    <a href="https://github.com/IanVzs/py-muti-scrcpy/blob/main/.github/workflows/ci.yml" target="_blank">\n        <img src="https://img.shields.io/github/workflow/status/ianvzs/py-muti-scrcpy/CI" />\n    </a>\n    <a href="https://app.codecov.io/gh/ianvzs/py-muti-scrcpy" target="_blank">\n        <img src="https://img.shields.io/codecov/c/github/ianvzs/py-muti-scrcpy" />\n    </a>\n    <img src="https://img.shields.io/github/license/ianvzs/py-muti-scrcpy" />\n    <a href="https://pepy.tech/project/muti-scrcpy-client" target="_blank">\n        <img src="https://pepy.tech/badge/muti-scrcpy-client" />\n    </a>\n    <a href="https://github.com/Genymobile/scrcpy/tree/v1.20" target="_blank">\n        <img src="https://img.shields.io/badge/scrcpy-v1.20-violet" />\n    </a>\n</p>\n\nThis package allows you to view and control android device in realtime.\n\n![demo png](https://raw.githubusercontent.com/ianvzs/py-muti-scrcpy/main/demo.png)  \n\nNote: This gif is compressed and experience lower quality than actual.\n\n## How to use\nTo begin with, you need to install this package via pip:\n```shell\npip install muti-scrcpy-client[ui]\n```\nThen, you can start `py-muti-scrcpy` to view the demo:\n\nNote: you can ignore `[ui]` if you don\'t want to view the demo ui\n\n## Document\nHere is the document GitHub page: [Documentation](https://leng-yue.github.io/py-scrcpy-client/)\nAlso, you can check `scrcpy_ui/main.py` for a full functional demo.\n\n## Reference & Appreciation\n- Core: [scrcpy](https://github.com/Genymobile/scrcpy)\n- Borther: [py-scrcpy-client](https://github.com/leng-yue/py-scrcpy-client/)\n- Idea: [py-android-viewer](https://github.com/razumeiko/py-android-viewer)\n- CI: [index.py](https://github.com/index-py/index.py)\n',
    'author': 'ianvzs',
    'author_email': 'ianvzs@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/IanVzs/py-muti-scrcpy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
