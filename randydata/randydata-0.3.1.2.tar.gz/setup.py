from setuptools import setup


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name="randydata",
    version="0.3.1.2",
    description="Tools for SQL or Excel of observational data handling.",
    long_description=readme(),
    keywords="excel sql data handling",
    url="https://github.com/JohannesRanderath/randydata",
    author="Johannes Randerath",
    author_email="randydata@randerath.eu",
    license="MIT",
    packages=["randydata"],
    install_requires=["pandas>=1.4.1", "mysql-connector-python>=8.0.0", "sqlalchemy>=1.4.32", "IPython>=8.1.1",
                      "greenlet>=1.1.2", "numpy>=1.22.3", "python-dateutil>=2.8.2", "pytz>=2021.3", "six>=1.16.0",
                      "appnope>=0.1.2", "backcall>=0.2.0", "decorator>=5.1.1", "jedi>=0.18.1", "parso>=0.8.3",
                      "matplotlib-inline>=0.1.3", "traitlets>=5.1.1", "pexpect>=4.8.0", "ptyprocess>=0.7.0",
                      "pickleshare>=0.7.5", "prompt-toolkit>=3.0.28", "wcwidth>=0.2.5", "pygments>=2.11.2",
                      "setuptools>=58.1.0", "stack-data>=0.2.0", "asttokens>=2.0.5", "executing>=0.8.3",
                      "pure-eval>=0.2.2", "protobuf>=3.19.4"],
    include_package_data=True
)
