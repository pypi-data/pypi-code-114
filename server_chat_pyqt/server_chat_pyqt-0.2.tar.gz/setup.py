from setuptools import setup, find_packages

setup(name="server_chat_pyqt",
      version="0.2",
      description="Client packet",
      author="Ekaterina Kondratyeva",
      author_email="kondraa@gmail.com",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
