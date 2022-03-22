from setuptools import setup,find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='python installer',
    version='0.0.2',
    license='MIT',
    author='Anmol Malik',
    author_email='malik16603@gmail.com',
    description='A package installer for python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anmolmalik01/python-installer",
    project_urls={
        "Bug Tracker": "https://github.com/anmolmalik01/python-installer/issues",
    },
    packages=find_packages(),
    install_requires=[
        'click',
        'pipreqs'
    ],
    keywords=['python', 'package installer', 'json'],
    classifiers= [
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: MacOS',
            'Operating System :: Unix',
            'Programming Language :: Python'
    ],
    entry_points={
        'console_scripts': [
    	    'package = python_installer.main:cli',
        ]
    },
)
