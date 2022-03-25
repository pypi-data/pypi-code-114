from setuptools import setup

from simplelogger import info

with open("README.md", "r") as f:
    README = f.read()  # Read the contents of `README.md` file.

print(info.title)
print()

setup(
    name="simplelogger-python",
    version='.'.join(map(str, info.version)),  # Get the program version from the package.
    description="A simple logger I made for some projects a year ago.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Chris1320/SimpleLogger-python",
    author="Chris1320",
    author_email="chris1320is@protonmail.com",
    license="MIT",
    classifiers=[  # https://pypi.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Topic :: System :: Logging"
    ],
    packages=["simplelogger"],
    include_package_data=True,
    install_requires=[],  # Required packages
    extras_require={  # Optional packages for optional features
        "Colors": ["colorama"]
    }
)
