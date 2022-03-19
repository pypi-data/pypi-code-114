from setuptools import setup, find_packages

setup(name="py_messager_client",
      version="0.0.2",
      description="Mess Client",
      author="Albina Bolsheva",
      author_email="kraeva_lelya@list.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
