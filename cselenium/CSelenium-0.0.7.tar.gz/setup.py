# coding=utf-8


from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='CSelenium',
    version="0.0.7",
    description=(
        '''
            Simplify native Selenium operations to locate elements in a shorter manner
        Make the code look cleaner.
        characteristics:
            Clean code,
            Code has and associated operations
        '''
    ),
    long_description=open('README.md', 'r').read(),
    long_description_content_type="text/markdown",
    author='LX',
    author_email='lx984608061@163.com',
    maintainer='LX',
    maintainer_email='lx984608061@163.com',
    license='BSD License',
    platforms=["all"],
    url='https://github.com/LX-sys/CSelenium',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries'
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        'bs4',
        'selenium'
    ]

)