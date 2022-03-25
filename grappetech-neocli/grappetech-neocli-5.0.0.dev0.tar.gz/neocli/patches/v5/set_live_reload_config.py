from neocli.config.common_site_config import update_config


def execute(neocli_path):
	update_config({'live_reload': True}, neocli_path)
