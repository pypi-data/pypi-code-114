from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="validate_brackets",                 #pip install validate_brackets
    version="0.0.3",
    description="validate brackets in a string",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    author="Amit Chojar",
    author_email="pythonchojar@gmail.com",
    licence="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    py_modules=["ValidateBrackets"],          #name of the py file
    package_dir={"": "src"},
    extras_require={
        "dev": [
            "pytest>=3.7",
        ],
    },
    include_package_data=True                 #includes all non code files
)