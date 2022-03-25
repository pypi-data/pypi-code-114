import setuptools
import os


def get_version(version_tuple):
    # additional handling of a,b,rc tags, this can
    # be simpler depending on your versioning scheme
    if not isinstance(version_tuple[-1], int):
        return '.'.join(
            map(str, version_tuple[:-1])
        ) + version_tuple[-1]
    return '.'.join(map(str, version_tuple))


# path to the packages __init__ module in project
# source tree
init = os.path.join(os.path.dirname(__file__),
                    'magnumapi',
                    '__init__.py')

version_line = list(
    filter(lambda l: l.startswith('VERSION'), open(init))
)[0]

# VERSION is a tuple so we need to eval 'version_line'.
# We could simply import it from the package but we
# cannot be sure that this package is importable before
# installation is done.
PKG_VERSION = get_version(eval(version_line.split('=')[-1]))

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS: dict = {
    'core': [
        'numpy',
        'pandas',
        'ansys-mapdl-reader',
        'ansys-mapdl-core',
        'matplotlib',
        'IPython',
        'ipywidgets',
        'plotly',
        'coverage',
        'dataclasses',
        'ipyaggrid'],
    'test': [
        'pytest',
        'tox',
        'sphinx',
        'sphinx-rtd-theme'
    ],
    'dev': [
        # 'requirement-for-development-purposes-only',
    ],
    'doc': [
        'sphinx',
        'sphinx-glpi-theme',
        'sphinx-autoapi',
        'sphinxcontrib.napoleon',
        'sphinx-autodoc-typehints',
    ],
}

setuptools.setup(
    name="magnum-api",
    version=PKG_VERSION,
    author="ETHZ D-ITET IEF",
    author_email="mmaciejewski@ethz.ch",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.ethz.ch/magnum/magnum-api",
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS['core'],
    extras_require={
        **REQUIREMENTS,
        # The 'dev' extra is the union of 'test' and 'doc', with an option
        # to have explicit development dependencies listed.
        'dev': [req
                for extra in ['dev', 'test', 'doc']
                for req in REQUIREMENTS.get(extra, [])],
        # The 'all' extra is the union of all requirements.
        'all': [req for reqs in REQUIREMENTS.values() for req in reqs],
    },

)
