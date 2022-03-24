from gettext import install
from setuptools import setup

setup(name='diana-2',
      version='0.1',
      description='This is the Python implementation of DIANA Clustering Algorithm',
      author='HPC-ML',
      author_email='flcus@example.com',
      license='MIT',
      packages=['diana'],
      install_requires=['numpy','pandas','scipy'],
      zip_safe=False)