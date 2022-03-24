from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="ratelib",
    version="0.1.2",
    description="Python interface to REACLIB databases",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    keywords="nucleosynthesis astrophysics",
    url="https://github.com/kompoth/ratelib",
    author="Vasily Negrebetskiy",
    author_email="negrebetckii.vv16@physics.msu.ru",
    license="MIT",
    license_files="LICENSE",
    packages=["ratelib"],
    package_data={"ratelib": ["data/*"]},
    python_requires=">=3.5",
    install_requires=["numpy", "scipy"],
    test_suite="test",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Topic :: Scientific/Engineering :: Physics ",
    ],
)
