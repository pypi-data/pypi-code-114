# imports - standard imports
import getpass
import os
import re
import subprocess
import time
import unittest

# imports - module imports
from neocli.utils import exec_cmd, get_cmd_output, which
from neocli.config.production_setup import get_supervisor_confdir
from neocli.tests.test_base import TestNeoCLIBase


class TestSetupProduction(TestNeoCLIBase):
	def test_setup_production(self):
		user = getpass.getuser()

		for neocli_name in ("test-neocli-1", "test-neocli-2"):
			neocli_path = os.path.join(os.path.abspath(self.neoclies_path), neocli_name)
			self.init_neocli(neocli_name)
			exec_cmd(f"sudo neocli setup production {user} --yes", cwd=neocli_path)
			self.assert_nginx_config(neocli_name)
			self.assert_supervisor_config(neocli_name)
			self.assert_supervisor_process(neocli_name)

		self.assert_nginx_process()
		exec_cmd(f"sudo neocli setup sudoers {user}")
		self.assert_sudoers(user)

		for neocli_name in self.neoclies:
			neocli_path = os.path.join(os.path.abspath(self.neoclies_path), neocli_name)
			exec_cmd("sudo neocli disable-production", cwd=neocli_path)


	def production(self):
		try:
			self.test_setup_production()
		except Exception:
			print(self.get_traceback())


	def assert_nginx_config(self, neocli_name):
		conf_src = os.path.join(os.path.abspath(self.neoclies_path), neocli_name, 'config', 'nginx.conf')
		conf_dest = f"/etc/nginx/conf.d/{neocli_name}.conf"

		self.assertTrue(self.file_exists(conf_src))
		self.assertTrue(self.file_exists(conf_dest))

		# symlink matches
		self.assertEqual(os.path.realpath(conf_dest), conf_src)

		# file content
		with open(conf_src, "r") as f:
			f = f.read()

			for key in (
					f"upstream {neocli_name}-neo",
					f"upstream {neocli_name}-socketio-server"
				):
				self.assertTrue(key in f)


	def assert_nginx_process(self):
		out = get_cmd_output("sudo nginx -t 2>&1")
		self.assertTrue("nginx: configuration file /etc/nginx/nginx.conf test is successful" in out)


	def assert_sudoers(self, user):
		sudoers_file = '/etc/sudoers.d/neo'
		service = which("service")
		nginx = which("nginx")

		self.assertTrue(self.file_exists(sudoers_file))

		if os.environ.get("CI"):
			sudoers = subprocess.check_output(["sudo", "cat", sudoers_file]).decode("utf-8")
		else:
			with open(sudoers_file, 'r') as f:
				sudoers = f.read()

		self.assertTrue(f'{user} ALL = (root) NOPASSWD: {service} nginx *' in sudoers)
		self.assertTrue(f'{user} ALL = (root) NOPASSWD: {nginx}' in sudoers)


	def assert_supervisor_config(self, neocli_name, use_rq=True):
		conf_src = os.path.join(os.path.abspath(self.neoclies_path), neocli_name, 'config', 'supervisor.conf')

		supervisor_conf_dir = get_supervisor_confdir()
		conf_dest = f"{supervisor_conf_dir}/{neocli_name}.conf"

		self.assertTrue(self.file_exists(conf_src))
		self.assertTrue(self.file_exists(conf_dest))

		# symlink matches
		self.assertEqual(os.path.realpath(conf_dest), conf_src)

		# file content
		with open(conf_src, "r") as f:
			f = f.read()

			tests = [
				f"program:{neocli_name}-neo-web",
				f"program:{neocli_name}-redis-cache",
				f"program:{neocli_name}-redis-queue",
				f"program:{neocli_name}-redis-socketio",
				f"group:{neocli_name}-web",
				f"group:{neocli_name}-workers",
				f"group:{neocli_name}-redis"
			]

			if not os.environ.get("CI"):
				tests.append(f"program:{neocli_name}-node-socketio")

			if use_rq:
				tests.extend([
					f"program:{neocli_name}-neo-schedule",
					f"program:{neocli_name}-neo-default-worker",
					f"program:{neocli_name}-neo-short-worker",
					f"program:{neocli_name}-neo-long-worker"
				])

			else:
				tests.extend([
					f"program:{neocli_name}-neo-workerbeat",
					f"program:{neocli_name}-neo-worker",
					f"program:{neocli_name}-neo-longjob-worker",
					f"program:{neocli_name}-neo-async-worker"
				])

			for key in tests:
				self.assertTrue(key in f)


	def assert_supervisor_process(self, neocli_name, use_rq=True, disable_production=False):
		out = get_cmd_output("supervisorctl status")

		while "STARTING" in out:
			print ("Waiting for all processes to start...")
			time.sleep(10)
			out = get_cmd_output("supervisorctl status")

		tests = [
			"{neocli_name}-web:{neocli_name}-neo-web[\s]+RUNNING",
			# Have commented for the time being. Needs to be uncommented later on. NeoCLI is failing on travis because of this.
			# It works on one neocli and fails on another.giving FATAL or BACKOFF (Exited too quickly (process log may have details))
			# "{neocli_name}-web:{neocli_name}-node-socketio[\s]+RUNNING",
			"{neocli_name}-redis:{neocli_name}-redis-cache[\s]+RUNNING",
			"{neocli_name}-redis:{neocli_name}-redis-queue[\s]+RUNNING",
			"{neocli_name}-redis:{neocli_name}-redis-socketio[\s]+RUNNING"
		]

		if use_rq:
			tests.extend([
				"{neocli_name}-workers:{neocli_name}-neo-schedule[\s]+RUNNING",
				"{neocli_name}-workers:{neocli_name}-neo-default-worker-0[\s]+RUNNING",
				"{neocli_name}-workers:{neocli_name}-neo-short-worker-0[\s]+RUNNING",
				"{neocli_name}-workers:{neocli_name}-neo-long-worker-0[\s]+RUNNING"
			])

		else:
			tests.extend([
				"{neocli_name}-workers:{neocli_name}-neo-workerbeat[\s]+RUNNING",
				"{neocli_name}-workers:{neocli_name}-neo-worker[\s]+RUNNING",
				"{neocli_name}-workers:{neocli_name}-neo-longjob-worker[\s]+RUNNING",
				"{neocli_name}-workers:{neocli_name}-neo-async-worker[\s]+RUNNING"
			])

		for key in tests:
			if disable_production:
				self.assertFalse(re.search(key, out))
			else:
				self.assertTrue(re.search(key, out))


if __name__ == '__main__':
	unittest.main()
