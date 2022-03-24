from setuptools import setup, find_packages

setup(name="message_app_server",
      version="0.0.2",
      description="message_app_server",
      author="Sinitsyn Andrey",
      author_email="andrey-sin@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex'],
      scripts=['server/server_run']
      )
