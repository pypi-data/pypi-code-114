# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['ice',
 'ice.api',
 'ice.api.models',
 'ice.api.scripts',
 'ice.api.transforms',
 'ice.api.transforms.image',
 'ice.core',
 'ice.llutil',
 'ice.llutil.launcher',
 'ice.llutil.multiprocessing']

package_data = \
{'': ['*'], 'ice.llutil': ['include/*']}

install_requires = \
['PySocks>=1.7.1,<2.0.0',
 'gputil>=1.4.0,<2.0.0',
 'multiprocess>=0.70.12,<0.71.0',
 'opencv-python>=4.5.5,<5.0.0',
 'setuptools==59.5.0',
 'tensorboard>=2.8.0,<3.0.0',
 'tqdm>=4.62.3,<5.0.0',
 'varname>=0.8.1,<0.9.0']

extras_require = \
{'pycuda': ['pycuda>=2021.1,<2022.0']}

entry_points = \
{'console_scripts': ['wait_process = ice.api.scripts.wait_process:_cli']}

setup_kwargs = {
    'name': 'ice-learn',
    'version': '0.3.1',
    'description': 'A high-level Deep Learning framework that extends PyTorch and PyCUDA.',
    'long_description': '# ice-learn\n\n<img align="left" width="128" height="128" src="https://s3.bmp.ovh/imgs/2022/03/e33e7e297b95b74c.jpg">\n\n> `ice` is a sweet extension of PyTorch, a modular high-level deep learning framework that extends and integrates PyTorch and PyCUDA with intuitive interfaces. We aims not only to minimize the boilerplate code without loss of functionality, but also maximize the flexibility and usability for extending and composing any deep learning tasks into an integrate multi-task learning program.\n\n**NOTE:** It is currently in pre-alpha versions, and the API is subject to change.\n\n## Features\n\n- **Minimize Boilerplates**: You don\'t need to repeat yourself.\n  - **Config Once, Use Everywhere:** Every mutable class can be converted into a `configurable`. Configuration for deep learning project has never been this easy before. A tagging system to manage and reuse any type of resources you need.\n  - **Inplace Argument Parser:** You can parse command line argument instantly without a long page of previous definition.\n\n- **Maximize Flexiblility**: Painless and Incremental Extension from CUDA to non-standard data-preprocessing and training schedules for multi-task learning.\n  - The kernel data structure of `ice` is a **Hypergraph** that manages different module nodes (e.g. `ice.DatasetNode`, `ice.ModuleNode`, etc.) that are switchable between multiple user-defined execution modes. Extending a new dataset, network module or loss function is by adding new `nn.Dataset`s, `nn.Module`s and python `callable`s to specific mode of the entire graph.\n  - We provide **PyCUDA** support by automatically managing the PyCUDA context as well as providing a simplified `torch.Tensor` class wrapper that supports efficient multi-dimensional element access in CUDA codes. This feature manages to make writing, compile, execution and testing CUDA extensions for PyTorch extremely fast. We also provide a [VSCode extension](https://marketplace.visualstudio.com/items?itemName=huangyuyao.pycuda-highlighter) for PyCUDA docstring highlight.\n  - We support **Multi-Task Learning** training by finding the **Pareto Optimal** for each task weight so that you do not need to tune them manually. (**TODO**)\n  - We support [dill](https://github.com/uqfoundation/dill)-backended **Elastic Multiprocessing** launch and management that is compitable with **Lambda Function and Closures**. You can not only build multi-gpu or multi-machine Data Distributed Parallel training program without effort, but also doesn\'t require to concern about pickability of any part of program in your application. We actually suggest heavy use of lambda functions such as for simple input and output transforms of modules. This feature also contributes to the *minimal boilerplates* aim of `ice`.\n\n## Install\n\n`pip install ice-learn` **(TODO)**\n\n**Note:** Currently installing via pip is not available, developers can install ice using poetry environment as specified [here](https://github.com/tjyuyao/ice-learn/blob/main/docs/resources/dev_notes/00_setup_devenv.md).\n\n## Documentation\n\nYou can access documentation through [Online Documentation Site](https://tjyuyao.github.io/ice-learn/), or the [`docs` subdirectory](https://github.com/tjyuyao/ice-learn/tree/main/docs) directly. The documentation is partial auto-generated from comment, and partial manually written, the note on how we produce the documenation can be found [here](https://tjyuyao.github.io/ice-learn/resources/dev_notes/02_docs_and_tests/).\n',
    'author': 'Yuyao Huang',
    'author_email': 'yycv.simon@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tjyuyao/ice-learn',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
