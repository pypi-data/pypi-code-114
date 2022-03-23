import re
from pathlib import Path
from setuptools import find_packages, setup

try:
    with open('setup.cfg') as fin:
        for line in fin:
            matched = re.match(r'\s*version\s*=\s*([.0-9abrc])\b', line)
            if matched:
                global __version__
                __version__ = (matched.groups()[-1] or '').strip()
                break
except Exception as e:
    print('ERROR in setup.py: Unable to find version in setup.cfg')
    print(e)

REPO_DIR = Path(__file__).resolve().absolute().parent
name = REPO_DIR.name
package_data = {
    name: [str(p) for p in REPO_DIR.glob(f'src/{name}/data')]
}

# TODO: default requirements here and try/except with loud failure
with Path('requirements.txt').open() as fin:
    install_requires = [req.strip() for req in fin]
    # r = install_requires[0]
    # if re.match(r'^#\s*\d{1,2}[.]\d{1,4}.\d{1,4}[rd]?\s*$', r):
    #     __version__ = req.strip().strip('#').strip()
    install_requires = [
        req.strip() for req in install_requires
        if req.strip() and not req.lstrip().startswith('#')]
    install_requires = [
        req for req in install_requires
        if req.strip() and not req.lstrip().startswith('#')]
    print('install_requires = [')
    for req in install_requires:
        print(f'    {req},')
    print(']')
    print(install_requires)


setup(
    name=name,
    install_requires=install_requires
)
