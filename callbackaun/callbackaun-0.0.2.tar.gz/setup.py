from setuptools import setup, Extension
from setuptools import find_packages

import callbackaun


with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

VERSION = '0.0.2'
if __name__ == "__main__":
    setup(
        name="callbackaun",
        version=VERSION,
        description="Callbackaun: Custom Callbacks that will control training",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Shivam Chhetry",
        author_email="Shivam.11712711@gmail.com",
        url="https://github.com/shivamkc01/CallbackAUN_library",
        license="MIT License",
        packages=find_packages(),
        include_package_data=True,
        platforms=["MacOS", "MacOS X", "Windows", "linux", "unix"],
        python_requires=">3.5.2",
        install_requires=["scikit-learn>=0.24.3"],
        keyword=['python', 'keras', 'callbacks', 'Model training']
    )