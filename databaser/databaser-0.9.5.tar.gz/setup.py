import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="databaser",
    version="0.9.5",
    author="Aly Mohamed Hassan",
    author_email="alyhassan10@hotmail.com",
    description="A small package to generate SQL for postgreSQL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alymohamedhassan/databaser",
    project_urls={
        "Bug Tracker": "https://github.com/alymohamedhassan/databaser/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
