import os
from neocli.utils import exec_cmd

def execute(neocli_path):
	exec_cmd('npm install yarn', os.path.join(neocli_path, 'apps/neo'))
