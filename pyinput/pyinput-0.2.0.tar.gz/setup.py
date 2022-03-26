from setuptools import setup

setup(
    name='pyinput',
    version='0.2.0',    
    description='Python library to send inputs to an executable',
    url='https://github.com/GaryFrazier/PyInput',
    author='Gary Frazier',
    author_email='garyfrazier95@yahoo.com',
    license='MIT',
    packages=['pyinput'],
    install_requires=['pywin32'],

    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
    ],
)