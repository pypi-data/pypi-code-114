from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='my_portfolio_analysis',
    version='0.1.1',
    packages=find_packages(),
    url='https://github.com/laye0619/my_portfolio_analysis',
    author='LayeWang',
    author_email='laye0619@gmail.com',
    description='',
    include_package_data=True,
    install_requires=[
        "xalpha",
        "pandas",
        "openpyxl"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
