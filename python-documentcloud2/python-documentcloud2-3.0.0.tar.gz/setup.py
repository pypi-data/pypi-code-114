# Third Party
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='python-documentcloud2',
    version='3.0.0',
    description='A simple Python wrapper for the DocumentCloud API',
    author='Mitchell Kotler',
    author_email='mitch@muckrock.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/muckrock/python-documentcloud',
    license="MIT",
    packages=("documentcloud",),
    include_package_data=True,
    install_requires=(
        'python-documentcloud',
    ),
)
