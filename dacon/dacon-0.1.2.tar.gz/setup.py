import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dacon",
    version="0.1.2",
    author="dacon",
    author_email="dacon@dacon.io",
    description="dacon-open-api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dacon-ds2/dacon-open-api", # project link
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    package_data={'': ['datasets/data/*.csv']},
)
"""
1. 패키지 빌드
python3 setup.py sdist bdist_wheel

2. 패키지 업로드
python3 -m twine upload dist/*
"""