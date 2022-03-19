import pathlib
from setuptools import setup
import setuptools

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="gameday-guru-sdk",
    version="0.0.13",
    description="The Gameday Guru SDK",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/reader",
    author="Real Python",
    author_email="info@realpython.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["gsdk", *setuptools.find_packages()],
    include_package_data=True,
    install_requires=[
        "atlastk==0.13",
        "bleach==4.1.0",
        "certifi==2021.10.8",
        "charset-normalizer==2.0.12",
        "colorama==0.4.4",
        "Deprecated==1.2.13",
        "docutils==0.18.1",
        "idna==3.3",
        "importlib-metadata==4.11.2",
        "keyring==23.5.0",
        "numpy==1.22.2",
        "packaging==21.3",
        "Pillow==9.0.1",
        "pkginfo==1.8.2",
        "pony==0.7.16",
        "Pygments==2.11.2",
        "PyJWT==2.3.0",
        "pyparsing==3.0.7",
        "python-dateutil==2.8.2",
        "python-dotenv==0.19.2",
        "readme-renderer==32.0",
        "redis==4.1.4",
        "requests==2.27.1",
        "requests-toolbelt==0.9.1",
        "rfc3986==2.0.0",
        "six==1.16.0",
        "SQLAlchemy==1.4.32",
        "torch==1.10.2",
        "torchaudio==0.10.2",
        "torchvision==0.11.3",
        "tortoise==0.1.1",
        "tqdm==4.63.0",
        "twine==3.8.0",
        "types-cryptography==3.3.15",
        "types-enum34==1.1.8",
        "types-ipaddress==1.0.8",
        "types-PyJWT==1.7.1",
        "types-redis==4.1.17",
        "typing_extensions==4.1.1",
        "urllib3==1.26.8",
        "webencodings==0.5.1",
        "wrapt==1.14.0",
        "zipp==3.7.0"
    ],
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    },
)