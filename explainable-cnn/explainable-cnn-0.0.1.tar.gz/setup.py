import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="explainable-cnn",
    version="0.0.1",
    author="Ashutosh Hathidara",
    author_email="ashutoshhathidara98@gmail.com",
    description="📦 Flexible visualization package for generating layer-wise explanations for CNNs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ashutosh1919/explainable-cnn",
    project_urls={
        "Bug Tracker": "https://github.com/ashutosh1919/explainable-cnn/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "explainable_cnn"},
    packages=setuptools.find_packages(where="explainable_cnn"),
    python_requires=">=3.6",
)
