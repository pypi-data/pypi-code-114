# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ingesture',
 'ingesture.export',
 'ingesture.export.nwb',
 'ingesture.fields',
 'ingesture.schema',
 'ingesture.spec']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'pandas>=1.1,<2.0',
 'parse>=1.19.0,<2.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'scipy>=1.8.0,<2.0.0']

extras_require = \
{'docs': ['Sphinx>=4.4.0,<5.0.0', 'furo>=2022.3.4,<2023.0.0'],
 'nwb': ['pynwb>=2.5.1,<3.0.0']}

setup_kwargs = {
    'name': 'ingesture',
    'version': '0.1.0',
    'description': 'Ingest gesturally-structured data into models with multiple export',
    'long_description': '# ingesture\nIngest gesturally-structured data into models with multiple export\n\nThis package is **not** even close to usable, and is just a sketch at the moment.\nIf for some reason you see it and would like to work on it with me, feel free to\nopen an issue :)\n\n\n# Declare your data\n\nEven the most disorganized data system has *some* structure. We want to be able\nto recover it without demanding that the entire acquisition process be reworked\n\nTo do that, we can use a family of specifiers to tell `ingest` where to get metadata\n\n```python\nfrom datetime import datetime\nfrom ingesture import Schema, spec\nfrom pydantic import Field\n\nclass MyData(Schema):\n    # parse metadata in a filename\n    subject_id: str = Field(..., \n        description="The ID of a subject of course!",\n        spec = spec.Path(\'electrophysiology_{subject_id}_*.csv\')\n    )\n    # parse multiple values at once\n    date: datetime\n    experimenter: str\n    date, experimenter = Field(...,\n        spec = spec.Path(\'{date}_{experimenter}_optodata.h5\')\n    )\n    \n    \n    # from inside a .mat file\n    other_meta: int = Field(...\n        spec = spec.Mat(\n            path=\'**/notebook.mat\', # 2 **s mean we can glob recursively\n            field = (\'nb\', 1, \'user\') # index recursively through the .mat\n        )\n    )\n    # and so on\n```\n\nThen, parse your schema from a folder\n\n```python\ndata = MyData.make(\'/home/lab/my_data\')\n```\n\nOr a bunch of them!\n\n```python\ndata = MyData.make(\'/home/lab/my_datas/*\')\n```\n\n## Multiple Strategies\n\n`todo`\n\n## Hierarchical Modeling\n\nOur data is rarely a single type, often there is a repeatable substructure that\nis paired with different macro-structures: eg. you have open-ephys data within a directory\nwith behavioral data in one experiment and paired with optical data in another.\n\nMake submodels and recombine them freely...\n\n`todo`\n\n\n# Export Data\n\nOnce we have data in an abstract model, then we want to be able to export it to\nmultiple formats! To do that we need an interface that describes\nthe basic methods of interacting with that format (eg. .csv files are\nwritten differently than hdf5 files) and a mapping from our model fields\nto locations, attributes, and names in the target format.\n\n## Pydantic base export\n\n### json\n\n## From the Field specification\n\n```python\nclass MyData(Schema):\n    subject_id: str = Field(\n        spec = ...,\n        nwb_field = "NWBFile:subject_id"\n    )\n```\n\n## From a `Mapping` object\n\n```python\n\nclass NWB_Map(Mapping):\n    subject_id = \'NWBFile:subject_id\'\n\nclass MyData(Schema):\n    subject_id: str = Field(...)\n    \n    __mapping__ = NWB_Map\n\n```\n    ',
    'author': 'sneakers-the-rat',
    'author_email': 'JLSaunders987@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/auto-pi-lot/ingest',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
