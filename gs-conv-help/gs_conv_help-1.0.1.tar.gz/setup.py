
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gs_conv_help",
    version="1.0.1",
    author="gupshup_gip",
    author_email="rahul.meka@gupshup.io",
    description="This repository contains artifacts to help accelerate development of conversational interfaces using Rasa & Gip",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
   'pymongo>=3.0',
   'pandas>=1.0',
   "pyyaml>=5.0",
   "fuzzywuzzy>=0.18.0"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires="<3.9",
)