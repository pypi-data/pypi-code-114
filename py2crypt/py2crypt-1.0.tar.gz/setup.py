from setuptools import setup

with open('README.md', 'r') as f:
    setup(
        name='py2crypt',
        version='1.0',
        description='This library provides a top-level interface to the cryptography.io module.',
        long_description=f.read(),
        long_description_content_type='text/markdown',
        license='MIT',
        url='https://github.com/badlock/py2crypt',
        author='Badlock',
        install_requires=['cryptography'],
        packages=['py2crypt'],
        package_dir={'': 'src'}
    )