import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-package-serguun42",
    version="0.2.0",
    author="serguun42",
    author_email="pypi@serguun42.ru",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/serguun42/serguun42-python-practices/practice3/test-package",
    project_urls={
        "Bug Tracker": "https://github.com/serguun42/serguun42-python-practices/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
