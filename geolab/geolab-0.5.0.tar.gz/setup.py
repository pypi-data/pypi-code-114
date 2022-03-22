from setuptools import find_packages, setup

setup(
    name='geolab',
    version='v0.5.0',
    description='',
    long_description='',
    url='https://github.com/DavidePellis/geolab',
    author='Davide Pellis',
    download_url='https://github.com/DavidePellis/geolab/archive/v0.5.0.tar.gz',
    author_email='davidepellis@gmail.com',
    packages=find_packages(),
    package_data={'': ['icons/*.png', '*.obj']},
    classifiers=['Development Status :: 1 - Planning'],
    license='MIT',
)
