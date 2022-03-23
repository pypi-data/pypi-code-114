#
# Module containing helpers to scan through files
#
import os


# Find all modules we need to import
# 1. Traverse all sub-directories under rootdir
# 2. Find all python files containing a decorator
# 3. If __init__.py doesn't exist in a subdir with a decorator, create it
# 4. Rename python filename to an importable module name
# 5. Return list of modules to import
def find_databutton_directive_modules(rootdir='./'):
    modules_to_import = []
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            file_path = subdir + '/' + file
            if(file.endswith('.py')):
                s = open(file_path, 'r').read()
                if('@' in s):
                    if('streamlit' in s):
                        if(subdir != rootdir):
                            init_file = subdir + '/__init__.py'
                            if(os.path.exists(init_file) is False):
                                open(init_file, 'a').close()
                        md = file_path.replace('.//', '')
                        md = md.replace('./', '')
                        md = md.replace('.py', '').replace('/', '.')
                        modules_to_import.append(md)

    return modules_to_import


# For a given python file, this returns
# a list with all import statements in that
# file
def get_library_dependencies_for_app(file):
    imports = []
    with open(file, 'r') as f:
        for line in f.readlines():
            if('import' in line):
                imports.append(line)
    return imports
