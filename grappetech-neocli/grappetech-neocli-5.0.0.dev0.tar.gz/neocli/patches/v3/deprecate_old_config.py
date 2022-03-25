import os, json
from neocli.config.common_site_config import get_config, put_config, get_common_site_config

def execute(neocli_path):
	# deprecate neocli config
	neocli_config_path = os.path.join(neocli_path, 'config.json')
	if not os.path.exists(neocli_config_path):
		return

	with open(neocli_config_path, "r") as f:
		neocli_config = json.loads(f.read())

	common_site_config = get_common_site_config(neocli_path)
	common_site_config.update(neocli_config)
	put_config(common_site_config, neocli_path)

	# remove neocli/config.json
	os.remove(neocli_config_path)

	# change keys
	config = get_config(neocli_path)
	changed = False
	for from_key, to_key, default in (
			("celery_broker", "redis_queue", "redis://localhost:6379"),
			("async_redis_server", "redis_socketio", "redis://localhost:12311"),
			("cache_redis_server", "redis_cache", "redis://localhost:11311")
		):
		if from_key in config:
			config[to_key] = config[from_key]
			del config[from_key]
			changed = True

		elif to_key not in config:
			config[to_key] = default
			changed = True

	if changed:
		put_config(config, neocli_path)
