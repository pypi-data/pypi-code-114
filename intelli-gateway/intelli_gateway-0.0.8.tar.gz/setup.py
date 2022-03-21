import setuptools

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setuptools.setup(
    name="intelli_gateway",
    version="0.0.8",
    author="Intelli Africa Solutions",
    author_email="ngoni.mangudya@intelliafrica.solutions",
    description="Python library for utilizing services offered on the Intelli Africa SMS/Email Gateway",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Intelli-Africa-Solutions/intelli-gateway",
    project_urls={
        "Issues": "https://github.com/Intelli-Africa-Solutions/intelli-gateway/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=["intelli_gateway"],
    package_dir={
        "": "src"
    },
    packages=setuptools.find_packages(where="src"),
    python_requires=">= 3.6",
    include_package_data=True,
    install_requires=[
        "requests",
        "numpy",
        "python-magic"
    ]
)
