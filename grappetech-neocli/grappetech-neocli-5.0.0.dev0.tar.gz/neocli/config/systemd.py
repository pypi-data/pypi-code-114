# imports - standard imports
import getpass
import os

# imports - third partyimports
import click

# imports - module imports
import neocli
from neocli.app import use_rq
from neocli.neocli import NeoCLI
from neocli.config.common_site_config import get_gunicorn_workers, update_config
from neocli.utils import exec_cmd, which, get_neocli_name


def generate_systemd_config(neocli_path, user=None, yes=False,
	stop=False, create_symlinks=False,
	delete_symlinks=False):

	if not user:
		user = getpass.getuser()

	config = NeoCLI(neocli_path).conf

	neocli_dir = os.path.abspath(neocli_path)
	neocli_name = get_neocli_name(neocli_path)

	if stop:
		exec_cmd(f'sudo systemctl stop -- $(systemctl show -p Requires {neocli_name}.target | cut -d= -f2)')
		return

	if create_symlinks:
		_create_symlinks(neocli_path)
		return

	if delete_symlinks:
		_delete_symlinks(neocli_path)
		return

	number_of_workers = config.get('background_workers') or 1
	background_workers = []
	for i in range(number_of_workers):
		background_workers.append(get_neocli_name(neocli_path) + "-neo-default-worker@" + str(i+1) + ".service")

	for i in range(number_of_workers):
		background_workers.append(get_neocli_name(neocli_path) + "-neo-short-worker@" + str(i+1) + ".service")

	for i in range(number_of_workers):
		background_workers.append(get_neocli_name(neocli_path) + "-neo-long-worker@" + str(i+1) + ".service")

	neocli_info = {
		"neocli_dir": neocli_dir,
		"sites_dir": os.path.join(neocli_dir, 'sites'),
		"user": user,
		"use_rq": use_rq(neocli_path),
		"http_timeout": config.get("http_timeout", 120),
		"redis_server": which('redis-server'),
		"node": which('node') or which('nodejs'),
		"redis_cache_config": os.path.join(neocli_dir, 'config', 'redis_cache.conf'),
		"redis_socketio_config": os.path.join(neocli_dir, 'config', 'redis_socketio.conf'),
		"redis_queue_config": os.path.join(neocli_dir, 'config', 'redis_queue.conf'),
		"webserver_port": config.get('webserver_port', 8000),
		"gunicorn_workers": config.get('gunicorn_workers', get_gunicorn_workers()["gunicorn_workers"]),
		"neocli_name": get_neocli_name(neocli_path),
		"worker_target_wants": " ".join(background_workers),
		"neocli_cmd": which('neocli')
	}

	if not yes:
		click.confirm('current systemd configuration will be overwritten. Do you want to continue?',
			abort=True)

	setup_systemd_directory(neocli_path)
	setup_main_config(neocli_info, neocli_path)
	setup_workers_config(neocli_info, neocli_path)
	setup_web_config(neocli_info, neocli_path)
	setup_redis_config(neocli_info, neocli_path)

	update_config({'restart_systemd_on_update': True}, neocli_path=neocli_path)
	update_config({'restart_supervisor_on_update': False}, neocli_path=neocli_path)

def setup_systemd_directory(neocli_path):
	if not os.path.exists(os.path.join(neocli_path, 'config', 'systemd')):
		os.makedirs(os.path.join(neocli_path, 'config', 'systemd'))

def setup_main_config(neocli_info, neocli_path):
	# Main config
	neocli_template = neocli.config.env().get_template('systemd/grappetech-neocli.target')
	neocli_config = neocli_template.render(**neocli_info)
	neocli_config_path = os.path.join(neocli_path, 'config', 'systemd' , neocli_info.get("neocli_name") + '.target')

	with open(neocli_config_path, 'w') as f:
		f.write(neocli_config)

def setup_workers_config(neocli_info, neocli_path):
	# Worker Group
	neocli_workers_target_template = neocli.config.env().get_template('systemd/grappetech-neocli-workers.target')
	neocli_default_worker_template = neocli.config.env().get_template('systemd/grappetech-neocli-neo-default-worker.service')
	neocli_short_worker_template = neocli.config.env().get_template('systemd/grappetech-neocli-neo-short-worker.service')
	neocli_long_worker_template = neocli.config.env().get_template('systemd/grappetech-neocli-neo-long-worker.service')
	neocli_schedule_worker_template = neocli.config.env().get_template('systemd/grappetech-neocli-neo-schedule.service')

	neocli_workers_target_config = neocli_workers_target_template.render(**neocli_info)
	neocli_default_worker_config = neocli_default_worker_template.render(**neocli_info)
	neocli_short_worker_config = neocli_short_worker_template.render(**neocli_info)
	neocli_long_worker_config = neocli_long_worker_template.render(**neocli_info)
	neocli_schedule_worker_config = neocli_schedule_worker_template.render(**neocli_info)

	neocli_workers_target_config_path = os.path.join(neocli_path, 'config', 'systemd' , neocli_info.get("neocli_name") + '-workers.target')
	neocli_default_worker_config_path = os.path.join(neocli_path, 'config', 'systemd' , neocli_info.get("neocli_name") + '-neo-default-worker@.service')
	neocli_short_worker_config_path = os.path.join(neocli_path, 'config', 'systemd' , neocli_info.get("neocli_name") + '-neo-short-worker@.service')
	neocli_long_worker_config_path = os.path.join(neocli_path, 'config', 'systemd' , neocli_info.get("neocli_name") + '-neo-long-worker@.service')
	neocli_schedule_worker_config_path = os.path.join(neocli_path, 'config', 'systemd' , neocli_info.get("neocli_name") + '-neo-schedule.service')

	with open(neocli_workers_target_config_path, 'w') as f:
		f.write(neocli_workers_target_config)

	with open(neocli_default_worker_config_path, 'w') as f:
		f.write(neocli_default_worker_config)

	with open(neocli_short_worker_config_path, 'w') as f:
		f.write(neocli_short_worker_config)

	with open(neocli_long_worker_config_path, 'w') as f:
		f.write(neocli_long_worker_config)

	with open(neocli_schedule_worker_config_path, 'w') as f:
		f.write(neocli_schedule_worker_config)

def setup_web_config(neocli_info, neocli_path):
	# Web Group
	neocli_web_target_template = neocli.config.env().get_template('systemd/grappetech-neocli-web.target')
	neocli_web_service_template = neocli.config.env().get_template('systemd/grappetech-neocli-neo-web.service')
	neocli_node_socketio_template = neocli.config.env().get_template('systemd/grappetech-neocli-node-socketio.service')

	neocli_web_target_config = neocli_web_target_template.render(**neocli_info)
	neocli_web_service_config = neocli_web_service_template.render(**neocli_info)
	neocli_node_socketio_config = neocli_node_socketio_template.render(**neocli_info)

	neocli_web_target_config_path = os.path.join(neocli_path, 'config', 'systemd' , neocli_info.get("neocli_name") + '-web.target')
	neocli_web_service_config_path = os.path.join(neocli_path, 'config', 'systemd' , neocli_info.get("neocli_name") + '-neo-web.service')
	neocli_node_socketio_config_path = os.path.join(neocli_path, 'config', 'systemd' , neocli_info.get("neocli_name") + '-node-socketio.service')

	with open(neocli_web_target_config_path, 'w') as f:
		f.write(neocli_web_target_config)

	with open(neocli_web_service_config_path, 'w') as f:
		f.write(neocli_web_service_config)

	with open(neocli_node_socketio_config_path, 'w') as f:
		f.write(neocli_node_socketio_config)

def setup_redis_config(neocli_info, neocli_path):
	# Redis Group
	neocli_redis_target_template = neocli.config.env().get_template('systemd/grappetech-neocli-redis.target')
	neocli_redis_cache_template = neocli.config.env().get_template('systemd/grappetech-neocli-redis-cache.service')
	neocli_redis_queue_template = neocli.config.env().get_template('systemd/grappetech-neocli-redis-queue.service')
	neocli_redis_socketio_template = neocli.config.env().get_template('systemd/grappetech-neocli-redis-socketio.service')

	neocli_redis_target_config = neocli_redis_target_template.render(**neocli_info)
	neocli_redis_cache_config = neocli_redis_cache_template.render(**neocli_info)
	neocli_redis_queue_config = neocli_redis_queue_template.render(**neocli_info)
	neocli_redis_socketio_config = neocli_redis_socketio_template.render(**neocli_info)

	neocli_redis_target_config_path = os.path.join(neocli_path, 'config', 'systemd' , neocli_info.get("neocli_name") + '-redis.target')
	neocli_redis_cache_config_path = os.path.join(neocli_path, 'config', 'systemd' , neocli_info.get("neocli_name") + '-redis-cache.service')
	neocli_redis_queue_config_path = os.path.join(neocli_path, 'config', 'systemd' , neocli_info.get("neocli_name") + '-redis-queue.service')
	neocli_redis_socketio_config_path = os.path.join(neocli_path, 'config', 'systemd' , neocli_info.get("neocli_name") + '-redis-socketio.service')

	with open(neocli_redis_target_config_path, 'w') as f:
		f.write(neocli_redis_target_config)

	with open(neocli_redis_cache_config_path, 'w') as f:
		f.write(neocli_redis_cache_config)

	with open(neocli_redis_queue_config_path, 'w') as f:
		f.write(neocli_redis_queue_config)

	with open(neocli_redis_socketio_config_path, 'w') as f:
		f.write(neocli_redis_socketio_config)

def _create_symlinks(neocli_path):
	neocli_dir = os.path.abspath(neocli_path)
	etc_systemd_system = os.path.join('/', 'etc', 'systemd', 'system')
	config_path = os.path.join(neocli_dir, 'config', 'systemd')
	unit_files = get_unit_files(neocli_dir)
	for unit_file in unit_files:
		filename = "".join(unit_file)
		exec_cmd(f'sudo ln -s {config_path}/{filename} {etc_systemd_system}/{"".join(unit_file)}')
	exec_cmd('sudo systemctl daemon-reload')

def _delete_symlinks(neocli_path):
	neocli_dir = os.path.abspath(neocli_path)
	etc_systemd_system = os.path.join('/', 'etc', 'systemd', 'system')
	unit_files = get_unit_files(neocli_dir)
	for unit_file in unit_files:
		exec_cmd(f'sudo rm {etc_systemd_system}/{"".join(unit_file)}')
	exec_cmd('sudo systemctl daemon-reload')

def get_unit_files(neocli_path):
	neocli_name = get_neocli_name(neocli_path)
	unit_files = [
		[neocli_name, ".target"],
		[neocli_name+"-workers", ".target"],
		[neocli_name+"-web", ".target"],
		[neocli_name+"-redis", ".target"],
		[neocli_name+"-neo-default-worker@", ".service"],
		[neocli_name+"-neo-short-worker@", ".service"],
		[neocli_name+"-neo-long-worker@", ".service"],
		[neocli_name+"-neo-schedule", ".service"],
		[neocli_name+"-neo-web", ".service"],
		[neocli_name+"-node-socketio", ".service"],
		[neocli_name+"-redis-cache", ".service"],
		[neocli_name+"-redis-queue", ".service"],
		[neocli_name+"-redis-socketio", ".service"],
	]
	return unit_files
