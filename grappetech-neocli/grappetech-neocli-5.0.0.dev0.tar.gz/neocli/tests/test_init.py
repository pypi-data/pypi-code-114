# imports - standard imports
import json
import os
import subprocess
import unittest

# imports - third paty imports
import git

# imports - module imports
from neocli.utils import exec_cmd
from neocli.release import get_bumped_version
from neocli.tests.test_base import neo_BRANCH, TestNeoCLIBase


# changed from neo_theme because it wasn't maintained and incompatible,
# chat app & wiki was breaking too. hopefully neo_docs will be maintained
# for longer since docs.erpneo.com is powered by it ;)
TEST_neo_APP = "neo_docs"

class TestNeoCLIInit(TestNeoCLIBase):
	def test_semantic_version(self):
		self.assertEqual( get_bumped_version('11.0.4', 'major'), '12.0.0' )
		self.assertEqual( get_bumped_version('11.0.4', 'minor'), '11.1.0' )
		self.assertEqual( get_bumped_version('11.0.4', 'patch'), '11.0.5' )
		self.assertEqual( get_bumped_version('11.0.4', 'prerelease'), '11.0.5-beta.1' )

		self.assertEqual( get_bumped_version('11.0.5-beta.22', 'major'), '12.0.0' )
		self.assertEqual( get_bumped_version('11.0.5-beta.22', 'minor'), '11.1.0' )
		self.assertEqual( get_bumped_version('11.0.5-beta.22', 'patch'), '11.0.5' )
		self.assertEqual( get_bumped_version('11.0.5-beta.22', 'prerelease'), '11.0.5-beta.23' )


	def test_utils(self):
		self.assertEqual(subprocess.call("neocli"), 0)


	def test_init(self, neocli_name="test-neocli", **kwargs):
		self.init_neocli(neocli_name, **kwargs)
		self.assert_folders(neocli_name)
		self.assert_virtual_env(neocli_name)
		self.assert_config(neocli_name)


	def basic(self):
		try:
			self.test_init()
		except Exception:
			print(self.get_traceback())


	def test_multiple_neoclies(self):
		for neocli_name in ("test-neocli-1", "test-neocli-2"):
			self.init_neocli(neocli_name)

		self.assert_common_site_config("test-neocli-1", {
			"webserver_port": 8000,
			"socketio_port": 9000,
			"file_watcher_port": 6787,
			"redis_queue": "redis://localhost:11000",
			"redis_socketio": "redis://localhost:12000",
			"redis_cache": "redis://localhost:13000"
		})

		self.assert_common_site_config("test-neocli-2", {
			"webserver_port": 8001,
			"socketio_port": 9001,
			"file_watcher_port": 6788,
			"redis_queue": "redis://localhost:11001",
			"redis_socketio": "redis://localhost:12001",
			"redis_cache": "redis://localhost:13001"
		})



	def test_new_site(self):
		neocli_name = "test-neocli"
		site_name = "test-site.local"
		neocli_path = os.path.join(self.neoclies_path, neocli_name)
		site_path = os.path.join(neocli_path, "sites", site_name)
		site_config_path = os.path.join(site_path, "site_config.json")

		self.init_neocli(neocli_name)
		exec_cmd("neocli setup requirements --node", cwd=neocli_path)
		self.new_site(site_name, neocli_name)

		self.assertTrue(os.path.exists(site_path))
		self.assertTrue(os.path.exists(os.path.join(site_path, "private", "backups")))
		self.assertTrue(os.path.exists(os.path.join(site_path, "private", "files")))
		self.assertTrue(os.path.exists(os.path.join(site_path, "public", "files")))
		self.assertTrue(os.path.exists(site_config_path))

		with open(site_config_path, "r") as f:
			site_config = json.loads(f.read())

			for key in ("db_name", "db_password"):
				self.assertTrue(key in site_config)
				self.assertTrue(site_config[key])

	def test_get_app(self):
		self.init_neocli("test-neocli")
		neocli_path = os.path.join(self.neoclies_path, "test-neocli")
		exec_cmd(f"neocli get-app {TEST_neo_APP}", cwd=neocli_path)
		self.assertTrue(os.path.exists(os.path.join(neocli_path, "apps", TEST_neo_APP)))
		app_installed_in_env = TEST_neo_APP in subprocess.check_output(["neocli", "pip", "freeze"], cwd=neocli_path).decode('utf8')
		self.assertTrue(app_installed_in_env)


	def test_install_app(self):
		neocli_name = "test-neocli"
		site_name = "install-app.test"
		neocli_path = os.path.join(self.neoclies_path, "test-neocli")

		self.init_neocli(neocli_name)
		exec_cmd("neocli setup requirements --node", cwd=neocli_path)
		exec_cmd("neocli build", cwd=neocli_path)
		exec_cmd(f"neocli get-app {TEST_neo_APP} --branch master", cwd=neocli_path)

		self.assertTrue(os.path.exists(os.path.join(neocli_path, "apps", TEST_neo_APP)))

		# check if app is installed
		app_installed_in_env = TEST_neo_APP in subprocess.check_output(["neocli", "pip", "freeze"], cwd=neocli_path).decode('utf8')
		self.assertTrue(app_installed_in_env)

		# create and install app on site
		self.new_site(site_name, neocli_name)
		installed_app = not exec_cmd(f"neocli --site {site_name} install-app {TEST_neo_APP}", cwd=neocli_path)

		app_installed_on_site = subprocess.check_output(["neocli", "--site", site_name, "list-apps"], cwd=neocli_path).decode('utf8')

		if installed_app:
			self.assertTrue(TEST_neo_APP in app_installed_on_site)


	def test_remove_app(self):
		self.init_neocli("test-neocli")
		neocli_path = os.path.join(self.neoclies_path, "test-neocli")

		exec_cmd("neocli setup requirements --node", cwd=neocli_path)
		exec_cmd(f"neocli get-app {TEST_neo_APP} --branch master --overwrite", cwd=neocli_path)
		exec_cmd(f"neocli remove-app {TEST_neo_APP}", cwd=neocli_path)

		with open(os.path.join(neocli_path, "sites", "apps.txt")) as f:
			self.assertFalse(TEST_neo_APP in f.read())
		self.assertFalse(TEST_neo_APP in subprocess.check_output(["neocli", "pip", "freeze"], cwd=neocli_path).decode('utf8'))
		self.assertFalse(os.path.exists(os.path.join(neocli_path, "apps", TEST_neo_APP)))


	def test_switch_to_branch(self):
		self.init_neocli("test-neocli")
		neocli_path = os.path.join(self.neoclies_path, "test-neocli")
		app_path = os.path.join(neocli_path, "apps", "neo")

		# * chore: change to 14 when avalible
		prevoius_branch = "version-13"
		if neo_BRANCH != "develop":
			# assuming we follow `version-#`
			prevoius_branch = f"version-{int(neo_BRANCH.split('-')[1]) - 1}"

		successful_switch = not exec_cmd(f"neocli switch-to-branch {prevoius_branch} neo --upgrade", cwd=neocli_path)
		app_branch_after_switch = str(git.Repo(path=app_path).active_branch)
		if successful_switch:
			self.assertEqual(prevoius_branch, app_branch_after_switch)

		successful_switch = not exec_cmd(f"neocli switch-to-branch {neo_BRANCH} neo --upgrade", cwd=neocli_path)
		app_branch_after_second_switch = str(git.Repo(path=app_path).active_branch)
		if successful_switch:
			self.assertEqual(neo_BRANCH, app_branch_after_second_switch)


if __name__ == '__main__':
	unittest.main()
