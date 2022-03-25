from setuptools import setup

with open('README.md', 'r') as f:
    setup(
        name='strict-types',
        version='1.2',
        description='Type checker for functions and classes.',
        long_description=f.read(),
        long_description_content_type='text/markdown',
        license='MIT',
        url='https://github.com/badlock/strict-types',
        author='Badlock',
        packages=['strict'],
        package_dir={'': 'src'}
    )