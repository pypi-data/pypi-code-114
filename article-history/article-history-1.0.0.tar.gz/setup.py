import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="article-history",
    version="1.0.0",
    author="Andrew and Bob @ PDM",
    author_email="support@pybit.es",
    description="A tool to find similarity between (historic) articles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Drucifer2082/Django",
    project_urls={
        "Bug Tracker": "https://github.com/Drucifer2082/Django",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["history"],
    include_package_data=True,
    install_requires=["requests", "bs4", "gensim", "python-dotenv"],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "history=history.__main__:main",
        ]
    },
)
