import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


# This call to setup() does all the work
setup(
    name="hifrank",
    version="1.0.0",
    description="Greets someone with the name Frank according to the time of day",
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/frankhuurman/hifrank',
    author="Frank",
    author_email="pypi-frank@protonmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["hifrank"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "hifrank=hifrank.__main__:main",
        ]
    },
)
