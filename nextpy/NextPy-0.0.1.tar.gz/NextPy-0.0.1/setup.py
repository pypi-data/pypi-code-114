import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NextPy",
    version="0.0.1",
    author="Studious Gamer, FloatingComet62",
    author_email="natyavidhanbiswas10@gmail.com",
    description="A Web development framework made in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/studiousgamer/NextPy",
    project_urls={
        "Bug Tracker": "https://github.com/studiousgamer/NextPy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "nextpy"},
    packages=setuptools.find_packages(where="nextpy"),
    python_requires=">=3.6",
)