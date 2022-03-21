# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="dsbox_corex",
    version="1.2.0",
    description="Return components/latent factors that explain the most multivariate mutual information in the data under Linear Gaussian model. For comparison, PCA returns components explaining the most variance in the data.",
    license="Apache-2.0",
    author="Rob Brekelmans/Greg Ver Steeg",
    author_email="brekelma@usc.edu",
    keywords='d3m_primitive',
    #packages = ['corexcontinuous', 'corextext', ]
    packages=find_packages(),
    url='https://gitlab.com/datadrivendiscovery/contrib/dsbox-corex',
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'six',
        'd3m-common-primitives',
        'd3m',
        'tensorflow',
        'keras',
        'scikit-learn',
        'GitPython',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data = True,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    entry_points = {
    'd3m.primitives': [
        'feature_construction.corex_continuous.DSBOX = dsbox_corex.corex_continuous:CorexContinuous',
        'feature_construction.corex_text.DSBOX = dsbox_corex.corex_text:CorexText',
        'regression.echo_linear.DSBOX = dsbox_corex.echo_regressor:EchoLinearRegression',
        'feature_construction.echo_ib.DSBOX = dsbox_corex.echo_ib:EchoIB',
        #'feature_construction.corex_supervised.EchoIBReg = echo_sae:EchoRegression',
        #'feature_construction.corex_supervised.EchoIBClf = echo_sae:EchoClassification'
    ]
    }
)
