
import setuptools

setuptools.setup(
    name="oddeven",
    version="0.1.0",
    author="Fernando Rodrigues",
    author_email="devfernandorodrigues@gmail.com",
    description="A package that show if number is odd or even",
    package_dir={"": "oddeven"},
    packages=setuptools.find_packages(where="oddeven"),
    python_requires=">=3.7",
)
