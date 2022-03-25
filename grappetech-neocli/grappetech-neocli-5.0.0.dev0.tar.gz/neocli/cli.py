# imports - standard imports
import atexit
import json
import os
import pwd
import sys

# imports - third party imports
import click

# imports - module imports
import neocli
from neocli.neocli import NeoCLI
from neocli.commands import neocli_command
from neocli.config.common_site_config import get_config
from neocli.utils import (
	neocli_cache_file,
	check_latest_version,
	drop_privileges,
	find_parent_neocli,
	generate_command_cache,
	get_cmd_output,
	is_neocli_directory,
	is_dist_editable,
	is_root,
	log,
	setup_logging,
	parse_sys_argv,
)
from neocli.utils.neocli import get_env_cmd

# these variables are used to show dynamic outputs on the terminal
dynamic_feed = False
verbose = False
is_envvar_warn_set = None
from_command_line = False # set when commands are executed via the CLI
neocli.LOG_BUFFER = []
sys_argv = None

change_uid_msg = "You should not run this command as root"
src = os.path.dirname(__file__)


def cli():
	global from_command_line, neocli_config, is_envvar_warn_set, verbose, sys_argv

	from_command_line = True
	command = " ".join(sys.argv)
	argv = set(sys.argv)
	is_envvar_warn_set = not (os.environ.get("BENCH_DEVELOPER") or os.environ.get("CI"))
	is_cli_command = len(sys.argv) > 1 and not argv.intersection({"src", "--version"})
	sys_argv = parse_sys_argv()

	if "--verbose" in sys_argv.options:
		verbose = True

	change_working_directory()
	logger = setup_logging()
	logger.info(command)
	setup_clear_cache()

	neocli_config = get_config(".")

	if is_cli_command:
		check_uid()
		change_uid()
		change_dir()

	if (
		is_envvar_warn_set
		and is_cli_command
		and is_dist_editable(neocli.PROJECT_NAME)
		and not neocli_config.get("developer_mode")
	):
		log(
			"neocli is installed in editable mode!\n\nThis is not the recommended mode"
			" of installation for production. Instead, install the package from PyPI"
			" with: `pip install grappetech-neocli`\n",
			level=3,
		)

	in_neocli = is_neocli_directory()

	if (
		not in_neocli
		and len(sys.argv) > 1
		and not argv.intersection({"init", "find", "src", "drop", "get", "get-app", "--version"})
		and not cmd_requires_root()
	):
		log("Command not being executed in neocli directory", level=3)

	if in_neocli and len(sys.argv) > 1:
		if sys.argv[1] == "--help":
			print(click.Context(neocli_command).get_help())
			print(get_neo_help())
			return

		if (
			sys_argv.commands.intersection(get_cached_neo_commands())
			or sys_argv.commands.intersection(get_neo_commands())
		):
			neo_cmd()

		if sys.argv[1] in NeoCLI(".").apps:
			app_cmd()

	if not is_cli_command:
		atexit.register(check_latest_version)

	try:
		neocli_command()
	except BaseException as e:
		return_code = getattr(e, "code", 1)

		if isinstance(e, Exception):
			click.secho(f"ERROR: {e}", fg="red")

		if return_code:
			logger.warning(f"{command} executed with exit code {return_code}")

		raise e


def check_uid():
	if cmd_requires_root() and not is_root():
		log("superuser privileges required for this command", level=3)
		sys.exit(1)


def cmd_requires_root():
	if len(sys.argv) > 2 and sys.argv[2] in (
		"production",
		"sudoers",
		"lets-encrypt",
		"fonts",
		"print",
		"firewall",
		"ssh-port",
		"role",
		"fail2ban",
		"wildcard-ssl",
	):
		return True
	if len(sys.argv) >= 2 and sys.argv[1] in (
		"patch",
		"renew-lets-encrypt",
		"disable-production",
	):
		return True
	if len(sys.argv) > 2 and sys.argv[1] in ("install"):
		return True


def change_dir():
	if os.path.exists("config.json") or "init" in sys.argv:
		return
	dir_path_file = "/etc/neo_neocli_dir"
	if os.path.exists(dir_path_file):
		with open(dir_path_file) as f:
			dir_path = f.read().strip()
		if os.path.exists(dir_path):
			os.chdir(dir_path)


def change_uid():
	if is_root() and not cmd_requires_root():
		neo_user = neocli_config.get("neo_user")
		if neo_user:
			drop_privileges(uid_name=neo_user, gid_name=neo_user)
			os.environ["HOME"] = pwd.getpwnam(neo_user).pw_dir
		else:
			log(change_uid_msg, level=3)
			sys.exit(1)


def app_cmd(neocli_path="."):
	f = get_env_cmd("python", neocli_path=neocli_path)
	os.chdir(os.path.join(neocli_path, "sites"))
	os.execv(f, [f] + ["-m", "neo.utils.neocli_helper"] + sys.argv[1:])


def neo_cmd(neocli_path="."):
	f = get_env_cmd("python", neocli_path=neocli_path)
	os.chdir(os.path.join(neocli_path, "sites"))
	os.execv(f, [f] + ["-m", "neo.utils.neocli_helper", "neo"] + sys.argv[1:])


def get_cached_neo_commands():
	if os.path.exists(neocli_cache_file):
		command_dump = open(neocli_cache_file, "r").read() or "[]"
		return set(json.loads(command_dump))
	return set()


def get_neo_commands():
	if not is_neocli_directory():
		return set()

	return set(generate_command_cache())


def get_neo_help(neocli_path="."):
	python = get_env_cmd("python", neocli_path=neocli_path)
	sites_path = os.path.join(neocli_path, "sites")
	try:
		out = get_cmd_output(
			f"{python} -m neo.utils.neocli_helper get-neo-help", cwd=sites_path
		)
		return "\n\nFramework commands:\n" + out.split("Commands:")[1]
	except Exception:
		return ""


def change_working_directory():
	"""Allows neocli commands to be run from anywhere inside a neocli directory"""
	cur_dir = os.path.abspath(".")
	neocli_path = find_parent_neocli(cur_dir)
	neocli.current_path = os.getcwd()
	neocli.updated_path = neocli_path

	if neocli_path:
		os.chdir(neocli_path)


def setup_clear_cache():
	from copy import copy
	f = copy(os.chdir)

	def _chdir(*args, **kwargs):
		NeoCLI.cache_clear()
		return f(*args, **kwargs)

	os.chdir = _chdir
