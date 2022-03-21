from setuptools import setup, find_packages

long_description = None
with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="abottle",
    version="0.0.13",
    author="taylorhere",
    author_email="taylorherelee@gmail.com",
    description="put your model into **a bottle** then you get a working server and more.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["abottle=abottle.main:main"]},
    packages=find_packages(),
    python_requires="<3.10",
    install_requires=[
        "fastapi",
        "uvicorn[standard]",
        "numpy",
    ],
)
