from setuptools import setup, find_packages
import os


def _process_requirements():
    packages = open('requirements.txt').read().strip().split('\n')
    requires = []
    for pkg in packages:
        if pkg.startswith('git+ssh'):
            return_code = os.system('pip install {}'.format(pkg))
            assert return_code == 0, 'error, status_code is: {}, exit!'.format(return_code)
        else:
            requires.append(pkg)
    return requires


setup(
    name='ofanalysis',
    version='0.1.1',
    packages=find_packages(),
    url='https://github.com/laye0619/ofanalysis',
    license='',
    author='LayeWang',
    author_email='laye0619@gmail.com',
    description='A framework analysing open fund in China',
    install_requires = _process_requirements()
)
