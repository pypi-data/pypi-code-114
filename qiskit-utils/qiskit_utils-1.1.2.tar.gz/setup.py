from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='qiskit_utils',
    version='1.1.2',
    license='MIT',
    author="Marek Grzesiuk",
    packages=['qiskit_utils'],
    url='https://github.com/mgrzesiuk/qiskit-utils',
    keywords='utility-methods qiskit',
    install_requires=[
          'qiskit>=0.34.2',
      ],
    description="package containing utility methods for qiskit like result parsing and instruction insertion for circuits",
    long_description=long_description,
    long_description_content_type='text/markdown'
)