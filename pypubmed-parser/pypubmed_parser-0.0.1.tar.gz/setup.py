import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='pypubmed_parser',  
     version='0.0.1',
     author="Scott Hirsch",
     author_email="sdh.equities@gmail.com",
     description="Package to search, retrieve, and parse article information",
     long_description=long_description,
   long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
