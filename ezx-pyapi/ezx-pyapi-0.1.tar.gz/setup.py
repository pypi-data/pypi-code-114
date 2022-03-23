from setuptools import setup, find_packages

setup(
    name='ezx-pyapi',
    version='0.1',
    license='MIT',
    author="EZX Inc.",
    author_email='support@ezxinc.com',
    packages=find_packages('.'),
    package_dir={'': '.'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='EZX iServer API trading',
    install_requires=[],
)
