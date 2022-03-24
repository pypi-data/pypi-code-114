from distutils.core import setup
from setuptools import find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(name='hzyUtils',
      version='1.0.0',
      description='hzyUtils',
      long_description=long_description,
      author='大轰',
      author_email='fondadam@hotmail.com',
      url='https://mmbiz.qpic.cn/mmbiz_jpg/g82uB8Bp44lVfsYGZJ2JlibDIqBJR6KxShuB2RTzNTVE0k9H7S3oc0FLfjLY69EWlElB3zX5EHqMxOaQibSwLGwA/0?wx_fmt=jpeg',
      install_requires=[],
      license='BSD License',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Software Development :: Libraries'
      ],
      )
