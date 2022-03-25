import click, os
from neocli.config.procfile import setup_procfile
from neocli.config.supervisor import generate_supervisor_config
from neocli.utils.app import get_current_neo_version, get_current_branch

def execute(neocli_path):
	neo_branch = get_current_branch('neo', neocli_path)
	neo_version = get_current_neo_version(neocli_path)

	if not (neo_branch=='develop' or neo_version >= 7):
		# not version 7+
		# prevent running this patch
		return False

	click.confirm('\nThis update will remove Celery config and prepare the neocli to use Python RQ.\n'
		'And it will overwrite Procfile and supervisor.conf.\n'
		'If you don\'t know what this means, type Y ;)\n\n'
		'Do you want to continue?',
		abort=True)

	setup_procfile(neocli_path, yes=True)

	# if production setup
	if os.path.exists(os.path.join(neocli_path, 'config', 'supervisor.conf')):
		generate_supervisor_config(neocli_path, yes=True)
