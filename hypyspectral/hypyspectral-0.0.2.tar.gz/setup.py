from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'HyPySpectral - Hyperspectral Image Analysis Toolbox for Python'
LONG_DESCRIPTION = 'HyPySpectral - Hyperspectral Image Analysis Toolbox for Python'

# Setting up
setup(
       # the name must match the folder name 'HyPySpectral'
        name="hypyspectral", 
        version=VERSION,
        author="Fraser Macfarlane",
        author_email="frasermac108@live.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'hyperspectral'],
        classifiers= [
            "Development Status :: 1 - Planning",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Natural Language :: English",
            "License :: OSI Approved :: MIT License",
            "Topic :: Scientific/Engineering :: Image Processing",
        ]
)