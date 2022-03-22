from setuptools import setup, find_packages

setup(name="ess_client",
      version="0.0.1",
      description="ess Client",
      author="Julia",
      author_email="Juhaqq@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
