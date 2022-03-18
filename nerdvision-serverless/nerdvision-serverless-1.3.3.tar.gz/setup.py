#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'nerdvision-serverless',
        version = '1.3.3',
        description = 'The NerdVision Python agent for live debugging, dynamic logging and data monitoring.',
        long_description = 'To use this please view the docs at https://docs.nerd.vision/python/configuration/',
        author = '',
        author_email = '',
        license = 'https://www.nerd.vision/legal/agent-license',
        url = 'https://nerd.vision',
        scripts = [],
        packages = [
            'nerdvision',
            'nerdvision.settings',
            'nerdvision.plugins',
            'nerdvision.models'
        ],
        namespace_packages = [],
        py_modules = [],
        classifiers = [
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Natural Language :: English',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: Implementation :: CPython',
            'Programming Language :: Python :: Implementation :: PyPy',
            'Topic :: Software Development :: Debuggers'
        ],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = [
            'certifi==2019.9.11',
            'chardet==3.0.4',
            'idna==2.8',
            'requests==2.22.0',
            'six==1.12.0',
            'urllib3==1.25.6'
        ],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        keywords = '',
        python_requires = '',
        obsoletes = [],
    )
