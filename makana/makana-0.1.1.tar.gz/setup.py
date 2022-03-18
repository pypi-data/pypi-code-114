from distutils.core import setup
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
setup(
  name = 'makana',         # How you named your package folder (MyLib)
  packages = ['makana'],   # Chose the same as "name"
  version = '0.1.1',      # Start with a small number and increase it with every change you make
  #license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'First Python Library',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'AlpsLogicITSolution',                   # Type in your name
  author_email = 'yash.patel@alpsinfo.net',      # Type in your E-Mail
  # url = 'https://github.com/vivek-lakhataria/Python-Sample-Library',   # Provide either the link to your github or to your website
  #download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Makana Python Library'],   # Keywords that define your package best
  python_requires=">=3.7",
  include_package_data=True,
  install_requires=[
    'requests'
    ],            # I get to this in a second
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
  ],
)