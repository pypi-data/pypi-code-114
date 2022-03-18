import setuptools

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setuptools.setup(
    name="keepcodingtest_jeanflores",
    version="0.0.1",
    author="keepcoder_jeanflores",
    author_email="keepcodingjeanflores@gmail.com",
    description="un ejemplo de prueba",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.9",
    install_requires=[
        "build",
        "twine"
    ]
)