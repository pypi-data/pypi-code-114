from setuptools import setup

setup(
    name='autoDropbox',
    version='0.9.6',
    author='Tiancheng Jiao',
    author_email='jtc1246@outlook.com',
    url='https://github.com/jtc1246/autoDropbox',
    description='A simple API for Dropbox',
    packages=['autoDropbox'],
    install_requires=['myHttp>=1.1.0','mySecrets'],
    python_requires='>=3',
    platforms=["all"],
    license='GPL-2.0 License'
)