# imports - standard imports
import grp
import os
import pwd
import shutil
import sys

# imports - module imports
import neocli
from neocli.utils import (
	exec_cmd,
	get_process_manager,
	log,
	run_neo_cmd,
	sudoers_file,
	which,
)
from neocli.utils.neocli import build_assets, clone_apps_from
from neocli.utils.render import job


@job(title="Initializing NeoCLI {path}", success="NeoCLI {path} initialized")
def init(
	path,
	apps_path=None,
	no_procfile=False,
	no_backups=False,
	neo_path=None,
	neo_branch=None,
	verbose=False,
	clone_from=None,
	skip_redis_config_generation=False,
	clone_without_update=False,
	skip_assets=False,
	python="python3",
	install_app=None,
):
	"""Initialize a new neocli directory

	* create a neocli directory in the given path
	* setup logging for the neocli
	* setup env for the neocli
	* setup config (dir/pids/redis/procfile) for the neocli
	* setup patches.txt for neocli
	* clone & install neo
		* install python & node dependencies
		* build assets
	* setup backups crontab
	"""

	# Use print("\033c", end="") to clear entire screen after each step and re-render each list
	# another way => https://stackoverflow.com/a/44591228/10309266

	import neocli.cli
	from neocli.app import get_app, install_apps_from_path
	from neocli.neocli import NeoCLI

	verbose = neocli.cli.verbose or verbose

	neocli = NeoCLI(path)

	neocli.setup.dirs()
	neocli.setup.logging()
	neocli.setup.env(python=python)
	neocli.setup.config(redis=not skip_redis_config_generation, procfile=not no_procfile)
	neocli.setup.patches()

	# local apps
	if clone_from:
		clone_apps_from(
			neocli_path=path, clone_from=clone_from, update_app=not clone_without_update
		)

	# remote apps
	else:
		neo_path = neo_path or "https://github.com/grappetech/neo.git"

		get_app(
			neo_path, branch=neo_branch, neocli_path=path, skip_assets=True, verbose=verbose
		)

		# fetch remote apps using config file - deprecate this!
		if apps_path:
			install_apps_from_path(apps_path, neocli_path=path)

	# getting app on neocli init using --install-app
	if install_app:
		get_app(
			install_app, branch=neo_branch, neocli_path=path, skip_assets=True, verbose=verbose
		)

	if not skip_assets:
		build_assets(neocli_path=path)

	if not no_backups:
		neocli.setup.backups()


def setup_sudoers(user):
	if not os.path.exists("/etc/sudoers.d"):
		os.makedirs("/etc/sudoers.d")

		set_permissions = False
		if not os.path.exists("/etc/sudoers"):
			set_permissions = True

		with open("/etc/sudoers", "a") as f:
			f.write("\n#includedir /etc/sudoers.d\n")

		if set_permissions:
			os.chmod("/etc/sudoers", 0o440)

	template = neocli.config.env().get_template("neo_sudoers")
	neo_sudoers = template.render(
		**{
			"user": user,
			"service": which("service"),
			"systemctl": which("systemctl"),
			"nginx": which("nginx"),
		}
	)

	with open(sudoers_file, "w") as f:
		f.write(neo_sudoers)

	os.chmod(sudoers_file, 0o440)
	log(f"Sudoers was set up for user {user}", level=1)


def start(no_dev=False, concurrency=None, procfile=None, no_prefix=False, procman=None):
	if procman:
		program = which(procman)
	else:
		program = get_process_manager()

	if not program:
		raise Exception("No process manager found")

	os.environ["PYTHONUNBUFFERED"] = "true"
	if not no_dev:
		os.environ["DEV_SERVER"] = "true"

	command = [program, "start"]
	if concurrency:
		command.extend(["-c", concurrency])

	if procfile:
		command.extend(["-f", procfile])

	if no_prefix:
		command.extend(["--no-prefix"])

	os.execv(program, command)


def migrate_site(site, neocli_path="."):
	run_neo_cmd("--site", site, "migrate", neocli_path=neocli_path)


def backup_site(site, neocli_path="."):
	run_neo_cmd("--site", site, "backup", neocli_path=neocli_path)


def backup_all_sites(neocli_path="."):
	from neocli.neocli import NeoCLI

	for site in NeoCLI(neocli_path).sites:
		backup_site(site, neocli_path=neocli_path)


def fix_prod_setup_perms(neocli_path=".", neo_user=None):
	from glob import glob
	from neocli.neocli import NeoCLI

	neo_user = neo_user or NeoCLI(neocli_path).conf.get("neo_user")

	if not neo_user:
		print("neo user not set")
		sys.exit(1)

	globs = ["logs/*", "config/*"]
	for glob_name in globs:
		for path in glob(glob_name):
			uid = pwd.getpwnam(neo_user).pw_uid
			gid = grp.getgrnam(neo_user).gr_gid
			os.chown(path, uid, gid)


def setup_fonts():
	fonts_path = os.path.join("/tmp", "fonts")

	if os.path.exists("/etc/fonts_backup"):
		return

	exec_cmd("git clone https://github.com/grappetech/fonts.git", cwd="/tmp")
	os.rename("/etc/fonts", "/etc/fonts_backup")
	os.rename("/usr/share/fonts", "/usr/share/fonts_backup")
	os.rename(os.path.join(fonts_path, "etc_fonts"), "/etc/fonts")
	os.rename(os.path.join(fonts_path, "usr_share_fonts"), "/usr/share/fonts")
	shutil.rmtree(fonts_path)
	exec_cmd("fc-cache -fv")
