import os
from setuptools import setup, find_packages
from common._version import __version__

dependencies = ["wheel>=0.31.0", "boto3>=1.20.15", "tensorflow", "click>=8.0.1", "questionary>=1.10.0", "torch", "torchvision"]

if os.environ.get('AWS_ACCESS_KEY_ID') == None or os.environ.get('AWS_SECRET_ACCESS_KEY') == None:
   raise RuntimeError('Please run the build from within a running docker server environment')

setup(
   name='autumn8',
   version=__version__,
   author='Autumn8',
   author_email='marcink@radcode.co',

   install_requires=dependencies,
   setup_requires=dependencies,


   packages=[
      *find_packages(),
   ],
   description='Utilities to export models to autodl',

   entry_points={
      'console_scripts': [
         'autodl-cli=cli:main',
      ],
   },
)
