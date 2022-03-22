# installation script for program Natorbs
# written by Mariusz Radon

import glob
from setuptools import setup

set = setup(
    name = "natorbs",
    version = "1.0.1",
    description = "quantum-chemical utility for computing natural orbitals",
    long_description = """
Natorbs computes natural or natural-spin orbitals 
and natural orbitals for chemical valence (NOCV)
based on the canonical HF/DFT orbitals interfaced
either through cclib or Molden format.
""",
    author = "Mariusz Radon",
    author_email = "mradon@chemia.uj.edu.pl",
    url = "https://tungsten.ch.uj.edu.pl/~mradon/natorbs",
    download_url = "https://tungsten.ch.uj.edu.pl/downloadmanager/click.php?id=natorbs-1.0.1",
    license = "BSD-3-Clause",
    keywords = ["quantum chemistry", "natural orbitals", "nocv"],
    packages = ["natorbs"],
    scripts = ["scripts/natorbs"],
    data_files = [("share/man/man1", glob.glob("doc/*.1")),
                  ("share/doc/natorbs",
                   ["README.md", "LICENSE.txt"])],
    install_requires = ['numpy', 'cclib>=1.7'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)

