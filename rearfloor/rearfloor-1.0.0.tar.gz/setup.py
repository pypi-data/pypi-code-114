import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rearfloor",
    version="1.0.0",
    author="Jason Carpenter",
    author_email="brad@identex.co",
    description="Easily background your functions in just 10 characters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/breadbored/rearfloor",
    project_urls={
        "Bug Tracker": "https://github.com/breadbored/rearfloor/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.3",
    install_requires=[
        "asyncio ; python_version<'3.4'",
    ]
)