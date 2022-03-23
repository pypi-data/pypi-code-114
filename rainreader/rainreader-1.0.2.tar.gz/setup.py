# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:52:11 2022

@author: ELNN
"""

from setuptools import setup

setup(
    name='rainreader',
    version='1.0.2',    
    description='Python Package for reading KMD files from The Danish Meterological Institute (DMI) as well as simple simple analysis for the data',
    url='https://github.com/enielsen93/rainreader',
    author='Emil Nielsen',
    author_email='enielsen93@hotmail.com',
    license='BSD 2-clause',
    packages=['rainreader'],
    install_requires=['numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)