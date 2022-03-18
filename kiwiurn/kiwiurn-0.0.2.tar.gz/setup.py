from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'Python Urn class and random number generator'
LONG_DESCRIPTION=DESCRIPTION

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="kiwiurn", 
        version=VERSION,
        author="Damien Martin",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'random generator'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
