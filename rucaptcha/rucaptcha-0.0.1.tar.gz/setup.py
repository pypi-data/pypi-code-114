import os

from setuptools import setup, find_packages

ROOT = os.path.dirname(os.path.realpath(__file__))

with open("README.md", encoding="utf-8") as inp:
    readme_content = inp.read()

setup(
    name="rucaptcha",
    version="0.0.1",
    author="Gregory Petukhov",
    author_email="lorien@lorien.name",
    maintainer="Gregory Petukhov",
    maintainer_email="lorien@lorien.name",
    url="https://github.com/lorien/rucaptcha",
    description="Python library to access rucaptcha/twocaptcha API",
    long_description=readme_content,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["script", "test"]),
    download_url="https://github.com/lorien/rucaptcha/releases",
    license="MIT",
    install_requires=["urllib3"],
    keywords="captcha",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
