import os
from MOMORING.modules.files.applications_init_template import get_app_init


def create_python_package(package):
    if not os.path.exists(package):
        os.mkdir(package)
    f = open(os.path.join(package, '__init__.py'), 'w')
    if os.path.basename(package) == 'applications':
        f.write(get_app_init())
    f.close()


def create_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def create_file(file_name, txt=''):
    if not os.path.exists(file_name):
        f = open(file_name, 'w')
        f.write(txt)
        f.close()


