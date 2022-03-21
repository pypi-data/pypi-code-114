from setuptools import setup, find_packages
import codecs
import os

DESCRIPTION = 'Get capital city and state language of Indian States'

# Setting up
setup(
    name="stateInfo",
    version='0.0.3',
    author="RohitS",
    author_email="rohitsanadi08@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'state', 'capital', 'language'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
