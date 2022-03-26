import re

from setuptools import setup


version = ''
with open('scathach/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)


requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()



if not version:
    raise RuntimeError('version is not set')

readme = ''
with open('README.md') as f:
    readme = f.read()


setup(
    name='booru',
    author='sinkaroid',
    author_email='anakmancasan@gmail.com',
    version='1.0.0',
    long_description=readme,
    url='https://github.com/sinkaroid/booru',
    packages=['scathach'],
    license='MIT',
    description='Python bindings for Booru imageboards',
    include_package_data=True,
    keywords = ['booru'],
    install_requires=requirements
)
