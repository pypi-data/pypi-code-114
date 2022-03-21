from setuptools import setup, find_packages

setup(name="massage_server_march_ru",
      version="0.1",
      description="Server packet",
      author="student_forever",
      author_email="test@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
