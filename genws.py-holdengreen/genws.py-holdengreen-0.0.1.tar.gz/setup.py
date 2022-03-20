import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="genws.py-holdengreen",
    version="0.0.1",
    author="Holden Green",
    author_email="holdenmgreen@gmail.com",
    description="website generator for GEM projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://greenempower.org/projects/genws.py",
    #project_urls={
    #    "Bug Tracker": ""
    #},
    classifiers=[
        "Programming Language :: Python :: 3",
        #"License :: Peer Production License",
        #"Operation System :: Unix like"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    scripts=['bin/genws.py'],
)
