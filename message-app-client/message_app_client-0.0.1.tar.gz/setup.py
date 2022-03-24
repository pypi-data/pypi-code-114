from setuptools import setup, find_packages

setup(name="message_app_client",
      version="0.0.1",
      description="message_app_client",
      author="Sinitsyn Andrey",
      author_email="andrey-sin@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
