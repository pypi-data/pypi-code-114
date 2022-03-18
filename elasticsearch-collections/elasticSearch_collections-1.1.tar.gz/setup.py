import setuptools

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = ["loguru", "elasticsearch == 7.11.0"]

setup(name="elasticSearch_collections",
      description="Collections of ElasticSearch pyscripts for human",
      long_description=long_description,
      long_description_content_type="text/markdown",
      license="MIT",
      version="1.1",
      author="Alex Ng",
      author_email="alex_q_wu@qq.com",
      maintainer="Alex Ng",
      maintainer_email="alex_q_wu@qq.com",
      url="https://github.com/AlexNg9527/ElasticSearchCollections",
      packages=setuptools.find_packages(),
      install_requires=requires,
      classifiers=[
          'Programming Language :: Python :: 3',
      ])
