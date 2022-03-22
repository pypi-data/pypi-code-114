from setuptools import setup

setup(name='d3m-simon',
    version='1.2.6',
    description='Character-level CNN+LSTM model for text classification',
    packages=['Simon', 'Simon.penny'],
    license='MIT',
    url='https://gitlab.com/datadrivendiscovery/contrib/simon',
    install_requires=['Faker >= 0.7.7',
        'scikit-learn==0.22.2.post1',
        'python-dateutil>=2.8.1',
        'pandas==1.1.3',
        'scipy==1.4.1',
        'h5py >= 2.7.0'],
    extras_require={
        "cpu": ["tensorflow==2.2.0"],
        "gpu": ["tensorflow-gpu==2.2.0"],
    },
    include_package_data=True,
)
