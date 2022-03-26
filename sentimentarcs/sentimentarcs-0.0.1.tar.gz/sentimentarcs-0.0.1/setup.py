from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'SentimentArcs'
LONG_DESCRIPTION = 'SentimenArcs for NLP Time Series Sentiment Analysis'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="sentimentarcs", 
    version=VERSION,
    author="Jon Chun",
    author_email="<jonchun@outlook.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[], # add any additional packages that 
    # needs to be installed along with your package. Eg: 'caer'
    
    keywords=['python', 'first package'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        # "Intended Audience :: Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)