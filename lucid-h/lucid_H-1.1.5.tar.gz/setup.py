from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.1.5'
DESCRIPTION = 'WORK_ENV emails'
LONG_DESCRIPTION = 'A package that allows check disk space and email'

# Setting up
setup(
    name="lucid_H",
    version=VERSION,
    author="HemantDhanwar",
    author_email="<ashuhemantsingh@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['smtpemail', 'fsspec', 'getpass4', 'pandas', 'numpy', 'gitpython', 'shutil' ],
    keywords=['python', 'Email', 'directory size', 'dir size'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
