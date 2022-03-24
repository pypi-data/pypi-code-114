from pathlib import Path

from setuptools import find_packages, setup

with open(Path(__file__).resolve().parent / "README.md") as f:
    readme = f.read()

extras = {
    "cli": ["httpx"],
}

setup(
    name="retractions",
    url="https://github.com/clbarnes/retractions",
    author="Chris L. Barnes",
    description="Check DOIs for retractions",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(include=["retractions"]),
    install_requires=[],
    extras_require=extras,
    python_requires=">=3.8, <4.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    entry_points={"console_scripts": ["retractions=retractions.cli:main"]},
)
