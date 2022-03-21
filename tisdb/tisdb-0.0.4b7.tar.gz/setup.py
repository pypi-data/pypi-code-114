from pkg_resources import get_distribution, DistributionNotFound
import re
import io

from setuptools import setup, find_packages

from os import path

this_directory = path.abspath(path.dirname(__file__))


def _read_home_file(filename):
    try:
        with io.open(path.join(this_directory, filename), "rt", encoding="utf-8") as fd:
            ret = fd.read()
    except Exception:
        ret = ""
    return ret


readme = _read_home_file("README.md")


try:
    __version__ = get_distribution("tisdb").py_version
except DistributionNotFound:
    with io.open("src/tisdb/__init__.py", "rt", encoding="utf-8") as f:
        __version__ = re.search(r"__version__ = \"(.*?)\"", f.read()).group(1)

reqs = _read_home_file("requirements.txt").splitlines()

setup(
    name="tisdb",
    version=__version__,
    license="BSD",
    maintainer="tisdb team",
    maintainer_email="dennias.chiu@gmail.com",
    author="deefox",
    author_email="602716933@qq.com",
    description=(
        "A relational DB based tsdb library for python tsdb project"
        " development that inherited and learned from TIDB and OpenTSDB."
    ),
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=reqs,
    use_scm_version={
        "tag_regex": r"^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$",
        # '{next_version}.dev{distance}+{scm letter}{revision hash}.dYYYMMMDD',
        "fallback_version": __version__,
        "relative_to": __file__,
    },
    setup_requires=["setuptools_scm"],
)
