from setuptools import setup, find_packages

# Read the contents of the README.md file
from pathlib import Path
current_directory = Path(__file__).parent
long_description = (current_directory/'README.md').read_text()

setup(
    name = 'sfdcfw',
    version = '0.1.5',
    packages = find_packages(),

    # Dependency
    install_requires = [
        'pandas',
        'requests',
        'zeep',
    ],

    # Metadata
    author = 'Yan Kuang',
    author_email = 'YTKme@Outlook.com',
    description = 'Saleforce.com FrameWork.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
    keywords = 'salesforce sfdc fw api',
)