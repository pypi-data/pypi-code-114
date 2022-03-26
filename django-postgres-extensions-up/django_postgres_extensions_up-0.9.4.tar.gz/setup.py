from setuptools import setup, find_packages

import django_postgres_extensions

setup(name='django_postgres_extensions_up',
    version=django_postgres_extensions.__version__,
    description="Extra features for django.contrib.postgres",
    long_description=open('description.rst').read(),
    author='Eduard Vasanski',
    author_email='eduard.vasanski@gmail.com',
    url='https://github.com/vasanski/django_postgres_extensions',
    packages=find_packages(exclude=['tests', 'tests.*']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)