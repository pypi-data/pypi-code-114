from setuptools import setup
from pathlib import Path

long_description = (Path(__file__).parent / "README.rst").read_text()

setup(
    name="vtkwriters",
    use_scm_version={"write_to": "vtkwriters/_version.py"},
    setup_requires=["setuptools_scm"],
    author="Simon Lopez",
    author_email="s.lopez@brgm.fr",
    description="A set of routines to write KitWare VTK/Paraview files.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    license="GPL v.3",
    url="https://github.com/BRGM/vtkwriters",
    download_url="https://github.com/BRGM/vtkwriters/tarball/master",
    packages=["vtkwriters"],
    keywords=["vtk", "paraview"],
    zip_safe=True,
)
