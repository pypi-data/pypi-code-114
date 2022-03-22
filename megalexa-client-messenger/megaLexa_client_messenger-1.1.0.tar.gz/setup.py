from setuptools import setup, find_packages

setup(name="megaLexa_client_messenger",
      version="1.1.0",
      description="megaLexa_client_messenger",
      author="MegaLexa",
      author_email="itsnotmyrealmail@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
