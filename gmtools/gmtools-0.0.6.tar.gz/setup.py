import io
import sys
import os
from shutil import rmtree
from setuptools import find_packages, setup, Command

name = 'gmtools' 
version = '0.0.6'
description = 'gmtool'
url = 'https://github.com/meihaoyidian/tm-pip-tools'
email = 'vida112728@gmail.com'
author = 'GM-TM-QA'
python_version = '>=3.9.0'
install_moudles = ['yagmail','urllib','requests','json']
extras = {}
here = os.path.abspath(os.path.dirname(__file__))

# README.md 描述
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = description


class UploadCommand(Command):
    description = '构建并发布软件包'
    user_options = []

    @staticmethod
    def status(s):
        print('\033[1m{0}\033[0m'.format(s))

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass
        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))
        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')
        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(version))
        os.system('git push --tags')
        sys.exit()

setup(name=name, version=version, description=description,
      long_description=long_description, long_description_content_type='text/markdown',
      author=author, author_email=email, python_requires=python_version, url=url,
      packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
      install_requires=install_moudles, extras_require=extras, include_package_data=True,
      license='MIT', classifiers=[
        'License :: OSI Approved :: MIT License', 'Programming Language :: Python',
        'Programming Language :: Python :: 3'],
      cmdclass={'upload': UploadCommand})