import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cloud_utility",                   # This is the name of the package
    version="0.0.1",                        # The initial release version
    author="Indranil Pal",                  # Full name of the author
    description="Package for any cloud apis",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.7',                # Minimum version requirement of the package
    py_modules=["google_storage_utility"],  # Name of the python package
    package_dir={'':'cloud_utility/src'},     # Directory of the source code of the package
    install_requires=["google-cloud-storage"]                     # Install other dependencies if any
)