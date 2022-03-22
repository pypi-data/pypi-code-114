from setuptools import setup, find_packages

setup(
    name = 'mylib_donghao',
    version = '0.1.1',
    keywords='mylib_donghao',
    description = 'A pythono package by DONG HAO about machine learing and other math problems.',
    license = 'MIT License',
    url = 'https://github.com/',
    author = 'Hao Dong',
    author_email = '1440027762@qq.com',
    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = ['numpy', 'torch', ],
)