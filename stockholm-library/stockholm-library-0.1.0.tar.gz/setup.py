from setuptools import find_packages, setup

packages = find_packages(exclude=["tests"])

setup(
    packages=packages,
    install_requires=[
        "requests[security]>=2,<3",
        "beautifulsoup4>=4,<5"
    ],
)
