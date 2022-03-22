import setuptools

with open('README.md', "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="RPCLayout",
    version="2.1.3",
    author="neokeee",
    author_email="neopkr90@gmail.com",
    description="Simple template API for Discord rich presence!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/neopkr/RPCLayout",
    project_urls={
        "Bug Tracker": "https://github.com/neopkr/RPCLayout/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['RPCLayout'],
    include_package_data=True,
    python_requires=">=3.5",
    platforms=['Windows', "OSX"],
    zip_safe=True,
    license="MIT"
)