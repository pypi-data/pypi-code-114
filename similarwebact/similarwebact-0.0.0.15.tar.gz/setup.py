import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="similarwebact", ##
    version="0.0.0.15", ##
    author="Sunkyeong Lee", ## ex) Sunkyeong Lee
    author_email="sunkyeong.lee@concentrix.com", ##
    description="automation tool for similarweb", ##
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SunkyeongLee/similarwebact", ##
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)