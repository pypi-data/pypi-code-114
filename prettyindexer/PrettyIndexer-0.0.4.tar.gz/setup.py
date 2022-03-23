from setuptools import setup

with open("README.md","r") as fh:
	long_description = fh.read()

setup (

	name="PrettyIndexer",
	version='0.0.4',
	description="Get positive and negative index values of a string displayed in a beautiful manner.",
	py_modules=["stringindexer"],
	package_dir={'':'src'},
	author='Ashwin.B',
    license='MIT',
    author_email = 'ahnashwin1305@gmail.com',
    url = 'https://github.com/ahn1305/PrettyIndexer',
	long_description=long_description,
	long_description_content_type = "text/markdown",
	classifiers=[
    'Programming Language :: Python :: 3.6',      
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',  
    'Operating System :: OS Independent',
  ],

)

install_requires = [
	'prettytable==2.1.0',
	'printtools==1.2',
]
