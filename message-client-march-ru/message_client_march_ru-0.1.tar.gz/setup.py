from setuptools import setup, find_packages

setup(name="message_client_march_ru",
      version="0.1",
      description="Client packet",
      author="student_forever",
      author_email="test@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
