from setuptools import setup, find_packages

setup(name="python_mess_server",
      version="0.0.3",
      description="Server for Messenger ",
      author="Viktor Sinaiskij",
      author_email="ekspertasds@gmail.com",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex'],
      scripts=['server/server_run.py']
      )
