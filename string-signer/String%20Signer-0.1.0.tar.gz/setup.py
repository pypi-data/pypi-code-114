import pathlib

from setuptools import setup

BASEDIR = pathlib.Path(__file__).parent
README = (BASEDIR / "README.md").read_text()

setup(
    name="String Signer",
    python_requires=">3.6",
    version="0.1.0",
    description="Used to sign strings.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/cesarmerjan/string_signer",
    download_url="https://github.com/cesarmerjan/string_signer/archive/refs/heads/master.zip",
    author="Cesar Merjan",
    author_email="cesarmerjan@gmail.com",
    keywords=["sign", "backend", "session", "security", "signer"],
    license="MIT",
    include_package_data=True,
    package_dir={"": "src"},
    packages=["string_signer"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Environment :: Web Environment",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
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
