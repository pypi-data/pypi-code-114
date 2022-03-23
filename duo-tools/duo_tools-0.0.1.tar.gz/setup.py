import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="duo_tools",  # Replace with your package name
    version="0.0.1",
    author="Chen Duo",
    author_email="cdsjtu@gmail.com",
    description="Chen Duo's personal tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cheduo/duo_tools",
    packages=setuptools.find_packages(),
    install_requires=['qpython'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
