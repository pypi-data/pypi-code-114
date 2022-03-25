from setuptools import setup, find_packages

setup(name="my_app_server",
      version="0.0.2",
      description="Server",
      author="Anastasia Yurko",
      author_email="anastsijajurko@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex'],
      scripts=['server/server_run']
      )
