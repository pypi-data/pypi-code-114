from setuptools import setup, find_packages

setup(name="ess_server",
      version="0.0.1",
      description="ess Server",
      author="Julia",
      author_email="Juhaqq@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex'],
      scripts=['server/server_run']
      )
