import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requires = [
	"aiohttp==3.8.1",
]

setuptools.setup(
    name="JSFetch",
    version="0.0.5",
    author="FSChatBot",
    description="Lets you make fetch requests in python as you would in JavaScript",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fschatbot/JSFetch",
    project_urls={
        "Bug Tracker": "https://github.com/fschatbot/JSFetch/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
	install_requires=requires,
    python_requires=">=3.10",
)