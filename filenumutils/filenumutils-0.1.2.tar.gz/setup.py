import pathlib
from setuptools import setup
from filenumutils import __version__

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="filenumutils",
    version=__version__,
    description="Python tools to find last file/folder number in a int indexed file/folder with specified extension, prefix and/or suffix. "
                "Also allows to create next folder, e.g if dir contains train_00 and train_01, it creates train_02",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/saravanabalagi/filenumutils",
    author="Saravanabalagi Ramachandran",
    author_email="saravanabalagi@hotmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["filenumutils"],
    include_package_data=True,
    install_requires=[],
    tests_requires=["pytest"],
)
