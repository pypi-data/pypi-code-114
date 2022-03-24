from setuptools import setup, find_packages


setup(
    name='riotapiutilities',
    version='1.1.3',
    license='MIT',
    author="Jack Fink",
    author_email='jackfink68@yahoo.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/bugg86/Riot-API-Utilities',
    keywords='riot api utilities',
    install_requires=[
          'requests',
      ],

)