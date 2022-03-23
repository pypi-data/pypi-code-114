from similib.cmd import exe_command
exe_command("rm -rf ./dist/*")
exe_command("pip install --upgrade setuptools wheel")
exe_command("python setup.py sdist bdist_wheel")
exe_command("pip install --upgrade twine")
# exe_command("python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*")