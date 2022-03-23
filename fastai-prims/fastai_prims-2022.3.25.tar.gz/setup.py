import os
from setuptools import setup

PACKAGE_NAME = 'fastai_prims'

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

git_files = package_files('fastai_prims/.git')

def read_package_variable(key):
    """Read the value of a variable from the package without importing."""
    module_path = os.path.join(PACKAGE_NAME, '__init__.py')
    with open(module_path) as module:
        for line in module:
            parts = line.strip().split(' ')
            if parts and parts[0] == key:
                return parts[-1].strip("'")
    assert False, "'{0}' not found in '{1}'".format(key, module_path)


setup(
    name=PACKAGE_NAME,
    version=read_package_variable('__version__'),
    license="Apache-2.0",
    description='Fastai Image Processing primitives',
    author=read_package_variable('__author__'),
    packages=['fastai_prims'],
    package_dir={'fastai_prims': 'fastai_prims'},
    install_requires=[
        'd3m',
        'torch==1.7.0',
        'torchvision==0.8.1',
        'fastai==2.3.0',
        'efficientnet_pytorch==0.7.1'
    ],
    url='https://gitlab.com/datadrivendiscovery/fastai_prims',
    entry_points={
        'd3m.primitives': [
            'classification.Convolutional_neural_network.Fastai = fastai_prims.fastai_tl:FastAIWrapperPrimitive'
        ],
    },
)