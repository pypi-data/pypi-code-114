import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mixnet",
    version="0.0.3",
    author="Has",
    author_email="author@example.com",
    description="A model to predict compressive strength of concrete based on it's composition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DaHamster/mixnet",
    project_urls={
        "Bug Tracker": "https://github.com/DaHamster/mixnet/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    include_package_data=True,
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
          'xgboost',
          'numpy'
      ],
)