import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="decOM",
    version="0.0.2",
    author="Camila Duitama González",
    author_email="cduitama@pasteur.fr",
    description="decOM: K-mer method for aOral metagenome decontamination",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CamilaDuitama/OM",
    project_urls={
        "Bug Tracker": "https://github.com/CamilaDuitama/OM/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    include_package_data=True,
    package_data={'': ['data/*']},
)
