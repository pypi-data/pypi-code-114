from pathlib import Path

from setuptools import setup, find_packages

here = Path(__file__).parent.resolve()

long_description = (here/'README.md').read_text(encoding='utf-8')

setup(
    name='tealc',
    version='0.2.0',
    author='David E. Lambert',
    author_email='david@davidelambert.com',
    description='Tension Estimate cALCulator for stringed instruments.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/davidelambert/tealc',
    project_urls={
        'Bug Reporting': 'https://github.com/davidelambert/tealc/issues',
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Topic :: Utilities',
    ],
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'tealc=tealc.cli:cli'
        ]
    },
    package_data={
        'tealc': ['*.json', 'manual.txt']
    }
)
