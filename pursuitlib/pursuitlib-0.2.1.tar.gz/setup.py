from setuptools import setup
from pathlib import Path

directory = Path(__file__).parent

setup(
    name='pursuitlib',
    version='0.2.1',
    packages=['pursuitlib'],
    entry_points={},
    author='Pursuit',
    author_email='fr.pursuit@gmail.com',
    description='Provides utility functions',
    long_description=(directory / "README.md").read_text(encoding="utf-8"),
    long_description_content_type='text/markdown',
    url='https://gitlab.com/frPursuit/pursuitlib-python',
    license='All rights reserved',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7"
)
