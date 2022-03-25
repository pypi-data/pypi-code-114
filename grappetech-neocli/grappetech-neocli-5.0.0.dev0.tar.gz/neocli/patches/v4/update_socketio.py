import subprocess

def execute(neocli_path):
	subprocess.check_output(['npm', 'install', 'socket.io'])