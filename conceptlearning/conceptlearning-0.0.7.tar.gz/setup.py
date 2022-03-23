from setuptools import setup

with open('README.md','r') as fh:
    long_desc = fh.read()
setup(
    name='conceptlearning',
    version='0.0.7',
    description='Concept Learning Algorithms',
    packages=['conceptlearning'],
    classifiers=["Intended Audience :: Education", 
    "Operating System :: OS Independent", 
    "Programming Language :: Python :: 3.0",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8"],
    long_description=long_desc,
    long_description_content_type="text/markdown",
)