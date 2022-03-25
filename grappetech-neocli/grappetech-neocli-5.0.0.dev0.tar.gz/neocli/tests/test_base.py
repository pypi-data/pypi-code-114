# imports - standard imports
import getpass
import json
import os
import shutil
import subprocess
import sys
import traceback
import unittest

# imports - module imports
import neocli
from neocli.utils import paths_in_neocli, exec_cmd
from neocli.utils.system import init
from neocli.neocli import NeoCLI

PYTHON_VER = sys.version_info

neo_BRANCH = "version-12"
if PYTHON_VER.major == 3:
	if PYTHON_VER.minor in [6, 7]:
		neo_BRANCH = "version-13"
	else:
		neo_BRANCH = "develop"

class TestNeoCLIBase(unittest.TestCase):
	def setUp(self):
		self.neoclies_path = "."
		self.neoclies = []

	def tearDown(self):
		for neocli_name in self.neoclies:
			neocli_path = os.path.join(self.neoclies_path, neocli_name)
			neocli = NeoCLI(neocli_path)
			mariadb_password = "travis" if os.environ.get("CI") else getpass.getpass(prompt="Enter MariaDB root Password: ")

			if neocli.exists:
				for site in neocli.sites:
					subprocess.call(["neocli", "drop-site", site, "--force", "--no-backup", "--root-password", mariadb_password], cwd=neocli_path)
				shutil.rmtree(neocli_path, ignore_errors=True)

	def assert_folders(self, neocli_name):
		for folder in paths_in_neocli:
			self.assert_exists(neocli_name, folder)
		self.assert_exists(neocli_name, "apps", "neo")

	def assert_virtual_env(self, neocli_name):
		neocli_path = os.path.abspath(neocli_name)
		python_path = os.path.abspath(os.path.join(neocli_path, "env", "bin", "python"))
		self.assertTrue(python_path.startswith(neocli_path))
		for subdir in ("bin", "lib", "share"):
			self.assert_exists(neocli_name, "env", subdir)

	def assert_config(self, neocli_name):
		for config, search_key in (
			("redis_queue.conf", "redis_queue.rdb"),
			("redis_socketio.conf", "redis_socketio.rdb"),
			("redis_cache.conf", "redis_cache.rdb")):

			self.assert_exists(neocli_name, "config", config)

			with open(os.path.join(neocli_name, "config", config), "r") as f:
				self.assertTrue(search_key in f.read())

	def assert_common_site_config(self, neocli_name, expected_config):
		common_site_config_path = os.path.join(self.neoclies_path, neocli_name, 'sites', 'common_site_config.json')
		self.assertTrue(os.path.exists(common_site_config_path))

		with open(common_site_config_path, "r") as f:
			config = json.load(f)

		for key, value in list(expected_config.items()):
			self.assertEqual(config.get(key), value)

	def assert_exists(self, *args):
		self.assertTrue(os.path.exists(os.path.join(*args)))

	def new_site(self, site_name, neocli_name):
		new_site_cmd = ["neocli", "new-site", site_name, "--admin-password", "admin"]

		if os.environ.get('CI'):
			new_site_cmd.extend(["--mariadb-root-password", "travis"])

		subprocess.call(new_site_cmd, cwd=os.path.join(self.neoclies_path, neocli_name))

	def init_neocli(self, neocli_name, **kwargs):
		self.neoclies.append(neocli_name)
		neo_tmp_path = "/tmp/neo"

		if not os.path.exists(neo_tmp_path):
			exec_cmd(f"git clone https://github.com/grappetech/neo -b {neo_BRANCH} --depth 1 --origin upstream {neo_tmp_path}")

		kwargs.update(dict(
			python=sys.executable,
			no_procfile=True,
			no_backups=True,
			neo_path=neo_tmp_path
		))

		if not os.path.exists(os.path.join(self.neoclies_path, neocli_name)):
			init(neocli_name, **kwargs)
			exec_cmd("git remote set-url upstream https://github.com/grappetech/neo", cwd=os.path.join(self.neoclies_path, neocli_name, "apps", "neo"))

	def file_exists(self, path):
		if os.environ.get("CI"):
			return not subprocess.call(["sudo", "test", "-f", path])
		return os.path.isfile(path)

	def get_traceback(self):
		exc_type, exc_value, exc_tb = sys.exc_info()
		trace_list = traceback.format_exception(exc_type, exc_value, exc_tb)
		body = "".join(str(t) for t in trace_list)
		return body
