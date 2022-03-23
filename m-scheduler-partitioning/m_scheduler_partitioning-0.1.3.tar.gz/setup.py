import os

from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


# cython detection
try:
    from Cython.Build import cythonize

    CYTHON = False
except ImportError:
    CYTHON = False

SOURCE_PATH = "./mobio"

ext_modules = []


# if CYTHON:
#     ext_modules = cythonize([SOURCE_PATH + "/**/*.py"], compiler_directives=dict(always_allow_keywords=True))


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))
    return paths


setup(
    name="m_scheduler_partitioning",
    version="0.1.3",
    description="Mobio scheduler partitioning sdk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mobiovn",
    author="MOBIO",
    author_email="contact@mobio.vn",
    license="MIT",
    packages=[
        "mobio/libs/m_scheduler_partitioning",
        "mobio/libs/m_scheduler_partitioning/scheduler_models"
    ],
    install_requires=[
        "nanoid==2.0.0",
        "kazoo==2.8.0"
    ],
    # package_data={'': extra_files},
    include_package_data=True,
    ext_modules=ext_modules,
    classifiers=[
        "Topic :: Software Development",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
