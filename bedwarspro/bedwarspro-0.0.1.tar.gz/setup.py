from setuptools import setup, find_packages

setup(
    name='bedwarspro',
    version='0.0.1',
    license='MIT',
    author="Co0kei",
    description='A Python wrapper for the Bedwars Pro API',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Co0kei',
    install_requires=[
        "aiohttp>=3.6.0"
    ],

)
