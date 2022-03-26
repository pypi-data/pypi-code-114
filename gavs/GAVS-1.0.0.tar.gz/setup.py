from setuptools import setup

INSTALL_REQUIRES = ["matplotlib", "numpy", "scipy", "argparse"]

TEST_REQUIRES = [
    # testing and coverage
    "pytest",
    "coverage",
    "pytest-cov",
    # to be able to run `python setup.py checkdocs`
    "collective.checkdocs",
    "pygments",
]


__version__ = "1.0.0"
long_description = "GAVS: a tool to analyse and visualize the GMX results files."


setup(
    name="GAVS",
    version=__version__,
    author="YinleiHan",
    author_email="",
    description="A tool for GROMACS results analysis and visualization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    download_url="",
    platforms="cross-platform",
    packages=["GAVS"],
    install_requires=INSTALL_REQUIRES,
    extras_require={
        "test": TEST_REQUIRES + INSTALL_REQUIRES,
    },
    package_data={"GAVS":["data/*.data"]},
    exclude_package_data={"GAVS":["test/*"]},
    entry_points={"console_scripts": ["gavs = GAVS.GAVS:main"]},
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Intended Audience :: Science/Research",
    ],
)
