import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="filewatch-cli",
    version="1.0.1",
    author="Adarsh Gourab Mahalik",
    description="FILEWATCH is a file watcher that allows you to watch files if something changes run arguments",
    license="MIT",
    keywords="filewatch",
    packages=['filewatch'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/tinasty/filewatch",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "click>=8.0.4",
        "colorama>=0.4.4",
        "commonmark>=0.9.1",
        "Pygments>=2.11.2",
        "rich>=12.0.0"
    ],
)
