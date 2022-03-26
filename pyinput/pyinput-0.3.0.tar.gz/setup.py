from setuptools import setup
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pyinput',
    version='0.3.0',    
    description='Python library to send inputs to an executable.',
    url='https://github.com/GaryFrazier/PyInput',
    author='Gary Frazier',
    author_email='garyfrazier95@yahoo.com',
    license='MIT',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=['pywin32'],

    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
    ],
)