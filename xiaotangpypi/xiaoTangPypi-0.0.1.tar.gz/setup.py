import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="xiaoTangPypi",
    version="0.0.1",
    author="xiaoTang",
    author_email="123456@gmail.com",
    description="Simple test example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/taw19960426/-Speech-signal-processing-experiment-tutorial-_python.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
