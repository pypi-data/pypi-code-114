"""Setup file for the project.

Most of the static configuration is in "setup.cfg".
"""


from setuptools import setup, find_packages


setup(
    use_scm_version={
        "write_to": "src/ptvpy/_version.py",
        "version_scheme": "no-guess-dev",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["ptvpy = ptvpy.__main__:main"]},
)
