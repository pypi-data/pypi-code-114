VERSION = "5.0.0-dev"
PROJECT_NAME = "grappetech-neocli"
neo_VERSION = None
current_path = None
updated_path = None
LOG_BUFFER = []


def set_neo_version(neocli_path="."):
	from .utils.app import get_current_neo_version

	global neo_VERSION
	if not neo_VERSION:
		neo_VERSION = get_current_neo_version(neocli_path=neocli_path)
