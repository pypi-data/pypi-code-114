from setuptools import setup, find_packages

setup(name="my_first_messenger_server",
      version="0.0.1",
      description="Messenger Server",
      author="Aleksandr",
      author_email="aleksander.17047665@gmail.com",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
