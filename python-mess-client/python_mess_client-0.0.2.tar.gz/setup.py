from setuptools import setup, find_packages

setup(name="python_mess_client",
      version="0.0.2",
      description="Client for Messenger ",
      author="Viktor Sinaiskij",
      author_email="ekspertasds@gmail.com",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
