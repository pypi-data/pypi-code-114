import os
import subprocess
import userconfig

pythonenv=userconfig.data['python']
processpath = userconfig.getProcessPath('\\Routines\\RunRoutines.py')
os.environ['PYTHONPATH'] = userconfig.data['source_directory']
os.system('start cmd /K '+pythonenv+' '+processpath)


# processpath = userconfig.getProcessPath('\\MarketData\\CME\\parse_files.py')
# os.system('start cmd /K '+pythonenv+' '+processpath+ ' 2020-01-01')
