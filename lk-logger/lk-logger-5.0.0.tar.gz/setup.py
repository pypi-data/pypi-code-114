# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lk_logger',
 'lk_logger.analyser',
 'lk_logger.config',
 'lk_logger.plugins',
 'lk_logger.scanner']

package_data = \
{'': ['*']}

install_requires = \
['pytermgui']

setup_kwargs = {
    'name': 'lk-logger',
    'version': '5.0.0',
    'description': 'Python advanced print with varnames.',
    'long_description': '# LK Logger\n\nAdvanced print tool for Python.\n\nFeatures:\n\n- Simple. Add two lines of code to enable lk-logger.\n\n    ```python\n    import lk_logger\n    lk_logger.setup()\n    ```\n\n    It will replace Python\'s built-in `print` function to take care all the leftovers.\n\n- Non-intrusive. After enable it like above, no more modifications on your source code projects (this is low-cost and low-effort migration). You will see new effects at once.\n\n    This would be a good chioce for developers who have already dived into their own projects with Python `print` too much to get a new start with a new logging tool.\n\n- Code highlight.\n\n    ![](.assets/20220321155834.png)\n\n- Show both varnames and values.\n\n    before:\n\n    ```python\n    a, b = 1, 2\n    print(\'a = {}, b = {}, a + b = {}\'.format(a, b, a + b))\n    ```\n\n    after:\n\n    ```python\n    import lk_logger\n    lk_logger.setup(show_varnames=True)\n    a, b = 1, 2\n    print(a, b, a + b)\n    ```\n\n    ![](.assets/20220321153646.png)\n\n## Install\n\n```shell\npip install lk-logger\n```\n\nThe latest version is 5.0.0 or higher.\n\n## Quick Start\n\n```python\nimport lk_logger\nlk_logger.setup(show_varnames=True)\n\nprint(\'hello world\')\n\na, b = 1, 2\nprint(a, b, a + b)\n\nprint(a, b, (c := a + b), c + 3)\n```\n\nScreenshot:\n\n![](.assets/20220321154014.png)\n\n## Advanced Usage\n\nGenerally, the two lines of code above are enough to use.\n\nThe advanced feature is its "markup" shorthand.\n\nUse a markup as in the first or the last parameter, the markup is a string that starts with \':\', consists of multiple marks.\n\nFor example:\n\n```python\nprint(\':i\', \'monday\')\nprint(\':i\', \'tuesday\')\nprint(\':i\', \'wednesday\')\n```\n\nIt prints weekdays with a numeric prefix:\n\n![](.assets/20220321155834.png)\n\nAnother one:\n\n```python\nprint(\'this is a divider\', \':d\')\n\nprint(\':v0\', \'this is a TRACE message\')\nprint(\':v1\', \'this is a DEBUG message\')\nprint(\':v2\', \'this is a INFO  message\')\nprint(\':v3\', \'this is a WARN  message\')\nprint(\':v4\', \'this is a ERROR message\')\nprint(\':v5\', \'this is a FATAL message\')\n```\n\n![](.assets/20220321160102.png)\n\n**Here are list of all available marks:**\n\n| Mark | Description                                  |\n| :--- | :------------------------------------------- |\n| `:d` | divider line                                 |\n| `:i` | index                                        |\n| `:l` | long / loose format (multiple lines)         |\n| `:p` | parent layer                                 |\n| `:r` | rich format                                  |\n| `:s` | short / single line format                   |\n| `:t` | timestamp (not available in current version) |\n| `:v` | verbosity / log level                        |\n\n**Markup options:**\n\n```\n:d0     default divider line (default)\n:d1+    user defined (if not, fallback to :d0)\n\n:i0     reset index\n:i1     number width fixed to 1 (1, 2, 3, ... 9, 10, 11, ...) (default)\n:i2     number width fixed to 2 (01, 02, 03, ..., 99, 100, 101, ...)\n:i3     number width fixed to 3 (001, 002, 003, ..., 999, 1000, 1001, ...)\n:i4~8   number width fixed to 4/5/6/7/8\n:i9+    reserved, not defined yet (will be fallback to :i1)\n\n:l0     let lk-print decide how to format long message (default)\n:l1     force expand all nodes\n\n:p0     self layer\n:p1     parent layer (default)\n:p2     grand parent layer\n:p3     great grand parent layer\n:p4     great great grand parent layer\n:p5+    great great grand ... grand parent layer\n        note: be careful using :p2+, it may crash if the layer not exists\n\n:v0     trace (default)\n        if you don\'t like using number, you can use an alias :vt\n:v1     debug (alias is :vd)\n:v2     info (alias is :vi)\n:v3     warning (alias is :vw)\n:v4     error (alias is :ve)\n:v5     fatal (alias is :vf)\n:v6+    user defined (if not, fallback to :v0)\n```\n\n**Detailed examples:**\n\nSee [examples/02_all_markup_usages.py](examples/02_all_markup_usages.py).\n\nScreenshot:\n\n![](.assets/20220321161728.png)\n\n## Caution\n\n- The back slash will be forcely converted to forward slash.\n\n    ```python\n    print(r\'C:\\Users\\<Username>\\AppData\\Local\\Temp\')\n    ```\n\n    ![](.assets/20220321155215.png)\n\n    There remained an unresolved issue in its internal parser. We will fix it in future version.\n',
    'author': 'Likianta',
    'author_email': 'likianta@foxmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
