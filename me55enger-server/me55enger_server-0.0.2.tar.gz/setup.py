from setuptools import setup, find_packages

setup(name='me55enger_server',
      version='0.0.2',
      description='me55enger_server',
      author='Konstantin Benderov',
      author_email='konstantinbenderov@gmail.com',
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
