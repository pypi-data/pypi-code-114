# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datacards']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'datasets>=1.14.0,<2.0.0',
 'pydantic>=1.8.0,<2.0.0',
 'rich[jupyter]>=10.14.0,<11.0.0']

setup_kwargs = {
    'name': 'datacards',
    'version': '0.1.1',
    'description': 'Append missing model cards to Huggingface datasets',
    'long_description': "# Datacard\n\nThis repo aims to find and update the missing model cards for Hugging face datasets.\n\nIf you find this a worth while pursute, feel free to reach out and let's try to make the Hugging face datasets complete :wink:\n\n## Setup\n\n```shell\n# install poetry\ngit clone --recurse-submodules --remote-submodules git@github.com:Hugging-Face-Supporter/datacards.git\ncd datacards\ngit submodule update\n\npoetry install\n```\n\n## Run\n\n```shell\npoetry shell\npython datacards/main.py\n```\n\n## WIP\n\n- [x] Look into how to provide multiple answers in model card (ex. Glue dataset)\n- [x] Find the datasets that are missing information by parsing the README\n- [x] Find ways to know what categories are valid answers\n- [ ] Create method to filter for missing datasets\n- [ ] Create [tool to annotate the datasets](https://huggingface.co/spaces/huggingface/datasets-tagging/blob/main/tagging_app.py)\n- [ ] Toggle between datasets to annotate.\n- [ ] Save modified files to the README again\n- [ ] Once done, find ways to create automatic PR to Hugging face datasets\n",
    'author': 'MarkusSagen',
    'author_email': 'markus.john.sagen@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Hugging-Face-Supporter/datacards',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
