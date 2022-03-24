from setuptools import setup, find_packages

setup(name="client_part",
      version="0.0.1",
      description="client_part_pyqt",
      author="Vyacheslav",
      author_email="rgka17@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycrypto', 'pycryptodomex']
      )
