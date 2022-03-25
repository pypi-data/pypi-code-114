from setuptools import setup, find_packages
'''
python setup.py sdist
twine upload dist/*
'''

setup(
    name='OSF_EIMTC',
    version='0.1.3',
    license='MIT',
    author="Ariel University",
    author_email='ofek.bader@msmail.ariel.ac.il',
    packages=['OSF.plugins', 'OSF.models'], #find_packages('EIMTC'),
    package_dir={'OSF': 'EIMTC'},
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