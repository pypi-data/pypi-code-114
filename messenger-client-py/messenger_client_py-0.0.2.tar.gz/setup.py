from setuptools import setup, find_packages

setup(name="messenger_client_py",
      version="0.0.2",
      description="Messenger client",
      author="Test author",
      author_email="msngrtest@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
