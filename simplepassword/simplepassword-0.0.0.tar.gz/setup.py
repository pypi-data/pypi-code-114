from setuptools import setup, find_packages

DESCRIPTION = 'Simple tool to generate password'
LONG_DESCRIPTION = """
    Simple tool to generate password.
    Solution for shad home work.
"""

setup(
    name="simplepassword",
    version='0.0.0',
    author="Johny Utah",
    author_email="jones.hovercraft2020@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['cryptography'],
    include_package_data=True,
    keywords=['python', 'password', 'password manager'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
