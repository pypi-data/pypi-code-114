"""SETUP PACKAGING"""
from setuptools import setup

with open("public.md", "r") as fh:
    long_description = fh.read()

# for experiments
dev_requires = [
    "mpmath==1.1.0",
    "numpy==1.18.1",
    "pandas==1.0.1",
    "boto3==1.14.56",
    "botocore==1.17.56",
    "scipy==1.4.1",
    "regex==2021.8.3",
    "requests==2.27.1",
]

base_requires = [
    'awswrangler==2.14.0',
    'scipy==1.4.1',
    'requests==2.27.1'
]

setup(
    name="dp_tms",
    version="0.1.0",
    description="reusable utilities shared across tms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Ringier South Africa',
    author_email='tools@ringier.co.za',
    packages=[
        "dp_tms",
        "dp_tms/utils",
        "dp_tms/database",
        "dp_tms/database/queries",
        "dp_tms/scorers",
        "dp_tms/services",
    ],
    python_requires=">=3.6",
    install_requires=base_requires,
    extras_require={
        "develop": dev_requires
    }
)
