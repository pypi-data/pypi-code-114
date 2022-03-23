from setuptools import setup, find_packages

setup(name="messenger_server_py",
      version="0.0.2",
      description="Messenger Server",
      author="Test author",
      author_email="msngrtest@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex'],
      # scripts=['server/server']
      )
