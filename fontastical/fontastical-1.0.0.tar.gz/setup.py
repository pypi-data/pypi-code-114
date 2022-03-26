import setuptools

with open("README.md", "r") as fhandle:
    long_description = fhandle.read()

setuptools.setup(
    name="fontastical",
    version="1.0.0",
    author="EpicCodeWizard",
    author_email="epiccodewizard@gmail.com",
    description="Fancy fonts for your terminal!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://replit.com/@EpicCodeWizard/Fontastical",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
