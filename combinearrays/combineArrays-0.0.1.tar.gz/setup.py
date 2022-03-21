from setuptools import setup

classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup( 
    name="combineArrays",
    version="0.0.1",
    description="Python CFFI bindings to combine an Array of Int32 with an Array of Double",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    #url='',
    author='Norbert Henseler',
    author_email='nhenseler@web.de',
    license_file='LICENSE',
    py_modules=['combineArrays'],
    install_requires=['cffi>=1.0.0'],
    setup_requires=['cffi>=1.0.0'],
    cffi_modules=['./src/buildCombineArrays.py:ffibuilder'],
    package_dir={'': 'src'},
    
)

    
    