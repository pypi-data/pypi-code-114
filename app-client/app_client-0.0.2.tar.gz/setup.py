from setuptools import setup, find_packages

setup(name="app_client",
      version="0.0.2",
      description="Client",
      author="Anastasia Yurko",
      author_email="anastsijajurko@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
