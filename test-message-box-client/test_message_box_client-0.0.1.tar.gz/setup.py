from setuptools import setup, find_packages

setup(name="test_message_box_client",
      version="0.0.1",
      description="message_box_client",
      author="Dmitrii F",
      author_email="dffss@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
