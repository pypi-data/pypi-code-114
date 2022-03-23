import pathlib

from setuptools import setup

BASEDIR = pathlib.Path(__file__).parent
README = (BASEDIR / "README.md").read_text()

setup(
    name="Web Encoder",
    python_requires=">3.6",
    version="0.1.0",
    description="Used to encode or decode data in a web-friendly format.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/cesarmerjan/web_encoder",
    download_url="https://github.com/cesarmerjan/web_encoder/archive/refs/heads/master.zip",
    author="Cesar Merjan",
    author_email="cesarmerjan@gmail.com",
    keywords=["encode", "backend", "session"],
    license="MIT",
    include_package_data=True,
    package_dir={"": "src"},
    packages=["web_encoder"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Environment :: Web Environment",
        "Topic :: Utilities",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Pre-processors",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
