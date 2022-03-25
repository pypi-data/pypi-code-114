# imports - standard imports
import functools
import os
import shutil
import sys
import logging
from typing import List, MutableSequence, TYPE_CHECKING

# imports - module imports
import neocli
from neocli.exceptions import ValidationError
from neocli.config.common_site_config import setup_config
from neocli.utils import (
	paths_in_neocli,
	exec_cmd,
	is_neocli_directory,
	is_neo_app,
	get_cmd_output,
	get_git_version,
	log,
	run_neo_cmd,
)
from neocli.utils.neocli import (
	validate_app_installed_on_sites,
	restart_supervisor_processes,
	restart_systemd_processes,
	restart_process_manager,
	remove_backups_crontab,
	get_venv_path,
	get_env_cmd,
)
from neocli.utils.render import job, step


if TYPE_CHECKING:
	from neocli.app import App

logger = logging.getLogger(neocli.PROJECT_NAME)


class Base:
	def run(self, cmd, cwd=None):
		return exec_cmd(cmd, cwd=cwd or self.cwd)


class Validator:
	def validate_app_uninstall(self, app):
		if app not in self.apps:
			raise ValidationError(f"No app named {app}")
		validate_app_installed_on_sites(app, neocli_path=self.name)


@functools.lru_cache(maxsize=None)
class NeoCLI(Base, Validator):
	def __init__(self, path):
		self.name = path
		self.cwd = os.path.abspath(path)
		self.exists = is_neocli_directory(self.name)

		self.setup = NeoCLISetup(self)
		self.teardown = NeoCLITearDown(self)
		self.apps = NeoCLIApps(self)

		self.apps_txt = os.path.join(self.name, "sites", "apps.txt")
		self.excluded_apps_txt = os.path.join(self.name, "sites", "excluded_apps.txt")

	@property
	def python(self) -> str:
		return get_env_cmd("python", neocli_path=self.name)

	@property
	def shallow_clone(self) -> bool:
		config = self.conf

		if config:
			if config.get("release_neocli") or not config.get("shallow_clone"):
				return False

		return get_git_version() > 1.9

	@property
	def excluded_apps(self) -> List:
		try:
			with open(self.excluded_apps_txt) as f:
				return f.read().strip().split("\n")
		except Exception:
			return []

	@property
	def sites(self) -> List:
		return [
			path
			for path in os.listdir(os.path.join(self.name, "sites"))
			if os.path.exists(os.path.join("sites", path, "site_config.json"))
		]

	@property
	def conf(self):
		from neocli.config.common_site_config import get_config

		return get_config(self.name)

	def init(self):
		self.setup.dirs()
		self.setup.env()
		self.setup.backups()

	def drop(self):
		self.teardown.backups()
		self.teardown.dirs()

	def install(self, app, branch=None):
		from neocli.app import App

		app = App(app, branch=branch)
		self.apps.append(app)
		self.apps.sync()

	def uninstall(self, app):
		from neocli.app import App

		self.validate_app_uninstall(app)
		self.apps.remove(App(app, neocli=self, to_clone=False))
		self.apps.sync()
		# self.build() - removed because it seems unnecessary
		self.reload()

	@step(title="Building NeoCLI Assets", success="NeoCLI Assets Built")
	def build(self):
		# build assets & stuff
		run_neo_cmd("build", neocli_path=self.name)

	@step(title="Reloading NeoCLI Processes", success="NeoCLI Processes Reloaded")
	def reload(self, web=False, supervisor=True, systemd=True):
		"""If web is True, only web workers are restarted
		"""
		conf = self.conf

		if conf.get("developer_mode"):
			restart_process_manager(neocli_path=self.name, web_workers=web)
		if supervisor and conf.get("restart_supervisor_on_update"):
			restart_supervisor_processes(neocli_path=self.name, web_workers=web)
		if systemd and conf.get("restart_systemd_on_update"):
			restart_systemd_processes(neocli_path=self.name, web_workers=web)


class NeoCLIApps(MutableSequence):
	def __init__(self, neocli: NeoCLI):
		self.neocli = neocli
		self.initialize_apps()

	def sync(self):
		self.initialize_apps()
		with open(self.neocli.apps_txt, "w") as f:
			return f.write("\n".join(self.apps))

	def initialize_apps(self):
		is_installed = lambda app: app in installed_packages

		try:
			installed_packages = get_cmd_output(f"{self.neocli.python} -m pip freeze", cwd=self.neocli.name)
		except Exception:
			self.apps = []
			return

		try:
			self.apps = [
				x
				for x in os.listdir(os.path.join(self.neocli.name, "apps"))
				if (
					is_neo_app(os.path.join(self.neocli.name, "apps", x))
					and is_installed(x)
				)
			]
			self.apps.sort()
		except FileNotFoundError:
			self.apps = []

	def __getitem__(self, key):
		""" retrieves an item by its index, key"""
		return self.apps[key]

	def __setitem__(self, key, value):
		""" set the item at index, key, to value """
		# should probably not be allowed
		# self.apps[key] = value
		raise NotImplementedError

	def __delitem__(self, key):
		""" removes the item at index, key """
		# TODO: uninstall and delete app from neocli
		del self.apps[key]

	def __len__(self):
		return len(self.apps)

	def insert(self, key, value):
		""" add an item, value, at index, key. """
		# TODO: fetch and install app to neocli
		self.apps.insert(key, value)

	def add(self, app: "App"):
		app.get()
		app.install()
		super().append(app.repo)
		self.apps.sort()

	def remove(self, app: "App"):
		app.uninstall()
		app.remove()
		super().remove(app.repo)

	def append(self, app: "App"):
		return self.add(app)

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		return str([x for x in self.apps])


class NeoCLISetup(Base):
	def __init__(self, neocli: NeoCLI):
		self.neocli = neocli
		self.cwd = self.neocli.cwd

	@step(title="Setting Up Directories", success="Directories Set Up")
	def dirs(self):
		os.makedirs(self.neocli.name, exist_ok=True)

		for dirname in paths_in_neocli:
			os.makedirs(os.path.join(self.neocli.name, dirname), exist_ok=True)

	@step(title="Setting Up Environment", success="Environment Set Up")
	def env(self, python="python3"):
		"""Setup env folder
		- create env if not exists
		- upgrade env pip
		- install neo python dependencies
		"""
		import neocli.cli

		neo = os.path.join(self.neocli.name, "apps", "neo")
		virtualenv = get_venv_path()
		quiet_flag = "" if neocli.cli.verbose else "--quiet"

		if not os.path.exists(self.neocli.python):
			self.run(f"{virtualenv} {quiet_flag} env -p {python}")

		self.pip()

		if os.path.exists(neo):
			self.run(f"{self.neocli.python} -m pip install {quiet_flag} --upgrade -e {neo}")

	@step(title="Setting Up NeoCLI Config", success="NeoCLI Config Set Up")
	def config(self, redis=True, procfile=True):
		"""Setup config folder
		- create pids folder
		- generate sites/common_site_config.json
		"""
		setup_config(self.neocli.name)

		if redis:
			from neocli.config.redis import generate_config

			generate_config(self.neocli.name)

		if procfile:
			from neocli.config.procfile import setup_procfile

			setup_procfile(self.neocli.name, skip_redis=not redis)

	@step(title="Updating pip", success="Updated pip")
	def pip(self, verbose=False):
		"""Updates env pip; assumes that env is setup
		"""
		import neocli.cli

		verbose = neocli.cli.verbose or verbose
		quiet_flag = "" if verbose else "--quiet"

		return self.run(f"{self.neocli.python} -m pip install {quiet_flag} --upgrade pip")

	def logging(self):
		from neocli.utils import setup_logging

		return setup_logging(neocli_path=self.neocli.name)

	@step(title="Setting Up NeoCLI Patches", success="NeoCLI Patches Set Up")
	def patches(self):
		shutil.copy(
			os.path.join(os.path.dirname(os.path.abspath(__file__)), "patches", "patches.txt"),
			os.path.join(self.neocli.name, "patches.txt"),
		)

	@step(title="Setting Up Backups Cronjob", success="Backups Cronjob Set Up")
	def backups(self):
		# TODO: to something better for logging data? - maybe a wrapper that auto-logs with more context
		logger.log("setting up backups")

		from crontab import CronTab

		neocli_dir = os.path.abspath(self.neocli.name)
		user = self.neocli.conf.get("neo_user")
		logfile = os.path.join(neocli_dir, "logs", "backup.log")
		system_crontab = CronTab(user=user)
		backup_command = f"cd {neocli_dir} && {sys.argv[0]} --verbose --site all backup"
		job_command = f"{backup_command} >> {logfile} 2>&1"

		if job_command not in str(system_crontab):
			job = system_crontab.new(
				command=job_command, comment="neocli auto backups set for every 6 hours"
			)
			job.every(6).hours()
			system_crontab.write()

		logger.log("backups were set up")

	def __get_installed_apps(self) -> List:
		"""Returns list of installed apps on neocli, not in excluded_apps.txt
		"""
		apps = [app for app in self.neocli.apps if app not in self.neocli.excluded_apps]
		apps.remove("neo")
		apps.insert(0, "neo")
		return apps

	@job(title="Setting Up NeoCLI Dependencies", success="NeoCLI Dependencies Set Up")
	def requirements(self):
		"""Install and upgrade all installed apps on given NeoCLI
		"""
		from neocli.app import App

		apps = self.__get_installed_apps()

		self.pip()

		print(f"Installing {len(apps)} applications...")

		for app in apps:
			App(app, neocli=self.neocli, to_clone=False).install()

	def python(self):
		"""Install and upgrade Python dependencies for installed apps on given NeoCLI
		"""
		import neocli.cli

		apps = self.__get_installed_apps()

		quiet_flag = "" if neocli.cli.verbose else "--quiet"

		self.pip()

		for app in apps:
			app_path = os.path.join(self.neocli.name, "apps", app)
			log(f"\nInstalling python dependencies for {app}", level=3, no_log=True)
			self.run(f"{self.neocli.python} -m pip install {quiet_flag} --upgrade -e {app_path}")

	def node(self):
		"""Install and upgrade Node dependencies for all apps on given NeoCLI
		"""
		from neocli.utils.neocli import update_node_packages

		return update_node_packages(neocli_path=self.neocli.name)


class NeoCLITearDown:
	def __init__(self, neocli):
		self.neocli = neocli

	def backups(self):
		remove_backups_crontab(self.neocli.name)

	def dirs(self):
		shutil.rmtree(self.neocli.name)
