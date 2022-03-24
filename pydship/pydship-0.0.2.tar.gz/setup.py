from setuptools import setup
import os

ROOT_DIR='pydship'
with open(os.path.join(ROOT_DIR, 'VERSION')) as version_file:
    version = version_file.read().strip()

setup(name='pydship',
      version=version,
      description='Tools to parse and convert WERUM DSHIP data',
      url='https://github.com/MarineDataTools/pydship',
      author='Peter Holtermann',
      author_email='peter.holtermann@io-warnemuende.de',
      license='GPLv03',
      packages=['pydship'],
      scripts = [],
      entry_points={},
      package_data = {'':['VERSION']},
      zip_safe=False)


