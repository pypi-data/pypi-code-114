# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

from aakrab import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
    'allianceauth>=2.11.0',
    # 'django-bootstrap-form',
    # 'django-esi>=4.0.0'
]

testing_extras = [

]

setup(
    name='aa-krab',
    version=__version__,
    author='Belial Morningstar',
    author_email='jtrenaud1s@gmail.com',
    description='A Wormhole Krab Fleet tracking system for Alliance Auth',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
        ':python_version=="3.8"': ['typing'],
    },
    python_requires='~=3.8',
    license='GPLv3',
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    url='https://gitlab.com/hole-punchers/aa-krab',
    zip_safe=False,
    include_package_data=True,
)
