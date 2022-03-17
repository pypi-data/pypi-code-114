from setuptools import setup, find_namespace_packages

setup(
    name='pointevector-irs990',
    version='0.0.8',
    author='Andrew Hoekstra',
    author_email='andrew@pointevector.com',
    url='https://github.com/Pointe-Vector/xml_parser',
    packages=find_namespace_packages(include=['pointevector.*']),
    install_requires=[
        'pointevector-xmlparser',
        'ruamel.yaml',
        'typing_extensions',
    ],
)
