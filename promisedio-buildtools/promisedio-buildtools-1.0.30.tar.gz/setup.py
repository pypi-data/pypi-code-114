# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['promisedio_buildtools']

package_data = \
{'': ['*'],
 'promisedio_buildtools': ['include/_promisedio/atomic.h',
                           'include/_promisedio/atomic.h',
                           'include/_promisedio/atomic.h',
                           'include/_promisedio/atomic.h',
                           'include/_promisedio/atomic.h',
                           'include/_promisedio/atomic.h',
                           'include/_promisedio/atomic.h',
                           'include/_promisedio/base.h',
                           'include/_promisedio/base.h',
                           'include/_promisedio/base.h',
                           'include/_promisedio/base.h',
                           'include/_promisedio/base.h',
                           'include/_promisedio/base.h',
                           'include/_promisedio/base.h',
                           'include/_promisedio/capsule.h',
                           'include/_promisedio/capsule.h',
                           'include/_promisedio/capsule.h',
                           'include/_promisedio/capsule.h',
                           'include/_promisedio/capsule.h',
                           'include/_promisedio/capsule.h',
                           'include/_promisedio/capsule.h',
                           'include/_promisedio/chain.h',
                           'include/_promisedio/chain.h',
                           'include/_promisedio/chain.h',
                           'include/_promisedio/chain.h',
                           'include/_promisedio/chain.h',
                           'include/_promisedio/chain.h',
                           'include/_promisedio/chain.h',
                           'include/_promisedio/memory.h',
                           'include/_promisedio/memory.h',
                           'include/_promisedio/memory.h',
                           'include/_promisedio/memory.h',
                           'include/_promisedio/memory.h',
                           'include/_promisedio/memory.h',
                           'include/_promisedio/memory.h',
                           'include/_promisedio/module.h',
                           'include/_promisedio/module.h',
                           'include/_promisedio/module.h',
                           'include/_promisedio/module.h',
                           'include/_promisedio/module.h',
                           'include/_promisedio/module.h',
                           'include/_promisedio/module.h',
                           'include/_promisedio/uv.h',
                           'include/_promisedio/uv.h',
                           'include/_promisedio/uv.h',
                           'include/_promisedio/uv.h',
                           'include/_promisedio/uv.h',
                           'include/_promisedio/uv.h',
                           'include/_promisedio/uv.h',
                           'include/clinic_converters.h',
                           'include/clinic_converters.h',
                           'include/clinic_converters.h',
                           'include/clinic_converters/*',
                           'include/promisedio.h',
                           'include/promisedio.h',
                           'include/promisedio.h',
                           'include/promisedio_uv.h',
                           'include/promisedio_uv.h',
                           'include/promisedio_uv.h']}

install_requires = \
['requests>=2.27.1,<3.0.0']

entry_points = \
{'console_scripts': ['capsule = promisedio_buildtools.capsule:main',
                     'clinic = promisedio_buildtools.clinic:main',
                     'download_sources = '
                     'promisedio_buildtools.download_sources:main',
                     'memcheck = promisedio_buildtools.memcheck:main']}

setup_kwargs = {
    'name': 'promisedio-buildtools',
    'version': '1.0.30',
    'description': 'Promisedio build tools',
    'long_description': None,
    'author': 'aachurin',
    'author_email': 'aachurin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/promisedio/buildtools',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
