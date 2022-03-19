from setuptools import setup, find_packages
from pathlib import Path

# Get the current directory of the setup.py file (as this is where the README.md will be too)
current_dir = Path(__file__).parent
long_description = (current_dir / "README.md").read_text()

# Set up the package metadata
setup(
    name="betfair_ex_connection",
    author="Jamie O'Brien",
    description="A package with functions for getting Betfair Exchange odds on upcoming Premier League matches.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    version="0.1.2",
    packages=find_packages(include=["betfair_ex_connection", "betfair_ex_connection.*"]),
    install_requires=[
        'numpy', 
        'pandas', 
        'requests'
        ]
)