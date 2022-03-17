import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamlit-authenticator",
    version="0.1.2",
    author="Mohammad Khorasani",
    author_email="khorasani.mohammad@gmail.com",
    description="A secure authentication module to validate user credentials in a Streamlit application.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mkhorasani/Streamlit-Authenticator",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=['Python', 'Streamlit', 'Authentication', 'Components'],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.86",
        "extra-streamlit-components >= 0.1.53",
        "bcrypt >= 3.1.7",
        "PyJWT >=2.3.0",
    ],
)
