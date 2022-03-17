# this file is a scratchpad for testing and trying out
# different things
import sys
import subprocess
from subprocess import CalledProcessError
from sciunit2.workspace import _mkdir_p
from sciunit2.workspace import at


# 1. install virtualenv using pip(assuming pip is installed)
try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                           '--user', 'virtualenv'])
except CalledProcessError as err:
    print(err.stderr)
    exit()
# 2. create new environment using virtualenv and
# install all Python dependencies in it
subprocess.check_call(['virtualenv', 'new_env'])
subprocess.check_call(['source', 'new_env/bin/activate'])

# 3. create new folder in cwd and bring all code+data
# in /home/<user> there
eid = 'e1'
req_file = eid + '-requirements.txt'
project_dir = at()
project_name = project_dir.split('/')[-1]
home_dir = project_dir + '/cde-package/cde-root/home/*/'
data_dir = home_dir.split('/')[-1]
_mkdir_p(data_dir)
subprocess.call(['cp', '-r', home_dir+'/*', data_dir])

