#! /usr/bin/env python

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requires = [
	"aiohttp==3.8.1",
]

setuptools.setup(
    name="JSFetch",
    version="0.0.6",
    author="FSChatBot",
    description="Lets you make fetch requests in python as you would in JavaScript",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fschatbot/JSFetch",
    project_urls={
        "Bug Tracker": "https://github.com/fschatbot/JSFetch/issues",
    },
    classifiers=[
		"Development Status :: 3 - Alpha",
		"Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	keywords = "Networking, Javascript, JS, Fetch, Async, AsyncIO, AsyncHTTPClient, AsyncHTTP",
    package_dir={"JSFetch": "src"},
	packages=["JSFetch"],
	install_requires=requires,
    python_requires=">=3.10",
)