#!/usr/bin/env python
import sys

from setuptools import Extension
from setuptools import setup
from torch.utils.cpp_extension import CppExtension

assert (3, 7) <= sys.version_info < (3, 9), "requires python 3.7 or 3.8"

long_description = """
TorchDynamo is a Python-level JIT compiler designed to make unmodified
PyTorch programs faster. TorchDynamo hooks into the frame evaluation API
in CPython ([PEP 523]) to dynamically modify Python bytecode right before
it is executed. It rewrites Python bytecode in order to extract sequences
of PyTorch operations into an [FX Graph] which is then just-in-time
compiled with an ensemble of different backends and autotuning. It
creates this FX Graph through bytecode analysis and is designed to mix
Python execution with compiled backends to get the best of both worlds:
usability and performance.

See the project [github page] for more details.

[PEP 523]: https://www.python.org/dev/peps/pep-0523/
[FX Graph]: https://pytorch.org/docs/stable/fx.html
[github page]: https://github.com/facebookresearch/torchdynamo
"""

setup(
    name="torchdynamo",
    version="0.1.1",
    url="https://github.com/facebookresearch/torchdynamo",
    description="A Python-level JIT compiler designed to make unmodified PyTorch programs faster.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jason Ansel",
    author_email="jansel@fb.com",
    license="BSD-3",
    keywords="pytorch machine learning compilers",
    python_requires=">=3.8, <3.9",
    install_requires=["torch>=1.11.0", "tabulate"],
    packages=["torchdynamo"],
    ext_modules=[
        Extension(
            "torchdynamo._eval_frame",
            ["torchdynamo/_eval_frame.c"],
            extra_compile_args=["-Werror"],
        ),
        CppExtension(
            name="torchdynamo._guards",
            sources=["torchdynamo/_guards.cpp"],
        ),
    ],
)
