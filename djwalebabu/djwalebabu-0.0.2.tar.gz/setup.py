import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'djwalebabu', # How I named my package folder
    packages = setuptools.find_packages(), #This gives ['luckycli']    
    version = '0.0.2',

    author = 'Hargun Oberoi',
    author_email = 'hargun3045@gmail.com',
    description = 'A demonstration library to show how package distribution works in python',
    long_description = long_description,    
    long_description_content_type = "text/markdown",
    keywords = ['pyds','ai0','hargun','oberoi','djwalebabu'], # Guess it's just a way to find out if someone can find my package    
    install_requires = [], # Dependencies, at the moment none   
    
    classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6',

    )
