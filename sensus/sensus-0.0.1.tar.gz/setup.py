# https://pythonhosted.org/an_example_pypi_project/setuptools.html
# https://www.youtube.com/watch?v=GIF3LaRqgXo

import os
import sys
import warnings
from setuptools import setup

if sys.version_info[:2] < (3, 8):
    raise RuntimeError("Python version >= 3.8 required.")

# if sys.version_info >= (3, 11):
#     fmt = "NumPy {} may not yet support Python {}.{}."
#     warnings.warn(
#         fmt.format(VERSION, *sys.version_info[:2]),
#         RuntimeWarning)
#     del fmt

# import numpy.distutils.command.sdist
# import setuptools
# if int(setuptools.__version__.split('.')[0]) >= 60:
#     # setuptools >= 60 switches to vendored distutils by default; this
#     # may break the numpy build, so make sure the stdlib version is used
#     try:
#         setuptools_use_distutils = os.environ['SETUPTOOLS_USE_DISTUTILS']
#     except KeyError:
#         os.environ['SETUPTOOLS_USE_DISTUTILS'] = "stdlib"
#     else:
#         if setuptools_use_distutils != "stdlib":
#             raise RuntimeError("setuptools versions >= '60.0.0' require "
#                     "SETUPTOOLS_USE_DISTUTILS=stdlib in the environment")


with open("README.md", "r") as fh:
    long_description=fh.read()

setup(
    name = "sensus",
    version = "0.0.1",
    author = "Farzad",
    author_email = "farzadziaien@gmail.com",
    description = ("this is just a template"),
    license = "BSD",
    # test_suite='pytest',
    keywords = "example documentation tutorial",
    url = "http://packages.python.org/an_example_pypi_project",
    # packages=['template'],
    py_modules=["template"],
    package_dir={'':'template'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Education :: Testing",
        "License :: OSI Approved :: MIT License",
    ],
    platforms=["Windows", "Linux"],
    python_requires='>=3.8',
    zip_safe=False,
    install_requires = [
        "numpy > 1.0.0",
    ],
    extras_require = {
        "dev":[
            "pytest>=3.7"
        ]
    }


)


# send the wheel to database

# pip install --upgrade pip
# python setup.py bdist_wheel
# pip install -e .