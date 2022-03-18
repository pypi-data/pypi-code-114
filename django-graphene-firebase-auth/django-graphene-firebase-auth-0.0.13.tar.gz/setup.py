from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.13'
DESCRIPTION = 'Firebase authentication with django graphene'
LONG_DESCRIPTION = 'A firebase authentication with django graphene.'

# Setting up
setup(
    name="django-graphene-firebase-auth",
    version=VERSION,
    author="Eba Alemayehu",
    author_email="<ebaalemayhu3@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pycryptodome', 'requests'],
    keywords=['python', 'telebirr', 'payment', 'ethiopia', 'ethio telecom'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
