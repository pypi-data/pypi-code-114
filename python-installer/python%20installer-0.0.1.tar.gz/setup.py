from setuptools import setup,find_packages


setup(
    name='python installer',
    version='0.0.1',
    license='MIT',
    author='Anmol Malik',
    author_email='malik16603@gmail.com',
    description='A package installer for python',
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
