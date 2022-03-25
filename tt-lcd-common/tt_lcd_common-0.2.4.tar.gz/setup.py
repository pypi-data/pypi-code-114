import setuptools

with open("README.md", "r", encoding="utf-8") as read_me:
    long_description = read_me.read()


setuptools.setup(
    name='tt_lcd_common',
    version='0.2.4',
    author="Jere Rignell",
    author_email="jere.rignell@terveystalo.com",
    description="Common LCD Python scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rignellj/tt_lcd_common",
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    python_requires=">=3.6",
)
