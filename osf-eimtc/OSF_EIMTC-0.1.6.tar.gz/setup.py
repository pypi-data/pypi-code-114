from setuptools import setup, find_packages
'''
python setup.py sdist
twine upload dist/*
'''

setup(
    name='OSF_EIMTC',
    version='0.1.6',
    long_description = 'file: README.rst',
    license='MIT',
    author="Ariel University",
    author_email='ofek.bader@msmail.ariel.ac.il',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/neyney10/PCAPFeatureExtractor',
    keywords='nfstream, pcap, network, deep-learning, extraction',
    install_requires=[
        'scikit-learn',
        'NFStream',
        'pandas',
        'numpy',
        'scapy',
        'pyasn',
        'click',
    ],
)