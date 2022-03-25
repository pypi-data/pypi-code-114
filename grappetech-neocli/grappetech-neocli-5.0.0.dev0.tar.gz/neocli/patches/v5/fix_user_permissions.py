# imports - standard imports
import getpass
import os
import subprocess

# imports - module imports
from neocli.cli import change_uid_msg
from neocli.config.production_setup import get_supervisor_confdir, is_centos7, service
from neocli.config.common_site_config import get_config
from neocli.utils import exec_cmd, get_neocli_name, get_cmd_output


def is_sudoers_set():
	"""Check if neocli sudoers is set"""
	cmd = ["sudo", "-n", "neocli"]

	with open(os.devnull, "wb") as f:
		return_code_check = not subprocess.call(cmd, stdout=f)

	if return_code_check:
		try:
			neocli_warn = change_uid_msg in get_cmd_output(cmd, _raise=False)
		except subprocess.CalledProcessError:
			neocli_warn = False
		finally:
			return_code_check = return_code_check and neocli_warn

	return return_code_check


def is_production_set(neocli_path):
	"""Check if production is set for current neocli"""
	production_setup = False
	neocli_name = get_neocli_name(neocli_path)

	supervisor_conf_extn = "ini" if is_centos7() else "conf"
	supervisor_conf_file_name = f'{neocli_name}.{supervisor_conf_extn}'
	supervisor_conf = os.path.join(get_supervisor_confdir(), supervisor_conf_file_name)

	if os.path.exists(supervisor_conf):
		production_setup = production_setup or True

	nginx_conf = f'/etc/nginx/conf.d/{neocli_name}.conf'

	if os.path.exists(nginx_conf):
		production_setup = production_setup or True

	return production_setup


def execute(neocli_path):
	"""This patch checks if neocli sudoers is set and regenerate supervisor and sudoers files"""
	user = get_config('.').get("neo_user") or getpass.getuser()

	if is_sudoers_set():
		if is_production_set(neocli_path):
			exec_cmd(f"sudo neocli setup supervisor --yes --user {user}")
			service("supervisord", "restart")

		exec_cmd(f"sudo neocli setup sudoers {user}")
