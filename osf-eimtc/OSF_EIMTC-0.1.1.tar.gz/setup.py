from setuptools import setup, find_packages


setup(
    name='OSF_EIMTC',
    version='0.1.1',
    license='MIT',
    author="Ariel University",
    author_email='ofek.bader@msmail.ariel.ac.il',
    packages=find_packages('EIMTC'),
    package_dir={'': 'EIMTC'},
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