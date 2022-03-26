import setuptools

with open("README.md", "rb") as fin:
    long_description = fin.read().decode("utf-8")

req = ["numpy",
       "scipy",
       "pytest",
       "h5py",
       "typing",
       "PyYAML",
       "recommonmark",
       "sphinx_rtd_theme",
       "opt_einsum",
       "qutip"]

setuptools.setup(
    name="renormalizer",
    version="0.0.2",
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shuaigroup/Renormalizer",
    install_requires=req,
    license="Apache",
)
