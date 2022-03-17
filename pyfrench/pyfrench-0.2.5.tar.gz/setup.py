from setuptools import find_packages, setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='pyfrench',
    packages=find_packages(),
    version='0.2.5',
    description='Une librairie qui traduit python en français',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Artic#6377',
    license='MIT',
    url='https://github.com/ArticOff/pyfrench',
    install_requires=[],
    setup_requires=['pytest-runner'], 
    tests_require=['pytest'], 
    test_suite='tests',
    author_email="artic.admisoffi@gmail.com",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: French',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ]
)