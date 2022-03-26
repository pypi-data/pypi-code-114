#encoding:utf-8
from setuptools import setup, find_packages
import sys, os

version = '0.1.2'

setup(name='wtot',
      version=version,
      description="terminal查词工具",
      long_description="""terminal查词工具""",
      keywords='python wt dictionary terminal',
      author='lmh',
      author_email='554408064@sjtu.edu.cn',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'termcolor',
      ],
      entry_points={
        'console_scripts':[
            'wtot = wtot.wtot:main'
        ]
      },
)
