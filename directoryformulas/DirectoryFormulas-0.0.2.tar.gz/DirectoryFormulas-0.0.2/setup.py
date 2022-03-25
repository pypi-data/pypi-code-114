from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: MacOS :: MacOS X',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.9'
]

setup(
    name='DirectoryFormulas',
    version='0.0.2',
    description='Module for Directory Value and other formulas',
    long_description='Get Current Directory and DivbyZero int and floats',
    url='',
    author='FrankieOliverTrading',
    author_email='ceruttifra@gmail.com',
    license='MIT',
    py_modules=['DirectoryFormulas'],
    classifiers=classifiers,
    keywords='calculator',
    packages=find_packages(),
    install_requires=['']
)