import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geojson_transformer",
    version="0.0.6",
    author="Ivan Gochev",
    author_email="ivan.gotchev94@gmail.comm",
    description="Tool for extracting data from geojson or gpx files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ivan4oto/gpx_geojson_py/",
    project_urls={
        "Bug Tracker": "https://github.com/ivan4oto/gpx_geojson_py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    package_data={
      'geojson_transformer': ['*.json'],
   },
    python_requires=">=3.6",
    install_requires=[
        'lxml'
    ]
)