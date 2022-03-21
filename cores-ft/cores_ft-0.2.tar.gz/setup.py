from setuptools import setup, find_packages


def read_readme():
    with open('README.md') as f:
        return f.read()


PACKAGE = 'cores_ft'
NAME = 'cores_ft'
DESCRIPTION = 'Monitora frequencia e temperatuda dos cores da CPU'
AUTHOR = 'Henrique C. C. de Andrade'
AUTHOR_EMAIL = 'henrique.ccda@gmail.com'
URL = 'https://github.com/HenriqueCCdA/cores_ft'
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    platforms=['Linux'],
    description=DESCRIPTION,
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license='MIT',
    url=URL,
    packages=find_packages(exclude=["cores_ft.tests"]),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
    ],
    install_requires=[
    ],
    zip_safe=False,
)
