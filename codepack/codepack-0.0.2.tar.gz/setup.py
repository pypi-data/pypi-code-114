import setuptools


with open("README.rst", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="codepack",
    version="0.0.2",
    author="ihnokim",
    author_email="ihnokim58@gmail.com",
    description="Codepack is the package for making workflows with Python",
    long_description=long_description,
    url="https://github.com/ihnokim/codepack",
    packages=setuptools.find_packages(),
    keywords=["codepack", "workflow", "pipeline"],
    install_requires=[
        "dill>=0.3.4",
        "pymongo>=3.12.1",
        "numpy",
        "pandas",
        "sshtunnel>=0.4.0",
        "PyMySQL>=1.0.2",
        "pymssql>=2.2.2",
        "boto3>=1.19.6",
        "cx-Oracle>=8.2.1",
        "parse>=1.19.0",
        "APScheduler>=3.8.1",
        "kafka-python>=2.0.2",
        "docker>=5.0.3",
        "requests>=2.26.0"
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)
