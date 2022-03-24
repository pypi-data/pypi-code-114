import shutil
import subprocess
from optimeed import VERSION


def update_pipy():
    shutil.rmtree('build', ignore_errors=True)
    shutil.rmtree('dist', ignore_errors=True)
    shutil.rmtree('optimeed.egg-info', ignore_errors=True)

    subprocess.run('python setup.py sdist bdist_wheel', shell=True)
    subprocess.run('twine upload dist/*', shell=True)


def update_git_version():
    import subprocess

    subprocess.run('git tag -a v{} -m "Version {}"'.format(VERSION, VERSION), shell=True)
    subprocess.run('git push origin --tags', shell=True)
