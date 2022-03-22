from setuptools import setup

setup(
    name="commitizen_oca",
    version="0.2.0",
    py_modules=["commitizen_oca/cz_commitizen_oca"],
    license="MIT",
    url="https://gitlab.com/coopdevs/tooling/commitizen-oca",
    long_description="Commitizen for Odoo Community",
    install_requires=["commitizen"],
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt"],
    }
)
