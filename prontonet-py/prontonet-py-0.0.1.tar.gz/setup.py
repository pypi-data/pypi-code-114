from setuptools import setup


def readme_file_contents():
    with open('README.rst') as readme:
        data = readme.read()
    return data


setup(
    name='prontonet-py',
    version='0.0.1',
    description='Python SDK library for Prontonet Family v2.5.4',
    long_description=readme_file_contents(),
    author='avc',
    author_email='avcsec@protonmail.com',
    license='MIT',
    packages=['prontonet'],
    zip_safe=False,
    install_requires=[]
)
