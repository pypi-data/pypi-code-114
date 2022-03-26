import os
def Terminal2Local():
    cwd = os.getcwd()
    print('DIRECTORY_IS ' + cwd)
    if cwd == '/Users/frankie':
        os.chdir('/Users/frankie/PycharmProjects/PycharmProjectsShared/TradingProject/')
        print('Directory Uploaded')
    elif cwd == '/Users/alessandroborsatti':
        os.chdir('/Users/alessandroborsatti/PycharmProjects/PycharmProjectsShared/TradingProject/')
        print('Directory Uploaded')
    if cwd != os.getcwd():
        print('NEW_DIRECTORY_IS ' + os.getcwd())
    return
Terminal2Local()

# This line of code will allow shorter imports
from DirectoryFormulas.Directory import DirX
