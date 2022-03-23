from setuptools import setup, find_packages


VERSION = '0.0.5' 
DESCRIPTION = 'Sid First Package'

# Read Requirements
with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

# Setting up
setup(
        name="sid_first_pack", 
        version=VERSION,
        author="Sid-ISQ",
        author_email="gmcovas@isq.pt", # to change
        description=DESCRIPTION,
        packages=find_packages(),
        test_suite='tests',
        install_requires = requirements,
        include_package_data=True
        )

