# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quickdump']

package_data = \
{'': ['*']}

install_requires = \
['dill>=0.3.4,<0.4.0',
 'loguru>=0.6.0,<0.7.0',
 'pyzstd>=0.15.2,<0.16.0',
 'starlette[server]>=0.19.0,<0.20.0',
 'uvicorn[server]>=0.17.6,<0.18.0']

entry_points = \
{'console_scripts': ['server = quickdump.server:main']}

setup_kwargs = {
    'name': 'quickdump',
    'version': '0.3.0',
    'description': 'Quickly store arbitrary Python objects in unique files.',
    'long_description': '# quickdump\n\n\nQuickly store arbitrary Python objects in unique files.\n\n* Optionally generate unique file names based on current time/date, uid, \nor [ulid](https://github.com/mdomke/python-ulid)\n* Optionally create and use a `~/.quickdump` hidden directory in the home folder\n\n```python\nimport random\nimport time\nfrom dataclasses import dataclass\nfrom datetime import datetime, timedelta\n\nfrom quickdump import QuickDumper, QuickDumpLoader\n\n\n@dataclass\nclass SomeObj:\n    a: int\n    b: datetime\n    c: bytes\n\n\nif __name__ == "__main__":\n\n    with QuickDumper(\n            file_name="test_dump.qd",\n            dump_every=timedelta(seconds=2),\n    ) as dumper:\n\n        for i in range(100):\n            time.sleep(0.1)\n            obj = SomeObj(i, datetime.now(), random.randbytes(10))\n            print(f"Dumping obj: {obj}")\n            dumper.add(obj)\n\n    for file in dumper.produced_files:\n        for loaded_obj in QuickDumpLoader(input_file=file).iter_objects():\n            print(loaded_obj)\n    # Prints - SomeObj(a=0, b=datetime.datetime(2022, 3, 6, 12, 52, 28, 99256), c=b\';?w\\xeb\\xaa}\\xe8\\xb9tJ\')\n    #          ...\n    #          SomeObj(a=99, b=datetime.datetime(2022, 3, 6, 12, 52, 28, 175175), c=b\'%\\x93\\xdc\\x93\\x9e\\x08@\\xed\\xe1\\n\')\n    # Saves the objects in one file in each run on the ~/.quickdump dir.\n```\n',
    'author': 'Pedro Batista',
    'author_email': 'pedrovhb@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pedrovhb/quickdump',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
