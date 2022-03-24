from setuptools import setup, find_packages
from pathlib import Path

# Get the current directory of the setup.py file (as this is where the README.md will be too)
current_dir = Path(__file__).parent
long_description = (current_dir / "README.md").read_text()

# Set up the package metadata
setup(
    name="psusannx_email",
    author="Jamie O'Brien",
    description="A package with a function for sending emails easily using sendgrid.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    version="0.1.0",
    packages=find_packages(include=["psusannx_email", "psusannx_email.*"]),
    install_requires=[
        'sendgrid>=6.9.7'
        ]
)