from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

project_slug = "webhook-actions"
module_name = project_slug.replace("-", "_")

setup(
    name=project_slug,
    use_scm_version=True,
    url=f"https://github.com/Senth/{project_slug}",
    license="MIT",
    author="Matteus Magnusson",
    author_email="senth.wallace@gmail.com",
    description="Webhook that runs scripts depending on the name",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    entry_points={"console_scripts": [f"{project_slug}={module_name}.__main__:main"]},
    include_package_data=True,
    data_files=[(f"config", [f"config/.{project_slug}.cfg"])],
    install_requires=[
        "blulib==0.1.0",
        "flask-classful",
        "flask",
        "tealprint==0.1.0",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
)
