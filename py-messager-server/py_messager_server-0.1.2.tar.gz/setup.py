from setuptools import setup, find_packages

setup(name="py_messager_server",
      version="0.1.2",
      description="Mess Server",
      author="Albina Bolsheva",
      author_email="kraeva_lelya@list.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex'],
      #scripts=['server/server_run']
      )
