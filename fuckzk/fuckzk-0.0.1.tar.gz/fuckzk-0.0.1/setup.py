from setuptools import setup, Extension
import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='fuckzk',
    version='0.0.1',
    author='WildboarG',
    author_email='959586@outlook.com',
    url='',
    description=u'A small function to obtain the health reporting and submission information of Zhengzhou Institute of science and technology.',
    long_description_content_type="text/markdown",
    long_description = long_description,
    package_dir={"": "fuckzk"},
    packages=setuptools.find_packages(where="fuckzk"),
    install_requires=['requests>=2.27.1'],
    entry_points={
        'console_scripts': [
        ]
    }
)
