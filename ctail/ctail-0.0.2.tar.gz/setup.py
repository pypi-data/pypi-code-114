import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ctail",
    version="0.0.2",
    author="Otger Ballester",
    author_email="otger@gmail.com",
    description="A colored tail",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/otger/ctail",
    project_urls={
        "Bug Tracker": "https://github.com/otger/ctail/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    scripts=['bin/ctail']
)