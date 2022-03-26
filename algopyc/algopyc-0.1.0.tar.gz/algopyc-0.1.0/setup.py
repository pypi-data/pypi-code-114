from setuptools import setup, find_packages, Extension

setup(
    name='algopyc',
    version='0.1.0',
    packages=find_packages(),
    author="Seonwhee Jin",
    maintainer="Seonwhee Jin",
    license='GPLv2+',
    keywords=['edit distance', 'Levenshtein', 'Wagner-Fischer'],
    url="https://github.com/Seonwhee-Genome/PyCextension",
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: C++',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    ext_modules=[
        Extension('pyalgorithm', sources=['algorithm.cpp', 'levenshtein.cpp'],
        ),
    ],
)
