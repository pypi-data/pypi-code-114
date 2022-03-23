from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="hybridvut",
    version="0.1.1",
    description=(
        "hybridvut is a tool to carry out hybrid LCA/IO"
        "based on the make and use framework"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/exiobase/hybridvut",
    author="Maik Budzinski",
    author_email="maik.budzinski@ntnu.no",
    license="GNU GPLv3",
    python_requires=">=3.9.0",
    install_requires=[
        "numpy >= 1.20.2",
        "pandas >= 1.2.4",
        "iam-units >= 2021.3.22",
        "openpyxl >= 3.0.7",
        "pyam-iamc >= 0.11.0",
    ],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Utilities",
    ],
)
