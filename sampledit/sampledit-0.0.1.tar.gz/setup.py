
from setuptools import setup, find_packages
setup(
  name='sampledit',
  version='0.0.1',
  description='dit document layout',
  long_description=open('README.txt').read() ,
  author='sneha dhole',
  packages=['sampledit'],
  install_requires=['torch','pyyaml','torchvision','opencv-python']
)