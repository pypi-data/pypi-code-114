from setuptools import setup, find_packages
setup(
 name = 'harvestnet',
 version = '0.0.7',
 description = 'HarvestNet',
 long_description = 'HarvestNet',
 license = 'MIT License',
 author = 'waterlily',
 author_email = 'b1929595403@gmail.com',
 platforms = 'any',
 python_requires = '>=3.7.*',
 data_files = [(r'd:\\',['ResNet50_SGD.pth', ])],
 install_requires = [],
 packages = find_packages()
 )
