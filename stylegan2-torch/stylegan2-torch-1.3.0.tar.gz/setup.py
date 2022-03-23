# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stylegan2_torch',
 'stylegan2_torch.discriminator',
 'stylegan2_torch.generator',
 'stylegan2_torch.op']

package_data = \
{'': ['*']}

install_requires = \
['torch-conv-gradfix>=0.1.0', 'torch>=1.7.0']

entry_points = \
{'console_scripts': ['docs = stylegan2_torch:__docs',
                     'serve = stylegan2_torch:__serve',
                     'test = stylegan2_torch:__test']}

setup_kwargs = {
    'name': 'stylegan2-torch',
    'version': '1.3.0',
    'description': 'A simple, typed, commented Pytorch implementation of StyleGAN2.',
    'long_description': "# StyleGAN2 Pytorch - Typed, Commented, Installable :)\n\nA simple, typed, commented Pytorch implementation of StyleGAN2.\n\n![action](https://img.shields.io/github/workflow/status/ppeetteerrs/stylegan2-torch/build?logo=githubactions&logoColor=white)\n[![pypi](https://img.shields.io/pypi/v/stylegan2-torch.svg)](https://pypi.python.org/pypi/stylegan2-torch)\n[![codecov](https://img.shields.io/codecov/c/github/ppeetteerrs/stylegan2-torch?label=codecov&logo=codecov)](https://app.codecov.io/gh/ppeetteerrs/stylegan2-torch)\n[![docs](https://img.shields.io/github/deployments/ppeetteerrs/stylegan2-torch/github-pages?label=docs&logo=readthedocs)](https://ppeetteerrs.github.io/stylegan2-torch)\n\nThis implementation is adapted from [here](https://github.com/rosinality/stylegan2-pytorch). This implementation seems more stable and editable than the over-engineered official implementation.\n\nThe focus of this repository is simplicity and readability. If there are any bugs / issues, please kindly let me know or submit a pull request!\n\nRefer to [my blog post](https://ppeetteerrsx.com/post/cuda/stylegan_cuda_kernels/) for an explanation on the custom CUDA kernels. The profiling code to optimize the custom operations is [here](https://github.com/ppeetteerrs/pytorch-cuda-kernels).\n\n## Installation\n\n```bash\npip install stylegan2-torch\n```\n\n## Training Tips\n\n1. Use a multi-GPU setup. An RTX 3090 can handle batch size of up to 8 at 1024 resolution. Based on experience, batch size of 8 works but 16 or 32 should be safer.\n2. Use LMDB dataset + SSD storage + multiple dataloader workers (and a big enough prefetch factor to cache at least one batch ahead). You never know how much time you waste on dataloading until you optimize it. For me, that shorted the training time by 30% (more time-saving than the custom CUDA kernels).\n\n## Known Issues\n\nPytorch is known to cause random reboots when using non-deterministic algorithms. Set `torch.use_deterministic_algorithms(True)` if you encounter that.\n\n## To Dos / Won't Dos\n1. Tidy up `conv2d_gradfix.py` and `fused_act.py`. These were just copied over from the original repo so they are still ugly and untidy.\n2. Provide pretrained model conversion method (not that hard tbh, just go map the state_dict keys).\n3. Clean up util functions to aid training loop design.",
    'author': 'Peter Yuen',
    'author_email': 'ppeetteerrsx@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ppeetteerrs/stylegan2-torch',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
