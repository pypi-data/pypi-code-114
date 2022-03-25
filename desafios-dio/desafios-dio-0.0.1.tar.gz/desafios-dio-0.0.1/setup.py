from setuptools import setup, find_packages

with open("README.md","r") as f:
    page_description = f.read()

setup(
    name="desafios-dio",
    version="0.0.1",
    author="José Francisco Azevedo da Silva",
    author_email="josezev@gmail.com",
    description="Arquivos criados para realização dos desafios 1 2 do bootcap Cognizant",
    long_description_content_type="text/markdown",
    url="https://github.com/joseazev/desafios-dio.git",
    python_requires='>=3.8',
    scripts=['nsmpy.py']
)