import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DSPutility",
    version="0.0.16",
    author="bonzo",
    author_email="bonzo.yang@dsp.im",
    description="DSP utility collection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dspim/DSPutility",
    packages=setuptools.find_packages(include=['dsputility', 'dsputility.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['sqlalchemy'],
    python_requires='>=3.8',
)
