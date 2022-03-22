from setuptools import setup, find_packages

setup(
    name="aws-sesh",
    version="0.0.1",
    packages=["sesh"],
    url="https://github.com/panchgonzalez/aws-sesh",
    author="Francisco Gonzalez",
    author_email="fg@panch.io",
    description="AWS MFA session manager",
    entry_points={
        "console_scripts": ["sesh=sesh.cli:sesh"]
    },
)