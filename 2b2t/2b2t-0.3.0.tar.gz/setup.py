import pathlib
from setuptools import setup, find_packages

setup(
    name="2b2t",
    version="0.3.0",
    description="A 2b2t toolbox.",
    long_description=(pathlib.Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/keuin/2b2t",
    author="Keuin",
    author_email="keuinx@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "mcstatus",
    ],
    entry_points={
        "console_scripts": [
            "2b2t=bbtt.__main__:main",
            "2b2t.coord=bbtt.coord.__main__:main"
        ]
    },
)
