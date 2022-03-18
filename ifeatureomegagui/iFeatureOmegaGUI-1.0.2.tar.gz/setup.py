#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhen Chen(chenzhen-win2009@163.com; zhenchen625@hotmail.com)
# Description: iFeatureOmega is an integrative platform for the prediction/feature engineering, visualization and analysis of features from molecular sequence, structural and ligand data sets.

from setuptools import setup, find_packages

setup(
    name = 'iFeatureOmegaGUI',
    version = '1.0.2',
    keywords='iFeatureOmegaGUI',
    description = 'An integrative platform for the prediction/feature engineering, visualization and analysis of features from molecular sequence, structural and ligand data sets',
    license = 'MIT License',
    url = 'https://github.com/Superzchen/iFeatureOmega-GUI',
    author = 'SuperZhen',
    author_email = 'chenzhen-win2009@163.com',    
    packages=find_packages("src"),
    package_dir = {'':'src'},
    
    package_data = {
        # 任何包中含有.txt文件，都包含它
        '': ['*.txt'],
        # 包含demo包data文件夹中的 *.dat文件
        'iFeatureOmegaGUI': ['data/*.txt', 'data/*.pdb', 'data/*.csv', 'images/logo.ico', 'images/progress_bar.gif', 'obsolete', 'util/data/*.txt', 'util/data/*.data'],

    },
    platforms = 'any',
    install_requires = [
        'qdarkstyle',
        'sip',
        'datetime',
        'networkx',        
        'numpy>=1.21.4',
        'pandas>=1.3.4',        
        'scikit-learn>=1.0.1',
        'scipy>=1.7.3',
        'matplotlib==3.4.3',
        'seaborn',
        'joblib'
        ],     
)